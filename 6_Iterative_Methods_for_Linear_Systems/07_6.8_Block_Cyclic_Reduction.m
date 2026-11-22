% One block Schur complement, 3x3 interior Poisson.
n=3; B=4*eye(n)-diag(ones(n-1,1),1)-diag(ones(n-1,1),-1);
off=diag(ones(n-1,1),1)+diag(ones(n-1,1),-1);
A=kron(eye(n),B)-kron(off,eye(n)); b=(1:9)';
E=4:6; O=[1:3,7:9]; Aoo=A(O,O);
S=A(E,E)-A(E,O)*(Aoo\A(O,E));
rhs=b(E)-A(E,O)*(Aoo\b(O));
x=zeros(9,1); x(E)=S\rhs; x(O)=Aoo\(b(O)-A(O,E)*x(E));
assert(norm(b-A*x)<1e-10);
assert(norm(S-(B-2*(B\eye(3))))<1e-10);
fprintf('block Schur residual=%.3e\n',norm(b-A*x));
