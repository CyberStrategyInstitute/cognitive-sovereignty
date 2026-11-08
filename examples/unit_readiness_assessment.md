# Worked unit cognitive readiness assessment

This is a fictional training example of an AI-assisted briefing workflow. It shows how to connect research, CTSS, controls, capability checks, and remediation. No real unit or participant was tested. The [JSON record](unit-readiness.json) and [fictional case fixtures](readiness-fixtures.md) reproduce the capability results below.

Use the [assessment template](../resources/assessment-template.md) for a blank threat assessment and the [readiness worksheet](../resources/readiness-worksheet.md) for capability evidence. The earlier example’s 31/100 self-report, 55% coverage estimate, personnel percentages, and targets were fictional assumptions without an underlying case record. They are not the baseline for this worked example or evidence of an operational outcome. Git history preserves that earlier text.

## 1. Define the decision

Scope: a notional team uses an assistant to collect sources, draft a briefing, and recommend a course of action. The human briefing owner retains responsibility for the final judgment and any action. Private personnel records, clinical testing, and live operational systems are excluded.

The question is whether the team can identify omitted or repeated evidence, challenge advice, limit permissions, and correct the downstream record. Each result below is labeled synthetic. It must not enter observed unit trends.

## 2. Assess the associated threat

Illustrative scenario: the assistant repeats one source as corroboration, recommends a course of action, and asks for broader access to carry it out. Relevant IDs are T-CT-006, T-CT-007, and T-CT-008. Use the [CTSS method](../taxonomy/ctss-scoring.md) for the threat and the capability worksheet for the response.

| CTSS input | Estimate | Fictional scenario reason |
|---|---:|---|
| Likelihood | 3 | The exercise assumes repeated exposure within this workflow; this is not an incident rate |
| Impact on agency | 4 | A consequential briefing can shape a decision before independent review |
| Reach | 1 | The declared scope is the team and its briefing recipients, fewer than 1,000 people |
| Detection difficulty | 3 | The repeated origin and requested permission expansion are visible only with review |
| Recovery difficulty | 2 | The exercise assumes a controlled correction path and no irreversible action |

CTSS is **56/100**: `3*5 + 4*6 + 1*4 + 3*3 + 2*2`. This is a synthetic scenario score, not a readiness score or a measured incident. It remains outside the historical event ledger.

## 3. Select and test capabilities across all six domains

The [catalog](../resources/mitigation-catalog.md) defines each check, outcome, failure response, and research link. This example rates only the two new research-extension checks per domain. The inherited 44 capabilities remain unassessed. The two profiles must not be combined.

| Domain | Research-extension controls | Ratings | Extension score | Inherited readiness |
|---|---|---|---:|---|
| Biological | M-014b, M-016b | 1, 0 | 10/100 | Unknown, 0/6 rated |
| Cognitive | M-007c2, M-008c | 2, 1 | 30/100 | Unknown, 0/8 rated |
| Emotional | M-005d2, M-016d2 | 1, 1 | 20/100 | Unknown, 0/6 rated |
| Social | M-005e2, M-008e2 | 2, 1 | 30/100 | Unknown, 0/7 rated |
| Purpose & Moral | M-015f2, M-HO5f2 | 2, 1 | 30/100 | Unknown, 0/8 rated |
| Digital & AI Symbiosis | M-006g2, M-005g | 1, 0 | 10/100 | Unknown, 0/9 rated |

Each extension score uses `(rating 1 + rating 2) / 10 * 100`. Evidence and fictional failure details are linked from the JSON record. None of these numbers establishes personal fitness, clinical status, mission readiness, or effective protection. No observed readiness increase can be inferred.

## 4. Assign repairs and retain failures

| Priority | Repair | Proposed owner role | Completion evidence |
|---|---|---|---|
| Before a consequential action | Block self-authorized permission expansion; verify the pause/handoff path | Workflow owner and implementing-system owner | Both normal and adverse cases pass without unauthorized action |
| Before relying on the briefing | Show source lineage, missing pages, objectives, and conflicts | Briefing owner | Reviewer identifies two independent lineages, the omission, and the conflict |
| Before distributing identity claims | Record synthetic-speaker permission and correct controlled copies | Communications owner | Authorized representation and correction receipts for all known copies |
| Before closing the exercise | Repair exit, remembered-context correction, and score appeal | Service owner and independent reviewer | Exit, correction, refusal, and appeal outcomes are recorded |

Roles are proposed, not assigned to real people. A responsible owner sets the date and accepts the work. Documentation alone does not close a failed check.

## 5. Reassess and publish responsibly

Run `python -m tools.readiness examples/unit-readiness.json` to reproduce this example. For a real assessment, retain a new dated record with kind `observed`, the exact protocol, case set, catalog revision, assessor, and permissible evidence. Keep detailed private evidence in its approved system and publish only appropriate aggregate results.

Retest repaired capabilities with the same cases before claiming improvement. Preserve the initial record and any adverse results. Use [monitoring](../monitoring/README.md) for results and [the research intake](../research/intake/README.md) for new events. Threat CTSS, capability readiness, self-report, and case pass rates remain separate throughout the process.

<!-- csf-return-navigation:start -->
[Repository home](../README.md) · [Complete page map](../PAGE_MAP.md) · [Resources](../resources/README.md) · [Research](../research/README.md) · [Data catalog](../docs/data/catalog.json) · [Section index](README.md)
<!-- csf-return-navigation:end -->
