# Medical truth overrides attention heuristics — v2.7.0

## Hard clinical stop
Reject any hook, title, thumbnail, sound or subtitle that introduces or implies a patient-specific fact absent from source. This includes doctor/test counts, prior 'normal' scans or negative findings, hospital transfers, stated diagnosis, outcome, death, medication efficacy, inferred emotions, a clinician quotation or a causal link without evidence. **A fictionalized appearance/bridging sentence is not permission to invent medical data.**

Reject false emergency urgency, fearbait, miracle cures, selective edited context that reverses clinical certainty, deliberately withheld urgent safety information, disrespectful reenactments or exploitative use of identifiable patient tragedy. On-screen 'micro-proof' must point to an actual reviewed source fact; never synthesize medical scans/screenshots to make a hook look credible.

## Verdict logic

```text
If source missing/unreadable -> HOOK_SOURCE_HOLD, no factual hook publication.
If any material factual or visible claim lacks FACT/visual ID -> CLINICAL_HOLD.
If claim implies a definitive disease while source only has differential -> CLINICAL_HOLD.
If claims about urgency/risk are unsupported or exaggerated -> REJECT.
If the title/thumbnail promises something the story cannot answer -> REWRITE.
If unsupported images/equipment appear in first frame -> REPAIR.
If exact approved dialogue has changed -> NEW_VERSION_AND_REVIEW; no silent reuse.
Else -> EDITORIAL_DRAFT_ELIGIBLE (NOT permission to render or publish).
```

## Grok report audit (2026-10-22)

The report labelled five generic hooks 'safe fictional examples'. **They are NOT generically safe templates**: 'not kidney disease', 'three doctors', 'a correct test', 'three months', 'diagnosis clear', and 'this is the disease' each imply case-specific clinical facts or actual participant statements. Use only when facts/consent demonstrate the exact claim. No default evidence is granted by being called a fictional example.

X source correction: Grok's submitted text omitted a direct post URL, but an independent lookup located the creator's [3 November 2025 public X post](https://x.com/danielhangan_/status/1985397722363412826) (also reproduced by [SuperX public mirror](https://superx.so/creators/danielhangan_)). The **post and self-reported 10,114-video claim exist**, but raw data, sample selection, analytical method and claimed efficacy were NOT independently verified. Tag `CREATOR_CLAIM_POST_FOUND_DATA_UNVERIFIED`; never convert the claimed result into a medical/viral performance benchmark. Repo `hookscore.py` thresholds, virality scores and isolated community reports are heuristics, not validated clinical communication outcomes.

## Clinical quality and audiences
Audience categories matter: patient/public versus clinician/medical trainee. Avoid unexplained jargon in public copy; do not distort medical uncertainty for either. No title/thumbnail implies individual diagnosis from educational dramatization. Use attribution and necessary disclosures in editorial package without forcing a full legal disclaimer into a 3-second video hook.

The right result may be a **quieter truthful opening**. A case with no dramatic reveal can still be useful; do not pad it with fabricated clinical progression to satisfy a fixed retention recipe.
