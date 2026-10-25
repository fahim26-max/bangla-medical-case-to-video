#!/usr/bin/env python3
"""Probe one standalone export. Technical PASS never means clinical/media approval."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess

def inspect(metadata, seconds=10.0, aspect='16:9', audio_route='NATIVE', tolerance=0.1):
    errors=[]
    if not math.isfinite(seconds) or not math.isfinite(tolerance) or seconds<=0 or tolerance<0:raise ValueError('Expected duration must be positive and finite; tolerance finite and nonnegative')
    try:
        w,h=map(float,aspect.split(':'));ratio=w/h
        if not math.isfinite(w) or not math.isfinite(h) or w<=0 or h<=0:raise ValueError
    except (ValueError,ZeroDivisionError):raise ValueError('Aspect must be positive W:H')
    streams=metadata.get('streams',[])
    video=[s for s in streams if s.get('codec_type')=='video' and not s.get('disposition',{}).get('attached_pic',0)]
    audio=[s for s in streams if s.get('codec_type')=='audio']
    duration=None
    try:
        duration=float(metadata['format']['duration'])
        if not math.isfinite(duration) or duration<=0:errors.append('Actual duration is not a positive finite number')
        elif abs(duration-seconds)>tolerance+1e-9:errors.append('Actual duration differs from the single-job contract; possible accumulated output. Reject, do not blindly trim.')
    except (KeyError,ValueError,TypeError):errors.append('Actual container duration unavailable')
    if len(video)!=1:errors.append('Exactly one video stream is required')
    if video:
        vs=video[0];vw=vs.get('width',0);vh=vs.get('height',0)
        if not vw or not vh:errors.append('Video dimensions unavailable')
        else:
            try:
                display=vs.get('display_aspect_ratio')
                if display and display not in ('0:1','N/A'):
                    dw,dh=map(float,display.split(':'));actual=dw/dh
                else:actual=vw/vh
                if not math.isfinite(actual) or abs(actual-ratio)>0.02:errors.append('Display aspect ratio differs from the job contract')
            except (ValueError,ZeroDivisionError):errors.append('Display aspect ratio invalid')
        try:
            vd=float(vs['duration'])
            if not math.isfinite(vd) or abs(vd-seconds)>tolerance+1e-9:errors.append('Video stream duration differs from the job contract')
        except (KeyError,ValueError,TypeError):pass
    if audio_route=='NATIVE' and not audio:errors.append('Native-dialogue job has no audio stream')
    return {'technical_result':'FAIL' if errors else 'PASS','requested_seconds':seconds,'actual_seconds':duration,'video_streams':len(video),'audio_streams':len(audio),'errors':errors,'clinical_qa':'NOT_TESTED','identity_qa':'NOT_TESTED','voice_and_exact_dialogue_qa':'NOT_TESTED','spoken_interval_qa':'NOT_TESTED','continuity_qa':'NOT_TESTED','user_approved':False,'boundary':'Probe metadata cannot certify independent content, detect recap, authenticate speakers or prove the exact Bengali line.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('video',type=Path);ap.add_argument('--seconds',type=float,default=10);ap.add_argument('--aspect',default='16:9');ap.add_argument('--audio-route',choices=['NATIVE','EXTERNAL','SILENT'],default='NATIVE');args=ap.parse_args()
    try:
        meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(args.video)],stderr=subprocess.PIPE,text=True))
        result=inspect(meta,args.seconds,args.aspect,args.audio_route)
        result['file']=str(args.video);result['sha256']=hashlib.sha256(args.video.read_bytes()).hexdigest()
    except (OSError,subprocess.CalledProcessError,ValueError) as exc:
        print(json.dumps({'technical_result':'BLOCKED','error':str(exc),'user_approved':False}));return 2
    print(json.dumps(result,indent=2));return 0 if result['technical_result']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
