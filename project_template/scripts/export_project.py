"""Export a safe, single-file text snapshot of this project.

Walks the repository, prints a folder tree, then concatenates the text of
source and config files into one file (default ``project_snapshot.txt``) that
is easy to paste into an LLM. Secrets, dependencies, binaries, and generated
artifacts are excluded. Cross-platform (pure standard library).

    python scripts/export_project.py                # snapshot the current dir
    python scripts/export_project.py path/to/proj   # snapshot another dir
    python scripts/export_project.py --structure-only
    python scripts/export_project.py --output snapshot.txt
"""

from pathlib import Path
import argparse
import os

# Folders that should not be scanned
EXCLUDED_DIRECTORIES = {
    ".git",
    ".idea",
    ".vscode",
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

# Files that may contain credentials or should not be shared
EXCLUDED_FILENAMES = {
    ".env",
    ".env.local",
    ".env.production",
    ".env.development",
    "credentials.json",
    "secrets.json",
    "service-account.json",
    "project_snapshot.txt",
}

# Binary, database, generated, or otherwise unsuitable file types
EXCLUDED_EXTENSIONS = {
    ".db",
    ".sqlite",
    ".sqlite3",
    ".pyc",
    ".pyo",
    ".pyd",
    ".dll",
    ".so",
    ".dylib",
    ".exe",
    ".bin",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".rar",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".mp3",
    ".mp4",
    ".mov",
    ".avi",
    ".woff",
    ".woff2",
    ".ttf",
}

# Source and configuration files whose contents are useful for analysis
INCLUDED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
    ".ini",
    ".cfg",
    ".conf",
    ".md",
    ".txt",
    ".html",
    ".css",
    ".scss",
    ".sql",
    ".sh",
    ".ps1",
    ".dockerfile",
}

INCLUDED_FILENAMES = {
    "Dockerfile",
    "Makefile",
    "Procfile",
    "requirements.txt",
    "package.json",
    "package-lock.json",
    "pyproject.toml",
    "Pipfile",
    "environment.yml",
    "docker-compose.yml",
    "docker-compose.yaml",
    ".gitignore",
}

MAX_FILE_SIZE = 300_000  # 300 KB per file


def is_excluded(path: Path) -> bool:
    """Return True when a file or directory should be excluded."""
    if any(part in EXCLUDED_DIRECTORIES for part in path.parts):
        return True

    if path.name in EXCLUDED_FILENAMES:
        return True

    if path.suffix.lower() in EXCLUDED_EXTENSIONS:
        return True

    return False


def should_include_content(path: Path) -> bool:
    """Decide whether the file's text content should be included."""
    return (
        path.name in INCLUDED_FILENAMES
        or path.suffix.lower() in INCLUDED_EXTENSIONS
    )



def get_project_files(root: Path) -> list[Path]:
    files = []


    for current_root, directories, filenames in os.walk(root):
        current_path = Path(current_root)

        # Prevent os.walk from entering excluded directories
        directories[:] = sorted(
            directory
            for directory in directories
            if directory not in EXCLUDED_DIRECTORIES
        )

        for filename in sorted(filenames):
            file_path = current_path / filename
            relative_path = file_path.relative_to(root)

            if not is_excluded(relative_path):
                files.append(relative_path)

    return sorted(files, key=lambda path: str(path).lower())


def build_tree(files: list[Path]) -> str:
    """Create a readable folder tree from the collected file paths."""
    tree = {}

    for file_path in files:
        current = tree

        for part in file_path.parts:
            current = current.setdefault(part, {})

    lines = []

    def add_nodes(node: dict, prefix: str = ""):
        entries = sorted(node.items(), key=lambda item: item[0].lower())

        for index, (name, children) in enumerate(entries):
            is_last = index == len(entries) - 1
            connector = "└── " if is_last else "├── "
            lines.append(prefix + connector + name)

            if children:
                extension = "    " if is_last else "│   "
                add_nodes(children, prefix + extension)

    add_nodes(tree)
    return "\n".join(lines)


def read_text_file(path: Path) -> tuple[str | None, str | None]:
    """Read a text file safely."""
    try:
        size = path.stat().st_size
    except OSError as error:
        return None, f"Could not inspect file: {error}"

    if size > MAX_FILE_SIZE:
        return None, f"Skipped because file is larger than {MAX_FILE_SIZE:,} bytes."

    try:
        content = path.read_text(encoding="utf-8")
        return content, None
    except UnicodeDecodeError:
        try:
            content = path.read_text(encoding="latin-1")
            return content, None
        except Exception as error:
            return None, f"Could not decode file: {error}"
    except Exception as error:
        return None, f"Could not read file: {error}"


def export_project(root: Path, output_path: Path, structure_only: bool) -> None:
    files = get_project_files(root)

    with output_path.open("w", encoding="utf-8") as output:
        output.write("PROJECT SNAPSHOT\n")
        output.write("=" * 80 + "\n\n")
        output.write(f"Project folder: {root.name}\n")
        output.write(f"Number of included files: {len(files)}\n\n")

        output.write("PROJECT STRUCTURE\n")
        output.write("=" * 80 + "\n")
        output.write(f"{root.name}/\n")

        tree = build_tree(files)
        output.write(tree if tree else "(No files found)")
        output.write("\n\n")

        if structure_only:
            return

        output.write("FILE CONTENTS\n")
        output.write("=" * 80 + "\n\n")

        for relative_path in files:
            if not should_include_content(relative_path):
                continue

            full_path = root / relative_path
            content, error = read_text_file(full_path)

            output.write("\n")
            output.write("#" * 80 + "\n")
            output.write(f"FILE: {relative_path.as_posix()}\n")
            output.write("#" * 80 + "\n\n")

            if error:
                output.write(f"[{error}]\n")
            else:
                output.write(content or "[Empty file]")
                if content and not content.endswith("\n"):
                    output.write("\n")

    print(f"Snapshot created: {output_path}")
    print(f"Included {len(files)} files in the project structure.")
    print("Database files, secrets, dependencies, and binary files were excluded.")


def main():
    parser = argparse.ArgumentParser(
        description="Export a safe text snapshot of a local project."
    )
    parser.add_argument(
        "project_directory",
        nargs="?",
        default=".",
        help="Project directory to scan. Defaults to the current directory.",
    )
    parser.add_argument(
        "--output",
        default="project_snapshot.txt",
        help="Name or path of the generated text file.",
    )
    parser.add_argument(
        "--structure-only",
        action="store_true",
        help="Export only the project structure, without file contents.",
    )

    args = parser.parse_args()

    root = Path(args.project_directory).resolve()
    output_path = Path(args.output).resolve()

    if not root.exists():
        raise SystemExit(f"Project directory does not exist: {root}")

    if not root.is_dir():
        raise SystemExit(f"Provided path is not a directory: {root}")

    export_project(root, output_path, args.structure_only)


if __name__ == "__main__":
    main()