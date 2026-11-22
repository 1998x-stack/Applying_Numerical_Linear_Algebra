% Near-collinear input, reduced QR, orthogonality and reconstruction.
t=(0:3)';epsilon=1e-8;
A=[ones(4,1),1+epsilon*t];
[Q,R]=qr(A,0);
etaQ=norm(Q'*Q-eye(2),2);
etaA=norm(A-Q*R,'fro')/norm(A,'fro');
assert(etaQ<1e-12 && etaA<1e-12);
fprintf('etaQ=%.4e, etaA=%.4e, kappa(A)=%.4e\n',etaQ,etaA,cond(A));
