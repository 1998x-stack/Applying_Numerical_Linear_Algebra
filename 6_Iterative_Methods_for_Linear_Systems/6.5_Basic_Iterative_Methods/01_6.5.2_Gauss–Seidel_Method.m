% 6.5.2 Gauss-Seidel iteration for T_N x = b
N = 16;
b = ones(N,1);
x = zeros(N,1);
steps = 40;
residual = zeros(steps+1,1);
residual(1) = norm(b - (2*x - [0; x(1:end-1)] - [x(2:end); 0]));
for k = 1:steps
    for i = 1:N
        left = 0; right = 0;
        if i > 1, left = x(i-1); end % already updated
        if i < N, right = x(i+1); end % not yet updated
        x(i) = (b(i) + left + right)/2;
    end
    residual(k+1) = norm(b - (2*x - [0; x(1:end-1)] - [x(2:end); 0]));
end
rhoJ = cos(pi/(N+1));
fprintf('rho_J=%.6f, rho_GS (1D model)=%.6f\n', rhoJ, rhoJ^2);
fprintf('residual: %.3e -> %.3e\n', residual(1), residual(end));
