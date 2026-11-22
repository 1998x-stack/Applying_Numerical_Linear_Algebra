"""Continuous/discrete sine eigenpairs for Dirichlet Poisson; NumPy."""
import numpy as np
def poisson_sine_mode(n):
    if n<3: raise ValueError("n>=3")
    h=1/(n+1); ix=np.arange(1,n+1); s=np.sin(np.pi*ix*h)
    eig=4*np.sin(np.pi/(2*(n+1)))**2/h**2
    T=(2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1))/h**2
    b=np.pi**2*s
    spectral=b/eig
    direct=np.linalg.solve(T,b)
    assert np.linalg.norm(spectral-direct)<1e-10
    return np.max(np.abs(spectral-s)),eig
def run_case():
    errors=[poisson_sine_mode(n)[0] for n in (7,15,31)]
    assert errors[0]>errors[1]>errors[2]
    assert 3<errors[0]/errors[1]<5
    return {"N":[7,15,31],"discretization_amplitude_errors":errors}
if __name__=="__main__": print(run_case())
