% Hypothetical roofline and Amdahl, not measured hardware speed.
peak=200; beta=50; densities=[1 2 4 8];
ceilings=min(peak,beta*densities);
fprintf('I=%.1f, predicted upper bound GFLOP/s=%.1f\n',[densities;ceilings]);
assert(all(ceilings==[50 100 200 200]));
f=0.2; processors=[1 2 4 16];
speedup=1./(f+(1-f)./processors);
assert(abs(speedup(1)-1)<1e-12);
assert(all(speedup<1/f));
