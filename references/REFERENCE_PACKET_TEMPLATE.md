# Canonical reference packet — copy into each case (v2.5.1)

**Goal:** Repeat exactly the same approved character description and correctly identified image roles in each independent shot. This is a **portable text form** usable on mobile or Windows. No Python, FFmpeg, generated image, saved Flow object or account feature is created by writing this file.

## Approval/preparation order

1. Read the case FACT_REGISTER first. Use source-supported age, sex and clinical constraints when available; describe fictional nonclinical appearance choices as `DRAMATIZED_NONCLINICAL`. Never claim a patient-specific image/diagnosis exists without a source.
2. Approve **one** neutral front canon still for each fictional recurring character. On difficult side-view shots, derive and approve ¾ and optionally profile/detail stills **from the canon**, not independent fresh character concepts. Avoid copying the entire turnaround composite as a single reference unless the selected provider explicitly supports that format.
3. Separate **identity** references from **style-only** (`STYLE01` where that style is approved for this case) and **environment/location** references. Don't use P01 case-history identity for another patient.
4. Define an immutable verbatim identity block and stable wardrobe version for each character. Voice reference ID is separately approved only when a real asset/control exists.
5. For **each shot**, choose only the reference subset supported by its **specific** selected model/mode. The 1–3 clean-image planning guideline is *not a universal right to upload three images*. Google Flow saved character creation documentation specifies **1–2 images**; Gemini/Vertex Veo reference-image route may support **up to 3 asset images or 1 style image** depending on version; Frame mode instead uses explicit first/last assets.
6. Approve a shot setup still when scene geometry/props need control; animate only after review. No rejection or cross-clip drift silently changes canon.

## Reusable blank packet — keep this immutable after owner approval

```text
CASE_ID: [real case-scoped ID]
CHARACTER_ID: [P01/D01/etc, unique in THIS case]
SOURCE_DEMOGRAPHIC_FACT_IDS: [IDs / UNKNOWN]
VISUAL_FICTION_APPROVAL: [USER-APPROVED receipt / PENDING]
CANON_FRONT_ASSET_ID: [approved actual image ID or PENDING]
CANON_FRONT_FILE: [actual attached/local file / NOT_ATTACHED]
CANON_3Q_ASSET_ID: [optional approved asset / NONE]
CANON_PROFILE_ASSET_ID: [optional approved asset / NONE]
WARDROBE_VERSION: [e.g. P01-W01 or PENDING]
VOICE_ASSET_ID: [real approved asset / NOT_CREATED]
STYLE_REF_ID: [STYLE_ONLY, approved / PENDING]
ENVIRONMENT_REF_ID: [real location asset / PENDING]
IMMUTABLE_IDENTITY_BLOCK_V1_BEGIN
Age/presentation: [approved description with source basis]
Face/hair: [specific approved features, not new creative guesses]
Body/proportions: [approved appearance]
Wardrobe/props: [exact type/color/carry/wear state and version]
Lock: face geometry, age range, body proportions, hair, clothing, identity marks, 2D illustration language.
Allowed changes: shot action, expression, approved camera angle, story-appropriate lighting.
IMMUTABLE_IDENTITY_BLOCK_V1_END
APPROVAL_EVENT_ID: [receipt / PENDING]
```

**Verbatim rule:** Copy *unchanged* from `IMMUTABLE_IDENTITY_BLOCK_V1_BEGIN` through `_END` into every relevant standalone video card. Any change requires a new block version and targeted dependent-clip review. A written filename is not an attached reference. PENDING blocks cannot authorize generation.

## Per-clip reference binding

```text
CASE_ID / CLIP_ID / clip_version: [...]
Execution device: MOBILE / WINDOWS_PC / OTHER / UNKNOWN
Platform / model / exact mode: [...] / [...] / [...]
Account entitlement evidence: OBSERVED_AVAILABLE / NOT_TESTED
Conditioning method: FRAMES_FIRST / FRAMES_FIRST_LAST / INGREDIENTS /
                     FLOW_SAVED_CHARACTER / OMNI_START_PLUS_REFERENCE / OTHER_VERIFIED
Reference slot limit for this exact mode: observed number / UNKNOWN
Reference 1: real attached asset ID + purpose IDENTITY/STYLE_ONLY/ENVIRONMENT/FRAME
Reference 2: optional real attached asset ID + purpose [...]
Reference 3: optional and only if selected mode supports it [...]
Saved Flow Character: observed exact object name / NOT_AVAILABLE
Saved Flow Voice: observed exact voice name / NOT_AVAILABLE
Setup still + last frame: actual IDs only when supported
Immutable identity block version and exact text: [copy verbatim]
One speaker + one Bengali line + timed duration: [...]
Screen positions, camera axis, hand-held medical props: [...]
Clinical FACT IDs / visual FACT IDs: [...]
Observed credit price + bounded owner approval: [...]
Output/QC: NOT_GENERATED / actual reviewed hash, technical + clinical + voice status
```

### On mobile
Copy the packet into one chat/project Note; use whatever actual file-picker is present to attach approved images for each independent video. Use the whole exact identity block (do not abbreviate it into 'same person as previous'). If source ID or attachment isn't available in the current app session, mark `NOT_ATTACHED/HOLD`.

### On Windows
Use the **same** packet, optionally record file hashes and machine-readable sidecar; Windows FFmpeg/ffprobe supplements completed media review only. No new Python dependency or schema change is introduced.

**Do not place private patient photos/IDs, voice biometrics without permission, or API tokens in public GitHub.** Any source-derived clinical visual must remain explicitly cited/reviewed.
