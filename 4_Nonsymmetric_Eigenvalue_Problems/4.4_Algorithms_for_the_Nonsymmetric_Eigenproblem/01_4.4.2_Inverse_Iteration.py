# 01_4.4.2_Inverse_Iteration

"""
Lecture: 4_Nonsymmetric_Eigenvalue_Problems/4.4_Algorithms_for_the_Nonsymmetric_Eigenproblem
Content: 01_4.4.2_Inverse_Iteration
"""

import numpy as np

def inverse_iteration(A, mu, num_iter=1000, tol=1e-10):
    """
    使用逆迭代法计算矩阵接近给定值的特征值和对应的特征向量

    参数:
        A (ndarray): 输入矩阵 (n, n)
        mu (float): 目标特征值初值
        num_iter (int): 最大迭代次数
        tol (float): 收敛判定阈值

    返回:
        eigenvector (ndarray): 对应的特征向量
        eigenvalue (float): 计算得到的特征值
    """
    # 初始化
    n = A.shape[0]
    x = np.random.rand(n)  # 随机初始向量
    x = x / np.linalg.norm(x)  # 归一化

    I = np.eye(n)  # 单位矩阵
    eigenvalue = 0

    for _ in range(num_iter):
        # 迭代计算 y = (A - mu * I)^{-1} * x
        y = np.linalg.solve(A - mu * I, x)

        # 计算新的特征向量
        x_new = y / np.linalg.norm(y)

        # 计算对应的特征值
        eigenvalue_new = np.dot(x_new.T, np.dot(A, x_new))

        # 检查收敛性
        if np.abs(eigenvalue_new - eigenvalue) < tol:
            break

        x = x_new
        eigenvalue = eigenvalue_new

    return x, eigenvalue

# 测试函数
def test_inverse_iteration():
    # 定义一个测试矩阵
    A = np.array([[4, 1, 0],
                  [1, 4, 1],
                  [0, 1, 4]])

    # 目标特征值初值
    mu = 4

    # 运行逆迭代法
    eigenvector, eigenvalue = inverse_iteration(A, mu)

    print("计算得到的特征值:", eigenvalue)
    print("对应的特征向量:", eigenvector)

# 运行测试函数
test_inverse_iteration()