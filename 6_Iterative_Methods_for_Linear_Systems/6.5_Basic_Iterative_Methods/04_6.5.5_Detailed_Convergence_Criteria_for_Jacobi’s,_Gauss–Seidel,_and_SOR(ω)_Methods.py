"""A symmetric positive-definite matrix where Jacobi does not converge."""
import numpy as np

def jacobi_radius(diagonal):
    if diagonal <= 1:
        raise ValueError("diagonal > 1 required for this SPD family")
    A = np.ones((3,3)) + (diagonal-1)*np.eye(3)
    B = np.eye(3) - np.diag(1/np.diag(A)) @ A
    assert np.min(np.linalg.eigvalsh(A)) > 0
    return float(max(abs(np.linalg.eigvals(B))))

def run_case():
    rho2 = jacobi_radius(2)
    rho3 = jacobi_radius(3)
    assert np.isclose(rho2, 1)
    assert np.isclose(rho3, 2/3)
    return {"SPD_but_Jacobi_stagnates": rho2, "SPD_and_Jacobi_converges": rho3}

if __name__ == "__main__":
    print(run_case())
