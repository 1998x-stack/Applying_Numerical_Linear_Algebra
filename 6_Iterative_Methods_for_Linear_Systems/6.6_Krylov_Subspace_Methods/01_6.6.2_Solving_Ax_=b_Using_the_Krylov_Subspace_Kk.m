% SPD Galerkin projection; base MATLAB/Octave, no toolboxes.
A = diag([1,2,3,4]); b = ones(4,1);
for k = [1,2,3,4]
    W = zeros(4,k); W(:,1) = b;
    for j = 2:k
        W(:,j) = A*W(:,j-1);
    end
    [V,~] = qr(W,0);
    y = (V'*A*V)\(V'*b);
    x = V*y;
    r = b-A*x;
    assert(norm(V'*r) < 1e-10);
    if k == 1
        assert(norm(x-0.4*b) < 1e-12);
    end
    if k == 4
        assert(norm(x-(A\b)) < 1e-10);
    end
    fprintf('k=%d, residual=%g, orthogonality=%g\n',k,norm(r),norm(V'*r));
end
