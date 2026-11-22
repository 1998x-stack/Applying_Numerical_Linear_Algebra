% MATLAB [L,U,P]=lu(A) satisfies P*A=L*U.
A=[0 2;1 3]; b=[2;4];
[L,U,P]=lu(A);
y=L\(P*b); x=U\y;
fprintf('LU reconstruction=%.3e, residual=%.3e\n',norm(P*A-L*U),norm(A*x-b));
assert(norm(P*A-L*U)<1e-12);
assert(norm(A*x-b)<1e-12);
