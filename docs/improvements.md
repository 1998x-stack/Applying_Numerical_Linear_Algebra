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
