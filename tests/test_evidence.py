import copy
import re
import unittest
from tools.csf import ROOT, WEIGHTS, assessment_check, assessment_report, check_registry, generated_outputs, read_json, reference_changes, research_check, score, summarize_measurements, tier, validate_measurements


def observation(**changes):
    row = dict(id="r1", date="2026-11-01", workflow="advice", metric="correct", protocol="v1", case_set="cases-v1", condition="AI-first", system="model-v1", population="adults", environment="lab", assessor="reviewer", kind="observed", passed=8, total=10, evidence="private:case-log-1")
    row.update(changes)
    return row


class ScoreTests(unittest.TestCase):
    def test_formula_and_corrected_ranking(self):
        reg = read_json(ROOT / "taxonomy/registry.json")
        self.assertEqual([], check_registry(reg))
        for entry in reg["manipulation_techniques"]:
            c = entry["ctss"]
            self.assertEqual(round((c["L"]*.25+c["Ia"]*.30+c["R"]*.20+c["D"]*.15+c["RecD"]*.10)*20), score(c))
        totals = {t["id"]:score(t["ctss"]) for t in reg["manipulation_techniques"]}
        self.assertEqual(83, totals["T-CT-008"])
        self.assertEqual(84, totals["T-CT-006"])
        self.assertEqual("T-CT-010", max(totals, key=totals.get))

    def test_missing_is_unknown_and_zero_is_known(self):
        self.assertIsNone(score({"L": 0}))
        self.assertEqual(0, score(dict.fromkeys(WEIGHTS, 0)))

    def test_invalid_values_even_when_other_inputs_missing(self):
        for bad in [-1,6,True,"4",float("nan"),2.5]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                score({"L":bad})

    def test_tier_boundaries(self):
        for value, expected in [(None,"unscored"),(0,"moderate"),(59,"moderate"),(60,"elevated"),(69.5,"elevated"),(70,"high"),(79.5,"high"),(80,"critical"),(100,"critical")]:
            self.assertEqual(expected,tier(value))

    def test_stale_score_duplicate_id_and_unknown_domain_fail(self):
        reg = read_json(ROOT / "taxonomy/registry.json")
        entry=reg["manipulation_techniques"][0]
        entry["ctss"]["score"]=99
        entry["primary_domains"]=["Invented domain"]
        reg["manipulation_techniques"].append(copy.deepcopy(entry))
        errors=check_registry(reg)
        for word in ["stored","Duplicate","unknown domain"]:
            self.assertTrue(any(word in e for e in errors))

    def test_generated_files_match(self):
        for path,content in generated_outputs(read_json(ROOT / "taxonomy/registry.json")).items():
            self.assertEqual(content,path.read_text(encoding="utf-8"))

    def test_dashboards_use_shared_scores(self):
        for name in ["command-center/index.html","docs/csf-command-center.html","docs/csf-explorer.html"]:
            text=(ROOT/name).read_text(encoding="utf-8")
            source = "../assets/csf-scores.js" if name.startswith("command-center/") else "assets/csf-scores.js"
            self.assertIn(f'src="{source}"',text)
            self.assertIn("window.CSF_SCORES[t.id]",text)
            self.assertEqual(18,len(re.findall(r"id:\s*'T-CT-\d{3}'[^\n]*?\b(?:s|score):\s*null",text)))


class MeasurementTests(unittest.TestCase):
    def test_empty_and_synthetic_are_not_real_results(self):
        self.assertEqual([],summarize_measurements([]))
        self.assertEqual([],summarize_measurements([observation(kind="synthetic")]))
        self.assertEqual([],summarize_measurements(read_json(ROOT/"monitoring/example-measurements.json")))

    def test_one_record_is_baseline_only(self):
        item=summarize_measurements([observation()])[0]
        self.assertEqual("BASELINE ONLY",item["status"])
        self.assertIsNone(item["change_points"])

    def test_drop_requests_review_including_model_change(self):
        later=observation(id="r2",date="2026-11-07",system="model-v2",passed=6)
        item=summarize_measurements([later,observation()])[0]
        self.assertEqual(-20,item["change_points"])
        self.assertEqual("REVIEW",item["status"])

    def test_changed_conditions_start_new_baselines(self):
        for change in [dict(protocol="v2"),dict(case_set="other"),dict(population="other"),dict(environment="other"),dict(condition="human-first")]:
            later=observation(id="r2",date="2026-11-07",passed=1,**change)
            groups=summarize_measurements([observation(),later])
            self.assertEqual(2,len(groups))
            self.assertTrue(all(g["status"]=="BASELINE ONLY" for g in groups))

    def test_unequal_denominators_compare_rates(self):
        later=observation(id="r2",date="2026-11-07",passed=16,total=20)
        self.assertEqual(0,summarize_measurements([observation(),later])[0]["change_points"])

    def test_first_baseline_is_preserved(self):
        rows=[observation(),observation(id="r2",date="2026-11-03",passed=6),observation(id="r3",date="2026-11-07",passed=7)]
        self.assertEqual(-10,summarize_measurements(rows)[0]["change_points"])

    def test_bad_counts_dates_and_missing_evidence_fail(self):
        for change in [dict(passed=11),dict(total=0,passed=0),dict(passed=True),dict(total=10.5),dict(evidence=""),dict(protocol=None),dict(kind="reported"),dict(date="unknown")]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_measurements([observation(**change)])

    def test_duplicate_and_same_day_ambiguity_fail(self):
        with self.assertRaises(ValueError):
            summarize_measurements([observation(),observation()])
        with self.assertRaises(ValueError):
            summarize_measurements([observation(),observation(id="r2")])


class ResearchTests(unittest.TestCase):
    def test_ctss_assessments_calculate_individual_and_aggregate_scores(self):
        rows = read_json(ROOT/"monitoring/assessments.json")
        research = read_json(ROOT/"research/evidence.json")
        text = assessment_report(rows,research)
        self.assertIn("Mean CTSS: 53.2/100",text)
        self.assertIn("First assessment edition",text)
        self.assertEqual([51,59,48,51,59,51],[score(row["inputs"]) for row in rows])

    def test_assessment_revision_preserves_baseline_and_separates_new_intake(self):
        rows = read_json(ROOT/"monitoring/assessments.json")
        later = copy.deepcopy(rows[0])
        later.update(id="US-001-next",date="2026-11-14")
        later["inputs"]["L"] = 2
        text = assessment_report(rows+[later],read_json(ROOT/"research/evidence.json"))
        self.assertIn("Matched scenario series: 6",text)
        self.assertIn("0.8 points",text)
        self.assertIn("New scenarios: 0",text)
        self.assertEqual(1,rows[0]["inputs"]["L"])

    def test_assessment_requires_reasons_and_sources(self):
        rows = read_json(ROOT/"monitoring/assessments.json")
        research=read_json(ROOT/"research/evidence.json")
        known={i for row in rows for i in row["taxonomy"]}
        assessment_check(rows,research,known)
        broken=copy.deepcopy(rows)
        broken[0]["reasons"]["Ia"]=""
        with self.assertRaises(ValueError): assessment_check(broken,research,known)
        with self.assertRaises(ValueError): assessment_check(rows,research,set())

    def test_snapshot_changes_are_record_changes(self):
        first = {"method":"csf-evidence-v1", "file_hashes":{"tools/csf.py":"a"}, "reference_scores":{"T-CT-008":83}, "research":{"R-001":"old"}}
        later = copy.deepcopy(first)
        later["reference_scores"]["T-CT-008"] = 84
        later["research"]["R-002"] = "new"
        text = reference_changes(first,later)
        self.assertIn("83 to 84",text)
        self.assertIn("Added research: R-002",text)
        self.assertIn("not measured changes in threat severity",text)

    def test_valid_sources_and_ids(self):
        reg=read_json(ROOT/"taxonomy/registry.json")
        ids={e["id"] for values in reg.values() if isinstance(values,list) for e in values if isinstance(e,dict) and "id" in e}
        research_check(read_json(ROOT/"research/evidence.json"),ids)

    def test_unknown_research_mapping_fails(self):
        with self.assertRaises(ValueError):
            research_check(read_json(ROOT/"research/evidence.json"),set())


if __name__=="__main__":
    unittest.main()
