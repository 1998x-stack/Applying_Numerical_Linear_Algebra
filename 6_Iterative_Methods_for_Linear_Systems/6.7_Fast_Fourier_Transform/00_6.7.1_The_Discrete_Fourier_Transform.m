% Explicit DFT and Parseval without toolbox, MATLAB/Octave.
x=[1;2;0;0]; N=length(x); j=(0:N-1)'; k=0:N-1;
F=exp(-2i*pi*(j*k)/N);
X=F*x; exact=[3;1-2i;-1;1+2i];
assert(norm(X-exact)<1e-12);
assert(norm(ifft(X)-x)<1e-12);
assert(abs(sum(abs(x).^2)-sum(abs(X).^2)/N)<1e-12);
disp(X);
