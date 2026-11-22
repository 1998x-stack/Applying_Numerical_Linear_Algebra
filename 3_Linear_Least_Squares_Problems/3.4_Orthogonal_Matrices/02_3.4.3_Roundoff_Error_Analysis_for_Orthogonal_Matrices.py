"""Orthogonality vs reconstruction for a nearly dependent 4x2 matrix."""
import numpy as np
def quality(epsilon):
    if epsilon<=0:raise ValueError("positive epsilon")
    t=np.arange(4,dtype=float)
    A=np.column_stack([np.ones(4),1+epsilon*t])
    Q,R=np.linalg.qr(A,mode="reduced")
    orth=np.linalg.norm(Q.T@Q-np.eye(2),ord=2)
    recon=np.linalg.norm(A-Q@R,ord="fro")/np.linalg.norm(A,ord="fro")
    return float(orth),float(recon),float(np.linalg.cond(A))
def run_case():
    orth,recon,cond=quality(1e-8)
    assert orth<1e-12
    assert recon<1e-12
    assert cond>1e8
    assert np.isclose(np.linalg.cond(np.linalg.qr(np.eye(4),mode="reduced")[0]),1)
    return {"orthogonality_defect":orth,"relative_reconstruction":recon,"kappa_A":cond}
if __name__=="__main__":print(run_case())
