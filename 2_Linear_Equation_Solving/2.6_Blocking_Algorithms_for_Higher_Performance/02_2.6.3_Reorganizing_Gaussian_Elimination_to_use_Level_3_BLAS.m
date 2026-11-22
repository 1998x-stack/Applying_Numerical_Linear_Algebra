% One no-pivot block elimination identity; production GEPP also permutes rows.
A=[4 1 1 0;1 3 0 1;1 0 3 1;0 1 1 4]; n=size(A,1);
for block=1:n-1
    A11=A(1:block,1:block); A12=A(1:block,block+1:end);
    A21=A(block+1:end,1:block); A22=A(block+1:end,block+1:end);
    L21=(A11'\A21')';
    S=A22-L21*A12;
    rec=[A11 A12;L21*A11 L21*A12+S];
    fprintf('b=%d, Schur error=%.3e\n',block,norm(rec-A,Inf));
    assert(norm(rec-A,Inf)<1e-12);
end
