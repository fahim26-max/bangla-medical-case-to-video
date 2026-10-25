# Humanizer composition for Bengali medical-drama production (v2.6.0)

## Purpose and source availability

Use the existing repository's [`humanizer` skill](https://github.com/refat247/medical-cdss-skills/tree/main/humanizer) **only if its instructions are genuinely available/loaded in the current planning host**. It is an older unversioned vendored copy: [humanizer README](https://github.com/refat247/medical-cdss-skills/blob/main/humanizer/README.md) explicitly warns that alignment with `blader/humanizer` v3.1.0 and licensing provenance are not established ([issue #12](https://github.com/refat247/medical-cdss-skills/issues/12)). Do not duplicate or silently execute the sibling skill, assume it is included in this video-skill ZIP, or quote/copy the complete upstream rule catalog.

**Standalone fallback:** even on a phone or when the AI client imports only this video folder/ZIP, apply this original short protocol. `HUMANIZER_SKILL_LOADED` means the actual separate skill instructions were accessible and used; otherwise use `HUMANIZER_FALLBACK_APPLIED`. If no editorial step was performed, use `NOT_RUN`. These are preparation states, not measured proof of naturalness.

## What is editable

| Category | Scope | Editorial permission |
|---|---|---|
| Dramatized patient–doctor **dialogue** | Fictional/creative spoken bridges mapped to actual source facts | **EDIT** for believable Bangladeshi Bengali, short natural sentences and stable patient/doctor register; do not alter clinical meaning or invented facts |
| Non-spoken screenplay description | Scene beats, transitions, emotional cues where justified by source | **EDIT** to remove generic, melodramatic AI filler; avoid unsupported emotions or clinical actions |
| Human-facing instructions | `05_jobs/OPERATOR_STEPS_v001.md`, mobile/Windows runbooks, QA explanations | **EDIT** for concise action-focused Bangla and technical English terms where essential |
| Titles/hooks | Proposed title and human-facing video description | **EDIT** only if source-grounded, appropriately attributed and consistent with reviewed clinical claims |
| Original medical source | Direct quotes, demographic/case history, original chronology, supporting guideline passages | **LOCK**; no paraphrasing in the evidentiary record |
| Clinical contracts | FACT_REGISTER, fact/source IDs, exact numbers/dose/unit, positive/negative findings, diagnosis certainty, `HOLD`, risk disclosures, consent/attribution | **LOCK**; stylistic rewrite cannot change or obscure clinical facts |
| Renderer/asset contracts | JSON/schema/field names, reference IDs, filename/hash, immutable character/voice blocks, negative constraints, camera/conditioning instructions, model/mode/quote | **LOCK**; humanizer must not touch structured technical inputs |
| Already approved outputs | Signed-off exact dialogue, associated audio timings, generated videos, receipts and release decisions | **LOCK** until a new approved version is explicitly opened |

**Important distinction:** a patient line created as a dramatised explanation can be made conversational, but direct source quotations must remain verbatim. Medical facts that the character speaks must stay clinically identical; changing meaning, certainty or medication dosing is prohibited. The **Final script** should have *one exact approved line per clip*, not a separate unmatched 'humanized' script.

## Execution order

1. **Source and clinical truth first:** read case, de-identify, preserve original quotes, create FACT_REGISTER with uncertainty and evidence IDs.
2. **Source-linked first draft:** generate screenplay and each clip's preliminary spoken/visual facts; record original language and the editable-vs-protected status.
3. **Constrained editorial pass:** if the existing `humanizer` is loaded, apply its prose guidance **subject to these stronger medical locks**. Otherwise apply fallback: use everyday Bangladeshi Bengali for the patient and concise professional Bengali for clinician; avoid invented sentiment, robotic transitions, high-flown summaries and predictable three-part clichés. Use simple questions, believable pauses and rhythm; do not overdo colloquial slang. Keep proper medical terminology explained where source supports explanation.
4. **Post-edit source audit:** compare each revised spoken clinical assertion to source fact IDs, speaker, confidence/unknowns, timeline, medication/dose/units and consent. Reject any new test, certainty, treatment, emotion or statement lacking evidence.
5. **Dialogue timing:** compare 8-second or 10-second clip limits and actual speech tests; a wording change may invalidate recorded audio duration. If audio not observed, `AUDIO_UNTESTED`; do not pretend word-count estimates are measured.
6. **Freeze reviewed final:** submit the final revised script for owner and, where needed, clinician approval. **Only then** place that identical line in the canonical production JSON, screenplay and every standalone clip card; reflect new hashes/contracts. If a previously approved line changes, retain old file/receipt and issue a new version with affected clip/audio/QA stale.
7. **Producer comprehension pass:** write the user-visible instructions in accessible Bangla with explicit action/object/expected output and one step at a time. Separate mobile copy/attach/save/QA from optional Windows local QC. Keep actual unavailable controls and `HOLD` visible; do not invent Flow/Gemini UI menu names.
8. **Audit → repair → re-audit:** produce `07_qa/HUMANIZER_REVIEW_v001.md` or equivalent chat summary. No claim of a completed pass without comparing actual text against the source.

## Reusable audit note (mobile-friendly)

```text
CASE_ID / screenplay_version: [...]
Editing engine: HUMANIZER_SKILL_LOADED / HUMANIZER_FALLBACK_APPLIED / NOT_RUN
Editable lines / scene descriptions changed: [clip IDs or NONE]
Source quotations preserved: PASS / FAIL / NOT_TESTED
Clinical FACT + VISUAL map unchanged: PASS / FAIL / NOT_TESTED
Medicine, certainty, negatives, dates/numbers preserved: PASS / FAIL / NOT_TESTED
Speaker and one-line-per-clip exact sync: PASS / FAIL / NOT_TESTED
Dialogue audio interval reconfirmed: value+evidence / AUDIO_UNTESTED
Mobile operator instructions clear: PASS / REPAIR / NOT_TESTED
Windows optional CLI properly separated: PASS / REPAIR / NOT_TESTED
Changed downstream approvals/contracts invalidated: list / NONE / UNKNOWN
Human clinical and owner review: PENDING / RECEIPT IDs
Final editorial status: DRAFT / NEEDS_REPAIR / READY_FOR_OWNER_CLINICIAN_REVIEW
```

## Example: preserve meaning, improve voice

**Source-grounded draft claim:** Patient reports nausea after meals. The script may dramatize that report without claiming why the nausea occurs.

- Stilted fictional patient: "খাদ্য গ্রহণের পর আমি ক্রমাগত বমিভাবের অভিজ্ঞতা অর্জন করি।"
- Natural fictional patient: "খাওয়ার পরই আমার বমি বমি লাগে।"

Both must point to the same actually reported symptom FACT ID; if the real source lacks a post-meal relationship, **neither version may assert it**.

**Clinician with an unconfirmed diagnosis:**
- Unsafe: "আপনার এই রোগটা নিশ্চিত হয়েছে।"
- Source-safe: "এখনও নিশ্চিত করে বলা যাচ্ছে না। আরও তথ্য দরকার।"

This correction is **clinical safety**, not a Humanizer style preference; apply it only when source truth actually reflects uncertainty and get clinical review.

## Naturalness and provenance boundaries

- Do not promise that text is undetectable by AI detection services, human-authored, or indistinguishable from a professional actor.
- Do not falsify human authorship, source attribution, patient speech or clinical consent. If a script uses dramatized speech, retain that disclosure.
- This is a prose-editing method, not a language model API, an executable code dependency, a Bengali-language speech generator, a real linguistic audition or an automated film.
- The raw `humanizer` wording is not bundled into this package; source references stay links. No new network dependency or proprietary font is required.
