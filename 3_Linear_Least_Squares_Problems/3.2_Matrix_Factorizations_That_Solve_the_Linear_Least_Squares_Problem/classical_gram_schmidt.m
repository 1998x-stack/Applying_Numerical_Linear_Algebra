function [Q, R] = classical_gram_schmidt(A)
    % 经典 Gram-Schmidt 正交化过程
    %
    % 输入:
    %     A - 输入矩阵, 大小为 (m, n)
    % 输出:
    %     Q - 正交矩阵, 大小为 (m, n)
    %     R - 上三角矩阵, 大小为 (n, n)
    
    [m, n] = size(A);  % 获取矩阵 A 的尺寸
    Q = zeros(m, n);   % 初始化正交矩阵 Q
    R = zeros(n, n);   % 初始化上三角矩阵 R
    
    for i = 1:n
        % 第一步: 将 a_i 赋值给 q_i
        q_i = A(:, i);
        
        % 第二步: 对于每一个已经计算出的 q_j (j < i), 进行正交化
        for j = 1:i-1
            R(j, i) = Q(:, j)' * A(:, i);  % 计算内积 q_j^T a_i
            q_i = q_i - R(j, i) * Q(:, j); % 进行正交化
        end
        
        % 第三步: 归一化 q_i
        R(i, i) = norm(q_i); % 计算 q_i 的二范数
        Q(:, i) = q_i / R(i, i); % 将 q_i 归一化
    end
end

% % 测试函数
% function test_classical_gram_schmidt()
%     A = [1, 1; 1, 2; 1, 3]; % 示例矩阵
%     [Q, R] = classical_gram_schmidt(A);
    
%     % 打印结果
%     disp('Q:');
%     disp(Q);
%     disp('R:');
%     disp(R);
%     disp('A:');
%     disp(A);
%     disp('Q * R:');
%     disp(Q * R);
% end

% % 运行测试函数
% test_classical_gram_schmidt();