#!/usr/bin/env python3
"""Offline structure/readiness checks. Never validates clinical truth or controls Flow."""
import argparse
import hashlib
import json
from pathlib import Path

import jsonschema

SCHEMA = Path(__file__).resolve().parents[1] / 'references/production.schema.json'
CRITERIA = {'CLINICAL','IDENTITY','VOICE_BENGALI','LOCATION_STYLE','ANATOMY_ACTION','TIMING','CONTINUITY'}

def digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def content_hashes(p):
    clinical=digest({'sources':p['sources'],'facts':p['facts'],'unknowns':p['unknowns']})
    fields=('id','version','start_s','end_s','duration_s','speaker_id','dialogue_bn','spoken_fact_ids','visual_fact_ids','creative_choice_ids','action','camera','transition')
    script=digest({'target':p['target'],'clips':[{k:c[k] for k in fields} for c in p['clips']]})
    auth={k:x for k,x in p['render_authorization'].items() if k!='owner_approval_id'}
    production=digest({'script':script,'clip_contracts':{c['id']:clip_contract(p,c) for c in p['clips']},'authorization':auth})
    return {'clinical_sha256':clinical,'script_sha256':script,'production_sha256':production}

def clip_contract(p,c):
    fields=('id','version','start_s','end_s','duration_s','speaker_id','voice_asset_id','visible_character_ids','mute_character_ids','location_id','style_id','keyframe_id','asset_ids','dialogue_bn','spoken_fact_ids','visual_fact_ids','creative_choice_ids','action','camera','transition','audio_route','audio_target_s','speech_presentation','negative_constraints','audio_asset_id','model','mode','resolution','selection_evidence','prompt_text','prompt_sha256')
    assets={a['id']:a for a in p['assets']};required=set(c['asset_ids'])
    def expand(aid):
        for dep in assets.get(aid,{}).get('depends_on',[]):
            if dep not in required:required.add(dep);expand(dep)
    for aid in list(required):expand(aid)
    asset_fields=('id','role','description','reference_role','file','depends_on','fact_ids','settings')
    return digest({'clip':{k:c[k] for k in fields},'assets':[{k:assets[aid][k] for k in asset_fields} for aid in sorted(required) if aid in assets]})

def assembly_contract(p):
    return digest({'production':content_hashes(p)['production_sha256'],'outputs':[(c['id'],c['output']['sha256'],c['output_contract_sha256']) for c in p['clips']]})

def validate(p,stage='plan',clip_id=None):
    errors=[]; blockers=[]; warnings=[]
    schema=json.loads(SCHEMA.read_text())
    for e in jsonschema.Draft202012Validator(schema,format_checker=jsonschema.FormatChecker()).iter_errors(p):
        errors.append('/'+'/'.join(map(str,e.absolute_path))+': '+e.message)
    if errors:return {'structural_result':'FAIL','stage':stage,'errors':errors,'blockers':[],'warnings':[],'readiness':'BLOCKED'}
    cid=p['case_id']; prefix=cid+':'
    collections=['sources','facts','unknowns','creative_choices','assets','clips','approval_events','capabilities','attempts']
    ids=[]
    for key in collections:
        for row in p[key]:
            ids.append(row['id'])
            if not row['id'].startswith(prefix):errors.append('Cross-case ID: '+row['id'])
    if len(ids)!=len(set(ids)):errors.append('Duplicate IDs')
    src={r['id']:r for r in p['sources']};facts={r['id']:r for r in p['facts']}
    assets={r['id']:r for r in p['assets']};clips={r['id']:r for r in p['clips']}
    choices={r['id']:r for r in p['creative_choices']}; approvals={r['id']:r for r in p['approval_events']}
    def check_ref(value,table,label):
        if value is not None and value not in table:errors.append('Unknown '+label+': '+str(value))
    def has_approval(scope,sha=None,clinical=False):
        roles=('CLINICIAN','OWNER_CLINICIAN') if clinical else ('OWNER','OWNER_CLINICIAN')
        return any(a['decision']=='APPROVED' and scope in a['scope_ids'] and (not sha or a['artifact_sha256']==sha) and a['role'] in roles and a['actor'].strip() and a['at'] and a['evidence_ref'].strip() for a in p['approval_events'])
    def linked_approval(row,sha=None):
        a=approvals.get(row['approval_event_id'])
        return bool(a and a['decision']=='APPROVED' and row['id'] in a['scope_ids'] and (not sha or a['artifact_sha256']==sha) and a['role'] in ('OWNER','OWNER_CLINICIAN') and a['actor'].strip() and a['at'] and a['evidence_ref'].strip())
    for scope in ('clinical_scope_id','script_scope_id','production_scope_id','release_scope_id'):
        if not p[scope].startswith(prefix):errors.append('Cross-case scope: '+p[scope])
    for f in facts.values():
        check_ref(f['source_id'],src,'source')
        if f['safe_to_use']!='NO' and f['category'] in ('UNCONFIRMED','EXCLUDED'):errors.append('Unsafe fact promoted: '+f['id'])
        if f['category']=='DRAMATIZED' and f['safe_to_use']!='NO':errors.append('Use creative_choices for harmless staging; dramatized medical facts cannot be promoted: '+f['id'])
        if f['category'] in ('SUPPORTED','ATTRIBUTED') and (not f['source_id'] or not f['quote'] or not f['locator']):errors.append('Missing claim provenance: '+f['id'])
        s=src.get(f['source_id'])
        if s and s['original_text'] is not None and f['quote'] and f['quote'] not in s['original_text']:errors.append('Quote does not match source: '+f['id'])
    for a in assets.values():
        if not a['id'].endswith(':'+a['file']['version']):errors.append('Asset version/ID mismatch: '+a['id'])
        for dep in a['depends_on']:check_ref(dep,assets,'asset dependency')
        for f in a['fact_ids']:check_ref(f,facts,'asset fact')
        if a['role']=='STYLE' and a['reference_role']!='STYLE_ONLY':errors.append('Style reference must be STYLE_ONLY: '+a['id'])
        if a['approval_state']=='APPROVED' and not linked_approval(a,a['file']['sha256']):errors.append('Asset approval receipt missing/mismatched: '+a['id'])
    visiting=set();done=set()
    def visit(aid):
        if aid in visiting:errors.append('Asset dependency cycle: '+aid);return
        if aid in done or aid not in assets:return
        visiting.add(aid)
        for dep in assets[aid]['depends_on']:visit(dep)
        visiting.remove(aid);done.add(aid)
    for aid in assets:visit(aid)
    target=p['target'];dur=target['clip_duration_s']
    if target['clip_count']*dur!=target['duration_s']:errors.append('Target arithmetic mismatch')
    if len(p['clips'])!=target['clip_count']:errors.append('Manifest row count mismatch')
    expected_start=0
    for i,c in enumerate(p['clips'],1):
        if c['id']!=prefix+f'C{i:02d}':errors.append('Clip order/ID mismatch: '+c['id'])
        if abs(c['start_s']-expected_start)>1e-6 or abs(c['end_s']-c['start_s']-c['duration_s'])>1e-6 or c['duration_s']!=dur:errors.append('Timeline gap/overlap/duration: '+c['id'])
        expected_start=c['end_s']
        for k in ('speaker_id','voice_asset_id','location_id','style_id','keyframe_id','audio_asset_id'):check_ref(c[k],assets,k)
        for a in c['visible_character_ids']+c['mute_character_ids']+c['asset_ids']:check_ref(a,assets,'clip asset')
        if not set(c['mute_character_ids']).issubset(c['visible_character_ids']):errors.append('Mute cast not visible: '+c['id'])
        if c['speaker_id'] in c['mute_character_ids']:errors.append('Speaker also mute: '+c['id'])
        if c['speaker_id'] and set(c['visible_character_ids'])-{c['speaker_id']} != set(c['mute_character_ids']):errors.append('Other visible characters must be explicitly mute: '+c['id'])
        for f in c['spoken_fact_ids']+c['visual_fact_ids']:
            check_ref(f,facts,'clip fact')
            if f in facts and facts[f]['safe_to_use']=='NO':errors.append('Disallowed fact in clip: '+c['id']+' / '+f)
        for x in c['creative_choice_ids']:check_ref(x,choices,'creative choice')
        for a in c['visible_character_ids']:
            if a in assets and assets[a]['role']!='CHARACTER':errors.append('Visible cast is not CHARACTER: '+a)
        required_refs=[c[k] for k in ('speaker_id','voice_asset_id','location_id','style_id','keyframe_id','audio_asset_id') if c[k] is not None]+c['visible_character_ids']
        if not set(required_refs).issubset(c['asset_ids']):errors.append('Missing frozen clip dependencies: '+c['id'])
        roles={'speaker_id':'CHARACTER','voice_asset_id':'VOICE','location_id':'ENVIRONMENT','style_id':'STYLE','keyframe_id':'KEYFRAME','audio_asset_id':'AUDIO'}
        for k,role in roles.items():
            if c[k] in assets and assets[c[k]]['role']!=role:errors.append('Wrong asset role '+k+': '+c['id'])
        if c['audio_route']=='SILENT':
            if c['dialogue_bn'] or c['speaker_id'] or c['voice_asset_id']:errors.append('Silent clip has speech: '+c['id'])
            if c['speech_presentation']!='SILENT':errors.append('Silent presentation mismatch: '+c['id'])
        elif not c['dialogue_bn'] or not c['speaker_id'] or not c['voice_asset_id']:errors.append('Speaking clip lacks line/speaker/voice: '+c['id'])
        elif c['speech_presentation']=='SILENT':errors.append('Speech presentation mismatch: '+c['id'])
        if c['speech_presentation']=='LIPSYNC' and c['speaker_id'] not in c['visible_character_ids']:errors.append('Lip-sync speaker not visible: '+c['id'])
        if c['audio_target_s']>c['duration_s']-1:errors.append('Audio target leaves inadequate margin: '+c['id'])
        if c['audio_route']=='EXTERNAL' and c['audio_asset_id'] is None:blockers.append(c['id']+': external master audio missing')
        if c['audio_span_s'] is not None and c['audio_span_s']>c['audio_target_s']:blockers.append(c['id']+': speech exceeds target')
        if c['audio_span_s'] is not None and not c['audio_measurement_evidence']:errors.append('Audio measurement lacks evidence: '+c['id'])
        if c['prompt_text'] is not None:
            actual=hashlib.sha256(c['prompt_text'].encode()).hexdigest()
            if c['prompt_sha256']!=actual:errors.append('Prompt hash mismatch: '+c['id'])
        if c['approval_state']=='APPROVED' and not linked_approval(c,c['output']['sha256']):errors.append('Clip approval receipt missing/mismatched: '+c['id'])
        qas=[q['criterion'] for q in c['qa']]
        if len(qas)!=len(set(qas)):errors.append('Duplicate QA criterion: '+c['id'])
    if abs(expected_start-target['duration_s'])>1e-6:errors.append('Manifest total mismatch')
    for pid in p['pilot_clip_ids']:check_ref(pid,clips,'pilot clip')
    hashes=content_hashes(p)
    for k,h in hashes.items():
        if p[k] is not None and p[k]!=h:errors.append('Stale '+k)
    if not any(s['kind']=='ORIGINAL_CASE' and s['original_text'] for s in p['sources']):blockers.append('Accessible original case text missing')
    for u in p['unknowns']:
        if u['resolution'] is None and u['impact']=='RENDER':blockers.append('Unresolved render blocker '+u['id']+': '+u['question'])
    if not p['clinical_sha256'] or not has_approval(p['clinical_scope_id'],p['clinical_sha256'],True):blockers.append('Clinical approval for exact fact version missing')
    if not p['script_sha256'] or not has_approval(p['script_scope_id'],p['script_sha256']):blockers.append('Script approval for exact script version missing')

    def clip_ready(c):
        b=[]
        b.extend('Explicit blocker: '+x for x in c['blockers'])
        auth=p['render_authorization'];aa=approvals.get(auth['owner_approval_id'])
        if c['id'] not in auth['authorized_clip_ids']:b.append('Clip outside authorized credit scope')
        if auth['quoted_credits_per_output'] is None or auth['max_total_credits'] is None or not auth['current_quote_evidence']:b.append('Current credit quote/bounded budget missing')
        elif auth['max_total_credits']<auth['quoted_credits_per_output']:b.append('Budget below one quoted output')
        spent=sum(a['charged_credits'] or 0 for a in p['attempts'])
        if stage=='render' and any(a['result']!='PLANNED' and a['charged_credits'] is None for a in p['attempts']):b.append('Prior actual charges unknown; reconcile budget before spending')
        if auth['quoted_credits_per_output'] is not None and auth['max_total_credits'] is not None and stage=='render' and spent+auth['quoted_credits_per_output']>auth['max_total_credits']:b.append('Remaining authorized budget insufficient')
        if not aa or aa['decision']!='APPROVED' or aa['role'] not in ('OWNER','OWNER_CLINICIAN') or not aa['actor'].strip() or not aa['at'] or not aa['evidence_ref'].strip() or p['production_scope_id'] not in aa['scope_ids'] or aa['artifact_sha256']!=p['production_sha256']:b.append('Owner budget authorization for current production contract missing')
        attempts=[a for a in p['attempts'] if a['clip_id']==c['id'] and a['result']!='PLANNED']
        if stage=='render' and len(attempts)>=auth['max_attempts_per_clip']:b.append('Authorized attempt limit reached')
        caps=[x for x in p['capabilities'] if x['scope'] in (c['id'],p['production_scope_id'])]
        if any(x['evidence_state']=='FAILED' for x in caps):b.append('Required capability is FAILED')
        if not any(x['evidence_state'] in ('VERIFIED','USER-APPROVED') and x['evidence'] for x in caps):b.append('Current mode/reference/voice capability evidence missing')
        required=set(c['asset_ids'])
        def include_dependencies(aid):
            for dep in assets.get(aid,{}).get('depends_on',[]):
                if dep not in required:required.add(dep);include_dependencies(dep)
        for aid in list(required):include_dependencies(aid)
        for aid in required:
            a=assets.get(aid)
            if not a:continue
            if a['approval_state']!='APPROVED' or not a['file']['sha256'] or not linked_approval(a,a['file']['sha256']):b.append('Unapproved/unfrozen asset '+aid)
            if a['evidence_state']=='FAILED':b.append('Failed asset '+aid)
            for fid in a['fact_ids']:
                f=facts.get(fid)
                if f and (f['safe_to_use']=='NO' or f['category'] in ('UNCONFIRMED','EXCLUDED','DRAMATIZED') or f['clinical_review']!='APPROVED'):b.append('Unsafe/unreviewed clinical content in referenced asset '+aid+' / '+fid)
        for fid in c['spoken_fact_ids']+c['visual_fact_ids']:
            f=facts.get(fid)
            if f and f['clinical_review']!='APPROVED':b.append('Clinical fact not approved '+fid)
        if not c['keyframe_id'] or not c['location_id'] or not c['style_id']:b.append('Frame/environment/style missing')
        if not c['model'] or not c['mode'] or not c['resolution'] or not c['selection_evidence']:b.append('Actual setting selection evidence missing')
        if not c['prompt_text'] or '{{' in c['prompt_text'] or '}}' in c['prompt_text']:b.append('Exact completed prompt missing')
        if c['audio_route']=='EXTERNAL' and (c['audio_span_s'] is None or not c['audio_measurement_evidence']):b.append('External audio not measured')
        if c['id'] not in p['pilot_clip_ids']:
            if len(set(p['pilot_clip_ids']))<2:b.append('Two representative pilots not designated')
            for pid in p['pilot_clip_ids']:
                pc=clips.get(pid)
                if not pc or pc['approval_state']!='APPROVED' or not pc['output']['sha256'] or not linked_approval(pc,pc['output']['sha256']):b.append('Pilot not approved '+pid)
                elif pilot_problems(pc):b.extend('Pilot '+pid+': '+x for x in pilot_problems(pc))
            coverage={(clips[pid]['speaker_id'],clips[pid]['location_id']) for pid in p['pilot_clip_ids'] if pid in clips}
            if len(coverage)<2:b.append('Pilots lack distinct representative speaker/location coverage')
            pcs=[clips[pid] for pid in p['pilot_clip_ids'] if pid in clips]
            if c['location_id'] not in {pc['location_id'] for pc in pcs}:b.append('New location requires a targeted pilot')
            if c['voice_asset_id'] and c['voice_asset_id'] not in {pc['voice_asset_id'] for pc in pcs}:b.append('New voice requires a targeted pilot')
            if c['style_id'] not in {pc['style_id'] for pc in pcs}:b.append('New style requires a targeted pilot')
            visible={a for pc in pcs for a in pc['visible_character_ids']}
            if not set(c['visible_character_ids']).issubset(visible):b.append('New visible identity requires a targeted pilot')
            if not has_approval(p['production_scope_id'],p['production_sha256']):b.append('Production authorization for current render contract missing')
        elif not has_approval(c['id']+':render',c['prompt_sha256']):b.append('Pilot render authorization missing')
        return [c['id']+': '+x for x in b]

    def pilot_problems(c):
        b=[];qas={q['criterion']:q for q in c['qa']}
        if set(qas)!=CRITERIA:b.append('Full seven-criterion QA missing')
        for q in c['qa']:
            if q['result'] not in ('PASS','EXCEPTION') or not q['evidence'] or not q['reviewer']:b.append('Unpassed '+q['criterion'])
            if q['result']=='EXCEPTION' and not valid_exception(c,q):b.append('Invalid exact-output exception')
        if c['audio_route']!='SILENT' and (c['audio_span_s'] is None or not c['audio_measurement_evidence'] or c['audio_span_s']>c['audio_target_s']):b.append('Spoken span missing/overlong')
        if c['output_contract_sha256']!=clip_contract(p,c):b.append('Output bound to stale/unknown generation contract')
        a=approvals.get(c['approval_event_id'])
        if not a or a['contract_sha256']!=clip_contract(p,c):b.append('Approval bound to stale/unknown generation contract')
        b.extend(c['blockers'])
        return b

    def valid_exception(c,q):
        a=approvals.get(q['exception_approval_id'])
        return bool(q['criterion'] not in ('CLINICAL','IDENTITY','VOICE_BENGALI') and a and a['decision']=='APPROVED' and a['role'] in ('OWNER','OWNER_CLINICIAN') and a['actor'].strip() and a['at'] and a['evidence_ref'].strip() and a['artifact_sha256']==c['output']['sha256'] and a['contract_sha256']==clip_contract(p,c) and c['id'] in a['scope_ids'] and a['exceptions'])
    selected=[clips[clip_id]] if clip_id in clips else p['clips']
    if clip_id and clip_id not in clips:errors.append('Unknown selected clip '+clip_id)
    if stage in ('render','release'):
        for c in selected:blockers.extend(clip_ready(c))
    if stage=='render' and clip_id is None:
        auth=p['render_authorization'];quote=auth['quoted_credits_per_output'];budget=auth['max_total_credits'];spent=sum(a['charged_credits'] or 0 for a in p['attempts'])
        if quote is not None and budget is not None and spent+len(selected)*quote>budget:blockers.append('Aggregate selected output cost exceeds authorized remaining budget')
    if stage=='release':
        for c in p['clips']:
            blockers.extend(c['id']+': '+x for x in pilot_problems(c))
            if not c['output']['sha256'] or c['approval_state']!='APPROVED':blockers.append(c['id']+': approved actual export missing')
            if {q['criterion'] for q in c['qa']}!=CRITERIA:blockers.append(c['id']+': full QA coverage missing')
            for q in c['qa']:
                if q['result'] not in ('PASS','EXCEPTION') or not q['evidence'] or not q['reviewer']:blockers.append(c['id']+': incomplete QA '+q['criterion'])
                if q['result']=='EXCEPTION':
                    if not valid_exception(c,q):blockers.append(c['id']+': invalid exception')
            if c['audio_route']!='SILENT' and (c['audio_span_s'] is None or not c['audio_measurement_evidence']):blockers.append(c['id']+': speech span not measured')
        a=p['assembly']
        if a['input_contract_sha256']!=assembly_contract(p):blockers.append('Assembly bound to stale/unknown clip inputs')
        if not a['output']['sha256'] or a['duration_s'] is None or abs(a['duration_s']-target['duration_s'])>1/24 or a['qa_result']!='PASS' or not a['review_evidence']:blockers.append('Actual full assembly review/duration missing')
        if a['release_state']!='APPROVED' or not has_approval(p['release_scope_id'],a['output']['sha256'],True):blockers.append('Clinician final release approval missing')
        if not has_approval(p['release_scope_id'],a['output']['sha256']):blockers.append('Owner final release approval missing')
        for u in p['unknowns']:
            if not u['resolution'] and u['impact']=='RELEASE':blockers.append('Unresolved release blocker '+u['id'])
    warnings.append('Structural checks do not verify clinical truth, hidden visual claims, human identity/voice judgement or approval authenticity.')
    return {'structural_result':'FAIL' if errors else 'PASS','stage':stage,'errors':errors,'blockers':sorted(set(blockers)),'warnings':warnings,'readiness':'BLOCKED' if errors or blockers else 'READY_FOR_REQUESTED_STAGE','computed_hashes':hashes}

def main():
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('package',type=Path);a.add_argument('--stage',choices=['plan','render','release'],default='plan');a.add_argument('--clip');args=a.parse_args()
    r=validate(json.loads(args.package.read_text()),args.stage,args.clip);print(json.dumps(r,indent=2,ensure_ascii=False))
    return 1 if r['errors'] or (args.stage!='plan' and r['blockers']) else 0
if __name__=='__main__':raise SystemExit(main())
