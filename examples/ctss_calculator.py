#!/usr/bin/env python3
"""Calculate reference CTSS priorities from their five inputs."""
import argparse
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.csf import score, tier

def compute_ctss(L, Ia, R, D, RecD):
    return score(dict(L=L, Ia=Ia, R=R, D=D, RecD=RecD))

def get_tier(value):
    return tier(value).upper(), ""

def show(entry):
    value = score(entry.get("ctss", {}))
    label = "Unknown" if value is None else str(value)
    print(f"{entry['id']}: {label} / 100, {tier(value)}. {entry['name']}")
    if entry.get("ctss", {}).get("score") != value:
        raise ValueError(f"{entry['id']}: stored total differs from calculated inputs")

def batch_mode(registry_path):
    registry = json.loads(Path(registry_path).read_text(encoding="utf-8"))
    entries = registry["manipulation_techniques"]
    entries.sort(key=lambda t: (-(score(t["ctss"]) if score(t["ctss"]) is not None else -1), t["id"]))
    for entry in entries:
        show(entry)

def technique_lookup(technique_id, registry_path=ROOT / "taxonomy/registry.json"):
    registry = json.loads(Path(registry_path).read_text(encoding="utf-8"))
    for entry in registry["manipulation_techniques"]:
        if entry["id"].upper() == technique_id.upper():
            show(entry)
            return
    raise ValueError(f"Unknown technique: {technique_id}")

def interactive_mode():
    print("CTSS reference estimate. Enter 0 to 5; enter ? for unknown.")
    values = {}
    for key, label in [("L", "Likelihood"), ("Ia", "Impact on agency"), ("R", "Population reach"), ("D", "Detection difficulty"), ("RecD", "Recovery difficulty")]:
        while True:
            raw = input(f"{label}: ").strip()
            if raw == "?":
                values[key] = None
                break
            try:
                value = int(raw)
                if 0 <= value <= 5:
                    values[key] = value
                    break
            except ValueError:
                pass
            print("Use a whole number from 0 to 5, or ?.")
    result = score(values)
    print(f"Result: {result if result is not None else 'Unknown'}, {tier(result)}")
    print("This estimate does not measure human capability or protection.")

def main():
    parser = argparse.ArgumentParser(description="Calculate CTSS from existing inputs")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--batch", type=Path)
    mode.add_argument("--technique")
    args = parser.parse_args()
    try:
        if args.batch:
            batch_mode(args.batch)
        elif args.technique:
            technique_lookup(args.technique)
        else:
            interactive_mode()
    except (ValueError, KeyError, OSError) as exc:
        parser.exit(1, f"Check failed: {exc}\n")

if __name__ == "__main__":
    main()
