"""Regression tests for the polynomial bisection tutorial."""
import contextlib
import io
from pathlib import Path
import runpy
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "1_Introduction" / "03_1.4_Example:_Polynomial_Evaluation.py"
with contextlib.redirect_stdout(io.StringIO()):
    bisect = runpy.run_path(str(SOURCE))["polynomial_root_bisection"]


class BisectionTests(unittest.TestCase):
    def test_interior_root(self):
        self.assertAlmostEqual(bisect([1, -2], 0, 3), 2, delta=1e-7)

    def test_endpoint_root(self):
        self.assertEqual(bisect([1, -1], 1, 3), 1)
        self.assertEqual(bisect([1, -3], 0, 3), 3)

    def test_negative_interval(self):
        self.assertAlmostEqual(bisect([1, 0, -4], -3, -1), -2, delta=1e-7)

    def test_invalid_bracket_and_parameters(self):
        for args in (([1, 0, 1], 0, 3), ([1, -1], 3, 1), ([1, -1], 0, 3, 0)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                bisect(*args)


if __name__ == "__main__":
    unittest.main()
