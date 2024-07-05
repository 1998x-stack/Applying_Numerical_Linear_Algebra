structure = {
    "structure": [
        {
            "1_Introduction": [
                "1.1_Basic_Notation",
                "1.2_Standard_Problems_of_Numerical_Linear_Algebra",
                {
                    "1.3_General_Techniques": [
                        "1.3.1_Matrix_Factorizations",
                        "1.3.2_Perturbation_Theory_and_Condition_Numbers",
                        "1.3.3_Effects_of_Roundoff_Error_on_Algorithms",
                        "1.3.4_Analyzing_the_Speed_of_Algorithms",
                        "1.3.5_Engineering_Numerical_Software"
                    ]
                },
                "1.4_Example:_Polynomial_Evaluation",
                "1.5_Floating_Point_Arithmetic",
                "1.6_Polynomial_Evaluation_Revisited",
                "1.7_Vector_and_Matrix_Norms",
                "1.8_References_and_Other_Topics_for_Chapter_1",
                "1.9_Questions_for_Chapter_1"
            ]
        },
        {
            "2_Linear_Equation_Solving": [
                "2.1_Introduction",
                "2.2_Perturbation_Theory",
                "2.2.1_Relative_Perturbation_Theory",
                "2.3_Gaussian_Elimination",
                {
                    "2.4_Error_Analysis": [
                        "2.4.1_The_Need_for_Pivoting",
                        "2.4.2_Formal_Error_Analysis_of_Gaussian_Elimination",
                        "2.4.3_Estimating_Condition_Numbers",
                        "2.4.4_Practical_Error_Bounds"
                    ]
                },
                {
                    "2.5_Improving_the_Accuracy_of_a_Solution": [
                        "2.5.1_Single_Precision_Iterative_Refinement",
                        "2.5.2_Equilibration"
                    ]
                },
                {
                    "2.6_Blocking_Algorithms_for_Higher_Performance": [
                        "2.6.1_Basic_Linear_Algebra_Subroutines_(BLAS)",
                        "2.6.2_How_to_Optimize_Matrix_Multiplication",
                        "2.6.3_Reorganizing_Gaussian_Elimination_to_use_Level_3_BLAS",
                        "2.6.4_More_About_Parallelism_and_Other_Performance_Issues"
                    ]
                },
                {
                    "2.7_Special_Linear_Systems": [
                        "2.7.1_Real_Symmetric_Positive_Definite_Matrices",
                        "2.7.2_Symmetric_Indefinite_Matrices",
                        "2.7.3_Band_Matrices",
                        "2.7.4_General_Sparse_Matrices",
                        "2.7.5_Dense_Matrices_Depending_on_Fewer_Than_O(n²)_Parameters"
                    ]
                },
                "2.8_References_and_Other_Topics_for_Chapter_2",
                "2.9_Questions_for_Chapter_2"
            ]
        },
        {
            "3_Linear_Least_Squares_Problems": [
                "3.1_Introduction",
                {
                    "3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem": [
                        "3.2.1_Normal_Equations",
                        "3.2.2_QR_Decomposition",
                        "3.2.3_Singular_Value_Decomposition"
                    ]
                },
                "3.3_Perturbation_Theory_for_the_Least_Squares_Problem",
                {
                    "3.4_Orthogonal_Matrices": [
                        "3.4.1_Householder_Transformations",
                        "3.4.2_Givens_Rotations",
                        "3.4.3_Roundoff_Error_Analysis_for_Orthogonal_Matrices",
                        "3.4.4_Why_Orthogonal_Matrices?"
                    ]
                },
                {
                    "3.5_Rank-Deficient_Least_Squares_Problems": [
                        "3.5.1_Solving_Rank-Deficient_Least_Squares_Problems_Using_the_SVD",
                        "3.5.2_Solving_Rank-Deficient_Least_Squares_Problems_Using_QR_with_Pivoting"
                    ]
                },
                "3.6_Performance_Comparison_of_Methods_for_Solving_Least_Squares_Problems",
                "3.7_References_and_Other_Topics_for_Chapter_3",
                "3.8_Questions_for_Chapter_3"
            ]
        },
        {
            "4_Nonsymmetric_Eigenvalue_Problems": [
                "4.1_Introduction",
                {
                    "4.2_Canonical_Forms": [
                        "4.2.1_Computing_Eigenvectors_from_the_Schur_Form"
                    ]
                },
                "4.3_Perturbation_Theory",
                {
                    "4.4_Algorithms_for_the_Nonsymmetric_Eigenproblem": [
                        "4.4.1_Power_Method",
                        "4.4.2_Inverse_Iteration",
                        "4.4.3_Orthogonal_Iteration",
                        "4.4.4_QR_Iteration",
                        "4.4.5_Making_QR_Iteration_Practical",
                        "4.4.6_Hessenberg_Reduction",
                        "4.4.7_Tridiagonal_and_Bidiagonal_Reduction",
                        "4.4.8_QR_Iteration_with_Implicit_Shifts"
                    ]
                },
                {
                    "4.5_Other_Nonsymmetric_Eigenvalue_Problems": [
                        "4.5.1_Regular_Matrix_Pencils_and_Weierstrass_Canonical_Form",
                        "4.5.2_Singular_Matrix_Pencils_and_the_Kronecker_Canonical_Form",
                        "4.5.3_Nonlinear_Eigenvalue_Problems"
                    ]
                },
                "4.6_Summary",
                "4.7_References_and_Other_Topics_for_Chapter_4",
                "4.8_Questions_for_Chapter_4"
            ]
        },
        {
            "5_The_Symmetric_Eigenproblem_and_Singular_Value_Decomposition": [
                "5.1_Introduction",
                "5.2_Perturbation_Theory",
                "5.2.1_Relative_Perturbation_Theory",
                {
                    "5.3_Algorithms_for_the_Symmetric_Eigenproblem": [
                        "5.3.1_Tridiagonal_QR_Iteration",
                        "5.3.2_Rayleigh_Quotient_Iteration",
                        "5.3.3_Divide-and-Conquer",
                        "5.3.4_Bisection_and_Inverse_Iteration",
                        "5.3.5_Jacobi’s_Method",
                        "5.3.6_Performance_Comparison"
                    ]
                },
                {
                    "5.4_Algorithms_for_the_Singular_Value_Decomposition": [
                        "5.4.1_QR_Iteration_and_Its_Variations_for_the_Bidiagonal_SVD",
                        "5.4.2_Computing_the_Bidiagonal_SVD_to_High_Relative_Accuracy",
                        "5.4.3_Jacobi’s_Method_for_the_SVD"
                    ]
                },
                {
                    "5.5_Differential_Equations_and_Eigenvalue_Problems": [
                        "5.5.1_The_Toda_Lattice",
                        "5.5.2_The_Connection_to_Partial_Differential_Equations"
                    ]
                },
                "5.6_References_and_Other_Topics_for_Chapter_5",
                "5.7_Questions_for_Chapter_5"
            ]
        },
        {
            "6_Iterative_Methods_for_Linear_Systems": [
                "6.1_Introduction",
                "6.2_On-line_Help_for_Iterative_Methods",
                {
                    "6.3_Poisson’s_Equation": [
                        "6.3.1_Poisson’s_Equation_in_One_Dimension",
                        "6.3.2_Poisson’s_Equation_in_Two_Dimensions",
                        "6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products"
                    ]
                },
                "6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation",
                {
                    "6.5_Basic_Iterative_Methods": [
                        "6.5.1_Jacobi’s_Method",
                        "6.5.2_Gauss–Seidel_Method",
                        "6.5.3_Successive_Overrelaxation",
                        "6.5.4_Convergence_of_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods_on_the_Model_Problem",
                        "6.5.5_Detailed_Convergence_Criteria_for_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods",
                        "6.5.6_Chebyshev_Acceleration_and_Symmetric_SOR_(SSOR)"
                    ]
                },
                {
                    "6.6_Krylov_Subspace_Methods": [
                        "6.6.1_Extracting_Information_about_A_via_Matrix-Vector_Multiplication",
                        "6.6.2_Solving_Ax_=b_Using_the_Krylov_Subspace_Kk",
                        "6.6.3_Conjugate_Gradient_Method",
                        "6.6.4_Convergence_Analysis_of_the_Conjugate_Gradient_Method",
                        "6.6.5_Preconditioning",
                        "6.6.6_Other_Krylov_Subspace_Algorithms_for_Solving_Ax_=b"
                    ]
                },
                {
                    "6.7_Fast_Fourier_Transform": [
                        "6.7.1_The_Discrete_Fourier_Transform",
                        "6.7.2_Solving_the_Continuous_Model_Problem_Using_Fourier_Series",
                        "6.7.3_Convolutions",
                        "6.7.4_Computing_the_Fast_Fourier_Transform"
                    ]
                },
                "6.8_Block_Cyclic_Reduction",
                {
                    "6.9_Multigrid": [
                        "6.9.1_Overview_of_Multigrid_on_Two-Dimensional_Poisson’s_Equation",
                        "6.9.2_Detailed_Description_of_Multigrid_on_One-Dimensional_Poisson’s_Equation"
                    ]
                },
                {
                    "6.10_Domain_Decomposition": [
                        "6.10.1_Nonoverlapping_Methods",
                        "6.10.2_Overlapping_Methods"
                    ]
                },
                "6.11_References_and_Other_Topics_for_Chapter_6",
                "6.12_Questions_for_Chapter_6"
            ]
        },
        {
            "7_Iterative_Algorithms_for_Eigenvalue_Problems": [
                "7.1_Introduction",
                "7.2_The_Rayleigh–Ritz_Method",
                "7.3_The_Lanczos_Algorithm_in_Exact_Arithmetic",
                "7.4_The_Lanczos_Algorithm_in_Floating_Point_Arithmetic",
                "7.5_The_Lanczos_Algorithm_with_Selective_Orthogonalization",
                "7.6_Beyond_Selective_Orthogonalization",
                "7.7_Iterative_Algorithms_for_the_Nonsymmetric_Eigenproblem",
                "7.8_References_and_Other_Topics_for_Chapter_7",
                "7.9_Questions_for_Chapter_7"
            ]
        },
        "Bibliography",
        "Index"
    ]
}




import os
from typing import Dict, Any

def create_directories_and_files(
        base_path: str, 
        structure: Dict[str, Any], 
        readme_file, 
        parent_path: str = "", 
        level: int = 1
    ):
    heading = "#" * level

    for key, value in structure.items():
        current_path = os.path.join(base_path, key.replace(" ", "_").replace("/", "_").replace("-", "_"))

        # 创建目录
        os.makedirs(current_path, exist_ok=True)

        # 在README中添加章节标题
        if parent_path:
            readme_file.write(f"{heading} {parent_path}/{key}\n\n")
        else:
            readme_file.write(f"{heading} {key}\n\n")

        # 递归调用创建子目录和文件
        if isinstance(value, dict) and value:
            create_directories_and_files(
                current_path, 
                value, 
                readme_file, 
                parent_path + "/" + key if parent_path else key, 
                level + 1
            )
        elif isinstance(value, list) and value:
            for idx, item in enumerate(value):
                if isinstance(item, dict) and item:
                    create_directories_and_files(
                        current_path, 
                        item, 
                        readme_file, 
                        parent_path + "/" + key if parent_path else key, 
                        level + 1
                    )
                else:
                    item = f"{idx:02d}_{item}"
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {item}\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.py)\n")
                    
                    
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {item}\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.md)\n")
                    
                    
                    
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".m"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"// {item}\n\n")
                        file.write(f'/*\n\nLecture: {parent_path}/{key}\nContent: {item}\n\n*/\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.m)\n")
        else:
            # 创建文件并写入初始内容
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {key}\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")
            
            
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {key}\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")
            
            
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".m"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"// {key}\n\n")
                file.write(f'/*\n\nLecture: {parent_path}/{key}\nContent: {key}\n\n*/\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")

        # 添加空行以分隔不同的章节
        readme_file.write("\n")

def main():
    root_dir = './'
    # 创建根目录
    os.makedirs(root_dir, exist_ok=True)

    # 创建 README.md 文件
    with open(os.path.join(root_dir, "README.md"), 'w', encoding='utf-8') as readme_file:
        readme_file.write("# Applying_Numerical_Linear_Algebra\n\n")
        readme_file.write("这是一个关于Applying_Numerical_Linear_Algebra的目录结构。\n\n")
        create_directories_and_files(root_dir, structure, readme_file)

    print("目录和文件结构已生成，并创建 README.md 文件。")

if __name__ == "__main__":
    main()