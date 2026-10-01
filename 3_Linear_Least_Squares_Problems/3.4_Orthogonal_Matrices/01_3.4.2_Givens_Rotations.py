# 01_3.4.2_Givens_Rotations

"""
Lecture: 3_Linear_Least_Squares_Problems/3.4_Orthogonal_Matrices
Content: 01_3.4.2_Givens_Rotations
"""

import numpy as np

def givens_rotation(a: float, b: float) -> tuple:
    """
    计算 Givens 旋转矩阵 G，使得 G [a; b] = [r; 0]

    输入:
        a - 向量的第一个分量
        b - 向量的第二个分量
    输出:
        G - Givens 旋转矩阵, 大小为 (2, 2)
        c - 余弦值
        s - 正弦值
    """
    if b == 0:
        c = 1
        s = 0
    else:
        if abs(b) > abs(a):
            tau = -a / b
            s = 1 / np.sqrt(1 + tau ** 2)
            c = s * tau
        else:
            tau = -b / a
            c = 1 / np.sqrt(1 + tau ** 2)
            s = c * tau
    
    # 构造 Givens 旋转矩阵 G
    G = np.array([[c, s], [-s, c]])
    
    return G, c, s

# 测试函数
def test_givens_rotation():
    # 示例向量分量
    a = 4
    b = 3
    
    # 计算 Givens 旋转矩阵 G 和旋转参数 c, s
    G, c, s = givens_rotation(a, b)
    
    # 打印结果
    print('Givens 旋转矩阵 G:')
    print(G)
    print('余弦值 c:')
    print(c)
    print('正弦值 s:')
    print(s)
    
    # 验证 Givens 旋转
    x = np.array([a, b])
    print('G * x:')
    print(np.dot(G, x))  # 应该是 [r, 0]，其中 r 为常数

# 运行测试函数
test_givens_rotation()