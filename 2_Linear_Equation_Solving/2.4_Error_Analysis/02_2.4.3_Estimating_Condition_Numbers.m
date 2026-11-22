% Teaching n-solve reference for cond_1, not a scalable estimator.
A=diag([1 1e-6]); n=size(A,1);
inverseNorm=0;
for j=1:n
    e=zeros(n,1); e(j)=1;
    z=A\e;
    inverseNorm=max(inverseNorm,sum(abs(z)));
end
kappa=norm(A,1)*inverseNorm;
fprintf('cond1 via basis solves: %.3e; MATLAB cond(A,1)=%.3e\n',kappa,cond(A,1));
assert(abs(kappa-cond(A,1))/cond(A,1)<1e-12);
