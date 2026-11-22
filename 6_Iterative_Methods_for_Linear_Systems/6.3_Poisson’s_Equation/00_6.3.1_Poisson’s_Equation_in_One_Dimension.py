"""Finite-difference operator for one-dimensional Dirichlet Poisson."""
from __future__ import annotations

import math


def apply_poisson_1d(values: list[float], h: float) -> list[float]:
    """Apply -d²/dx² using the centered stencil and zero boundary values."""
    if h <= 0:
        raise ValueError("h must be positive")
    result = []
    for i, value in enumerate(values):
        left = values[i - 1] if i > 0 else 0.0
        right = values[i + 1] if i + 1 < len(values) else 0.0
        result.append((2.0 * value - left - right) / (h * h))
    return result


def manufactured_problem(n: int) -> tuple[list[float], list[float], float]:
    """Sample v=sin(pi*x), f=pi²sin(pi*x) on n interior points."""
    if n < 1:
        raise ValueError("n must be at least one")
    h = 1.0 / (n + 1)
    x = [(i + 1) * h for i in range(n)]
    exact = [math.sin(math.pi * xi) for xi in x]
    rhs = [math.pi**2 * value for value in exact]
    return exact, rhs, h


if __name__ == "__main__":
    exact, rhs, h = manufactured_problem(8)
    discrete = apply_poisson_1d(exact, h)
    error = max(abs(a - b) for a, b in zip(discrete, rhs))
    print(f"interior points = {len(exact)}, h = {h:.4f}")
    print(f"max pointwise stencil defect = {error:.3e} (expected O(h^2))")
