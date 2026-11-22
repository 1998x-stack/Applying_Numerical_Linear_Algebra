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
      function A(x) {const h=1/(x.length+1);return x.map((u,i)=>(2*u-(i?x[i-1]:0)-(i+1<x.length?x[i+1]:0))/(h*h));}
      function mg(b,x) {
        const m=b.length,h=1/(m+1);
        if(m===1)return [b[0]*h*h/2];
        const smooth=(arr)=>{let Ax=A(arr);return arr.map((u,i)=>u+(2/3)*(h*h/2)*(b[i]-Ax[i]));};
        x=smooth(smooth(x));
        const rr=b.map((u,i)=>u-A(x)[i]),rc=[];
        for(let i=1;i<m;i+=2)rc.push((rr[i-1]+2*rr[i]+rr[i+1])/4);
        const ec=mg(rc,Array(rc.length).fill(0)),P=Array(m).fill(0);
        ec.forEach((v,i)=>P[2*i+1]=v);
        for(let i=0;i<m;i+=2)P[i]=((i>0?P[i-1]:0)+(i+1<m?P[i+1]:0))/2;
        x=x.map((u,i)=>u+P[i]);return smooth(smooth(x));
      }
      const truth=Array.from({length:n},(_,i)=>Math.sin(Math.PI*(i+1)/(n+1))),b=A(truth);
      let x=Array(n).fill(0);for(let j=0;j<cycles;j++)x=mg(b,x);
      const Ax=A(x),r=Math.sqrt(b.reduce((s,v,i)=>s+(v-Ax[i])**2,0));
      output.textContent="15→7→3→1 四层 Poisson V-cycle，完成 "+cycles+
        " 轮后真实 ||b−Ax||₂≈"+r.toExponential(5)+"（从零初值开始，b=A sin(πih)，每层前后各两次加权 Jacobi）。";
    } else if(kind==="substructure"){
      const n=Number(value),k=(n-1)/2,S=2/(k+1);
      output.textContent="1D Poisson N="+n+"（左右各 "+k+" 个内部点，公共界面 1 点），界面 Schur 补是单个数 S=2/(k+1)≈"+S.toFixed(6)+
        "；2k 个内部节点的方程可以分成两个独立子问题。";
    } else if(kind==="schwarz"){
      const overlap=Number(value),last=3+Math.floor((overlap-1)/2),first=4-Math.ceil((overlap+1)/2);
      output.textContent="n=7，Ω₁={0,…,"+last+"}，Ω₂={"+first+",…,6}；交叠自由度 "+overlap+
        " 个，序号 "+first+"…"+last+"；加性 Schwarz 在这些节点叠加两个局部校正。";
    } else if(kind==="fit"){
      const y=Number(value),beta=0.5,alpha=(3+y)/3-beta;
      const sq=(2*y-3)**2/6;
      output.textContent="三个观测 (1,"+y.toFixed(2)+",2)，线性拟合 y≈α+βt：α="+alpha.toFixed(5)+
        "，β="+beta.toFixed(5)+"，最小残差平方和="+sq.toFixed(6)+
        "。该对称 t=0,1,2 案例中，仅改变中间点并不会改变斜率。";
    } else if(kind==="normal"){
      const p=Number(value),eps=10**(-p),det=6*eps*eps,trace=6+6*eps+5*eps*eps;
      const large=(trace+Math.sqrt(trace*trace-4*det))/2,small=det/large,cond=Math.sqrt(large/small);
      output.textContent="ε=10⁻"+p+"，A=[1,1;1,1+ε;1,1+2ε]：κ₂(A)≈"+cond.toExponential(4)+
        "；κ₂(AᵀA)≈"+(cond*cond).toExponential(4)+
        "。小特征值通过 det(AᵀA)=6ε² 计算以减少演示自身的相消误差。";
    } else if(kind==="qr"){
      const theta=Number(value)*Math.PI/180,c=Math.cos(theta),kappa=Math.sqrt((1+c)/(1-c));
      output.textContent="两个等长单位列向量夹角 "+value+"°；κ₂(A)=√[(1+cosθ)/(1−cosθ)]≈"+
        kappa.toFixed(5)+"；用 QR 重写列空间后 QᵀQ=I，但 R 仍反映原始问题的条件。";
    } else if(kind==="svd"){
      const sigma=Number(value);
      output.textContent="教学对角模型 Σ=diag(1,"+sigma.toFixed(2)+")："+
        (sigma===0?"第二个方向完全不可辨识；伪逆把该方向的参数设为 0。":"第二方向伪逆系数为 1/σ≈"+(1/sigma).toFixed(2)+"，该方向观测误差也会相应放大。");
    } else if(kind==="perturb"){
      const p=Number(value),eps=10**(-p),delta=1e-3;
      const dx2=-.1*delta/eps,dx1=.4*delta+.1*delta/eps;
      output.textContent="ε=10⁻"+p+"，δb=(0,10⁻³,0,0)：近共线两列使参数改变量 ||δx||₂≈"+
        Math.hypot(dx1,dx2).toExponential(5)+"，但数据扰动范数始终为 0.001。";
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