% Use the solver interface and validate its residual; do not form inv(A)*b.
A = [3 1; 1 2];
b = [9; 8];
x = A\b;
r = A*x-b;
backwardError = norm(r)/(norm(A,'fro')*norm(x)+norm(b));
fprintf('solution = [%g; %g]\n', x(1), x(2));
fprintf('residual norm = %.3e\n', norm(r));
fprintf('normalized backward error = %.3e\n', backwardError);
