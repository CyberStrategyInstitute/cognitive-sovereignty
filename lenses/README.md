<!-- csf-module-header:start -->
![LENS: Baseline and perspectives. CSF 3.0.0. Status is repeated in text below.](../assets/headers/lenses.svg)

CSF 3.0.0. Documentation: NEW in 3.0. Published documentation; lens profiles remain draft/templates.

[![Framework 3.0.0](../assets/badges/version.svg)](../VERSION) [![Documentation license: CC BY-SA 4.0](../assets/badges/docs-license.svg)](../LICENSE)
<!-- csf-module-header:end -->

# Declared lenses, shared baseline

The baseline is CSI's U.S. founding-principles profile. An optional lens adds a declared perspective. It cannot silently replace a baseline event record or the CTSS formula.

[Assessment and recommendation](founding-baseline-assessment.md) explains the historical sources, limits, reconstructed perspectives, scores, and implementation proposal.

`profiles.json` contains the baseline and four draft templates. They are data-only reference profiles, not installed app plugins or approved representations of a nation, party, ideology, or religion. Each template requires its user to supply authoritative sources and declare its assumptions before publication.

`examples.json` shows two illustrative lens assessments using real baseline items. The changed assumptions are hypothetical demonstrations; they do not revise the event ledger. Run `python -m tools.lens_check` to calculate baseline and lens scores and verify that the baseline remains intact.

Every output should show the baseline ID/version, lens ID/version, source event, five inputs, baseline score, lens score, changed assumptions, and a rationale. Readers can then disagree with our judgment without losing the common reference point.

<!-- csf-section-files:start -->
## Section files

- [example-results.json](example-results.json)
- [examples.json](examples.json)
- [founding-baseline-assessment.md](founding-baseline-assessment.md)
- [profiles.json](profiles.json)
<!-- csf-section-files:end -->

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](../resources/README.md) · [Research](../research/README.md) · [Data catalog](../docs/data/catalog.json)
<!-- csf-return-navigation:end -->
