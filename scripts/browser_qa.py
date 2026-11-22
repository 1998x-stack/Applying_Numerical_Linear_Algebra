#!/usr/bin/env python3
"""Responsive, offline-first Chromium QA for the homepage and Chapters 1/2 lessons."""
from __future__ import annotations
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
from datetime import datetime, timezone
import json
import os
import shutil

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports" / "browser-qa"
PAGES = [
    ("home", "index.html"),
    ("01", "1_Introduction/00_1.1_Basic_Notation.html"),
    ("02", "1_Introduction/01_1.2_Standard_Problems_of_Numerical_Linear_Algebra.html"),
    ("03", "1_Introduction/1.3_General_Techniques/00_1.3.1_Matrix_Factorizations.html"),
    ("04", "1_Introduction/1.3_General_Techniques/01_1.3.2_Perturbation_Theory_and_Condition_Numbers.html"),
    ("05", "1_Introduction/1.3_General_Techniques/02_1.3.3_Effects_of_Roundoff_Error_on_Algorithms.html"),
    ("06", "1_Introduction/1.3_General_Techniques/03_1.3.4_Analyzing_the_Speed_of_Algorithms.html"),
    ("07", "1_Introduction/1.3_General_Techniques/04_1.3.5_Engineering_Numerical_Software.html"),
    ("08", "1_Introduction/03_1.4_Example:_Polynomial_Evaluation.html"),
    ("9", "2_Linear_Equation_Solving/00_2.1_Introduction.html"),
    ("10", "2_Linear_Equation_Solving/01_2.2_Perturbation_Theory.html"),
    ("11", "2_Linear_Equation_Solving/02_2.2.1_Relative_Perturbation_Theory.html"),
    ("12", "2_Linear_Equation_Solving/03_2.3_Gaussian_Elimination.html"),
    ("13", "2_Linear_Equation_Solving/2.4_Error_Analysis/00_2.4.1_The_Need_for_Pivoting.html"),
    ("14", "2_Linear_Equation_Solving/2.4_Error_Analysis/01_2.4.2_Formal_Error_Analysis_of_Gaussian_Elimination.html"),
    ("15", "2_Linear_Equation_Solving/2.4_Error_Analysis/02_2.4.3_Estimating_Condition_Numbers.html"),
    ("16", "2_Linear_Equation_Solving/2.4_Error_Analysis/03_2.4.4_Practical_Error_Bounds.html"),
    ("17", "2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/00_2.5.1_Single_Precision_Iterative_Refinement.html"),
    ("18", "2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/01_2.5.2_Equilibration.html"),
    ("19", "2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/00_2.6.1_Basic_Linear_Algebra_Subroutines_(BLAS).html"),
    ("20", "2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/01_2.6.2_How_to_Optimize_Matrix_Multiplication.html"),
    ("21", "2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/02_2.6.3_Reorganizing_Gaussian_Elimination_to_use_Level_3_BLAS.html"),
    ("22", "2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/03_2.6.4_More_About_Parallelism_and_Other_Performance_Issues.html"),
    ("23", "2_Linear_Equation_Solving/2.7_Special_Linear_Systems/00_2.7.1_Real_Symmetric_Positive_Definite_Matrices.html"),
    ("24", "2_Linear_Equation_Solving/2.7_Special_Linear_Systems/01_2.7.2_Symmetric_Indefinite_Matrices.html"),
    ("25", "2_Linear_Equation_Solving/2.7_Special_Linear_Systems/02_2.7.3_Band_Matrices.html"),
    ("26", "2_Linear_Equation_Solving/2.7_Special_Linear_Systems/03_2.7.4_General_Sparse_Matrices.html"),
    ("27", "2_Linear_Equation_Solving/2.7_Special_Linear_Systems/04_2.7.5_Dense_Matrices_Depending_on_Fewer_Than_O(n²)_Parameters.html"),
    ("28", "3_Linear_Least_Squares_Problems/00_3.1_Introduction.html"),
    ("29", "3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/00_3.2.1_Normal_Equations.html"),
    ("30", "3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/01_3.2.2_QR_Decomposition.html"),
    ("31", "3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/02_3.2.3_Singular_Value_Decomposition.html"),
    ("32", "3_Linear_Least_Squares_Problems/02_3.3_Perturbation_Theory_for_the_Least_Squares_Problem.html"),
]
VIEWPORTS = [(1440, 900), (768, 1024), (390, 844), (360, 800)]

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass

def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is not installed; browser QA not verified.")
        return 2

    if REPORT_DIR.exists():
        shutil.rmtree(REPORT_DIR)
    REPORT_DIR.mkdir(parents=True)
    os.chdir(ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", 0), QuietHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}/"
    failures = []
    external_requests = []
    screenshots = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for label, rel in PAGES:
                for width, height in VIEWPORTS:
                    page = browser.new_page(viewport={"width": width, "height": height})
                    page_errors = []
                    console_errors = []
                    bad_responses = []
                    page.on("pageerror", lambda exc: page_errors.append(str(exc)))
                    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
                    page.on("response", lambda response: bad_responses.append(f"{response.status} {response.url}") if response.status >= 400 else None)

                    def offline_route(route):
                        url = route.request.url
                        if url.startswith(base) or url.startswith("data:") or url.startswith("blob:"):
                            route.continue_()
                        else:
                            external_requests.append(f"{rel}: blocked external request {url}")
                            route.abort()
                    page.route("**/*", offline_route)

                    try:
                        response = page.goto(base + rel, wait_until="networkidle", timeout=30000)
                        if response is None or response.status >= 400:
                            failures.append(f"{rel} @ {width}: page response missing/failed")
                        page.wait_for_timeout(80)

                        metrics = page.evaluate("""() => ({
                          viewport: window.innerWidth,
                          documentWidth: document.documentElement.scrollWidth,
                          h1Count: document.querySelectorAll('h1').length,
                          images: [...document.images].map(img => ({src: img.getAttribute('src'), loaded: img.complete && img.naturalWidth > 0})),
                          math: [...document.querySelectorAll('math')].map(el => {
                            const r = el.getBoundingClientRect();
                            return {namespace: el.namespaceURI, width: r.width, height: r.height};
                          }),
                          fractions: [...document.querySelectorAll('mfrac')].map(el => {
                            const c = [...el.children];
                            if (c.length !== 2) return {arity: c.length, valid: false};
                            const n = c[0].getBoundingClientRect(), d = c[1].getBoundingClientRect();
                            return {arity: c.length, valid: n.width > 0 && d.width > 0 && n.top < d.top};
                          }),
                          mathInsideSvg: !!document.querySelector('svg math'),
                          overflowNodes: [...document.querySelectorAll('body *')].map(el => {
                            const r = el.getBoundingClientRect();
                            return {tag: el.tagName, cls: typeof el.className === 'string' ? el.className : '', right: r.right, width: r.width};
                          }).filter(x => x.right > window.innerWidth + 1).slice(0, 8)
                        })""")

                        if metrics["documentWidth"] > width:
                            failures.append(f"{rel} @ {width}: document overflow {metrics['documentWidth']}px; offenders={metrics['overflowNodes']}")
                        if metrics["h1Count"] != 1:
                            failures.append(f"{rel} @ {width}: expected one H1, got {metrics['h1Count']}")
                        for img in metrics["images"]:
                            if not img["loaded"]:
                                failures.append(f"{rel} @ {width}: image failed {img['src']}")
                        if rel != "index.html":
                            if not metrics["math"]:
                                failures.append(f"{rel} @ {width}: no MathML")
                            for item in metrics["math"]:
                                if item["namespace"] != "http://www.w3.org/1998/Math/MathML" or item["width"] <= 0 or item["height"] <= 0:
                                    failures.append(f"{rel} @ {width}: MathML namespace/geometry failure {item}")
                            if metrics["mathInsideSvg"]:
                                failures.append(f"{rel} @ {width}: MathML nested inside SVG")
                            if any(not item["valid"] for item in metrics["fractions"]):
                                failures.append(f"{rel} @ {width}: malformed or invisible mfrac {metrics['fractions']}")

                            controls = page.locator("[data-demo-control]")
                            if controls.count() < 2:
                                failures.append(f"{rel}: missing interactive controls")
                            else:
                                before = page.locator("[data-output]").inner_text()
                                controls.nth(1).click()
                                after = page.locator("[data-output]").inner_text()
                                if before == after:
                                    failures.append(f"{rel}: demo did not change meaningful output")

                            # Advanced lessons: move a native range slider and check the
                            # actual computed chart and live numerical explanation.
                            lab = page.locator("[data-advanced-lab]")
                            if lab.count():
                                slider = lab.locator("[data-lab-slider]")
                                output = lab.locator("[data-lab-output]")
                                if slider.count() != 1 or output.count() != 1:
                                    failures.append(f"{rel}: numeric lab slider or output missing")
                                else:
                                    prior = output.inner_text()
                                    slider.evaluate("(el) => { el.value = el.max; el.dispatchEvent(new Event('input', {bubbles:true})); }")
                                    current = output.inner_text()
                                    if prior == current:
                                        failures.append(f"{rel}: moving numeric slider did not update the computed result")
                                    rows = lab.locator(".model-row")
                                    if rows.count() < 2:
                                        failures.append(f"{rel}: numeric model failed to draw comparison bars")
                                    elif not rows.first.locator(".model-fill").get_attribute("style"):
                                        failures.append(f"{rel}: numeric model bar has no computed geometry")
                                # The four graphical deep dives must redraw SVG geometry.
                                lab_kind = lab.get_attribute("data-advanced-lab")
                                if lab_kind in ("gemm", "blockedlu", "roofline", "indefinite"):
                                    drawing = lab.locator("[data-dynamic-svg]")
                                    if drawing.count() != 1 or drawing.locator("svg").count() != 1:
                                        failures.append(f"{rel}: missing live domain-specific SVG")
                                    else:
                                        fingerprint = drawing.get_attribute("data-model-fingerprint")
                                        if fingerprint != f"{lab_kind}:{slider.get_attribute('max')}":
                                            failures.append(f"{rel}: SVG did not redraw with changed parameter")
                                        bbox = drawing.locator("svg").bounding_box()
                                        if bbox is None or bbox["width"] <= 0 or bbox["height"] <= 0:
                                            failures.append(f"{rel}: live SVG geometry is empty")


                            # Chapter 2/3 lessons redraw numerical output and live SVG.
                            new_lab = page.locator("[data-next-lab]")
                            if new_lab.count():
                                new_slider = new_lab.locator("[data-next-slider]")
                                new_output = new_lab.locator("[data-next-output]")
                                new_visual = new_lab.locator("[data-next-visual]")
                                if new_slider.count()!=1 or new_output.count()!=1 or new_visual.count()!=1:
                                    failures.append(f"{rel}: new numerical model controls missing")
                                else:
                                    old_value = new_output.inner_text()
                                    old_picture = new_visual.inner_html()
                                    new_slider.evaluate("(el) => { el.value = el.max; el.dispatchEvent(new Event('input', {bubbles: true})); }")
                                    if old_value == new_output.inner_text():
                                        failures.append(f"{rel}: changing numerical slider did not update output")
                                    if old_picture == new_visual.inner_html():
                                        failures.append(f"{rel}: changing numerical slider did not redraw SVG")
                                    picture = new_visual.locator("svg")
                                    if picture.count()!=1:
                                        failures.append(f"{rel}: no live SVG generated")
                                    else:
                                        bounds = picture.bounding_box()
                                        if bounds is None or bounds["width"]<=0 or bounds["height"]<=0:
                                            failures.append(f"{rel}: live SVG geometry invisible")
                                    wanted = f"{new_lab.get_attribute('data-next-lab')}:{new_slider.get_attribute('max')}"
                                    if new_visual.get_attribute("data-model-fingerprint") != wanted:
                                        failures.append(f"{rel}: numeric diagram did not track current parameter")

                            # Keyboard focus must move through native controls.
                            first = page.locator("[data-demo-control]").first
                            first.focus()
                            page.keyboard.press("Tab")
                            if page.evaluate("document.activeElement === document.body"):
                                failures.append(f"{rel}: keyboard focus was lost after Tab")

                            # If a formula genuinely overflows its own region, ArrowRight must scroll it.
                            for region in page.locator(".math-scroll").all():
                                sizes = region.evaluate("(el) => ({client:el.clientWidth, scroll:el.scrollWidth})")
                                if sizes["scroll"] > sizes["client"] + 8:
                                    region.focus()
                                    # Focusing a partially visible MathML element may auto-scroll its
                                    # container to the far end; reset before exercising the keyboard.
                                    region.evaluate("(el) => { el.scrollLeft = 0; }")
                                    page.wait_for_timeout(80)
                                    before_scroll = region.evaluate("(el) => el.scrollLeft")
                                    for _ in range(3):
                                        page.keyboard.press("ArrowRight")
                                    # Chromium processes default keyboard scrolling on animation frames.
                                    page.wait_for_timeout(300)
                                    after_scroll = region.evaluate("(el) => el.scrollLeft")
                                    if after_scroll <= before_scroll + 1:
                                        failures.append(
                                            f"{rel} @ {width}: keyboard cannot scroll wide formula; "
                                            f"client={sizes['client']} scroll={sizes['scroll']} "
                                            f"before={before_scroll} after={after_scroll}"
                                        )

                        if page_errors:
                            failures.append(f"{rel} @ {width}: JS page errors {page_errors}")
                        if console_errors:
                            failures.append(f"{rel} @ {width}: console errors {console_errors}")
                        if bad_responses:
                            failures.append(f"{rel} @ {width}: failed responses {bad_responses}")

                        shot = REPORT_DIR / f"{label}-{width}.png"
                        page.screenshot(path=str(shot), full_page=True)
                        screenshots.append(str(shot.relative_to(ROOT)))
                        if width == 1440:
                            page.emulate_media(media="print")
                            print_shot = REPORT_DIR / f"{label}-print.png"
                            page.screenshot(path=str(print_shot), full_page=True)
                            screenshots.append(str(print_shot.relative_to(ROOT)))
                    except Exception as exc:
                        failures.append(f"{rel} @ {width}: browser exception {type(exc).__name__}: {exc}")
                    finally:
                        page.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()

    failures.extend(external_requests)
    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "browser": "Chromium via Playwright",
        "viewports": [{"width": w, "height": h} for w, h in VIEWPORTS],
        "pages": [path for _, path in PAGES],
        "checks": ["offline local-only requests", "page and console errors", "document overflow", "H1 count", "image load", "MathML namespace and geometry", "mfrac structure", "no MathML inside SVG", "interactive output", "keyboard focus", "formula keyboard scrolling when needed", "print screenshots"],
        "screenshots": screenshots,
        "failures": failures,
        "status": "passed" if not failures else "failed",
    }
    (REPORT_DIR / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Browser QA {report['status']}: {len(PAGES)} pages × {len(VIEWPORTS)} viewports; screenshots={len(screenshots)}; report={REPORT_DIR / 'report.json'}")
    if failures:
        print("\n".join(failures))
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
