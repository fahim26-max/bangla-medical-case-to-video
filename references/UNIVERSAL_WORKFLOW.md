# Universal workflow and authority — v2.2

## Contents
1. Evidence and states; 2. Phases; 3. Dependency graph; 4. Approvals; 5. Recovery; 6. Costs; 7. Maintenance.

## 1. Evidence and states
Maintain separate fields. `evidence_state` = PLANNED (no execution), TESTED (an attempt occurred), FAILED (observed failure), VERIFIED (specified criterion supported), USER-APPROVED (owner accepted specified artifact). These are not a linear ladder: an approved clip may still have an unmeasured field. Keep `qa_result` PASS/FAIL/NOT_TESTED/EXCEPTION/STALE and `approval_state` PENDING/APPROVED/REJECTED separately. Record the claim's scope, evidence reference, reviewer and timestamp with UTC offset; display times in Asia/Dhaka.

An official help page verifies a documented capability only. Screenshot verifies the shown account UI at that time. An export verifies its media properties; an owner statement verifies that approval. None proves account access today, stable voice cloning, installation, API control, or full-film quality. Never upgrade search snippets or assistant summaries into original clinical sources.

## 2. Phases
| Stage | Automatic work allowed | Exit evidence / human or Flow action |
|---|---|---|
| Case Intake | Read supplied bytes; checksum; de-identify derivative; allocate case ID; list missing source items | Original text/file accessible. Capture consent/rights basis or release HOLD. No optional interview before useful draft. |
| Fact Register | Atomic facts, exact source quotes/locators, chronology, unknowns, exclusions, claim index | Source owner and clinical author retained. Missing result stays null; no diagnostic completion. |
| Clinical Audit | Check internal consistency; verify consequential general claims against primary guidance; flag unsafe implications | Named clinician explicitly approves facts and clinically faithful script scope. Source-only reports stay attributed. |
| Screenplay | Draft 15x8 timeline, single speaker default, exact Bengali lines, visual claim mappings | Owner/clinician approves version/hash. Short sources may use silent actions/pauses; no fabricated event to fill 120s. State insufficiency if meaningful 120s cannot be achieved. |
| Character Bible | New case-specific fictional identity descriptions, wardrobe/pose variants; reuse only explicitly authorized existing assets | Owner approves master identity; source age/sex separated from fictional appearance choices. No default elderly Case14 patient. |
| Voice Bible | Define distinct speaker profiles, pronunciation and native/external route | Owner selects actual available preset and reviews sample. Text labels never prove voice identity. |
| Environment Bible | Fixed layout, light, props, camera axes and STYLE01-only style role | Owner approves references. A generic clinic master is not an ECG/lab/CT/endoscopy suite. Create only needed sublocation variants. |
| Keyframe | Compose one exact scene from frozen identity/environment/style dependencies | Owner approves frame; inspect anatomy/clinical props. Create missing assets only. Never regenerate approved originals just to rename them. |
| Google Flow Manifest | Validate arithmetic, evidence/asset IDs, versions, full prompts, native/external audio plan | Current UI/model/mode/voice/reference combination checked by operator; actual planned credit quote recorded. Unresolved placeholders block render. |
| Pilot QA | Prepare earliest patient and doctor scenes (or two genuinely representative scenes); probe returned exports, compare references, transcript and spoken interval | Human listens to Bengali, compares voices and watches full clips; clinician judges claims/action. Both representative pilots approved before bulk rendering. C01/C09 numbers are Case14-only. |
| Full Production | Prepare eligible prompts and QA one returned clip at a time initially; update ledger | Explicit approved manifest/budget scope before new Flow credit spending. Stop on critical failure. New location or voice uncertainty requires targeted pilot. |
| Final Audit | Assemble locally if actual tools/media permit; test duration, captions, attribution, chronology, levels | Watch/listen complete final film; clinical reviewer + owner release approval. No assumed release permission from pilot approval. |

Native dialogue pilot exception: independent pre-render speech timing can be unavailable. Record `audio_span_s: null` and NOT_TESTED, then test the authorized pilot. Measure first to last spoken word including internal pauses, not container length or non-silent background music. Target <=7s in an 8s clip. Store timecodes/manual reviewer evidence. ASR may assist transcription, never independently certify exact Bengali/voice match. Historical approved pilots with missing exact prompt or timing remain approved as historical files, but their reproduction specification is incomplete. Do not silently use them as fully measured new acceptance examples.

## 3. Dependency graph
Source version/hash -> fact IDs -> clinical approval -> screenplay version/hash -> clip line + visual claims -> character/voice/environment/style -> keyframe -> prompt + actual selected settings -> rendered export -> clip QA/approval -> assembly -> release.

IDs must include case namespace. For assets use CASE_ID:ROLE:vN. Style source may be globally shared only with explicit role `STYLE_ONLY`, never identity inheritance. A clip depends on exact asset versions, not mutable file names. Any fact, line, voice, frame or setting revision creates a new version and marks affected current QA STALE; preserve old export and old approval event. Traverse reverse dependencies and re-audit only affected clips, then full chronology/assembly if it changes. Owner-accepted decor/equipment exceptions are exact-export exceptions, never inherited into a new generation.

## 4. Approval receipts
Use append-only `approval_events`: actor, role, timestamp (null if unrecovered), event evidence locator, exact artifact ID/hash or explicit non-file scope, decision, exceptions and scope. The AI may draft a receipt but cannot invent an owner or clinician sign-off. Approval can cover a complete manifest or asset pack once; no need to ask separately per row when already authorized. Render approval is distinct from technical readiness; a script edit is not permission to spend credits. The current project request authorizes audit, repair and packaging, not new Flow rendering or publication.

Minimum human checkpoints: clinical/script review; fictional master/voice selection; two actual pilot reviews; owner-approved production scope; final release. Bundle related approvals to minimize manual intervention. Silent visuals/external audio is a planned fallback until empirically tested and approved; do not promise lip sync.

## 5. Recovery
| Failure | Resume point and exact action |
|---|---|
| Missing original source | Keep drafts/source summaries labelled DERIVATIVE; request original text/export when available; withhold affected factual prompts. Never fill gaps from memory. |
| Wrong identity or age | Repair master/frame dependency first; retry one target clip, with new attempt/hash. |
| Room/style drift | Compare scene frame to master; tighten permitted changes; new approved frame before one retry. |
| Wrong native voice or clipped Bengali | Verify actual selected preset; shorten/re-test line; if repeat failure, propose external voice and silent visual pilot. No unlimited retries. |
| Medical error | Stop spending; correct fact/claim and script; clinician review; regenerate affected visuals/audio; re-audit returned new file. |
| Mode/account unavailable | Recheck UI; mark prior setting STALE; choose demonstrated supported route and pilot it. Never substitute a model silently. |
| Changed reference | Keep old file; version replacement; compute reverse-dependency invalidation; never overwrite approved media. |
| Interrupted session | Load checkpoint + source/asset inventory and hashes; resume next eligible stage. Prompt-only work cannot imply rendered output. |
| Failed write/conflict | Retain local output and identity/version; report actual error; resolve version conflict rather than create duplicate. |

Checkpoint fields: case_id, package hash, last completed stage, outstanding blockers, next eligible action, selected actual asset/settings evidence, output IDs/hashes, authorization scope, spend ledger, release HOLD. Record a checkpoint after each approval/export; never include secrets.

## 6. Costs
Accuracy first, time second, effective credits per accepted clip third. `credits_per_accepted_clip = actual known credits / accepted distinct clips`; unknown costs remain null. Track quoted versus charged credits, failed attempts and reused approved outputs separately. Screenshots showing 12 credits are historic quotes, not invoices or today's price. Start with x1. Do not authorize x2-x4 variants by accident. Stop after a second failure in the same failure class, diagnose dependencies and seek a changed controlled approach. No extra NotebookLM strict-duration retries for the already failed approach.

## 7. Maintenance
Before each new case, verify only the current features actually required; do not repeat unrelated research. Run regression checks after skill/schema changes, new model/mode, changed voice/reference mechanism or recurrent failure. Keep installation, local validation, Git synchronization, runtime invocation and Flow execution as separate records. Preserve v1.1/v2.0/v2.1 history and add v2.2 evidence without rewriting old verdicts.
