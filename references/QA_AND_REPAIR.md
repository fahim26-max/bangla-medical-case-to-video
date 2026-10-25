# QA, repair, re-audit ledger

## Gates and objective evidence
- `G0 Clinical`: all medical claims map to case FACT IDs, no invented test or premature confirmation; reviewer sign-off recorded when available.
- `G1 Cast`: visible age, same face geometry, hair, proportions and wardrobe as approved master(s); unrelated silent doctors not confused with main character.
- `G2 Voice`: correct voice ID; stable Bangladesh Bengali timbre/pronunciation; single designated speaker; no unintended narrator; sample listened to and/or waveform/transcript checked.
- `G3 Location/style`: approved setting layout, character placement, light, stable illustrated style; avoid naturalistic actor when style requires 2D.
- `G4 Anatomy and action`: medical gestures/equipment plausible; Doppler/CTA/endoscopy/ECG are accurate schematics; don't label invented anatomical sites.
- `G5 Time`: actual media duration per manifest, audio doesn't clip, valid aspect/resolution; intro/transition already included.
- `G6 Continuity & legal`: matches neighboring clips, no prohibited personal identifiers, attribution and educational disclaimer in final edit/description.

## Evidence ledger
| clip | version/hash | model/mode | references/version | G0 | G1 | G2 | G3 | G4 | G5 | G6 | exact problem/timecode | repair action | reaudit of new file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | awaiting file | TBD | P01-v1 | UNTESTED | UNTESTED | UNTESTED | UNTESTED | UNTESTED | UNTESTED | UNTESTED | | | |

`PASS` only on actually reviewed artifact; `NOT_TESTED`, `FAIL`, `REPAIR_REQUIRED`, `BLOCKED` otherwise. No fabricated audit. Source asset approval is distinct from generated clip QA. Failed pilot = stop bulk production. When any frozen master is revised, invalidate downstream dependent clips.

v2.2 clarification: preserve historical receipts/exports; mark current dependent QA STALE and bind every new export/receipt to its exact generation contract. Use `SCHEMAS.md` for fingerprints and explicit credit authorization. Prior USER-APPROVED status does not fill missing speech measurements or override a current critical QA FAIL.

## Failure repair decision tree
1. Wrong patient age/face, doctor or clinic: fix/reference master still and start frame, then re-generate. Text-only edits to an image with wrong identity are lower reliability; avoid accumulating wasted credits.
2. Wrong voice/accent: lock or switch to repeatable external TTS/voice actor; test one patient and one doctor voice; rerender or mute generated speech. Check lip sync separately.
3. Medical disinformation: go back to fact register and correct script first; regenerate medical graphic only after reviewed anatomy.
4. Overlong dialogue: shorten precisely and re-record; don't force speech faster than clear normal conversation.
5. Unexpected text or logo: ask video model for none, mask/replace or overlay in editor; check rights, watermark policies (do not remove provenance watermarks).
6. Re-audit **new file** with new version/hash; never mark old video repaired by writing a new prompt.

## Humanizer editorial re-audit (v2.6.0)

Before approving **new** screenplay/job cards, read `HUMANIZER_COMPOSITION.md` and reconcile after any prose changes:
- `EDITABLE_DRAMATIZED`: natural dialogue and operator prose only; author style samples only when actually provided.
- `LOCKED_SOURCE`: original case quotations, patient-specific symptoms/findings, age/sex, tests, medication/dose, diagnosis/differential/uncertainty, dates/numbers and evidence locators; **not eligible for creative language rewriting**.
- `LOCKED_TECHNICAL`: every ID, reference-file role, timing/prompt control, JSON field, approved voice/character/style block, approval event and original media hash.
- After rewrite, require fact/visual map parity and speaker/voice/duration checks; substantive clinical change `FAIL/CLINICIAN_HOLD`. If altered past an approved script/clip/voice, create new version and stale only affected downstream QA; preserve prior receipts. Humanizer is not a medical reviewer, audio engine or AI-detector oracle.
- Operator instructions: one action per step, simple Bangla, technical English in parentheses if useful; mobile flow executable without CLI, Windows scripts optional. No invented feature buttons or unchecked claims. Record `HUMANIZER_SKILL_LOADED`, `HUMANIZER_FALLBACK_APPLIED` or `NOT_RUN` truthfully.

## Retention, promise and medical trust review (v2.7.0)
Apply `HOOK_CLINICAL_SAFETY.md` and `RETENTION_HOOKS.md` before rendering new C01. Review first actual 3s when a file is supplied, and the actual complete 120s before final film approval. One explicit evidence-supported hook promise must receive a real factual payoff, or an honest unresolved-evidence explanation; do not hide time-sensitive warnings for suspense. Track redundant scenes, misaligned title/thumbnail, unclear muted-frame meaning, misleading preview text and unsupported clinical/investigation visuals.
- **DRAFT** candidate language or scene plan is not generated media or audience data.
- **HEURISTIC_REVIEWED** states subjective editorial assessment only, never a predicted retention score.
- **MEDIA_REVIEWED** requires actual visual/audio video and a reviewer; **AUDIENCE_METRICS_OBSERVED** requires platform report/data actually provided.
- A failed source, consent, medical-claim or promise-to-payoff gate is **REPAIR/HOLD**, not something a higher hook heuristic score can override.
- Do not automatically rewrite previously approved Case14 C01/C09, source quotations or hard-locked render prompts.

## Final prepublish
Exact total run time, 16:9, all clips PASS, subtitles not occluding clinical diagrams, audio loudness and music balanced, no repeated voices mismatched, readable metadata/attribution and educational disclaimer. `RELEASE_HOLD` until clinical sign-off where teaching claims are medically consequential.

## Device-aware QA and continuity (v2.5.0)
- Mobile: inspect video at normal playback speed with sound; inspect start/middle/end using the available scrubber or saved stills; compare against the actual approved canon, voice sample, script and neighboring clip; log per-criterion `PASS/FAIL/NOT_TESTED`. If exact exported duration is unavailable, mark G5 `NOT_TESTED` until equivalent measurement is obtained. Do not require desktop apps to prepare drafts or assess identity/Bengali.
- Windows: optionally run `python scripts/qc_media.py clip.mp4 --expected-seconds 8 --audio-route NATIVE`, and `python scripts/make_contact_sheet.py --canon master.png --output sheet.jpg clips/*.mp4` using **installed** FFmpeg/ffprobe. Technical checks flag black/freeze/audio-stream/duration concerns; not speech content, clinical facts, stylistic identity or release eligibility.
- For both devices, audit clip **against canon rather than a possibly drifting previous clip**. Maintain the smallest regeneration ledger (`KEEP/CHECK/REGENERATE/GENERATE`) and protect unrelated approved assets. See `CONTINUITY_PLAYBOOK.md`.
