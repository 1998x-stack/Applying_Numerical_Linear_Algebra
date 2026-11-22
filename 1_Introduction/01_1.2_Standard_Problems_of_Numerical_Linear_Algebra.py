"""Small, deterministic examples of the four standard problem families."""
import numpy as np

def standard_problem_examples():
    A = np.array([[3.0, 1.0], [1.0, 2.0]])
    x_true = np.array([1.0, 2.0])
    b = A @ x_true
    x = np.linalg.solve(A, b)

    A_ls = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])
    b_ls = np.array([1.0, 2.0, 2.0])
    x_ls, residuals, rank, singular_values = np.linalg.lstsq(A_ls, b_ls, rcond=None)

    S = np.array([[2.0, 1.0], [1.0, 2.0]])
    eigenvalues, eigenvectors = np.linalg.eigh(S)

    M = np.array([[3.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    U, sigma, Vh = np.linalg.svd(M, full_matrices=False)
    return {
        "linear_solution": x, "linear_residual": np.linalg.norm(A @ x - b),
        "least_squares_solution": x_ls, "least_squares_residual": np.linalg.norm(A_ls @ x_ls - b_ls),
        "least_squares_rank": rank, "eigenvalues": eigenvalues,
        "eigen_residual": np.linalg.norm(S @ eigenvectors - eigenvectors @ np.diag(eigenvalues)),
        "singular_values": sigma, "svd_reconstruction": np.linalg.norm(M - U @ np.diag(sigma) @ Vh)
    }

if __name__ == "__main__":
    for key, value in standard_problem_examples().items():
        print(f"{key}: {value}")
