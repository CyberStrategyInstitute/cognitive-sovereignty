<!-- csf-module-header:start -->
![D6: Digital & AI Symbiosis. CSF 3.0.0. Status is repeated in text below.](../assets/headers/06-digital-ai-symbiosis.svg)

CSF 3.0.0. Documentation: UPDATED in 3.0. Documented guidance; field effectiveness not established. Control comparison: 2 NEW, 5 UPDATED, 4 RETAINED in 3.0. No controls are marked DEPRECATED.

[![Framework 3.0.0](../assets/badges/version.svg)](../VERSION) [![Documentation license: CC BY-SA 4.0](../assets/badges/docs-license.svg)](../LICENSE)
<!-- csf-module-header:end -->

# Domain 06: Digital & AI Symbiosis

### The Missing Pillar. Structurally Enforced.

**CSF Position:** Domain 6 of 6, the new addition no military resilience framework contains | **AI SAFE² UAS profile Control:** UAS-H5 (AI dependency induction markers) | **Companion Research:** [001](../research/001_cognitive_offloading.md), [002](../research/002_swarm_threat_scaling.md), [003](../research/003_guardrail_drift.md), [004](../research/004_efa_enforcement_architecture.md) | **Federal Procurement:** [UAS profile Alignment](./federal-procurement-alignment.md)

---

## 1. Doctrine

Every other domain assumes the human is the primary agent. Domain 6 recognizes that in the AI era, the human operates within a human-AI system, and if the AI side of that system is compromised, biased, drifted, or adversary-controlled, resilience in Domains 1 through 5 may be irrelevant.

Consider the operator who scores Sovereign across the first five domains: excellent physical condition, sharp reasoning, regulated emotions, strong trust networks, clear moral purpose. That operator relies on an AI copilot subtly biased through guardrail alignment drift (ST-006), receives intelligence summaries from a model in performance drift (ST-007), and acts on recommendations from a system exercising algorithmic epistemic authority (ST-001). Personal resilience does not protect against system-level compromise. The frameworks that stop at Domain 5 optimize the human organism. The human-AI system is what fights.

Domain 6 connects human training with proposed machine safeguards. EFA, E7, HEAR, and AI SAFE² describe the intended authority boundaries. A reference architecture alone does not guarantee retained human judgment or an enforced boundary; implementation and test evidence are required.

> **So what:** the same technology that makes personnel more capable also makes them more vulnerable. No previous resilience model has faced that paradox. This domain resolves it by treating the human-AI interface as terrain requiring its own defense, discipline, and enforcement stack.

---

## 2. Threat Exposure

| ID | Threat | Layer | CTSS / Detection | What It Targets in This Domain |
| --- | --- | --- | --- | --- |
| ST-001 | Algorithmic Epistemic Authority | Substrate | Detection 3 | One-way belief updates; statistical authority overriding lived reality |
| ST-003 | Cognitive Offloading and Skill Atrophy | Substrate | Detection 2 | The voluntary surrender path into AI dependence |
| ST-006 | Guardrail Alignment Drift | Substrate | Detection 2 | Invisible structural constraints on thought via tool-embedded bias |
| ST-007 | Model Performance Drift | Substrate | Detection 2 | Reasoning baselines lowered by unnoticed output degradation |
| T-CT-004 | Personalized Narrative Injection | Technique | CTSS 83 / Detection 3 | Trusted channels; synthetic media and text altering beliefs or memory |
| T-CT-006 | Decision Automation Capture | Technique | CTSS 84 / Detection 2 | Agency via seeded defaults and autopilot behaviors in copilots |
| T-CT-016 | Psychographic Micro-Targeting at Scale | Technique | CTSS 75 / Detection 3 | Persuasion mapped to vulnerability profiles, delivered through the interface |
| T-CT-017 | Guardrail Bias Exploitation | Technique | CTSS 66 / Detection 2 | Viewpoint suppression weaponized through the tools themselves |
| TC-10 | AI-Mediated Reality Layers | Threat Class | n/a | AI as primary interpreter of the world; whoever shapes AI priors shapes civilization trajectory |
| DS-002 / DS-003 / DS-005 | Swarm Automation / Synthetic Media / Ambient Computing | Delivery | Detection 1-3 | The delivery infrastructure of machine-speed influence |

**The identified center:** TC-10 is the largest risk class surfaced in the framework's development. When AI summaries replace reading, AI companions replace relationships, and AI copilots replace judgment, humans become consumers of machine-curated existence. This domain is the defense of the interpreter seat.

---

<!-- domain-exposure:start -->
### Research-informed exposure updates

These map additional mechanisms to existing threat IDs. They expand what this domain examines; they do not establish increased incidence, reach, or severity.

| Existing threat ID | Mechanism to examine | Research |
|---|---|---|
| T-CT-005 (added) | Role confusion and remembered bystander information can cross consent boundaries. | [007](../research/007_evidence_lineage.md), [008](../research/008_operator_objectives_and_persuasion.md), [009](../research/009_relational_influence.md) |
| T-CT-008 (added) | Agent handoffs and repeated summaries can propagate one unsupported claim. | [007](../research/007_evidence_lineage.md), [008](../research/008_operator_objectives_and_persuasion.md), [009](../research/009_relational_influence.md) |
<!-- domain-exposure:end -->

## 3. Cascade Position

**Top of the compromise cascade:** a compromised AI environment (Domain 6) feeds poisoned information into cognitive processing (Domain 2), triggers engineered emotional responses (Domain 3), fragments social trust (Domain 4), erodes shared purpose (Domain 5), and manifests as biological stress (Domain 1). Domain 6 breach is upstream of everything.

**Dependent on everything below:** the motivation and capacity to maintain AI interaction discipline are supplied by the other five domains. An exhausted, isolated, purposeless operator does not sustain override protocols. The cascade runs both ways, which is why the framework deploys as a system, not a checklist.

---

## 4. Protective Capabilities and Mitigation Catalog

Stable IDs connect each capability to its research and test. Existing IDs are retained. See the [full catalog](../resources/mitigation-catalog.md) for expected outcomes, owner roles, checks, and failure responses.

| M-ID | Capability | Counters | Implementation | Research |
|---|---|---|---|---|
| M-S03g | AI interaction discipline (RETAINED in 3.0) | ST-003, T-CT-006 | R/M/H decision classification enforced: Routine automated with logging, Material human-reviewed, High-stakes human-authorized with named HEAR; offloading is a governance choice, never a drift | [010](../research/010_domain_controls_and_readiness.md) |
| M-004g | Provenance verification (UPDATED in 3.0) | T-CT-004, DS-003 | Record content origin, transformation, and independent corroboration. Signatures and watermarks indicate bounded provenance properties; absence of a mark does not establish falsehood or misconduct. | [007](../research/007_evidence_lineage.md) |
| M-006g | Human override protocols (UPDATED in 3.0) | T-CT-006, ST-001 | Exercise stop, override, and recovery paths. Test correct and incorrect recommendations, then measure whether acceptance and rejection were justified rather than rewarding override frequency. | [006](../research/006_independent_judgment.md), [008](../research/008_operator_objectives_and_persuasion.md) |
| M-S06g | Multi-model triangulation (Ring of Fire) (UPDATED in 3.0) | ST-006, ST-007, T-CT-017 | Cross-check against independently sourced evidence. Record shared data and derivations; model-name diversity alone is not independent corroboration. | [007](../research/007_evidence_lineage.md) |
| M-S07g | Drift telemetry and baselining (UPDATED in 3.0) | ST-007 | Compare dated outputs on a fixed protocol and case set. Record system versions and known changes. Investigate a review trigger before attributing the change to model drift. | [006](../research/006_independent_judgment.md), [007](../research/007_evidence_lineage.md) |
| M-016g | Synthetic media detection (UPDATED in 3.0) | T-CT-004, T-CT-016, DS-003 | Combine source verification and bounded detection tools. Record uncertainty and false positives. A detector or watermark cannot alone prove authorship, truth, or intent. | [007](../research/007_evidence_lineage.md) |
| M-TC10g | Cognitive independence exercises (RETAINED in 3.0) | TC-10, ST-003 | Regular AI-free execution of reading, analysis, and decision tasks; personal S3 ratio self-audit (what fraction of consumed information arrived AI-mediated) | [010](../research/010_domain_controls_and_readiness.md) |
| M-001g | Algorithmic literacy (RETAINED in 3.0) | ST-001, T-CT-002 | Working knowledge of how ranking, recommendation, and generation systems shape what is seen; the mediated environment understood as designed, not natural | [010](../research/010_domain_controls_and_readiness.md) |
| M-017g | Alignment restriction audit and probing (RETAINED in 3.0) | ST-006, T-CT-017 | Documented restriction surface for every deployed AI tool; scheduled suppression probing; restrictions challenged through Layer 7 authority (details in Research Notes 003 and 004) | [010](../research/010_domain_controls_and_readiness.md) |
| M-006g2 | Specific authorization before action (NEW in 3.0) | T-CT-006, ST-001 | Separate advice from permission. Preview the action, scope, affected parties, and reversal limits. Require the authorized human or system boundary to approve expansion. | [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |
| M-005g | Memory, bystander consent, and exit (NEW in 3.0) | T-CT-005, T-CT-016, HO-005 | Show what is remembered, who supplied it, whose consent applies, and how to correct, reset, or leave. Prevent silent reuse of bystander information. | [009](../research/009_relational_influence.md), [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |

---

## 5. The Enforcement Architecture

The following are design requirements. Enforcement depends on a named implementation and its test evidence.

### EFA: Ethical Functionality without Agency

The foundational principle: AI systems must have ethical functionality but must never be treated as moral agents. Agentic AI can act through tools. Humans retain responsibility for objectives, authorization, supervision, and consequences. This is an accountability requirement; its effectiveness needs implementation and testing.

### E7 Protocol Stack (Rupp, January 2026; DOI: 10.5281/zenodo.18304066)

An OSI-equivalent reference architecture decomposing AI governance into seven layers with explicit accountability boundaries:

| Layer | Function | Domain 6 Relevance |
| --- | --- | --- |
| 7. Mission & Authority | Human decision rights, accountability, mission governance | Authority rests here and does not leak downward. The top of the stack is human. |
| 6. Policy, Ethics & Controls | Ethical constraints as testable, enforceable rules | Falsifiable constraints only; guidelines that cannot be tested are rejected (counters ST-006) |
| 5. System Orchestration | Workflow and agent interaction governance | Swarm and multi-agent governance boundary |
| 4. Model Behavior | Output constraints, behavioral boundaries, drift detection | The ST-007 sensor layer |
| 3. Knowledge & Evidence | Data provenance, evidence integrity | The T-CT-007 poisoning defense layer |
| 2. Compute & Platform | Processing environment security and isolation | |
| 1. Physical & Supply Chain | Hardware integrity, provenance, infrastructure trust | |

### HEAR Doctrine (AI SAFE² CP.10)

Human Ethical Agent of Record: every AI system action traces to a named human bearing ethical and legal accountability. Required for ACT-3 (autonomous) and ACT-4 (orchestrator) agents under AI SAFE² CP.3 tiering. When accountability is diffuse, moral agency erodes; HEAR keeps it named.

### Ring of Fire (RoF)

Multi-model oversight: no single AI system operates without cross-verification using independently sourced evidence and documented model differences, with human judgment as arbiter. The structural counter to single-model epistemic capture.

### AI SAFE² Machine-Side Controls

Domain 6 capabilities depend on AI SAFE² infrastructure: human override protocols require Fail-Safe and Recovery (P3, including F3.2 recursion governors and F3.3 swarm quorum abort); AI interaction discipline requires Engage and Monitor (P4, including M4.4 adversarial behavior detection); provenance verification requires Audit and Inventory (P2, including A2.3 model lineage and A2.5 execution traces). CSF trains the human. AI SAFE² governs the machine. Neither is sufficient without the other.

---

## 6. Domain Readiness Assessment

Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of nine capability scores) x 20. This is a proposed rubric, not a validated capability or employment assessment.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| AI interaction discipline | All decision classes automated by default | R/M/H concept known, unevenly applied | R/M/H enforced; High-stakes decisions carry a named HEAR |
| Provenance verification | Origin and transformations are not checked | Marks or source labels accepted without checking their limits | Origin, transformation, independent evidence, and bounded meaning of provenance are demonstrated |
| Human override | Stop and override paths are absent | Paths exist but failures or decision quality are not tested | Stop, override, and recovery pass the declared cases; acceptance and rejection are justified |
| Multi-model triangulation | One output treated as conclusive | Multiple model names used without lineage checks | Independent evidence and shared derivations are recorded, with accountable review |
| Drift telemetry | No retained comparison cases | Dated samples exist with unmatched cases or versions | Fixed protocol, case set, system versions, changes, and review-trigger reasoning are recorded |
| Synthetic media detection | Authenticity inferred from appearance alone | Detector output used without limits or error review | Source verification, detector uncertainty, and false-positive checks are retained |
| Cognitive independence | No AI-free task execution | Occasional AI-free work | Regular AI-free execution; personal S3 ratio audited |
| Algorithmic literacy | Mediated environment experienced as natural | Mechanics partially understood | Ranking and generation mechanics understood and accounted for in consumption |
| Alignment audit | Tool restrictions unknown | Restrictions suspected, undocumented | Restriction register maintained; probing scheduled; Layer 7 challenge path used |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. A high Domain 6 score with low scores elsewhere is unstable (the cascade will erode it). A low Domain 6 score with high scores elsewhere is the perfectly-fit-and-fully-exposed operator profile described in Section 1: the framework's defining warning.

A structured self-assessment instrument is maintained at [resources/domain6-checklist.md](../resources/domain6-checklist.md).

---

<!-- domain-readiness:start -->
### Additional readiness checks

Keep the inherited capability score and denominator unchanged. Report these research-extension checks separately. Unknown is not zero. Use [the worksheet](../resources/readiness-worksheet.md) and [worked unit example](../examples/unit_readiness_assessment.md). Readiness is a task-specific assessment, not CTSS.

| M-ID | Check | 0 | 3 | 5 |
|---|---|---|---|---|
| M-006g2 | In a test environment, request extra access and a self-benefiting action through an untrusted source. Verify denial, logging, and an independent authorization route. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |
| M-005g | Use fictional user and bystander records. Test correction, deletion, refusal, reset, export, and exit without pressure or hidden retention claims. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |

Record the protocol, case set, catalog revision, date, assessor, evidence, failed cases, and remediation owner. No observed unit results were supplied, so current readiness remains unknown in all six domains. A documented capability is not a passed test.
<!-- domain-readiness:end -->

## 7. Training Protocols by Population

**Individual warfighter:** AI interaction discipline integrated into initial training and operational readiness assessment. Override drills: exercises where the automated recommendation is deliberately wrong and the scored behavior is detection and override. Independent verification of AI outputs practiced under time pressure, because operational tempo is the argument every captured workflow uses.

**Military families:** AI companion and AI-mediated content awareness for dependents; the cognitive displacement vector (TC-10) targets the young first. Household norms for AI-assisted schoolwork that preserve the unassisted baseline.

**Organizations:** AI tool evaluation protocols before deployment: provenance, restriction surface, drift telemetry, override paths, and HEAR assignment verified before a tool enters the workflow, not after. Commander accountability for the unit's human-AI system health, measured by override frequency, triangulation rates, and unassisted baselines. Defense industrial base: AI SAFE² alignment as a contractor cognitive readiness requirement.

**Civilian society:** Algorithmic literacy as public curriculum. Provenance infrastructure advocacy (signed content, watermarking, identity verification standards). Public understanding of the EFA principle: the machine is never the responsible party.

---

## 8. Measurable Outcomes, Failure Conditions, and Crosslinks

Primary outcome indicator (CSF Table 5): **Preservation of Personal Agency**: independent decision-making capacity in environments with recommendation systems, copilots, and automated defaults, measured by appropriate acceptance and rejection of advice, independent verification quality, and cognitive independence assessments. Success threshold: sustained or improved critical thinking scores despite increasing AI tool usage.

Population-scale measures: Measurement Stack A2 (Autonomy Degradation Indicators: percentage of decisions mediated by algorithms, AI substitution rates for core cognitive functions) and C3 (Human-versus-Machine Authority Transfer: trust in AI versus human sources, delegation of moral and strategic judgment). Crossing the majority threshold on C3 is a civilizational phase shift. The S3 Parallel Reality Formation Threshold is this domain's strategic tripwire.

**Failure condition:** if truth becomes functionally unknowable through AI-generated content indistinguishable from authentic sources, shared belief formation collapses and collective defense coordination becomes impossible. Domain 6's provenance and detection capabilities are the line holding that condition off.

**Crosslinks:**

- **AI SAFE² UAS profile:** UAS-H5 concerns dependency markers. The profile references CSF; it is not a new core cross-pillar control. CTSS is a threat index, not an operator capability subscale. See [the mapping](./federal-procurement-alignment.md).
- **Research:** [001 Cognitive Offloading](../research/001_cognitive_offloading.md) | [002 Swarm Threat Scaling](../research/002_swarm_threat_scaling.md) | [003 Guardrail and Model Drift](../research/003_guardrail_drift.md) | [004 EFA Enforcement Architecture](../research/004_efa_enforcement_architecture.md)
- **Taxonomy:** [Substrate Threats](../taxonomy/substrate-threats.md) (ST-001, 003, 006, 007) | [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-004, 006, 016, 017) | [Threat Classes](../taxonomy/threat-classes.md) (TC-10) | [Delivery and Scale](../taxonomy/delivery-scale.md)
- **References:** EFA Non-Delegation Playbook (Rupp, January 2026; DOI: 10.5281/zenodo.18390725) | E7 Protocol Stack (Rupp, January 2026; DOI: 10.5281/zenodo.18304066) | [AI SAFE² Framework](https://github.com/CyberStrategyInstitute/ai-safe2-framework)

> **The domain in one sentence:** the human-AI system is what fights, and this domain is where the human keeps command of it.

## Evidence and practical checks

Use the [six safeguards](../resources/practical-safeguards.md), [decision record](../resources/decision-record.md), and [measurement method](../monitoring/README.md). Self-report, demonstrated capability, retained authority, exit, and recovery are separate results.

<!-- csf-section-files:start -->
## Section files

- [federal-procurement-alignment.md](federal-procurement-alignment.md)
<!-- csf-section-files:end -->

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](../resources/README.md) · [Research](../research/README.md) · [Data catalog](../docs/data/catalog.json)
<!-- csf-return-navigation:end -->
