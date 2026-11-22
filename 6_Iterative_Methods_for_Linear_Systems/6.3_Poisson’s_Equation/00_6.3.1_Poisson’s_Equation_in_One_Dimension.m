% 6.3.1 One-dimensional Poisson equation
N = 12;
h = 1 / (N + 1);
x = (1:N)' * h;
T = 2*eye(N) - diag(ones(N-1,1),1) - diag(ones(N-1,1),-1);
f = pi^2 * sin(pi*x);
rhs = h^2 * f;
vDiscrete = T \ rhs;
vExact = sin(pi*x);
fprintf('N=%d, h=%.4f, residual=%.3e, max error=%.3e\n', ...
    N, h, norm(T*vDiscrete-rhs), norm(vDiscrete-vExact, inf));
