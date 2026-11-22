# 应用数值线性代数 · Applying Numerical Linear Algebra

这是一本面向数值计算学习者的开放式课程伴读仓库。课程围绕**问题结构、数值稳定性、算法代价与可复现实验**展开：不只给出公式，还解释公式如何变成可运行的算法、算法在什么条件下可靠，以及如何验证计算结果。

> 本仓库以 James W. Demmel, *Applied Numerical Linear Algebra*（SIAM, 1997）为主要知识脉络，配合现代 Python / MATLAB 实验和独立绘制的图解。它不是 SIAM 官方课程或原书的逐字翻译；请将原书作为正式参考来源。

- **在线课程首页：** [打开课程门户](./index.html)
- **原书书目信息：** [SIAM Publications Library](https://doi.org/10.1137/1.9781611971446)
- **核心主题：** 线性方程组、最小二乘、特征值、SVD、稀疏迭代方法。

## 从哪里开始

如果你第一次学习数值线性代数，建议按以下顺序建立概念：

1. [基本记号与标准问题](./1_Introduction/00_1.1_Basic_Notation.html)：区分向量、矩阵、范数和问题类型。
2. [高斯消去与误差分析](./2_Linear_Equation_Solving/03_2.3_Gaussian_Elimination.html)：理解直接法、主元和后向稳定性。
3. [线性最小二乘](./3_Linear_Least_Squares_Problems/00_3.1_Introduction.html)：从残差最小化连接 QR 与 SVD。
4. [第六章：迭代求解线性系统](./6_Iterative_Methods_for_Linear_Systems/00_6.1_Introduction.html)：从停止准则走向 Poisson 模型、Jacobi 与 Gauss–Seidel。

## 七章课程地图

| 章节 | 核心问题 | 当前内容状态 |
|---|---|---|
| 1. Introduction | 浮点运算、范数、条件数与数值算法的基本语言 | 已有较完整的基础内容，仍需逐页技术审计 |
| 2. Linear Equation Solving | 如何稳定、高效地求解 (Ax=b) | 直接法与误差分析已有内容；部分高级主题待补 |
| 3. Linear Least Squares Problems | 如何处理超定、欠定和秩亏问题 | 已有主要方法内容，需继续统一实验与引用 |
| 4. Nonsymmetric Eigenvalue Problems | 非对称矩阵的特征值与 Schur / QR 算法 | 部分主题已有正文，多个高级主题待补 |
| 5. The Symmetric Eigenproblem and SVD | 对称特征问题与奇异值分解 | 待系统补写 |
| 6. Iterative Methods for Linear Systems | 稀疏系统、Poisson 方程与迭代求解器 | **第一批 8 个基础模块已精细化** |
| 7. Iterative Algorithms for Eigenvalue Problems | Rayleigh–Ritz、Lanczos 与大型特征值问题 | 待系统补写 |

## 第六章：第一批 8 个精细化模块

每个页面都可以独立阅读：先定义问题，再给出离散化或迭代公式，解释关键假设，配有原理图、可交互实验、Python / MATLAB 示例和证据清单。

| 模块 | 主题 | 页面 |
|---|---|---|
| 6.1 | 迭代法解决什么问题，何时停止 | [阅读](./6_Iterative_Methods_for_Linear_Systems/00_6.1_Introduction.html) · [Markdown](./6_Iterative_Methods_for_Linear_Systems/00_6.1_Introduction.md) |
| 6.2 | 如何选择迭代求解器与软件 | [阅读](./6_Iterative_Methods_for_Linear_Systems/01_6.2_On_line_Help_for_Iterative_Methods.html) · [Markdown](./6_Iterative_Methods_for_Linear_Systems/01_6.2_On_line_Help_for_Iterative_Methods.md) |
| 6.3.1 | 一维 Poisson 方程与三对角离散 | [阅读](./6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/00_6.3.1_Poisson’s_Equation_in_One_Dimension.html) · [Markdown](./6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/00_6.3.1_Poisson’s_Equation_in_One_Dimension.md) |
| 6.3.2 | 二维 Poisson 方程与五点模板 | [阅读](./6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/01_6.3.2_Poisson’s_Equation_in_Two_Dimensions.html) · [Markdown](./6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/01_6.3.2_Poisson’s_Equation_in_Two_Dimensions.md) |
| 6.3.3 | Kronecker 积如何组织二维算子 | [阅读](./6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/02_6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products.html) · [Markdown](./6_Iterative_Methods_for_Linear_Systems/6.3_Poisson’s_Equation/02_6.3.3_Expressing_Poisson’s_Equation_with_Kronecker_Products.md) |
| 6.4 | Poisson 模型问题上的算法比较 | [阅读](./6_Iterative_Methods_for_Linear_Systems/03_6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation.html) · [Markdown](./6_Iterative_Methods_for_Linear_Systems/03_6.4_Summary_of_Methods_for_Solving_Poisson’s_Equation.md) |
| 6.5.1 | Jacobi：全量旧迭代同步更新 | [阅读](./6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/00_6.5.1_Jacobi’s_Method.html) · [Markdown](./6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/00_6.5.1_Jacobi’s_Method.md) |
| 6.5.2 | Gauss–Seidel：立即复用新分量 | [阅读](./6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/01_6.5.2_Gauss–Seidel_Method.html) · [Markdown](./6_Iterative_Methods_for_Linear_Systems/6.5_Basic_Iterative_Methods/01_6.5.2_Gauss–Seidel_Method.md) |

## 仓库结构

```text
.
├── index.html                    # GitHub Pages 课程门户
├── README.md                     # 仓库入口与学习路线
├── assets/
│   ├── css/course.css            # 统一的课程与文章设计系统
│   └── js/course.js              # 搜索与教学交互
├── 1_Introduction/ ... 7_*/      # 按原书章节保留的教材内容
├── docs/
│   ├── ARCHITECTURE.md           # 目录、页面和发布约定
│   ├── CONTENT_STANDARD.md       # 独立讲解、引用与实验规范
│   └── improvements.md           # 追加式工程变更记录
├── scripts/browser_check.py      # 多视口浏览器验收
├── tests/                        # 数值回归与课程完整性测试
└── .github/workflows/            # 自动质量门禁与 Pages 发布
```

原有章节目录与页面路径保持不变。新增模块采用同名的 `.md`、`.html`、`.py`、`.m` 和 `evidence.json` 文件，避免因重命名破坏既有链接。

## 本地验证

需要 Python 3.10+。数值示例尽量使用 Python 标准库，避免为基础实验引入不必要的依赖。

```bash
# 检查章节文件是否成对存在；默认只读，不会覆盖讲义
python main.py --check

# 运行数值回归与课程完整性测试
python -m unittest discover -s tests -v

# 安装浏览器验收依赖并安装 Chromium
python -m pip install -r requirements-dev.txt
python -m playwright install chromium

# 逐页检查桌面、平板、手机视口、SVG 和交互
python scripts/browser_check.py
```

## 内容与质量约定

- 每一页必须是**独立、完整的解释**，不能只说“本节讨论了什么”；读者不需要先读上一页才能理解当前页面。
- 先讲清楚问题、变量、维度、边界条件和假设，再给公式、图解与算法。
- 图必须表达真实的数据流、网格邻接或迭代依赖；静态图在 JavaScript 未运行时也能说明核心概念。
- 数学公式使用可访问的 MathML；宽公式只能在公式容器内部滚动，不能让整个页面横向溢出。
- 数值例子要能运行，并通过残差、维度、对称性或与独立实现比较进行交叉验证。
- 每个新增页面包含 `evidence.json`，把关键事实标为 `verified`、`derived`、`illustrative` 或 `unverified`。
- 浏览器没有实际执行的视口或交互必须标记为未验证，不得写成已通过。

## 参考来源

- James W. Demmel, *Applied Numerical Linear Algebra*, SIAM, 1997. [书目与目录](https://doi.org/10.1137/1.9781611971446)
- [SciPy sparse linear algebra](https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html)：稀疏直接法、CG、GMRES、MINRES、LSQR 等接口。
- [SciPy Conjugate Gradient](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.cg.html)：CG 的正定性要求、停止条件和预条件器接口。

## 版权与来源

本仓库的解释文字、代码实验和 SVG 图解应保持独立创作，并在相关页面标明可核查来源。原书版权归作者与 SIAM 所有；引用书目不意味着获得原书内容或插图的再发布许可。
