"""A solver wrapper that reports residual and normalized backward error."""
import numpy as np

def solve_and_validate(A, b):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A must be square for this direct solve example")
    if b.shape[0] != A.shape[0]:
        raise ValueError("the leading dimension of b must match A")
    x = np.linalg.solve(A, b)
    residual = A @ x - b
    denom = np.linalg.norm(A) * np.linalg.norm(x) + np.linalg.norm(b)
    backward_error = np.linalg.norm(residual) / denom if denom else np.linalg.norm(residual)
    return x, float(np.linalg.norm(residual)), float(backward_error)

if __name__ == "__main__":
    A = np.array([[3.0, 1.0], [1.0, 2.0]])
    b = np.array([9.0, 8.0])
    x, residual, backward_error = solve_and_validate(A, b)
    print("solution:", x)
    print("residual norm:", residual)
    print("normalized backward error:", backward_error)
