import re,json,urllib.request,base64,sys
sys.stdout.reconfigure(encoding="utf-8")
k=re.search(r'ELEVENLABS_API_KEY=(\S+)',open('.env',encoding='utf8').read()).group(1)
md=open('LOI-DOC-ANNA-THU.md',encoding='utf8').read()
segs=re.findall(r'### (vo-[\w-]+)\.mp3\n```\n(.*?)\n```',md,re.S)
model=sys.argv[1]; out="videos/thaifex-2026/assets/voice-huyentrang"
import os; os.makedirs(out,exist_ok=True); meta={}
for name,t in segs:
  body=json.dumps({"text":t,"model_id":model}).encode()
  r=json.load(urllib.request.urlopen(urllib.request.Request("https://api.elevenlabs.io/v1/text-to-speech/BlZK9tHPU6XXjwOSIiYA/with-timestamps?output_format=mp3_44100_128",data=body,headers={"xi-api-key":k,"Content-Type":"application/json"})))
  open(f"{out}/{name}.mp3","wb").write(base64.b64decode(r["audio_base64"]))
  a=r["alignment"]; meta[name]={"text":t,"chars":a["characters"],"start":a["character_start_times_seconds"],"end":a["character_end_times_seconds"]}
  print(name, round(a["character_end_times_seconds"][-1],2))
json.dump(meta,open(f"{out}/alignment.json","w",encoding="utf8"),ensure_ascii=False)
