"""SPD Cholesky, factor reconstruction and two triangular solves."""
import numpy as np

def cholesky_solve(A,b):
    A=np.asarray(A,dtype=np.float64)
    b=np.asarray(b,dtype=np.float64)
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or b.shape!=(A.shape[0],):
        raise ValueError("square A and matching b expected")
    if not np.isfinite(A).all() or not np.isfinite(b).all():
        raise ValueError("finite inputs required")
    if not np.allclose(A,A.T,rtol=1e-12,atol=1e-14):
        raise ValueError("real symmetry required")
    L=np.linalg.cholesky(A) # rejects non-SPD matrices
    x=np.linalg.solve(L.T,np.linalg.solve(L,b))
    return {"L":L,"x":x,"factor_error":float(np.linalg.norm(A-L@L.T,ord=np.inf)),
            "residual":float(np.linalg.norm(A@x-b,ord=np.inf))}

if __name__=="__main__":
    A=np.array([[4.,2.],[2.,3.]])
    b=A@np.array([1.,2.])
    print(cholesky_solve(A,b))
    try:
        cholesky_solve(np.array([[0.,1.],[1.,0.]]),np.ones(2))
    except np.linalg.LinAlgError:
        print("indefinite matrix correctly rejected")
