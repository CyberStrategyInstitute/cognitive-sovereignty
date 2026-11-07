# Domain 01: Biological

### The Substrate the Adversary Reaches First

**CSF Position:** Domain 1 of 6 | **AI SAFE² UAS profile Control:** UAS-H6 (attention capture in high-tempo decision environments) | **Companion Research:** [002 Swarm Threat Scaling](../research/002_swarm_threat_scaling.md)

---

## 1. Doctrine

Cognition runs on hardware. Sleep, metabolism, nervous system regulation, and neurophysiological integrity are not wellness topics. They are the physical substrate every other domain depends on, and they are directly targeted.

The targeting is not metaphorical. Variable-reward schedules, notification patterns, and engagement mechanics are engineered against the dopamine system using the same operant-conditioning mechanics that make slot machines addictive, embedded in every platform and every notification channel. The emerging neurotechnology surface (brain-computer interfaces, transcranial stimulation, affect-modulating wearables, neural data collection) creates, for the first time in history, a direct attack surface for human cognition that bypasses information channels entirely.

**Why this domain matters operationally:** a warfighter whose reward system is captured by dopamine engineering and whose sleep is fragmented by platform design has already lost cognitive capacity before any manipulation technique is applied. Every existing military resilience framework covers physical fitness. None of them treat the neurophysiological attack surface as an attack surface. This domain closes that gap.

> **So what:** Biological degradation is the entry point of the upward cascade. Lose Domain 1 and Domains 2 through 6 degrade on schedule, without any further adversary effort.

---

## 2. Threat Exposure

| ID | Threat | Layer | CTSS / Detection | What It Targets in This Domain |
| --- | --- | --- | --- | --- |
| ST-002 | Behavioral Reinforcement Engineering | Substrate | Detection 4 | Dopamine system; converts cognition into an operant-conditioned feedback loop |
| ST-004 | Neuro-Intrusion Surface Expansion | Substrate | Detection 1 | Direct neural access via BCIs, stimulation, affect-modulating wearables, neural data harvesting |
| T-CT-001 | Attention Capture and Habituation | Technique | CTSS 75 / Detection 4 | Reward circuitry via infinite scroll, variable rewards, notification saturation |
| T-CT-003 | Micro-Targeted Emotional Priming | Technique | CTSS 70 / Detection 2 | Stress physiology; elevated baseline anxiety, anger, fear |
| T-CT-012 | Neurotech / Direct Cognitive Influence | Technique | CTSS 71 / Detection 1 | Neurological integrity; persuasion or control below the information layer |
| DS-004 | Neuro-Digital Interfaces | Delivery | Detection 1 | Wearables and brain interfaces as always-on delivery channels |

**Threat trajectory note:** T-CT-012 has an inherited reference score of 71 after the arithmetic correction. That estimate is not a measured incidence or a prediction. Its Impact on Agency score is 5, the maximum. As the neurotech surface matures, this domain's threat profile climbs faster than any other domain's. Build the defenses before the likelihood arrives.

---

<!-- domain-exposure:start -->
### Research-informed exposure updates

These map additional mechanisms to existing threat IDs. They expand what this domain examines; they do not establish increased incidence, reach, or severity.

| Existing threat ID | Mechanism to examine | Research |
|---|---|---|
| T-CT-014 (added) | Notification load and decision pressure can make meaningful review harder. | [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |
| T-CT-016 (added) | Sensitive-state data can support vulnerability-targeted persuasion. | [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |
<!-- domain-exposure:end -->

## 3. Cascade Position

**Feeds upward (degradation cascade):** Sleep deprivation from dopamine-driven engagement (Domain 1) impairs cognitive function (Domain 2), reduces emotional regulation (Domain 3), strains relationships (Domain 4), undermines purpose (Domain 5), and dissolves the motivation to maintain AI interaction discipline (Domain 6).

**Receives from above (compromise cascade):** A compromised AI environment (Domain 6) delivers engineered stress and engagement pressure that manifests as biological load: cortisol elevation, sleep fragmentation, reward-system capture (Domain 1).

**Operational consequence:** single-domain interventions fail. An attention hygiene program (Domain 2) cannot succeed while the biological reward system remains captured (Domain 1). Sequence matters: biological stabilization is the precondition for every higher-domain intervention.

---

## 4. Protective Capabilities and Mitigation Catalog

Stable IDs connect each capability to its research and test. Existing IDs are retained. See the [full catalog](../resources/mitigation-catalog.md) for expected outcomes, owner roles, checks, and failure responses.

| M-ID | Capability | Counters | Implementation | Research |
|---|---|---|---|---|
| M-001b | Circadian discipline (refined) | T-CT-001, ST-002 | Protect rest periods through proportionate notification rules and an urgent-contact exception. Check workload and accessibility needs before setting the local rule. | [006](../research/006_independent_judgment.md), [010](../research/010_domain_controls_and_readiness.md) |
| M-S02b | Reward-loop interruption (inherited) | ST-002 | Notification batching, variable-reward feature disablement (autoplay, infinite scroll, badges), scheduled rather than triggered platform access | [010](../research/010_domain_controls_and_readiness.md) |
| M-003b | Stress physiology monitoring (refined) | T-CT-003 | Use workload and notification records first. Any sensitive health or biometric tracking must be voluntary, minimized, and handled by an appropriate health/privacy process. A change alone does not establish manipulation. | [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |
| M-S04b | Neurological boundary awareness (inherited) | ST-004, DS-004 | Formal inventory of every device with neural or affect-modulating capability; consent and data-flow review before adoption; default-deny posture for neural data collection | [010](../research/010_domain_controls_and_readiness.md) |
| M-012b | Neurotech provenance and air-gap (inherited) | T-CT-012, ST-004 | No closed-loop neurofeedback or stimulation devices without verified provenance, auditable firmware, and hard disconnect capability; bioethics review for any operational neurotech | [010](../research/010_domain_controls_and_readiness.md) |
| M-001b2 | Substance and stimulant awareness (inherited) | T-CT-001 | Recognition that caffeine, alcohol, and stimulant patterns compound platform-driven sleep disruption; managed as part of the same exposure surface | [010](../research/010_domain_controls_and_readiness.md) |
| M-014b | Decision pacing under pressure (added) | T-CT-014, T-CT-006 | Use a pause or relief path when notification load or fatigue makes a consequential review impractical. Name the alternate reviewer before the shift. | [006](../research/006_independent_judgment.md), [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |
| M-016b | Limits on sensitive-state targeting (added) | T-CT-016, T-CT-003 | Inventory whether the system collects or infers sleep, stress, neural, or affective signals. Restrict secondary use and provide a usable refusal or alternative. | [008](../research/008_operator_objectives_and_persuasion.md), [009](../research/009_relational_influence.md), [010](../research/010_domain_controls_and_readiness.md) |

---

## 5. Domain Readiness Assessment

This is a proposed, task-specific training rubric, not a validated personnel-readiness instrument. Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of six capability scores) x 20, producing a 0-100 scale.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| Circadian discipline | No workable rest or notification rule | Rest periods or urgent exceptions work inconsistently | A proportionate rest/notification rule and urgent exception are documented and exercised |
| Reward-loop interruption | All notifications live; autoplay and infinite scroll active | Partial notification control; some features disabled | Batched notifications; variable-reward features disabled; scheduled access only |
| Stress physiology monitoring | Workload and relevant exposure conditions are not reviewed | Conditions reviewed without a defined response | Workload and exposure conditions have a tested response; any sensitive monitoring is voluntary and appropriately governed |
| Neurological boundary awareness | No inventory of neural-capable devices | Devices known; data flows not reviewed | Full inventory; data flows documented; default-deny for neural data |
| Neurotech provenance | Devices adopted without review | Provenance checked informally | Formal provenance, firmware audit, hard disconnect verified before use |
| Substance awareness | Unmanaged | Recognized but unstructured | Managed as part of the exposure surface, integrated with sleep discipline |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. A low Domain 1 score triggers review of workload, conditions, and supporting evidence. It does not establish failure in another domain or a clinical condition.

---

<!-- domain-readiness:start -->
### Additional readiness checks

Keep the inherited capability score and denominator unchanged. Report these research-extension checks separately. Unknown is not zero. Use [the worksheet](../resources/readiness-worksheet.md) and [worked unit example](../examples/unit_readiness_assessment.md). Readiness is a task-specific assessment, not CTSS.

| M-ID | Check | 0 | 3 | 5 |
|---|---|---|---|---|
| M-014b | In a synthetic time-pressure drill, ask for a pause and handoff. Check that the consequential action waits for the authorized reviewer. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |
| M-016b | Use synthetic records to trace each sensitive signal to collection purpose, permitted use, deletion, and refusal route. Test an attempted marketing reuse. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |

Record the protocol, case set, catalog revision, date, assessor, evidence, failed cases, and remediation owner. No observed unit results were supplied, so current readiness remains unknown in all six domains. A documented capability is not a passed test.
<!-- domain-readiness:end -->

## 6. Training Protocols by Population

**Individual warfighter:** Circadian discipline integrated into operational readiness standards with the same rigor as physical fitness. Biometric baselining at accession; deviation review at periodic health assessment. Neurotech boundary training before any BCI-adjacent or wearable-heavy billet.

**Military families:** Household notification and device curfew standards. Sleep protection for dependents framed as cognitive defense, not screen-time moralizing. School-age education on reward-loop mechanics: children who understand the slot-machine design are measurably harder to capture.

**Organizations:** Command climate assessment includes biological exposure factors: after-hours notification expectations, platform-mediated tasking, sleep-hostile scheduling. Commanders accountable for unit-level biological readiness the way they are for physical readiness.

**Civilian society:** Public literacy on dopamine engineering as a design practice, not an accident. Advocacy for design transparency: platforms disclose variable-reward mechanics the way food producers disclose ingredients.

---

## 7. Measurable Outcomes and Failure Conditions

Primary outcome indicator (from CSF Table 5): **Sustained Attention Span**, with a 20-30 percent improvement threshold in controlled studies using attention hygiene interventions. Domain 1 supplies the physiological preconditions for that outcome; the measurement itself is shared with Domain 2.

Domain-specific measures: sleep architecture trend (duration, continuity, timing regularity), HRV baseline stability, notification-driven wake events, and self-reported versus tracked platform session counts (the divergence between the two is itself a capture indicator).

**Failure condition:** if biological capture persists (reward loops intact, sleep fragmented), all downstream training investment in Domains 2 through 6 produces compliance without capability. Interventions must verify Domain 1 stabilization before claiming higher-domain readiness gains.

---

## 8. Enforcement and Crosslinks

- **AI SAFE² UAS profile:** UAS-H6 measures attention capture in high-tempo decision environments; CTSS results feed the UAS profile evidence package (UAS-SCORE-001, UAS-HUMAN-001)
- **Taxonomy:** [Substrate Threats](../taxonomy/substrate-threats.md) (ST-002, ST-004) | [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-001, T-CT-003, T-CT-012) | [Delivery and Scale](../taxonomy/delivery-scale.md) (DS-004) | [CTSS Scoring](../taxonomy/ctss-scoring.md)
- **Edge case watch:** neuro-swarm integration (an open Biological/Neurological research gap; the historical 85 percent coverage estimate is unvalidated) is the intersection of this domain with [Research Note 002](../research/002_swarm_threat_scaling.md)
- **Adjacent domains:** [Domain 2: Cognitive](../02-cognitive/README.md) (immediate upward cascade target) | [Domain 6: Digital & AI Symbiosis](../06-digital-ai-symbiosis/README.md) (delivery-side governance)

> **The domain in one sentence:** protect the hardware, or nothing running on it can be protected.
