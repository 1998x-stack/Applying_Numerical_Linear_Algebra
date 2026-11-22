% Chebyshev polynomial filter on interval [1,9]; no toolbox.
lambda = [1,3,6,9]; lo = 1; hi = 9;
for k = [1,3,5]
    t = (hi+lo-2*lambda)/(hi-lo);
    q = cos(k*acos(t))/cosh(k*acosh((hi+lo)/(hi-lo)));
    bound = 1/cosh(k*acosh(1.25));
    assert(max(abs(q)) <= bound+1e-12);
    fprintf('k=%d, worst-case bound=%.8f\n',k,bound);
end
