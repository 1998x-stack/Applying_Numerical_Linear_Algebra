% 00_3.4.1_Householder_Transformations

%

%Lecture: 3_Linear_Least_Squares_Problems/3.4_Orthogonal_Matrices
%Content: 00_3.4.1_Householder_Transformations

%
function [P, u] = householder(x)
    % 计算 Householder 变换矩阵 P 和向量 u
    % 输入:
    %   x - 输入向量
    % 输出:
    %   P - Householder 变换矩阵
    %   u - Householder 向量

    % 计算向量 x 的 2-范数
    x_norm = norm(x);
    
    % 构造向量 e1，大小与 x 相同，只有第一个元素为 1
    e1 = zeros(size(x));
    e1(1) = 1;
    
    % 计算 Householder 向量 u
    u = x + sign(x(1)) * x_norm * e1;
    u = u / norm(u);  % 归一化
    
    % 计算 Householder 变换矩阵 P
    P = eye(length(x)) - 2 * (u * u');
end

% 测试函数
function test_householder()
    % 示例向量
    x = [4; 1; 1];
    
    % 计算 Householder 变换矩阵 P 和向量 u
    [P, u] = householder(x);
    
    % 打印结果
    disp('Householder 变换矩阵 P:');
    disp(P);
    disp('Householder 向量 u:');
    disp(u);
    disp('P * x:');
    disp(P * x);  % 应该是 [c; 0; 0]，其中 c 为常数
end

% 运行测试函数
test_householder();
