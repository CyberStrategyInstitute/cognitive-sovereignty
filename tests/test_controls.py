import copy
import hashlib
import unittest
from unittest.mock import patch
from tools.csf import ROOT, read_json, score
from tools.controls import validate, views
from tools.readiness import assess, observed_summary
from tools.query import get_record


class ControlTests(unittest.TestCase):
    def setUp(self):
        self.controls=read_json(ROOT/'resources/controls.json')
        self.domains=read_json(ROOT/'resources/domains.json')
        self.sample=read_json(ROOT/'examples/unit-readiness.json')

    def test_inherited_denominators_and_unique_ids(self):
        validate(self.controls,self.domains)
        self.assertEqual([6,8,6,7,8,9],[len(d['baseline_controls']) for d in self.domains])
        self.assertEqual([2]*6,[len(d['extension_controls']) for d in self.domains])
        self.assertEqual(56,len(self.controls))
        refined=[c for c in self.controls if c['kind']=='refined']
        self.assertEqual(20,len(refined))
        self.assertTrue(all(c['previous_implementation'] and c['previous_readiness_anchors'] and c['readiness_anchors'] for c in refined))

    def test_unknowns_are_not_zero_or_partial_averages(self):
        record=copy.deepcopy(self.sample);record['ratings']=record['ratings'][:1]
        result=assess(record)
        profile=result['domains'][0]['profiles']['research-extension-v1']
        self.assertEqual(1,profile['rated']);self.assertIsNone(profile['score'])
        self.assertIsNone(result['domains'][0]['profiles']['legacy-v1']['score'])

    def test_known_absence_is_zero(self):
        record=copy.deepcopy(self.sample)
        for row in record['ratings']:row['rating']=0
        for domain in assess(record)['domains']:
            self.assertEqual(0,domain['profiles']['research-extension-v1']['score'])

    def test_sample_calculation_and_catalog_pin(self):
        result=assess(self.sample)
        self.assertEqual(56,score(self.sample['threat_assessment']['inputs']))
        self.assertEqual([10,30,20,30,30,10],[d['profiles']['research-extension-v1']['score'] for d in result['domains']])
        self.assertEqual('sha256-utf8-lf:'+hashlib.sha256((ROOT/'resources/controls.json').read_text(encoding='utf-8').encode()).hexdigest(),self.sample['catalog_revision'])

    def test_invalid_or_unsupported_ratings_are_rejected(self):
        for bad in (True,-1,6,1.5):
            record=copy.deepcopy(self.sample);record['ratings'][0]['rating']=bad
            with self.assertRaises(ValueError):assess(record)
        for field in ('evidence','note'):
            record=copy.deepcopy(self.sample);record['ratings'][0][field]=''
            with self.assertRaises(ValueError):assess(record)
        record=copy.deepcopy(self.sample);record['ratings'][0]['rating']=5;record['ratings'][0]['adverse_case_passed']='no'
        with self.assertRaises(ValueError):assess(record)

    def test_synthetic_example_cannot_become_observed_readiness(self):
        with patch('tools.readiness.read_json',side_effect=lambda path:[self.sample] if str(path).endswith('readiness-assessments.json') else read_json(path)):
            result=observed_summary()
        self.assertEqual(0,result['observed_assessments']);self.assertEqual(1,result['synthetic_excluded']);self.assertEqual([],result['results'])

    def test_domain_views_stay_in_sync(self):
        for path,text in views().items():self.assertEqual(path.read_text(encoding='utf-8'),text,str(path))

    def test_control_lookup_retains_research_and_test(self):
        record=get_record('controls','M-006g2')
        self.assertIn('research/008_operator_objectives_and_persuasion.md',record['research_notes'])
        self.assertTrue(record['test']);self.assertTrue(record['failure_response'])

    def test_readme_layout_and_logo_provenance(self):
        for path in ('README.md','FRAMEWORK.md'):
            self.assertNotIn('align="center"',(ROOT/path).read_text(encoding='utf-8'))
        for r in read_json(ROOT/'docs/assets/brand/provenance.json'):
            self.assertEqual(r['sha256'],hashlib.sha256((ROOT/'docs/assets/brand'/r['file']).read_bytes()).hexdigest())
