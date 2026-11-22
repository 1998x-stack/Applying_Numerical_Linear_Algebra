(() => {
  "use strict";

  const solverAdvice = {
    spd: "优先考虑 CG；要求矩阵对称（Hermitian）正定。预条件器应近似 A⁻¹，且满足 CG 对预条件器的正定性要求。",
    symmetric: "对称不定系统可评估 MINRES；先确认矩阵确实对称，并检查实现对奇异或近奇异情形的说明。",
    general: "一般非对称方阵可评估 GMRES / BiCGSTAB；注意重启长度、预条件方向和真实残差停止条件。",
    least: "最小二乘问题优先评估 LSQR / LSMR；不要把一般超定问题误当作可直接调用 CG 的方阵系统。"
  };

  const methodAdvice = {
    jacobi: "Jacobi 每轮是 O(nnz(A)) 的稀疏矩阵更新，容易并行；对 Poisson 网格通常收敛偏慢，常作为教学基线或平滑器。",
    cg: "CG 适用于对称正定系统。每轮主要是矩阵向量乘法与向量运算；总成本受条件数和预条件器影响。",
    fft: "FFT 利用规则矩形网格和可分离算子，速度很快；边界、系数或几何一旦偏离模型假设，就不能直接套用同一结论。",
    multigrid: "多重网格通过不同尺度消除误差；对合适的椭圆问题可接近线性复杂度，但平滑、限制、延拓和粗网格求解都必须设计正确。",
    direct: "稀疏 Cholesky / LU 可提供直接解法；实际代价受消元填充、排序、内存和稀疏结构影响。"
  };

  function updateDemo(panel) {
    const control = panel.querySelector("[data-demo-control]");
    const output = panel.querySelector("[data-demo-output]");
    if (!control || !output) return;
    const kind = panel.dataset.demoKind;
    const value = control.value;

    if (kind === "tolerance") {
      const tolerance = Math.pow(10, Number(value));
      output.textContent = "当前相对阈值 rtol = " + tolerance.toExponential(0) +
        "。实际停止界为 max(rtol · ||b||₂, atol)；若 ||b||₂ = 0，绝对阈值尤其重要。";
    } else if (kind === "solver") {
      output.textContent = solverAdvice[value] || "先判断矩阵结构，再查看求解器的适用条件与停止准则。";
    } else if (kind === "grid1d") {
      const n = Number(value), h = 1 / (n + 1);
      output.textContent = "内部未知量 N = " + n + "；网格间距 h = " + h.toFixed(4) +
        "；三对角矩阵非零元数 = " + (3 * n - 2) + "。";
    } else if (kind === "grid2d") {
      const n = Number(value), unknowns = n * n, nnz = 5 * n * n - 4 * n;
      output.textContent = n + " × " + n + " 个内部网格点共有 " + unknowns +
        " 个未知量；五点模板矩阵最多有 " + nnz + " 个非零元，而不是 " +
        (unknowns * unknowns) + " 个稠密存储位置。";
    } else if (kind === "kronecker") {
      const dims = value.split("x").map(Number), nx = dims[0], ny = dims[1];
      output.textContent = "V 的形状为 " + nx + " × " + ny + "；vec(V) 有 " +
        (nx * ny) + " 个分量；算子维度为 " + (nx * ny) + " × " + (nx * ny) +
        "，可写成 Iᵧ ⊗ Tₓ + Tᵧ ⊗ Iₓ（等距网格需再乘 h⁻²）。";
    } else if (kind === "method") {
      output.textContent = methodAdvice[value] || "结合矩阵结构、精度目标、内存和硬件测量选择。";
    } else if (kind === "jacobi") {
      const n = Number(value), rho = Math.cos(Math.PI / (n + 1));
      const sweeps = Math.ceil(-1 / Math.log(rho));
      output.textContent = "一维 Dirichlet Poisson 的 Jacobi 谱半径 ρ = cos(π/(N+1)) ≈ " +
        rho.toFixed(5) + "。误差缩小到 e⁻¹ 约需 " + sweeps +
        " 轮（谱半径模型；实际误差还取决于初始误差中的各个模态）。";
    } else if (kind === "gauss-seidel") {
      const n = Number(value), rhoJ = Math.cos(Math.PI / (n + 1)), rhoGS = rhoJ * rhoJ;
      output.textContent = "二维 Poisson 的红黑排序满足本模型的谱关系 ρ(GS) = ρ(J)²；当前 N = " +
        n + " 时，ρ(J) ≈ " + rhoJ.toFixed(5) + "，ρ(GS) ≈ " + rhoGS.toFixed(5) +
        "。该关系依赖模型与排序，不应推广到任意矩阵。";
    }
  }

  document.querySelectorAll("[data-demo-panel]").forEach((panel) => {
    const control = panel.querySelector("[data-demo-control]");
    if (!control) return;
    control.addEventListener("input", () => updateDemo(panel));
    control.addEventListener("change", () => updateDemo(panel));
    updateDemo(panel);
  });

  const search = document.querySelector("[data-course-search]");
  const list = document.querySelector("[data-course-list]");
  const empty = document.querySelector("[data-search-empty]");
  if (search && list) {
    const rows = Array.from(list.querySelectorAll("[data-search]"));
    search.addEventListener("input", () => {
      const query = search.value.trim().toLocaleLowerCase();
      let visible = 0;
      rows.forEach((row) => {
        const haystack = (row.dataset.search + " " + row.textContent).toLocaleLowerCase();
        const match = !query || haystack.includes(query);
        row.hidden = !match;
        if (match) visible += 1;
      });
      if (empty) empty.hidden = visible !== 0;
    });
  }
})();