% Unpreconditioned CG for a tiny SPD system; no toolboxes.
A = diag([1,2,3,4]); b = ones(4,1);
x = zeros(size(b)); r = b-A*x; p = r; rr = r'*r;
for k = 1:8
    if sqrt(rr) <= 1e-12*norm(b), break; end
    Ap = A*p;
    alpha = rr/(p'*Ap);
    x = x + alpha*p;
    r = r - alpha*Ap;
    rrnew = r'*r;
    fprintf('k=%d, true residual=%.3e\n',k,norm(b-A*x));
    if sqrt(rrnew) <= 1e-12*norm(b), break; end
    beta = rrnew/rr;
    p = r + beta*p;
    rr = rrnew;
end
assert(norm(x-(A\b)) < 1e-10);
