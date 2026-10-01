# 01_3.2.2_QR_Decomposition

"""
Lecture: 3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem
Content: 01_3.2.2_QR_Decomposition
"""

import numpy as np

def classical_gram_schmidt(A: np.ndarray) -> tuple:
    """
    经典 Gram-Schmidt 正交化过程

    输入:
        A - 输入矩阵, 大小为 (m, n)
    输出:
        Q - 正交矩阵, 大小为 (m, n)
        R - 上三角矩阵, 大小为 (n, n)
    """
    m, n = A.shape  # 获取矩阵 A 的尺寸
    Q = np.zeros((m, n))  # 初始化正交矩阵 Q
    R = np.zeros((n, n))  # 初始化上三角矩阵 R
    
    for i in range(n):
        # 第一步: 将 a_i 赋值给 q_i
        q_i = A[:, i].copy()
        
        # 第二步: 对于每一个已经计算出的 q_j (j < i), 进行正交化
        for j in range(i):
            R[j, i] = np.dot(Q[:, j], A[:, i])  # 计算内积 q_j^T a_i
            q_i -= R[j, i] * Q[:, j]  # 进行正交化
        
        # 第三步: 归一化 q_i
        R[i, i] = np.linalg.norm(q_i)  # 计算 q_i 的二范数
        Q[:, i] = q_i / R[i, i]  # 将 q_i 归一化
    
    return Q, R

# 测试函数
def test_classical_gram_schmidt():
    A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)  # 示例矩阵
    Q, R = classical_gram_schmidt(A)
    
    # 打印结果
    print('Q:')
    print(Q)
    print('R:')
    print(R)
    print('A:')
    print(A)
    print('Q @ R:')
    print(Q @ R)

# 运行测试函数
test_classical_gram_schmidt()

import numpy as np

def modified_gram_schmidt(A: np.ndarray) -> tuple:
    """
    修正 Gram-Schmidt 正交化过程

    输入:
        A - 输入矩阵, 大小为 (m, n)
    输出:
        Q - 正交矩阵, 大小为 (m, n)
        R - 上三角矩阵, 大小为 (n, n)
    """
    m, n = A.shape  # 获取矩阵 A 的尺寸
    Q = np.zeros((m, n))  # 初始化正交矩阵 Q
    R = np.zeros((n, n))  # 初始化上三角矩阵 R
    
    for i in range(n):
        # 第一步: 将 a_i 赋值给 q_i
        q_i = A[:, i].copy()
        
        # 第二步: 归一化 q_i
        R[i, i] = np.linalg.norm(q_i)  # 计算 q_i 的二范数
        Q[:, i] = q_i / R[i, i]  # 将 q_i 归一化
        
        # 第三步: 对于每一个后续的向量 a_j (j > i), 进行正交化
        for j in range(i + 1, n):
            R[i, j] = np.dot(Q[:, i], A[:, j])  # 计算内积 q_i^T a_j
            A[:, j] -= R[i, j] * Q[:, i]  # 进行正交化
    
    return Q, R

# 测试函数
def test_modified_gram_schmidt():
    A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)  # 示例矩阵
    Q, R = modified_gram_schmidt(A)
    
    # 打印结果
    print('Q:')
    print(Q)
    print('R:')
    print(R)
    print('A:')
    print(A)
    print('Q @ R:')
    print(Q @ R)

# 运行测试函数
test_modified_gram_schmidt()


import numpy as np

def householder_reflection(A: np.ndarray) -> tuple:
    """
    使用 Householder 反射进行 QR 分解

    输入:
        A - 输入矩阵, 大小为 (m, n)
    输出:
        Q - 正交矩阵, 大小为 (m, m)
        R - 上三角矩阵, 大小为 (m, n)
    """
    m, n = A.shape  # 获取矩阵 A 的尺寸
    Q = np.eye(m)  # 初始化正交矩阵 Q 为单位矩阵
    R = A.copy()  # 初始化 R 为 A 的副本

    for i in range(n):
        # 提取当前列向量 x
        x = R[i:m, i]
        # 计算 Householder 向量 u
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        u = x - e
        u = u / np.linalg.norm(u)

        # 构建 Householder 矩阵 P
        P = np.eye(m - i) - 2 * np.outer(u, u)

        # 扩展 P 矩阵到与 A 相同的尺寸
        P_full = np.eye(m)
        P_full[i:m, i:m] = P

        # 更新 R 矩阵
        R = P_full @ R

        # 更新 Q 矩阵
        Q = Q @ P_full

    return Q, R

# 测试函数
def test_householder_reflection():
    A = np.array([[4, 1], [3, 3], [0, 4]], dtype=float)  # 示例矩阵
    Q, R = householder_reflection(A)

    # 打印结果
    print('Q:')
    print(Q)
    print('R:')
    print(R)
    print('A:')
    print(A)
    print('Q @ R:')
    print(Q @ R)

# 运行测试函数
test_householder_reflection()


import numpy as np

def givens_rotation(a, b):
    """
    计算 Givens 旋转矩阵 G，使得 G [a; b] = [r; 0]
    
    输入:
        a - 向量的第一个分量
        b - 向量的第二个分量
    输出:
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
    return c, s

def apply_givens(Q, R, i, k, c, s):
    """
    应用 Givens 旋转矩阵 G 到矩阵 R 的第 i 行和第 k 行，以及更新 Q 矩阵
    
    输入:
        Q - 正交矩阵
        R - 上三角矩阵
        i - 旋转的行索引
        k - 旋转的行索引
        c - 余弦值
        s - 正弦值
    输出:
        Q - 更新后的正交矩阵
        R - 更新后的上三角矩阵
    """
    G = np.array([[c, s], [-s, c]])
    R[[i, k], :] = G @ R[[i, k], :]
    Q[:, [i, k]] = Q[:, [i, k]] @ G.T
    return Q, R

def qr_decomposition_givens(A):
    """
    使用 Givens 旋转进行 QR 分解
    
    输入:
        A - 输入矩阵, 大小为 (m, n)
    输出:
        Q - 正交矩阵, 大小为 (m, m)
        R - 上三角矩阵, 大小为 (m, n)
    """
    m, n = A.shape  # 获取矩阵 A 的尺寸
    Q = np.eye(m)  # 初始化正交矩阵 Q 为单位矩阵
    R = A.copy()  # 初始化 R 为 A 的副本

    for j in range(n):
        for i in range(m-1, j, -1):
            c, s = givens_rotation(R[i-1, j], R[i, j])
            Q, R = apply_givens(Q, R, i-1, i, c, s)
    
    return Q, R

# 测试函数
def test_givens_rotation():
    A = np.array([[4, 1], [3, 3], [0, 4]], dtype=float)  # 示例矩阵
    Q, R = qr_decomposition_givens(A)

    # 打印结果
    print('Q:')
    print(Q)
    print('R:')
    print(R)
    print('A:')
    print(A)
    print('Q @ R:')
    print(Q @ R)

# 运行测试函数
test_givens_rotation()
