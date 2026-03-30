# Cognitive Sovereignty Threat Assessment Template

> **Doctrine-grade prompt for evaluating any era, technology, institution, media system, or policy against Cognitive Sovereignty risk.** Intended for operational use across red-team exercises, policy review, and technology evaluation.

---

## How to Use This Template

Apply this template to **any system, institution, technology, or policy** you want to evaluate for cognitive sovereignty risk. Each assessment step builds on the previous one. A complete assessment should require no more than 90 minutes for a trained analyst.

**Rule:** If your assessment cannot complete Step 8 with a clear answer, the system has structural gaps. Identify them before deployment.

---

## Assessment Template

### Step 1 — Domain Being Assessed
*Identify the specific technology, institution, media system, policy, or environment under evaluation.*

```
Domain:         _______________________________________________
Description:    _______________________________________________
Assessment Date: _______________________________________________
Analyst(s):     _______________________________________________
```

---

### Step 2 — Manipulation Vectors Present
*Score each vector 0–5 for the domain being assessed. 0 = not present, 5 = severely present.*

| Vector | Score (0–5) | Evidence / Notes |
|---|---|---|
| Attention capture | | |
| Narrative shaping | | |
| Identity influence | | |
| Autonomy reduction | | |
| Reality distortion | | |

**Total vector score:** ___ / 25

**Threshold:** Score ≥ 15 indicates significant cognitive sovereignty risk. Score ≥ 20 indicates critical risk requiring immediate countermeasure mapping.

---

### Step 3 — Human Faculties at Risk
*Assess which human cognitive faculties are threatened by this domain.*

| Faculty | At Risk? | Mechanism |
|---|---|---|
| Perception | ☐ Yes / ☐ No | |
| Memory | ☐ Yes / ☐ No | |
| Reasoning | ☐ Yes / ☐ No | |
| Morality | ☐ Yes / ☐ No | |
| Agency | ☐ Yes / ☐ No | |

---

### Step 4 — Control Mechanisms Used
*Identify which control mechanisms are active in this domain.*

| Mechanism | Present? | Notes |
|---|---|---|
| Authority | ☐ | |
| Incentives | ☐ | |
| Fear | ☐ | |
| Convenience | ☐ | |
| Social pressure | ☐ | |
| Algorithmic optimization | ☐ | |

---

### Step 5 — Scale Potential
*Determine the maximum scale at which this domain can affect human cognition.*

☐ Individual  
☐ Family / Community  
☐ National  
☐ Civilizational  
☐ Autonomous swarm (machine-speed, unbounded)

**Notes on scale mechanisms:** _______________________________________________

---

### Step 6 — Resilience Countermeasures
*Map available countermeasures to the six CSF domains.*

| Domain | Available Countermeasures | Gap? |
|---|---|---|
| 1. Biological | | |
| 2. Cognitive | | |
| 3. Emotional | | |
| 4. Social | | |
| 5. Purpose & Moral | | |
| 6. Digital & AI Symbiosis | | |

---

### Step 7 — Edge-Case Stress Test

Answer each question honestly. If the answer to any question is "no" or "unknown," the framework has a gap.

**Q7a:** If truth becomes functionally unknowable through AI-generated content and competing reality ecosystems, does resilience remain?  
☐ Yes — explain: ___________________  
☐ No — gap identified: ___________________  
☐ Unknown

**Q7b:** If the institutions responsible for cognitive defense are themselves captured, does resilience remain?  
☐ Yes — explain: ___________________  
☐ No — gap identified: ___________________  
☐ Unknown

**Q7c:** If AI controls the primary information flow available to the affected population, does resilience remain?  
☐ Yes — explain: ___________________  
☐ No — gap identified: ___________________  
☐ Unknown

---

### Step 8 — 90% Coverage Determination

The assessment succeeds only if all three conditions are met:

| Condition | Met? | Evidence |
|---|---|---|
| Majority of manipulation vectors neutralized | ☐ Yes / ☐ No | |
| Human agency measurably preserved | ☐ Yes / ☐ No | |
| Identity and morality remain self-directed | ☐ Yes / ☐ No | |

**Overall Coverage Estimate:** ____%

**Gaps requiring remediation:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

### Assessment Summary

| Field | Value |
|---|---|
| Domain Assessed | |
| Vector Score | / 25 |
| Faculties at Risk | |
| Primary Control Mechanisms | |
| Maximum Scale | |
| Coverage Estimate | % |
| Passed Edge Cases? | ☐ Yes / ☐ No / ☐ Partial |
| Ready for Deployment? | ☐ Yes / ☐ No — remediation required |

---

## Example Completed Assessments

See `/examples/` for completed assessment templates applied to:
- A unit-level AI copilot deployment
- A social platform exposure scenario
- A military family resilience program evaluation

---

## Cross-Reference

- Threat taxonomy IDs: See [`/taxonomy/`](../taxonomy/)
- CTSS scoring: See [`/taxonomy/ctss-scoring.md`](../taxonomy/ctss-scoring.md)
- Domain 6 specific guidance: See [`/06-digital-ai-symbiosis/`](../06-digital-ai-symbiosis/)
- Python CTSS calculator: See [`/examples/ctss_calculator.py`](../examples/ctss_calculator.py)
