"""One exact block cyclic-reduction Schur step on a 3x3 Poisson grid."""
import numpy as np
def block_poisson(n):
    if n<2: raise ValueError("n>=2")
    B=4*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
    off=np.eye(n,k=1)+np.eye(n,k=-1)
    return np.kron(np.eye(n),B)-np.kron(off,np.eye(n))
def eliminate_odd_block_rows(A,b,blocks,width):
    evenblocks=list(range(1,blocks,2))
    oddblocks=list(range(0,blocks,2))
    E=np.array([i*width+j for i in evenblocks for j in range(width)])
    O=np.array([i*width+j for i in oddblocks for j in range(width)])
    Aee=A[np.ix_(E,E)]; Aeo=A[np.ix_(E,O)]
    Aoe=A[np.ix_(O,E)]; Aoo=A[np.ix_(O,O)]
    S=Aee-Aeo@np.linalg.solve(Aoo,Aoe)
    rhs=b[E]-Aeo@np.linalg.solve(Aoo,b[O])
    xe=np.linalg.solve(S,rhs)
    xo=np.linalg.solve(Aoo,b[O]-Aoe@xe)
    x=np.zeros_like(b);x[E]=xe;x[O]=xo
    return x,S
def run_case():
    A=block_poisson(3); b=np.arange(1,10,dtype=float)
    x,S=eliminate_odd_block_rows(A,b,3,3)
    assert S.shape==(3,3)
    B=4*np.eye(3)-np.eye(3,k=1)-np.eye(3,k=-1)
    assert np.allclose(S,B-2*np.linalg.solve(B,np.eye(3)))
    assert np.allclose(x,np.linalg.solve(A,b))
    return {"Schur_shape":S.shape,"true_residual":float(np.linalg.norm(b-A@x))}
if __name__=="__main__":print(run_case())
