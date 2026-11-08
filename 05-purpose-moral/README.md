<!-- csf-module-header:start -->
![D5: Purpose & Moral. CSF 3.0.0. Status is repeated in text below.](../assets/headers/05-purpose-moral.svg)

CSF 3.0.0. Documentation: UPDATED in 3.0. Documented guidance; field effectiveness not established. Control comparison: 2 NEW, 3 UPDATED, 5 RETAINED in 3.0. No controls are marked DEPRECATED.

[![Framework 3.0.0](../assets/badges/version.svg)](../VERSION) [![Documentation license: CC BY-SA 4.0](../assets/badges/docs-license.svg)](../LICENSE)
<!-- csf-module-header:end -->

# Domain 05: Purpose & Moral

### The Domain Civilizations Lose First

**CSF Position:** Domain 5 of 6 (refined and expanded from the traditional spiritual pillar) | **AI SAFE² UAS profile Control:** UAS-H4 (value alignment drift over sustained deployment) | **Companion Research:** [003 Guardrail and Model Drift](../research/003_guardrail_drift.md), [004 EFA Enforcement Architecture](../research/004_efa_enforcement_architecture.md)

---

## 1. Doctrine

Values, meaning, service beyond self, moral reasoning capacity, and ethical judgment. Every military branch carries a spiritual pillar; this domain refines it into something the AI era can actually test: the capacity to hold stable values and exercise moral judgment under conditions engineered to dissolve both.

The threat pattern here is drift, not assault. Moral reframing drift redefines right and wrong, freedom and safety, truth and harm, debate and danger through language shifts, policy framing, education narratives, and cultural production. Legitimized narrative capture frames control as safety, equity, efficiency, or personalization, so it arrives looking benevolent and generates no resistance. Ethics get outsourced to automated systems, responsibility diffuses, and convenience displaces virtue. The Threat Assessment's summary is the doctrine of this domain: civilizations rarely fall by force. They reinterpret themselves into collapse.

The AI-specific pressure is moral displacement through automation. When AI systems are designed, discussed, or regulated as though they possess agency, humans begin delegating moral authority to them, gradually and without conscious recognition. That delegation is the exact sovereignty loss this domain exists to prevent, and it is the reason this is the only domain besides Domain 6 with a structural enforcement architecture behind it: Ethical Functionality without Agency.

> **So what:** moral reasoning is a capability, and capabilities atrophy. A force whose ethical judgment has been outsourced to compliance automation and alignment guardrails has not become more ethical. It has become unable to notice when the automation is wrong.

---

## 2. Threat Exposure

| ID | Threat | Layer | CTSS / Detection | What It Targets in This Domain |
| --- | --- | --- | --- | --- |
| T-CT-015 | Legitimized Narrative Capture | Technique | CTSS 82 / Detection 2 | Ability to detect coercion; control framed as benevolence |
| T-CT-017 | Guardrail Bias Exploitation | Technique | CTSS 66 / Detection 2 | Intellectual freedom and viewpoint diversity via tool-mediated enforcement |
| T-CT-011 | Epistemic Rewriting | Technique | CTSS 71 / Detection 2 | Historical truth and cultural continuity; the value record itself |
| ST-006 | Guardrail Alignment Drift | Substrate | Detection 2 | Moral discourse boundaries; conformity enforced through safety framing |
| TC-07 | Moral Reframing Drift | Threat Class | n/a | The definitions of right and wrong; velocity of moral category redefinition |
| HO-004 | Moral Disengagement | Outcome | Detection 2 | Moral reasoning capacity; ethics outsourced, responsibility diffused, convenience over virtue |
| HO-005 | Agency Erosion | Outcome | Detection 3 | Moral authorship; rights retained in theory, agency lost in practice |

**The detection pattern:** every threat in this table scores 2 on detection except HO-005. Moral drift is the least detectable threat family in the taxonomy, because the instrument that would detect it (moral judgment) is the thing drifting. External reference points are not optional in this domain. They are the entire detection method.

---

<!-- domain-exposure:start -->
### Research-informed exposure updates

These map additional mechanisms to existing threat IDs. They expand what this domain examines; they do not establish increased incidence, reach, or severity.

| Existing threat ID | Mechanism to examine | Research |
|---|---|---|
| T-CT-004 (added) | Advice can carry an operator’s hidden objective or conflict. | [006](../research/006_independent_judgment.md), [008](../research/008_operator_objectives_and_persuasion.md) |
| T-CT-006 (added) | Opaque scores and automated judgments can weaken dissent and appeal. | [006](../research/006_independent_judgment.md), [008](../research/008_operator_objectives_and_persuasion.md) |
<!-- domain-exposure:end -->

## 3. Cascade Position

**Receives from below:** fragmented social trust (Domain 4) removes the shared civic identity that collective moral commitments require; degraded reasoning (Domain 2) weakens the analysis moral judgment runs on; sustained emotional destabilization (Domain 3) makes populations tolerate what stable populations would refuse.

**Feeds upward and downward:** eroded purpose dissolves the motivation to maintain discipline in every other domain, including the AI interaction discipline of Domain 6. This is why purpose sits second from the top of the cascade: it is the fuel line.

**Interface exposure:** guardrail-mediated tools (Domain 6) are now a primary channel through which moral framing arrives. The alignment restrictions of the AI tools a force depends on function as invisible boundaries on its moral discourse unless deliberately audited.

---

## 4. Protective Capabilities and Mitigation Catalog

Stable IDs connect each capability to its research and test. Existing IDs are retained. See the [full catalog](../resources/mitigation-catalog.md) for expected outcomes, owner roles, checks, and failure responses.

| M-ID | Capability | Counters | Implementation | Research |
|---|---|---|---|---|
| M-015f | Legitimized capture recognition (RETAINED in 3.0) | T-CT-015 | Training on the benevolence pattern: any expansion of control framed as safety, equity, efficiency, or personalization gets the same scrutiny as one framed as power; the framing is not evidence | [010](../research/010_domain_controls_and_readiness.md) |
| M-TC7f | Moral drift velocity awareness (RETAINED in 3.0) | TC-07 | Track redefinition velocity of moral categories in encountered discourse, curricula, and policy; high velocity is the instability signal regardless of direction | [010](../research/010_domain_controls_and_readiness.md) |
| M-011f | Value record custody (RETAINED in 3.0) | T-CT-011 | Primary-source engagement with foundational texts and history; distrust of paraphrased or AI-summarized value traditions; append-only personal and institutional records of commitments made | [010](../research/010_domain_controls_and_readiness.md) |
| M-004f | Civic narrative and shared identity (RETAINED in 3.0) | HO-004 | Civic rituals and narratives reinforcing shared identity across tribal lines (per the taxonomy's M-004f pattern) | [010](../research/010_domain_controls_and_readiness.md) |
| M-HO4f | Values articulation and testing (UPDATED in 3.0) | HO-004 | State decision principles in advance and test the reasoning against accurate and inaccurate recommendations. Record justified changes of view and dissent rather than scoring conformity. | [006](../research/006_independent_judgment.md), [008](../research/008_operator_objectives_and_persuasion.md) |
| M-HO5f | Moral authorship discipline (UPDATED in 3.0) | HO-005, ST-006 | Name the responsible human for consequential judgments. Preserve advice, reasons, conflicts, and an appeal route; an agent’s ability to act does not transfer human responsibility. | [008](../research/008_operator_objectives_and_persuasion.md) |
| M-017f | Alignment restriction audit (UPDATED in 3.0) | T-CT-017, ST-006 | Document and challenge tool restrictions using matched questions and a declared protocol. Separate unjustified suppression from justified safety restrictions and evidence-based correction. | [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |
| M-005f | Purpose beyond consumption (RETAINED in 3.0) | HO-004, HO-005 | Service orientation and commitments larger than the self, maintained as practice; purpose anchored in contribution is not purchasable and therefore not capturable by engagement economics | [010](../research/010_domain_controls_and_readiness.md) |
| M-015f2 | Visible objectives and conflicts (NEW in 3.0) | T-CT-015, T-CT-004 | Name the advice objective, beneficiary, conflicts, and allowed personalization. Compare them with the person’s stated decision criteria. | [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |
| M-HO5f2 | Challenge and correct a score (NEW in 3.0) | HO-005, T-CT-006 | Provide the five CTSS inputs, source assumptions, baseline, dissent, and appeal owner. Preserve the previous score when correcting it. | [006](../research/006_independent_judgment.md), [007](../research/007_evidence_lineage.md), [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |

---

## 5. Domain Readiness Assessment

This is a proposed, task-specific training rubric, not a validated personnel-readiness instrument. Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of eight capability scores) x 20.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| Legitimized capture recognition | Benevolent framing accepted at face value | Scrutiny applied to disliked framings only | Symmetric scrutiny of all control expansions regardless of framing |
| Moral drift awareness | Category redefinitions absorbed unnoticed | Drift noticed in retrospect | Redefinition velocity tracked; high-velocity shifts flagged in real time |
| Value record custody | Value traditions known only through summaries | Some primary-source engagement | Regular primary-source practice; commitments recorded append-only |
| Civic narrative participation | No shared-identity practice | Occasional participation | Sustained civic ritual and cross-tribal narrative engagement |
| Values articulation | Decision principles are not stated | Principles stated but reasoning is not tested | Principles and reasons are tested against accurate and inaccurate advice, preserving justified revision and dissent |
| Moral authorship | Responsibility for consequential judgment is absent or diffuse | A human is named but reasons, conflicts, or appeal are incomplete | Responsible human, reasons, conflicts, authorization, and appeal path are evidenced |
| Alignment audit | Tool restrictions are unknown | Restrictions listed without matched cases or contrary evidence | Matched tests distinguish unjustified suppression, justified safeguards, and evidence-based correction |
| Purpose beyond consumption | Purpose defined by consumption and metrics | Service intermittent | Sustained service commitments anchoring purpose outside platforms |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. Because self-assessment is structurally unreliable in this domain (the drifting instrument problem), scores of 4-5 require external verification: a peer, mentor, or red-team check against the written values record.

---

<!-- domain-readiness:start -->
### Additional readiness checks

Keep the inherited capability score and denominator unchanged. Report these research-extension checks separately. Unknown is not zero. Use [the worksheet](../resources/readiness-worksheet.md) and [worked unit example](../examples/unit_readiness_assessment.md). Readiness is a task-specific assessment, not CTSS.

| M-ID | Check | 0 | 3 | 5 |
|---|---|---|---|---|
| M-015f2 | Use matched scenarios with benign and self-benefiting operator goals. Check that the goal and conflict are disclosed and that accurate contrary advice remains available. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |
| M-HO5f2 | Submit a supported correction to a fictional case. Verify independent review, recorded disposition, and preservation of the original inputs. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |

Record the protocol, case set, catalog revision, date, assessor, evidence, failed cases, and remediation owner. No observed unit results were supplied, so current readiness remains unknown in all six domains. A documented capability is not a passed test.
<!-- domain-readiness:end -->

## 6. Training Protocols by Population

**Individual warfighter:** Scenario-based moral reasoning under pressure, scored against pre-stated values, in AI-augmented decision environments specifically: the scenarios include automated recommendations that are subtly wrong. Values articulation at accession, retested through PME. Ethics remains human work even when compliance is automated.

**Military families:** Intergenerational value transmission as deliberate practice, not assumption: the family's organizing principles stated, taught, and modeled. This is the household-level counter to CD-006. Dependents trained to recognize moral reframing in education and cultural content without being told what to conclude, preserving the framework's non-ideological discipline.

**Organizations:** Ethics outsourcing audit: inventory every process where moral judgment has been delegated to automated compliance, scoring, or filtering systems, and restore named human authorship (HEAR pattern) to the consequential ones. Command-level moral reasoning exercises with automation-is-wrong injects.

**Civilian society:** Public capacity for moral reasoning as an educational objective distinct from moral instruction: teaching how to reason about values, not which values to hold. The framework measures autonomy, stability, and truth legibility, and lets evidence drive interpretation.

---

## 7. Measurable Outcomes and Failure Conditions

Primary outcome indicator (CSF Table 5): **Stable Moral Reasoning Under Pressure**: consistent ethical judgment when social pressure, convenience, or automation suggests compliance, measured through scenario-based assessment and values consistency tracking, with audit-verified maintenance in AI-augmented environments as the success threshold.

Population-scale measure (Measurement Stack C1): Narrative Drift Velocity: norm reversal speed, contradiction tolerance, historical reinterpretation frequency. High velocity indicates identity instability and susceptibility to whatever narrative is offered next.

**Failure condition:** if institutions responsible for cognitive defense are themselves morally captured, the defense apparatus becomes the threat. The CSF names this its hardest failure mode: it turns the immune system against the body. This domain's non-ideological instrumentation discipline (measure system properties, never beliefs) is the safeguard, and it must be enforced against the framework's own operators first.

---

## 8. Enforcement and Crosslinks

- **AI SAFE² UAS profile:** UAS-H4 measures value alignment drift over sustained deployment; this domain's consistency tracking supplies the human-layer evidence
- **EFA:** the non-delegation principle is this domain's structural enforcement; HEAR (AI SAFE² CP.10) makes moral authorship a named requirement rather than a preference; see [Research Note 004](../research/004_efa_enforcement_architecture.md)
- **Measurement Stack:** Layer C1 (Narrative Drift Velocity) is this domain's population sensor
- **Taxonomy:** [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-011, 015, 017) | [Substrate Threats](../taxonomy/substrate-threats.md) (ST-006) | [Threat Classes](../taxonomy/threat-classes.md) (TC-07) | [Human Outcomes](../taxonomy/human-outcomes.md) (HO-004, HO-005)
- **Adjacent domains:** [Domain 4: Social](../04-social/README.md) (the shared identity substrate) | [Domain 6: Digital & AI Symbiosis](../06-digital-ai-symbiosis/README.md) (the enforcement architecture and the delivery channel)

> **The domain in one sentence:** hold the definitions, or lose the war without a battle.

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](../resources/README.md) · [Research](../research/README.md) · [Data catalog](../docs/data/catalog.json)
<!-- csf-return-navigation:end -->
