# Declared lenses, shared baseline

The baseline is CSI's U.S. founding-principles profile. An optional lens adds a declared perspective. It cannot silently replace a baseline event record or the CTSS formula.

[Assessment and recommendation](founding-baseline-assessment.md) explains the historical sources, limits, reconstructed perspectives, scores, and implementation proposal.

`profiles.json` contains the baseline and four draft templates. They are data-only reference profiles, not installed app plugins or approved representations of a nation, party, ideology, or religion. Each template requires its user to supply authoritative sources and declare its assumptions before publication.

`examples.json` shows two illustrative lens assessments using real baseline items. The changed assumptions are hypothetical demonstrations; they do not revise the event ledger. Run `python -m tools.lens_check` to calculate baseline and lens scores and verify that the baseline remains intact.

Every output should show the baseline ID/version, lens ID/version, source event, five inputs, baseline score, lens score, changed assumptions, and a rationale. Readers can then disagree with our judgment without losing the common reference point.
