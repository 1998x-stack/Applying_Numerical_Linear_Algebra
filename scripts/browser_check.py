"""Chromium responsive smoke tests for Chapter 6's expanded articles and homepage.

Install: python -m pip install -r requirements-dev.txt
         python -m playwright install chromium
Run:     python scripts/browser_check.py
"""
from __future__ import annotations

import http.server
import socket
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BASE = "6_Iterative_Methods_for_Linear_Systems/"
ARTICLES = [
    BASE + "00_6.1_Introduction.html",
    BASE + "01_6.2_On_line_Help_for_Iterative_Methods.html",
    BASE + "6.3_Poisson’s_Equation/00_6.3.1_Poisson’s_Equation_in_One_Dimension.html",
    BASE + "6.3_Poisson’s_Equation/01_6.3.2_Poisson’s_Equation_in_Two_Dimensions.html",
    BASE + "6.3_Poisson’s_Equation/02_6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products.html",
    BASE + "03_6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation.html",
    BASE + "6.5_Basic_Iterative_Methods/00_6.5.1_Jacobi’s_Method.html",
    BASE + "6.5_Basic_Iterative_Methods/01_6.5.2_Gauss–Seidel_Method.html",
]
VIEWPORTS = [(1440, 900), (768, 1024), (390, 844), (360, 800)]
SCREENSHOTS = ROOT / ".artifacts" / "browser"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, *_args):
        pass


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def main() -> int:
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    server = http.server.ThreadingHTTPServer(("127.0.0.1", free_port()), QuietHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    errors: list[str] = []
    checked = 0
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            for index, article in enumerate(["index.html", *ARTICLES]):
                page = browser.new_page()
                page_errors: list[str] = []
                bad_responses: list[str] = []
                page.on("pageerror", lambda error: page_errors.append(str(error)))
                page.on("response", lambda response: bad_responses.append(f"{response.status} {response.url}") if response.status >= 400 else None)
                url = f"http://127.0.0.1:{server.server_port}/{article}"
                response = page.goto(url, wait_until="networkidle")
                if response is None or not response.ok:
                    errors.append(f"{article}: failed to load ({response.status if response else 'no response'})")
                    page.close()
                    continue

                for width, height in VIEWPORTS:
                    page.set_viewport_size({"width": width, "height": height})
                    page.wait_for_timeout(60)
                    metrics = page.evaluate("""() => ({
                      overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
                      h1: document.querySelectorAll('h1').length,
                      svgCount: document.querySelectorAll('figure svg[role="img"]').length,
                      badSvg: [...document.querySelectorAll('figure svg[role="img"]')].some(svg =>
                        !svg.querySelector('title')?.textContent.trim() ||
                        !svg.querySelector('desc')?.textContent.trim() ||
                        svg.getBoundingClientRect().width === 0),
                      mathCount: document.querySelectorAll('math').length,
                      badMath: [...document.querySelectorAll('math')].some(m =>
                        m.namespaceURI !== 'http://www.w3.org/1998/Math/MathML'),
                      mathOverflow: [...document.querySelectorAll('.math-scroll')].some(el =>
                        el.getBoundingClientRect().right > document.documentElement.clientWidth + 1)
                    })""")
                    checked += 1
                    if metrics["overflow"] > 1:
                        errors.append(f"{article} @ {width}px: horizontal page overflow {metrics['overflow']}px")
                    if metrics["h1"] != 1:
                        errors.append(f"{article} @ {width}px: expected exactly one h1")
                    if article != "index.html":
                        if metrics["svgCount"] < 1 or metrics["badSvg"]:
                            errors.append(f"{article} @ {width}px: missing or inaccessible SVG")
                        if metrics["mathCount"] < 1 or metrics["badMath"] or metrics["mathOverflow"]:
                            errors.append(f"{article} @ {width}px: missing or incorrectly laid out MathML")
                    page.screenshot(path=str(SCREENSHOTS / f"{index:02d}_{width}.png"), full_page=True)

                if article == "index.html":
                    search = page.locator("[data-course-search]")
                    search.fill("6.5.1")
                    if page.locator("[data-course-list] a:visible").count() != 1:
                        errors.append("homepage: search filtering did not narrow to one entry")
                else:
                    control = page.locator("[data-demo-control]").first
                    output = page.locator("[data-demo-output]").first
                    if control.count() == 0 or output.count() == 0:
                        errors.append(f"{article}: missing interactive control or live output")
                    else:
                        before = output.inner_text()
                        if control.get_attribute("type") == "range":
                            control.evaluate("""el => {
                                const next = String(Number(el.value) === Number(el.max) ? Number(el.min) : Number(el.max));
                                el.value = next;
                                el.dispatchEvent(new Event('input', {bubbles: true}));
                            }""")
                        else:
                            options = control.locator("option").evaluate_all("(items) => items.map(item => item.value)")
                            if len(options) > 1:
                                control.select_option(options[1] if control.input_value() != options[1] else options[0])
                        page.wait_for_timeout(80)
                        if before == output.inner_text():
                            errors.append(f"{article}: interaction did not change the live output")

                if page_errors:
                    errors.extend(f"{article}: JavaScript error: {message}" for message in page_errors)
                if bad_responses:
                    errors.extend(f"{article}: broken request: {message}" for message in bad_responses)
                page.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()

    print(f"Checked {1+len(ARTICLES)} pages across {len(VIEWPORTS)} viewports ({checked} viewport checks).")
    if errors:
        print("Browser QA failures:")
        for error in errors:
            print("-", error)
        return 1
    print("Browser QA passed: layout, MathML/SVG, local assets, homepage search and live article interactions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
