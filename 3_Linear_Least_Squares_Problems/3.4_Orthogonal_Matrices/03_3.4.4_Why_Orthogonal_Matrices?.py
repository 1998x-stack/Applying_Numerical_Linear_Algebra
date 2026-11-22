"""Orthogonal rotation preserves norm and inner product."""
import numpy as np
def rotate(theta_degrees):
    th=np.deg2rad(theta_degrees);c=np.cos(th);s=np.sin(th)
    return np.array([[c,-s],[s,c]])
def run_case():
    Q=rotate(30);x=np.array([3.,4.]);y=np.array([-2.,1.])
    assert np.allclose(Q.T@Q,np.eye(2))
    assert np.isclose(np.linalg.norm(Q@x),5)
    assert np.isclose(np.vdot(Q@x,Q@y),np.vdot(x,y))
    assert np.isclose(np.linalg.cond(Q),1)
    T=np.diag([10.,.1])
    assert np.isclose(np.linalg.cond(T),100)
    return {"Qx":(Q@x).tolist(),"dot":float(np.vdot(Q@x,Q@y)),"kappa_Q":float(np.linalg.cond(Q))}
if __name__=="__main__":print(run_case())
