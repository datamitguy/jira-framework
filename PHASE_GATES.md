# Phase by phase: how to enter and exit each stage in Jira

For each stage of the life of a piece of work, this page says what must be true to enter it, what you do in Jira while you are in it, what must be true to leave it, and how anyone can see that in Jira.

It also answers a practical question: when are the filters created, and what has to be touched at each PI? The short answer is that filters are built once and are live. You do not rebuild anything when tickets change. A few small edits are made at each PI, on three set days (section 2).

All names are placeholders.

## 1. The stages at a glance

| # | Stage | Feature status | Epic status | Who leads |
| --- | --- | --- | --- | --- |
| 1 | New demand (a request in the demand intake project) | not yet a Feature | | Intake owner, then the DDT |
| 2 | Triage | Idea | | Product lead |
| 3 | Design | Analysis | Idea, Analysis | Product lead, product owners |
| 4 | Ready, waiting for a PI | Ready | Ready | Product lead |
| 5 | PI planning | Ready | Ready | Delivery lead |
| 6 | Delivery | Implementing | Implementing | Product owners, teams |
| 7 | Testing and acceptance | Testing, Validation | Implementing | Product lead |
| 8 | Release | Released | Released | Delivery lead |
| 9 | Early life and close | Done | Done | Product lead |
| 10 | PI close | | | Delivery lead |

A ticket's status is the evidence of which stage it is in. Nobody keeps a separate tracker.

## 2. When the filters are created and changed

**Filters are live.** A saved filter is a question Jira answers again every time someone opens it. When a product owner sets Target PI on an Epic during planning, that Epic appears in the PI filters, the dashboards and the Confluence pages straight away. Nothing is recreated and nothing is "rolled up" by hand.

**Built once, at set-up:** every filter in the library, the dashboards and the Confluence pages.

**Touched at each PI, on these days:**

| When | What | Who | Why then |
| --- | --- | --- | --- |
| Week 9 of the current PI, when drafting the next PI begins | Create two new filters: `PI <next> planned Features` and `PI <next> planned Epics`. Copy the PI plan page in Confluence for the next PI and change its filter and start date. | Delivery lead | The draft plan can be watched filling up before and during planning |
| The day planning closes (the lock) | Paste the committed list from those two filters, and the dependency board, into the new PI scorecard page | Delivery lead | This is the baseline. It is taken once and never edited. |
| Day 1 of the new PI | Repoint `VS: PI planned Features` and the first part of `VS: PI Epics` to the new PI's filters | Delivery lead | Until day 1 the dashboards should still show the PI that is finishing |
| Day 1 of the new PI | Add the PI that has just ended to the list in `VS: spillover` | Delivery lead | From this day its unfinished committed work counts as spillover |
| Day 1 of the new PI | Change the PI value in automation rule 4 and in the board quick filter | Delivery lead | So Actual PI is stamped with the right PI |

Old per-PI filters are kept and never edited, because old scorecards read them.

**The filter `VS: PI Epics`**

```text
VS: PI Epics =
      filter = "PI 2027.1 planned Epics"
   OR (filter = "VS: spillover" AND issuetype = Epic)
   OR (issuetype = Epic AND project in (CA, DRAW, FL) AND status = Implementing)
```

It means "every Epic the value stream is working on in this PI", and it has three parts:

| Part | Picks up | Why it is there |
| --- | --- | --- |
| 1 | Epics whose Target PI is this PI | The plan |
| 2 | Committed Epics from an earlier PI that are still not Released | Carried-over work, so it sits beside the new plan and takes capacity first |
| 3 | Any Epic that is actually in progress, whatever its Target PI | Catches work started outside the plan, so nothing in progress is hidden |

You create it once. At each PI you change only the name inside part 1. Parts 2 and 3 look after themselves.

## 3. Stage by stage

### Stage 1: New demand

The front door is the demand intake project in Jira Service Management. The full steps are in WAYS_OF_WORKING.md, section 5.

| | |
| --- | --- |
| **Enter when** | Someone wants something that is in nobody's backlog. Work already on a team's Epic list does not come here; it is stitched to a Feature. |
| **What happens** | A request is raised through the portal. The intake owner screens and routes it within 5 working days. A product lead assesses it within 10: the VS Epic it would serve, a rough size, the applications likely to change, a proposed PI. |
| **Exit when** | The DDT, the advisory board forum for new demand, approves, declines, parks or merges it, recorded on the request in the meeting. |
| **On exit, in Jira** | On approval, a **Feature** is created in the portfolio project, status **Idea**, linked to the request, with its text copied (by automation, or by the product lead with "Create linked issue"). If it is clearly larger than one PI, the value stream lead creates a **VS Epic** and the request is linked to that. The requester is notified on the request. |
| **How to see it** | The intake queue in the demand intake project; `VS: intake waiting` lists every Feature in Idea. |

### Stage 2: Triage

| | |
| --- | --- |
| **Enter when** | A Feature exists in status Idea (from an approved request, or created during stitching). |
| **What you do in Jira** | Set Value Stream and Sub-Value Stream, Enabler Type, and Parent Link to the VS Epic. Assign the product lead. |
| **Exit when** | The product lead has capacity to shape it, and the three fields above are set. |
| **On exit, in Jira** | Move the Feature to **Analysis**. Or close it as a duplicate or Won't Do with a reason. |
| **How to see it** | Weekly backlog triage on the Feature board, Idea column. Anything waiting over a week is discussed. |

### Stage 3: Design

| | |
| --- | --- |
| **Enter when** | Feature is in **Analysis** with parent, sub value stream and Enabler Type set. |
| **What you do in Jira** | On the Feature: fill in Acceptance Criteria and Business Benefits; link the design page; raise sign-off tasks (architecture, risk, control) assigned to the approvers; fill in T-Shirt Size and the four scores. For each application that must change: its product owner creates an **Epic** with Parent Link to the Feature and a Story Points estimate. Link dependencies with **blocks**. Work from another application inside the same Feature is an Epic under the Feature, with a blocks link. For work from a team outside the Feature, or from outside Jira, the waiting product owner raises a Delivery RAID Dependency (white paper, section 12). For a fixed regulatory date: create the Milestone and link it. |
| **Exit when** | The definition of ready is met: parent, sub value stream and Enabler Type set; Acceptance Criteria and Business Benefits agreed with the sponsor; every application has an Epic with an estimate; design linked and sign-off tasks raised; dependencies linked; scores filled in (or Milestone for a regulatory date); fits one PI or is an agreed two-PI Feature. |
| **On exit, in Jira** | Product lead moves the Feature to **Ready** and places it in order on the board. Product owners move their Epics to **Ready** when the first two sprints of stories are written and estimated. |
| **How to see it** | `VS: Analysis over 30 days` shows Features stuck in design. `VS: Features with gaps` shows what is missing. |

### Stage 4: Ready, waiting for a PI

| | |
| --- | --- |
| **Enter when** | Feature and its Epics are in **Ready**. |
| **What you do in Jira** | Keep the order of the Ready column current. Nothing else. |
| **Exit when** | PI planning takes it, or it is closed. |
| **How to see it** | `VS: Ready, no Target PI`, sorted by score. This list is the proposal for the next PI. |

### Stage 5: PI planning

**Enter (weeks 7 to 10 of the PI before)**

| Week | Must be true | In Jira |
| --- | --- | --- |
| 7 | Features proposed for the next PI are at least in Analysis; new demand for that PI has closed | |
| 8 | Every ask to another team for the next PI has been raised | Delivery RAID Dependency tickets, status Backlog |
| 9 | Proposed Features are Ready | Delivery lead creates the two per-PI filters. Product leads set **Target PI** on proposed Features (the draft). |
| 10 | Each team's capacity is known; every ask has an answer; dependencies are linked | Capacity typed into the capacity table on the PI plan page in Confluence; sprints created and named; agreed dependency tickets In Progress with a promised date |

A Feature that is not Ready by week 9 does not enter planning.

**During planning**

1. Carried-over work is placed first.
2. Each product owner sets **Target PI** on the Epics they can take, and places stories into sprints on the team board, up to capacity.
3. For each Feature, the product lead checks every Epic has the Target PI. If one application cannot take its share: move the Feature, cut it down, or plan it over two PIs on purpose.
4. New dependencies are linked in the room. Unresolved ones become Delivery RAID tickets with an owner.
5. Each Epic that stays, then each Feature, gets `pi-committed` or `pi-stretch`, a date (End Date on an Epic, Due date on a Feature), and RAG Status Green.

**Exit (the lock)**

| Must be true | In Jira |
| --- | --- |
| Every committed Feature has all its Epics committed | Label and Target PI on each |
| Every team's load is within capacity | Capacity table on the PI plan page in Confluence |
| Every dependency has both ends planned, giver before receiver | Dependency board on the PI plan page: no negative or unknown margin |
| No committed Epic waits on an unagreed dependency | The dependency board, read at the lock. Such an Epic is stretch, not committed. |
| Risks raised in the room have an owner and a response | Delivery RAID tickets |
| Confidence vote taken | Comment on the planning Milestone |
| The delivery lead announces the lock | Committed list pasted into the PI scorecard page as the baseline |

After the lock, Target PI and the commitment labels change only by decision.

### Stage 6: Delivery

| | |
| --- | --- |
| **Enter when** | The PI has started and the Epic has Target PI, commitment label, RAG and Parent Link. |
| **On entry, in Jira** | Product owner moves the Epic to **Implementing** when its first story starts. The Feature moves to **Implementing** when its first Epic does. |
| **What you do in Jira** | Teams: story status daily, flags when stopped. Product owners weekly: Epic status, RAG, End Date, Fix versions, and a recovery plan if Amber or Red. Product leads weekly: Feature RAG. Delivery lead: blockers, RAID, Milestones. |
| **Changes to the plan** | Only by decision of the product lead and delivery lead. In: Target PI plus `unplanned`. Out: `pi-descoped` plus a reason. |
| **Exit when** | Every story in the Epic is Done and deployed to the test environment. |
| **How to see it** | Dashboards 6, 2 and 3. `VS: PI Epics not started` from week 5. `VS: open blockers`. `VS: Red and Amber`. |

### Stage 7: Testing and acceptance

| | |
| --- | --- |
| **Enter when** | Every story in every Epic of the Feature is Done and in the test environment. |
| **On entry, in Jira** | Product lead moves the Feature to **Testing**. Epics stay at Implementing until go-live. |
| **What you do in Jira** | Defects are raised as Bugs under the right Epic, with Severity, Testing Phase and Environment. |
| **Move to Validation when** | End-to-end test across applications has passed and no severity 1 or 2 Bug is open. Product lead moves the Feature to **Validation**. |
| **Exit when** | Business users have accepted it; sign-off tasks are closed by the approvers; no severity 1 or 2 Bug is open. |
| **How to see it** | `Release: open bugs`. The sign-off tasks on the Feature. |

### Stage 8: Release

**Enter**

| Must be true | In Jira |
| --- | --- |
| The release is on the change calendar | Delivery lead creates the Fix version in each application project, same name, with the go-live date |
| Scope is known | Fix version set on the Epics, Stories and Bugs going in |
| Two sprints before go-live | Release gadgets reviewed weekly: open work, open bugs, flags, linked RAID |
| One sprint before go-live: scope cut-off | Anything not Done is moved to the next version; the product lead is told |
| Features in scope have passed Validation | Feature status |
| Go or no-go decided through the change process | Decision recorded as a comment on the go-live Milestone; change record number in Change Request ID on the Epics |

**Exit**

| Must be true | In Jira |
| --- | --- |
| Deployed to production | Delivery lead marks the version as released in each project |
| | Product owners move Epics to **Released**. Automation fills in Actual PI. |
| Every Epic of a Feature is Released, Done or closed as Won't Do | Product lead moves the Feature to **Released**. Automation fills in Actual PI. |
| Milestone met | Milestone moved to Done, with the actual date in a comment |

A Feature is never Released while one of its Epics is still open. If one application is late, the Feature waits, or is split by decision at the PI review.

### Stage 9: Early life and close

| | |
| --- | --- |
| **Enter when** | Feature is **Released**. |
| **What you do in Jira** | Production defects are raised as Bugs with the incident reference. |
| **Exit when** | The early-life support period has ended with no open critical Bug, and Business Benefits have been looked at against what was expected. |
| **On exit, in Jira** | Epics, then the Feature, move to **Done**. When every planned Feature of a VS Epic is Released, the VS Epic moves to **Released**; it moves to **Done** when its outcome has been measured and recorded. |

### Stage 10: PI close

| | |
| --- | --- |
| **Enter when** | The last day of the PI (week 12). |
| **What you do in Jira and Confluence** | Score every committed line of the baseline: delivered, spilled, descoped, or stopped. Report the three figures (Features, Epics, story points). Give each spillover a reason and a decision: carry on, stop or split. Move unfinished stretch and unplanned work to the next PI or back to Ready. Record up to five improvement actions as tasks. |
| **Exit when** | The scorecard is complete, every spillover has a decision, and on day 1 of the new PI the four filter and rule edits in section 2 are done. |

## 4. What is kept up to date, from Epic level upward

The stage tables above say what must be true to move on. This section says what is maintained while work sits in a stage, and how often. Stories and below are covered in [JIRA_UPDATE_GUIDE.md](JIRA_UPDATE_GUIDE.md). The full list of fields per issue type is in [FIELDS.md](FIELDS.md).

### By rhythm

| How often | Epic (product owner) | Feature (product lead) | VS Epic (value stream lead) | Milestone and Delivery RAID (delivery lead) |
| --- | --- | --- | --- | --- |
| **The same day** | Flag on or off when actually stopped or freed. Status when it changes. A new dependency: link the two Epics with blocks if they are under the same Feature; otherwise raise an ask as a Delivery RAID Dependency. An ask addressed to you: answer within five working days. | Flag. Management Attention when a decision is needed now. | Flag. | A new risk, issue or outside dependency raised as a ticket with an owner. |
| **Weekly, before the delivery sync** | Status. RAG Status. End Date still true. Fix versions. Recovery plan if Amber or Red. Links to other Epics. | Status against its Epics. RAG Status. Path to Green and Date to Green if Amber or Red. Due date still true. Executive Summary if Amber, Red or on the watch list. | | Blockers past their date chased. Flags reviewed. |
| **Fortnightly, before the portfolio sync** | | | Status. RAG Status. Executive Summary. Path to Green and Date to Green if Amber or Red. Rank order. | Every Red and Amber RAID ticket: RAG, Due date, a comment. Milestones: Due date, RAG. |
| **Monthly** | Hygiene check: no Epic without Parent Link; nothing open with a resolution. | Hygiene check: no Feature without parent, sub value stream or Enabler Type. | Work in progress against the limit. | Every open RAID ticket reviewed or closed. Risks: Probability, Impact, ROAM Response. |
| **Each sprint** | Fix versions on what is going into the next release. Story Points on the Epic revised once its stories are estimated. | | | Release versions and dates. |
| **Each PI, at planning** | Target PI. `pi-committed` or `pi-stretch`. End Date. RAG set to Green. Story Points. | Target PI. `pi-committed` or `pi-stretch`. Due date. RAG set to Green. Scores re-checked for anything still waiting. | Start date and End Date for the roadmap. Scores re-checked for anything still waiting. | Planning Milestone. Dependencies from the room. |
| **Each PI, at the close** | Reason for any spillover, as a comment. | Change Reason for anything descoped, split or carried over. | Executive Summary reflects the PI result. | Scorecard completed. `unplanned` and `pi-descoped` labels checked. |
| **Once, then left alone** | Parent Link, Epic Name, Components, Team. | Parent Link, sub value stream, Enabler Type, Acceptance Criteria, Business Benefits, T-Shirt Size. | Objective ID, Business Benefits, sub value stream. | Baseline End Date. RAID Type. Kind label on a Milestone. |
| **Never typed** | Actual PI; sub value stream (copied from the Feature once rule 1 exists). | Actual PI; Weighted Shortest Job First Score. | Weighted Shortest Job First Score. | |

Nothing at Epic level or above needs a daily update unless something actually changed that day. The daily habit belongs to stories.

### By stage

What is being maintained while a ticket sits in each stage.

| Stage | On the Epic | On the Feature | On the VS Epic |
| --- | --- | --- | --- |
| 2 Triage | | Set once: Parent Link, sub value stream, Enabler Type, Assignee. | Review: Assignee, Objective ID, sub value stream. |
| 3 Design | Set once: Parent Link, Epic Name, Components, Team, Story Points. Links as dependencies are found. | Built up weekly: Acceptance Criteria, Business Benefits, T-Shirt Size, the four scores, design link, sign-off tasks, links. | Analysis: Business Benefits, the four scores, case linked, first Features created. |
| 4 Ready | Nothing, unless the estimate changes. | Rank order on the board. Scores re-checked each PI. | Rank order. Start date and End Date. |
| 5 PI planning | Target PI, commitment label, End Date, RAG to Green. | Target PI, commitment label, Due date, RAG to Green. | Start date, End Date and Due date confirmed. |
| 6 Delivery | Weekly: Status, RAG, End Date, Fix versions, links, recovery plan if needed. Same day: flag. | Weekly: Status, RAG, Path to Green, Date to Green, Due date, Management Attention. | Fortnightly: Status, RAG, Executive Summary, Path to Green, Date to Green. |
| 7 Testing and acceptance | Weekly: RAG, Fix versions. Bugs raised under it carry Severity, Testing Phase, Environment. | Weekly: Status (Testing, then Validation), RAG, sign-off tasks closing. | Fortnightly, as above. |
| 8 Release | Fix versions final. Change Request ID. Status to Released. Actual PI appears. | Status to Released once every Epic is. Actual PI appears. | Status to Released once every planned Feature is. |
| 9 Early life and close | Status to Done when all child tickets are closed. | Business Benefits reviewed. Status to Done. | Business Benefits and any Financial Benefit recorded against what was promised. Status to Done. |
| 10 PI close | Spillover reason as a comment. Target PI left alone. | Change Reason if descoped, split or carried over. Target PI left alone for committed work. | Executive Summary updated with the PI result. |

**One note on Epics.** From the standards page, an Epic does not appear to have Path to Green, Date to Green or Due date. Until that is confirmed or the fields are added: the Epic's expected go-live date is its **End Date**, and the recovery plan for an Amber or Red Epic is a comment that starts "Path to green:".

## 5. One-page summary of the gates

| To move a Feature | From | To | You need |
| --- | --- | --- | --- |
| Into the portfolio | Request | Idea | Request approved at the DDT; the Feature is linked to it |
| Into design | Idea | Analysis | Parent VS Epic, sub value stream, Enabler Type |
| Out of design | Analysis | Ready | Definition of ready |
| Into a PI | Ready | Implementing | Target PI, commitment label, RAG; all Epics have Target PI; plan locked |
| Into test | Implementing | Testing | All stories of all Epics Done and in test |
| Into acceptance | Testing | Validation | End-to-end test passed; no severity 1 or 2 Bug |
| Into production | Validation | Released | Business acceptance; sign-offs closed; every Epic Released |
| Closed | Released | Done | Early-life support over; benefits reviewed |

| To move an Epic | From | To | You need |
| --- | --- | --- | --- |
| Into design | Idea | Analysis | Parent Link to the Feature; product owner assigned |
| Out of design | Analysis | Ready | Story Points; stories for two sprints written; dependencies linked |
| Into a PI | Ready | Implementing | Target PI, commitment label, RAG; first story started |
| Into production | Implementing | Released | Fix version released; Change Request ID |
| Closed | Released | Done | All child tickets closed |

These gates are checked by people today. Admin request 6 asks for Jira to enforce the main ones, so that a Feature cannot leave Analysis or enter Implementing with the fields missing.
