"""Track the element growth factor in GEPP with first-row tie breaking."""
import numpy as np

def wilkinson_matrix(n):
    if not isinstance(n,int) or n<2: raise ValueError("n must be integer >=2")
    A=np.eye(n)+np.tril(-np.ones((n,n)),-1)
    A[:,-1]=1.
    return A

def growth_factor(A):
    U=np.asarray(A,dtype=float).copy()
    if U.ndim!=2 or U.shape[0]!=U.shape[1] or U.shape[0]<2 or not np.isfinite(U).all():
        raise ValueError("finite square matrix of order >=2 required")
    scale=np.max(np.abs(U))
    if scale==0: raise ValueError("zero matrix")
    maximum=float(scale)
    for k in range(U.shape[0]-1):
        pivot=k+int(np.argmax(np.abs(U[k:,k])))
        if U[pivot,k]==0: raise np.linalg.LinAlgError("singular matrix")
        if pivot!=k: U[[pivot,k],:]=U[[k,pivot],:]
        for i in range(k+1,U.shape[0]):
            m=U[i,k]/U[k,k]
            U[i,k:]-=m*U[k,k:]
            U[i,k]=0.
        maximum=max(maximum,float(np.max(np.abs(U))))
    return maximum/scale

if __name__=="__main__":
    for n in (2,3,4,5):
        print(n,growth_factor(wilkinson_matrix(n)),2**(n-1))
