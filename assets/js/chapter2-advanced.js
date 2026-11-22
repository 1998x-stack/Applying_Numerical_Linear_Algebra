/* Deterministic, educational model explorations. No external dependencies. */
(() => {
  "use strict";
  const short = x => Number.isFinite(x) ? (Math.abs(x) >= 10000 || (Math.abs(x) < 1e-3 && x !== 0) ? x.toExponential(2) : Number(x.toPrecision(4)).toString()) : "—";
  function model(kind,v){
    const row = (label,value,scaled,color="") => ({label,value:short(value),fraction:Math.max(0,Math.min(1,scaled)),color});
    switch(kind){
      case "refinement": {
        const ys=Array.from({length:5},(_,i)=>0.08*Math.pow(v,i));
        const peak=Math.max(...ys,0.08);
        return {description:`示意误差传播：θ=${short(v)}，e₀=0.08，e₄=${short(ys[4])}；${v<1?"θ<1：模型收缩":"θ≥1：无法从该模型保证收敛"}。未计残差舍入下限。`,
          rows:ys.map((y,i)=>row(`迭代 ${i}`,y,y/peak,i===4?"warm":""))};
      }
      case "equilibration": {
        const k=Math.pow(10,v);
        return {description:`仅对角例子：κ₂(diag(10^${v},1))=${short(k)}；列缩放 C=diag(10^(-${v}),1) 后 κ₂(I)=1。解必须用 x=Cy 还原。`,
          rows:[row("原矩阵 κ₂",k,1,"warm"),row("缩放后 κ₂",1,1/k,"")]};
      }
      case "blas": {
        const axpy=1/12, gemv=2*v*v/(8*v*v+16*v),gemm=v/16;
        return {description:`n=${v}：流式模型 AXPY I≈1/12；GEMV ≈${short(gemv)}；GEMM 理想最低流量取 32n² 字节，I≈n/16=${short(gemm)} FLOP/byte。`,
          rows:[row("AXPY L1",axpy,axpy/gemm,"warm"),row("GEMV L2",gemv,gemv/gemm,"blue"),row("GEMM L3",gemm,1)]};
      }
      case "gemm": {
        const n=8, flops=2*n*n*n, tiles=Math.ceil(n/v)**2;
        return {description:`8×8 矩阵：b=${v}，输出块数 ${tiles}；标准乘法主导 FLOPs≈${flops}，不会因块大小改变。尾块长度需截断。`,
          rows:[row("输出块数量",tiles,tiles/64,"blue"),row("块边长度",v,v/8),row("FLOPs",flops,1,"warm")]};
      }
      case "blockedlu": {
        const n=8,tail=n-v,flops=2*tail*tail*v;
        return {description:`8×8 单步分块示意：panel宽 b=${v}，尾随块 ${tail}×${tail}，尾随 GEMM 更新约 2(8-b)²b=${flops} FLOPs。`,
          rows:[row("panel 元素",8*v,v/8,"warm"),row("尾块元素",tail*tail,tail*tail/64,"blue"),row("更新 FLOPs",flops,flops/256)]};
      }
      case "roofline": {
        const memory=50*v,compute=200,ceiling=Math.min(compute,memory);
        return {description:`纯示意硬件：峰值 200 GFLOP/s，带宽 50 GB/s。I=${short(v)} 时 P≤min(200,50×I)=${short(ceiling)} GFLOP/s，${v<4?"访存屋顶":"计算屋顶"}限制。`,
          rows:[row("带宽屋顶",memory,memory/500,"blue"),row("计算屋顶",compute,compute/500,"warm"),row("可达上界",ceiling,ceiling/500)]};
      }
      case "cholesky": {
        const l11=Math.sqrt(v),l21=1/l11,l22=Math.sqrt(2-1/v);
        return {description:`A=[[a,1],[1,2]]，a=${short(v)}：L₁₁=${short(l11)}，L₂₁=${short(l21)}，L₂₂=${short(l22)}；Schur 补 2−1/a=${short(2-1/v)}>0。`,
          rows:[row("L₁₁",l11,l11/3),row("L₂₁",l21,l21/3,"blue"),row("L₂₂",l22,l22/3,"warm")]};
      }
      case "indefinite": {
        const disc=Math.sqrt(v*v+4),hi=(v+disc)/2,lo=(v-disc)/2;
        return {description:`t=${short(v)}；λ₊=${short(hi)}>0，λ₋=${short(lo)}<0，det A=−1，A 始终可逆而非 SPD。`,
          rows:[row("正特征值 λ₊",hi,hi/4.0),row("负特征值 |λ₋|",Math.abs(lo),Math.abs(lo)/4.0,"warm")]};
      }
      default: return {description:"未知教学模型",rows:[]};
    }
  }
  function draw(root){
    const slider=root.querySelector("[data-lab-slider]");
    const output=root.querySelector("[data-lab-output]");
    const bars=root.querySelector("[data-lab-bars]");
    if (!slider || !output || !bars) return;
    const v=Number(slider.value), {description,rows}=model(root.dataset.advancedLab,v);
    output.textContent=description;
    bars.replaceChildren();
    for (const item of rows){
      const line=document.createElement("div");line.className="model-row";
      const label=document.createElement("span");label.className="model-label";label.textContent=item.label;
      const track=document.createElement("span");track.className="model-track";
      const fill=document.createElement("span");fill.className="model-fill"+(item.color?" "+item.color:"");
      fill.style.display="block";fill.style.width=(100*item.fraction).toFixed(2)+"%";
      track.append(fill);
      const value=document.createElement("span");value.className="model-value";value.textContent=item.value;
      line.append(label,track,value);bars.append(line);
    }
    bars.setAttribute("aria-label",description);
  }
  document.addEventListener("DOMContentLoaded",()=>{
    document.querySelectorAll("[data-advanced-lab]").forEach(root=>{
      const slider=root.querySelector("[data-lab-slider]");
      if(!slider)return;
      slider.addEventListener("input",()=>draw(root));
      slider.addEventListener("change",()=>draw(root));
      draw(root);
    });
  });
})();
