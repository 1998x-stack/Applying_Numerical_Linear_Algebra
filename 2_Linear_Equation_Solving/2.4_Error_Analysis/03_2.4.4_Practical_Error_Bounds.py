"""Residual, componentwise backward error, and a teaching forward bound."""
import numpy as np

def practical_error_metrics(A,b,xhat):
    A=np.asarray(A,dtype=float); b=np.asarray(b,dtype=float); xhat=np.asarray(xhat,dtype=float)
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or A.shape[0]==0 or b.shape!=(A.shape[0],) or xhat.shape!=b.shape:
        raise ValueError("square A and matching vectors required")
    if not all(np.isfinite(z).all() for z in (A,b,xhat)):
        raise ValueError("all inputs must be finite")
    r=b-A@xhat
    d=np.abs(A)@np.abs(xhat)+np.abs(b)
    ratios=np.divide(np.abs(r),d,out=np.full_like(d,np.inf),where=d!=0)
    ratios[(d==0)&(np.abs(r)==0)]=0.
    berr=float(np.max(ratios))
    # n triangular solves would be appropriate with cached factors; this
    # basis scan is solely a reproducible small-matrix teaching reference.
    n=A.shape[0]
    inverse_columns=[np.linalg.solve(A,np.eye(n)[:,j]) for j in range(n)]
    inverse_infty=max(float(np.sum(np.abs([col[i] for col in inverse_columns]))) for i in range(n))
    bound=float(inverse_infty*np.linalg.norm(r,ord=np.inf))
    reference=np.linalg.solve(A,b)
    actual=float(np.linalg.norm(reference-xhat,ord=np.inf))
    return {"residual_inf":float(np.linalg.norm(r,ord=np.inf)),
            "berr":berr,"forward_bound":bound,"actual_error_reference":actual}

if __name__=="__main__":
    A=np.array([[3.,1.],[1.,2.]])
    b=np.array([9.,8.])
    print(practical_error_metrics(A,b,np.array([2.001,2.999])))
