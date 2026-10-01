# 02_4.4.3_Orthogonal_Iteration

"""
Lecture: 4_Nonsymmetric_Eigenvalue_Problems/4.4_Algorithms_for_the_Nonsymmetric_Eigenproblem
Content: 02_4.4.3_Orthogonal_Iteration
"""

import numpy as np
from scipy.linalg import qr

def orthogonal_iteration(A, num_vectors, num_iter=1000, tol=1e-10):
    """
    使用正交迭代法计算矩阵的多个特征值和对应的特征向量

    参数:
        A (ndarray): 输入矩阵 (n, n)
        num_vectors (int): 需要计算的特征向量个数
        num_iter (int): 最大迭代次数
        tol (float): 收敛判定阈值

    返回:
        eigenvalues (ndarray): 计算得到的特征值
        eigenvectors (ndarray): 对应的特征向量矩阵，每列为一个特征向量
    """
    # 初始化
    n = A.shape[0]
    X = np.random.rand(n, num_vectors)  # 随机初始向量矩阵
    Q, _ = np.linalg.qr(X)  # QR分解确保初始向量正交

    for i in range(num_iter):
        Z = A @ Q  # 计算 Z = A * Q
        Q_new, R = np.linalg.qr(Z)  # QR分解 Z
        # 计算特征值
        eigenvalues = np.diag(R)
        # 检查收敛性
        if np.linalg.norm(Q - Q_new) < tol:
            break
        Q = Q_new

    eigenvectors = Q
    return eigenvalues, eigenvectors

# 测试函数
def test_orthogonal_iteration():
    # 定义一个测试矩阵
    A = np.array([[4, 1, 0],
                  [1, 4, 1],
                  [0, 1, 4]])

    # 需要计算的特征向量个数
    num_vectors = 3

    # 运行正交迭代法
    eigenvalues, eigenvectors = orthogonal_iteration(A, num_vectors)

    print("计算得到的特征值:")
    print(eigenvalues)
    print("对应的特征向量矩阵:")
    print(eigenvectors)

# 运行测试函数
test_orthogonal_iteration()
