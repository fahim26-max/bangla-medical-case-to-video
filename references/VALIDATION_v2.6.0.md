# v2.6.0 governed Humanizer composition validation ledger

**Baseline:** open draft v2.5.1 PR #31, commit d827731f0cb230eb4ab264805271fe77d93a9714. The v2.5.1 patch is not merged when this change is authored.
**SemVer:** MINOR; add a backward-compatible optional prose-editing composition capability to a case-video production pack. Five current metadata declarations synchronized to 2.6.0 on the stacked branch.
**Scope:** only `bangla-medical-case-to-video/`; no changes to sibling `humanizer`, its NIQS bridge or upstream provenance issue #12.

## Required audit before merging
- [ ] Review v2.5.1 parent PR #31 and merge/resolve it **first**; then re-check this PR diff relative to current `main`.
- [ ] Verify five current version declarations and no version-manager drift.
- [ ] GitHub Actions / repository `qa/check_all.py` and per-skill tests passed for exact final head.
- [ ] Test a synthetic medical case with fixed facts, source quotation, unsupported differential and one dramatized line: only editable line changes; no new clinical claims/units/diagnosis/quote edits.
- [ ] Test one mobile-only and one Windows operator pack in a planning host; ensure instructions are simple and desktop-only CLI stays optional.
- [ ] If claiming separate `humanizer` runtime access, observe actual loaded skill and record host/session; otherwise apply self-contained fallback.
- [ ] New script line audibility, natural Bangladeshi pronunciation and actor performance verified only on real owner-reviewed media. Never promote synthetic text checks to voice/clinical release QA.
- [ ] v2.2.0 production JSON schema, existing approved Case14 C01/C09 and historical file fingerprints unchanged.
- [ ] Optional ZIP export, manual install and fresh-session runtime smoke test separately evidenced before declaring release.

**At authoring:** Documents and regression assertions drafted; clinical/dialogue naturalness performance, actual cross-skill activation, mobile/Windows operator experience, ZIP packaging, generation and publication are **NOT_TESTED**. A passing CI run cannot certify those outcomes.
