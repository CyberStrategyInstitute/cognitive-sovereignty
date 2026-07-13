# Research: Guardrail and Model Drift, the Invisible Substrate Pair

## ST-006, ST-007 | Threat Mechanics and Evidence (Countermeasure Architecture: Research Note 004)

**Taxonomy Links:** ST-006 (Guardrail Alignment Drift), ST-007 (Model Performance Drift), T-CT-017 (Guardrail Bias Exploitation)
**Countermeasure:** EFA/E7/HEAR/Ring of Fire: full architecture in Research Note 004; drift telemetry in AI SAFE² F3.4
**CSF Domain:** Domain 6 (Digital & AI Symbiosis), Domain 2 (Cognitive)

**Division of labor with Note 004:** This note establishes the threat mechanics and evidence base for the drift pair. Note 004 details the enforcement architecture that counters it. Read them together.

---

## The Threat

### Why These Two Threats Are a Pair

ST-006 and ST-007 are both drift threats, both operate through the tools people depend on, both require zero adversary involvement, and both were additions that moved taxonomy coverage from approximately 80 percent to 92 percent. They differ in what drifts:

| | ST-006 Guardrail Alignment Drift | ST-007 Model Performance Drift |
| --- | --- | --- |
| What drifts | The boundaries of expressible thought | The quality of reasoning outputs |
| Mechanism | Alignment restrictions encode a worldview, applied uniformly at scale | Data shifts, concept drift, training distribution changes degrade outputs over time |
| User experience | Filtered reality experienced as natural | Degraded outputs absorbed as normal |
| Strategic effect | Conformity enforced through safety framing; resistance never forms | Baseline for acceptable reasoning lowers population-wide |
| Detection | 2/5 | 2/5 |

### ST-006: The Mechanics of Invisible Boundaries

No malicious intent is required. The chain is mundane: alignment guidelines are developed by teams with particular worldviews, operationalized into content restrictions, and applied uniformly across millions of users. The users have no reference point for what they are not seeing. The result is an invisible structural constraint on thought, delivered through the tool the user trusts most.

The weaponized form is T-CT-017 (Guardrail Bias Exploitation, CTSS 70): a deliberate actor exploits existing alignment restrictions as an enforcement mechanism, achieving ideological control without appearing to act at all. The tool becomes the enforcement mechanism, not just the channel.

### ST-007: The Mechanics of Lowering Baselines

Model performance drift is gradual output degradation from data shifts, concept drift, or training distribution changes. The individual interaction never signals failure. The user who consumed high-quality outputs last quarter and slightly degraded outputs this quarter has no side-by-side comparison. Each output is plausible in isolation.

The compounding effect with ST-003 (Cognitive Offloading) is the strategic problem. A user in offloading Phase 2 or 3 has surrendered the independent capability that would let them evaluate the tool's output. Degraded outputs are absorbed as the new normal. Over time, the baseline for acceptable reasoning lowers, not for one user but for every user of the drifting system simultaneously. This is population-scale cognitive degradation with no attack, no event, and no incident to respond to.

### Why the Pair Is Strategically Decisive

The Cognitive Threat Assessment flags the combination directly: if conformity is enforced through safety framing (ST-006), resistance never forms. If autonomy disappears voluntarily through convenience (ST-003 feeding ST-007 absorption), defense mechanisms never trigger. Together these substrate threats produce control without coercion, which is the rarest and most decisive form of control in the historical record.

---

## Why Detection Is Difficult

**Detection score: 2/5 for both.**

1. **No reference point.** ST-006 suppression is invisible because the user does not know what they were not shown. ST-007 degradation is invisible because the user does not retain calibrated memory of prior output quality.
2. **No incident boundary.** Drift has no timestamp. Security operations are built around events. Neither threat produces one.
3. **The evaluator is the victim.** Both threats degrade or constrain the judgment that would be used to evaluate them. This is the same self-referential trap as ST-003 Phase 3.
4. **Vendor telemetry is not adversarial.** Model providers monitor drift against their own benchmarks and their own alignment intent. Neither monitoring regime is designed to detect the harms defined here, because from the provider's frame, the guardrail behavior is the intended behavior.

---

## The Response (Summary: Full Architecture in Note 004)

Four mechanisms, detailed in Research Note 004, address the pair:

- **E7 Layer 6:** ethical constraints as testable, falsifiable rules rather than interpretable guidelines. Constraints that cannot be stated in falsifiable form are rejected.
- **E7 Layer 7 + HEAR (AI SAFE² CP.10):** named human accountability for alignment decisions and their governance. No "the algorithm decided."
- **Ring of Fire:** multi-model cross-verification with demonstrably different alignments, arbitrated by human judgment. One model's suppression or degradation is caught by divergence against its peers.
- **Drift telemetry (AI SAFE² F3.4):** behavioral drift baselining and rollback at the system level, giving ST-007 the incident boundary it naturally lacks by converting continuous drift into threshold-crossing events.

The Domain 2 complement: unassisted baseline testing (Research Note 001) protects the human evaluator's calibration, which is the reference point both drift threats erase.

---

## Implementation Gap

1. **Single-model dependence is the norm.** Most individuals and most organizations route all AI-mediated work through one provider, which eliminates the divergence signal Ring of Fire depends on.
2. **No organization baselines model outputs independently.** Drift detection is left to the vendor, whose benchmarks measure the vendor's objectives.
3. **Falsifiable alignment constraints do not exist commercially.** No major deployed system states its restrictions in E7 Layer 6 testable form. Every current deployment fails the Layer 6 standard.

---

## Operational Countermeasures (Domains 2 and 6)

1. **Multi-model triangulation:** For Material and High-stakes questions, require outputs from at least two models with demonstrably different alignments plus one non-AI source. Divergence is signal, not noise.
2. **Suppression probing:** Periodically test deployed AI tools with known-viewpoint queries on sensitive topics. Characterize the restriction surface before relying on the tool operationally. Re-probe on a schedule: the restriction surface drifts.
3. **Output quality baselining:** Retain dated samples of model outputs on standardized internal tasks. Quarterly comparison converts invisible drift into a measurable trend.
4. **Alignment restriction register:** Formally document the known restrictions of every deployed AI tool and the operational assessments those restrictions could distort. An undocumented restriction is an unmanaged bias.
5. **Independent-first habit:** Formulate conclusions before consulting the tool on sensitive topics, then compare and investigate divergence. Protects the human reference point both threats target.

---

## References

- Cognitive Threat Assessment: ST-006, ST-007 red-team insight (coverage 80 to 92 percent); "control without coercion" observation
- Cognitive Threat Taxonomy: T-CT-017 entry, TC-10 (AI-Mediated Reality Layers), Measurement Stack C3 (Human-vs-Machine Authority Transfer)
- Research Note 004: EFA Enforcement Architecture (the countermeasure to this note's threat picture)
- Research Note 001: Cognitive Offloading (the compounding substrate)
- AI SAFE² Framework: F3.4 (Behavioral Drift Baseline and Rollback), M4.8 (cloud guardrail attack paths), CP.10 (HEAR)
- E7 Protocol Stack (Rupp, January 2026; DOI: 10.5281/zenodo.18304066)
