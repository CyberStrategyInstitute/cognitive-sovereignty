<img src="docs/assets/brand/csi-shield-color.png" width="96" alt="Cyber Strategy Institute shield">

# Cognitive Sovereignty Framework 3.0

CSF helps people and organizations examine whether they retain the ability to understand, choose, challenge, and govern AI-mediated decisions. Cyber Strategy Institute maintains the model, taxonomy, research, and CTSS assessments.

The core remains **six domains, five causal layers, and the existing CTSS formula**. CSF v3.0.0 connects the research intake to domain controls, assessments, tracked actions, and reusable data. The major version identifies the expanded research-to-control workflow and revised readiness criteria.

## Start with your task

| I want to... | Go here |
|---|---|
| Understand the model | [Framework reference](FRAMEWORK.md) and [six domains](#the-six-domains) |
| Read the research and individual scores | [Research hub](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/research.html) or [complete report](research/intake/reports/research-assessment.md) |
| Inspect the weekly baseline | [Seven weekly reports and trends](research/intake/reports/baseline.md), [CSV](research/intake/event-scores.csv), [JSON](research/intake/events.json) |
| Apply controls and assess readiness | [Control catalog](resources/mitigation-catalog.md), [resources workflow](resources/README.md), [worked unit example](examples/unit_readiness_assessment.md) |
| Check the roadmap | [Evidence and remaining milestones](EVOLUTION.md) |
| Find the next action | [Watch/action register](research/intake/signals/README.md) |
| Assess a new item | [Intake method](research/intake/README.md), [scorecard template](resources/scorecard-template.md), [decision record](resources/decision-record.md) |
| Use another declared perspective | [Baseline and lens assessment](lenses/founding-baseline-assessment.md) |
| Use CSF from an agent or MCP server | [Integration guide](integration/README.md), [catalog](docs/data/catalog.json), [schemas](schemas/README.md) |
| See what changed and remains open | [Recommendation coverage](RECOMMENDATIONS.md), [change log](CHANGELOG.md) |

New website pages and exports become live only after the owner approves and the repository's Pages publication process runs. All of the linked repository records can be reviewed in the PR first.

## The six domains

| Domain | What it covers |
|---|---|
| [Biological](01-biological/README.md) | Sleep, metabolism, nervous-system regulation, and physiological integrity |
| [Cognitive](02-cognitive/README.md) | Attention, reasoning, memory, learning, and independent judgment |
| [Emotional](03-emotional/README.md) | Regulation, stress tolerance, identity stability, and recovery |
| [Social](04-social/README.md) | Trust networks, relationships, belonging, and community coordination |
| [Purpose and Moral](05-purpose-moral/README.md) | Values, meaning, responsibility, and moral reasoning |
| [Digital and AI Symbiosis](06-digital-ai-symbiosis/README.md) | Working with AI while retaining capability, authority, and resistance to manipulation |

The causal layers remain civilizational drivers, substrate threats, manipulation techniques, delivery/scale, and human outcomes. See the [taxonomy architecture](taxonomy/threat-architecture.md), [registry](taxonomy/registry.json), and [generated technique rankings](taxonomy/ctss-rankings.md).

## What a CTSS score means

CTSS is our assessed severity for a declared threat scenario or event-linked risk. It combines likelihood, agency impact, reach, detection difficulty, and recovery difficulty. Each estimate needs a reason and evidence or a declared assumption. A provisional score is a usable judgment with explicit uncertainty.

The existing formula can be written as whole points: `L*5 + Ia*6 + R*4 + D*3 + RecD*2`. It still produces 0-100. See [the method](taxonomy/ctss-scoring.md) and [the arithmetic correction](research/scoring-correction-2026-11-07.md).

Keep taxonomy reference estimates, item assessments, directly measured outcomes, and illustrative lens results separate. Helpful and contrary evidence belong in the record. An aggregate describes its declared sample; it is not a percentage of Americans harmed or protected.

## Research and actions

The supplied September-November collection is preserved as **87 assessed item records**, **92 appearances**, **86 source-linked story threads**, and **217 tracked source excerpts**. Those excerpts include grouping labels, proposed actions, research questions, indicators, and watch items. They are not 217 independent incidents. The historical scores were backfilled November 7, 2026.

Every item retains original analysis, sources, input reasons, action, and research trigger. Every tracked signal has an ID, status, proposed responsible role, review trigger, and history. Documented guidance is distinguished from field validation. See [the full ledger](research/intake/events.json) and [signal register](research/intake/signals/register.json).

The [six safeguards](resources/practical-safeguards.md), [additional research checks](resources/advanced-checks.md), and [pilot plan](monitoring/pilot-plan.md) turn findings into reviewable work. Claims of population protection or architectural guarantees require the relevant implementation and test evidence.

## Repository structure

```text
01-biological/ ... 06-digital-ai-symbiosis/  Domain doctrine, threats, controls, readiness
research/             Notes, original intake, scores, and weekly reports
resources/            Assessment workflow, mitigation catalog, and worksheets
examples/             Reproducible fictional assessments
monitoring/           Observed results, protocols, and roadmap status
docs/                 Learning Hub, Explorer, Command Center, and practice pages
integration/          Agent and optional MCP access
tools/ and tests/     Shared calculations, builds, and verification
```

The control catalog now has 56 entries: 44 inherited IDs, including 20 refinements, plus 12 additions. [Research note 010](research/010_domain_controls_and_readiness.md) explains each domain’s changes and the separate readiness profiles. More documented controls do not establish measured readiness.

## Read it in a browser

- [Learning hub](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/)
- [Research, scores, and signals](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/research.html)
- [Controls, resources, and readiness](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/practice.html)
- [Threat explorer](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/csf-explorer.html)
- [Command center](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/csf-command-center.html)
- [How to use and build it](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/guide.html)

For a local preview, run `python -m http.server 8000 --directory docs` from the checkout and open `http://localhost:8000/research.html`.

## Build, check, and contribute

Python 3.12 and Node 22 are the CI baseline. Local checks also passed with Node 24. `VERSION` is the single framework-version source. `python -m tools.version` checks all seven webpages, citation, taxonomy, and data catalog. Core Python tools use the standard library. The MCP adapter is optional and has its own dependency file.

```text
python -m tools.build
python tools/csf.py check
python -m tools.event_monitor check
python -m tools.signals check
python -m tools.export check
python -m tools.version
python -m tools.check_repo
python -m unittest discover -s tests
node tests/check_dashboards.cjs
```

Read [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), and [SECURITY.md](SECURITY.md). Changes belong in a PR for owner review. CODEOWNERS and automated checks support review; they do not replace branch-protection settings or authorize a merge.

[AI SAFEÃ‚Â²](https://github.com/CyberStrategyInstitute/ai-safe2-framework) is the companion machine-side governance framework. The [UAS crosswalk](06-digital-ai-symbiosis/federal-procurement-alignment.md) explains the profile relationship and its limits.

## License and citation

The existing [dual license](LICENSE) remains: MIT for the covered code/machine-readable components and CC BY-SA 4.0 for framework documentation. Retain attribution and source rights. [CITATION.cff](CITATION.cff) provides citation metadata. Use a pinned commit when reproducibility matters.
