% Linear-vs-circular convolution, no toolbox.
a=[1 2 1]; b=[1 -1];
linear=conv(a,b);
short=ifft(fft(a,3).*fft(b,3));
long=ifft(fft(a,4).*fft(b,4));
assert(norm(linear-[1 1 -1 -1])<1e-12);
assert(norm(real(short)-[0 1 -1])<1e-12);
assert(norm(real(long)-linear)<1e-12);
fprintf('L=3 aliases; L=4 recovers linear convolution.\n');
