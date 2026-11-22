% 6.3.3 Kronecker-sum representation with column-major vec(V)
nx = 5; ny = 3;
hx = 0.2; hy = 0.25;
Tx = 2*eye(nx) - diag(ones(nx-1,1),1) - diag(ones(nx-1,1),-1);
Ty = 2*eye(ny) - diag(ones(ny-1,1),1) - diag(ones(ny-1,1),-1);
A = kron(eye(ny),Tx)/hx^2 + kron(Ty,eye(nx))/hy^2;
V = reshape(1:(nx*ny),nx,ny);
lhs = reshape(A*V(:),nx,ny);
rhs = (Tx*V)/hx^2 + (V*Ty)/hy^2;
fprintf('Kronecker / matrix form defect = %.3e\n', norm(lhs-rhs,'fro'));
