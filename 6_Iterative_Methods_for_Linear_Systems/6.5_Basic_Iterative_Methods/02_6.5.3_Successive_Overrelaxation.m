% SOR on 1-D Dirichlet Poisson; base MATLAB/Octave, no toolboxes.
n = 16;
A = diag(2*ones(n,1)) + diag(-ones(n-1,1),1) + diag(-ones(n-1,1),-1);
b = ones(n,1);
omega_opt = 2/(1+sin(pi/(n+1)));
for omega = [0.8, 1, 1.5, omega_opt]
    x = zeros(n,1);
    for k = 1:300
        old = x;
        for i = 1:n
            lower = A(i,1:i-1)*x(1:i-1);
            upper = A(i,i+1:n)*old(i+1:n);
            candidate = (b(i)-lower-upper)/A(i,i);
            x(i) = (1-omega)*old(i)+omega*candidate;
        end
    end
    assert(norm(x-(A\b)) < 1e-7);
    fprintf('omega=%.6f, ||r||2=%.3e\n', omega, norm(b-A*x));
end
