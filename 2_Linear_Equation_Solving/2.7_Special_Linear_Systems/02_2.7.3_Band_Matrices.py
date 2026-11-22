"""Tridiagonal Thomas elimination (nonzero pivots required); reference NumPy solve."""
import numpy as np

def thomas_solve(lower, diag, upper, b):
    d=np.asarray(diag,dtype=float).copy()
    a=np.asarray(lower,dtype=float).copy()
    c=np.asarray(upper,dtype=float).copy()
    r=np.asarray(b,dtype=float).copy()
    n=d.size
    if n<1 or d.ndim!=1 or a.shape!=(n-1,) or c.shape!=(n-1,) or r.shape!=(n,):
        raise ValueError("diagonal lengths must be n-1, n, n-1 and b length n")
    if any(not np.isfinite(x).all() for x in (a,d,c,r)):
        raise ValueError("finite inputs required")
    if d[0]==0: raise np.linalg.LinAlgError("zero pivot; pivoted solver required")
    for i in range(1,n):
        m=a[i-1]/d[i-1]
        d[i]-=m*c[i-1]
        r[i]-=m*r[i-1]
        if d[i]==0: raise np.linalg.LinAlgError("zero pivot; pivoted solver required")
    x=np.zeros(n)
    x[-1]=r[-1]/d[-1]
    for i in range(n-2,-1,-1):
        x[i]=(r[i]-c[i]*x[i+1])/d[i]
    return x

def tridiagonal_matrix(n):
    if not isinstance(n,int) or n<1: raise ValueError("n positive integer")
    d=4*np.ones(n); lo=-np.ones(n-1);up=-np.ones(n-1)
    A=np.diag(d)+np.diag(lo,-1)+np.diag(up,1)
    return A,lo,d,up

if __name__=="__main__":
    for n in (2,4,8):
        A,a,d,c=tridiagonal_matrix(n)
        b=A@np.ones(n)
        x=thomas_solve(a,d,c,b)
        print("n",n,"nnz",int(np.count_nonzero(A)),"residual",np.linalg.norm(A@x-b))
        np.testing.assert_allclose(x,np.linalg.solve(A,b),atol=1e-12)
