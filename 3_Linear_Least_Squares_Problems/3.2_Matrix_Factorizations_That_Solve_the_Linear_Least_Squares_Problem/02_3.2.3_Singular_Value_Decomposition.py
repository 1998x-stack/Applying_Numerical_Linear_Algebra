# 02_3.2.3_Singular_Value_Decomposition

"""
Lecture: 3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem
Content: 02_3.2.3_Singular_Value_Decomposition
"""

import numpy as np

def compute_svd(A):
    """
    从头开始计算矩阵 A 的奇异值分解 (SVD)
    
    输入:
        A - 输入矩阵, 大小为 (m, n)
    输出:
        U - 左奇异向量矩阵, 大小为 (m, m)
        Sigma - 奇异值对角矩阵, 大小为 (m, n)
        Vt - 右奇异向量矩阵的转置, 大小为 (n, n)
    """
    # 计算 A^T A 的特征值和特征向量
    AtA = np.dot(A.T, A)
    eigenvalues, V = np.linalg.eigh(AtA)
    
    # 将特征值按降序排列
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    V = V[:, idx]
    
    # 计算奇异值
    singular_values = np.sqrt(eigenvalues)
    
    # 构造奇异值对角矩阵 Sigma
    m, n = A.shape
    Sigma = np.zeros((m, n))
    np.fill_diagonal(Sigma, singular_values)
    
    # 计算左奇异向量矩阵 U
    U = np.zeros((m, m))
    for i in range(n):
        U[:, i] = np.dot(A, V[:, i]) / singular_values[i]
    
    # 如果 m > n，填充 U 的剩余列
    if m > n:
        for i in range(n, m):
            # 选择一个正交于前 n 个列的随机向量
            u = np.random.rand(m)
            for j in range(i):
                u -= np.dot(U[:, j], u) * U[:, j]
            U[:, i] = u / np.linalg.norm(u)
    
    return U, Sigma, V.T

# 测试函数
def test_compute_svd():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)  # 示例矩阵
    U, Sigma, Vt = compute_svd(A)

    # 打印结果
    print('U:')
    print(U)
    print('Sigma:')
    print(Sigma)
    print('Vt:')
    print(Vt)
    print('A:')
    print(A)
    print('U @ Sigma @ Vt:')
    print(U @ Sigma @ Vt)

# 运行测试函数
test_compute_svd()
