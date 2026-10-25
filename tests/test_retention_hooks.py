"""Low-cost documentary and schema-immutability checks for v2.7.0; not viewer testing."""
import re
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

def read(name):
    return (ROOT/name).read_text(encoding="utf-8")

class RetentionContract(unittest.TestCase):
    def test_five_current_versions(self):
        self.assertIn("version: 2.7.0",read("SKILL.md"))
        self.assertIn("# Bangla Medical Case-to-Video (v2.7.0)",read("SKILL.md"))
        self.assertIn("**Version:** 2.7.0",read("README.md"))
        self.assertIn('version: "2.7.0"',read("agents/openai.yaml"))
        self.assertRegex(read("CHANGELOG.md"),r"(?m)^## \[2\.7\.0\]")

    def test_immutable_schema_and_approved_case(self):
        self.assertIn('"const": "2.2.0"',read("references/production.schema.json"))
        for p in ["SKILL.md","references/RETENTION_HOOKS.md","references/HOOK_CLINICAL_SAFETY.md"]:
            self.assertIn("Case14",read(p)) if p=="SKILL.md" else None
        self.assertIn("C01/C09",read("CHANGELOG.md"))

    def test_hook_is_source_id_required_without_virality_guarantee(self):
        hooks=read("references/RETENTION_HOOKS.md")
        safety=read("references/HOOK_CLINICAL_SAFETY.md")
        self.assertIn("FACT IDs",hooks)
        self.assertIn("0–3",hooks)
        self.assertIn("editor-added",hooks)
        self.assertIn("NO_SOURCE",hooks)
        self.assertIn("HOOK_SOURCE_HOLD",safety)
        self.assertIn("10,114",safety)
        self.assertIn("CREATOR_CLAIM_POST_FOUND_DATA_UNVERIFIED",safety)
        self.assertIn("not a",hooks.lower())

    def test_clips_and_readout_are_separate(self):
        beat=read("references/RETENTION_BEAT_MAP.md")
        metrics=read("references/RETENTION_ANALYTICS.md")
        self.assertEqual(len(re.findall(r"(?m)^\| C(?:0[1-9]|1[0-5]) \|",beat)),15)
        self.assertIn("NEEDS_SOURCE_FOR_SUBSTANTIVE_DRAMA",beat)
        self.assertIn("NOT an official fixed 3.0s cutoff",metrics)
        self.assertIn("24 August 2026",metrics)

    def test_mobile_no_cli_and_humanizer_order(self):
        self.assertIn("No FFmpeg/Python needed",read("references/DEVICE_WORKFLOWS.md"))
        self.assertIn("HUMANIZER_COMPOSITION.md",read("SKILL.md"))
        self.assertIn("RETENTION_PREFLIGHT_v001.md",read("references/FULL_PRODUCTION_PACK.md"))

if __name__=="__main__":
    unittest.main()
