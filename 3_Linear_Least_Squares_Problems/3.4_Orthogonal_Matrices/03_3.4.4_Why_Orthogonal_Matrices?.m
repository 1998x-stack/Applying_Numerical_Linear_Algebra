% Orthonormal rotation preserves lengths and inner products.
theta=pi/6;c=cos(theta);s=sin(theta);
Q=[c -s;s c];x=[3;4];y=[-2;1];
assert(norm(Q'*Q-eye(2))<1e-12);
assert(abs(norm(Q*x)-5)<1e-12);
assert(abs((Q*x)'*(Q*y)-x'*y)<1e-12);
assert(abs(cond(Q)-1)<1e-12);
assert(abs(cond(diag([10 .1]))-100)<1e-12);
disp(Q*x);
