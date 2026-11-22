"""Unpreconditioned conjugate gradient on an SPD system; NumPy >=1.26."""
import numpy as np

def conjugate_gradient(A, b, tol=1e-12, maxiter=None):
    A = np.asarray(A, float)
    b = np.asarray(b, float)
    if A.ndim != 2 or A.shape[0] != A.shape[1] or b.shape != (A.shape[0],):
        raise ValueError("square A and matching vector required")
    if not np.allclose(A, A.T) or np.min(np.linalg.eigvalsh(A)) <= 0:
        raise ValueError("standard CG requires SPD A")
    x = np.zeros_like(b)
    r = b - A @ x
    p = r.copy()
    rr = float(r @ r)
    history = [float(np.linalg.norm(r))]
    for _ in range(maxiter if maxiter is not None else 2 * len(b)):
        if np.sqrt(rr) <= tol * max(np.linalg.norm(b), 1):
            break
        Ap = A @ p
        denom = float(p @ Ap)
        if denom <= 0:
            raise ArithmeticError("nonpositive curvature")
        alpha = rr / denom
        x += alpha * p
        r -= alpha * Ap
        next_rr = float(r @ r)
        history.append(float(np.linalg.norm(b-A@x)))
        if np.sqrt(next_rr) <= tol * max(np.linalg.norm(b), 1):
            break
        beta = next_rr / rr
        p = r + beta * p
        rr = next_rr
    return x, np.asarray(history)

def run_case():
    A = np.diag([1.,2.,3.,4.])
    b = np.ones(4)
    x, hist = conjugate_gradient(A, b)
    exact = np.linalg.solve(A,b)
    assert np.linalg.norm(x-exact) < 1e-10
    assert len(hist) <= 5
    return {"iterations": len(hist)-1, "true_residual": float(hist[-1])}

if __name__ == "__main__":
    print(run_case())
