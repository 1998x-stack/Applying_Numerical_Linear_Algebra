% 00_4.4.1_Power_Method

%

%Lecture: 4_Nonsymmetric_Eigenvalue_Problems/4.4_Algorithms_for_the_Nonsymmetric_Eigenproblem
%Content: 00_4.4.1_Power_Method

%
function [eigenvalue, eigenvector] = power_method(A, num_iter, tol)
    % 使用幂方法计算矩阵的主特征值和对应的特征向量
    %
    % 参数:
    %   A (matrix): 输入矩阵 (n, n)
    %   num_iter (int): 最大迭代次数
    %   tol (float): 收敛判定阈值
    %
    % 返回:
    %   eigenvalue (float): 主特征值
    %   eigenvector (vector): 对应的特征向量

    if nargin < 2
        num_iter = 1000; % 默认最大迭代次数
    end
    if nargin < 3
        tol = 1e-10; % 默认收敛阈值
    end

    % 初始化
    n = size(A, 1);
    x = rand(n, 1); % 随机初始向量
    x = x / norm(x); % 归一化

    eigenvalue = 0;

    for i = 1:num_iter
        % 迭代计算 y = A * x
        y = A * x;

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

    eigenvalue = eigenvalue_new;
    eigenvector = x_new;
end

% 测试函数
function test_power_method()
    % 定义一个测试矩阵
    A = [4, 1;
         2, 3];

    % 运行幂方法
    [eigenvalue, eigenvector] = power_method(A);

    disp('主特征值:');
    disp(eigenvalue);
    disp('对应的特征向量:');
    disp(eigenvector);
end

% 运行测试函数
test_power_method();
