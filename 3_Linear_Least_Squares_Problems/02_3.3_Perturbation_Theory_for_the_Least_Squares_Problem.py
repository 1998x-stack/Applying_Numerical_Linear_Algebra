"""Fixed observation perturbation vs near-collinear design columns."""
import numpy as np
def experiment(eps):
    if not 0<eps<1:raise ValueError("0<eps<1")
    t=np.arange(4.,dtype=float)
    A=np.column_stack([np.ones(4),1+eps*t])
    truth=np.ones(2)
    b=A@truth
    db=np.array([0.,1e-3,0.,0.])
    fit=np.linalg.lstsq(A,b+db,rcond=None)[0]
    dx=fit-truth
    sing=np.linalg.svd(A,compute_uv=False)
    assert np.linalg.norm(dx)<=np.linalg.norm(db)/sing[-1]*(1+1e-8)
    relative=np.linalg.norm(dx)/np.linalg.norm(truth)
    bound=np.linalg.cond(A)*np.linalg.norm(db)/np.linalg.norm(b)
    assert relative<=bound*(1+1e-8)
    return float(np.linalg.norm(dx)),float(sing[-1]),float(relative),float(bound)
def run_case():
    a,s,rel,bound=experiment(1e-2)
    b,small,_,_=experiment(1e-3)
    assert 9<b/a<11
    assert small<s
    return {"dx_eps_1e-2":a,"dx_eps_1e-3":b,"relative_error":rel,"relative_bound":bound}
if __name__=="__main__":print(run_case())
