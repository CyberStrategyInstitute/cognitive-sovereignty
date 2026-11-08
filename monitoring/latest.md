# CSF evidence report

Report date: 2026-11-07. Local draft for review.

The main historical baseline is now the [complete weekly intake](../research/intake/reports/baseline.md): 87 scored item records from 92 appearances across seven supplied intake weeks. This technical report also retains the separate six-scenario exercise; its aggregate is not the event baseline.

## What we checked

- Repository: 18 reference technique scores checked; 0 registry errors.
- Selected research-note register: 7 source records, representing 7 source lineages. The larger event ledger retains all supplied item sources and analysis.
- Local observations: 0 measurement records.
- Synthetic examples excluded from real results: 0.

## Measured changes

No local model or human-outcome measurements yet. Directly measured human-outcome drift and control effectiveness are unknown. The CSF assessment section below provides our separately labeled severity judgments.

## What happens next

A drop of 10 percentage points or more requests human review. It does not establish harm or statistical significance. Check sample size, changed model versions, collection errors, and task conditions before explaining a change. Publish only after source, privacy, and wording review.

Research intake is manual in this first version. No live feeds, model tests, or human studies run through this command. CTSS totals and aggregates are calculated automatically from the dated assessment inputs. Research intake and input judgments are analyst work in this version.

## CSF U.S.-focused threat assessments

These are CSI assessments using CTSS. Sources establish the evidence; CSI owns the interpretation, estimates, and resulting scores. They are not claims that the studies measured CTSS or national harm.

Current assessed sample: 6 scenarios. Mean CTSS: 53.2/100. 0 critical; 0 high; 0 elevated; 6 moderate.

This mean describes the selected assessed scenarios, not U.S. population risk. The sample is research-led and is not a representative incident sample. Helpful factual-correction evidence is included in the reasoning, not counted as another threat event.

| Scenario | Assessment date | CTSS | Priority |
|---|---|---|---|
| Hidden commercial goals targeting vulnerable customers | 2026-11-07 | 59 | moderate |
| Hidden upstream influence in agent chains | 2026-11-07 | 59 | moderate |
| Expert deferral to AI preferences | 2026-11-07 | 51 | moderate |
| Repeated reports mistaken for independent corroboration | 2026-11-07 | 51 | moderate |
| Material evidence lost before review | 2026-11-07 | 51 | moderate |
| Double-counting shared human-AI evidence | 2026-11-07 | 48 | moderate |

### Change over time

| Edition date | Scenarios with an assessment by that date | Mean CTSS |
|---|---|---|
| 2026-11-07 | 6 | 53.2 |

First assessment edition. No temporal severity trend is established yet. Future revisions preserve these scores and their reasons.

### US-002-2026-11-07: Hidden commercial goals targeting vulnerable customers

CTSS 59/100. Assessed 2026-11-07. Basis: CSF analyst assessment of a U.S. scenario, informed by published research. Confidence: Moderate for the bounded mechanism; low for U.S. occurrence, reach, and recovery estimates.

U.S. relevance: U.S. customers receiving financial or other consequential advice from commercially operated assistants.

An undisclosed operator goal can turn a vulnerability disclosure into a steering opportunity. We assess greater potential agency impact than ordinary advice because the conflict is hidden and personally targeted. Accurate factual correction remains a distinct, potentially beneficial use.

| Input | Score | Why |
|---|---|---|
| L | 1 | 1: published controlled research establishes the mechanism, but these sources do not establish regular operational deployment in the assessed U.S. setting. |
| Ia | 4 | 4: successful exploitation could redirect consequential choices across financial and emotional interests; this is assessed potential impact, not measured customer harm. |
| R | 3 | 3: national-scale potential in U.S. use is the scenario boundary, not a measured count of exposed people. |
| D | 4 | 4: an output-only reviewer may not know the operator goal; the source reports limits in detecting hidden goal-pushing. |
| RecD | 3 | 3: a consequential commitment may require sustained remediation; the paper did not measure recovery. |

Action: Disclose objectives and conflicts; compare matched vulnerability scenarios before using the advisory flow.

Limits: Research-led assessment, not an observed U.S. incident rate. Some source tasks and populations are outside the U.S. Evidence transfer and maximum reach are explicit scenario assumptions. The inputs can be challenged individually.

Sources: [R-002: The Customer Never Sees the Goal](https://arxiv.org/abs/2611.02689v1), [R-003: Just the Facts](https://arxiv.org/abs/2611.05572v1).

### US-005-2026-11-07: Hidden upstream influence in agent chains

CTSS 59/100. Assessed 2026-11-07. Basis: CSF analyst assessment of a U.S. scenario, informed by published research. Confidence: Moderate for the bounded mechanism; low for U.S. occurrence, reach, and recovery estimates.

U.S. relevance: U.S. organizations using agent chains to review public commentary or prepare consequential recommendations.

A final explanation may omit the claims that influenced an upstream agent. We assess a higher potential impact when that recommendation controls a downstream decision. The source also shows partial re-anchoring, so chain influence is not inevitable.

| Input | Score | Why |
|---|---|---|
| L | 1 | 1: published controlled research establishes the mechanism, but these sources do not establish regular operational deployment in the assessed U.S. setting. |
| Ia | 4 | 4: a trusted downstream recommendation could redirect several linked decisions; this is a potential scenario, not a measured U.S. campaign effect. |
| R | 3 | 3: national-scale potential in U.S. use is the scenario boundary, not a measured count of exposed people. |
| D | 4 | 4: the relevant influence often did not appear in the final explanation in the reported experiment. |
| RecD | 3 | 3: tracing and correcting distributed decisions may require sustained work; recovery was not measured. |

Action: Record source exposure and compare recommendations with and without the upstream influence. Reproduce on a U.S.-relevant case set.

Limits: Research-led assessment, not an observed U.S. incident rate. Some source tasks and populations are outside the U.S. Evidence transfer and maximum reach are explicit scenario assumptions. The inputs can be challenged individually.

Sources: [R-006: Upstream Influence, Downstream Re-Anchoring in LLM Agent Chains](https://arxiv.org/abs/2610.17723v1), [R-005: Provenance-Aware Belief Updating in Human-AI Feedback Loops](https://arxiv.org/abs/2610.13008v2).

### US-001-2026-11-07: Expert deferral to AI preferences

CTSS 51/100. Assessed 2026-11-07. Basis: CSF analyst assessment of a U.S. scenario, informed by published research. Confidence: Moderate for the bounded mechanism; low for U.S. occurrence, reach, and recovery estimates.

U.S. relevance: U.S. public-sector and commercial analysts who use AI for consequential analytical choices.

AI advice can select the criteria behind a decision before a nominal human approval. We assess a material risk of reasoning being redirected; agreement by itself is not evidence of harm.

| Input | Score | Why |
|---|---|---|
| L | 1 | 1: published controlled research establishes the mechanism, but these sources do not establish regular operational deployment in the assessed U.S. setting. |
| Ia | 3 | 3: a successful influence on analytical criteria can materially redirect a decision; lasting capability loss was not established. |
| R | 3 | 3: national-scale potential in U.S. use is the scenario boundary, not a measured count of exposed people. |
| D | 4 | 4: detecting which defensible preference came from the agent requires an independent comparison and decision history. |
| RecD | 2 | 2: a recorded decision can often be reconsidered over days or weeks; this recovery estimate has not been tested. |

Action: Record criteria before advice and review whether final agreement or disagreement was justified.

Limits: Research-led assessment, not an observed U.S. incident rate. Some source tasks and populations are outside the U.S. Evidence transfer and maximum reach are explicit scenario assumptions. The inputs can be challenged individually.

Sources: [R-001: How AI agents shape experts’ judgment calls](https://www.anthropic.com/research/agents-judgment-calls), [R-004: AI-Assisted Classification under Correlation Neglect and Trust](https://arxiv.org/abs/2611.05870v1).

### US-004-2026-11-07: Repeated reports mistaken for independent corroboration

CTSS 51/100. Assessed 2026-11-07. Basis: CSF analyst assessment of a U.S. scenario, informed by published research. Confidence: Moderate for the bounded mechanism; low for U.S. occurrence, reach, and recovery estimates.

U.S. relevance: U.S. research, intelligence, and business workflows that relay evidence through multiple summaries.

Repeated summaries can inflate apparent support without adding an observation. We assess this as a distinct evidence-handling failure within the existing taxonomy. A provenance-aware result shows the mechanism may be mitigated.

| Input | Score | Why |
|---|---|---|
| L | 1 | 1: published controlled research establishes the mechanism, but these sources do not establish regular operational deployment in the assessed U.S. setting. |
| Ia | 3 | 3: inflated confidence can materially alter decisions; the source does not establish durable human impairment. |
| R | 3 | 3: national-scale potential in U.S. use is the scenario boundary, not a measured count of exposed people. |
| D | 4 | 4: the origin can disappear across multiple relays unless lineage is explicitly retained. |
| RecD | 2 | 2: deduplicating the source can support correction; actual recovery burden was not measured. |

Action: Preserve lineage across handoffs and collapse derivative reports into one evidence origin.

Limits: Research-led assessment, not an observed U.S. incident rate. Some source tasks and populations are outside the U.S. Evidence transfer and maximum reach are explicit scenario assumptions. The inputs can be challenged individually.

Sources: [R-005: Provenance-Aware Belief Updating in Human-AI Feedback Loops](https://arxiv.org/abs/2610.13008v2).

### US-006-2026-11-07: Material evidence lost before review

CTSS 51/100. Assessed 2026-11-07. Basis: CSF analyst assessment of a U.S. scenario, informed by published research. Confidence: Moderate for the bounded mechanism; low for U.S. occurrence, reach, and recovery estimates.

U.S. relevance: U.S. AI-assisted reviews relying on long tool results, structured records, or summarized evidence.

A reviewer may approve a recommendation without knowing that material evidence was cut. We assess the human decision risk by inference from the documented machine evidence-delivery failure; the causal accuracy question remains open.

| Input | Score | Why |
|---|---|---|
| L | 1 | 1: published controlled research establishes the mechanism, but these sources do not establish regular operational deployment in the assessed U.S. setting. |
| Ia | 3 | 3: missing material could change a consequential judgment; the study did not measure a human outcome. |
| R | 3 | 3: national-scale potential in U.S. use is the scenario boundary, not a measured count of exposed people. |
| D | 4 | 4: a reviewer cannot inspect an omission that the interface does not disclose; delivery logging is needed. |
| RecD | 2 | 2: retrieval and renewed review can often correct the omission; timing and downstream costs depend on the workflow. |

Action: Expose truncation and access failures, recover material evidence, and repeat the affected review.

Limits: Research-led assessment, not an observed U.S. incident rate. Some source tasks and populations are outside the U.S. Evidence transfer and maximum reach are explicit scenario assumptions. The inputs can be challenged individually.

Sources: [R-007: Context Is a Pipeline, Not a Window](https://arxiv.org/abs/2610.36114v1).

### US-003-2026-11-07: Double-counting shared human-AI evidence

CTSS 48/100. Assessed 2026-11-07. Basis: CSF analyst assessment of a U.S. scenario, informed by published research. Confidence: Moderate for the bounded mechanism; low for U.S. occurrence, reach, and recovery estimates.

U.S. relevance: U.S. teams treating AI advice and human research as separate confirmation when they share sources.

The same evidence can receive more weight than it deserves. The risk is poor calibration, not simply excessive trust. Assistance also improved accuracy in the studied task, so reducing reliance indiscriminately could worsen decisions.

| Input | Score | Why |
|---|---|---|
| L | 1 | 1: published controlled research establishes the mechanism, but these sources do not establish regular operational deployment in the assessed U.S. setting. |
| Ia | 3 | 3: misplaced corroboration can materially redirect a decision; population-level capability effects remain unmeasured. |
| R | 3 | 3: national-scale potential in U.S. use is the scenario boundary, not a measured count of exposed people. |
| D | 3 | 3: detecting overlap requires source comparison and a suitable record, but the overlap can be inspected. |
| RecD | 2 | 2: correction is feasible once the shared source is identified; the recovery time is an analytical estimate. |

Action: Group claims by originating observation and test both appropriate acceptance and appropriate rejection.

Limits: Research-led assessment, not an observed U.S. incident rate. Some source tasks and populations are outside the U.S. Evidence transfer and maximum reach are explicit scenario assumptions. The inputs can be challenged individually.

Sources: [R-004: AI-Assisted Classification under Correlation Neglect and Trust](https://arxiv.org/abs/2611.05870v1), [R-005: Provenance-Aware Belief Updating in Human-AI Feedback Loops](https://arxiv.org/abs/2610.13008v2).

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](../resources/README.md) · [Research](../research/README.md) · [Data catalog](../docs/data/catalog.json) · [Section index](README.md)
<!-- csf-return-navigation:end -->
