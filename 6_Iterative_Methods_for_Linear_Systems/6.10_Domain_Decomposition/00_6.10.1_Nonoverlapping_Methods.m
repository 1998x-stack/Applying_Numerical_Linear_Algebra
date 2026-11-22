% Nonoverlapping Schur complement on five interior Poisson nodes.
n=5;A=2*eye(n)-diag(ones(n-1,1),1)-diag(ones(n-1,1),-1);
b=(1:n)';I=[1,2,4,5];G=3;
Aii=A(I,I);Aig=A(I,G);Agi=A(G,I);
Y=Aii\Aig;z=Aii\b(I);
S=A(G,G)-Agi*Y;g=b(G)-Agi*z;
xg=S\g;xi=z-Y*xg;x=zeros(n,1);
x(I)=xi;x(G)=xg;
assert(abs(S-2/3)<1e-12);
assert(norm(A*x-b)<1e-12);
assert(norm(x-A\b)<1e-12);
fprintf('Schur S=%g, residual=%g\n',S,norm(A*x-b));
