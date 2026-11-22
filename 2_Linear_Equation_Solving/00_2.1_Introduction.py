"""Direct-system example: solve, residual and condition estimate."""
import numpy as np

def solve_with_diagnostics(A, b):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1] or b.ndim != 1 or b.size != A.shape[0]:
        raise ValueError("A must be square, b must be a matching vector")
    if not np.isfinite(A).all() or not np.isfinite(b).all():
        raise ValueError("inputs must be finite")
    x = np.linalg.solve(A, b)
    r = b - A @ x
    denom = np.linalg.norm(A, 2)*np.linalg.norm(x) + np.linalg.norm(b)
    eta = float(np.linalg.norm(r) / denom) if denom else float(np.linalg.norm(r))
    return {"x":x, "residual":float(np.linalg.norm(r)), "backward_error":eta,
            "condition_2":float(np.linalg.cond(A, p=2))}

if __name__ == "__main__":
    result=solve_with_diagnostics([[3,1],[1,2]], [9,8])
    print(result)
