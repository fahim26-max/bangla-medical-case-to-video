"""Adversarial readiness checks using explicitly synthetic evidence, not real media."""
import copy
import hashlib
import unittest
from test_production import fixture, v

def h(s):return hashlib.sha256(s.encode()).hexdigest()

def ready():
    p=fixture();prefix=p['case_id']+':'
    def approve(scope,sha,role='OWNER',contract=None):
        aid=prefix+f'A{len(p["approval_events"])+1:03d}'
        p['approval_events'].append({'id':aid,'scope_ids':[scope],'artifact_sha256':sha,'contract_sha256':contract,'decision':'APPROVED','actor':'SYNTHETIC reviewer','role':role,'at':'2026-10-21T12:00:00+06:00','evidence_ref':'SYNTHETIC unit-test receipt only','exceptions':[],'scope_note':'Not a real approval'})
        return aid
    p['facts'][0]['clinical_review']='APPROVED'
    doctor=copy.deepcopy(p['assets'][0]);doctor['id']=prefix+'D01:v1';doctor['description']='SYNTHETIC clinician identity';p['assets'].append(doctor)
    c=p['clips'][1];c['speaker_id']=doctor['id'];c['visible_character_ids']=[doctor['id']];c['asset_ids'].append(doctor['id'])
    for a in p['assets']:
        a['file']['sha256']=h(a['id']);a['approval_state']='APPROVED';a['evidence_state']='USER-APPROVED';a['approval_event_id']=approve(a['id'],a['file']['sha256'])
    ev={'ref':'SYNTHETIC UI evidence','criterion':'Current selected model/mode/reference/voice combination','scope':p['production_scope_id'],'reviewer':'SYNTHETIC operator','at':'2026-10-21T12:00:00+06:00'}
    p['capabilities']=[{'id':prefix+'CAP01','claim':'SYNTHETIC supported combination','scope':p['production_scope_id'],'evidence_state':'VERIFIED','evidence':[ev],'limitations':['Unit fixture only']}]
    p['render_authorization'].update(quoted_credits_per_output=1,max_total_credits=100,current_quote_evidence='SYNTHETIC quote',authorized_clip_ids=[c['id'] for c in p['clips']])
    for c in p['clips']:
        c.update(model='SYNTHETIC model',mode='SYNTHETIC native',resolution='720p',selection_evidence=[ev],prompt_text='SYNTHETIC prompt '+c['id'],audio_span_s=6,audio_measurement_evidence='SYNTHETIC spoken interval')
        c['prompt_sha256']=h(c['prompt_text'])
        c['output']['sha256']=h(c['id']+'output');c['output_contract_sha256']=v.clip_contract(p,c);c['approval_state']='APPROVED';c['approval_event_id']=approve(c['id'],c['output']['sha256'],contract=c['output_contract_sha256'])
        c['qa']=[{'criterion':q,'result':'PASS','timecodes':'00:00-00:08','evidence':'SYNTHETIC QA','reviewer':'SYNTHETIC reviewer','exception_approval_id':None} for q in sorted(v.CRITERIA)]
        approve(c['id']+':render',c['prompt_sha256'])
    p.update(v.content_hashes(p));approve(p['clinical_scope_id'],p['clinical_sha256'],'CLINICIAN');approve(p['script_scope_id'],p['script_sha256'])
    p['render_authorization']['owner_approval_id']=approve(p['production_scope_id'],p['production_sha256'])
    p['assembly'].update(output={'path':None,'library_file_id':None,'sha256':h('SYNTHETIC final'),'version':'v1'},duration_s=120,qa_result='PASS',review_evidence='SYNTHETIC full film review',release_state='APPROVED',input_contract_sha256=v.assembly_contract(p))
    approve(p['release_scope_id'],p['assembly']['output']['sha256'],'OWNER_CLINICIAN')
    return p

class Gates(unittest.TestCase):
    def setUp(self):self.p=ready()
    def result(self,stage='render'):return v.validate(self.p,stage,'CASE-NEW:C03' if stage=='render' else None)
    def blocked(self,stage='render'):self.assertEqual(self.result(stage)['readiness'],'BLOCKED')
    def test_synthetic_positive_render(self):self.assertEqual(self.result()['readiness'],'READY_FOR_REQUESTED_STAGE',self.result())
    def test_synthetic_positive_release(self):self.assertEqual(self.result('release')['readiness'],'READY_FOR_REQUESTED_STAGE',self.result('release'))
    def test_failed_pilot(self):self.p['clips'][0]['qa'][0]['result']='FAIL';self.blocked()
    def test_pilot_unmeasured(self):self.p['clips'][0]['audio_span_s']=None;self.blocked()
    def test_pilot_missing_qa(self):self.p['clips'][0]['qa']=[];self.blocked()
    def test_identical_pilot_coverage(self):self.p['pilot_clip_ids']=['CASE-NEW:C01','CASE-NEW:C04'];self.blocked()
    def test_explicit_blocker(self):self.p['clips'][2]['blockers']=['Critical clinical error'];self.blocked()
    def test_failed_capability(self):self.p['capabilities'][0]['evidence_state']='FAILED';self.blocked()
    def test_missing_budget(self):self.p['render_authorization']['max_total_credits']=None;self.blocked()
    def test_clinician_cannot_authorize_credits(self):
        aid=self.p['render_authorization']['owner_approval_id'];next(a for a in self.p['approval_events'] if a['id']==aid)['role']='CLINICIAN';self.blocked()
    def test_unsourced_dramatized_medical_fact(self):
        self.p['facts'][0].update(category='DRAMATIZED',source_id=None,quote=None,locator=None,claim='CTA confirms dissection');self.blocked()
    def test_new_prompt_stales_output(self):
        c=self.p['clips'][2];c['prompt_text']='SYNTHETIC changed prompt';c['prompt_sha256']=h(c['prompt_text']);self.p.update(v.content_hashes(self.p));self.blocked('release')
    def test_new_model_stales_output(self):self.p['clips'][2]['model']='SYNTHETIC other model';self.blocked('release')
    def test_changed_master_hash_stales_output(self):self.p['assets'][0]['file']['sha256']='f'*64;self.blocked('release')
    def test_rejected_nonowner_exception(self):
        c=self.p['clips'][2];a=copy.deepcopy(self.p['approval_events'][-1]);a.update(id='CASE-NEW:A999',scope_ids=[c['id']],artifact_sha256=c['output']['sha256'],contract_sha256=v.clip_contract(self.p,c),decision='REJECTED',role='CLINICIAN',evidence_ref='',exceptions=['Rejected deviation']);self.p['approval_events'].append(a)
        next(q for q in c['qa'] if q['criterion']=='LOCATION_STYLE').update(result='EXCEPTION',exception_approval_id=a['id']);self.blocked('release')
    def test_changed_assembly_input(self):self.p['assembly']['input_contract_sha256']='0'*64;self.blocked('release')
    def test_asset_clinical_claim_cannot_bypass_clip_map(self):
        f=copy.deepcopy(self.p['facts'][0]);f.update(id='CASE-NEW:F02',category='UNCONFIRMED',safe_to_use='NO',clinical_review='REJECTED');self.p['facts'].append(f);self.p['assets'][4]['fact_ids']=[f['id']];self.p.update(v.content_hashes(self.p));self.blocked()
    def test_new_location_requires_pilot(self):
        a=copy.deepcopy(self.p['assets'][2]);a['id']='CASE-NEW:ENV02:v1';self.p['assets'].append(a);c=self.p['clips'][2];c['location_id']=a['id'];c['asset_ids'].append(a['id']);self.blocked()
    def test_batch_budget_is_aggregate(self):
        self.p['render_authorization']['max_total_credits']=1;self.p.update(v.content_hashes(self.p));aid=self.p['render_authorization']['owner_approval_id'];next(a for a in self.p['approval_events'] if a['id']==aid)['artifact_sha256']=self.p['production_sha256'];r=v.validate(self.p,'render');self.assertIn('Aggregate selected output cost exceeds authorized remaining budget',r['blockers'])
    def test_final_owner_receipt_needs_evidence(self):
        a=self.p['approval_events'][-1];a.update(role='CLINICIAN');owner=copy.deepcopy(a);owner.update(id='CASE-NEW:A999',role='OWNER',actor='',evidence_ref='',at=None);self.p['approval_events'].append(owner);self.blocked('release')
    def test_unknown_prior_charge_not_assumed_zero(self):
        self.p['attempts']=[{'id':'CASE-NEW:T001','clip_id':'CASE-NEW:C03','take':1,'prompt_sha256':None,'output_sha256':None,'quoted_credits':1,'charged_credits':None,'at':None,'failure_class':'VOICE','result':'FAILED','evidence_ref':'SYNTHETIC attempt'}];self.blocked()

if __name__=='__main__':unittest.main()
