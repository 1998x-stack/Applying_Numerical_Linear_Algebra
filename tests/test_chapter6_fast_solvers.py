"""Regression checks for the eight fast Chapter 6 deep dives."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path
import numpy as np

BASE=Path(__file__).resolve().parents[1]/"6_Iterative_Methods_for_Linear_Systems"
STEMS=[
  "6.6_Krylov_Subspace_Methods/04_6.6.5_Preconditioning",
  "6.6_Krylov_Subspace_Methods/05_6.6.6_Other_Krylov_Subspace_Algorithms_for_Solving_Ax_=b",
  "6.7_Fast_Fourier_Transform/00_6.7.1_The_Discrete_Fourier_Transform",
  "6.7_Fast_Fourier_Transform/01_6.7.2_Solving_the_Continuous_Model_Problem_Using_Fourier_Series",
  "6.7_Fast_Fourier_Transform/02_6.7.3_Convolutions",
  "6.7_Fast_Fourier_Transform/03_6.7.4_Computing_the_Fast_Fourier_Transform",
  "07_6.8_Block_Cyclic_Reduction",
  "6.9_Multigrid/00_6.9.1_Overview_of_Multigrid_on_Two_Dimensional_Poisson’s_Equation"
]
def load(stem):
    path=BASE/(stem+".py")
    spec=importlib.util.spec_from_file_location("ch6_fast_"+stem.split("/")[-1].replace(".","_"),path)
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

class FastSolverLessonTests(unittest.TestCase):
    def test_every_example_runs(self):
        for stem in STEMS:
            with self.subTest(stem=stem):
                self.assertIsNotNone(load(stem).run_case())
    def test_preconditioner_changes_spectrum(self):
        f=load(STEMS[0])
        A=np.diag([1.,100.,4.,400.])
        x,h=f.pcg(A,np.ones(4),np.diag(A))
        self.assertLess(h[-1],1e-12)
        np.testing.assert_allclose(x,np.linalg.solve(A,np.ones(4)))
    def test_gmres_real_residual_monotone_for_full_method(self):
        f=load(STEMS[1])
        A=np.array([[3.,1.,0.],[0.,2.,1.],[0.,0.,1.]])
        x,h=f.gmres_history(A,np.array([1.,2.,3.]))
        self.assertTrue(np.all(np.diff(h)<=1e-10))
        self.assertLess(h[-1],1e-10)
    def test_dft_parseval(self):
        f=load(STEMS[2])
        x=np.array([1.,2.,0.,0.])
        X=f.direct_dft(x)
        self.assertAlmostEqual(float(np.vdot(X,X).real/4),5.)
    def test_sine_mode_discretization_converges(self):
        f=load(STEMS[3])
        e7,_=f.poisson_sine_mode(7)
        e15,_=f.poisson_sine_mode(15)
        self.assertGreater(e7/e15,3.)
    def test_circular_aliasing_requires_padding(self):
        f=load(STEMS[4]); a=np.array([1.,2.,1.]);b=np.array([1.,-1.])
        self.assertFalse(np.allclose(f.fft_convolution(a,b,3),np.array([1,1,-1])))
        np.testing.assert_allclose(f.fft_convolution(a,b,4).real,np.convolve(a,b))
    def test_fft_matches_direct_definition(self):
        f=load(STEMS[5]); x=np.arange(8)
        np.testing.assert_allclose(f.fft_radix2(x),np.fft.fft(x))
    def test_bcr_schur_complement_retains_solution(self):
        f=load(STEMS[6]); A=f.block_poisson(3);b=np.arange(9,dtype=float)
        x,S=f.eliminate_odd_block_rows(A,b,3,3)
        self.assertEqual(S.shape,(3,3))
        self.assertLess(np.linalg.norm(A@x-b),1e-9)
    def test_two_grid_correction_reduces_residual(self):
        f=load(STEMS[7]);n=7;h=1/8
        v=np.sin(np.pi*h*np.arange(1,8))
        b=f.apply_a(np.outer(v,v),h)
        _,before,after=f.two_grid(b)
        self.assertLess(after,before/3)
        self.assertEqual(f.prolong_bilinear(np.ones((3,3))).shape,(7,7))

if __name__=="__main__":unittest.main()
