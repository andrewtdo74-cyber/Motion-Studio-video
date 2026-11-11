"""Đổi bộ giọng đang dùng trong index.html và canh lại thời gian toàn video (cảnh, hiệu ứng, nhạc, timeline từng cảnh).
usage: python tools/swap_voice.py <thu-muc-giong-hien-tai> <thu-muc-giong-moi>
vd:    python tools/swap_voice.py assets/voice-huyentrang assets/voice-edge
Có thể chạy nhiều lần, chạy ngược lại để về giọng cũ (thời gian khớp theo độ dài file)."""
import re,sys,json
sys.stdout.reconfigure(encoding="utf-8")
from mutagen.mp3 import MP3
OLD,NEW=sys.argv[1].rstrip('/'),sys.argv[2].rstrip('/'); PAD=float(sys.argv[3]) if len(sys.argv)>3 else 0.0  # giãn thêm sau mỗi đoạn giọng (giây)
s=open('index.html',encoding='utf8').read()
tags=list(re.finditer(r'<(audio|div)\b[^>]*?>',s,re.S))
def attr(t,a):
    m=re.search(r'\s'+a+r'="([^"]+)"',t); return m.group(1) if m else None
voices=sorted((float(attr(m.group(0),'data-start')),float(attr(m.group(0),'data-duration')),attr(m.group(0),'src').split('/')[-1])
              for m in tags if (attr(m.group(0),'src') or '').startswith(OLD+'/'))
K=[(0.0,0.0)]
for S,D,name in voices:
    L=MP3(f'{NEW}/{name}').info.length; lo,ln=K[-1]; Sn=ln+(S-lo); K+=[(S,Sn),(S+D,Sn+L+PAD)]
def interp(P,t):
    for (a,b),(c,d) in zip(P,P[1:]):
        if t<=c: return b+(t-a)*(d-b)/(c-a) if c>a else d
    return P[-1][1]+t-P[-1][0]
f=lambda t:interp(K,t)
out=[];last=0;scenes={}
for m in tags:
    t=m.group(0); st=attr(t,'data-start')
    if st is None: continue
    st=float(st); d=attr(t,'data-duration'); d=float(d) if d else None; src=attr(t,'src') or ''; comp=attr(t,'data-composition-src')
    nt=t.replace(f'data-start="{attr(t,"data-start")}"',f'data-start="{round(f(st),3)}"',1)
    if src.startswith(OLD+'/'):
        name=src.split('/')[-1]; nt=nt.replace(src,f'{NEW}/{name}'); nd=MP3(f'{NEW}/{name}').info.length
    elif comp or 'music' in src or (st==0 and d and d>100):
        nd=f(st+d)-f(st)
        if comp: scenes[comp]=(st,d)
    else: nd=d
    if d is not None: nt=nt.replace(f'data-duration="{attr(t,"data-duration")}"',f'data-duration="{round(nd,3)}"',1)
    out.append(s[last:m.start()]); out.append(nt); last=m.end()
out.append(s[last:]); s=''.join(out)
# chuyển cảnh (crossfade) trong script "main" phải theo mốc bắt đầu mới của từng cảnh, nếu không cảnh sẽ bị làm mờ mất
sc=sorted((float(attr(m.group(0),'data-start')),attr(m.group(0),'id')) for m in re.finditer(r'<div\b[^>]*?data-composition-src="[^"]+"[^>]*?>',s,re.S))
total=float(re.search(r'id="root"[\s\S]*?data-duration="([^"]+)"',s).group(1))
L=[]
for (a,i),(b,j) in zip(sc,sc[1:]):
    L+=[f'        tl.to("#{i}", {{ opacity: 0, duration: 0.5, ease: "power2.inOut" }}, {b});',
        f'        tl.fromTo("#{j}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.5, ease: "power2.inOut" }}, {b});',
        f'        tl.addLabel("hf:transition:{i[3:]}:{j[3:]}:crossfade", {b});']
L.append(f'        tl.to({{}}, {{ duration: {total} }}, 0.0); // full-span anchor — main.duration() == composition total (Studio master duration)')
s=re.sub(r'(\(function \(\) \{ var tl = window\.__timelines\["main"\];\n)[\s\S]*?(\n      \}\)\(\);)',lambda m:m.group(1)+'\n'.join(L)+m.group(2),s,count=1)
open('index.html','w',encoding='utf8').write(s)
for comp,(Sc,dur) in scenes.items():
    h=open(comp,encoding='utf8').read()
    m=re.search(r'const __K=(\[.*?\]);',h)
    old=json.loads(m.group(1)) if m else [[0,0],[dur,dur]]
    inv=[(b,a) for a,b in old]          # scene-time -> tl-time
    pts=sorted({b for _,b in old}|{a-Sc for a,_ in K if Sc<a<Sc+dur}|{0.0,dur})
    g=lambda x:f(Sc+x)-f(Sc)
    loc=[[round(interp(inv,x),3),round(g(x),3)] for x in pts]
    if m: h=h.replace(m.group(0),f'const __K={json.dumps(loc)};')
    else: raise SystemExit(f'{comp}: chưa có __K')
    open(comp,'w',encoding='utf8').write(h)
    print(comp.split('/')[-1], round(dur,2),'->',loc[-1][1])
end=[float(attr(m.group(0),'data-start'))+float(attr(m.group(0),'data-duration')) for m in tags if attr(m.group(0),'id')=='root']
print('tổng', round(f(end[0]),2) if end else '?')
