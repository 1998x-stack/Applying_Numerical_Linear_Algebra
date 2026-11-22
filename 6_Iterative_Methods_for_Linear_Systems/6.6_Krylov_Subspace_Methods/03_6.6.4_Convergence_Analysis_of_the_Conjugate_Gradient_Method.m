% CG A-energy convergence vs theoretical kappa bound; no toolboxes.
A=diag([1,3,20,100]); b=ones(4,1);
exact = A\b; x=zeros(4,1); r=b; p=r; rr=r'*r;
norm0=sqrt((exact-x)'*A*(exact-x));
kappa=cond(A); q=(sqrt(kappa)-1)/(sqrt(kappa)+1);
for k=1:4
    Ap=A*p; alpha=rr/(p'*Ap);
    x=x+alpha*p; r=r-alpha*Ap;
    rrnew=r'*r;
    e=exact-x;
    ratio=sqrt(e'*A*e)/norm0;
    bound=2*q^k;
    assert(ratio <= bound+1e-9);
    fprintf('k=%d, A-error ratio=%.7f, upper bound=%.7f\n',k,ratio,bound);
    if k<4
        p=r+(rrnew/rr)*p; rr=rrnew;
    end
end
assert(norm(x-exact)<1e-10);
