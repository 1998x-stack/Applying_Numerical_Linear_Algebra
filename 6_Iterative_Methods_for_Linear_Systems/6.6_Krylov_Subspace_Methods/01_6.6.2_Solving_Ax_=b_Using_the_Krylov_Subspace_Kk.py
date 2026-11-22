"""Galerkin projection onto nested Krylov spaces, SPD example."""
import numpy as np

def solve_projected(A, b, k):
    A = np.asarray(A, float)
    b = np.asarray(b, float)
    if not 1 <= k <= len(b):
        raise ValueError("1 <= k <= n")
    powers = [b.copy()]
    for _ in range(1, k):
        powers.append(A @ powers[-1])
    V, _ = np.linalg.qr(np.column_stack(powers), mode="reduced")
    y = np.linalg.solve(V.T @ A @ V, V.T @ b)
    x = V @ y
    r = b - A @ x
    return x, float(np.linalg.norm(V.T @ r))

def run_case():
    A = np.diag([1.,2.,3.,4.])
    b = np.ones(4)
    x1, ortho1 = solve_projected(A,b,1)
    x4, ortho4 = solve_projected(A,b,4)
    assert np.allclose(x1, .4*b)
    assert ortho1 < 1e-12 and ortho4 < 1e-12
    assert np.linalg.norm(x4-np.linalg.solve(A,b)) < 1e-10
    return {"x1": x1.tolist(), "VTr_k1": ortho1, "error_k4": float(np.linalg.norm(x4-np.linalg.solve(A,b)))}

if __name__ == "__main__":
    print(run_case())
