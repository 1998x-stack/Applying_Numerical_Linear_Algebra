# Repository architecture

## Design goal

Keep the original seven-chapter path and its stable filenames while making the repository usable as both a source tree and a static learning website. The top-level `index.html` is the course portal; the root `README.md` is the GitHub repository entry point.

## Layout

- `1_Introduction/` through `7_Iterative_Algorithms_for_Eigenvalue_Problems/`: chapter-oriented teaching material. Existing paths are preserved.
- `*.md`: readable source notes and a GitHub-friendly version of each article.
- `*.html`: the standalone browser article. New pages use local CSS/JS, native MathML, semantic headings, accessible SVG and no CDN.
- `*.py` / `*.m`: runnable Python and MATLAB companions. Small deterministic examples are preferred over opaque benchmark claims.
- `evidence.json`: one evidence ledger per newly authored article; each claim has a source, locator and verification status.
- `assets/css/course.css`: shared responsive reading system for new pages.
- `assets/js/course.js`: progressive-enhancement controls and course search. Static figures remain understandable without JavaScript.
- `docs/`: architecture, authoring standards and append-only engineering history.
- `tests/`: numerical regression tests and content/HTML integrity checks.
- `scripts/browser_check.py`: actual Chromium checks at desktop, tablet and mobile widths.
- `.github/workflows/`: quality gate and optional GitHub Pages deployment.

## Article file contract

For a newly expanded module named `<path>/<stem>`, keep these siblings together:

```text
<stem>.md
<stem>.html
<stem>.py
<stem>.m
evidence.json
```

The article must stand alone. A reader should be able to identify the problem, all variables and dimensions, assumptions, derivation, algorithm, numerical limitations and verification method without reading an earlier page.

## Path stability

Do not rename the original chapter directories or numbered filenames in a content-only change. Links in old README files and pages may use those exact paths. The portal may curate only fully authored modules; it must not send readers to a placeholder page as if it were complete.

## Safe inventory script

`main.py` is now a read-only inventory checker by default. It never regenerates README files and never truncates existing modules. The optional `--create-missing-stubs` flag only creates absent companion files; it does not overwrite existing files.

## Publishing

The `pages.yml` workflow uploads the repository as a static site and deploys it through GitHub Pages when Pages is configured to use GitHub Actions. A workflow file alone does not prove that the site is publicly live; confirm the deployment job and published URL after merging.
