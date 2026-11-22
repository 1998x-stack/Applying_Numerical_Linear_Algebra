"""Independent numerical checks for the eight newly deepened Chapter 6 lessons."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"6_Iterative_Methods_for_Linear_Systems"
STEMS=[
    "6.5_Basic_Iterative_Methods/02_6.5.3_Successive_Overrelaxation",
    "6.5_Basic_Iterative_Methods/03_6.5.4_Convergence_of_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods_on_the_Model_Problem",
    "6.5_Basic_Iterative_Methods/04_6.5.5_Detailed_Convergence_Criteria_for_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods",
    "6.5_Basic_Iterative_Methods/05_6.5.6_Chebyshev_Acceleration_and_Symmetric_SOR_(SSOR)",
    "6.6_Krylov_Subspace_Methods/00_6.6.1_Extracting_Information_about_A_via_Matrix_Vector_Multiplication",
    "6.6_Krylov_Subspace_Methods/01_6.6.2_Solving_Ax_=b_Using_the_Krylov_Subspace_Kk",
    "6.6_Krylov_Subspace_Methods/02_6.6.3_Conjugate_Gradient_Method",
    "6.6_Krylov_Subspace_Methods/03_6.6.4_Convergence_Analysis_of_the_Conjugate_Gradient_Method"
]

def load_module(stem, i):
    path=BASE/(stem+".py")
    spec=importlib.util.spec_from_file_location("ch6_batch4_"+str(i),path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

class Chapter6Batch4Tests(unittest.TestCase):
    def test_all_examples_execute_and_assert(self):
        for i,stem in enumerate(STEMS):
            with self.subTest(stem=stem):
                module=load_module(stem,i)
                result=module.run_case()
                self.assertTrue(result is not None)
    def test_sor_one_sweep_is_gauss_seidel_at_omega_one(self):
        a=np.array([[2.,-1.],[-1.,2.]])
        m=load_module(STEMS[0],0)
        x,_=m.sor(a,np.ones(2),1.0,sweeps=1)
        np.testing.assert_allclose(x,[.5,.75],atol=1e-12)
    def test_model_spectral_radii(self):
        m=load_module(STEMS[1],1)
        j,g,w,s=m.spectral_factors(16)
        self.assertTrue(0<s<g<j<1 and 1<w<2)
    def test_spd_is_not_sufficient_for_jacobi(self):
        m=load_module(STEMS[2],2)
        self.assertAlmostEqual(m.jacobi_radius(2),1.)
        self.assertAlmostEqual(m.jacobi_radius(3),2/3)
    def test_chebyshev_polynomial_is_one_at_zero(self):
        m=load_module(STEMS[3],3)
        v=m.polynomial(np.array([0.]),1.,9.,5)[0]
        self.assertAlmostEqual(float(v),1.)
    def test_krylov_rank_depends_on_initial_vector(self):
        m=load_module(STEMS[4],4)
        a=np.diag([1.,2.,3.,4.])
        self.assertEqual(np.linalg.matrix_rank(m.krylov(a,np.ones(4),4)),4)
        self.assertEqual(np.linalg.matrix_rank(m.krylov(a,np.eye(4)[0],4)),1)
    def test_galerkin_first_step(self):
        m=load_module(STEMS[5],5)
        x,orth=m.solve_projected(np.diag([1.,2.,3.,4.]),np.ones(4),1)
        np.testing.assert_allclose(x,np.full(4,.4),atol=1e-12)
        self.assertLess(orth,1e-12)
    def test_cg_first_step(self):
        m=load_module(STEMS[6],6)
        x,h=m.conjugate_gradient(np.diag([1.,2.,3.,4.]),np.ones(4),maxiter=1)
        np.testing.assert_allclose(x,np.full(4,.4),atol=1e-12)
        self.assertAlmostEqual(float(h[1]),np.sqrt(.8))
    def test_cg_bound_controls_a_norm_not_raw_residual(self):
        m=load_module(STEMS[7],7)
        for k,ratio,bound,res in m.run_case():
            self.assertLessEqual(ratio,bound+1e-10)
            self.assertGreaterEqual(res,0)

if __name__=="__main__":
    unittest.main()
