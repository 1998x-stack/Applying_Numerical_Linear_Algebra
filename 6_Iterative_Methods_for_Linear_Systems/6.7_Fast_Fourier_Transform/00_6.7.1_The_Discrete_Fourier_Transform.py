"""DFT convention, inverse and Parseval checks; NumPy >=1.26."""
import numpy as np
def direct_dft(x):
    x=np.asarray(x,complex); n=len(x)
    if n<1: raise ValueError("nonempty vector required")
    j=np.arange(n)[:,None];k=np.arange(n)[None,:]
    return np.exp(-2j*np.pi*j*k/n)@x
def run_case():
    x=np.array([1.,2.,0.,0.])
    X=direct_dft(x)
    expected=np.array([3,1-2j,-1,1+2j])
    assert np.allclose(X,expected)
    assert np.allclose(X,np.fft.fft(x))
    assert np.allclose(np.fft.ifft(X),x)
    assert np.isclose(np.vdot(x,x).real,np.vdot(X,X).real/len(x))
    return {"dft":X.tolist(),"energy":float(np.vdot(x,x).real)}
if __name__=="__main__":print(run_case())
