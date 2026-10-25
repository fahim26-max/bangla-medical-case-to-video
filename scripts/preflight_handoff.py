#!/usr/bin/env python3
"""Check a declared handoff. No clinical, attachment-authenticity or spend approval."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT_KEYS = {'handoff_schema_version','case_id','session_id','identity_locks','attachments','jobs'}
LOCK_KEYS = {'character_id','age_band','sex_presentation','description','demographic_basis','basis_evidence','approval_evidence'}
CAST_KEYS = {'character_id','age_band','sex_presentation','description'}
ATT_KEYS = {'asset_id','filename','role','availability','inspection_session_id','inspection_evidence','approval_evidence','local_path','sha256'}
JOB_KEYS = {'clip_id','characters','attachment_asset_ids','keyframe_asset_id','line_bn','line_sha256','prompt_text'}
ACCESS = {'DOCUMENTED_ONLY','LOCAL_AVAILABLE','ATTACHED_UNINSPECTED','INSPECTED_THIS_SESSION'}
ROLES = {'IDENTITY','SCENE','ENVIRONMENT','STYLE_ONLY','VOICE'}

def check(data, verify_files=False):
    errors, blockers = [], []
    def obj(value, keys, label):
        if not isinstance(value,dict) or set(value)!=keys:
            errors.append(label+': exact required keys missing or unknown keys present');return False
        return True
    def nonblank(x):return isinstance(x,str) and bool(x.strip())
    def optional_text(x):return x is None or nonblank(x)
    def texts(value, names, label):
        for k in names:
            if not nonblank(value[k]):errors.append(label+': '+k+' must be nonempty text')
    def result():
        return {'structural_result':'FAIL' if errors else 'PASS','handoff_state':'BLOCKED' if errors or blockers else 'CHECKED','errors':errors,'blockers':blockers,'render_permission':'NOT_GRANTED','clinical_qa':'NOT_TESTED','voice_and_dialogue_qa':'NOT_TESTED','boundary':'Declared identity/inventory checks do not authenticate attachments, approvals, clinical truth or actual media.'}
    if not obj(data,ROOT_KEYS,'root'):return result()
    if data['handoff_schema_version']!='1.0.0':errors.append('Unsupported handoff schema version')
    if not nonblank(data['case_id']):errors.append('case_id missing');return result()
    prefix=data['case_id']+':'
    if not optional_text(data['session_id']):errors.append('session_id must be text/null')
    if not data['session_id']:blockers.append('Actual planning session not recorded')
    for name in ['identity_locks','attachments','jobs']:
        if not isinstance(data[name],list):errors.append(name+' must be an array')
    if errors:return result()
    if not data['identity_locks'] or not data['jobs']:blockers.append('Identity locks and jobs have not been prepared')
    locks, attachments, ids = {}, {}, set()
    def ident(value,label):
        if not isinstance(value,str) or not value.startswith(prefix):errors.append(label+': cross-case or missing ID');return
        if value in ids:errors.append(label+': duplicate ID')
        ids.add(value)
    for i,lock in enumerate(data['identity_locks']):
        label=f'identity[{i}]'
        if not obj(lock,LOCK_KEYS,label):continue
        ident(lock['character_id'],label)
        texts(lock,['age_band','sex_presentation','description'],label)
        if not isinstance(lock['demographic_basis'],str) or lock['demographic_basis'] not in {'SOURCE_SUPPORTED','APPROVED_FICTIONAL','UNKNOWN'}:errors.append(label+': invalid demographic basis')
        for k in ['basis_evidence','approval_evidence']:
            if not optional_text(lock[k]):errors.append(label+': invalid '+k)
            if not lock[k]:blockers.append(label+': '+k+' missing')
        if lock['demographic_basis']=='UNKNOWN':blockers.append(label+': demographic basis unresolved')
        if isinstance(lock['character_id'],str):locks[lock['character_id']]=lock
    for i,a in enumerate(data['attachments']):
        label=f'attachment[{i}]'
        if not obj(a,ATT_KEYS,label):continue
        ident(a['asset_id'],label);texts(a,['filename'],label)
        if not isinstance(a['role'],str) or a['role'] not in ROLES or not isinstance(a['availability'],str) or a['availability'] not in ACCESS:errors.append(label+': invalid role/access state')
        for k in ['inspection_session_id','inspection_evidence','approval_evidence','local_path']:
            if not optional_text(a[k]):errors.append(label+': invalid '+k)
        if a['sha256'] is not None and (not isinstance(a['sha256'],str) or not re.fullmatch('[0-9a-f]{64}',a['sha256'])):errors.append(label+': invalid sha256')
        if isinstance(a['asset_id'],str):attachments[a['asset_id']]=a
    for i,job in enumerate(data['jobs']):
        label=f'job[{i}]'
        if not obj(job,JOB_KEYS,label):continue
        ident(job['clip_id'],label)
        if not isinstance(job['characters'],list) or not isinstance(job['attachment_asset_ids'],list):errors.append(label+': cast/attachments must be arrays');continue
        if not job['characters']:blockers.append(label+': visible cast contract empty')
        texts(job,['prompt_text'],label)
        if not isinstance(job['line_bn'],str):errors.append(label+': line must be text');continue
        if hashlib.sha256(job['line_bn'].encode()).hexdigest()!=job['line_sha256']:errors.append(label+': changed exact line/hash')
        if isinstance(job['prompt_text'],str):
            if job['line_bn'] not in job['prompt_text']:errors.append(label+': literal line absent from prompt')
            if re.search(r'\{\{|\}\}|same as (?:G\d|C\d|before|previous)',job['prompt_text'],re.I):errors.append(label+': placeholder or cross-job memory dependency')
        cast_ids=set()
        for c in job['characters']:
            if not obj(c,CAST_KEYS,label+' cast'):continue
            texts(c,CAST_KEYS,label+' cast')
            cid=c['character_id']
            if not isinstance(cid,str):continue
            if cid in cast_ids:errors.append(label+': duplicate visible character')
            cast_ids.add(cid);lock=locks.get(cid)
            if not lock:errors.append(label+': identity lock missing');continue
            if any(c[k]!=lock[k] for k in ['age_band','sex_presentation','description']):errors.append(label+': identity/demographics differ from frozen lock')
            if isinstance(job['prompt_text'],str) and isinstance(c['description'],str) and c['description'] not in job['prompt_text']:errors.append(label+': full identity omitted from prompt')
        if not isinstance(job['keyframe_asset_id'],str) or job['keyframe_asset_id'] not in job['attachment_asset_ids']:errors.append(label+': keyframe absent from selected attachments')
        for aid in job['attachment_asset_ids']:
            if not isinstance(aid,str):errors.append(label+': invalid attachment ID');continue
            a=attachments.get(aid)
            if not a:errors.append(label+': missing attachment record');continue
            if a['availability']!='INSPECTED_THIS_SESSION' or not data['session_id'] or a['inspection_session_id']!=data['session_id'] or not a['inspection_evidence']:blockers.append(label+': selected file not inspected in this planning session: '+aid)
            if not a['approval_evidence']:blockers.append(label+': selected asset approval evidence missing: '+aid)
            if aid==job['keyframe_asset_id'] and a['role']!='SCENE':errors.append(label+': keyframe role must be SCENE')
            if verify_files:
                try:
                    if not a['local_path'] or not a['sha256'] or hashlib.sha256(Path(a['local_path']).read_bytes()).hexdigest()!=a['sha256']:blockers.append(label+': local bytes/hash unavailable or mismatched: '+aid)
                except (OSError,TypeError,ValueError):blockers.append(label+': local file unavailable: '+aid)
    return result()

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('handoff',type=Path);p.add_argument('--verify-files',action='store_true');a=p.parse_args()
    try:r=check(json.loads(a.handoff.read_text(encoding='utf-8')),a.verify_files)
    except (OSError,ValueError) as e:print(json.dumps({'handoff_state':'BLOCKED','error':str(e),'render_permission':'NOT_GRANTED'}));return 2
    print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r['handoff_state']=='CHECKED' else 1

if __name__=='__main__':raise SystemExit(main())
