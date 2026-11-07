# Make CSF easier to use and test

Local implementation started November 7, 2026. The six domains, five causal layers, existing threat IDs, and CTSS formula stay intact.

Expanded after source review: the primary baseline now contains 87 individually assessed intake items from 92 appearances in seven weekly collections, plus 217 preserved watch/action signals. One repeated UNESCO source links two items to the same story, yielding 86 source-linked story threads. All 16 supplied files are archived locally without modification. See [the full baseline](research/intake/reports/baseline.md) and [the founding-principles lens assessment](lenses/founding-baseline-assessment.md). The earlier six scenarios and their 53.2 mean remain a separate exercise, excluded from event trends.

## Working instruction

Improve the evidence and practical guidance supporting the Cognitive Sovereignty Framework. Use plain language. Start each addition with the problem, the action, and the outcome. Put technical detail beneath that explanation only when needed to reproduce a result.

Preserve useful research for future decisions. For each source, record what it found, how it was studied, its limits, the affected CSF entries, and why it changes a decision. Keep reported findings separate from local measurements. Include contrary evidence. Prefer improving existing entries over creating new categories.

Repair arithmetic and documentation errors without changing the core model. Give each proposed safeguard a clear owner, a small test, an expected result, and a response when it fails. Use the smallest set of files and tools that can do the job.

Use CSF as the source of record for U.S.-focused analysis and CTSS assessments. Score individual developments and scenarios, explain each input, preserve dated revisions, and publish aggregate trends alongside the underlying assessments. Use incomplete evidence where analysis supports a judgment, clearly stating assumptions and uncertainty. Direct experiments are an additional validation path, not a prerequisite for assessment or publication.

Build repeatable checks that count observable results. Compare like with like. Missing data stays unknown. Preserve the baseline and the evidence behind each change. Prepare readable draft reports; keep external publication and release under owner control. Never present a synthetic exercise, researcher-reported result, or documentation check as measured human protection.

## Delivered in this branch

| Work | Why | Outcome |
|---|---|---|
| Correct stored CTSS arithmetic | Different totals produced misleading rankings | Existing inputs give the same answer in the calculator and dashboards |
| Keep a small research register | Briefing insights were difficult to reuse | Sources link to findings, limits, and decisions |
| Add practical safeguards | Training guidance needed clearer tests | Six safeguards have plain-language checks and failure responses |
| Add an offline reporting tool | Publishing needs traceable results | Counts, missing evidence, and comparable changes are visible |
| Add automatic repository checks | Future edits could reintroduce inconsistencies | Invalid inputs and stale generated files fail the check |

## Next decisions

Scope clarified November 7: CSF is the source of record for its own U.S.-focused assessments. The first edition now includes six scored scenarios, individual input rationales, a sample aggregate, and revision comparison. Experiments support validation but are not a gate on issuing an analytical judgment. The first sample mean is 53.2; there is no prior assessment edition from which to infer a time trend.

1. Review the pull request before merging or publishing the resulting reports.
2. Continue the U.S.-focused assessment series and prepare its individual scores, aggregate, reasoning, and limits for publication. Alongside it, choose one advisory workflow and a consenting adult pilot group. The workflow owner defines acceptable errors, accessibility needs, and stop conditions before collecting results.
3. Run the same cases before and after a change. Record model versions, evidence, and failures. A small pilot describes that pilot; it cannot establish population-wide protection.
4. Verify the next execution of the existing weekly brief automation. Its CSF intake instructions were updated without changing its schedule. No automatic report publication is enabled.

Start with [practical safeguards](resources/practical-safeguards.md), [research](research/README.md), and [monitoring](monitoring/README.md). The [scoring correction](research/scoring-correction-2026-11-07.md) explains why the rankings changed.

## Verification

Fifty Python tests passed, covering intake retention, original analysis integrity, item scores, role-separated aggregates, recurring signals, missing weeks, dated revisions, baseline preservation, signal closure evidence, bounded queries, export freshness, and rejection of hidden lens weight changes. Seven browser pages and their scripts parse; three reference dashboards use the shared scoring data. All 1,428 local document links and HTML anchors resolve. The optional MCP adapter passed real client/server protocol checks with SDK 1.30.0, including discovery, lookup, pagination, calculation, missing inputs, and rejection of invalid inputs or arbitrary paths. All 16 originals and archive copies matched their recorded hashes.

Rendered desktop/mobile layout remains unverified because the in-app browser could not reach the preview and the local-browser access approval timed out. Shared styling and responsive rules have code checks, which do not establish rendered accessibility or layout. The branch is prepared for an owner-reviewed PR. No merge, release, deployment, participant study, or automatic publication is authorized by this change.

The existing `csi-weekly-briefs-and-catch-up` heartbeat was updated through the app on November 7. It remains active with its previous schedule and target chat. Only a CSF-specific intake/scoring appendix was added; the other brief topics and existing delivery boundaries remain. The update requests the item ledger, CTSS CSV, full research report, lower-salience retention, and explicit baseline/lens handling. Its next successful due run remains to be verified.

## Domain-control and presentation follow-up

The first pass did not fully integrate the shared safeguards into each domain. The follow-up retains 44 mitigation IDs, refines 20 implementations and their readiness anchors, and adds 12 controls. Prior wording and anchors are retained in the catalog. The six domain pages now include research-linked exposure mappings, control rows, and separate readiness-extension checks. The inherited capability counts and calculation stay intact; changed criteria require a new comparison at the revised catalog version.

[Research note 010](research/010_domain_controls_and_readiness.md) records the rationale, benefits, costs, and limits. [Resources](resources/README.md) now form an assessment workflow. The [unit example](examples/unit_readiness_assessment.md) has a reproducible synthetic record and fixtures across all six domains. No observed readiness data is supplied.

The Learning Hub promotes each assessment step and domain control view. The Threat Explorer adds combined search/domain/tier filters, sorting, catalog links, corrected tier counts, and a corrected swarm score panel. Command Center views include the same domain/control entrypoints. All pages share the original shield asset and navigation. README and framework-reference centering is removed. The roadmap now records partial delivery and the still-open neuro-swarm, quantum, individual exposure, legislative, and DIB work without inventing completion dates.

New checks cover inherited denominators, unknown/zero distinctions, evidence-backed ratings, adverse-case requirements, synthetic exclusion, reproducible example scores, catalog version pins, generated domain views, logo hashes, README alignment, and Explorer filtering/sorting. Both core and MCP checks are repeated in the PR workflow. Rendered desktop/mobile review remains unverified after the browser access failures above.
