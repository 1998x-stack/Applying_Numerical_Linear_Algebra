/* Standalone deterministic mathematical visualizations; no network dependencies. */
(() => {
  "use strict";
  const fmt = x => Math.abs(x)>=10000 || (Math.abs(x)>0 && Math.abs(x)<.0001) ? x.toExponential(3) : Number(x.toPrecision(5)).toString();
  const grid = (n, f, x0=130, y0=35, cell=34) => {
    let s="";
    for(let i=0;i<n;i++)for(let j=0;j<n;j++){
      const c=f(i,j);
      s+='<rect x="'+(x0+j*cell)+'" y="'+(y0+i*cell)+'" width="'+(cell-2)+'" height="'+(cell-2)+'" rx="3" fill="'+(c?"#378d85":"#edf3f1")+'"/>';
    }
    return s;
  };
  const label=(x,y,t,z=18)=>'<text x="'+x+'" y="'+y+'" font-family="sans-serif" fill="#28515b" text-anchor="middle" font-size="'+z+'">'+t+'</text>';
  function calculate(type,v){
    let fig="",output="";
    if(type==="band"){
      const n=8,k=Math.round(v),nnz=n*(2*k+1)-k*(k+1);
      fig=label(260,22,"8×8 的非零结构：半带宽 k="+k,20)+grid(n,(i,j)=>Math.abs(i-j)<=k)+label(510,156,"结构非零 = "+nnz+" / 64",22);
      output="n=8，k="+k+"：结构非零数 "+nnz+"，紧凑对称带高度 "+(2*k+1)+"；k=1 时为 3n−2=22。";
    }else if(type==="fill"){
      const hubFirst=v<.5, n=6,nnz=hubFirst?21:11;
      // Cholesky of star SPD: hub first -> all lower triangular; hub last -> diagonal + final row.
      const nonzero=(i,j)=>i>=j && (hubFirst || i===j || i===n-1);
      fig=label(260,25,hubFirst?"中心先消去：新增叶—叶填充":"叶子先消去：没有叶—叶填充",19)
          +grid(6,nonzero,185,40,40)+label(515,162,"L 的结构非零数："+nnz,20);
      output="n=6 星形 SPD：中心"+(hubFirst?"先":"最后")+"，Cholesky L 结构非零数="+nnz+"。A 原始有 16 个结构非零，L 中可有不同的填充。";
    }else if(type==="woodbury"){
      const n=12,k=Math.round(v),count=n+2*n*k;
      fig=label(255,24,"A=D+UVᵀ：可稠密的 12×12",19)+grid(12,()=>true,80,34,23)
          +label(515,130,"参数 "+count+" vs 稠密 144",19)+label(518,183,"小系统 K："+k+"×"+k,19);
      output="n=12，k="+k+"：存 D、U、V 的数值参数数="+count+"；完全展开 A 为 144 个元素。两者不等同于内存峰值或时间实测。";
    }else if(type==="projection"){
      const b=[1,2,v],c=(3+v)/3,res=b.map(x=>x-c),rss=res.reduce((a,x)=>a+x*x,0);
      const X=[190,355,520],Y=y=>306-y*31;
      fig='<path d="M80 30V310H645" fill="none" stroke="#748f91" stroke-width="3"/>'
          +'<line x1="91" y1="'+Y(c)+'" x2="600" y2="'+Y(c)+'" stroke="#329a8c" stroke-width="4"/>';
      b.forEach((value,i)=>{
        fig+='<line x1="'+X[i]+'" y1="'+Y(value)+'" x2="'+X[i]+'" y2="'+Y(c)+'" stroke="#c78159" stroke-width="4"/>'
            +'<circle cx="'+X[i]+'" cy="'+Y(value)+'" r="8" fill="#4f82b0"/>'+label(X[i],336,"b"+(i+1)+"="+fmt(value),15);
      });
      output="观测 [1,2,"+fmt(v)+"]；最佳常数 c="+fmt(c)+"；残差平方和="+fmt(rss)+"；Σrᵢ="+fmt(res.reduce((a,x)=>a+x,0))+"。";
      fig+=label(562,23,"绿线=c="+fmt(c),17);
    }else if(type==="normal"){
      const p=Math.round(v),a=Math.pow(10,p),b=Math.pow(10,2*p);
      fig='<path d="M100 310H618" stroke="#82969b" stroke-width="3"/>';
      fig+='<rect x="185" y="'+(310-p*32)+'" width="115" height="'+Math.max(5,p*32)+'" fill="#4d97a4"/>';
      fig+='<rect x="395" y="'+(310-2*p*16)+'" width="115" height="'+Math.max(5,2*p*16)+'" fill="#c98759"/>';
      fig+=label(238,341,"log₁₀κ(A)="+p,17)+label(452,341,"log₁₀κ(AᵀA)="+(2*p),17);
      output="模型 κ₂(A)=10^"+p+" = "+fmt(a)+"；κ₂(AᵀA)=κ₂(A)²=10^"+(2*p)+" = "+fmt(b)+"。不是实测的误差位数。";
    }else if(type==="qr"){
      const x0=132,y0=304,scale=67, bx=x0+3*scale, by=y0-v*scale;
      fig='<path d="M91 304H621 M132 343V27" fill="none" stroke="#748e92" stroke-width="3"/>';
      fig+='<line x1="'+x0+'" y1="'+y0+'" x2="'+bx+'" y2="'+y0+'" stroke="#318f86" stroke-width="5"/>';
      fig+='<line x1="'+bx+'" y1="'+y0+'" x2="'+bx+'" y2="'+by+'" stroke="#c57a58" stroke-width="4"/>';
      fig+='<line x1="'+x0+'" y1="'+y0+'" x2="'+bx+'" y2="'+by+'" stroke="#4f85ad" stroke-width="3"/>';
      fig+=label(bx+25,by,"b",18)+label(bx-28,y0+28,"p=3",17)+label(bx+25,(y0+by)/2,"r",17);
      output="正交分解 b=p+r：p=[3,0]，r=[0,"+fmt(v)+"]，||b||²=9+"+fmt(v*v)+"；Qᵀr=0，不依赖 r 的长度。";
    }else if(type==="svd"){
      const s2=v,ry=205*s2/3;
      fig='<path d="M70 195H633 M350 20V354" fill="none" stroke="#82969b" stroke-width="2"/>';
      fig+='<circle cx="350" cy="195" r="70" fill="none" stroke="#9bb6b9" stroke-width="3"/>';
      fig+='<ellipse cx="350" cy="195" rx="205" ry="'+ry+'" fill="#b8dbd5" fill-opacity=".6" stroke="#358f84" stroke-width="4"/>';
      fig+=label(570,72,"σ₁=3",20)+label(570,102,"σ₂="+fmt(s2),20);
      output="A=diag(3,"+fmt(s2)+")：单位圆映射的椭圆半轴为 (3,"+fmt(s2)+")，κ₂="+fmt(3/s2)+"；小奇异值对应较大的逆方向敏感性。";
    }else if(type==="perturb"){
      const delta=.01, eps=1e-6;
      const actual=(delta*delta+eps*v)/(delta*delta+eps*eps)-1;
      const linear=eps*v/(delta*delta);
      const sx=q=>118+q/2*450,sy=q=>307-q/.020*245;
      const pts=Array.from({length:17},(_,i)=>i/8).map(q=>sx(q)+","+sy((delta*delta+eps*q)/(delta*delta+eps*eps)-1)).join(" ");
      fig='<path d="M103 32V310H612" fill="none" stroke="#80979c" stroke-width="3"/>';
      fig+='<polyline points="'+pts+'" stroke="#378f86" stroke-width="4" fill="none"/>';
      fig+='<circle cx="'+sx(v)+'" cy="'+sy(actual)+'" r="8" fill="#cb8058"/>';
      fig+=label(475,40,"δ=0.01, ε=10⁻⁶",18)+label(451,349,"原始残差分量 b₃",17);
      output="b₃="+fmt(v)+"：精确 Δx₂="+fmt(actual)+"；一阶残差项 εb₃/δ²="+fmt(linear)+"；二阶误差不可忽略时，两者不再完全相同。";
    }
    return {output,svg:'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="当前数值参数驱动的可视化图解" viewBox="0 0 680 370"><rect width="680" height="370" rx="12" fill="#fcfefd"/>'+fig+'</svg>'};
  }
  document.addEventListener("DOMContentLoaded",()=>{
    document.querySelectorAll("[data-next-lab]").forEach(root=>{
      const slider=root.querySelector("[data-next-slider]"),out=root.querySelector("[data-next-output]"),visual=root.querySelector("[data-next-visual]");
      if(!slider||!out||!visual)return;
      const update=()=>{
        const v=Number(slider.value),res=calculate(root.dataset.nextLab,v);
        out.textContent=res.output;
        visual.innerHTML=res.svg;
        visual.setAttribute("data-model-fingerprint",root.dataset.nextLab+":"+slider.value);
      };
      slider.addEventListener("input",update);slider.addEventListener("change",update);update();
    });
  });
})();