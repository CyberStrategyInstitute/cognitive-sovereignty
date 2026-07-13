# Domain 06: Digital & AI Symbiosis

### The Missing Pillar. Structurally Enforced.

**CSF Position:** Domain 6 of 6, the new addition no military resilience framework contains | **AI SAFE² CP.11 Control:** UAS-H5 (AI dependency induction markers) | **Companion Research:** [001](../research/001_cognitive_offloading.md), [002](../research/002_swarm_threat_scaling.md), [003](../research/003_guardrail_drift.md), [004](../research/004_efa_enforcement_architecture.md) | **Federal Procurement:** [CP.11 Alignment](./federal-procurement-alignment.md)

---

## 1. Doctrine

Every other domain assumes the human is the primary agent. Domain 6 recognizes that in the AI era, the human operates within a human-AI system, and if the AI side of that system is compromised, biased, drifted, or adversary-controlled, resilience in Domains 1 through 5 may be irrelevant.

Consider the operator who scores Sovereign across the first five domains: excellent physical condition, sharp reasoning, regulated emotions, strong trust networks, clear moral purpose. That operator relies on an AI copilot subtly biased through guardrail alignment drift (ST-006), receives intelligence summaries from a model in performance drift (ST-007), and acts on recommendations from a system exercising algorithmic epistemic authority (ST-001). Personal resilience does not protect against system-level compromise. The frameworks that stop at Domain 5 optimize the human organism. The human-AI system is what fights.

Domain 6 has a second distinction: it is the only resilience domain backed by both human training and technical enforcement architecture. The Ethical Functionality without Agency (EFA) paradigm, the E7 Protocol Stack, the HEAR Doctrine, and the AI SAFE² control set convert "the human stays in charge" from a behavioral preference into an architectural guarantee. Training builds the capability. Architecture makes it non-optional.

> **So what:** the same technology that makes personnel more capable also makes them more vulnerable. No previous resilience model has faced that paradox. This domain resolves it by treating the human-AI interface as terrain requiring its own defense, discipline, and enforcement stack.

---

## 2. Threat Exposure

| ID | Threat | Layer | CTSS / Detection | What It Targets in This Domain |
| --- | --- | --- | --- | --- |
| ST-001 | Algorithmic Epistemic Authority | Substrate | Detection 3 | One-way belief updates; statistical authority overriding lived reality |
| ST-003 | Cognitive Offloading and Skill Atrophy | Substrate | Detection 2 | The voluntary surrender path into AI dependence |
| ST-006 | Guardrail Alignment Drift | Substrate | Detection 2 | Invisible structural constraints on thought via tool-embedded bias |
| ST-007 | Model Performance Drift | Substrate | Detection 2 | Reasoning baselines lowered by unnoticed output degradation |
| T-CT-004 | Personalized Narrative Injection | Technique | CTSS 85 / Detection 3 | Trusted channels; synthetic media and text altering beliefs or memory |
| T-CT-006 | Decision Automation Capture | Technique | CTSS 82 / Detection 2 | Agency via seeded defaults and autopilot behaviors in copilots |
| T-CT-016 | Psychographic Micro-Targeting at Scale | Technique | CTSS 79 / Detection 3 | Persuasion mapped to vulnerability profiles, delivered through the interface |
| T-CT-017 | Guardrail Bias Exploitation | Technique | CTSS 70 / Detection 2 | Viewpoint suppression weaponized through the tools themselves |
| TC-10 | AI-Mediated Reality Layers | Threat Class | n/a | AI as primary interpreter of the world; whoever shapes AI priors shapes civilization trajectory |
| DS-002 / DS-003 / DS-005 | Swarm Automation / Synthetic Media / Ambient Computing | Delivery | Detection 1-3 | The delivery infrastructure of machine-speed influence |

**The identified center:** TC-10 is the largest risk class surfaced in the framework's development. When AI summaries replace reading, AI companions replace relationships, and AI copilots replace judgment, humans become consumers of machine-curated existence. This domain is the defense of the interpreter seat.

---

## 3. Cascade Position

**Top of the compromise cascade:** a compromised AI environment (Domain 6) feeds poisoned information into cognitive processing (Domain 2), triggers engineered emotional responses (Domain 3), fragments social trust (Domain 4), erodes shared purpose (Domain 5), and manifests as biological stress (Domain 1). Domain 6 breach is upstream of everything.

**Dependent on everything below:** the motivation and capacity to maintain AI interaction discipline are supplied by the other five domains. An exhausted, isolated, purposeless operator does not sustain override protocols. The cascade runs both ways, which is why the framework deploys as a system, not a checklist.

---

## 4. Protective Capabilities and Mitigation Catalog

Mitigation ID convention: `M-{threat}{g}` (g = Digital/AI Symbiosis), per the taxonomy's operational template.

| M-ID | Capability | Counters | Implementation |
| --- | --- | --- | --- |
| M-S03g | AI interaction discipline | ST-003, T-CT-006 | R/M/H decision classification enforced: Routine automated with logging, Material human-reviewed, High-stakes human-authorized with named HEAR; offloading is a governance choice, never a drift |
| M-004g | Provenance verification | T-CT-004, DS-003 | Mandatory provenance headers, signed content, verifiable identity tokens, AI watermarking where available; unverifiable content weighted near zero for Material and High-stakes decisions |
| M-006g | Human override protocols | T-CT-006, ST-001 | Explicit, exercised override paths for every automated recommendation stream; override frequency tracked as a health metric (a zero-override environment is a captured one) |
| M-S06g | Multi-model triangulation (Ring of Fire) | ST-006, ST-007, T-CT-017 | No single model's output treated as definitive for consequential assessments; cross-verification across demonstrably different alignments, arbitrated by human judgment |
| M-S07g | Drift telemetry and baselining | ST-007 | Organizational output baselining on standardized tasks (AI SAFE² F3.4 behavioral drift baseline and rollback); drift converted from invisible trend into threshold-crossing event |
| M-016g | Synthetic media detection | T-CT-004, T-CT-016, DS-003 | Detection tooling plus trained skepticism; cross-source provenance checks and triangulation of independent signals per the taxonomy's T-CT-004 detection methods |
| M-TC10g | Cognitive independence exercises | TC-10, ST-003 | Regular AI-free execution of reading, analysis, and decision tasks; personal S3 ratio self-audit (what fraction of consumed information arrived AI-mediated) |
| M-001g | Algorithmic literacy | ST-001, T-CT-002 | Working knowledge of how ranking, recommendation, and generation systems shape what is seen; the mediated environment understood as designed, not natural |
| M-017g | Alignment restriction audit and probing | ST-006, T-CT-017 | Documented restriction surface for every deployed AI tool; scheduled suppression probing; restrictions challenged through Layer 7 authority (details in Research Notes 003 and 004) |

---

## 5. The Enforcement Architecture

This section is what makes Domain 6 different in kind. The capabilities above are trained. The following are enforced.

### EFA: Ethical Functionality without Agency

The foundational principle: AI systems must have ethical functionality but must never be treated as moral agents. AI is a tool, not an agent. There is no such thing as an AI decision; there are only human decisions executed through AI tools. This prevents the gradual moral delegation that produces agency erosion (HO-005) by making the delegation architecturally impossible rather than merely discouraged.

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

Multi-model oversight: no single AI system operates without cross-verification from independently aligned systems, with human judgment as arbiter. The structural counter to single-model epistemic capture.

### AI SAFE² Machine-Side Controls

Domain 6 capabilities depend on AI SAFE² infrastructure: human override protocols require Fail-Safe and Recovery (P3, including F3.2 recursion governors and F3.3 swarm quorum abort); AI interaction discipline requires Engage and Monitor (P4, including M4.4 adversarial behavior detection); provenance verification requires Audit and Inventory (P2, including A2.3 model lineage and A2.5 execution traces). CSF trains the human. AI SAFE² governs the machine. Neither is sufficient without the other.

---

## 6. Domain Readiness Assessment

Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of nine capability scores) x 20.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| AI interaction discipline | All decision classes automated by default | R/M/H concept known, unevenly applied | R/M/H enforced; High-stakes decisions carry a named HEAR |
| Provenance verification | Content consumed without provenance checks | Checks for obviously suspect content | Habitual verification; unverifiable content discounted for consequential decisions |
| Human override | Override paths absent or never exercised | Paths exist, rarely used | Paths exercised routinely; override frequency tracked as health metric |
| Multi-model triangulation | Single-model dependence | Second opinion sought occasionally | Cross-alignment verification standard for consequential assessments |
| Drift telemetry | No output baselining | Informal quality memory | Dated baselines; quarterly structured comparison; drift thresholds defined |
| Synthetic media detection | No detection capability or habit | Tooling present, skepticism inconsistent | Tooling plus trained skepticism; cross-source triangulation habitual |
| Cognitive independence | No AI-free task execution | Occasional AI-free work | Regular AI-free execution; personal S3 ratio audited |
| Algorithmic literacy | Mediated environment experienced as natural | Mechanics partially understood | Ranking and generation mechanics understood and accounted for in consumption |
| Alignment audit | Tool restrictions unknown | Restrictions suspected, undocumented | Restriction register maintained; probing scheduled; Layer 7 challenge path used |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. A high Domain 6 score with low scores elsewhere is unstable (the cascade will erode it). A low Domain 6 score with high scores elsewhere is the perfectly-fit-and-fully-exposed operator profile described in Section 1: the framework's defining warning.

A structured self-assessment instrument is maintained at [resources/domain6-checklist.md](../resources/domain6-checklist.md).

---

## 7. Training Protocols by Population

**Individual warfighter:** AI interaction discipline integrated into initial training and operational readiness assessment. Override drills: exercises where the automated recommendation is deliberately wrong and the scored behavior is detection and override. Independent verification of AI outputs practiced under time pressure, because operational tempo is the argument every captured workflow uses.

**Military families:** AI companion and AI-mediated content awareness for dependents; the cognitive displacement vector (TC-10) targets the young first. Household norms for AI-assisted schoolwork that preserve the unassisted baseline.

**Organizations:** AI tool evaluation protocols before deployment: provenance, restriction surface, drift telemetry, override paths, and HEAR assignment verified before a tool enters the workflow, not after. Commander accountability for the unit's human-AI system health, measured by override frequency, triangulation rates, and unassisted baselines. Defense industrial base: AI SAFE² alignment as a contractor cognitive readiness requirement.

**Civilian society:** Algorithmic literacy as public curriculum. Provenance infrastructure advocacy (signed content, watermarking, identity verification standards). Public understanding of the EFA principle: the machine is never the responsible party.

---

## 8. Measurable Outcomes, Failure Conditions, and Crosslinks

Primary outcome indicator (CSF Table 5): **Preservation of Personal Agency**: independent decision-making capacity in environments with recommendation systems, copilots, and automated defaults, measured by human override frequency, independent verification rates, and cognitive independence assessments. Success threshold: sustained or improved critical thinking scores despite increasing AI tool usage.

Population-scale measures: Measurement Stack A2 (Autonomy Degradation Indicators: percentage of decisions mediated by algorithms, AI substitution rates for core cognitive functions) and C3 (Human-versus-Machine Authority Transfer: trust in AI versus human sources, delegation of moral and strategic judgment). Crossing the majority threshold on C3 is a civilizational phase shift. The S3 Parallel Reality Formation Threshold is this domain's strategic tripwire.

**Failure condition:** if truth becomes functionally unknowable through AI-generated content indistinguishable from authentic sources, shared belief formation collapses and collective defense coordination becomes impossible. Domain 6's provenance and detection capabilities are the line holding that condition off.

**Crosslinks:**

- **AI SAFE² CP.11:** UAS-H5 (AI dependency induction markers) is this domain's procurement-facing control; CTSS results flow into the CP.11 evidence package (UAS-SCORE-001, UAS-HUMAN-001); full federal alignment in [federal-procurement-alignment.md](./federal-procurement-alignment.md) and [Research Note 005](../research/005_uas_federal_standard.md)
- **Research:** [001 Cognitive Offloading](../research/001_cognitive_offloading.md) | [002 Swarm Threat Scaling](../research/002_swarm_threat_scaling.md) | [003 Guardrail and Model Drift](../research/003_guardrail_drift.md) | [004 EFA Enforcement Architecture](../research/004_efa_enforcement_architecture.md)
- **Taxonomy:** [Substrate Threats](../taxonomy/substrate-threats.md) (ST-001, 003, 006, 007) | [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-004, 006, 016, 017) | [Threat Classes](../taxonomy/threat-classes.md) (TC-10) | [Delivery and Scale](../taxonomy/delivery-scale.md)
- **References:** EFA Non-Delegation Playbook (Rupp, January 2026; DOI: 10.5281/zenodo.18390725) | E7 Protocol Stack (Rupp, January 2026; DOI: 10.5281/zenodo.18304066) | [AI SAFE² Framework](https://github.com/CyberStrategyInstitute/ai-safe2-framework)

> **The domain in one sentence:** the human-AI system is what fights, and this domain is where the human keeps command of it.
