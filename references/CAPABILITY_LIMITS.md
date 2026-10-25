# What this skill cannot do or guarantee

| Requested result | Actual boundary / available assistance |
|---|---|
| Automatically render a video by uploading SKILL.md | Instructions and planning artifacts do not establish an execution integration. Official Gemini help currently excludes Create video from Skills. Supply a standalone job card to the ordinary video interface. |
| Change an unavailable duration/model/quota | The generator UI/account decides available settings. Replan the timeline around a confirmed unit. A prompt cannot unlock a missing control. |
| Prevent every age/face/sex/wardrobe/environment change | References and explicit invariants guide generation; actual media can still drift. Inspect and reject failed takes. |
| Guarantee the same voice, exact Bengali or perfect lip sync | Text-only voice prose cannot establish persistent identity. Some Flow modes document saved/custom voice references, but require account/mode inspection and independent Bengali voice pilots. External audio/Edge-TTS (online) is an optional fallback; adding voiceover does not automatically establish visible-mouth lip sync. |
| Force separate outputs through a prompt alone | New independent video conversations and no earlier MP4 reduce the chance of cumulative editing. The output must still be inspected; reject concatenated/replayed/rewritten results. |
| Prove why drift appeared around forty seconds | Owner reported that pattern; no controlled cause or universal length ceiling is established. |
| Guarantee Gemini is faster/cheaper/better than Flow | Current impression is owner-reported. Measure model/settings, waiting/render time, retries, quota/spend and accepted output quality before comparing. |
| Transfer a saved Flow character or Algenib/Charon preset to Gemini | Exported stills may be attached where supported. Platform objects/presets/voice locks do not transfer merely because their names appear in text. |
| Invent missing clinical events for a complete narrative | Unknown diagnoses, vessels, investigations and outcomes remain unknown or the relevant claim is held. |
| Complete clinical/owner approvals automatically | The skill drafts review evidence. Real clinicians/owners make their own scoped decisions; selecting quoted approval text is not silently promoted into a clinical decision. |
| Certify identity/voice/clinical quality from a file probe | Technical tools check metadata and arithmetic. Full media/source review remains necessary. |
| Open new Gemini chats, spend quota, download, rename, merge in CapCut or publish by itself | It supplies job cards, operation checklists, filenames, assembly plans and supported local checks. Actual platform actions need user operation or a separately verified authorized integration. |
| Treat old approved clips as newly validated 10s Gemini outputs | Preserve exact old exports and historical approvals. New profile/edits need their own versioned manifest, actual outputs and QA. |
| Retrieve old chat knowledge from a bare asset ID/path | Attach the actual references and expand the current scene specification in each rendering job. |

Status vocabulary: USER-REPORTED observation; PLANNED workflow; TESTED local code/document check; VERIFIED scoped evidence; USER-APPROVED exact artifact. Do not collapse these states into 'production verified'.

## Optional Vids route
See PLATFORM_ROUTES.md for current documented generation, Bangla voiceover and MP4 assembly routes. Account access, pronunciation, voice identity, lip sync and actual Vids media quality remain untested. The Skill is not an installable Flow/Vids plugin; starter and handoff checks do not create clinical facts, images or approvals.

## Device-specific constraints
- A mobile-only workflow must **never** require local Python, FFmpeg, ffprobe, PowerShell, desktop-only Vids controls, a GPU or a command line. Use `DEVICE_WORKFLOWS.md` manual QA and a compatible observed mobile app/editor. If playback metadata cannot be measured, keep timing `NOT_TESTED`; do not pretend manual inspection produced precise technical properties.
- Optional Windows CLI checks supplement but never replace the required human reviews. A phone→Windows transfer preserves source, immutable prompts, version/hash where available, decisions and original exported media; do not silently re-render accepted clips.
- Research/README claims that a particular interface is available on an iPhone/Android device are not proof that this account currently exposes it. Missing platform control → alternative route or HOLD, not fabricated access.
