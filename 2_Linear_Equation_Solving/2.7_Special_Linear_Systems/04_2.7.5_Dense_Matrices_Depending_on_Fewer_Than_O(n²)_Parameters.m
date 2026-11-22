% Woodbury low-rank update, n=4 k=1 hand-check.
n=4;d=ones(n,1);U=ones(n,1);V=ones(n,1);b=[1;0;0;0];
z=b./d;W=U./d;K=eye(size(U,2))+V'*W;
c=K\(V'*z);x=z-W*c;
A=diag(d)+U*V';
fprintf('small system K=%g, residual=%g\n',K,norm(A*x-b));
assert(norm(x-[.8;-.2;-.2;-.2])<1e-12);
assert(norm(A*x-b)<1e-12);
