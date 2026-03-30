# Cognitive Sovereignty Framework (CSF)

### A Six-Domain Model for Human Resilience in the AI Era

[![Version](https://img.shields.io/badge/version-2.0.0-crimson.svg)](https://github.com/CyberStrategyInstitute/cognitive-sovereignty-framework/releases)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![DoD Aligned](https://img.shields.io/badge/Aligned-DoD_AI_Ethical_Principles-005696?style=flat-square)](https://www.ai.mil/docs/RAI_Toolkit_Intro_Oct_21.pdf)
[![Companion](https://img.shields.io/badge/Companion-AI_SAFE²_Framework-orange)](https://github.com/CyberStrategyInstitute/ai-safe2-framework)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/CyberStrategyInstitute/cognitive-sovereignty-framework/graphs/commit-activity)

[**The Threat**](#-what-we-are-defending-against) | [**The Six Domains**](#-the-six-domain-model) | [**The Taxonomy**](#-threat-taxonomy) | [**CTSS Scoring**](#-cognitive-threat-severity-scoring) | [**Command Center**](#-command-center) | [**Roadmap**](#-implementation-roadmap) | [**Contributing**](#-contributing)

## Interactive Documentation

→ [CSF Learning Hub](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/)  
→ [Threat Explorer](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/csf-explorer.html)  
→ [Command Center](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/csf-command-center.html)

---

## 🧠 What Is the Cognitive Sovereignty Framework?

The **Cognitive Sovereignty Framework (CSF)** is an open-source, doctrine-grade resilience model designed to protect human cognition against the full spectrum of AI-era threats.

> **The primary battlefield of the 21st century is human cognition, not territory. The nation that loses cognitive sovereignty loses the ability to govern itself, fight wars, or sustain its civilization. This is not a metaphor. It is an operational reality.**

The CSF was developed by the **Cyber Strategy Institute** as the direct response to its companion *Cognitive Threat Assessment* — a first-principles analysis of what is actually happening to human cognition, and why current frameworks are structurally insufficient to address it.

### 🏆 The Gap No One Is Closing

Every U.S. military branch operates a resilience program. All of them share a four-domain core: mental, physical, social, and spiritual fitness.

**None of them contain a domain for digital, cognitive, or informational resilience.**

A warfighter can score perfectly on every existing resilience metric and still be fully vulnerable to AI-driven deception, algorithmic manipulation, cognitive offloading atrophy, and identity destabilization. The CSF closes that gap — for military personnel, their families, organizations, and civilian society.

---

## 🛡️ What We Are Defending Against

The threat to human cognition operates in five causal layers. Most current defenses target only one.

| Layer | Designation | Function |
|---|---|---|
| **Layer -2** | Civilizational Drivers (CD) | Root forces generating vulnerability conditions |
| **Layer -1** | Substrate Threats (ST) | Pre-manipulation foundations that make manipulation succeed |
| **Layer 0** | Manipulation Techniques (T-CT) | 18 active cognitive technique families |
| **Layer +1** | Delivery & Scale (DS) | Amplification mechanisms reaching populations |
| **Layer +2** | Human Outcomes (HO) | Observable effects when threats succeed |

> **Critical Insight:** If the substrate conditions (Layer -1) are not addressed, new techniques will always find new pathways. Tactical defense without substrate resilience is an infinite regression.

The complete threat taxonomy — 41 classified entries across all five layers, plus 10 newly identified threat classes and 3 edge domain additions — is maintained in [`/taxonomy`](./taxonomy/).

---

## 🔬 The Six-Domain Model

The CSF proposes six interdependent domains of human resilience. Domains 1–4 align with the universal military core. Domain 5 refines the purpose dimension. **Domain 6 is entirely new and the missing pillar across all branches.**

| # | Domain | Core Definition | Primary Threats | New? |
|---|---|---|---|---|
| **1** | **Biological** | Sleep, metabolism, nervous system regulation, neurophysiological integrity | Dopamine engineering, sleep disruption, neuro-intrusion via BCIs | No |
| **2** | **Cognitive** | Attention control, deep thinking, memory, learning agility, reasoning capacity | Attention capture, cognitive load flooding, offloading atrophy | No |
| **3** | **Emotional** | Stress tolerance, emotional regulation, identity stability, trauma recovery | Micro-targeted emotional priming, anxiety engineering, identity fragmentation | No |
| **4** | **Social** | Trust networks, belonging, family continuity, community cohesion, civic identity | Social trust fragmentation, synthetic persona infiltration, micro-tribe reinforcement | No |
| **5** | **Purpose & Moral** | Values, meaning, service beyond self, moral reasoning capacity, ethical judgment | Moral displacement through automation, legitimized narrative capture, ethics outsourcing | Refined |
| **6** | **Digital & AI Symbiosis** | Working with AI without cognitive erosion; maintaining agency in automated environments; resisting manipulation by synthetic media | Decision automation capture, guardrail bias exploitation, model drift degradation, psychographic microtargeting | **✅ NEW** |

### Why Domain 6 Changes Everything

Every other domain assumes the human is the primary agent. Domain 6 recognizes that in the AI era, the human operates within a **human-AI system**. If the AI side of that system is compromised, biased, or adversary-controlled, the human's resilience in Domains 1–5 may be irrelevant.

Domain 6 is also the only resilience domain backed by both human training and technical enforcement architecture — specifically, the **Ethical Functionality without Agency (EFA)** paradigm and the **EFA/AI-SAFE² 7-Layer Protocol Stack (E7)**, which ensure that human authority over AI systems is not a preference but an architectural guarantee.

### Domain Interdependency Cascade

The six domains form a reinforcing system. Degradation in one domain creates vulnerability in others:

```
Biological Degradation Cascade (upward):
  Domain 1 → Domain 2 → Domain 3 → Domain 4 → Domain 5 → Domain 6
  Sleep loss → Impaired cognition → Reduced emotional regulation →
  Strained relationships → Eroded purpose → AI discipline failure

Digital Compromise Cascade (downward):
  Domain 6 → Domain 2 → Domain 3 → Domain 4 → Domain 5 → Domain 1
  Compromised AI → Poisoned information → Triggered emotions →
  Fragmented social trust → Eroded purpose → Biological stress
```

---

## 📂 Repository Structure

```
/
├── .github/                          # CI/CD Workflows & Issue Templates
│   ├── ISSUE_TEMPLATE/
│   │   ├── new-threat-entry.md
│   │   └── technique-update.md
│   └── workflows/
│       └── taxonomy-lint.yml
│
├── 01-biological/                    # Domain 1: Biological Resilience
│   └── README.md
├── 02-cognitive/                     # Domain 2: Cognitive Resilience
│   └── README.md
├── 03-emotional/                     # Domain 3: Emotional Resilience
│   └── README.md
├── 04-social/                        # Domain 4: Social Resilience
│   └── README.md
├── 05-purpose-moral/                 # Domain 5: Purpose & Moral Resilience
│   └── README.md
├── 06-digital-ai-symbiosis/          # Domain 6: Digital & AI Symbiosis (NEW)
│   └── README.md
│
├── taxonomy/                         # Complete Threat Taxonomy Registry
│   ├── registry.json                 # Machine-readable full registry (41+ entries)
│   ├── threat-architecture.md        # Five-layer causal stack overview
│   ├── civilizational-drivers.md     # Layer -2: CD-001 through CD-006
│   ├── substrate-threats.md          # Layer -1: ST-001 through ST-007
│   ├── manipulation-techniques.md    # Layer 0: T-CT-001 through T-CT-018
│   ├── delivery-scale.md             # Layer +1: DS-001 through DS-005
│   ├── human-outcomes.md             # Layer +2: HO-001 through HO-005
│   ├── threat-classes.md             # TC-01 through TC-10 (newly identified)
│   └── ctss-scoring.md              # Cognitive Threat Severity Scoring model
│
├── command-center/                   # Interactive HTML5 + JSON Command Center
│   └── index.html                    # Visual threat map and domain dashboard
│
├── research/                         # Deep Dive Evidence & Justifications
│   ├── 001_cognitive_offloading.md
│   ├── 002_swarm_threat_scaling.md
│   ├── 003_guardrail_drift.md
│   └── 004_efa_enforcement_architecture.md
│
├── resources/                        # Free Community Tools
│   ├── assessment-template.md        # Reusable Threat Assessment Template
│   ├── ctss-calculator.md            # Manual CTSS scoring worksheet
│   └── domain6-checklist.md          # Domain 6 self-assessment checklist
│
├── examples/                         # Operational Examples
│   ├── ctss_calculator.py            # Python CTSS scoring tool
│   ├── technique_entry_T-CT-004.md   # Full operational template example
│   └── unit_readiness_assessment.md  # Sample unit-level cognitive readiness assessment
│
├── assets/                           # Visual Maps & Diagrams
│
├── CITATION.cff                      # Academic Citation
├── CODE_OF_CONDUCT.md
├── CODEOWNERS
├── CONTRIBUTING.md
├── EVOLUTION.md                      # Version history
├── LICENSE                           # Dual License: MIT + CC-BY-SA 4.0
├── MAINTAINERS.md
├── README.md                         # You are here
├── SECURITY.md
└── SENTINEL_PROGRAM.md               # Community tiers & contributor recognition
```

---

## ⚡ Threat Taxonomy

The CSF threat taxonomy contains **41 classified entries** across five causal layers, designed as a living system at the technique layer (T-CT) while maintaining structural stability at the foundation layers.

### CTSS Top 5 — Critical Threats (Score 80–100)

| Rank | ID | Technique | CTSS |
|---|---|---|---|
| 1 | T-CT-008 | Memetic Swarm Orchestration | **90** |
| 2 | T-CT-010 | Economic Coercion & Incentive Corruption | **88** |
| 3 | T-CT-004 | Personalized Narrative Injection | **85** |
| 4 | T-CT-013 | Social Scoring & Behavioral Governance | **83** |
| 5 | T-CT-006 | Decision Automation Capture | **82** |

> **Key Finding:** Memetic Swarm Orchestration (T-CT-008) scores highest due to high likelihood (already operational with UGC farms), high impact on agency, and global reach. Neurotech (T-CT-012) scores lowest today but will climb rapidly as the technology matures.

📄 **[View the complete CTSS ranking →](./taxonomy/ctss-scoring.md)**
📊 **[Interactive Command Center →](./command-center/index.html)**

---

## 📊 Cognitive Threat Severity Scoring

The **CTSS** is the weighted severity model enabling threat prioritization and resource allocation.

| Component | Description | Weight |
|---|---|---|
| **Likelihood (L)** | Probability of occurrence (0–5 scale) | 0.25 |
| **Impact on Agency (Ia)** | Effect on human autonomy (0–5 scale) | 0.30 |
| **Population Reach (R)** | Scale of affected people (0–5 scale) | 0.20 |
| **Detection Difficulty (D)** | How hard to identify (0–5; higher = harder) | 0.15 |
| **Recovery Difficulty (RecD)** | How hard to reverse (0–5; higher = harder) | 0.10 |

**Formula:** `CTSS = (L×0.25 + Ia×0.30 + R×0.20 + D×0.15 + RecD×0.10) × 20`

Range: **0–100** | Critical ≥ 80 | High ≥ 70 | Elevated ≥ 60

---

## 🖥️ Command Center

The CSF includes an interactive **HTML5 Command Center** — a visual threat map and domain dashboard deployable locally or as a GitHub Pages site.

**Features:**
- Live CTSS heatmap across all 18 technique families
- Five-layer causal stack visualization
- Six-domain resilience status dashboard
- Edge case coverage matrix
- Swarm threat phase progression tracker
- JSON-driven — all data sourced from `taxonomy/registry.json`

```bash
# Run locally
cd command-center
open index.html
# or
python3 -m http.server 8080
```

---

## 🗺️ Implementation Roadmap

The CSF deploys in three phases across 36 months.

### Phase 1 — Foundation (0–12 months)
- Develop Domain 6 assessment tools and training curriculum
- Conduct baseline cognitive resilience assessments across pilot units
- Integrate CSF concepts into existing resilience training programs
- Establish CTSS scoring and threat monitoring protocols
- Develop measurement protocols for the five outcome indicators

### Phase 2 — Integration (12–24 months)
- Expand Domain 6 training to initial accession training across services
- Integrate cognitive resilience metrics into unit readiness assessments
- Deploy inoculation training based on identified manipulation techniques
- Establish family and dependent cognitive resilience programs
- Begin cross-service coordination for standardized assessment tools

### Phase 3 — Operationalization (24–36 months)
- Full integration with PME curricula across all services
- Operational cognitive readiness assessments comparable in rigor to physical fitness testing
- Commander accountability for unit cognitive resilience
- Continuous red-teaming of CSF effectiveness against evolving threats
- Extension of CSF principles to defense industrial base and public programs

---

## 📐 Measurable Outcomes

Resilience must be observable, not inspirational. Five outcome indicators determine success or failure:

| Indicator | What It Measures | Success Threshold |
|---|---|---|
| Sustained Attention Span | Ability to maintain deep focus without platform-driven interruption | 20–30% improvement in controlled studies |
| Resistance to False Narratives | Ability to identify and reject manipulative content including deepfakes | ~40% reduction in false narrative adoption |
| Stable Moral Reasoning Under Pressure | Maintaining ethical judgment when social pressure or automation suggests compliance | Audit-verified maintenance in AI-augmented environments |
| Ability to Act Against Social Manipulation | Recognizing and resisting synthetic consensus and manufactured outrage | Measurable independence in red-team pressure exercises |
| Preservation of Personal Agency | Independent decision-making despite AI recommendation systems | Sustained or improved critical thinking scores despite increasing AI usage |

> **The true metric is not misinformation detected or propaganda countered. The true metric is the preservation or loss of self-directed cognition.**

---

## 🔗 Companion Framework: AI SAFE²

The CSF protects the human cognitive layer. It does not secure the AI system the human is operating.

An AI infrastructure with prompt injection vulnerabilities, misconfigured agent scoping, or compromised memory systems can undermine human cognitive sovereignty regardless of how well-trained the operator is. The CSF covers the human side. **[AI SAFE²](https://github.com/CyberStrategyInstitute/ai-safe2-framework)** covers the machine side.

| | CSF | AI SAFE² |
|---|---|---|
| **Layer** | Human | Machine |
| **Defends** | The human operator | The AI system |
| **Governs** | The capacity to govern the tool | The tool |
| **Prevents** | Cognitive offloading, attention capture, decision automation capture, identity fragmentation | Prompt injection, data leakage, unsafe autonomy, swarm governance failures |
| **Ensures** | The human stays capable of defining the lane | AI stays in its lane |
| **Repo** | [https://github.com/CyberStrategyInstitute/cognitive-sovereignty](https://github.com/CyberStrategyInstitute/cognitive-sovereignty) | [https://github.com/CyberStrategyInstitute/ai-safe2-framework](https://github.com/CyberStrategyInstitute/ai-safe2-framework) |

**The shared principle:** Both frameworks enforce the same core commitment — AI is always a tool, never a moral agent. Human authority is non-negotiable. The CSF's EFA paradigm and E7 Protocol Stack enforce this at the human-AI interface layer. AI SAFE²'s runtime governors and circuit breakers enforce it at the technical infrastructure layer.

**The threat that connects both frameworks:** The highest-scoring threat in the CSF taxonomy is [T-CT-008: Memetic Swarm Orchestration (CTSS 90)](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/csf-explorer.html) — coordinated AI agent campaigns that test, evolve, and amplify narratives at non-human speed. AI SAFE² defends AI system integrity against adversarial swarm techniques. The CSF defends human populations against the cognitive effects of swarm-delivered narratives. Defending only one layer leaves the other entirely exposed.

> **Together, CSF + AI SAFE² cover the full human-AI system: CSF for the human, AI SAFE² for the machine. Neither is sufficient without the other.**

→ **[AI SAFE² Repository](https://github.com/CyberStrategyInstitute/ai-safe2-framework)** — The Universal GRC Operating System for Agentic AI, Non-Human Identities, and Swarm Governance  
→ **[AI SAFE² Companion Release Note](https://github.com/CyberStrategyInstitute/ai-safe2-framework/blob/main/docs/CSF-COMPANION.md)** — How the two frameworks fit together in practice

### DoW AI Ethical Principles Alignment (Feb 24, 2020)

| Principle | CSF Alignment |
| --- | --- |
| **Responsible** | Domain 5 (Purpose & Moral) builds the moral reasoning capacity required for responsible AI use |
| **Equitable** | Domain 4 (Social) addresses algorithmic bias and access equity |
| **Traceable** | Domain 6 (Digital & AI Symbiosis) mandates provenance verification and HEAR accountability |
| **Reliable** | Domain 2 (Cognitive) builds independent verification capacity to detect model drift |
| **Governable** | E7 Layer 7 ensures human authority remains at the top of every system |

---

## 📋 Validation Requirements

The framework is not valid until it passes four empirical tests.

| Test | Requirement | Failure Condition |
|---|---|---|
| **1. Threat Surface Coverage** | Framework must map and mitigate 90%+ of identified threat vectors | Coverage drops below 90% = structural gaps adversaries will exploit |
| **2. Measurable Human Outcomes** | All five resilience indicators show measurable improvement | No measurable improvement = aspirational, not operational |
| **3. Edge-Case Stress Testing** | Framework survives extreme propaganda, total information saturation, AI-generated reality indistinguishability | Breaks under edge-case stress = below 90% coverage |
| **4. Long-Arc Historical Consistency** | Model holds across all historical eras from pre-industrial to AI swarm era | Only works in current era = time-bound ideology, not doctrine |

---

## 📈 Framework Evolution

| Version | Focus | Key Addition | Classification Entries |
|---|---|---|---|
| **v2.0** | Complete AI-Era Architecture | Domain 6, EFA integration, E7 Stack, HEAR Doctrine | 41 entries + 10 threat classes + 3 edge domains |
| **v1.0** | Foundation | Six-domain model proposal, CTSS scoring baseline | 18 technique families, 4-layer stack |

👉 **[Read the full evolution history →](./EVOLUTION.md)**

---

## 🤝 Contributing

This is a living doctrine. Contributions follow the same red-team standard used to develop the framework itself.

**How to contribute:**
- **New Threat Entry:** Use the [New Threat Entry Template](.github/ISSUE_TEMPLATE/new-threat-entry.md) to propose additions to the T-CT layer
- **Technique Update:** Use the [Technique Update Template](.github/ISSUE_TEMPLATE/technique-update.md) to revise CTSS scores or detection methods
- **Research Submission:** Add peer-testable evidence to `/research/` with full sourcing

The taxonomy is designed to grow at the T-CT layer. The CD and ST layers are designed to be stable but expandable. All contributions must pass the **Adversarial Reproduction Test**: opponents using the same data and methodology must arrive at the same measurements.

📄 **[Read the full Contributing Guide →](./CONTRIBUTING.md)**

---

## 🛡️ Sentinel Program

Recognize and reward the contributors who help harden this doctrine.

- ⭐ **Star the Repo:** Unlock `Supporter` status
- 💡 **Contribute a Technique Entry:** Earn `Analyst` status  
- 🔬 **Submit Validated Research:** Earn `Researcher` status
- 🏆 **The Sentinel Tier:** Priority access to upcoming CSI tools and assessment platforms

📄 **[Read the Sentinel Program Details →](./SENTINEL_PROGRAM.md)**

---

## ✏️ Citation

```bibtex
@misc{csf_framework_2026,
  title   = {Cognitive Sovereignty Framework v2.0: A Six-Domain Model for Human Resilience in the AI Era},
  author  = {{Cyber Strategy Institute}},
  year    = {2026},
  month   = {February},
  publisher = {Cyber Strategy Institute},
  url     = {https://github.com/CyberStrategyInstitute/cognitive-sovereignty-framework},
  note    = {Version 2.0. Companion to the Cognitive Threat Assessment and Cognitive Threat Taxonomy.}
}
```

---

## ⚖️ Licensing

This project uses a Dual-License Model.

### 💻 Code: MIT License
Applies to: Command Center HTML/JS, CTSS calculator scripts, JSON registry, and all code files.
You may use this code commercially, modify it, and build products on top of it.

### 📘 Framework/Docs: CC-BY-SA 4.0
Applies to: The CSF methodology text, domain definitions, threat taxonomy, and all documentation.
You may share, adapt, and redistribute. **You must attribute the Cyber Strategy Institute and share derivatives under the same license.**

---

Managed by [Cyber Strategy Institute](https://cyberstrategyinstitute.com) | Copyright © 2026. All Rights Reserved.

> *"The question is not whether we build the defenses. The question is whether we build them before the substrate is too degraded to support them."*
