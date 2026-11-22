% A nearly dependent matrix has a large condition number.
delta = 1e-8;
A = [1 1; 1 1+delta];
xTrue = [1; 1];
b = A*xTrue;
bPerturbed = b + [0; 1e-10];
x = A\b;
xPerturbed = A\bPerturbed;
fprintf('cond_2(A): %.3e\n', cond(A,2));
fprintf('relative input change: %.3e\n', norm(bPerturbed-b)/norm(b));
fprintf('relative solution change: %.3e\n', norm(xPerturbed-x)/norm(x));
