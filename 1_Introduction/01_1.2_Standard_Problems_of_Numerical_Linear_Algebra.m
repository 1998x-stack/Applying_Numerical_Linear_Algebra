% Four standard numerical linear algebra problem families.
A = [3 1; 1 2]; xTrue = [1; 2]; b = A*xTrue;
x = A\b;
fprintf('Linear-system residual: %.3e\n', norm(A*x-b));

Als = [1 0; 1 1; 1 2]; bls = [1; 2; 2];
xls = Als\bls;
fprintf('Least-squares residual: %.3e\n', norm(Als*xls-bls));

S = [2 1; 1 2];
[V,D] = eig(S);
fprintf('Eigen residual: %.3e\n', norm(S*V-V*D,'fro'));

M = [3 0 0; 0 1 0];
[U,Sigma,V] = svd(M,'econ');
fprintf('SVD reconstruction: %.3e\n', norm(M-U*Sigma*V','fro'));
