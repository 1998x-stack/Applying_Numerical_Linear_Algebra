% One radix-2 butterfly merge, checked against MATLAB FFT.
x=[1;2;3;4;0;0;0;0]; n=length(x);
E=fft(x(1:2:end)); O=fft(x(2:2:end));
w=exp(-2i*pi*(0:n/2-1)'/n);
X=[E+w.*O; E-w.*O];
assert(norm(X-fft(x))<1e-12);
assert(norm(ifft(X)-x)<1e-12);
disp(X);
