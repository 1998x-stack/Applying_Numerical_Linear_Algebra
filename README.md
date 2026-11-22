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
