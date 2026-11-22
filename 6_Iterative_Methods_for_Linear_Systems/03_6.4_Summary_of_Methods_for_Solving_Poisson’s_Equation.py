"""Qualitative and model-specific comparison of Poisson solvers."""
from __future__ import annotations


def method_summary() -> list[dict[str, str]]:
    """Return textbook model-problem orders with explicit assumptions.

    Here n=N^2 is the number of unknowns on a two-dimensional regular grid.
    The time orders assume a fixed error target and a serial cost model; they
    are not measured timings or universal complexity guarantees.
    """
    return [
        {"method": "Jacobi", "time": "O(n^2)", "space": "O(n)",
         "assumptions": "regular 2D Poisson model; simple stationary baseline; slow low-frequency error reduction"},
        {"method": "Gauss–Seidel", "time": "O(n^2)", "space": "O(n)",
         "assumptions": "regular 2D Poisson model; update ordering affects convergence and parallelism"},
        {"method": "CG", "time": "O(n^(3/2))", "space": "O(n)",
         "assumptions": "symmetric positive-definite model; Krylov convergence depends on conditioning"},
        {"method": "SOR", "time": "O(n^(3/2))", "space": "O(n)",
         "assumptions": "model-compatible ordering and relaxation parameter are required"},
        {"method": "FFT", "time": "O(n log n)", "space": "O(n)",
         "assumptions": "constant-coefficient separable rectangular Poisson operator with compatible boundaries"},
        {"method": "Multigrid", "time": "O(n)", "space": "O(n)",
         "assumptions": "elliptic model with effective smoothing, restriction, prolongation and coarse-grid solve"},
    ]


if __name__ == "__main__":
    for item in method_summary():
        print(f"{item['method']:14s} time {item['time']:12s} space {item['space']}: {item['assumptions']}")
