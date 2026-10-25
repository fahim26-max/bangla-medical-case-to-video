"""Synthetic mobile/desktop parity and optional technical-QA regression tests; no real-media claims."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


qc = load("qc_media")
sheet = load("make_contact_sheet")


class DeviceContract(unittest.TestCase):
    def test_mobile_no_mandatory_cli(self):
        doc = (ROOT / "references" / "DEVICE_WORKFLOWS.md").read_text(encoding="utf-8")
        self.assertIn("no shell/FFmpeg/Python", doc)
        self.assertIn("RELEASE_HOLD", doc)
        self.assertIn("Phone → Windows handoff", doc)
    def test_skill_keeps_schema(self):
        contract = (ROOT / "references" / "production.schema.json").read_text(encoding="utf-8")
        self.assertIn('"const": "2.2.0"', contract)
    def test_no_clinical_approval_from_technical_tool(self):
        r = qc.check("/file/that/does/not/exist.mp4", 8)
        self.assertEqual(r["technical_verdict"], "NOT_TESTED")
        self.assertEqual(r["clinical_verdict"], "HUMAN_REQUIRED")
        self.assertEqual(r["owner_release_approval"], "NOT_GRANTED")


class TechnicalChecks(unittest.TestCase):
    def setUp(self):
        self.v = {"streams": [{"codec_type": "video", "width": 1280,
                               "height": 720, "avg_frame_rate": "24/1"},
                              {"codec_type": "audio"}],
                  "format": {"duration": "8.000"}}
    def test_expected_8s_audio(self):
        r = qc.analyze_probe(self.v, 8, 0.2, "NATIVE")
        self.assertEqual(r["blocking_problems"], [])
        self.assertEqual(r["fps"], 24.0)
    def test_bad_duration(self):
        self.assertIn("DURATION_MISMATCH", qc.analyze_probe(self.v, 10, 0.2, "NATIVE")["blocking_problems"])
    def test_missing_native_audio(self):
        self.v["streams"].pop()
        self.assertIn("EXPECTED_AUDIO_STREAM_MISSING", qc.analyze_probe(self.v, 8, 0.2, "NATIVE")["blocking_problems"])
        self.assertNotIn("EXPECTED_AUDIO_STREAM_MISSING", qc.analyze_probe(self.v, 8, 0.2, "SILENT")["blocking_problems"])
    def test_black_freeze_warnings(self):
        w = qc.parse_warnings("black_start:1.0\nfreeze_start:2.0")
        self.assertTrue(w["black_detected"])
        self.assertTrue(w["freeze_detected"])
    def test_contact_sheet_layout(self):
        self.assertEqual(sheet.coordinates(5, 4), ["0_0", "320_0", "640_0", "960_0", "0_180"])
        with self.assertRaises(ValueError):
            sheet.coordinates(27, 4)
    def test_windows_wildcard_expansion(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            (base / "C01.mp4").touch()
            (base / "C02.mp4").touch()
            result = sheet.expand_clip_args([str(base / "C*.mp4")])
            self.assertEqual(len(result), 2)
            self.assertTrue(result[0].endswith("C01.mp4"))
            with self.assertRaises(FileNotFoundError):
                sheet.expand_clip_args([str(base / "missing*.mp4")])

    def test_no_input_or_media_in_package(self):
        self.assertNotIn("Case14", (ROOT / "references" / "CONTINUITY_PLAYBOOK.md").read_text())


if __name__ == "__main__":
    unittest.main()
