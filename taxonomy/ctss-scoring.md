# Cognitive Threat Severity Scoring (CTSS)

> The CTSS is the weighted severity model enabling threat prioritization and resource allocation. It produces a 0–100 score for each technique family, enabling direct comparison and resource allocation. **Without CTSS, the threat picture remains philosophical.**

---

## Scoring Model

| Component | Description | Weight |
|---|---|---|
| **Likelihood (L)** | Probability of occurrence on a 0–5 scale | **0.25** |
| **Impact on Agency (Ia)** | Effect on human autonomy on a 0–5 scale | **0.30** |
| **Population Reach (R)** | Scale of affected people on a 0–5 scale | **0.20** |
| **Detection Difficulty (D)** | How hard to identify (0–5; higher = harder) | **0.15** |
| **Recovery Difficulty (RecD)** | How hard to reverse (0–5; higher = harder) | **0.10** |

**Formula:**
```
CTSS = (L × 0.25 + Ia × 0.30 + R × 0.20 + D × 0.15 + RecD × 0.10) × 20
```

**Range:** 0–100

| Tier | Score | Color |
|---|---|---|
| **Critical** | ≥ 80 | 🔴 Maroon |
| **High** | 70–79 | 🟠 Orange |
| **Elevated** | 60–69 | ⚪ Grey |

---

## Complete CTSS Rankings

| Rank | ID | Technique | L | Ia | R | D | RecD | **CTSS** |
|---|---|---|---|---|---|---|---|---|
| 1 | T-CT-008 | Memetic Swarm Orchestration | 5 | 4 | 5 | 2 | 4 | **90** 🔴 |
| 2 | T-CT-010 | Economic Coercion & Incentive Corruption | 5 | 4 | 5 | 3 | 4 | **88** 🔴 |
| 3 | T-CT-004 | Personalized Narrative Injection | 4 | 5 | 4 | 3 | 4 | **85** 🔴 |
| 4 | T-CT-013 | Social Scoring & Behavioral Governance | 4 | 5 | 3 | 3 | 4 | **83** 🔴 |
| 5 | T-CT-006 | Decision Automation Capture | 4 | 5 | 4 | 4 | 3 | **82** 🔴 |
| 6 | T-CT-015 | Legitimized Narrative Capture | 4 | 4 | 5 | 4 | 3 | **81** 🔴 |
| 7 | T-CT-001 | Attention Capture and Habituation | 5 | 3 | 5 | 2 | 3 | **80** 🔴 |
| 8 | T-CT-016 | Psychographic Micro-Targeting at Scale | 4 | 4 | 4 | 3 | 3 | **79** 🟠 |
| 9 | T-CT-005 | Identity Replacement / Persona Hijacking | 4 | 4 | 4 | 2 | 4 | **78** 🟠 |
| 10 | T-CT-014 | Cognitive Load Flooding | 5 | 3 | 4 | 2 | 3 | **77** 🟠 |
| 11 | T-CT-007 | Information Ecosystem Poisoning | 4 | 3 | 5 | 3 | 3 | **76** 🟠 |
| 12 | T-CT-002 | Algorithmic Amplification | 5 | 3 | 5 | 3 | 2 | **75** 🟠 |
| 13 | T-CT-018 | Repetition & Normalization Manipulation | 5 | 3 | 5 | 3 | 2 | **74** 🟠 |
| 14 | T-CT-009 | Institutional & Bureaucratic Capture | 4 | 3 | 4 | 3 | 3 | **72** 🟠 |
| 15 | T-CT-003 | Micro-Targeted Emotional Priming | 4 | 3 | 4 | 4 | 2 | **70** 🟠 |
| 15 | T-CT-017 | Guardrail Bias Exploitation | 4 | 3 | 3 | 4 | 2 | **70** 🟠 |
| 17 | T-CT-011 | Epistemic Rewriting | 3 | 4 | 3 | 4 | 4 | **65** ⚪ |
| 18 | T-CT-012 | Neurotech / Direct Cognitive Influence | 2 | 5 | 2 | 5 | 4 | **60** ⚪ |

---

## Key Findings

**Highest:** Memetic Swarm Orchestration (T-CT-008) scores highest due to high likelihood (already operational with UGC farms), high impact on agency, and global population reach.

**Highest Agency Impact:** Personalized Narrative Injection (T-CT-004), Social Scoring (T-CT-013), and Decision Automation Capture (T-CT-006) all score Ia = 5 — maximum impact on human autonomy.

**Watch-List:** Neurotech / Direct Cognitive Influence (T-CT-012) scores lowest today (CTSS = 60) due to low current likelihood, but its Ia score of 5 means it will climb rapidly as brain-computer interface technology matures.

**Invisible Threats:** Guardrail Bias Exploitation (T-CT-017) and Model Performance Drift (ST-007) both have Detection = 2 or lower, meaning most affected populations cannot identify they are being influenced.

---

## Coverage Proof Process

**Step 1 — Inventory:** Map all systems, channels, platforms, communications, and institutions to manipulation vectors and technique exposure.

**Step 2 — Score:** Compute CTSS per technique per asset.

**Step 3 — Map Mitigations:** Assign mitigation IDs (M-###) and compute residual CTSS after mitigations.

**Step 4 — Cumulative Coverage:** Rank techniques by residual CTSS. Show that implementing top-N mitigations reduces total systemic CTSS by 90% or more. Validate with Monte Carlo simulation across actor vectors and swarm scenarios.

**Step 5 — Operational Validation:** Run periodic exercises (red-team, blue-team, purple-team, human cohort psychometric tests). Measure real-world indicators: belief drift, behavior change, decision errors, default acceptance of autopilot flows.

**Evidence Standard:** Require empirical pre/post metrics and objective system telemetry. Without measured improvement, the mitigation is rejected.

---

## Using CTSS for Resource Allocation

CTSS enables prioritized defense investment:

1. **Focus substrate defense first.** Substrate threats (ST layer) do not have their own CTSS but enable all T-CT layer techniques. Addressing ST-003 (Cognitive Offloading) and ST-006 (Guardrail Alignment Drift) reduces the effective CTSS of multiple technique families simultaneously.

2. **Prioritize high-Ia techniques.** Impact on Agency (Ia = 0.30) has the highest weight in the formula. Techniques with Ia ≥ 4 deserve disproportionate defensive investment because they strike at the foundational capacity for self-determination.

3. **Monitor low-detection threats.** Techniques with Detection ≤ 2 (T-CT-006, T-CT-003, T-CT-011, T-CT-012, T-CT-015, T-CT-017) require active monitoring programs because affected populations will not self-identify exposure.

4. **Track recovery difficulty for long-term planning.** Techniques with RecD ≥ 4 (T-CT-004, T-CT-008, T-CT-010, T-CT-012, T-CT-013) cause persistent damage that does not reverse when the active technique stops. Prevention is orders of magnitude more efficient than recovery.
