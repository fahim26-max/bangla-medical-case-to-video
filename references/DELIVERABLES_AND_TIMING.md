# Universal deliverables, timing, and continuity

## Default runtime
Default 15 clips × 8 seconds = 120 seconds exactly (00:00–02:00). Video has no extra unbudgeted intro, logo, or transition. A medical disclaimer and case attribution may be placed in existing frames and full description.

For i=1..15: `start_s = (i-1)*8`, `end_s = i*8`; use continuous intervals `[start_s,end_s)`. If model supports only alternate durations, propose exact math and obtain an approved change before generating. E.g. 12×10 = 120 if the user chooses a documented 10-second mode. Default: 15×8 to maximize compatibility.

## First-three-second and full-film attention layer
For any NEW case, `RETENTION_HOOKS.md` provides 3 C01 alternatives, each with source FACT IDs, exact approved-language draft, visual first frame and promised payoff. Reserve 0–3s inside C01's 8-second unit (or inside the first confirmed alternate unit); do not add a new intro. The remaining 3–8s or 3–10s of C01 starts truthful context. One final approved line is copied into the canonical package. Any optional text overlay is an editor operation and cannot contradict the core `no generated text` visual contract.

Read `RETENTION_BEAT_MAP.md` for a case-adaptive beat map. A phase absent from the actual history stays absent: no fixed number of clinicians, investigations, diagnosis reveal, treatment or death. Avoid repeated static explanations where alternative clinically accurate shots already exist. The hook's promised learning point must be delivered or explicitly bounded by uncertainty **before** the ending. Do not delay genuine urgent safety information.

## Suggested dramaturgy, not rigid case fiction
- Clips 01–02: authentic symptom hook and context
- Clips 03–05: first documented consultation/tests, unresolved effects
- Clips 06–08: subsequent true events, important negatives/clues, clinical reassessment
- Clips 09–10: physical examination and crucial clue
- Clips 11–12: clinician explains reasonable differential and justified investigations
- Clips 13–14: actual evidence supporting diagnosis / or explicit unresolved diagnosis
- Clip 15: authentic outcome and accurate take-home

Rebalance or remove phases if patient history differs. Do not invent a third doctor, surgery, or vascular dissection. For case with a single doctor, retain only that doctor.

## Cast & voice bible schema
Each character:
- Character ID, fictional name, apparent age, sex/presentation, face geometry, hairstyle/facial hair, consistent clothing, stature, posture, temperament
- Reference images: front, 3/4, relevant pose; asset path/name; exact Flow name only after saved; approval and version
- Voice ID, actor or TTS provider preset / seed if supported, Bangladeshi dialect, pitch, speed, timbre, pronunciation dictionary, stable master audio sample, user confirmation; do NOT imply a written voice description guarantees identical samples

Each set/location:
- ID, master reference frame, layout, fixed decor, windows/curtains, furniture, lighting, dominant palette, allowed camera angles, prop placements
- Where time/date changes, create a deliberate NEW location variant, do not silently mutate original

Each style:
- Aspect ratio 16:9, reference art style, 2D cel-shaded/illustrated (default) rather than photorealistic, medically accurate schematic anatomy; subtitle/font planned in editor, not generated raster text

## Manifest fields
| clip_id | start-end | speaker / voice_id | visible IDs | location | EXACT Bengali dialogue | audio_sec VERIFIED? | asset refs | action/camera | source fact IDs | model/mode | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | 00:00–00:08 | P01 / V_P01 | P01 | HOME01 | ... | UNTESTED | ... | ... | F01 | Flow selected model | NOT_GENERATED |

## Prompt skeleton
`CASE: [ID], CLIP: [Cxx], DURATION: 8s, 16:9. Use selected approved ORIGINAL master references: characters [IDs], environment [ID], style [ID], voice [ID] if this mode supports voice. Keep approved identity exact. Scene action: [...]. Camera: [...]. Speaker: [ONE ID ONLY], all others silent. Spoken audio (Bengali, EXACT): "[...]". Must complete within measured target. Clinical facts allowed [IDs]; no other diagnoses, tests or overlays. No generated text, extra people/voices, face age drift, wardrobe changes, photorealism, anatomy errors. If voice cannot be controlled, generate silent clip and use voice master during editing. Render current duration/mode only if actually available.`

## Production states
`NOT_STARTED → FACTS_REVIEWED → SCRIPT_READY → ASSET_PENDING → ASSET_APPROVED → PILOT_PENDING → PILOT_APPROVED → CLIPS_PENDING → CLIPS_QA_PASS → ASSEMBLY_QA_PASS → RELEASE_APPROVED`

Stop/repair states: `UNVERIFIED_FACT`, `AUDIO_UNTESTED`, `CLIP_QA_FAIL`, `REPAIR_REQUIRED`, `RELEASE_HOLD`. Never promote automatically from prompt to generated/approved.

## Optional v2.3 Gemini profile
For confirmed 10s Gemini units use 12x10=120, standalone jobs in separate video conversations. Read GEMINI_INDEPENDENT_CLIPS.md. This alternate profile does not convert old approved 8s outputs. Use the same data schema with a mathematically consistent target and entirely new derivative/approval scope.
