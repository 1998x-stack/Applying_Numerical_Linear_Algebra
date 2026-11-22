% 6.2 Solver selection by matrix structure
problem = 'spd'; % choose: spd, symmetric-indefinite, nonsymmetric, least-squares
switch problem
    case 'spd'
        disp('Candidate: CG. Verify A is symmetric positive definite.');
    case 'symmetric-indefinite'
        disp('Candidate: MINRES. Verify symmetry and inspect preconditioner requirements.');
    case 'nonsymmetric'
        disp('Candidate: GMRES or BiCGSTAB. Check restart, memory and true residual.');
    case 'least-squares'
        disp('Candidate: LSQR or LSMR for the rectangular least-squares problem.');
    otherwise
        error('Unknown problem structure.');
end
