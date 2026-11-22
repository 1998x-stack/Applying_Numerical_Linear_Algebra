"""Woodbury low-rank updated diagonal solve, avoiding explicit inverses."""
import numpy as np

def woodbury_solve(d,U,V,b):
    d=np.asarray(d,dtype=float);U=np.asarray(U,dtype=float)
    V=np.asarray(V,dtype=float);b=np.asarray(b,dtype=float)
    n=d.size
    if d.ndim!=1 or n<1 or U.ndim!=2 or U.shape[0]!=n or V.shape!=U.shape or b.shape!=(n,):
        raise ValueError("d must be n-vector; U,V n×k; b n-vector")
    if any(not np.isfinite(x).all() for x in (d,U,V,b)):
        raise ValueError("finite input required")
    if np.any(d==0): raise np.linalg.LinAlgError("base diagonal D singular")
    z=b/d;W=U/d[:,None]
    K=np.eye(U.shape[1])+V.T@W
    correction=np.linalg.solve(K,V.T@z)
    x=z-W@correction
    A=np.diag(d)+U@V.T
    return {"x":x,"small_system":K,"residual":float(np.linalg.norm(A@x-b)),
            "parameter_count":int(n+2*n*U.shape[1])}

if __name__=="__main__":
    n=4;ones=np.ones((n,1));b=np.array([1.,0.,0.,0.])
    ans=woodbury_solve(np.ones(n),ones,ones,b)
    print(ans)
    np.testing.assert_allclose(ans["x"],[.8,-.2,-.2,-.2],atol=1e-12)
