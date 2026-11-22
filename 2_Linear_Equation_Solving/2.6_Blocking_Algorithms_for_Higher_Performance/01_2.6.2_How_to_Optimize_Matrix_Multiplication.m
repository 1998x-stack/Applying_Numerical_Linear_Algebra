% Blocked GEMM with tail blocks; correctness not speed benchmark.
rng(7); A=randn(7,5); B=randn(5,6);
for block=[1 2 3 8]
    C=zeros(size(A,1),size(B,2));
    for i=1:block:size(A,1)
        ii=i:min(i+block-1,size(A,1));
        for j=1:block:size(B,2)
            jj=j:min(j+block-1,size(B,2));
            for k=1:block:size(A,2)
                kk=k:min(k+block-1,size(A,2));
                C(ii,jj)=C(ii,jj)+A(ii,kk)*B(kk,jj);
            end
        end
    end
    fprintf('block=%d, error=%.3e\n',block,norm(C-A*B,'fro'));
    assert(norm(C-A*B,'fro')<1e-11);
end
