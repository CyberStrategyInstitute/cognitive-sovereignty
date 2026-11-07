# 010: Put research into domain controls

The first research PR preserved the intake and added shared safeguards. It did not fully update the six domain catalogs. This revision closes that implementation gap: 44 inherited mitigation IDs remain, 20 controls are refined, and 12 are added. The core domains, causal layers, threat IDs, CTSS inputs, and weights remain unchanged.

## What changes by domain

| Domain | Inherited controls | Refined | Added | New practical outcome |
|---|---:|---:|---:|---|
| Biological | 6 | 2 | 2 | A pause/handoff path and limits on sensitive-state targeting |
| Cognitive | 8 | 5 | 2 | Visible evidence omissions and a trace from influence capability to observed outcome |
| Emotional | 6 | 3 | 2 | Understandable relationship limits, usable exit, and checks for vulnerability exploitation |
| Social | 7 | 2 | 2 | Authorized synthetic testimony and correction across known copies |
| Purpose & Moral | 8 | 3 | 2 | Visible advice objectives and a way to challenge CSI’s own scores |
| Digital & AI Symbiosis | 9 | 5 | 2 | Specific authorization and tested memory, bystander-consent, and exit paths |

Refined counts are a subset of inherited controls. The catalog grows from 44 to 56, not to 76. Each domain adds two exposure mechanisms mapped to existing taxonomy IDs. This is an expanded assessment surface, not a measured increase in real-world threat frequency or an automatic CTSS increase.

## Research and limits

[006: independent judgment](006_independent_judgment.md) supports evaluating justified acceptance and rejection, task comprehension, and retained capability. [007: evidence lineage](007_evidence_lineage.md) supports grouping derivative reports and making missing material visible. [008: objectives and persuasion](008_operator_objectives_and_persuasion.md) supports checking operator goals, conflicts, vulnerability targeting, and specific authorization. [009: relationships and exit](009_relational_influence.md) supplies a bounded research plan for roles, memory, outside support, and exit. Those notes retain primary-source links, study populations where known, and review limits. The [full intake](intake/events.json) preserves the wider source analysis and contrary findings.

These findings have different strengths. The analyst study concerns expert choice under experimentally strengthened preferences. Several lineage and persuasion findings concern model outputs or synthetic tasks. Relational findings require further primary-source review. The Biological additions are operational inferences about review conditions and sensitive data, not evidence that these studies measured sleep disruption, neural injury, or clinical benefit. No participant study or clinical protocol is introduced here.

The source-backed reason for each added or refined control is stored with its M-ID in [the catalog](../resources/mitigation-catalog.md). Inherited controls retain their historical text unless specifically refined. A reference to this synthesis documents the design rationale; it does not retroactively validate an inherited claim.

## Benefits, costs, and decision

The benefit is a complete path from research to domain, control, check, failed case, and remediation. Keeping stable IDs lets units reuse prior evidence. The cost is a larger catalog and more review work. Apply controls to the declared workflow and record non-applicability with a reason; do not demand every control for every routine task.

Adding two new items to an old readiness average would change its denominator and could make an unchanged unit appear worse. Keep the original capability profile and the new research-extension profile separate. A missing rating stays unknown; report rated checks out of declared checks. Use the same case set, protocol, profile, and catalog revision for a trend. No observed unit data is supplied, so none of the six domains has an evidenced readiness increase.

The 20 refined controls also have clearer readiness anchors. Their previous implementation wording and anchors are retained in the JSON catalog. The inherited capability counts and mean-times-20 calculation stay intact. Because the criteria are refined, start a new comparison at the revised catalog version rather than silently comparing it with an older score.

Adopt the documented controls for review, run the [worked example](../examples/unit_readiness_assessment.md), and gather task-specific results with the [worksheet](../resources/readiness-worksheet.md). Revise a control when its benefit, burden, failure cases, or contrary evidence justify a change. Do not increase a threat score or claim better human protection merely because the catalog grew.
