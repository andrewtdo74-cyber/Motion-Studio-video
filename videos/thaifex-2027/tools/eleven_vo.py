import re,json,urllib.request,base64,sys,os
HERE=os.path.dirname(os.path.abspath(__file__)); PROJ=os.path.dirname(HERE)
sys.stdout.reconfigure(encoding="utf-8")
k=re.search(r'ELEVENLABS_API_KEY=(\S+)',open(os.path.join(PROJ,'..','..','.env'),encoding='utf8').read()).group(1)
md=open(os.path.join(PROJ,'docs','LOI-DOC-ANNA-THU.md'),encoding='utf8').read()
segs=re.findall(r'### (vo-[\w-]+)\.mp3\n```\n(.*?)\n```',md,re.S)
model=sys.argv[1]; out=os.path.join(PROJ,"assets","voice-huyentrang")
only=set(sys.argv[2:])  # optional: only regenerate these names, keep the rest
if only: segs=[x for x in segs if x[0] in only]
os.makedirs(out,exist_ok=True); ap=f"{out}/alignment.json"
meta=json.load(open(ap,encoding="utf8")) if only and os.path.exists(ap) else {}
for name,t in segs:
  body=json.dumps({"text":t,"model_id":model}).encode()
  r=json.load(urllib.request.urlopen(urllib.request.Request("https://api.elevenlabs.io/v1/text-to-speech/BlZK9tHPU6XXjwOSIiYA/with-timestamps?output_format=mp3_44100_128",data=body,headers={"xi-api-key":k,"Content-Type":"application/json"})))
  open(f"{out}/{name}.mp3","wb").write(base64.b64decode(r["audio_base64"]))
  a=r["alignment"]; meta[name]={"text":t,"chars":a["characters"],"start":a["character_start_times_seconds"],"end":a["character_end_times_seconds"]}
  print(name, round(a["character_end_times_seconds"][-1],2))
json.dump(meta,open(f"{out}/alignment.json","w",encoding="utf8"),ensure_ascii=False)
