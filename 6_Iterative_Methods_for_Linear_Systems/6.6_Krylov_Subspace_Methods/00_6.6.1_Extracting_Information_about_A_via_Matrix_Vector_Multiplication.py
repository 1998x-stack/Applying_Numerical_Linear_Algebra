"""Matrix-vector oracle and Krylov column rank; NumPy >=1.26."""
import numpy as np

def krylov(A, r0, k):
    A = np.asarray(A, float)
    v = np.asarray(r0, float)
    if A.ndim != 2 or A.shape[0] != A.shape[1] or v.shape != (A.shape[0],) or not 1 <= k <= len(v):
        raise ValueError("square A, matching r0 and 1<=k<=n required")
    columns = []
    for _ in range(k):
        columns.append(v.copy())
        v = A @ v
    return np.column_stack(columns)

def run_case():
    A = np.diag([1., 2., 3., 4.])
    K = krylov(A, np.ones(4), 4)
    Kflat = krylov(A, np.array([1.,0.,0.,0.]), 4)
    assert np.linalg.matrix_rank(K) == 4
    assert np.linalg.matrix_rank(Kflat) == 1
    assert np.allclose(A @ K[:,:-1], K[:,1:])
    return {"full_rank": int(np.linalg.matrix_rank(K)), "eigenvector_start_rank": int(np.linalg.matrix_rank(Kflat))}

if __name__ == "__main__":
    print(run_case())
