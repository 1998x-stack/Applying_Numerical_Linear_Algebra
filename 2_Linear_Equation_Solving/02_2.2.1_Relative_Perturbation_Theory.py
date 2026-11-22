"""Structured componentwise relative perturbations of a diagonal system."""
import numpy as np

def diagonal_componentwise_demo(gamma=1e8, eps=1e-6):
    if not (np.isfinite(gamma) and gamma>=1 and np.isfinite(eps) and 0<=eps<1):
        raise ValueError("gamma>=1, 0<=eps<1, both finite")
    A=np.diag([gamma,1.])
    b=np.array([gamma,1.])
    x=np.linalg.solve(A,b)
    # The same proportional bounds are applied separately to the two diagonal
    # entries and right-hand-side components. Zero entries remain zero.
    relative_A=np.array([eps,-eps])
    relative_b=np.array([-eps,eps])
    A2=np.diag(np.diag(A)*(1+relative_A))
    b2=b*(1+relative_b)
    x2=np.linalg.solve(A2,b2)
    actual=np.max(np.abs(x2-x)/np.abs(x))
    component_bound=2*eps/(1-eps)
    return {"condition_2":float(np.linalg.cond(A,p=2)),
            "componentwise_relative_error":float(actual),
            "componentwise_bound":float(component_bound)}

if __name__=="__main__":
    print(diagonal_componentwise_demo())
