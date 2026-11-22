"""Chapter 2 (eight standalone lessons) independent numerical regression tests."""
from __future__ import annotations
from pathlib import Path
import runpy
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
BASE = "2_Linear_Equation_Solving/"
FILES = [
"00_2.1_Introduction.py",
"01_2.2_Perturbation_Theory.py",
"02_2.2.1_Relative_Perturbation_Theory.py",
"03_2.3_Gaussian_Elimination.py",
"2.4_Error_Analysis/00_2.4.1_The_Need_for_Pivoting.py",
"2.4_Error_Analysis/01_2.4.2_Formal_Error_Analysis_of_Gaussian_Elimination.py",
"2.4_Error_Analysis/02_2.4.3_Estimating_Condition_Numbers.py",
"2.4_Error_Analysis/03_2.4.4_Practical_Error_Bounds.py",
]

def namespace(index):
    return runpy.run_path(str(ROOT / BASE / FILES[index]))

class LinearSystemsDeepDiveTests(unittest.TestCase):
    def test_21_solver_residual_and_solution(self):
        ans=namespace(0)["solve_with_diagnostics"]([[3,1],[1,2]],[9,8])
        np.testing.assert_allclose(ans["x"],[2,3],atol=1e-12)
        self.assertLess(ans["residual"],1e-12)
        self.assertLess(ans["backward_error"],1e-12)
        self.assertGreater(ans["condition_2"],1)

    def test_21_rejects_shape_errors(self):
        with self.assertRaises(ValueError):
            namespace(0)["solve_with_diagnostics"]([[1,2,3]], [1])

    def test_22_perturbation_identity_and_bound(self):
        A=np.diag([2.,1.]); b=np.array([2.,1.])
        dA=np.diag([1e-7,-1e-7]); db=np.array([0.,1e-6])
        ans=namespace(1)["perturbation_bound"](A,b,dA,db)
        self.assertLess(ans["identity_residual"],1e-12)
        self.assertLessEqual(ans["actual"],ans["bound"]+1e-12)

    def test_22_refuses_to_use_bound_outside_assumption(self):
        A=np.diag([100.,1.]); b=np.array([100.,1.])
        with self.assertRaises(ValueError):
            namespace(1)["perturbation_bound"](A,b,np.diag([0.,2.]),np.zeros(2))

    def test_221_componentwise_bound_not_normwise_cond(self):
        fn=namespace(2)["diagonal_componentwise_demo"]
        for gamma in (1e2,1e6,1e8):
            x=fn(gamma,1e-6)
            self.assertAlmostEqual(x["condition_2"],gamma,delta=gamma*1e-10)
            self.assertLessEqual(x["componentwise_relative_error"],x["componentwise_bound"]+1e-12)

    def test_23_partial_pivoted_lu_and_linear_solve(self):
        A=np.array([[0.,2.,1.],[1.,3.,2.],[2.,0.,2.]])
        b=A@np.array([1.,2.,3.])
        fn=namespace(3)
        P,L,U=fn["lu_partial_pivoting"](A)
        np.testing.assert_allclose(P@A,L@U,atol=1e-12)
        np.testing.assert_allclose(np.diag(L),np.ones(3))
        self.assertAlmostEqual(np.linalg.norm(np.tril(U,-1)),0.,delta=1e-12)
        result=fn["solve_from_lu"](A,b)
        np.testing.assert_allclose(result["x"],[1,2,3],atol=1e-12)

    def test_23_reject_singular_matrix(self):
        with self.assertRaises(np.linalg.LinAlgError):
            namespace(3)["lu_partial_pivoting"]([[1.,2.],[2.,4.]])

    def test_241_multiplier_reduction_and_reference_solution(self):
        fn=namespace(4)["pivot_multiplier_example"]
        a=fn(1e-4)
        self.assertEqual(a["multiplier_without"],1e4)
        self.assertAlmostEqual(a["multiplier_with"],1e-4)
        np.testing.assert_allclose(a["solution"],[1.,1.],atol=1e-12)

    def test_242_wilkinson_growth_factor(self):
        funcs=namespace(5)
        for n in (2,3,4,5):
            self.assertAlmostEqual(funcs["growth_factor"](funcs["wilkinson_matrix"](n)),2**(n-1),delta=1e-12)

    def test_242_reject_invalid_input(self):
        with self.assertRaises(ValueError):
            namespace(5)["growth_factor"](np.zeros((3,3)))

    def test_243_condition_by_basis_solve(self):
        fn=namespace(6)["one_norm_condition_from_basis_solves"]
        for A in [np.eye(3),np.diag([1.,1e-6]),np.array([[4.,2.],[1.,3.]])]:
            self.assertAlmostEqual(fn(A),np.linalg.cond(A,p=1),delta=1e-8)

    def test_244_forward_bound_and_componentwise_berr(self):
        fn=namespace(7)["practical_error_metrics"]
        A=np.array([[3.,1.],[1.,2.]])
        b=np.array([9.,8.])
        result=fn(A,b,np.array([2.001,2.999]))
        self.assertLessEqual(result["actual_error_reference"],result["forward_bound"]+1e-12)
        self.assertGreater(result["berr"],0.)
        self.assertLess(result["berr"],0.001)

    def test_244_exact_solution_has_zero_or_small_error(self):
        fn=namespace(7)["practical_error_metrics"]
        A=np.eye(2); b=np.array([1.,2.])
        result=fn(A,b,b)
        self.assertEqual(result["berr"],0.)
        self.assertEqual(result["forward_bound"],0.)

if __name__=="__main__":
    unittest.main()
