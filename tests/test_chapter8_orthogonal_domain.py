"""Numeric, accessibility and source-parity regressions for the eighth batch."""
import importlib.util
import json
import re
import unittest
from pathlib import Path
from html.parser import HTMLParser
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
STEMS=[
  "6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/01_6.9.2_Detailed_Description_of_Multigrid_on_One_Dimensional_Poisson’s_Equation",
  "6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/00_6.10.1_Nonoverlapping_Methods",
  "6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/01_6.10.2_Overlapping_Methods",
  "3_Linear_Least_Squares_Problems/3.4_Orthogonal_Matrices/00_3.4.1_Householder_Transformations",
  "3_Linear_Least_Squares_Problems/3.4_Orthogonal_Matrices/01_3.4.2_Givens_Rotations",
  "3_Linear_Least_Squares_Problems/3.4_Orthogonal_Matrices/02_3.4.3_Roundoff_Error_Analysis_for_Orthogonal_Matrices",
  "3_Linear_Least_Squares_Problems/3.4_Orthogonal_Matrices/03_3.4.4_Why_Orthogonal_Matrices?",
  "3_Linear_Least_Squares_Problems/3.5_Rank_Deficient_Least_Squares_Problems/00_3.5.1_Solving_Rank_Deficient_Least_Squares_Problems_Using_the_SVD"
]
def load(stem):
    p=ROOT/(stem+".py")
    spec=importlib.util.spec_from_file_location("eighth_"+re.sub("[^a-zA-Z0-9_]","_",stem),p)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.h1=0;self.main=0;self.math=0;self.svg=0;self.demo=0;self.output=0;self.external=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=="h1":self.h1+=1
        if tag=="main":self.main+=1
        if tag=="math":self.math+=1
        if tag=="svg":self.svg+=1
        if "data-demo-control" in d:self.demo+=1
        if "data-demo-output" in d:self.output+=1
        if tag in ("script","link","img"):
            p=d.get("href") or d.get("src") or ""
            if p.startswith(("http:","https:")):self.external.append(p)
class EighthBatchTests(unittest.TestCase):
    def test_all_eight_numerical_examples(self):
        for stem in STEMS:
            with self.subTest(stem=stem):
                self.assertIsNotNone(load(stem).run_case())
    def test_companions_and_evidence(self):
        for stem in STEMS:
            with self.subTest(stem=stem):
                for suffix in (".html",".md",".py",".m",".evidence.json"):
                    self.assertTrue((ROOT/(stem+suffix)).is_file(),stem+suffix)
                data=json.loads((ROOT/(stem+".evidence.json")).read_text("utf-8"))
                self.assertGreaterEqual(len(data["claims"]),3)
                for claim in data["claims"]:
                    for key in ("id","claim","kind","source_url","locator","status","notes"):
                        self.assertTrue(claim[key],stem+" / "+key)
    def test_accessible_offline_html_md_parity(self):
        for stem in STEMS:
            with self.subTest(stem=stem):
                h=(ROOT/(stem+".html")).read_text("utf-8")
                md=(ROOT/(stem+".md")).read_text("utf-8")
                p=Page();p.feed(h)
                self.assertEqual(p.h1,1)
                self.assertEqual(p.main,1)
                self.assertGreaterEqual(p.svg,1)
                self.assertGreaterEqual(p.math,1)
                self.assertGreaterEqual(p.demo,1)
                self.assertGreaterEqual(p.output,1)
                self.assertEqual(p.external,[])
                self.assertGreater(len(md),1200)
                self.assertEqual(re.search(r"^# (.+)$",md,re.M).group(1),re.search(r"<h1[^>]*>(.*?)</h1>",h,re.S).group(1))
    def test_multigrid_galerkin_and_residual(self):
        m=load(STEMS[0]);A=m.lap(15)
        truth=np.sin(np.pi*np.arange(1,16)/16)
        b=A@truth;x=m.vcycle(A,b)
        self.assertLess(np.linalg.norm(b-A@x),np.linalg.norm(b)/4)
        k=7;P=np.column_stack([m.prolong(np.eye(k)[:,j]) for j in range(k)])
        np.testing.assert_allclose((P.T/2)@A@P,m.lap(k))
    def test_schur_interface_and_schwarz(self):
        m=load(STEMS[1]);n=5;A=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1);b=np.arange(1.,6.)
        x,S=m.schur_solve(A,b,[0,1,3,4],[2])
        np.testing.assert_allclose(S,[[2/3]])
        np.testing.assert_allclose(A@x,b)
        m=load(STEMS[2]);n=7;A=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
        B=m.additive_schwarz(A,[range(5),range(2,7)])
        self.assertGreater(np.linalg.eigvalsh(B).min(),0)
        self.assertLess(np.max(np.abs(1-.5*np.linalg.eigvals(B@A).real)),1)
    def test_reflection_and_rotation(self):
        h=load(STEMS[3]);H=h.reflector([3.,4.,0.])
        np.testing.assert_allclose(H@[3,4,0],[-5,0,0],atol=1e-12)
        g=load(STEMS[4]);G=g.givens(3,4)
        np.testing.assert_allclose(G@[3,4],[5,0],atol=1e-12)
    def test_orthogonality_and_rank_deficiency(self):
        f=load(STEMS[5]);oq,rq,k=f.quality(1e-8)
        self.assertLess(oq,1e-12)
        self.assertLess(rq,1e-12)
        self.assertGreater(k,1e8)
        rotation=load(STEMS[6]).rotate(30)
        np.testing.assert_allclose(rotation.T@rotation,np.eye(2),atol=1e-14)
        A=np.array([[5.,0.,0.],[0.,.02,0.],[0.,0.,0.],[0.,0.,0.]])
        b=np.array([5.,.02,.1,0.])
        t=load(STEMS[7]);x,s=t.truncated_svd(A,b,0);y,_=t.truncated_svd(A,b,.05)
        np.testing.assert_allclose(x,[1,1,0])
        np.testing.assert_allclose(y,[1,0,0])
        self.assertLess(np.linalg.norm(y),np.linalg.norm(x))
        self.assertGreater(np.linalg.norm(b-A@y),np.linalg.norm(b-A@x))
    def test_portal_counts_and_links(self):
        c=json.loads((ROOT/"courses.json").read_text("utf-8"))
        d={int(e["id"]):e.get("deepened",0) for e in c["chapters"]}
        self.assertEqual([d[i] for i in (1,2,3,6)],[8,19,10,27])
        self.assertEqual(sum(d.values()),64)
        html=(ROOT/"index.html").read_text("utf-8")
        for stem in STEMS:self.assertIn(stem+".html",html)
        self.assertIn("<strong>64</strong>",html)
if __name__=="__main__":unittest.main()
