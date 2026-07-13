# Research: Cognitive Offloading and Skill Atrophy

## ST-003, T-CT-006, HO-005 | Countermeasure: Domain 2 Cognitive Independence Protocols

**Taxonomy Links:** ST-003 (Cognitive Offloading and Skill Atrophy), T-CT-006 (Decision Automation Capture), HO-005 (Agency Erosion)
**Countermeasure:** Domain 2 cognitive independence exercises, Domain 6 AI interaction discipline, EFA R/M/H classification
**CSF Domain:** Domain 2 (Cognitive), Domain 6 (Digital & AI Symbiosis)

---

## The Threat

### ST-003: Cognitive Offloading and Skill Atrophy (Substrate)

Cognitive offloading is the voluntary transfer of cognitive work to external systems. Each individual trade is rational. GPS is more accurate than spatial memory. Autocomplete is faster than composing. An AI copilot reasons across more variables than a tired analyst. No single trade looks like a threat.

The threat is the aggregate. Each offloaded function atrophies. Spatial memory declines with GPS dependence. Language construction declines with autocomplete dependence. Reasoning capacity declines with copilot dependence. Knowledge retention declines with search dependence. The population does not lose these capabilities through attack. It surrenders them through convenience.

This is why ST-003 sits at the substrate layer, not the technique layer. No adversary is required. The system produces the outcome on its own. An adversary who later wishes to exploit the outcome inherits a population that has already disarmed itself.

### The Three-Phase Cycle

The Cognitive Threat Assessment documents the progression as a three-phase cycle:

| Phase | Mechanism | Observable Signal |
| --- | --- | --- |
| 1. Dependency | Tool adoption for convenience; task completion improves | Rising percentage of decisions mediated by automation |
| 2. Atrophy | Underlying capability degrades from disuse | Declining performance on unassisted versions of the same task |
| 3. Bias Internalization | The tool's framing becomes the user's framing; outputs absorbed as own conclusions | User cannot distinguish own reasoning from tool-generated reasoning |

Phase 3 is the strategic failure point. In Phases 1 and 2, the human can still recognize the dependency and reverse it. In Phase 3, the reference point for independent judgment is gone. The user defends the tool's conclusions as their own.

### T-CT-006: Decision Automation Capture (Active Technique)

The weaponized version. Where ST-003 is drift, T-CT-006 is exploitation: seeding biased defaults, autopilot behaviors, and recommendation patterns into the AI copilots and automation a population already depends on. The substrate condition (dependence) makes the technique nearly free to execute. CTSS 82: Likelihood 4, Impact on Agency 5, Reach 4, Detection 4, Recovery 3.

The technique does not need to change what the target believes. It needs only to shape the defaults the target no longer reviews.

### HO-005: Agency Erosion (Outcome)

The measurable end state. The person retains rights in theory and loses agency in practice. Per the Cognitive Threat Assessment, studies show a significant negative correlation between frequent AI tool usage and critical thinking abilities, with younger populations showing both higher AI dependence and lower critical thinking scores. The outcome manifests physically: decision paralysis, obedience without awareness, workforce displacement driven by capability loss rather than automation alone.

---

## Why Detection Is Difficult

**Detection score: 2/5**: the erosion is voluntary, gradual, and experienced as improvement.

Three properties defeat conventional detection:

1. **No attack signature.** There is no adversary action to detect in Phases 1 and 2. Telemetry shows a user becoming more productive, not less capable.
2. **The measurement instrument is compromised.** Self-assessment fails because the person doing the assessing is the person whose judgment has degraded. Phase 3 users rate their reasoning as improved.
3. **Baseline drift.** Organizations benchmark performance with tools included. The unassisted baseline is never measured, so the atrophy never appears in any metric.

**The critical insight:** if autonomy disappears voluntarily, defense mechanisms never trigger. Detection requires deliberately instrumenting the unassisted baseline, because no natural signal will ever fire.

---

## The Response

### Measure the Unassisted Baseline (Domain 2)

The only reliable detection method is periodic unassisted task performance measurement: reasoning, writing, navigation, and recall tasks performed without tools, benchmarked against the individual's own history. Declining unassisted performance with stable or rising assisted performance is the ST-003 signature.

This maps directly to CSF outcome indicator: Preservation of Personal Agency (sustained or improved critical thinking scores despite increasing AI tool usage).

### EFA R/M/H Classification (Domain 6)

The EFA Non-Delegation Playbook's Routine/Material/High-stakes classification is the structural countermeasure to T-CT-006:

- **Routine (R):** automated with logging. Offloading is acceptable and efficient.
- **Material (M):** human review required. The human must engage the reasoning, not just approve the output.
- **High-stakes (H):** human authorization mandatory, with a named Human Ethical Agent of Record (HEAR, AI SAFE² CP.10).

R/M/H converts the offloading decision from an unconscious drift into an explicit governance choice. The question stops being "is the tool convenient" and becomes "is this decision class one we have chosen to automate."

### Deliberate Friction

Convenience is the delivery mechanism, so friction is a countermeasure. Domain 2 protocols insert structured friction at Material and High-stakes decision points: independent conclusion formulation before consulting the tool, then comparison. The purpose is not to determine which answer is correct. It is to keep the independent reasoning pathway exercised and to surface divergence between human and machine framing while the human can still recognize it.

---

## Implementation Gap

1. **No organization measures unassisted baselines.** Readiness assessments test assisted performance exclusively. The atrophy is structurally invisible to every existing metric.
2. **Productivity incentives run the wrong direction.** Every organizational incentive rewards Phase 1 adoption and punishes the friction that prevents Phase 3.
3. **R/M/H classification is rare.** Most deployments treat all decision classes as Routine by default, which is exactly the condition T-CT-006 exploits.

---

## Operational Countermeasures (Domain 2)

1. **Unassisted baseline testing:** Quarterly reasoning, writing, and recall tasks performed without tools, scored against the individual's own trend line. Declining trend triggers a cognitive independence protocol.
2. **Independent-first habit:** For any Material or High-stakes question, formulate a position before consulting AI tools. Log divergences. Investigate systematic divergence patterns, which may indicate T-CT-006 seeding.
3. **Offloading inventory:** Document which cognitive functions each role has offloaded, to which tools, and at what decision class. An undocumented offload is an ungoverned offload.
4. **Rotation of manual capability:** Periodic tool-free execution of navigation, drafting, calculation, and analysis tasks. Capability that is exercised does not atrophy.
5. **Phase 3 screening:** Structured exercises requiring users to reconstruct the reasoning behind conclusions they hold. Inability to reconstruct reasoning for held conclusions is the Phase 3 marker.

---

## References

- Cognitive Threat Assessment: ST-003, T-CT-006, HO-005 entries and the three-phase cycle (dependency, atrophy, bias internalization)
- Cognitive Threat Taxonomy: CTSS scoring for T-CT-006; TC-09 (Autonomy Erosion by Convenience)
- EFA Non-Delegation Playbook (Rupp, January 2026; DOI: 10.5281/zenodo.18390725): R/M/H classification
- AI SAFE² Framework: CP.10 (HEAR Doctrine), CP.3 (ACT Capability Tiers)
- Research Note 004: EFA Enforcement Architecture
