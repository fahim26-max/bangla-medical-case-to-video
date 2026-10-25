# v2.5.0 change-scope / validation ledger — 22 October 2026

## Before change
- Target baseline: main commit 191141f6d452000e521bba18e269d9950f0984bc, skill v2.4.0.
- Read AGENTS.md and existing v2.4.0 production, release, schema, skill and test contracts.
- New user requirement: full phone-only workflow and optional Windows/8 GB RAM features; no mandatory FFmpeg on mobile.

## Scope and explicit boundaries
- Add platform/device-independent clinical/video gating and mobile manual evidence method.
- Add Windows FFmpeg + standard library optional QC/contact-sheet helpers; no mandatory installed provider SDK.
- Continuity/voice research integrated only as rules and bounded tests; external service/saved Character availability remains untested.
- Clinical source text, v2.2.0 production.schema.json, Case14 C01/C09 approved hashes and downstream histories are **not modified**.
- No patient media, paid rendering, UI automation or public release included.

## Verification checklist
- [ ] GitHub diff restricted to `bangla-medical-case-to-video/`.
- [ ] Five current version declarations match 2.5.0: SKILL metadata/heading, README, agents YAML and newest CHANGELOG.
- [ ] `python -m unittest discover -s tests -p 'test_*.py'` (run in checked out skill directory).
- [ ] `python scripts/package_skill.py --output ../bangla-medical-case-to-video-v2.5.0.zip` on a clean checkout with correct version, CRC and hashes (optional release step; don't overwrite existing ZIP).
- [ ] Installed FFmpeg/ffprobe smoke tests with known-good and failure-fixture media.
- [ ] Fresh mobile-device planning and manual-QA walkthrough.
- [ ] Actual current Jio Flow/Gemini/Vids account capability inspection and approved Bengali/identity pilot tests.

**Validation state at authored time:** workflow contracts and synthetic tests authored; no local checkout in this environment, no actual unit tests run, no release ZIP, no real media rendered or approved. CLI tool detection/reporting must be checked in CI/local Windows before promotion. PR review required. Never represent this file as a completed validation receipt.
