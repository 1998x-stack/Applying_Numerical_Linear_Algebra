"""Fresh Chapter 6/3 numerical regressions, Markdown/HTML parity and evidence checks."""
import importlib.util
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
STEMS=[
  "6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/01_6.9.2_Detailed_Description_of_Multigrid_on_One_Dimensional_Poisson’s_Equation",
  "6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/00_6.10.1_Nonoverlapping_Methods",
  "6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/01_6.10.2_Overlapping_Methods",
  "3_Linear_Least_Squares_Problems/00_3.1_Introduction",
  "3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/00_3.2.1_Normal_Equations",
  "3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/01_3.2.2_QR_Decomposition",
  "3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/02_3.2.3_Singular_Value_Decomposition",
  "3_Linear_Least_Squares_Problems/02_3.3_Perturbation_Theory_for_the_Least_Squares_Problem"
]

class PageChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1=0; self.main=0; self.svg=0;self.math=0;self.demo=0;self.live=0;self.external=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=="h1":self.h1+=1
        if tag=="main":self.main+=1
        if tag=="svg":self.svg+=1
        if tag=="math":self.math+=1
        if "data-demo-control" in d:self.demo+=1
        if "data-demo-output" in d:self.live+=1
        if tag in {"script","link","img"}:
            url=d.get("src") or d.get("href") or ""
            if url.startswith(("https://","http://")):self.external.append(url)

def load(stem):
    path=ROOT/(stem+".py")
    name="lesson_"+re.sub(r"[^a-zA-Z0-9_]", "_",stem)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class NewCourseBatchTests(unittest.TestCase):
    def test_all_eight_python_numerical_examples(self):
        for stem in STEMS:
            with self.subTest(stem=stem):
                result=load(stem).run_case()
                self.assertIsNotNone(result)
    def test_all_companion_files_and_source_claims(self):
        for stem in STEMS:
            with self.subTest(stem=stem):
                for extension in (".html",".md",".py",".m",".evidence.json"):
                    self.assertTrue((ROOT/(stem+extension)).is_file())
                data=json.loads((ROOT/(stem+".evidence.json")).read_text(encoding="utf-8"))
                self.assertGreaterEqual(len(data["claims"]),3)
                for item in data["claims"]:
                    for key in ("id","claim","kind","source_url","locator","status","notes"):
                        self.assertTrue(item[key])
    def test_offline_accessibility_and_heading_parity(self):
        for stem in STEMS:
            with self.subTest(stem=stem):
                html=(ROOT/(stem+".html")).read_text(encoding="utf-8")
                md=(ROOT/(stem+".md")).read_text(encoding="utf-8")
                parser=PageChecker();parser.feed(html)
                self.assertEqual(parser.h1,1)
                self.assertEqual(parser.main,1)
                self.assertGreaterEqual(parser.svg,1)
                self.assertGreaterEqual(parser.math,1)
                self.assertGreaterEqual(parser.demo,1)
                self.assertGreaterEqual(parser.live,1)
                self.assertFalse(parser.external)
                self.assertGreater(len(md),1200)
                h1=re.search(r"<h1[^>]*>(.*?)</h1>",html,re.S)
                self.assertIsNotNone(h1)
                self.assertEqual(re.search(r"^# (.+)$",md,re.M).group(1),h1.group(1))
                self.assertNotIn("mathjax",html.lower())
    def test_geometric_vcycle_residual_and_galerkin(self):
        f=load(STEMS[0]);A=f.lap(15)
        xstar=np.sin(np.pi*np.arange(1,16)/16)
        b=A@xstar
        x=f.vcycle(A,b)
        self.assertLess(np.linalg.norm(b-A@x),np.linalg.norm(b)/4)
        k=7;P=np.column_stack([f.prolong(np.eye(k)[:,i]) for i in range(k)])
        np.testing.assert_allclose((P.T/2)@A@P,f.lap(k))
    def test_schur_and_schwarz_structure(self):
        s=load(STEMS[1]);d=load(STEMS[2]);n=5
        A=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
        x,S=s.schur_solve(A,np.arange(1.,6.),[0,1,3,4],[2])
        np.testing.assert_allclose(S,[[2/3]],atol=1e-12)
        self.assertLess(np.linalg.norm(A@x-np.arange(1.,6.)),1e-10)
        n=7;A=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
        B=d.additive_schwarz(A,[range(5),range(2,7)])
        self.assertGreater(np.linalg.eigvalsh(B).min(),0)
        self.assertLess(max(abs(1-0.5*np.linalg.eigvals(B@A).real)),1)
    def test_projected_fit_and_svd_minimum_norm(self):
        f=load(STEMS[3]);x,r,A=f.fit_line([1,2,2])
        np.testing.assert_allclose(x,[7/6,.5])
        np.testing.assert_allclose(A.T@r,np.zeros(2),atol=1e-12)
        d=load(STEMS[6])
        A=np.array([[1.,1.],[2.,2.],[3.,3.]])
        x,s=d.svd_min_norm(A,np.array([1.,2.,2.]))
        np.testing.assert_allclose(x,[11/28,11/28])
        self.assertLess(s[-1],1e-12)
    def test_conditioning_qr_and_perturbation(self):
        f=load(STEMS[4]);A,c,cc=f.test_condition(1e-3)
        self.assertAlmostEqual(cc/c**2,1,places=5)
        q=load(STEMS[5]);A=np.array([[1.,0.],[1.,1.],[1.,2.]])
        x,Q,R=q.qr_lstsq(A,np.array([1.,2.,2.]))
        np.testing.assert_allclose(Q@R,A)
        np.testing.assert_allclose(x,[7/6,.5])
        p=load(STEMS[7]);big,*_=p.experiment(1e-3);small,*_=p.experiment(1e-2)
        self.assertGreater(big/small,9)
    def test_curriculum_counts_and_live_links(self):
        course=json.loads((ROOT/"courses.json").read_text(encoding="utf-8"))
        counts={int(c["id"]):c.get("deepened",0) for c in course["chapters"]}
        self.assertEqual(counts[3],5)
        self.assertEqual(counts[6],27)
        self.assertEqual(sum(counts.values()),56)
        index=(ROOT/"index.html").read_text(encoding="utf-8")
        for stem in STEMS:
            self.assertIn(stem+".html",index)
        self.assertIn("56",index)

if __name__=="__main__":unittest.main()
