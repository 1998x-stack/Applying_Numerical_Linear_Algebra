% Mixed-precision refinement teaching example.
% MATLAB defaults to double for x and residual; single for correction solves.
A=[1 1;1 1.001]; xTrue=[1;1]; b=A*xTrue;
Alow=single(A); blow=single(b);
x=double(Alow\blow);
history=zeros(6,1);
for k=1:6
    r=b-A*x;
    history(k)=norm(r,Inf)/(norm(A,Inf)*norm(x,Inf)+norm(b,Inf));
    if k<6
        d=double(Alow\single(r));
        x=x+d;
    end
end
fprintf('mixed-precision IR: first=%.3e, last=%.3e, error=%.3e\n',history(1),history(end),norm(x-xTrue));
assert(history(end)<=history(1)+1e-13);
assert(norm(A*x-b)<1e-10);
