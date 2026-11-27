"""Writes MOCKUP_GUIDE.md from the fragments produced by build_mockup.py. Run build_mockup.py first."""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(D, "_fragments.json")))
E = json.load(open(os.path.join(D, "_expected.json")))
def e(n): return f'{len(E[n])} ({", ".join(E[n])})' if E[n] else "0"

doc = f'''# Mock-up in one Jira project

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
| Milestone slippage (Baseline End Date against Due date) | Not tested | A Task may not carry Baseline End Date |

Every mock ticket carries the label `mock`, so the filters never pick up anything else in the project and the tickets are easy to find and delete afterwards.

**Change these three things first if yours differ**, in `build_mockup.py` or by hand:

- the project key: `CL123`
- the current and previous PI as your Target PI field writes them: `PI 2026.4` and `PI 2026.3`
- the release name: `CL123 2027.01`

Dates in the tables were worked out from 27 November 2026. If you build the mock-up much later, move the dates by the same number of days, or the "late" and "due soon" panels will show different tickets.

## 2. Before creating tickets

- [ ] Three Components exist in the project: Credit Application, Drawdowns, Governance and Conditions.
- [ ] One version exists: `CL123 2027.01`, with a release date about six weeks ahead.
- [ ] The issue types Capability, Initiative, Epic, Story, Bug, Task and Delivery RAID can be created in the project.
- [ ] You know the exact values your fields accept for: Target PI, RAG Status, RAID Type, ROAM Response, Probability, Impact, Severity, Enabler Type, Regulatory or Control Change Type, Management Attention. The tables use placeholders; use your own values with the same meaning.
- [ ] A Scrum board exists on the project (needed only for the team dashboard).

If a field in the tables is not on the screen for that issue type, skip it and note it: that is itself a finding for the proof of concept.

## 3. The tickets to create

Create them in this order, because each level needs the one above as its parent. The ID in the first column is only a name for this guide; write the real Jira key beside it in the Key map sheet as you go.

### 3.1 Capabilities (3)

Fields on every Capability: Summary, Status, RAG Status, Due date, Value Stream and Sub-Value Stream, Assignee, Labels. Path to Green where shown.

{G["cap"]}

### 3.2 Initiatives (8)

Fields: Summary, Parent Link, Status, Target PI, Actual PI, RAG Status, Labels, Due date, Value Stream and Sub-Value Stream, Assignee, and the extras in the last column. "Scores" are the four scoring fields in the order value, time criticality, risk reduction, job size.

{G["ini"]}

I6 has no parent and almost no fields on purpose: it is raw intake. I5 has no sub value stream on purpose: it should appear in the "gaps" list.

### 3.3 Epics (9)

Fields: Summary, Epic Name, Parent Link, Component, Status, Target PI, Actual PI, RAG Status, Labels, End Date, Story Points, Fix version, Assignee.

{G["epic"]}

E8 has no parent on purpose: it should appear in the hygiene list. E7 has last PI as its Target PI on purpose: it is the spillover.

### 3.4 Stories and Bugs (8)

Fields: Summary, Epic Link, Component, Status, Story Points (stories), Severity (bugs), Fix version, Assignee.

{G["story"]}

### 3.5 Delivery RAID (8)

Fields: Summary, RAID Type, Status, RAG Status, Due date, Value Stream and Sub-Value Stream (who is affected or waiting), Component, Impact, Assignee. For a Dependency: Supplier Value Stream and Sub Value Stream, and Baseline End Date once agreed. For a Risk: Probability and ROAM Response.

On a Dependency, **Due date is the date the receiver needs it** and **Baseline End Date is the date the supplier promised**.

{G["raid"]}

### 3.6 Milestone stand-ins (2 Tasks)

{G["ms"]}

## 4. What to set by hand after the tickets exist

### 4.1 Parents (Parent Link): 15 tickets

{G["parents"]}

### 4.2 Links: 14

{G["links"]}

### 4.3 Flags: 2

Add the flag (right-click the card on the board, or More > Add flag) to **E4** Covenant trigger rules and **S1** Role checks on the drawdown approval screen.

### 4.4 Sprint: 6 tickets

On the board's backlog, create a sprint named `PI 2026.4 S3 mock`, put S1, S2, S3, S4, S6 and B1 into it, and start it.

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
2. Accept R2: move it to In Progress and set Baseline End Date a week before its Due date. It should leave "not agreed" and show a positive margin.
3. Fix R1: change its Baseline End Date to before its Due date. The conflict should disappear from the dependency board.

## 6. Saved filters for one project

Create them in this order; later ones refer to earlier ones by name. The last two columns say what each should return once the mock tickets exist.

{G["jql"]}

Two filters from the white paper are left out because they depend on the `issueLinkType` query field, which may not exist on this Jira version. Try this once: `filter = "MOCK: all" AND issueLinkType = "is blocked by"`. If it works it should return E2, E5, M1 and M2. If it gives an error, that answers proof-of-concept check 10.

## 7. The dashboards, and what each panel should show

"2D" is the gadget Two Dimensional Filter Statistics.

### Dashboard 1: Value stream portfolio

| Gadget | Filter | Should show |
| --- | --- | --- |
| Filter Results (RAG Status, Due date) | MOCK: open Capabilities | {e("MOCK: open Capabilities")} |
| Pie Chart by RAG Status | MOCK: open Capabilities | 1 Green, 1 Amber, 1 Red |
| 2D, Status by RAG Status | MOCK: open Capabilities | Implementing: 1 Amber, 1 Red. Analysis: 1 Green. |
| Filter Results (Path to Green) | MOCK: Management Attention and Red | {e("MOCK: Management Attention and Red")} |
| Filter Results, by Due date | MOCK: milestones next 90 days and overdue | {e("MOCK: milestones next 90 days and overdue")}; M2 is overdue |
| 2D, RAID Type by RAG Status | MOCK: open RAID | Dependency: 1 Green, 2 Amber, 1 Red. Risk: 1 Green, 1 Amber. Issue: 1 Red. Assumption: 1 Green. |
| Filter Results | MOCK: intake waiting | {e("MOCK: intake waiting")} |
| Created vs Resolved | MOCK: all Initiatives | A flat line: all created on the same day. Not meaningful in a mock-up. |

### Dashboard 2: Initiatives across the value stream

| Gadget | Filter | Should show |
| --- | --- | --- |
| Filter Results (Parent Link, sub value stream, RAG, Target PI, Due date) | MOCK: current PI Initiatives | {e("MOCK: current PI Initiatives")} |
| 2D, Status by RAG Status | MOCK: current PI Initiatives | Implementing: 2 Green, 2 Amber, 1 Red. Released: 1 Green. |
| Pie Chart by Status | MOCK: committed Initiatives | {e("MOCK: committed Initiatives")}: 3 Implementing, 1 Released |
| Filter Results (Path to Green) | MOCK: Red and Amber, with issuetype = Initiative | I1, I3, I7 |
| Filter Results, by score | MOCK: Ready, no Target PI | {e("MOCK: Ready, no Target PI")} |
| Filter Results | MOCK: regulatory Initiatives | {e("MOCK: regulatory Initiatives")} |
| Filter Results | MOCK: unplanned in PI | {e("MOCK: unplanned in PI")} |
| Filter Results | MOCK: Initiatives with gaps | {e("MOCK: Initiatives with gaps")} |

### Dashboard 3: Epics across applications

| Gadget | Filter | Should show |
| --- | --- | --- |
| 2D, Component by Status | MOCK: PI Epics | Credit Application: 1 Released, 2 Implementing. Drawdowns: 2 Implementing, 1 Ready. Governance and Conditions: 1 Released, 2 Implementing. |
| 2D, Component by RAG Status | MOCK: PI Epics | Credit Application: 2 Green, 1 Amber. Drawdowns: 2 Green, 1 Amber. Governance and Conditions: 2 Green, 1 Red. |
| 2D, Component by Target PI | MOCK: spillover | {e("MOCK: spillover")}; E7 under Credit Application |
| Filter Results | MOCK: PI Epics not started | {e("MOCK: PI Epics not started")} |
| Filter Results | MOCK: flagged | {e("MOCK: flagged")} |
| Filter Results | MOCK: Amber or Red without a plan | {e("MOCK: Amber or Red without a plan")} |
| Filter Results | MOCK: hygiene exceptions | {e("MOCK: hygiene exceptions")} |

### Dashboard 4: Risks, dates and releases

| Gadget | Filter | Should show |
| --- | --- | --- |
| Filter Results | MOCK: open Red and Amber RAID | {e("MOCK: open Red and Amber RAID")} |
| Filter Results | MOCK: open dependencies | {e("MOCK: open dependencies")} |
| Filter Results | MOCK: risks not reviewed | {e("MOCK: risks not reviewed")} |
| Filter Results | MOCK: RAID past its date | {e("MOCK: RAID past its date")} |
| Filter Results | MOCK: milestones next 90 days and overdue | {e("MOCK: milestones next 90 days and overdue")} |
| 2D, Component by Status | MOCK release: scope | {e("MOCK release: scope")} |
| Pie Chart by Priority or Severity | MOCK release: open bugs | {e("MOCK release: open bugs")} |

### Dashboard 5: Team

| Gadget | Source | Should show |
| --- | --- | --- |
| Sprint Health, Sprint Burndown | The board, sprint `PI 2026.4 S3 mock` | 6 tickets: 2 Done, 3 In Progress, 1 not started |
| Filter Results | MOCK team: flagged in sprint | {e("MOCK team: flagged in sprint")} |
| 2D, Status by Fix Version | MOCK team: open Epics | {e("MOCK team: open Epics")} |
| Pie Chart | MOCK team: open bugs | {e("MOCK team: open bugs")} |
| Filter Results | MOCK: hygiene exceptions | {e("MOCK: hygiene exceptions")} |
| Filter Results | MOCK team: Stories without Epic | {e("MOCK team: Stories without Epic")} |

"Carried over" cannot be shown until a second sprint has been run.

### Dashboard 6: Dependencies

| Gadget | Filter | Should show |
| --- | --- | --- |
| Filter Results (Linked Issues, supplier, Due date) | MOCK: dependencies not agreed | {e("MOCK: dependencies not agreed")} |
| 2D, supplier by Status | MOCK: open dependencies | Governance and Conditions: 1 Backlog, 2 In Progress. No supplier: 1 Backlog. |
| 2D, sub value stream by RAG Status | MOCK: open dependencies | Drawdown: 1 Red, 1 Green. Monitoring: 2 Amber. |
| Filter Results, by Due date | MOCK: dependencies late or due soon | {e("MOCK: dependencies late or due soon")} |
| Filter Results | MOCK: flagged | {e("MOCK: flagged")} |
| Filter Results | MOCK: dependencies at risk | {e("MOCK: dependencies at risk")} |
| Filter Results | MOCK: dependencies without an owner or date | {e("MOCK: dependencies without an owner or date")} |

If a 2D gadget refuses the sub value stream or supplier field as an axis, that answers proof-of-concept check 4; use the Confluence table in section 8 for those panels.

## 8. The Confluence pages, and what each should show

Use the recipes in the [Confluence guide](../confluence/CONFLUENCE_PORTFOLIO_GUIDE.md), with two changes for one project: use the MOCK filters, and use **Component** wherever a recipe says Project.

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
| Milestone slippage | No Milestone issue type on Data Center | Test after the move to Cloud, or check whether Task carries Baseline End Date |
| Hierarchy queries across projects | Everything is in one project | Covered by the proof-of-concept slice in real projects |
| The intake hand-over from the service management project | It is a different project | Proof-of-concept check 12 |

## 10. Clean-up

Search `project = CL123 AND labels = mock`, select all, and delete or move them when you have finished. Delete the filters and dashboards whose names start with MOCK.
'''
open(os.path.join(D, "MOCKUP_GUIDE.md"), "w").write(doc)
print("guide written", len(doc.split("\n")), "lines")
