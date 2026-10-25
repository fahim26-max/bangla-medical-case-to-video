# Case intake & evidence register template

## Input (read first)
- CASE_ID / provisional title / original language / source supplied / author as shown / original publication link when available / retrieval date if actually opened
- Audience: clinical trainees by default; adapt to patients when asked
- Duration 120s default; output language Bangladeshi Bengali; English clinical terms permitted
- Patient consent/privacy: make character fictional; remove names, unique institutions, dates, image identifiers unless explicit public and consent-backed use
- Case chronology: time-since-onset; symptoms and negatives; first consultation and actual actions; later consultations; exam signs; test names/results; working diagnoses; definitive confirmatory evidence; specialist interpretation; treatment/outcome

## Facts table — must fill; never guess
| ID | Exact claim | Evidence category | Supported by (quote/source) | Safe to narrate? | Notes |
|---|---|---|---|---|---|
| F01 | ... | SUPPORTED / ATTRIBUTED / UNCONFIRMED / DRAMATIZED / EXCLUDED | user case phrase, document page, accessible source URL | YES / ATTRIBUTION_ONLY / NO | ... |

Definitions:
- SUPPORTED = explicitly in supplied reliable case/source (still may need external clinical review)
- ATTRIBUTED = reported opinion or unverified interpretation of named person (say "according to the report")
- UNCONFIRMED = missing, conflicting, incomplete, or clinically dubious; withhold definite voice-over claim
- DRAMATIZED = fictional line/action that doesn't add medical results
- EXCLUDED = unnecessary or inaccurate assertion that must not appear

## Clinical story check
1. Is final diagnosis genuinely established, or a differential/quoted interpretation?
2. Does the named test confirm what the script claims? Normal ECG alone is not ACS exclusion; endoscopic retained food alone is not definitive gastroparesis; and a bruit is a clue, not proof of a particular lesion.
3. Are medical diagrams illustrative, not patient images? Label schematics accordingly.
4. Where missing facts affect scene continuity, represent uncertainty without inventing doctor count, result, or outcome.
5. Release gate: source evidence + medical reviewer approval if clinical teaching is public-facing.

## Output
- `VERIFICATION_STATUS`: SOURCE_ONLY / SOURCE_AND_EXTERNAL / HOLD
- `RELEASE_GATE`: PENDING_CLINICIAN_REVIEW until legitimately reviewed
- `FACT_REGISTER` + supported storyline. Avoid forcing all cases into a diagnosis reveal if unresolved.
