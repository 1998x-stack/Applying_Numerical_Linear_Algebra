"""Check the Chebyshev worst-case A-norm bound for CG."""
import numpy as np

def energy(A, error):
    return float(np.sqrt(error @ A @ error))

def run_case():
    A = np.diag([1.,3.,20.,100.])
    b = np.ones(4)
    exact = np.linalg.solve(A,b)
    x = np.zeros(4)
    r = b.copy()
    p = r.copy()
    rr = float(r@r)
    initial = energy(A, exact-x)
    kappa = float(np.linalg.cond(A))
    q = (np.sqrt(kappa)-1)/(np.sqrt(kappa)+1)
    measured = []
    for k in range(1,5):
        Ap = A @ p
        alpha = rr / float(p@Ap)
        x += alpha * p
        r -= alpha * Ap
        new_rr = float(r@r)
        ratio = energy(A,exact-x)/initial
        bound = 2*q**k
        assert ratio <= bound+1e-10
        measured.append((k,float(ratio),float(bound),float(np.linalg.norm(b-A@x))))
        if k<4:
            p = r + (new_rr/rr)*p
            rr = new_rr
    assert energy(A,exact-x)<1e-10
    return measured

if __name__ == "__main__":
    print("k, measured A-error ratio, bound, true residual:",run_case())
