# Bengali voice reliability and device-aware fallback (v2.5.0)

Never claim a voice name, prose profile or one approved pilot establishes persistent voice identity. For current Flow modes, reusable Characters and saved/custom voices are **documented controls** but account-specific availability and Bangladeshi Bengali output must be tested on separate clips. Do not infer Gemini App, Vids or Vertex share these controls.

## Audio strategy
1. **NATIVE_TESTED:** For a visible talking face, prefer an actually tested Flow/other renderer native voice reference when it repeatedly preserves correct exact Bengali, timbre and acceptable lip-sync; use an approved pilot plus repeat-speaker clip.
2. **EXTERNAL_MASTER:** Where native voice drifts, record an actor or use a tested Bangla voiceover/TTS service. Measure spoken interval; create silent visuals for cutaways or off-screen explanations. Visible talking plus post-hoc audio is **LIPSYNC_NOT_TESTED** until actual playback reviewed.
3. **VOICEOVER_EDITOR:** Vids or a user-available phone/Windows editor may support voiceover separately. Check Bangla availability, precise wording, length and voice quality on the actual account. An added voiceover is not a cloned voice.
4. **Fallback order:** change only failed audio dependency where possible, not all already approved visual clips; no automatic audio overwrite.

**Edge-TTS accuracy:** the Python `edge-tts` package accesses an **online** Microsoft Edge TTS service; it is not an offline voice engine. Its Bangladesh Bengali voices may be evaluated as candidates, but naturalness, account/network reliability, commercial terms, speech duration and lip-sync need testing. It is **not** a default dependency; no API key/premium subscription is assumed.

## Phone-only voice procedure
- Paste the exact short approved Bangla line into the currently available video/voiceover app.
- Listen to the exported clip at normal speed with earphones, compare with approved reference, check unintended words, timing and extra speakers; record YES/NO/NOT_TESTED.
- If separate audio is preferred, record real speech with phone audio recorder or an actually accessible TTS UI; save exact audio file. Use it as voiceover only where the editor supports it. Do not claim mouth movement is synced or that external TTS can be installed locally on mobile.
- No laptop/FFmpeg/Python is required to plan or inspect speech manually.

## Windows extra procedure
- Optional measured master WAV/MP3, waveform inspection/audio duration (local editor or ffprobe), consistent file naming and per-clip audio ledger.
- `qc_media.py` only checks that an audio stream exists; cannot determine exact Bengali, intelligibility or speaker matching. Medical jargon pronunciation needs Bangladeshi human/clinical reviewer.

## One-line QA
`clip_id | speaker_id | voice_ref | exact_line_bn | actual_first_word_s | actual_last_word_s | timbre | language | pronunciation | lip_sync | evidence | approval`. Unknown measurements stay NOT_TESTED; do not infer word timings from text length.
