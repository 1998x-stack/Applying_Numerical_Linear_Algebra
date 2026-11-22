% Tridiagonal structure / Thomas and production sparse solver comparison.
for n=[2 4 8]
    a=-ones(n-1,1);d=4*ones(n,1);c=-ones(n-1,1);
    A=diag(d)+diag(a,-1)+diag(c,1);
    b=A*ones(n,1);
    dd=d;rr=b;
    for i=2:n
        if dd(i-1)==0,error('zero pivot');end
        m=a(i-1)/dd(i-1);
        dd(i)=dd(i)-m*c(i-1);
        rr(i)=rr(i)-m*rr(i-1);
    end
    x=zeros(n,1);x(n)=rr(n)/dd(n);
    for i=n-1:-1:1
        x(i)=(rr(i)-c(i)*x(i+1))/dd(i);
    end
    fprintf('n=%d nnz=%d residual=%.3e\n',n,nnz(A),norm(A*x-b));
    assert(norm(x-(A\b))<1e-11);
end
