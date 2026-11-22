% Model-specific spectral radii; no toolboxes.
for n = [8, 16, 32]
    A = diag(2*ones(n,1))+diag(-ones(n-1,1),1)+diag(-ones(n-1,1),-1);
    BJ = eye(n)-A/2;
    rhoj = cos(pi/(n+1));
    rhogs = rhoj^2;
    omega = 2/(1+sin(pi/(n+1)));
    assert(abs(max(abs(eig(BJ)))-rhoj) < 1e-10);
    assert(0 < omega-1 && omega-1 < rhogs && rhogs < rhoj);
    fprintf('N=%d: rhoJ=%g, rhoGS=%g, omega*=%.5f\n',n,rhoj,rhogs,omega);
end
