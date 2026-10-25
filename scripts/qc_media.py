#!/usr/bin/env python3
"""Optional Windows/macOS/Linux FFmpeg technical QA. No clinical or voice verification."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import re
import shutil
import subprocess


def analyze_probe(data, expected_seconds, tolerance, audio_route):
    """Pure structural checks; never asserts speech, likeness or approval."""
    streams = data.get("streams") or []
    fmt = data.get("format") or {}
    video = next((x for x in streams if x.get("codec_type") == "video"), None)
    audio = any(x.get("codec_type") == "audio" for x in streams)
    problems = []
    if video is None:
        problems.append("NO_VIDEO_STREAM")
    try:
        duration = float(fmt.get("duration"))
        if not (duration >= 0):
            raise ValueError()
    except (ValueError, TypeError):
        duration = None
        problems.append("DURATION_UNAVAILABLE")
    if duration is not None and abs(duration - expected_seconds) > tolerance:
        problems.append("DURATION_MISMATCH")
    if audio_route != "SILENT" and not audio:
        problems.append("EXPECTED_AUDIO_STREAM_MISSING")
    fps = None
    if video:
        try:
            frac = Fraction(video.get("avg_frame_rate") or "0/1")
            if frac > 0:
                fps = round(float(frac), 4)
        except (ValueError, ZeroDivisionError):
            pass
    return {
        "duration_s": duration,
        "fps": fps,
        "width": video.get("width") if video else None,
        "height": video.get("height") if video else None,
        "audio_stream_present": audio,
        "blocking_problems": problems,
    }


def parse_warnings(stderr):
    return {
        "black_detected": bool(re.search(r"black_start:", stderr)),
        "freeze_detected": bool(re.search(r"freeze_start:", stderr)),
    }


def run_binary(arguments, timeout=90):
    proc = subprocess.run(arguments, capture_output=True, text=True, timeout=timeout, check=False)
    if proc.returncode:
        raise RuntimeError(f"{arguments[0]} failed ({proc.returncode}): {proc.stderr[-500:]}")
    return proc.stdout, proc.stderr


def check(file_path, expected_seconds, tolerance=0.5, audio_route="NATIVE", scan=True):
    out = {
        "file": str(file_path),
        "technical_verdict": "NOT_TESTED",
        "clinical_verdict": "HUMAN_REQUIRED",
        "identity_verdict": "HUMAN_REQUIRED",
        "bangla_speech_verdict": "HUMAN_REQUIRED",
        "owner_release_approval": "NOT_GRANTED",
        "scan_state": "NOT_TESTED",
    }
    if not Path(file_path).is_file():
        out["error"] = "FILE_NOT_FOUND"
        return out
    if not shutil.which("ffprobe") or (scan and not shutil.which("ffmpeg")):
        out["error"] = "REQUIRED_LOCAL_TOOL_UNAVAILABLE"
        return out
    try:
        stdout, _ = run_binary(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", str(file_path)])
        values = analyze_probe(json.loads(stdout), expected_seconds, tolerance, audio_route)
        out.update(values)
        if scan:
            _, stderr = run_binary(["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "info", "-i", str(file_path), "-vf", "blackdetect=d=0.5:pic_th=0.98,freezedetect=n=-60dB:d=1.0", "-an", "-f", "null", "-"])
            out.update(parse_warnings(stderr))
            out["scan_state"] = "MEASURED"
        out["technical_verdict"] = ("HOLD" if values["blocking_problems"] else
            "REVIEW_REQUIRED" if out.get("black_detected") or out.get("freeze_detected") or not scan else "TECHNICAL_PASS")
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
        out["technical_verdict"] = "NOT_TESTED"
        out["error"] = type(exc).__name__ + ": " + str(exc)[:280]
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("file")
    p.add_argument("--expected-seconds", type=float, required=True)
    p.add_argument("--tolerance", type=float, default=0.5)
    p.add_argument("--audio-route", choices=["NATIVE", "EXTERNAL", "SILENT"], default="NATIVE")
    p.add_argument("--skip-scan", action="store_true", help="Skip black/freeze scan; verdict remains REVIEW_REQUIRED")
    args = p.parse_args()
    if args.expected_seconds <= 0 or args.tolerance < 0:
        p.error("Expected seconds must be >0 and tolerance >=0")
    result = check(args.file, args.expected_seconds, args.tolerance, args.audio_route, not args.skip_scan)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result["technical_verdict"] in ("NOT_TESTED", "HOLD") else 0


if __name__ == "__main__":
    raise SystemExit(main())
