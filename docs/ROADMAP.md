# 建设路线

## 课程基线

本仓库包含七章课程和原有 HTML / Markdown / Python / MATLAB 文件。旧页面保留稳定路径；第一批优先重构第一章中八篇核心内容。

## 第一批：第一章 8 篇

| 编号 | 主题 | 页面状态 | 数学/代码重点 |
|---|---|---|---|
| 01 | 数值线性代数的语言：向量、矩阵与记号 | 本分支已重写，待 CI/Pages 验收 | 推导、SVG、Python、MATLAB、证据台账 |
| 02 | 数值线性代数究竟要解决哪些问题 | 本分支已重写，待 CI/Pages 验收 | 推导、SVG、Python、MATLAB、证据台账 |
| 03 | 为什么要把矩阵分解成更简单的矩阵 | 本分支已重写，待 CI/Pages 验收 | 推导、SVG、Python、MATLAB、证据台账 |
| 04 | 输入误差如何放大：扰动理论与条件数 | 本分支已重写，待 CI/Pages 验收 | 推导、SVG、Python、MATLAB、证据台账 |
| 05 | 计算机为什么会算错：舍入误差与稳定性 | 本分支已重写，待 CI/Pages 验收 | 推导、SVG、Python、MATLAB、证据台账 |
| 06 | 为什么 FLOPs 少不一定跑得快 | 本分支已重写，待 CI/Pages 验收 | 推导、SVG、Python、MATLAB、证据台账 |
| 07 | 如何构建可信的数值计算软件 | 本分支已重写，待 CI/Pages 验收 | 推导、SVG、Python、MATLAB、证据台账 |
| 08 | 多项式求值：Horner 方法与数值稳定性 | 本分支已重写，待 CI/Pages 验收 | 推导、SVG、Python、MATLAB、证据台账 |

## 后续批次建议

1. **第二章 2.1–2.4**：线性系统建模、扰动、带主元高斯消去、后向误差与条件数估计。
2. **第二章 2.5–2.7**：迭代改进、均衡化、BLAS/分块算法和特殊矩阵。
3. **第三章**：正规方程、QR、SVD、Householder/Givens、秩亏最小二乘。
4. **第四至第五章**：Schur、非对称/对称特征值问题、SVD 算法。
5. **第六至第七章**：Jacobi、Gauss–Seidel、SOR、Krylov/CG、多重网格、Lanczos。

## 状态约定

- S0：原始资料/占位内容。
- S1：课程目录和稳定链接。
- S2：独立文章完成，具备完整定义、推导、案例和边界。
- S3：数学与来源审计完成。
- S4：Python/MATLAB 实验、静态检查和浏览器 QA 完成。
- S5：Actions 与 Pages 部署验收完成。

只有有证据的检查才能提升状态；静态通过不等于浏览器通过，commit 不等于 Pages 已发布。

## 第二批：第六章 8 篇（2026-11-22）

- 6.1 残差、前向误差与收敛/停止准则
- 6.2 根据矩阵结构筛选 CG、MINRES、GMRES、LSQR 等求解器
- 6.3.1 一维 Poisson 中心差分与三对角正定系统
- 6.3.2 二维 Poisson 五点模板与稀疏非零元数
- 6.3.3 Kronecker 积、列主序 vec 与矩阵自由算子
- 6.4 二维规则 Poisson 模型上的复杂度比较
- 6.5.1 Jacobi 双缓冲同步更新与谱半径
- 6.5.2 Gauss–Seidel 新旧分量复用与红黑排序

状态：源文档、示例、SVG 与证据台账已提交到工作分支；CI / Pages 必须以远端结果为准。后续 6.5.3 SOR、6.6 Krylov/CG、6.7 FFT、6.9 Multigrid 将按同一标准逐篇完善。


## 第三批：第二章 8 篇（2026-11-22）

- **2.1 从 Ax=b 出发：求解可靠性**：独立 HTML / MD，Python / MATLAB 实验，SVG 与 evidence/09.json
- **2.2 矩阵与右端项同时扰动**：独立 HTML / MD，Python / MATLAB 实验，SVG 与 evidence/10.json
- **2.2.1 范数与逐元素相对扰动**：独立 HTML / MD，Python / MATLAB 实验，SVG 与 evidence/11.json
- **2.3 高斯消去 PA=LU**：独立 HTML / MD，Python / MATLAB 实验，SVG 与 evidence/12.json
- **2.4.1 小主元为何危险**：独立 HTML / MD，Python / MATLAB 实验，SVG 与 evidence/13.json
- **2.4.2 舍入误差与增长因子**：独立 HTML / MD，Python / MATLAB 实验，SVG 与 evidence/14.json
- **2.4.3 逆范数与条件数诊断**：独立 HTML / MD，Python / MATLAB 实验，SVG 与 evidence/15.json
- **2.4.4 残差、BERR 与前向界**：独立 HTML / MD，Python / MATLAB 实验，SVG 与 evidence/16.json

本批提交以 S2/S3 内容与代码基线为目标；S4/S5 只在实际 Actions/Pages 验收成功后标记，MATLAB 未实机执行前不标记为已验证。


## 第四批：第六章 6.5.3–6.6.4（2026-11-22）

- **6.5.3** SOR：松弛参数与步长：独立 HTML / MD / Python / MATLAB / evidence
- **6.5.4** 误差慢模态：三种迭代的收敛尺度：独立 HTML / MD / Python / MATLAB / evidence
- **6.5.5** SPD 仍可能使 Jacobi 不收敛：独立 HTML / MD / Python / MATLAB / evidence
- **6.5.6** Chebyshev 加速和 SSOR：独立 HTML / MD / Python / MATLAB / evidence
- **6.6.1** 只用 Av 提取 Krylov 信息：独立 HTML / MD / Python / MATLAB / evidence
- **6.6.2** Krylov 投影与残差正交：独立 HTML / MD / Python / MATLAB / evidence
- **6.6.3** CG：A-共轭短递推：独立 HTML / MD / Python / MATLAB / evidence
- **6.6.4** CG 的 A-范数误差界：独立 HTML / MD / Python / MATLAB / evidence

对所有模块按“独立问题 → 公式推导 → 具体算例 → 解释图 → 原生交互 → 限制 → 证据”组织；保留原有文件路径与章节顺序。新增 `tests/test_chapter6_batch4.py` 与既有 `scripts/browser_check.py` 16 篇验收。第六章深化进度 16 篇，全站累计 32 篇；CI 和 Pages 的 S4/S5 状态需根据实际远端结果标注。


## 第五批：第二章 2.5–2.7 八篇进阶精讲

- 2.5.1 迭代改进：低精度分解与高精度残差：HTML / MD / Python / MATLAB / SVG 与 evidence/17.json，路径 2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/00_2.5.1_Single_Precision_Iterative_Refinement
- 2.5.2 矩阵均衡化：量级变化与真实病态：HTML / MD / Python / MATLAB / SVG 与 evidence/18.json，路径 2_Linear_Equation_Solving/2.5_Improving_the_Accuracy_of_a_Solution/01_2.5.2_Equilibration
- 2.6.1 BLAS 三级与数据复用：HTML / MD / Python / MATLAB / SVG 与 evidence/19.json，路径 2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/00_2.6.1_Basic_Linear_Algebra_Subroutines_(BLAS)
- 2.6.2 分块矩阵乘法与缓存工作集：HTML / MD / Python / MATLAB / SVG 与 evidence/20.json，路径 2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/01_2.6.2_How_to_Optimize_Matrix_Multiplication
- 2.6.3 分块 LU 与 Schur 补：HTML / MD / Python / MATLAB / SVG 与 evidence/21.json，路径 2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/02_2.6.3_Reorganizing_Gaussian_Elimination_to_use_Level_3_BLAS
- 2.6.4 Roofline、Amdahl 与并行瓶颈：HTML / MD / Python / MATLAB / SVG 与 evidence/22.json，路径 2_Linear_Equation_Solving/2.6_Blocking_Algorithms_for_Higher_Performance/03_2.6.4_More_About_Parallelism_and_Other_Performance_Issues
- 2.7.1 Cholesky：对称正定与 LLᵀ：HTML / MD / Python / MATLAB / SVG 与 evidence/23.json，路径 2_Linear_Equation_Solving/2.7_Special_Linear_Systems/00_2.7.1_Real_Symmetric_Positive_Definite_Matrices
- 2.7.2 对称不定：LDLᵀ 与 2×2 主元：HTML / MD / Python / MATLAB / SVG 与 evidence/24.json，路径 2_Linear_Equation_Solving/2.7_Special_Linear_Systems/01_2.7.2_Symmetric_Indefinite_Matrices

本批深度门禁：每篇对照数学假设、可调可视化和代码测试；新增 tests/test_chapter2_advanced.py（18 项）。原 Chapter 6 的 16 篇深化成果保留。合并后的课程合计 40 篇深度文章。Pages/CI 须按对应 SHA 的结果记录。


## 第六批：第六章 6.6.5–6.9.1（2026-11-22）

- 6.6.5 预条件：让困难的 SPD 系统拥有更好的谱：HTML / Markdown / Python / MATLAB / 原生 MathML / SVG / evidence
- 6.6.6 GMRES：非对称系统的残差最小化：HTML / Markdown / Python / MATLAB / 原生 MathML / SVG / evidence
- 6.7.1 离散 Fourier 变换 DFT 的方向与能量：HTML / Markdown / Python / MATLAB / 原生 MathML / SVG / evidence
- 6.7.2 连续/离散 Poisson 的正弦谱求解：HTML / Markdown / Python / MATLAB / 原生 MathML / SVG / evidence
- 6.7.3 卷积定理、线性卷积和补零：HTML / Markdown / Python / MATLAB / 原生 MathML / SVG / evidence
- 6.7.4 radix-2 FFT 与蝶形递归：HTML / Markdown / Python / MATLAB / 原生 MathML / SVG / evidence
- 6.8 块循环约化与 Schur 补：HTML / Markdown / Python / MATLAB / 原生 MathML / SVG / evidence
- 6.9.1 二维 Poisson 的两网格纠错：HTML / Markdown / Python / MATLAB / 原生 MathML / SVG / evidence

全站 48 篇，其中第六章 24 篇；CI/Pages 只按实际成功的 workflow 和 SHA 更新发布状态。强调 PCG 必须保留 SPD 理论条件、GMRES 的真残差与 Arnoldi 内部残差区分、DST-I 与周期 DFT 边界差别、BCR 的 Schur 填充，以及多重网格重新离散与 Galerkin 粗算子的不同。


## 第七批：第六章多重网格 / 区域分解，第三章最小二乘（2026-11-22）

- 6.9.2：一维 Poisson 的完整多重网格 V-cycle。
- 6.10.1：非重叠分解：界面 Schur 补。
- 6.10.2：重叠 Additive Schwarz 预条件。
- 3.1：最小二乘的几何投影与残差正交。
- 3.2.1：正规方程的条件数平方效应。
- 3.2.2：QR 的正交基与上三角回代。
- 3.2.3：SVD、伪逆和最小范数解。
- 3.3：最小二乘扰动理论与观测敏感性。

实现了 8 篇自足内容和 Python/MATLAB 数值案例，累计 56 篇。第六章达到 27 篇，第三章 5 篇。逐项对照教材推导、代码断言和浏览器验收：完整递归 V-cycle、界面 Schur 补、一层 additive Schwarz、最小二乘正交投影、κ(AᵀA)=κ(A)²、QR 与 SVD 最小范数、b-only 扰动界。页面状态需以实际 CI/Pages 工作流确认。
