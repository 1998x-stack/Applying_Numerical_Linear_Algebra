% Factorization residuals. MATLAB lu returns P*A = L*U.
A = [2 1 1; 4 -6 0; -2 7 2];
[L,U,P] = lu(A);
fprintf('LU residual: %.3e\n', norm(P*A-L*U,'fro'));

[Q,R] = qr(A,0);
fprintf('QR residual: %.3e\n', norm(A-Q*R,'fro'));
fprintf('Q orthogonality: %.3e\n', norm(Q'*Q-eye(size(Q,2)),'fro'));

H = [4 1; 1 3];
C = chol(H,'lower');
fprintf('Cholesky residual: %.3e\n', norm(H-C*C','fro'));

M = [3 0 0; 0 1 0];
[Us,Sigma,V] = svd(M,'econ');
fprintf('SVD residual: %.3e\n', norm(M-Us*Sigma*V','fro'));
