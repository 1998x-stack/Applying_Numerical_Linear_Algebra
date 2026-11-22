% Plane Givens rotation with convention [c s;-s c].
a=3;b=4;r=hypot(a,b);c=a/r;s=b/r;
G=[c s;-s c];y=G*[a;b];
assert(norm(y-[5;0])<1e-12);
assert(norm(G'*G-eye(2))<1e-12);
H=eye(3);H([1,3],[1,3])=G;
A=[3 1;8 9;4 2];B=H*A;
assert(abs(B(3,1))<1e-12);
assert(norm(B(2,:)-A(2,:))<1e-12);
disp(B);
