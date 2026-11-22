% Additive Schwarz on 7 interior nodes, overlapping subdomains.
n=7;A=2*eye(n)-diag(ones(n-1,1),1)-diag(ones(n-1,1),-1);
blocks={1:5,3:7};B=zeros(n);
for k=1:2
    ids=blocks{k};
    B(ids,ids)=B(ids,ids)+(A(ids,ids)\eye(length(ids)));
end
lam=eig(B*A); omega=.5;rho=max(abs(1-omega*lam));
assert(rho<1);
b=ones(n,1);x=zeros(n,1);
before=norm(b);
for j=1:120,x=x+omega*B*(b-A*x);end
after=norm(b-A*x);
assert(after<1e-8);
assert(norm(x-A\b)<1e-7);
fprintf('rho=%g, residual %g -> %g\n',rho,before,after);
