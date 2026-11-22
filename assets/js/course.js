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

    } else if (kind==="pcg") {
      const max=Number(value);
      output.textContent="对角 SPD 示例 A=diag(1,4,10,"+max+")：κ₂(A)="+Math.max(max,10)+
        "；取 M=diag(A) 后 C=I，κ₂(C)=1。该等式只在此对角案例中成立。";
    } else if (kind==="gmres") {
      const k=Number(value),vals=[3.7416573868,2.1340611208,1.4852213145,0];
      output.textContent="非对称上三角 3×3 模型，满 GMRES 的 Krylov 维数 k="+k+
        "，真实残差 ||b−Axₖ||₂≈"+vals[k].toFixed(6)+
        "。这些值取自对应微型算例，不代表重启 GMRES 的通用曲线。";
    } else if (kind==="dft") {
      const k=Number(value),cs=["3","1−2i","−1","1+2i"],amp=[3,Math.sqrt(5),1,Math.sqrt(5)];
      output.textContent="x=(1,2,0,0)，N=4；频率 j="+k+" 的 Xⱼ="+cs[k]+
        "，|Xⱼ|="+amp[k].toFixed(5)+"。Σ|Xⱼ|²/N=5=Σ|xₖ|²。";
    } else if (kind==="sine") {
      const n=Number(value),h=1/(n+1),lambda=4*Math.sin(Math.PI/(2*(n+1)))**2/h**2;
      output.textContent="N="+n+"，h="+h.toFixed(5)+
        "：首个离散正弦模态的 λ₁,h="+lambda.toFixed(6)+
        "；连续 π²="+(Math.PI*Math.PI).toFixed(6)+
        "；振幅相对差 |π²/λ−1|="+Math.abs(Math.PI**2/lambda-1).toExponential(4)+"。";
    } else if (kind==="convolution") {
      const n=Number(value),sequence=n===3?"(0, 1, −1)":"(1, 1, −1, −1)";
      output.textContent="a=(1,2,1)，b=(1,−1)，L="+n+
        "。"+(n>=4?"补零足够：IFFT/FFT 的前 4 项是线性卷积 ":"补零不足：末端的 −1 回绕，循环卷积变为 ")+sequence+
        "。线性结果始终是 (1,1,−1,−1)。";
    } else if (kind==="fft") {
      const m=Number(value),n=2**m;
      output.textContent="radix-2 的 N=2^"+m+"="+n+
        "；递归层数="+m+"；每层 N/2="+n/2+
        " 个蝶形，总数="+n*m/2+"。这是运算图计数，不是实际用时。";
    } else if (kind==="bcr") {
      const n=Number(value),blocks=Math.floor(n/2);
      output.textContent="二维 N×N 内部网格，N="+n+"，原有 "+n*n+
        " 个未知量。一次交替块行消元保留 "+blocks+
        " 个宽度 N 的块，即 "+n*blocks+" 个未知量。Schur 块可能变稠密。";
    } else if (kind==="mg") {
      const nu=Number(value),c=Math.cos(Math.PI/8);
      const low=Math.abs(1-(2/3)*(1-c))**nu;
      const high=Math.abs(1-(2/3)*(1+c))**nu;
      output.textContent="N=7 Dirichlet Poisson、ω=2/3 加权 Jacobi 作用 "+nu+
        " 轮：最低二维正弦模态因子绝对值≈"+low.toFixed(5)+
        "，最高模态≈"+high.toExponential(3)+
        "。低频仍顽固，故需要粗网格校正；非两网格实测残差。";

    } else if(kind==="vcycle"){
      const cycles=Number(value),n=15;
      function Ap(x){const h=1/(x.length+1),h2=h*h;return x.map((v,i)=>(2*v-(i?x[i-1]:0)-(i+1<x.length?x[i+1]:0))/h2);}
      function mg(b,x){
        const n=b.length,h=1/(n+1);
        if(n===1)return [b[0]*h*h/2];
        const smooth=a=>{const aa=Ap(a);return a.map((v,i)=>v+(2/3)*(h*h/2)*(b[i]-aa[i]));};
        x=smooth(smooth(x));const aa=Ap(x),r=b.map((v,i)=>v-aa[i]),rc=[];
        for(let j=1;j<n;j+=2)rc.push((r[j-1]+2*r[j]+r[j+1])/4);
        const ec=mg(rc,Array(rc.length).fill(0)),e=Array(n).fill(0);
        ec.forEach((v,i)=>e[2*i+1]=v);
        for(let i=0;i<n;i+=2)e[i]=((i>0?e[i-1]:0)+(i+1<n?e[i+1]:0))/2;
        return smooth(smooth(x.map((v,i)=>v+e[i])));
      }
      const truth=Array.from({length:n},(_,i)=>Math.sin(Math.PI*(i+1)/(n+1))),b=Ap(truth);
      let x=Array(n).fill(0);for(let k=0;k<cycles;k++)x=mg(b,x);
      const Ax=Ap(x),res=Math.sqrt(b.reduce((acc,v,i)=>acc+(v-Ax[i])**2,0));
      output.textContent="1D Poisson 15→7→3→1 四层 V-cycle 执行 "+cycles+
        " 次；真实残差 ||b−Ax||₂≈"+res.toExponential(5)+
        "（b=A sin(πih)，每层前、后各两次加权 Jacobi）。";
    } else if(kind==="substructure"){
      const n=Number(value),k=(n-1)/2,S=2/(k+1);
      output.textContent="一维 Poisson 共 "+n+" 个内部点，两子域各 "+k+" 个内部点，界面 1 个节点；Schur S=2/(k+1)≈"+
      S.toFixed(6)+"。这是指定三对角模型的解析式。";
    } else if(kind==="schwarz"){
      const q=Number(value),last=3+Math.floor((q-1)/2),first=4-Math.ceil((q+1)/2);
      output.textContent="n=7，Ω₁={0,…,"+last+"}、Ω₂={"+first+",…,6}；重叠节点序号 "+first+" 到 "+last+
        " 共 "+q+" 个。Additive Schwarz 叠加局部修正，还需检查步长和谱。";
    } else if(kind==="householder"){
      const b=Number(value),r=Math.hypot(3,b);
      output.textContent="x=(3,"+b.toFixed(1)+")，||x||₂="+r.toFixed(5)+
        "；取 v=x+||x||e₁，反射 Hx=(−"+r.toFixed(5)+",0)，2-范数保持（精确算术）。";
    } else if(kind==="givens"){
      const b=Number(value),r=Math.hypot(3,b),c=3/r,s=b/r;
      output.textContent="a=3、b="+b+"，r=hypot(a,b)="+r.toFixed(5)+"，c="+c.toFixed(5)+
        "，s="+s.toFixed(5)+"；[[c,s],[−s,c]](a,b)ᵀ=(r,0)ᵀ。";
    } else if(kind==="orthround"){
      const p=Number(value),epsilon=10**(-p),approx=Math.sqrt(64/(20*epsilon*epsilon));
      output.textContent="A=[1,1+εt]、ε=10⁻"+p+
        " 的 κ₂(A) 小 ε 渐近估算≈"+approx.toExponential(4)+
        "；正交 Q 的 κ₂(Q)=1；真实 ηQ 和 ηA 必须运行数值代码测量。";
    } else if(kind==="orthogonal"){
      const th=Number(value)*Math.PI/180,c=Math.cos(th),s=Math.sin(th);
      const x=3*c-4*s,y=3*s+4*c;
      output.textContent="旋转角 "+value+"°：Q(3,4)ᵀ≈("+x.toFixed(4)+","+y.toFixed(4)+
        ")ᵀ；||Qx||₂=5、κ₂(Q)=1。";
    } else if(kind==="tsvd"){
      const tau=Number(value),keep=tau<0.02;
      const length=keep?Math.sqrt(2):1,residual=keep?.1:Math.hypot(.1,.02);
      output.textContent="Σ=(5,0.02,0)，阈值 τ="+tau.toFixed(2)+"：保留 "+
        (keep?2:1)+" 个有效模态，||xτ||₂="+length.toFixed(5)+
        "，真实 ||b−Axτ||₂="+residual.toFixed(5)+
        "。保留规则是严格 σ>τ，τ=0.02 时不保留第二模态。";
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