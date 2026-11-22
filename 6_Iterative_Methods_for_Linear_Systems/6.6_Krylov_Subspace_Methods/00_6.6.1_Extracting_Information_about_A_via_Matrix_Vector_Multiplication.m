% Krylov powers via matrix-vector multiplication, no toolboxes.
A = diag([1,2,3,4]);
r = ones(4,1);
K = zeros(4,4);
for j = 1:4
    K(:,j) = r;
    r = A*r;
end
assert(rank(K)==4);
assert(norm(A*K(:,1:3)-K(:,2:4),'fro') < 1e-12);
e1 = [1;0;0;0];
assert(rank([e1,A*e1,A^2*e1,A^3*e1])==1);
fprintf('Krylov full rank=%d, eigenvector start rank=1\n',rank(K));
