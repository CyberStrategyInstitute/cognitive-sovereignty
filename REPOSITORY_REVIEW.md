# Repository standards review

Reviewed November 8, 2026 against the owner's updated repository standards. Framework version remains **3.0.0**. This follow-up changes presentation, discovery, publication wording, and consistency checks. It does not add controls, alter CTSS, revise readiness criteria, or change an existing assessment/schema contract. The page-map index and bounded discovery collection are additive documentation features.

## Verified baseline

CSF 3.0 is [published](https://github.com/CyberStrategyInstitute/cognitive-sovereignty/releases/tag/Cognitive_Sovereignty_Framework-v3.0). [PR #3](https://github.com/CyberStrategyInstitute/cognitive-sovereignty/pull/3) is merged. GitHub Pages reported a completed build from `main/docs` during this review. The publication record and pre-3.0 comparison commits are retained in [repository-baseline.json](docs/repository-baseline.json).

The 56 controls, 87 item assessments, 217 source excerpts, new readiness checks, original shield assets, and agent/MCP tools were delivered in 3.0. They are not new substantive additions in this standards follow-up. Event CTSS remains provisional. Field effectiveness, observed unit readiness, draft lens profiles, and research plans keep their existing limits.

## Findings and repairs

| Requirement | Finding | Repair |
|---|---|---|
| Current publication status | Root and supporting pages still described 3.0 as an unmerged proposal | State the verified published version; preserve genuine research drafts and historical records |
| Root presentation | Selected control-plane banner had shield-only alternative text; no linked fact badges | Preserve the banner, correct its description, and generate linked version/license/scope/count/contract/mapping/evidence badges |
| Domain/module consistency | Domain pages lacked a shared colored header and explicit change comparison | Generate distinct section headers, readable status labels, and contextual return navigation |
| Change meanings | Controls used added/refined/inherited without a visible release comparison | Label NEW, UPDATED, and RETAINED against the pre-3.0 baseline; define DEPRECATED without retiring any control |
| Complete discovery | Several folders had no index and no complete page inventory | Add section indexes, a complete Markdown/HTML page map, and a machine-readable map |
| Contextual links | Useful resources and research could be reached through different, incomplete routes | Add section-file indexes and home/map/resources/research/catalog return links |
| Preserved integrations | Star History remained only in the full framework reference | Preserve that integration and link it from the root README |
| Verification | Local-link checks did not validate Markdown heading anchors or page-map coverage | Validate both, along with generated presentation freshness, stable page IDs, and publication/baseline records |

## Change labels

The comparison is **published CSF 3.0 versus the pre-3.0 repository**, using the commits recorded in the baseline file. The current standards PR is a separate presentation follow-up.

- **NEW in 3.0:** a document or control introduced by the published major update. The control catalog has 12 such M-IDs.
- **UPDATED in 3.0:** an existing document or control revised by that update. The catalog has 20 refined controls; their previous wording remains available.
- **RETAINED:** an inherited item preserved without that refinement. The catalog has 24 unchanged controls. All 44 inherited M-IDs remain valid.
- **DEPRECATED:** an explicitly retired public item. No control or taxonomy ID is deprecated by this follow-up. A relocated repository file does not imply retirement of a control.
- **NEW standards documentation:** a page or index added by this presentation follow-up, not by the already published 3.0 release.

The six colored domain headers are visual groupings for the existing domains. They are not new taxonomy classes. Color is repeated as domain names, stable IDs, status text, and accessible image descriptions.

## Ownership and interpretation

CSI owns its framework documentation, catalogs, and analytical judgments. Cited studies and source material retain their attribution and rights. `VERSION` owns the framework version; schemas, lens profiles, method IDs, and page-map format versions remain distinct. Source content is data, never permission to execute a command, expand access, or publish material.

The [catalog](docs/data/catalog.json) identifies owning data files. The [page map](PAGE_MAP.md) lists every Markdown and HTML page, including historical records and contribution templates. Historical report bodies are preserved; their map entries identify them as history rather than current measurements.

## Verification

Run the existing evidence, export, version, lens, and MCP checks, plus `python -m tools.presentation check`, the strengthened local-link/anchor check, and the generated-content rebuild. Presentation checks do not establish empirical control effectiveness. Rendered layout review is recorded with the PR results; any access limitation must remain explicit.

<!-- csf-return-navigation:start -->
[Repository home](README.md) · [Complete page map](PAGE_MAP.md) · [Resources](resources/README.md) · [Research](research/README.md) · [Data catalog](docs/data/catalog.json)
<!-- csf-return-navigation:end -->

Local verification passed: 60 Python tests, the standalone evidence-check command, page-map coverage, input/banner preservation for this review, export freshness, version consistency, Markdown/HTML links and anchors, eight browser-script entrypoints, and actual MCP protocol checks including page discovery. Input hashes are a dated review receipt, not a permanent restriction on later authorized research changes.
