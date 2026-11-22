"""One Schur-complement block elimination step; no pivoting in this demo.

For full general GEPP, pivot selection and permutation across panels must be
implemented; use LAPACK DGETRF for production rather than this derivation.
"""
import numpy as np

def block_schur_step(A, block):
    A=np.asarray(A,dtype=np.float64)
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or not np.isfinite(A).all():
        raise ValueError("finite square A required")
    n=A.shape[0]
    if not isinstance(block,int) or not 1<=block<n:
        raise ValueError("block must be an integer from 1 to n-1")
    A11=A[:block,:block];A12=A[:block,block:]
    A21=A[block:,:block];A22=A[block:,block:]
    # Solve A11.T * L21.T = A21.T without explicitly forming A11 inverse.
    L21=np.linalg.solve(A11.T,A21.T).T
    schur=A22-L21@A12
    reconstructed=np.block([[A11,A12],[L21@A11,L21@A12+schur]])
    return {"L21":L21,"schur":schur,
            "reconstruction_error":float(np.linalg.norm(reconstructed-A,ord=np.inf)),
            "update_flops_model":2*(n-block)**2*block}

if __name__=="__main__":
    A=np.array([[4.,1.,1.,0.],[1.,3.,0.,1.],[1.,0.,3.,1.],[0.,1.,1.,4.]])
    for b in (1,2,3):
        ans=block_schur_step(A,b)
        print("b",b,"reconstruction error",ans["reconstruction_error"],"Schur",ans["schur"])
