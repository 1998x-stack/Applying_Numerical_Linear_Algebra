# 00_3.4.1_Householder_Transformations

"""
Lecture: 3_Linear_Least_Squares_Problems/3.4_Orthogonal_Matrices
Content: 00_3.4.1_Householder_Transformations
"""

import numpy as np

def householder_transformation(x: np.ndarray) -> tuple:
    """
    计算 Householder 变换矩阵 P 和向量 u

    输入:
        x - 输入向量, 大小为 (n,)
    输出:
        P - Householder 变换矩阵, 大小为 (n, n)
        u - Householder 向量, 大小为 (n,)
    """
    # 计算向量 x 的 2-范数
    x_norm = np.linalg.norm(x)
    
    # 构造向量 e1，大小与 x 相同，只有第一个元素为 1
    e1 = np.zeros_like(x)
    e1[0] = 1
    
    # 计算 Householder 向量 u
    u = x + np.sign(x[0]) * x_norm * e1
    u = u / np.linalg.norm(u)  # 归一化
    
    # 计算 Householder 变换矩阵 P
    P = np.eye(len(x)) - 2 * np.outer(u, u)
    
    return P, u

# 测试函数
def test_householder_transformation():
    # 示例向量
    x = np.array([4, 1, 1], dtype=float)
    
    # 计算 Householder 变换矩阵 P 和向量 u
    P, u = householder_transformation(x)
    
    # 打印结果
    print('Householder 变换矩阵 P:')
    print(P)
    print('Householder 向量 u:')
    print(u)
    print('P * x:')
    print(np.dot(P, x))  # 应该是 [c, 0, 0]，其中 c 为常数

# 运行测试函数
test_householder_transformation()