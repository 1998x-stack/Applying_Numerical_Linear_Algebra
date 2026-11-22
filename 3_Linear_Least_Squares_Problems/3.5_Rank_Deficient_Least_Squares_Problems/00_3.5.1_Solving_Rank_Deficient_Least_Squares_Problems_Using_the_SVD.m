% Rank deficient 4x3 LS and truncated SVD, without toolboxes.
A=[5 0 0;0 .02 0;0 0 0;0 0 0];b=[5;.02;.1;0];
[U,S,V]=svd(A,0);s=diag(S);
d=zeros(size(s)); tol=eps*max(size(A))*s(1);
d(s>tol)=1./s(s>tol);
x=V*(d.*(U'*b));
dt=zeros(size(s));dt(s>.05)=1./s(s>.05);
xt=V*(dt.*(U'*b));
assert(norm(x-[1;1;0])<1e-12);
assert(norm(xt-[1;0;0])<1e-12);
assert(abs(norm(b-A*x)-.1)<1e-12);
assert(abs(norm(b-A*xt)-hypot(.1,.02))<1e-12);
fprintf('norm x=%g, norm truncated=%g\n',norm(x),norm(xt));
