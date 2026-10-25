# Device-aware production: Mobile-first, Windows-enhanced (v2.5.0)

**Contract:** A phone user and a Windows user receive the **same source grounding, P0–P7 clip plan, clinical review and final-approval gates**. Device only changes how prompts, media QA, files and editing are operated. Do not infer available UI features from platform marketing. If device not provided and materially important, ask once; otherwise give a mobile-first path with Windows extras.

## Preflight on either device (v2.5.1)
Copy the exact `REFERENCE_PACKET_TEMPLATE.md` and check `JIO_ACCOUNT_CAPABILITY_MATRIX.md` for the selected mobile or desktop session. The source-restricted `CONDITIONING_COMPATIBILITY.md` does not depend on having FFmpeg. Record `NOT_TESTED` until real account/device controls are observed. If unavailable on phone, use a supported documented fallback or hand off the same files to Windows; never infer that changing device upgrades subscription entitlements.

## Humanized producer output (no extra app required)
Use `HUMANIZER_COMPOSITION.md` to make the **same reviewed script** conversational and the device-specific operator steps concise in Bangla. A mobile user should receive one short copy-ready clip card at a time and clear steps: choose actual route, attach approved reference, paste exact line, inspect/download, record manual QA. A Windows user receives the same steps plus optional FFmpeg/QC commands. Editing for style never changes clinical facts or the approved exact dialogue during cross-device handoff. No special phone Humanizer installation is required for the self-contained editorial fallback; do not claim the separately vendored GitHub skill was activated.

## Retention workflow stays mobile-first (v2.7.0)
On a phone: review three **text-only** source-grounded C01 hook alternatives, select one, verify first 0–3s of the actual video by replay/scrubbing and compare with clinician/owner-approved promise. If a mobile editor supports optional text, apply it as a final edit, not in STYLE01 generated frames; do not invent a button. Use a readable per-clip beat map and a blank platform metrics ledger after real publication. No FFmpeg/Python needed.
On Windows: same clinical and editorial gates. Optional editor side-by-side hook previews and manual/CSV analytics inspection are allowed with actual files; no GPU, social analytics token, provider API or retention score predictor assumed. A 9:16 discovery cut needs an actual supported editor and checked compositions (face, hands, anatomy, Bangla captions, UI safe zones).

## Two orthogonal choices

- `execution_device`: `MOBILE` (Android/iPhone/iPad), `WINDOWS_PC` (Windows 11 desktop/laptop), or `OTHER/UNKNOWN`.
- `video_profile`: currently verified `FLOW_8S` by default, optional supported Flow/Gemini/Vids route. A mobile phone is **not** a new model, duration, API or subscription.
- `capability_status` per action: `OBSERVED_AVAILABLE`, `NOT_CHECKED`, `UNAVAILABLE_ON_DEVICE`. Do not claim screenshots, mode or audio access never observed.
- `technical_qa_state`: `MEASURED`, `MANUALLY_REVIEWED` or `NOT_TESTED`. Human playback cannot establish exact numeric FPS or audio-waveform timing.

## Mobile runbook — no shell/FFmpeg/Python

1. **P0 Case intake:** Paste/supply the actual case text or supported file in ChatGPT/Gemini. De-identify patient information. If links/files cannot be read, preserve source as MISSING; never reconstruct data.
2. **P1 Clinical/script:** Obtain FACT_REGISTER and complete Bengali dialogue mapped to source; clinician reviews unsupported claims. No video generation until required source and safety approvals.
3. **P2 Assets:** Generate or upload approved fictional character, STYLE_ONLY and room masters in a supported image interface. Approve canon/front and selected three-quarter only if needed; record actual file names/versions in the chat/Notion/project folder. Never pretend an image stored in another chat is attached.
4. **P3–P5 Cards:** Ask for all **standalone copy-ready cards**, one per clip, with actual reference attachment list, 8s/10s as observed, single voice and exact Bengali line. Use Flow/Gemini ordinary video UI where that device/account exposes it; Google Vids only if create/edit/export controls are actually accessible. **Never invent taps/menu names.**
5. **P6 Pilot:** Generate one patient and one doctor clip (plus repeat speaker in a new independent route), download/save original when available. Listen with earphones, play through once, scrub first/middle/last, compare to approved canon and actual voice sample. Fill the manual checklist below; mark unmeasurable data NOT_TESTED.
6. **P7 Remaining clips:** Generate only accepted next cards, one at a time; record attempt/take, used reference and changes, original file or durable link, manual PASS/FAIL and charged credits if shown.
7. **Edit:** Use an actually available mobile editor/Flow sequence/Vids surface; align accepted tracks and reviewed captions, check doubled audio, export an MP4 if possible. If a necessary function is absent, stop at approved clip exports and hand off to Windows; do not claim completion.
8. **Final review:** Watch and listen to the **entire exported film**; verify clinical words and visuals, identity, rights, source attribution, captions and total runtime **only when measured by an available device/editor method**. Missing verified runtime or clinical sign-off means RELEASE_HOLD, not automatic failure of mobile.

**Mobile clip ledger (copy per clip):**
```text
Case/clip/take: ...
Route/model/mode: OBSERVED / NOT_CHECKED
Actual attached assets: ...
Expected unit: ... seconds
Downloaded/exported original: YES / NO
Canon appearance: PASS / FAIL / NOT_TESTED
Exact Bengali + speaker voice: PASS / FAIL / NOT_TESTED
Scene/props/anatomy: PASS / FAIL / NOT_TESTED
Full-motion + audio reviewed: YES / NO
Exported duration: value + device evidence / NOT_TESTED
Clinical/source-fact review: PASS / FAIL / HOLD
Continuity with neighbors: PASS / FAIL / NOT_TESTED
Credits shown: amount / UNKNOWN
Decision: KEEP / CHECK / REGENERATE / GENERATE
Next step / approval evidence: ...
```

## Windows PC/laptop — **additional** features only

The **same P0–P7** applies. If installed and authorized, use:
- Python local `new_case.py`, `validate_package.py`, `preflight_handoff.py` and the existing `check_gemini_export.py`; validate source/manifest/attachment data, never medical truth.
- `python scripts/qc_media.py clip.mp4 --expected-seconds 8 --audio-route NATIVE` (optional; installed `ffmpeg` and `ffprobe`). Returns duration, dimensions, FPS, audio-stream presence and black/freeze *warnings* with JSON and no false clinical PASS.
- `python scripts/make_contact_sheet.py --canon PATIENT_MASTER.png --output patient_sheet.jpg C01.mp4 C02.mp4` (optional; FFmpeg/ffprobe). Compare middle frames side by side **against original canon**. Requires actual local files, not Notion or chat asset labels.
- Use a supported editor/FFmpeg for track alignment/concat/captions. Verify final export against clip manifest; cut/overlap affects 120s duration. Scripts never upload case data.
- Windows performance: default FFmpeg + standard Python, no mandatory CUDA/Torch/face-recognition or cloud key; suitable for an 8 GB RAM laptop with bounded clip processing.

## Phone → Windows handoff without redoing approved work

Transfer the **actual original media** through a user-chosen secure mechanism, plus case ID, canonical package, approved stills/voice samples, clip names/versions, QA decisions and outstanding fields. Verify hashes on Windows where originals exist; unsupported mobile hash collection stays UNKNOWN. Run only *missing* technical checks, preserving human approvals and prior failures; never silently overwrite or re-render. If source lacks consent/de-identification, do not transfer/share until corrected.

## Blocking versus optional checks

- **Always blocking:** unresolved consequential clinical facts, missing required images/voice approvals, unsafe identifiable data, failed pilot, unavailable actual generator route, missing final medical owner approval.
- **Device-specific:** unavailable local FFmpeg is **not** a reason to forbid source/script/clip creation on a phone. Numeric FPS/duration or audio presence claims must still be measured when required for release; mobile can use any demonstrably reliable export/media-property method rather than obligatory Windows.
- `TECHNICAL_PASS` from an optional script never equals `G0–G6 PASS` or `RELEASE_APPROVED`.
