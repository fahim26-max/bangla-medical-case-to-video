# Flow, Gemini Apps and Google Vids adapters

**Execution device is not a generation profile.** On mobile, offer only operator steps confirmed usable in that device's app/browser; on Windows, add optional local QC and editor paths. If the required creation/import/export control is absent on mobile, document `CAPABILITY_UNAVAILABLE_ON_THIS_DEVICE`, preserve the reviewed draft, and use an actually available alternate route or continue later on desktop; do not invent feature parity. See `DEVICE_WORKFLOWS.md`.

**Feature source scope:** Flow's documented saved Characters and selected/custom voice-reference mechanisms can improve conditioning where the actual selected mode/account exposes them. They are not guaranteed voice/identity locks and do not transfer automatically to Gemini or Vids. Use current UI evidence; see `BENGALI_AUDIO_PLAYBOOK.md`.


Checked21October2026. These are documented/operator routes, not tested app integrations. Actual selected account/model/region/quota/settings must be observed; Jio partner Google AI Pro does not establish all ordinary paid-plan entitlements.

## Conditioning preflight is route-specific (v2.5.1)
Before any clip card is marked render-ready, consult `CONDITIONING_COMPATIBILITY.md` and `JIO_ACCOUNT_CAPABILITY_MATRIX.md`. A compatibility rule from the Veo/Vertex API applies only to that request surface and cannot be silently carried over to Gemini Omni API or Flow UI. Flow Saved Characters/voice reference support is documented, not verified on the owner's Jio promotional account. For actual render, record account/region, device, selected model, selected mode, available reference slots, duration, voice control and credit quote. Unsupported or unobserved features stay HOLD, not optimistic YES.

## Profiles
| Profile | Default planning math | Entry condition |
|---|---|---|
| FLOW_8S |15×8=120| Existing default; verify current selected settings. |
| FLOW_10S |12×10=120| Supported selected model/mode observed; new script/pilots. |
| GEMINI_APP_INDEPENDENT_10S |12×10=120| Current account unit confirmed; fresh video conversation for each job. |
| VIDS_8S |15×8=120| Current Vids mode supports8s; generation/Bengali pilot pending. |
| VIDS_10S |12×10=120| Current Vids mode supports10s; generation/Bengali pilot pending. |
| VIDS_ASSEMBLY | From approved input manifest | Editor-only; no new media generation assumed. Preserve supplied clip durations; do not stretch8s to10s. |

The starter uses explicit uniform units; mixed-duration editor timelines stay in the manually reviewed canonical manifest. Alternate target durations must be divisible by selected units or explicitly rebuilt;15×10 is150, not120.

## Flow generation
Use `FLOW_PRODUCTION_CONTRACT.md` and per-clip cards. Operator: correct project/account → observed model/mode/aspect/length/resolution/x1/current quote → actual approved references/frame and available voice → one scoped job → original export → QA/log. IDs/prompt preset mentions do not select UI assets. Existing C01/C09 fixtures are exact approved8s exports, not transferable Gemini approvals. A documented Flow Agent is not a verified controller for this Skill.

Official feature reference: https://support.google.com/flow/answer/16352836 . It lists model-dependent8/10s options, reference/frame routes and voice customization; account availability and accepted-media performance remain unknown. Do not copy API controls into the app without observing them.

## Gemini Apps generation
Read `GEMINI_INDEPENDENT_CLIPS.md`. Plan with the Skill; render separately in ordinary Create video. Every job gets a fresh video conversation, actual relevant stills, expanded identity/room/style and one exact line. No previous MP4, full screenplay, Extend or Continue. Download separately; reject accumulated or incomplete content rather than blind tail trimming. This mitigation does not guarantee facial/voice consistency.

Official: https://support.google.com/gemini/answer/16126339 ; https://support.google.com/gemini/answer/18560919 ; https://support.google.com/gemini/answer/17094296 . Skills currently exclude Create video; import the complete folder and test selection separately. Five-image video reference limit is documented for this app, not every Google product. No Algenib/Charon portability or general audio-reference import is assumed.

Scoped model evidence: https://ai.google.dev/gemini-api/docs/omni documents10s extensions up to40s total using the last10s context. This is not a universal app limit or a proven cause of the owner's age/sex drift.

## Google Vids generation and editing
Treat “Google vid” as Google Vids. Official generation help describes Create/Animate, duration3–10s, landscape/portrait, generation from ingredients and inserting outputs into a Vid. Create and Edit have different reference capacities; the page also retains an8s Animate paragraph. Verify the actual mode/UI rather than impose one universal unit. Preserve generated clips by inserting them; check track/speaker mute before retrying missing sound. Source: https://support.google.com/docs/answer/16143507?hl=en . No Vids account or media quality was tested here.

**Manual generation recipe:** use a reviewed job card in the available Create/Animate workflow; attach its actual approved references within that mode's capacity; select the observed duration/aspect; request only its one speaker/line/action; insert the result and audit before producing more. For Animate use the exact composed frame with a concise motion instruction; keep the full contract in the producer record instead of flooding the motion prompt with redundant descriptions. Never replace a missing composed frame with a fictional filename.

**Bangla audio candidate:** official AI Voiceover help lists Bangla and scene-level voiceover generation. Operator may put the exact approved scene line in Voiceover, select a displayed voice, insert and measure it; preserve the accepted audio. This documents language availability, not Bangladeshi pronunciation or persistent identity on this account. An external voiceover is narration unless lip sync is separately demonstrated. Source: https://support.google.com/docs/answer/15070345?hl=en . Do not replace an accepted native soundtrack without a reviewed reason; avoid doubled voices.

**Assembly-first recipe:** open a blank Vid, import accepted clips and approved audio, order by manifest, set timing/cuts, captions/attribution, mix and export an MP4 to the device; review the actual file. Editor/import/export source: https://support.google.com/docs/answer/15082958?hl=en . Native Vids project, clip download and final MP4 are different artifacts; separately preserving/exporting a single clip needs observed UI or a one-clip Vid, not an invented “download individual clip” button.

**Optional Storyboard/Help me create:** supply a de-identified reviewed case/script through actual supported files and ask for an editable draft respecting the exact timeline/facts. Check generated script, stock media and voiceovers against the canonical package; reject invented medical visuals/extra words. It is an optional draft aid, not a tested replacement for controlled drama production. Source: https://support.google.com/docs/answer/15067819?hl=en . A draft's automatic voiceover can require replacement when you supply your own audio.

**Captions:** add/edit actual-speech-timed captions through the observed editor controls; correct Bengali spelling and timing. Autogenerated text/language support must be tested, not assumed from Bangla voiceover availability. Source: https://support.google.com/docs/answer/14953386?hl=en . Do not invent SRT import support from a general captions page; use manual/editor-supported captions or an external editor when unavailable.

## Copy-paste Vids planning prompt (draft only)
```text
Prepare a Google Vids production/edit plan from the attached reviewed case
package. Preserve its exact Bengali lines, chronology, source attribution,
fictional cast identities and approved assets. Target {{SECONDS}}s, {{ASPECT}}.
List the observed account controls and unavailable features separately.
For generation create one standalone shot card per supported unit; do not
extend a prior video or invent scans/results. For existing exports build an
assembly manifest without regenerating them. If using Bangla Voiceover,
select an actually available voice and pilot pronunciation/timing/identity.
Do not claim access, automatic execution, lip sync or final media approval.
```

## Native audio versus separate voiceover
Native dialogue: requested single-speaker mouth movement and sound must be reviewed on real output; when preflight audio cannot be separately exported, use the existing authorized pilot exception. Separate voiceover: measure master audio before final visuals/edit, request silent visuals and match timing; visible talking needs a separately tested sync route. Do not equate AI Voiceover, personal avatar voice, custom saved voice and voice cloning. Maintain the exact same written profile across independent jobs and compare actual samples.

## Import/runtime boundary
This package is a planning Skill, not an installable Flow/Vids plug-in. Gemini import success, fresh-session behaviour, local helper execution, app access, media acceptance and GitHub merge are separate states. Use text templates when a host cannot execute Python/ffprobe. Report inability; never invent a successful command. New tools/modes require targeted pilots, not unrelated research or regeneration of approved originals.
