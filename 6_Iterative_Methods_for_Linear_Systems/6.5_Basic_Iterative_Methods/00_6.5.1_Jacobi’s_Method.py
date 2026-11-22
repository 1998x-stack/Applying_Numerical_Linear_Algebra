"""Jacobi iteration for the one-dimensional Poisson tridiagonal system."""
from __future__ import annotations

import math


def _residual_norm(x: list[float], b: list[float]) -> float:
    residual = []
    for i, value in enumerate(x):
        left = x[i - 1] if i > 0 else 0.0
        right = x[i + 1] if i + 1 < len(x) else 0.0
        residual.append(b[i] - (2.0 * value - left - right))
    return math.sqrt(sum(value * value for value in residual))


def jacobi_1d(
    n: int, b: list[float], steps: int, x0: list[float] | None = None
) -> tuple[list[float], list[float]]:
    """Solve T_n x=b by Jacobi; return final x and residual history."""
    if n < 1 or len(b) != n or steps < 0:
        raise ValueError("require n>=1, len(b)==n and steps>=0")
    x = list(x0) if x0 is not None else [0.0] * n
    if len(x) != n:
        raise ValueError("x0 must have length n")
    history = [_residual_norm(x, b)]
    for _ in range(steps):
        new = [0.0] * n
        for i in range(n):
            left = x[i - 1] if i > 0 else 0.0
            right = x[i + 1] if i + 1 < n else 0.0
            new[i] = (b[i] + left + right) / 2.0
        x = new
        history.append(_residual_norm(x, b))
    return x, history


if __name__ == "__main__":
    n = 16
    _, residuals = jacobi_1d(n, [1.0] * n, steps=40)
    rho = math.cos(math.pi / (n + 1))
    print(f"Jacobi spectral radius for 1D Poisson: {rho:.6f}")
    print(f"residual: {residuals[0]:.3e} -> {residuals[-1]:.3e}")
