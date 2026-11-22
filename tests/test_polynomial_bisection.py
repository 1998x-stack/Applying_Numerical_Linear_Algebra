"""Regression tests for polynomial bisection and coefficient ordering."""
import contextlib
import io
from pathlib import Path
import runpy
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "1_Introduction" / "03_1.4_Example:_Polynomial_Evaluation.py"
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(SOURCE))
bisect = ns["polynomial_root_bisection"]
condition = ns["polynomial_condition_number"]

class BisectionTests(unittest.TestCase):
    def test_interior_endpoint_and_negative_roots(self):
        self.assertAlmostEqual(bisect([1,-2],0,3),2,delta=1e-7)
        self.assertEqual(bisect([1,-1],1,3),1)
        self.assertEqual(bisect([1,-3],0,3),3)
        self.assertAlmostEqual(bisect([1,0,-4],-3,-1),-2,delta=1e-7)

    def test_invalid_bracket_and_parameters(self):
        for args in (([1,0,1],0,3),([1,-1],3,1),([1,-1],0,3,0),([],0,1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                bisect(*args)

    def test_condition_number_uses_descending_coefficient_powers(self):
        # p(x)=2x^3-6x^2+2x-1; at x=3, sum |a_i||x|^(3-i)=115 and |p(3)|=5.
        self.assertAlmostEqual(condition([2,-6,2,-1],3),23.0)

if __name__ == "__main__":
    unittest.main()
