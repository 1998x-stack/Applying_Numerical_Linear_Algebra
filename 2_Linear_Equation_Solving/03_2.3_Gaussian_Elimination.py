# 03_2.3_Gaussian_Elimination

"""
Lecture: /2_Linear_Equation_Solving
Content: 03_2.3_Gaussian_Elimination
"""

import numpy as np

def gaussian_elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    高斯消去法求解线性方程组 Ax = b
    :param A: 系数矩阵 (n x n)
    :param b: 常数向量 (n x 1)
    :return: 解向量 (n x 1)
    """
    n = len(b)
    
    # 增广矩阵
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    # 高斯消去过程（部分主元法）
    for k in range(n - 1):
        # 寻找列 k 中的最大主元
        max_index = np.argmax(np.abs(Ab[k:n, k])) + k
        
        # 交换行
        if max_index != k:
            Ab[[k, max_index]] = Ab[[max_index, k]]
        
        # 消去
        for i in range(k + 1, n):
            factor = Ab[i, k] / Ab[k, k]
            Ab[i, k:] -= factor * Ab[k, k:]
    
    # 回代过程
    x = np.zeros(n)
    x[-1] = Ab[-1, -1] / Ab[-1, -2]
    for i in range(n - 2, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]
    
    return x

# 测试高斯消去法
A = np.array([[2, -1, 1], [3, 3, 9], [3, 3, 5]], dtype=float)
b = np.array([2, -1, 4], dtype=float)
x = gaussian_elimination(A, b)
print('解向量 x:')
print(x)
