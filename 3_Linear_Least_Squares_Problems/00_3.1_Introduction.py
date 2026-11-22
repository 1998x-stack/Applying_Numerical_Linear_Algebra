"""A three-point line fit and orthogonal projection; NumPy >=1.26."""
import numpy as np
def fit_line(y):
    y=np.asarray(y,float)
    if y.shape!=(3,):raise ValueError("three observations required")
    A=np.array([[1.,0.],[1.,1.],[1.,2.]])
    x=np.linalg.lstsq(A,y,rcond=None)[0]
    r=y-A@x
    return x,r,A
def run_case():
    x,r,A=fit_line([1,2,2])
    assert np.allclose(x,[7/6,.5])
    assert np.allclose(r,[-1/6,1/3,-1/6])
    assert np.linalg.norm(A.T@r)<1e-12
    assert np.isclose(r@r,1/6)
    return {"intercept":float(x[0]),"slope":float(x[1]),"squared_residual":float(r@r)}
if __name__=="__main__":print(run_case())
