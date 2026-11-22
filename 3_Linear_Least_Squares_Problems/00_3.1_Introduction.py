"""Constant-model least squares, orthogonal projection and residual."""
import numpy as np

def constant_fit(values):
    b=np.asarray(values,dtype=float)
    if b.ndim!=1 or b.size==0 or not np.isfinite(b).all():
        raise ValueError("nonempty finite observation vector required")
    A=np.ones((b.size,1))
    x,*_=np.linalg.lstsq(A,b,rcond=None)
    projected=A@x
    residual=b-projected
    return {"constant":float(x[0]),"projection":projected,"residual":residual,
            "orthogonality":float(np.linalg.norm(A.T@residual)),
            "squared_residual":float(residual@residual)}

if __name__=="__main__":
    d=constant_fit([1,2,4])
    print(d)
    assert abs(d["constant"]-7/3)<1e-12
    assert d["orthogonality"]<1e-12
