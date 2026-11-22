"""Educational Gaussian elimination with partial pivoting, PA=LU."""
import numpy as np

def lu_partial_pivoting(A):
    A=np.asarray(A,dtype=float)
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or A.shape[0]==0 or not np.isfinite(A).all():
        raise ValueError("A must be finite and square with nonzero dimension")
    n=A.shape[0]
    P=np.eye(n); L=np.eye(n); U=A.copy()
    for k in range(n):
        pivot=k+int(np.argmax(np.abs(U[k:,k])))
        if U[pivot,k]==0.0: raise np.linalg.LinAlgError("singular matrix")
        if pivot!=k:
            U[[k,pivot],:]=U[[pivot,k],:]
            P[[k,pivot],:]=P[[pivot,k],:]
            if k: L[[k,pivot],:k]=L[[pivot,k],:k]
        for i in range(k+1,n):
            L[i,k]=U[i,k]/U[k,k]
            U[i,k:]-=L[i,k]*U[k,k:]
            U[i,k]=0.
    return P,L,U

def solve_from_lu(A,b):
    A=np.asarray(A,dtype=float)
    b=np.asarray(b,dtype=float)
    P,L,U=lu_partial_pivoting(A)
    if b.shape!=(A.shape[0],): raise ValueError("b must match A")
    y=np.linalg.solve(L,P@b)
    x=np.linalg.solve(U,y)
    return {"x":x, "factorization_residual":float(np.linalg.norm(P@A-L@U)),
            "solution_residual":float(np.linalg.norm(A@x-b))}

if __name__=="__main__":
    print(solve_from_lu([[0.,2.],[1.,3.]],[2.,4.]))
