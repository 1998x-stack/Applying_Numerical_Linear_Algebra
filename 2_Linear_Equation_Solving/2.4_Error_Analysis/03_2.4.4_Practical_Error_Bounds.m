% Residual, componentwise backward error and teaching forward bound.
A=[3 1;1 2]; b=[9;8]; xhat=[2.001;2.999];
r=b-A*xhat; d=abs(A)*abs(xhat)+abs(b);
ratios=zeros(size(r));
for i=1:numel(r)
    if d(i)==0
        if r(i)==0, ratios(i)=0; else, ratios(i)=Inf; end
    else
        ratios(i)=abs(r(i))/d(i);
    end
end
berr=max(ratios);
% Small-matrix basis-solve reference for ||A^-1||_infinity.
n=size(A,1); cols=zeros(n);
for j=1:n
    e=zeros(n,1); e(j)=1; cols(:,j)=A\e;
end
invNormInf=max(sum(abs(cols),2));
bound=invNormInf*norm(r,Inf);
actual=norm(A\b-xhat,Inf);
fprintf('BERR=%.3e, actual=%.3e, bound=%.3e\n',berr,actual,bound);
assert(actual<=bound+1e-12);
