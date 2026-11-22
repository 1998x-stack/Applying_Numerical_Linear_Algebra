% Wilkinson growth factor with deterministic first-row tie breaking.
for n=[2 3 4]
    W=eye(n)+tril(-ones(n),-1); W(:,end)=1;
    U=W; baseline=max(abs(W(:))); observed=baseline;
    for k=1:n-1
        [~,rel]=max(abs(U(k:n,k))); pivot=k+rel-1;
        U([k pivot],:)=U([pivot k],:);
        for i=k+1:n
            mult=U(i,k)/U(k,k);
            U(i,k:end)=U(i,k:end)-mult*U(k,k:end);
            U(i,k)=0;
        end
        observed=max(observed,max(abs(U(:))));
    end
    rho=observed/baseline;
    fprintf('n=%d, rho=%.4g, expected %.4g\n',n,rho,2^(n-1));
    assert(abs(rho-2^(n-1))<1e-12);
end
