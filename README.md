# 应用数值线性代数 · Applying Numerical Linear Algebra

> 一套围绕“问题结构—条件数—数值稳定性—算法实现—性能验证”组织的中文数值线性代数课程。

**在线课程入口：** [打开课程首页](https://1998x-stack.github.io/Applying_Numerical_Linear_Algebra/)（发布状态以 GitHub Actions 和实际站点检查为准）。

## 本轮课程建设

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

## 学习路线

问题类型 → 矩阵分解 → 条件数 → 浮点误差与稳定性 → 性能分析 → 数值软件 → 多项式求值案例。

## 仓库结构

```text
.
├── index.html                 # 课程门户
├── README.md / README.html
├── AGENTS.md                  # 数学、内容、代码和发布规范
├── courses.json               # 课程元数据
├── assets/                    # CSS、JS、原创 SVG
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
