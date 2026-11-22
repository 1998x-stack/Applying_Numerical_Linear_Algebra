"""Teaching reference for kappa_1 via basis-vector solves (NOT a fast estimator)."""
import numpy as np

def one_norm_condition_from_basis_solves(A):
    A=np.asarray(A,dtype=float)
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or A.shape[0]==0 or not np.isfinite(A).all():
        raise ValueError("A must be finite, nonempty square")
    n=A.shape[0]
    # Computes all n columns of A^-1 through n solves. Intended as a
    # transparent reference, not as Hager/Higham's fast estimator.
    columns=[np.linalg.solve(A,np.eye(n)[:,j]) for j in range(n)]
    inverse_norm_1=max(float(np.sum(np.abs(col))) for col in columns)
    return float(np.linalg.norm(A,ord=1)*inverse_norm_1)

if __name__=="__main__":
    A=np.diag([1.,1e-6])
    print("basis solves:",one_norm_condition_from_basis_solves(A))
    print("NumPy reference:",np.linalg.cond(A,p=1))
