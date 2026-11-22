"""Mixed-precision IR: float32 linear solves, float64 residuals.

Educational implementation recomputes the factorization on every correction.
Production solvers should reuse LU factors and handle error bounds carefully.
"""
from __future__ import annotations
import numpy as np

def refine_mixed_precision(A, b, iterations=5):
    A = np.asarray(A, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    if A.ndim != 2 or A.shape[0] != A.shape[1] or b.shape != (A.shape[0],):
        raise ValueError("expected square A and matching b")
    if not np.isfinite(A).all() or not np.isfinite(b).all() or iterations < 0:
        raise ValueError("nonfinite inputs or negative iteration count")
    A_low = A.astype(np.float32)
    if not np.isfinite(A_low).all():
        raise ValueError("float32 conversion overflow")
    b_low = b.astype(np.float32)
    if not np.isfinite(b_low).all():
        raise ValueError("float32 right-hand-side overflow")
    x = np.linalg.solve(A_low, b_low).astype(np.float64)
    def backward(z):
        r = b - A @ z
        denom = np.linalg.norm(A, ord=np.inf) * np.linalg.norm(z, ord=np.inf) + np.linalg.norm(b, ord=np.inf)
        return float(np.linalg.norm(r, ord=np.inf) / denom) if denom else float(np.linalg.norm(r, ord=np.inf))
    history = [backward(x)]
    for _ in range(iterations):
        residual = b - A @ x  # higher precision than the correction solve
        correction = np.linalg.solve(A_low, residual.astype(np.float32)).astype(np.float64)
        x = x + correction  # keep accumulated x in float64
        history.append(backward(x))
        if history[-1] <= 10*np.finfo(np.float64).eps:
            break
    return {"x": x, "backward_errors": history, "float32_condition_product": float(np.linalg.cond(A)*np.finfo(np.float32).eps)}

if __name__ == "__main__":
    A = np.array([[1.,1.],[1.,1.001]])
    b = A @ np.ones(2)
    result = refine_mixed_precision(A, b)
    print("initial / final backward error", result["backward_errors"][0], result["backward_errors"][-1])
    print("solution", result["x"])
