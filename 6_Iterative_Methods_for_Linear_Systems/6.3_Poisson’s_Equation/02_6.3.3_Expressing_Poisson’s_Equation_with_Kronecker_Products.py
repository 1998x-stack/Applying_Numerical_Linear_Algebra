"""Matrix-free Kronecker-sum action for the two-dimensional Poisson operator."""
from __future__ import annotations


def apply_kronecker_sum(values: list[list[float]], hx: float, hy: float) -> list[list[float]]:
    """Apply (I_y kron T_x)/hx² + (T_y kron I_x)/hy² to V.

    V has shape (N_x, N_y). vec(V) is column-major, and the two one-dimensional
    operators are applied independently along rows and columns.
    """
    if hx <= 0 or hy <= 0:
        raise ValueError("grid spacings must be positive")
    if not values or not values[0]:
        raise ValueError("values must be a non-empty rectangular grid")
    ny = len(values[0])
    if any(len(row) != ny for row in values):
        raise ValueError("values must be rectangular")
    nx = len(values)

    # T_x V: second difference down the first (x) index.
    tx_v = [[0.0] * ny for _ in range(nx)]
    for i in range(nx):
        for j in range(ny):
            left = values[i - 1][j] if i > 0 else 0.0
            right = values[i + 1][j] if i + 1 < nx else 0.0
            tx_v[i][j] = (2.0 * values[i][j] - left - right) / (hx * hx)

    # V T_y: second difference across the second (y) index.
    v_ty = [[0.0] * ny for _ in range(nx)]
    for i in range(nx):
        for j in range(ny):
            down = values[i][j - 1] if j > 0 else 0.0
            up = values[i][j + 1] if j + 1 < ny else 0.0
            v_ty[i][j] = (2.0 * values[i][j] - down - up) / (hy * hy)

    return [[tx_v[i][j] + v_ty[i][j] for j in range(ny)] for i in range(nx)]


if __name__ == "__main__":
    nx, ny = 5, 3
    values = [[float(i + 2 * j) for j in range(ny)] for i in range(nx)]
    result = apply_kronecker_sum(values, hx=0.2, hy=0.25)
    print(f"V shape = {nx} x {ny}; vec(V) length = {nx*ny}")
    print(f"operator shape = {nx*ny} x {nx*ny}; result shape = {len(result)} x {len(result[0])}")
