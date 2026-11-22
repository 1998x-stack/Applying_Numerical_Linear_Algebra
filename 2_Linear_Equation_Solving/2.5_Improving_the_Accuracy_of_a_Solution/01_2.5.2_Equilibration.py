"""Row/column max equilibration, including the transformed right-hand side."""
from __future__ import annotations
import numpy as np

def equilibrate_and_solve(A, b):
    A=np.asarray(A,dtype=np.float64)
    b=np.asarray(b,dtype=np.float64)
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or b.shape!=(A.shape[0],):
        raise ValueError("square A and matching b required")
    if not np.isfinite(A).all() or not np.isfinite(b).all():
        raise ValueError("finite matrix and rhs required")
    row_max=np.max(np.abs(A),axis=1)
    if np.any(row_max==0):
        raise np.linalg.LinAlgError("zero row; cannot equilibrate")
    R=1./row_max
    B=R[:,None]*A
    col_max=np.max(np.abs(B),axis=0)
    if np.any(col_max==0):
        raise np.linalg.LinAlgError("zero column; cannot equilibrate")
    C=1./col_max
    B=B*C[None,:]
    if not all(np.isfinite(x).all() for x in (R,C,B)):
        raise ValueError("scaling overflow")
    y=np.linalg.solve(B,R*b)
    x=C*y
    return {"R":R,"C":C,"scaled_A":B,"x":x,
            "condition_original":float(np.linalg.cond(A)),
            "condition_scaled":float(np.linalg.cond(B)),
            "original_residual":float(np.linalg.norm(A@x-b,ord=np.inf))}

if __name__=="__main__":
    A=np.diag([1e6,1.])
    b=A@np.ones(2)
    print(equilibrate_and_solve(A,b))
    near=np.array([[1.,1.],[1.,1.+1e-8]])
    print("nearly dependent: original and scaled condition",
          equilibrate_and_solve(near,near@np.ones(2))["condition_original"],
          equilibrate_and_solve(near,near@np.ones(2))["condition_scaled"])
