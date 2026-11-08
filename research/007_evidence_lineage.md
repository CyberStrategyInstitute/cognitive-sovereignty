<!-- csf-research-status:start -->
**NEW in 3.0.** Research note 007. Published as documentation in CSF 3.0.0; proposal, source-review, and validation limits below remain in force.
<!-- csf-research-status:end -->

# 007: Three summaries can still be one source

CSF links: ST-001, T-CT-006, T-CT-008. Domains 2 and 6. Status: proposed safeguard informed by bounded model experiments.

## What we learned

Huang and colleagues test whether models count repeated reports as new evidence. In a controlled benchmark, provenance-aware training reduced repeated-evidence errors. The results depend on supplied lineage information and tested model families. [Preprint v2](https://arxiv.org/abs/2610.13008v2).

Hsu and colleagues find that source access and handoff format affect influence in agent chains. Some downstream influence faded when agents could re-anchor on evidence. Repeated exposure preserved more influence; the injected claims often did not appear in explanations. This limits what a final-answer audit alone can show. [Preprint v1](https://arxiv.org/abs/2610.17723v1).

Sehgal and colleagues report lost tool output in an agent pipeline, even with spare context capacity. Their study finds additional work after truncation, while the causal link to accuracy loss remains unresolved. This is a machine evidence-delivery finding, with possible downstream human consequences. [Preprint v1](https://arxiv.org/abs/2610.36114v1).

## What changes

Record the original observation behind each claim. Group derivative reports together. Show inaccessible, omitted, or truncated evidence. Different model names do not establish independent corroboration. A source receipt records what was supplied; it does not prove truth, comprehension, or absence of hidden influence.

## Small test and decision

Give a reviewer three summaries of one observation and a separate conflicting observation. A sound evidence record identifies two underlying lineages and preserves the conflict. Remove a material page and verify that the omission is visible before approval. Use [the decision record](../resources/decision-record.md). Cross-checking should add independent evidence or make uncertainty clearer.

## Apply this note through controls

[M-007c: Source verification habit](../resources/mitigation-catalog.md#m-007c), [M-S07c: Output quality baselining](../resources/mitigation-catalog.md#m-s07c), [M-005e: Persona verification discipline](../resources/mitigation-catalog.md#m-005e), [M-008e: Consensus provenance](../resources/mitigation-catalog.md#m-008e), [M-004g: Provenance verification](../resources/mitigation-catalog.md#m-004g), [M-S06g: Multi-model triangulation (Ring of Fire)](../resources/mitigation-catalog.md#m-s06g), [M-S07g: Drift telemetry and baselining](../resources/mitigation-catalog.md#m-s07g), [M-016g: Synthetic media detection](../resources/mitigation-catalog.md#m-016g), [M-007c2: Evidence completeness check](../resources/mitigation-catalog.md#m-007c2), [M-008c: Trace influence to an outcome](../resources/mitigation-catalog.md#m-008c), [M-005e2: Consent for synthetic testimony](../resources/mitigation-catalog.md#m-005e2), [M-008e2: Correction across copies](../resources/mitigation-catalog.md#m-008e2), [M-HO5f2: Challenge and correct a score](../resources/mitigation-catalog.md#m-ho5f2).

Use [the readiness worksheet](../resources/readiness-worksheet.md) to retain results. These mappings are documented design decisions, not evidence of field effectiveness.

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](../resources/README.md) · [Research](README.md) · [Data catalog](../docs/data/catalog.json) · [Section index](README.md)
<!-- csf-return-navigation:end -->
