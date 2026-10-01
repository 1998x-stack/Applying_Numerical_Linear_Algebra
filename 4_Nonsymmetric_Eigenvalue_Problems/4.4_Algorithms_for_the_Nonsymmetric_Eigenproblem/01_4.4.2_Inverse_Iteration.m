% 01_4.4.2_Inverse_Iteration

%

%Lecture: 4_Nonsymmetric_Eigenvalue_Problems/4.4_Algorithms_for_the_Nonsymmetric_Eigenproblem
%Content: 01_4.4.2_Inverse_Iteration

%
function [eigenvector, eigenvalue] = inverse_iteration(A, mu, num_iter, tol)
    % 使用逆迭代法计算矩阵接近给定值的特征值和对应的特征向量
    %
    % 参数:
    %   A (matrix): 输入矩阵 (n, n)
    %   mu (float): 目标特征值初值
    %   num_iter (int): 最大迭代次数
    %   tol (float): 收敛判定阈值
    %
    % 返回:
    %   eigenvector (vector): 对应的特征向量
    %   eigenvalue (float): 计算得到的特征值

    if nargin < 3
        num_iter = 1000; % 默认最大迭代次数
    end
    if nargin < 4
        tol = 1e-10; % 默认收敛阈值
    end

    % 初始化
    n = size(A, 1);
    x = rand(n, 1); % 随机初始向量
    x = x / norm(x); % 归一化

    I = eye(n); % 单位矩阵
    eigenvalue = 0;

    for i = 1:num_iter
        % 迭代计算 y = (A - mu * I)^{-1} * x
        y = (A - mu * I) \ x;

        % 计算新的特征向量
        x_new = y / norm(y);

        % 计算对应的特征值
        eigenvalue_new = x_new' * A * x_new;

        % 检查收敛性
        if abs(eigenvalue_new - eigenvalue) < tol
            break;
        end

        x = x_new;
        eigenvalue = eigenvalue_new;
    end

    eigenvector = x_new;
end

% 测试函数
function test_inverse_iteration()
    % 定义一个测试矩阵
    A = [4, 1, 0;
         1, 4, 1;
         0, 1, 4];

    % 目标特征值初值
    mu = 4;

    % 运行逆迭代法
    [eigenvector, eigenvalue] = inverse_iteration(A, mu);

    disp('计算得到的特征值:');
    disp(eigenvalue);
    disp('对应的特征向量:');
    disp(eigenvector);
end

% 运行测试函数
test_inverse_iteration();
