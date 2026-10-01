% 02_4.4.3_Orthogonal_Iteration

%

%Lecture: 4_Nonsymmetric_Eigenvalue_Problems/4.4_Algorithms_for_the_Nonsymmetric_Eigenproblem
%Content: 02_4.4.3_Orthogonal_Iteration

%
function [eigenvalues, eigenvectors] = orthogonal_iteration(A, num_vectors, num_iter, tol)
    % 使用正交迭代法计算矩阵的多个特征值和对应的特征向量
    %
    % 参数:
    %   A (matrix): 输入矩阵 (n, n)
    %   num_vectors (int): 需要计算的特征向量个数
    %   num_iter (int): 最大迭代次数
    %   tol (float): 收敛判定阈值
    %
    % 返回:
    %   eigenvalues (vector): 计算得到的特征值
    %   eigenvectors (matrix): 对应的特征向量矩阵，每列为一个特征向量

    if nargin < 3
        num_iter = 1000; % 默认最大迭代次数
    end
    if nargin < 4
        tol = 1e-10; % 默认收敛阈值
    end

    % 初始化
    n = size(A, 1);
    X = rand(n, num_vectors); % 随机初始向量矩阵
    [Q, ~] = qr(X, 0); % QR分解确保初始向量正交

    for i = 1:num_iter
        Z = A * Q; % 计算 Z = A * Q
        [Q_new, R] = qr(Z, 0); % QR分解 Z
        % 计算特征值
        eigenvalues = diag(R);
        % 检查收敛性
        if norm(Q - Q_new, 'fro') < tol
            break;
        end
        Q = Q_new;
    end

    eigenvectors = Q;
end

% 测试函数
function test_orthogonal_iteration()
    % 定义一个测试矩阵
    A = [4, 1, 0;
         1, 4, 1;
         0, 1, 4];

    % 需要计算的特征向量个数
    num_vectors = 3;

    % 运行正交迭代法
    [eigenvalues, eigenvectors] = orthogonal_iteration(A, num_vectors);

    disp('计算得到的特征值:');
    disp(eigenvalues);
    disp('对应的特征向量矩阵:');
    disp(eigenvectors);
end

% 运行测试函数
test_orthogonal_iteration();
