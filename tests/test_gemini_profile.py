"""Synthetic contract checks; no Gemini UI or medical media generated."""
import copy
import importlib.util
from pathlib import Path
import unittest
from test_production import fixture,v

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('gemini_probe',ROOT/'scripts/check_gemini_export.py')
probe=importlib.util.module_from_spec(spec);spec.loader.exec_module(probe)

class GeminiProfile(unittest.TestCase):
    def meta(self,seconds=10,audio=True):
        return {'format':{'duration':str(seconds)},'streams':[{'codec_type':'video','width':1280,'height':720,'duration':str(seconds)}]+([{'codec_type':'audio'}] if audio else [])}
    def test_twelve_ten_second_draft(self):
        p=fixture();p['target'].update(clip_count=12,clip_duration_s=10);p['clips']=p['clips'][:12]
        for i,c in enumerate(p['clips']):c.update(start_s=i*10,end_s=(i+1)*10,duration_s=10,audio_target_s=8.5)
        r=v.validate(p);self.assertEqual(r['structural_result'],'PASS',r);self.assertEqual(r['readiness'],'BLOCKED')
    def test_fifteen_ten_is_not_120(self):
        p=fixture();p['target']['clip_duration_s']=10;self.assertEqual(v.validate(p)['structural_result'],'FAIL')
    def test_ten_second_export(self):
        r=probe.inspect(self.meta());self.assertEqual(r['technical_result'],'PASS');self.assertFalse(r['user_approved']);self.assertEqual(r['identity_qa'],'NOT_TESTED')
    def test_accumulated_exports(self):
        for seconds in [20,30,40,50]:self.assertEqual(probe.inspect(self.meta(seconds))['technical_result'],'FAIL')
    def test_fixed_different_duration_is_not_relabelled(self):self.assertEqual(probe.inspect(self.meta(8))['technical_result'],'FAIL')
    def test_missing_native_audio(self):self.assertEqual(probe.inspect(self.meta(audio=False))['technical_result'],'FAIL')
    def test_silent_route_allows_no_audio_but_no_quality_pass(self):
        r=probe.inspect(self.meta(audio=False),audio_route='SILENT');self.assertEqual(r['technical_result'],'PASS');self.assertEqual(r['voice_and_exact_dialogue_qa'],'NOT_TESTED')
    def test_aspect_drift(self):
        m=self.meta();m['streams'][0].update(width=720,height=1280);self.assertEqual(probe.inspect(m)['technical_result'],'FAIL')
    def test_short_video_with_audio_padding(self):
        m=self.meta();m['streams'][0]['duration']='4';self.assertEqual(probe.inspect(m)['technical_result'],'FAIL')
    def test_missing_duration(self):
        m=self.meta();m['format']={};self.assertEqual(probe.inspect(m)['technical_result'],'FAIL')
    def test_nonfinite_duration(self):self.assertEqual(probe.inspect(self.meta('nan'))['technical_result'],'FAIL')
    def test_nonfinite_expected_duration(self):
        with self.assertRaises(ValueError):probe.inspect(self.meta(),seconds=float('nan'))

if __name__=='__main__':unittest.main()
