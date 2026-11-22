"""Matrix-free five-point finite-difference operator for -Laplace."""
from __future__ import annotations


def apply_poisson_2d(values: list[list[float]], hx: float, hy: float) -> list[list[float]]:
    """Apply -Delta to an interior grid; values[i][j] uses x-major indexing.

    Homogeneous Dirichlet values are assumed outside the interior array.
    """
    if hx <= 0 or hy <= 0:
        raise ValueError("grid spacings must be positive")
    if not values or not values[0]:
        raise ValueError("values must be a non-empty rectangular grid")
    ny = len(values[0])
    if any(len(row) != ny for row in values):
        raise ValueError("values must be rectangular")
    nx = len(values)
    result = [[0.0] * ny for _ in range(nx)]
    for i in range(nx):
        for j in range(ny):
            center = values[i][j]
            left = values[i - 1][j] if i > 0 else 0.0
            right = values[i + 1][j] if i + 1 < nx else 0.0
            down = values[i][j - 1] if j > 0 else 0.0
            up = values[i][j + 1] if j + 1 < ny else 0.0
            result[i][j] = (
                (2.0 * center - left - right) / (hx * hx)
                + (2.0 * center - down - up) / (hy * hy)
            )
    return result


if __name__ == "__main__":
    n = 8
    h = 1.0 / (n + 1)
    grid = [[0.0 for _ in range(n)] for _ in range(n)]
    grid[n // 2][n // 2] = 1.0
    applied = apply_poisson_2d(grid, h, h)
    print(f"grid = {n} x {n}; unknowns = {n*n}; nnz = {5*n*n-4*n}")
    print(f"center response = {applied[n//2][n//2]:.3f}")
