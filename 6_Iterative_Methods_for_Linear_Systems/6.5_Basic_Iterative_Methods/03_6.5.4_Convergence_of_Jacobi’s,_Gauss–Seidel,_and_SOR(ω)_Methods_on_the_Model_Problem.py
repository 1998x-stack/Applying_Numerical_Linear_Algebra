"""Exact spectral-factor checks on the Dirichlet Poisson model."""
import numpy as np

def spectral_factors(n):
    if n < 2:
        raise ValueError("n >= 2")
    rho_j = float(np.cos(np.pi/(n+1)))
    rho_gs = rho_j**2
    omega = float(2/(1+np.sin(np.pi/(n+1))))
    return rho_j, rho_gs, omega, omega-1

def run_case():
    result = {}
    for n in (8, 16, 32):
        j, gs, omega, sor = spectral_factors(n)
        A = np.diag(np.full(n, 2.0)) + np.diag(np.full(n-1, -1.0), 1) + np.diag(np.full(n-1, -1.0), -1)
        bj = np.eye(n) - A/2
        assert np.isclose(max(abs(np.linalg.eigvals(bj))), j, atol=1e-10)
        assert 0 < sor < gs < j < 1
        result[n] = dict(rho_j=j, rho_gs=gs, omega_opt=omega, rho_sor=sor)
    return result

if __name__ == "__main__":
    print(run_case())
