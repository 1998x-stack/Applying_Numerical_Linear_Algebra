# 00_4.4.1_Power_Method

"""
Lecture: 4_Nonsymmetric_Eigenvalue_Problems/4.4_Algorithms_for_the_Nonsymmetric_Eigenproblem
Content: 00_4.4.1_Power_Method
"""

import numpy as np

def power_method(A, num_iter=1000, tol=1e-10):
    """
    使用幂方法计算矩阵的主特征值和对应的特征向量

    参数:
        A (ndarray): 输入矩阵 (n, n)
        num_iter (int): 最大迭代次数
        tol (float): 收敛判定阈值

    返回:
        eigenvalue (float): 主特征值
        eigenvector (ndarray): 对应的特征向量
    """
    # 初始化
    n = A.shape[0]
    x = np.random.rand(n)  # 随机初始向量
    x = x / np.linalg.norm(x)  # 归一化

    eigenvalue = 0

    for _ in range(num_iter):
        # 迭代计算 y = A * x
        y = np.dot(A, x)

        # 计算新的特征向量
        x_new = y / np.linalg.norm(y)

        # 计算对应的特征值
        eigenvalue_new = np.dot(x_new.T, np.dot(A, x_new))

        # 检查收敛性
        if np.abs(eigenvalue_new - eigenvalue) < tol:
            break

        x = x_new
        eigenvalue = eigenvalue_new

    return eigenvalue, x

# 测试函数
def test_power_method():
    # 定义一个测试矩阵
    A = np.array([[4, 1],
                  [2, 3]])

    # 运行幂方法
    eigenvalue, eigenvector = power_method(A)

    print("主特征值:", eigenvalue)
    print("对应的特征向量:", eigenvector)

# 运行测试函数
test_power_method()
