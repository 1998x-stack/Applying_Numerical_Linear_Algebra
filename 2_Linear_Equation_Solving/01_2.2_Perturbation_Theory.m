% Conditional perturbation bound for a specified example.
A=[2 0;0 1]; b=[2;1]; dA=zeros(2); db=[0;1e-6];
x=A\b; xNew=(A+dA)\(b+db);
alpha=norm(dA,2)/norm(A,2); beta=norm(db)/norm(b);
kappa=cond(A,2); assert(kappa*alpha<1);
bound=kappa*(alpha+beta)/(1-kappa*alpha);
actual=norm(xNew-x)/norm(x);
fprintf('actual=%.5e, bound=%.5e\n',actual,bound);
assert(actual<=bound+1e-12);
