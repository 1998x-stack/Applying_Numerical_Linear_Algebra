% Reduced QR least squares, no toolboxes.
A=[1 0;1 1;1 2];b=[1;2;2];
[Q,R]=qr(A,0);x=R\(Q'*b);
assert(norm(Q'*Q-eye(2))<1e-12);
assert(norm(Q*R-A)<1e-12);
assert(norm(x-[7/6;1/2])<1e-12);
r=b-A*x;p=b-Q*(Q'*b);
assert(abs(r'*r-p'*p)<1e-12);
fprintf('QR: intercept=%g, slope=%g\n',x(1),x(2));
