# Domain 6: Digital & AI Symbiosis

> **The Missing Pillar.** Every military branch in the Department of Defense operates a resilience framework. None of them contain this domain. Domain 6 is why all the others are now insufficient.

---

## Definition

**Digital & AI Symbiosis** is the capacity to work with AI systems without experiencing cognitive erosion, to filter signal from noise at machine-generated scale, to maintain human agency in automated environments, and to recognize and resist manipulation by synthetic media.

Domain 6 addresses the **interface** — the point where the human meets the AI system — and the specific vulnerabilities that emerge at that interface.

---

## Why This Domain Changes Everything

Every other domain assumes the human is the primary agent. Domain 6 recognizes that in the AI era, the human operates within a **human-AI system**. The system includes the AI tools used to process information, make decisions, communicate, and execute tasks.

Consider the operator who maintains:
- ✅ Excellent physical fitness (Domain 1)
- ✅ Strong emotional regulation (Domain 3)
- ✅ Deep social connections (Domain 4)
- ✅ Clear moral purpose (Domain 5)

If that operator relies on an AI copilot that has been subtly biased through guardrail alignment drift (ST-006), receives intelligence summaries from a model experiencing performance drift (ST-007), and makes decisions based on recommendations subject to algorithmic epistemic authority (ST-001) — **the operator's personal resilience does not protect against the system-level vulnerability.**

Domain 6 addresses the interface. The human's resilience in Domains 1–5 is necessary. It is not sufficient.

---

## Primary Threats (from Threat Assessment)

| Threat ID | Name | Mechanism |
|---|---|---|
| T-CT-006 | Decision Automation Capture | Seeding biased defaults through AI copilots and recommendation engines |
| T-CT-017 | Guardrail Bias Exploitation | Using AI alignment restrictions to suppress viewpoints and enforce conformity |
| ST-003 | Cognitive Offloading and Skill Atrophy | GPS replaces navigation, autocomplete replaces reasoning, AI replaces judgment |
| ST-006 | Guardrail Alignment Drift | AI ideological alignment restrictions become invisible structural constraints |
| ST-007 | Model Performance Drift | Gradual AI degradation absorbed as normal; reasoning baseline lowers |
| ST-001 | Algorithmic Epistemic Authority | Algorithms decide with low evidence; humans need high evidence to challenge |
| T-CT-016 | Psychographic Micro-Targeting at Scale | AI-powered profiling targeting psychological vulnerability patterns |

---

## Key Protective Capabilities

Domain 6 resilience is built through the following capabilities:

### 1. AI Interaction Discipline
The deliberate regulation of how, when, and how much to rely on AI tools. Discipline is not rejection of AI — it is structured use that preserves the cognitive independence required to verify, override, and maintain accountability.

**Training:** Structured AI-off exercises where personnel complete tasks independently, then compare results to AI-assisted outputs. Tracks cognitive atrophy over time.

### 2. Provenance Verification
The habit and technical capability to verify the origin, integrity, and chain of custody of information — especially information delivered through AI-mediated channels.

**Indicators:** Cryptographic content provenance, cross-source triangulation, metadata integrity checks.

### 3. Human Override Protocols
Explicit, trained procedures for identifying when AI outputs should be overridden by human judgment — and the organizational authority and psychological safety to execute overrides without penalty.

**Implementation:** R/M/H classification (Routine/Material/High-Stakes) from the EFA Non-Delegation Playbook maps directly to when to trust, verify, or override AI outputs.

### 4. Cognitive Independence Exercises
Deliberate practice of unassisted reasoning, navigation, writing, analysis, and decision-making. Prevents and reverses the cognitive offloading atrophy documented in ST-003.

**Success metric:** Personnel who use AI extensively maintain or improve independent cognitive performance on benchmark assessments.

### 5. Synthetic Media Detection
Training and tools for recognizing AI-generated video, audio, images, and text — including the meta-skill of recognizing when provenance cannot be established rather than assuming authenticity.

**Key principle:** The absence of detectable manipulation does not equal authenticity. Provenance must be established positively, not assumed.

### 6. Algorithmic Literacy
Understanding of how recommendation systems, social platforms, and AI tools shape information exposure, decision defaults, and behavioral nudges. Includes understanding of how those systems can be adversary-influenced or structurally biased.

---

## Technical Enforcement Architecture

Domain 6 is the only CSF domain backed by both human training and technical enforcement architecture. This architecture ensures that the human authority protected by Domain 6 training is not merely a behavioral preference but a structural guarantee.

### EFA (Ethical Functionality without Agency)
The foundational principle: **AI is a tool, not an agent.** This distinction prevents the gradual cognitive delegation that produces agency erosion (HO-005). If the machine is always a tool, the human must always be the agent.

### E7 Protocol Stack
The EFA/AI-SAFE² 7-Layer Protocol Stack places **Mission and Authority at Layer 7** — the top of the stack. Authority does not leak downward into automated systems. Every layer below serves the human authority at the top.

### HEAR Doctrine
**Human Ethical Agent of Record.** Every AI system action must trace to a named human who bears ethical and legal accountability. There is no such thing as an AI decision — there are only human decisions executed through AI tools.

### Ring of Fire (RoF)
Multi-model oversight architecture ensuring no single AI system operates without cross-verification. Addresses guardrail alignment drift (ST-006) and model performance drift (ST-007).

---

## CSF–AI SAFE² Domain 6 Mapping

Domain 6 capabilities directly map to AI SAFE² pillars:

| Domain 6 Capability | AI SAFE² Pillar |
|---|---|
| Human override protocols | P3: Fail-Safe & Recovery — kill switches and safe-mode reversion |
| AI interaction discipline | P4: Engage & Monitor — real-time anomaly detection |
| Provenance verification | P2: Audit & Inventory — immutable logging and asset registry |
| Synthetic media detection | P1: Sanitize & Isolate — input validation and injection defense |
| Algorithmic literacy | P5: Evolve & Educate — continuous red-teaming and operator training |

---

## Federal Procurement Alignment (CP.11)

Domain 6 is now the anchor of a formal cross-framework integration. Four Domain 6 control concepts are published as part of **AI SAFE² CP.11, the Unbiased AI Standard**, the procurement-facing compliance surface for draft GSAR clause 552.239-7001 (j)(1):

| Domain 6 Concept | CP.11 Control | Function |
|---|---|---|
| AI dependency induction monitoring | UAS-H5 | Detects functional dependency impairing mission decision-making |
| Cross-session cognitive drift tracking | UAS-X3 (bridge) | Maps AI interaction volume against sovereignty risk thresholds |
| Override rate preservation | UAS-H8 | Keeps human override health measurable, integrates AI SAFE² CP.9 |
| AI-human boundary clarity | UAS-H7 | Resists persona blurring and role-boundary erosion |

Federal deployments amplify every Domain 6 risk: high-consequence decisions, an authority gradient that accelerates deference to "government approved" outputs, multi-year contracts creating the long-horizon interaction patterns where dependency emerges, and reduced external calibration in classified environments.

The full analysis, including CTSS integration into the CP.11 evidence package and suggested performance work statement language for contracting officers, is in the Domain 6 supplement:

📄 **[Federal Procurement Alignment supplement →](./federal-procurement-alignment.md)**

---

## Failure Modes

Domain 6 fails under three specific conditions:

**1. Autonomy surrender without awareness.** When cognitive offloading (ST-003) accumulates gradually through convenience-driven AI adoption, the defense mechanism never triggers because the degradation never feels like a threat.

**2. Institutional normalization of AI authority.** When organizations reward fast AI-assisted decisions over verified independent judgment, override protocols become culturally inert even when technically available.

**3. Detection threshold collapse.** When synthetic media quality exceeds the current detection capability, and personnel have not developed the meta-skill of provenance-positive verification, the entire synthetic media detection capability fails simultaneously.

---

## Assessment Metrics

| Metric | Baseline | Target |
|---|---|---|
| AI override frequency | Establish baseline | Track for trend (neither too high nor too low) |
| Independent verification rate | Establish baseline | Sustained or improving |
| Cognitive independence scores (AI-off benchmark) | Establish baseline | Stable or improving despite increasing AI tool usage |
| Synthetic media detection accuracy | Establish baseline | 20%+ improvement after inoculation training |
| Provenance verification habit adoption | 0% | > 80% of personnel in targeted cohorts |

---

## Key References

- Cognitive Threat Assessment — Substrate Threats ST-001, ST-003, ST-006, ST-007
- Cognitive Threat Assessment — Techniques T-CT-006, T-CT-016, T-CT-017
- EFA Non-Delegation Playbook (Rupp, January 2026; DOI: 10.5281/zenodo.18390725)
- E7 Protocol Stack (Rupp, January 2026; DOI: 10.5281/zenodo.18304066)
- AI SAFE² Framework — [github.com/CyberStrategyInstitute/ai-safe2-framework](https://github.com/CyberStrategyInstitute/ai-safe2-framework)
- DoD AI Ethical Principles (February 24, 2020)
- DoD Directive 3000.09 (updated January 25, 2023)
- CP.11 Unbiased AI Standard — [ai-safe2-framework/00-cross-pillar/unbiased-ai](https://github.com/CyberStrategyInstitute/ai-safe2-framework/tree/main/00-cross-pillar/unbiased-ai)
- Domain 6 Federal Procurement Alignment supplement — [federal-procurement-alignment.md](./06-digital-ai-symbiosis/federal-procurement-alignment.md)