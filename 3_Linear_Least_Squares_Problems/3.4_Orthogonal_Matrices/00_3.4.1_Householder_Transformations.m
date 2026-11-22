% Householder reflection Hx=-||x|| e1.
x=[3;4;0];a=sign(x(1))*norm(x);
v=x;v(1)=v(1)+a;u=v/norm(v);
H=eye(length(x))-2*(u*u');
y=H*x;
assert(norm(y-[-5;0;0])<1e-12);
assert(norm(H'*H-eye(3))<1e-12);
assert(norm(H*H*x-x)<1e-12);
disp(y');
