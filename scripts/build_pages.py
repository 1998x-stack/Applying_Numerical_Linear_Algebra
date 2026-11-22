#!/usr/bin/env python3
"""Build a static Pages artifact without publishing executable/source artifacts."""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
WEB_SUFFIXES = {".html", ".css", ".js", ".svg", ".json", ".md", ".png", ".jpg", ".jpeg", ".webp", ".ico", ".txt"}
EXCLUDED_DIRS = {".git", ".github", ".venv", "__pycache__", "tests", "scripts", "evidence", "dist"}

def build(output: Path) -> int:
    output = output.resolve()
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    copied = 0
    for source in ROOT.rglob("*"):
        if not source.is_file():
            continue
        relative = source.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if source.suffix.lower() not in WEB_SUFFIXES and source.name != ".nojekyll":
            continue
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied += 1
    print(f"Built Pages artifact: {copied} web/document files -> {output}")
    print("Excluded: PDF, Python, MATLAB, tests, evidence ledgers, scripts and Git metadata.")
    return copied

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dist")
    args = parser.parse_args()
    build(ROOT / args.output)
