"""A reproducible two-grid correction on a 7x7 2D Dirichlet Poisson grid."""
import numpy as np

def apply_a(x,h):
    y=np.pad(x,1)
    return (4*y[1:-1,1:-1]-y[:-2,1:-1]-y[2:,1:-1]-y[1:-1,:-2]-y[1:-1,2:])/(h*h)

def relax(x,b,h,steps):
    x=x.copy()
    for _ in range(steps):
        x=x+(2/3)*(h*h/4)*(b-apply_a(x,h))
    return x

def restrict_full_weighting(residual):
    n=residual.shape[0]
    if n%2!=1 or n<3 or residual.shape!=(n,n):
        raise ValueError("odd square fine grid, n>=3")
    r=np.pad(residual,1)
    coarse=np.zeros(((n-1)//2,(n-1)//2))
    for i in range(coarse.shape[0]):
        for j in range(coarse.shape[1]):
            a=2*i+2; b=2*j+2
            coarse[i,j]=(4*r[a,b]+2*(r[a-1,b]+r[a+1,b]+r[a,b-1]+r[a,b+1])+
                         r[a-1,b-1]+r[a-1,b+1]+r[a+1,b-1]+r[a+1,b+1])/16
    return coarse

def prolong_bilinear(coarse):
    n=coarse.shape[0]
    if coarse.shape!=(n,n):raise ValueError("square coarse grid")
    nodes=np.arange(0,2*(n+1)+1,2)
    target=np.arange(1,2*(n+1))
    ext=np.pad(coarse,1)
    temp=np.array([np.interp(target,nodes,ext[:,j]) for j in range(n+2)]).T
    return np.array([np.interp(target,nodes,temp[i,:]) for i in range(len(target))])

def solve_coarse(rhs):
    n=len(rhs); H=1/(n+1)
    A=np.column_stack([apply_a(np.eye(n*n)[:,j].reshape(n,n),H).ravel()
                       for j in range(n*n)])
    return np.linalg.solve(A,rhs.ravel()).reshape(n,n)

def two_grid(b):
    n=len(b)
    if n!=7 or b.shape!=(7,7):raise ValueError("this demonstration uses 7x7 only")
    h=1/(n+1); x=np.zeros_like(b)
    before=float(np.linalg.norm(b-apply_a(x,h)))
    x=relax(x,b,h,2)
    rc=restrict_full_weighting(b-apply_a(x,h))
    ec=solve_coarse(rc)
    x=x+prolong_bilinear(ec)
    x=relax(x,b,h,2)
    after=float(np.linalg.norm(b-apply_a(x,h)))
    return x,before,after

def run_case():
    n=7;h=1/(n+1); t=np.arange(1,n+1)*h
    truth=np.outer(np.sin(np.pi*t),np.sin(np.pi*t))
    rhs=apply_a(truth,h)
    x,before,after=two_grid(rhs)
    assert after < before/3
    assert np.linalg.norm(x-truth) < np.linalg.norm(truth)
    assert np.allclose(restrict_full_weighting(np.ones((7,7))),np.ones((3,3)))
    return {"initial_true_residual":before,"after_one_two_grid_cycle":after}
if __name__=="__main__":print(run_case())
