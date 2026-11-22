% Theory-only work estimate for dense n-by-n matrix multiplication.
for n = [32 128 512]
    flops = 2*n^3;
    idealizedBytes = 3*n^2*8; % read A, read B, write C once
    intensity = flops/idealizedBytes;
    fprintf('n=%d: %.0f FLOPs, %.0f idealized bytes, %.3f FLOP/byte\n', ...
        n, flops, idealizedBytes, intensity);
end
% These are analytical estimates, not measured timings.
