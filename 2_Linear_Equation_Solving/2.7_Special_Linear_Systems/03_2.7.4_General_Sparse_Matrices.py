"""Star-graph SPD Cholesky fill: same A, two elimination orderings."""
import numpy as np

def star_spd(n=6):
    if not isinstance(n,int) or n<3: raise ValueError("n >= 3 required")
    A=np.eye(n)
    for j in range(1,n):
        A[0,0]+=1
        A[j,j]+=1
        A[0,j]-=1; A[j,0]-=1
    return A

def ordering_fill(n=6):
    A=star_spd(n)
    results={}
    for name,perm in [("hub_first",np.arange(n)),("hub_last",np.r_[np.arange(1,n),0])]:
        B=A[np.ix_(perm,perm)]
        L=np.linalg.cholesky(B)
        nz=int(np.count_nonzero(np.abs(np.tril(L))>1e-12))
        results[name]={"nnz_factor":nz,"L":L,"permutation":perm,
                       "reconstruction_residual":float(np.linalg.norm(L@L.T-B))}
    return results

def csr_from_dense(A):
    A=np.asarray(A,dtype=float)
    if A.ndim!=2: raise ValueError("two-dimensional input required")
    values=[];indices=[];indptr=[0]
    for row in A:
        nz=np.flatnonzero(row)
        values.extend(row[nz].tolist())
        indices.extend(nz.tolist())
        indptr.append(len(values))
    return np.array(values),np.array(indices,dtype=int),np.array(indptr,dtype=int)

if __name__=="__main__":
    A=star_spd(6)
    data,cols,ptr=csr_from_dense(A)
    print("CSR",len(data),cols.tolist(),ptr.tolist())
    d=ordering_fill()
    print({k:v["nnz_factor"] for k,v in d.items()})
    assert d["hub_first"]["nnz_factor"]>d["hub_last"]["nnz_factor"]
