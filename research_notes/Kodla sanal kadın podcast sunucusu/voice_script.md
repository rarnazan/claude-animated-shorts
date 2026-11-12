# Voice Synthesis & Script Generation for a Code-Generated Virtual Female Podcast Host (Turkish + English, as of Nov 2026)

Research date: 2026-11-12. Many search results were third-party aggregators; primary vendor pages were fetched where possible and are marked as such. Treat aggregator-only figures as "to verify".

## 1. Commercial TTS for Turkish (and English) female voices: quality, emotion control, pricing, licence, timestamps/visemes

### Takeaway
For Turkish, the strongest commercial options as of late 2026 are ElevenLabs (v3 / v4, Turkish confirmed on v3, Multilingual v2 and Flash v2.5), Google Gemini-TTS (tr-TR is GA, with style prompts and multi-speaker), and Azure (tr-TR-EmelNeural plus the new expressive female HD voice tr-TR-Elif:MAI-Voice-2 with 10 styles). Only Azure gives native viseme IDs for Turkish (no blend shapes; those are en-US/zh-CN only). Any vendor can be lip-synced by running forced alignment afterwards (see section 5).

### Cited Findings

**ElevenLabs**
- Official API pricing page (fetched Nov 2026): TTS per 1K characters: v4 $0.08, v4 Turbo $0.04, v3 $0.08, v3 Conversational $0.04, Multilingual v2 $0.08, Flash/Turbo $0.04. Scribe STT costs $0.20/hour (Scribe v3/v2) and $0.22/hour realtime. The page does not list a separate dialogue price. — [ElevenLabs API pricing](https://elevenlabs.io/pricing/api)
- An October 5, 2026 update reportedly cut v3, v2 Multilingual and Flash/Turbo API rates 20% (from ~$0.10 to $0.08 per 1K characters; Flash $0.04). Earlier (Sept 2026) sources list $0.10/1K. — [usagepricing.com (aggregator)](https://www.usagepricing.com/blueprint/activity/elevenlabs-2026-10-05-v4-launch-tts-price-cut); [Puter pricing breakdown](https://developer.puter.com/tutorials/elevenlabs-api-pricing/)
- On the website/UI, Eleven v3 generation costs 1 credit per character, and API generations are discounted. — [ElevenLabs help center](https://help.elevenlabs.io/hc/en-us/articles/35869113958801-How-much-does-it-cost-to-generate-using-Eleven-v3)
- Turkish (tr) is officially supported on Eleven v3 (70+ languages), Multilingual v2 (29 languages) and Flash v2.5 (32 languages). v4 coverage is on a separate page. — [ElevenLabs: What languages do you support?](https://elevenlabs.io/docs/help-center/other/what-languages-do-you-support)
- Eleven v4 / v4 Turbo were reported at 90+ languages (up from 70 in v3). — [tbreak](https://tbreak.com/elevenlabs-v4-90-languages-expressive-voice-model/)
- The pricing page states "Commercial use licensing on Starter+ plans", but this appears in the Music section. Enterprise has custom terms. — [ElevenLabs API pricing](https://elevenlabs.io/pricing/api)
- Third-party directories list ElevenLabs Turkish voices with an Istanbul accent. — [famulor.io](https://www.famulor.io/voices/elevenlabs/languages/tr/accents/istanbul)
- Professional Voice Cloning (PVC) needs voice verification. The FAQ has entries on PVC verification failures and on "Can I create a Professional Voice Clone of someone else's voice?". I could not fetch the full answers. — [ElevenLabs voice-cloning FAQ index](https://elevenlabs.io/docs/help-center/product/voices/voice-cloning)
- Third-party guides say PVC requires speaking a verification phrase (KYC-style), while the consent for Instant Voice Cloning of others rests on the user. — [innfactory.ai](https://innfactory.ai/en/ai-models/elevenlabs/); [pixelmind review](https://pixelmind-ai-delta.vercel.app/reviews/elevenlabs-review)

**Google Gemini-TTS (Cloud Text-to-Speech / Vertex)**
- Models in Cloud TTS: `gemini-3.1-flash-tts-preview` (Preview), `gemini-2.5-flash-tts`, `gemini-2.5-flash-lite-preview-tts` (Preview, single speaker only) and `gemini-2.5-pro-tts`. Gemini 3.8 Flash TTS and 3.8 Flash-Lite TTS are GA through the Agent Platform API / Agent Studio but not through the Cloud TTS API. — [Google Cloud Gemini-TTS docs](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
- **Turkish (tr-TR) is supported at GA status.** — [Google Cloud Gemini-TTS docs](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
- Multi-speaker works on 3.1 Flash, 2.5 Flash and 2.5 Pro, with speakers set through aliases. The examples use 2 speakers, and the docs give no stated maximum. — [Google Cloud Gemini-TTS docs](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts). Third parties conflict on the limit: invideo (Aug 2026) and EmpirioLabs say a maximum of 2 speakers per request, while Runflow and Developers Digest claim 8–10 on newer models. — [invideo](https://invideo.io/blog/gemini-tts-ai-voice/); [EmpirioLabs](https://empiriolabs.ai/models/gemini-2-5-pro-tts); [Runflow](https://www.runflow.io/models/google/gemini-tts); [Developers Digest](https://www.developersdigest.tech/models/speech/google)
- Emotion and style control comes from natural-language style prompts plus markup tags (Preview): non-speech sounds `[sigh]`, `[laughing]`, `[uhm]`; modifiers `[whispering]`, `[shouting]`, `[sarcasm]`; pacing `[short pause]`, `[medium pause]`, `[long pause]`. Adjective tags like `[scared]` may be spoken aloud, which is undesired. — [Google Cloud Gemini-TTS docs](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
- Output formats: LINEAR16, MP3, OGG_OPUS, PCM and others. The Vertex API returns headerless 16-bit PCM at 24 kHz. The docs do not mention word timestamps. — [Google Cloud Gemini-TTS docs](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
- Pricing is token-based (per invideo, which cites Google): 3.1 Flash TTS $1.00/M input text tokens and $20/M output audio tokens. 2.5 Flash TTS costs $0.50/$10 and 2.5 Pro TTS $1/$20. Batch is half price. — [invideo](https://invideo.io/blog/gemini-tts-ai-voice/) (official pricing page not verified)
- Gemini 2.5 Flash Preview TTS reportedly retires on 2026-11-17. — [Developers Digest](https://www.developersdigest.tech/models/speech/google)

**Microsoft Azure AI Speech**
- tr-TR voices from the official language-support table:
  - `tr-TR-EmelNeural` (female, standard)
  - `tr-TR-AhmetNeural` (male, standard)
  - **`tr-TR-Elif:MAI-Voice-2`** (female, Neural HD) and `tr-TR-Elif:MAI-Voice-2-Flash` (Neural HD Flash)
  - `tr-TR-Aydın:MAI-Voice-2` and `tr-TR-Aydın:MAI-Voice-2-Flash` (male)

  The MAI-Voice-2 voices are public preview and support the styles adventurous, caringempathy, curious, encouraging, excited, friendlycheerful, nostalgic, reflective, saddisappointed and serious. — [Azure Speech language support](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)
- **Visemes:** tr-TR supports **Viseme ID** only. Blend shapes are available for en-US and zh-CN, and SVG is only for en-US. — [Azure language support, Visemes table](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts); [Azure viseme how-to](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-speech-synthesis-viseme)
- Viseme details: 22 viseme IDs (0 = silence … 21 = p/b/m), each with an audio offset in 100-ns ticks. You get them via the Speech SDK `VisemeReceived` event. Blend shapes come as 55 ARKit-style facial values per frame at 60 FPS (where supported). The doc was updated 2026-06. — [Azure viseme how-to](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-speech-synthesis-viseme)
- In 2021, visemes were en-US only and SDK-only. That has since changed and is now outdated. — [Microsoft Tech Community 2021](https://techcommunity.microsoft.com/t5/azure-ai/azure-neural-text-to-speech-extended-to-support-lip-sync-with/ba-p/2356748)
- Word boundary events are available in the Speech SDK. Multilingual "Turbo" voices note full SSML and word boundary support. — [Azure language support footnotes](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)
- The free tier is reported at 500K TTS characters/month (third party). Exact Neural/NeuralHD rates are on the official pricing page and were not retrieved. — [Turbo360 playbook](https://azure-cost-management-playbook.turbo360.com/docs/ai-speech); [Azure Speech pricing (TR)](https://azure.microsoft.com/tr-tr/pricing/details/speech/)

**OpenAI**
- `gpt-4o-mini-tts` (snapshot 2025-12-15 exists) takes an `instructions` parameter for delivery style. It is priced at about $0.60/M text input tokens and $12/M audio output tokens, roughly $0.015/minute. — [OpenAI community forum](https://community.openai.com/t/new-tts-api-pricing-and-gotchas/1150616); [PromptLayer](https://blog.promptlayer.com/gpt-4o-mini-tts-steerable-low-cost-speech-via-simple-apis/); [Maxim calculator](https://www.getmaxim.ai/bifrost/llm-cost-calculator/provider/openai/model/gpt-4o-mini-tts-2025-12-15)
- Voice count is 13 (adds Ballad, Verse, Marin, Cedar) per one source; other sources say 6 (conflicting). Turkish is not explicitly confirmed in the sources found. — [Developers Digest](https://www.developersdigest.tech/models/speech/openai); [Eden AI](https://www.edenai.co/expert-models/openai-gpt-4o-mini-tts)

**Cartesia**
- Cartesia has a Turkish TTS landing page. Turkish was added with Sonic Multilingual's "next 8 languages" (to 15 total), and later Sonic versions list 42 languages. — [Cartesia Turkish](https://cartesia.ai/languages/turkish); [Cartesia blog](https://www.cartesia.ai/blog/sonic-multilingual-next-8-languages); [Cartesia models docs](https://docs.cartesia.ai/getting-started/available-models)
- The API offers word-level and phoneme-level timestamp flags (per AWS Marketplace listing text). — [AWS Marketplace listing](https://aws.amazon.com/marketplace/pp/prodview-h5rfrnvkbnlki)

**Amazon Polly**
- Polly has a Turkish (tr-TR) phoneme table, so SSML phoneme control and Polly speech marks (viseme/word) exist for Turkish. — [AWS Polly Turkish phoneme table](https://docs.aws.amazon.com/en_en/polly/latest/dg/ph-table-turkish.html)

### Inferences
- **Best Turkish female voice + lip sync in one API:** use Azure `tr-TR-Elif:MAI-Voice-2` (expressive, styles) or `EmelNeural` (stable, GA). Viseme IDs drive a 2D mouth-shape rig directly; for a 3D blend-shape rig, map the 22 IDs to visemes yourself, since Turkish lacks blend-shape output.
- **Best naturalness / emotion:** ElevenLabs v3/v4 (audio tags, Turkish confirmed) or Gemini-TTS (style prompts, GA Turkish, native 2-speaker). Neither documents per-word timestamps in what I fetched (ElevenLabs does offer `with-timestamps` endpoints per my prior knowledge; unverified here), so plan on WhisperX or forced alignment for lip sync.
- Approximate cost per 10-minute episode (~9,000 characters): ElevenLabs about $0.72 (v3/v4) or $0.36 (Flash/v3 Conversational). OpenAI mini-tts is about $0.15. Gemini Flash TTS is likely sub-$1. Arithmetic based on the cited rates.
- Use Voice Design / stock synthetic voices (ElevenLabs Voice Library, Azure prebuilt, Gemini prebuilt) for an original host persona. This avoids cloning consent issues entirely.

### Gaps
- Official Azure per-character price for Neural vs NeuralHD (MAI-Voice-2) voices was not retrieved.
- Official Gemini-TTS pricing page and speaker cap were not verified. The 3.8 TTS model details come only from aggregators plus one line in the Google docs.
- Cartesia Sonic TTS pricing and Turkish quality were not found from reliable sources.
- OpenAI TTS Turkish quality and official language list are unconfirmed. OpenAI policy requires disclosing that the voice is AI-generated (prior knowledge, unverified here).
- I found no independent Turkish-specific MOS/blind comparison across commercial vendors. TTS Arena-style leaderboards are English-centric (not fetched).
- I could not read the full ElevenLabs PVC consent rules. ElevenLabs "no-go voices" (political figures) safeguards are from prior knowledge and unverified.
- Polly Turkish voice names (e.g. Filiz) and whether a neural/generative Turkish voice exists were not verified.

## 2. Open-source TTS with Turkish: quality, licence, GPU

### Takeaway
The only well-maintained, commercially licensed, out-of-the-box Turkish open model is **Chatterbox Multilingual V3 (MIT, 500M, includes Turkish, Perth watermark)**, though Resemble declared the repo "retired research" in Aug 2026. Other options are community Turkish fine-tunes of F5-TTS and Orpheus (licences vary from MIT/Apache to CC-BY-NC) and Piper (MIT, lightweight but robotic). XTTS-v2 is non-commercial.

### Cited Findings
- **Chatterbox (Resemble AI):**
  - The Multilingual model supports 23 languages including Turkish (tr). The repo is MIT-licensed. Variants are Multilingual V3 (500M, recommended), Turbo (350M, English), Nano (110M, English, CPU 3x realtime on 8 cores) and the Original (500M, English).
  - Emotion control: `exaggeration` (default 0.5; set ≥0.7 for drama) with `cfg_weight` (around 0.3 to slow the pace). Turbo/Nano accept tags like `[laugh]` and `[chuckle]`.
  - Every output carries an imperceptible Perth neural watermark.
  - The README states the project is "retired research and is no longer maintained" as of August 2026.
  
  — [Chatterbox README](https://cdn.jsdelivr.net/gh/resemble-ai/chatterbox@master/README.md)
- Chatterbox Multilingual v3 (June 2026) was described as having 25 languages with embedded watermarking, so sources conflict on 23 vs 25. — [Resemble AI](https://www.resemble.ai/resources/chatterbox-multilingual-v3-tts-with-embedded-watermarking-for-25-languages)
- **XTTS-v2** covers Turkish but uses the Coqui Public Model License (non-commercial). Coqui shut down in early 2024, so the model is community-maintained only. — [findskill.ai](https://findskill.ai/blog/best-open-source-tts-2026/); [localaimaster](https://localaimaster.com/blog/kokoro-vs-xtts-vs-chatterbox)
- **F5-TTS:** the code is MIT, but the base weights are reported as CC-BY-NC. — [datarootlabs](https://datarootlabs.com/blog/text-to-speech-models)
- **Open-source Turkish TTS survey (2026), cataloguing 21 models.** Licences in the table conflict in places; the survey says to check each card.
  - Orkhon-TTS F5-TTS (Apache 2.0, alpha, 3.4 GB)
  - Karayakar/F5-Turkish (MIT, 4.1 GB)
  - marduk-ra/F5-Turkish (CC-BY-NC)
  - Karayakar/Orpheus-PT-5000 (Orpheus 3B, MIT, 13.2 GB, the most popular; partial non-verbal tags such as laugh and sigh)
  - Karayakar/Orpheus-GGUF Q5 (2.4 GB)
  - Cosmobillian/turkish_orpheus (Apache 2.0)
  - facebook/mms-tts-tur (VITS 36M, CC-BY-NC, most downloaded)
  - Kani-TTS-400m Turkish (Apache 2.0 but listed as academic use)
  - Piper tr_TR-dfki (MIT, 63 MB)
  - SalihHub/karagoz-hacivat (XTTS-v2, CC-BY-NC-SA)

  — [Turkish TTS survey](https://danielquillanroxas.github.io/turkish-tts-survey)
- Quality findings from the survey:
  - No community Turkish model reports formal MOS.
  - The highest reported open MOS is 4.49 (Oyucu), but its artifacts are incomplete.
  - Turkcell's proprietary system scores MOS 4.39 (63 h of a professional actress; not released).
  - No Turkish emotion-labelled speech dataset exists.

  — [Turkish TTS survey](https://danielquillanroxas.github.io/turkish-tts-survey)

### Inferences
- GPU: Chatterbox 500M and F5 (~0.3B) run comfortably on a single consumer GPU (8–12 GB). Orpheus 3B fp16 (13 GB checkpoint) wants about 16 GB+ VRAM, or use the 2.4 GB GGUF quant. Piper runs on CPU. These figures are inferred from model sizes in the cited sources and should be benchmarked.
- For a commercial channel, use Chatterbox Multilingual (MIT) or MIT/Apache community fine-tunes. Avoid XTTS-v2, mms-tts-tur and CC-BY-NC F5 checkpoints.
- Open-source Turkish quality still trails ElevenLabs, Gemini and Azure HD in expressiveness. A hybrid approach is a reasonable choice: open-source for drafts, commercial for final renders.
- Chatterbox's watermark is a plus for AI-disclosure and transparency obligations.

### Gaps
- Fish Speech / OpenAudio S1, Kokoro, Dia, Sesame CSM, Orpheus (base), IndexTTS-2, Higgs Audio and VibeVoice: Turkish support and licences not verified this session. Prior knowledge (unverified): Kokoro has no Turkish; Dia and CSM are English-centric; Fish Speech weights have had non-commercial (CC-BY-NC-SA) licences.
- I found no measured GPU/RTF benchmarks for Turkish models.
- No blind Turkish MOS comparison between open and commercial models exists.

## 3. Two-host / multi-speaker podcast generation

### Takeaway
The standard pattern is LLM-generated dialogue script, then per-speaker TTS (or native multi-speaker TTS), then concatenation and mixing. Native two-speaker TTS exists in Gemini-TTS (tr-TR GA) and ElevenLabs v3 (dialogue). Podcastfy is the main Apache-2.0 open pipeline and supports OpenAI, Google, ElevenLabs and Edge TTS, all of which can do Turkish.

### Cited Findings
- Gemini-TTS multi-speaker uses speaker aliases in one request (2-speaker examples), and Turkish is GA. — [Google Cloud Gemini-TTS docs](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
- ElevenLabs v3 supports multi-speaker dialogue per the pricing page, with no separate rate listed. A third-party site lists a "Text to Dialogue V3" product. — [ElevenLabs API pricing](https://elevenlabs.io/pricing/api); [muapi comparison](https://muapi.ai/comparison/elevenlabs-text-to-dialogue-v3)
- **Podcastfy** turns URLs, PDFs, YouTube, images and topics into conversational audio. It writes transcripts with 100+ LLMs (OpenAI, Anthropic, Google, or local HF models). TTS backends are OpenAI, Google, ElevenLabs and Microsoft Edge, with a multi-speaker TTS model from v0.4.0. It offers short (2–5 min) and longform (30+ min) modes, is multilingual (French and pt-BR examples), and is Apache 2.0. — [Podcastfy GitHub](https://github.com/souzatharsis/podcastfy)

### Inferences
- For a single virtual female host, a monologue with an occasional "co-host" or guest voice is simpler and makes lip sync easier (one face).
- For a two-host format, generate each turn separately with its own voice. That gives per-turn audio files and simplifies per-character lip sync and camera cuts, compared with one blended multi-speaker file that would need diarization.
- Podcastfy can be adapted for Turkish by setting the output language in its conversation config and choosing Edge (`tr-TR-EmelNeural`), Google or ElevenLabs voices. This is inferred from backend support and needs a test.

### Gaps
- NotebookLM Audio Overview internals, its current Turkish availability, and ElevenLabs GenFM/Studio Turkish support were not verified this session. Prior knowledge: NotebookLM expanded Audio Overviews to 50+ languages in 2025 (unverified).
- Open NotebookLM / other open generators were not reviewed.

## 4. LLM script writing for podcasts (Claude / GPT / Gemini)

### Takeaway
I found no authoritative sources this session. The recommendations below are practitioner inferences and should be treated as such.

### Cited Findings
- Podcastfy shows the established pattern: an LLM produces a structured multi-speaker transcript from source content, with configurable style and format, before TTS. — [Podcastfy GitHub](https://github.com/souzatharsis/podcastfy)
- Gemini-TTS and ElevenLabs v3 accept inline delivery tags, so scripts can embed performance cues. Gemini examples: `[sigh]`, `[laughing]`, `[short pause]`, `[whispering]`. Avoid adjective tags that get spoken aloud. — [Google Cloud Gemini-TTS docs](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)

### Inferences (practical patterns)
- **Persona bible:** keep a fixed system prompt with the host's name, age range, personality, catchphrases, banned phrases, register (Turkish "siz" vs "sen"), and examples of 3–5 ideal past turns. Version it in the repo and reuse it with prompt caching.
- **Two-pass generation:**
  1. Outline with sourced facts, as JSON with claim and source URL.
  2. Spoken script built only from the outline.
  3. Optionally a third "fact-check" pass that compares script claims against the outline and flags unsupported ones.
- **Output as structured JSON**, for example `[{speaker, text, style, pause_after_ms}]`, so code can route each line to the right voice and style (e.g. Azure `mstts:express-as style="curious"`, or a Gemini style prompt).
- **Spoken-language rules:** short sentences, contractions, no lists or URLs read aloud, and numbers and abbreviations written out phonetically. Turkish needs particular care: "%25" should become "yüzde yirmi beş", and English loanwords may need SSML phoneme or alias handling.
- **Naturalness:** allow fillers sparingly ("hmm", "yani", "aslında"), interruptions, and callbacks. Set a target word count per minute (around 130–150 wpm in English; Turkish is agglutinative, so measure characters per second on your chosen voice instead).
- **Consistency checks:** run an automated rubric pass (LLM-as-judge) for persona drift, length and banned claims before TTS.

### Gaps
- I found no cited prompting guides, benchmarks of Claude/GPT/Gemini for Turkish conversational scripts, or Turkish developer blog posts in this session.

## 5. Word-level timing (captions, lip sync), music/SFX, loudness standards

### Takeaway
Use the TTS vendor's native events where they exist (Azure tr-TR viseme IDs and word boundaries; Cartesia word/phoneme timestamps). Otherwise run WhisperX or forced alignment on the generated audio, aligned against the known script. Master to -16 LUFS integrated (Apple), or -14 LUFS for Spotify-centric output, with a true peak of -1 dBTP or lower.

### Cited Findings
- **WhisperX** adds wav2vec2 forced alignment to Whisper for word-level timestamps, plus pyannote diarization (needs an HF token and acceptance of the speaker-diarization-community-1 terms; "far from perfect"). Default torchaudio align models cover en/fr/de/es/it, with more via HF in `DEFAULT_ALIGN_MODELS_HF`. Words with characters missing from the aligner's dictionary (such as numbers) get no timing. Licence is BSD-2-Clause (pyannote model CC-BY-4.0). large-v2 needs under 8 GB VRAM, and CPU int8 works. — [WhisperX GitHub](https://github.com/m-bain/whisperX)
- Azure provides viseme IDs with audio offsets for tr-TR, plus SDK word-boundary events. — [Azure viseme how-to](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-speech-synthesis-viseme); [Azure language support](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)
- ElevenLabs Scribe STT costs $0.20/h and could serve as a timestamp source (Scribe supports 90+ languages). — [ElevenLabs API pricing](https://elevenlabs.io/pricing/api)
- **Loudness:**
  - Apple Podcasts: -16 LUFS integrated, true peak -1 dBTP, ±1 dB tolerance.
  - Spotify: -14 LUFS integrated, true peak below -1 dB; if mastering louder than -14 LUFS, keep below -2 dBTP. The -2 dBTP guidance is from a 2020 source and may be dated.
  
  — [Apple Podcasts audio requirements](https://podcasters.apple.com/support/audio-requirements); [Podnews LUFS FAQ](https://podnews.net/article/lufs-lkfs-for-podcasters); [WBUR 2020](https://www.wbur.org/citrus/2020/07/02/lufs-loudness-public-radio-npr-spotify-google); [Auphonic](https://auphonic.com/blog/2019/06/12/the-new-loudness-target-war/)

### Inferences
- **Lip-sync pipeline:**
  1. TTS produces WAV.
  2. Get timings: if Azure, store viseme IDs and offsets directly. Otherwise, use WhisperX or a forced aligner with the known script text, which is better than free transcription because the text is ground truth. Turkish needs an HF wav2vec2 Turkish model; verify it is in the default list.
  3. Map phonemes or characters to a Preston-Blair / Rhubarb-style mouth set. Rhubarb Lip Sync is English-phonetic, but its "phonetic" recogniser can be used on any language (prior knowledge; verify).
- Since TTS text is known, numbers should be spelled out in the script before TTS. That also fixes WhisperX's untimed-number issue.
- For mastering in code: `ffmpeg -af loudnorm=I=-16:TP=-1:LRA=11` (two-pass). Duck background music about 15–20 dB under speech with sidechaincompress. These are standard practice and not cited this session.
- For music and SFX, use royalty-free or AI-generated music with a commercial licence (ElevenLabs Music is "commercial use on Starter+", per the pricing page). — [ElevenLabs API pricing](https://elevenlabs.io/pricing/api)

### Gaps
- I did not confirm whether WhisperX's HF default list includes a Turkish wav2vec2 aligner, nor which model is best for Turkish (e.g. MMS-based aligners via torchaudio `MMS_FA` cover 1,100+ languages, per prior knowledge; unverified).
- I did not research YouTube's loudness normalisation target (commonly cited as about -14 LUFS) or AI-voice disclosure rules (YouTube "altered or synthetic content" label, EU AI Act Art. 50 transparency).
- I did not survey Turkish-specific caption/subtitle conventions.
