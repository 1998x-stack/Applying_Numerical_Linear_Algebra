# 05_3.6_Performance_Comparison_of_Methods_for_Solving_Least_Squares_Problems

"""
Lecture: /3_Linear_Least_Squares_Problems
Content: 05_3.6_Performance_Comparison_of_Methods_for_Solving_Least_Squares_Problems
"""

import numpy as np
import time

def generate_random_matrix(n, m):
    """
    生成一个元素在 [-1, 1] 范围内均匀分布的随机矩阵
    """
    return np.random.uniform(-1, 1, (n, m))

def generate_geometric_singular_matrix(n, m, epsilon=1e-10):
    """
    生成一个奇异值从 1 到 epsilon 几何分布的矩阵
    """
    U, _ = np.linalg.qr(np.random.randn(n, n))
    V, _ = np.linalg.qr(np.random.randn(m, m))
    singular_values = np.geomspace(1, epsilon, min(n, m))
    S = np.zeros((n, m))
    np.fill_diagonal(S, singular_values)
    return U @ S @ V

def solve_least_squares_normal_equation(A, b):
    """
    使用正规方程法解决最小二乘问题
    """
    return np.linalg.solve(A.T @ A, A.T @ b)

def solve_least_squares_qr(A, b):
    """
    使用 QR 分解解决最小二乘问题
    """
    Q, R = np.linalg.qr(A)
    return np.linalg.solve(R, Q.T @ b)

def solve_least_squares_svd(A, b):
    """
    使用 SVD 解决最小二乘问题
    """
    U, sigma, VT = np.linalg.svd(A, full_matrices=False)
    return VT.T @ np.linalg.solve(np.diag(sigma), U.T @ b)

def time_method(method, A, b):
    """
    测量方法的执行时间
    """
    start_time = time.time()
    x = method(A, b)
    return time.time() - start_time

def run_experiments():
    sizes = [20, 100, 400, 1600]
    methods = [solve_least_squares_normal_equation, solve_least_squares_qr, solve_least_squares_svd]
    method_names = ["Normal Equation", "QR Decomposition", "SVD"]
    
    print("随机矩阵性能比较:")
    for n in sizes:
        A = generate_random_matrix(n, n)
        b = np.random.randn(n)
        
        print(f"矩阵规模: {n} x {n}")
        times = [time_method(method, A, b) for method in methods]
        
        for i, method_name in enumerate(method_names):
            print(f"{method_name} 时间: {times[i]:.6f} 秒")
        
        print("相对慢:")
        print(f"QR 分解相对正规方程法慢: {times[1] / times[0]:.2f} 倍")
        print(f"SVD 相对 QR 分解慢: {times[2] / times[1]:.2f} 倍")
        print()
    
    print("几何分布的奇异值矩阵性能比较:")
    for n in sizes:
        A = generate_geometric_singular_matrix(n, n)
        b = np.random.randn(n)
        
        print(f"矩阵规模: {n} x {n}")
        times = [time_method(method, A, b) for method in methods]
        
        for i, method_name in enumerate(method_names):
            print(f"{method_name} 时间: {times[i]:.6f} 秒")
        
        print("相对慢:")
        print(f"QR 分解相对正规方程法慢: {times[1] / times[0]:.2f} 倍")
        print(f"SVD 相对 QR 分解慢: {times[2] / times[1]:.2f} 倍")
        print()

if __name__ == "__main__":
    run_experiments()
