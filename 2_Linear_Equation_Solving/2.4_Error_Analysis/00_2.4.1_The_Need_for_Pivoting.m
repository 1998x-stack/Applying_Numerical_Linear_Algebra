% Inspect pivot multiplier size; no experiment speed claim.
tiny=1e-4;
A=[tiny 1;1 1]; b=A*[1;1];
mNoPivot=1/tiny; mPivot=tiny;
[L,U,P]=lu(A); x=U\(L\(P*b));
fprintf('multipliers: no pivot=%g, pivot=%g\n',mNoPivot,mPivot);
assert(mNoPivot==1e4 && abs(mPivot-1e-4)<1e-15);
assert(norm(A*x-b)<1e-12);
