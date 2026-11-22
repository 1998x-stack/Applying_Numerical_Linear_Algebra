% 6.5.1 Jacobi iteration for T_N x = b
N = 16;
b = ones(N,1);
xOld = zeros(N,1);
steps = 40;
residual = zeros(steps+1,1);
residual(1) = norm(b - (2*xOld - [0; xOld(1:end-1)] - [xOld(2:end); 0]));
for k = 1:steps
    xNew = zeros(N,1);
    for i = 1:N
        left = 0; right = 0;
        if i > 1, left = xOld(i-1); end
        if i < N, right = xOld(i+1); end
        xNew(i) = (b(i) + left + right)/2;
    end
    xOld = xNew;
    residual(k+1) = norm(b - (2*xOld - [0; xOld(1:end-1)] - [xOld(2:end); 0]));
end
fprintf('residual: %.3e -> %.3e\n', residual(1), residual(end));
