% 6.1 Iterative methods: a residual-based stopping rule
bNorm = 3.0;
residualNorm = 2e-9;
rtol = 1e-8;
atol = 1e-12;
threshold = max(rtol * bNorm, atol);
fprintf('residual = %.2e; threshold = %.2e\n', residualNorm, threshold);
if residualNorm <= threshold
    disp('The residual stopping test is satisfied.');
else
    disp('Continue iterating.');
end
