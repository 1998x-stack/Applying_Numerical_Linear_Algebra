# 01_2.5.2_Equilibration

"""
Lecture: 2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution
Content: 01_2.5.2_Equilibration
"""

import numpy as np
from typing import Tuple

class Equilibration:
    """Class for matrix equilibration to improve the accuracy of linear system solutions.
    
    This class provides methods to equilibrate a given matrix by scaling its rows
    and columns to reduce its condition number, thereby improving the stability and
    accuracy of solutions to the linear system.
    
    Attributes:
        matrix (np.ndarray): The original matrix to be equilibrated.
    """
    
    def __init__(self, matrix: np.ndarray):
        """
        Initialize the Equilibration class with a matrix.
        
        Args:
            matrix (np.ndarray): The matrix to be equilibrated.
        """
        self.matrix = matrix
    
    def row_scale_factors(self) -> np.ndarray:
        """
        Compute the row scaling factors for equilibration.
        
        Returns:
            np.ndarray: A 1D array containing the scaling factors for each row.
        """
        row_norms = np.linalg.norm(self.matrix, axis=1)
        return 1.0 / row_norms
    
    def column_scale_factors(self) -> np.ndarray:
        """
        Compute the column scaling factors for equilibration.
        
        Returns:
            np.ndarray: A 1D array containing the scaling factors for each column.
        """
        column_norms = np.linalg.norm(self.matrix, axis=0)
        return 1.0 / column_norms
    
    def equilibrate(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Apply row and column scaling to equilibrate the matrix.
        
        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray]: The row scaling factors, column scaling factors,
                                                      and the equilibrated matrix.
        """
        row_factors = self.row_scale_factors()
        col_factors = self.column_scale_factors()
        
        D_row = np.diag(row_factors)
        D_col = np.diag(col_factors)
        
        equilibrated_matrix = D_row @ self.matrix @ D_col
        
        return row_factors, col_factors, equilibrated_matrix
    
    def validate_equilibration(self, row_factors: np.ndarray, col_factors: np.ndarray) -> bool:
        """
        Validate the equilibration by checking the norms of the rows and columns of the equilibrated matrix.
        
        Args:
            row_factors (np.ndarray): The row scaling factors used for equilibration.
            col_factors (np.ndarray): The column scaling factors used for equilibration.
        
        Returns:
            bool: True if equilibration is successful, False otherwise.
        """
        D_row = np.diag(row_factors)
        D_col = np.diag(col_factors)
        equilibrated_matrix = D_row @ self.matrix @ D_col
        
        row_norms = np.linalg.norm(equilibrated_matrix, axis=1)
        col_norms = np.linalg.norm(equilibrated_matrix, axis=0)
        
        return np.allclose(row_norms, 1) and np.allclose(col_norms, 1)
    
def main():
    # 示例矩阵
    A = np.array([[4, 1, 2],
                  [3, 6, 1],
                  [2, 1, 3]], dtype=float)
    
    # 初始化均衡化类
    equilibration = Equilibration(A)
    
    # 进行均衡化
    row_factors, col_factors, equilibrated_matrix = equilibration.equilibrate()
    
    # 打印结果
    print("Row Scaling Factors:\n", row_factors)
    print("Column Scaling Factors:\n", col_factors)
    print("Equilibrated Matrix:\n", equilibrated_matrix)
    
    # 验证均衡化结果
    is_valid = equilibration.validate_equilibration(row_factors, col_factors)
    print("Is equilibration valid?", is_valid)

if __name__ == "__main__":
    main()