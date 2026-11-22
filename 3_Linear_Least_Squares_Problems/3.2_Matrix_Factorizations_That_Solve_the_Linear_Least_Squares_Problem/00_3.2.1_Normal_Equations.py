"""Normal equations, singular values, and squared conditioning."""
import numpy as np
def test_condition(eps):
    if eps<=0: raise ValueError("eps>0")
    A=np.array([[1.,1.],[1.,1.+eps],[1.,1.+2*eps]])
    return A,float(np.linalg.cond(A)),float(np.linalg.cond(A.T@A))
def run_case():
    A,c,cc=test_condition(1e-3)
    assert np.isclose(cc,c*c,rtol=2e-7),(c,cc)
    A2,c2,cc2=test_condition(1e-4)
    assert 9<c2/c<11
    assert 90<cc2/cc<110
    b=np.array([1.,2.,2.])
    x=np.linalg.solve(A.T@A,A.T@b)
    assert np.linalg.norm(A.T@(b-A@x))<1e-8
    return {"kappa_A":c,"kappa_AtA":cc,"kappa_smaller_eps":c2}
if __name__=="__main__":print(run_case())
