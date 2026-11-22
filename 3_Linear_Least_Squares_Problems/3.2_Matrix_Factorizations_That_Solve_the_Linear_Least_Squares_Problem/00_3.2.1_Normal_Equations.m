% Normal equations and QR reference (no explicit matrix inverse).
A=[1 0;1 1;1 2];b=[1;2;2];
x=(A'*A)\(A'*b);xqr=A\b;
kA=cond(A);kG=cond(A'*A);
fprintf('normal x=[%.8g %.8g], condA=%g, condGram=%g\n',x(1),x(2),kA,kG);
assert(norm(x-[7/6;1/2])<1e-12);
assert(norm(x-xqr)<1e-12);
assert(norm(A'*(b-A*x))<1e-12);
assert(abs(kG/kA^2-1)<1e-12);
