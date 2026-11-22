% One-dimensional geometric V-cycle on 15->7->3->1 nested grids.
% MATLAB R2016b+ (local functions supported); no toolboxes.
n=15;A=poisson1(n);h=1/(n+1);
truth=sin(pi*(1:n)'*h);b=A*truth;
x=zeros(n,1); history=zeros(8,1);history(1)=norm(b);
for i=1:7
    x=mgcycle1(A,b,x);
    history(i+1)=norm(b-A*x);
end
assert(history(end)<history(1)*1e-5);
assert(norm(x-(A\b))<1e-4);
disp(history');
function A=poisson1(n)
  h=1/(n+1);A=(2*eye(n)-diag(ones(n-1,1),1)-diag(ones(n-1,1),-1))/h^2;
end
function x=mgcycle1(A,b,x)
  n=numel(b);
  if n==1,x=A\b;return;end
  d=diag(A);
  for i=1:2,x=x+(2/3)*(b-A*x)./d;end
  r=b-A*x;
  rc=(r(1:2:end-2)+2*r(2:2:end-1)+r(3:2:end))/4;
  ec=mgcycle1(poisson1(numel(rc)),rc,zeros(size(rc)));
  k=numel(ec);fine=zeros(2*k+1,1);
  fine(2:2:end)=ec;
  fine(1:2:end)=( [0;ec]+[ec;0] )/2;
  x=x+fine;
  for i=1:2,x=x+(2/3)*(b-A*x)./d;end
end
