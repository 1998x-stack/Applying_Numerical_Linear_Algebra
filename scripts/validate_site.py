#!/usr/bin/env python3
"""Static checks for the first eight lessons and the course portal."""
from __future__ import annotations
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
"1_Introduction/00_1.1_Basic_Notation.html",
"1_Introduction/01_1.2_Standard_Problems_of_Numerical_Linear_Algebra.html",
"1_Introduction/1.3_General_Techniques/00_1.3.1_Matrix_Factorizations.html",
"1_Introduction/1.3_General_Techniques/01_1.3.2_Perturbation_Theory_and_Condition_Numbers.html",
"1_Introduction/1.3_General_Techniques/02_1.3.3_Effects_of_Roundoff_Error_on_Algorithms.html",
"1_Introduction/1.3_General_Techniques/03_1.3.4_Analyzing_the_Speed_of_Algorithms.html",
"1_Introduction/1.3_General_Techniques/04_1.3.5_Engineering_Numerical_Software.html",
"1_Introduction/03_1.4_Example:_Polynomial_Evaluation.html",
]

class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.ids = set()
        self.duplicates = []
        self.links = []
        self.images = []
        self.math = 0
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1": self.h1 += 1
        if "id" in a:
            if a["id"] in self.ids: self.duplicates.append(a["id"])
            self.ids.add(a["id"])
        if tag == "a" and "href" in a: self.links.append(a["href"])
        if tag == "img" and "src" in a: self.images.append(a["src"])
        if tag == "math": self.math += 1
        if tag == "script" and "src" in a: self.scripts.append(a["src"])

def check_file(path: Path, require_math: bool = True) -> list[str]:
    errors = []
    if not path.exists():
        return [f"missing page: {path.relative_to(ROOT)}"]
    text = path.read_text(encoding="utf-8")
    parser = Audit()
    parser.feed(text)
    if parser.h1 != 1: errors.append(f"{path.name}: expected one H1, got {parser.h1}")
    if parser.duplicates: errors.append(f"{path.name}: duplicate ids {parser.duplicates}")
    if require_math and parser.math == 0: errors.append(f"{path.name}: no MathML formula")
    for target in parser.links + parser.images + parser.scripts:
        if target.startswith(("http://", "https://", "mailto:", "#")):
            if target.startswith(("http://", "https://")) and ("cdnjs" in target or "polyfill.io" in target or "mathjax" in target.lower()):
                errors.append(f"{path.name}: remote runtime dependency {target}")
            continue
        local = (path.parent / target.split("#",1)[0]).resolve()
        if target and not local.exists(): errors.append(f"{path.name}: missing local target {target}")
    if re.search(r"讲义(介绍|指出|提到)|本节主要讨论|原创图解.*单文件", text):
        errors.append(f"{path.name}: process narration or banned boilerplate")
    return errors

def check_lesson_sources(html_path: Path) -> list[str]:
    errors = []
    md_path = html_path.with_suffix(".md")
    if not md_path.exists():
        return [f"missing Markdown source: {md_path.relative_to(ROOT)}"]
    md = md_path.read_text(encoding="utf-8")
    html = html_path.read_text(encoding="utf-8")
    headings = [h.strip() for h in re.findall(r"^## (.+)$", md, flags=re.M)
                if h.strip() not in {"学习目标", "动手检查", "参考资料"}]
    for heading in headings:
        if f"<h2>{heading}</h2>" not in html:
            errors.append(f"{html_path.name}: Markdown heading missing in HTML: {heading}")
    return errors

def main() -> int:
    errors = check_file(ROOT / "index.html", require_math=False)
    for rel in PAGES:
        page = ROOT / rel
        errors.extend(check_file(page, require_math=True))
        errors.extend(check_lesson_sources(page))
        for suffix in (".py", ".m"):
            example = page.with_suffix(suffix)
            if not example.exists():
                errors.append(f"missing example: {example.relative_to(ROOT)}")
    for i in range(1, 9):
        if not (ROOT / "evidence" / f"{i:02d}.json").exists():
            errors.append(f"missing evidence ledger: evidence/{i:02d}.json")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Static validation passed: homepage + {len(PAGES)} lessons, Markdown headings, examples and evidence ledgers.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
