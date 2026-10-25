# v2.5.1 scoped gap patch — validation ledger (2026-10-22)

**Base:** main v2.5.0, merged PR #30, commit 52968bce5a3fb02c26e9a41f756132c08fe50573.
**Reason:** Grok gap review identifies missing explicit conditioning-mode exclusivity, exact canon/reference template and a per-account/per-device Jio capability matrix.
**Change class:** SemVer PATCH. This tightens documentation/preflight for existing capabilities; no backward-incompatible schema or runtime engine feature is added.

## Before writing
- [x] Inspect current main and Version Manager SemVer rules.
- [x] Review Google official Veo/Vertex REST field constraints vs Gemini Omni start-frame/reference example.
- [x] Review existing device, continuity and account caveat docs.
- [x] Avoid unsupported global 'first/last + Ingredients incompatible' rule.

## After writing / independent QA
- [ ] Verify GitHub diff scope remains `bangla-medical-case-to-video/`.
- [ ] Verify SKILL metadata + heading, README, agents YAML and CHANGELOG declarations all 2.5.1.
- [ ] Run GitHub Actions / per-skill synthetic tests at final head and record result.
- [ ] Version Manager inspect/verify on clean checkout.
- [ ] Optional ZIP packaging version/hash integrity from checked-out clean source.
- [ ] Manual mobile/Windows mode/UI inspection on owner's Jio account.
- [ ] Actual native voice/reference/identity pilots authorized and judged after account observation.

**Not changed:** clinical fact register, production schema 2.2.0, private patient files, Case14 master/reference files, C01/C09 approved media and original release provenance.
**Boundary:** documentation and synthetic CI cannot verify consumer app access, Bengali voice continuity, clip fidelity, or final-media clinical correctness. No UI/paid video generation or user login was performed.
