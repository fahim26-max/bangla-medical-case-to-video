# Jio promotional Google AI Pro — account + device capability ledger (v2.5.1)

**Owner case:** Google AI Pro activated through the Jio promotional programme (user-reported). Normal retail Google AI Pro marketing documentation does **not** verify this specific account has the feature. This document contains **blank observation slots**, not account-level verification.

**Audit baseline:** 2026-10-22. **Account inspection:** NOT_PERFORMED. **No login, app click, credit consumption or screen test performed here.** Do not store password, tokens, billing IDs or private images.

## Legend
- `DOC`: current first-party docs describe a feature.
- `UI`: this exact account/device/model showed the control, with observation date and screenshot/owner receipt.
- `TEST`: an actual artifact demonstrated that the requested feature works (clip hash + QA decision).
- `UNKNOWN`: absent evidence, **not** the same as feature unavailable.
- `UNAVAILABLE`: actively observed unavailable in this account/device/mode.
- `PRICE_UNKNOWN`: never guess credits, even if another account sees pricing.

## Blank current-session matrix — **all user observations unverified**

| Surface | Device | Exact account/model/mode | First frame | First+last | Ingredient/references | Saved Character | Voice reference | Duration/resolution | Quoted credits | UI/test evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Google Flow | Android/iPhone mobile | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | PRICE_UNKNOWN | NOT_TESTED |
| Google Flow | Windows browser | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | PRICE_UNKNOWN | NOT_TESTED |
| Gemini App Create Video | Android/iPhone mobile | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | PRICE_UNKNOWN | NOT_TESTED |
| Gemini App Create Video | Windows browser | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | PRICE_UNKNOWN | NOT_TESTED |
| Google Vids create/animate/assemble | Mobile | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | PRICE_UNKNOWN | NOT_TESTED |
| Google Vids create/animate/assemble | Windows browser | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | PRICE_UNKNOWN | NOT_TESTED |
| Gemini API / Vertex Veo | API, device-independent | UNCONFIRMED_SEPARATE_BILLING | DOC_TASK_SPECIFIC | DOC_TASK_SPECIFIC | DOC_TASK_SPECIFIC | N/A | DOC_TASK_SPECIFIC | DOC_TASK_SPECIFIC | PRICE_UNKNOWN | NOT_TESTED |

**Official feature guidance does not overwrite this table.** Documented Flow Saved Characters/voice references are promising, but remain `UNKNOWN` for the Jio account and available devices until inspected. Generic Gemini API / Vertex access and cost must **not** be inferred from a Jio consumer subscription.

## Evidence entry form (copy one per exact observation)

```text
Observation ID: [unique]
Timestamp (Asia/Dhaka): [date/time or UNKNOWN]
Operator: [owner / authorized reviewer]
Source: OFFICIAL_DOC / OWNER_UI_SCREEN / MEDIA_OUTPUT
Platform + device + browser/app version: [...]
Account type: JIO_PROMOTIONAL_AI_PRO (user-reported)
Displayed model / mode / duration / aspect / resolution: [...]
Feature checked: [first frame / last frame / ingredients / 1..N refs /
                  saved character / @voice / Bengali voice / export /
                  editor / current quoted credits]
Control appears: YES / NO / NOT_CHECKED
Selected mode accepts requested combination: YES / NO / NOT_TESTED
UI screenshot / official URL / other receipt: [link or owner record]
Media output hash, speaker and duration QA: [only if tested; else NOT_TESTED]
Effective credits per accepted second: [only measured; else UNKNOWN]
Conclusion: DOCUMENTED / OBSERVED_AVAILABLE / UNAVAILABLE / MEDIA_TESTED / UNKNOWN
Next minimal bounded test: [...]
```

## No-credit inspection order

1. Inspect phone interface first (actual Flow and Gemini Create Video); capture *visible* menu controls without rendering, payment or trial.
2. Inspect Windows interface for extra import/export, frames, reference and voice options. **Do not conclude phone lacks a feature merely because its UI differs.**
3. Separate selected **model/mode** (Veo vs Omni, Frames vs Ingredients, Vids Create vs Animate) into distinct observation records rather than one combined 'Google supports' row.
4. Preserve screenshots/records in a private case folder or Notion (not public GitHub). Populate this template from actual evidence only.
5. Use `CONDITIONING_COMPATIBILITY.md` to rule out a documented unsupported input composition; if uncertain, select a known supported route or mark `RENDER_HOLD`. No paid experiment without owner-scoped authorization and current displayed price.
6. Recheck when account/region/plan, provider UI/model, or feature restrictions change. A past working clip does not confer future entitlements.

## Relevant official sources

- [Google Flow model and supported feature guide](https://support.google.com/flow/answer/16352836)
- [Google Flow Characters guide](https://support.google.com/flow/answer/16935308)
- [Google Flow generate-video and voice-reference guide](https://support.google.com/flow/answer/16353334)
- [Google Vids video-generation help](https://support.google.com/docs/answer/16143507)
- [Gemini App video creation help](https://support.google.com/gemini/answer/16126339)
- [Gemini API Veo reference](https://ai.google.dev/gemini-api/docs/veo)

**State boundary:** blank template ≠ observed access; `DOCUMENTED` ≠ `MEDIA_TESTED`; `TECHNICAL_PASS` ≠ Bengali/clinical/owner approval.
