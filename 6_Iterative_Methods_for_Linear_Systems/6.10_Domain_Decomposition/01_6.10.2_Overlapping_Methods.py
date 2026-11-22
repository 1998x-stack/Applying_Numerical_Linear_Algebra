"""Additive Schwarz preconditioner on a seven-point 1D SPD model."""
import numpy as np
def additive_schwarz(A,subdomains):
    n=A.shape[0];B=np.zeros_like(A,dtype=float)
    covered=set()
    for ids in subdomains:
        ids=np.asarray(ids,dtype=int);covered.update(ids.tolist())
        Ai=A[np.ix_(ids,ids)]
        B[np.ix_(ids,ids)]+=np.linalg.solve(Ai,np.eye(len(ids)))
    if covered!=set(range(n)):raise ValueError("subdomains must cover all nodes")
    return B
def run_case():
    n=7;A=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
    sub=[range(0,5),range(2,7)]
    B=additive_schwarz(A,sub)
    assert np.allclose(B,B.T) and np.linalg.eigvalsh(B).min()>0
    eig=np.linalg.eigvals(B@A).real
    omega=0.5;rho=max(abs(1-omega*eig))
    assert rho<1,(eig,rho)
    b=np.ones(n);x=np.zeros(n);history=[np.linalg.norm(b)]
    for _ in range(120):
        x=x+omega*B@(b-A@x)
        history.append(np.linalg.norm(b-A@x))
    assert history[-1]<1e-8
    assert np.linalg.norm(x-np.linalg.solve(A,b))<1e-7
    return {"overlap_nodes":[2,3,4],"rho_iteration":float(rho),"initial_residual":float(history[0]),"end_residual":float(history[-1])}
if __name__=="__main__":print(run_case())
