# Framework Evolution

The Cognitive Sovereignty Framework is versioned. This document separates inherited history from current implementation and the remaining roadmap. Historical coverage estimates and architectural guarantee language below do not establish measured protection. See the current registry and implementation evidence.

---

## v2.0 — February 2026
**Focus:** Complete AI-Era Architecture

### Major Additions
- **Domain 6: Digital & AI Symbiosis** — The missing pillar across all DoD resilience frameworks. Addresses the human-AI interface and the specific vulnerabilities that emerge when humans operate within human-AI systems.
- **EFA Integration** — Ethical Functionality without Agency paradigm integrated as technical enforcement architecture for Domain 6. Domain 6 is now backed by both human training and structural technical guarantees.
- **E7 Protocol Stack** — EFA/AI-SAFE² 7-Layer Protocol Stack integrated as the architectural reference ensuring human authority at Layer 7.
- **HEAR Doctrine** — Human Ethical Agent of Record accountability requirement formalized and linked to CSF Domain 6 assessment.
- **Ring of Fire (RoF)** — Multi-model oversight architecture added as Domain 6 technical enforcement mechanism.
- **ST-006: Guardrail Alignment Drift** — Added following analysis of LLM guardrail behaviors. Captures risk that AI alignment mechanisms themselves become instruments of ideological control.
- **ST-007: Model Performance Drift** — Added following analysis of model drift patterns. Captures gradual AI degradation that erodes user cognitive capacity without triggering awareness.
- **T-CT-017: Guardrail Bias Exploitation** — Added as active technique distinct from narrative capture; operates through the tools people use to access information.
- **T-CT-018: Repetition and Normalization Manipulation** — Added; detectable through n-gram spike analysis and linguistic pattern monitoring.
- **CD-005: Computational Acceleration Misalignment** — Added following wargame analysis showing speed mismatch between AI evolution and human governance.
- **CD-006: Civilizational Reproduction Failure** — Added following wargame scenarios where family dissolution and intergenerational value transmission failure produced civilizational collapse outcomes no amount of technical defense could prevent.
- **10 Newly Identified Threat Classes (TC-01 through TC-10)** — Capturing the estimated 20–30% of modern cognitive influence previously unattributed; operating through incentive structures, environmental conditioning, and voluntary adoption.
- **3 Edge Domain Additions (E1–E3)** — Autonomous Swarm Reality Formation, Synthetic Consensus Economies, Civilizational Reproduction Failure.
- **Three-Layer Measurement Stack** — Technical telemetry (Layer A), societal stability metrics (Layer B), and civilizational trajectory analysis (Layer C).
- **Swarm Detection Module (S1–S3)** — Dedicated detection capabilities addressing ecosystem-scale autonomous manipulation.
- **Command Center** — Interactive HTML5 visualization dashboard with JSON-driven threat registry.

### Coverage Change
v1.0 → v2.0: ~80% → 92% overall coverage

---

## v1.0 — Initial Release
**Focus:** Foundation

- Six-domain model proposal
- Initial CTSS scoring baseline (Likelihood, Impact on Agency, Population Reach)
- 18 technique families (T-CT-001 through T-CT-016)
- Four-layer threat architecture (Civilizational Drivers, Manipulation Techniques, Delivery Scale, Human Outcomes)
- Mapping against existing DoD resilience frameworks (CAF, CSF2, OSC, Total Fitness, Guardian Resilience)
- Information Operations doctrine lineage established
- DoD AI Ethical Principles alignment documented

---

## Roadmap status, reviewed November 7, 2026

The work advances the research foundation and unit-scorecard prototype. It does not complete every v2.1 milestone. Targets are version labels, not dated commitments, so calendar progress cannot be assessed from this roadmap alone. Framework metadata currently says v2.1.0; that label is not evidence that all v2.1 roadmap items shipped.

| Priority | Planned addition | Original target | Current state | Evidence and next step |
|---|---|---|---|---|
| High | Neuro-swarm integration techniques | v2.1 | Research open | [The taxonomy and Biological controls identify the intersection; no distinct validated technique or protocol is delivered.](research/010_domain_controls_and_readiness.md) Retain as research until a distinct mechanism, primary evidence, and test justify an entry. |
| High | Quantum acceleration threat class | v2.1 | Research open | [A watch item exists; no evidence-backed distinct threat class is implemented.](taxonomy/civilizational-drivers.md) Review whether quantum capabilities add a distinct mechanism beyond CD-005 before adding a class. |
| Medium | Individual-level CTSS assessment tool | v2.1 | Partial | [The calculator and item-level CTSS records work. Individual exposure profiling and calibration are not delivered.](examples/ctss_calculator.py) Specify a personal exposure workflow while keeping threat severity separate from personal capability. |
| Medium | Unit-level cognitive readiness scorecard | v2.2 | Prototype delivered | [Six-domain control catalog, worksheet, evidenced-rating tool, and reproducible fictional example exist. Observed unit validation is absent.](examples/unit_readiness_assessment.md) Run the same bounded cases in an authorized unit workflow and retain failures, burden, and reassessment. |
| Low | Legislative response integration | v2.2 | Partial | [The U.S. founding-principles lens and UAS crosswalk are documented; no comprehensive current-law response catalog exists.](lenses/founding-baseline-assessment.md) Define jurisdiction, applicable authorities, effective dates, and a legal-review owner. |
| Low | Defense industrial base application guide | v2.3 | Planned | [The crosswalk and unit example are reusable inputs; a dedicated DIB application guide is absent.](06-digital-ai-symbiosis/federal-procurement-alignment.md) Scope one supplier workflow and its evidence needs before writing a sector guide. |

## Research-to-control update in the current PR

- Keep the six domains, five causal layers, taxonomy IDs, and CTSS weights.
- Preserve 44 inherited mitigation IDs, refine 20 controls, and add 12 research-linked controls, two per domain.
- Expand domain exposure mappings and capability checks without claiming increased incidence or demonstrated readiness.
- Provide a shared catalog, resources workflow, worked unit example, and agent-readable data.
- Update the Learning Hub, Threat Explorer, Command Center, and README to connect the model with research, controls, and assessment.

[Detailed change assessment](research/010_domain_controls_and_readiness.md) | [Implementation record](IMPLEMENTATION.md) | [Machine-readable roadmap](monitoring/roadmap.json)

Next owner priorities: review the controls and their burden, select a bounded unit workflow, and decide whether the two high-priority research items remain release requirements. Do not silently mark them complete to match a version label.
