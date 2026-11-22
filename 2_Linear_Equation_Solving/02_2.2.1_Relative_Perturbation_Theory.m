% Componentwise relative perturbations for diagonal system.
gamma=1e8; eps0=1e-6;
A=diag([gamma 1]); b=[gamma;1]; x=A\b;
Anew=diag(diag(A).*[1+eps0;1-eps0]);
bnew=b.*[1-eps0;1+eps0];
xnew=Anew\bnew;
componentwise=max(abs(xnew-x)./abs(x));
bound=2*eps0/(1-eps0);
fprintf('cond2(A)=%.3e, max component relative error=%.3e\n',cond(A),componentwise);
assert(componentwise<=bound+1e-12);
