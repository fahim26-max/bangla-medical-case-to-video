#!/usr/bin/env python3
"""Build a canon-first FFmpeg contact sheet from actual short video exports (optional)."""
import argparse
import glob
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


def coordinates(count, columns):
    if not (1 <= count <= 26) or not (1 <= columns <= 8):
        raise ValueError("count 1..26 and columns 1..8 required")
    return [f"{320 * (i % columns)}_{180 * (i // columns)}" for i in range(count)]


def command(args):
    p = subprocess.run(args, capture_output=True, text=True, check=False, timeout=90)
    if p.returncode:
        raise RuntimeError(f"{args[0]} returned {p.returncode}: {p.stderr[-400:]}")
    return p.stdout


def duration(path):
    data = json.loads(command(["ffprobe", "-v", "error", "-show_format", "-of", "json", str(path)]))
    return float(data["format"]["duration"])


def expand_clip_args(arguments):
    """Expand PowerShell/Windows wildcard inputs without shell glob reliance."""
    expanded = []
    for name in arguments:
        if any(x in name for x in ("*", "?", "[")):
            matches = sorted(glob.glob(name))
            if not matches:
                raise FileNotFoundError("No clips match: " + name)
            expanded.extend(matches)
        else:
            expanded.append(name)
    return expanded


def create(canon, clips, output, columns=4):
    canon, output = Path(canon), Path(output)
    clips = [Path(c) for c in expand_clip_args(clips)]
    if not canon.is_file() or any(not c.is_file() for c in clips):
        raise FileNotFoundError("Use real existing canon and video files")
    if len(clips) == 0 or len(clips) > 25:
        raise ValueError("Provide between 1 and 25 clips")
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise FileNotFoundError("Optional ffmpeg and ffprobe are unavailable")
    if output.exists():
        raise FileExistsError("Preserve previous contact sheet; choose a new path")
    with tempfile.TemporaryDirectory() as td:
        frames = [canon]
        for i, clip in enumerate(clips, 1):
            sec = max(0.0, duration(clip) * 0.5)
            frame = Path(td) / f"clip_{i:02d}.png"
            command(["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error",
                     "-ss", str(sec), "-i", str(clip), "-frames:v", "1", "-y", str(frame)])
            frames.append(frame)
        filters = []
        for i in range(len(frames)):
            filters.append(f"[{i}:v]scale=320:180:force_original_aspect_ratio=decrease,pad=320:180:(ow-iw)/2:(oh-ih)/2,setsar=1[v{i}]")
        layout = "|".join(coordinates(len(frames), columns))
        filters.append("".join(f"[v{i}]" for i in range(len(frames))) +
                       f"xstack=inputs={len(frames)}:layout={layout}:fill=black[out]")
        args = ["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error"]
        for frame in frames:
            args += ["-i", str(frame)]
        args += ["-filter_complex", ";".join(filters), "-map", "[out]", "-frames:v", "1", "-y", str(output)]
        output.parent.mkdir(parents=True, exist_ok=True)
        command(args)
    return {
        "sheet": str(output), "reference": str(canon),
        "clips": [str(c) for c in clips], "sample_point": "video midpoint",
        "identity_approval": "HUMAN_REQUIRED", "clinical_approval": "HUMAN_REQUIRED"
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--canon", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--columns", type=int, default=4)
    p.add_argument("clips", nargs="+")
    args = p.parse_args()
    try:
        print(json.dumps(create(args.canon, args.clips, args.output, args.columns), indent=2))
        return 0
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"status": "NOT_TESTED", "error": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
