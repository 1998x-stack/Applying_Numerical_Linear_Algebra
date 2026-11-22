% Positive definiteness alone does not guarantee Jacobi convergence.
for d = [2, 3]
    A = ones(3)+(d-1)*eye(3);
    BJ = eye(3)-diag(1./diag(A))*A;
    assert(min(eig(A)) > 0);
    rho = max(abs(eig(BJ)));
    assert(abs(rho-2/d) < 1e-12);
    fprintf('d=%g, min eig(A)=%g, rho(Jacobi)=%g\n',d,min(eig(A)),rho);
end
