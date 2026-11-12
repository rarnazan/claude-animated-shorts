# Sanal sunucu prototipi: "Tuhaf Ama Gerçek" (Defne)

Kodla çizilmiş, kurgusal bir yapay zekâ kadın podcast sunucusu. Senaryodan sese ve dikey videoya kadar her şey kodla üretiliyor.
GPU ve ücretli avatar servisi gerekmiyor.

```
pip install -r requirements.txt        # ffmpeg de gerekli
python senaryo.py "konu"               # 1) Claude ile bolum.json  (ANTHROPIC_API_KEY gerekir; yoksa hazır bolum.json'u kullanın)
python ses.py                          # 2) Türkçe kadın sesi -> build/ses.wav + build/zamanlar.json
python video.py                        # 3) 1080x1920, 30 fps -> build/video.mp4 (-16 LUFS)
python video.py --kare 40              #    tek kare önizleme (build/kare_00040.png)
python video.py --altyazisiz           #    altyazısız
```

## Nasıl çalışıyor
- **Senaryo** (`senaryo.py`): `claude-opus-5-5` modeli, yapılandırılmış çıktıyla JSON döndürür: başlık, sunucu, cümleler.
  Sunucunun kişiliği ve "yalnızca doğrulanabilir gerçek" kuralı sistem isteminde. Reddetme durumunda `fallbacks="default"` devreye girer.
- **Ses** (`ses.py`): Her cümle ayrı seslendirilir, böylece cümlelerin başlangıç ve bitiş zamanları kesin olarak bilinir.
  - `ELEVENLABS_API_KEY` ve `ELEVENLABS_VOICE_ID` tanımlıysa ElevenLabs kullanılır.
  - Tanımlı değilse **gTTS** kullanılır. gTTS yalnızca deneme içindir; ticari yayında kullanmayın.
- **Video** (`video.py`):
  - Karakter Pillow ile 2 kat çözünürlükte çizilip küçültülür (kenar yumuşatma için).
  - Ağız açıklığı sesin karedeki enerjisinden hesaplanır. Ağzın genişliği (yuvarlak "o/u" ile yayvan "e/i" arası), sesteki yüksek ve alçak frekansların oranından gelir.
  - Göz kırpma 1,2–3,6 saniyede bir, 4 kare sürer.
  - Soru cümlelerinde kaşlar kalkar. Konuşurken baş hafifçe hareket eder.
  - Altyazılar 2–4 kelimelik parçalar hâlinde gösterilir.
  - Videonun köşesinde "Yapay zekâ ile üretilmiştir" etiketi bulunur.

## Sonraki adımlar (rapordaki yol haritası)
- **Daha iyi dudak senkronu:** Azure TTS'in Türkçe viseme (ağız şekli) kimliklerini veya WhisperX kelime zamanlarını kullanmak.
- **Gerçekçi avatar** (YouTube'da "AI" etiketi zorunlu olur): HeyGen API, fal üzerinde Kling Avatar veya InfiniteTalk.
- **Kısa klipler ve yükleme:** Bölümden otomatik kısa klip çıkarmak, YouTube Data API ile yüklemek.
- **Sponsorlu bölümler:** Türkiye'de 1 Ağustos 2026'dan beri "Reklam/Tanıtım" etiketi ve dijital karakter bildirimi zorunlu.
