"""Economy QR: verify factors, subspace projection and least squares."""
import numpy as np

def thin_qr_least_squares(A,b):
    A=np.asarray(A,dtype=float);b=np.asarray(b,dtype=float)
    if A.ndim!=2 or A.shape[0]<A.shape[1] or b.shape!=(A.shape[0],):
        raise ValueError("m>=n and b matching rows required")
    if not np.isfinite(A).all() or not np.isfinite(b).all():
        raise ValueError("finite input required")
    if np.linalg.matrix_rank(A)<A.shape[1]:
        raise np.linalg.LinAlgError("full column rank required")
    Q,R=np.linalg.qr(A,mode="reduced")
    x=np.linalg.solve(R,Q.T@b)
    residual=b-A@x
    return {"Q":Q,"R":R,"x":x,
            "factor_residual":float(np.linalg.norm(A-Q@R)),
            "orthogonality":float(np.linalg.norm(Q.T@Q-np.eye(Q.shape[1]))),
            "residual_orthogonality":float(np.linalg.norm(Q.T@residual)),
            "residual_norm":float(np.linalg.norm(residual))}

if __name__=="__main__":
    A=np.array([[1.,0.],[1.,1.],[1.,2.]])
    b=np.array([1.,2.,2.])
    d=thin_qr_least_squares(A,b)
    print("x",d["x"],"Q shape",d["Q"].shape,"R shape",d["R"].shape)
    np.testing.assert_allclose(d["x"],[7/6,1/2],atol=1e-12)
