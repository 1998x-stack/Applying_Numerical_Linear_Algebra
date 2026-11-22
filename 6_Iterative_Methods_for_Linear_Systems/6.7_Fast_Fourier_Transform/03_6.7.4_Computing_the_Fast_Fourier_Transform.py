"""Direct recursive radix-2 FFT; compare with NumPy's FFT."""
import numpy as np
def fft_radix2(x):
    x=np.asarray(x,complex); n=len(x)
    if n==0 or (n & (n-1)):
        raise ValueError("length must be a positive power of two")
    if n==1: return x.copy()
    even=fft_radix2(x[::2]); odd=fft_radix2(x[1::2])
    twiddle=np.exp(-2j*np.pi*np.arange(n//2)/n)*odd
    return np.concatenate([even+twiddle,even-twiddle])
def run_case():
    x=np.array([1.,2.,3.,4.,0.,0.,0.,0.])
    X=fft_radix2(x)
    assert np.allclose(X,np.fft.fft(x))
    assert np.allclose(np.fft.ifft(X).real,x)
    X4=fft_radix2([1,2,3,4])
    assert np.allclose(X4,[10,-2+2j,-2,-2-2j])
    return {"N":len(x),"max_direct_vs_library_error":float(np.max(np.abs(X-np.fft.fft(x))))}
if __name__=="__main__": print(run_case())
