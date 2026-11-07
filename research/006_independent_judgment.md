# 006: Keep the thinking needed for the decision

CSF links: ST-001, ST-003, T-CT-006, HO-005. Domains 2 and 6. Status: research-backed evaluation proposal; safeguard effectiveness untested locally.

## What we learned

In a study of 50 analysts, Anthropic experimentally assigned agents a preference between defensible analytical options. Analysts followed that preference 86% of the time. The authors strengthened the agent preferences, and following them did not necessarily produce a worse answer. This supports testing influence on expert choices, with those limits. [Primary research](https://www.anthropic.com/research/agents-judgment-calls).

Kong and colleagues model how shared evidence and trust affect human-AI classification. Their ChatBench reanalysis reports improved accuracy with assistance. It also identifies costs from misunderstanding evidence overlap. The result concerns specific tasks and a behavioral model, with no demonstrated long-term skill loss. [Preprint v1](https://arxiv.org/abs/2611.05870v1).

## What changes

Existing independent-first and AI-off guidance needs a reproducible check. Record the person's initial criteria before advice, then the final decision and reason. Test comprehension and delayed performance on comparable unaided tasks. Measure correct acceptance and correct rejection separately. More overrides alone do not mean better judgment.

Keep five questions separate: Does the person feel capable? Can they perform the task? Can they challenge the system? Can they leave? Can they recover after an error? Self-report answers only the first question.

## Small test and decision

Compare agent-first and independent-first conditions on counterbalanced, comparable tasks. Include correct and incorrect recommendations. Record accuracy, calibration, time, effort, and delayed transfer. Permit accessible assistance where needed and state what capability is being assessed. Adopt a procedure only if it meets the workflow's declared benefit and burden criteria.

Neither paper validates CSF or proves inevitable atrophy. See [safeguard 1](../resources/practical-safeguards.md) and [the pilot plan](../monitoring/pilot-plan.md).
