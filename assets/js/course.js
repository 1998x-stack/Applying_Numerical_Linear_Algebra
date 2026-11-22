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

  // Exact-arithmetic toy CG recurrence on SPD diag(1,2,3,4).
  // Projection onto K_k gives the same iterates in this SPD example.
  function toyCG(steps) {
    const diag = [1, 2, 3, 4], exact = diag.map(v => 1/v);
    let x = [0,0,0,0], r = [1,1,1,1], p = r.slice(), rr = 4;
    for (let k=0; k<Math.min(steps,4); k++) {
      const Ap = p.map((v,i)=>diag[i]*v);
      const denom = p.reduce((s,v,i)=>s+v*Ap[i],0);
      const alpha = rr/denom;
      x = x.map((v,i)=>v+alpha*p[i]);
      r = r.map((v,i)=>v-alpha*Ap[i]);
      const rrNew = r.reduce((s,v)=>s+v*v,0);
      if (rrNew < 1e-26) break;
      const beta = rrNew/rr;
      p = r.map((v,i)=>v+beta*p[i]);
      rr=rrNew;
    }
    const residual=Math.sqrt(x.reduce((s,v,i)=>s+Math.pow(1-diag[i]*v,2),0));
    const energy=Math.sqrt(x.reduce((s,v,i)=>s+diag[i]*Math.pow(exact[i]-v,2),0));
    return {residual,energy};
  }

  function updateDemo(panel) {
    const control = panel.querySelector("[data-demo-control]");
    const output = panel.querySelector("[data-demo-output]");
    if (!control || !output) return;
    const kind = panel.dataset.demoKind;
    const value = control.value;
    const meter = panel.querySelector("[data-demo-meter]");
    if (meter) {
      const min = Number(control.min), max = Number(control.max);
      const pct = max > min ? (Number(value)-min)/(max-min) : 0;
      meter.style.width = (8+92*Math.max(0,Math.min(1,pct))).toFixed(1)+"%";
    }

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

    } else if (kind === "sor") {
      const w=Number(value), n=16, x=Array(n).fill(0);
      for(let k=0;k<12;k++){
        const old=x.slice();
        for(let i=0;i<n;i++) {
          const candidate=(1+(i>0?x[i-1]:0)+(i+1<n?old[i+1]:0))/2;
          x[i]=(1-w)*old[i]+w*candidate;
        }
      }
      const residual=Math.sqrt(x.reduce((sum,v,i)=>sum+Math.pow(1-(2*v-(i>0?x[i-1]:0)-(i+1<n?x[i+1]:0)),2),0));
      const optimal=2/(1+Math.sin(Math.PI/(n+1)));
      output.textContent="1D Poisson N=16，做 12 次 SOR 扫描后真实残差 ||b−Ax||₂ ≈ "+residual.toFixed(5)+
        "（初始残差=4）。ω="+w.toFixed(2)+"；仅对此模型 ω*≈"+optimal.toFixed(3)+"。";
    } else if(kind==="spectral") {
      const n=Number(value), j=Math.cos(Math.PI/(n+1)),gs=j*j;
      const optimal=2/(1+Math.sin(Math.PI/(n+1)));
      output.textContent="1D Dirichlet Poisson N="+n+"：ρ(J)="+j.toFixed(5)+
        "；ρ(GS)="+gs.toFixed(5)+"；ω*="+optimal.toFixed(5)+
        "，相应 ρ(SOR*)≈"+(optimal-1).toFixed(5)+"。属于指定模型的理论谱关系。";
    } else if(kind==="criteria") {
      const d=Number(value),rho=2/d;
      output.textContent="A=(d−1)I+11ᵀ (3×3)，d="+d.toFixed(1)+
        "；A 在 d>1 时 SPD，但 Jacobi 的谱半径 ρ=2/d≈"+rho.toFixed(4)+
        "。"+(rho<1-1e-10?"本例 Jacobi 收敛。":Math.abs(rho-1)<1e-10?"此时是 ρ=1 的临界反例，不能保证收敛。":"虽然 A 是 SPD，Jacobi 在此例仍不收敛。");
    } else if(kind==="cheb") {
      const k=Number(value),bound=1/Math.cosh(k*Math.acosh(1.25));
      output.textContent="谱区间 [1,9]、Chebyshev 次数 k="+k+
        "：归一化多项式的最大绝对值 ≤ 1/Tₖ(5/4) ≈ "+bound.toFixed(6)+
        "；此值为可证明上界，不是测得的运行时间。";
    } else if(kind==="krylov") {
      const k=Number(value);
      output.textContent="A=diag(1,2,3,4)，r₀=(1,1,1,1)：由 "+k+
        " 个幂向量构成的 Krylov 空间维数="+k+"。若改为 r₀=e₁，同样的操作维数始终只有 1。";
    } else if(kind==="projection") {
      const k=Number(value), cg=toyCG(k);
      output.textContent="SPD 对角示例的 Galerkin 投影维数 k="+k+
        "：投影矩阵大小 "+k+"×"+k+"；真实残差 ||b−Axₖ||₂ ≈ "+cg.residual.toExponential(4)+
        "；A-范数误差 ≈ "+cg.energy.toExponential(4)+"。与精确算术 CG 的 k 步解对应。";
    } else if(kind==="cgsteps") {
      const k=Number(value),cg=toyCG(k);
      output.textContent="A=diag(1,2,3,4) 的 CG 第 "+k+" 步：真实残差 ||b−Axₖ||₂ ≈ "+
        cg.residual.toExponential(4)+"；||x*−xₖ||_A ≈ "+cg.energy.toExponential(4)+
        "。有限步性质只适用于精确算术。";
    } else if(kind==="cgbound") {
      const kappa=Number(value),q=(Math.sqrt(kappa)-1)/(Math.sqrt(kappa)+1);
      output.textContent="假设 SPD 条件数 κ="+kappa+"，取 k=10：CG 的 A-范数误差比最坏界 2q¹⁰ ≈ "+
        (2*Math.pow(q,10)).toFixed(6)+"，其中 q="+q.toFixed(5)+
        "。这是理论上界，不是普通残差 2-范数比，也不是任何特定矩阵的实测值。";
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