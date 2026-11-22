"""Independent numerical regression tests for the eight Chapter 6 modules.

Only the Python standard library is needed to run these checks.
"""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "6_Iterative_Methods_for_Linear_Systems/"
POISSON = BASE + "6.3_Poisson’s_Equation/"
BASIC = BASE + "6.5_Basic_Iterative_Methods/"


def load_module(relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(path.name.replace(".", "_"), path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class IterativeMethodsTests(unittest.TestCase):
    def test_stopping_rule_uses_relative_and_absolute_tolerance(self):
        module = load_module(BASE + "00_6.1_Introduction.py")
        self.assertTrue(module.meets_stopping_rule(1e-8, 1.0, rtol=1e-6, atol=1e-12))
        self.assertFalse(module.meets_stopping_rule(1e-4, 1.0, rtol=1e-6, atol=1e-12))
        self.assertTrue(module.meets_stopping_rule(5e-13, 0.0, rtol=1e-6, atol=1e-12))
        with self.assertRaises(ValueError):
            module.meets_stopping_rule(-1, 1)

    def test_solver_advice_respects_matrix_structure(self):
        module = load_module(BASE + "01_6.2_On_line_Help_for_Iterative_Methods.py")
        for structure, expected in [
            ("spd", "CG"), ("symmetric-indefinite", "MINRES"),
            ("nonsymmetric", "GMRES"), ("least-squares", "LSQR")
        ]:
            self.assertIn(expected, module.recommend_solver(structure))
        with self.assertRaises(ValueError):
            module.recommend_solver("unknown")

    def test_one_dimensional_poisson_stencil(self):
        module = load_module(POISSON + "00_6.3.1_Poisson’s_Equation_in_One_Dimension.py")
        result = module.apply_poisson_1d([0.0, 1.0, 0.0], h=0.5)
        self.assertEqual(result, [-4.0, 8.0, -4.0])
        with self.assertRaises(ValueError):
            module.apply_poisson_1d([1.0], h=0.0)

    def test_two_dimensional_operator_cross_check_with_kronecker_sum(self):
        stencil = load_module(POISSON + "01_6.3.2_Poisson’s_Equation_in_Two_Dimensions.py")
        kron = load_module(POISSON + "02_6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products.py")
        for grid, hx, hy in [
            ([[0.0, 1.0, 0.5], [2.0, 3.0, 1.0], [1.0, 0.0, 4.0]], 0.25, 0.5),
            ([[2.0, 3.0], [-1.0, 0.0], [2.0, -2.0], [3.0, 0.5]], 0.2, 0.33),
            ([[1.0]], 1.0, 1.0),
        ]:
            direct = stencil.apply_poisson_2d(grid, hx, hy)
            structured = kron.apply_kronecker_sum(grid, hx, hy)
            for row_a, row_b in zip(direct, structured):
                for a, b in zip(row_a, row_b):
                    self.assertAlmostEqual(a, b, delta=1e-12)

    def test_algorithm_comparison_names_the_assumptions(self):
        module = load_module(BASE + "03_6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation.py")
        methods = module.method_summary()
        names = {item["method"] for item in methods}
        self.assertTrue({"Jacobi", "Gauss–Seidel", "CG", "FFT", "Multigrid"} <= names)
        fft = next(item for item in methods if item["method"] == "FFT")
        self.assertIn("separable", fft["assumptions"].lower())

    def test_jacobi_and_gauss_seidel_reduce_residual(self):
        jacobi = load_module(BASIC + "00_6.5.1_Jacobi’s_Method.py")
        gs = load_module(BASIC + "01_6.5.2_Gauss–Seidel_Method.py")
        b = [1.0] * 16
        _, jacobi_history = jacobi.jacobi_1d(len(b), b, steps=20)
        _, gs_history = gs.gauss_seidel_1d(len(b), b, steps=20)
        self.assertEqual(len(jacobi_history), 21)
        self.assertEqual(len(gs_history), 21)
        self.assertLess(jacobi_history[-1], jacobi_history[0])
        self.assertLess(gs_history[-1], gs_history[0])
        self.assertLess(gs_history[-1], jacobi_history[-1])

    def test_zero_rhs_stays_zero(self):
        jacobi = load_module(BASIC + "00_6.5.1_Jacobi’s_Method.py")
        gs = load_module(BASIC + "01_6.5.2_Gauss–Seidel_Method.py")
        for solve in [jacobi.jacobi_1d, gs.gauss_seidel_1d]:
            x, residuals = solve(4, [0.0] * 4, steps=8)
            self.assertEqual(x, [0.0] * 4)
            self.assertTrue(all(r == 0 for r in residuals))


if __name__ == "__main__":
    unittest.main()
