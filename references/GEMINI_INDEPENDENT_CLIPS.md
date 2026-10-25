# Gemini Apps independent clips — optional v2.3 profile

## Contents
1. Evidence; 2. Planner and renderer handoff; 3. References and isolation; 4. Job card; 5. QA and recovery; 6. Editing; 7. Limits.

## 1. Evidence, not universal promises
Owner report in this conversation, 2026-10-21 Asia/Dhaka: Gemini renders fixed 10s clips on their account and feels faster than Flow. Asking for subsequent segments in the same conversation yielded accumulated 20/30/40s outputs; beyond about 40s the owner saw missing dialogue/story events, failed extension and age/sex/identity drift. Classify this as USER-REPORTED observation. The underlying exports, settings, timings and latency comparison were not inspected for this report. Do not invent a universal 40s technical ceiling, a 10s limit for every account/model, or a proven cause such as context exhaustion. Cumulative editing is one plausible interaction interpretation, not an established diagnosis of the failure.

Official Google help checked 2026-10-21 documents Gemini video creation, conversational video editing, image references, and downloads. It currently excludes Create video from Gemini Skills. Sources:
- https://support.google.com/gemini/answer/16126339?hl=en
- https://support.google.com/gemini/answer/18560919?hl=en
- https://support.google.com/gemini/answer/17094296?hl=en

Use profile `GEMINI_APP_INDEPENDENT_10S` only when the current operator confirms that unit for the selected account/model. Default for a NEW 120s Gemini project: 12x10s, one independent export per job. This is an explicit alternate profile; retain default Flow 15x8s. If actual supported duration changes, recompute the timeline and get the changed script reviewed. Never create 15x10=150s while claiming 120s. Never stretch, relabel or replace approved Case14 C01/C09 8s pilots. A Case14 Gemini derivative needs its own namespace, e.g. CASE14-GEMINI10, new 12-row screenplay and fresh pilot coverage; it inherits no Flow media/voice approvals by implication.

## 2. Planner and renderer are separate surfaces
In the planning chat, use this skill with the original case. Produce facts/uncertainties, the reviewed 12-row screenplay, case-specific Bibles, approved still dependencies and a complete per-clip render job card. Keep missing information and approval status explicit. Produce cards as DRAFT when dependencies remain missing; do not call them executable/approved.

For actual generation, the operator opens an ordinary Gemini Create video conversation and pastes ONE self-contained card with its actual attached images. Do not invoke the skill as an executable video action. A SKILL.md uploaded as ordinary source material is not proof of native skill installation. Do not rely on the video chat retrieving the planning chat, the full original case, a Library link, a local filesystem path or an internal asset ID. The job card must expand the relevant identity, setting, style, exact line and action in plain text, with actual files attached by the user.

The existing production.schema.json supports arbitrary consistent clip counts/durations. Use 12 rows with start/end 0-10 ... 110-120 for this profile. Keep the schema version compatible with the existing v2.2 data contract. The bundled validate_package.py is local structural checking and Flow-oriented spending/readiness checks; it is not a Gemini quota/controller integration. Use its plan check for a Gemini package and document operator capability/quota authorization separately. Do not use its Flow-credit READY result to claim Gemini render authorization. No video generation, automatic new-chat control, downloading or CapCut execution is supplied by the skill.

## 3. Independent context, frozen references
For each job, start a fresh video creation conversation/session. This is a proposed mitigation to test, not proof of isolation enforced by the model. Do not upload a previous MP4, click Extend/Continue/Edit for another clip, or ask for 'the next ten seconds of that video'. Do not paste the full 120s script into the rendering conversation. Earlier conversation content must not be the identity source.

Attach the approved composite keyframe for THIS shot. If current UI permits useful additional images, attach the original patient/doctor identity masters and environment/style references within the available limit. The checked official page permits up to five images; recheck actual UI instead of assuming every reference mechanism or attachment type is available. Prefer one correctly composed frame over an arbitrary collage of faces/rooms. Label each actual file's role; STYLE_ONLY is not identity. An image reference improves the intended starting condition; it cannot guarantee exact motion/frame enforcement or zero identity drift.

Each card carries a compact immutable contract: apparent/source-supported age, source-supported sex/presentation where supplied, fictional face/hair/facial hair, body proportions, wardrobe variant, visible cast, one speaker, muted cast, setting layout, camera axis, props, lighting, style. Distinguish source demographics from fictional visual choices. Repeat the same exact relevant descriptions on every card; 'same person as before' is insufficient. Scene changes are intentional manifest changes, not silent room substitutions. New cases do not inherit Case14 people or presets.

For native voices, repeat the same chosen delivery profile and pronunciation, but mark cross-clip identity UNVERIFIED until compared with the actual approved sample. Do not assume Flow presets such as Algenib/Charon, custom voice storage, audio-reference import or cloning exist in Gemini's video UI. Only claim a setting after observing it there. If native identity drifts, pilot silent visuals plus one external approved actor/TTS profile per speaker; external audio and lip sync remain separate work, not an automatic guarantee. A fresh chat may improve context separation while making voice identity harder; test both.

## 4. Self-contained render job card (fill every placeholder)
Keep planning metadata outside the spoken line. Technical names and IDs are labels for the producer, not file-import commands. No placeholder may remain in a card presented as ready for rendering.

```text
NEW INDEPENDENT VIDEO — render this single shot only.
Project: {{CASE_ID}}. Clip: {{CLIP_ID}}. Prompt revision: {{VERSION}}.
Requested output: ONE standalone 10-second video, 16:9.
This job does not extend, replay, summarize, concatenate or modify another video.
Do not include earlier/later clips, a recap, an intro or an outro.

Actual attached images and roles:
{{KEYFRAME_FILENAME}} = approved shot composition.
{{IDENTITY_REFERENCE_FILENAMES_AND_ROLES}}.
{{ENVIRONMENT_AND_STYLE_REFERENCE_FILENAMES_AND_ROLES}}.

Fixed visible characters: {{FULL_IDENTITY_AND_WARDROBE_DESCRIPTIONS}}.
Only {{SPEAKER_DESCRIPTION}} speaks. {{OTHER_VISIBLE_CAST}} stay silent.
Environment and camera axis: {{FIXED_LAYOUT_LIGHT_PROPS}}.
Art style: {{STYLE_CONTRACT}}.
Action and camera for THIS shot: {{ACTION_CAMERA_START_END_POSE}}.

Exact Bangladeshi Bengali dialogue, with no other words:
“{{ONE_APPROVED_BENGALI_LINE}}”
Voice delivery: {{PROFILE_AND_PRONUNCIATION}}.
Use a natural pace with brief silent head/tail room. Spoken target <=8.5s;
actual speech duration and wording will be checked after export.
If the line cannot fit, report the limitation; do not omit or rewrite it silently.

No age/face/sex/wardrobe drift, extra people or voices, invented clinical facts,
new diagnoses/tests/outcomes, incidental text/subtitles/logos, style changes,
or impossible anatomy/equipment actions. Do not assume an absent voice control exists.
Return this shot as a separate output. Final joining will occur in an external editor.
```

Do not instruct the video model to burn the requested output filename into the image. The operator downloads and names it `CASE_ID_C01_GEMINI_TAKE001_v001.mp4` after checking what was actually returned. Record selected UI/model where exposed; otherwise mark unknown. For silent visuals replace the native line with an explicit silent-action card and preserve the exact line in the external-audio ledger; do not request both silence and speech at once.

## 5. Pilot, QA, stop and recovery
First test one patient-speaking and one doctor-speaking job, each in its own fresh video conversation. Before bulk generation, make an additional independent job with the SAME speaker and approved references, also in a fresh conversation. The additional job tests between-conversation face/age/voice consistency that the two-speaker pilot alone cannot establish. Use an existing planned scene from the 12-row manifest; do not add a thirteenth content slot. New locations/voices/cast still require coverage under the universal workflow.

Download each original export separately. Probe actual duration/aspect/audio streams and compare the entire clip with the exact line and references. For 10s jobs, 20/30/40/50s accumulated exports FAIL the unit contract. Do not fix an accumulated clip by blindly trimming its last ten seconds: content may have been rewritten, omitted or recapped. Restart one isolated job from original masters. If a ten-second export still contains recap or dropped dialogue, it also FAILS despite a technical duration pass.

Use `python scripts/check_gemini_export.py VIDEO.mp4 --seconds 10 --aspect 16:9 --audio-route NATIVE` for a local technical check where ffprobe is available. The checker cannot judge speech span, literal Bengali, number of voices, age/sex/identity, clinical content or whether the model edited an earlier video. Those require actual full viewing/listening and QA receipts. Do not approve media from ffprobe alone.

Measure the first-to-last spoken-word interval including internal pauses; target <=8.5s for this profile. This is a conservative production target, not a measured capacity guarantee. If too long, shorten the approved line in the planning package, version it and re-review the changed wording; never force accelerated or truncated speech. External master audio must be measured before video. Native audio without a separate preflight export uses the existing explicitly authorized pilot-test exception; speech QA is NOT_TESTED until the actual return is reviewed.

On age/sex/face/room change, reject the take and return to the original approved masters/keyframe. Do not accept the bad take as a new identity reference or iteratively edit the drifting accumulated video. On repeated independent-output refusal, voice drift or missing dialogue after two attempts of the same failure class, stop that route, preserve failures and use a controlled fallback (Flow with real selected references, or tested external audio). Neither fallback inherits Gemini approvals. Keep unknown latency/cost/quota unknown; compare elapsed time and effective accepted-output cost only after measurement.

## 6. CapCut / other external assembly
Maintain separate approved exports, order C01-C12, use straight cuts for a simple 12x10=120s timeline. Place titles, source attribution and disclaimer inside those slots. Overlap transitions shorten the timeline unless explicitly compensated. Do not ask Gemini to join the clips. Add captions from the approved actual speech, music below dialogue, and review lip sync, volume, meaning and continuity. Measure the final exported file; summed intended slot durations do not prove actual final runtime. CapCut operations and final quality are not verified by an edit plan.

## 7. Explicit limits
Read CAPABILITY_LIMITS.md and return the relevant limits at the end of each proposed production plan. This profile is PLANNED/LOCALLY_TESTED for documents/checks; it is NOT empirically proven against the user's Gemini exports or installed in their Gemini account by this update. Never promise that a prompt can lock a face, voice, scene or exact duration with 100% reliability.

## Dated evidence addendum,21October2026
Official https://ai.google.dev/gemini-api/docs/omni documents Omni1.1 extensions in10s steps up to40s total with last10s context. This scoped model/API fact does not establish the selected app/account model or the cause of owner-reported identity drift. Preserve the original observation as USER-REPORTED; do not promote it into a universal Gemini limit.
