% SVD pseudoinverse for a rank-one 3-by-2 design matrix.
A=[1 1;2 2;3 3];b=[1;2;2];
[U,S,V]=svd(A,0);s=diag(S); tol=1e-12*s(1);
d=zeros(size(s));d(s>tol)=1./s(s>tol);
x=V*(d.*(U'*b));
assert(norm(x-[11/28;11/28])<1e-12);
assert(norm(A'*(b-A*x))<1e-12);
assert(norm(x-pinv(A)*b)<1e-12);
fprintf('minimum norm x=[%g,%g]\n',x(1),x(2));
