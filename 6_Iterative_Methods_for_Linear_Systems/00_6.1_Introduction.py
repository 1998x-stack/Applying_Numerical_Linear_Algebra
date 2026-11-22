"""Residual-based stopping rules for iterative linear solvers."""
from __future__ import annotations


def stopping_threshold(b_norm: float, rtol: float = 1e-8, atol: float = 0.0) -> float:
    """Return max(rtol * ||b||, atol), after validating nonnegative inputs."""
    if b_norm < 0 or rtol < 0 or atol < 0:
        raise ValueError("norms and tolerances must be nonnegative")
    return max(rtol * b_norm, atol)


def meets_stopping_rule(
    residual_norm: float, b_norm: float, rtol: float = 1e-8, atol: float = 0.0
) -> bool:
    """Whether the residual norm satisfies the mixed relative/absolute test."""
    if residual_norm < 0:
        raise ValueError("residual_norm must be nonnegative")
    return residual_norm <= stopping_threshold(b_norm, rtol, atol)


if __name__ == "__main__":
    b_norm, residual_norm = 3.0, 2e-9
    threshold = stopping_threshold(b_norm, rtol=1e-8, atol=1e-12)
    print(f"residual = {residual_norm:.2e}; stopping threshold = {threshold:.2e}")
    print("converged" if meets_stopping_rule(residual_norm, b_norm, 1e-8, 1e-12) else "continue")
