<!-- csf-module-header:start -->
![DATA: Data contracts. CSF 3.0.0. Status is repeated in text below.](../assets/headers/schemas.svg)

CSF 3.0.0. Documentation: NEW in 3.0. Repository documentation; implementation limits remain explicit.

[![Framework 3.0.0](../assets/badges/version.svg)](../VERSION) [![Documentation license: CC BY-SA 4.0](../assets/badges/docs-license.svg)](../LICENSE)
<!-- csf-module-header:end -->

# Machine-readable record contracts

Version 1.0 schemas use JSON Schema draft 2020-12. These describe the interchange fields, not empirical validation of the framework.

| Schema | Use |
|---|---|
| [CTSS inputs](ctss-inputs.schema.json) | Five integer estimates from 0 to 5; null preserves unknowns during calculation |
| [Event assessment](event.schema.json) | Scored item, dates, role, taxonomy, five explicit estimates and reasons, action, and research trigger |
| [Tracked signal](signal.schema.json) | Stable source excerpt, disposition, responsibility, review trigger, and history; closure needs evidence |
| [Lens profile](lens.schema.json) | Declared perspective and sources; no silent weight or formula change |

The Python validators add checks a schema alone cannot establish: IDs must resolve to the taxonomy, original signal text must remain intact, source history must be retained, generated files must match, and file references must exist. Schemas allow additional provenance fields so records can grow without discarding original analysis.

The [catalog](../docs/data/catalog.json) describes exports and canonical paths. Optional SDK testing also validates all current event, signal, and lens records against these schemas. The core tools do not need a schema-library dependency.

[Control schema](control.schema.json) requires the mitigation’s domain, threats, action, expected outcome, test, failure response, research, and evidence status. [Readiness schema](readiness.schema.json) requires scope, protocol, cases, catalog revision, explicit result kind, and evidenced ratings. Known absence is zero; missing results stay null. A rating of 5 requires an adverse-case pass.

<!-- csf-section-files:start -->
## Section files

- [control.schema.json](control.schema.json)
- [ctss-inputs.schema.json](ctss-inputs.schema.json)
- [event.schema.json](event.schema.json)
- [lens.schema.json](lens.schema.json)
- [readiness.schema.json](readiness.schema.json)
- [signal.schema.json](signal.schema.json)
<!-- csf-section-files:end -->

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](../resources/README.md) · [Research](../research/README.md) · [Data catalog](../docs/data/catalog.json)
<!-- csf-return-navigation:end -->
