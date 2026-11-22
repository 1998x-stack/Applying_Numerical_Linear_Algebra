% 6.4 Qualitative complexity table for the 2D Poisson model
methods = ["Jacobi"; "Gauss-Seidel"; "CG"; "SOR"; "FFT"; "Multigrid"];
timeOrder = ["O(n^2)"; "O(n^2)"; "O(n^(3/2))"; "O(n^(3/2))"; "O(n log n)"; "O(n)"];
spaceOrder = repmat("O(n)",size(methods));
disp(table(methods,timeOrder,spaceOrder));
disp('Orders assume a regular 2D Poisson model and a fixed error target; not benchmark timings.');
