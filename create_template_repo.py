#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


DEFAULT_SOURCE_DIR = "project_template"
DEFAULT_PROJECT_NAME = "my_new_project"

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

    copy_template(source, target, overwrite=args.overwrite)

    print(f"Created project template copy at: {target}")
    print(f"Copied from: {source}")
    print("Next: open the new project folder and start from CLAUDE.md and PROMPT_START.md.")


if __name__ == "__main__":
    main()