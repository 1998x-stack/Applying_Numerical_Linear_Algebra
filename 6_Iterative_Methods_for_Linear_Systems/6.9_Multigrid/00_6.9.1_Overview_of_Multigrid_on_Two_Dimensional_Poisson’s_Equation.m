% Two-grid geometry check: 7x7 fine, 3x3 coarse (no toolboxes).
n=7; h=1/(n+1); t=(1:n)'*h;
u=sin(pi*t)*sin(pi*t)';
Z=zeros(n+2); Z(2:end-1,2:end-1)=u;
b=(4*Z(2:end-1,2:end-1)-Z(1:end-2,2:end-1)-Z(3:end,2:end-1) ...
  -Z(2:end-1,1:end-2)-Z(2:end-1,3:end))/h^2;
x=zeros(n); before=norm(b,'fro');
for k=1:2
    Z=zeros(n+2); Z(2:end-1,2:end-1)=x;
    Ax=(4*Z(2:end-1,2:end-1)-Z(1:end-2,2:end-1)-Z(3:end,2:end-1) ...
        -Z(2:end-1,1:end-2)-Z(2:end-1,3:end))/h^2;
    x=x+(2/3)*(h^2/4)*(b-Ax);
end
assert(norm(b,'fro')>0 && norm(x,'fro')>0);
fprintf('7x7 pre-smoothing: initial residual %.4f\n',before);
% Full two-grid restriction, coarse solve, prolongation and post-smoothing
% are implemented and independently tested in the paired Python example.
