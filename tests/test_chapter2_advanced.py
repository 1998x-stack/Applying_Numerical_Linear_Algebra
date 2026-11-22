"""Numerical assertions for the eight Chapter 2 advanced visual lessons."""
from __future__ import annotations
from pathlib import Path
import runpy
import unittest
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
P5="2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/"
P6="2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/"
P7="2_Linear_Equation_Solving/2.7_Special_Linear_Systems/"
PATHS=[
P5+"00_2.5.1_Single_Precision_Iterative_Refinement.py",
P5+"01_2.5.2_Equilibration.py",
P6+"00_2.6.1_Basic_Linear_Algebra_Subroutines_(BLAS).py",
P6+"01_2.6.2_How_to_Optimize_Matrix_Multiplication.py",
P6+"02_2.6.3_Reorganizing_Gaussian_Elimination_to_use_Level_3_BLAS.py",
P6+"03_2.6.4_More_About_Parallelism_and_Other_Performance_Issues.py",
P7+"00_2.7.1_Real_Symmetric_Positive_Definite_Matrices.py",
P7+"01_2.7.2_Symmetric_Indefinite_Matrices.py",
]
def lesson(i):
    return runpy.run_path(str(ROOT/PATHS[i]))

class AdvancedNumericalLinearAlgebraTests(unittest.TestCase):
    def test_251_mixed_precision_reduces_backward_error(self):
        A=np.array([[1.,1.],[1.,1.001]])
        b=A@np.ones(2)
        d=lesson(0)["refine_mixed_precision"](A,b,5)
        self.assertGreaterEqual(len(d["backward_errors"]),2)
        self.assertLessEqual(d["backward_errors"][-1],d["backward_errors"][0]+1e-13)
        np.testing.assert_allclose(d["x"],np.ones(2),atol=2e-9)

    def test_251_mixed_precision_rejects_bad_input(self):
        f=lesson(0)["refine_mixed_precision"]
        with self.assertRaises(ValueError):
            f([[1.,2.]],np.ones(2))
        with self.assertRaises(ValueError):
            f(np.eye(2),np.ones(2),-1)

    def test_252_equilibration_preserves_original_solution(self):
        A=np.diag([1e6,1.])
        b=A@np.array([2.,3.])
        d=lesson(1)["equilibrate_and_solve"](A,b)
        np.testing.assert_allclose(d["x"],[2.,3.],atol=1e-12)
        np.testing.assert_allclose(d["scaled_A"],d["R"][:,None]*A*d["C"][None,:],atol=1e-12)
        self.assertLess(d["condition_scaled"],d["condition_original"])
        self.assertLess(d["original_residual"],1e-9)

    def test_252_near_dependent_not_fixed_by_scaling(self):
        A=np.array([[1.,1.],[1.,1+1e-8]])
        d=lesson(1)["equilibrate_and_solve"](A,A@np.ones(2))
        self.assertGreater(d["condition_scaled"],1e6)

    def test_252_zero_row_fails_cleanly(self):
        with self.assertRaises(np.linalg.LinAlgError):
            lesson(1)["equilibrate_and_solve"]([[1.,2.],[0.,0.]],[1.,0.])

    def test_261_blas_intensity_uses_read_write_C(self):
        f=lesson(2)["intensity_models"]
        for n in (16,64,128):
            d=f(n)
            self.assertAlmostEqual(d["axpy"]["intensity"],1/12)
            self.assertAlmostEqual(d["gemm"]["intensity"],n/16)
            self.assertEqual(d["gemm"]["bytes"],32*n*n)
            self.assertEqual(d["gemm"]["flops"],2*n**3)
            self.assertLess(d["gemv"]["intensity"],0.25)
        with self.assertRaises(ValueError):
            f(0)

    def test_261_blas_example_shapes(self):
        d=lesson(2)["check_blas_equivalents"](5)
        self.assertEqual(d["axpy"].shape,(5,))
        self.assertEqual(d["gemv"].shape,(5,))
        self.assertEqual(d["gemm"].shape,(5,5))
        a=np.arange(1,26,dtype=float).reshape(5,5)
        np.testing.assert_allclose(d["gemm"],2*a)

    def test_262_blocked_gemm_tail_and_rectangular(self):
        f=lesson(3)["blocked_gemm"]
        rng=np.random.default_rng(4)
        A=rng.normal(size=(7,5));B=rng.normal(size=(5,6))
        for b in (1,2,3,4,10):
            np.testing.assert_allclose(f(A,B,b),A@B,rtol=1e-12,atol=1e-12)

    def test_262_blocked_gemm_rejects_bad_geometry(self):
        f=lesson(3)["blocked_gemm"]
        with self.assertRaises(ValueError):
            f(np.eye(3),np.eye(2),2)
        with self.assertRaises(ValueError):
            f(np.eye(3),np.eye(3),0)

    def test_263_schur_reconstructs_input(self):
        f=lesson(4)["block_schur_step"]
        A=np.array([[4.,1.,1.,0.],[1.,3.,0.,1.],[1.,0.,3.,1.],[0.,1.,1.,4.]])
        for b in (1,2,3):
            d=f(A,b)
            self.assertLess(d["reconstruction_error"],1e-12)
            self.assertGreater(np.linalg.eigvalsh(d["schur"]).min(),0.)
            self.assertEqual(d["update_flops_model"],2*(4-b)**2*b)

    def test_263_schur_rejects_invalid_panel(self):
        f=lesson(4)["block_schur_step"]
        with self.assertRaises(ValueError):
            f(np.eye(3),3)

    def test_264_roofline_memory_and_compute_roofs(self):
        f=lesson(5)["roofline"]
        self.assertEqual([f(200,50,k) for k in (1,2,4,8)],[50,100,200,200])
        with self.assertRaises(ValueError):
            f(200,50,-1)

    def test_264_amdahl_limits(self):
        f=lesson(5)["amdahl"]
        self.assertAlmostEqual(f(.2,4),2.5)
        self.assertEqual(f(.2,1),1.)
        self.assertLess(f(.2,1000),5)
        with self.assertRaises(ValueError):
            f(.3,0)

    def test_271_cholesky_reconstruction_and_solve(self):
        f=lesson(6)["cholesky_solve"]
        A=np.array([[4.,2.],[2.,3.]])
        x=np.array([1.,2.]);b=A@x
        d=f(A,b)
        np.testing.assert_allclose(d["x"],x,atol=1e-12)
        np.testing.assert_allclose(d["L"]@d["L"].T,A,atol=1e-12)
        np.testing.assert_allclose(np.triu(d["L"],1),0.,atol=1e-12)

    def test_271_rejects_indefinite_and_non_symmetric(self):
        f=lesson(6)["cholesky_solve"]
        with self.assertRaises(np.linalg.LinAlgError):
            f([[0.,1.],[1.,0.]],[1.,2.])
        with self.assertRaises(ValueError):
            f([[1.,2.],[0.,1.]],[1.,2.])

    def test_272_two_by_two_indefinite_pivot(self):
        f=lesson(7)["indefinite_2x2"]
        for t in (-3.,-1.,0.,1.,3.):
            d=f(t)
            self.assertLess(d["eigenvalues"][0],0)
            self.assertGreater(d["eigenvalues"][1],0)
            self.assertAlmostEqual(d["determinant"],-1.,places=12)
            np.testing.assert_allclose(d["eigenvalues"],d["analytic_eigenvalues"],atol=1e-12)
            np.testing.assert_allclose(d["A"],d["L"]@d["D"]@d["L"].T,atol=1e-12)
            self.assertLess(d["residual"],1e-12)

    def test_272_indefinite_does_not_admit_spd_cholesky(self):
        with self.assertRaises(np.linalg.LinAlgError):
            np.linalg.cholesky(lesson(7)["indefinite_2x2"](0.)["A"])

    def test_advanced_html_has_mathml_visual_and_live_experiment(self):
        from html.parser import HTMLParser
        for i,path in enumerate(PATHS,17):
            h=(ROOT/path).with_suffix(".html").read_text(encoding="utf-8")
            m=(ROOT/path).with_suffix(".md").read_text(encoding="utf-8")
            self.assertIn("<math display=",h)
            self.assertIn("data-advanced-lab=",h)
            self.assertIn("data-lab-slider",h)
            self.assertIn(f"{i}-advanced.svg",h)
            self.assertGreater(m.count("## "),6)
            self.assertIn("## 参考来源",m)

if __name__=="__main__":
    unittest.main()
