% Observation perturbation amplified by nearly dependent columns.
for e=[1e-2,1e-3]
    t=(0:3)';A=[ones(4,1),1+e*t];
    truth=[1;1];b=A*truth;db=[0;1e-3;0;0];
    x=A\(b+db);
    dx=x-truth;s=svd(A);
    assert(norm(dx)<=norm(db)/s(end)*(1+1e-7));
    assert(norm(dx)/norm(truth)<=cond(A)*norm(db)/norm(b)*(1+1e-7));
    fprintf('eps=%g, ||dx||=%g, sigma_min=%g\n',e,norm(dx),s(end));
end
