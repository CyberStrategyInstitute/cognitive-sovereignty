# Domain 01: Biological

### The Substrate the Adversary Reaches First

**CSF Position:** Domain 1 of 6 | **AI SAFE² CP.11 Control:** UAS-H6 (attention capture in high-tempo decision environments) | **Companion Research:** [002 Swarm Threat Scaling](../research/002_swarm_threat_scaling.md)

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
| T-CT-001 | Attention Capture and Habituation | Technique | CTSS 80 / Detection 4 | Reward circuitry via infinite scroll, variable rewards, notification saturation |
| T-CT-003 | Micro-Targeted Emotional Priming | Technique | CTSS 70 / Detection 2 | Stress physiology; elevated baseline anxiety, anger, fear |
| T-CT-012 | Neurotech / Direct Cognitive Influence | Technique | CTSS 60 / Detection 1 | Neurological integrity; persuasion or control below the information layer |
| DS-004 | Neuro-Digital Interfaces | Delivery | Detection 1 | Wearables and brain interfaces as always-on delivery channels |

**Threat trajectory note:** T-CT-012 carries the lowest current CTSS in the taxonomy (60) purely on likelihood. Its Impact on Agency score is 5, the maximum. As the neurotech surface matures, this domain's threat profile climbs faster than any other domain's. Build the defenses before the likelihood arrives.

---

## 3. Cascade Position

**Feeds upward (degradation cascade):** Sleep deprivation from dopamine-driven engagement (Domain 1) impairs cognitive function (Domain 2), reduces emotional regulation (Domain 3), strains relationships (Domain 4), undermines purpose (Domain 5), and dissolves the motivation to maintain AI interaction discipline (Domain 6).

**Receives from above (compromise cascade):** A compromised AI environment (Domain 6) delivers engineered stress and engagement pressure that manifests as biological load: cortisol elevation, sleep fragmentation, reward-system capture (Domain 1).

**Operational consequence:** single-domain interventions fail. An attention hygiene program (Domain 2) cannot succeed while the biological reward system remains captured (Domain 1). Sequence matters: biological stabilization is the precondition for every higher-domain intervention.

---

## 4. Protective Capabilities and Mitigation Catalog

Mitigation ID convention: `M-{threat}{b}` where the suffix letter maps to the domain (b = Biological), following the operational template established at T-CT-004 in the taxonomy.

| M-ID | Capability | Counters | Implementation |
| --- | --- | --- | --- |
| M-001b | Circadian discipline | T-CT-001, ST-002 | Fixed sleep window enforcement; no engagement-optimized platforms within 90 minutes of sleep; blue-light and notification curfews as unit standard, not personal preference |
| M-S02b | Reward-loop interruption | ST-002 | Notification batching, variable-reward feature disablement (autoplay, infinite scroll, badges), scheduled rather than triggered platform access |
| M-003b | Stress physiology monitoring | T-CT-003 | Biometric baseline tracking (HRV, resting heart rate, sleep architecture); deviation alerts treated as potential exposure indicators, not just health data |
| M-S04b | Neurological boundary awareness | ST-004, DS-004 | Formal inventory of every device with neural or affect-modulating capability; consent and data-flow review before adoption; default-deny posture for neural data collection |
| M-012b | Neurotech provenance and air-gap | T-CT-012, ST-004 | No closed-loop neurofeedback or stimulation devices without verified provenance, auditable firmware, and hard disconnect capability; bioethics review for any operational neurotech |
| M-001b2 | Substance and stimulant awareness | T-CT-001 cascade | Recognition that caffeine, alcohol, and stimulant patterns compound platform-driven sleep disruption; managed as part of the same exposure surface |

---

## 5. Domain Readiness Assessment

Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of six capability scores) x 20, producing a 0-100 scale.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| Circadian discipline | No fixed sleep window; devices in sleep environment | Window kept most nights; devices present but silenced | Fixed window kept; sleep environment device-free; verified by tracking |
| Reward-loop interruption | All notifications live; autoplay and infinite scroll active | Partial notification control; some features disabled | Batched notifications; variable-reward features disabled; scheduled access only |
| Stress physiology monitoring | No baseline data | Occasional tracking; no deviation response | Continuous baseline; deviations trigger a defined response protocol |
| Neurological boundary awareness | No inventory of neural-capable devices | Devices known; data flows not reviewed | Full inventory; data flows documented; default-deny for neural data |
| Neurotech provenance | Devices adopted without review | Provenance checked informally | Formal provenance, firmware audit, hard disconnect verified before use |
| Substance awareness | Unmanaged | Recognized but unstructured | Managed as part of the exposure surface, integrated with sleep discipline |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. A Compromised Domain 1 score invalidates readiness claims in Domains 2 through 6 regardless of their individual scores, because the cascade guarantees degradation in progress.

---

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

- **AI SAFE² CP.11:** UAS-H6 measures attention capture in high-tempo decision environments; CTSS results feed the CP.11 evidence package (UAS-SCORE-001, UAS-HUMAN-001)
- **Taxonomy:** [Substrate Threats](../taxonomy/substrate-threats.md) (ST-002, ST-004) | [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-001, T-CT-003, T-CT-012) | [Delivery and Scale](../taxonomy/delivery-scale.md) (DS-004) | [CTSS Scoring](../taxonomy/ctss-scoring.md)
- **Edge case watch:** neuro-swarm integration (the coverage gap flagged at 85 percent for the Biological/Neurological spectrum) is the intersection of this domain with [Research Note 002](../research/002_swarm_threat_scaling.md)
- **Adjacent domains:** [Domain 2: Cognitive](../02-cognitive/README.md) (immediate upward cascade target) | [Domain 6: Digital & AI Symbiosis](../06-digital-ai-symbiosis/README.md) (delivery-side governance)

> **The domain in one sentence:** protect the hardware, or nothing running on it can be protected.
