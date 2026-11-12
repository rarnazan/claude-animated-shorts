# Technology for generating a talking virtual female podcast host video programmatically (late 2026)

Research date: 2026-11-12. I used 15 tool calls. Many pricing figures come from third-party blogs that disagree with each other; I say so wherever they conflict. I could not reach the official HeyGen API pricing page: it redirects to an app modal that needs a login.

## 1. Commercial avatar / talking-head APIs: availability, price, length, Turkish, custom avatars, terms

### Takeaway
Every major vendor (HeyGen, Synthesia, D-ID, Hedra, Tavus) now has an API. Vendors that sell per-second video models (Kling Avatar 2.0, OmniHuman 1.5 via fal, Veo 3.1) are the cheapest way to make photo-plus-audio lip sync from code, at roughly $0.04–0.16/s ($2.4–10/min). Full avatar platforms cost about $1–7/min. HeyGen is the only vendor I could confirm supports Turkish lip sync.

### Cited Findings
**HeyGen**
- A HeyGen-published comparison (updated 5 Nov 2026, pricing checked Oct–Nov 2026) gives these API rates: pay-as-you-go with a $5 minimum; $1.00/min for Avatar III Digital Twin, $3.00/min for Avatar IV Photo Avatar, $4.00/min for Avatar V Digital Twin. The article contradicts itself, also giving $0.60/min for Avatar III and $7.20/min for Avatar V. Custom avatar creation by API is listed at $2.13 per Digital Twin call and $1.32 per Photo Avatar, but the same page's table says "Enterprise only". It claims 177+ languages. This is a vendor source that ranks itself first. — [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis)
- Third-party figures: API billing moved to pay-as-you-go in Feb 2026, from a separate USD wallet that does not draw on Studio plan credits. Avatar IV is quoted at $3/min (photo) and $4/min (digital twin), and also at $2.31 and $4.83/min. Avatar III is quoted at $0.60–0.99/min. — [Creatify](https://creatify.ai/blog/heygen-pricing-(2026)-plans-and-what-you-ll-actually-pay); [Magic Hour](https://magichour.ai/blog/heygen-pricing); [diyai.io](https://diyai.io/ai-tools/video-generation/heygen-pricing/)
- Turkish: HeyGen lists Turkish among its 175+ languages. Its Turkish TTS page markets phoneme-level lip sync for Turkish speech, and its video translation feature offers lip-sync mode. — [HeyGen Turkish TTS](https://www.heygen.com/en-gb/text-to-speech/turkish); [HeyGen translation languages](https://help.heygen.com/en/articles/11391941-video-translation-languages-we-support)

**Synthesia**
- API access starts on the $89/mo Creator plan. Per-minute price is not published; usage is about 120 credits per standard minute. — [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis)
- Third-party figures conflict: 120 credits/min standard versus 90 credits/min via API. Starter is $19/mo ($14 billed yearly) and Pro/Creator is $89/mo. Custom Studio avatars work through the API, but personal photo/video avatars reportedly do not. A $1,000/yr custom-avatar add-on is reported but unconfirmed. — [Magic Hour](https://magichour.ai/blog/synthesia-pricing-2026); [Dupple](https://dupple.com/learn/synthesia-pricing); [Arcade](https://www.arcade.software/post/synthesia-pricing)

**D-ID**
- D-ID has an API with per-plan minute allotments (Build 16 min, Launch 45, Scale 200). Per-minute price is not published. — [Creatify D-ID](https://creatify.ai/blog/d-id-pricing-(2026)-plans-credits-and-what-you-ll-actually-pay); [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis)

**Hedra (Character-3)**
- Hedra's API uses a prepaid dollar balance: $1.50/min at 540p, $3.00/min at 720p, $3.75/min at 1080p, with videos up to 10 minutes. — [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis)
- Per-second figures conflict across sources (2.5/5/6.25 ¢/s by resolution versus 6–7 credits/s). Some sources still describe Hedra as UI-only. — [novoads](https://novoads.ai/en/blog/hedra-pricing); [usagepricing](https://usagepricing.com/blueprint/hedra)

**Tavus**
- Tavus has a REST API. Overage costs about $0.80–1.00/min (about $1.30/min effective on Growth), and replicas (custom avatars) can be trained by API on self-serve plans. — [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis)

**Kling AI Avatar 2.0 (image + audio → talking video)**
- On fal: Standard costs $0.0562/s (`fal-ai/kling-video/ai-avatar/v2/standard`) and Pro $0.115/s (`.../v2/pro`). — [fal Standard](https://fal.ai/models/fal-ai/kling-video/ai-avatar/v2/standard); [fal Pro](https://fal.ai/models/fal-ai/kling-video/ai-avatar/v2/pro)
- Other resellers are cheaper. Runware: $0.044/s Standard, $0.087/s Pro. PoYo: $0.035/$0.070 per second, billed on audio duration rounded up. — [Runware](https://runware.ai/models/klingai-avatar-2.0-pro); [PoYo](https://poyo.ai/en/models/kling-avatar-2-0)

**ByteDance OmniHuman 1.5**
- On fal it takes one portrait plus an audio file and outputs a lip-synced avatar video for $0.16/s. — [fal OmniHuman 1.5 guide](https://fal.ai/learn/devs/omnihuman-15-user-guide)

**Google Veo 3.1 (generates native audio and dialogue itself)**
- Gemini API: Standard costs $0.40/s at 720p/1080p and $0.60/s at 4K. Fast costs $0.10/s (720p) or $0.12/s (1080p). Clips are at most about 8 s. Runway resells Veo 3.1 at $0.40/s with audio. — [Hedra cost comparison](https://www.hedra.com/blog/video-model-api-cost-comparison); [apiframe](https://apiframe.ai/blog/ai-video-api-pricing-2026)
- Kling 3.0 general video with native audio costs about $0.168/s at 1080p. — [AI Video Costs](https://aivideocosts.fyi/)

**Other**
- The HeyGen comparison also mentions Google real-time avatars via the Gemini API, with custom avatars limited to select customers, and Banuba's talking-photo API with no public rate. — [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis)

### Inferences
- For a fictional host built from one locked portrait plus your own TTS audio, audio-driven endpoints are the most code-friendly and cheapest per minute. Kling Avatar 2.0 Standard works out to about $2.1–3.4/min and Pro about $4.2–6.9/min; OmniHuman 1.5 is about $9.6/min. HeyGen Avatar III/IV ($1–4/min) can beat them on price for long talking segments.
- Veo 3.1 at about $24/min (Standard) or $6–7/min (Fast), with an 8 s clip cap, suits B-roll or cutaway shots rather than a 10–20 min host monologue. It also generates its own voice, which makes it hard to keep one consistent TTS voice.
- Audio-driven models (Kling Avatar, OmniHuman, Hedra, open-source models) lip-sync from the audio waveform, so in principle they work for any language, Turkish included, if you supply Turkish TTS audio. Text-driven avatar platforms instead depend on the vendor's own Turkish TTS. This inference is consistent with a third-party claim that HeyGen Avatar 4 lip-syncs any supplied speech ([creativeclaw](https://creativeclaw.co/ai-video-generator/turkish/)), which I could not verify.

### Gaps
- I could not verify official HeyGen API pricing; the page needs a login and redirects to app.heygen.com.
- Max video length per API call was not found for HeyGen, Synthesia, D-ID, Tavus or Kling Avatar. Only Hedra's 10-minute limit was found.
- I found no source on Synthesia, D-ID, Hedra, Tavus or Kling Avatar confirming Turkish lip-sync quality or Turkish UI/TTS support.
- I did not research Captions (Mirage), Runway Act-Two, OpenAI Sora 2 API or Kling Avatar's maximum duration within my tool budget.
- I did not fetch commercial-use and ownership clauses from any vendor's ToS. Check each vendor's terms of service, especially for synthetic/stock avatars and AI-disclosure rules.

## 2. Open-source audio-driven talking-head / lip-sync models

### Takeaway
For commercial use, the safest strong options are InfiniteTalk (Apache-2.0 code and weights; Wan2.1-14B; long video) and LatentSync 1.6 (Apache-2.0; 18 GB VRAM; best lip-sync quality but slow). MuseTalk (MIT) is the real-time option but runs at 256×256. Wav2Lip's public model does not allow commercial use. Hallo2 and Hallo3 have restrictive or inherited licences.

### Cited Findings
- **InfiniteTalk (MeiGen-AI):** Generates audio-driven video from image+audio or video+audio, with lips, head, body and expression all driven by the audio. It is built on Wan2.1-I2V-14B-480P with a chinese-wav2vec2 audio encoder and runs at 480p or 720p. Streaming mode gives "unlimited" length: the default `max_frame_num` is 1,000 frames (40 s), and image-to-video looks good up to about 1 min before colour shift appears. Low-VRAM options include `--num_persistent_param_in_dit 0`, fp8 quantization, and multi-GPU FSDP. Default sampling is 40 steps; FusionX LoRA cuts that to 8 steps and lightx2v to 4. An official ComfyUI branch exists. The README says the models are licensed under Apache 2.0. Weights were released in Aug 2025. Related news: LongCat-Video-Avatar (Dec 2025) and LongCat-Video-Avatar-1.5 (May 21, 2026), which uses a Whisper-Large encoder, supports multi-stream audio and runs in 8 steps. — [InfiniteTalk GitHub](https://github.com/MeiGen-AI/InfiniteTalk)
- **LatentSync (ByteDance):** The latest version is 1.6 (2025-06-11), trained at 512×512. Minimum inference VRAM is 8 GB for v1.5 and 18 GB for v1.6. Licence is Apache-2.0. More steps (20–50) give better quality but run slower. This is a video-to-video lip-sync model: it edits the mouth of an existing video. — [LatentSync GitHub](https://github.com/bytedance/LatentSync)
- A third-party source says LatentSync checkpoints on HF are tagged openrail++ and MuseTalk's creativeml-openrail-m, and that both still permit commercial use. — [search summary of tomodahinata / others](https://tomodahinata.com/en/blog/ai-lip-sync-talking-head-model-selection-guide-2026)
- **MuseTalk:** Code is MIT and the model is usable commercially; test data is research-only. It does real-time latent-space inpainting at 30+ fps on a V100 but outputs only a 256×256 face region, so it needs super-resolution. Known issues are jitter and loss of fine identity detail. It supports multiple languages. — [tomodahinata guide (June/July 2026)](https://tomodahinata.com/en/blog/ai-lip-sync-talking-head-model-selection-guide-2026); [MuseTalk GitHub](https://github.com/TMElyralab/MuseTalk)
- **LatentSync** is called language-independent because it uses Whisper audio embeddings, and is rated the highest quality but slow. — [tomodahinata guide](https://tomodahinata.com/en/blog/ai-lip-sync-talking-head-model-selection-guide-2026)
- **Wav2Lip:** The public model is research/non-commercial only (trained on LRS2) and outputs a 96×96 mouth region with strong sync but low detail. Commercial use requires a separate HD-model contract. — [tomodahinata guide](https://tomodahinata.com/en/blog/ai-lip-sync-talking-head-model-selection-guide-2026)
- **SadTalker (2023, older):** Licensed Apache-2.0 excluding third-party components; an earlier non-commercial restriction has been removed. It is 3DMM-based, generating from a single image, and its naturalness is weaker. — [tomodahinata guide](https://tomodahinata.com/en/blog/ai-lip-sync-talking-head-model-selection-guide-2026); [sync.so](https://sync.so/blog/what-is-sadtalker)
- **Hallo3 (Fudan, CVPR 2025):** A video diffusion transformer built on CogVideoX-5B I2V. Use must comply with the CogVideo-5B licence. **Hallo2:** its high-resolution part is under the S-Lab License 1.0. — [Hallo3 paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Cui_Hallo3_Highly_Dynamic_and_Realistic_Portrait_Image_Animation_with_Video_CVPR_2025_paper.pdf); [SourcePulse hallo3](https://www.sourcepulse.org/projects/1845276); [SourcePulse hallo2](https://www.sourcepulse.org/projects/1855774)
- **Ditto (Ant Group, ACM MM 2025):** Motion-space diffusion for controllable real-time talking heads, Apache-2.0. — [Ditto GitHub](https://github.com/antgroup/ditto-talkinghead)
- **EchoMimic V2/V3 (Ant Group):** V2 was updated Feb 2026. Secondary sources say V3 runs half-body and full-body on 12 GB VRAM. I did not verify the licence. — [GitHub talking-head topic](https://github.com/topics/talking-head); [search summary](https://tomodahinata.com/en/blog/musetalk-realtime-lip-sync-production-guide)
- Hallo, EchoMimic and AniPortrait are described as heavier and slower, with mixed licences and commercial conditions. — [tomodahinata guide](https://tomodahinata.com/en/blog/ai-lip-sync-talking-head-model-selection-guide-2026)
- Lists of further models: [Awesome-Talking-Head-Synthesis](https://github.com/Kedreamix/Awesome-Talking-Head-Synthesis). Training dataset: TalkVid (CVPR 2026 Findings), Apache-2.0 code with a separate dataset licence. — [TalkVid](https://github.com/FreedomIntelligence/TalkVid)

### Inferences
- Practical hardware tiers:
  - 24 GB (RTX 4090/3090): LatentSync 1.6, InfiniteTalk with fp8 and offload at 480p, MuseTalk real-time.
  - 48–80 GB (A6000/A100/H100): InfiniteTalk 720p at reasonable speed.
  - Renting a cloud GPU at about $1–3/hr is the usual route.
- A hybrid pipeline is common and robust: generate the body and head motion once (an idle talking loop from an I2V model or InfiniteTalk), then run LatentSync or MuseTalk per episode to re-lip-sync the mouth to new Turkish audio.
- Turkish: the Whisper-based models (LatentSync, LongCat-Avatar-1.5, MuseTalk) should handle Turkish phonetics better than models with Chinese- or English-only audio encoders (InfiniteTalk uses chinese-wav2vec2). This is my inference; I found no Turkish benchmark.

### Gaps
- I found no measured VRAM for Hallo2/Hallo3, EchoMimicV3, Wan2.2-S2V or LivePortrait in this session.
- I did not fetch LivePortrait's licence. From memory: the code is MIT, but it depends on InsightFace models that are non-commercial. This is unverified and must be checked.
- I found no objective 2026 benchmark (LSE-C/D, FID) comparing these models, and no Turkish-specific evaluation.

## 3. Code-driven 3D/2D avatar route (VRM, three.js, Remotion, Blender, MetaHuman, Live2D, visemes)

### Takeaway
A fully code-rendered podcast studio is feasible and costs nothing per minute: Azure TTS supplies 22 viseme IDs and 55 ARKit-style blend shapes at 60 fps, and a three.js engine such as TalkingHead (MIT) animates an ARKit/Oculus-viseme GLB avatar. Turkish needs a TTS that outputs visemes or timestamps, because TalkingHead has no built-in Turkish module. The look is stylised 3D, not photoreal.

### Cited Findings
- **Azure Speech visemes:** Neural TTS can output viseme IDs (22 visemes with audio offsets in 100 ns ticks), SVG (en-US only), or 3D blend shapes. Blend shapes are a JSON matrix at 60 fps with 55 facial positions per frame (ARKit-style names such as jawOpen, mouthFunnel, eyeBlinkLeft, plus headRoll and eye rolls). They are requested with the `mstts:viseme` SSML element and received via the SDK's `VisemeReceived` event, available in C#, C++, Java, Python and JS. Visemes vary by locale; the supported-locale list is a separate page. — [Microsoft Learn: viseme (updated 2026-06)](https://learn.microsoft.com/azure/ai-services/speech-service/how-to-speech-synthesis-viseme)
- **TalkingHead (met4citizen):** A JS class (three.js/WebGL) for real-time lip sync of full-body GLB avatars with a Mixamo rig and ARKit + Oculus viseme blend shapes. Avaturn avatars are fully compatible; VRoid/VRM needs Blender conversion. Built-in lip-sync languages are English, German, French, Brazilian Portuguese, Finnish, Lithuanian and Bengali; Turkish is not listed, but you can write a language module or use a TTS that outputs visemes (Azure, for 100+ languages). It integrates Google TTS (default), ElevenLabs (word timestamps), Azure (visemes or blend shapes) and HeadTTS (Kokoro, in-browser). The class is MIT, and the sample Ready Player Me avatar is CC BY-NC 4.0. There is no built-in offline export; the demos are screen captures. — [TalkingHead GitHub](https://github.com/met4citizen/talkinghead)
- Open-source "video OS" projects combine Remotion with voice cloning, avatars and Wan 2.2/LTX, for example vanta. — [vanta GitHub](https://github.com/nickstrooo-bot/vanta)

### Inferences
- Code-rendered pipeline:
  1. Script.
  2. Azure TTS (tr-TR voice) with visemes or blend shapes JSON, or Turkish TTS from another vendor plus Rhubarb or a forced aligner for timings.
  3. Drive the blend shapes in three.js (TalkingHead) inside a Remotion composition, or in Blender via a Python script that keyframes shape keys.
  4. Render deterministic frames headlessly (Remotion renders frames via headless Chromium; Blender via `blender -b -P`).
  5. Mux with ffmpeg.
- The "studio" can be a GLB room scene with desk, mic, neon sign and screen texture for topic graphics. Script camera cuts and idle motions (blinks, head sway, gestures from Mixamo clips) in code.
- Unreal MetaHuman with Audio2Face or MetaHuman Animator gives the most realistic 3D, but needs a Windows/GPU workstation and Unreal's licence terms. It is less easy to automate headlessly than three.js or Blender.
- Live2D (2D anime style) also accepts viseme/mouth-open parameters, but Live2D's SDK has its own commercial licence tiers. This is from memory; check it.
- Ready Player Me: I believe its consumer service was wound down in 2025–2026 after an acquisition, but this is unverified (the TalkingHead page doesn't mention it). Prefer Avaturn, VRoid→GLB or a custom Blender model.

### Gaps
- I could not confirm whether tr-TR is in Azure's viseme/blend-shape locale list; the language-support page was not fetched. Test with a tr-TR neural voice and `mstts:viseme type="FacialExpression"`.
- I did not verify Rhubarb Lip Sync's licence or language support. From memory it is MIT with an English recognizer and a language-independent "phonetic" mode suitable for Turkish; unverified.
- I did not check the current Ready Player Me status, Live2D licence fees or MetaHuman licence terms.

## 4. Keeping the same character consistent across episodes

### Takeaway
For a single static on-camera host, the simplest and strongest method is to lock one master portrait (or a short master video of the avatar) and reuse it as the input image for every episode. Use reference-image editors (Nano Banana Pro, Flux Kontext / Flux.2) or a LoRA only for variant outfits, angles and thumbnails.

### Cited Findings
- One guide ranks consistency methods: seed control is mild, reference images are strong, and LoRA training is near-perfect. LoRAs are recommended for 15+ images or ongoing work. The same guide says Nano Banana Pro is the strongest no-training commercial reference workflow, Flux Kontext suits precise single-element edits, and Flux 2 Pro accepts up to 10 references with roles. — [rangy.ai](https://rangy.ai/blog/ai-character-consistency)
- Native multi-reference in major video tools now handles many short-series jobs that previously needed a custom LoRA. — [ocdevel](https://ocdevel.com/podcaster/ai-video-generation/e6d4b1b8-a0a1-425c-8680-e92ee595a6b2)
- Sources conflict: one says Nano Banana and GPT-4o lead hard consistency tests while Flux Kontext trails over long sequences; others praise Kontext for face preservation. — [batchframes](https://batchframes-landing.pages.dev/blog/keep-ai-characters-consistent-across-shots/); [martini.art](https://martini.art/en/blog/how-to-build-consistent-ai-character)
- The common pattern is to lock a still, then hand it to a talking-head model such as Kling Avatar or OmniHuman. — [martini.art](https://martini.art/en/blog/how-to-build-consistent-ai-character)
- Vendor equivalent: HeyGen Photo Avatar / Digital Twin creation via API ($1.32 / $2.13 per creation per HeyGen) turns the fictional host into a reusable avatar ID. — [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis)

### Inferences
- Recommended setup:
  1. Generate the fictional host once (text-to-image).
  2. Build a character sheet (front, 3/4, outfits) with Nano Banana Pro or Flux Kontext.
  3. Optionally train a Flux/SDXL LoRA on 15–30 curated images for thumbnails and B-roll.
  4. Always feed the same 1080p frontal "studio" frame to the lip-sync model.
  5. Keep the voice fixed: one TTS voice ID or a cloned synthetic voice.
- Many I2V talking-head models drift in identity or colour over long clips (InfiniteTalk notes colour shift after about 1 min). Render in 20–60 s chunks, each restarted from the master frame, and join them with cuts or B-roll.
- The 3D/code route has perfect consistency by design, since it is the same mesh every time.

### Gaps
- I found no primary-source benchmark of identity consistency; all the rankings above come from vendor or secondary blogs.

## 5. End-to-end pipeline and realistic per-episode cost

### Takeaway
A typical code pipeline is: LLM script → TTS (Turkish voice) → lip-sync video (API or self-hosted) → Remotion/ffmpeg assembly with captions and B-roll → automatic vertical clips. For a 10-minute episode, avatar-video cost is roughly $10–70 via commercial APIs, a few dollars of GPU time self-hosted, and near $0 on the code-rendered 3D route (TTS costs extra).

### Cited Findings
- Per-minute rates used in the estimates below:

  | Option | Rate | Source |
  |---|---|---|
  | HeyGen Avatar III | $1/min | [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis) |
  | HeyGen Avatar IV photo | $3/min | [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis) |
  | Hedra 720p | $3/min | [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis) |
  | Tavus | about $1–1.30/min | [HeyGen blog](https://www.heygen.com/blog/best-ai-avatar-talking-head-apis) |
  | Kling Avatar 2.0 Std | $0.0562/s on fal | [fal](https://fal.ai/models/fal-ai/kling-video/ai-avatar/v2/standard) |
  | OmniHuman 1.5 | $0.16/s | [fal](https://fal.ai/learn/devs/omnihuman-15-user-guide) |
  | Veo 3.1 Fast | $0.10–0.12/s | [Hedra comparison](https://www.hedra.com/blog/video-model-api-cost-comparison) |

- Example open-source pipelines that compose these steps:
  - Remotion + avatars + Wan 2.2/LTX: [vanta](https://github.com/nickstrooo-bot/vanta)
  - An Apache-2.0 song → lip-sync music-video pipeline: [beenga-video-os](https://github.com/Beenga/beenga-video-os)
  - A self-hosted GPU dubbing pipeline (2026): [Spheron](https://www.spheron.network/blog/self-host-ai-dubbing-gpu-cloud-localization-pipeline-2026/)

### Inferences
- Pipeline sketch:
  1. **Script:** LLM generates the Turkish script with segment markers.
  2. **TTS:** ElevenLabs / Azure tr-TR / OpenAI TTS (verify Turkish quality) produces a WAV per segment, plus word timestamps or visemes.
  3. **Video:**
     - (a) API route: POST the master portrait and audio to Kling Avatar / OmniHuman / Hedra / HeyGen, poll the job, download MP4.
     - (b) Self-hosted route: InfiniteTalk or LatentSync in ComfyUI or a Python script on a rented GPU.
     - (c) 3D route: three.js/Blender driven by visemes.
  4. **Edit:** Remotion (React) or ffmpeg composites the studio background, lower thirds, Turkish captions from word timestamps, and B-roll.
  5. **Shorts:** Cut 9:16 clips by crop/reframe with ffmpeg (`crop=ih*9/16:ih`), or by a Remotion vertical composition, with burned-in captions.
  6. **Upload** via the YouTube/TikTok APIs.
- Rough avatar-only cost for a 10-minute episode at the cited rates:

  | Option | Cost per 10-min episode |
  |---|---|
  | HeyGen Avatar III | about $10 |
  | HeyGen Avatar IV | about $30–48 |
  | Hedra 720p | about $30 |
  | Kling Avatar Std | about $34 on fal (about $21 on cheaper resellers) |
  | Kling Pro | about $69 |
  | OmniHuman 1.5 | about $96 |
  | Veo 3.1 Fast | about $60–72 (and 8 s clips) |
  | Self-hosted InfiniteTalk/LatentSync | GPU-hours × $1–3/hr; rendering speed unbenchmarked, plausibly a few hours on one 24–80 GB GPU |
  | Code-rendered 3D | near $0 plus TTS |

- A practical cost saver: show the avatar only on intro, outro and key lines, about 30–40% of runtime, and cover the rest with B-roll or slides. That cuts avatar spend by 60–70%.
- Commercial TTS for Turkish (ElevenLabs, Azure) adds a few dollars per episode at typical character pricing. I did not verify those prices in this session.

### Gaps
- I found no measured wall-clock render times per minute for InfiniteTalk or LatentSync on specific GPUs.
- I did not research Turkish TTS vendor pricing or quality comparisons (ElevenLabs v3, Azure tr-TR, Google, OpenAI) within my budget.
- I did not research platform rules on AI disclosure and labelling (YouTube/TikTok synthetic content labels, EU AI Act Art. 50 transparency from Aug 2026).
