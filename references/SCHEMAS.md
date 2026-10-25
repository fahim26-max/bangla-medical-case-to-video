# Exact storage and schemas

Canonical machine schema: `production.schema.json` (JSON Schema Draft 2020-12; all declared fields required, unknown fields rejected; null explicitly means unavailable/unmeasured). `assets/EMPTY_PACKAGE.json` is the blank record. Do not fill null with guessed IDs, hashes, costs, times, settings or approval names. Use UTF-8; timestamps RFC3339 with offset, user-facing Asia/Dhaka. Preserve original source text as supplied; no hidden rewriting. For redaction retain a private original and a separate redacted derivative plus map, never re-expose identifiers in prompts.

## Directory / filenames
One existing project root, no second Notion/Drive mirror. New case directory `cases/CASE-YYYYMMDD-slug/`:
- `00_sources/`: original bytes with ORIGINAL names, read-only. `source_registry.json` is a generated view of package.sources; do not maintain divergent copies.
- `01_evidence/`: `production_package_v001.json` canonical record (facts, provenance, uncertainty, approvals, capabilities, spend).
- `02_script/`: `CASE_ID_SCREENPLAY_v001.md`, derived human view of exact package dialogue and visual fact IDs.
- `03_bibles/`: `CASE_ID_BIBLES_v001.md` derived view; actual media `CASE_ID_P01_MASTER_v001.png`, `CASE_ID_D01_MASTER_v001.png`, `CASE_ID_ENV01_MASTER_v001.png`, `CASE_ID_STYLE01_MASTER_v001.png`, `CASE_ID_VP01_SAMPLE_v001.wav`.
- `04_keyframes/`: `CASE_ID_C01_KEYFRAME_v001.png`.
- `05_flow/`: `CASE_ID_C01_PROMPT_v001.txt`, exact submitted text; `CASE_ID_C01_SETTINGS_v001.json` represented by clip fields/capabilities/evidence. Do not invent JSON import support in Flow.
- `06_media/`: `CASE_ID_C01_TAKE001_v001.mp4`, `CASE_ID_C01_AUDIO_v001.wav`. Keep every attempt needed for QA. Existing approved files retain actual original filenames and identity; aliases are index entries only.
- `07_qa/`: `CASE_ID_AUDIT_v001.md`, reports derived from package ledger. `CASE_ID_CHECKPOINT_v001.json` contains the schema checkpoint object.
- `08_final/`: `CASE_ID_FINAL_v001.mp4`, `CASE_ID_CAPTIONS_v001.srt`, `CASE_ID_ATTRIBUTION_v001.txt`. Captions use actual speech timing and literal approved lines, not estimated word timing.

JSON IDs: source `CASE_ID:S01`, fact `CASE_ID:F01`, choice `CASE_ID:X01`, asset `CASE_ID:P01:v1`, clip `CASE_ID:C01`; approval `CASE_ID:A001`; capabilities `CASE_ID:CAP01`; attempts `CASE_ID:T001`. Every asset has a version in its ID; new media version needs a new ID. Internal `P01` abbreviations are presentation labels only. Shared style asset requires explicit permission/selection evidence and STYLE_ONLY role; it cannot silently import a patient identity. Asset references are exact IDs, not filenames inferred from visual similarity.

## Field semantics
`meta.author` identifies the package writer; source.author identifies the case author; approval.actor is the real approving person. These are different roles. `quote` must match source text and locator; category describes evidence strength. DRAMATIZED clinical-sounding results are prohibited; put harmless fictional staging in creative_choices with clinical_fact=false. General teaching is GUIDELINE-grounded and distinguished from the patient's recorded events.

`clip.spoken_fact_ids` maps all spoken medical claims and `visual_fact_ids` maps visible clinical implications (ECG, scan, line, injection, operation, apparatus). `creative_choice_ids` maps harmless poses/dialogue bridges. `asset.fact_ids` maps clinical content in diagrams/props. Descriptions cannot bypass the fact register. Null dialogue is not allowed: use empty string with SILENT route for deliberate silence.

`clip.asset_ids` includes all selected references, and `depends_on` tracks frozen versions within assets. Include character/voice/environment/style/keyframe/audio dependencies as applicable. Record selected settings evidence separately from requested prompt settings. `prompt_sha256` hashes literal UTF-8 prompt bytes. Do not claim missing historic prompt text reconstructed from ASR is the original prompt.

`approval_events` is append-only and exact-scope. Missing historical timestamp stays null with its available record locator. New approvals should carry timestamp and exact artifact hash. `qa` lists all seven criteria separately, including timecodes and reviewer evidence; an exception requires an explicit owner receipt scoped to that exact artifact. A changed dependency marks new current QA STALE without modifying old receipts.

`clinical_sha256` binds source/fact/unknown content; `script_sha256` binds the screenplay; `production_sha256` binds all current render contracts and the bounded credit authorization. Each clip's `output_contract_sha256` and its approval receipt's `contract_sha256` must equal the current computed clip contract (prompt, actual model/mode, exact asset versions/settings/dependencies, line and action). `assembly.input_contract_sha256` binds the current production contract and ordered clip export hashes. Recomputing current package hashes does not renew old export approvals. Use `content_hashes`, `clip_contract` and `assembly_contract` in the bundled validator; these produce fingerprints, not evidence of generation.

`render_authorization` stores current quoted credits per x1 output, quote evidence, a finite maximum total credit budget, attempt limit, exact allowed clip IDs and the owner's receipt ID. The receipt must approve the current production hash. Use one conservative quote only when its evidence covers all selected configurations; otherwise split production scopes/configurations and reauthorize. Unknown prior actual charges block new spending until reconciled. Clinician-only approval cannot grant a credit budget. Approved pilots alone cannot authorize full production.

Before bulk rendering, all clinical facts inside referenced assets (including transitive schematic/prop dependencies) require the same safety and review gates as spoken/visual clip facts. A new voice, location, style or visible identity absent from approved pilots requires a targeted pilot. Add its clip ID to the pilot set and obtain its scoped render authorization; do not silently treat reference approval as successful generated-media coverage. With no `--clip`, render readiness checks the aggregate cost of the selected output set, not one output's quote repeated against the same balance.

Historical receipts may retain null unrecovered fields in the project evidence archive. Current operational receipts used to authorize rendering/release require a real actor, timestamp and evidence reference. An archival approval remains historically valid; it cannot be used to pretend a missing contemporary acceptance measurement exists.

## Validator boundaries
`python scripts/validate_package.py PACKAGE.json --stage plan` validates schema, timelines, IDs, references, quote linkage, speaker/audio consistency, dependency cycles and cross-case leakage. It reports stage readiness separately. `--stage render --clip CASE_ID:Cxx` adds source/clinical/script/asset/settings/pilot/production gates for that one clip. `--stage release` also requires actual exports, seven-criterion reviews, final assembly and release sign-off. Use local `jsonschema`; if absent report inability or install the dependency through the host's permitted dependency route. This local validator is not a Flow API or proof that Gemini can execute scripts.

The validator cannot recognize every hidden clinical claim in prose/pixels, authenticate owner approval, judge Bengali/voice quality, or verify that a UI selection actually occurred. These require source review and actual human/media evidence. A structurally valid draft may correctly be render BLOCKED.

## v2.3 compatibility
The production JSON schema remains the v2.2 data contract; both 15x8 and 12x10 targets are supported when internally consistent. Skill release version 2.3.0 does not force schema_version changes or rewrite historical JSON. For Gemini use the plan checker and documented operator capability/quota gates; existing Flow-credit readiness checks are not a Gemini controller.

## v2.4 additive compatibility
Keep production schema_version2.2.0 and its receipts/validators. Companion handoff_schema_version1.0.0 is separately defined in ATTACHMENT_AND_IDENTITY_GATE.md and checked by preflight_handoff.py. It compares declared immutable identities/attachment inspection without granting render permission. new_case.py produces an INTAKE scaffold: empty facts/clips are not a completed valid plan. Vids/Gemini use local plan checks plus documented operator quota/approval gates, not the Flow-credit READY result.
