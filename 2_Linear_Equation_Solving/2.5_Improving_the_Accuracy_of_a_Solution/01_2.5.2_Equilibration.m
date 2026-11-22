% Row + column max equilibration and original-equation residual.
A=diag([1e6 1]); b=A*[1;1];
r=1./max(abs(A),[],2); B=diag(r)*A;
c=1./max(abs(B),[],1)'; B=B*diag(c);
y=B\(diag(r)*b); x=diag(c)*y;
fprintf('kappa original=%.4g, scaled=%.4g, residual=%.3e\n',cond(A),cond(B),norm(A*x-b,Inf));
assert(norm(x-[1;1])<1e-10);
assert(cond(B)<cond(A));
% Near-collinearity survives simple row/column scaling.
N=[1 1;1 1+1e-8]; nr=1./max(abs(N),[],2);
NB=diag(nr)*N; nc=1./max(abs(NB),[],1)';
NB=NB*diag(nc);
assert(cond(NB)>1e6);
