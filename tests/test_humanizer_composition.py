"""Synthetic documentation/safety checks for Humanizer composition, not a language-quality benchmark."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

class HumanizerComposition(unittest.TestCase):
    def test_semver_current_declarations(self):
        self.assertIn("version: 2.7.0", read("SKILL.md"))
        self.assertIn("# Bangla Medical Case-to-Video (v2.7.0)", read("SKILL.md"))
        self.assertIn("**Version:** 2.7.0", read("README.md"))
        self.assertIn('version: "2.7.0"', read("agents/openai.yaml"))
        self.assertIn("## [2.7.0]", read("CHANGELOG.md"))

    def test_reused_skill_not_vendored_or_assumed_active(self):
        rules = read("references/HUMANIZER_COMPOSITION.md")
        self.assertIn("humanizer", rules)
        self.assertIn("issue #12", rules)
        self.assertIn("HUMANIZER_SKILL_LOADED", rules)
        self.assertIn("HUMANIZER_FALLBACK_APPLIED", rules)
        self.assertIn("NOT_RUN", rules)
        self.assertIn("not bundled", rules)

    def test_source_clinical_asset_and_approval_protection(self):
        rules = read("references/HUMANIZER_COMPOSITION.md")
        for term in ["FACT_REGISTER", "Original medical source", "AUDIO_UNTESTED", "LOCK", "clinical", "HOLD", "JSON", "consent", "approval"]:
            self.assertIn(term, rules)
        script = read("references/PROMPT_TEMPLATES.md")
        self.assertIn("Clinical audit", script)
        self.assertIn("source quotations", script)
        self.assertIn("exact words", script.lower())
        self.assertIn("one-line-per-clip", rules)

    def test_device_parity_and_producer_delivery(self):
        rules = read("references/HUMANIZER_COMPOSITION.md")
        self.assertIn("mobile", rules.lower())
        self.assertIn("Windows", rules)
        pack = read("references/FULL_PRODUCTION_PACK.md")
        self.assertIn("07_qa/HUMANIZER_REVIEW_v001.md", pack)
        self.assertIn("OPERATOR_STEPS_v001.md", pack)
        self.assertIn("same final exact", pack.lower())

    def test_schema_is_not_changed(self):
        self.assertIn('"const": "2.2.0"', read("references/production.schema.json"))
        self.assertIn("C01/C09", read("CHANGELOG.md"))

if __name__ == "__main__":
    unittest.main()
