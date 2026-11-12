"""3. adım: build/ses.wav + build/zamanlar.json -> çizgi film sanal sunucu videosu (1080x1920, 30 fps).

Karakter tamamen kodla çizilir (Pillow); dudak hareketi sesin enerjisinden ve tonundan,
göz kırpma ve baş hareketi kurallardan gelir. Çıktı: build/video.mp4

Kullanım:  python video.py [--altyazisiz] [--sure SN] [--kare N  (tek kare PNG)]
"""
import argparse
import json
import math
import random
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS, SR = 1080, 1920, 30, 48000
SS = 2                                   # karakter katmanı için süper örnekleme
INK = (36, 23, 38)                       # mor-siyah çizgi rengi
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BUILD = Path("build")

# ---------------------------------------------------------------- ses analizi

def ses_oku() -> np.ndarray:
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(BUILD / "ses.wav"), "-ac", "1", "-ar", str(SR),
                          "-f", "f32le", "-"], check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def agiz_egrileri(x: np.ndarray, n: int):
    """Her kare için (açıklık 0-1, genişlik 0-1: 0=yuvarlak 'o/u', 1=yayvan 'e/i')."""
    hop = SR // FPS
    win = np.hanning(2048).astype(np.float32)
    freqs = np.fft.rfftfreq(2048, 1 / SR)
    lo, hi = (freqs > 150) & (freqs < 900), (freqs > 1500) & (freqs < 4000)
    rms, ton = np.zeros(n), np.zeros(n)
    for i in range(n):
        c = i * hop + hop // 2
        seg = x[max(0, c - 1024): c + 1024]
        if len(seg) < 2048:
            seg = np.pad(seg, (0, 2048 - len(seg)))
        rms[i] = np.sqrt(np.mean(seg ** 2))
        sp = np.abs(np.fft.rfft(seg * win))
        ton[i] = sp[hi].sum() / (sp[lo].sum() + sp[hi].sum() + 1e-9)
    ref = np.percentile(rms[rms > 1e-4], 95) if np.any(rms > 1e-4) else 1.0
    hedef = np.clip((rms / ref - 0.10) / 0.9, 0, 1) ** 0.8
    acik = np.zeros(n)
    for i in range(1, n):                                 # hızlı açıl, biraz yavaş kapan
        k = 0.65 if hedef[i] > acik[i - 1] else 0.45
        acik[i] = acik[i - 1] + k * (hedef[i] - acik[i - 1])
    ton = np.clip((ton - np.percentile(ton, 20)) / (np.ptp(ton) * 0.6 + 1e-9), 0, 1)
    ton = np.convolve(ton, np.ones(3) / 3, mode="same")
    return acik, ton


# ---------------------------------------------------------------- arka plan

def arka_plan(baslik: str) -> Image.Image:
    img = Image.new("RGB", (W, H))
    y = np.linspace(0, 1, H)[:, None]
    ust, alt = np.array([43, 39, 92]), np.array([120, 62, 98])
    grad = (ust * (1 - y) + alt * y)[:, None, :].repeat(W, 1)
    img = Image.fromarray(grad.reshape(H, W, 3).astype(np.uint8))
    d = ImageDraw.Draw(img, "RGBA")
    rnd = random.Random(7)
    bokeh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bokeh)
    for _ in range(26):                                   # sıcak bulanık ışıklar
        r = rnd.randint(25, 70); cx = rnd.randint(0, W); cy = rnd.randint(200, 1100)
        col = rnd.choice([(255, 196, 120), (255, 140, 170), (140, 200, 255)])
        bd.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col + (rnd.randint(35, 80),))
    img.paste(bokeh.filter(ImageFilter.GaussianBlur(14)), (0, 0), bokeh.filter(ImageFilter.GaussianBlur(14)))
    # raf + bitkiler + akustik panel
    for px in (70, 860):
        for k in range(3):
            y0 = 330 + k * 150
            d.rounded_rectangle((px, y0, px + 150, y0 + 120), 14, fill=(70, 58, 120), outline=INK, width=5)
            bx = px + 14
            for _ in range(rnd.randint(3, 5)):            # raftaki kitaplar
                bw, bh = rnd.randint(16, 26), rnd.randint(60, 95)
                if bx + bw > px + 136:
                    break
                d.rectangle((bx, y0 + 112 - bh, bx + bw, y0 + 112), outline=INK, width=4,
                            fill=rnd.choice([(232, 120, 96), (96, 170, 200), (240, 200, 90), (150, 110, 190)]))
                bx += bw + 4
    d.rectangle((0, 1000, W, 1022), fill=(88, 56, 64), outline=INK, width=5)
    for bx, h in ((150, 120), (930, 150)):
        d.polygon([(bx - 45, 1000), (bx + 45, 1000), (bx + 32, 915), (bx - 32, 915)], fill=(214, 120, 84),
                  outline=INK, width=5)
        for a in (-60, -25, 10, 45, 80):
            t = math.radians(a - 90)
            ex, ey = bx + math.cos(t) * h * 0.8, 915 + math.sin(t) * h
            d.line([(bx, 915), (ex, ey)], fill=(70, 150, 90), width=22)
            d.ellipse((ex - 22, ey - 22, ex + 22, ey + 22), fill=(86, 172, 104), outline=INK, width=4)
    # neon program adı
    neon = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    nd = ImageDraw.Draw(neon)
    f = ImageFont.truetype(FONT_B, 74)
    yazi = "TUHAF AMA GERÇEK"
    tw = nd.textlength(yazi, font=f)
    nd.text(((W - tw) / 2, 175), yazi, font=f, fill=(255, 120, 180, 255))
    glow = neon.filter(ImageFilter.GaussianBlur(16))
    img.paste(glow, (0, 0), glow); img.paste(glow, (0, 0), glow)
    d = ImageDraw.Draw(img, "RGBA")
    d.text(((W - tw) / 2, 175), yazi, font=f, fill=(255, 225, 240))
    # masa
    d.rounded_rectangle((-20, 1480, W + 20, H + 40), 30, fill=(150, 92, 70), outline=INK, width=7)
    d.rectangle((0, 1500, W, 1525), fill=(176, 112, 86))
    # kupa + buhar
    d.rounded_rectangle((150, 1520, 260, 1650), 18, fill=(250, 240, 226), outline=INK, width=6)
    d.arc((235, 1550, 295, 1615), 270, 90, fill=INK, width=12)
    d.rectangle((150, 1560, 260, 1580), fill=(84, 196, 200))
    for k in range(2):
        d.arc((175 + k * 35, 1440, 215 + k * 35, 1510), 100, 260, fill=(255, 255, 255, 110), width=6)
    # bölüm başlığı kartı
    fb = ImageFont.truetype(FONT_B, 40)
    bw = d.textlength(baslik, font=fb)
    d.rounded_rectangle(((W - bw) / 2 - 34, 285, (W + bw) / 2 + 34, 355), 35, fill=(255, 236, 200, 235),
                        outline=INK, width=4)
    d.text(((W - bw) / 2, 297), baslik, font=fb, fill=INK)
    return img


# ---------------------------------------------------------------- karakter (Defne)

def karakter(acik: float, ton: float, goz: float, kas: float, dx: float, dy: float) -> Image.Image:
    """Karakter katmanı (RGBA, W x 1500 bölgesi). goz: 1 açık, 0 kapalı. kas: kaş kaldırma 0-1."""
    s = SS
    L = Image.new("RGBA", (W * s, 1500 * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(L)
    lw = 7 * s

    def P(*pts):  # tasarım koordinatı -> süper örnekli
        return [v * s for v in pts]

    cx, cy = 540 + dx, 760 + dy                # baş merkezi
    # gövde (kazak) + boyun
    d.rounded_rectangle(P(215, 1110 + dy * 0.3, 865, 1700), 150 * s, fill=(236, 178, 64), outline=INK, width=lw)
    d.polygon(P(445, 1112 + dy * .3, 635, 1112 + dy * .3, 540, 1230 + dy * .3), fill=(250, 245, 232), outline=INK)
    d.line(P(445, 1112 + dy * .3, 540, 1230 + dy * .3, 635, 1112 + dy * .3), fill=INK, width=lw)
    d.rounded_rectangle(P(490 + dx * .5, 960 + dy, 590 + dx * .5, 1130 + dy * .4), 40 * s, fill=(232, 176, 140),
                        outline=INK, width=lw)
    # arka saç
    d.ellipse(P(cx - 235, cy - 245, cx + 235, cy + 215), fill=(78, 44, 40), outline=INK, width=lw)
    d.rounded_rectangle(P(cx - 235, cy - 40, cx + 235, cy + 250), 60 * s, fill=(78, 44, 40), outline=INK, width=lw)
    # yüz (fasulye biçimi: üstte geniş, çenede dar)
    yuz = []
    for k in range(64):
        t = 2 * math.pi * k / 64
        rx = 190 * (1 - 0.10 * max(0, math.sin(t)))       # alt yarı biraz daralır
        yuz.append((cx + rx * math.cos(t), cy + 10 + 205 * math.sin(t)))
    d.polygon([(x * s, y * s) for x, y in yuz], fill=(244, 196, 160))
    d.line([(x * s, y * s) for x, y in yuz + yuz[:1]], fill=INK, width=lw, joint="curve")
    # kulaklık bandı + kulaklıklar
    d.arc(P(cx - 225, cy - 270, cx + 225, cy + 180), 190, 350, fill=INK, width=30 * s)
    d.arc(P(cx - 225, cy - 270, cx + 225, cy + 180), 192, 348, fill=(84, 196, 200), width=18 * s)
    for sx in (-1, 1):
        d.rounded_rectangle(P(cx + sx * 215 - 38, cy - 40, cx + sx * 215 + 38, cy + 90), 30 * s,
                            fill=(84, 196, 200), outline=INK, width=lw)
    # kâkül
    kakul = [(cx - 195, cy - 40), (cx - 185, cy - 150), (cx - 110, cy - 215), (cx, cy - 232), (cx + 110, cy - 215),
             (cx + 185, cy - 150), (cx + 195, cy - 40), (cx + 120, cy - 105), (cx + 40, cy - 85), (cx - 30, cy - 120),
             (cx - 110, cy - 95)]
    d.polygon([(x * s, y * s) for x, y in kakul], fill=(92, 52, 46))
    d.line([(x * s, y * s) for x, y in kakul + kakul[:1]], fill=INK, width=lw, joint="curve")
    # kaşlar
    ky = cy - 62 - 16 * kas
    for sx in (-1, 1):
        d.arc(P(cx + sx * 80 - 38, ky - 6 - 4 * kas, cx + sx * 80 + 38, ky + 26), 200, 340, fill=INK, width=9 * s)
    # gözler
    for sx in (-1, 1):
        ex, ey = cx + sx * 80, cy - 5
        if goz > 0.25:
            h = 34 * goz
            d.ellipse(P(ex - 26, ey - h, ex + 26, ey + h), fill=INK)
        else:
            d.arc(P(ex - 28, ey - 14, ex + 28, ey + 14), 20, 160, fill=INK, width=8 * s)
    # burun
    d.arc(P(cx - 14, cy + 30, cx + 14, cy + 62), 300, 120, fill=INK, width=6 * s)
    # ağız
    my = cy + 112
    gen = 34 + 34 * ton * (0.5 + acik) + 10 * (1 - acik)
    yuk = 4 + 58 * acik * (1.05 - 0.35 * ton)
    if acik < 0.06:
        d.arc(P(cx - 40, my - 22, cx + 40, my + 10), 25, 155, fill=INK, width=8 * s)   # gülümseme
    else:
        d.ellipse(P(cx - gen, my - yuk * .45, cx + gen, my + yuk), fill=(110, 30, 52), outline=INK, width=lw)
        if yuk > 22:
            d.ellipse(P(cx - gen * .55, my + yuk * .35, cx + gen * .55, my + yuk * .95), fill=(226, 104, 112))
        if yuk > 14:
            d.chord(P(cx - gen * .8, my - yuk * .45, cx + gen * .8, my + yuk * .25), 180, 360, fill=(255, 252, 245))
    # mikrofon kolu (sağdan gelir, ağzın altında durur)
    d.line(P(1080, 820, 900, 1040, 740, 1030), fill=INK, width=22 * s, joint="curve")
    d.line(P(1080, 820, 900, 1040, 740, 1030), fill=(60, 60, 72), width=12 * s, joint="curve")
    d.rounded_rectangle(P(650, 980, 770, 1100), 50 * s, fill=(70, 70, 84), outline=INK, width=lw)
    for k in range(4):
        d.line(P(665, 1000 + k * 24, 755, 1000 + k * 24), fill=(120, 120, 140), width=4 * s)
    return L.resize((W, 1500), Image.LANCZOS)


# ---------------------------------------------------------------- altyazı + etiket

def parcalar(zamanlar):
    """Cümleleri 2-4 kelimelik altyazı parçalarına böl, süreyi harf sayısına göre paylaştır."""
    out = []
    for c in zamanlar["cumleler"]:
        kel = c["metin"].split()
        grup, gruplar = [], []
        for k in kel:
            grup.append(k)
            if len(grup) >= 3 or k[-1] in ",.?!":
                gruplar.append(" ".join(grup)); grup = []
        if grup:
            gruplar.append(" ".join(grup))
        top = sum(len(g) for g in gruplar)
        t = c["bas"]
        for g in gruplar:
            dt = (c["son"] - c["bas"]) * len(g) / top
            out.append((t, t + dt, g)); t += dt
    return out


def yazi_ciz(img, metin, y, boyut, dolgu=(255, 255, 255)):
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT_B, boyut)
    tw = d.textlength(metin, font=f)
    d.text(((W - tw) / 2, y), metin, font=f, fill=dolgu, stroke_width=8, stroke_fill=INK)


def ai_etiketi(img):
    d = ImageDraw.Draw(img, "RGBA")
    f = ImageFont.truetype(FONT_R, 30)
    t = "Yapay zekâ ile üretilmiştir"
    tw = d.textlength(t, font=f)
    d.rounded_rectangle((36, 52, 36 + tw + 40, 104), 26, fill=(0, 0, 0, 120))
    d.text((56, 59), t, font=f, fill=(255, 255, 255))


# ---------------------------------------------------------------- ana döngü

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--altyazisiz", action="store_true")
    ap.add_argument("--sure", type=float)
    ap.add_argument("--kare", type=int, help="yalnızca bu kareyi PNG olarak kaydet")
    ap.add_argument("--bolum", default="bolum.json")
    a = ap.parse_args()

    bolum = json.loads(Path(a.bolum).read_text("utf-8"))
    zam = json.loads((BUILD / "zamanlar.json").read_text("utf-8"))
    x = ses_oku()
    sure = min(a.sure or 1e9, len(x) / SR)
    n = int(sure * FPS)
    acik, ton = agiz_egrileri(x, n)
    alt = parcalar(zam)
    soru = [(c["bas"], c["son"]) for c in zam["cumleler"] if c["metin"].strip().endswith("?")]

    rnd = random.Random(3)
    kirp, t = set(), 0.8
    while t < sure:                                        # 0.5-2.3 sn arası kırpma, 4 kare
        f0 = int(t * FPS); kirp.update({f0: 0.5, f0 + 1: 0.0, f0 + 2: 0.0, f0 + 3: 0.5}.items())
        t += rnd.uniform(1.2, 3.6)
    kirp = dict(kirp)

    bg = arka_plan(bolum["baslik"])
    ai_etiketi(bg)

    def kare(i):
        tt = i / FPS
        enerji = float(np.mean(acik[max(0, i - 8): i + 1]))
        dx = 9 * math.sin(tt * 0.9) + 5 * math.sin(tt * 2.3)
        dy = 6 * math.sin(tt * 1.4) - 10 * enerji
        kas = max([1.0 for b, s in soru if b - 0.2 <= tt <= s + 0.3] + [0.15 * enerji])
        img = bg.copy()
        k = karakter(float(acik[i]), float(ton[i]), kirp.get(i, 1.0), kas, dx, dy)
        img.paste(k, (0, 0), k)
        if not a.altyazisiz:
            for b, s, g in alt:
                if b <= tt < s:
                    yazi_ciz(img, g, 1640, 74, (255, 236, 120)); break
        return img

    if a.kare is not None:
        kare(a.kare).save(BUILD / f"kare_{a.kare:05d}.png"); print("kare kaydedildi"); return

    sessiz = BUILD / "video_sessiz.mp4"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                          "-pix_fmt", "yuv420p", str(sessiz)], stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(kare(i).tobytes())
        if i % 150 == 0:
            print(f"  kare {i}/{n}", flush=True)
    p.stdin.close(); p.wait()
    # ses: -16 LUFS (Apple podcast hedefi), true peak -1.5 dBTP
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(sessiz), "-i", str(BUILD / "ses.wav"),
                    "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=7",
                    "-ar", "48000", "-c:a", "aac", "-b:a", "192k", "-t", f"{sure:.3f}", str(BUILD / "video.mp4")],
                   check=True)
    print("build/video.mp4 yazıldı")


if __name__ == "__main__":
    main()
