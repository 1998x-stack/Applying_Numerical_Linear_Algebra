% Solve Ax=b and check residual and condition number.
A=[3 1;1 2]; b=[9;8]; x=A\b;
residual=norm(b-A*x,2);
eta=residual/(norm(A,2)*norm(x,2)+norm(b,2));
fprintf('x=[%.8g, %.8g], residual=%.3e, eta=%.3e, kappa2=%.3e\n',x(1),x(2),residual,eta,cond(A,2));
assert(norm(x-[2;3])<1e-12);
