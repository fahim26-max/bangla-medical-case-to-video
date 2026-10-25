"""Synthetic workflow/package regression; no app/medical-media approval evidence."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
starter=module('new_case');handoff=module('preflight_handoff');pack=module('package_skill')

def sample():
    cid='CASE-TEST';desc='Synthetic adult male in neutral clothing; not an actual person.'
    lock={'character_id':cid+':P01','age_band':'adult','sex_presentation':'male','description':desc,'demographic_basis':'SOURCE_SUPPORTED','basis_evidence':'SYNTHETIC source quote','approval_evidence':'SYNTHETIC receipt, not real approval'}
    attachment={'asset_id':cid+':K01','filename':'synthetic.png','role':'SCENE','availability':'INSPECTED_THIS_SESSION','inspection_session_id':'SYNTHETIC-session','inspection_evidence':'SYNTHETIC test attestation','approval_evidence':'SYNTHETIC receipt','local_path':None,'sha256':None}
    line='এটি পরীক্ষার নমুনা।'
    job={'clip_id':cid+':C01','characters':[{k:lock[k] for k in handoff.CAST_KEYS}],'attachment_asset_ids':[attachment['asset_id']],'keyframe_asset_id':attachment['asset_id'],'line_bn':line,'line_sha256':hashlib.sha256(line.encode()).hexdigest(),'prompt_text':desc+' Exact: '+line}
    return {'handoff_schema_version':'1.0.0','case_id':cid,'session_id':'SYNTHETIC-session','identity_locks':[lock],'attachments':[attachment],'jobs':[job]}

class CaseStarter(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.base=Path(self.tmp.name);self.source=self.base/'actual_source.txt';self.raw='একজন নারীর দুই দিনের মাথাব্যথা। আর কিছু জানানো হয়নি।\r\n'.encode();self.source.write_bytes(self.raw)
    def create(self,cid='CASE-ONE',**kw):return starter.create_case(cid,self.source,self.base/'cases',**kw)
    def test_source_bytes_and_no_invented_facts(self):
        r=self.create();d=Path(r['case_directory']);self.assertEqual((d/'00_sources'/self.source.name).read_bytes(),self.raw)
        p=json.loads((d/'01_evidence/production_package_v001.json').read_text());self.assertEqual(p['facts'],[]);self.assertEqual(p['clips'],[]);self.assertEqual(p['approval_events'],[]);self.assertEqual(p['stage'],'INTAKE');self.assertFalse(r['media_generated']);self.assertIsNone(p['sources'][0]['author']);self.assertEqual(p['sources'][0]['sha256'],hashlib.sha256(self.raw).hexdigest())
    def test_all_profiles_and_math(self):
        for i,profile in enumerate(starter.PROFILES):
            r=self.create(f'CASE-{i}',profile=profile,clip_seconds=8 if profile=='VIDS_ASSEMBLY' else None)
            self.assertEqual(r['requested_clip_count'],15 if profile.endswith('8S') or profile=='VIDS_ASSEMBLY' else 12)
    def test_no_overwrite(self):
        self.create()
        with self.assertRaises(FileExistsError):self.create()
    def test_case_path_traversal_rejected(self):
        with self.assertRaises(ValueError):self.create('../CASE-EVIL')
    def test_nondivisible_runtime_rejected(self):
        with self.assertRaises(ValueError):self.create(duration=121)
    def test_assembly_requires_explicit_unit(self):
        with self.assertRaises(ValueError):self.create(profile='VIDS_ASSEMBLY')
    def test_missing_source_no_case_created(self):
        self.source.unlink()
        with self.assertRaises(FileNotFoundError):self.create()
        self.assertFalse((self.base/'cases/CASE-ONE').exists())
    def test_all_templates_created_and_case_scoped(self):
        d=Path(self.create()['case_directory']);self.assertTrue((d/'05_jobs/handoff_v001.json').exists());self.assertTrue((d/'08_final/EDIT_PLAN_v001.md').exists())
        for f in d.rglob('*.md'):
            self.assertNotIn('{{CASE_ID}}',f.read_text());self.assertNotIn('CASE14',f.read_text())
    def test_conflicting_unit_rejected(self):
        with self.assertRaises(ValueError):self.create(profile='FLOW_8S',clip_seconds=10)
    def test_binary_not_claimed_as_extracted_text(self):
        f=self.base/'case.pdf';f.write_bytes(b'%PDF-1.0')
        with self.assertRaises(ValueError):starter.create_case('CASE-PDF',f,self.base/'cases')

class Handoff(unittest.TestCase):
    def setUp(self):self.p=sample()
    def test_scoped_pass_never_grants_render(self):
        r=handoff.check(self.p);self.assertEqual(r['handoff_state'],'CHECKED');self.assertEqual(r['render_permission'],'NOT_GRANTED');self.assertEqual(r['clinical_qa'],'NOT_TESTED')
    def test_male_to_female_drift_fails(self):
        self.p['jobs'][0]['characters'][0]['sex_presentation']='female';self.assertEqual(handoff.check(self.p)['structural_result'],'FAIL')
    def test_new_female_case_does_not_inherit_fixture(self):
        self.p['identity_locks'][0]['sex_presentation']='female';self.p['jobs'][0]['characters'][0]['sex_presentation']='female';desc='Synthetic adult female; not a real patient.';self.p['identity_locks'][0]['description']=desc;self.p['jobs'][0]['characters'][0]['description']=desc;self.p['jobs'][0]['prompt_text']=desc+self.p['jobs'][0]['line_bn'];self.assertEqual(handoff.check(self.p)['handoff_state'],'CHECKED')
    def test_age_drift_fails(self):
        self.p['jobs'][0]['characters'][0]['age_band']='elderly';self.assertEqual(handoff.check(self.p)['structural_result'],'FAIL')
    def test_documented_only_is_not_present(self):
        self.p['attachments'][0]['availability']='DOCUMENTED_ONLY';self.assertEqual(handoff.check(self.p)['handoff_state'],'BLOCKED')
    def test_old_session_inspection_not_current(self):
        self.p['attachments'][0]['inspection_session_id']='other';self.assertEqual(handoff.check(self.p)['handoff_state'],'BLOCKED')
    def test_same_as_previous_not_self_contained(self):
        self.p['jobs'][0]['prompt_text']='same as G01 '+self.p['jobs'][0]['line_bn'];self.assertEqual(handoff.check(self.p)['structural_result'],'FAIL')
    def test_changed_dialogue_hash(self):
        self.p['jobs'][0]['line_bn']='বদলে গেছে।';self.assertEqual(handoff.check(self.p)['structural_result'],'FAIL')
    def test_missing_keyframe(self):
        self.p['jobs'][0]['attachment_asset_ids']=[];self.assertEqual(handoff.check(self.p)['structural_result'],'FAIL')
    def test_empty_template_correctly_blocks(self):
        p=json.loads((ROOT/'assets/HANDOFF_TEMPLATE.json').read_text());r=handoff.check(p);self.assertEqual(r['structural_result'],'PASS');self.assertEqual(r['handoff_state'],'BLOCKED')
    def test_duplicate_job_id_fails(self):
        self.p['jobs'].append(copy.deepcopy(self.p['jobs'][0]));self.assertEqual(handoff.check(self.p)['structural_result'],'FAIL')
    def test_invalid_member_types_do_not_crash(self):
        for key in ['role','availability']:
            p=copy.deepcopy(self.p);p['attachments'][0][key]={};self.assertEqual(handoff.check(p)['structural_result'],'FAIL')
        self.p['identity_locks'][0]['demographic_basis']=[];self.assertEqual(handoff.check(self.p)['structural_result'],'FAIL')
    def test_local_byte_hash_mismatch_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/'test.png';f.write_bytes(b'synthetic bytes, not a real image');self.p['attachments'][0].update(local_path=str(f),sha256='0'*64);self.assertEqual(handoff.check(self.p,True)['handoff_state'],'BLOCKED')
    def test_cross_case_identifier_fails(self):
        self.p['jobs'][0]['clip_id']='CASE14:C01';self.assertEqual(handoff.check(self.p)['structural_result'],'FAIL')

class Packaging(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.base=Path(self.tmp.name);self.root=self.base/'skill';self.root.mkdir()
        for n in pack.REQUIRED:
            f=self.root/n;f.parent.mkdir(parents=True,exist_ok=True);f.write_text('Fixture only.\n')
        (self.root/'SKILL.md').write_text('---\nname: test-skill\nmetadata:\n  version: 1.0.0\n---\n# Test (v1.0.0)\n')
        (self.root/'README.md').write_text('**Version:** 1.0.0\n');(self.root/'CHANGELOG.md').write_text('## [1.0.0] - 2026-10-21\n');(self.root/'agents/openai.yaml').write_text('version: "1.0.0"\n')
    def test_zip_integrity_root_hashes_and_cache_exclusion(self):
        c=self.root/'__pycache__/bad.pyc';c.parent.mkdir();c.write_bytes(b'junk');out=self.base/'one.zip';r=pack.build(self.root,out)
        with zipfile.ZipFile(out) as z:
            self.assertIsNone(z.testzip());self.assertIn('test-skill/SKILL.md',z.namelist());self.assertFalse(any('__pycache__' in n for n in z.namelist()));m=json.loads(z.read('test-skill/PACKAGE_MANIFEST.json'));self.assertEqual(m['skill_version'],'1.0.0')
            for n,rec in m['files'].items():self.assertEqual(hashlib.sha256(z.read('test-skill/'+n)).hexdigest(),rec['sha256'])
        self.assertEqual(r['installation'],'NOT_TESTED')
    def test_versions_cannot_drift(self):
        (self.root/'agents/openai.yaml').write_text('version: "1.0.1"\n')
        with self.assertRaises(ValueError):pack.build(self.root,self.base/'bad.zip')
    def test_existing_release_not_overwritten(self):
        out=self.base/'one.zip';pack.build(self.root,out)
        with self.assertRaises(FileExistsError):pack.build(self.root,out)
    def test_unreviewed_media_not_exported(self):
        (self.root/'patient.mp4').write_bytes(b'not real')
        with self.assertRaises(ValueError):pack.build(self.root,self.base/'bad.zip')
    def test_export_is_deterministic(self):
        a=pack.build(self.root,self.base/'a.zip');b=pack.build(self.root,self.base/'b.zip');self.assertEqual(a['sha256'],b['sha256'])
    def test_output_inside_skill_root_rejected(self):
        with self.assertRaises(ValueError):pack.build(self.root,self.root/'bad.zip')
    def test_plain_git_metadata_is_portable(self):
        (self.root/'.gitignore').write_text('__pycache__/\n*.pyc\n')
        r=pack.build(self.root,self.base/'git-style.zip');self.assertEqual(r['version'],'1.0.0')

if __name__=='__main__':unittest.main()
