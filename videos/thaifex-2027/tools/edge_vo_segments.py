"""Edge TTS (test voice) cho từng đoạn trong docs/LOI-DOC-ANNA-THU.md -> assets/voice-edge/
usage: python tools/edge_vo_segments.py [vo-04 vo-04b ...]   (không ghi tên = tạo tất cả)"""
import asyncio,re,sys,os,json
import edge_tts
from mutagen.mp3 import MP3
sys.stdout.reconfigure(encoding="utf-8")
PROJ=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOICE="vi-VN-HoaiMyNeural"; out=os.path.join(PROJ,"assets","voice-edge"); os.makedirs(out,exist_ok=True)
md=open(os.path.join(PROJ,"docs","LOI-DOC-ANNA-THU.md"),encoding="utf8").read()
segs=re.findall(r'### (vo-[\w-]+)\.mp3\n```\n(.*?)\n```',md,re.S)
only=set(sys.argv[1:]); segs=[x for x in segs if not only or x[0] in only]
async def one(name,t):
    for i in range(20):
        try:
            sent=[]
            with open(f"{out}/{name}.mp3","wb") as fh:
                async for c in edge_tts.Communicate(t,VOICE,boundary="SentenceBoundary").stream():
                    if c["type"]=="audio": fh.write(c["data"])
                    elif c["type"].endswith("Boundary"): sent.append({"text":c["text"],"start":round(c["offset"]/1e7,3),"end":round((c["offset"]+c["duration"])/1e7,3)})
            bp=f"{out}/sentences.json"; allb=json.load(open(bp,encoding="utf8")) if os.path.exists(bp) else {}
            allb[name]=sent; json.dump(allb,open(bp,"w",encoding="utf8"),ensure_ascii=False,indent=1); break
        except edge_tts.exceptions.NoAudioReceived: await asyncio.sleep(3)
    print(name, round(MP3(f"{out}/{name}.mp3").info.length,2))
async def main():
    for n,t in segs: await one(n,t)
asyncio.run(main())
