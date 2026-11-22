"""Normwise system perturbations: exact equation and conditional bound."""
import numpy as np

def perturbation_bound(A,b,dA,db):
    A=np.asarray(A,dtype=float); b=np.asarray(b,dtype=float)
    dA=np.asarray(dA,dtype=float); db=np.asarray(db,dtype=float)
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or b.shape!=(A.shape[0],) or dA.shape!=A.shape or db.shape!=b.shape:
        raise ValueError("shapes must match a square system")
    if not all(np.isfinite(z).all() for z in (A,b,dA,db)):
        raise ValueError("nonfinite input")
    x=np.linalg.solve(A,b); x2=np.linalg.solve(A+dA,b+db)
    normA=np.linalg.norm(A,2); normb=np.linalg.norm(b)
    if normb==0: raise ValueError("relative input error requires nonzero b")
    kappa=float(np.linalg.cond(A,p=2))
    alpha=float(np.linalg.norm(dA,2)/normA)
    beta=float(np.linalg.norm(db)/normb)
    if kappa*alpha>=1:
        raise ValueError("condition kappa*alpha < 1 is necessary for this bound")
    bound=kappa*(alpha+beta)/(1-kappa*alpha)
    actual=float(np.linalg.norm(x2-x)/np.linalg.norm(x))
    exact_residual=(A+dA)@(x2-x)-(db-dA@x)
    return {"actual":actual,"bound":float(bound),"condition":kappa,
            "identity_residual":float(np.linalg.norm(exact_residual))}

if __name__=="__main__":
    A=np.array([[2.,0.],[0.,1.]])
    print(perturbation_bound(A,np.array([2.,1.]),np.zeros_like(A),np.array([0.,1e-6])))
