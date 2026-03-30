# Contributing to the Cognitive Sovereignty Framework

The CSF is a **living doctrine**. The threat taxonomy is designed as a living system, particularly at the Technique (T-CT) layer. Contributions are governed by the same red-team standard used to develop the framework itself.

---

## Guiding Principle

> A framework that cannot be falsified is not a framework — it is a philosophy. Every contribution must be testable, measurable, and disprovable.

All contributions must pass the **Adversarial Reproduction Test**: an opponent using the same data and methodology must arrive at the same measurements, even if they disagree with the interpretation.

---

## What We Accept

### 1. New Threat Entries (T-CT Layer)

The T-CT layer is the living system. New technique families should be submitted when:
- A mechanism has been observed in the wild or validated through wargaming
- It represents a meaningfully distinct technique from existing entries
- Observable detection signals (indicators) can be defined
- Mitigations can be mapped to at least two of the six CSF domains

Use the [New Threat Entry template](.github/ISSUE_TEMPLATE/new-threat-entry.md).

### 2. CTSS Score Updates

Scores change as conditions evolve. Submit a CTSS update when:
- Likelihood (L) has materially changed due to observed deployment
- Population Reach (R) has expanded or contracted
- Detection Difficulty (D) has changed due to new tools or adversary adaptation
- Recovery Difficulty (RecD) evidence is available from real-world cases

Use the [Technique Update template](.github/ISSUE_TEMPLATE/technique-update.md).

### 3. Research Submissions

Add peer-testable evidence to `/research/` with:
- Clear sourcing (cite to primary data where possible)
- Explicit link to taxonomy IDs affected
- Observable measurement methodology

### 4. CD and ST Layer Additions

Civilizational Drivers and Substrate Threats are designed to be stable but expandable. Proposals for new entries at these layers require:
- Wargaming validation showing the condition enabled threats the taxonomy did not previously capture
- Evidence that the condition pre-exists and enables active techniques (not just correlates with them)
- Cross-era consistency test: does the mechanism apply across historical eras or only to the current moment?

---

## What We Do Not Accept

- Contributions that encode political or ideological conclusions
- Threat entries that measure what people believe rather than system properties
- Mitigations without mapped CSF domain coverage
- CTSS score proposals without observable evidence rationale

---

## Submission Process

1. **Open an Issue** using the appropriate template before submitting a PR
2. **Reference existing taxonomy IDs** in your proposal — show how it fits the causal stack
3. **Include detection indicators** — at least one observable signal per new entry
4. **Map to CSF domains** — every threat entry must link to at least one of the six resilience domains
5. **Submit the PR** against the `develop` branch, not `main`

---

## Red-Team Standard

All new technique entries undergo structured red-team evaluation before acceptance:

1. Does the mechanism represent a genuine cognitive threat or a content-layer threat?
2. Is it distinct from existing entries, or is it better represented as a sub-technique?
3. Can the CTSS components be scored independently by multiple evaluators?
4. Does the associated mitigation address the mechanism, not just the symptom?
5. Would the entry survive the Policy Neutrality Test — would it flag misuse regardless of the ideology of the actor?

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). Cognitive security research requires rigor, not tribalism. Contributions grounded in evidence are welcome from all perspectives.

---

## Recognition

Contributors who meet the standards above are recognized in the [Sentinel Program](./SENTINEL_PROGRAM.md). Significant contributions — validated research, wargaming results, new technique families with full operational templates — qualify for Sentinel tier access.

---

Managed by [Cyber Strategy Institute](https://cyberstrategyinstitute.com)
