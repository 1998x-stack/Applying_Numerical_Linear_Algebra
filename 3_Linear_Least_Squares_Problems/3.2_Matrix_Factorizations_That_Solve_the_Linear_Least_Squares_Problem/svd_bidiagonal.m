function [U, Sigma, V] = compute_svd_bidiagonal(A)
    % 计算矩阵 A 的奇异值分解 (SVD) 基于双对角化方法
    % 输入:
    %   A - 输入矩阵, 大小为 (m, n)
    % 输出:
    %   U - 左奇异向量矩阵, 大小为 (m, m)
    %   Sigma - 奇异值对角矩阵, 大小为 (m, n)
    %   V - 右奇异向量矩阵, 大小为 (n, n)

    [m, n] = size(A);  % 获取矩阵 A 的尺寸

    % 双对角化
    [U, B, V] = bidiagonalize(A);

    % 对双对角矩阵 B 进行 SVD 分解
    [U_B, Sigma, V_B] = svd_bidiagonal(B);

    % 恢复原矩阵的 SVD
    U = U * U_B;
    V = V * V_B;
end

function [U, B, V] = bidiagonalize(A)
    % 将矩阵 A 转换为双对角矩阵 B
    % 输入:
    %   A - 输入矩阵
    % 输出:
    %   U - 左正交矩阵
    %   B - 双对角矩阵
    %   V - 右正交矩阵

    [m, n] = size(A);
    U = eye(m);
    V = eye(n);
    B = A;

    for i = 1:min(m, n)
        % Householder 反射将第 i 列的下面部分变为零
        [U_i, beta] = householder(B(i:m, i));
        U_i = eye(m - i + 1) - beta * U_i * U_i';
        B(i:m, i:n) = U_i * B(i:m, i:n);
        U(i:m, i:m) = U(i:m, i:m) * U_i;

        if i <= n - 2
            % Householder 反射将第 i 行的右边部分变为零
            [V_i, beta] = householder(B(i, i+1:n)');
            V_i = eye(n - i) - beta * V_i * V_i';
            B(i:m, i+1:n) = B(i:m, i+1:n) * V_i;
            V(i+1:n, i+1:n) = V(i+1:n, i+1:n) * V_i;
        end
    end
end

function [v, beta] = householder(x)
    % 计算 Householder 向量
    % 输入:
    %   x - 输入向量
    % 输出:
    %   v - Householder 向量
    %   beta - Householder 反射参数

    sigma = x(2:end)' * x(2:end);
    v = [1; x(2:end)];
    if sigma == 0 && x(1) >= 0
        beta = 0;
    elseif sigma == 0 && x(1) < 0
        beta = -2;
    else
        mu = sqrt(x(1)^2 + sigma);
        if x(1) <= 0
            v(1) = x(1) - mu;
        else
            v(1) = -sigma / (x(1) + mu);
        end
        beta = 2 * v(1)^2 / (sigma + v(1)^2);
        v = v / v(1);
    end
end

function [U, Sigma, V] = svd_bidiagonal(B)
    % 对双对角矩阵 B 进行 SVD 分解
    % 输入:
    %   B - 双对角矩阵
    % 输出:
    %   U - 左奇异向量矩阵
    %   Sigma - 奇异值对角矩阵
    %   V - 右奇异向量矩阵

    [U, Sigma, V] = svd(B);  % 直接对双对角矩阵 B 进行 SVD 分解
end

% 测试函数
function test_compute_svd_bidiagonal()
    A = [1, 2, 3; 4, 5, 6; 7, 8, 9];  % 示例矩阵
    [U, Sigma, V] = compute_svd_bidiagonal(A);

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
test_compute_svd_bidiagonal();
