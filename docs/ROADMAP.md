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
