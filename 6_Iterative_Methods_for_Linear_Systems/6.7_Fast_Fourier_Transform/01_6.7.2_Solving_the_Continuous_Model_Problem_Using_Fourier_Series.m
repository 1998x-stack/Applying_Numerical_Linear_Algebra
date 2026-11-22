% Dirichlet Poisson: discrete sine eigenvalue vs continuous sine mode.
for n=[7,15,31]
    h=1/(n+1); i=(1:n)';
    s=sin(pi*i*h); lambda=4*sin(pi/(2*(n+1)))^2/h^2;
    A=(2*eye(n)-diag(ones(n-1,1),1)-diag(ones(n-1,1),-1))/h^2;
    b=pi^2*s; x=b/lambda;
    assert(norm(A*x-b)<1e-10);
    fprintf('N=%d, max discretization error=%g\n',n,max(abs(x-s)));
end
