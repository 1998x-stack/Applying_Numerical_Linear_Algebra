# 00_3.2.1_Normal_Equations

"""
Lecture: 3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem
Content: 00_3.2.1_Normal_Equations
"""

import numpy as np
from typing import Tuple

class NormalEquationsSolver:
    """Class to solve linear least squares problems using Normal Equations.

    This class provides methods to solve Ax = b using the normal equations approach,
    where A is the input matrix and b is the target vector.
    """

    def __init__(self, A: np.ndarray, b: np.ndarray):
        """
        Initialize the NormalEquationsSolver with matrix A and vector b.
        
        Args:
            A (np.ndarray): The input matrix of shape (m, n).
            b (np.ndarray): The target vector of shape (m,).
        """
        self.A = A
        self.b = b

    def solve(self) -> np.ndarray:
        """
        Solve the least squares problem using the normal equations.
        
        Returns:
            np.ndarray: The solution vector x of shape (n,).
        """
        # 计算 A^T A 和 A^T b
        A_T_A = self.A.T @ self.A
        A_T_b = self.A.T @ self.b

        # 解正规方程 A^T A x = A^T b
        x = np.linalg.solve(A_T_A, A_T_b)
        return x

    def compute_residuals(self, x: np.ndarray) -> np.ndarray:
        """
        Compute the residuals of the least squares solution.
        
        Args:
            x (np.ndarray): The solution vector of shape (n,).
        
        Returns:
            np.ndarray: The residual vector of shape (m,).
        """
        residuals = self.b - self.A @ x
        return residuals

def main():
    # 示例矩阵 A 和向量 b
    A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)
    b = np.array([1, 2, 2.5], dtype=float)

    # 初始化正规方程求解器
    solver = NormalEquationsSolver(A, b)
    
    # 求解正规方程
    x = solver.solve()
    
    # 计算残差
    residuals = solver.compute_residuals(x)
    
    # 打印结果
    print("Solution vector x:\n", x)
    print("Residuals:\n", residuals)

if __name__ == "__main__":
    main()