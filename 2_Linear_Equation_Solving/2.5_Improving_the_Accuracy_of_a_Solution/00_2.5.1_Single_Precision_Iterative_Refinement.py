# 00_2.5.1_Single_Precision_Iterative_Refinement

"""
Lecture: 2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution
Content: 00_2.5.1_Single_Precision_Iterative_Refinement
"""

import numpy as np

def single_precision_iterative_refinement(A, b, tol=1e-6, max_iter=10):
    """
    单精度迭代改进求解线性方程组 Ax = b
    :param A: 系数矩阵 (n x n)
    :param b: 常数向量 (n x 1)
    :param tol: 误差容限
    :param max_iter: 最大迭代次数
    :return: 精确解向量 (n x 1)
    """
    # 将矩阵和向量转换为单精度
    A_single = A.astype(np.float32)
    b_single = b.astype(np.float32)
    
    # 初始解（单精度）
    x = np.linalg.solve(A_single, b_single).astype(np.float64)
    
    for k in range(max_iter):
        # 计算残差（双精度）
        r = b - np.dot(A, x)
        
        # 求解修正方程（单精度）
        d = np.linalg.solve(A_single, r.astype(np.float32)).astype(np.float64)
        
        # 更新解（双精度）
        x += d
        
        # 检查收敛性
        if np.linalg.norm(r, np.inf) < tol:
            break
    
    return x

# 测试单精度迭代改进
A = np.array([[2, -1, 1], [3, 3, 9], [3, 3, 5]], dtype=np.float64)
b = np.array([2, -1, 4], dtype=np.float64)
tol = 1e-6
max_iter = 10

x = single_precision_iterative_refinement(A, b, tol, max_iter)
print('精确解向量 x:')
print(x)
