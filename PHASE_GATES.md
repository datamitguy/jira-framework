# Phase by phase: how to enter and exit each stage in Jira

For each stage of the life of a piece of work, this page says what must be true to enter it, what you do in Jira while you are in it, what must be true to leave it, and how anyone can see that in Jira.

It also answers a practical question: when are the filters created, and what has to be touched at each PI? The short answer is that filters are built once and are live. You do not rebuild anything when tickets change. Four small edits are made at each PI, on set days (section 2).

All names are placeholders.

## 1. The stages at a glance

| # | Stage | Feature status | Epic status | Who leads |
| --- | --- | --- | --- | --- |
| 1 | New demand (DDT) | not yet in Jira | | Owner of the DDT decision |
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
| Week 9 of the current PI, when drafting the next PI begins | Create two new filters: `PI <next> planned Features` and `PI <next> planned Epics` | Delivery lead | The draft plan can be watched filling up before and during planning |
| The day planning closes (the lock) | Paste the committed list from those two filters into the new PI scorecard page | Delivery lead | This is the baseline. It is taken once and never edited. |
| Day 1 of the new PI | Repoint `VS: PI planned Features` and the first part of `VS: PI Epics` to the new PI's filters | Delivery lead | Until day 1 the dashboards should still show the PI that is finishing |
| Day 1 of the new PI | Add the PI that has just ended to the list in `VS: spillover` | Delivery lead | From this day its unfinished committed work counts as spillover |
| Day 1 of the new PI | Change the PI value in automation rule 4 and in the board quick filter | Delivery lead | So Actual PI is stamped with the right PI |

Old per-PI filters are kept and never edited, because old scorecards read them.

**The filter you asked about**

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

### Stage 1: New demand (DDT)

| | |
| --- | --- |
| **Enter when** | Someone wants something that is in nobody's backlog. Work already on a team's Epic list does not come here; it is stitched to a Feature. |
| **What happens** | In the DDT: the need is described, discussed, and a decision is made on whether to do it, with a rough timeline and a proposed PI. Nothing is created in Jira yet. |
| **Exit when** | The demand is agreed (or declined) by the owner of the DDT decision. |
| **On exit, in Jira** | The product lead creates a **Feature** in the portfolio project, status **Idea**, with the DDT reference, sponsor, problem and outcome, any hard date, and the applications likely to change. If it is clearly larger than one PI, a **VS Epic** is created instead. The DDT entry is closed. |
| **How to see it** | `VS: intake waiting` lists everything in Idea. |

### Stage 2: Triage

| | |
| --- | --- |
| **Enter when** | A Feature exists in status Idea (from the DDT, or created during stitching). |
| **What you do in Jira** | Set Value Stream and Sub-Value Stream, Enabler Type, and Parent Link to the VS Epic. Assign the product lead. |
| **Exit when** | The product lead has capacity to shape it, and the three fields above are set. |
| **On exit, in Jira** | Move the Feature to **Analysis**. Or close it as a duplicate or Won't Do with a reason. |
| **How to see it** | Weekly backlog triage on the Feature board, Idea column. Anything waiting over a week is discussed. |

### Stage 3: Design

| | |
| --- | --- |
| **Enter when** | Feature is in **Analysis** with parent, sub value stream and Enabler Type set. |
| **What you do in Jira** | On the Feature: fill in Acceptance Criteria and Business Benefits; link the design page; raise sign-off tasks (architecture, risk, control) assigned to the approvers; fill in T-Shirt Size and the four scores. For each application that must change: its product owner creates an **Epic** with Parent Link to the Feature and a Story Points estimate. Link dependencies with **blocks**. Raise a Delivery RAID ticket for anything needed from another sub value stream or from outside. For a fixed regulatory date: create the Milestone and link it. |
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
| 9 | Proposed Features are Ready | Delivery lead creates the two per-PI filters. Product leads set **Target PI** on proposed Features (the draft). |
| 10 | Each team's capacity is known; dependencies are linked | Capacity entered in the plan; sprints created and named |

A Feature that is not Ready by week 9 does not enter planning.

**During planning**

1. Carried-over work is placed first.
2. Each product owner sets **Target PI** on the Epics they can take, and drags stories into sprints up to capacity.
3. For each Feature, the product lead checks every Epic has the Target PI. If one application cannot take its share: move the Feature, cut it down, or plan it over two PIs on purpose.
4. New dependencies are linked in the room. Unresolved ones become Delivery RAID tickets with an owner.
5. Each Epic that stays, then each Feature, gets `pi-committed` or `pi-stretch`, a Due date, and RAG Status Green.

**Exit (the lock)**

| Must be true | In Jira |
| --- | --- |
| Every committed Feature has all its Epics committed | Label and Target PI on each |
| Every team's load is within capacity | Capacity view in the plan |
| Every dependency has both ends planned, giver before receiver | Dependencies view in the plan |
| Risks raised in the room have an owner and a response | Delivery RAID tickets |
| Confidence vote taken | Comment on the planning Milestone |
| The delivery lead announces the lock | Committed list pasted into the PI scorecard page as the baseline |

After the lock, Target PI and the commitment labels change only by decision.

### Stage 6: Delivery

| | |
| --- | --- |
| **Enter when** | The PI has started and the Epic has Target PI, commitment label, RAG and Parent Link. |
| **On entry, in Jira** | Product owner moves the Epic to **Implementing** when its first story starts. The Feature moves to **Implementing** when its first Epic does. |
| **What you do in Jira** | Teams: story status daily, flags when stopped. Product owners weekly: Epic status, RAG, Path to Green and Date to Green if Amber or Red, Fix version. Product leads weekly: Feature RAG. Delivery lead: blockers, RAID, Milestones. |
| **Changes to the plan** | Only by decision of the product lead and delivery lead. In: Target PI plus `unplanned`. Out: `pi-descoped` plus a reason. |
| **Exit when** | Every story in the Epic is Done and deployed to the test environment. |
| **How to see it** | Dashboards 2 and 3. `VS: PI Epics not started` from week 5. `VS: open blockers`. `VS: Red and Amber`. |

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
| Go or no-go decided through the bank's change process | Decision recorded as a comment on the go-live Milestone; change record number in Change Request ID on the Epics |

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

## 4. One-page summary of the gates

| To move a Feature | From | To | You need |
| --- | --- | --- | --- |
| Into Jira | DDT | Idea | Demand agreed; DDT reference on the Feature |
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
