% Horner evaluation for descending-power coefficients.
coefficients = [2 -6 2 -1]; % 2*x^3 - 6*x^2 + 2*x - 1
x = 3;
value = coefficients(1);
for k = 2:numel(coefficients)
    value = value*x + coefficients(k);
end
fprintf('Horner p(3) = %.16g; polyval p(3) = %.16g\n', value, polyval(coefficients,x));

degree = numel(coefficients)-1;
numerator = 0;
for k = 1:numel(coefficients)
    numerator = numerator + abs(coefficients(k))*abs(x)^(degree-k+1);
end
denominator = abs(value);
if denominator == 0
    conditionNumber = Inf;
else
    conditionNumber = numerator/denominator;
end
fprintf('relative condition number = %.6g\n', conditionNumber);

% Bisection requires a continuous function and a sign-changing bracket.
p = @(z) polyval(coefficients,z);
low = 0; high = 3; tol = 1e-7;
fLow = p(low); fHigh = p(high);
if fLow == 0
    root = low;
elseif fHigh == 0
    root = high;
elseif sign(fLow) == sign(fHigh)
    error('The interval endpoints do not bracket a root.');
else
    while (high-low)/2 > tol
        mid = low+(high-low)/2;
        fMid = p(mid);
        if fMid == 0
            low = mid; high = mid; break;
        elseif sign(fMid) == sign(fLow)
            low = mid; fLow = fMid;
        else
            high = mid; fHigh = fMid;
        end
    end
    root = low+(high-low)/2;
end
fprintf('bisection root = %.10g\n', root);
