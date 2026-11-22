% Economy QR and projection for m>n.
A=[1 0;1 1;1 2];b=[1;2;2];
[Q,R]=qr(A,0);x=R\(Q'*b);
r=b-A*x;
fprintf('shapeQ=%dx%d, shapeR=%dx%d, orth=%.3e\n',size(Q),size(R),norm(Q'*Q-eye(2)));
assert(isequal(size(Q),[3 2]));
assert(isequal(size(R),[2 2]));
assert(norm(Q*R-A)<1e-12);
assert(norm(Q'*r)<1e-12);
assert(norm(x-[7/6;1/2])<1e-12);
