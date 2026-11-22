% Floating-point non-associativity and machine precision.
u = eps('double')/2;
large = 1e16;
leftAssociated = (large + (-large)) + 1;
rightAssociated = large + ((-large) + 1);
fprintf('binary64 unit roundoff: %.17g\n', u);
fprintf('(large-large)+1 = %.17g\n', leftAssociated);
fprintf('large+(-large+1) = %.17g\n', rightAssociated);
