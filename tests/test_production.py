"""Synthetic package tests; no data here is evidence of Flow/media execution."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validate_package',ROOT/'scripts/validate_package.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

def fixture():
    p=json.loads((ROOT/'assets/EMPTY_PACKAGE.json').read_text())
    cid=p['case_id'];prefix=cid+':'
    p['sources']=[{'id':prefix+'S01','kind':'ORIGINAL_CASE','title':'SYNTHETIC test source','author':'test author','locator':'test line 1','original_text':'Patient reports a symptom. No result supplied.','sha256':None,'accessed_at':None,'evidence_state':'TESTED','limitations':['Synthetic test only; not real patient evidence']}]
    p['facts']=[{'id':prefix+'F01','claim':'Patient reports a symptom.','category':'SUPPORTED','source_id':prefix+'S01','quote':'Patient reports a symptom.','locator':'test line 1','safe_to_use':'YES','clinical_review':'PENDING','notes':'Synthetic test'}]
    def asset(role,label,rr):
        return {'id':prefix+label+':v1','role':role,'description':'Synthetic test '+label,'reference_role':rr,'file':{'path':None,'library_file_id':None,'sha256':None,'version':'v1'},'depends_on':[],'fact_ids':[],'evidence_state':'PLANNED','approval_state':'PENDING','approval_event_id':None,'selection_evidence':[],'settings':{'platform':None,'preset':None,'flow_name':None,'performance':None,'sample_asset_id':None,'pronunciation':[]}}
    p['assets']=[asset('CHARACTER','P01','IDENTITY'),asset('VOICE','VP01','VOICE'),asset('ENVIRONMENT','ENV01','ENVIRONMENT'),asset('STYLE','STYLE01','STYLE_ONLY'),asset('KEYFRAME','K01','SCENE')]
    aid=[a['id'] for a in p['assets']]
    for i in range(1,16):
        p['clips'].append({'id':prefix+f'C{i:02d}','version':'v1','start_s':(i-1)*8,'end_s':i*8,'duration_s':8,'speaker_id':aid[0],'voice_asset_id':aid[1],'visible_character_ids':[aid[0]],'location_id':aid[2],'style_id':aid[3],'keyframe_id':aid[4],'asset_ids':aid[:],'dialogue_bn':'একটি উপসর্গ আছে।','spoken_fact_ids':[prefix+'F01'],'visual_fact_ids':[],'creative_choice_ids':[],'action':'Synthetic quiet seated pose','camera':'Static','transition':'Cut','audio_target_s':7,'speech_presentation':'LIPSYNC','negative_constraints':['No extra speech or facts'],'mute_character_ids':[],'audio_route':'NATIVE','audio_span_s':None,'audio_measurement_evidence':None,'audio_asset_id':None,'model':None,'mode':None,'resolution':None,'selection_evidence':[],'prompt_text':None,'prompt_sha256':None,'output_contract_sha256':None,'output':{'path':None,'library_file_id':None,'sha256':None,'version':'v1'},'evidence_state':'PLANNED','approval_state':'PENDING','approval_event_id':None,'qa':[],'blockers':[]})
    p['pilot_clip_ids']=[p['clips'][0]['id'],p['clips'][1]['id']]
    return p

class Regression(unittest.TestCase):
    def setUp(self):self.p=fixture()
    def result(self,stage='plan',clip=None):return v.validate(self.p,stage,clip)
    def fail(self):self.assertEqual(self.result()['structural_result'],'FAIL')
    def test_valid_draft_is_not_render_ready(self):
        r=self.result();self.assertEqual(r['structural_result'],'PASS');self.assertEqual(r['readiness'],'BLOCKED')
    def test_overlap(self):self.p['clips'][4]['start_s']=31;self.fail()
    def test_extra_intro(self):self.p['clips'].append(copy.deepcopy(self.p['clips'][0]));self.fail()
    def test_false_150_second_target(self):self.p['target']['clip_duration_s']=10;self.fail()
    def test_case14_leakage(self):self.p['assets'][0]['id']='CASE14:P01:v1';self.fail()
    def test_missing_fact(self):self.p['clips'][0]['spoken_fact_ids']=['CASE-NEW:F99'];self.fail()
    def test_invented_quote(self):self.p['facts'][0]['quote']='A specific artery was dissected.';self.fail()
    def test_excluded_fact(self):self.p['facts'][0]['category']='EXCLUDED';self.p['facts'][0]['safe_to_use']='NO';self.fail()
    def test_voice_is_not_just_a_label(self):self.p['clips'][0]['voice_asset_id']='VOICE_P01';self.fail()
    def test_missing_original(self):
        self.p['sources'][0]['kind']='DERIVATIVE';self.assertIn('Accessible original case text missing',self.result()['blockers'])
    def test_unsupported_claim_not_confirmed(self):
        self.p['facts'][0]['category']='UNCONFIRMED';self.fail()
    def test_long_speech(self):
        self.p['clips'][0]['audio_span_s']=7.8;self.p['clips'][0]['audio_measurement_evidence']='SYNTHETIC timecode measurement';self.assertTrue(any('exceeds' in b for b in self.result()['blockers']))
    def test_audio_container_is_not_speech_span(self):
        self.p['clips'][0]['audio_span_s']=6;self.fail()
    def test_prompt_hash(self):self.p['clips'][0]['prompt_text']='new text';self.p['clips'][0]['prompt_sha256']='0'*64;self.fail()
    def test_approval_not_inferred(self):self.p['clips'][0]['approval_state']='APPROVED';self.fail()
    def test_asset_cycle(self):self.p['assets'][0]['depends_on']=[self.p['assets'][0]['id']];self.fail()
    def test_style_cannot_be_identity(self):self.p['assets'][3]['reference_role']='IDENTITY';self.fail()
    def test_modified_script_stales_hash(self):
        self.p.update(v.content_hashes(self.p));self.p['clips'][0]['dialogue_bn']='পরিবর্তিত কথা।';self.fail()
    def test_no_unseen_final_pass(self):
        r=self.result('release');self.assertEqual(r['readiness'],'BLOCKED');self.assertTrue(any('assembly' in b for b in r['blockers']))
    def test_external_audio_is_not_preflighted_by_label(self):
        self.p['clips'][0]['audio_route']='EXTERNAL';r=self.result('render',self.p['clips'][0]['id']);self.assertTrue(any('audio' in b for b in r['blockers']))
    def test_unknown_schema_fields_fail(self):self.p['Flow_API_verified']=True;self.fail()

if __name__=='__main__':unittest.main()
