"""Rank-deficient least squares and truncated SVD; NumPy >=1.26."""
import numpy as np
def truncated_svd(A,b,tau):
    A=np.asarray(A,float);b=np.asarray(b,float)
    if tau<0:raise ValueError("tau>=0")
    U,s,Vt=np.linalg.svd(A,full_matrices=False)
    tol=max(tau,np.finfo(float).eps*max(A.shape)*s[0])
    inv=np.divide(1,s,out=np.zeros_like(s),where=s>tol)
    x=Vt.T@(inv*(U.T@b))
    return x,s
def run_case():
    A=np.array([[5.,0.,0.],[0.,.02,0.],[0.,0.,0.],[0.,0.,0.]])
    b=np.array([5.,.02,.1,0.])
    x,s=truncated_svd(A,b,0)
    y,_=truncated_svd(A,b,.05)
    assert np.allclose(s,[5.,.02,0.])
    assert np.allclose(x,[1.,1.,0.])
    assert np.allclose(y,[1.,0.,0.])
    assert np.isclose(np.linalg.norm(b-A@x),.1)
    assert np.isclose(np.linalg.norm(b-A@y),np.hypot(.1,.02))
    assert np.linalg.norm(y)<np.linalg.norm(x)
    return {"singular_values":s.tolist(),"minimum_norm_x":x.tolist(),"truncated_x":y.tolist()}
if __name__=="__main__":print(run_case())
