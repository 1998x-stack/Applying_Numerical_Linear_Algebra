% 03_2.3_Gaussian_Elimination

%

%Lecture: /2_Linear_Equation_Solving
%Content: 03_2.3_Gaussian_Elimination

%
function x = gaussian_elimination(A, b)
    % 高斯消去法求解线性方程组 Ax = b
    % 输入:
    %   A - 系数矩阵 (n x n)
    %   b - 常数向量 (n x 1)
    % 输出:
    %   x - 解向量 (n x 1)

    % 获取矩阵 A 的维度
    [n, ~] = size(A);

    % 构造增强矩阵
    Ab = [A b];

    % 高斯消去过程（部分主元法）
    for k = 1:n-1
        % 寻找列 k 中的最大主元
        [~, max_index] = max(abs(Ab(k:n, k)));
        max_index = max_index + k - 1;

        % 交换行
        if max_index ~= k
            Ab([k max_index], :) = Ab([max_index k], :);
        end

        % 消去
        for i = k+1:n
            factor = Ab(i, k) / Ab(k, k);
            Ab(i, k:n+1) = Ab(i, k:n+1) - factor * Ab(k, k:n+1);
        end
    end

    % 回代过程
    x = zeros(n, 1);
    x(n) = Ab(n, end) / Ab(n, n);
    for i = n-1:-1:1
        x(i) = (Ab(i, end) - Ab(i, i+1:n) * x(i+1:n)) / Ab(i, i);
    end
end

% 测试高斯消去法
A = [2 -1 1; 3 3 9; 3 3 5];
b = [2; -1; 4];
x = gaussian_elimination(A, b);
disp('解向量 x:');
disp(x);
