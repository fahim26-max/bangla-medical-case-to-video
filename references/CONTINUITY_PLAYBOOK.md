# Canon, scene and cross-clip continuity (v2.5.0)

Use with `DEVICE_WORKFLOWS.md`; both phone and Windows operators follow identical visual rules.

## Reference packet and available conditioning controls
Fill `REFERENCE_PACKET_TEMPLATE.md` for every new character and independent shot. Limit references to clean noncontradictory assets inside the **selected mode's observed maximum**; 1–3 is a planning ceiling only, not permission to attach three in every route. Prefer canon/front plus a derived three-quarter only when needed. Keep any Flow saved Character identity and voice as separate **account-observed** resources. Always apply mode-specific exclusions from `CONDITIONING_COMPATIBILITY.md`.

## Canon creation and custody
- Fix source-grounded demographic truth separately from fictional, consent-safe appearance. Preserve STYLE_ONLY, IDENTITY and ENVIRONMENT reference roles.
- Approve one stable canonical character front image; create a three-quarter view **only when the planned shots require it**, derived from canon. Optional profile/detail plates are cost-justified, not mandatory bulk generation.
- Approve wardrobe/accessories and stable room layout. Do not regenerate an approved master because a downstream clip failed; investigate inputs first.
- Freeze an **immutable identity/voice/wardrobe statement** per character; reuse verbatim in each independent card. Actual image conditioning is more important than textual labels alone, and no method guarantees exact identity.
- For difficult doctor–patient reverse shots, generate the composed **setup still** from approved assets, confirm the screen axis/eyelines/clinical props and only then animate.

## Per-shot continuity sheet (mobile text; Windows sidecar optional)

```text
case_id / clip_id / scene_story_time:
canonical_identity_ref / wardrobe_version / environment_ref:
screen_position / camera_side / action_axis / eyeline:
prop_ids + ownership (left/right hand) / clinical visual fact_ids:
lighting / audio_route / speaker_id / voice_version:
start_frame_ref / optional last_frame_ref / duration_profile:
prompt_version / approved_media_version / manual_QA_receipt:
```

- Compare **every neighboring pair** for location, cast, eye lines, props, time, audio bridge, previous knowledge and setup/payoff.
- Only use last-frame chaining where the *selected account route* actually supports it and the specific shot needs uninterrupted motion. Chaining preserves local composition but compounds prior errors; **audit every output against original canon**, not merely its predecessor.
- An API-specific reference/first-frame incompatibility does not imply that every Google consumer mode excludes the same combination. Record mode-specific UI evidence before rendering.

## Revision ledger

| Status | Meaning | Action |
|---|---|---|
| KEEP | Approved artifact unaffected by revised dependency | Preserve exact original/hash and receipt |
| CHECK | Reinforcement or neighboring state changed but original may remain good | Inspect referenced frame/timecode before spending |
| REGENERATE | Action/dialogue/visual facts or required dependency materially changed | Repair only affected clip with new version |
| GENERATE | No actual clip exists yet | Create after source/assets/pilot authorization |

No automatic whole-film regeneration. Any major clinical source correction goes through FACT_REGISTER/clinician review before affected scene work. A failed video must never become the next character canon.

## Two-screen / two-character safeguards
- Record patient screen side, doctor screen side, camera line, stable clinic geometry, glasses/stethoscope and positions.
- Prefer one visible speaker and one restrained action beat per shot. A listener may be offscreen where appropriate; never invent medical equipment or reported test result for an illustrative cutaway.
- Maintain timeline arithmetic: 15×8s or 12×10s **only on supported selected route**, without invisible crossfades changing duration.

## Evidence & attribution

Adapted continuity concepts: [Nagacash/character-continuity-skill](https://github.com/Nagacash/character-continuity-skill) (documentation CC BY 4.0; method attribution, no text/code copied) and [raphaelbgr/ai-video-prompting](https://github.com/raphaelbgr/ai-video-prompting) (MIT). Implementation and scripts here are new. Source code rights and patient consent remain separate.
