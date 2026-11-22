"""Householder reflection of [3,4,0] onto the first coordinate axis."""
import numpy as np
def reflector(x):
    x=np.asarray(x,float)
    if x.ndim!=1 or x.size==0 or np.linalg.norm(x)==0:raise ValueError("nonzero vector")
    alpha=np.copysign(np.linalg.norm(x),x[0] if x[0]!=0 else 1.)
    v=x.copy();v[0]+=alpha;u=v/np.linalg.norm(v)
    return np.eye(len(x))-2*np.outer(u,u)
def run_case():
    x=np.array([3.,4.,0.])
    H=reflector(x);y=H@x
    assert np.allclose(H.T@H,np.eye(3))
    assert np.allclose(y,[-5,0,0])
    assert np.isclose(np.linalg.norm(y),np.linalg.norm(x))
    assert np.allclose(H@H@x,x)
    return {"reflected":y.tolist(),"orthogonality_error":float(np.linalg.norm(H.T@H-np.eye(3)))}
if __name__=="__main__":print(run_case())
