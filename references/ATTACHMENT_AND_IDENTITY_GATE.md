# Attachment and identity handoff preflight

Apply to all routes before a card is called self-contained. The Gemini planning rehearsal changed an elderly male into a female and labelled dossier-mentioned images PRESENT without inspecting them. These are demonstrated planning failures; images/voice quality were not rendered. Do not fix this by hardcoding Case14 male/elderly into a universal default.

## Required distinctions
Inventory each asset's exact ID/version, actual filename, role, bytes/hash where available, approval evidence and current host/session access:
- DOCUMENTED_ONLY: mentioned in records; actual media absent.
- LOCAL_AVAILABLE: bytes located; not attached/inspected in target planning chat.
- ATTACHED_UNINSPECTED: attached but no actual inspection evidence.
- INSPECTED_THIS_SESSION: actual file examined in the stated session; record the inspection evidence. This is an attestation, not something a text validator can authenticate.

A Library ID, filename, old chat, screenshot caption or hash in a dossier does not give another AI access. Upload actual stills. In a fresh renderer job reattach actual approved files; planning-chat inspection does not prove rendering-chat attachment. Existing asset approval and suitability for a new shot are separate. Do not copy an accepted export's incidental poster/equipment exceptions to new frames.

## Freeze identities
Record case-scoped character ID, age band, sex/presentation, full approved appearance/wardrobe description, demographic basis and evidence. Source demographics must agree with supplied source; if unknown, label unknown and distinguish reviewed fictional choices. Do not infer a clinical age from an image or invent clothing without reading the reference. Exact physical details not visible stay unknown or require an approved fictional choice.

Expand the same immutable text in every job, including repeat-speaker jobs. Never use “same as G01”, “same as before” or external chat memory as the sole identity/voice/environment definition. A composed approved frame may carry multiple roles; label them without claiming extra files exist. Case14 expected patient is elderly male only within that fixture. A new source-supported female patient must remain female.

## Companion JSON v1.0.0
Use `assets/HANDOFF_TEMPLATE.json`; keep it separate from the unchanged v2.2 production schema. All objects have exactly the keys below; null means unavailable, empty arrays mean not prepared. The local checker enforces these key sets/types and relationships. It is not a replacement clinical or spending authority.

Root: `handoff_schema_version`, `case_id`, `session_id` (string/null), `identity_locks`, `attachments`, `jobs`.

Each identity lock: `character_id`, `age_band`, `sex_presentation`, `description`, `demographic_basis` (SOURCE_SUPPORTED/APPROVED_FICTIONAL/UNKNOWN), `basis_evidence` (string/null), `approval_evidence` (string/null). IDs begin `case_id:`. Text is an immutable specification; evidence/approval strings link real records, not invented sign-offs.

Each attachment: `asset_id`, `filename`, `role` (IDENTITY/SCENE/ENVIRONMENT/STYLE_ONLY/VOICE), `availability`, `inspection_session_id` (string/null), `inspection_evidence` (string/null), `approval_evidence` (string/null), `local_path` (string/null), `sha256` (64 lowercase hex/null).

Each job: `clip_id`, `characters` (objects with `character_id`, `age_band`, `sex_presentation`, `description`), `attachment_asset_ids`, `keyframe_asset_id`, `line_bn`, `line_sha256` (hash of exact UTF-8 line), `prompt_text`. Full descriptions and literal line must appear in the submitted prompt; no unfilled `{{...}}` variables. An intentional silent shot uses empty `line_bn`, SHA256 of empty bytes and an explicit silent action. Jobs must use their own full case-scoped IDs consistently in ledgers.

## Run and interpret
`python scripts/preflight_handoff.py HANDOFF.json` checks declared inventory/identity consistency. Add `--verify-files` only in a local host with actual `local_path` files to compare bytes/hashes. It cannot attach media, certify truthful session inspection, approve clinical content, hear Bengali or authenticate a receipt.

Outputs: structural PASS/FAIL; handoff CHECKED/BLOCKED; render_permission always NOT_GRANTED. Empty jobs/identities/session or missing inspections/approval evidence cause BLOCKED, even if the object structure is valid. A CHECKED handoff still needs the canonical production package's review, supported actual renderer settings, budget scope and real media QA. False ledger entries can defeat a text checker; human/source evidence remains authoritative.

Use the native-audio pilot exception where appropriate: actual timing/voice starts UNTESTED, not a reason to fabricate pre-render audio. Missing references block affected renders but not draft fact/script/asset-prompt preparation. Correct actual dependencies rather than repeatedly asking another AI to restate a report.
