% Full two-grid correction for a 7x7 2-D Dirichlet Poisson problem.
% MATLAB R2016b+ / compatible Octave supports local functions in scripts.
n=7; h=1/(n+1); t=(1:n)'*h;
truth=sin(pi*t)*sin(pi*t)';
b=lap2(truth,h); x=zeros(n,n);
before=norm(b,'fro');
x=smooth2(x,b,h,2);
r=b-lap2(x,h);
rc=restriction2(r);
ec=coarsesolve2(rc);
x=x+prolong2(ec);
x=smooth2(x,b,h,2);
after=norm(b-lap2(x,h),'fro');
assert(after < before/3);
assert(norm(x-truth,'fro') < norm(truth,'fro'));
fprintf('initial residual=%g, after two-grid cycle=%g\n',before,after);

function Y=lap2(X,h)
  n=size(X,1); P=zeros(n+2,n+2); P(2:end-1,2:end-1)=X;
  Y=(4*P(2:end-1,2:end-1)-P(1:end-2,2:end-1)-P(3:end,2:end-1) ...
      -P(2:end-1,1:end-2)-P(2:end-1,3:end))/h^2;
end

function X=smooth2(X,B,h,k)
  for q=1:k
    X=X+(2/3)*(h^2/4)*(B-lap2(X,h));
  end
end

function R=restriction2(r)
  n=size(r,1); P=zeros(n+2,n+2); P(2:end-1,2:end-1)=r;
  R=zeros((n-1)/2);
  for i=1:size(R,1)
    for j=1:size(R,2)
      a=2*i+1; b=2*j+1;
      R(i,j)=(4*P(a,b)+2*(P(a-1,b)+P(a+1,b)+P(a,b-1)+P(a,b+1)) ...
         +P(a-1,b-1)+P(a-1,b+1)+P(a+1,b-1)+P(a+1,b+1))/16;
    end
  end
end

function F=prolong2(C)
  n=size(C,1); E=zeros(n+2); E(2:end-1,2:end-1)=C;
  nodes=0:2:(2*n+2); fine=1:(2*n+1);
  [xg,yg]=meshgrid(nodes,nodes);
  [xf,yf]=meshgrid(fine,fine);
  F=interp2(xg,yg,E,xf,yf,'linear');
end

function E=coarsesolve2(R)
  n=size(R,1); H=1/(n+1); A=zeros(n*n,n*n);
  for j=1:n*n
    basis=zeros(n,n); basis(j)=1;
    A(:,j)=reshape(lap2(basis,H),n*n,1);
  end
  E=reshape(A\R(:),n,n);
end
