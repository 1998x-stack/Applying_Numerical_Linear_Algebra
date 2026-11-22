"""Shape, transpose and adjoint conventions used throughout the course."""
import numpy as np

def matrix_shape_demo():
    A = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    x = np.array([1.0, -1.0, 2.0])
    return {"A_shape": A.shape, "x_shape": x.shape, "Ax": A @ x, "Ax_shape": (A @ x).shape}

def adjoint(A):
    """Conjugate transpose: transpose first, then complex conjugation."""
    A = np.asarray(A)
    return np.conjugate(A.T)

def elementwise_absolute_value(A):
    return np.abs(np.asarray(A))

if __name__ == "__main__":
    result = matrix_shape_demo()
    print("A shape:", result["A_shape"])
    print("x shape:", result["x_shape"])
    print("Ax:", result["Ax"], "shape:", result["Ax_shape"])
    C = np.array([[1 + 2j, 3 - 1j]])
    print("C*:", adjoint(C))
