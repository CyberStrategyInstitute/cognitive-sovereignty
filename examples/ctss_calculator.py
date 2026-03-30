#!/usr/bin/env python3
"""
CTSS Calculator — Cognitive Threat Severity Score
Cognitive Sovereignty Framework v2.0
Cyber Strategy Institute | cyberstrategyinstitute.com

Usage:
    python3 ctss_calculator.py
    python3 ctss_calculator.py --batch taxonomy/registry.json
    python3 ctss_calculator.py --technique T-CT-008
"""

import json
import argparse
from pathlib import Path

# CTSS weights per the CSF specification
WEIGHTS = {
    "L": 0.25,    # Likelihood
    "Ia": 0.30,   # Impact on Agency (highest weight)
    "R": 0.20,    # Population Reach
    "D": 0.15,    # Detection Difficulty
    "RecD": 0.10  # Recovery Difficulty
}

TIERS = {
    (80, 100): ("CRITICAL", "\033[91m"),  # Red
    (70, 79):  ("HIGH",     "\033[93m"),  # Orange/Yellow
    (60, 69):  ("ELEVATED", "\033[37m"),  # Grey
    (0, 59):   ("MODERATE", "\033[94m"),  # Blue
}

RESET = "\033[0m"


def compute_ctss(L: int, Ia: int, R: int, D: int, RecD: int) -> float:
    """
    Compute CTSS score.
    Formula: CTSS = (L*0.25 + Ia*0.30 + R*0.20 + D*0.15 + RecD*0.10) * 20
    Range: 0-100
    """
    score = (
        L * WEIGHTS["L"] +
        Ia * WEIGHTS["Ia"] +
        R * WEIGHTS["R"] +
        D * WEIGHTS["D"] +
        RecD * WEIGHTS["RecD"]
    ) * 20
    return round(score, 1)


def get_tier(score: float) -> tuple[str, str]:
    """Return (tier_name, color_code) for a given score."""
    for (low, high), (name, color) in TIERS.items():
        if low <= score <= high:
            return name, color
    return "MODERATE", "\033[94m"


def interactive_mode():
    """Interactive CTSS scoring for a new threat entry."""
    print("\n" + "="*60)
    print("  CTSS CALCULATOR — Cognitive Sovereignty Framework v2.0")
    print("  Cyber Strategy Institute")
    print("="*60)
    print("\nScore each component on a 0–5 scale.\n")

    descriptions = {
        "L":    "Likelihood          (0=theoretical, 5=already deployed)",
        "Ia":   "Impact on Agency    (0=no effect, 5=total autonomy erosion)",
        "R":    "Population Reach    (0=individual, 5=global)",
        "D":    "Detection Difficulty(0=obvious, 5=undetectable)",
        "RecD": "Recovery Difficulty (0=instant, 5=permanent damage)",
    }

    scores = {}
    for key, desc in descriptions.items():
        while True:
            try:
                val = int(input(f"  {desc}: "))
                if 0 <= val <= 5:
                    scores[key] = val
                    break
                print("  ⚠  Please enter a value between 0 and 5.")
            except ValueError:
                print("  ⚠  Please enter an integer.")

    score = compute_ctss(**scores)
    tier, color = get_tier(score)

    print(f"\n{'─'*60}")
    print(f"  CTSS Score: {color}{score:5.1f}{RESET}  [{color}{tier}{RESET}]")
    print(f"{'─'*60}")
    print(f"\n  Formula:  ({scores['L']}×0.25 + {scores['Ia']}×0.30 + {scores['R']}×0.20 + "
          f"{scores['D']}×0.15 + {scores['RecD']}×0.10) × 20 = {score}")

    print("\n  Tier Reference:")
    print("    🔴 CRITICAL  ≥ 80  —  Immediate defense priority")
    print("    🟠 HIGH      70–79 —  High defense priority")
    print("    ⚪ ELEVATED  60–69 —  Monitor and address")
    print("    🔵 MODERATE  < 60  —  Watch-list")
    print()


def batch_mode(registry_path: str):
    """Score all techniques from the JSON registry."""
    path = Path(registry_path)
    if not path.exists():
        print(f"Error: Registry file not found at {registry_path}")
        return

    with open(path) as f:
        registry = json.load(f)

    techniques = registry.get("manipulation_techniques", [])
    if not techniques:
        print("No techniques found in registry.")
        return

    print(f"\n{'─'*70}")
    print(f"  {'ID':<12} {'CTSS':>6}  {'TIER':<10}  {'TECHNIQUE'}")
    print(f"{'─'*70}")

    results = []
    for t in techniques:
        ctss_data = t.get("ctss", {})
        score = ctss_data.get("score", 0)
        tier, color = get_tier(score)
        results.append((score, t["id"], t["name"], tier, color))

    results.sort(reverse=True)

    for score, tid, name, tier, color in results:
        name_short = name[:40] + "…" if len(name) > 40 else name
        print(f"  {tid:<12} {color}{score:>6.1f}{RESET}  {color}{tier:<10}{RESET}  {name_short}")

    print(f"{'─'*70}")
    print(f"  Total techniques: {len(results)}")
    critical = sum(1 for s, *_ in results if s >= 80)
    high = sum(1 for s, *_ in results if 70 <= s < 80)
    print(f"  Critical (≥80): {critical}  |  High (70–79): {high}  |  Other: {len(results)-critical-high}\n")


def technique_lookup(technique_id: str, registry_path: str = "taxonomy/registry.json"):
    """Look up a specific technique from the registry."""
    path = Path(registry_path)
    if not path.exists():
        # Fallback: use hardcoded data
        print(f"Registry not found at {registry_path}. Showing formula only.")
        return

    with open(path) as f:
        registry = json.load(f)

    for t in registry.get("manipulation_techniques", []):
        if t["id"].upper() == technique_id.upper():
            ctss_data = t.get("ctss", {})
            score = ctss_data.get("score", 0)
            tier, color = get_tier(score)

            print(f"\n{'='*60}")
            print(f"  {t['id']} — {t['name']}")
            print(f"{'='*60}")
            print(f"  CTSS Score: {color}{score}{RESET} [{color}{tier}{RESET}]")
            print(f"\n  Scoring Components:")
            print(f"    Likelihood (L):           {ctss_data.get('L', 'N/A')} / 5")
            print(f"    Impact on Agency (Ia):    {ctss_data.get('Ia', 'N/A')} / 5  ← highest weight")
            print(f"    Population Reach (R):     {ctss_data.get('R', 'N/A')} / 5")
            print(f"    Detection Difficulty (D): {ctss_data.get('D', 'N/A')} / 5")
            print(f"    Recovery Difficulty:      {ctss_data.get('RecD', 'N/A')} / 5")
            print(f"\n  Primary Domains: {', '.join(t.get('primary_domains', []))}")
            print(f"  Timeline: {t.get('timeline', 'N/A')}")
            print(f"  Mechanism: {t.get('mechanism', 'N/A')}\n")
            return

    print(f"Technique '{technique_id}' not found in registry.")


def main():
    parser = argparse.ArgumentParser(
        description="CTSS Calculator — Cognitive Sovereignty Framework v2.0"
    )
    parser.add_argument("--batch", metavar="REGISTRY_JSON",
                        help="Score all techniques from a JSON registry file")
    parser.add_argument("--technique", metavar="ID",
                        help="Look up a specific technique (e.g., T-CT-008)")
    args = parser.parse_args()

    if args.batch:
        batch_mode(args.batch)
    elif args.technique:
        technique_lookup(args.technique)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
