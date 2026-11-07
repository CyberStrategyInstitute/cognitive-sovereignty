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
