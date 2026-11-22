"""Chebyshev polynomial error filter for a known SPD spectral interval."""
import numpy as np
from numpy.polynomial.chebyshev import chebval

def polynomial(lambdas, lo, hi, order):
    if not (0 < lo < hi and order >= 0):
        raise ValueError("require 0<lo<hi and k>=0")
    coeff = [0.0]*order + [1.0]
    t = (lo+hi-2*np.asarray(lambdas))/(hi-lo)
    denom = chebval((hi+lo)/(hi-lo), coeff)
    return chebval(t, coeff)/denom

def run_case():
    eig = np.array([1., 3., 6., 9.])
    observed = {}
    for k in (1, 3, 5):
        q = polynomial(eig, 1., 9., k)
        bound = 1/np.cosh(k*np.arccosh(1.25))
        assert np.max(np.abs(q)) <= bound+1e-12
        assert abs(polynomial(np.array([0.]),1.,9.,k)[0]-1) < 1e-12
        observed[k] = float(bound)
    return observed

if __name__ == "__main__":
    print("spectral interval minimax bounds:", run_case())
