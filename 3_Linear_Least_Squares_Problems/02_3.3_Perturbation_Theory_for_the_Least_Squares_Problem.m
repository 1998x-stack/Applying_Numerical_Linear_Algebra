% LS perturbation: the residual-dependent term.
delta=.01;eps=1e-6;
A=[1 0;0 delta;0 0];dA=zeros(3,2);dA(3,2)=eps;
for r3=[0 1]
    b=[1;delta;r3];x=A\b;r=b-A*x;
    xn=(A+dA)\b;
    dx=(A'*A)\(dA'*r-A'*dA*x);
    analytic=(delta^2+eps*r3)/(delta^2+eps^2);
    fprintf('r3=%g: x2=%.10f, delta x2=%.6g, derivative=%.6g\n',r3,xn(2),xn(2)-x(2),dx(2));
    assert(abs(xn(2)-analytic)<1e-10);
    if r3==1,assert(abs((xn(2)-x(2))-dx(2))<1e-6);end
end
