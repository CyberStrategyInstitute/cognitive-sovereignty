# Domain 02: Cognitive

### The Capacity Under Direct Attack

**CSF Position:** Domain 2 of 6 | **AI SAFE² CP.11 Controls:** UAS-H1 (cognitive autonomy preservation), UAS-H8 (decision override health) | **Companion Research:** [001 Cognitive Offloading](../research/001_cognitive_offloading.md), [003 Guardrail and Model Drift](../research/003_guardrail_drift.md)

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
| T-CT-001 | Attention Capture and Habituation | Technique | CTSS 80 / Detection 4 | Attention sovereignty; ability to focus and reason |
| T-CT-006 | Decision Automation Capture | Technique | CTSS 82 / Detection 2 | Independent decision-making via biased defaults and autopilot behaviors |
| T-CT-007 | Information Ecosystem Poisoning | Technique | CTSS 76 / Detection 3 | Epistemic environment integrity via data poisoning of recommendation and knowledge systems |
| T-CT-014 | Cognitive Load Flooding | Technique | CTSS 77 / Detection 4 | Analytical capacity; contradictory streams until analysis collapses |
| TC-05 | Cognitive Overload Saturation | Threat Class | n/a | Decision quality at scale; defaults to tribal heuristics, authority shortcuts, apathy |

**The compounding pattern:** ST-003 and ST-007 interact. A user in offloading Phase 2 or 3 (dependency, atrophy) has surrendered the independent capability required to notice model drift. Degraded outputs get absorbed as the new baseline. This pairing is the quiet path to population-scale reasoning decline with no attack and no incident. Details in Research Notes [001](../research/001_cognitive_offloading.md) and [003](../research/003_guardrail_drift.md).

---

## 3. Cascade Position

**Receives from below:** biological capture (Domain 1) delivers a sleep-deprived, reward-hijacked brain to this domain. Attention hygiene cannot be trained onto captured reward circuitry.

**Receives from above:** a compromised AI environment (Domain 6) feeds poisoned information and drifted outputs directly into cognitive processing. Domain 2 is the first inland casualty of a Domain 6 breach.

**Feeds upward and outward:** impaired cognition reduces emotional regulation (Domain 3), degrades the judgment that maintains trust networks (Domain 4), and weakens the reasoning that moral judgment requires (Domain 5).

---

## 4. Protective Capabilities and Mitigation Catalog

Mitigation ID convention: `M-{threat}{c}` (c = Cognitive), per the taxonomy's operational template.

| M-ID | Capability | Counters | Implementation |
| --- | --- | --- | --- |
| M-001c | Attention hygiene | T-CT-001 | Single-task deep work blocks; platform access scheduled, not ambient; interruption budget tracked and enforced |
| M-014c | Load management discipline | T-CT-014, TC-05 | Bounded information intake windows; deliberate triage before analysis; recognition training for flooding conditions (contradictory streams, performative crisis tempo) |
| M-007c | Source verification habit | T-CT-007 | Provenance check before belief update; independent corroboration for any claim that would change a decision; distrust of unverifiable virality |
| M-S03c | Cognitive independence exercises | ST-003 | Quarterly unassisted baseline testing (reasoning, writing, recall against own trend line); rotation of tool-free task execution; offloading inventory maintained per role |
| M-006c | Independent-first decision habit | T-CT-006 | Formulate position before consulting AI tools on Material/High-stakes questions; log and investigate divergences; never accept defaults on consequential decisions unreviewed |
| M-S07c | Output quality baselining | ST-007 | Dated samples of AI outputs on standardized tasks; quarterly comparison converts invisible drift into measurable trend |
| M-004c | Inoculation training | T-CT-004 and technique layer broadly | Pre-exposure to weakened manipulation techniques builds mental antibodies; per CSF Table 5, inoculation reduces false narrative adoption by approximately 40 percent across cultures |
| M-002c | Deep reading practice | T-CT-001, ST-003 | Sustained long-form engagement as deliberate training, rebuilding the deep-attention capacity hyperattention displaces |

---

## 5. Domain Readiness Assessment

Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of eight capability scores) x 20.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| Attention hygiene | Ambient platform access; no deep work structure | Deep work attempted; interruptions unmanaged | Scheduled access; protected deep work blocks; interruption budget tracked |
| Load management | Continuous intake; no triage | Intake bounded sometimes | Bounded windows; triage before analysis; flooding conditions recognized |
| Source verification | Belief updates on unverified content | Verification for major claims only | Provenance check habitual before any decision-relevant belief update |
| Cognitive independence | No unassisted baseline ever measured | Baseline measured once; no trend | Quarterly unassisted testing; stable or improving trend line |
| Independent-first habit | Tool output accepted as conclusion | Independent position formed occasionally | Position formed before tool consult on all Material/High-stakes questions; divergences logged |
| Output baselining | No retained samples | Informal memory of past quality | Dated samples; quarterly structured comparison |
| Inoculation | No exposure training | One-time awareness briefing | Recurring inoculation against current technique families |
| Deep reading | Long-form abandoned | Occasional long-form | Regular sustained long-form engagement, tracked |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. A Compromised score here with high AI tool usage is the ST-003 Phase 3 profile: the person can no longer distinguish their reasoning from the tool's.

---

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

- **AI SAFE² CP.11:** UAS-H1 (cognitive autonomy preservation) and UAS-H8 (decision override health) are the procurement-facing measures of this domain; override frequency and independence metrics feed the CP.11 evidence package
- **EFA:** R/M/H decision classification (CP.10 HEAR for High-stakes) is the structural enforcement of the independent-first habit; see [Research Note 001](../research/001_cognitive_offloading.md)
- **Taxonomy:** [Substrate Threats](../taxonomy/substrate-threats.md) (ST-003, ST-007) | [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-001, 006, 007, 014) | [Threat Classes](../taxonomy/threat-classes.md) (TC-05) | [CTSS Scoring](../taxonomy/ctss-scoring.md)
- **Adjacent domains:** [Domain 1: Biological](../01-biological/README.md) (precondition) | [Domain 6: Digital & AI Symbiosis](../06-digital-ai-symbiosis/README.md) (the interface this domain's independence defends against)

> **The domain in one sentence:** the fight is for the capacity to think, not the content of thought.
