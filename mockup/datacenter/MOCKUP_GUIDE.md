# Mock-up in one Jira project

> **Data Center edition.** This copy uses the field names and values of today's Jira: Target PI values `PI 5` and `PI 4`, WSJF, Enabler, Is it Regulatory, RAG Description, Risk Probability, Priority and Baseline End. "Needs management attention" is the label `mgmt-attention`. What changed and why is in [FIELD_MAPPING.md](FIELD_MAPPING.md).

A small set of tickets, all in one project, that is enough to build and check every dashboard and Confluence page in the white paper. Nothing here creates tickets for you: this page lists the tickets to create, the fields to fill in on each, the saved filters for a single project, and what every dashboard panel should then show.

**38 tickets:** 3 Capabilities, 8 Initiatives, 9 Epics, 6 Stories, 2 Bugs, 8 Delivery RAID and 2 Tasks. Creating them by hand takes about an hour.

The same list is in [mock_tickets.xlsx](mock_tickets.xlsx) (sheets: Tickets, Expected results, Key map) and [mock_tickets.csv](mock_tickets.csv).

## 1. How the mock-up differs from the full design

| In the white paper | In this mock-up | Why |
| --- | --- | --- |
| VS Epic | **Capability** | That is the name of the issue type on today's Data Center |
| Feature | **Initiative** | Same reason |
| One portfolio project and one project per application | One project, `CL123` | To test without touching real projects |
| The application is the project | The application is the **Component**: Credit Application, Drawdowns, Governance and Conditions | Everything is in one project |
| Milestone issue type | A **Task** with the labels `milestone` and `ms-regulatory` or `ms-golive` | The Milestone type arrives with Jira Cloud |
| Milestone slippage (Baseline End against Due date) | Not tested | A Task may not carry Baseline End |

Every mock ticket carries the label `mock`, so the filters never pick up anything else in the project and the tickets are easy to find and delete afterwards.

**Change these three things first if yours differ**, in `build_mockup.py` or by hand:

- the project key: `CL123`
- the current and previous PI as your Target PI field writes them: `PI 5` and `PI 4`
- the release name: `CL123 2027.01`

Dates in the tables were worked out from 27 November 2026. If you build the mock-up much later, move the dates by the same number of days, or the "late" and "due soon" panels will show different tickets.

## 2. Before creating tickets

- [ ] Three Components exist in the project: Credit Application, Drawdowns, Governance and Conditions.
- [ ] One version exists: `CL123 2027.01`, with a release date about six weeks ahead.
- [ ] The issue types Capability, Initiative, Epic, Story, Bug, Task and Delivery RAID can be created in the project.
- [ ] You know the exact values your fields accept for: Target PI, RAG Status, RAID Type, ROAM Response, Risk Probability, Priority, Severity, Enabler, Is it Regulatory. The tables use placeholders; use your own values with the same meaning.
- [ ] A Scrum board exists on the project (needed only for the team dashboard).

If a field in the tables is not on the screen for that issue type, skip it and note it: that is itself a finding for the proof of concept.

## 3. The tickets to create

Create them in this order, because each level needs the one above as its parent. The ID in the first column is only a name for this guide; write the real Jira key beside it in the Key map sheet as you go.

### 3.1 Capabilities (3)

Fields on every Capability: Summary, Status, RAG Status, Due date, Value Stream and Sub-Value Stream, Assignee, Labels. RAG Description where shown.

| ID | Summary | Status | RAG Status | Due date | Value Stream and Sub-Value Stream | RAG Description | Labels |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | Avoid audit risk through access control | Implementing | Amber | 2027-06-15 | Credit and Lending -> Governance and Conditions | Drawdowns to borrow one engineer from Credit Application in January | `mock` |
| C2 | Earlier warning on deteriorating exposures | Implementing | Red | 2027-09-23 | Credit and Lending -> Monitoring | Group Data to name a covenant data owner by mid December | `mock` |
| C3 | One view of conditions from approval to drawdown | Analysis | Green | 2027-12-12 | Credit and Lending -> Drawdown |  | `mock` |

### 3.2 Initiatives (8)

Fields: Summary, Parent Link, Status, Target PI, Actual PI, RAG Status, Labels, Due date, Value Stream and Sub-Value Stream, Assignee, and the extras in the last column. WSJF is the single score field; a higher number goes first.

| ID | Summary | Parent (Parent Link) | Status | Target PI | Actual PI | RAG Status | Labels | Due date | Sub value stream | Other |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I1 | M&P across the platform | C1 Avoid audit risk through access control | Implementing | PI 5 |  | Amber | `mock`, `pi-committed` | 2027-01-11 | Governance and Conditions | WSJF 5.2; Is it Regulatory: Yes; RAG Description: Drawdowns to borrow one engineer in January |
| I2 | Access review evidence pack | C1 Avoid audit risk through access control | Released | PI 5 | PI 5 | Green | `mock`, `pi-committed` | 2026-11-22 | Governance and Conditions | WSJF 5.3 |
| I3 | Watch-list triggers from covenant breaches | C2 Earlier warning on deteriorating exposures | Implementing | PI 5 |  | Red | `mock`, `pi-committed`, `mgmt-attention` | 2026-12-27 | Monitoring | WSJF 3.6 |
| I4 | Conditions carried into drawdown checks | C3 One view of conditions from approval to drawdown | Implementing | PI 5 |  | Green | `mock`, `pi-committed` | 2027-01-16 | Drawdown | WSJF 3.6 |
| I5 | Covenant breach alerts by email | C2 Earlier warning on deteriorating exposures | Implementing | PI 5 |  | Green | `mock`, `pi-stretch`, `unplanned` | 2027-01-21 |  | WSJF 3.3; Enabler: Yes |
| I6 | Exposure roll-up by client group | none (on purpose) | Idea |  |  |  | `mock` |  |  |  |
| I7 | Facility letter generated from approved terms | C3 One view of conditions from approval to drawdown | Implementing | PI 4 |  | Amber | `mock`, `pi-committed` | 2026-12-17 | Drawdown | WSJF 3.8; RAG Description: Credit Application feed to finish in sprint 2 |
| I8 | Conditions change history for auditors | C1 Avoid audit risk through access control | Ready |  |  | Green | `mock` |  | Governance and Conditions | WSJF 8.7 |

I6 has no parent and almost no fields on purpose: it is raw intake. I5 has no sub value stream on purpose: it should appear in the "gaps" list.

### 3.3 Epics (9)

Fields: Summary, Epic Name, Parent Link, Component, Status, Target PI, Actual PI, RAG Status, Labels, End Date, Story Points, Fix version, Assignee.

| ID | Summary | Epic Name | Parent (Parent Link) | Component | Status | Target PI | Actual PI | RAG Status | Labels | End Date | Story Points | Fix version |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | M&P for Credit Application | M&P CA | I1 M&P across the platform | Credit Application | Released | PI 5 | PI 5 | Green | `mock`, `pi-committed` | 2026-11-17 | 21 | CL123 2027.01 |
| E2 | M&P for Drawdowns | M&P DRAW | I1 M&P across the platform | Drawdowns | Implementing | PI 5 |  | Amber | `mock`, `pi-committed` | 2027-01-06 | 34 | CL123 2027.01 |
| E3 | Evidence pack for conditions | Evidence GC | I2 Access review evidence pack | Governance and Conditions | Released | PI 5 | PI 5 | Green | `mock`, `pi-committed` | 2026-11-21 | 13 |  |
| E4 | Covenant trigger rules | Triggers GC | I3 Watch-list triggers from covenant breaches | Governance and Conditions | Implementing | PI 5 |  | Red | `mock`, `pi-committed` | 2026-12-25 | 21 |  |
| E5 | Covenant alerts shown in Drawdowns | Alerts DRAW | I3 Watch-list triggers from covenant breaches | Drawdowns | Ready | PI 5 |  | Green | `mock`, `pi-stretch` | 2027-01-08 | 13 |  |
| E6 | Alert emails from Credit Application | Emails CA | I5 Covenant breach alerts by email | Credit Application | Implementing | PI 5 |  | Green | `mock`, `pi-stretch`, `unplanned` | 2027-01-16 | 8 |  |
| E7 | Approved terms feed for the facility letter | Terms feed CA | I7 Facility letter generated from approved terms | Credit Application | Implementing | PI 4 |  | Amber | `mock`, `pi-committed` | 2026-12-15 | 13 |  |
| E8 | Limit check rewrite | Limit check DRAW | none (on purpose) | Drawdowns | Implementing |  |  | Green | `mock` | 2027-01-01 | 8 |  |
| E9 | Conditions API v2 | Conditions API GC | I4 Conditions carried into drawdown checks | Governance and Conditions | Implementing | PI 5 |  | Green | `mock`, `pi-committed` | 2027-01-02 | 21 |  |

E8 has no parent on purpose: it should appear in the hygiene list. E7 has last PI as its Target PI on purpose: it is the spillover.

### 3.4 Stories and Bugs (8)

Fields: Summary, Epic Link, Component, Status, Story Points (stories), Severity (bugs), Fix version, Assignee.

| ID | Type | Summary | Epic Link | Component | Status | Story Points | Severity | Fix version | In the sprint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | Story | Role checks on the drawdown approval screen | E2 M&P for Drawdowns | Drawdowns | In Progress | 5 |  | CL123 2027.01 | Yes |
| S2 | Story | Role model read from the shared service | E2 M&P for Drawdowns | Drawdowns | Done | 8 |  | CL123 2027.01 | Yes |
| S3 | Story | Trigger rule for a missed covenant test | E4 Covenant trigger rules | Governance and Conditions | In Progress | 5 |  |  | Yes |
| S4 | Story | Email template for a covenant breach | E6 Alert emails from Credit Application | Credit Application | Backlog | 3 |  |  | Yes |
| S5 | Story | Tidy up logging in limit checks | none (on purpose) | Drawdowns | Backlog | 2 |  |  |  |
| S6 | Story | Approved terms mapped to letter fields | E7 Approved terms feed for the facility letter | Credit Application | Done | 5 |  |  | Yes |
| B1 | Bug | Approver role not applied to joint facilities | E2 M&P for Drawdowns | Drawdowns | In Progress |  | 2 | CL123 2027.01 | Yes |
| B2 | Bug | Evidence export misses archived conditions | E3 Evidence pack for conditions | Governance and Conditions | Done |  | 3 |  |  |

### 3.5 Delivery RAID (8)

Fields: Summary, RAID Type, Status, RAG Status, Due date, Value Stream and Sub-Value Stream (who is affected or waiting), Component, Priority, Assignee. For a Dependency: Supplier Value Stream and Sub Value Stream, and Baseline End once agreed. For a Risk: Risk Probability and ROAM Response.

On a Dependency, **Due date is the date the receiver needs it** and **Baseline End is the date the supplier promised**.

| ID | Summary | RAID Type | Status | RAG Status | Due date | Baseline End | Sub value stream (waiting) | Supplier | Component | Risk Probability | Priority | ROAM Response | Assignee |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Drawdowns needs Conditions API v2 before sprint 3 | Dependency | In Progress | Red | 2026-12-18 | 2027-01-01 | Drawdown | Governance and Conditions | Drawdowns |  | High |  | anyone |
| R2 | Credit Application needs the covenant event feed for alert emails | Dependency | Backlog | Amber | 2026-12-11 |  | Monitoring | Governance and Conditions | Credit Application |  | Medium |  | anyone |
| R3 | Drawdowns needs the evidence export format agreed | Dependency | In Progress | Green | 2027-01-06 | 2026-12-22 | Drawdown | Governance and Conditions | Drawdowns |  | Low |  | anyone |
| R4 | Covenant test environment needed from Group IT | Dependency | Backlog | Amber | 2026-11-23 |  | Monitoring |  | Governance and Conditions |  | High |  | leave empty |
| R5 | Drawdowns loses two engineers in January | Risk | In Progress | Amber | 2026-12-07 |  | Drawdown |  | Drawdowns | High | High | Owned | anyone |
| R6 | Audit may widen the scope of the access finding | Risk | Backlog | Green | 2026-11-20 |  | Governance and Conditions |  | Governance and Conditions | Low | High |  | anyone |
| R7 | Covenant data for legacy facilities is incomplete | Issue | In Progress | Red | 2026-12-09 |  | Monitoring |  | Governance and Conditions |  | High |  | anyone |
| R8 | Group IT will keep the current role service until June | Assumption | Backlog | Green | 2027-01-26 |  | Governance and Conditions |  | Credit Application |  | Medium |  | anyone |

### 3.6 Milestone stand-ins (2 Tasks)

| ID | Summary | Status | Labels | Due date | RAG Status |
| --- | --- | --- | --- | --- | --- |
| M1 | MILESTONE: audit point AP-12 remediation due | In Progress | `mock`, `milestone`, `ms-regulatory` | 2027-02-05 | Green |
| M2 | MILESTONE: M&P live in all origination applications | In Progress | `mock`, `milestone`, `ms-golive` | 2026-11-24 | Amber |

## 4. What to set by hand after the tickets exist

### 4.1 Parents (Parent Link): 15 tickets

| Set Parent Link on | To |
| --- | --- |
| I1 M&P across the platform | C1 Avoid audit risk through access control |
| I2 Access review evidence pack | C1 Avoid audit risk through access control |
| I3 Watch-list triggers from covenant breaches | C2 Earlier warning on deteriorating exposures |
| I4 Conditions carried into drawdown checks | C3 One view of conditions from approval to drawdown |
| I5 Covenant breach alerts by email | C2 Earlier warning on deteriorating exposures |
| I7 Facility letter generated from approved terms | C3 One view of conditions from approval to drawdown |
| I8 Conditions change history for auditors | C1 Avoid audit risk through access control |
| E1 M&P for Credit Application | I1 M&P across the platform |
| E2 M&P for Drawdowns | I1 M&P across the platform |
| E3 Evidence pack for conditions | I2 Access review evidence pack |
| E4 Covenant trigger rules | I3 Watch-list triggers from covenant breaches |
| E5 Covenant alerts shown in Drawdowns | I3 Watch-list triggers from covenant breaches |
| E6 Alert emails from Credit Application | I5 Covenant breach alerts by email |
| E7 Approved terms feed for the facility letter | I7 Facility letter generated from approved terms |
| E9 Conditions API v2 | I4 Conditions carried into drawdown checks |

### 4.2 Links: 14

| On this ticket | Add link | To |
| --- | --- | --- |
| E2 M&P for Drawdowns | is blocked by | E1 M&P for Credit Application |
| E5 Covenant alerts shown in Drawdowns | is blocked by | E9 Conditions API v2 |
| R1 Drawdowns needs Conditions API v2 before sprint 3 | relates to | E5 Covenant alerts shown in Drawdowns |
| R1 Drawdowns needs Conditions API v2 before sprint 3 | relates to | E9 Conditions API v2 |
| R2 Credit Application needs the covenant event feed for alert emails | relates to | E6 Alert emails from Credit Application |
| R3 Drawdowns needs the evidence export format agreed | relates to | E2 M&P for Drawdowns |
| R3 Drawdowns needs the evidence export format agreed | relates to | E3 Evidence pack for conditions |
| R4 Covenant test environment needed from Group IT | relates to | E4 Covenant trigger rules |
| R5 Drawdowns loses two engineers in January | relates to | I1 M&P across the platform |
| R6 Audit may widen the scope of the access finding | relates to | C1 Avoid audit risk through access control |
| R7 Covenant data for legacy facilities is incomplete | relates to | E4 Covenant trigger rules |
| R8 Group IT will keep the current role service until June | relates to | I1 M&P across the platform |
| M1 MILESTONE: audit point AP-12 remediation due | is blocked by | I1 M&P across the platform |
| M2 MILESTONE: M&P live in all origination applications | is blocked by | I1 M&P across the platform |

### 4.3 Flags: 2

Add the flag (right-click the card on the board, or More > Add flag) to **E4** Covenant trigger rules and **S1** Role checks on the drawdown approval screen.

### 4.4 Sprint: 6 tickets

On the board's backlog, create a sprint named `PI 5 S3 mock`, put S1, S2, S3, S4, S6 and B1 into it, and start it.

### 4.5 Leave one ticket unassigned

**R4** has no assignee on purpose: it should appear in "dependencies without an owner or date".

## 5. The dependencies you can raise in the mock-up

Four dependency tickets and two blocks links cover every case in section 12 of the white paper.

| What | Case | Tickets | What it shows |
| --- | --- | --- | --- |
| Drawdowns needs Credit Application's part of M&P first | A: two applications inside the same Initiative | E1 blocks E2. No RAID ticket. | A dependency inside a Feature is just a link |
| Drawdowns needs Conditions API v2 | B: work from a team outside the Initiative, agreed, **but promised 14 days after it is needed** | R1, linked to E5 (waiting) and E9 (supplier); E9 blocks E5 | A date conflict on the dependency board; E5 is therefore stretch, not committed |
| Credit Application needs the covenant event feed | B: asked, **not yet agreed** | R2, linked to E6 | The "asked, not agreed" list |
| Drawdowns needs the evidence export format | B: agreed, **on track** (promised 15 days before it is needed) | R3, linked to E2 and E3 | A healthy dependency, for contrast |
| A test environment from Group IT | C: an outside party, **overdue and with no owner** | R4, linked to E4 | The "past need-by date" and "no owner" lists |

Three more to raise yourself once the dashboards work, to see them react:

1. Raise a new Dependency for E7 (the spillover Epic) with a need-by date next week and no supplier answer. It should appear at the top of "not agreed" and in "late or due soon".
2. Accept R2: move it to In Progress and set Baseline End a week before its Due date. It should leave "not agreed" and show a positive margin.
3. Fix R1: change its Baseline End to before its Due date. The conflict should disappear from the dependency board.

## 6. Saved filters for one project

Create them in this order; later ones refer to earlier ones by name. The last two columns say what each should return once the mock tickets exist.

| Save as | Query | Should return | Which |
| --- | --- | --- | --- |
| `MOCK: all` | `project = CL123 AND labels = mock` | 38 | all 38 |
| `MOCK PI planned Initiatives` | `filter = "MOCK: all" AND issuetype = Initiative AND "Target PI" = "PI 5"` | 5 | I1, I2, I3, I4, I5 |
| `MOCK PI planned Epics` | `filter = "MOCK: all" AND issuetype = Epic AND "Target PI" = "PI 5"` | 7 | E1, E2, E3, E4, E5, E6, E9 |
| `MOCK: spillover` | `filter = "MOCK: all" AND issuetype in (Initiative, Epic) AND "Target PI" in ("PI 4") AND labels = pi-committed AND status not in (Released, Done)` | 2 | I7, E7 |
| `MOCK: PI Epics` | `filter = "MOCK PI planned Epics" OR (filter = "MOCK: spillover" AND issuetype = Epic) OR (filter = "MOCK: all" AND issuetype = Epic AND status = Implementing)` | 9 | E1, E2, E3, E4, E5, E6, E7, E8, E9 |
| `MOCK: current PI Initiatives` | `filter = "MOCK PI planned Initiatives" OR (filter = "MOCK: all" AND issuetype = Initiative AND status in (Implementing, Testing, Validation))` | 6 | I1, I2, I3, I4, I5, I7 |
| `MOCK: committed Initiatives` | `filter = "MOCK PI planned Initiatives" AND labels = pi-committed` | 4 | I1, I2, I3, I4 |
| `MOCK: committed and released` | `filter = "MOCK: committed Initiatives" AND status in (Released, Done)` | 1 | I2 |
| `MOCK: unplanned in PI` | `filter = "MOCK PI planned Initiatives" AND labels = unplanned` | 1 | I5 |
| `MOCK: open Capabilities` | `filter = "MOCK: all" AND issuetype = Capability AND status not in (Idea, Done) ORDER BY Rank` | 3 | C1, C2, C3 |
| `MOCK: all Initiatives` | `filter = "MOCK: all" AND issuetype = Initiative` | 8 | I1, I2, I3, I4, I5, I6, I7, I8 |
| `MOCK: Red and Amber` | `(filter = "MOCK: current PI Initiatives" OR filter = "MOCK: PI Epics" OR filter = "MOCK: open Capabilities") AND "RAG Status" in (Red, Amber) AND status not in (Released, Done)` | 8 | C1, C2, I1, I3, I7, E2, E4, E7 |
| `MOCK: Management Attention and Red` | `filter = "MOCK: all" AND issuetype in (Initiative, Capability) AND status not in (Released, Done) AND (labels = mgmt-attention OR "RAG Status" = Red)` | 2 | C2, I3 |
| `MOCK: Amber or Red without a plan` | `filter = "MOCK: Red and Amber" AND issuetype != Epic AND "RAG Description" is EMPTY` | 1 | I3 |
| `MOCK: intake waiting` | `filter = "MOCK: all" AND issuetype in (Initiative, Capability) AND status = Idea ORDER BY created` | 1 | I6 |
| `MOCK: Ready, no Target PI` | `filter = "MOCK: all" AND issuetype = Initiative AND status = Ready AND "Target PI" is EMPTY ORDER BY WSJF DESC` | 1 | I8 |
| `MOCK: Initiatives with gaps` | `filter = "MOCK: all" AND issuetype = Initiative AND status not in (Idea, Analysis, Done) AND ("Parent Link" is EMPTY OR "RAG Status" is EMPTY OR "Value Stream and Sub-Value Stream" is EMPTY)` | 1 | I5 |
| `MOCK: regulatory Initiatives` | `filter = "MOCK: all" AND issuetype = Initiative AND "Is it Regulatory" = Yes AND status not in (Released, Done)` | 1 | I1 |
| `MOCK: PI Epics not started` | `filter = "MOCK: PI Epics" AND status in (Idea, Analysis, Ready)` | 1 | E5 |
| `MOCK: flagged` | `filter = "MOCK: all" AND Flagged = Impediment` | 2 | E4, S1 |
| `MOCK: hygiene exceptions` | `filter = "MOCK: all" AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` | 1 | E8 |
| `MOCK: open RAID` | `filter = "MOCK: all" AND issuetype = "Delivery RAID" AND statusCategory != Done` | 8 | R1, R2, R3, R4, R5, R6, R7, R8 |
| `MOCK: open Red and Amber RAID` | `filter = "MOCK: open RAID" AND "RAG Status" in (Red, Amber) ORDER BY duedate` | 5 | R1, R2, R4, R5, R7 |
| `MOCK: risks not reviewed` | `filter = "MOCK: open RAID" AND "RAID Type" = Risk AND "ROAM Response" is EMPTY` | 1 | R6 |
| `MOCK: RAID past its date` | `filter = "MOCK: open RAID" AND duedate < now()` | 2 | R4, R6 |
| `MOCK: milestones next 90 days and overdue` | `filter = "MOCK: all" AND labels = milestone AND statusCategory != Done AND duedate <= endOfDay("+90d") ORDER BY duedate` | 2 | M1, M2 |
| `MOCK: open dependencies` | `filter = "MOCK: open RAID" AND "RAID Type" = Dependency ORDER BY duedate` | 4 | R1, R2, R3, R4 |
| `MOCK: dependencies not agreed` | `filter = "MOCK: open dependencies" AND status = Backlog ORDER BY duedate` | 2 | R2, R4 |
| `MOCK: dependencies agreed` | `filter = "MOCK: open dependencies" AND status = "In Progress"` | 2 | R1, R3 |
| `MOCK: dependencies late or due soon` | `filter = "MOCK: open dependencies" AND duedate <= endOfDay("+28d") ORDER BY duedate` | 3 | R1, R2, R4 |
| `MOCK: dependencies at risk` | `filter = "MOCK: open dependencies" AND "RAG Status" in (Amber, Red)` | 3 | R1, R2, R4 |
| `MOCK: dependencies without an owner or date` | `filter = "MOCK: open dependencies" AND (assignee is EMPTY OR duedate is EMPTY)` | 1 | R4 |
| `MOCK release: scope` | `filter = "MOCK: all" AND fixVersion = "CL123 2027.01"` | 5 | E1, E2, S1, S2, B1 |
| `MOCK release: not finished` | `filter = "MOCK: all" AND fixVersion = "CL123 2027.01" AND status not in (Released, Done)` | 3 | E2, S1, B1 |
| `MOCK release: open bugs` | `filter = "MOCK: all" AND fixVersion = "CL123 2027.01" AND issuetype = Bug AND statusCategory != Done` | 1 | B1 |
| `MOCK team: flagged in sprint` | `filter = "MOCK: all" AND sprint in openSprints() AND Flagged = Impediment` | 1 | S1 |
| `MOCK team: open Epics` | `filter = "MOCK: all" AND issuetype = Epic AND status not in (Released, Done)` | 7 | E2, E4, E5, E6, E7, E8, E9 |
| `MOCK team: open bugs` | `filter = "MOCK: all" AND issuetype = Bug AND statusCategory != Done` | 1 | B1 |
| `MOCK team: Stories without Epic` | `filter = "MOCK: all" AND issuetype = Story AND "Epic Link" is EMPTY AND statusCategory != Done` | 1 | S5 |

Two filters from the white paper are left out because they depend on the `issueLinkType` query field, which may not exist on this Jira version. Try this once: `filter = "MOCK: all" AND issueLinkType = "is blocked by"`. If it works it should return E2, E5, M1 and M2. If it gives an error, that answers proof-of-concept check 10.

## 7. The dashboards, and what each panel should show

"2D" is the gadget Two Dimensional Filter Statistics.

### Dashboard 1: Value stream portfolio

| Gadget | Filter | Should show |
| --- | --- | --- |
| Filter Results (RAG Status, Due date) | MOCK: open Capabilities | 3 (C1, C2, C3) |
| Pie Chart by RAG Status | MOCK: open Capabilities | 1 Green, 1 Amber, 1 Red |
| 2D, Status by RAG Status | MOCK: open Capabilities | Implementing: 1 Amber, 1 Red. Analysis: 1 Green. |
| Filter Results (RAG Description) | MOCK: Management Attention and Red | 2 (C2, I3) |
| Filter Results, by Due date | MOCK: milestones next 90 days and overdue | 2 (M1, M2); M2 is overdue |
| 2D, RAID Type by RAG Status | MOCK: open RAID | Dependency: 1 Green, 2 Amber, 1 Red. Risk: 1 Green, 1 Amber. Issue: 1 Red. Assumption: 1 Green. |
| Filter Results | MOCK: intake waiting | 1 (I6) |
| Created vs Resolved | MOCK: all Initiatives | A flat line: all created on the same day. Not meaningful in a mock-up. |

### Dashboard 2: Initiatives across the value stream

| Gadget | Filter | Should show |
| --- | --- | --- |
| Filter Results (Parent Link, sub value stream, RAG, Target PI, Due date) | MOCK: current PI Initiatives | 6 (I1, I2, I3, I4, I5, I7) |
| 2D, Status by RAG Status | MOCK: current PI Initiatives | Implementing: 2 Green, 2 Amber, 1 Red. Released: 1 Green. |
| Pie Chart by Status | MOCK: committed Initiatives | 4 (I1, I2, I3, I4): 3 Implementing, 1 Released |
| Filter Results (RAG Description) | MOCK: Red and Amber, with issuetype = Initiative | I1, I3, I7 |
| Filter Results, by score | MOCK: Ready, no Target PI | 1 (I8) |
| Filter Results | MOCK: regulatory Initiatives | 1 (I1) |
| Filter Results | MOCK: unplanned in PI | 1 (I5) |
| Filter Results | MOCK: Initiatives with gaps | 1 (I5) |

### Dashboard 3: Epics across applications

| Gadget | Filter | Should show |
| --- | --- | --- |
| 2D, Component by Status | MOCK: PI Epics | Credit Application: 1 Released, 2 Implementing. Drawdowns: 2 Implementing, 1 Ready. Governance and Conditions: 1 Released, 2 Implementing. |
| 2D, Component by RAG Status | MOCK: PI Epics | Credit Application: 2 Green, 1 Amber. Drawdowns: 2 Green, 1 Amber. Governance and Conditions: 2 Green, 1 Red. |
| 2D, Component by Target PI | MOCK: spillover | 2 (I7, E7); E7 under Credit Application |
| Filter Results | MOCK: PI Epics not started | 1 (E5) |
| Filter Results | MOCK: flagged | 2 (E4, S1) |
| Filter Results | MOCK: Amber or Red without a plan | 1 (I3) |
| Filter Results | MOCK: hygiene exceptions | 1 (E8) |

### Dashboard 4: Risks, dates and releases

| Gadget | Filter | Should show |
| --- | --- | --- |
| Filter Results | MOCK: open Red and Amber RAID | 5 (R1, R2, R4, R5, R7) |
| Filter Results | MOCK: open dependencies | 4 (R1, R2, R3, R4) |
| Filter Results | MOCK: risks not reviewed | 1 (R6) |
| Filter Results | MOCK: RAID past its date | 2 (R4, R6) |
| Filter Results | MOCK: milestones next 90 days and overdue | 2 (M1, M2) |
| 2D, Component by Status | MOCK release: scope | 5 (E1, E2, S1, S2, B1) |
| Pie Chart by Priority or Severity | MOCK release: open bugs | 1 (B1) |

### Dashboard 5: Team

| Gadget | Source | Should show |
| --- | --- | --- |
| Sprint Health, Sprint Burndown | The board, sprint `PI 5 S3 mock` | 6 tickets: 2 Done, 3 In Progress, 1 not started |
| Filter Results | MOCK team: flagged in sprint | 1 (S1) |
| 2D, Status by Fix Version | MOCK team: open Epics | 7 (E2, E4, E5, E6, E7, E8, E9) |
| Pie Chart | MOCK team: open bugs | 1 (B1) |
| Filter Results | MOCK: hygiene exceptions | 1 (E8) |
| Filter Results | MOCK team: Stories without Epic | 1 (S5) |

"Carried over" cannot be shown until a second sprint has been run.

### Dashboard 6: Dependencies

| Gadget | Filter | Should show |
| --- | --- | --- |
| Filter Results (Linked Issues, supplier, Due date) | MOCK: dependencies not agreed | 2 (R2, R4) |
| 2D, supplier by Status | MOCK: open dependencies | Governance and Conditions: 1 Backlog, 2 In Progress. No supplier: 1 Backlog. |
| 2D, sub value stream by RAG Status | MOCK: open dependencies | Drawdown: 1 Red, 1 Green. Monitoring: 2 Amber. |
| Filter Results, by Due date | MOCK: dependencies late or due soon | 3 (R1, R2, R4) |
| Filter Results | MOCK: flagged | 2 (E4, S1) |
| Filter Results | MOCK: dependencies at risk | 3 (R1, R2, R4) |
| Filter Results | MOCK: dependencies without an owner or date | 1 (R4) |

If a 2D gadget refuses the sub value stream or supplier field as an axis, that answers proof-of-concept check 4; use the Confluence table in section 8 for those panels.

## 8. The Confluence pages, and what each should show

Use the recipes in the [Confluence guide](../../confluence/CONFLUENCE_PORTFOLIO_GUIDE.md), with two changes for one project: use the MOCK filters, and use **Component** wherever a recipe says Project.

| Page | Recipe | Filters | Should show |
| --- | --- | --- | --- |
| Feature progress across applications (figure 9) | 4.2a | MOCK: PI Epics; MOCK: current PI Initiatives | I1: Credit Application Released, Drawdowns Implementing, so "1 of 2, still open in Drawdowns". I2: Governance and Conditions Released. I3: Governance and Conditions Implementing, Drawdowns Ready. I4: Governance and Conditions Implementing. I5: Credit Application Implementing. I7: Credit Application Implementing. E8 has no parent and drops out of the join. |
| Dependency board (figure 17, part 2) | 4.16 | MOCK: open dependencies | R1: margin -14 days, "Date conflict". R2: "Asked, not agreed". R3: margin +15 days, "Agreed". R4: "Asked, not agreed", past its need-by date. |
| Epics by application and sprint (figure 17, part 1) | 4.14 | MOCK: PI Epics | Epics spread across the sprint columns by End Date. Use the first day of your PI in the query. |
| Load against capacity (figure 8) | 4.15 | MOCK: PI Epics, and a typed capacity table with a number for each Component | Committed points: Credit Application 34, Drawdowns 34, Governance and Conditions 55. Stretch: Credit Application 8, Drawdowns 13. |
| Portfolio tree | 4.1 | MOCK: open Capabilities; MOCK: all Initiatives | C1: 3 Initiatives, 1 Released. C2: 2 Initiatives, 1 Red. C3: 2 Initiatives. |
| PI scorecard | 4.7 | Paste the result of MOCK: committed Initiatives as the baseline table | 4 committed lines; 1 delivered (I2) |
| Role pages | 4.17 | The MOCK filters | Delivery lead: 2 flagged, 2 asks not agreed, 1 date conflict, 1 Epic not started |

Where a recipe joins on Parent Link, look first at what that column shows in the Jira Issues macro (a key, or a key with the summary); that decides whether to join on Key or on Summary.

## 9. What the mock-up cannot show

| Panel | Why not | What to do |
| --- | --- | --- |
| Analysis over 30 days; RAG not refreshed in 14 days | They depend on time passing | Leave the mock in place for a month, or trust the query |
| Created against resolved, predictability trend, velocity history | They need several PIs of history | Not testable in a mock-up |
| Milestone slippage | No Milestone issue type on Data Center | Test after the move to Cloud, or check whether Task carries Baseline End |
| Hierarchy queries across projects | Everything is in one project | Covered by the proof-of-concept slice in real projects |
| The intake hand-over from the service management project | It is a different project | Proof-of-concept check 12 |

## 10. Clean-up

Search `project = CL123 AND labels = mock`, select all, and delete or move them when you have finished. Delete the filters and dashboards whose names start with MOCK.
