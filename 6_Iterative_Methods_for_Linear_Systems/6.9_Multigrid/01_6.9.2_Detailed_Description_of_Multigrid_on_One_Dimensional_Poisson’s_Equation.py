"""Recursive one-dimensional geometric multigrid V-cycle; NumPy >= 1.26."""
import numpy as np

def lap(n):
    if n<1:return np.empty((0,0))
    h=1/(n+1)
    return (2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1))/h**2

def restrict(r):
    n=len(r)
    if n<3 or (n+1)&n: raise ValueError("n must be 2^k-1 and >=3")
    return (r[0:-2:2]+2*r[1:-1:2]+r[2::2])/4

def prolong(e):
    k=len(e); v=np.zeros(2*k+1)
    v[1::2]=e
    v[0::2]=(np.r_[0.,e]+np.r_[e,0.])/2
    return v

def vcycle(A,b,x=None,pre=2,post=2):
    b=np.asarray(b,float); n=b.size
    if A.shape!=(n,n) or n<1 or (n+1)&n:
        raise ValueError("nested 2^k-1 grid required")
    if n==1: return np.linalg.solve(A,b)
    x=np.zeros(n) if x is None else np.asarray(x,float).copy()
    invd=1/np.diag(A)
    for _ in range(pre):x=x+(2/3)*invd*(b-A@x)
    rc=restrict(b-A@x)
    ec=vcycle(lap(len(rc)),rc,pre=pre,post=post)
    x=x+prolong(ec)
    for _ in range(post):x=x+(2/3)*invd*(b-A@x)
    return x

def run_case():
    n=15;A=lap(n);h=1/(n+1)
    truth=np.sin(np.pi*np.arange(1,n+1)*h);b=A@truth
    x=np.zeros(n);history=[float(np.linalg.norm(b))]
    for _ in range(7):
        x=vcycle(A,b,x)
        history.append(float(np.linalg.norm(b-A@x)))
    assert history[-1]<history[0]*1e-5,history
    assert np.linalg.norm(x-np.linalg.solve(A,b))<1e-4
    # For these nested Poisson grids the Galerkin product equals rediscretization.
    k=7;P=np.column_stack([prolong(np.eye(k)[:,i]) for i in range(k)])
    R=P.T/2
    assert np.allclose(R@A@P,lap(k))
    return {"levels":[15,7,3,1],"true_residual_history":history}
if __name__=="__main__":print(run_case())
