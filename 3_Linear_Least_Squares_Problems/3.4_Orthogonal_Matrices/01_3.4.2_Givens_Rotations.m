% 01_3.4.2_Givens_Rotations

%

%Lecture: 3_Linear_Least_Squares_Problems/3.4_Orthogonal_Matrices
%Content: 01_3.4.2_Givens_Rotations

%
function [G, c, s] = givens_rotation(a, b)
    % 计算 Givens 旋转矩阵 G，使得 G [a; b] = [r; 0]
    % 输入:
    %   a - 向量的第一个分量
    %   b - 向量的第二个分量
    % 输出:
    %   G - Givens 旋转矩阵
    %   c - 余弦值
    %   s - 正弦值

    if b == 0
        c = 1;
        s = 0;
    else
        if abs(b) > abs(a)
            tau = -a / b;
            s = 1 / sqrt(1 + tau^2);
            c = s * tau;
        else
            tau = -b / a;
            c = 1 / sqrt(1 + tau^2);
            s = c * tau;
        end
    end
    
    % 构造 Givens 旋转矩阵 G
    G = [c, s; -s, c];
end

% 测试函数
function test_givens_rotation()
    % 示例向量分量
    a = 4;
    b = 3;
    
    % 计算 Givens 旋转矩阵 G 和旋转参数 c, s
    [G, c, s] = givens_rotation(a, b);
    
    % 打印结果
    disp('Givens 旋转矩阵 G:');
    disp(G);
    disp('余弦值 c:');
    disp(c);
    disp('正弦值 s:');
    disp(s);
    
    % 验证 Givens 旋转
    x = [a; b];
    disp('G * x:');
    disp(G * x);  % 应该是 [r; 0]，其中 r 为常数
end

% 运行测试函数
test_givens_rotation();