# CTSS Manual Scoring Worksheet

> Use this worksheet when scoring a new or proposed technique entry. Complete one worksheet per technique. All five components must be scored before computing CTSS. Justification for each score is required — scores without rationale will not be accepted in taxonomy submissions.

---

## Worksheet Header

| Field | Value |
|---|---|
| **Technique ID (proposed)** | T-CT-0___ |
| **Technique Name** | |
| **Analyst** | |
| **Date** | |
| **Red-Team Reviewer** | |

---

## CTSS Formula Reference

```
CTSS = (L × 0.25 + Ia × 0.30 + R × 0.20 + D × 0.15 + RecD × 0.10) × 20
```

Range: **0–100**

| Tier | Score |
|---|---|
| 🔴 Critical | ≥ 80 |
| 🟠 High | 70–79 |
| ⚪ Elevated | 60–69 |
| 🔵 Moderate | < 60 |

---

## Component 1: Likelihood (L) — Weight 0.25

**Question:** What is the probability that this technique is currently in deployment or will be deployed within the next 12 months?

| Score | Meaning |
|---|---|
| 0 | Theoretical — no documented deployment |
| 1 | Emerging — documented in research but not operational |
| 2 | Limited — documented isolated deployments |
| 3 | Moderate — regularly deployed by sophisticated actors |
| 4 | Likely — deployed at scale by multiple actor classes |
| 5 | Certain — already deployed and operational at scale |

**Proposed Score:** ___ / 5

**Rationale (required):**
```
Evidence:
Source(s):
```

---

## Component 2: Impact on Agency (Ia) — Weight 0.30

**Question:** If this technique succeeds, how severely does it impair the target's capacity for independent decision-making?

> This is the highest-weighted component. Agency is the core metric of the CSF — the preservation or loss of self-directed cognition.

| Score | Meaning |
|---|---|
| 0 | No impact on agency |
| 1 | Mild — minor influence, easily corrected |
| 2 | Moderate — measurable reduction in independent judgment |
| 3 | Significant — persistent reduction requiring intervention to reverse |
| 4 | Severe — erodes decision-making capacity across multiple domains |
| 5 | Maximum — attacks the epistemic foundation of independent thought itself |

**Proposed Score:** ___ / 5

**Rationale (required):**
```
Mechanism by which technique reduces agency:
Duration of effect:
Reversibility:
```

---

## Component 3: Population Reach (R) — Weight 0.20

**Question:** At maximum deployment scale, what proportion of the population can this technique reach?

| Score | Meaning |
|---|---|
| 0 | Single individual |
| 1 | Small group (< 1,000) |
| 2 | Local/regional (thousands to hundreds of thousands) |
| 3 | National scale (millions) |
| 4 | Multi-national scale (tens to hundreds of millions) |
| 5 | Global scale (billions) |

**Proposed Score:** ___ / 5

**Rationale (required):**
```
Maximum deployment scenario:
Current observed reach:
Scale-limiting factors:
```

---

## Component 4: Detection Difficulty (D) — Weight 0.15

**Question:** How difficult is it for an affected individual or monitoring system to identify that this technique is in operation?

> Higher score = harder to detect.

| Score | Meaning |
|---|---|
| 0 | Immediately obvious to any observer |
| 1 | Detectable with basic awareness |
| 2 | Detectable with moderate training |
| 3 | Requires specialized tools or significant training |
| 4 | Requires advanced tooling; most affected populations will not detect |
| 5 | Effectively undetectable with current technology and training |

**Proposed Score:** ___ / 5

**Rationale (required):**
```
Detection indicators available:
Tools required:
Why affected population typically fails to detect:
```

---

## Component 5: Recovery Difficulty (RecD) — Weight 0.10

**Question:** After successful deployment, how difficult is it for the affected individual or population to recover to their pre-affected cognitive state?

| Score | Meaning |
|---|---|
| 0 | Immediate self-correction |
| 1 | Recovers with basic intervention |
| 2 | Recovers with moderate effort over days to weeks |
| 3 | Requires sustained intervention over months |
| 4 | Persistent damage; recovery possible but slow and incomplete |
| 5 | Permanent or effectively irreversible damage |

**Proposed Score:** ___ / 5

**Rationale (required):**
```
Evidence for recovery difficulty:
Known recovery interventions:
Documented cases:
```

---

## CTSS Calculation

| Component | Score | Weight | Weighted Score |
|---|---|---|---|
| Likelihood (L) | | × 0.25 | |
| Impact on Agency (Ia) | | × 0.30 | |
| Population Reach (R) | | × 0.20 | |
| Detection Difficulty (D) | | × 0.15 | |
| Recovery Difficulty (RecD) | | × 0.10 | |
| **Sum** | | | |
| **× 20** | | | |
| **CTSS Score** | | | **___ / 100** |

**Tier:** ☐ 🔴 Critical (≥80) &nbsp;&nbsp; ☐ 🟠 High (70–79) &nbsp;&nbsp; ☐ ⚪ Elevated (60–69) &nbsp;&nbsp; ☐ 🔵 Moderate (<60)

---

## Adversarial Reproduction Check

Before submitting, answer: **Could an analyst with opposing views, using this same evidence and methodology, arrive at the same CTSS score?**

☐ Yes — the scoring is evidence-grounded and methodology-consistent  
☐ No — scoring depends on interpretive judgments that others may reach differently  
☐ Partially — indicate which components have interpretive ambiguity:

```
Ambiguous components:
Alternative scoring rationale:
```

---

## Submission Checklist

☐ All five components scored with written rationale  
☐ Evidence sources cited for each component  
☐ Adversarial reproduction check completed  
☐ Primary domains identified  
☐ Layer links documented (CD/ST/DS/HO)  
☐ At least one detection indicator specified  
☐ At least two CSF domain mitigations mapped  
☐ Reviewed by at least one additional analyst

---

## Python Calculator Reference

For programmatic scoring, use the CTSS calculator:

```bash
python3 examples/ctss_calculator.py
# Interactive mode — enter scores and receive calculated CTSS

python3 examples/ctss_calculator.py --batch taxonomy/registry.json
# Validate all scores in the registry

python3 examples/ctss_calculator.py --technique T-CT-008
# Look up a specific technique
```
