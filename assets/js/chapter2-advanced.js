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

  function renderDynamicDiagram(kind,v) {
    const rect=(x,y,w,h,c)=>'<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+c+'" stroke="#fff" stroke-width="1.5"/>';
    const text=(x,y,label,size=16)=>'<text x="'+x+'" y="'+y+'" text-anchor="middle" font-size="'+size+'" fill="#284a51" font-family="sans-serif">'+label+'</text>';
    let s='';
    if (kind==='gemm' || kind==='blockedlu') {
      const b=Math.round(v), n=8, startX=120,startY=28,cell=28;
      for(let i=0;i<n;i++)for(let k=0;k<n;k++){
        const color=kind==='gemm'
          ? ((i<b&&k<b)?'#439d91':(Math.floor(i/b)+Math.floor(k/b))%2?'#e8f1ef':'#cfe6e2')
          : (i<b&&k<b?'#d9a169':i<b?'#a9cde1':k<b?'#9dcbbd':'#dbe9f1');
        s+=rect(startX+k*cell,startY+i*cell,cell-1,cell-1,color);
      }
      for(let k=0;k<=n;k+=b){
        s+='<path d="M'+(startX+k*cell)+' '+startY+'V'+(startY+n*cell)+' M'+startX+' '+(startY+k*cell)+'H'+(startX+n*cell)+'" stroke="#486d70" stroke-width="2" fill="none"/>';
      }
      s+=text(478,72,'b = '+b,24)+text(478,106,kind==='gemm'?'输出矩阵 C':'黄色：面板 A₁₁',17);
      s+=text(478,145,kind==='gemm'?'绿色：当前输出块':'蓝色：上方面板',15);
      s+=text(478,185,kind==='gemm'?'交替色：其余分块':'灰蓝：尾随 A₂₂',15);
    } else if (kind==='roofline') {
      const X=x=>70+x/10*500,Y=y=>230-y/225*185,cur=Math.min(200,50*v);
      s+='<path d="M70 25V230H585" stroke="#526f73" stroke-width="3" fill="none"/>';
      s+='<path d="M'+X(0)+' '+Y(0)+'L'+X(4)+' '+Y(200)+'H'+X(10)+'" fill="none" stroke="#318c85" stroke-width="4"/>';
      s+='<circle cx="'+X(v)+'" cy="'+Y(cur)+'" r="9" fill="#c57955"/>';
      s+='<path d="M'+X(v)+' '+Y(cur)+'V230" stroke="#c57955" stroke-dasharray="5 4"/>';
      s+=text(332,20,'P ≤ min(200, 50I)',19)+text(395,261,'I='+v+'，屋顶='+cur+' GFLOP/s',14);
    } else if (kind==='indefinite') {
      const d=Math.sqrt(v*v+4),plus=(v+d)/2,minus=(v-d)/2,X=x=>322+x/4*250;
      s+='<path d="M65 137H580" stroke="#526f73" stroke-width="3"/><path d="M322 55V215" stroke="#b2c2c4" stroke-dasharray="7 5" stroke-width="2"/>';
      s+='<circle cx="'+X(plus)+'" cy="137" r="11" fill="#348f83"/><circle cx="'+X(minus)+'" cy="137" r="11" fill="#c47955"/>';
      s+=text(X(plus),114,'λ+ '+plus.toFixed(2),15)+text(X(minus),178,'λ− '+minus.toFixed(2),15);
      s+=text(322,245,'det A = −1：特征值永在零的两侧',18);
    }
    if(!s) return '';
    return '<svg viewBox="0 0 640 282" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="随当前参数重绘的数学示意图"><rect x="0" y="0" width="640" height="282" rx="14" fill="#fbfdfc"/>'+s+'</svg>';
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
    const drawing=renderDynamicDiagram(root.dataset.advancedLab,v);
    if(drawing){
      let holder=root.querySelector("[data-dynamic-svg]");
      if(!holder){
        holder=document.createElement("div");
        holder.className="model-detail";
        holder.setAttribute("data-dynamic-svg","");
        bars.after(holder);
      }
      holder.innerHTML=drawing;
      holder.dataset.modelFingerprint=root.dataset.advancedLab+":"+slider.value;
    }

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
