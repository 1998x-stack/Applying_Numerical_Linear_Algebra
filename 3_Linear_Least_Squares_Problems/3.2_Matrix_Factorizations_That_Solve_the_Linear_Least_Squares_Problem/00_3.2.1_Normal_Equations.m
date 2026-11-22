% Near-dependent columns and squared normal-equation condition.
for e=[1e-3,1e-4]
    A=[1 1;1 1+e;1 1+2*e];
    c=cond(A); cn=cond(A'*A);
    assert(abs(cn/c^2-1)<1e-5);
    fprintf('epsilon=%g, kappa(A)=%g, kappa(AtA)=%g\n',e,c,cn);
end
A=[1 1;1 1+1e-3;1 1+2e-3]; b=[1;2;2];
x=(A'*A)\(A'*b);
assert(norm(A'*(b-A*x))<1e-8);
