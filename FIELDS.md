# Field shortlist: the fields we use, per issue type

Each issue type in Jira offers many fields. The framework reads only a few of them. This page lists those few, says who fills each one in and when, and says what to leave alone.

Three groups per issue type:

- **Core**: always filled in, by the status shown.
- **When it applies**: filled in only in the situation described.
- **Set by Jira or automation**: nobody types these.

Any other field on the screen is not used by the framework. Fill it in only if the bank's own standards require it (for example Region, Country, Legal Entity, Reporting Level, Billable Product ID, funding and order book fields).

The field names were read from a photo of the standards page. Check each against your Jira, letter for letter, before relying on this page.

## Summary: how many fields

| Issue type | Core | When it applies | Automatic | Offered on screen (approx.) |
| --- | --- | --- | --- | --- |
| VS Epic | 16 | 6 | 1 | 60 |
| Feature | 17 | 13 | 2 | 55 |
| Epic | 14 | 4 | 2 | 30 |
| Story | 8 | 3 | 1 | 25 |
| Task | 6 | 2 | 1 | 22 |
| Sub-task | 3 | 1 | 1 | 18 |
| Bug | 11 | 4 | 1 | 35 |
| Test | 7 | 1 | 1 | 28 |
| Milestone | 9 | 5 | 0 | 22 |
| Delivery RAID | 9 | 10, mostly by RAID Type | 0 | 32 |

## VS Epic

| Field | Group | Filled in by | When | Kept current |
| --- | --- | --- | --- | --- |
| Summary | Core | Whoever raises it | Idea | When the outcome is reworded |
| Description | Core | Lead | Idea | |
| Assignee (the lead) | Core | Value stream lead | Review | When ownership changes |
| Value Stream and Sub-Value Stream | Core | Lead | Review | |
| Objective ID | Core | Lead | Review | |
| Business Benefits | Core | Lead | Analysis | At the benefits review |
| User/Business Value Score | Core | Lead, at the scoring session | Analysis | Re-scored each PI if still waiting |
| Time Criticality Score | Core | Lead | Analysis | |
| Risk Reduction / Opportunity Enablement Score | Core | Lead | Analysis | |
| Job Size Score | Core | Lead | Analysis | |
| Start date | Core | Lead | Ready | When the roadmap is re-issued |
| End Date | Core | Lead | Ready | When the roadmap is re-issued |
| Due date | Core | Lead | Ready | Only by decision |
| RAG Status | Core | Lead | Implementing | Fortnightly |
| Executive Summary | Core | Lead | Implementing | Fortnightly |
| Linked work items | Core | Delivery lead | When a Milestone or RAID ticket concerns it | |
| Path to Green, Date to Green | When it applies | Lead | RAG is Amber or Red | Fortnightly |
| Financial Benefit (USD) | When it applies | Lead | A money benefit is claimed | At the benefits review |
| Regulatory or Control ID | When it applies | Lead | A regulatory or control driver | |
| Change Reason | When it applies | Lead | Scope or date changed, or stopped | |
| Flagged | When it applies | Lead | Actually stopped | Same day |
| Weighted Shortest Job First Score | Automatic | Calculated from the four scores | | |

## Feature

| Field | Group | Filled in by | When | Kept current |
| --- | --- | --- | --- | --- |
| Summary | Core | Product lead | Idea | |
| Description (with DDT reference) | Core | Product lead | Idea | |
| Assignee | Core | Product lead | Idea | |
| Parent Link (the VS Epic) | Core | Product lead | Triage | |
| Value Stream and Sub-Value Stream | Core | Product lead | Triage | |
| Enabler Type | Core | Product lead | Triage | |
| Acceptance Criteria | Core | Product lead | Analysis | When scope changes |
| Business Benefits | Core | Product lead | Analysis | At close |
| T-Shirt Size | Core | Product lead | Analysis | |
| User/Business Value Score | Core | Product lead, at the scoring session | Analysis | Re-scored each PI if still waiting |
| Time Criticality Score | Core | Product lead | Analysis | |
| Risk Reduction / Opportunity Enablement Score | Core | Product lead | Analysis | |
| Job Size Score | Core | Product lead | Analysis | |
| Target PI | Core | Product lead | PI planning | Only by decision after the lock |
| Labels (`pi-committed` or `pi-stretch`) | Core | Product lead | PI planning | Only by decision after the lock |
| Due date | Core | Product lead | PI planning | Only with a comment |
| RAG Status | Core | Product lead | Implementing | Weekly |
| Start date, End Date | When it applies | Product lead | The Feature is on the roadmap | When the roadmap is re-issued |
| Path to Green, Date to Green | When it applies | Product lead | RAG is Amber or Red | Weekly |
| Management Attention | When it applies | Product lead | RAG is Red, or a decision is needed | Cleared when resolved |
| Executive Summary | When it applies | Product lead | Amber or Red, or on the sponsor's watch list | Weekly while it applies |
| Regulatory or Control Change Type, Regulatory or Control ID | When it applies | Product lead | A regulatory or control driver | |
| Architectural Governance | When it applies | Product lead | Architecture sign-off is required | |
| Contains Resiliency Work | When it applies | Product lead | It does | |
| Change Reason | When it applies | Delivery lead | Descoped, split or re-planned | |
| Linked work items | When it applies | Product lead, delivery lead | Dependencies, Milestones, RAID | When found |
| Flagged | When it applies | Product lead | Actually stopped | Same day |
| Actual PI | Automatic | Automation, at Released | | |
| Weighted Shortest Job First Score | Automatic | Calculated | | |

## Epic

| Field | Group | Filled in by | When | Kept current |
| --- | --- | --- | --- | --- |
| Summary | Core | Product owner | Creation | |
| Epic Name | Core | Product owner | Creation | Same as the summary |
| Description | Core | Product owner | Creation | |
| Assignee | Core | Product owner | Creation | |
| Parent Link (the Feature) | Core | Product owner | Creation | |
| Components (the module) | Core | Product owner | Creation | |
| Team | Core | Product owner | Analysis | |
| Story Points (planning estimate) | Core | Product owner, from the team | Analysis | Revised once stories are estimated |
| Target PI | Core | Product owner | PI planning | Only by decision after the lock |
| Labels (`pi-committed` or `pi-stretch`) | Core | Product owner | PI planning | Only by decision after the lock |
| End Date (expected go-live) | Core | Product owner | PI planning | Weekly check; change with a comment |
| RAG Status | Core | Product owner | Implementing | Weekly |
| Fix versions | Core | Product owner | Sprint planning, once the release is known | When the release changes |
| Linked work items (blocks, is blocked by) | Core | Product owner | When a dependency is found | |
| Start date | When it applies | Product owner | The Epic is scheduled in the plan | |
| Change Request ID | When it applies | Product owner | At release | |
| Regulatory or Control Change Type | When it applies | Product owner | Inherited from a regulatory Feature | |
| Flagged | When it applies | Product owner | Actually stopped | Same day |
| Value Stream and Sub-Value Stream | Automatic | Copied from the parent Feature (rule 1); by hand until the rule exists | | |
| Actual PI | Automatic | Automation, at Released | | |

**A gap to know about.** From the photo, Epic does not appear to carry Path to Green, Date to Green or Due date. Until that is confirmed or the fields are added to Epic:

- the expected go-live date of an Epic is its **End Date**;
- the recovery plan for an Amber or Red Epic is a **comment that starts "Path to green:"** and gives the plan and the date.

If your Epic screen does show those three fields, use them as on a Feature.

## Story

| Field | Group | Filled in by | When |
| --- | --- | --- | --- |
| Summary | Core | Whoever creates it | Creation |
| Description | Core | Whoever creates it | Creation |
| Epic Link | Core | Whoever creates it | Creation |
| Acceptance Criteria | Core | Product owner, analyst | Refinement |
| Story Points | Core | Team | Refinement |
| Assignee | Core | Team | When work starts |
| Sprint | Core | Team | Sprint planning |
| Components | Core | Whoever creates it | Creation |
| Fix versions | When it applies | Product owner | The release is known |
| Story Type | When it applies | As the team uses it | |
| Flagged | When it applies | The person who is stopped | Same day |
| Status, Resolution | Automatic | Set by moving the ticket | |

## Task

| Field | Group | Filled in by | When |
| --- | --- | --- | --- |
| Summary, Description | Core | Whoever creates it | Creation |
| Epic Link | Core | Whoever creates it | Creation |
| Assignee | Core | Team | When work starts |
| Sprint | Core | Team | Sprint planning |
| Story Points | Core | Team | Refinement, if the team estimates tasks |
| Acceptance Criteria | When it applies | Whoever creates it | The outcome is not obvious |
| Flagged | When it applies | The person who is stopped | Same day |
| Status, Resolution | Automatic | | |

Sign-off tasks on a Feature use the same fields: the summary names the approval, the assignee is the approver, and the approver closes it.

## Sub-task

| Field | Group | Filled in by | When |
| --- | --- | --- | --- |
| Summary | Core | Team | Creation |
| Assignee | Core | Team | When work starts |
| Parent | Core | Set on creation | |
| Flagged | When it applies | The person who is stopped | Same day |
| Status | Automatic | | |

## Bug

| Field | Group | Filled in by | When |
| --- | --- | --- | --- |
| Summary | Core | Whoever raises it | Creation |
| Description (steps, expected, actual) | Core | Whoever raises it | Creation |
| Epic Link | Core | Whoever raises it | Creation |
| Severity | Core | Whoever raises it; confirmed by the product owner | Creation |
| Priority | Core | Product owner | Triage |
| Testing Phase | Core | Whoever raises it | Creation |
| Environment | Core | Whoever raises it | Creation |
| Affects versions | Core | Whoever raises it | Creation |
| Assignee | Core | Team | When work starts |
| Sprint | Core | Team | Sprint planning |
| Components | Core | Whoever raises it | Creation |
| Fix versions | When it applies | Product owner | The fix is scheduled |
| Root cause category | When it applies | The fixer | At closure |
| Root cause analysis | When it applies | The fixer | Severity 1 or 2, or found in production |
| Flagged | When it applies | The person who is stopped | Same day |
| Status, Resolution | Automatic | | |

## Test

| Field | Group | Filled in by | When |
| --- | --- | --- | --- |
| Summary, Description | Core | Tester | Creation |
| Epic Link | Core | Tester | Creation |
| Testing Phase | Core | Tester | Creation |
| Environments | Core | Tester | Creation |
| Assignee | Core | Tester | Creation |
| Sprint | Core | Team | Sprint planning |
| Fix versions | When it applies | Tester | The test belongs to a release |
| Status, Resolution | Automatic | | |

## Milestone

| Field | Group | Filled in by | When | Kept current |
| --- | --- | --- | --- | --- |
| Summary | Core | Delivery lead | Creation | |
| Description | Core | Delivery lead | Creation | |
| Assignee | Core | Delivery lead | Creation | |
| Value Stream and Sub-Value Stream | Core | Delivery lead | Creation | |
| Due date (current target) | Core | Delivery lead | Creation | When it moves, with a comment |
| Baseline End Date (first commitment) | Core | Delivery lead | Creation | Never changed |
| RAG Status | Core | Delivery lead | Creation | Fortnightly |
| Labels (the kind: `ms-regulatory`, `ms-golive`, `ms-pi`, `ms-external`) | Core | Delivery lead | Creation | |
| Linked work items (what must finish for it) | Core | Delivery lead | Creation | When scope changes |
| Path to Green, Date to Green | When it applies | Delivery lead | Amber or Red | Fortnightly |
| Executive Summary | When it applies | Delivery lead | Reported to sponsors | Fortnightly |
| Regulatory or Control ID | When it applies | Delivery lead | A regulatory Milestone | |
| Fix versions | When it applies | Delivery lead | A go-live Milestone | |

## Delivery RAID

| Field | Group | Filled in by | When | Kept current |
| --- | --- | --- | --- | --- |
| Summary | Core | Whoever raises it | Creation | |
| Description | Core | Whoever raises it | Creation | |
| RAID Type | Core | Whoever raises it | Creation | |
| Assignee (the owner) | Core | Delivery lead | Within a week | |
| Value Stream and Sub-Value Stream (who is affected) | Core | Whoever raises it | Creation | |
| RAG Status | Core | Owner | Creation | At each review |
| Due date (next review, or need-by date) | Core | Owner | Creation | At each review |
| Impact | Core | Owner | Creation | At each review |
| Linked work items (what it affects) | Core | Owner | Creation | |
| Probability | Risk only | Owner | Creation | At each review |
| Risk Trigger Event | Risk only | Owner | Creation | |
| ROAM Response | Risk only | Owner | First review | At each review |
| Dependency Type | Dependency only | Owner | Creation | |
| Supplier Value Stream and Sub Value Stream (who must deliver) | Dependency only | Owner | Creation | |
| Baseline End Date (date first agreed) | Dependency only | Owner | When agreed | Never changed |
| Impact Details | Issue only | Owner | Creation | |
| Path to Green, Date to Green | Issue only, or Amber or Red | Owner | Creation | At each review |
| Executive Summary | When it applies | Owner | Reported to sponsors | |

## Fields the framework does not use

Left exactly as the bank's standards require; nothing in the filters, dashboards or Confluence pages reads them:

Region, Country, Legal Entity, Collaborators, Reporting Level, Billable Product ID, Funding B/GI, Funding Period, Funding Type, Delivery B/GI, Order Book ID, Project ID, Task ID, Change Type, Customer Impact, Operational Resilience Impact, Regulatory Impact, Span of Change Impact, Value Stream Epic Impact Rating, Cost Estimate and its confidence level, First Customer Release, Category, Thematic, RAID ID, Risk Impact Assessment ID, Security Level (used only to restrict a sensitive ticket).

Several of these are useful for the case on a VS Epic (the impact fields, the funding fields). Use them there if your portfolio process asks for them; the framework's views do not depend on them.

## Two rules for keeping the shortlist short

1. A field joins the shortlist only when a filter, dashboard, Confluence page or decision reads it. "It might be useful" is not enough.
2. When a field is added, one is reviewed for removal. The framework owner keeps the list and records changes in the change log.
