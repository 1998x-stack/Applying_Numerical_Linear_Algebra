"""Static parity, source evidence and accessibility checks for Chapter 6."""
from __future__ import annotations

import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "6_Iterative_Methods_for_Linear_Systems"
STEMS = [
    "00_6.1_Introduction",
    "01_6.2_On_line_Help_for_Iterative_Methods",
    "6.3_Poisson’s_Equation/00_6.3.1_Poisson’s_Equation_in_One_Dimension",
    "6.3_Poisson’s_Equation/01_6.3.2_Poisson’s_Equation_in_Two_Dimensions",
    "6.3_Poisson’s_Equation/02_6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products",
    "03_6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation",
    "6.5_Basic_Iterative_Methods/00_6.5.1_Jacobi’s_Method",
    "6.5_Basic_Iterative_Methods/01_6.5.2_Gauss–Seidel_Method",
    "6.5_Basic_Iterative_Methods/02_6.5.3_Successive_Overrelaxation",
    "6.5_Basic_Iterative_Methods/03_6.5.4_Convergence_of_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods_on_the_Model_Problem",
    "6.5_Basic_Iterative_Methods/04_6.5.5_Detailed_Convergence_Criteria_for_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods",
    "6.5_Basic_Iterative_Methods/05_6.5.6_Chebyshev_Acceleration_and_Symmetric_SOR_(SSOR)",
    "6.6_Krylov_Subspace_Methods/00_6.6.1_Extracting_Information_about_A_via_Matrix_Vector_Multiplication",
    "6.6_Krylov_Subspace_Methods/01_6.6.2_Solving_Ax_=b_Using_the_Krylov_Subspace_Kk",
    "6.6_Krylov_Subspace_Methods/02_6.6.3_Conjugate_Gradient_Method",
    "6.6_Krylov_Subspace_Methods/03_6.6.4_Convergence_Analysis_of_the_Conjugate_Gradient_Method",
]


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.document_title = ""
        self.main = False
        self.svg = 0
        self.math = 0
        self.controls = 0
        self.outputs = 0
        self.external_assets = []
        self._in_head = False
        self._in_doc_title = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "head":
            self._in_head = True
        if tag == "h1":
            self.h1 += 1
        if tag == "title" and self._in_head:
            self._in_doc_title = True
        if tag == "main":
            self.main = True
        if tag == "svg":
            self.svg += 1
        if tag == "math":
            self.math += 1
        if "data-demo-control" in values:
            self.controls += 1
        if "data-demo-output" in values:
            self.outputs += 1
        if tag in {"script", "link", "img"}:
            target = values.get("src") or values.get("href")
            if target and target.startswith(("http://", "https://")):
                self.external_assets.append(target)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_doc_title = False
        if tag == "head":
            self._in_head = False

    def handle_data(self, text):
        if self._in_doc_title:
            self.document_title += text


def same_stem_file(relative_stem: str, extension: str) -> Path:
    # Path.with_suffix() is incorrect here: section number 6.3.1 contains dots.
    stem_path = BASE / relative_stem
    return stem_path.with_name(stem_path.name + extension)


class CourseIntegrityTests(unittest.TestCase):
    def test_all_companions_and_evidence(self):
        for stem in STEMS:
            with self.subTest(module=stem):
                for suffix in (".md", ".html", ".py", ".m", ".evidence.json"):
                    self.assertTrue(same_stem_file(stem, suffix).is_file())
                evidence = json.loads(same_stem_file(stem, ".evidence.json").read_text(encoding="utf-8"))
                self.assertTrue(evidence["article"])
                self.assertTrue(evidence["claims"])
                for claim in evidence["claims"]:
                    self.assertIn(claim["status"], {"verified", "derived", "illustrative", "unverified"})
                    for field in ("id", "claim", "kind", "source_url", "locator", "notes"):
                        self.assertTrue(claim[field], f"{stem} missing {field}")

    def test_html_semantics_offline_and_interaction(self):
        for stem in STEMS:
            with self.subTest(module=stem):
                html = same_stem_file(stem, ".html").read_text(encoding="utf-8")
                parser = ArticleParser()
                parser.feed(html)
                self.assertTrue(parser.document_title.strip())
                self.assertEqual(parser.h1, 1)
                self.assertTrue(parser.main)
                self.assertGreaterEqual(parser.svg, 1)
                self.assertGreaterEqual(parser.math, 1)
                self.assertGreaterEqual(parser.controls, 1)
                self.assertGreaterEqual(parser.outputs, 1)
                self.assertEqual(parser.external_assets, [])
                self.assertNotIn("cdn.", html.lower())
                self.assertNotIn("mathjax", html.lower())

    def test_markdown_html_primary_heading_and_length(self):
        for stem in STEMS:
            with self.subTest(module=stem):
                md = same_stem_file(stem, ".md").read_text(encoding="utf-8")
                html = same_stem_file(stem, ".html").read_text(encoding="utf-8")
                heading_md = re.search(r"^#\s+(.+)$", md, flags=re.MULTILINE)
                heading_html = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.DOTALL)
                self.assertIsNotNone(heading_md)
                self.assertIsNotNone(heading_html)
                self.assertEqual(re.sub(r"<[^>]+>", "", heading_html.group(1)).strip(), heading_md.group(1).strip())
                self.assertGreater(len(md), 1200)


if __name__ == "__main__":
    unittest.main()
