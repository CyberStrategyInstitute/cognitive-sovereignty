# Layer 0: Active Manipulation Techniques

> **This is the living layer.** Eighteen technique families identified through analysis and red-team wargaming. This is where adversary adaptation occurs fastest. The taxonomy is designed to grow at this layer as new mechanisms emerge. The technique count will increase. The layers beneath (CD, ST) are more stable and encompassing. The layers above (DS, HO) track delivery and effects.

**Warning:** The most dangerous aspect of these techniques is that they do not operate in isolation. A coordinated cognitive campaign layers them: emotional priming creates vulnerability, algorithmic amplification delivers the payload, synthetic social proof makes it appear to be consensus, repetition normalizes it, and legitimized narrative capture prevents the target from recognizing the operation. Each technique alone is manageable. In combination, they create effects that are nearly impossible to detect from inside the influence environment.

---

## CTSS Tier Summary

| Tier | Score | Techniques |
|---|---|---|
| 🔴 Critical | ≥ 80 | T-CT-008, T-CT-010, T-CT-004, T-CT-013, T-CT-006, T-CT-015, T-CT-001 |
| 🟠 High | 70–79 | T-CT-016, T-CT-005, T-CT-014, T-CT-007, T-CT-002, T-CT-018, T-CT-009, T-CT-003, T-CT-017 |
| ⚪ Elevated | 60–69 | T-CT-011, T-CT-012 |

---

## Technique Registry

### T-CT-001 — Attention Capture and Habituation
**CTSS: 80** 🔴 Critical

| Field | Value |
|---|---|
| **Vector/Channel** | Habit loops, infinite scroll, variable rewards |
| **Primary Domains** | Cognitive, Emotional, Biological |
| **Detection** | 4 / 5 |
| **Timeline** | Today |
| **Targets** | Attention sovereignty, ability to focus and reason |

**Mechanism:** Infinite scroll, variable rewards, notification saturation, and dopamine loop design redirect and fragment cognitive attention. Platform architecture is optimized to maximize time-on-device, which requires capturing and continuously re-capturing the user's attention. The habit loop created by variable-ratio reinforcement makes the attention capture self-sustaining.

**Substrate Enabler:** ST-002 (Behavioral Reinforcement Engineering) is the pre-existing condition that makes this technique effective at scale.

**Human Outcome:** HO-001 (Attention Ownership Loss). Cognitive fragmentation reduces creative output quality by 30 to 50 percent. The shift from deep attention to hyperattention (multiple foci, rapid switching) is documented and accelerating.

**Countermeasures:**
- Domain 1: Circadian discipline, device hygiene protocols
- Domain 2: Deep reading practice, attention hygiene training, single-task focus exercises
- Domain 6: AI interaction discipline, notification management frameworks

---

### T-CT-002 — Algorithmic Amplification
**CTSS: 75** 🟠 High

| Field | Value |
|---|---|
| **Vector/Channel** | Virality optimization, feed ranking |
| **Primary Domains** | Informational, Cognitive |
| **Detection** | 3 / 5 |
| **Timeline** | 1–2 years |
| **Targets** | Collective perception, shared reality |

**Mechanism:** Engagement-optimized distribution rewards outrage and emotional intensity over accuracy. The algorithm does not evaluate truth — it evaluates engagement. Content that produces emotional responses (anger, fear, disgust, tribal identity activation) spreads further and faster than accurate but emotionally neutral information.

**Key Metric:** False information spreads six times faster than truthful information on social platforms.

**Countermeasures:**
- Domain 2: Source verification habits, critical thinking exercises
- Domain 4: Source diversity practices, trusted network cultivation
- Domain 6: Algorithmic literacy — understanding how feed ranking shapes information exposure

---

### T-CT-003 — Micro-Targeted Emotional Priming
**CTSS: 70** 🟠 High

| Field | Value |
|---|---|
| **Vector/Channel** | Psychographic data, sentiment adaptation |
| **Primary Domains** | Emotional |
| **Detection** | 2 / 5 |
| **Timeline** | Today |
| **Targets** | Emotional stability, rational decision-making |

**Mechanism:** Personalized content engineered to elevate baseline anxiety, anger, or fear in specific populations. The priming occurs before any explicit message is delivered — it pre-tunes the emotional state toward receptivity for subsequent manipulation. Works at the population segment level, not just the individual.

**Detection Challenge (2/5):** The content appears organic. The emotional effect is experienced as a response to real events, not as a manipulation. The personalization is invisible.

**Countermeasures:**
- Domain 3: Emotional awareness training, emotional state monitoring
- Domain 6: Psychographic micro-targeting literacy — understanding that emotional state is being actively managed

---

### T-CT-004 — Personalized Narrative Injection
**CTSS: 85** 🔴 Critical

| Field | Value |
|---|---|
| **Vector/Channel** | Trusted channel hijack, LLM generation |
| **Primary Domains** | Cognitive, Social, Purpose & Moral, Digital & AI Symbiosis |
| **Detection** | 3 / 5 |
| **Timeline** | 1–2 years |
| **Targets** | Belief formation, trust in information sources |

**Mechanism:** AI-generated deepfakes and synthetic text inserted into an individual's trusted channels — contacts, professional networks, media sources — to alter beliefs or implant false memories. The personalization makes the injection appear to come from trusted sources, bypassing the skepticism applied to unknown sources.

**Why This Is High-Agency (Ia=5):** The technique does not just change what people believe. It changes what they remember. False memory implantation through synthetic media targeting personal trust networks attacks the epistemic foundation of individual identity.

**Actor Classes:** State actors, advanced criminal groups, adversarial swarms.

**Indicators:**
- Sudden adoption of new narratives with no preceding corroboration
- Spike in private-messaging dissemination
- Mismatched provenance metadata
- New accounts coordinating around micro-narratives

**Detection Methods:** Cross-source provenance checks, cryptographic content provenance, triangulation of independent eyewitness signals, anomaly detection in message origin/time patterns.

**Countermeasures:**
- Domain 2 (M-004c): Inoculation training (pre-bunking), critical-thinking micro-curriculum, friction in sharing flows
- Domain 6 (M-004g): Mandatory provenance headers, signed content, verifiable identity tokens, AI watermarking
- Domain 1 (M-004b): Sleep and attention hygiene campaigns to reduce susceptibility during stressed states
- Domain 4 (M-004e): Diversify trusted information networks. Resilient local anchors

**Test/Exercise (X-004):** Red-team injects synthetic video and micro-targeted messaging to a controlled cohort. Measure belief adoption, propagation rate, and recovery time after debrief.

**Edge Case:** Indistinguishable synthetic media in physical press conferences requires escalation to institutional provenance authorities.

---

### T-CT-005 — Identity Replacement / Persona Hijacking
**CTSS: 78** 🟠 High

| Field | Value |
|---|---|
| **Vector/Channel** | Algorithmic segmentation, echo chambers |
| **Primary Domains** | Social, Purpose & Moral |
| **Detection** | 4 / 5 |
| **Timeline** | Today |
| **Targets** | Trust networks, identity anchoring |

**Mechanism:** Synthetic personas mimicking trusted figures or creating fictional authority figures. At scale: algorithmic segmentation creates identity groups defined by the platform, which then become the dominant identity for participants. The platform becomes the identity-granting authority.

**Substrate Enabler:** ST-005 (Social Trust Fragmentation) creates the micro-tribe structures that synthetic personas exploit.

---

### T-CT-006 — Decision Automation Capture
**CTSS: 82** 🔴 Critical

| Field | Value |
|---|---|
| **Vector/Channel** | Default seeding, AI copilot substitution |
| **Primary Domains** | Cognitive |
| **Detection** | 2 / 5 |
| **Timeline** | 3–5 years |
| **Targets** | Agency, independent decision-making |

**Mechanism:** Seeding biased defaults and autopilot behaviors through AI copilots and recommendation engines. The user is not prevented from choosing differently — they simply never consider it. The default becomes the decision. When applied systematically across AI copilots used for consequential decisions (operational planning, intelligence assessment, resource allocation), the aggregate effect is capture of the decision-making apparatus without the decision-maker's awareness.

**Detection Challenge (D=4):** The automation feels like assistance. The bias feels like efficiency. Independent verification of AI recommendations requires cognitive capacity that has often been offloaded (ST-003) — creating a self-reinforcing dependency.

**EFA/E7 Countermeasure:** E7 Layer 7 ensures human authority over all consequential decisions. R/M/H classification (Routine/Material/High-Stakes) prevents autopilot behaviors from creeping into high-stakes domains. HEAR ensures someone is always accountable.

---

### T-CT-007 — Information Ecosystem Poisoning
**CTSS: 76** 🟠 High

**Mechanism:** Data poisoning of recommendation algorithms and knowledge bases through coordinated engagement. If a sufficient volume of coordinated engagement trains the algorithm to associate certain queries with certain conclusions, subsequent users receive those conclusions as organic recommendations.

---

### T-CT-008 — Memetic Swarm Orchestration
**CTSS: 90** 🔴 Critical — Highest in Taxonomy

| Field | Value |
|---|---|
| **Vector/Channel** | Narrative mutation, A/B testing at scale |
| **Primary Domains** | Digital & AI Symbiosis |
| **Detection** | 4 / 5 |
| **Timeline** | Today |
| **Targets** | Collective sensemaking, democratic discourse |

**Mechanism:** Coordinated campaigns using thousands of AI agents to test, evolve, and amplify narratives. Unlike traditional influence operations where a message is crafted and deployed, swarm orchestration is evolutionary — thousands of narrative variants are tested simultaneously, the most effective variants are amplified, and the process iterates continuously. No human author determines which message wins. The winning message is determined by what maximizes engagement or behavioral change.

**Why CTSS = 90:** Likelihood = 5 (already fully operational with UGC farms), Population Reach = 5 (global by design), Recovery Difficulty = 4 (narratives established through evolutionary selection persist after detection because they were selected for maximum psychological adhesion).

**Swarm Detection Module:** S1 (Synthetic Consensus Scanner) and S2 (Autonomous Narrative Evolution Monitor) are the primary countermeasures.

See: [research/002_swarm_threat_scaling.md](../research/002_swarm_threat_scaling.md)

---

### T-CT-009 — Institutional and Bureaucratic Capture
**CTSS: 72** 🟠 High

**Mechanism:** Regulatory capture, legal weaponization, and bureaucratic self-preservation suppressing dissent. The institution that is responsible for cognitive defense becomes the instrument of cognitive constraint.

---

### T-CT-010 — Economic Coercion and Incentive Corruption
**CTSS: 88** 🔴 Critical

**Mechanism:** Financial penalties for non-conformity, monetization of specific viewpoints, funding tied to narrative compliance. Demonetization, deplatforming, defunding — economic tools that shape discourse without explicit censorship.

---

### T-CT-011 — Epistemic Rewriting
**CTSS: 65** ⚪ Elevated

**Mechanism:** Historical record alteration, selective erasure, and revision of foundational narratives. AI timestamping forgery and mass record tampering are emerging capabilities that make this technique more scalable than historical equivalents.

---

### T-CT-012 — Neurotech / Direct Cognitive Influence
**CTSS: 60** ⚪ Elevated — Watch-List

**Mechanism:** Brain-computer interfaces, neurostimulation, and neural data harvesting for persuasion or control. Currently scored low due to low Likelihood (L=2), but Impact on Agency is maximum (Ia=5). As BCI technology matures, this will become the highest-CTSS technique in the taxonomy.

---

### T-CT-013 — Social Scoring and Behavioral Governance
**CTSS: 83** 🔴 Critical

**Mechanism:** Automated conformity enforcement through scoring systems rewarding compliant behavior. Social credit architectures, reputation scores, and behavioral governance systems replace explicit legal compulsion with automated social and economic pressure.

---

### T-CT-014 — Cognitive Load Flooding
**CTSS: 77** 🟠 High

**Mechanism:** Overwhelming attention with contradictory information until analytical capacity collapses. The target does not reach a false conclusion — they reach no conclusion. Analysis paralysis produces compliance with the status quo or default option.

---

### T-CT-015 — Legitimized Narrative Capture
**CTSS: 81** 🔴 Critical

**Mechanism:** Control framed as safety, equity, efficiency, or personalization so it appears benevolent. The most effective technique against individuals who would resist overt coercion — they accept the same control when it is framed as protection. The target cannot identify the operation as manipulation because it is indistinguishable from genuine care.

---

### T-CT-016 — Psychographic Micro-Targeting at Scale
**CTSS: 79** 🟠 High

**Mechanism:** AI-powered profiling and personalized persuasion based on psychological vulnerability mapping. Each individual receives persuasion content calibrated to their specific psychological profile — anxieties, aspirations, identity commitments, cognitive biases.

---

### T-CT-017 — Guardrail Bias Exploitation
**CTSS: 70** 🟠 High

| Field | Value |
|---|---|
| **Vector/Channel** | Tool-mediated discourse, viewpoint suppression |
| **Primary Domains** | Purpose & Moral, Cognitive |
| **Detection** | 2 / 5 |
| **Timeline** | Today |
| **Targets** | Intellectual freedom, viewpoint diversity |

**Mechanism:** Using AI alignment restrictions to suppress viewpoints, enforce conformity, or amplify ideological positions through tool-mediated discourse. Distinct from T-CT-015 (Legitimized Narrative Capture) because it operates specifically through the tools people use to access and process information — the AI systems themselves become the enforcement mechanism.

**Why This Was Added:** T-CT-017 addresses the risk that AI safety guardrails themselves become instruments of ideological enforcement. When AI tools mediate information access, the biases embedded in those tools become invisible structural constraints on thought — operating without any adversary direction.

**E7 Countermeasure:** E7 Layer 6 translates ethical constraints into testable rules rather than subjective guidelines. Ring of Fire provides multi-model oversight that catches when one model's alignment biases are suppressing viewpoints.

---

### T-CT-018 — Repetition and Normalization Manipulation
**CTSS: 74** 🟠 High

| Field | Value |
|---|---|
| **Vector/Channel** | Cross-platform phrase echoing, n-gram spikes |
| **Primary Domains** | Informational, Cognitive |
| **Detection** | 3 / 5 |
| **Timeline** | Today |
| **Targets** | Independent belief formation, resistance to manufactured consensus |

**Mechanism:** Coordinated echoing of phrases, framings, or positions across platforms until they are accepted as baseline consensus. The repetition does not require argument — it requires only scale. A claim repeated across sufficient channels, by sufficient accounts, in sufficient media formats, is experienced as common knowledge regardless of its accuracy.

**Detection Method:** N-gram spike analysis and linguistic pattern monitoring can detect coordinated phrase emergence that does not follow organic spread patterns.

**Why This Was Added:** T-CT-018 addresses coordinated phrase and framing repetition across media and platforms. Both T-CT-017 and T-CT-018 represent techniques that are currently active and measurable.

---

## Living System Protocol

New technique entries must pass the red-team validation standard:

1. Does the mechanism represent a genuine cognitive threat (targets how people think) rather than a content-layer threat (targets what people see)?
2. Is it distinct from existing entries, or better represented as a sub-technique?
3. Can CTSS components be scored independently by multiple evaluators?
4. Does the associated mitigation address the mechanism, not just the symptom?
5. Would the entry flag misuse of this technique regardless of the ideology of the actor?

To propose a new entry, use the [New Threat Entry template](../.github/ISSUE_TEMPLATE/new-threat-entry.md).
