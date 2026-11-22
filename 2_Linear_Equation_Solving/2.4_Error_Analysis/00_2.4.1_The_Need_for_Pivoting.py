"""The pivot-size contrast in a 2-by-2 system."""
import numpy as np

def pivot_multiplier_example(tiny=1e-4):
    if not np.isfinite(tiny) or tiny<=0 or tiny>=1:
        raise ValueError("tiny must lie strictly between 0 and 1")
    A=np.array([[tiny,1.],[1.,1.]])
    b=A@np.ones(2)
    m_without=1/tiny
    P=np.array([[0.,1.],[1.,0.]])
    m_with=tiny
    x=np.linalg.solve(A,b)
    return {"multiplier_without":m_without,"multiplier_with":m_with,
            "solution":x, "residual":float(np.linalg.norm(A@x-b)),
            "pivoted_matrix":P@A}

if __name__=="__main__":
    print(pivot_multiplier_example())
