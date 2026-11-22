% BLAS levels with explicit dimensions and traffic models.
n=64; x=(1:n)'; y=ones(n,1); A=reshape(1:n*n,n,n); B=eye(n);
axpy=2*x+y; gemv=A*x; gemm=A*B+A;
I1=(2*n)/(24*n);
I2=(2*n^2)/(8*n^2+16*n);
I3=(2*n^3)/(32*n^2);
fprintf('AXPY I=%.5f, GEMV I=%.5f, GEMM ideal I=%.5f FLOP/byte\n',I1,I2,I3);
assert(all(axpy==2*x+y));
assert(norm(gemv-A*x)==0);
assert(norm(gemm-2*A,'fro')==0);
assert(I3>I2 && I2>I1);
