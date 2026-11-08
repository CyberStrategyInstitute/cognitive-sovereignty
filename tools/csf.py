"""Small, offline CSF checks. Uses the Python standard library only."""
import argparse
import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if __package__ in {None,""}:sys.path.insert(0,str(ROOT))
WEIGHTS = {"L": 5, "Ia": 6, "R": 4, "D": 3, "RecD": 2}
DOMAINS = {"Biological", "Cognitive", "Emotional", "Social", "Purpose & Moral", "Digital & AI Symbiosis"}


def score(values):
    """Same existing CTSS formula, expressed as integer points. None means unknown."""
    if not isinstance(values, dict):
        raise ValueError("CTSS inputs must be an object")
    for key in WEIGHTS:
        value = values.get(key)
        if value is not None and (type(value) is not int or not 0 <= value <= 5):
            raise ValueError(f"{key} must be a whole number from 0 to 5, or null")
    if any(values.get(key) is None for key in WEIGHTS):
        return None
    return sum(values[key] * weight for key, weight in WEIGHTS.items())


def tier(value):
    if value is None:
        return "unscored"
    return "critical" if value >= 80 else "high" if value >= 70 else "elevated" if value >= 60 else "moderate"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_registry(registry):
    errors, ids = [], set()
    for entries in registry.values():
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if not isinstance(entry, dict) or "id" not in entry:
                errors.append("Every registry entry needs an ID")
                continue
            if entry["id"] in ids:
                errors.append(f"Duplicate ID: {entry['id']}")
            ids.add(entry["id"])
            for domain in entry.get("primary_domains", entry.get("csf_domains", [])):
                if domain not in DOMAINS:
                    errors.append(f"{entry['id']}: unknown domain {domain}")
    for entry in registry["manipulation_techniques"]:
        try:
            expected = score(entry.get("ctss", {}))
            stored = entry.get("ctss", {}).get("score")
            if stored != expected or isinstance(stored, bool):
                errors.append(f"{entry['id']}: stored {stored}, calculated {expected}")
        except ValueError as exc:
            errors.append(f"{entry['id']}: {exc}")
    return errors


def ranking(registry):
    return sorted(registry["manipulation_techniques"], key=lambda t: (-(score(t["ctss"]) if score(t["ctss"]) is not None else -1), t["id"]))


def generated_outputs(registry):
    rows = ["# CTSS reference scores", "", "Generated from registry inputs with `python tools/csf.py build`. These are inherited analyst estimates, not measured incident results. The formula and five inputs are unchanged.", "", "| Rank | ID | Technique | Score | Priority |", "|---|---|---|---|---|"]
    data = {}
    for n, entry in enumerate(ranking(registry), 1):
        value = score(entry["ctss"])
        data[entry["id"]] = {"score": value, "tier": tier(value), "inputs": {k:entry["ctss"].get(k) for k in WEIGHTS}, "domains": entry["primary_domains"]}
        rows.append(f"| {n} | {entry['id']} | {entry['name']} | {value if value is not None else 'Unknown'} | {tier(value)} |")
    javascript = "// Generated from taxonomy/registry.json. Do not edit by hand.\nwindow.CSF_SCORES = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
    from tools.presentation import decorate
    return {ROOT / "taxonomy/ctss-rankings.md": decorate(ROOT / "taxonomy/ctss-rankings.md", "\n".join(rows) + "\n"), ROOT / "assets/csf-scores.js": javascript, ROOT / "docs/assets/csf-scores.js": javascript}


def validate_measurements(records):
    if not isinstance(records, list):
        raise ValueError("Measurements must be a list")
    ids = set()
    required = ("id", "date", "workflow", "metric", "protocol", "case_set", "condition", "system", "population", "environment", "assessor", "kind", "passed", "total", "evidence")
    for row in records:
        if not isinstance(row, dict):
            raise ValueError("Each measurement must be an object")
        if any(k not in row or row[k] == "" for k in required):
            raise ValueError("Measurement is missing a required field")
        for key in set(required) - {"passed", "total"}:
            if not isinstance(row[key], str) or not row[key].strip():
                raise ValueError(f"{key} must be nonempty text")
        if row["id"] in ids:
            raise ValueError("Duplicate measurement ID")
        ids.add(row["id"])
        date.fromisoformat(row["date"])
        if row["kind"] not in {"observed", "synthetic"}:
            raise ValueError("Measurement kind must be observed or synthetic")
        p, n = row["passed"], row["total"]
        if type(p) is not int or type(n) is not int or not 0 <= p <= n or n < 1:
            raise ValueError("Measurement needs whole counts: 0 <= passed <= total, total > 0")
        if not isinstance(row["evidence"], str) or not row["evidence"].strip():
            raise ValueError("Measurement needs a traceable evidence location")


def summarize_measurements(records):
    validate_measurements(records)
    groups = {}
    # Compare only the same protocol, cases, condition, population, and environment.
    keys = ("workflow", "metric", "protocol", "case_set", "condition", "population", "environment")
    for row in records:
        if row["kind"] == "observed":
            groups.setdefault(tuple(row[k] for k in keys), []).append(row)
    results = []
    for key, rows in sorted(groups.items()):
        rows.sort(key=lambda row: (row["date"], row["id"]))
        dates = [r["date"] for r in rows]
        if len(set(dates)) != len(dates):
            raise ValueError("Use one aggregate per day for each comparable metric")
        first, last = rows[0], rows[-1]
        delta = round(100 * (last["passed"] / last["total"] - first["passed"] / first["total"]), 1) if len(rows) > 1 else None
        # Operational review trigger only. This is not statistical significance.
        status = "BASELINE ONLY" if delta is None else "REVIEW" if delta <= -10 else "NO REVIEW TRIGGER"
        results.append({"workflow": key[0], "metric": key[1], "status": status, "baseline": first, "latest": last, "change_points": delta})
    return results


def research_check(records, known_ids):
    if not isinstance(records, list):
        raise ValueError("Research must be a list")
    ids = set()
    required = ("id", "title", "url", "version", "published", "reviewed", "review_depth", "evidence_type", "finding", "limits", "decision", "taxonomy", "lineage")
    for row in records:
        if not isinstance(row, dict):
            raise ValueError("Each research record must be an object")
        if any(not row.get(k) for k in required):
            raise ValueError("Research record is incomplete")
        if row["id"] in ids:
            raise ValueError("Duplicate research ID")
        ids.add(row["id"])
        if not row["url"].startswith("https://"):
            raise ValueError("Research record needs a source URL")
        if set(row["taxonomy"]) - known_ids:
            raise ValueError(f"{row['id']}: unknown taxonomy ID")
        date.fromisoformat(row["reviewed"])
        date.fromisoformat(row["published"])


def assessment_check(records, research, known_ids):
    sources = {r["id"] for r in research}
    ids, versions = set(), set()
    for row in records:
        required = ("id", "series", "date", "scenario", "us_relevance", "scope", "method", "assessor", "basis", "confidence", "judgment", "action", "limits", "taxonomy", "sources", "inputs", "reasons")
        if not isinstance(row, dict) or any(not row.get(k) for k in required):
            raise ValueError("Assessment needs its scope, reasoning, sources, and all five inputs")
        date.fromisoformat(row["date"])
        if row["id"] in ids or (row["series"],row["date"]) in versions:
            raise ValueError("Duplicate assessment or same-day series revision")
        ids.add(row["id"])
        versions.add((row["series"],row["date"]))
        if set(row["sources"]) - sources or set(row["taxonomy"]) - known_ids:
            raise ValueError("Assessment cites an unknown source or taxonomy ID")
        if row["method"] != "CTSS-existing-v1" or row["scope"] != "US-12-month-scenario":
            raise ValueError("Use this series' declared method and U.S. scope; version other methods separately")
        if score(row["inputs"]) is None:
            raise ValueError("A scored assessment needs five explicit estimates")
        if any(not row["reasons"].get(k) for k in WEIGHTS):
            raise ValueError("Explain each CTSS estimate")


def assessment_report(records, research):
    if not records:
        return "\n## CSF assessments\n\nNo scored assessments recorded yet.\n"
    sources = {r["id"]:r for r in research}
    latest = {}
    for row in sorted(records,key=lambda r:(r["date"],r["id"])):
        latest[row["series"]] = row
    rows = sorted(latest.values(),key=lambda r:(-score(r["inputs"]),r["series"]))
    average = round(sum(score(r["inputs"]) for r in rows)/len(rows),1)
    bands = {name:sum(tier(score(r["inputs"]))==name for r in rows) for name in ["critical","high","elevated","moderate"]}
    lines = ["", "## CSF U.S.-focused threat assessments", "", "These are CSI assessments using CTSS. Sources establish the evidence; CSI owns the interpretation, estimates, and resulting scores. They are not claims that the studies measured CTSS or national harm.", "", f"Current assessed sample: {len(rows)} scenarios. Mean CTSS: {average}/100. " + "; ".join(f"{n} {name}" for name,n in bands.items()) + ".", "", "This mean describes the selected assessed scenarios, not U.S. population risk. The sample is research-led and is not a representative incident sample. Helpful factual-correction evidence is included in the reasoning, not counted as another threat event.", "", "| Scenario | Assessment date | CTSS | Priority |", "|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['scenario']} | {r['date']} | {score(r['inputs'])} | {tier(score(r['inputs']))} |")
    dates=sorted({r["date"] for r in records})
    lines.extend(["", "### Change over time", ""])
    lines.extend(["| Edition date | Scenarios with an assessment by that date | Mean CTSS |", "|---|---|---|"])
    for cutoff in dates:
        edition = {}
        for item in sorted(records,key=lambda r:(r["date"],r["id"])):
            if item["date"] <= cutoff:
                edition[item["series"]] = item
        mean = round(sum(score(item["inputs"]) for item in edition.values())/len(edition),1)
        lines.append(f"| {cutoff} | {len(edition)} | {mean} |")
    lines.append("")
    if len(dates)==1:
        lines.append("First assessment edition. No temporal severity trend is established yet. Future revisions preserve these scores and their reasons.")
    else:
        previous={}
        for r in sorted(records,key=lambda r:(r["date"],r["id"])):
            if r["date"] < dates[-1]: previous[r["series"]]=r
        matched=set(previous)&set(latest)
        delta=round(sum(score(latest[k]["inputs"])-score(previous[k]["inputs"]) for k in matched)/len(matched),1) if matched else None
        lines.append(f"Latest edition: {dates[-1]}; prior cutoff: {dates[-2]}. Matched scenario series: {len(matched)}. Mean score change for that matched set: {delta if delta is not None else 'unknown'} points. New scenarios: {len(set(latest)-set(previous))}. New intake is reported separately from changed severity.")
    for r in rows:
        lines.extend(["",f"### {r['id']}: {r['scenario']}","",f"CTSS {score(r['inputs'])}/100. Assessed {r['date']}. Basis: {r['basis']}. Confidence: {r['confidence']}.","",f"U.S. relevance: {r['us_relevance']}","",r["judgment"],"", "| Input | Score | Why |","|---|---|---|"])
        for key in WEIGHTS: lines.append(f"| {key} | {r['inputs'][key]} | {r['reasons'][key]} |")
        lines.extend(["",f"Action: {r['action']}","",f"Limits: {r['limits']}","", "Sources: " + ", ".join(f"[{sid}: {sources[sid]['title']}]({sources[sid]['url']})" for sid in r["sources"]) + "."])
    return "\n".join(lines)+"\n"


def monitor(registry, research, measurements):
    issues = check_registry(registry)
    summaries = summarize_measurements(measurements)
    lines = ["# CSF evidence report", "", f"Report date: {date.today().isoformat()}. Local draft for review.", "", "The main historical baseline is now the [complete weekly intake](../research/intake/reports/baseline.md): 87 scored item records from 92 appearances across seven supplied intake weeks. This technical report also retains the separate six-scenario exercise; its aggregate is not the event baseline.", "", "## What we checked", "", f"- Repository: {len(registry['manipulation_techniques'])} reference technique scores checked; {len(issues)} registry errors.", f"- Selected research-note register: {len(research)} source records, representing {len({r['lineage'] for r in research})} source lineages. The larger event ledger retains all supplied item sources and analysis.", f"- Local observations: {sum(r['kind'] == 'observed' for r in measurements)} measurement records.", f"- Synthetic examples excluded from real results: {sum(r['kind'] == 'synthetic' for r in measurements)}.", "", "## Measured changes", ""]
    if issues:
        lines.extend(["REPOSITORY CHECK FAILED. Resolve these errors before publication:", *[f"- {issue}" for issue in issues], ""])
    if not summaries:
        lines.append("No local model or human-outcome measurements yet. Directly measured human-outcome drift and control effectiveness are unknown. The CSF assessment section below provides our separately labeled severity judgments.")
    for item in summaries:
        last = item["latest"]
        delta = "not available" if item["change_points"] is None else f"{item['change_points']:+g} percentage points"
        lines.extend([f"### {item['workflow']}: {item['metric']}", "", f"{item['status']}. Latest: {last['passed']} of {last['total']} passed ({last['date']}); change from first comparable observation: {delta}.", f"Baseline evidence: {item['baseline']['evidence']}. Latest evidence: {last['evidence']}.", ""])
    lines.extend(["", "## What happens next", "", "A drop of 10 percentage points or more requests human review. It does not establish harm or statistical significance. Check sample size, changed model versions, collection errors, and task conditions before explaining a change. Publish only after source, privacy, and wording review.", "", "Research intake is manual in this first version. No live feeds, model tests, or human studies run through this command. CTSS totals and aggregates are calculated automatically from the dated assessment inputs. Research intake and input judgments are analyst work in this version."])
    return "\n".join(lines) + "\n"


def snapshot(registry, research, measurements, assessments=None):
    """Save actual inputs and provenance so a later report can explain a change."""
    hashes = {}
    for name in ["taxonomy/registry.json", "research/evidence.json", "monitoring/assessments.json", "research/intake/events.json", "lenses/profiles.json", "tools/csf.py"]:
        hashes[name] = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True).strip())
    except (OSError, subprocess.CalledProcessError):
        commit, dirty = "unavailable", None
    return {"method": "csf-evidence-v1", "date": date.today().isoformat(), "commit": commit, "working_tree_changed": dirty, "file_hashes": hashes, "measurement_hash": hashlib.sha256(json.dumps(measurements, sort_keys=True).encode()).hexdigest(), "registry_errors": check_registry(registry), "reference_scores": {t["id"]:score(t["ctss"]) for t in registry["manipulation_techniques"]}, "research": {r["id"]:hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest() for r in research}, "assessments": assessments or [], "observations": summarize_measurements(measurements)}


def reference_changes(previous, current):
    if previous.get("method") != current["method"]:
        raise ValueError("Snapshot method changed; start a new comparison baseline")
    lines = ["", "## Changes in recorded evidence", "", "These are record changes, not measured changes in threat severity.", ""]
    changes = []
    if previous.get("file_hashes", {}).get("tools/csf.py") != current["file_hashes"]["tools/csf.py"]:
        changes.append("- Reporting code changed. Review method compatibility before interpreting trends.")
    for key in ["reference_scores", "research"]:
        before, after = previous[key], current[key]
        for entry_id in sorted(set(before) | set(after)):
            if entry_id not in before:
                changes.append(f"- Added {key}: {entry_id}.")
            elif entry_id not in after:
                changes.append(f"- Removed {key}: {entry_id}; review why.")
            elif before[entry_id] != after[entry_id]:
                detail = f" {before[entry_id]} to {after[entry_id]}." if key == "reference_scores" else " Source record changed; review the saved versions."
                changes.append(f"- Changed {key}: {entry_id}.{detail}")
    return "\n".join(lines + (changes or ["No reference-score or research-record changes."])) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Check CSF evidence and prepare a plain-language report")
    parser.add_argument("command", choices=["check", "build", "report"])
    parser.add_argument("--measurements", type=Path, default=ROOT / "monitoring/measurements.json")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--baseline", type=Path, help="Previous report JSON snapshot to compare")
    args = parser.parse_args()
    try:
        registry = read_json(ROOT / "taxonomy/registry.json")
        research = read_json(ROOT / "research/evidence.json")
        assessments = read_json(ROOT / "monitoring/assessments.json")
        measurements = read_json(args.measurements)
        ids = {e["id"] for entries in registry.values() if isinstance(entries, list) for e in entries if isinstance(e, dict) and "id" in e}
        research_check(research, ids)
        assessment_check(assessments, research, ids)
        validate_measurements(measurements)
        errors = check_registry(registry)
        if args.command == "build":
            if errors:
                raise ValueError("; ".join(errors))
            for path, content in generated_outputs(registry).items():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            print("Generated reference rankings and shared dashboard scores.")
        elif args.command == "check":
            for path, content in generated_outputs(registry).items():
                if not path.exists() or path.read_text(encoding="utf-8") != content:
                    errors.append(f"Generated file needs rebuilding: {path.relative_to(ROOT)}")
            if errors:
                raise ValueError("\n".join(errors))
            print(f"PASS: {len(registry['manipulation_techniques'])} reference scores, generated files, research records, and measurement records checked.")
        else:
            report = monitor(registry, research, measurements) + assessment_report(assessments, research)
            current = snapshot(registry, research, measurements, assessments)
            if args.baseline:
                report += reference_changes(read_json(args.baseline), current)
            if args.output:
                if args.baseline and args.output.with_suffix(".json").resolve() == args.baseline.resolve():
                    raise ValueError("Choose a new output path; do not overwrite the baseline")
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(report, encoding="utf-8")
                args.output.with_suffix(".json").write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                print(f"Wrote {args.output}")
            else:
                print(report)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"Check failed: {exc}\n")


if __name__ == "__main__":
    main()
