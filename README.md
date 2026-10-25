# Bengali Medical Case-to-Video

**Version:** 2.7.0

যেকোনো accessible medical case history থেকে source-grounded Bengali patient–doctor drama-এর complete production instructions তৈরি করুন। Accuracy → time → effective accepted-output cost। Default120s,15×8s,16:9,semi-realistic2D; confirmed10s routes use12×10s।

## Start

Import the complete folder/ZIP with root `SKILL.md`, not a loose instruction excerpt. In ChatGPT/Codex select this skill; in Gemini import the complete package where supported, then test activation in a normal planning chat. Gemini Skills currently cannot invoke Create video. Flow and Google Vids consume the generated operator instructions; installation in those apps is not supplied.

Paste: **“এই original case থেকে full production pack তৈরি করো। Route: Flow [বা Gemini / Google Vids]। Clinical facts বানাবে না। All script, character/voice/environment specifications, asset/keyframe prompts, per-clip cards, operator steps, QA, cost log ও editing instructions দাও। Missing inputs DRAFT/HOLD রাখো।”** Then supply the original case. No paid generation or publication is authorized by a planning request.

Read [the complete pack procedure](references/FULL_PRODUCTION_PACK.md), [platform routes](references/PLATFORM_ROUTES.md), [attachment/identity gate](references/ATTACHMENT_AND_IDENTITY_GATE.md), and [Case14 process reference](references/CASE14_PRODUCTION_REFERENCE.md). New cases never inherit Case14 people or diagnoses. Existing actual case media stay in their original project; no media binaries/private patient data are embedded here.

## Mobile-first / Windows-enhanced

**Phone only (Android/iPhone/iPad):** provide case text/files through the chat, approve source facts and character/voice/room masters, copy each independent clip card into the *available* Flow/Gemini/Vids UI, download/save originals, review first/middle/last and full video with sound, and record a manual QA checklist. Assemble in a phone-capable editor **only if the exact export/track controls are present**. No terminal, FFmpeg, Python or cloud GPU is required. If clip duration/voice/identity cannot be established, mark the relevant gate NOT_TESTED/HOLD rather than claiming completion. See [device runbooks](references/DEVICE_WORKFLOWS.md).

**Windows PC/laptop:** same clinical/visual gates, with optional ffprobe/FFmpeg duration/audio/black/freeze checks, video contact sheets, structured logs and local editor/FFmpeg assembly. FFmpeg-based QA is **technical only**, never a clinical/voice/identity approval, and remains optional. You can start on phone and continue on Windows without regenerating accepted media; preserve the actual files, versioned references and manifest. See [continuity playbook](references/CONTINUITY_PLAYBOOK.md), [Bengali audio options](references/BENGALI_AUDIO_PLAYBOOK.md) and [bounded tests](references/EXPERIMENT_PROTOCOLS.md).

## Reference and account preflight (v2.5.1)

Before spending credits, inspect [conditioning compatibility](references/CONDITIONING_COMPATIBILITY.md), fill the [canonical reference packet](references/REFERENCE_PACKET_TEMPLATE.md), and record the actual selected Jio promotional account's UI/device controls in [account capability matrix](references/JIO_ACCOUNT_CAPABILITY_MATRIX.md). **Documented ≠ available in your account ≠ successfully tested.** The selected model/route decides whether Frames, Ingredients, reference images, saved Character and saved Voice controls coexist; do not treat a Vertex/Veo API restriction as universal Flow/Gemini UI behavior. Mobile and Windows have the same preflight and clinical gates; Windows FFmpeg is optional.

## Bengali natural-language pass for the whole production package

The existing [humanizer](../humanizer/SKILL.md) is reused **when loaded in the AI client**; its GitHub presence alone does not activate it. The video skill also carries a short self-contained [Humanizer composition and clinical-safety protocol](references/HUMANIZER_COMPOSITION.md) so the importable single-skill ZIP still works on mobile and Windows. It improves **dramatized dialogue** (conversational, accurate Bangladesh Bengali) and **operator instructions** (short plain Bangla steps with English technical labels). It does **not** rewrite the original case, medical findings, precise quotes, data schema, approved lines or image/voice prompt locks.

The source-faithfulness and clinical audit runs **again after** the rewrite; changes in dialogue may affect actual audio timing, clip contracts and earlier approvals. The final package must contain one canonical version of each exact spoken line, plus an audit note identifying any text pass or fallback. The technique improves naturalness but cannot guarantee that AI authorship is undetectable.

## Audience attention without clinical sensationalism (v2.7.0)

Every new production pack includes **three source-grounded first-three-second hook proposals** and a case-adaptive **15-clip retention beat map** (or the correct observed 10s profile). Only **one** hook/line is approved and copied unchanged into screenplay, canonical JSON and standalone clip cards. The humanizer edits dramatized Bengali prose before clinical re-audit; hook writing cannot change medical certainty, quote source patients without evidence, or imply undisclosed test results. No viral prediction or guaranteed completion claims.

The producer receives a zero-credit [hook comparison / safety protocol](references/RETENTION_HOOKS.md), [clip-by-clip beat map](references/RETENTION_BEAT_MAP.md), [clinical safety rejects](references/HOOK_CLINICAL_SAFETY.md), and [post-publication analytics ledger](references/RETENTION_ANALYTICS.md). Mobile can review manually; Windows analytics analysis is optional and has no new FFmpeg/GPU/Python dependency. On-screen captions for sound-off discovery are **editor-only and optional**: maintain original STYLE01 video-generation no-generated-text rule. A proposed 9:16 vertical cut is **not** evidence that the 16:9 master was safely cropped.

## Local helpers, optional

```bash
python scripts/new_case.py --case-id CASE-EXAMPLE --source case.txt --output-root cases --profile FLOW_8S
python scripts/validate_package.py cases/CASE-EXAMPLE/01_evidence/production_package_v001.json --stage plan
python scripts/preflight_handoff.py cases/CASE-EXAMPLE/05_jobs/handoff_v001.json
python scripts/check_gemini_export.py returned.mp4 --seconds 10 --audio-route NATIVE
python scripts/qc_media.py returned.mp4 --expected-seconds 8 --audio-route NATIVE
python scripts/make_contact_sheet.py --canon approved_canon.png --output continuity.jpg clip01.mp4 clip02.mp4
python -m unittest discover -s tests -p 'test_*.py'
```

The starter preserves source bytes and produces INTAKE templates, not invented facts or an already complete screenplay. The production validator uses `jsonschema` from `requirements.txt`; the starter/handoff checker use Python standard library. Export probing additionally needs installed ffprobe. No helper is a Flow/Gemini/Vids API, no API key is required, and no app integration is assumed. Helpers are optional in text-only hosts; disclose unavailable execution and perform a labelled manual preflight.

## Package and maintenance

`SKILL.md` routes instructions; `references/` holds clinical/production contracts; `assets/CASE_STARTER/` contains editable case templates; `scripts/` holds local checks; `tests/` holds synthetic regressions; `agents/openai.yaml` and `assets/icon.svg` hold UI metadata. Preserve historical changelog/Git versions; bump optional capabilities with a SemVer minor and align current declarations only. [Release alignment](references/RELEASE_ALIGNMENT.md). [Current audit and validation](references/VALIDATION_v2.7.0.md).

Status: preparation tools and scoped tests are distinct from installation, runtime activation, actual media quality, GitHub merge and release. Human clinical/script, real reference/voice, pilot and final-film decisions remain necessary. Credits, timing and profit remain UNKNOWN until measured. Do not interpret unit-test success as clinical approval or complete-film validation.
