"""2. adım: bolum.json'daki cümleleri Türkçe kadın sesine çevirir.

Çıktı: build/ses.wav (48 kHz mono) + build/zamanlar.json (cümle başı/sonu, saniye).
Sağlayıcılar:
  - ELEVENLABS_API_KEY ve ELEVENLABS_VOICE_ID varsa ElevenLabs (ticari kullanım için önerilir)
  - yoksa gTTS (Google Translate sesi; yalnızca prototip/deneme içindir, ticari yayında kullanmayın)
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np

SR = 48000
ARA = 0.28          # cümleler arası sessizlik (sn)
HIZ = 1.12          # gTTS biraz yavaş konuşur; hafif hızlandır


def tts_gtts(metin: str, mp3: Path) -> None:
    from gtts import gTTS
    gTTS(metin, lang="tr").save(str(mp3))


def tts_elevenlabs(metin: str, mp3: Path) -> None:
    import requests
    voice = os.environ["ELEVENLABS_VOICE_ID"]
    r = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
        headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"]},
        json={"text": metin, "model_id": "eleven_multilingual_v2", "language_code": "tr"},
        timeout=120,
    )
    r.raise_for_status()
    mp3.write_bytes(r.content)


def wav_oku(yol: Path, tempo: float) -> np.ndarray:
    af = f"atempo={tempo}," if tempo != 1.0 else ""
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(yol), "-af", f"{af}silenceremove=start_periods=1:start_threshold=-45dB,"
         "areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse",
         "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
        check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def main() -> None:
    bolum = json.loads(Path(sys.argv[1] if len(sys.argv) > 1 else "bolum.json").read_text("utf-8"))
    out = Path("build"); out.mkdir(exist_ok=True)
    eleven = bool(os.environ.get("ELEVENLABS_API_KEY") and os.environ.get("ELEVENLABS_VOICE_ID"))
    tts, tempo = (tts_elevenlabs, 1.0) if eleven else (tts_gtts, HIZ)
    print("Ses sağlayıcı:", "ElevenLabs" if eleven else "gTTS (prototip)")

    parcalar, zamanlar, t = [np.zeros(int(0.35 * SR), np.float32)], [], 0.35
    for i, cumle in enumerate(bolum["cumleler"]):
        mp3 = out / f"c{i:02d}.mp3"
        if not mp3.exists():
            tts(cumle, mp3)
        x = wav_oku(mp3, tempo)
        zamanlar.append({"metin": cumle, "bas": round(t, 3), "son": round(t + len(x) / SR, 3)})
        parcalar += [x, np.zeros(int(ARA * SR), np.float32)]
        t += len(x) / SR + ARA
        print(f"  {i+1}/{len(bolum['cumleler'])}  {len(x)/SR:4.1f} sn  {cumle[:50]}")
    ses = np.concatenate(parcalar + [np.zeros(int(0.5 * SR), np.float32)])
    ses = ses / (np.abs(ses).max() + 1e-9) * 0.89
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                    str(out / "ses.wav")], input=ses.astype(np.float32).tobytes(), check=True)
    (out / "zamanlar.json").write_text(json.dumps(
        {"sure": round(len(ses) / SR, 3), "cumleler": zamanlar}, ensure_ascii=False, indent=2), "utf-8")
    print(f"build/ses.wav yazıldı ({len(ses)/SR:.1f} sn)")


if __name__ == "__main__":
    main()
