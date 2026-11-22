% SPD Cholesky with explicit factors; chol(A,'lower') returns lower factor.
A=[4 2;2 3]; b=A*[1;2];
L=chol(A,'lower'); x=L'\(L\b);
fprintf('factor error=%.3e, residual=%.3e\n',norm(L*L'-A,'fro'),norm(A*x-b));
assert(norm(L*L'-A,'fro')<1e-12);
assert(norm(x-[1;2])<1e-12);
% chol with 2 outputs returns a positive flag for a non-SPD matrix.
[~,flag]=chol([0 1;1 0]);
assert(flag>0);
