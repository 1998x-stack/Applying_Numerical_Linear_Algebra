% A(t) is nonsingular, symmetric, and indefinite for any finite real t.
for t=[-3 0 3]
    A=[0 1;1 t]; b=[1;2];
    eigNumeric=sort(eig(A));
    expected=sort([(t-sqrt(t^2+4))/2;(t+sqrt(t^2+4))/2]);
    L=eye(2); D=A; x=A\b; % D is a valid 2x2 pivot block.
    fprintf('t=%g, eigs=[%.4g, %.4g], determinant=%.4g\n',t,eigNumeric(1),eigNumeric(2),det(A));
    assert(norm(eigNumeric-expected)<1e-12);
    assert(eigNumeric(1)<0 && eigNumeric(2)>0);
    assert(norm(A-L*D*L')<1e-12);
    assert(norm(A*x-b)<1e-12);
end
