(function(){
  const wave=document.getElementById('wave-path'),dots=document.getElementById('sample-points'),lines=document.getElementById('quant-lines');if(!wave)return;
  const points=16,cx=55,span=620,mid=120,amp=76,period=2*Math.PI;let phase=0,running=true,last=0,raf=0;
  const yAt=x=>mid-amp*Math.sin((x-cx)/span*period+phase);
  wave.setAttribute('d',Array.from({length:150},(_,i)=>{const x=cx+i*span/149;return `${i?'L':'M'}${x.toFixed(1)},${yAt(x).toFixed(1)}`}).join(' '));
  for(let i=0;i<points;i++){const x=cx+i*span/(points-1);const dot=document.createElementNS('http://www.w3.org/2000/svg','circle');dot.setAttribute('r','6');dot.dataset.x=x;dots.append(dot);const line=document.createElementNS('http://www.w3.org/2000/svg','line');line.setAttribute('x1',String(x-10));line.setAttribute('x2',String(x+10));lines.append(line)}
  const speed=document.getElementById('anim-speed'),label=document.getElementById('speed-value'),play=document.getElementById('anim-play');
  function render(t){if(running){phase+=(t-last||0)*.0008*Number(speed.value);last=t;wave.setAttribute('d',Array.from({length:150},(_,i)=>{const x=cx+i*span/149;return `${i?'L':'M'}${x.toFixed(1)},${yAt(x).toFixed(1)}`}).join(' '));dots.querySelectorAll('circle').forEach(d=>{const x=Number(d.dataset.x),y=yAt(x);d.setAttribute('cy',String(y));d.dataset.y=y});lines.querySelectorAll('line').forEach((line,i)=>{const x=cx+i*span/(points-1),y=yAt(x),qy=mid+Math.round((y-mid)/20)*20;line.setAttribute('y1',String(qy));line.setAttribute('y2',String(qy))});last=t}raf=requestAnimationFrame(render)}
  play.addEventListener('click',()=>{running=!running;play.textContent=running?'Pausar animação':'Reproduzir animação';if(running)last=0});document.getElementById('anim-reset').addEventListener('click',()=>{phase=0;last=0;running=true;play.textContent='Pausar animação'});speed.addEventListener('input',()=>label.textContent=`${speed.value}×`);render(0);
})();
