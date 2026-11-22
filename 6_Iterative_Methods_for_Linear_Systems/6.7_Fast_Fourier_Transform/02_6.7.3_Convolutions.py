"""Linear convolution and circular aliasing; NumPy >=1.26."""
import numpy as np
def fft_convolution(a,b,length):
    a=np.asarray(a,float); b=np.asarray(b,float)
    if len(a)==0 or len(b)==0 or length<max(len(a),len(b)):
        raise ValueError("FFT length must accommodate each input")
    return np.fft.ifft(np.fft.fft(a,n=length)*np.fft.fft(b,n=length))
def run_case():
    a=np.array([1.,2.,1.]); b=np.array([1.,-1.])
    linear=np.convolve(a,b); expected=np.array([1.,1.,-1.,-1.])
    circular=fft_convolution(a,b,3)
    padded=fft_convolution(a,b,4)
    assert np.allclose(linear,expected)
    assert np.allclose(circular.real,[0.,1.,-1.])
    assert np.allclose(padded.real,expected)
    assert np.max(np.abs(padded.imag))<1e-12
    return {"linear":linear.tolist(),"length3_alias":circular.real.tolist()}
if __name__=="__main__":print(run_case())
