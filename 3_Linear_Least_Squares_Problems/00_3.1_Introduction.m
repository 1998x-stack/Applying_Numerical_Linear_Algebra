% Constant least squares via QR/lstsq and orthogonality.
b=[1;2;4];A=ones(3,1);x=A\b;
p=A*x;r=b-p;
fprintf('constant=%.12g, residual squared=%.12g\n',x,r'*r);
assert(abs(x-7/3)<1e-12);
assert(norm(A'*r)<1e-12);
assert(abs(b'*b-(p'*p+r'*r))<1e-12);
