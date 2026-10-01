% 02_3.2.3_Singular_Value_Decomposition

%

%Lecture: 3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem
%Content: 02_3.2.3_Singular_Value_Decomposition

%
function [U, Sigma, V] = compute_svd(A)
    % 计算矩阵 A 的奇异值分解 (SVD)
    % 输入:
    %   A - 输入矩阵, 大小为 (m, n)
    % 输出:
    %   U - 左奇异向量矩阵, 大小为 (m, m)
    %   Sigma - 奇异值对角矩阵, 大小为 (m, n)
    %   V - 右奇异向量矩阵, 大小为 (n, n)

    [m, n] = size(A);  % 获取矩阵 A 的尺寸

    % 计算 A^T A 的特征值和特征向量
    [V, D] = eig(A' * A);  % D 是对角矩阵，包含特征值
    [eigenvalues, idx] = sort(diag(D), 'descend');  % 特征值按降序排列
    V = V(:, idx);  % 重排特征向量

    % 计算奇异值
    singular_values = sqrt(eigenvalues);
    
    % 构造奇异值对角矩阵 Sigma
    Sigma = zeros(m, n);
    for i = 1:min(m, n)
        Sigma(i, i) = singular_values(i);
    end

    % 计算左奇异向量矩阵 U
    U = zeros(m, m);
    for i = 1:n
        U(:, i) = A * V(:, i) / singular_values(i);
    end

    % 如果 m > n，填充 U 的剩余列
    if m > n
        for i = n+1:m
            u = rand(m, 1);  % 选择一个随机向量
            for j = 1:i-1
                u = u - (U(:, j)' * u) * U(:, j);  % 进行正交化
            end
            U(:, i) = u / norm(u);  % 归一化
        end
    end
end

% 测试函数
function test_compute_svd()
    A = [1, 2, 3; 4, 5, 6; 7, 8, 9];  % 示例矩阵
    [U, Sigma, V] = compute_svd(A);

    % 打印结果
    disp('U:');
    disp(U);
    disp('Sigma:');
    disp(Sigma);
    disp('V:');
    disp(V);
    disp('A:');
    disp(A);
    disp('U * Sigma * V'':');
    disp(U * Sigma * V');
end

% 运行测试函数
test_compute_svd();
