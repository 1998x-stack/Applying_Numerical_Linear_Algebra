"""Thin QR least squares, orthogonality, Pythagorean check."""
import numpy as np
def qr_lstsq(A,b):
    A=np.asarray(A,float);b=np.asarray(b,float)
    if A.ndim!=2 or A.shape[0]<A.shape[1] or b.shape!=(A.shape[0],):
        raise ValueError("tall A and b required")
    Q,R=np.linalg.qr(A,mode="reduced")
    if np.linalg.matrix_rank(R)<R.shape[0]:raise ValueError("full rank required")
    return np.linalg.solve(R,Q.T@b),Q,R
def run_case():
    A=np.array([[1.,0.],[1.,1.],[1.,2.]])
    b=np.array([1.,2.,2.])
    x,Q,R=qr_lstsq(A,b)
    assert np.allclose(Q.T@Q,np.eye(2))
    assert np.allclose(Q@R,A)
    assert np.allclose(x,[7/6,.5])
    resid=b-A@x
    perp=b-Q@(Q.T@b)
    assert np.isclose(resid@resid,perp@perp)
    assert np.isclose(resid@resid,1/6)
    return {"parameters":x.tolist(),"orthogonality_defect":float(np.linalg.norm(Q.T@Q-np.eye(2)))}
if __name__=="__main__":print(run_case())
