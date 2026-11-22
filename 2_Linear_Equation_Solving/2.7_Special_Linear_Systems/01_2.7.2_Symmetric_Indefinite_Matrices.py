"""2x2 symmetric indefinite family with a valid 2x2 LDL^T pivot block."""
import numpy as np

def indefinite_2x2(t, b=(1.,2.)):
    if not np.isfinite(t):
        raise ValueError("t finite")
    A=np.array([[0.,1.],[1.,float(t)]])
    b=np.asarray(b,dtype=float)
    if b.shape!=(2,) or not np.isfinite(b).all():
        raise ValueError("finite length-two RHS")
    eigs=np.linalg.eigvalsh(A)
    root=np.sqrt(t*t+4)
    expected=np.array([(t-root)/2,(t+root)/2])
    # Whole A is one legal nonsingular 2x2 symmetric pivot block.
    L=np.eye(2);D=A.copy()
    x=np.linalg.solve(A,b)
    return {"A":A,"L":L,"D":D,"eigenvalues":eigs,
            "analytic_eigenvalues":expected,"determinant":float(np.linalg.det(A)),
            "solution":x,"residual":float(np.linalg.norm(A@x-b,ord=np.inf))}

if __name__=="__main__":
    for t in (-3.,0.,3.):
        r=indefinite_2x2(t)
        print("t",t,"eigenvalues",r["eigenvalues"],"det",r["determinant"])
        assert np.allclose(r["A"],r["L"]@r["D"]@r["L"].T)
