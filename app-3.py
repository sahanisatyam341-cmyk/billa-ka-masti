import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Billa ka Masti",
    page_icon="👹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Poori screen pe game dikhane ke liye Streamlit ka header/padding hata deta hai
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {position: fixed; inset: 0; width: 100vw; height: 100dvh; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

GAME_HTML = r'''<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no, viewport-fit=cover">
<title>Billa ka Masti 👹😁</title>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
:root{--gold:#ffd23f;--red:#e63946;color-scheme:dark;box-sizing:border-box}
*{box-sizing:border-box;user-select:none;-webkit-user-select:none;touch-action:none;font-family:'Baloo 2',system-ui,sans-serif}
html,body{margin:0;height:100%;overflow:hidden;overscroll-behavior:none;background:#070a12;color:#fff}
#cv{position:absolute;inset:0}
.g{background:rgba(15,23,42,.85);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:2px solid rgba(255,210,63,.3);box-shadow:0 8px 24px rgba(0,0,0,.6);border-radius:18px}
#hud{position:absolute;top:0;left:0;right:0;padding:calc(env(safe-area-inset-top,0px) + 10px) 12px 0;display:flex;justify-content:space-between;align-items:flex-start;pointer-events:none;z-index:5}
#hud .g{padding:6px 12px;font-weight:800;color:#fcd34d}
#score{font-size:24px}.sm{font-size:11px;color:#cbd5e1;text-transform:uppercase}
.row{display:flex;gap:8px;align-items:center}
#fps{font-size:13px;color:#2dd4bf}#coins{font-size:22px}
#mag{display:none;color:#fb7185;font-size:14px;animation:p 1s infinite}
@keyframes p{50%{opacity:.5}}
#pad{position:absolute;left:0;right:0;bottom:calc(env(safe-area-inset-bottom,0px) + 14px);padding:0 18px;display:flex;justify-content:space-between;max-width:520px;margin:0 auto;z-index:5}
#pad div{display:flex;gap:10px}
#pad button{width:64px;height:64px;font-size:26px;color:#fff;cursor:pointer}
#pad button:active{transform:scale(.92);filter:brightness(1.4)}
.scr{position:absolute;inset:0;z-index:10;display:flex;align-items:center;justify-content:center;padding:16px;background:rgba(2,6,23,.88)}
.hide{display:none!important}
.box{max-width:420px;width:100%;padding:22px;text-align:center}
h1{margin:0 0 4px;font-size:38px;font-weight:800;color:#fbbf24;text-shadow:0 0 12px rgba(255,210,63,.6),0 3px 0 var(--red)}
h2{margin:0 0 4px;font-size:36px;color:#ef4444}
p{margin:0 0 14px;color:#cbd5e1;font-size:14px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:16px}
.c{padding:10px 4px;border-radius:16px;border:1px solid #334155;background:rgba(15,23,42,.6);cursor:pointer;transition:.25s}
.c.on{border-color:var(--gold);background:rgba(255,210,63,.15);box-shadow:0 0 18px rgba(255,210,63,.4)}
.c b{display:block;font-size:12px;color:#fcd34d}.c i{font-style:normal;font-size:30px;display:block}.c small{font-size:10px;color:#94a3b8}
.how{background:rgba(15,23,42,.8);border:1px solid #1e293b;border-radius:16px;padding:10px 12px;font-size:12px;text-align:left;color:#cbd5e1;margin-bottom:16px}
.how div{display:flex;justify-content:space-between;gap:8px}.how b{color:#fbbf24}
.go{width:100%;padding:12px;border:0;border-radius:16px;font-size:24px;font-weight:800;color:#0f172a;cursor:pointer;background:linear-gradient(90deg,#fbbf24,#f97316,#ef4444)}
.go.alt{background:linear-gradient(90deg,#34d399,#14b8a6)}
.go:active{transform:scale(.96)}
.st{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:16px}
.st div{background:rgba(15,23,42,.8);border:1px solid #1e293b;border-radius:16px;padding:8px}
.st em{font-style:normal;display:block;font-size:11px;color:#94a3b8;text-transform:uppercase}.st b{font-size:30px;color:#fbbf24}
</style>
</head>
<body>
<div id="cv"></div>

<div id="hud">
  <div class="g"><div id="score">0</div><div class="sm">Best: <b id="best" style="color:#fff">0</b></div></div>
  <div class="row">
    <div class="g" id="mag">🧲 <span id="mt">7s</span></div>
    <div class="g"><span id="fps">-- FPS</span></div>
    <div class="g">🪙 <span id="coins">0</span></div>
  </div>
</div>

<div id="pad">
  <div><button class="g" data-a="l">◀</button><button class="g" data-a="r">▶</button></div>
  <div><button class="g" data-a="s">▼</button><button class="g" data-a="j">▲</button></div>
</div>

<div id="start" class="scr">
  <div class="g box">
    <h1>Billa ka Masti 👹😁</h1>
    <p>Hero chuno aur raat ke shehar me bhaago!</p>
    <div class="cards">
      <div class="c on" data-c="billa"><i>👹</i><b>Billa Ravan</b><small>Classic Runner</small></div>
      <div class="c" data-c="cyber"><i>⚡</i><b>Cyber Bot</b><small>Lamba Magnet</small></div>
      <div class="c" data-c="gold"><i>👑</i><b>Gold King</b><small>Double Coins</small></div>
    </div>
    <div class="how">
      <div><span>Lane badlo:</span><b>Swipe ←/→ ya A / D</b></div>
      <div><span>Kudo:</span><b>Swipe ↑ ya W / Space</b></div>
      <div><span>Neeche sarko:</span><b>Swipe ↓ ya S</b></div>
    </div>
    <button id="play" class="go">BHAAGO! 🔥</button>
  </div>
</div>

<div id="over" class="scr hide">
  <div class="g box">
    <div style="font-size:56px">🔥</div>
    <h2>Billa Jal Gaya!</h2>
    <p>Track pe accident ho gaya!</p>
    <div class="st"><div><em>Score</em><b id="fs">0</b></div><div><em>Coins</em><b id="fc">0</b></div></div>
    <button id="again" class="go alt">PHIR SE BHAAGO! 😁</button>
  </div>
</div>

<script>
const $=id=>document.getElementById(id), LW=3.6;
let scene,camera,renderer,hero,body,head,legL,legR,armL,armR,ch='billa';
let obs=[],coinL=[],magL=[],deco=[],parts=[],sleepers=[];
let run=false,score=0,coins=0,dist=0,speed=26,lane=0,px=0,py=0,vy=0,jump=false,slide=0,gt=0,magOn=false,magT=0;
let best=0;try{best=parseInt(localStorage.getItem('bkm_best'))||0}catch(e){}
$('best').textContent=best;

// Sound (tiny WebAudio beeps)
let AC;function beep(f,d,t,v){try{AC=AC||new(window.AudioContext||window.webkitAudioContext)();const o=AC.createOscillator(),g=AC.createGain();o.type=t||'square';o.frequency.value=f;g.gain.value=v||.04;g.gain.exponentialRampToValueAtTime(.001,AC.currentTime+d);o.connect(g);g.connect(AC.destination);o.start();o.stop(AC.currentTime+d)}catch(e){}}

const mat=(c,e=0,m=.2,r=.5)=>new THREE.MeshStandardMaterial({color:c,emissive:e,metalness:m,roughness:r});
const part=(p,g,m,x=0,y=0,z=0)=>{const s=new THREE.Mesh(g,m);s.position.set(x,y,z);s.castShadow=true;p.add(s);return s};
const G={hurdle:new THREE.BoxGeometry(2.6,.9,.5),barrier:new THREE.BoxGeometry(2.8,.9,.5),train:new THREE.BoxGeometry(2.8,3.4,11),
 coin:new THREE.CylinderGeometry(.38,.38,.1,14).rotateX(Math.PI/2),magnet:new THREE.TorusGeometry(.35,.12,10,16),
 spark:new THREE.SphereGeometry(.12,6,6),pole:new THREE.BoxGeometry(.3,3.4,.3),bulb:new THREE.SphereGeometry(.5,8,8),lamp:new THREE.SphereGeometry(.2,8,8)};
const M={hurdle:mat(0xef4444,0x450a0a,.3,.4),barrier:mat(0xf97316,0x431407,.3,.4),train:mat(0x0284c7,0x075985,.6,.3),
 coin:mat(0xffd23f,0xb45309,.8,.2),magnet:mat(0xf43f5e,0x881337,.6,.2),pole:mat(0x1e293b),
 bulb:new THREE.MeshBasicMaterial({color:0xffb347}),lamp:new THREE.MeshBasicMaterial({color:0xfef08a})};
const PM=[0xff4d00,0xffb347,0xffd23f].map(c=>new THREE.MeshBasicMaterial({color:c}));

function init(){
  scene=new THREE.Scene();scene.background=new THREE.Color(0x070a12);scene.fog=new THREE.FogExp2(0x070a12,.008);
  camera=new THREE.PerspectiveCamera(60,innerWidth/innerHeight,.1,400);camera.position.set(0,5.5,9.5);
  renderer=new THREE.WebGLRenderer({antialias:false,powerPreference:'high-performance'});
  renderer.setSize(innerWidth,innerHeight);renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));
  renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFShadowMap;
  $('cv').appendChild(renderer.domElement);
  scene.add(new THREE.AmbientLight(0xffe8d6,.7));
  const d=new THREE.DirectionalLight(0xffffff,.9);d.position.set(10,25,12);d.castShadow=true;
  d.shadow.mapSize.set(512,512);const sc=d.shadow.camera;sc.left=-9;sc.right=9;sc.top=9;sc.bottom=-9;sc.near=1;sc.far=60;
  scene.add(d);
  // skyline
  const sun=new THREE.Mesh(new THREE.CircleGeometry(42,40),new THREE.MeshBasicMaterial({color:0xff5500,fog:false}));sun.position.set(0,25,-350);scene.add(sun);
  const sp=[];for(let i=0;i<200;i++)sp.push((Math.random()-.5)*500,30+Math.random()*140,-340);
  const sg=new THREE.BufferGeometry();sg.setAttribute('position',new THREE.Float32BufferAttribute(sp,3));
  scene.add(new THREE.Points(sg,new THREE.PointsMaterial({color:0xffffff,size:1.5,fog:false})));
  const bm=new THREE.MeshBasicMaterial({color:0x090d16});
  for(let i=-10;i<=10;i++){if(Math.abs(i)<2)continue;const h=40+Math.random()*60,w=15+Math.random()*15;
    const b=new THREE.Mesh(new THREE.BoxGeometry(w,h,20),bm);b.position.set(i*18,h/2-10,-280);scene.add(b)}
  // ground, rails, sleepers
  const gr=new THREE.Mesh(new THREE.BoxGeometry(16,.2,400),mat(0x0f172a,0x020617,.1,.9));gr.position.set(0,-.1,-180);gr.receiveShadow=true;scene.add(gr);
  const rg=new THREE.BoxGeometry(.12,.09,400),rm=mat(0x94a3b8,0x1e293b,.8,.2);
  for(let l=-1;l<=1;l++)[-.55,.55].forEach(o=>{const r=new THREE.Mesh(rg,rm);r.position.set(l*LW+o,.04,-180);scene.add(r)});
  const sg2=new THREE.BoxGeometry(11,.08,.55),sm=mat(0x334155,0x0f172a,.1,.8);
  for(let i=0;i<40;i++){const s=new THREE.Mesh(sg2,sm);s.position.set(0,.02,10-i*4);scene.add(s);sleepers.push(s)}
  buildHero();addEventListener('resize',()=>{camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight)});
}

function buildHero(){
  if(hero)scene.remove(hero);
  hero=new THREE.Group();body=new THREE.Group();hero.add(body);hero.scale.setScalar(.72);
  let P,A,S;
  if(ch==='cyber'){P=mat(0x06b6d4,0x0891b2,.6,.2);A=mat(0x38bdf8,0x0284c7,.7,.2);S=mat(0x0284c7,0x0369a1,.5,.3)}
  else if(ch==='gold'){P=mat(0xeab308,0xca8a04,.9,.1);A=mat(0xfde047,0xa16207,.9,.1);S=mat(0xfef08a,0xca8a04,.8,.2)}
  else{P=mat(0xef4444,0x991b1b,.2,.5);A=mat(0xeab308,0xa16207,.6,.3);S=mat(0xfca5a5,0x7f1d1d,.1,.6)}
  const K=mat(0x0f172a,0x020617),W=mat(0xffffff);
  const leg=x=>{const g=new THREE.Group();g.position.set(x,1.3,0);part(g,new THREE.BoxGeometry(.42,1.1,.42),P,0,-.55,0);part(g,new THREE.BoxGeometry(.52,.25,.75),K,0,-1.17,.12);body.add(g);return g};
  legL=leg(-.3);legR=leg(.3);
  part(body,new THREE.CylinderGeometry(.6,.9,.95,14),P,0,1.55,0);
  part(body,new THREE.CylinderGeometry(.92,.95,.22,14),A,0,1.15,0);
  part(body,new THREE.CylinderGeometry(.78,.66,1.5,14),P,0,2.75,0);
  const arm=s=>{const g=new THREE.Group();g.position.set(s*.95,3.35,0);part(g,new THREE.CylinderGeometry(.3,.27,.55,10),P,0,-.2,0);part(g,new THREE.CylinderGeometry(.2,.18,1,10),S,0,-.9,0);part(g,new THREE.SphereGeometry(.22,8,8),K,0,-1.45,0);body.add(g);return g};
  armL=arm(-1);armR=arm(1);
  head=new THREE.Group();head.position.set(0,4.15,0);body.add(head);
  part(head,new THREE.SphereGeometry(.55,18,14),S).scale.set(.9,1.12,.95);
  [-1,1].forEach(s=>{
    part(head,new THREE.SphereGeometry(.1,8,8),W,s*.2,.12,.46).scale.z=.5;
    part(head,new THREE.SphereGeometry(.05,8,8),K,s*.2,.12,.52);
    part(head,new THREE.CylinderGeometry(.2,.2,.05,12),S,s*.6,.05,0).rotation.x=Math.PI/2;
    part(head,new THREE.TorusGeometry(.17,.035,6,16),A,s*.62,-.3,0);
  });
  part(head,new THREE.CylinderGeometry(.5,.56,.22,12),A,0,.52,0);
  for(let i=0;i<8;i++){const a=i*Math.PI/4;part(head,new THREE.ConeGeometry(.09,.4,5),A,Math.cos(a)*.5,.78,Math.sin(a)*.5)}
  part(head,new THREE.ConeGeometry(.13,.55,6),A,0,.9,0);
  scene.add(hero);
}

function spawnRow(z){
  const empty=(Math.random()*3|0)-1;
  for(let l=-1;l<=1;l++){
    const x=l*LW;
    if(l===empty){
      for(let i=0;i<4;i++){const c=new THREE.Mesh(G.coin,M.coin);c.position.set(x,1.1,z-i*2.4);scene.add(c);coinL.push(c)}
      if(Math.random()<.15&&!magL.length){const m=new THREE.Mesh(G.magnet,M.magnet);m.position.set(x,1.2,z-12);scene.add(m);magL.push(m)}
      continue;
    }
    if(Math.random()<.65){
      const r=Math.random();let o;
      if(r<.35){o=new THREE.Mesh(G.hurdle,M.hurdle);o.position.set(x,.45,z);o.userData={t:'h',d:.25}}
      else if(r<.68){o=new THREE.Mesh(G.barrier,M.barrier);o.position.set(x,2.3,z);o.userData={t:'b',d:.25}}
      else{o=new THREE.Mesh(G.train,M.train);o.position.set(x,1.7,z);o.userData={t:'t',d:5.2};
        [-.8,.8].forEach(hx=>{const L=new THREE.Mesh(G.lamp,M.lamp);L.position.set(hx,0,5.5);o.add(L)})}
      scene.add(o);obs.push(o);
    }
  }
  [-1,1].forEach(s=>{
    const g=new THREE.Group();g.position.set(s*8.6,1.7,z);
    g.add(new THREE.Mesh(G.pole,M.pole));const b=new THREE.Mesh(G.bulb,M.bulb);b.position.y=1.9;g.add(b);
    scene.add(g);deco.push(g);
  });
}

function burst(n,ci=0){
  for(let i=0;i<n;i++){
    const p=new THREE.Mesh(G.spark,PM[ci%3]);p.position.set(px,py+1.8,0);
    p.userData={vx:(Math.random()-.5)*12,vy:Math.random()*10+2,vz:(Math.random()-.5)*12,life:.6};
    scene.add(p);parts.push(p);
  }
}

function reset(){
  [...obs,...coinL,...magL,...deco,...parts].forEach(o=>scene.remove(o));
  obs=[];coinL=[];magL=[];deco=[];parts=[];
  score=0;coins=0;dist=0;speed=26;lane=0;px=0;py=0;vy=0;jump=false;slide=0;magOn=false;magT=0;
  $('mag').style.display='none';hero.visible=true;body.scale.y=1;hero.position.set(0,0,0);
  for(let z=-56;z>-160;z-=28)spawnRow(z);
  $('score').textContent=0;$('coins').textContent=0;
}

function act(a){
  if(!run)return;
  if(a==='l'&&lane>-1){lane--;beep(330,.06)}
  else if(a==='r'&&lane<1){lane++;beep(330,.06)}
  else if(a==='j'&&!jump){jump=true;vy=16.5;slide=0;beep(520,.12,'sine')}
  else if(a==='s'){slide=.55;if(jump)vy=-22;beep(200,.08,'sine')}
}

function crash(){
  run=false;hero.visible=false;burst(70);beep(110,.5,'sawtooth',.08);
  if(score>best){best=score;try{localStorage.setItem('bkm_best',best)}catch(e){}}
  $('best').textContent=best;$('fs').textContent=score;$('fc').textContent=coins;
  setTimeout(()=>$('over').classList.remove('hide'),700);
}

function step(dt){
  speed=Math.min(58,speed+dt*.75);const mz=speed*dt;dist+=mz;
  if(dist>=28){dist-=28;spawnRow(-150+dist)}
  px+=(lane*LW-px)*Math.min(1,dt*17);
  if(jump){py+=vy*dt;vy-=46*dt;if(py<=0){py=0;vy=0;jump=false}}
  if(slide>0)slide=Math.max(0,slide-dt);
  body.scale.y+=((slide>0?.45:1)-body.scale.y)*Math.min(1,dt*30);
  const a=gt*14;
  if(jump){legL.rotation.x=-.65;legR.rotation.x=.45;armL.rotation.set(0,0,-1.4);armR.rotation.set(0,0,1.4);hero.position.y=py}
  else{legL.rotation.x=Math.sin(a)*.85;legR.rotation.x=-Math.sin(a)*.85;armL.rotation.set(-Math.sin(a)*.9,0,0);armR.rotation.set(Math.sin(a)*.9,0,0);hero.position.y=Math.abs(Math.sin(a))*.12}
  hero.position.x=px;
  sleepers.forEach(s=>{s.position.z+=mz;if(s.position.z>8)s.position.z-=160});
  [obs,coinL,magL,deco].forEach(arr=>{for(let i=arr.length-1;i>=0;i--){const o=arr[i];o.position.z+=mz;if(o.position.z>22){scene.remove(o);arr.splice(i,1)}}});
  if(magOn){magT-=dt;$('mt').textContent=Math.ceil(magT)+'s';if(magT<=0){magOn=false;$('mag').style.display='none'}}
  for(let i=magL.length-1;i>=0;i--){const m=magL[i];m.rotation.y+=dt*4;
    if(Math.abs(m.position.x-px)<1.2&&Math.abs(m.position.z)<1.2){scene.remove(m);magL.splice(i,1);magOn=true;magT=ch==='cyber'?11:7;$('mag').style.display='flex';burst(15,1);beep(700,.2,'triangle')}}
  for(let i=coinL.length-1;i>=0;i--){const c=coinL[i];c.rotation.y+=dt*6;
    if(magOn&&c.position.z>-25&&c.position.z<10){c.position.x+=(px-c.position.x)*Math.min(1,dt*10);c.position.y+=(py+1.2-c.position.y)*Math.min(1,dt*10)}
    if(Math.abs(c.position.x-px)<1.1&&Math.abs(c.position.z)<1.2&&py<2.5){scene.remove(c);coinL.splice(i,1);coins+=ch==='gold'?2:1;burst(4,2);beep(880,.08,'triangle');$('coins').textContent=coins}}
  for(const o of obs){
    if(Math.abs(o.position.z)<o.userData.d&&Math.abs(o.position.x-px)<1.55){
      const t=o.userData.t;
      if(t==='t'||(t==='h'&&py<.85)||(t==='b'&&(slide<=0||py>.35))){crash();break}
    }
  }
  score=Math.floor(dist*2)+coins*15;$('score').textContent=score;
  camera.position.x+=(px*.35-camera.position.x)*Math.min(1,dt*6);camera.lookAt(px*.25,2.2,-12);
}

let last=performance.now(),fc=0,ft=last;
function frame(now){
  requestAnimationFrame(frame);
  const dt=Math.min((now-last)/1000,.05);last=now;
  fc++;if(now-ft>500){$('fps').textContent=Math.round(fc*1000/(now-ft))+' FPS';fc=0;ft=now}
  gt+=dt;head.rotation.y=Math.sin(gt*2.5)*.25; // face camera ki taraf
  if(run)step(dt);
  for(let i=parts.length-1;i>=0;i--){const p=parts[i],u=p.userData;
    p.position.x+=u.vx*dt;p.position.y+=u.vy*dt;p.position.z+=u.vz*dt;u.vy-=25*dt;u.life-=dt;
    if(u.life<=0){scene.remove(p);parts.splice(i,1)}}
  renderer.render(scene,camera);
}

function start(){$('start').classList.add('hide');$('over').classList.add('hide');buildHero();reset();run=true;beep(600,.15,'triangle')}
$('play').onclick=start;$('again').onclick=start;
document.querySelectorAll('.c').forEach(c=>c.onclick=()=>{
  document.querySelectorAll('.c').forEach(x=>x.classList.remove('on'));c.classList.add('on');ch=c.dataset.c;buildHero()});
addEventListener('keydown',e=>{const k=e.key.toLowerCase();
  if(k==='arrowleft'||k==='a')act('l');if(k==='arrowright'||k==='d')act('r');
  if(k==='arrowup'||k==='w'||k===' ')act('j');if(k==='arrowdown'||k==='s')act('s')});
document.querySelectorAll('#pad button').forEach(b=>b.addEventListener('pointerdown',e=>{e.preventDefault();act(b.dataset.a)}));
let tx=0,ty=0,tOk=false;
addEventListener('touchstart',e=>{tOk=!e.target.closest('#pad,.scr');tx=e.touches[0].clientX;ty=e.touches[0].clientY},{passive:true});
addEventListener('touchend',e=>{if(!tOk)return;const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;
  if(Math.abs(dx)>Math.abs(dy)){if(Math.abs(dx)>30)act(dx>0?'r':'l')}else if(Math.abs(dy)>30)act(dy>0?'s':'j')},{passive:true});
window.onload=()=>{init();requestAnimationFrame(frame)};
</script>
</body>
</html>
'''

components.html(GAME_HTML, height=800, scrolling=False)
