# Improvement History

### 2026-11-05 13:17 UTC — ChatGPT Portfolio Iteration
- Run ID: 20261105T131752Z-anla-8246
- Repo / Base SHA: 1998x-stack/Applying_Numerical_Linear_Algebra @ a4b0858e7d085216e0dd3db5a96075b4f8865aeb
- Product problem & expected user value: invalid polynomial bisection brackets could return false roots and endpoint roots could be missed.
- Changes: validate ordered endpoints, positive tolerance, endpoint roots and sign-changing bracket; add regression tests.
- Validation: isolated tests passed; full checkout/CI was not verified in that iteration.
- Follow-up: correct polynomial_condition_number coefficient ordering with independent tests.
- PR: https://github.com/1998x-stack/Applying_Numerical_Linear_Algebra/pull/1 (merged 2026-11-06).

### 2026-11-22 — First chapter content and engineering upgrade
- Scope: first eight Chapter 1 lessons (1.1, 1.2, 1.3.1–1.3.5, 1.4), course portal, README, AGENTS.md, evidence ledgers, Python/MATLAB examples, validation and Pages workflows.
- Diagnosis: legacy pages depended on remote MathJax/polyfill/CDN; several Python and MATLAB examples were placeholders; polynomial condition number paired descending coefficients with ascending powers; introductory explanations overgeneralized LU, SVD and roundoff claims.
- Changes: preserve public lesson paths; add native MathML, eight original SVG diagrams, interactive demos, Python/MATLAB counterparts, per-lesson evidence JSON, tests, static/browser QA scripts, and a Pages-only build excluding PDF and executable source files.
- Numerical correction: for p(x)=2x^3−6x^2+2x−1 at x=3, the correctly indexed coefficient sum is 115, |p(3)|=5, so κ_p(3)=23.
- Validation status: awaiting pull-request Actions. MATLAB scripts are not claimed as executed in MATLAB; Pages is not claimed published until deployment and live URL are checked.
- PR/commit: pending.


- CI first attempt: workflow run 44982406159 failed because the static validator incorrectly required MathML on the course homepage. The homepage intentionally has no mathematical formula. Validator scope corrected; rerun pending.
- QR least-squares explanation clarified: distinguish full QR from economy QR and include the orthogonal-complement residual term Q₂* b.

- CI second attempt: static validation passed; one Python test exposed an API keyword mismatch (`np.linalg.cond` accepts `p`, not `ord`). Updated the wrapper to use `p=ord`; rerun pending.

- CI browser QA found a 390/360 px overflow caused by the responsive grid's automatic min-content track sizing. Changed the mobile track to minmax(0, 1fr), set grid children to min-width:0, and allowed TOC links to wrap. Also clarified MATLAB's conjugate-transpose vs non-conjugating-transpose notation.

- CI browser QA: mobile page overflow fixed; wide MathML formula keyboard-scroll check initially failed with ArrowRight. QA now tests End-to-scroll-end first, then ArrowRight, and ignores sub-8px rounding differences.

### 2026-11-22 — Second batch: Chapter 6 iterative solvers

- Scope: eight standalone Chapter 6 lessons (6.1–6.5.2), Markdown/HTML/Python/MATLAB parity, independent original SVG, offline MathML and per-article evidence files.
- Integration: preserve the concurrently completed eight Chapter 1 lessons, homepage layout, existing build/QA workflows, and public URLs. Append Chapter 6 to the canonical portal instead of replacing Chapter 1.
- Numerical evidence: checked against Demmel Chapter 6 §§6.1–6.5 (including Table 6.1, Theorem 6.1 and Lemma 6.2) and SciPy CG/GMRES API references.
- Cross-checks: two independently written 2D stencil vs Kronecker-sum kernels, one-dimensional Poisson sign and scaling, residual histories for Jacobi and Gauss–Seidel, solver preconditions, and content/evidence parity.
- QA: unittest regression suite and Playwright multi-viewport audit are included; GitHub Actions run status determines actual pass/fail. No MATLAB execution is claimed.
- Publishing: CI-gated GitHub Pages workflow is retained from the main branch. Public availability will be confirmed separately.
- Work branch / PR: anla/iterative-methods-foundations, #3.
