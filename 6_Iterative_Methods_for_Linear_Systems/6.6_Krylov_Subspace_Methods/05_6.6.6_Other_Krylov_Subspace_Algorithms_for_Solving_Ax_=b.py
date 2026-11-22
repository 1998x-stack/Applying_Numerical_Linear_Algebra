"""Small full GMRES via Arnoldi and least squares; NumPy >=1.26."""
import numpy as np

def gmres_history(A,b):
    A=np.asarray(A,float); b=np.asarray(b,float)
    n=len(b)
    if A.shape!=(n,n): raise ValueError("square A and vector")
    beta=np.linalg.norm(b); V=np.zeros((n,n+1)); H=np.zeros((n+1,n))
    if beta==0: return np.zeros(n),np.array([0.])
    V[:,0]=b/beta; hist=[beta]; x=np.zeros(n)
    for j in range(n):
        w=A@V[:,j]
        for i in range(j+1):
            H[i,j]=V[:,i]@w
            w-=H[i,j]*V[:,i]
        H[j+1,j]=np.linalg.norm(w)
        if j+1<n and H[j+1,j]>1e-14: V[:,j+1]=w/H[j+1,j]
        rhs=np.zeros(j+2);rhs[0]=beta
        y=np.linalg.lstsq(H[:j+2,:j+1],rhs,rcond=None)[0]
        x=V[:,:j+1]@y
        hist.append(float(np.linalg.norm(b-A@x)))
    return x,np.array(hist)

def run_case():
    A=np.array([[3.,1.,0.],[0.,2.,1.],[0.,0.,1.]])
    b=np.array([1.,2.,3.])
    x,h=gmres_history(A,b)
    assert np.all(np.diff(h)<=1e-10)
    assert np.linalg.norm(x-np.linalg.solve(A,b))<1e-10
    return {"residual_by_k":h.tolist(),"x":x.tolist()}
if __name__=="__main__":print(run_case())
