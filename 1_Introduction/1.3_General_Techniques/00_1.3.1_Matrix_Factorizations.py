"""Numerical checks for LU, QR, Cholesky and SVD factorization identities."""
import numpy as np

def lu_partial_pivoting(A):
    """Return P, L, U satisfying P @ A = L @ U (square nonsingular A)."""
    U = np.array(A, dtype=float, copy=True)
    if U.ndim != 2 or U.shape[0] != U.shape[1]:
        raise ValueError("A must be a square matrix")
    n = U.shape[0]
    P = np.eye(n)
    L = np.eye(n)
    for k in range(n):
        pivot = k + int(np.argmax(np.abs(U[k:, k])))
        if abs(U[pivot, k]) <= np.finfo(float).eps * max(1.0, np.linalg.norm(U, ord=np.inf)):
            raise np.linalg.LinAlgError("matrix is singular to working precision")
        if pivot != k:
            U[[k, pivot], :] = U[[pivot, k], :]
            P[[k, pivot], :] = P[[pivot, k], :]
            if k:
                L[[k, pivot], :k] = L[[pivot, k], :k]
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]
            U[i, k] = 0.0
    return P, L, U

def factorization_residuals():
    A = np.array([[2.0, 1.0, 1.0], [4.0, -6.0, 0.0], [-2.0, 7.0, 2.0]])
    P, L, U = lu_partial_pivoting(A)
    Q, R = np.linalg.qr(A)
    H = np.array([[4.0, 1.0], [1.0, 3.0]])
    C = np.linalg.cholesky(H)
    M = np.array([[3.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    Us, s, Vh = np.linalg.svd(M, full_matrices=False)
    return {
        "lu": np.linalg.norm(P @ A - L @ U),
        "qr": np.linalg.norm(A - Q @ R),
        "orthogonality": np.linalg.norm(Q.T @ Q - np.eye(Q.shape[1])),
        "cholesky": np.linalg.norm(H - C @ C.T),
        "svd": np.linalg.norm(M - Us @ np.diag(s) @ Vh)
    }

if __name__ == "__main__":
    print(factorization_residuals())
