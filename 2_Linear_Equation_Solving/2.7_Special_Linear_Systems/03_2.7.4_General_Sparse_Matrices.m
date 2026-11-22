% Symmetric star graph SPD and Cholesky fill, two permutations.
n=6;A=eye(n);
for j=2:n
    A(1,1)=A(1,1)+1;
    A(j,j)=A(j,j)+1;
    A(1,j)=-1;A(j,1)=-1;
end
p1=1:n;p2=[2:n 1];counts=zeros(1,2);
for k=1:2
    if k==1,p=p1;else,p=p2;end
    B=A(p,p);L=chol(B,'lower');
    counts(k)=nnz(abs(tril(L))>1e-12);
    assert(norm(L*L'-B,'fro')<1e-11);
end
fprintf('Cholesky nnz hub-first=%d hub-last=%d\n',counts(1),counts(2));
assert(counts(1)>counts(2));
