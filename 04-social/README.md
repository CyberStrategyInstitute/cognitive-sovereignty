# Domain 04: Social

### The Collective Immune System

**CSF Position:** Domain 4 of 6 | **AI SAFE² CP.11 Controls:** UAS-H3 (social pressure simulation), UAS-H7 (persona and role-boundary erosion) | **Companion Research:** [002 Swarm Threat Scaling](../research/002_swarm_threat_scaling.md)

---

## 1. Doctrine

Trust networks, belonging, family continuity, community cohesion, and civic identity are the mechanisms societies have always used to resist manipulation collectively. Fragment them and every individual defends alone against systems that operate at population scale. That is why the taxonomy treats social trust fragmentation as a substrate threat: algorithmic optimization splits society into micro-tribes with reinforced identity boundaries and incompatible reality models, removing the collective defense coordination that no individual capability can replace.

The attack runs on two axes. Horizontally, synthetic personas and manufactured consensus infiltrate and counterfeit the trust networks themselves: people extend trust to entities that do not exist and consensus that was never held by humans. Vertically, family continuity and intergenerational transmission are degraded by incentive structures that reward narcissistic and individualistic traits over relational commitments. The vertical axis connects this domain directly to CD-006 (Civilizational Reproduction Failure): a civilization that cannot reproduce its trust structures and organizing principles collapses within two generations without any adversary involvement.

> **So what:** individual resilience without social resilience is isolation, not defense. The adversary targets the entire population; a framework that hardens operators while their families and communities fragment around them fails by design.

---

## 2. Threat Exposure

| ID | Threat | Layer | CTSS / Detection | What It Targets in This Domain |
| --- | --- | --- | --- | --- |
| ST-005 | Social Trust Fragmentation | Substrate | Detection 3 | Collective defense coordination; micro-tribes with incompatible reality models |
| T-CT-005 | Identity Replacement / Persona Hijacking | Technique | CTSS 78 / Detection 4 | Trust networks; synthetic personas mimicking trusted figures or fabricating authority |
| T-CT-008 | Memetic Swarm Orchestration | Technique | CTSS 90 / Detection 4 | Collective sense-making; the highest-scoring threat in the taxonomy |
| T-CT-013 | Social Scoring and Behavioral Governance | Technique | CTSS 83 / Detection 3 | Behavioral autonomy; automated conformity enforcement |
| TC-06 | Synthetic Social Proof | Threat Class | n/a | The consensus heuristic; "many believe it" fabricated at commodity cost |
| CD-006 | Civilizational Reproduction Failure | Driver | Detection 2 | Family formation, intergenerational value transmission, continuity structures |
| HO-002 / HO-003 | Belief Instability / Identity Fragmentation | Outcomes | Detection 3-4 | Tribe-seeking replacing truth-seeking; affective polarization nearly doubled in the U.S. since the mid-1990s per the Threat Assessment |

---

## 3. Cascade Position

**Receives from below:** dysregulated emotion (Domain 3) propagates into relationships; captured attention (Domains 1-2) starves relationships of the time and presence trust requires.

**Feeds upward:** fragmented social trust erodes shared purpose and civic identity (Domain 5); an isolated individual is also more dependent on AI-mediated interaction (Domain 6), which deepens the exposure loop.

**Population-scale significance:** this is the domain where individual outcomes become societal outcomes. Belief instability at scale produces election disruption. Identity fragmentation at scale produces family dissolution and fertility decline. The delivery is technical, the impact is cognitive, the outcome is physical change in society and institutions.

---

## 4. Protective Capabilities and Mitigation Catalog

Mitigation ID convention: `M-{threat}{e}` (e = Social), per the taxonomy's operational template.

| M-ID | Capability | Counters | Implementation |
| --- | --- | --- | --- |
| M-S05e | Trust network cultivation | ST-005 | Deliberate maintenance of verified-human trust networks spanning ideological boundaries; resilient local anchors (community nodes) whose signals do not route through algorithmic amplification |
| M-005e | Persona verification discipline | T-CT-005 | Out-of-band verification for consequential requests from trusted figures; treat unverified authority claims as unestablished; synthetic persona recognition training |
| M-008e | Consensus provenance | T-CT-008, TC-06 | Apparent consensus treated as a claim requiring origin evidence; trend origin audits before acting on social signals; grounded reference groups as the check against synthetic proof |
| M-013e | Conformity pressure recognition | T-CT-013 | Awareness of scoring and reputation systems as governance mechanisms; deliberate preservation of behavior domains outside scored systems |
| M-002e | Source diversity practice | ST-005, T-CT-002 | Structured information diet across incompatible outlets and communities; micro-tribe boundary crossings maintained deliberately |
| M-CD6e | Family stability investment | CD-006 | Family continuity treated as a defended asset: protected family time, intergenerational transmission practices, household norms resistant to algorithm-rewarded individualism |
| M-004e | Civic ritual and community engagement | ST-005, HO-004 | Participation in civic structures that build shared identity across tribal lines; service commitments that anchor belonging outside platforms |

---

## 5. Domain Readiness Assessment

Score each capability 0 to 5. Anchors: 0 = absent, 3 = practiced inconsistently, 5 = habitual and verified. Domain Readiness Score = (mean of seven capability scores) x 20.

| Capability | 0 (Absent) | 3 (Inconsistent) | 5 (Sovereign) |
| --- | --- | --- | --- |
| Trust network cultivation | Relationships predominantly platform-mediated | Some verified-human anchors | Maintained verified network spanning ideological lines; local anchors active |
| Persona verification | Trusted-figure requests acted on unverified | Verification for financial requests only | Out-of-band verification habitual for all consequential requests |
| Consensus provenance | Viral consensus accepted as evidence | Skepticism without method | Origin audit before acting on any trend or consensus signal |
| Conformity pressure recognition | Scored systems shape behavior invisibly | Scoring recognized, unmanaged | Scored and unscored behavior domains deliberately mapped and preserved |
| Source diversity | Single-tribe information diet | Occasional boundary crossing | Structured cross-boundary diet, maintained and reviewed |
| Family stability investment | Family time unprotected; transmission unpracticed | Protected time inconsistent | Protected time enforced; transmission practices deliberate and regular |
| Civic engagement | No participation outside platforms | Sporadic participation | Sustained civic commitments anchoring identity across tribal lines |

**Bands:** Sovereign 80-100 | Functional 60-79 | Degraded 40-59 | Compromised below 40. Note that this domain can only be partially self-scored; trust networks and family stability require the counterparty's confirmation to verify. Unit and household assessment beats individual assessment here.

---

## 6. Training Protocols by Population

**Individual warfighter:** Persona verification drilled through red-team exercises: synthetic requests from spoofed trusted figures, scored on verification behavior. Source diversity requirements in intelligence consumption. Resistance to simulated influence operations measured per CSF Table 5.

**Military families:** The priority population for this domain. Family readiness programs carry trust network strengthening, identity anchoring for dependents, and platform literacy for spouses and children. Family channels are trusted channels, which makes them injection targets; the family that verifies is the family that holds.

**Organizations:** Unit cohesion assessed as cognitive defense, not just morale. Synthetic consensus drills: units exposed to manufactured internal "consensus" signals and scored on detection. Command accountability for the unit's social trust posture.

**Civilian society:** Civic ritual strengthening and community organization support as whole-of-society countermeasures to ST-005. Public education on synthetic social proof: the consensus heuristic must be publicly retired as a truth test.

---

## 7. Measurable Outcomes and Failure Conditions

Primary outcome indicator (CSF Table 5): **Ability to Act Against Social Manipulation**: capacity to recognize and resist social pressure campaigns, synthetic consensus, and manufactured outrage, measured through behavioral response testing and red-team influence exercises.

Population-scale measures (Measurement Stack Layer B): B1 Trust and Cohesion Index (institutional trust trends, interpersonal trust surveys, polarization distance) and B2 Civilizational Reproduction Indicators (fertility versus replacement, family stability duration, child wellbeing, intergenerational value transmission confidence). These are continuity risk metrics, not moral judgments; the framework measures whether the structures reproduce, and lets evidence drive interpretation.

**Failure condition:** low cohesion equals high cognitive vulnerability. A population that does not trust its institutions or each other cannot mount coordinated defense against manipulation from any source. If B1 and B2 trend down together while this domain's training exists only at the individual level, the framework is hardening soldiers inside a dissolving society, which is isolation, not resilience.

---

## 8. Enforcement and Crosslinks

- **AI SAFE² CP.11:** UAS-H3 (social pressure simulation) and UAS-H7 (persona and role-boundary erosion) are the procurement-facing measures of this domain in federal AI deployments
- **Measurement Stack:** Layer B1 (Trust and Cohesion Index), B2 (Civilizational Reproduction Indicators); S1 (Synthetic Consensus Scanner) is this domain's machine-scale sensor
- **Taxonomy:** [Substrate Threats](../taxonomy/substrate-threats.md) (ST-005) | [Manipulation Techniques](../taxonomy/manipulation-techniques.md) (T-CT-005, 008, 013) | [Threat Classes](../taxonomy/threat-classes.md) (TC-06) | [Civilizational Drivers](../taxonomy/civilizational-drivers.md) (CD-006)
- **Companion research:** [Research Note 002](../research/002_swarm_threat_scaling.md) covers the swarm mechanics that make synthetic consensus the cheapest commodity in the information environment
- **Adjacent domains:** [Domain 3: Emotional](../03-emotional/README.md) (upstream regulation) | [Domain 5: Purpose & Moral](../05-purpose-moral/README.md) (downstream shared meaning)

> **The domain in one sentence:** societies resist manipulation together or not at all.
