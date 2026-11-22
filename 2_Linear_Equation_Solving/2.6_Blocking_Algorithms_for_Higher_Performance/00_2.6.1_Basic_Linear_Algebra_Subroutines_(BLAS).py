"""BLAS geometry and idealized compulsory-traffic models (not timings)."""
import numpy as np

def intensity_models(n):
    if not isinstance(n,int) or n<1:
        raise ValueError("n must be a positive integer")
    n=float(n)
    return {
      "axpy":{"flops":2*n,"bytes":24*n,"intensity":1/12},
      "gemv":{"flops":2*n*n,"bytes":8*n*n+16*n,
              "intensity":2*n*n/(8*n*n+16*n)},
      # C <- A B + C needs reading A,B,C and writing C: 4*n^2 doubles.
      "gemm":{"flops":2*n**3,"bytes":32*n*n,"intensity":n/16},
    }

def check_blas_equivalents(n=4):
    if not isinstance(n,int) or n<1 or n>1024:
        raise ValueError("1 <= n <= 1024")
    x=np.arange(1,n+1,dtype=float)
    y=np.ones(n)
    A=np.arange(1,n*n+1,dtype=float).reshape(n,n)
    B=np.eye(n)
    return {"axpy":2*x+y,"gemv":A@x,"gemm":A@B+A.copy()}

if __name__=="__main__":
    print(intensity_models(64))
    print("shapes", {key:value.shape for key,value in check_blas_equivalents().items()})
