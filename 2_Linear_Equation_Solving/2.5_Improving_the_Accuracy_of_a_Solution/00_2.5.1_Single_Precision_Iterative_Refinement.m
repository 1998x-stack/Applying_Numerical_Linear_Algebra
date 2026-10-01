% 00_2.5.1_Single_Precision_Iterative_Refinement

%

%Lecture: 2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution
%Content: 00_2.5.1_Single_Precision_Iterative_Refinement

%
function x = single_precision_iterative_refinement(A, b, tol, max_iter)
    % 单精度迭代改进求解线性方程组 Ax = b
    % 输入:
    %   A - 系数矩阵 (n x n)
    %   b - 常数向量 (n x 1)
    %   tol - 误差容限
    %   max_iter - 最大迭代次数
    % 输出:
    %   x - 精确解向量 (n x 1)

    % 将矩阵和向量转换为单精度
    A_single = single(A);
    b_single = single(b);
    
    % 初始解（单精度）
    x = A_single \ b_single;
    
    % 迭代改进过程
    for k = 1:max_iter
        % 计算残差（双精度）
        r = b - double(A) * double(x);
        
        % 求解修正方程（单精度）
        d = A_single \ single(r);
        
        % 更新解（双精度）
        x = x + double(d);
        
        % 检查收敛性
        if norm(r, inf) < tol
            break;
        end
    end
end

% 测试单精度迭代改进
A = [2 -1 1; 3 3 9; 3 3 5];
b = [2; -1; 4];
tol = 1e-6;
max_iter = 10;

x = single_precision_iterative_refinement(A, b, tol, max_iter);
disp('精确解向量 x:');
disp(x);
