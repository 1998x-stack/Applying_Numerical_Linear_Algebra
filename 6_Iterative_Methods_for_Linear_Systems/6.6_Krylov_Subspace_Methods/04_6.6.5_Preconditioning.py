"""Preconditioned CG on a diagonal SPD teaching example; NumPy >=1.26."""
import numpy as np

def pcg(A, b, mdiag, maxiter=20, tol=1e-12):
    A=np.asarray(A,float); b=np.asarray(b,float); d=np.asarray(mdiag,float)
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or b.shape!=(A.shape[0],) or d.shape!=b.shape:
        raise ValueError("matrix/vector dimensions")
    if np.min(d)<=0 or not np.allclose(A,A.T) or np.min(np.linalg.eigvalsh(A))<=0:
        raise ValueError("SPD A and positive preconditioner required")
    x=np.zeros_like(b); r=b-A@x; z=r/d; p=z.copy(); rz=float(r@z)
    hist=[float(np.linalg.norm(r))]
    for _ in range(maxiter):
        if hist[-1]<tol: break
        Ap=A@p; alpha=rz/float(p@Ap)
        x=x+alpha*p; r=r-alpha*Ap
        hist.append(float(np.linalg.norm(b-A@x)))
        if hist[-1]<tol: break
        z=r/d; newrz=float(r@z)
        p=z+(newrz/rz)*p; rz=newrz
    return x,np.asarray(hist)

def run_case():
    A=np.diag([1.,100.,4.,400.]); b=np.ones(4)
    x,h=pcg(A,b,np.diag(A))
    exact=np.linalg.solve(A,b)
    assert np.linalg.norm(x-exact)<1e-12
    assert len(h)==2 and h[-1]<1e-12
    assert np.linalg.cond(A)==400.
    C=np.diag(1/np.sqrt(np.diag(A)))@A@np.diag(1/np.sqrt(np.diag(A)))
    assert np.allclose(C,np.eye(4))
    return {"kappa_A":float(np.linalg.cond(A)),"kappa_preconditioned":float(np.linalg.cond(C)),"true_residual":h[-1]}
if __name__=="__main__": print(run_case())
