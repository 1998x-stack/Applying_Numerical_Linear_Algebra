"""Floating-point examples: non-associativity, unit roundoff and error bounds."""
import math
import numpy as np

def unit_roundoff(dtype=np.float64):
    """For round-to-nearest binary formats, u is half the spacing at 1."""
    return float(np.finfo(dtype).eps / 2.0)

def reordered_sums():
    large = 1e16
    left_associated = (large + (-large)) + 1.0
    right_associated = large + ((-large) + 1.0)
    return left_associated, right_associated

def gamma_n(n, u=None):
    if n < 0:
        raise ValueError("n must be nonnegative")
    u = unit_roundoff() if u is None else float(u)
    if n * u >= 1:
        raise ValueError("n*u must be smaller than 1")
    return n * u / (1.0 - n * u)

def normalized_backward_error(A, x, b):
    A, x, b = np.asarray(A), np.asarray(x), np.asarray(b)
    numerator = np.linalg.norm(A @ x - b)
    denominator = np.linalg.norm(A) * np.linalg.norm(x) + np.linalg.norm(b)
    return float(numerator / denominator) if denominator else float(numerator)

if __name__ == "__main__":
    print("binary64 unit roundoff:", unit_roundoff())
    print("left/right association:", reordered_sums())
    print("gamma_100:", gamma_n(100))
