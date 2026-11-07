import copy
import hashlib
import json
import unittest
from tools.csf import ROOT, read_json, score
from tools.event_monitor import aggregate, merge_items, revise, revision_trend, slow_signals, validate
from tools.lens_check import apply_lens


class IntakeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.events=read_json(ROOT/'research/intake/events.json')
        cls.originals=[e for e in cls.events if e['assessment_date']=='2026-11-07']

    def test_all_initial_items_and_appearances_preserved(self):
        self.assertGreaterEqual(len(self.events),87)
        initial=[e for e in self.events if e['week_end']<='2026-11-06']
        self.assertEqual(87,len(initial))
        self.assertEqual(92,sum(len(e['occurrences']) for e in initial))
        self.assertEqual(86,len({e['story_id'] for e in initial}))
        self.assertIn('EV-20261106-15',{e['id'] for e in initial})
        self.assertEqual([],validate(self.events))

    def test_original_analysis_and_urls_are_retained(self):
        for e in self.events:
            if e.get('historical_backfill'):self.assertTrue(e['source_urls'])
            texts=[p['text'] for a in e['original_analysis'] for p in a['paragraphs']]
            self.assertEqual(e['original_analysis_sha256'],hashlib.sha256('\n'.join(texts).encode()).hexdigest())
            if e['record_type']!='context':
                self.assertTrue(any(e['title'] in text for text in texts))
            else:
                self.assertTrue(texts)

    def test_docx_locators_match_raw_extracts(self):
        for e in self.events:
            for occurrence in e['occurrences']:
                if occurrence['paragraph_start'] is None:continue
                raw=read_json(ROOT/'research/intake/raw'/(occurrence['source_id']+'.json'))
                self.assertIn(e['title'],raw['paragraphs'][occurrence['paragraph_start']]['text'])

    def test_legacy_score_is_not_replaced_by_new_assessment(self):
        first=next(e for e in self.events if e['id']=='EV-20260921-01')
        self.assertEqual(90,first['original_numeric_score'])
        self.assertEqual(74,score(first['inputs']))
        self.assertIn('rating of 90',first['original_score_statement'])

    def test_every_initial_word_edition_has_twelve_items_per_week(self):
        manifest=read_json(ROOT/'research/intake/manifest.json')
        word=[r for r in manifest['files'] if r['relative_path'].endswith('.docx')]
        self.assertEqual([12,12,60],sorted(r['ranked_occurrences'] for r in word))
        self.assertTrue(all(r['embedded_images']==0 and r['external_images']==0 for r in word))

    def test_protective_and_counterevidence_remain_separate(self):
        self.assertTrue(any(e['role']=='counterevidence' for e in self.events))
        for row in aggregate(self.events):
            self.assertEqual(row['items'],sum(row['roles'].values()))
            self.assertEqual(row['threat_items'],row['roles'].get('threat',0))

    def test_quiet_signal_and_missing_week_not_zero(self):
        self.assertTrue(any(score(e['inputs'])<40 for e in self.events))
        self.assertNotIn('2026-10-23',[r['week_end'] for r in aggregate(self.events)])
        signals=read_json(ROOT/'research/intake/signals.json')
        self.assertGreaterEqual(len(signals),217)

    def test_revision_preserves_first_inputs_and_actual_dates(self):
        first=self.events[0]
        revision={'date':'2026-11-14','inputs':dict(first['inputs'],L=3),'input_reasons':first['input_reasons'],'reason':'Test only: new occurrence evidence','new_evidence':['test evidence']}
        changed=revise(first,revision)
        self.assertEqual(first['inputs'],changed['assessment_history'][0]['inputs'])
        self.assertNotEqual(first['assessment_date'],changed['assessment_date'])
        trend=revision_trend([changed])
        self.assertEqual(['2026-11-07','2026-11-14'],[r['assessment_date'] for r in trend])
        self.assertEqual(score(first['inputs']),trend[0]['mean_ctss'])

    def test_revision_requires_new_reason_and_later_date(self):
        with self.assertRaises(ValueError):revise(self.events[0],{})
        first=self.events[0]
        r={'date':first['assessment_date'],'inputs':first['inputs'],'input_reasons':first['input_reasons'],'reason':'x','new_evidence':['x']}
        with self.assertRaises(ValueError):revise(first,r)

    def test_new_intake_added_without_changing_baseline(self):
        initial=self.events[:1];before=copy.deepcopy(initial)
        candidate=copy.deepcopy(initial[0]);candidate['id']='TEST-NEW-ITEM'
        result=merge_items(initial,[candidate])
        self.assertEqual(2,len(result));self.assertEqual(before,initial)
        with self.assertRaises(ValueError):merge_items(initial,initial)

    def test_missing_collection_breaks_recurrence(self):
        items=[{'week_end':day,'theme':'quiet signal'} for day in ['2026-10-02','2026-10-09','2026-10-23']]
        self.assertEqual([],slow_signals(items))
        items[-1]['week_end']='2026-10-16'
        self.assertEqual(1,len(slow_signals(items)))


class LensTests(unittest.TestCase):
    def setUp(self):
        self.events={e['id']:e for e in read_json(ROOT/'research/intake/events.json')}
        self.profiles=read_json(ROOT/'lenses/profiles.json')
        self.lenses=read_json(ROOT/'lenses/examples.json')

    def test_baseline_unchanged_and_delta_reproducible(self):
        lens=self.lenses[0];event=self.events[lens['event_id']];before=copy.deepcopy(event)
        output=apply_lens(event,lens,self.profiles)
        self.assertEqual(71,output['baseline_score']);self.assertEqual(77,output['lens_score'])
        self.assertEqual(before,event)
        output['baseline_inputs']['L']=0
        self.assertEqual(before,event)

    def test_hidden_weight_change_and_missing_reason_rejected(self):
        lens=copy.deepcopy(self.lenses[0]);event=self.events[lens['event_id']]
        lens['weights']={'Ia':99}
        with self.assertRaises(ValueError):apply_lens(event,lens,self.profiles)
        del lens['weights'];lens['reasons']={}
        with self.assertRaises(ValueError):apply_lens(event,lens,self.profiles)

    def test_template_not_misrepresented_as_production(self):
        lens=copy.deepcopy(self.lenses[0]);lens['illustrative']=False
        with self.assertRaises(ValueError):apply_lens(self.events[lens['event_id']],lens,self.profiles)

    def test_identity_label_alone_does_not_change_score(self):
        lens=copy.deepcopy(self.lenses[0]);lens['input_changes']={};lens['reasons']={}
        a=apply_lens(self.events[lens['event_id']],lens,self.profiles)
        lens['scope']='Identical mechanism; a different party or faith label only'
        b=apply_lens(self.events[lens['event_id']],lens,self.profiles)
        self.assertEqual(a['lens_score'],b['lens_score'])


if __name__=='__main__':unittest.main()
