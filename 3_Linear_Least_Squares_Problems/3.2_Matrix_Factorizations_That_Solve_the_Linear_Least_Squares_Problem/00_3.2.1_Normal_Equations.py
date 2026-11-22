"""Full-column-rank normal equations, with reference QR-style lstsq."""
import numpy as np

def normal_equations(A,b):
    A=np.asarray(A,dtype=float);b=np.asarray(b,dtype=float)
    if A.ndim!=2 or A.shape[0]<A.shape[1] or b.shape!=(A.shape[0],) or not np.isfinite(A).all() or not np.isfinite(b).all():
        raise ValueError("finite m×n with m>=n and matching b required")
    if np.linalg.matrix_rank(A)<A.shape[1]:
        raise np.linalg.LinAlgError("full column rank required")
    gram=A.T@A;rhs=A.T@b
    x=np.linalg.solve(gram,rhs)
    x_ref=np.linalg.lstsq(A,b,rcond=None)[0]
    return {"x":x,"reference":x_ref,
            "stationarity":float(np.linalg.norm(A.T@(b-A@x))),
            "condition_A":float(np.linalg.cond(A)),
            "condition_gram":float(np.linalg.cond(gram)),
            "original_residual":float(np.linalg.norm(A@x-b))}

if __name__=="__main__":
    A=np.array([[1.,0.],[1.,1.],[1.,2.]])
    b=np.array([1.,2.,2.])
    d=normal_equations(A,b);print(d)
    np.testing.assert_allclose(d["x"],[7/6,1/2],atol=1e-12)
