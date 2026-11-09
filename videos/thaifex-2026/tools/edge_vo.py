"""Edge TTS voiceover with word timings -> audio_meta.json (frame-keyed shape used by faceless-explainer).
usage: python edge_vo.py <script-v3.md> <project_dir> <frames e.g. 1,2,3,4,5> [rate]
"""
import asyncio, json, re, subprocess, sys, os
import edge_tts

VOICE = "vi-VN-HoaiMyNeural"
script_path, proj, frames = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(",")]
rate = sys.argv[4] if len(sys.argv) > 4 else "+0%"
FFPROBE = os.environ.get("HYPERFRAMES_FFPROBE_PATH", "ffprobe")

text = open(script_path, encoding="utf-8").read()
sections = {}
for m in re.finditer(r"^## s(\d+)\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M):
    sections[int(m.group(1))] = " ".join(m.group(2).split())

sys.stdout.reconfigure(encoding="utf-8")

async def one(n):
    for attempt in range(20):
        try:
            return await one_try(n)
        except edge_tts.exceptions.NoAudioReceived:
            print(f"frame {n}: no audio, retry {attempt + 1}")
            await asyncio.sleep(3)
    raise SystemExit(f"frame {n}: Edge TTS failed")

async def one_try(n):
    out = os.path.join(proj, "assets", "voice", f"vo-{n:02d}.mp3")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    comm = edge_tts.Communicate(sections[n], VOICE, rate=rate, boundary="WordBoundary")
    words = []
    with open(out, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                s = chunk["offset"] / 1e7
                words.append({"id": f"w{n:02d}_{len(words):03d}", "text": chunk["text"],
                              "start": round(s, 3), "end": round(s + chunk["duration"] / 1e7, 3)})
    dur = float(subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                                "-of", "default=nw=1:nk=1", out], capture_output=True, text=True).stdout.strip())
    return {"frame": n, "path": f"assets/voice/vo-{n:02d}.mp3", "duration_s": round(dur, 3), "words": words}

async def main():
    voices = [await one(n) for n in frames]
    meta_path = os.path.join(proj, "audio_meta.json")
    meta = {"bgm": None, "bgm_pending": False, "voices": voices, "sfx": []}
    if os.path.exists(meta_path):
        old = json.load(open(meta_path, encoding="utf-8"))
        meta["bgm"] = old.get("bgm"); meta["sfx"] = old.get("sfx", [])
    json.dump(meta, open(meta_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    for v in voices:
        print(f"frame {v['frame']}: {v['duration_s']}s, {len(v['words'])} words")
    print("total", round(sum(v["duration_s"] for v in voices), 2), "s")

asyncio.run(main())
