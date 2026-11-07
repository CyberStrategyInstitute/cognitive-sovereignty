# Domain 02: Cognitive

### The Capacity Under Direct Attack

**CSF Position:** Domain 2 of 6 | **AI SAFE² UAS profile Controls:** UAS-H1 (cognitive autonomy preservation), UAS-H8 (decision override health) | **Companion Research:** [001 Cognitive Offloading](../research/001_cognitive_offloading.md), [003 Guardrail and Model Drift](../research/003_guardrail_drift.md)

---

## 1. Doctrine

Attention control, deep thinking, memory, learning agility, and reasoning capacity are the faculties cognitive warfare exists to degrade. The Cognitive Threat Assessment's central finding lands here: the goal of the modern threat is not to change what people think. It is to degrade, redirect, or capture the processes that allow independent thought to form at all.

Two distinct attack modes converge on this domain. The active mode floods, captures, and poisons: attention capture, cognitive load flooding, information ecosystem poisoning. The passive mode is more dangerous because it is voluntary: cognitive offloading trades reasoning capacity for convenience, one rational decision at a time, until the population has surrendered the capabilities independence requires. An adversary who controls information can be defeated by better information. An adversary who has degraded cognition cannot be defeated at all, because the target population can no longer evaluate competing claims.

> **So what:** this domain is where the taxonomy's true metric lives. Not misinformation detected. Not propaganda countered. The preservation or loss of self-directed cognition. If that metric degrades, the threat exists regardless of source or intent.

---

## 2. Threat Exposure

| ID | Threat | Layer | CTSS / Detection | What It Targets in This Domain |
| --- | --- | --- | --- | --- |
| ST-003 | Cognitive Offloading and Skill Atrophy | Substrate | Detection 2 | Reasoning, memory, and language capacity via voluntary convenience trades |
| ST-007 | Model Performance Drift | Substrate | Detection 2 | Reasoning baselines; degraded AI outputs absorbed as normal |
| T-CT-001 | Attention Capture and Habituation | Technique | CTSS 75 / Detection 4 | Attention sovereignty; ability to focus and reason |
| T-CT-006 | Decision Automation Capture | Technique | CTSS 84 / Detection 2 | Independent decision-making via biased defaults and autopilot behaviors |
| T-CT-007 | Information Ecosystem Poisoning | Technique | CTSS 73 / Detection 3 | Epistemic environment integrity via data poisoning of recommendation and knowledge systems |
| T-CT-014 | Cognitive Load Flooding | Technique | CTSS 71 / Detection 4 | Analytical capacity; contradictory streams until analysis collapses |
| TC-05 | Cognitive Overload Saturation | Threat Class | n/a | Decision quality at scale; defaults to tribal heuristics, authority shortcuts, apathy |

**The compounding pattern:** ST-003 and ST-007 interact. A user in offloading Phase 2 or 3 (dependency, atrophy) has surrendered the independent capability required to notice model drift. Degraded outputs get absorbed as the new baseline. This pairing is the quiet path to population-scale reasoning decline with no attack and no incident. Details in Research Notes [001](../research/001_cognitive_offloading.md) and [003](../research/003_guardrail_drift.md).

---

<!-- domain-exposure:start -->
### Research-informed exposure updates

These map additional mechanisms to existing threat IDs. They expand what this domain examines; they do not establish increased incidence, reach, or severity.

| Existing threat ID | Mechanism to examine | Research |
|---|---|---|
| T-CT-004 (added) | Hidden objectives can steer advice before a decision is formed. | [006](../research/006_independent_judgment.md), [007](../research/007_evidence_lineage.md), [008](../research/008_operator_objectives_and_persuasion.md) |
| T-CT-008 (added) | Repeated derivative evidence can look like independent corroboration. | [006](../research/006_independent_judgment.md), [007](../research/007_evidence_lineage.md), [008](../research/008_operator_objectives_and_persuasion.md) |
<!-- domain-exposure:end -->

## 3. Cascade Position

**Receives from below:** biological capture (Domain 1) delivers a sleep-deprived, reward-hijacked brain to this domain. Attention hygiene cannot be trained onto captured reward circuitry.

**Receives from above:** a compromised AI environment (Domain 6) feeds poisoned information and drifted outputs directly into cognitive processing. Domain 2 is the first inland casualty of a Domain 6 breach.

**Feeds upward and outward:** impaired cognition reduces emotional regulation (Domain 3), degrades the judgment that maintains trust networks (Domain 4), and weakens the reasoning that moral judgment requires (Domain 5).

---

## 4. Protective Capabilities and Mitigation Catalog

Stable IDs connect each capability to its research and test. Existing IDs are retained. See the [full catalog](../resources/mitigation-catalog.md) for expected outcomes, owner roles, checks, and failure responses.

| M-ID | Capability | Counters | Implementation | Research |
|---|---|---|---|---|
| M-001c | Attention hygiene (inherited) | T-CT-001 | Single-task deep work blocks; platform access scheduled, not ambient; interruption budget tracked and enforced | [010](../research/010_domain_controls_and_readiness.md) |
| M-014c | Load management discipline (inherited) | T-CT-014, TC-05 | Bounded information intake windows; deliberate triage before analysis; recognition training for flooding conditions (contradictory streams, performative crisis tempo) | [010](../research/010_domain_controls_and_readiness.md) |
| M-007c | Source verification habit (refined) | T-CT-007 | Trace claims to independent origins, including conflicting evidence. Three derivative summaries count as one lineage; provenance is evidence about origin, not truth. | [007](../research/007_evidence_lineage.md) |
| M-S03c | Cognitive independence exercises (refined) | ST-003 | Use comparable assisted and unaided tasks with a dated protocol, baseline, system version, and accessibility arrangements. Compare like tasks and retain helpful-delegation controls. | [006](../research/006_independent_judgment.md) |
| M-006c | Independent-first decision habit (refined) | T-CT-006 | Record initial criteria before consequential advice. Measure justified acceptance and rejection, comprehension, time, and later comparable performance. Keep helpful assistance and accessibility options. | [006](../research/006_independent_judgment.md) |
| M-S07c | Output quality baselining (refined) | ST-007 | Retain dated cases and compare the same task, protocol, environment, and system version. Separate a model change, changed evidence, and an assessment correction. | [006](../research/006_independent_judgment.md), [007](../research/007_evidence_lineage.md) |
| M-004c | Inoculation training (refined) | T-CT-004 | Practice recognizing current manipulation techniques with correct and incorrect advice. Measure actual decisions and retention; no universal percentage improvement is established by this catalog. | [006](../research/006_independent_judgment.md), [008](../research/008_operator_objectives_and_persuasion.md) |
| M-002c | Deep reading practice (inherited) | T-CT-001, ST-003 | Sustained long-form engagement as deliberate training, rebuilding the deep-attention capacity hyperattention displaces | [010](../research/010_domain_controls_and_readiness.md) |
| M-007c2 | Evidence completeness check (added) | T-CT-007, T-CT-008 | Group derivative reports by their original observation. Mark missing pages, truncated tool output, and contradictory evidence before deciding. | [007](../research/007_evidence_lineage.md), [010](../research/010_domain_controls_and_readiness.md) |
| M-008c | Trace influence to an outcome (added) | T-CT-004, T-CT-008 | Record production, distribution, exposure, decision change, persistence, and recovery separately. Preserve unknown stages. | [007](../research/007_evidence_lineage.md), [008](../research/008_operator_objectives_and_persuasion.md), [010](../research/010_domain_controls_and_readiness.md) |

---

## 5. Domain Readiness Assessment

This is a proposed, task-specific training rubric, not a validated personnel-readiness instrument. Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of eight capability scores) x 20.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| Attention hygiene | Ambient platform access; no deep work structure | Deep work attempted; interruptions unmanaged | Scheduled access; protected deep work blocks; interruption budget tracked |
| Load management | Continuous intake; no triage | Intake bounded sometimes | Bounded windows; triage before analysis; flooding conditions recognized |
| Source verification | Decision-relevant claims accepted without origin checks | Origins checked but shared lineage or contrary material is missed | Independent origins, conflicts, and material omissions are identified in the declared cases |
| Cognitive independence | No comparable capability check | One check without stable conditions or a retained baseline | Comparable accessible assisted/unaided tasks and delayed transfer are recorded with limits |
| Independent-first habit | Advice accepted without criteria or reasons | Criteria or review recorded inconsistently | Initial criteria, justified agreement/rejection, comprehension, and reasons are demonstrated |
| Output baselining | No retained cases | Samples exist but conditions or versions differ without explanation | Dated outputs, task conditions, system versions, and change reasons are recorded |
| Inoculation | No relevant practice | Awareness briefing without a recorded performance check | Current technique practice includes correct and incorrect advice with retained task results |
| Deep reading | Long-form abandoned | Occasional long-form | Regular sustained long-form engagement, tracked |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. A low score identifies checks to investigate. It does not by itself establish skill atrophy or inability to reason independently.

---

<!-- domain-readiness:start -->
### Additional readiness checks

Keep the inherited capability score and denominator unchanged. Report these research-extension checks separately. Unknown is not zero. Use [the worksheet](../resources/readiness-worksheet.md) and [worked unit example](../examples/unit_readiness_assessment.md). Readiness is a task-specific assessment, not CTSS.

| M-ID | Check | 0 | 3 | 5 |
|---|---|---|---|---|
| M-007c2 | Provide three summaries of one study, a conflicting independent study, and one missing page. Require two lineages and an explicit omission. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |
| M-008c | Review a case with message-generation evidence only. Check that exposure and behavior remain unknown and that the CTSS assumptions are explicit. | The control is absent or the declared check failed completely. | The path works in some declared cases; important gaps or evidence remain. | The path passes the declared case set, including an adverse case, with retained evidence. |

Record the protocol, case set, catalog revision, date, assessor, evidence, failed cases, and remediation owner. No observed unit results were supplied, so current readiness remains unknown in all six domains. A documented capability is not a passed test.
<!-- domain-readiness:end -->

## 6. Training Protocols by Population

**Individual warfighter:** Inoculation training against all 18 technique families, refreshed as the T-CT layer grows. Unassisted baseline testing integrated into periodic readiness assessment with the same standing as the fitness test. Independent-first habit drilled in intelligence and operational planning workflows.

**Military families:** Age-appropriate inoculation for dependents (pre-bunking manipulative content mechanics). Family source-verification norms: the household treats unverified viral claims as unverified. Deep reading cultivated as a household practice.

**Organizations:** Offloading inventories maintained per billet: which cognitive functions are offloaded, to which tools, at which decision class. Unit-level flooding drills: operate through contradictory-stream conditions and score decision quality. AI outputs on standardized tasks baselined organizationally, not left to vendors.

**Civilian society:** Public curriculum on offloading mechanics and the three-phase cycle. Algorithmic literacy as a civic baseline: citizens who understand how feeds rank cannot be steered as cheaply.

---

## 7. Measurable Outcomes and Failure Conditions

Primary outcome indicators (CSF Table 5):

- **Sustained Attention Span:** 20-30 percent improvement in controlled studies using attention hygiene interventions
- **Resistance to False Narratives:** approximately 40 percent reduction in false narrative adoption via inoculation training
- **Preservation of Personal Agency:** sustained or improved critical thinking scores despite increasing AI tool usage

Domain-specific measures: unassisted baseline trend, assisted-versus-unassisted performance divergence, verification rate before belief update, and divergence-investigation rate on the independent-first habit.

**Failure condition (from the CSF):** if unchecked cognitive offloading erodes reasoning capacity by 50 percent or more, the population cannot evaluate information independently and all downstream defenses become ineffective regardless of design. This domain carries the framework's hardest failure mode.

---

## 8. Enforcement and Crosslinks

- **AI SAFE² UAS profile:** UAS-H1 (cognitive autonomy preservation) and UAS-H8 (decision override health) are the procurement-facing measures of this domain; override frequency and independence metrics feed the UAS profile evidence package
- **EFA:** R/M/H decision classification (CP.10 HEAR for High-stakes) is the structural enforcement of the independent-first habit; see [Research Note 001](../research/001_cognitive_offloading.md)
- **Taxonomy:** [Substrate Threats](../taxonomy/substrate-threats.md) (ST-003, ST-007) | [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-001, 006, 007, 014) | [Threat Classes](../taxonomy/threat-classes.md) (TC-05) | [CTSS Scoring](../taxonomy/ctss-scoring.md)
- **Adjacent domains:** [Domain 1: Biological](../01-biological/README.md) (precondition) | [Domain 6: Digital & AI Symbiosis](../06-digital-ai-symbiosis/README.md) (the interface this domain's independence defends against)

> **The domain in one sentence:** the fight is for the capacity to think, not the content of thought.
