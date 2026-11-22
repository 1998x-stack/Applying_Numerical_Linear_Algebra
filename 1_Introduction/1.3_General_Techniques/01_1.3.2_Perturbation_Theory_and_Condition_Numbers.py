"""Condition numbers and a reproducible near-dependent linear system."""
import numpy as np

def matrix_condition_number(A, ord=2):
    A = np.asarray(A, dtype=float)
    return float(np.linalg.cond(A, ord=ord))

def first_order_relative_bound(kappa, relative_A_perturbation, relative_b_perturbation):
    """A standard normwise bound; valid only when kappa*rel_A < 1."""
    product = kappa * relative_A_perturbation
    if product >= 1:
        raise ValueError("the perturbation bound requires kappa * rel_A < 1")
    return kappa * (relative_A_perturbation + relative_b_perturbation) / (1.0 - product)

def near_dependent_system(delta=1e-8):
    if not (delta > 0 and np.isfinite(delta)):
        raise ValueError("delta must be positive and finite")
    A = np.array([[1.0, 1.0], [1.0, 1.0 + delta]])
    x_true = np.array([1.0, 1.0])
    b = A @ x_true
    b_perturbed = b + np.array([0.0, 1e-10])
    x = np.linalg.solve(A, b)
    x_perturbed = np.linalg.solve(A, b_perturbed)
    return {
        "condition_number_2": matrix_condition_number(A),
        "relative_input_change": np.linalg.norm(b_perturbed - b) / np.linalg.norm(b),
        "relative_solution_change": np.linalg.norm(x_perturbed - x) / np.linalg.norm(x)
    }

if __name__ == "__main__":
    print(near_dependent_system())
