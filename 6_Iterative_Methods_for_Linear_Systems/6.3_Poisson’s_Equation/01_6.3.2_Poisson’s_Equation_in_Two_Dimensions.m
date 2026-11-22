% 6.3.2 Two-dimensional Poisson equation: five-point matrix
N = 8;
h = 1 / (N + 1);
T = 2*eye(N) - diag(ones(N-1,1),1) - diag(ones(N-1,1),-1);
A = (kron(eye(N),T) + kron(T,eye(N))) / h^2;
fprintf('unknowns=%d, nnz=%d, dense entries=%d\n', N^2, nnz(A), N^4);
fprintf('symmetry defect = %.3e\n', norm(A-A','fro'));
