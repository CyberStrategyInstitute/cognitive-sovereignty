# Threat Architecture: The Five-Layer Causal Stack

> **Design Principle:** The threats to human cognition operate in layers. Addressing any single layer in isolation produces incomplete defense. Most current defenses target only Layer 0 (active manipulation) while ignoring the layers beneath that make manipulation possible, and the layers above that scale its delivery.

---

## The Five Layers

| Layer | Designation | Function | Question It Answers | Entries |
|---|---|---|---|---|
| **Layer -2** | Civilizational Drivers (CD) | Root forces generating vulnerability conditions | Why is the environment vulnerable? | 6 |
| **Layer -1** | Substrate Threats (ST) | Pre-manipulation foundations | What operates before manipulation begins? | 7 |
| **Layer 0** | Manipulation Techniques (T-CT) | Active cognitive technique families | What discrete actions influence cognition? | 18 |
| **Layer +1** | Delivery & Scale (DS) | Amplification mechanisms | How do techniques reach populations? | 5 |
| **Layer +2** | Human Outcomes (HO) | Observable effects on people | What happens when threats succeed? | 5 |

**Total:** 41 primary entries + 10 newly identified threat classes (TC) + 3 edge domain additions (E)

---

## Critical Insight: The Strategic Center of Gravity

The Civilizational Driver and Substrate layers are relatively stable and all-encompassing. They change slowly and apply broadly. The Active Manipulation layer (T-CT) is where adversary adaptation occurs fastest.

This means the taxonomy must be designed as a **living system at the technique layer** while maintaining structural stability at the foundation layers.

> Wargaming confirmed that if the substrate conditions are not addressed, active techniques will always find new pathways. Defending against personalized narrative injection (T-CT-004) is meaningless if the population has already lost the cognitive capacity to evaluate narratives independently (ST-003).

**The defense must match the architecture of the threat.**

---

## Layer Descriptions

### Layer -2: Civilizational Drivers

These are not attacks. They are structural conditions that make attacks effective. They are the root forces that generate vulnerability. If these conditions exist, the layers above them will always find expression.

See: [civilizational-drivers.md](./civilizational-drivers.md)

**Entries:** CD-001 through CD-006

| Entry | Name | Timeline |
|---|---|---|
| CD-001 | Incentive Misalignment | Today |
| CD-002 | Information Abundance Collapse | 1–2 years |
| CD-003 | Technological Mediation of Reality | 3–5 years |
| CD-004 | Institutional Trust Erosion | Today |
| CD-005 | Computational Acceleration Misalignment | 1–2 years |
| CD-006 | Civilizational Reproduction Failure | 3–5 years |

---

### Layer -1: Substrate Threats

These threats operate before any adversary acts. They are the pre-conditions that make manipulation succeed. If these conditions exist, the active manipulation layer will always find targets.

See: [substrate-threats.md](./substrate-threats.md)

**Entries:** ST-001 through ST-007

| Entry | Name | Timeline |
|---|---|---|
| ST-001 | Algorithmic Epistemic Authority | 1–2 years |
| ST-002 | Behavioral Reinforcement Engineering | Today |
| ST-003 | Cognitive Offloading and Skill Atrophy | 3–5 years |
| ST-004 | Neuro-Intrusion Surface Expansion | 1–2 years |
| ST-005 | Social Trust Fragmentation | Today |
| ST-006 | Guardrail Alignment Drift | Today |
| ST-007 | Model Performance Drift | 1–2 years |

**Critical observation:** ST-003 and ST-006 together represent the most strategically decisive conditions in the entire taxonomy. If autonomy disappears voluntarily through convenience (ST-003), defense mechanisms never trigger. If conformity is enforced through safety framing (ST-006), resistance never forms. Both produce **control without coercion**.

---

### Layer 0: Active Manipulation Techniques

Eighteen technique families identified through analysis. This is where adversary adaptation occurs fastest. The taxonomy is designed as a living system at this layer — the technique count will grow as new mechanisms emerge.

See: [manipulation-techniques.md](./manipulation-techniques.md)

**Entries:** T-CT-001 through T-CT-018

**CTSS Severity Tiers:**

| Tier | Score Range | Count |
|---|---|---|
| **Critical** | 80–100 | 7 techniques |
| **High** | 70–79 | 9 techniques |
| **Elevated** | 60–69 | 2 techniques |

---

### Layer +1: Delivery & Scale Mechanisms

These mechanisms amplify techniques from individual reach to population scale. The key shift: manipulation moves from events to environment.

See: [delivery-scale.md](./delivery-scale.md)

**Entries:** DS-001 through DS-005

---

### Layer +2: Human Outcome Effects

When these threats succeed, they produce measurable changes in human cognition and behavior. These are not theoretical risks — they are observable patterns already present in the population.

See: [human-outcomes.md](./human-outcomes.md)

**Entries:** HO-001 through HO-005

---

## ID Structure Reference

| Level | Format | Example |
|---|---|---|
| Goal | G-### | G-001: Autonomy Erosion |
| Actor Class | A-### | A-002: Platform / Corporate |
| Civilizational Driver | CD-### | CD-001: Incentive Misalignment |
| Substrate Threat | ST-### | ST-003: Cognitive Offloading |
| Manipulation Technique | T-CT-### | T-CT-008: Memetic Swarm Orchestration |
| Delivery/Scale | DS-### | DS-002: Bot/Swarm Automation |
| Human Outcome | HO-### | HO-005: Agency Erosion |
| Capability/Tool | C-### | C-004a: LLM deepfake pipeline |
| Indicator | I-### | I-008: Burst coordination signature |
| Mitigation | M-### | M-004c: Inoculation training |
| Test/Exercise | X-### | X-004: Synthetic injection red-team |

---

## Governing Principles

**Non-Ideological Instrumentation:** The taxonomy never measures beliefs. It measures system properties: autonomy, coercion, opacity, incentive distortion, information integrity, social trust. A left-leaning government using safety narratives to expand control triggers the same metrics as a right-leaning government using security narratives. The framework does not care about ideology. It cares about autonomy.

**Evidence Before Interpretation:** Every output must be observable, quantifiable, and replicable by adversaries. The framework measures patterns and allows evidence to drive interpretation.

**Early Warning Over Post-Mortem:** Trust erosion rates matter more than trust levels. Narrative drift velocity matters more than narrative content. The system watches direction and speed of change, not just current state.

**Three Validity Tests:**
1. **Adversarial Reproduction Test:** Opponents using the same data must arrive at the same measurements, even if they disagree about interpretation.
2. **Predictive Power Test:** The framework must forecast instability before mainstream recognition.
3. **Policy Neutrality Test:** Metrics must remain valid under any administration or ideology.
