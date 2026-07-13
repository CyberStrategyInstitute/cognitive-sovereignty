# Domain 03: Emotional

### Pre-Decision Terrain

**CSF Position:** Domain 3 of 6 | **AI SAFE² CP.11 Control:** UAS-H2 (emotional state manipulation in operator-AI dialogue) | **Companion Research:** [002 Swarm Threat Scaling](../research/002_swarm_threat_scaling.md)

---

## 1. Doctrine

Stress tolerance, emotional regulation, identity stability, and trauma recovery are targeted for a precise strategic reason: emotion determines what populations will tolerate. The Cognitive Threat Assessment classifies emotional climate engineering (TC-04) as pre-decision manipulation. The adversary does not need to persuade a thought. It tunes the baseline mood, and the tolerances shift on their own. A population held in chronic anxiety accepts surveillance. In chronic anger, it accepts conflict. In chronic hopelessness, it accepts authoritarian promises.

At the individual level, the same mechanics run through micro-targeted emotional priming and psychographic profiling: personalized content that elevates baseline anxiety, anger, or fear in specific populations, delivered against psychological vulnerability maps built at scale. The second attack surface is identity itself. When recommendation systems co-author a person's identity trajectory (lifestyle, values, relationships, self-worth metrics), identity becomes platform-dependent, and a platform-dependent identity is a manipulable one.

> **So what:** an emotionally destabilized operator fails every downstream test. Regulation is not soft-skills training. It is the armor between engineered emotional climate and captured decisions.

---

## 2. Threat Exposure

| ID | Threat | Layer | CTSS / Detection | What It Targets in This Domain |
| --- | --- | --- | --- | --- |
| T-CT-003 | Micro-Targeted Emotional Priming | Technique | CTSS 70 / Detection 2 | Emotional stability; elevated baseline anxiety, anger, fear in targeted populations |
| T-CT-016 | Psychographic Micro-Targeting at Scale | Technique | CTSS 79 / Detection 3 | Psychological integrity; persuasion mapped to individual vulnerability profiles |
| ST-002 | Behavioral Reinforcement Engineering | Substrate | Detection 4 | Emotional reward loops; approval metrics as operant conditioning |
| TC-03 | Algorithmic Identity Shaping | Threat Class | n/a | Identity trajectory; self-worth metrics co-authored by recommendation systems |
| TC-04 | Emotional Climate Engineering | Threat Class | n/a | Baseline societal mood; tuning what populations will tolerate |
| HO-003 | Identity Fragmentation | Outcome | Detection 4 | Platform-dependent sense of self; per the Threat Assessment, heavy digital media users (5+ hours/day) are 48 to 171 percent more likely to exhibit low well-being or suicide risk factors |

**The mechanism worth internalizing:** identity coherence is the defensive variable. Individuals high in identity coherence present authentic selves online. Those high in identity confusion present false or idealized selves, creating a feedback loop that platforms monetize and adversaries exploit. Identity anchoring is therefore a countermeasure, not a self-help slogan.

---

## 3. Cascade Position

**Receives from below:** impaired cognition (Domain 2) reduces the appraisal capacity emotional regulation depends on; a flooded, exhausted mind regulates poorly. Biological stress load (Domain 1) sets the physiological floor.

**Feeds upward:** dysregulated emotion strains trust networks and relationships (Domain 4), and sustained emotional destabilization erodes the sense of purpose that anchors moral reasoning (Domain 5).

**Interface exposure:** Domain 6 is the delivery path. Operator-AI dialogue is itself an emotional manipulation surface (the exact exposure UAS-H2 measures in federal deployments): sycophancy, urgency framing, and affect-adaptive messaging arrive through the tools, not just the feeds.

---

## 4. Protective Capabilities and Mitigation Catalog

Mitigation ID convention: `M-{threat}{d}` (d = Emotional), per the taxonomy's operational template.

| M-ID | Capability | Counters | Implementation |
| --- | --- | --- | --- |
| M-003d | Emotional awareness training | T-CT-003, TC-04 | Baseline mood self-monitoring; recognition that a shift in baseline anxiety, anger, or urgency may be an exposure indicator rather than an internal state; structured after-action review of emotionally charged content encounters |
| M-016d | Priming recognition | T-CT-016 | Training on psychographic targeting mechanics; the tell is content that lands too precisely on personal vulnerabilities; treat precision-targeted emotional content as hostile until proven organic |
| M-S02d | Approval-metric detachment | ST-002 | Deliberate decoupling of self-assessment from engagement metrics; social approval numbers excluded from identity inputs; metric-free creation and communication practiced regularly |
| M-005d | Identity anchoring | TC-03, HO-003 | Identity maintained in platform-independent anchors: relationships, service, competence, place, faith or philosophy as applicable; periodic audit of which identity inputs are algorithmically mediated |
| M-014d | Resilience under information pressure | T-CT-014 cascade | Stress inoculation through graduated exposure to flooding and outrage conditions with regulated response as the trained outcome |
| M-003d2 | Rapid recovery access | T-CT-003, HO-003 | Pre-identified counseling and peer support paths; community moderator capacity to cool emotional hotspots before they cascade (per the taxonomy's M-004d pattern) |

---

## 5. Domain Readiness Assessment

Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of six capability scores) x 20.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| Emotional awareness | Baseline shifts unnoticed or attributed inward by default | Shifts noticed after the fact | Baseline monitored; shifts assessed for exposure causes in near real time |
| Priming recognition | Precision-targeted content consumed unexamined | Targeting recognized on reflection | Precision emotional content flagged on contact; provenance questioned before reaction |
| Approval-metric detachment | Self-worth tracks engagement numbers | Metrics matter less but still checked compulsively | Metrics excluded from identity inputs; verified by behavior under metric removal |
| Identity anchoring | Identity substantially platform-mediated | Mixed anchors; platform share unexamined | Platform-independent anchors dominant; algorithmic identity inputs audited |
| Pressure resilience | Regulation fails under flooding or outrage conditions | Holds under moderate pressure | Regulated response maintained through graduated red-team pressure exercises |
| Recovery access | No identified support paths | Paths known, untested | Paths pre-identified, exercised, and normalized within the unit or family |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. A Compromised Domain 3 score under high platform exposure is the HO-003 risk profile and warrants immediate intervention, not a training plan.

---

## 6. Training Protocols by Population

**Individual warfighter:** Stress inoculation extended from combat stressors to information-environment stressors: graduated exposure to outrage, flooding, and precision-primed content with regulation as the scored outcome. Identity anchoring assessed at accession and PME touchpoints.

**Military families:** Identity anchoring for dependents is the priority line of effort; adolescents are the primary target population for TC-03 and carry the HO-003 statistics. Household norms that keep approval metrics out of self-worth conversations. Spouse networks trained on priming recognition, since family channels are trusted channels and trusted channels are injection targets (T-CT-004).

**Organizations:** Command climate assessment includes emotional climate telemetry: is the unit's baseline mood being tuned by its information diet? Emotional hotspot response capacity (trained moderators, rapid counseling access) resourced as an operational capability.

**Civilian society:** Public literacy on emotional climate engineering: populations that know their mood is a targetable surface are harder to tune. Platform accountability advocacy for psychographic targeting transparency.

---

## 7. Measurable Outcomes and Failure Conditions

Primary outcome indicators (CSF Table 5):

- **Stable Moral Reasoning Under Pressure** (shared with Domain 5): consistent ethical judgment when social pressure or emotional manipulation suggests compliance
- **Ability to Act Against Social Manipulation:** measurable independence during red-team social pressure exercises, including manufactured outrage scenarios

Domain-specific measures: population and unit emotional climate baselines tracked longitudinally (Measurement Stack C2: persistent elevation of anxiety, anger, hopelessness, meaninglessness predicts susceptibility to extreme solutions), identity coherence assessments, and regulation performance under graduated pressure exercises.

**Failure condition:** persistent baseline elevation that goes unmeasured is a strategic warning missed. If emotional climate telemetry is absent, the earliest indicator of population-scale cognitive attack is invisible, and the framework detects the campaign only at the belief-instability stage (HO-002), which is later and costlier.

---

## 8. Enforcement and Crosslinks

- **AI SAFE² CP.11:** UAS-H2 measures emotional state manipulation in operator-AI dialogue; Domain 3 assessment results feed the CP.11 evidence package
- **Measurement Stack:** Layer C2 (Emotional Climate Baseline) is this domain's population-scale sensor
- **Taxonomy:** [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-003, T-CT-016) | [Threat Classes](../taxonomy/threat-classes.md) (TC-03, TC-04) | [Human Outcomes](../taxonomy/human-outcomes.md) (HO-003) | [CTSS Scoring](../taxonomy/ctss-scoring.md)
- **Adjacent domains:** [Domain 2: Cognitive](../02-cognitive/README.md) (appraisal capacity) | [Domain 4: Social](../04-social/README.md) (where dysregulation propagates) | [Domain 6: Digital & AI Symbiosis](../06-digital-ai-symbiosis/README.md) (the delivery interface)

> **The domain in one sentence:** whoever tunes the mood sets the tolerances; regulation keeps that dial in human hands.
