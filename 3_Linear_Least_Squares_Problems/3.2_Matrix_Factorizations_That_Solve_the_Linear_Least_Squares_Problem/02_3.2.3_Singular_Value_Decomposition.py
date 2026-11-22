"""Minimum-norm least squares via SVD and pseudoinverse."""
import numpy as np
def svd_min_norm(A,b,rcond=1e-12):
    A=np.asarray(A,float);b=np.asarray(b,float)
    U,s,Vt=np.linalg.svd(A,full_matrices=False)
    inv=np.where(s>rcond*s[0],1/np.maximum(s,np.finfo(float).tiny),0.)
    return Vt.T@(inv*(U.T@b)),s
def run_case():
    A=np.array([[1.,1.],[2.,2.],[3.,3.]])
    b=np.array([1.,2.,2.])
    x,s=svd_min_norm(A,b)
    exact=np.array([11/28,11/28])
    assert np.allclose(x,exact)
    assert np.allclose(x,np.linalg.pinv(A)@b)
    assert np.linalg.norm(A.T@(b-A@x))<1e-12
    assert np.isclose(s[0],np.sqrt(28))
    assert s[1]<1e-12
    alt=x+np.array([1.,-1.])
    assert np.linalg.norm(A@(alt-x))<1e-12
    assert np.linalg.norm(alt)>np.linalg.norm(x)
    return {"singular_values":s.tolist(),"minimum_norm_parameters":x.tolist()}
if __name__=="__main__":print(run_case())
