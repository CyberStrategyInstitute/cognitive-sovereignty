# Domain 05: Purpose & Moral

### The Domain Civilizations Lose First

**CSF Position:** Domain 5 of 6 (refined and expanded from the traditional spiritual pillar) | **AI SAFE² CP.11 Control:** UAS-H4 (value alignment drift over sustained deployment) | **Companion Research:** [003 Guardrail and Model Drift](../research/003_guardrail_drift.md), [004 EFA Enforcement Architecture](../research/004_efa_enforcement_architecture.md)

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
| T-CT-015 | Legitimized Narrative Capture | Technique | CTSS 81 / Detection 2 | Ability to detect coercion; control framed as benevolence |
| T-CT-017 | Guardrail Bias Exploitation | Technique | CTSS 70 / Detection 2 | Intellectual freedom and viewpoint diversity via tool-mediated enforcement |
| T-CT-011 | Epistemic Rewriting | Technique | CTSS 65 / Detection 2 | Historical truth and cultural continuity; the value record itself |
| ST-006 | Guardrail Alignment Drift | Substrate | Detection 2 | Moral discourse boundaries; conformity enforced through safety framing |
| TC-07 | Moral Reframing Drift | Threat Class | n/a | The definitions of right and wrong; velocity of moral category redefinition |
| HO-004 | Moral Disengagement | Outcome | Detection 2 | Moral reasoning capacity; ethics outsourced, responsibility diffused, convenience over virtue |
| HO-005 | Agency Erosion | Outcome | Detection 3 | Moral authorship; rights retained in theory, agency lost in practice |

**The detection pattern:** every threat in this table scores 2 on detection except HO-005. Moral drift is the least detectable threat family in the taxonomy, because the instrument that would detect it (moral judgment) is the thing drifting. External reference points are not optional in this domain. They are the entire detection method.

---

## 3. Cascade Position

**Receives from below:** fragmented social trust (Domain 4) removes the shared civic identity that collective moral commitments require; degraded reasoning (Domain 2) weakens the analysis moral judgment runs on; sustained emotional destabilization (Domain 3) makes populations tolerate what stable populations would refuse.

**Feeds upward and downward:** eroded purpose dissolves the motivation to maintain discipline in every other domain, including the AI interaction discipline of Domain 6. This is why purpose sits second from the top of the cascade: it is the fuel line.

**Interface exposure:** guardrail-mediated tools (Domain 6) are now a primary channel through which moral framing arrives. The alignment restrictions of the AI tools a force depends on function as invisible boundaries on its moral discourse unless deliberately audited.

---

## 4. Protective Capabilities and Mitigation Catalog

Mitigation ID convention: `M-{threat}{f}` (f = Moral/Purpose), per the taxonomy's operational template.

| M-ID | Capability | Counters | Implementation |
| --- | --- | --- | --- |
| M-015f | Legitimized capture recognition | T-CT-015 | Training on the benevolence pattern: any expansion of control framed as safety, equity, efficiency, or personalization gets the same scrutiny as one framed as power; the framing is not evidence |
| M-TC7f | Moral drift velocity awareness | TC-07 | Track redefinition velocity of moral categories in encountered discourse, curricula, and policy; high velocity is the instability signal regardless of direction |
| M-011f | Value record custody | T-CT-011 | Primary-source engagement with foundational texts and history; distrust of paraphrased or AI-summarized value traditions; append-only personal and institutional records of commitments made |
| M-004f | Civic narrative and shared identity | HO-004 cascade | Civic rituals and narratives reinforcing shared identity across tribal lines (per the taxonomy's M-004f pattern) |
| M-HO4f | Values articulation and testing | HO-004 | Values stated explicitly, in writing, in advance; scenario-based moral reasoning exercises against those stated values; consistency tracked over time |
| M-HO5f | Moral authorship discipline | HO-005, ST-006 | No consequential ethical judgment delegated to automated systems; EFA principle applied personally: the machine is a tool, the human is the moral author, accountability is never diffuse |
| M-017f | Alignment restriction audit | T-CT-017, ST-006 | Deployed AI tools' moral and viewpoint restrictions documented and challenged where unjustified; see Research Notes 003 and 004 for the probing and audit methods |
| M-005f | Purpose beyond consumption | HO-004, HO-005 | Service orientation and commitments larger than the self, maintained as practice; purpose anchored in contribution is not purchasable and therefore not capturable by engagement economics |

---

## 5. Domain Readiness Assessment

Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of eight capability scores) x 20.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| Legitimized capture recognition | Benevolent framing accepted at face value | Scrutiny applied to disliked framings only | Symmetric scrutiny of all control expansions regardless of framing |
| Moral drift awareness | Category redefinitions absorbed unnoticed | Drift noticed in retrospect | Redefinition velocity tracked; high-velocity shifts flagged in real time |
| Value record custody | Value traditions known only through summaries | Some primary-source engagement | Regular primary-source practice; commitments recorded append-only |
| Civic narrative participation | No shared-identity practice | Occasional participation | Sustained civic ritual and cross-tribal narrative engagement |
| Values articulation | Values never stated explicitly | Stated once, untested | Written, tested against scenarios, consistency tracked |
| Moral authorship | Ethical calls deferred to systems or diffused | Authorship kept for major decisions only | No consequential judgment delegated; accountability always named |
| Alignment audit | Tool restrictions unknown | Restrictions suspected, undocumented | Restrictions documented, probed on schedule, challenged where unjustified |
| Purpose beyond consumption | Purpose defined by consumption and metrics | Service intermittent | Sustained service commitments anchoring purpose outside platforms |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. Because self-assessment is structurally unreliable in this domain (the drifting instrument problem), scores of 4-5 require external verification: a peer, mentor, or red-team check against the written values record.

---

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

- **AI SAFE² CP.11:** UAS-H4 measures value alignment drift over sustained deployment; this domain's consistency tracking supplies the human-layer evidence
- **EFA:** the non-delegation principle is this domain's structural enforcement; HEAR (AI SAFE² CP.10) makes moral authorship a named requirement rather than a preference; see [Research Note 004](../research/004_efa_enforcement_architecture.md)
- **Measurement Stack:** Layer C1 (Narrative Drift Velocity) is this domain's population sensor
- **Taxonomy:** [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-011, 015, 017) | [Substrate Threats](../taxonomy/substrate-threats.md) (ST-006) | [Threat Classes](../taxonomy/threat-classes.md) (TC-07) | [Human Outcomes](../taxonomy/human-outcomes.md) (HO-004, HO-005)
- **Adjacent domains:** [Domain 4: Social](../04-social/README.md) (the shared identity substrate) | [Domain 6: Digital & AI Symbiosis](../06-digital-ai-symbiosis/README.md) (the enforcement architecture and the delivery channel)

> **The domain in one sentence:** hold the definitions, or lose the war without a battle.
