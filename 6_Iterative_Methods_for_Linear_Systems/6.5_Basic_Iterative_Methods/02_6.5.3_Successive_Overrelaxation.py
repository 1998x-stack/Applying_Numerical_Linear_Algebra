"""SOR on a 1-D Dirichlet Poisson system; NumPy >=1.26."""
import numpy as np

def sor(A, b, omega, sweeps=300):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1] or b.shape != (A.shape[0],):
        raise ValueError("square A and matching b required")
    if not (0 < omega < 2) or np.any(np.diag(A) == 0):
        raise ValueError("require 0 < omega < 2 and nonzero diagonal")
    x = np.zeros_like(b)
    history = [float(np.linalg.norm(b - A @ x))]
    for _ in range(sweeps):
        old = x.copy()
        for i in range(len(b)):
            candidate = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
            x[i] = (1 - omega) * old[i] + omega * candidate
        history.append(float(np.linalg.norm(b - A @ x)))
    return x, np.asarray(history)

def run_case():
    n = 16
    A = np.diag(np.full(n, 2.0)) + np.diag(np.full(n-1, -1.0), 1) + np.diag(np.full(n-1, -1.0), -1)
    b = np.ones(n)
    optimal = 2.0 / (1.0 + np.sin(np.pi / (n+1)))
    results = {}
    reference = np.linalg.solve(A, b)
    for omega in (0.8, 1.0, 1.5, optimal):
        x, hist = sor(A, b, omega)
        assert np.linalg.norm(x-reference) < 1e-7
        results[round(omega, 6)] = float(hist[-1])
    assert 1 < optimal < 2
    return results

if __name__ == "__main__":
    print("final true residuals:", run_case())
