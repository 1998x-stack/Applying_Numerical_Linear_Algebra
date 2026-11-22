% Three-point line fit and residual orthogonality, no toolboxes.
A=[1 0;1 1;1 2];b=[1;2;2];
x=A\b;r=b-A*x;
assert(norm(x-[7/6;1/2])<1e-12);
assert(norm(r-[-1/6;1/3;-1/6])<1e-12);
assert(norm(A'*r)<1e-12);
assert(abs(r'*r-1/6)<1e-12);
fprintf('line y=%.5f + %.5f t\n',x(1),x(2));
