#!/usr/bin/env python3
"""Chromium smoke checks for the homepage and first eight lessons."""
from __future__ import annotations
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
import contextlib
import os
import time

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
"index.html",
"1_Introduction/00_1.1_Basic_Notation.html",
"1_Introduction/01_1.2_Standard_Problems_of_Numerical_Linear_Algebra.html",
"1_Introduction/1.3_General_Techniques/00_1.3.1_Matrix_Factorizations.html",
"1_Introduction/1.3_General_Techniques/01_1.3.2_Perturbation_Theory_and_Condition_Numbers.html",
"1_Introduction/1.3_General_Techniques/02_1.3.3_Effects_of_Roundoff_Error_on_Algorithms.html",
"1_Introduction/1.3_General_Techniques/03_1.3.4_Analyzing_the_Speed_of_Algorithms.html",
"1_Introduction/1.3_General_Techniques/04_1.3.5_Engineering_Numerical_Software.html",
"1_Introduction/03_1.4_Example:_Polynomial_Evaluation.html",
]
VIEWPORTS = [(1440,900),(768,1024),(390,844),(360,800)]

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args): pass

def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is not installed; browser QA not verified.")
        return 2
    os.chdir(ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", 0), QuietHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}/"
    failures = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for rel in PAGES:
                for width,height in VIEWPORTS:
                    page = browser.new_page(viewport={"width":width,"height":height})
                    page_errors = []
                    page.on("pageerror", lambda exc: page_errors.append(str(exc)))
                    page.goto(base + rel, wait_until="networkidle")
                    page.wait_for_timeout(80)
                    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
                    if overflow: failures.append(f"{rel} @ {width}: document overflow")
                    if page_errors: failures.append(f"{rel} @ {width}: JS errors {page_errors}")
                    if rel != "index.html":
                        controls = page.locator("[data-demo-control]")
                        if controls.count() < 2: failures.append(f"{rel}: missing interactive controls")
                        else:
                            before = page.locator("[data-output]").inner_text()
                            controls.nth(1).click()
                            after = page.locator("[data-output]").inner_text()
                            if before == after: failures.append(f"{rel}: demo did not change output")
                    page.emulate_media(media="print")
                    if page.locator("h1").count() != 1: failures.append(f"{rel}: print H1 count mismatch")
                    page.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    if failures:
        print("\n".join(failures))
        return 1
    print(f"Chromium smoke passed: {len(PAGES)} pages × {len(VIEWPORTS)} viewports, interactive demos checked.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
