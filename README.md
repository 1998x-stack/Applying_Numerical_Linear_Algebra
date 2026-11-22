# 应用数值线性代数 · Applying Numerical Linear Algebra

> 一套围绕“问题结构—条件数—数值稳定性—算法实现—性能验证”组织的中文数值线性代数课程。

**在线课程入口：** [打开课程首页](https://1998x-stack.github.io/Applying_Numerical_Linear_Algebra/)（发布状态以 GitHub Actions 和实际站点检查为准）。

## 第一批课程建设：第一章 8 篇

首批 8 篇围绕 James W. Demmel《Applied Numerical Linear Algebra》第一章基础主题进行独立重写。每篇页面都从问题本身建立上下文，不要求读者先读上一页；包含推导、原创 SVG、交互演示、参考资料和 Python/MATLAB 对照实现。

| # | 主题 | 页面 | Markdown | Python | MATLAB |
|---:|---|---|---|---|---|
| 01 | 数值线性代数的语言：向量、矩阵与记号 | [HTML](1_Introduction/00_1.1_Basic_Notation.html) | [MD](1_Introduction/00_1.1_Basic_Notation.md) | [PY](1_Introduction/00_1.1_Basic_Notation.py) | [M](1_Introduction/00_1.1_Basic_Notation.m) |
| 02 | 数值线性代数究竟要解决哪些问题 | [HTML](1_Introduction/01_1.2_Standard_Problems_of_Numerical_Linear_Algebra.html) | [MD](1_Introduction/01_1.2_Standard_Problems_of_Numerical_Linear_Algebra.md) | [PY](1_Introduction/01_1.2_Standard_Problems_of_Numerical_Linear_Algebra.py) | [M](1_Introduction/01_1.2_Standard_Problems_of_Numerical_Linear_Algebra.m) |
| 03 | 为什么要把矩阵分解成更简单的矩阵 | [HTML](1_Introduction/1.3_General_Techniques/00_1.3.1_Matrix_Factorizations.html) | [MD](1_Introduction/1.3_General_Techniques/00_1.3.1_Matrix_Factorizations.md) | [PY](1_Introduction/1.3_General_Techniques/00_1.3.1_Matrix_Factorizations.py) | [M](1_Introduction/1.3_General_Techniques/00_1.3.1_Matrix_Factorizations.m) |
| 04 | 输入误差如何放大：扰动理论与条件数 | [HTML](1_Introduction/1.3_General_Techniques/01_1.3.2_Perturbation_Theory_and_Condition_Numbers.html) | [MD](1_Introduction/1.3_General_Techniques/01_1.3.2_Perturbation_Theory_and_Condition_Numbers.md) | [PY](1_Introduction/1.3_General_Techniques/01_1.3.2_Perturbation_Theory_and_Condition_Numbers.py) | [M](1_Introduction/1.3_General_Techniques/01_1.3.2_Perturbation_Theory_and_Condition_Numbers.m) |
| 05 | 计算机为什么会算错：舍入误差与稳定性 | [HTML](1_Introduction/1.3_General_Techniques/02_1.3.3_Effects_of_Roundoff_Error_on_Algorithms.html) | [MD](1_Introduction/1.3_General_Techniques/02_1.3.3_Effects_of_Roundoff_Error_on_Algorithms.md) | [PY](1_Introduction/1.3_General_Techniques/02_1.3.3_Effects_of_Roundoff_Error_on_Algorithms.py) | [M](1_Introduction/1.3_General_Techniques/02_1.3.3_Effects_of_Roundoff_Error_on_Algorithms.m) |
| 06 | 为什么 FLOPs 少不一定跑得快 | [HTML](1_Introduction/1.3_General_Techniques/03_1.3.4_Analyzing_the_Speed_of_Algorithms.html) | [MD](1_Introduction/1.3_General_Techniques/03_1.3.4_Analyzing_the_Speed_of_Algorithms.md) | [PY](1_Introduction/1.3_General_Techniques/03_1.3.4_Analyzing_the_Speed_of_Algorithms.py) | [M](1_Introduction/1.3_General_Techniques/03_1.3.4_Analyzing_the_Speed_of_Algorithms.m) |
| 07 | 如何构建可信的数值计算软件 | [HTML](1_Introduction/1.3_General_Techniques/04_1.3.5_Engineering_Numerical_Software.html) | [MD](1_Introduction/1.3_General_Techniques/04_1.3.5_Engineering_Numerical_Software.md) | [PY](1_Introduction/1.3_General_Techniques/04_1.3.5_Engineering_Numerical_Software.py) | [M](1_Introduction/1.3_General_Techniques/04_1.3.5_Engineering_Numerical_Software.m) |
| 08 | 多项式求值：Horner 方法与数值稳定性 | [HTML](1_Introduction/03_1.4_Example:_Polynomial_Evaluation.html) | [MD](1_Introduction/03_1.4_Example:_Polynomial_Evaluation.md) | [PY](1_Introduction/03_1.4_Example:_Polynomial_Evaluation.py) | [M](1_Introduction/03_1.4_Example:_Polynomial_Evaluation.m) |


## 第二批课程建设：第六章 8 篇

第六章的前八个关键基础主题已按独立教学单元精细化。所有页面都明确变量和维度、边界条件、算子符号、算法适用范围；配有原生 MathML、独立原创 SVG、交互解释、Python / MATLAB 对照示例和同名 `.evidence.json` 主张—来源台账。

| 章节 | 主题 | HTML | Markdown | Python | MATLAB |
|---|---|---|---|---|---|
| 6.1 | 迭代法、残差与停止准则 | [HTML](6_Iterative_Methods_for_Linear_Systems/00_6.1_Introduction.html) | [MD](6_Iterative_Methods_for_Linear_Systems/00_6.1_Introduction.md) | [PY](6_Iterative_Methods_for_Linear_Systems/00_6.1_Introduction.py) | [M](6_Iterative_Methods_for_Linear_Systems/00_6.1_Introduction.m) |
| 6.2 | 如何选择迭代求解器 | [HTML](6_Iterative_Methods_for_Linear_Systems/01_6.2_On_line_Help_for_Iterative_Methods.html) | [MD](6_Iterative_Methods_for_Linear_Systems/01_6.2_On_line_Help_for_Iterative_Methods.md) | [PY](6_Iterative_Methods_for_Linear_Systems/01_6.2_On_line_Help_for_Iterative_Methods.py) | [M](6_Iterative_Methods_for_Linear_Systems/01_6.2_On_line_Help_for_Iterative_Methods.m) |
| 6.3.1 | 一维 Poisson：三对角离散 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/00_6.3.1_Poisson’s_Equation_in_One_Dimension.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/00_6.3.1_Poisson’s_Equation_in_One_Dimension.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/00_6.3.1_Poisson’s_Equation_in_One_Dimension.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/00_6.3.1_Poisson’s_Equation_in_One_Dimension.m) |
| 6.3.2 | 二维 Poisson：五点模板 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/01_6.3.2_Poisson’s_Equation_in_Two_Dimensions.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/01_6.3.2_Poisson’s_Equation_in_Two_Dimensions.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/01_6.3.2_Poisson’s_Equation_in_Two_Dimensions.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/01_6.3.2_Poisson’s_Equation_in_Two_Dimensions.m) |
| 6.3.3 | Kronecker 积与向量化 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/02_6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/02_6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/02_6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/02_6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products.m) |
| 6.4 | Poisson 求解器的复杂度比较 | [HTML](6_Iterative_Methods_for_Linear_Systems/03_6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation.html) | [MD](6_Iterative_Methods_for_Linear_Systems/03_6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation.md) | [PY](6_Iterative_Methods_for_Linear_Systems/03_6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation.py) | [M](6_Iterative_Methods_for_Linear_Systems/03_6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation.m) |
| 6.5.1 | Jacobi：同步更新 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/00_6.5.1_Jacobi’s_Method.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/00_6.5.1_Jacobi’s_Method.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/00_6.5.1_Jacobi’s_Method.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/00_6.5.1_Jacobi’s_Method.m) |
| 6.5.2 | Gauss–Seidel：新旧分量复用 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/01_6.5.2_Gauss–Seidel_Method.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/01_6.5.2_Gauss–Seidel_Method.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/01_6.5.2_Gauss–Seidel_Method.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/01_6.5.2_Gauss–Seidel_Method.m) |

建议顺序：**残差与停止准则 → 软件选型 → 一维/二维 Poisson → Kronecker 和 → 复杂度比较 → Jacobi → Gauss–Seidel**。不要求先读上一页才能理解当前页。已有旧章文件路径全部保留。

## 学习路线

第一批：问题类型 → 矩阵分解 → 条件数 → 浮点误差与稳定性 → 性能分析 → 数值软件 → 多项式求值案例。

第二批：线性系统残差 → 矩阵结构与软件选型 → Poisson 有限差分 → Kronecker 和 → 迭代收敛。

## 仓库结构

```text
.
├── index.html                 # 课程门户
├── README.md / README.html
├── AGENTS.md                  # 数学、内容、代码和发布规范
├── courses.json               # 课程元数据
├── assets/                    # 第一批与第六章两套共享样式、JS、原创 SVG
├── 1_Introduction/             # 第一章原有路径保持稳定
├── 2_Linear_Equation_Solving/
├── 3_Linear_Least_Squares_Problems/
├── 4_Nonsymmetric_Eigenvalue_Problems/
├── 5_The_Symmetric_Eigenproblem_and_Singular_Value_Decomposition/
├── 6_Iterative_Methods_for_Linear_Systems/
├── 7_Iterative_Algorithms_for_Eigenvalue_Problems/
├── evidence/                  # 逐篇主张—来源证据台账
├── scripts/                   # 站点构建、静态校验、浏览器验收
├── tests/
└── docs/
```



## 第二章深度重构：新增 8 篇

本批次保留原文件路径，将第二章 2.1–2.4.4 的八篇内容改写为独立文章，强调问题条件数与算法稳定性的区别、数学假设、数值验证与实际使用边界。前两批第一章和第六章内容不被覆盖。

| 原编号 | 数值线性代数主题 | HTML | Python | MATLAB |
|---|---|---|---|---|
| 2.1 | 从 Ax=b 出发：求解可靠性 | [阅读](2_Linear_Equation_Solving/00_2.1_Introduction.html) | [运行](2_Linear_Equation_Solving/00_2.1_Introduction.py) | [运行](2_Linear_Equation_Solving/00_2.1_Introduction.m) |
| 2.2 | 矩阵与右端项同时扰动 | [阅读](2_Linear_Equation_Solving/01_2.2_Perturbation_Theory.html) | [运行](2_Linear_Equation_Solving/01_2.2_Perturbation_Theory.py) | [运行](2_Linear_Equation_Solving/01_2.2_Perturbation_Theory.m) |
| 2.2.1 | 范数与逐元素相对扰动 | [阅读](2_Linear_Equation_Solving/02_2.2.1_Relative_Perturbation_Theory.html) | [运行](2_Linear_Equation_Solving/02_2.2.1_Relative_Perturbation_Theory.py) | [运行](2_Linear_Equation_Solving/02_2.2.1_Relative_Perturbation_Theory.m) |
| 2.3 | 高斯消去 PA=LU | [阅读](2_Linear_Equation_Solving/03_2.3_Gaussian_Elimination.html) | [运行](2_Linear_Equation_Solving/03_2.3_Gaussian_Elimination.py) | [运行](2_Linear_Equation_Solving/03_2.3_Gaussian_Elimination.m) |
| 2.4.1 | 小主元为何危险 | [阅读](2_Linear_Equation_Solving/2.4_Error_Analysis/00_2.4.1_The_Need_for_Pivoting.html) | [运行](2_Linear_Equation_Solving/2.4_Error_Analysis/00_2.4.1_The_Need_for_Pivoting.py) | [运行](2_Linear_Equation_Solving/2.4_Error_Analysis/00_2.4.1_The_Need_for_Pivoting.m) |
| 2.4.2 | 舍入误差与增长因子 | [阅读](2_Linear_Equation_Solving/2.4_Error_Analysis/01_2.4.2_Formal_Error_Analysis_of_Gaussian_Elimination.html) | [运行](2_Linear_Equation_Solving/2.4_Error_Analysis/01_2.4.2_Formal_Error_Analysis_of_Gaussian_Elimination.py) | [运行](2_Linear_Equation_Solving/2.4_Error_Analysis/01_2.4.2_Formal_Error_Analysis_of_Gaussian_Elimination.m) |
| 2.4.3 | 逆范数与条件数诊断 | [阅读](2_Linear_Equation_Solving/2.4_Error_Analysis/02_2.4.3_Estimating_Condition_Numbers.html) | [运行](2_Linear_Equation_Solving/2.4_Error_Analysis/02_2.4.3_Estimating_Condition_Numbers.py) | [运行](2_Linear_Equation_Solving/2.4_Error_Analysis/02_2.4.3_Estimating_Condition_Numbers.m) |
| 2.4.4 | 残差、BERR 与前向界 | [阅读](2_Linear_Equation_Solving/2.4_Error_Analysis/03_2.4.4_Practical_Error_Bounds.html) | [运行](2_Linear_Equation_Solving/2.4_Error_Analysis/03_2.4.4_Practical_Error_Bounds.py) | [运行](2_Linear_Equation_Solving/2.4_Error_Analysis/03_2.4.4_Practical_Error_Bounds.m) |

### 本批次的准确性修订

- 保留 (A+ΔA)Δx=Δb−ΔA x，并在相对扰动界中明确 κ(A)α<1。
- 区分范数条件与逐元素比例扰动；对角阵可能整体病态但对结构化扰动不敏感。
- GEPP 使用 PA=LU，清晰区分无主元、小主元与部分选主元。
- Wilkinson 增长因子说明最坏界；不将选主元直接写成无条件数值稳定保证。
- 基向量解算逆范数为教学参考，不冒充高效条件数估计器；FERR/BERR/RCOND 使用官方 LAPACK 语义。
- 浏览器质量门禁覆盖第一章和第二章；第六章保留自己的浏览器验收脚本。


## 第五批：第二章 2.5–2.7 深度精讲（新增 8 篇）

这一批沿着“残差校正 → 矩阵缩放 → 运算密度 → GEMM 分块 → LU 的 Schur 补 → 并行屋顶 → SPD / 不定系统分解”的因果链推进。每篇包含完整独立的数学分析、原创建模图解、可调的数学可视化、代码与反例，不只是章节摘要。之前第六章 Krylov/CG 的 8 篇增量完整保留。

| 节次 | 文章主题 | HTML | Markdown | Python | MATLAB |
|---|---|---|---|---|---|
| 2.5.1 | 迭代改进：低精度分解与高精度残差 | [阅读](2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/00_2.5.1_Single_Precision_Iterative_Refinement.html) | [正文](2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/00_2.5.1_Single_Precision_Iterative_Refinement.md) | [代码](2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/00_2.5.1_Single_Precision_Iterative_Refinement.py) | [代码](2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/00_2.5.1_Single_Precision_Iterative_Refinement.m) |
| 2.5.2 | 矩阵均衡化：量级变化与真实病态 | [阅读](2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/01_2.5.2_Equilibration.html) | [正文](2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/01_2.5.2_Equilibration.md) | [代码](2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/01_2.5.2_Equilibration.py) | [代码](2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/01_2.5.2_Equilibration.m) |
| 2.6.1 | BLAS 三级与数据复用 | [阅读](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/00_2.6.1_Basic_Linear_Algebra_Subroutines_(BLAS).html) | [正文](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/00_2.6.1_Basic_Linear_Algebra_Subroutines_(BLAS).md) | [代码](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/00_2.6.1_Basic_Linear_Algebra_Subroutines_(BLAS).py) | [代码](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/00_2.6.1_Basic_Linear_Algebra_Subroutines_(BLAS).m) |
| 2.6.2 | 分块矩阵乘法与缓存工作集 | [阅读](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/01_2.6.2_How_to_Optimize_Matrix_Multiplication.html) | [正文](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/01_2.6.2_How_to_Optimize_Matrix_Multiplication.md) | [代码](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/01_2.6.2_How_to_Optimize_Matrix_Multiplication.py) | [代码](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/01_2.6.2_How_to_Optimize_Matrix_Multiplication.m) |
| 2.6.3 | 分块 LU 与 Schur 补 | [阅读](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/02_2.6.3_Reorganizing_Gaussian_Elimination_to_use_Level_3_BLAS.html) | [正文](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/02_2.6.3_Reorganizing_Gaussian_Elimination_to_use_Level_3_BLAS.md) | [代码](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/02_2.6.3_Reorganizing_Gaussian_Elimination_to_use_Level_3_BLAS.py) | [代码](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/02_2.6.3_Reorganizing_Gaussian_Elimination_to_use_Level_3_BLAS.m) |
| 2.6.4 | Roofline、Amdahl 与并行瓶颈 | [阅读](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/03_2.6.4_More_About_Parallelism_and_Other_Performance_Issues.html) | [正文](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/03_2.6.4_More_About_Parallelism_and_Other_Performance_Issues.md) | [代码](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/03_2.6.4_More_About_Parallelism_and_Other_Performance_Issues.py) | [代码](2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/03_2.6.4_More_About_Parallelism_and_Other_Performance_Issues.m) |
| 2.7.1 | Cholesky：对称正定与 LLᵀ | [阅读](2_Linear_Equation_Solving/2.7_Special_Linear_Systems/00_2.7.1_Real_Symmetric_Positive_Definite_Matrices.html) | [正文](2_Linear_Equation_Solving/2.7_Special_Linear_Systems/00_2.7.1_Real_Symmetric_Positive_Definite_Matrices.md) | [代码](2_Linear_Equation_Solving/2.7_Special_Linear_Systems/00_2.7.1_Real_Symmetric_Positive_Definite_Matrices.py) | [代码](2_Linear_Equation_Solving/2.7_Special_Linear_Systems/00_2.7.1_Real_Symmetric_Positive_Definite_Matrices.m) |
| 2.7.2 | 对称不定：LDLᵀ 与 2×2 主元 | [阅读](2_Linear_Equation_Solving/2.7_Special_Linear_Systems/01_2.7.2_Symmetric_Indefinite_Matrices.html) | [正文](2_Linear_Equation_Solving/2.7_Special_Linear_Systems/01_2.7.2_Symmetric_Indefinite_Matrices.md) | [代码](2_Linear_Equation_Solving/2.7_Special_Linear_Systems/01_2.7.2_Symmetric_Indefinite_Matrices.py) | [代码](2_Linear_Equation_Solving/2.7_Special_Linear_Systems/01_2.7.2_Symmetric_Indefinite_Matrices.m) |

**关键事实**：混合精度迭代改进不保证收敛；均衡化改变坐标不必然改变原问题敏感性；C←AB+C 的理想读写流量模型计入 A、B、C 的读取及 C 写回共 32n² 字节；Schur 教学示例未实现 DGETRF 的主元交换；Roofline 使用假设的硬件峰值而不是性能实测；对称不定系统与 Cholesky 的 SPD 假设不可混同。新增 18 项 Python 单元测试与浏览器滑块断言，MATLAB 未实机验证时不声明通过。

## 本地运行

需要 Python 3.10+。核心数值示例使用 NumPy；浏览器验收额外需要 Playwright 和 Chromium。

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/validate_site.py
python scripts/build_pages.py --output dist
python -m http.server 8000
```

访问 `http://localhost:8000`。浏览器自动化：

```bash
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python scripts/browser_qa.py
python scripts/browser_check.py
```

## 数值验证原则

- 先说明问题假设，再选择算法；不把算法稳定性和问题条件数混为一谈。
- 线性系统优先使用求解接口，不以显式矩阵求逆代替求解。
- 重要结论检查残差、后向误差、重构误差或正交性。
- 区分理论 FLOPs、理论数据流量下界和实测运行时间。
- Python 与 MATLAB 示例表达同一数学问题；不同 BLAS 后端的末位结果不要求完全相同。

## 参考主线与版权边界

课程结构参考 James W. Demmel, *Applied Numerical Linear Algebra*, SIAM, 1997, DOI: [10.1137/1.9781611971446](https://doi.org/10.1137/1.9781611971446)。浮点数与稳定性补充参考 IEEE 754-2019、David Goldberg (1991) 和 Nicholas Higham (2002)；性能分析补充参考 Roofline 模型。

本项目独立撰写解释、示例和图示，不复制原书段落或图形。仓库已有原始资料文件的再分发许可尚未独立核验；GitHub Pages 构建不会发布 PDF、Python 或 MATLAB 源文件。


## 第四批：第六章 SOR → Krylov → CG（新增 8 篇）

本批继续沿用原课程章节路径，每篇均为独立的完整中文文章，含 MathML 数学推导、具有解释意义的 SVG 数据流图、滑块交互、NumPy 与 MATLAB/Octave 对照脚本、同名证据文件 `.evidence.json`。这些内容与原第 6.1–6.5.2 八篇共同构成 **第六章 16 篇深读内容**；全站累计 **32 篇精细化文章**。

| 编号 | 独立主题 | 网页 | 文本 | Python | MATLAB |
|---|---|---|---|---|---|
| 6.5.3 | SOR：松弛参数与步长 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/02_6.5.3_Successive_Overrelaxation.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/02_6.5.3_Successive_Overrelaxation.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/02_6.5.3_Successive_Overrelaxation.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/02_6.5.3_Successive_Overrelaxation.m) |
| 6.5.4 | 误差慢模态：三种迭代的收敛尺度 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/03_6.5.4_Convergence_of_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods_on_the_Model_Problem.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/03_6.5.4_Convergence_of_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods_on_the_Model_Problem.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/03_6.5.4_Convergence_of_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods_on_the_Model_Problem.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/03_6.5.4_Convergence_of_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods_on_the_Model_Problem.m) |
| 6.5.5 | SPD 仍可能使 Jacobi 不收敛 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/04_6.5.5_Detailed_Convergence_Criteria_for_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/04_6.5.5_Detailed_Convergence_Criteria_for_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/04_6.5.5_Detailed_Convergence_Criteria_for_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/04_6.5.5_Detailed_Convergence_Criteria_for_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods.m) |
| 6.5.6 | Chebyshev 加速和 SSOR | [HTML](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/05_6.5.6_Chebyshev_Acceleration_and_Symmetric_SOR_(SSOR).html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/05_6.5.6_Chebyshev_Acceleration_and_Symmetric_SOR_(SSOR).md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/05_6.5.6_Chebyshev_Acceleration_and_Symmetric_SOR_(SSOR).py) | [M](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/05_6.5.6_Chebyshev_Acceleration_and_Symmetric_SOR_(SSOR).m) |
| 6.6.1 | 只用 Av 提取 Krylov 信息 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/00_6.6.1_Extracting_Information_about_A_via_Matrix_Vector_Multiplication.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/00_6.6.1_Extracting_Information_about_A_via_Matrix_Vector_Multiplication.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/00_6.6.1_Extracting_Information_about_A_via_Matrix_Vector_Multiplication.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/00_6.6.1_Extracting_Information_about_A_via_Matrix_Vector_Multiplication.m) |
| 6.6.2 | Krylov 投影与残差正交 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/01_6.6.2_Solving_Ax_=b_Using_the_Krylov_Subspace_Kk.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/01_6.6.2_Solving_Ax_=b_Using_the_Krylov_Subspace_Kk.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/01_6.6.2_Solving_Ax_=b_Using_the_Krylov_Subspace_Kk.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/01_6.6.2_Solving_Ax_=b_Using_the_Krylov_Subspace_Kk.m) |
| 6.6.3 | CG：A-共轭短递推 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/02_6.6.3_Conjugate_Gradient_Method.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/02_6.6.3_Conjugate_Gradient_Method.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/02_6.6.3_Conjugate_Gradient_Method.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/02_6.6.3_Conjugate_Gradient_Method.m) |
| 6.6.4 | CG 的 A-范数误差界 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/03_6.6.4_Convergence_Analysis_of_the_Conjugate_Gradient_Method.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/03_6.6.4_Convergence_Analysis_of_the_Conjugate_Gradient_Method.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/03_6.6.4_Convergence_Analysis_of_the_Conjugate_Gradient_Method.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/03_6.6.4_Convergence_Analysis_of_the_Conjugate_Gradient_Method.m) |

**学习顺序：** 先从 [6.5.3 SOR](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/02_6.5.3_Successive_Overrelaxation.html) 理解加权更新；再以 [6.5.5 的 SPD 反例](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/04_6.5.5_Detailed_Convergence_Criteria_for_Jacobi’s,_Gauss–Seidel,_and_SOR(ω)_Methods.html) 区分矩阵结构与迭代收敛；接着用 [6.5.6 的多项式](6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/05_6.5.6_Chebyshev_Acceleration_and_Symmetric_SOR_(SSOR).html) 连接谱与加速；最后按 6.6.1 → 6.6.4 逐步建立 Krylov、投影和 CG 收敛理论。

**可复现验收：** `python -m unittest discover -s tests -v`、`python scripts/validate_site.py`、`python scripts/browser_check.py` 和 `python main.py --check`。浏览器脚本检查首页与第六章 16 篇在 1440 / 768 / 390 / 360 px 的排版、MathML / SVG、交互与脚本错误。MATLAB 脚本提供等价算例，但没有实机执行时不得声称验证通过。原书参考 Demmel §§6.5.3–6.6.4，软件接口另以 SciPy 官方文档核对。


## 第六批：第六章 PCG / GMRES / FFT / Multigrid（新增 8 篇）

**累计进度：全站 48 篇独立深化文章，其中第六章 24 篇。** 本批沿用原教材的正式章节编号和仓库文件路径（包括 6.8 的根目录位置），每篇提供同步 HTML、Markdown、NumPy 与 MATLAB/Octave 脚本及同名 `<stem>.evidence.json`。网页均使用本地 CSS/JS、原生 MathML、可访问 SVG 和滑块实验。

| 章节 | 学习问题 | 网页 | Markdown | Python | MATLAB |
|---|---|---|---|---|---|
| 6.6.5 | 预条件：让困难的 SPD 系统拥有更好的谱 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/04_6.6.5_Preconditioning.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/04_6.6.5_Preconditioning.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/04_6.6.5_Preconditioning.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/04_6.6.5_Preconditioning.m) |
| 6.6.6 | GMRES：非对称系统的残差最小化 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/05_6.6.6_Other_Krylov_Subspace_Algorithms_for_Solving_Ax_=b.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/05_6.6.6_Other_Krylov_Subspace_Algorithms_for_Solving_Ax_=b.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/05_6.6.6_Other_Krylov_Subspace_Algorithms_for_Solving_Ax_=b.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.6_Krylov_Subspace_Methods/05_6.6.6_Other_Krylov_Subspace_Algorithms_for_Solving_Ax_=b.m) |
| 6.7.1 | 离散 Fourier 变换 DFT 的方向与能量 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/00_6.7.1_The_Discrete_Fourier_Transform.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/00_6.7.1_The_Discrete_Fourier_Transform.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/00_6.7.1_The_Discrete_Fourier_Transform.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/00_6.7.1_The_Discrete_Fourier_Transform.m) |
| 6.7.2 | 连续/离散 Poisson 的正弦谱求解 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/01_6.7.2_Solving_the_Continuous_Model_Problem_Using_Fourier_Series.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/01_6.7.2_Solving_the_Continuous_Model_Problem_Using_Fourier_Series.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/01_6.7.2_Solving_the_Continuous_Model_Problem_Using_Fourier_Series.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/01_6.7.2_Solving_the_Continuous_Model_Problem_Using_Fourier_Series.m) |
| 6.7.3 | 卷积定理、线性卷积和补零 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/02_6.7.3_Convolutions.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/02_6.7.3_Convolutions.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/02_6.7.3_Convolutions.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/02_6.7.3_Convolutions.m) |
| 6.7.4 | radix-2 FFT 与蝶形递归 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/03_6.7.4_Computing_the_Fast_Fourier_Transform.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/03_6.7.4_Computing_the_Fast_Fourier_Transform.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/03_6.7.4_Computing_the_Fast_Fourier_Transform.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.7_Fast_Fourier_Transform/03_6.7.4_Computing_the_Fast_Fourier_Transform.m) |
| 6.8 | 块循环约化与 Schur 补 | [HTML](6_Iterative_Methods_for_Linear_Systems/07_6.8_Block_Cyclic_Reduction.html) | [MD](6_Iterative_Methods_for_Linear_Systems/07_6.8_Block_Cyclic_Reduction.md) | [PY](6_Iterative_Methods_for_Linear_Systems/07_6.8_Block_Cyclic_Reduction.py) | [M](6_Iterative_Methods_for_Linear_Systems/07_6.8_Block_Cyclic_Reduction.m) |
| 6.9.1 | 二维 Poisson 的两网格纠错 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/00_6.9.1_Overview_of_Multigrid_on_Two_Dimensional_Poisson’s_Equation.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/00_6.9.1_Overview_of_Multigrid_on_Two_Dimensional_Poisson’s_Equation.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/00_6.9.1_Overview_of_Multigrid_on_Two_Dimensional_Poisson’s_Equation.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/00_6.9.1_Overview_of_Multigrid_on_Two_Dimensional_Poisson’s_Equation.m) |

**连续阅读路线：** 6.6.5 的 PCG 谱改善 → 6.6.6 的非对称 GMRES → 6.7.1 DFT 符号约定 → 6.7.2 零 Dirichlet 边界的离散正弦变换 → 6.7.3 补零避免循环混叠 → 6.7.4 FFT 蝶形 → 6.8 Schur 补块约化 → 6.9.1 二维多重网格误差校正。

**质量复现：** `python -m unittest discover -s tests -v`，`python scripts/validate_site.py`，`python scripts/browser_check.py`，`python main.py --check`。浏览器检查首页与第六章 24 篇、4 个视口，检查局部资源、交互、脚本异常、原生 MathML 和可访问 SVG。NumPy 算例只运行小规模确定性问题，结果不构成硬件性能 benchmark。MATLAB 对照提供数值断言，但未在 MATLAB 实机执行时必须标记为未验证。


## 第七批：第六章多重网格/区域分解 + 第三章最小二乘（8 篇）

全站累计 56 篇独立深化文章：第一章 8、第二章 16、第三章 5、第六章 27。以下 8 篇保留原目录中的 URL，不复写历史深度文章。

| 编号 | 独立主题 | 网页 | Markdown | Python | MATLAB |
|---|---|---|---|---|---|
| 6.9.2 | 一维 Poisson 的完整多重网格 V-cycle | [HTML](6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/01_6.9.2_Detailed_Description_of_Multigrid_on_One_Dimensional_Poisson’s_Equation.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/01_6.9.2_Detailed_Description_of_Multigrid_on_One_Dimensional_Poisson’s_Equation.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/01_6.9.2_Detailed_Description_of_Multigrid_on_One_Dimensional_Poisson’s_Equation.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.9_Multigrid/01_6.9.2_Detailed_Description_of_Multigrid_on_One_Dimensional_Poisson’s_Equation.m) |
| 6.10.1 | 非重叠分解：界面 Schur 补 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/00_6.10.1_Nonoverlapping_Methods.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/00_6.10.1_Nonoverlapping_Methods.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/00_6.10.1_Nonoverlapping_Methods.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/00_6.10.1_Nonoverlapping_Methods.m) |
| 6.10.2 | 重叠 Additive Schwarz 预条件 | [HTML](6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/01_6.10.2_Overlapping_Methods.html) | [MD](6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/01_6.10.2_Overlapping_Methods.md) | [PY](6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/01_6.10.2_Overlapping_Methods.py) | [M](6_Iterative_Methods_for_Linear_Systems/6.10_Domain_Decomposition/01_6.10.2_Overlapping_Methods.m) |
| 3.1 | 最小二乘的几何投影与残差正交 | [HTML](3_Linear_Least_Squares_Problems/00_3.1_Introduction.html) | [MD](3_Linear_Least_Squares_Problems/00_3.1_Introduction.md) | [PY](3_Linear_Least_Squares_Problems/00_3.1_Introduction.py) | [M](3_Linear_Least_Squares_Problems/00_3.1_Introduction.m) |
| 3.2.1 | 正规方程的条件数平方效应 | [HTML](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/00_3.2.1_Normal_Equations.html) | [MD](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/00_3.2.1_Normal_Equations.md) | [PY](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/00_3.2.1_Normal_Equations.py) | [M](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/00_3.2.1_Normal_Equations.m) |
| 3.2.2 | QR 的正交基与上三角回代 | [HTML](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/01_3.2.2_QR_Decomposition.html) | [MD](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/01_3.2.2_QR_Decomposition.md) | [PY](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/01_3.2.2_QR_Decomposition.py) | [M](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/01_3.2.2_QR_Decomposition.m) |
| 3.2.3 | SVD、伪逆和最小范数解 | [HTML](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/02_3.2.3_Singular_Value_Decomposition.html) | [MD](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/02_3.2.3_Singular_Value_Decomposition.md) | [PY](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/02_3.2.3_Singular_Value_Decomposition.py) | [M](3_Linear_Least_Squares_Problems/3.2_Matrix_Factorizations_That_Solve_the_Linear_Least_Squares_Problem/02_3.2.3_Singular_Value_Decomposition.m) |
| 3.3 | 最小二乘扰动理论与观测敏感性 | [HTML](3_Linear_Least_Squares_Problems/02_3.3_Perturbation_Theory_for_the_Least_Squares_Problem.html) | [MD](3_Linear_Least_Squares_Problems/02_3.3_Perturbation_Theory_for_the_Least_Squares_Problem.md) | [PY](3_Linear_Least_Squares_Problems/02_3.3_Perturbation_Theory_for_the_Least_Squares_Problem.py) | [M](3_Linear_Least_Squares_Problems/02_3.3_Perturbation_Theory_for_the_Least_Squares_Problem.m) |

**推荐顺序：** 先用 6.9.2 的 15→7→3→1 几何 V-cycle 掌握残差与误差校正，再读 6.10.1 子域内解和界面 Schur 补，最后读 6.10.2 重叠加性 Schwarz。第三章从 3.1 正交投影建立概念，依次推导 3.2.1 正规方程、3.2.2 QR、3.2.3 SVD 和 3.3 扰动界；核心问题是“数值等价是否意味着同样稳定”。

**测试与限制：** `python -m unittest discover -s tests -v`、`python scripts/validate_site.py`、`python scripts/browser_check.py`、`python main.py --check`。新增 8 篇均有本地离线 MathML、SVG 与可变参数交互，Playwright 在 1440 / 768 / 390 / 360 像素验证。Python 用 NumPy 确定性算例复算残差、谱、正交性；MATLAB/Octave 对照可运行但不在未执行时宣称实机通过。来源为 Demmel 原书对应 §6.9.2、§6.10、§3.1–3.3；软件实现以 NumPy 官方 API 为准。
