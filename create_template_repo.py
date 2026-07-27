#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


DEFAULT_SOURCE_DIR = "project_template"
DEFAULT_PROJECT_NAME = "my_new_project"
DEFAULT_AGENT_PROFILE = "generic"
AGENT_SHIMS_DIRNAME = ".agent_shims"

# Kit-root directory holding composable per-type overlays (web, mobile, ...).
PROFILES_DIRNAME = "profiles"
SUPPORTED_TYPE_PROFILES = {"web", "mobile", "unity", "python"}

# Agent profiles that also get a promoted `.claude/` config seed. The seed lives
# in the template at `.agent_shims/<seed_dir>/` and is copied to `.claude/`.
AGENT_CONFIG_SEED_DIR = "claude_home"
CLAUDE_CONFIG_TARGET = ".claude"
AGENT_PROFILES_WITH_CLAUDE_CONFIG = {"claude", "multi-agent"}

EXCLUDED_DIRECTORIES = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "dist",
    "build",
    "coverage",
    ".next",
}

EXCLUDED_FILENAMES = {
    ".DS_Store",
    "project_snapshot.txt",
}

SUPPORTED_AGENT_PROFILES = {"generic", "claude", "gemini", "multi-agent"}

AGENT_PROFILE_TO_SHIM = {
    "claude": "CLAUDE.md",
    "gemini": "GEMINI.md",
}

# The lean core kept when --minimal is used. Everything else in the template
# payload is pruned so small projects start with less to read and delete.
# Promoted agent shims (CLAUDE.md, GEMINI.md, ...) are always kept as well.
MINIMAL_KEEP_PATHS = {
    ".gitignore",
    "README.md",
    "AGENTS.md",
    "PROMPT_START.md",
    "docs/roadmap/current_feature.md",
    "docs/roadmap/next_phase.md",
    "docs/fixes/fixes_log.md",
    # The repo-snapshot tool is handy even for small projects.
    "scripts/export_project.py",
}

# Any path under these prefixes survives --minimal (promoted agent config, etc.).
MINIMAL_KEEP_PREFIXES = (
    f"{CLAUDE_CONFIG_TARGET}/",
)


def ignore_filter(_directory: str, names: list[str]) -> set[str]:
    ignored: set[str] = set()

    for name in names:
        if name in EXCLUDED_DIRECTORIES or name in EXCLUDED_FILENAMES:
            ignored.add(name)

    return ignored


def resolve_target(script_dir: Path, target: str | None, name: str | None) -> Path:
    if target:
        return Path(target).expanduser().resolve()

    project_name = name or DEFAULT_PROJECT_NAME
    return (script_dir.parent / project_name).resolve()


def copy_template(source: Path, target: Path, overwrite: bool) -> None:
    if not source.exists() or not source.is_dir():
        raise SystemExit(f"Source template directory not found: {source}")

    if target.exists():
        if not overwrite:
            raise SystemExit(
                f"Target already exists: {target}\n"
                "Use --overwrite to replace it."
            )
        shutil.rmtree(target)

    shutil.copytree(source, target, ignore=ignore_filter)


def copy_shim(shims_dir: Path, target: Path, shim_filename: str) -> None:
    source_file = shims_dir / shim_filename
    target_file = target / shim_filename

    if not source_file.exists():
        available = ", ".join(sorted(p.name for p in shims_dir.glob("*.md")))
        raise SystemExit(
            f"Requested agent shim not found: {source_file}\n"
            f"Available shim files: {available if available else '(none)'}"
        )

    shutil.copy2(source_file, target_file)


def cleanup_shims_dir(target: Path) -> None:
    shims_dir = target / AGENT_SHIMS_DIRNAME
    if shims_dir.exists() and shims_dir.is_dir():
        shutil.rmtree(shims_dir)


def promote_claude_config(shims_dir: Path, target: Path) -> list[str]:
    """
    Copy the `.claude/` config seed (settings.json) from
    `.agent_shims/<AGENT_CONFIG_SEED_DIR>/` into the project root's `.claude/`.

    Returns the promoted project-relative paths.
    """
    seed_dir = shims_dir / AGENT_CONFIG_SEED_DIR
    if not seed_dir.exists() or not seed_dir.is_dir():
        return []

    config_target = target / CLAUDE_CONFIG_TARGET
    promoted: list[str] = []

    for src in sorted(seed_dir.rglob("*")):
        if src.is_dir():
            continue
        relative = src.relative_to(seed_dir)
        dest = config_target / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        promoted.append((Path(CLAUDE_CONFIG_TARGET) / relative).as_posix())

    return sorted(promoted)


def configure_agent_profile(target: Path, agent: str) -> list[str]:
    """
    Configure which agent entrypoint files are added to the generated project root.

    Expected model:
    - AGENTS.md is the canonical generic instruction file
    - tool-specific entrypoints live in .agent_shims/ inside the template
    - selected shims are copied to the project root
    - the .agent_shims/ directory is removed afterwards

    Returns the list of promoted shim filenames.
    """
    canonical_file = target / "AGENTS.md"
    shims_dir = target / AGENT_SHIMS_DIRNAME
    promoted_shims: list[str] = []

    if not canonical_file.exists():
        print(
            "Warning: AGENTS.md was not found in the generated project. "
            "Consider adding it as the canonical cross-agent instruction file."
        )

    if agent == "generic":
        cleanup_shims_dir(target)
        return promoted_shims

    if not shims_dir.exists() or not shims_dir.is_dir():
        if agent == "multi-agent":
            return promoted_shims
        raise SystemExit(
            f"Agent profile '{agent}' requires shim files, but no shim directory was found: {shims_dir}"
        )

    if agent == "multi-agent":
        for shim_file in sorted(shims_dir.glob("*.md"), key=lambda p: p.name.lower()):
            shutil.copy2(shim_file, target / shim_file.name)
            promoted_shims.append(shim_file.name)

        if agent in AGENT_PROFILES_WITH_CLAUDE_CONFIG:
            promoted_shims.extend(promote_claude_config(shims_dir, target))

        cleanup_shims_dir(target)
        return promoted_shims

    shim_filename = AGENT_PROFILE_TO_SHIM.get(agent)
    if not shim_filename:
        raise SystemExit(f"No shim mapping is defined for agent profile: {agent}")

    copy_shim(shims_dir, target, shim_filename)
    promoted_shims.append(shim_filename)

    if agent in AGENT_PROFILES_WITH_CLAUDE_CONFIG:
        promoted_shims.extend(promote_claude_config(shims_dir, target))

    cleanup_shims_dir(target)
    return promoted_shims


def apply_minimal_profile(target: Path, keep_extra: list[str]) -> list[str]:
    """
    Prune the generated project down to a lean core for small projects.

    Deletes the over-provisioned scaffolding (design, product, workflow,
    archive, and scripts) and keeps only the files most projects need on
    day one, plus any promoted agent shims. Empty directories left behind
    are removed. Returns the sorted list of removed project-relative paths.
    """
    keep = MINIMAL_KEEP_PATHS | set(keep_extra)
    removed: list[str] = []

    # Sort deepest-first so files are unlinked before we check their parent
    # directories for emptiness.
    for path in sorted(target.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if path.is_dir():
            if not any(path.iterdir()):
                path.rmdir()
            continue

        relative_path = path.relative_to(target).as_posix()
        if relative_path in keep:
            continue
        if relative_path.startswith(MINIMAL_KEEP_PREFIXES):
            continue

        path.unlink()
        removed.append(relative_path)

    return sorted(removed)


def parse_type_profiles(raw: str | None) -> list[str]:
    """
    Parse the comma-separated --type value into an ordered, de-duplicated list
    of known type profiles. Types are composable (e.g. "python,web").
    """
    if not raw:
        return []

    types: list[str] = []
    for token in raw.split(","):
        name = token.strip().lower()
        if not name:
            continue
        if name not in SUPPORTED_TYPE_PROFILES:
            supported = ", ".join(sorted(SUPPORTED_TYPE_PROFILES))
            raise SystemExit(
                f"Unknown project type: '{name}'. Supported types: {supported}."
            )
        if name not in types:
            types.append(name)

    return types


def overlay_profile_files(files_dir: Path, target: Path) -> list[str]:
    """Copy a profile's `files/` tree into the project."""
    applied: list[str] = []

    for src in sorted(files_dir.rglob("*")):
        if src.is_dir():
            continue
        relative = src.relative_to(files_dir)
        dest = target / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        applied.append(relative.as_posix())

    return applied


def apply_type_profiles(target: Path, kit_root: Path, types: list[str]) -> list[str]:
    """
    Apply each composable type overlay to the generated project:
    - append the type's `.gitignore` fragment,
    - copy its `files/` tree.

    Returns the sorted list of project-relative paths that were written or
    appended to.
    """
    profiles_root = kit_root / PROFILES_DIRNAME
    touched: set[str] = set()

    for type_name in types:
        profile_dir = profiles_root / type_name
        if not profile_dir.is_dir():
            raise SystemExit(
                f"Type profile directory not found: {profile_dir}"
            )

        gitignore_fragment = profile_dir / "gitignore.append"
        if gitignore_fragment.is_file():
            fragment = gitignore_fragment.read_text(encoding="utf-8").rstrip("\n")
            gitignore_path = target / ".gitignore"
            with gitignore_path.open("a", encoding="utf-8") as handle:
                handle.write(f"\n{fragment}\n")
            touched.add(".gitignore")

        files_dir = profile_dir / "files"
        if files_dir.is_dir():
            touched.update(overlay_profile_files(files_dir, target))

    return sorted(touched)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a fresh project by copying the maintained template repo."
    )
    parser.add_argument(
        "target",
        nargs="?",
        help=(
            "Target directory for the new project copy. "
            "If omitted, a sibling folder will be created from --name."
        ),
    )
    parser.add_argument(
        "--name",
        help=(
            f"Project folder name to create next to this repo "
            f"when target is omitted. Defaults to {DEFAULT_PROJECT_NAME}."
        ),
    )
    parser.add_argument(
        "--source",
        default=DEFAULT_SOURCE_DIR,
        help=f"Template source directory. Defaults to {DEFAULT_SOURCE_DIR}.",
    )
    parser.add_argument(
        "--agent",
        default=DEFAULT_AGENT_PROFILE,
        choices=sorted(SUPPORTED_AGENT_PROFILES),
        help=(
            "Agent profile to configure in the generated project. "
            "Use 'generic' for AGENTS.md only, "
            "'claude' to add CLAUDE.md, "
            "'gemini' to add GEMINI.md, "
            "or 'multi-agent' to add all available shims. "
            f"Defaults to {DEFAULT_AGENT_PROFILE}."
        ),
    )
    parser.add_argument(
        "--type",
        dest="types",
        default=None,
        help=(
            "Composable project type overlay(s), comma-separated. "
            f"Supported: {', '.join(sorted(SUPPORTED_TYPE_PROFILES))}. "
            "Each overlay adds a .gitignore fragment and a fill-in stack-notes "
            "stub; unity also adds a workflow handoff doc. Overlays ship no live "
            "config with a baked-in tool/port. Types compose, e.g. --type python,web."
        ),
    )
    parser.add_argument(
        "--minimal",
        action="store_true",
        help=(
            "Prune the generated project to a lean core for small projects: "
            "AGENTS.md, README.md, PROMPT_START.md, current_feature.md, "
            "next_phase.md, fixes_log.md, and any agent shim. Deletes the "
            "design, product, workflow, archive, and scripts scaffolding. "
            "Combine with --agent as usual."
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace the target directory if it already exists.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    script_dir = Path(__file__).resolve().parent
    source = (script_dir / args.source).resolve()
    target = resolve_target(script_dir, args.target, args.name)
    types = parse_type_profiles(args.types)

    copy_template(source, target, overwrite=args.overwrite)
    promoted_shims = configure_agent_profile(target, args.agent)

    removed_paths: list[str] = []
    if args.minimal:
        removed_paths = apply_minimal_profile(target, promoted_shims)

    # Type overlays run last so their seeded files survive --minimal pruning.
    type_paths: list[str] = []
    if types:
        type_paths = apply_type_profiles(target, script_dir, types)

    print(f"Created project template copy at: {target}")
    print(f"Copied from: {source}")
    print(f"Agent profile: {args.agent}")
    print(f"Project type(s): {', '.join(types) if types else 'none'}")
    print(f"Minimal: {'yes' if args.minimal else 'no'}")

    if promoted_shims:
        print(f"Promoted agent shim/config files: {', '.join(promoted_shims)}")
    else:
        print("Promoted agent shim/config files: none")

    if args.minimal:
        print(f"Pruned {len(removed_paths)} scaffolding file(s) for minimal profile:")
        for removed in removed_paths:
            print(f"  - {removed}")

    if types:
        print(f"Applied {len(type_paths)} type-overlay path(s):")
        for applied in type_paths:
            print(f"  - {applied}")

    if args.agent == "generic":
        print("Next: open the new project folder and start from AGENTS.md and PROMPT_START.md.")
    elif args.agent == "multi-agent":
        print(
            "Next: open the new project folder and start from AGENTS.md, "
            "then use the tool-specific shim relevant to your coding agent, "
            "then PROMPT_START.md."
        )
    else:
        shim_name = AGENT_PROFILE_TO_SHIM.get(args.agent, "the selected agent shim")
        print(
            f"Next: open the new project folder and start from {shim_name} "
            f"(or AGENTS.md) and PROMPT_START.md."
        )


if __name__ == "__main__":
    main()