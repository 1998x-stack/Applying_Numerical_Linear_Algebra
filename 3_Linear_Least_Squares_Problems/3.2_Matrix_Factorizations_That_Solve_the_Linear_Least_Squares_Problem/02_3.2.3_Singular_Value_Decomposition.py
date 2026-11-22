"""SVD thresholded minimum-norm least squares, explicit numerical rank."""
import numpy as np

def svd_minimum_norm(A,b,rcond=1e-12):
    A=np.asarray(A,dtype=float);b=np.asarray(b,dtype=float)
    if A.ndim!=2 or A.shape[0]==0 or A.shape[1]==0 or b.shape!=(A.shape[0],):
        raise ValueError("nonempty m×n and matching b required")
    if not np.isfinite(A).all() or not np.isfinite(b).all() or not np.isfinite(rcond) or rcond<0:
        raise ValueError("finite data and nonnegative cutoff required")
    U,s,Vt=np.linalg.svd(A,full_matrices=False)
    keep=s>rcond*s[0] if s.size else np.zeros(0,dtype=bool)
    coeff=np.zeros_like(s)
    coeff[keep]=(U.T@b)[keep]/s[keep]
    x=Vt.T@coeff
    return {"x":x,"singular_values":s,"rank":int(np.sum(keep)),
            "reconstruction":float(np.linalg.norm((U*s)@Vt-A)),
            "residual":float(np.linalg.norm(A@x-b))}

if __name__=="__main__":
    A=np.array([[1.,1.],[2.,2.],[3.,3.]])
    b=np.array([1.,2.,3.])
    d=svd_minimum_norm(A,b)
    print("rank",d["rank"],"x",d["x"],"sigma",d["singular_values"])
    np.testing.assert_allclose(d["x"],[.5,.5],atol=1e-12)
