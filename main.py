"""Read-only course inventory by default.

The historic version regenerated README.md and many chapter files on execution.
This version does not overwrite any content. Optional stubs require an explicit flag.
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COMPANIONS = (".html", ".py", ".m")


def markdown_modules() -> list[Path]:
    """Return all Markdown article files under the seven numbered chapters."""
    paths: list[Path] = []
    for chapter in sorted(ROOT.iterdir()):
        if chapter.is_dir() and chapter.name[:2] in {f"{n}_" for n in range(1, 8)}:
            paths.extend(p for p in chapter.rglob("*.md") if p.is_file())
    return sorted(paths)


def companion(markdown: Path, extension: str) -> Path:
    """Preserve dotted section numbers like 6.3.1 when changing .md to .py."""
    if markdown.suffix != ".md":
        raise ValueError("expected a Markdown module")
    return markdown.with_name(markdown.name[:-3] + extension)


def inspect_modules() -> tuple[int, list[Path]]:
    paths = markdown_modules()
    missing: list[Path] = []
    for path in paths:
        for extension in COMPANIONS:
            target = companion(path, extension)
            if not target.is_file():
                missing.append(target)
    return len(paths), missing


def create_missing_stubs(missing: list[Path]) -> None:
    for path in missing:
        path.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation ensures even a concurrent writer cannot be overwritten.
        try:
            with path.open("x", encoding="utf-8") as output:
                if path.suffix == ".py":
                    output.write('"""TODO: add a verified runnable numerical example."""\n')
                elif path.suffix == ".m":
                    output.write("% TODO: add a verified MATLAB example.\n")
                else:
                    output.write('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>待完善</title><body><p>内容待完善</p></body></html>\n')
        except FileExistsError:
            pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report absent companion files without editing them")
    parser.add_argument("--create-missing-stubs", action="store_true", help="create absent files only (never overwrite)")
    args = parser.parse_args()

    count, missing = inspect_modules()
    if args.create_missing_stubs:
        create_missing_stubs(missing)
        count, missing = inspect_modules()

    print(f"发现 {count} 个 Markdown 教学模块。")
    if missing:
        for path in missing:
            print("缺少配套文件:", path.relative_to(ROOT))
        return 1 if args.check else 0
    print("所有 Markdown 模块都有对应的 HTML / Python / MATLAB 文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
