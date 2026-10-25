"""Documentation and capability regression originally introduced in 2.5.1; survives later versions."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ResearchGaps(unittest.TestCase):
    def read(self, rel):
        return (ROOT / rel).read_text(encoding="utf-8")

    def test_versions_aligned(self):
        self.assertIn("version: 2.7.0", self.read("SKILL.md"))
        self.assertIn("# Bangla Medical Case-to-Video (v2.7.0)", self.read("SKILL.md"))
        self.assertIn("**Version:** 2.7.0", self.read("README.md"))
        self.assertIn('version: "2.7.0"', self.read("agents/openai.yaml"))
        self.assertIn("## [2.5.1]", self.read("CHANGELOG.md"))

    def test_specific_api_exclusivity_not_universal_google_claim(self):
        rules = self.read("references/CONDITIONING_COMPATIBILITY.md")
        self.assertIn("BLOCK_THIS_API_COMBINATION", rules)
        self.assertIn("Gemini Omni API", rules)
        self.assertIn("Starting frame plus additional reference image", rules)
        self.assertIn("REQUIRE_INGREDIENTS_AND_ACCOUNT_PROOF", rules)
        self.assertIn("not", rules.lower())

    def test_packet_identity_and_attachment_gates(self):
        packet = self.read("references/REFERENCE_PACKET_TEMPLATE.md")
        self.assertIn("IMMUTABLE_IDENTITY_BLOCK_V1_BEGIN", packet)
        self.assertIn("NOT_ATTACHED", packet)
        self.assertIn("Reference 3: optional and only if", packet)
        self.assertIn("Flow saved character creation documentation specifies **1–2 images**", packet)

    def test_jio_unknown_not_falsely_verified(self):
        matrix = self.read("references/JIO_ACCOUNT_CAPABILITY_MATRIX.md")
        self.assertIn("Account inspection:** NOT_PERFORMED", matrix)
        self.assertIn("PRICE_UNKNOWN", matrix)
        self.assertIn("UNCONFIRMED_SEPARATE_BILLING", matrix)
        self.assertNotIn("ALL_FEATURES_AVAILABLE", matrix)

    def test_mobile_no_cli_and_existing_schema(self):
        self.assertIn("no shell/FFmpeg/Python", self.read("references/DEVICE_WORKFLOWS.md"))
        self.assertIn('"const": "2.2.0"', self.read("references/production.schema.json"))
        self.assertIn("C01/C09", self.read("CHANGELOG.md"))


if __name__ == "__main__":
    unittest.main()
