"""Reproducible invariants for 2.7.3–3.3 (8 independent deep dives)."""
from __future__ import annotations
from pathlib import Path
import runpy
import unittest
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
B2="2_Linear_Equation_Solving/2.7_Special_Linear_Systems/"
B3="3_Linear_Least_Squares_Problems/"
LS=B3+"3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/"
FILES=[
B2+"02_2.7.3_Band_Matrices.py",
B2+"03_2.7.4_General_Sparse_Matrices.py",
B2+"04_2.7.5_Dense_Matrices_Depending_on_Fewer_Than_O(n²)_Parameters.py",
B3+"00_3.1_Introduction.py",
LS+"00_3.2.1_Normal_Equations.py",
LS+"01_3.2.2_QR_Decomposition.py",
LS+"02_3.2.3_Singular_Value_Decomposition.py",
B3+"02_3.3_Perturbation_Theory_for_the_Least_Squares_Problem.py",
]

def source(i):
    return runpy.run_path(str(ROOT/FILES[i]))

class Chapter23NextNumericalTests(unittest.TestCase):
    def test_273_tridiagonal_reference_solve(self):
        m=source(0)
        for n in (1,2,4,8,17):
            A,lo,d,up=m["tridiagonal_matrix"](n)
            b=A@np.arange(1,n+1,dtype=float)
            x=m["thomas_solve"](lo,d,up,b)
            np.testing.assert_allclose(x,np.linalg.solve(A,b),atol=1e-12,rtol=1e-12)
            self.assertEqual(np.count_nonzero(A),3*n-2)

    def test_273_zero_pivot_requires_other_solver(self):
        f=source(0)["thomas_solve"]
        with self.assertRaises(np.linalg.LinAlgError):
            f([1.],[0.,1.],[1.],[1.,1.])

    def test_273_checks_shapes(self):
        with self.assertRaises(ValueError):
            source(0)["thomas_solve"]([1.,1.],[2.,2.],[1.],[2.,2.])

    def test_274_sparse_star_fill_depends_on_order(self):
        m=source(1)
        x=m["ordering_fill"](6)
        self.assertEqual(x["hub_first"]["nnz_factor"],21)
        self.assertEqual(x["hub_last"]["nnz_factor"],11)
        for v in x.values():
            self.assertLess(v["reconstruction_residual"],1e-12)

    def test_274_csr_roundtrip(self):
        m=source(1)
        A=m["star_spd"](6)
        v,idx,ptr=m["csr_from_dense"](A)
        self.assertEqual(len(ptr),7)
        self.assertEqual(len(v),np.count_nonzero(A))
        B=np.zeros_like(A)
        for i in range(6):
            B[i,idx[ptr[i]:ptr[i+1]]]=v[ptr[i]:ptr[i+1]]
        np.testing.assert_allclose(B,A)

    def test_274_rejects_invalid_star_size(self):
        with self.assertRaises(ValueError):
            source(1)["star_spd"](1)

    def test_275_rank_one_woodbury_hand_solution(self):
        f=source(2)["woodbury_solve"]
        ones=np.ones((4,1))
        d=f(np.ones(4),ones,ones,np.array([1.,0.,0.,0.]))
        np.testing.assert_allclose(d["x"],[.8,-.2,-.2,-.2],atol=1e-12)
        np.testing.assert_allclose(d["small_system"],[[5.]])
        self.assertLess(d["residual"],1e-12)

    def test_275_general_rank_two_matches_direct(self):
        f=source(2)["woodbury_solve"]
        rng=np.random.default_rng(22)
        n=9;k=2
        d=np.linspace(2,4,n)
        U=.2*rng.normal(size=(n,k))
        V=.2*rng.normal(size=(n,k))
        b=rng.normal(size=n)
        got=f(d,U,V,b)
        np.testing.assert_allclose(got["x"],np.linalg.solve(np.diag(d)+U@V.T,b),atol=1e-12)
        self.assertEqual(got["parameter_count"],n+2*n*k)

    def test_275_singular_base_or_small_system(self):
        f=source(2)["woodbury_solve"]
        with self.assertRaises(np.linalg.LinAlgError):
            f([0.],[[1.]],[[-1.]],[1.])
        with self.assertRaises(np.linalg.LinAlgError):
            f([1.],[[1.]],[[-1.]],[1.])

    def test_31_constant_fit_geometry(self):
        f=source(3)["constant_fit"]
        got=f([1.,2.,4.])
        self.assertAlmostEqual(got["constant"],7/3,places=12)
        np.testing.assert_allclose(got["residual"],[-4/3,-1/3,5/3],atol=1e-12)
        self.assertLess(got["orthogonality"],1e-12)
        self.assertAlmostEqual(float(np.dot(got["projection"],got["residual"])),0.,delta=1e-12)

    def test_31_rejects_invalid_observations(self):
        with self.assertRaises(ValueError):
            source(3)["constant_fit"]([])

    def test_321_normal_equations_stationarity(self):
        f=source(4)["normal_equations"]
        A=np.array([[1.,0.],[1.,1.],[1.,2.]])
        b=np.array([1.,2.,2.])
        got=f(A,b)
        np.testing.assert_allclose(got["x"],[7/6,1/2],atol=1e-12)
        np.testing.assert_allclose(got["x"],got["reference"],atol=1e-12)
        self.assertLess(got["stationarity"],1e-12)
        self.assertAlmostEqual(got["condition_gram"],got["condition_A"]**2,delta=1e-10)

    def test_321_rank_deficient_is_not_spd(self):
        with self.assertRaises(np.linalg.LinAlgError):
            source(4)["normal_equations"]([[1.,1.],[2.,2.],[3.,3.]],[1.,2.,3.])

    def test_322_qr_factor_shapes_and_orthogonality(self):
        f=source(5)["thin_qr_least_squares"]
        A=np.array([[1.,0.],[1.,1.],[1.,2.]])
        b=np.array([1.,2.,2.])
        got=f(A,b)
        self.assertEqual(got["Q"].shape,(3,2))
        self.assertEqual(got["R"].shape,(2,2))
        np.testing.assert_allclose(got["x"],[7/6,1/2],atol=1e-12)
        self.assertLess(got["factor_residual"],1e-12)
        self.assertLess(got["orthogonality"],1e-12)
        self.assertLess(got["residual_orthogonality"],1e-12)

    def test_322_reject_rank_deficiency(self):
        with self.assertRaises(np.linalg.LinAlgError):
            source(5)["thin_qr_least_squares"]([[1.,1.],[2.,2.],[3.,3.]],[1.,2.,3.])

    def test_323_svd_minimum_norm_and_rank(self):
        f=source(6)["svd_minimum_norm"]
        A=np.array([[1.,1.],[2.,2.],[3.,3.]])
        b=np.array([1.,2.,3.])
        got=f(A,b)
        self.assertEqual(got["rank"],1)
        np.testing.assert_allclose(got["x"],[.5,.5],atol=1e-12)
        self.assertLess(got["residual"],1e-12)
        self.assertLess(got["reconstruction"],1e-12)
        # For the solution family (t, 1-t), (1/2, 1/2) is min-norm.
        self.assertLess(np.linalg.norm(got["x"]),np.linalg.norm([1.,0.]))

    def test_323_svd_full_rank_reference(self):
        f=source(6)["svd_minimum_norm"]
        A=np.array([[1.,0.],[1.,1.],[1.,2.]])
        b=np.array([1.,2.,2.])
        got=f(A,b)
        self.assertEqual(got["rank"],2)
        np.testing.assert_allclose(got["x"],np.linalg.lstsq(A,b,rcond=None)[0],atol=1e-12)

    def test_323_svd_cutoff_and_bad_input(self):
        f=source(6)["svd_minimum_norm"]
        self.assertEqual(f(np.diag([1.,1e-8]),np.ones(2),rcond=1e-6)["rank"],1)
        with self.assertRaises(ValueError):
            f(np.eye(2),np.ones(2),rcond=-1)

    def test_33_nonzero_residual_changes_sensitivity(self):
        f=source(7)["residual_amplification"]
        clean=f(r3=0.)
        noisy=f(r3=1.)
        self.assertLess(abs(clean["observed_x2_change"]),1e-6)
        self.assertGreater(noisy["observed_x2_change"],.009)
        self.assertAlmostEqual(noisy["perturbed"][1],noisy["analytic_x2"],delta=1e-12)
        self.assertAlmostEqual(noisy["observed_x2_change"],noisy["first_order_x2_change"],delta=1e-6)

    def test_33_input_validation(self):
        with self.assertRaises(ValueError):
            source(7)["residual_amplification"](delta=0)

    def test_article_pairs_visuals_and_evidence(self):
        for index,py in enumerate(FILES,25):
            stem=(ROOT/py).with_suffix("")
            md=Path(str(stem)+".md")
            html=Path(str(stem)+".html")
            # Path.with_suffix fails for original names like "02_2.7.3_..." only
            # because suffix is the last period after extension? Here py ends .py,
            # so changing .py to .md/.html is safe.
            self.assertTrue(md.is_file(),str(md))
            self.assertTrue(html.is_file(),str(html))
            markup=html.read_text(encoding="utf-8")
            self.assertIn("<math display=",markup)
            self.assertIn("data-next-lab=",markup)
            self.assertIn("data-next-slider",markup)
            self.assertIn(f"{index}-next.svg",markup)
            self.assertGreaterEqual(md.read_text(encoding="utf-8").count("## "),6)
            self.assertTrue((ROOT/"evidence"/f"{index}.json").is_file())

if __name__=="__main__":
    unittest.main()
