"""Block GEMM proof of identity, without claiming this Python loop is fast."""
import numpy as np

def blocked_gemm(A,B,block=32):
    A=np.asarray(A,dtype=np.float64)
    B=np.asarray(B,dtype=np.float64)
    if A.ndim!=2 or B.ndim!=2 or A.shape[1]!=B.shape[0]:
        raise ValueError("A and B must be conformable matrices")
    if not isinstance(block,int) or block<1:
        raise ValueError("block width must be a positive integer")
    if not np.isfinite(A).all() or not np.isfinite(B).all():
        raise ValueError("finite operands required")
    m,k=A.shape; _,n=B.shape
    C=np.zeros((m,n),dtype=np.float64)
    for i in range(0,m,block):
        for j in range(0,n,block):
            for q in range(0,k,block):
                C[i:i+block,j:j+block]+=A[i:i+block,q:q+block]@B[q:q+block,j:j+block]
    return C

if __name__=="__main__":
    rng=np.random.default_rng(7)
    A=rng.normal(size=(7,5));B=rng.normal(size=(5,6))
    for block in [1,2,3,8]:
        C=blocked_gemm(A,B,block)
        print(block,np.linalg.norm(C-A@B,ord=np.inf))
        assert np.allclose(C,A@B,atol=1e-12)
