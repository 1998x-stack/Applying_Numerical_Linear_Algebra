% Diagonal SPD example: one-step PCG with Jacobi preconditioner.
A=diag([1,100,4,400]); b=ones(4,1); d=diag(A);
x=zeros(4,1); r=b-A*x; z=r./d; p=z;
alpha=(r'*z)/(p'*A*p); x=x+alpha*p; r=b-A*x;
assert(norm(x-(A\b))<1e-12);
assert(norm(r)<1e-12);
C=diag(1./sqrt(d))*A*diag(1./sqrt(d));
assert(norm(C-eye(4),'fro')<1e-12);
fprintf('kappa(A)=%.1f, kappa(C)=%.1f\n',cond(A),cond(C));
