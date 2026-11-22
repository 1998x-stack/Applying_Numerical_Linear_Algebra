"""Nonoverlapping Schur-complement domain split of 1D Poisson."""
import numpy as np
def schur_solve(A,b,interior,interface):
    A=np.asarray(A,float); b=np.asarray(b,float)
    I=np.array(interior,dtype=int);G=np.array(interface,dtype=int)
    if sorted(np.r_[I,G].tolist())!=list(range(len(b))) or A.shape!=(len(b),len(b)):
        raise ValueError("disjoint complete partition required")
    Aii=A[np.ix_(I,I)];Aig=A[np.ix_(I,G)]
    Agi=A[np.ix_(G,I)];Agg=A[np.ix_(G,G)]
    Y=np.linalg.solve(Aii,Aig)
    z=np.linalg.solve(Aii,b[I])
    S=Agg-Agi@Y; g=b[G]-Agi@z
    xg=np.linalg.solve(S,g); xi=z-Y@xg
    x=np.zeros_like(b);x[I]=xi;x[G]=xg
    return x,S
def run_case():
    n=5;A=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
    b=np.arange(1.,n+1)
    x,S=schur_solve(A,b,[0,1,3,4],[2])
    assert S.shape==(1,1) and np.allclose(S,[[2/3]])
    assert np.linalg.norm(b-A@x)<1e-12
    assert np.allclose(x,np.linalg.solve(A,b))
    return {"S":S.tolist(),"true_residual":float(np.linalg.norm(b-A@x))}
if __name__=="__main__":print(run_case())
