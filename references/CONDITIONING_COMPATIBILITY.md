# Video conditioning compatibility — model and surface scoped (v2.5.1)

**Scope:** This is a preflight decision aid. **Never claim first/last frame + Ingredients are universally incompatible across every Google product.** Distinguish the underlying API fields from buttons exposed in Flow, Gemini App, Google Vids or a third-party tool. Current as-researched: 2026-10-22. Each real account/model/UI selection must be inspected again before spending.

## Mode decision matrix

| Surface / selected mode | Input composition | Verified documentation claim | Preflight verdict |
|---|---|---|---|
| **Veo / Vertex REST `VideoGenerationModelInstance`** | `image` + `lastFrame` | Allowed: `lastFrame` requires `image`. | **ALLOW** when current model supports frames |
| **Veo / Vertex REST `VideoGenerationModelInstance`** | `referenceImages` + any of `image`, `video`, `lastFrame` | **Not permitted in the same request** by that API resource. | **BLOCK_THIS_API_COMBINATION** |
| **Veo / Vertex REST `VideoGenerationModelInstance`** | 1–3 asset reference images or 1 style image, `prompt` | Reference count/type limits are defined there; exact model/version additionally matters. | **CHECK_MODEL_LIMITS** |
| **Gemini API Veo 3.1 video generation** | Reference-image task versus first/last-frame task | Both task types documented; do not infer a single request supports a mixed task because both features exist separately. | **SELECT_DOCUMENTED_TASK** |
| **Gemini Omni API** | Starting frame plus additional reference image | Official examples explicitly show these combined with different roles. | **DOCUMENTED_EXAMPLE / VERIFY_CURRENT_MODEL** |
| **Google Flow — selected Veo Frames mode** | First only / first and last | Flow lists mode- and model-specific Frames generation. Separate mode from Ingredients in actual UI. | **OBSERVE_ACTUAL_MODE** |
| **Google Flow — selected Veo Ingredients mode** | Clean image ingredients (model duration/slots apply) | Mode listed independently. No blanket inference that Frames can be added in the same consumer UI operation. | **OBSERVE_ACTUAL_MODE** |
| **Google Flow — Omni Flash voice references** | Voice reference via **Ingredients** | Google Flow states voice references only work with Ingredients; other generation types return error. | **REQUIRE_INGREDIENTS_AND_ACCOUNT_PROOF** |
| **Google Flow Saved Characters** | Character created from 1–2 images + selected voice where supported | Documentation describes reusable Characters; output fidelity and owner entitlement not yet tested. | **ACCOUNT_HOLD_UNTIL_OBSERVED** |
| **Gemini App Create Video / Google Vids** | Actual UI exposed reference and frame modes | Neither a Veo REST request nor Omni API examples prove that a consumer UI exposes a combination. | **ACCOUNT_HOLD_UNTIL_OBSERVED** |

### Operator decision logic

```text
1. Declare exact SURFACE + MODEL + MODE + DEVICE + ACCOUNT.
2. Consult dated official documentation for that specific request surface.
3. If Veo/Vertex API input has referenceImages AND image/video/lastFrame:
       BLOCK_THIS_API_COMBINATION (no paid request).
4. If Flow voice reference is requested:
       require actual Flow Omni + Ingredients path and observed account control.
5. If model accepts exactly 1 or 2 images, do not attach 3 because another mode allows 3.
6. If combination is undocumented or not exposed on this device/account:
       NOT_TESTED / HOLD; choose another genuinely supported route.
7. After first generated output:
       verify visual identity + Bengali audio + clinical claims as a separate gate.
```

**Two-stage workaround:** An approved still built separately from canon and references can be used as a later **first frame** if its generation mode supports frame animation. Stage 1 setup-still and Stage 2 video generation are **different operations** and must not be represented as if the same API request accepted incompatible input fields. Avoid paid multi-step plans without scoped authorization.

## First-party source links

- [Google Cloud VideoGenerationModelInstance REST reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance): `image` incompatible with `referenceImages`, `referenceImages` incompatible with `lastFrame`; `lastFrame` needs `image`.
- [Google Veo 3.1 Gemini API guide](https://ai.google.dev/gemini-api/docs/veo): reference-image and first+last video tasks.
- [Gemini Omni API documentation](https://ai.google.dev/gemini-api/docs/omni): first-frame + reference-image combined example.
- [Google Flow model feature matrix](https://support.google.com/flow/answer/16352836): model/mode-specific Frames and Ingredients.
- [Google Flow create-video guide](https://support.google.com/flow/answer/16353334): Omni voice reference available only with Ingredients.
- [Google Flow Characters guide](https://support.google.com/flow/answer/16935308): 1–2 character appearance images and selected voice.

**Evidence policy:** Official capability text is `DOCUMENTED`, account UI observation is `OBSERVED_AVAILABLE`, and successful paid output is `MEDIA_TESTED`. The three states cannot substitute for one another.
