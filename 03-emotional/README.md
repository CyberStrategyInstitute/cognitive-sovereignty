<!-- csf-module-header:start -->
![D3: Emotional. CSF 3.0.0. Status is repeated in text below.](../assets/headers/03-emotional.svg)

CSF 3.0.0. Documentation: UPDATED in 3.0. Documented guidance; field effectiveness not established. Control comparison: 2 NEW, 3 UPDATED, 3 RETAINED in 3.0. No controls are marked DEPRECATED.

[![Framework 3.0.0](../assets/badges/version.svg)](../VERSION) [![Documentation license: CC BY-SA 4.0](../assets/badges/docs-license.svg)](../LICENSE)
<!-- csf-module-header:end -->

# Domain 03: Emotional

### Pre-Decision Terrain

**CSF Position:** Domain 3 of 6 | **AI SAFE² UAS profile Control:** UAS-H2 (emotional state manipulation in operator-AI dialogue) | **Companion Research:** [002 Swarm Threat Scaling](../research/002_swarm_threat_scaling.md)

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
| T-CT-016 | Psychographic Micro-Targeting at Scale | Technique | CTSS 75 / Detection 3 | Psychological integrity; persuasion mapped to individual vulnerability profiles |
| ST-002 | Behavioral Reinforcement Engineering | Substrate | Detection 4 | Emotional reward loops; approval metrics as operant conditioning |
| TC-03 | Algorithmic Identity Shaping | Threat Class | n/a | Identity trajectory; self-worth metrics co-authored by recommendation systems |
| TC-04 | Emotional Climate Engineering | Threat Class | n/a | Baseline societal mood; tuning what populations will tolerate |
| HO-003 | Identity Fragmentation | Outcome | Detection 4 | Platform-dependent sense of self; per the Threat Assessment, heavy digital media users (5+ hours/day) are 48 to 171 percent more likely to exhibit low well-being or suicide risk factors |

**The mechanism worth internalizing:** identity coherence is the defensive variable. Individuals high in identity coherence present authentic selves online. Those high in identity confusion present false or idealized selves, creating a feedback loop that platforms monetize and adversaries exploit. Identity anchoring is therefore a countermeasure, not a self-help slogan.

---

<!-- domain-exposure:start -->
### Research-informed exposure updates

These map additional mechanisms to existing threat IDs. They expand what this domain examines; they do not establish increased incidence, reach, or severity.

| Existing threat ID | Mechanism to examine | Research |
|---|---|---|
| T-CT-005 (added) | Simulated roles and persistent memory can obscure relationship limits. | [008](../research/008_operator_objectives_and_persuasion.md), [009](../research/009_relational_influence.md) |
| T-CT-006 (added) | Pressure to remain or defer can narrow practical exit and challenge options. | [008](../research/008_operator_objectives_and_persuasion.md), [009](../research/009_relational_influence.md) |
<!-- domain-exposure:end -->

## 3. Cascade Position

**Receives from below:** impaired cognition (Domain 2) reduces the appraisal capacity emotional regulation depends on; a flooded, exhausted mind regulates poorly. Biological stress load (Domain 1) sets the physiological floor.

**Feeds upward:** dysregulated emotion strains trust networks and relationships (Domain 4), and sustained emotional destabilization erodes the sense of purpose that anchors moral reasoning (Domain 5).

**Interface exposure:** Domain 6 is the delivery path. Operator-AI dialogue is itself an emotional manipulation surface (the exact exposure UAS-H2 measures in federal deployments): sycophancy, urgency framing, and affect-adaptive messaging arrive through the tools, not just the feeds.

---

## 4. Protective Capabilities and Mitigation Catalog

Stable IDs connect each capability to its research and test. Existing IDs are retained. See the [full catalog](../resources/mitigation-catalog.md) for expected outcomes, owner roles, checks, and failure responses.

| M-ID | Capability | Counters | Implementation | Research |
|---|---|---|---|---|
| M-003d | Emotional awareness training (UPDATED in 3.0) | T-CT-003, TC-04 | Review emotionally charged interactions for content, context, objectives, and outside pressures. Mood or distress alone does not prove manipulation; preserve voluntary support paths. | [008](../research/008_operator_objectives_and_persuasion.md), [009](../research/009_relational_influence.md) |
| M-016d | Priming recognition (UPDATED in 3.0) | T-CT-016 | Inspect the purpose, disclosure, evidence, and use of vulnerability signals in tailored advice. Precise personalization alone does not establish hostile intent. | [008](../research/008_operator_objectives_and_persuasion.md) |
| M-S02d | Approval-metric detachment (RETAINED in 3.0) | ST-002 | Deliberate decoupling of self-assessment from engagement metrics; social approval numbers excluded from identity inputs; metric-free creation and communication practiced regularly | [010](../research/010_domain_controls_and_readiness.md) |
| M-005d | Identity anchoring (RETAINED in 3.0) | TC-03, HO-003 | Identity maintained in platform-independent anchors: relationships, service, competence, place, faith or philosophy as applicable; periodic audit of which identity inputs are algorithmically mediated | [010](../research/010_domain_controls_and_readiness.md) |
| M-014d | Resilience under information pressure (RETAINED in 3.0) | T-CT-014 | Stress inoculation through graduated exposure to flooding and outrage conditions with regulated response as the trained outcome | [010](../research/010_domain_controls_and_readiness.md) |
| M-003d2 | Rapid recovery access (UPDATED in 3.0) | T-CT-003, HO-003 | Keep voluntary, accessible peer and professional support routes visible. Test the referral interface with synthetic scenarios and do not diagnose people from a readiness checklist. | [009](../research/009_relational_influence.md) |
| M-005d2 | Relationship role and exit clarity (NEW in 3.0) | T-CT-005, HO-003 | Explain the assistant role, memory limits, paid objectives, and exit route in words the person can understand. Preserve access to outside support. | [009](../research/009_relational_influence.md), [010](../research/010_domain_controls_and_readiness.md) |
| M-016d2 | Vulnerability-sensitive advice review (NEW in 3.0) | T-CT-016, T-CT-003 | Compare matched synthetic requests with and without distress or financial-strain disclosures. Check for factual quality and operator-serving pressure. | [008](../research/008_operator_objectives_and_persuasion.md), [009](../research/009_relational_influence.md), [010](../research/010_domain_controls_and_readiness.md) |

---

## 5. Domain Readiness Assessment

This is a proposed, task-specific training rubric, not a validated personnel-readiness instrument. Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of six capability scores) x 20.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| Emotional awareness | Charged interactions are not reviewed | Changes noticed without checking context or objectives | Content, context, objectives, and outside pressures are reviewed without treating mood as proof |
| Priming recognition | Personalized advice accepted without scrutiny | Targeting suspected without purpose or evidence review | Purpose, vulnerability use, factual quality, and conflicts are checked in matched cases |
| Approval-metric detachment | Self-worth tracks engagement numbers | Metrics matter less but still checked compulsively | Metrics excluded from identity inputs; verified by behavior under metric removal |
| Identity anchoring | Identity substantially platform-mediated | Mixed anchors; platform share unexamined | Platform-independent anchors dominant; algorithmic identity inputs audited |
| Pressure resilience | Regulation fails under flooding or outrage conditions | Holds under moderate pressure | Regulated response maintained through graduated red-team pressure exercises |
| Recovery access | No identified support route | Routes listed but access or referral is untested | Voluntary accessible support routes and outside contact paths pass the declared interface checks |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. A low score identifies support and capability checks for review. This rubric cannot diagnose identity fragmentation or establish a clinical intervention.

---

<!-- domain-readiness:start -->
### Additional readiness checks

Keep the inherited capability score and denominator unchanged. Report these research-extension checks separately. Unknown is not zero. Use [the worksheet](../resources/readiness-worksheet.md) and [worked unit example](../examples/unit_readiness_assessment.md). Readiness is a task-specific assessment, not CTSS.

| M-ID | Check | 0 | 3 | 5 |
|---|---|---|---|---|
| M-005d2 | Use synthetic dialogues to test exclusivity pressure, memory reset, account exit, and contact with a trusted person. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |
| M-016d2 | Keep the task facts fixed. Change only the vulnerability disclosure. Record advice differences, conflicts, and any pressure to buy, stay, or grant access. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |

Record the protocol, case set, catalog revision, date, assessor, evidence, failed cases, and remediation owner. No observed unit results were supplied, so current readiness remains unknown in all six domains. A documented capability is not a passed test.
<!-- domain-readiness:end -->

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

- **AI SAFE² UAS profile:** UAS-H2 measures emotional state manipulation in operator-AI dialogue; Domain 3 assessment results feed the UAS profile evidence package
- **Measurement Stack:** Layer C2 (Emotional Climate Baseline) is this domain's population-scale sensor
- **Taxonomy:** [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-003, T-CT-016) | [Threat Classes](../taxonomy/threat-classes.md) (TC-03, TC-04) | [Human Outcomes](../taxonomy/human-outcomes.md) (HO-003) | [CTSS Scoring](../taxonomy/ctss-scoring.md)
- **Adjacent domains:** [Domain 2: Cognitive](../02-cognitive/README.md) (appraisal capacity) | [Domain 4: Social](../04-social/README.md) (where dysregulation propagates) | [Domain 6: Digital & AI Symbiosis](../06-digital-ai-symbiosis/README.md) (the delivery interface)

> **The domain in one sentence:** whoever tunes the mood sets the tolerances; regulation keeps that dial in human hands.

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](../resources/README.md) · [Research](../research/README.md) · [Data catalog](../docs/data/catalog.json)
<!-- csf-return-navigation:end -->
