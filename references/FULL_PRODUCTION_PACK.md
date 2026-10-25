# Complete case-independent production pack

## Contents
1. Input and defaults;2. Output contract;3. Instrument list;4. Prompt stages;5. Human decisions;6. Resume.

## Device-aware deliverables (same clinical quality on every device)
Before generating operator instructions, distinguish `execution_device` from Flow/Gemini/Vids `video_profile`. Read `DEVICE_WORKFLOWS.md`: a phone-only user gets a complete compact copy-paste card set and human QA/checkpoint log; a Windows user additionally gets optional runnable FFmpeg checks and contact sheets. Include `05_jobs/DEVICE_RUNBOOK_v001.md` as an operator view, and `07_qa/MANUAL_QA_v001.md` in **both** modes (forms may be plain text). Technical sidecars may be absent in mobile mode; never synthesize results. This adds no required keys to `production.schema.json`. Device switching is a checkpoint/handoff, not a new production or rerender.

## Human-readable production layer (v2.6.0)
Read `HUMANIZER_COMPOSITION.md`. Generate the *source-anchored* full screenplay first. Apply constrained natural-Bangladesh-Bengali editing **only to invented/dramatized dialogue and user-facing explanations**, never original clinical facts or quoted utterances. Then re-audit speaker, intended clinical message, fact IDs, attribution, uncertainties and timed audio against the original before marking the script ready for owner/clinician approval. The same final exact spoken line must appear in `02_script/SCREENPLAY_v001.md`, canonical JSON `clips`, and renderer-ready `05_jobs/JOB_CARDS_v001.md`; no draft/final divergence or new runtime just to sound fluent.

For the operator, write `05_jobs/OPERATOR_STEPS_v001.md` as simple Bangla action instructions with copy-ready exact prompts; mobile has no shell/FFmpeg and Windows additions must be clearly marked optional. Generate one `07_qa/HUMANIZER_REVIEW_v001.md` note per revision with **skill actually loaded vs fallback**, protected facts/quotes, before→after changed dialogue IDs, source-claim reconciliation, duration check, version/approval invalidation and human-review status. Do not claim a pass for a report that was not completed. The humanizer layer is editorial, not source validation or AI-detection certification.

## Attention and retention deliverables (v2.7.0)
After `FACT_REGISTER` and before the final exact screenplay, consult `RETENTION_HOOKS.md`, `HOOK_CLINICAL_SAFETY.md`, `RETENTION_BEAT_MAP.md`, and `RETENTION_ANALYTICS.md`. Draft 3 **case-grounded** and fact-ID-linked C01 0–3s candidate openings; include first-frame image/action, exact short Bengali line, optional **final-editor** text overlay, first sound and how the film fulfills its promise. Select one on source safety/naturalness/realistic timing and owner review; retain alternatives as DRAFT, not separate approval or render permission. Humanizer editorial pass must preserve medical meaning; a final re-audit freezes one exact screenplay/JSON/clip-card line.

Include `02_script/HOOK_VARIANTS_v001.md` (no invented source claims), `02_script/RETENTION_BEAT_MAP_v001.md` (one useful intent/visual/payoff per real supported clip), `07_qa/RETENTION_PREFLIGHT_v001.md` (promise, silence/muted preview, fidelity, pacing, payoff), and `08_final/RETENTION_ANALYTICS_v001.md` as **blank post-publish template until real measurements exist**. The optional 9:16 vertical extraction must preserve composition/facts/captions with separate owner/editor review; do not assume an automatic crop is viable.

Neither editorial heuristics nor text-only A/B picks predict real views. The available human+clinical review, generator pilot and publication approvals remain independent. No unnecessary new patient scenes/consultations/tests, no fixed cliffhanger placement and no made-up viewer data.

## 1. Start from the case, not the fixture
Accept original accessible text/PDF/transcript/link through the host's available readers. Preserve author and source. A failed URL or unreadable image is missing evidence, not permission to reconstruct text. Extract source-supported demographics, chronology, signs, investigations, interpretations, management and outcomes; unknown stays unknown. Distinguish source facts from fictional appearance/staging. The optional local starter accepts UTF-8 text only; it is not an OCR/PDF extractor.

Default route FLOW_8S,120s,15×8,16:9,Bangladeshi Bengali,controlled semi-realistic2D style. Read `PLATFORM_ROUTES.md` before selecting alternate units. Use existing audience preference; otherwise disclose the existing clinical-learning default and write accessible Bengali. Do not force every case into multiple consultations, definitive diagnosis or surgery. Sparse source: label NEEDS_SOURCE_FOR_SUBSTANTIVE_DRAMA/HOLD; offer a shorter faithful draft. Minimal optional questions; proceed with labelled drafts where safe.

## 2. Produce everything requested in one planning pack
For “full pack”, prepare all draft lines, all needed asset/keyframe prompts and all per-clip job cards now; do not stop after two pilot cards. Only eligible, inspected and approved dependencies can become ready for a scoped render. A DRAFT card is useful but is not an executable/approved job. Keep the canonical production JSON and human-readable views consistent; no divergent dialogue copies.

| Output location | Required content |
|---|---|
| `00_sources/` | Original source bytes/text and source receipt; actual author/URL/date/hash, limits, de-identified derivative if needed. |
| `01_evidence/production_package_v001.json` | Existing v2.2 schema: facts, quotes/locators, unknowns/exclusions, visual facts, creative choices, dependencies, receipts. |
| `02_script/SCREENPLAY_v001.md` | Hook/arc appropriate to source; one canonical natural-Bangla exact dialogue per clip, speaker, fact IDs, continuous timing, mute cast and visual claim IDs; source/quote locks preserved. |
| `02_script/HOOK_VARIANTS_v001.md` | Three factual C01 0–3s options with first-frame/line/optional editor overlay/sound/promise; owner selects one, others DRAFT. |
| `02_script/RETENTION_BEAT_MAP_v001.md` | Every selected-unit clip's truthful story beat, visual action, unresolved/resolved question and source fact IDs; flexible to actual case. |
| `03_bibles/BIBLES_v001.md` | Characters, voices/pronunciation, rooms/style/props; demographic basis and approved immutable identity text; allowed variants. |
| `03_bibles/ASSET_PROMPTS_v001.md` | Copy-paste image/audio specifications for every missing master/sample; exact supplied reference roles. Do not generate/recreate existing approved originals. |
| `04_keyframes/KEYFRAME_PROMPTS_v001.md` | Every necessary shot composition from approved dependencies, anatomy/props, camera axis, cast placement; reuse an adequate approved frame. |
| `05_jobs/JOB_CARDS_v001.md` | Every clip's expanded renderer-specific card: actual attachment roles, literal dialogue, voice route, mute cast, action, camera, current/requested settings, negative constraints and state. |
| `05_jobs/handoff_v001.json` | Companion identity/attachment inventory for local handoff preflight; not an app import API or a replacement production/approval record. |
| `05_jobs/OPERATOR_STEPS_v001.md` | Selected app's click/copy/attach/download sequence; native/external audio steps; capability, quota and permission boundary. |
| `07_qa/ATTEMPTS.csv` | Every take: prompt/dependency versions, observed settings, active/elapsed time, quoted/charged units, exported hash/duration, seven QA criteria and failure decision. |
| `07_qa/CHECKPOINT_v001.md` | Last completed work, actual files, receipts, budget remaining, missing dependencies, next eligible action. |
| `07_qa/HUMANIZER_REVIEW_v001.md` | Optional/scope-limited editing provenance: sibling skill actually loaded vs fallback, changed dramatized line IDs, locked clinical quote check, audio duration recheck, clinical/owner status. Never invent a completed pass. |
| `07_qa/RETENTION_PREFLIGHT_v001.md` | Human-reviewed first 3 seconds, continuity, promise fulfillment and clinical-safety checks. Retention from actual audience stays UNMEASURED. |
| `08_final/RETENTION_ANALYTICS_v001.md` | Blank platform/format-aware post-publication observation form, actual stats only when supplied; no auto-publish/analytics access assumed. |
| `08_final/EDIT_PLAN_v001.md` | Ordered accepted files, cuts/transition budget, voice/music/captions/attribution and export/final-review steps. No fabricated caption timestamps. |
| `08_final/PUBLISH_PLAN_v001.md` | Source-faithful title/hooks/thumbnail brief and distribution hypothesis; rights/clinical/owner review; analytics and revenue UNKNOWN before evidence. |

Before final delivery, return a concise Bengali state table: CREATED/DRAFT, missing source/assets, tested functions, actual approvals, actual media, next step and GO/CONDITIONAL GO/NO-GO by stage. “Ready instructions” never implies “finished accurate video”.

## 3. Instruments and who supplies them
| Instrument | Use / boundary |
|---|---|
| Host LLM + supported file reader | Facts/script/Bibles/prompts/checklists; scripts are optional, source reading errors disclosed. |
| Image generator or existing approved stills | Fictional identities, rooms and composed frames. Choose the available tool; no paid model availability assumed. |
| Voice route | Native renderer audio pilot, recorded actor or actual available Bengali TTS/Vids voiceover. Written labels do not prove a reusable voice. |
| Flow / ordinary Gemini Create video / Vids | Actual operator generation, selected supported settings, original downloads and finite authorized scope. |
| Local ffprobe / viewing/listening | Technical export metadata plus actual full-motion/Bengali review. One does not replace the other. |
| Vids / CapCut / another available editor | Assemble, captions, mix, attribution, final export. No editor automation claimed. |
| Clinical reviewer + owner | Source fidelity, exact script, fictional assets/voice, representative pilots, scoped spend and final release; bundle related decisions. |

No compulsory premium tool, custom API, cloud server, voice clone or video-agent installation is introduced. Record the actually available instrument, not the most powerful advertised feature.

## 4. Reusable prompt sequence
Use the existing detailed `PROMPT_TEMPLATES.md` together with these additions; fill all placeholders before calling a card render-ready.

**Intake/full-pack invocation:**
```text
Use this full Skill package with the actual original case below.
Selected route: {{ROUTE}}, requested total {{SECONDS}}s, aspect {{ASPECT}}.
Produce ALL outputs listed in FULL_PRODUCTION_PACK.md, including missing-asset
prompts and every per-clip DRAFT card. Map spoken and visible medical claims
to source facts; distinguish source demographics from fictional staging.
Do not invent findings, investigations, arteries, diagnoses or outcomes.
List actual available inputs and missing dependencies. Do not generate paid
media or publish as part of this planning request. Case: {{ORIGINAL_CASE}}
```

**Master image instruction:**
```text
Create only the missing {{CHARACTER_OR_ROOM_ID}} master described in the
reviewed Bible. Source demographics: {{SOURCE_FACTS_OR_UNKNOWN}}.
Fictional visual choices: {{REVIEWED_APPEARANCE_WARDROBE_OR_LAYOUT}}.
Actual attached references/roles: {{FILENAMES_ROLES}}.
Keep STYLE_ONLY separate from identity. Output {{ASPECT}}, selected 2D style,
natural anatomy, no invented clinical equipment/findings/text/logos.
Do not change or regenerate an already approved original.
```

**Composed shot keyframe instruction:**
```text
Compose {{CLIP_ID}} from the attached original approved identity/room/style
masters. Repeat immutable character descriptions: {{FULL_DESCRIPTIONS}}.
Place {{VISIBLE_CAST}} in {{EXACT_LAYOUT_POSES}}, camera {{AXIS_FRAMING}}.
Intended speaker {{SPEAKER}}, others silent in the later video. Physical action
must be supported by {{VISUAL_FACT_IDS}} or harmless reviewed staging.
No patient scan, vessel label, procedure or equipment finding beyond evidence.
Return one still for review; a generated still is not an approved asset.
```

**Audio instruction:**
```text
Use the actual selected {{ACTOR_PROVIDER_PRESET_IF_OBSERVED}} for {{SPEAKER}}.
Exact Bengali: {{APPROVED_LINE}}. Delivery/pronunciation: {{FIXED_PROFILE}}.
Natural pace; do not omit words or speed up to force a fit. Produce a separate
master line if this route supports it; measure the real spoken interval.
If only native video audio is possible, label timing UNTESTED and prepare
only the scoped pilot exception, not a preflight PASS.
```

**Render card:** use the selected platform contract, immutable expanded identity, actual attachments, exact line, one speaker and specific action. Native Gemini/Vids output does not inherit Flow preset names. A silent-visual job must explicitly request no speech and place its exact external line in the audio ledger, not simultaneously request speech.

**Clip QA:** compare the entire actual output to source/script/master/voice; report clinical, identity, voice/Bengali, room/style, anatomy/action, timing and continuity separately. Record first/last spoken word timecodes; accept only authentic human receipts. Probe cannot certify words/identity.

**Assembly:** order accepted exports from the manifest, straight cuts for simple exact totals, captions from actual speech, source attribution inside allocated slots, music below speech. Overlaps change runtime. Measure and review final export. Existing pilot approval is not full-film/public-release permission.

## 5. Minimize unnecessary effort
Freeze the source/script and visual choices before expensive work. Reuse adequate approved masters/frames; create extra angles/sets only for a demonstrated need. Pilot patient, doctor and a repeat speaker in separate jobs before bulk on a new renderer/reference route; reuse slots from the final manifest. New location/action/cast requires targeted coverage only when used. Preserve existing scoped Flow approvals.

Start x1. Stop on critical medical/identity error. Same failure class after two attempts triggers dependency/route review whether or not consecutive; use finite authorized budgets, no automatic unlimited retries. Record active handling/QA separately from wall-clock waits and actual charged units separately from historic quotes/subscriptions. Compare accepted distinct seconds; no first-pass or speed percentage without denominators. Native voice fallback to external audio adds editing/lip-sync work until actually tested.

## 6. Resume and version
After each review/export update the checkpoint and dependency versions. A changed fact/line/reference/settings invalidates only affected current QA while preserving old files/receipts. Source author, package writer and approving clinician are distinct. Consult Case14 process reference only for continuation/regression or explicit explanation; never use its clinical facts as defaults for a new case.
