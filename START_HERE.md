# ব্যবহার — v2.4
নতুন case history এবং original source দিন; `references/PROMPT_TEMPLATES.md`-এর New case prompt ব্যবহার করুন। Default ১২০ সেকেন্ড = ১৫x৮ সেকেন্ড। Skill প্রথমে Fact Register ও Clinical Audit, তারপর script, case-specific Bibles, asset dependencies ও Flow prompts তৈরি করে। Missing clinical details বানাবে না।

এই skill planning ও audit-এর জন্য। নতুন case-এর clinical/script approval, reference/voice approval এবং দুই actual pilot review লাগবে। Flow-তে actual asset/voice select ও generation করতে হবে; এই skill দিয়ে unattended control প্রমাণিত নয়। Existing approved files আবার বানাবেন না।

Current official Gemini import guidance permits SKILL.md, folder or ZIP import. This package's installation in the user's Gemini account is not verified. A successful ChatGPT Skills Git save does not prove Gemini installation, fresh-session activation or Google Flow execution. See `references/FLOW_PRODUCTION_CONTRACT.md` for current source links.

Gemini-তে separate 10s clips চাইলে বলুন: `GEMINI_APP_INDEPENDENT_10S profile; 12x10s; one standalone job per fresh video conversation; no extend, merge or previous MP4.` Skill planning chat-এ কাজ করবে; generated job card actual imagesসহ সাধারণ Create video interface-এ ব্যবহার করবেন। পুরো 120s script render chat-এ দেবেন না। দশ সেকেন্ড আপনার observed account behavior; সব account-এর universal limit নয়।

Full pack: read README.md and references/FULL_PRODUCTION_PACK.md. Optional Google Vids and source-preserving starter are documented in references/PLATFORM_ROUTES.md. All missing dependencies remain explicit; no render/install guarantee.
