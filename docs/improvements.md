# Improvement History

### 2026-11-05 13:17 UTC — ChatGPT Portfolio Iteration
- Run ID: 20261105T131752Z-anla-8246
- Repo / Base SHA: 1998x-stack/Applying_Numerical_Linear_Algebra @ a4b0858e7d085216e0dd3db5a96075b4f8865aeb
- Historical context: First initialization; default-branch docs/improvements.md returned GitHub 404; no prior PRs returned by search. Default branch last observed 2026-10-01.
- Product problem & expected user value: Numerical linear algebra learners calling bisection on an interval without a sign change receive a plausible but false root, and endpoint roots can be missed. Fail explicitly instead of teaching incorrect answers.
- Engineering diagnosis & evidence: 1_Introduction/03_1.4_Example:_Polynomial_Evaluation.py: polynomial_root_bisection omitted bracket validation and endpoint handling; old [1,0,1] on [0,3] returned approximately 3 despite no real root, and [1,-1] on [1,3] returned approximately 3 instead of 1. Secondary candidate: polynomial_condition_number pairs descending coefficients with ascending powers (unfixed). Third candidate: horner_method empty coefficients raises IndexError without explicit contract (unfixed).
- Options & decision: Bracket validation (user 5 + correctness 5 + evidence 5 + testability 5 - cost 1 - risk 1 = 18); condition number coefficient order (5+5+4+4-2-2=14); empty coefficients contract (3+3+5+5-1-1=14). Selected bracket fix as isolated correctness defect.
- Changes: 1_Introduction/03_1.4_Example:_Polynomial_Evaluation.py validates positive tolerance and ordered interval, handles roots at endpoints, requires sign change, maintains cached f_low. tests/test_polynomial_bisection.py adds four regression scenarios. Public function signature unchanged; invalid inputs now raise ValueError.
- Validation: B — original logic locally reproduced wrong outputs for nonbracketing and endpoint cases. A (limited) — local Python unittest executed four equivalent isolated cases, all passed; repository test file was not executed against a full checkout, so classify it D pending checkout verification. C — GitHub branch source and test files read back successfully. No CI or browser E2E claimed.
- Security & regression review: No dependencies, credentials, workflow, permissions, deployment, or production data changed. Review of isolated patch shows no unrelated edits; branch integration tests remain outstanding.
- Risk & rollback: Callers relying on silent invalid-bracket results will now receive ValueError, an intentional correctness contract change. Revert PR/commit before merge to restore old behavior.
- Follow-up: Run python -m unittest discover -s tests -p 'test_polynomial_bisection.py' on full checkout, then fix polynomial_condition_number coefficient ordering with independent tests.
- Commit: a64c74968587536f0892e70c0a4ae2b98412b2a9; a9684103d316951c8069690bf5dc1fbe1994e6cb
- PR: pending
