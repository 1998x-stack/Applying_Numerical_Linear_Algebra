% 00_3.2.1_Normal_Equations

%

%Lecture: 3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem
%Content: 00_3.2.1_Normal_Equations

%
function [x, residuals] = normal_equations_solver(A, b)
    % 正规方程法求解线性最小二乘问题
    %
    % Args:
    %     A: 输入矩阵，大小为 (m, n)
    %     b: 目标向量，大小为 (m, 1)
    %
    % Returns:
    %     x: 解向量，大小为 (n, 1)
    %     residuals: 残差向量，大小为 (m, 1)
    
    % 计算 A^T A 和 A^T b
    A_T_A = A' * A;
    A_T_b = A' * b;
    
    % 求解正规方程 A^T A x = A^T b
    x = A_T_A \ A_T_b;
    
    % 计算残差
    residuals = b - A * x;
end

% 主函数，演示如何使用 normal_equations_solver 函数
function main()
    % 示例矩阵 A 和向量 b
    A = [1, 1; 1, 2; 1, 3];
    b = [1; 2; 2.5];
    
    % 使用正规方程法求解
    [x, residuals] = normal_equations_solver(A, b);
    
    % 打印结果
    fprintf('Solution vector x:\n');
    disp(x);
    
    fprintf('Residuals:\n');
    disp(residuals);
end

% 运行主函数
main();