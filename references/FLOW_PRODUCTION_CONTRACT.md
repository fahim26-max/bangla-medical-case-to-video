# Case-independent Google Flow production contract — v2.2

Contract owner: case producer. Clinical authority: identified clinician. Rendering operator: user or separately verified integration. This skill prepares artifacts; no Flow control was demonstrated by the skill.

## Entry contract
Require accessible original case, source quote/fact map, clinically reviewed exact screenplay, owner-approved case-scoped references, approved voice sample/route, exact keyframe, supported current UI settings, intended speaker/mute cast, generation authorization and budget scope. If any is missing, supply a draft with explicit blockers, not a render-ready claim.

Default output: 120s, C01-C15, each 8s, [0,8)...[112,120), 16:9; 720p target when supported; semi-realistic 2D cel shading, controlled contour lines, natural anatomy, soft painted shadows, restrained warm-neutral palette, believable Bangladeshi environments. Patient-first/doctor-later only when the source supports it. Default one speaker per clip; dialogue in natural Bangladeshi Bengali. No unbudgeted title/outro. A source/style portrait controls style only unless its character identity is explicitly selected.

## Operator checklist
1. Open correct account/project. Do not create another copy of approved assets.
2. Confirm model, mode, length, aspect, resolution, x1 output and current credit quote. Record UI evidence and date; do not infer all settings from an exported video.
3. Attach/select the exact approved frame and supported references. Verify voice preset in the actual UI; a mention in prompt is not proof of selection. No fictitious @names.
4. Use standard render prompt below. If using Flow Agent, first request a plan and no generation; inspect its proposed changes and model. Keep its credit confirmation enabled unless the owner explicitly authorizes a bounded automatic run. Published Agent capability is not proof of this project's unattended execution.
5. For a NEW cast, choose patient and clinician pilots by coverage, not fixed clip numbers. Render only authorized pilots. Download exact outputs without replacing originals.
6. Compare against masters and exact Bengali line. Check full motion, speaker, pronunciation/voice, clinical implications, equipment handling, no readable incidental text, actual duration and speech timecodes. Record exceptions with exact output hash.
7. After both pass and production scope is authorized, continue small batches. Stop on critical error; do not repair Case14 approved pilots during this project audit.
8. Assemble with cuts or budgeted transitions. A crossfade overlapping 14 boundaries shortens a simple 15x8 timeline unless compensated within an approved edit plan. Re-measure final export. Add captions/attribution in editor, not generated raster text. Preserve provider provenance watermarks.

## Render prompt template
CASE {{CASE_ID}} / CLIP {{CLIP_ID}} / SCRIPT {{SCRIPT_VERSION}}.
Generate exactly {{DURATION_S}} seconds, {{ASPECT_RATIO}}, {{RESOLUTION}} using the selected {{MODEL}} / {{MODE}}. Output one variation.
Selected approved start frame: {{KEYFRAME_FILENAME}} ({{KEYFRAME_ID}}, {{SHA256}}).
Identity references: {{CHARACTER_ASSETS}}. Environment: {{ENVIRONMENT_ASSET}}. Style: {{STYLE_ASSET}}. Preserve their assigned roles; style reference is not a new character.
Visible cast: {{VISIBLE_CAST}}. One speaking character: {{SPEAKER}}. All other characters: silent, no speaking-mouth movement. Actual selected voice: {{VOICE_PRESET}}. Delivery: {{APPROVED_PERFORMANCE}}.
Exact Bengali speech, no additions: “{{EXACT_BENGALI_DIALOGUE}}”
Action and examination sequence: {{APPROVED_ACTION}}. Camera: {{CAMERA}}. Continuity: {{START_END_POSE}}. Use only facts {{FACT_IDS}} and approved visual claims {{VISUAL_FACT_IDS}}. Do not invent anatomy, test results, diagnoses, treatment or outcome. Any diagrams are illustrative, never patient scans.
Natural pace; speech must finish within the tested {{AUDIO_TARGET_S}} seconds. No narration, extra voices/people, incidental labels/subtitles/logos, new clinical props, face/age/wardrobe drift, photorealism, 3D CGI, exaggerated anime features or implausible equipment handling. For a planned listen-then-explain scene, complete auscultation before speaking and remove earpieces naturally if that action is approved. Do not add an examination the case does not support.

## Silent fallback template
Use the same approved frame/cast/action/settings. No generated speech or lip movements implying dialogue; no new clinical events. External approved audio {{AUDIO_ASSET_ID}} will be added in editor as {{VOICEOVER_OR_TESTED_LIPSYNC_ROUTE}}. Lip sync remains unverified unless a separate returned output passes QA. Pilot this route before batch production.

## Flow Agent planning template
Read the supplied manifest and selected assets. Prepare a proposed per-clip plan only. Do not generate, edit, rename, delete or spend credits yet. List actual model/mode/voice/reference selections you can use, exact missing inputs, current per-output quote and intended x1 count. Preserve approved locked outputs. Do not add facts, voices, people or scenes. Wait for the producer's already-defined pilot/production authorization scope before a credit action. If you cannot bind a supplied ID to a real asset, report the mismatch.

## Current evidence boundary (checked 2026-10-21)
Official Flow help documents model-dependent lengths/reference/voice features and a built-in Agent. User screenshots image(3)/(4) show Omni 1.1 Flash, Frames/Ingredients, 8s, 16:9, 720p, x1 and a 12-credit quote in the Case14 project. image(6) shows Voices including Algenib and Charon. They do not prove the exact final click selections for both successful renders. Their bytes are preserved as existing user source files, not republished screenshots.

Two Case14 exports are USER-APPROVED and independently probed at 8.000s, 1280x720, 24fps with audio. This does not establish stable custom voice storage, 13 remaining clips, final film, current entitlements or Gemini installation. NotebookLM's strict 120s drama approach failed twice and is not the default renderer.

Official sources, retrieved 2026-10-21:
- https://support.google.com/flow/answer/16352836 — model/mode compatibility; check at use time.
- https://support.google.com/flow/answer/17093911 — Flow Agent, project sessions, instructions, credit confirmation.
- https://support.google.com/gemini/answer/18560919 — Skills/Create video boundary.
- https://support.google.com/gemini/answer/17094296 — file/folder/ZIP import rules. Installation on this user's Gemini account is NOT VERIFIED.
