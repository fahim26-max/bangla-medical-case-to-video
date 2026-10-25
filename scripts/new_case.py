#!/usr/bin/env python3
"""Create a source-preserving INTAKE workspace, never a clinically completed package."""
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile

ROOT=Path(__file__).resolve().parents[1]
PROFILES={'FLOW_8S':8,'FLOW_10S':10,'GEMINI_APP_INDEPENDENT_10S':10,'VIDS_8S':8,'VIDS_10S':10,'VIDS_ASSEMBLY':None}

def create_case(case_id,source,output_root,profile='FLOW_8S',duration=120,aspect='16:9',author='Operator not supplied',source_author=None,source_kind='ORIGINAL_CASE',clip_seconds=None):
    if not re.fullmatch(r'[A-Z][A-Z0-9_-]{1,79}',case_id):raise ValueError('Use a case-scoped uppercase ID; paths/spaces are not allowed')
    if profile not in PROFILES:raise ValueError('Unknown profile')
    unit=PROFILES[profile]
    if unit is None:unit=clip_seconds
    elif clip_seconds is not None and clip_seconds!=unit:raise ValueError('Clip unit conflicts with selected profile')
    if isinstance(duration,bool) or not isinstance(duration,int) or duration<=0 or isinstance(unit,bool) or not isinstance(unit,int) or unit<=0 or duration%unit:raise ValueError('Positive integer total must be divisible by the selected unit; assembly profile requires an explicit unit')
    if aspect not in ('16:9','9:16'):raise ValueError('Unsupported aspect')
    if source_kind not in ('ORIGINAL_CASE','DERIVATIVE'):raise ValueError('Invalid declared source kind')
    source=Path(source).resolve()
    if source.suffix.lower() not in ('.txt','.md'):raise ValueError('Starter accepts UTF-8 .txt/.md only; use a supported reader for other formats first')
    raw=source.read_bytes();clinical_text=raw.decode('utf-8-sig')
    if not clinical_text.strip():raise ValueError('Original source is empty')
    output_root=Path(output_root).resolve();output_root.mkdir(parents=True,exist_ok=True)
    dest=output_root/case_id
    if dest.exists():raise FileExistsError('Existing case preserved: '+str(dest))
    # Current Asia/Dhaka civil offset; no system tzdata dependency on Windows.
    stamp=datetime.now(timezone(timedelta(hours=6))).isoformat(timespec='seconds')
    p=json.loads((ROOT/'assets/EMPTY_PACKAGE.json').read_text())
    def replace(value):
        if isinstance(value,str):return value.replace('CASE-NEW',case_id)
        if isinstance(value,list):return [replace(x) for x in value]
        if isinstance(value,dict):return {k:replace(v) for k,v in value.items()}
        return value
    p=replace(p);p['meta'].update(author=author,created_at=stamp,updated_at=stamp)
    p['target'].update(duration_s=duration,clip_count=duration//unit,clip_duration_s=unit,aspect_ratio=aspect)
    p['sources']=[{'id':case_id+':S01','kind':source_kind,'title':source.name,'author':source_author,'locator':'00_sources/'+source.name,'original_text':clinical_text,'sha256':hashlib.sha256(raw).hexdigest(),'accessed_at':stamp,'evidence_state':'TESTED','limitations':['Bytes read locally; declared source kind is not authentication or primary-record verification.','No clinical facts, approvals, media or voice samples have been generated.']}]
    substitutions={'CASE_ID':case_id,'PROFILE':profile,'TARGET_S':str(duration),'CLIP_SECONDS':str(unit),'CLIP_COUNT':str(duration//unit),'ASPECT':aspect}
    temp=Path(tempfile.mkdtemp(prefix='case-intake-',dir=output_root))
    try:
        for f in sorted((ROOT/'assets/CASE_STARTER').rglob('*')):
            if not f.is_file():continue
            rel=f.relative_to(ROOT/'assets/CASE_STARTER');target=temp/rel;target.parent.mkdir(parents=True,exist_ok=True)
            text=f.read_text(encoding='utf-8')
            for k,v in substitutions.items():text=text.replace('{{'+k+'}}',v)
            target.write_text(text,encoding='utf-8')
        (temp/'00_sources').mkdir(exist_ok=True)
        (temp/'00_sources'/source.name).write_bytes(raw)
        (temp/'01_evidence').mkdir(exist_ok=True)
        (temp/'01_evidence/production_package_v001.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        h=replace(json.loads((ROOT/'assets/HANDOFF_TEMPLATE.json').read_text()))
        (temp/'05_jobs/handoff_v001.json').write_text(json.dumps(h,indent=2)+'\n',encoding='utf-8')
        for folder in ['06_media','04_keyframes','08_final']:(temp/folder).mkdir(exist_ok=True)
        # Rename only after all writes; never merge into an existing case.
        if dest.exists():raise FileExistsError('Case appeared during preparation; existing contents preserved')
        temp.rename(dest)
    except Exception:
        shutil.rmtree(temp,ignore_errors=True);raise
    return {'case_directory':str(dest),'stage':'INTAKE','profile':profile,'requested_clip_count':duration//unit,'source_sha256':hashlib.sha256(raw).hexdigest(),'source_preserved':True,'clinical_facts_extracted':False,'media_generated':False,'render_readiness':'BLOCKED','next_action':'Read START_CASE_HERE.md; ground and review facts/script and fill actual dependencies.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case-id',required=True);p.add_argument('--source',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);p.add_argument('--profile',choices=PROFILES,default='FLOW_8S');p.add_argument('--duration',type=int,default=120);p.add_argument('--aspect',choices=['16:9','9:16'],default='16:9');p.add_argument('--clip-seconds',type=int);p.add_argument('--author',default='Operator not supplied');p.add_argument('--source-author');p.add_argument('--source-kind',choices=['ORIGINAL_CASE','DERIVATIVE'],default='ORIGINAL_CASE');a=p.parse_args()
    try:r=create_case(a.case_id,a.source,a.output_root,a.profile,a.duration,a.aspect,a.author,a.source_author,a.source_kind,a.clip_seconds)
    except (OSError,ValueError) as e:print(json.dumps({'stage':'BLOCKED','error':str(e),'media_generated':False}));return 2
    print(json.dumps(r,ensure_ascii=False,indent=2));return 0

if __name__=='__main__':raise SystemExit(main())
