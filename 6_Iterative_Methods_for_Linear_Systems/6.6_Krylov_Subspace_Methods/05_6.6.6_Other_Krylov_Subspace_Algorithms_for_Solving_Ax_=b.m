% Full Arnoldi GMRES for a small nonsymmetric system.
A=[3 1 0;0 2 1;0 0 1]; b=[1;2;3]; n=length(b);
beta=norm(b); V=zeros(n,n+1); H=zeros(n+1,n);
V(:,1)=b/beta; residual=zeros(n+1,1); residual(1)=beta;
for j=1:n
    w=A*V(:,j);
    for i=1:j
        H(i,j)=V(:,i)'*w; w=w-H(i,j)*V(:,i);
    end
    H(j+1,j)=norm(w);
    if j<n && H(j+1,j)>1e-14, V(:,j+1)=w/H(j+1,j); end
    e=zeros(j+1,1); e(1)=beta;
    y=H(1:j+1,1:j)\e;
    x=V(:,1:j)*y;
    residual(j+1)=norm(b-A*x);
end
assert(all(diff(residual)<=1e-9));
assert(norm(x-(A\b))<1e-9);
disp(residual');
