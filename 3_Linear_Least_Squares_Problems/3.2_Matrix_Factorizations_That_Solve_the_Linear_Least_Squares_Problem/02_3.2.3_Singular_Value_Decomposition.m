% Rank-deficient minimum norm solution from SVD with explicit cutoff.
A=[1 1;2 2;3 3];b=[1;2;3];
[U,S,V]=svd(A,'econ');
sigma=diag(S);tol=1e-12*max(sigma);
gain=zeros(size(sigma));gain(sigma>tol)=1./sigma(sigma>tol);
x=V*(gain.*(U'*b));
fprintf('numerical rank=%d, x=[%.9g %.9g]\n',sum(sigma>tol),x(1),x(2));
assert(norm(x-[.5;.5])<1e-12);
assert(norm(A*x-b)<1e-12);
assert(norm(U*S*V'-A)<1e-12);
