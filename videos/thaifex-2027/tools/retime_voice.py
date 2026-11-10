"""Swap voice files and retime index.html + frame timelines with a piecewise-linear old->new time map.
usage: python retime_voice.py <new_voice_dir>   (run once from the committed Edge-TTS state)"""
import re,sys,json
from mutagen.mp3 import MP3
VD=sys.argv[1]; PAD=0.25
s=open('index.html',encoding='utf8').read()
tags=list(re.finditer(r'<(audio|div)\b[^>]*?>',s,re.S))
def attr(t,a):
    m=re.search(a+r'="([^"]+)"',t); return m.group(1) if m else None
voices=[]
for m in tags:
    src=attr(m.group(0),'src')
    if src and '/voice/vo-' in src:
        name=src.split('/')[-1]; voices.append((float(attr(m.group(0),'data-start')),float(attr(m.group(0),'data-duration')),name,MP3(f'{VD}/{name}').info.length))
voices.sort()
K=[(0.0,0.0)]
for S,D,name,L in voices:
    lo,ln=K[-1]; Sn=ln+(S-lo); K+= [(S,Sn),(S+D,Sn+L+PAD)]
def f(t):
    for (a,b),(c,d) in zip(K,K[1:]):
        if t<=c: return b+(t-a)*(d-b)/(c-a) if c>a else d
    return K[-1][1]+t-K[-1][0]
out=[];last=0;scenes={}
for m in tags:
    t=m.group(0); st=attr(t,'data-start')
    if st is None: continue
    st=float(st); d=attr(t,'data-duration'); d=float(d) if d else None; src=attr(t,'src') or ''; comp=attr(t,'data-composition-src')
    nt=t.replace(f'data-start="{attr(t,"data-start")}"',f'data-start="{round(f(st),3)}"')
    if '/voice/vo-' in src:
        name=src.split('/')[-1]; nt=nt.replace(src,f'{VD}/{name}')
        nd=MP3(f'{VD}/{name}').info.length
    elif comp or 'music' in src or st==0 and d and d>100:
        nd=f(st+d)-f(st)
        if comp: scenes[comp]=(st,d)
    else: nd=d
    if d is not None: nt=nt.replace(f'data-duration="{attr(t,"data-duration")}"',f'data-duration="{round(nd,3)}"',1)
    out.append(s[last:m.start()]); out.append(nt); last=m.end()
out.append(s[last:]); open('index.html','w',encoding='utf8').write(''.join(out))
for comp,(Sc,dur) in scenes.items():
    loc=[(0.0,0.0)]+[(a-Sc,f(a)-f(Sc)) for a,_ in K if Sc<a<Sc+dur]+[(dur,f(Sc+dur)-f(Sc))]
    loc=[(round(a,3),round(b,3)) for a,b in loc]
    p=comp; h=open(p,encoding='utf8').read()
    m=re.search(r'window\.__timelines\["([^"]+)"\] = tl;',h); cid=m.group(1)
    code=(f'const __K={json.dumps(loc)}; const __o=gsap.timeline({{paused:true}});\n'
          f'      for(let i=0;i<__K.length-1;i++) __o.fromTo(tl,{{time:__K[i][0]}},{{time:__K[i+1][0],duration:__K[i+1][1]-__K[i][1],ease:"none",immediateRender:false}},__K[i][1]);\n'
          f'      window.__timelines["{cid}"] = __o;')
    open(p,'w',encoding='utf8').write(h.replace(m.group(0),code))
    print(cid, round(dur,2),'->',loc[-1][1])
print('total', round(f(167.516),2))
