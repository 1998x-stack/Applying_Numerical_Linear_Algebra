"""Real Givens plane rotation, using hypot for stability."""
import numpy as np
def givens(a,b):
    r=float(np.hypot(a,b))
    if r==0:return np.eye(2)
    c=a/r;s=b/r
    return np.array([[c,s],[-s,c]],float)
def run_case():
    G=givens(3,4)
    assert np.allclose(G@np.array([3.,4.]),[5.,0.])
    assert np.allclose(G.T@G,np.eye(2))
    H=np.eye(3);H[np.ix_([0,2],[0,2])]=G
    A=np.array([[3.,1.],[8.,9.],[4.,2.]])
    transformed=H@A
    assert abs(transformed[2,0])<1e-12
    assert np.allclose(transformed[1,:],A[1,:])
    assert np.allclose(H.T@H,np.eye(3))
    return {"c":float(G[0,0]),"s":float(G[0,1]),"zeroed":float(transformed[2,0])}
if __name__=="__main__":print(run_case())
