# v2.7.0 Hook & Retention Layer — validation ledger (2026-10-22)

**Base:** canonical `main` commit `514611493d45cf8b70d493b9b3b711ba7a32c8d1`, skill v2.6.0. Both prior PR #31 and #32 confirmed merged before this scoped change.
**SemVer:** MINOR, compatible new hook/retention planning deliverables. Canonical production JSON schema remains **v2.2.0**. No runtime provider feature or Python dependency required.

## Evidence grades and corrections
- Google/YouTube official: Stayed to watch measures beyond Shorts' *initial seconds* (not a fixed 3-second cutoff); 30-second Intro is separate. YouTube view-count definitions changed 24 August 2026. Instagram 3-second skip rate is reported; availability/ranking impact must be verified, not presumed.
- Grok's pasted report omitted its 10,114-video X link; later lookup found the [3 November 2025 creator post](https://x.com/danielhangan_/status/1985397722363412826) (public [SuperX reproduction](https://superx.so/creators/danielhangan_)). **Public claim confirmed, underlying data/method not verified.** Do not infer quantitative success for medical videos. Example hook claims involving kidneys, number of doctors, tests or confirmed diseases are **not source-independent safe**.
- Github first-three-second frameworks are creator design heuristics, not experimentally validated clinical retention predictors. Code/assets from donor repos not copied; conceptual references/licences cited.
- Medical ethics/factual provenance outrank curiosity, scoring and clip pacing.

## Review tasks before merge
- [ ] Diff confined to `bangla-medical-case-to-video/` and existing approved media/Case14 reference untouched.
- [ ] Five current version declarations aligned to 2.7.0, prior tests updated, no schema alteration.
- [ ] GitHub CI unit tests and project QA pass on latest PR head.
- [ ] Local Version Manager `--inspect`/`--verify` on checked-out folder.
- [ ] Manual source-fidelity test with a sparse clinical case; assert unsupported hooks become NO_SOURCE/CLINICAL_HOLD, not creative new diagnoses.
- [ ] Mobile operator dry-run for the 0–3s hook and beat map, Windows optional analytics/QA scenario.
- [ ] Real rendered C01 + complete film + Bangla voice QA **NOT_TESTED** until actual owner-approved media supplied.
- [ ] Actual audience response and performance remain UNKNOWN until content is published with measured insights.

No account access, posting, social analytics, paid generation, new releases or merge is authorized by this research integration request.
