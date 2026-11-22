"""Conservative solver recommendations based on matrix structure."""
from __future__ import annotations

ADVICE = {
    "spd": "CG: verify symmetry/Hermitian positive definiteness; evaluate a suitable SPD preconditioner.",
    "symmetric-indefinite": "MINRES: verify symmetry and inspect singular/near-singular behavior and preconditioner requirements.",
    "nonsymmetric": "GMRES or BiCGSTAB: inspect restart, memory, preconditioning and the true residual.",
    "least-squares": "LSQR or LSMR: solve the rectangular least-squares problem directly.",
}


def recommend_solver(problem: str) -> str:
    """Return a candidate and its key caveat; this is not a convergence guarantee."""
    try:
        return ADVICE[problem]
    except KeyError as exc:
        raise ValueError(f"unknown problem structure: {problem!r}") from exc


if __name__ == "__main__":
    for kind in ADVICE:
        print(f"{kind}: {recommend_solver(kind)}")
