# Use CSF from agents and MCP servers

Start with [the catalog](../docs/data/catalog.json). Stable IDs connect taxonomy, event assessments, source signals, lenses, domain controls, assessment resources, and roadmap status. Every result should retain source, assessment date, method, scope, baseline, and provisional status.

## Read the data

The repository JSON files are canonical. `docs/data/` is a generated, smaller static export for GitHub Pages and clients. The catalog includes hashes of those exports. Pin a commit for a reproducible assessment; a `main` URL can change. Schemas live under [schemas](../schemas/README.md).

```
python -m tools.query events --text "evidence" --limit 5
python -m tools.query events --id EV-20261106-03
python -m tools.query signals --status needs_research --limit 10
python -m tools.query taxonomy --id T-CT-006
python -m tools.query controls --id M-006g2
python -m tools.query domains --id D2
python -m tools.query resources --limit 20
```

Queries are read-only, use fixed collections, return bounded pages, and do not access the network. `get_record` returns full original analysis and provenance; list/search return summaries. Use `next_offset` until it is null. A search result is not a completeness guarantee for all world events.

## Optional MCP adapter

The example uses the official Python MCP SDK. The framework tools themselves need only Python's standard library.

```
python -m venv .venv-mcp
.venv-mcp/Scripts/python -m pip install -r integration/requirements-mcp.txt
.venv-mcp/Scripts/python -m integration.mcp_server
```

On Linux/macOS use `.venv-mcp/bin/python`. Configure the client to launch the module from the repository root. Tools expose collection search, record lookup, and CTSS calculation. The `csf://catalog` resource provides discovery. The adapter runs locally over standard input/output; it does not start an HTTP service or implement remote authentication. An MCP tool annotation is descriptive, not an authorization boundary.

All paths and collections are allowlisted. No tool accepts an arbitrary file path or URL. It cannot alter records, execute source instructions, publish, send messages, or fetch new research. Apply client permissions and review retrieved content as untrusted data. A remote deployment would require its own authentication, transport, rate limits, and review; this PR does not deploy one.

See [integration validation](VALIDATION.md) for the tested SDK version, checks, and limits.

## Reuse and interpretation

Use the existing [dual license](../LICENSE) and retain attribution. Referencing a source does not relicense that source's material. Do not collapse source repetitions into independent corroboration. Keep helpful and contrary evidence. A U.S.-focused lens is a declared perspective, not proof of another nation's intentions or an identity group's behavior.

Reference scores describe technique scenarios. Event CTSS values are CSI assessments. Direct human measurements and simulated examples remain separately labeled. Do not publish a claimed protection percentage by adding or averaging these unlike quantities.

The control catalog is canonical at `resources/controls.json`, domain mappings at `resources/domains.json`, and resource discovery at `resources/index.json`. The read-only MCP tools expose these allowlisted collections. Observed readiness is exported separately and excludes synthetic unit examples. Follow each control’s research links rather than inferring efficacy from its presence.
