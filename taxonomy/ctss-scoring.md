# Cognitive Threat Severity Score (CTSS)

CTSS expresses CSI’s assessed severity for a declared threat scenario or event-linked risk. It combines five estimates: likelihood, impact on agency, reach, difficulty of detection, and difficulty of recovery. A higher score means a higher review priority. It does not mean that a percentage of people are harmed or protected.

The existing inputs, weights, and thresholds are unchanged. The November 7 repair corrects arithmetic and labels inherited estimates. See [the correction](../research/scoring-correction-2026-11-07.md) and [generated rankings](ctss-rankings.md).

## Use it carefully

Name the scenario, date, assessor, sources, and reasons for each input. Record uncertainty separately. Missing inputs stay unknown and the total stays unscored. Zero is a known estimate, never a substitute for missing data. The independent detection labels elsewhere in the taxonomy use a different convention; do not silently copy them into CTSS detection difficulty.

An arithmetic correction is not a new threat observation. More papers or repeated reports do not automatically increase severity. A change to an input needs a source-backed review and a preserved prior value.

## Technical reference

Each input is a whole number from 0 to 5. Impact has the greatest weight.

| Input | Meaning | Points per input step |
|---|---|---|
| L | Likelihood | 5 |
| Ia | Impact on agency | 6 |
| R | Population reach | 4 |
| D | Detection difficulty, higher means harder | 3 |
| RecD | Recovery difficulty, higher means harder | 2 |

`CTSS = L*5 + Ia*6 + R*4 + D*3 + RecD*2`

This is exactly the existing weighted formula expressed in whole points: `(L*0.25 + Ia*0.30 + R*0.20 + D*0.15 + RecD*0.10)*20`.

Range 0 to 100. Critical: 80 or above. High: 70 to below 80. Elevated: 60 to below 70. Moderate: below 60. Unknown: not scored.

## Check a change

Run `python tools/csf.py build` after approved input changes, then `python tools/csf.py check`. The calculator computes from inputs. Dashboards read the generated score file. Human-outcome observations are recorded separately in [monitoring](../monitoring/README.md).

Do not sum CTSS totals into a claim of systemic protection or a coverage percentage. Measure tested cases and human outcomes directly. The weights and bands define our assessment method; their empirical calibration remains open.

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](../resources/README.md) · [Research](../research/README.md) · [Data catalog](../docs/data/catalog.json) · [Section index](README.md)
<!-- csf-return-navigation:end -->
