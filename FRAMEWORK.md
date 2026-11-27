# Jira framework: technical reference

As of 27 November 2026. All names and figures in examples are placeholders.

This file is the build reference: the set-up assumed, the complete saved filter library, the gadget list for each dashboard, the automation rules and the requests to the Jira administrator. The design itself (structure, workflows, planning, dependencies, roles, the implementation path) is in the [white paper](whitepaper/WHITE_PAPER.md), which is the current source. Until 27 November this file also carried that design text; it was removed so that there is one place for it.

## Where to find what

| Topic | Where |
| --- | --- |
| Why change, the proposal, decisions requested | White paper, sections 1 to 3 and 20 |
| Hierarchy, the two layers, stitching, relationships | White paper, section 4 |
| Fields, RAG rules, labels, links | White paper, section 5; [FIELDS.md](FIELDS.md) for who fills in what |
| Status meanings, gates, definition of done | White paper, section 6; [PHASE_GATES.md](PHASE_GATES.md) for entry and exit by stage |
| Intake through the demand intake project, who creates which ticket, definition of ready | White paper, section 7; [WAYS_OF_WORKING.md](WAYS_OF_WORKING.md), section 5 |
| Roadmap, sizing, prioritisation | White paper, section 8 |
| PI planning, commitment, the baseline | White paper, section 9; WAYS_OF_WORKING.md, section 7, for the step-by-step |
| Spillover, partial delivery, the PI scorecard | White paper, section 10 |
| Releases | White paper, section 11 |
| Dependencies, Delivery RAID, Milestones, who is responsible | White paper, section 12 |
| Portfolio management at VS Epic level | White paper, section 13 |
| Dashboards, role pages, Confluence pages | White paper, section 14; this file for gadget lists; the two build guides for steps |
| Roles, meetings, who decides | White paper, sections 15 and 16; [WAYS_OF_WORKING.md](WAYS_OF_WORKING.md); [JIRA_UPDATE_GUIDE.md](JIRA_UPDATE_GUIDE.md) |
| Implementation path, risks | White paper, sections 18 and 19; [PROGRAMME_PLAN.md](PROGRAMME_PLAN.md) |

## The set-up this reference assumes

The reference is written for Jira Data Center and for the field list in the organisation's Jira standards page, as confirmed on 26 November 2026.

| Confirmed | What it means here |
| --- | --- |
| The hierarchy VS Epic > Feature > Epic > Story exists, and VS Epic and Feature sit in one project. | That project is the portfolio project. A Feature is the parent of Epics in application projects through Parent Link. |
| Each application has its own Jira project. | Application is read from the project. Component is free for modules. |
| On today's Data Center the two top issue types are named Capability and Initiative, and there is no Milestone issue type. | In every query here, write `Capability` for `"VS Epic"` and `Initiative` for `Feature` until the move to Cloud. A Milestone is a Task with the labels `milestone` and `ms-...`; the Milestone filters then use `labels = milestone` in place of `issuetype = Milestone`. |
| Plans (Advanced Roadmaps) is available, but few people use it. | Plans is used for the L0 roadmap only. It also provides the Parent Link field, which is set on the ticket screen. |
| A PI is 12 weeks. | Five two-week sprints and one planning sprint. |
| Existing fields cover sub value stream, PI, status colour and prioritisation. | They are used as they are: Value Stream and Sub-Value Stream, Target PI, Actual PI, RAG Status, Path to Green, Date to Green, Executive Summary, the four scoring fields, Enabler Type, Team. |
| Delivery RAID has RAID Type, Probability, Impact, ROAM Response, Dependency Type and a supplier sub value stream field. | RAID and dependency reporting uses those fields. |
| Almost every ticket has RAG Status, and Due date is the target date. | RAG and Due date drive the dashboards. Epic appears to be the exception: see FIELDS.md. |
| No ScriptRunner. Project automation is available. | No scripted queries. A few automation rules keep fields in step. |
| Confluence has the Jira Issues macro, Table Transformer, Pivot Table and Chart from Table. | The PI plan, the dependency board, roll-ups, trends and the role pages are built there. |

**Twelve checks for the proof of concept.** Nothing here has yet been run on real data.

- [ ] 1. Field names match the standards page letter for letter. They were read from a photo of that page.
- [ ] 2. All of those fields are live in today's Data Center projects. The standards page is titled for Jira Cloud.
- [ ] 3. The allowed values of Enabler Type, RAG Status, RAID Type, ROAM Response and Severity, and the way PI values are written, are filled into the queries.
- [ ] 4. Whether Value Stream and Sub-Value Stream is a two-step dropdown, and whether a dashboard gadget accepts it. If not, switch on the shadow label.
- [ ] 5. The organisation's own rule for when Actual PI is filled in, and whether Target PI may change. This reference assumes "at Released" and "only by decision".
- [ ] 6. Each base filter run once on real data and checked by hand.
- [ ] 7. The Jira version, and whether the Parent Link column shows correctly in the Confluence Jira Issues macro.
- [ ] 8. Whether project admins may create automation rules.
- [ ] 9. How often the DDT sits, and that it will decide from the intake queue and record its decisions on the request.
- [ ] 10. One dependency run end to end (ask, accept, link, plan) and shown on the Confluence dependency board with a correct margin. Whether the `issueLinkType` query field works, and whether Parent Link can be set by bulk edit.
- [ ] 11. A product owner can create and move a Delivery RAID ticket in the portfolio project.
- [ ] 12. One real request put through intake: raised in the portal, approved, and a linked Feature created from it. Whether the approval step and "Create linked issue" are available in the demand intake project.

## Saved filter library

The library has 47 value stream, dependency, release and hygiene filters, plus 7 per application team. There is no set per sub value stream. All of them hang off five base filters. At each PI change the delivery lead creates two, repoints two and extends one, and edits the PI value in automation rule 4; nothing else changes. Filters are owned by the framework owner, shared with the value stream group, and never renamed, because dashboards and Confluence pages refer to them by name.

Placeholders to replace: `CLP` is the portfolio project key; `CA, DRAW, FL` stand for the application project keys; `Credit and Lending` and `Monitoring` stand for a value stream and a sub value stream; `PI 2027.1` is the current PI as the Target PI field writes it; `CLP 2027.03` is a release name; `Red`, `Amber`, `Risk` and `Dependency` stand for the field values. Test each query once before sharing it.

**Base filters (the last column says what to do at each PI change)**

| Save as | Query | At each PI change |
| --- | --- | --- |
| PI 2027.1 planned Features | `project = CLP AND issuetype = Feature AND "Target PI" = "PI 2027.1"` | Create a new one for the new PI. Never edit an old one: past scorecards read it. |
| PI 2027.1 planned Epics | `issuetype = Epic AND project in (CA, DRAW, FL) AND "Target PI" = "PI 2027.1"` | Create a new one. |
| VS: PI planned Features | `filter = "PI 2027.1 planned Features"` | Repoint to the new PI's filter. |
| VS: spillover | `issuetype in (Feature, Epic) AND project in (CLP, CA, DRAW, FL) AND "Target PI" in ("PI 2026.3", "PI 2026.4") AND labels = pi-committed AND status not in (Released, Done)` | Add the PI that has just ended to its list. Keep the list to the last four PIs. |
| VS: PI Epics | `filter = "PI 2027.1 planned Epics" OR (filter = "VS: spillover" AND issuetype = Epic) OR (issuetype = Epic AND project in (CA, DRAW, FL) AND status = Implementing)` | Repoint the first part. |

**Value stream**

| Save as | Query |
| --- | --- |
| VS: current PI Features | `filter = "VS: PI planned Features" OR (project = CLP AND issuetype = Feature AND status in (Implementing, Testing, Validation))` |
| VS: committed Features | `filter = "VS: PI planned Features" AND labels = pi-committed` |
| VS: committed and released | `filter = "VS: committed Features" AND status in (Released, Done) AND (resolution is EMPTY OR resolution = Done)` |
| VS: unplanned in PI | `filter = "VS: PI planned Features" AND labels = unplanned` |
| VS: open VS Epics | `project = CLP AND issuetype = "VS Epic" AND status not in (Idea, Done) ORDER BY Rank` |
| VS: all Features | `project = CLP AND issuetype = Feature` |
| VS: Red and Amber | `(filter = "VS: current PI Features" OR filter = "VS: PI Epics" OR filter = "VS: open VS Epics") AND "RAG Status" in (Red, Amber) AND status not in (Released, Done)` |
| VS: Management Attention and Red | `project = CLP AND issuetype in (Feature, "VS Epic") AND status not in (Released, Done) AND ("Management Attention" is not EMPTY OR "RAG Status" = Red)` |
| VS: Amber or Red without a plan | `filter = "VS: Red and Amber" AND issuetype != Epic AND "Path to Green" is EMPTY` (Epics are left out because Epic appears not to carry Path to Green; an Epic's recovery plan is a comment starting "Path to green:") |
| VS: RAG not refreshed in 14 days | `(filter = "VS: current PI Features" OR filter = "VS: PI Epics") AND status not in (Released, Done) AND updated <= -14d` |
| VS: open RAID | `project = CLP AND issuetype = "Delivery RAID" AND statusCategory != Done` |
| VS: open Red and Amber RAID | `filter = "VS: open RAID" AND "RAG Status" in (Red, Amber) ORDER BY duedate` |
| VS: risks not reviewed | `filter = "VS: open RAID" AND "RAID Type" = Risk AND "ROAM Response" is EMPTY` |
| VS: RAID past its date | `filter = "VS: open RAID" AND duedate < now()` |
| VS: Milestones next 90 days and overdue | `project = CLP AND issuetype = Milestone AND statusCategory != Done AND duedate <= endOfDay("+90d") ORDER BY duedate` |
| VS: intake waiting | `project = CLP AND issuetype in (Feature, "VS Epic") AND status = Idea ORDER BY created` |
| VS: flagged | `(project = CLP OR filter = "VS: PI Epics") AND Flagged = Impediment` |

**Delivery control**

| Save as | Query |
| --- | --- |
| VS: PI Epics not started | `filter = "VS: PI Epics" AND status in (Idea, Analysis, Ready)` |
| VS: open blockers | `(filter = "VS: current PI Features" OR filter = "VS: PI Epics") AND issueLinkType = blocks AND status not in (Released, Done)` (to be tested: `issueLinkType` may not exist on this Jira version) |
| VS: Features with a late application | Not possible as a Jira query. Use the Confluence page "Feature progress across applications". |

**Dependencies** (the method is section 12 of the white paper)

| Save as | Query |
| --- | --- |
| VS: open dependencies | `filter = "VS: open RAID" AND "RAID Type" = Dependency ORDER BY duedate` |
| VS: dependencies not agreed | `filter = "VS: open dependencies" AND status = Backlog ORDER BY duedate` |
| VS: dependencies agreed | `filter = "VS: open dependencies" AND status = "In Progress"` |
| VS: dependencies late or due soon | `filter = "VS: open dependencies" AND duedate <= endOfDay("+28d") ORDER BY duedate` |
| VS: dependencies at risk | `filter = "VS: open dependencies" AND "RAG Status" in (Amber, Red)` |
| VS: dependencies without an owner or date | `filter = "VS: open dependencies" AND (assignee is EMPTY OR duedate is EMPTY)` |
| VS: dependencies closed this PI | `project = CLP AND issuetype = "Delivery RAID" AND "RAID Type" = Dependency AND resolved >= "2027-01-04"` (the first day of the PI) |
| Everything linked to one ticket | `issue in linkedIssues("CLP-123")`, for one key at a time |

**Features across the value stream.** There is no filter set per sub value stream. These filters cover every Feature in the value stream; add the sub value stream as a column.

| Save as | Query |
| --- | --- |
| VS: open Features | `project = CLP AND issuetype = Feature AND status != Done ORDER BY Rank` |
| VS: Red and Amber Features | `filter = "VS: Red and Amber" AND issuetype = Feature` |
| VS: Ready, no Target PI | `project = CLP AND issuetype = Feature AND status = Ready AND "Target PI" is EMPTY ORDER BY "Weighted Shortest Job First Score" DESC` |
| VS: Analysis over 30 days | `project = CLP AND issuetype = Feature AND status = Analysis AND NOT status changed AFTER -30d` |
| VS: Features with gaps | `project = CLP AND issuetype = Feature AND status not in (Idea, Analysis, Done) AND ("Parent Link" is EMPTY OR "Enabler Type" is EMPTY OR "Weighted Shortest Job First Score" is EMPTY OR "RAG Status" is EMPTY OR "Value Stream and Sub-Value Stream" is EMPTY)` |
| VS: regulatory Features | `project = CLP AND issuetype = Feature AND "Regulatory or Control Change Type" is not EMPTY AND status not in (Released, Done) ORDER BY duedate` |
| One sub value stream, when someone asks | Add `AND "Value Stream and Sub-Value Stream" in cascadeOption("Credit and Lending", "Monitoring")` to any filter above. Do not save it as a separate set. |

"Team: all bugs" is "Team: open bugs" without the status condition.

**Release**

| Save as | Query |
| --- | --- |
| Release: scope | `fixVersion = "CLP 2027.03"` |
| Release: not finished | `fixVersion = "CLP 2027.03" AND statusCategory != Done` |
| Release: open bugs | `fixVersion = "CLP 2027.03" AND issuetype = Bug AND statusCategory != Done` |
| Release: notes | `fixVersion = "CLP 2027.03" AND issuetype in (Story, Bug) AND resolution = Done` |

**Team.** One set per application project.

| Save as | Query |
| --- | --- |
| Team: flagged in sprint | `project = DRAW AND sprint in openSprints() AND Flagged = Impediment` |
| Team: carried over | `project = DRAW AND sprint in openSprints() AND sprint in closedSprints() AND statusCategory != Done` |
| Team: open Epics | `project = DRAW AND issuetype = Epic AND statusCategory != Done` |
| Team: Epics blocked by others | `project = DRAW AND issuetype = Epic AND issueLinkType = "is blocked by" AND statusCategory != Done` (to be tested, as above; the fallback is the "We are waiting on" panel of the product owner page) |
| Team: open bugs | `project = DRAW AND issuetype = Bug AND statusCategory != Done` |
| Team: Epics without Feature | `project = DRAW AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` |
| Team: Stories without Epic | `project = DRAW AND issuetype in (Story, Task) AND "Epic Link" is EMPTY AND statusCategory != Done` |

**Hygiene (review monthly)**

| Save as | Query | Why it matters |
| --- | --- | --- |
| VS: hygiene exceptions | `project in (CA, DRAW, FL) AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` | Work the portfolio cannot see. |
| Hygiene: no sub value stream | `(project = CLP OR filter = "VS: PI Epics") AND "Value Stream and Sub-Value Stream" is EMPTY AND status != Idea` | Missing from every grouped view. |
| Hygiene: released without Actual PI | `issuetype in (Feature, Epic) AND project in (CLP, CA, DRAW, FL) AND status in (Released, Done) AND "Target PI" is not EMPTY AND "Actual PI" is EMPTY` | Predictability cannot be counted. |
| Hygiene: in progress without Target PI | `issuetype in (Feature, Epic) AND project in (CLP, CA, DRAW, FL) AND status = Implementing AND "Target PI" is EMPTY` | Work started outside the plan. |
| Hygiene: done without resolution | `project in (CLP, CA, DRAW, FL) AND statusCategory = Done AND resolution is EMPTY` | Missed by the trend gadgets. |
| Hygiene: open with resolution | `project in (CLP, CA, DRAW, FL) AND statusCategory != Done AND resolution is not EMPTY` | Wrongly counted as finished. |

**Notes for Data Center**

- **Parent.** `"Parent Link"` joins Epic to Feature and Feature to VS Epic. `"Epic Link"` joins Story to Epic. `"Parent Link" = CLP-123` returns the Features of a VS Epic, or the Epics of a Feature.
- **Everything under one ticket.** `issuekey in childIssuesOf("CLP-123")` returns all levels below it. Atlassian notes it can return too much when a ticket has changed type and kept an old Parent Link, and can fail on very large parents. Use it for one VS Epic at a time.
- **Sub value stream.** `cascadeOption("parent", "child")` is the query form for a two-step dropdown. If the field is a plain dropdown, write `"Value Stream and Sub-Value Stream" = "Monitoring"` instead.
- **Epics of a PI across applications.** This works because Epics carry Target PI and the sub value stream of their Feature. The sub value stream is copied down by automation rule 1. Target PI is set by the team at PI planning.
- **Links.** `issue in linkedIssues("KEY")` and `issue in linkedIssues("KEY", "blocks")` are documented for Data Center and take one key. A query cannot follow links from the results of another filter. Whether the `issueLinkType` field exists on this version is a proof-of-concept check.
- **History.** Jira can search when Status changed, but not when RAG Status or Target PI changed. "RAG not refreshed" therefore uses the last update of the ticket, and scope added after planning uses the `unplanned` label.

## Dashboards

Reporting runs top-down in one line: VS Epics, then Features across the whole value stream, then Epics across applications, then the team. There is no separate set of views per sub value stream; the sub value stream is a column to sort or group by, never a filter that hides the rest. Six dashboards, each built only from standard Jira gadgets on saved filters: five follow that line, and the sixth is the dependency register. Filter names refer to the filter library. Three role pages in Confluence (delivery lead, platform owner, product owner) sit beside them; see section 14 of the white paper and recipe 4.17 of the Confluence guide.

Three facts about Jira dashboards shape the design:

- A gadget shows what a saved filter returns. It cannot add up stories under a Feature by itself. So each level has its own filters.
- A viewer sees nothing in a gadget if the filter is not shared with them. Share every filter and dashboard with one group for the whole value stream.
- A dashboard holds 20 gadgets by default. Each design below uses 10 or fewer.

**1. Value stream portfolio** (VS Epics; for the value stream lead and sponsors)

| Gadget | Filter or source | Question answered |
| --- | --- | --- |
| Filter Results, with RAG Status, Due date and Executive Summary, in rank order | VS: open VS Epics | What are the value stream's outcomes and how is each going? |
| Pie Chart by RAG Status | VS: open VS Epics | How healthy is the portfolio? |
| Two Dimensional Filter Statistics, Status by RAG Status | VS: open VS Epics | Where in the pipeline is the trouble? |
| Filter Results, with Path to Green | VS: Management Attention and Red | What needs a decision at value stream level? |
| Filter Results, by Due date | VS: Milestones next 90 days and overdue | Which dates are close or missed? |
| Two Dimensional Filter Statistics, RAID Type by RAG Status | VS: open RAID | How much risk is open, and how serious? |
| Filter Results | VS: intake waiting | What is waiting to be shaped? |
| Created vs Resolved, 180 days | VS: all Features | Is the value stream finishing Features as fast as it takes them on? |

**2. Features across the value stream** (for product leads and delivery leads; one dashboard for everyone)

| Gadget | Filter or source | Question answered |
| --- | --- | --- |
| Filter Results, with Parent Link, sub value stream, RAG Status, Target PI and Due date | VS: current PI Features | What is the value stream delivering this PI, under which VS Epic? |
| Two Dimensional Filter Statistics, Status by RAG Status | VS: current PI Features | How far along, and how healthy? |
| Pie Chart by Status | VS: committed Features | How much of the commitment is delivered? |
| Two Dimensional Filter Statistics, Enabler Type by Status | VS: current PI Features | Where is the investment going? |
| Filter Results, with Path to Green and Date to Green | VS: Red and Amber Features | What is off track, and what is the recovery plan? |
| Filter Results, sorted by Weighted Shortest Job First Score | VS: Ready, no Target PI | What is ready for the next PI, best value first? |
| Filter Results | VS: Analysis over 30 days | Which Features are stuck in design? |
| Filter Results | VS: regulatory Features | Which Features carry a regulatory or control change, and when are they due? |
| Filter Results | VS: unplanned in PI | What was added after planning? |
| Filter Results | VS: Features with gaps | Which Features lack a parent, a score, a sub value stream or an Enabler Type? |

**3. Epics across applications** (for delivery leads and product owners)

| Gadget | Filter or source | Question answered |
| --- | --- | --- |
| Two Dimensional Filter Statistics, Project by Status | VS: PI Epics | How far is each application with its share of this PI? |
| Two Dimensional Filter Statistics, Project by RAG Status | VS: PI Epics | Which application is in trouble? |
| Two Dimensional Filter Statistics, Project by Target PI | VS: spillover | Which application spills, and from which PI? |
| Filter Results | VS: PI Epics not started | Which committed Epics have not begun? |
| Filter Results, by Due date | VS: open blockers | Whose unfinished work is someone else waiting for? |
| Filter Results | VS: flagged | What is stopped right now? |
| Filter Results | VS: Amber or Red without a plan | Which tickets claim trouble but give no Path to Green? |
| Filter Results | VS: hygiene exceptions | Which Epics have no parent Feature? |

**4. Risks, dates and releases** (for delivery leads)

| Gadget | Filter or source | Question answered |
| --- | --- | --- |
| Filter Results, with RAID Type, RAG Status, ROAM Response and Due date | VS: open Red and Amber RAID | What are the serious risks and issues? |
| Filter Results, with the supplier and receiver sub value streams | VS: open dependencies | Who is waiting on whom across the value stream? |
| Filter Results | VS: risks not reviewed | Which risks has nobody assessed? |
| Filter Results | VS: RAID past its date | Which RAID tickets are overdue? |
| Filter Results, with Baseline End Date and Due date | VS: Milestones next 90 days and overdue | Which dates have moved? |
| Two Dimensional Filter Statistics, Project by Status | Release: scope | Is the next release ready in every application? |
| Pie Chart by Priority | Release: open bugs | Are there bugs that stop the release? |

**5. Team** (one per application team; owner: product owner or scrum master)

| Gadget | Filter or source | Question answered |
| --- | --- | --- |
| Sprint Health | Team board | Are we on track this sprint? |
| Sprint Burndown | Team board | Is work burning down or piling up at the end? |
| Filter Results | Team: flagged in sprint | What is blocked today? |
| Filter Results | Team: carried over | Which stories have rolled from an earlier sprint? |
| Two Dimensional Filter Statistics, Status by Fix Version | Team: open Epics | Where is each Epic, and for which release? |
| Filter Results | Team: Epics blocked by others | What are we waiting on from another team? |
| Pie Chart by Priority | Team: open bugs | How many bugs, and how serious? |
| Filter Results | Team: Epics without Feature | Which of our Epics are invisible to the portfolio? |

**6. Dependencies** (for delivery leads and product owners; opens the weekly delivery sync)

| Gadget | Filter or source | Question answered |
| --- | --- | --- |
| Filter Results, with Linked Issues, supplier, Due date and Created | VS: dependencies not agreed | Which asks have no answer, and how old are they? |
| Two Dimensional Filter Statistics, supplier by Status | VS: open dependencies | What does each sub value stream owe? |
| Two Dimensional Filter Statistics, sub value stream by RAG Status | VS: open dependencies | What is each sub value stream waiting for? |
| Filter Results, by Due date, with Baseline End Date | VS: dependencies late or due soon | What is past its need-by date, or due in the next two sprints? |
| Filter Results | VS: flagged | What is stopped right now? |
| Filter Results, with Path to Green | VS: dependencies at risk | Which agreed dependencies are Amber or Red? |
| Filter Results | VS: dependencies without an owner or date | Which asks cannot be chased? |

**What standard Jira cannot show, and the way round it**

| Wanted | Why a gadget cannot | Where it comes from |
| --- | --- | --- |
| Percentage complete of a Feature from its stories | Gadgets do not roll up the hierarchy. | Confluence: the portfolio tree and Feature progress pages. |
| Feature progress across applications as a table | Same reason. | Confluence guide, recipe 4.2. |
| Predictability trend across PIs | Jira keeps no snapshot of what was planned. | Confluence guide, recipes 4.7 and 4.8. |
| Scope added and removed during a PI | Same reason. | Confluence guide, recipe 4.7. |
| Time spent waiting versus working | Needs time in each status. | An add-on (Time in Status, eazyBI) or an export to Power BI. |
| Team velocity as a gadget | Velocity is a board report. | The Velocity report on the team board; it gives the capacity typed into the PI plan page. |
| The PI plan, load against capacity, and dependencies with their dates | No gadget joins or compares them. | Confluence guide, recipes 4.14 to 4.16. |
| Deployment frequency and failure rate | That data sits in release and incident tools. | Those tools, not Jira. |

**Boards complement the dashboards.** Two boards serve the whole value stream. The VS Epic board has the VS Epic statuses as columns. The Feature board has the Feature statuses as columns, one swimlane per VS Epic, card colours by RAG Status, and quick filters for Current PI, Committed, Red and Amber, and Flagged. Neither board is split by sub value stream.

The view Jira cannot give is the roll-up along the line: each VS Epic with its Features, and each Feature with its Epics, counted and coloured. That lives in the Confluence portfolio pages.

**A known limit, and its fix.** If Value Stream and Sub-Value Stream is a two-step dropdown, dashboard gadgets may not accept it as an axis (Atlassian's pages do not confirm it for current versions), and Plans cannot show it as a column. Test one gadget first. If it fails, use the shadow label: automation rules 1 and 2 write a label such as `svs-monitoring` on every ticket to match the field. Labels work as a gadget axis, a board swimlane and a Confluence column. People keep filling in the field; only automation writes the label.

## Confluence pages

Roll-ups, the PI plan, the dependency board, trends and the role pages are Confluence pages. The page tree, every recipe and a figure-by-figure build table are in the [Confluence guide](confluence/CONFLUENCE_PORTFOLIO_GUIDE.md).

Three limits to plan around. The Jira Issues macro shows about 1,000 issues at most, so each macro's filter is kept narrow: one PI, or one level of the hierarchy. On Jira versions 10.5 to 10.7 the Parent Link column in the macro showed raw text instead of the parent's key. And the first join on every page is checked by hand, because joins have been reported to drop unmatched rows silently.

## Automation rules

Nine automation rules keep the fields in step, chase missing updates and join intake to delivery, so that people are not asked to type the same thing twice or to police each other.

| # | Rule | When it runs | What it does | Who can build it |
| --- | --- | --- | --- | --- |
| 1 | Copy sub value stream down | An Epic is created, or its Parent Link changes | Looks up the parent Feature with `key in parentIssuesOf("<the Epic>") AND issuetype = Feature`, copies Value Stream and Sub-Value Stream to the Epic, and writes the matching `svs-` label. | Jira admin: it spans projects |
| 2 | Shadow label | Value Stream and Sub-Value Stream changes on a VS Epic, Feature, Milestone or Delivery RAID | Writes the matching `svs-` label and removes the old one. Needed only if the test of the field in gadgets fails. | Portfolio project admin |
| 3 | Ask for a recovery plan | RAG Status changes to Amber or Red while Path to Green is empty | Comments on the ticket, naming the assignee, asking for Path to Green and Date to Green. | Project admin |
| 4 | Record the finishing PI | A Feature or Epic moves to Released with Actual PI empty | Sets Actual PI to the current PI. The value in the rule is edited on the first day of each PI. | Project admin |
| 5 | Chase stale trouble | Every Monday | Emails the assignee of each Amber or Red ticket not updated in 14 days. Green tickets are not chased. | Project admin, one rule per project |
| 6 | Chase overdue RAID | Every Monday | Comments on each ticket in "VS: RAID past its date", naming the assignee. | Portfolio project admin |
| 7 | Keep Parent Link clean | An issue changes type | Clears Parent Link, which otherwise keeps a stale value and corrupts the hierarchy queries. This is Atlassian's own recommended fix. | Jira admin |
| 8 | Create the Feature from a request | A request in the demand intake project is approved | Creates a Feature in the portfolio project in status Idea, copies summary, description and sponsor, links the two, and comments on the request. | Jira admin: it spans projects |
| 9 | Close the loop | A Feature with a linked request moves to Released | Comments on the request and closes it. | Jira admin: it spans projects |

Build rules 3 to 6 first; they sit inside one project each. Whether a project admin may create rules is a setting the Jira admin controls, so confirm it. Rule 1 is the one to test carefully: Atlassian documents copying from a parent down to its children when the parent changes, and this rule works from the child's side, for which no published example was found. Until rule 1 exists, product owners set the sub value stream on Epics by hand, and the hygiene filter catches the gaps.

## What to ask the Jira admin for

Eight requests, none of which adds a field or a status. Requests 1 to 4 and 7 are needed to start; 5, 6 and 8 can follow the proof of concept.

| # | Request | Why | Without it |
| --- | --- | --- | --- |
| 1 | Show Parent Link, Target PI, Actual PI, RAG Status and Value Stream and Sub-Value Stream on the create, edit and view screens of Epic in every application project. | Product owners can set and see them. This is the join between applications. | Nobody can set the parent without opening Plans. With Plans kept for the roadmap only, this request is essential. |
| 2 | A user group for the value stream that can create shared filters and dashboards; the framework owner and delivery leads can also edit the roadmap plan. | Dashboards are blank for anyone who cannot see the filter. | Each person builds their own. |
| 3 | A resolution screen on the transition to Done for every issue type, with resolutions Done and Won't Do; resolution cleared on reopen. | Trend and predictability figures depend on resolution. | Cancelled work counts as delivered. |
| 4 | Automation rule 1, across the portfolio project and the application projects. | Epics inherit the sub value stream of their Feature. | Set by hand; gaps caught by the hygiene filter. |
| 5 | For the roadmap only: make RAG Status and the sub value stream field available for colour and grouping in Plans. | The roadmap can be coloured by RAG and grouped by sub value stream. | The roadmap shows dates and hierarchy only. |
| 6 | Workflow checks: a Feature cannot leave Analysis without Parent Link, sub value stream and Enabler Type, and cannot enter Implementing without Target PI and RAG Status. | The definition of ready enforces itself. | Product leads check by hand, using "VS: Features with gaps". |
| 7 | In the portfolio project: let product owners and scrum masters create issues, comment, link and move Delivery RAID tickets between statuses; and create one Component per application. | Teams can raise and answer asks on neutral ground, and RAID can be listed by application. | Asks go through the delivery lead, who becomes a bottleneck. |
| 8 | Two automation rules across the demand intake project and the portfolio project (rules 8 and 9). | Nothing is typed twice at intake, and the requester is told the outcome. | The product lead uses "Create linked issue" on each approved request, and closes requests by hand. |

Jira grants the right to create issues for a whole project, not for one issue type. Product owners and scrum masters will therefore also be able to create a Feature in the portfolio project; the weekly triage of the Idea column catches anything raised by mistake.

Two questions for the owner of the standards page: when is Actual PI meant to be filled in, and is Target PI allowed to change after planning? This reference assumes "at Released" and "no, for committed work". A third: can Path to Green, Date to Green and Due date be shown on Epic?

One status to consider: "In Review" for stories, only if teams need to see work waiting for test or review. No other new statuses are needed.

One decision for the admin, not a request: the status Released on Feature and Epic should sit in the green Done category only if a resolution is set at that point. Otherwise keep it in the blue In Progress category. The filters name the statuses directly, so they work either way.

## Bringing in a new application or team

- [ ] The application project uses the standard issue types, workflows and screens, with Parent Link, Target PI, Actual PI, RAG Status and the sub value stream field visible on Epic.
- [ ] Board created; sprints named to the convention; a Team value for the team.
- [ ] Project added to the project lists in the base filters, the hygiene filters and automation rule 1, and to the sources of the roadmap plan.
- [ ] A Component for the application created in the portfolio project, so Delivery RAID can be listed by application.
- [ ] Existing open Epics given a parent Feature.
- [ ] Team filters set; team dashboard copied from the template; product owner page copied from the template in Confluence.
- [ ] Product owner and scrum master can create and move Delivery RAID tickets in the portfolio project.
- [ ] Product owner walked through the update guide; first delivery sync attended.

## At each PI change

| When | What | Who |
| --- | --- | --- |
| Week 9 of the current PI | Create `PI <next> planned Features` and `PI <next> planned Epics`; copy the PI plan page in Confluence for the next PI and change its filter and its start date | Delivery lead |
| The day planning closes | Paste the committed list and the dependency board into the new PI scorecard page | Delivery lead |
| Day 1 of the new PI | Repoint `VS: PI planned Features` and the first part of `VS: PI Epics`; add the ended PI to `VS: spillover`; change the PI value in automation rule 4 and in the board quick filter; change the date in `VS: dependencies closed this PI` | Delivery lead |

Old per-PI filters are kept and never edited, because old scorecards read them.

## Cloud version: later

This document is for Jira Data Center as it runs today; a Cloud version will follow once this one is working.

The design should travel well, because it rests on standard fields and not on scripts. The known changes are small: the queries that use Parent Link and Epic Link are rewritten with the single `parent` field, the automation rules are re-tested, and the Confluence reports are re-tested with the Cloud editions of the add-ons.

One thing is worth asking the migration team early: on Cloud, Plans and the levels above Epic need the Premium plan.

## Sources

Checked on 26 and 27 November 2026. Some Atlassian pages loaded only in part, so the Jira Cloud gadget list and the behaviour of `parent` above Epic on a site without Plans are not confirmed; both are covered by the test-first note in the filter library.

- [Configure custom hierarchy levels in Plans](https://support.atlassian.com/jira-software-cloud/docs/configure-custom-hierarchy-levels-in-advanced-roadmaps/) (Atlassian)
- [Epic Link replaced with Parent](https://support.atlassian.com/jira-software-cloud/docs/upcoming-changes-epic-link-replaced-with-parent/) (Atlassian)
- [Configuring the Parent Link field in Jira Data Center](https://confluence.atlassian.com/roadmaps-kb/how-to-properly-configure-the-parent-link-field-on-screens-in-jira-data-center-1295682320.html) (Atlassian)
- [Hierarchy search functions returning wrong results](https://support.atlassian.com/jira/kb/searching-for-child-or-parent-issues-using-jql-functions-report-wrong-results-in-jira/) (Atlassian)
- [Searching Plans fields in JQL](https://confluence.atlassian.com/jiraportfoliocloud/searching-for-portfolio-for-jira-custom-fields-in-jql-941619014.html) (Atlassian)
- [Plan and view cross-project work](https://support.atlassian.com/jira-software-cloud/docs/plan-and-view-cross-project-work-with-advanced-roadmaps/) (Atlassian)
- [JQL functions](https://support.atlassian.com/jira-software-cloud/docs/jql-functions/) (Atlassian)
- [Gadgets for Jira applications](https://confluence.atlassian.com/jirasoftwareserver0917/gadgets-for-jira-applications-1431245257.html) (Atlassian, Data Center)
- [Gadget limit on a dashboard](https://support.atlassian.com/jira/kb/modifying-gadget-limit-on-a-dashboard/) (Atlassian)
- [Configuring swimlanes](https://confluence.atlassian.com/display/JIRASOFTWARECLOUD/Configuring+swimlanes) (Atlassian)
- [Best practices on using the Resolution field](https://support.atlassian.com/jira/kb/best-practices-on-using-the-resolution-field-in-jira-cloud/) (Atlassian)
- [The Dependencies report in Plans](https://confluence.atlassian.com/jirasoftwareserver/the-dependencies-report-in-advanced-roadmaps-1077915784.html) (Atlassian, Data Center)
- [Advanced searching: functions reference](https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-functions-reference-939938746.html) (Atlassian, Data Center)
- [Release Train Engineer](https://framework.scaledagile.com/release-train-engineer-and-solution-train-engineer) (Scaled Agile)
- [Accelerating flow with SAFe](https://framework.scaledagile.com/accelerating-flow-with-safe) (Scaled Agile)
- [Milestones](https://v5.scaledagileframework.com/milestones/) (Scaled Agile)
- [Labels, components or custom fields](https://community.atlassian.com/forums/App-Central-articles/Labels-Component-or-Custom-Field-Which-one-is-best-for-your/ba-p/2809685) (Atlassian Community)
- [Jira link types: practice and misuse](https://community.atlassian.com/forums/App-Central-articles/Jira-Link-Types-Best-Practices-Common-Misuse-and-How-to-Control/ba-p/3155484) (Atlassian Community)
