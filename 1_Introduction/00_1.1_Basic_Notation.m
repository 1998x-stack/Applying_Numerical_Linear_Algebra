% Basic matrix/vector shape and complex adjoint conventions.
A = [1 2 3; 4 5 6];
x = [1; -1; 2];
y = A*x;
fprintf('size(A) = %d x %d\n', size(A,1), size(A,2));
fprintf('size(x) = %d x %d\n', size(x,1), size(x,2));
disp('A*x ='); disp(y);
C = [1+2i, 3-1i];
disp('C prime is conjugate transpose; C dot-prime is non-conjugating transpose.');
disp(C');
disp('Elementwise absolute value:'); disp(abs(C));
