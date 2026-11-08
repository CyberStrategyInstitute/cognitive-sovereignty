import copy
import unittest
from tools import query, signals
from tools.csf import read_json
from tools.export import outputs

class IntegrationTests(unittest.TestCase):
    def test_signal_conservation(self):
        records=read_json(signals.PATH)
        signals.validate(records)
        self.assertEqual(len(records),217)
        records[0]['source_text']='Changed original'
        with self.assertRaises(ValueError):signals.validate(records)

    def test_closure_requires_evidence(self):
        records=copy.deepcopy(read_json(signals.PATH))
        records[0]['status']='closed'
        with self.assertRaises(ValueError):signals.validate(records)

    def test_evidence_stays_inside_repo(self):
        with self.assertRaises(ValueError):signals.evidence_file('../outside.md')

    def test_query_pagination_and_paths(self):
        first=query.query('events',limit=2)
        second=query.query('events',limit=2,offset=first['next_offset'])
        self.assertTrue(set(r['id'] for r in first['results']).isdisjoint(r['id'] for r in second['results']))
        for collection in ('../events','secrets'):
            with self.assertRaises(ValueError):query.query(collection)
        for limit in (True,0,101):
            with self.assertRaises(ValueError):query.query('events',limit=limit)

    def test_exports_match_canonical_records(self):
        for path,text in outputs().items():self.assertEqual(path.read_text(encoding='utf-8'),text,str(path))
