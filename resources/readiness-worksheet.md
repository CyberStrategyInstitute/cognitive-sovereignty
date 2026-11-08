# Test a capability and retain the result

Select a scoped workflow and the relevant [mitigation IDs](mitigation-catalog.md). Keep the six domain results separate. A high threat CTSS means greater assessed severity; a high capability rating means stronger performance on the declared checks. They are not interchangeable and must not be subtracted to invent residual risk.

## Record the assessment

| Field | Record |
|---|---|
| Assessment ID, date, assessor | A unique ID, ISO date, and responsible reviewer |
| Scope and people | The decision, workflow, population, accessibility needs, and exclusions |
| Kind | Observed result or synthetic training example |
| Protocol, case set, catalog revision | Exact versions and a pinned repository commit or catalog hash |
| Capability profile | Inherited domain capabilities or research-extension checks |
| Evidence | A permissible case record, task result, and limits; avoid personal records in this public repository |

| M-ID | Applicable? / reason | Rating 0-5 or unknown | Check and adverse case | Evidence / reason | Repair owner and due date |
|---|---|---|---|---|---|
| | | | | | |

Use 0 for an observed absence or failed capability, not missing evidence. Use 1 for a path that exists but mostly fails, 2 for limited demonstrated performance, 3 for inconsistent performance with important gaps, 4 for demonstrated performance with a remaining noncritical gap, and 5 for the full declared case set including an adverse case. The catalog supplies the control-specific check. A 5 requires retained evidence of the adverse-case pass.

Non-applicable and untested items remain outside a completed score until a separately named tailored profile defines its denominator. Do not silently drop an inconvenient item. Report rated/declared counts even when a total is unknown.

## Calculate and compare

The inherited six-domain capability counts remain 6, 8, 6, 7, 8, and 9. The research extension has two checks per domain. Report these as separate profiles. When all declared checks in a profile have evidence-backed ratings, its score is `sum of ratings / (5 * number of checks) * 100`. Otherwise its score is unknown, with the number rated still visible. The inherited domain interpretation bands remain proposed training guidance, not validated fitness thresholds.

The [worked example](../examples/unit_readiness_assessment.md) supplies a [JSON record](../examples/unit-readiness.json) and fictional fixtures. Run `python -m tools.readiness examples/unit-readiness.json` to reproduce it. `python -m tools.readiness` reads the observed assessment collection, which starts empty. Synthetic examples never become observed readiness.

Keep the baseline and every later dated result. Compare only matching scope, population, accessibility arrangements, protocol, case set, profile, and catalog revision. A changed tool version may be the variable being studied; record it. Adding controls, changing a case set, or using a different profile starts a new comparison. Investigate failures before making a deployment decision or a claim about people.

## Act on the evidence

Record the failed case, responsible owner, due date, and retest. Preserve unresolved gaps in the [decision record](decision-record.md). A failed test can trigger remediation without diagnosing a person or declaring that every other domain has failed. Reassess after the repair using the same cases and retain contrary results.

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](README.md) · [Research](../research/README.md) · [Data catalog](../docs/data/catalog.json) · [Section index](README.md)
<!-- csf-return-navigation:end -->
