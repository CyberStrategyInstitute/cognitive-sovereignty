# Weekly intake: keep every relevant item

The unit of intake is one event, news item, report, study, or distinct insight. Each item retains its evidence and its own assessment. A short editorial brief can select highlights; the research ledger keeps the rest.

## Start here

- [Full baseline and weekly trends](reports/baseline.md).
- [Individual scores for all items](event-scores.csv).
- [Complete event records and original analysis](events.json).
- [Watch and action signals](signals.json).
- [Source inventory, hashes, and gaps](manifest.json).

The imported collection contains three Word editions/compilations, their available Markdown editions, and supporting records. The local archive preserves all 16 originals byte for byte. Raw Word paragraph text, links, and auxiliary text parts are retained here. Originals were not modified. Personal local paths are excluded from the public-facing manifest.

## The record for one item

Keep a stable ID, occurrence date if known, publication date if known, intake week, assessment date, original source and version, original analysis, evidence type, affected domains and taxonomy IDs, U.S. relevance, evidence role, five CTSS inputs, reasons, score status, action, and research trigger. Event time, publication time, intake time, and assessment time are different fields. Do not guess a missing event date from a headline.

An item may be threat evidence, protective evidence, counterevidence, mixed, or context. Its CTSS describes the human-agency risk being assessed. Its role explains whether the development exposes, reduces, challenges, or frames that risk. A standard announcing safeguards is not automatically evidence that protection works. A helpful study is not relabeled as a harmful event.

The current backfill uses the supplied analysis as evidence. Scores are new CSI provisional judgments dated November 7, 2026. They are not invented historical scores. Each source's original score wording remains intact. No item was excluded for lacking a high headline impact.

## Raw information to an assessment

1. **Capture:** retain the source, text, date, and link before drafting. Save even a minor or inconclusive scoped item. Identify whether it repeats an existing event, adds evidence, or describes a new event.
2. **Analyze:** identify the mechanism, affected person or institution, U.S. relevance, domains, and existing taxonomy IDs. Explain what changed and why it affects CSF. Include useful counterevidence.
3. **Score:** assign all five estimates with reasons. A preliminary estimate can use declared assumptions. Unknown facts do not become measured values. Set status to provisional and name what research could change the score.
4. **Validate:** the tool applies the unchanged CTSS formula, checks records, and generates individual and weekly results. Preserve prior revisions instead of replacing them.
5. **Review and publish:** prioritize high impact, weak evidence, disputed claims, and sharp score changes for review. Publish scoped analysis and provisional scores with their labels. Retain lower-scoring items in the ledger and trend tables.

The analysis step can be performed by a configured research assistant using [the weekly instruction](../../monitoring/weekly-intake-prompt.md). Arithmetic and validation are deterministic. A generic keyword count cannot substitute for interpreting evidence and explaining a score.

```
python -m tools.event_monitor check
python -m tools.event_monitor build
```

The machine-readable [item template](event-template.json) is a technical reference for the research assistant. After analysis supplies the reasons and preliminary inputs, `python -m tools.event_monitor ingest --input scored-items.json` adds a list of new records and builds the scores and reports. Existing IDs are rejected so new intake cannot silently replace history. Repeated coverage can link a new appearance to an existing story. The raw-to-analysis step is performed by the research assistant; this tool validates and calculates its result.

To revise an existing assessment, supply its new date, five inputs, input reasons, revision reason, and new evidence or documented correction in a JSON file. Run `python -m tools.event_monitor revise --id EVENT_ID --input revision.json`. The tool preserves the old assessment before building the new reports. The one-time backfill script refuses replacement by default.

## Make slow changes visible

Keep two histories: changes to the same event or threat series, and changes in the mix of new weekly items. Report item count, evidence role, provisional count, score distribution, and theme recurrence. Preserve quiet weeks, missing weeks, and low scores. A missing collection is a gap, not a score of zero.

The first reports show intake-cohort trends. They do not claim that a moving weekly average proves the same threat worsened. Event revisions require a revision ID, previous ID, effective date, changed inputs, new evidence, and reason. A live fixed-cohort threat index should be a separate declared series using the existing taxonomy, with its own inclusion and update rules. Do not merge the earlier six broad scenarios into the historical event ledger.

Flag a theme recurring in three consecutive available weekly collections for a research check, even if no item is high severity. A missed collection breaks the continuity claim. Use monthly review to test whether repeated small observations change the assessed mechanism, likelihood, reach, or recovery. This trigger starts research; it does not add a hidden score multiplier.

## What is still missing

The original Top 12 selection cannot reveal minor items that were never collected. Future collection needs a declared watchlist covering U.S. government and courts, provider incident disclosures, relevant research, election and public-information integrity, education, commercial delegation, privacy, and human-agency outcomes. Retain non-U.S. developments when their U.S. implications are explained. Source reports, allegations, studies, and direct observations remain distinguishable.

No October 16-23 ranked edition was found. The user clarified that scoring images belong to another research folder and withdrew that recovery request. The supplied scorecard ZIP is a separate template. The 217 watch/action signals are preserved as research leads, not fabricated incidents. They enter the scored event ledger when tied to a specific source or assessed scenario. The initial scoring is ready for review; underlying sources are not all newly reverified.
