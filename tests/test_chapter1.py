"""Regression tests for the first eight numerical linear algebra lessons."""
import contextlib
import io
from pathlib import Path
import runpy
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def load(relative):
    with contextlib.redirect_stdout(io.StringIO()):
        return runpy.run_path(str(ROOT / relative))

class ChapterOneTests(unittest.TestCase):
    def test_basic_shapes_and_adjoint(self):
        m = load("1_Introduction/00_1.1_Basic_Notation.py")
        result = m["matrix_shape_demo"]()
        self.assertEqual(result["A_shape"], (2, 3))
        self.assertEqual(result["x_shape"], (3,))
        self.assertEqual(result["Ax_shape"], (2,))
        C = np.array([[1+2j, 3-1j]])
        np.testing.assert_allclose(m["adjoint"](C), C.conj().T)

    def test_standard_problem_residuals(self):
        result = load("1_Introduction/01_1.2_Standard_Problems_of_Numerical_Linear_Algebra.py")["standard_problem_examples"]()
        self.assertLess(result["linear_residual"], 1e-12)
        self.assertLess(result["least_squares_residual"], 2.0)
        self.assertLess(result["eigen_residual"], 1e-12)
        self.assertLess(result["svd_reconstruction"], 1e-12)

    def test_factorization_identities(self):
        result = load("1_Introduction/1.3_General_Techniques/00_1.3.1_Matrix_Factorizations.py")["factorization_residuals"]()
        for key in ("lu", "qr", "orthogonality", "cholesky", "svd"):
            self.assertLess(result[key], 1e-11, key)

    def test_condition_number_grows_for_nearly_dependent_columns(self):
        m = load("1_Introduction/1.3_General_Techniques/01_1.3.2_Perturbation_Theory_and_Condition_Numbers.py")
        k1 = m["matrix_condition_number"]([[1,1],[1,1.01]])
        k2 = m["matrix_condition_number"]([[1,1],[1,1+1e-8]])
        self.assertGreater(k2, k1 * 1e5)
        self.assertGreater(m["first_order_relative_bound"](10, 1e-4, 1e-4), 0)

    def test_roundoff_order_is_not_associative(self):
        m = load("1_Introduction/1.3_General_Techniques/02_1.3.3_Effects_of_Roundoff_Error_on_Algorithms.py")
        left, right = m["reordered_sums"]()
        self.assertEqual(left, 1.0)
        self.assertEqual(right, 0.0)
        self.assertGreater(m["gamma_n"](100), 0)

    def test_performance_estimates(self):
        m = load("1_Introduction/1.3_General_Techniques/03_1.3.4_Analyzing_the_Speed_of_Algorithms.py")
        self.assertEqual(m["matmul_flops"](4), 128)
        self.assertEqual(m["minimum_matrix_bytes"](4), 384)
        self.assertAlmostEqual(m["arithmetic_intensity_lower_bound"](4), 1/3)

    def test_solver_reports_small_backward_error(self):
        m = load("1_Introduction/1.3_General_Techniques/04_1.3.5_Engineering_Numerical_Software.py")
        A = np.array([[3.,1.],[1.,2.]])
        b = np.array([9.,8.])
        x, residual, backward = m["solve_and_validate"](A,b)
        self.assertLess(residual, 1e-12)
        self.assertLess(backward, 1e-14)
        np.testing.assert_allclose(A@x,b)

    def test_horner_direct_condition_and_bisection(self):
        m = load("1_Introduction/03_1.4_Example:_Polynomial_Evaluation.py")
        coeffs = [2, -6, 2, -1]
        self.assertAlmostEqual(m["horner_method"](coeffs,3), 5)
        self.assertAlmostEqual(m["evaluate_polynomial"](coeffs,3), 5)
        self.assertAlmostEqual(m["polynomial_condition_number"](coeffs,3), 23.0)
        self.assertAlmostEqual(m["polynomial_root_bisection"]([1,-2],0,3),2,delta=1e-7)
        self.assertEqual(m["polynomial_root_bisection"]([1,-1],1,3),1)
        with self.assertRaises(ValueError):
            m["polynomial_root_bisection"]([1,0,1],0,3)
        with self.assertRaises(ValueError):
            m["horner_method"]([],2)

if __name__ == "__main__":
    unittest.main()
