"""Least-squares A perturbation: residual adds (A^T A)^-1 dA^T r."""
import numpy as np

def residual_amplification(delta=1e-2,eps=1e-6,r3=1.):
    if not all(np.isfinite(z) for z in (delta,eps,r3)) or delta<=0 or eps<0:
        raise ValueError("delta>0, eps>=0 and all finite required")
    A=np.array([[1.,0.],[0.,delta],[0.,0.]])
    b=np.array([1.,delta,r3])
    dA=np.zeros_like(A);dA[2,1]=eps
    x=np.linalg.lstsq(A,b,rcond=None)[0]
    perturbed=np.linalg.lstsq(A+dA,b,rcond=None)[0]
    exact_component=(delta*delta+eps*r3)/(delta*delta+eps*eps)
    residual=b-A@x
    differential=np.linalg.solve(A.T@A, dA.T@residual-A.T@dA@x)
    return {"baseline":x,"perturbed":perturbed,"residual":residual,
            "analytic_x2":float(exact_component),
            "first_order_x2_change":float(differential[1]),
            "observed_x2_change":float(perturbed[1]-x[1])}

if __name__=="__main__":
    for residual in (0.,1.):
        d=residual_amplification(r3=residual)
        print("r3",residual,"observed",d["observed_x2_change"],"linear",d["first_order_x2_change"])
