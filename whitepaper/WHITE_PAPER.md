# One Jira for the value stream

**A white paper on a unified Jira framework for product and delivery operations**

| | |
| --- | --- |
| Status | Draft 0.1 for review and comment |
| Date | 27 November 2026 |
| Applies to | Jira Data Center with Plans, and Confluence with Table Transformer and Chart from Table. A Cloud edition follows the migration. |
| Audience | Value stream lead, head of product, head of technology, product leads, delivery leads, product owners, business analysts, scrum masters, engineers, testers, Jira administrators |
| What is asked of the reader | Read the parts marked for your role in the reading guide, then comment against the decisions in section 20 |

> **About the figures.** Every chart in this paper uses illustrative mock data and placeholder names. The charts show what each view will look like once the framework is running; they are not measurements of today. Project keys (`CLP`, `CA`, `DRAW`, `FL`, `GC`, `WWM`, `PEM`, `FORB`), PI names and dates are placeholders.

> **About what has been tested.** The design has been reviewed for contradictions and its technical claims checked against Atlassian and add-on vendor documentation. No query, import or Confluence recipe has yet been run in the live Jira or Confluence. The proof of concept in section 18 exists to close that gap before anything is rolled out.

---

## Contents

**Part A: The proposal**
1. [Summary](#1-summary)
2. [Why change](#2-why-change)
3. [Design principles and constraints](#3-design-principles-and-constraints)

**Part B: The model**
4. [Structure: two layers, one join](#4-structure-two-layers-one-join)
5. [Fields, labels and links](#5-fields-labels-and-links)
6. [Workflows and gates](#6-workflows-and-gates)

**Part C: How work flows**
7. [Intake and design](#7-intake-and-design)
8. [Roadmap, sizing and prioritisation](#8-roadmap-sizing-and-prioritisation)
9. [PI planning](#9-pi-planning)
10. [Delivery control](#10-delivery-control)
11. [Release planning](#11-release-planning)
12. [Delivery RAID and Milestones](#12-delivery-raid-and-milestones)
13. [Managing the portfolio](#13-managing-the-portfolio)

**Part D: Seeing it**
14. [Dashboards and reports](#14-dashboards-and-reports)

**Part E: Running it**
15. [Roles: what changes for whom](#15-roles-what-changes-for-whom)
16. [Operating rhythm and governance](#16-operating-rhythm-and-governance)

**Part F: Building it**
17. [Technology view](#17-technology-view)
18. [Implementation path](#18-implementation-path)
19. [Risks](#19-risks)
20. [Decisions requested and open questions](#20-decisions-requested-and-open-questions)

**Appendices**
- [A. Glossary](#appendix-a-glossary)
- [B. Questions people will ask](#appendix-b-questions-people-will-ask)
- [C. Key saved filters](#appendix-c-key-saved-filters)
- [D. Detailed guides](#appendix-d-detailed-guides)
- [E. Sources](#appendix-e-sources)

## Reading guide

The paper is long on purpose: it is the full reference, and it will be split into shorter documents by audience. Until then, read these sections.

| If you are | Read first | Then | Time |
| --- | --- | --- | --- |
| Value stream lead, head of product, sponsor | 1, 2, 13, 14, 20 | 8, 16, 18 | 25 min |
| Head of technology, architecture | 1, 3, 4, 17, 18, 19, 20 | 6, 11 | 30 min |
| Jira administrator, tooling team | 3, 4, 5, 17, appendix C | 6, 14 | 30 min |
| Product lead | 1, 4, 6, 7, 8, 9, 10 | 13, 15, 16 | 40 min |
| Delivery lead | 1, 4, 9, 10, 11, 12, 14 | 15, 16, 18 | 40 min |
| Application product owner | 1, 4, 5, 9, 10, 15 | 6, 11 | 25 min |
| Business analyst, designer | 1, 4, 6, 7 | 15 | 15 min |
| Scrum master, engineer, tester | 1, 4 (first figure only), 15 | 6, 11 | 10 min |

---

# Part A: The proposal

## 1. Summary

**The problem.** Each application team runs its own Jira project in its own way. An initiative that needs three applications exists as three unconnected Epics. Nobody can open one page and see what the value stream is delivering, which application an initiative is waiting for, what was promised for the Program Increment (PI) and what was delivered. Those answers are assembled by hand, in slides, every reporting cycle.

**The proposal.** One line of work that every ticket sits on:

**VS Epic > Feature > Epic > Story, Task, Bug, Test > Sub-task**, with **Milestone** and **Delivery RAID** tickets linked alongside.

- One portfolio project holds every VS Epic, Feature, Milestone and Delivery RAID ticket for the value stream.
- Each application keeps its own project for Epics and everything below.
- A Feature is the parent of one Epic in each application that must change to deliver it. That parent link is the join between applications.
- Fields that already exist (sub value stream, Target PI, Actual PI, RAG Status) carry planning and status. A few labels cover what no field does.
- Views start at the value stream, then show Features across the whole value stream, then Epics across applications.

**What is not asked for.** No new issue type, no new field, no new status, no scripting add-on, and no re-entry of existing Epics. Existing Epics are joined upward to Features and VS Epics, a step this paper calls stitching.

**What it gives each audience.**

| Audience | Gets |
| --- | --- |
| Value stream lead and sponsors | The portfolio on one page: outcomes, health, dates, risks, and what needs a decision |
| Head of product and product leads | Features across all applications, a ranked backlog for the next PI, and a record of what was committed |
| Head of technology | One structure across applications, with capacity, dependencies and investment mix visible; a design that survives the move to Jira Cloud |
| Delivery leads | Spillover, blockers and release readiness from live filters in place of spreadsheets |
| Product owners | Credit for what their own application delivered, even when another application is late |
| Teams | No extra daily work. The daily habit stays with stories; everything above is updated weekly or less often |
| Jira administrators | Six requests, none of which adds a field or a status |

**What it costs.**

| Cost | Size |
| --- | --- |
| Stitching existing Epics to Features and VS Epics | Two half-day sessions per sub value stream, with its product owners |
| Weekly upkeep by a product owner | About ten minutes before the delivery sync |
| Building filters, dashboards and Confluence pages | A few days for the minimum set; done once by the framework owner |
| Jira administrator time | Six requests (section 17), four needed to start |
| Per-PI upkeep | Four small filter and rule edits by the delivery lead on set days |
| A named framework owner | Part of one person's time, ongoing |

**The path.** A two-week proof of concept on one real slice while this paper is reviewed; one decision meeting; then stitching in waves, top-down, finishing just before a PI planning so that planning becomes the first baseline. Section 18 has the detail.

**The decisions requested** are listed in section 20.

## 2. Why change

### What is hard today

| Question someone asks | What happens today | Why |
| --- | --- | --- |
| What is the value stream delivering this year? | A slide is assembled from several product owners' lists | Epics in different projects share no parent |
| Which applications does this initiative need, and which one is it waiting for? | Someone asks around | The same capability is a separate Epic in each project, with no join |
| What did we commit for this PI, and did we deliver it? | Recollection, or a spreadsheet kept by one person | Target PI is edited when plans change, so the record of the promise is lost |
| Is this late, and what is the plan? | A status meeting | RAG is used differently by each team, and often has no recovery plan behind it |
| Who is waiting on whom? | Discovered during the PI | Dependencies live in conversation, not in links |
| Can we take this new request? | A judgement call | Demand and capacity are not held in the same place |
| Where is our capacity going? | Not known | Kind of work is not recorded consistently |

### What it costs

- **Late surprises.** A Feature that needs three applications is only as early as its latest one, and the late one is found at the end of the PI.
- **Reporting effort.** Delivery leads rebuild the same status picture by hand each cycle.
- **Plans nobody can hold to account.** Without a fixed record of what was committed, predictability cannot be measured, so planning does not improve.
- **A harder Cloud migration.** Each project's private conventions have to be understood and carried across one by one.

### How the change will be judged

The project has its own measures. The starting figures have not been counted yet; counting them is part of the proof of concept.

![Figure 1: Success measures](charts/02_success_measures.png)

*Figure 1. Success measures for the project. Starting points are examples; targets are proposals.*

| Measure | Target after two PIs |
| --- | --- |
| Epics with a parent Feature | Above 95% |
| Features with a parent VS Epic | 100% |
| In-progress Features and Epics with RAG refreshed in the last two weeks | Above 90% |
| Portfolio sync run from the dashboard with no separate slide pack | Yes |
| Time spent each month assembling status reports | Halved |
| Cross-application dependencies found at planning, not during the PI | Rising |
| Teams saying the weekly update takes under ten minutes | Most |

## 3. Design principles and constraints

### Principles

1. **One line, top-down.** Every ticket can be reached from a VS Epic. Views start at the value stream and go down; nothing is reported from the bottom up by hand.
2. **Use what exists.** Existing issue types, statuses and fields only. Central administration makes new ones slow to get, and they would have to be migrated to Cloud.
3. **One meaning per field.** Each field answers one question and has one named person who keeps it right. That is what makes a filter reliable.
4. **The ticket is the status report.** Meetings are run from boards and dashboards, and tickets are updated in the room.
5. **A promise is recorded once and not edited.** What was committed at PI planning is kept as a baseline, so what happened can be compared with it.
6. **Judgement stays with people.** RAG is the owner's judgement, not a calculation. Gates are checked by people until the administrator can enforce them.
7. **Measure a group against its own past.** Story points and predictability are never used to rank teams against each other.
8. **Small upkeep.** Daily updates belong to stories. Nothing at Epic level or above needs a daily update unless something changed that day.

### Constraints the design works within

| Constraint | Consequence in the design |
| --- | --- |
| Jira Data Center today; Jira Cloud next year | Built on standard fields and links, not scripts. Section 17 lists what survives the move and what is redone. |
| Jira administration is central | No new fields or statuses. Six requests to the administrator, none structural. |
| No ScriptRunner | No scripted queries or calculated fields. A few standard automation rules instead. |
| Plans (Advanced Roadmaps) is available | The hierarchy above Epic, cross-project planning, capacity and roll-up of progress run in one plan. |
| Each application has its own project | The application is read from the project. Component is free for modules. |
| Confluence has Table Transformer and Chart from Table | Roll-ups and trends that Jira dashboards cannot produce are built there. |
| A PI is 12 weeks | Five two-week sprints and one planning sprint. |

---

# Part B: The model

## 4. Structure: two layers, one join

![Figure 2: The hierarchy](charts/01_hierarchy.png)

*Figure 2. The hierarchy with a worked example. The Feature "M&P across the platform" is delivered by two applications; each has its own Epic under the same Feature.*

**Portfolio layer: one Jira project for the whole value stream.** It holds only VS Epics, Features, Milestones and Delivery RAID. No team does sprint work here.

**Team layer: one Jira project per application.** Each holds Epics, Stories, Tasks, Bugs, Tests and Sub-tasks.

**The join is the Feature.** It lives in the portfolio project and is the parent of one Epic in each application that must change to deliver it.

### The levels

| Level | Issue type | Lives in | What it is | Size | Owner |
| --- | --- | --- | --- | --- | --- |
| 1 | VS Epic | Portfolio project | A business outcome for the value stream, usually crossing sub value streams | 2 to 4 PIs | Value stream lead |
| 2 | Feature | Portfolio project | A slice of a VS Epic that one sub value stream can deliver and show to users. May need several applications. | One PI; two only when planned that way and agreed | Product lead |
| 3 | Epic | Application project | One application's share of a Feature | 1 to 5 sprints | Application product owner |
| 4 | Story, Task, Bug, Test | Application project | A piece of work one team finishes in a sprint | Under one sprint | Team |
| 5 | Sub-task | Application project | A step inside a story. Optional. | Days | Individual |
| Side | Milestone | Portfolio project | A date that matters: regulatory deadline, go-live, PI boundary | A date | Delivery lead |
| Side | Delivery RAID | Portfolio project | A risk, assumption, issue or dependency that needs managing above team level | Until closed | Delivery lead |

### The worked example

| Level | Ticket | Where | Named as |
| --- | --- | --- | --- |
| VS Epic | Avoid audit risk through access control | Portfolio project | An outcome: what gets better, for whom |
| Feature | M&P across the platform | Portfolio project | A capability, with no application name in it |
| Epic | M&P for Credit Application | Credit Application project | The capability plus the application |
| Epic | M&P for Drawdowns | Drawdowns project | The capability plus the application |

### Five rules that keep the structure honest

1. **Every Epic has a parent Feature.** An Epic with no parent is invisible to the portfolio, appears on an exceptions list, and is not planned into a PI.
2. **Every Feature has a parent VS Epic.** Upkeep goes under one standing Feature per sub value stream per year, "Run and improve". That Feature has no Target PI and no commitment label, is left out of predictability, and is closed at year end.
3. **A Feature belongs to exactly one sub value stream:** the one accountable for the result. Its Epics may sit in any application, including one owned by another sub value stream.
4. **A Feature is never split by application.** The application split is the Epic's job.
5. **Stories never sit in the portfolio project, and Features never sit in an application project.**

### How ticket types relate

Parent relationships are strict: one parent only. Everything else is a link, and links can be many to many.

| From | To | How many | Recorded as |
| --- | --- | --- | --- |
| VS Epic | Feature | One VS Epic has many Features. A Feature has one VS Epic. | Parent Link on the Feature |
| Feature | Epic | One Feature has many Epics, often in different applications. An Epic has one Feature. | Parent Link on the Epic |
| Epic | Story, Task, Bug, Test | One Epic has many. Each has one Epic. | Epic Link |
| Story | Sub-task | One Story has many. | Built-in parent |
| VS Epic | Milestone | Many to many. A VS Epic usually has several Milestones; one regulatory date can serve several VS Epics. | blocks link (VS Epic blocks Milestone) |
| Feature | Milestone | Many to many. A go-live waits for several Features; a Feature can serve a pilot date and a full launch. | blocks link (Feature blocks Milestone) |
| Delivery RAID | VS Epic, Feature, Milestone | Many to many | relates to link |
| Feature | Feature | Many to many | blocks link |
| Epic | Epic | Many to many, usually across applications | blocks link |
| Feature | Sub value stream | Many Features to one sub value stream | Value Stream and Sub-Value Stream field |
| Feature | Program Increment | Many Features to one PI | Target PI field |
| Epic, Story, Bug | Release | Many to one release | Fix version in the application project |
| Feature | Application | Many to many | Read from the child Epics' projects |

Two guards keep the many-to-many links readable. Link a Milestone at the highest level that is true: to the VS Epic if the whole outcome is due, to specific Features if only they are. And when one Feature seems to need two parents, it is two Features.

### Stitching: joining what already exists

Each application product owner already has a list of Epics for next year. Nobody re-enters anything. The lists are joined upward in seven steps.

| # | Step | Who | Result |
| --- | --- | --- | --- |
| 1 | **List.** Every wanted Epic exists in its application project in Idea or Analysis, with a one-line purpose, a rough size and a hoped-for quarter. | Product owners | A complete starting list |
| 2 | **Cluster.** In one working session per sub value stream, group Epics that deliver the same capability in different applications. Each group becomes a Feature, and the Epics get it as Parent Link. | Product lead, product owners | Features with Epics beneath them |
| 3 | **Lift.** Group Features by the outcome they serve. Each group becomes a VS Epic. | Value stream lead, product leads | The cross-stream picture |
| 4 | **Place the leftovers.** An Epic that shares a capability with nobody gets a Feature of its own if users will notice it, or goes under "Run and improve" if it is upkeep. | Product lead | No orphan Epics |
| 5 | **Look down from the top.** For each Feature, ask which applications must change. Where one has no Epic, add a placeholder or mark the Feature as partial. | Product lead | Gaps found before planning |
| 6 | **Spot clashes.** Two applications building the same thing differently become a Delivery RAID issue or a blocks link. | Delivery lead | Clashes on record |
| 7 | **Check.** The hygiene filter returns nothing, every Feature has a VS Epic, every VS Epic has an owner. | Framework owner | Stitching complete |

What this produces is the candidate backlog for the year: every Epic reachable from a VS Epic. It is not yet a plan. Sequencing and Target PI come from PI planning.

## 5. Fields, labels and links

### The connecting fields

| Question it answers | Field | On which tickets | Rule |
| --- | --- | --- | --- |
| Which sub value stream? | Value Stream and Sub-Value Stream | VS Epic, Feature, Epic, Milestone, Delivery RAID, Bug, Test | An Epic takes the value of its parent Feature, even when it sits in another sub value stream's application |
| Which application? | Project | Epic and below | The project itself |
| Which module? | Component | Epic and below | One component per module |
| Which PI was it planned for? | Target PI | Feature, Epic | Set at PI planning. Not changed afterwards for committed work. |
| Which PI did it finish in? | Actual PI | Feature, Epic | Set by automation when the ticket reaches Released |
| Which production release? | Fix versions | Epic, Story, Bug | One version per release in each application project |
| Which team? | Team | Epic, Story, Task, Bug | The shared team from Plans |
| What kind of work? | Enabler Type; Regulatory or Control Change Type | Feature | Set at triage. Drives the investment mix. |
| How is it going? | RAG Status, Path to Green, Date to Green, Executive Summary | VS Epic, Feature, Epic, Milestone, Delivery RAID | Reviewed weekly by the owner |
| What comes first? | The four scoring fields and Weighted Shortest Job First Score, then Rank | VS Epic, Feature | Scored in Analysis |
| When is it due? | Due date; Start date and End Date for the plan | All | Due date is the date people outside the team are told |

### RAG: one meaning for each colour, at every level

| Colour | Means | Owner must also |
| --- | --- | --- |
| **Green** | On track for its date. No help needed. | Nothing |
| **Amber** | The date is at risk and the owner has a recovery plan | Fill in Path to Green and Date to Green |
| **Red** | The date will be missed unless someone outside the team decides or acts | Say what is needed and from whom; on a Feature, set Management Attention |

A parent is never greener than the facts beneath it: a Feature with a Red Epic is at least Amber. A RAG nobody has touched for two weeks is treated as unknown. Raising Amber early is the right thing to do; staying Green until the last week is what the rule exists to stop.

### Labels: four small groups, and no others

| Label | Used on | Meaning | Set by |
| --- | --- | --- | --- |
| `pi-committed` or `pi-stretch` | Feature, and each of its Epics | Firm commitment for the Target PI, or a stretch goal | Product owner on the Epic, product lead on the Feature, at PI planning only |
| `unplanned` | Feature, Epic | Entered a PI after planning closed, by decision | Delivery lead |
| `pi-descoped` | Feature, Epic | Taken out of a PI after planning closed, by decision | Delivery lead |
| `ms-regulatory`, `ms-golive`, `ms-pi`, `ms-external` | Milestone | The kind of Milestone | Delivery lead |

### Links: three types only

| Link | Use |
| --- | --- |
| **blocks / is blocked by** | A real dependency between two Features or two Epics. The ticket that must finish first blocks the other. |
| **relates to** | Ties a Delivery RAID ticket to the work it concerns |
| **duplicates** | Closes repeat requests at intake |

### The field shortlist

Each issue type offers between about 18 and 60 fields on its screen. The framework reads only a shortlist. Core fields are always filled in; the others only when the situation applies. Any field not on the shortlist is left as the organisation's standards require and is read by no filter, dashboard or report here.

![Figure 3: Field shortlist](charts/19_fields_per_issue_type.png)

*Figure 3. Fields the framework uses, against fields offered on the screen. Screen totals are approximate.*

| Issue type | Core fields (always) | Only when it applies | Set by Jira or automation |
| --- | --- | --- | --- |
| **VS Epic** (16) | Summary, Description, Assignee, Value Stream and Sub-Value Stream, Objective ID, Business Benefits, the four scores, Start date, End Date, Due date, RAG Status, Executive Summary, Linked work items | Path to Green, Date to Green, Financial Benefit (USD), Regulatory or Control ID, Change Reason, Flagged | Weighted Shortest Job First Score |
| **Feature** (17) | Summary, Description, Assignee, Parent Link, Value Stream and Sub-Value Stream, Enabler Type, Acceptance Criteria, Business Benefits, T-Shirt Size, the four scores, Target PI, Labels, Due date, RAG Status | Start date, End Date, Path to Green, Date to Green, Management Attention, Executive Summary, Regulatory or Control Change Type, Regulatory or Control ID, Architectural Governance, Contains Resiliency Work, Change Reason, Linked work items, Flagged | Actual PI, Weighted Shortest Job First Score |
| **Epic** (14) | Summary, Epic Name, Description, Assignee, Parent Link, Components, Team, Story Points, Target PI, Labels, End Date, RAG Status, Fix versions, Linked work items | Start date, Change Request ID, Regulatory or Control Change Type, Flagged | Actual PI, Value Stream and Sub-Value Stream |
| **Story** (8) | Summary, Description, Epic Link, Acceptance Criteria, Story Points, Assignee, Sprint, Components | Fix versions, Story Type, Flagged | Status, Resolution |
| **Task** (6) | Summary, Description, Epic Link, Assignee, Sprint, Story Points | Acceptance Criteria, Flagged | Status, Resolution |
| **Sub-task** (3) | Summary, Assignee, Parent | Flagged | Status |
| **Bug** (11) | Summary, Description, Epic Link, Severity, Priority, Testing Phase, Environment, Affects versions, Assignee, Sprint, Components | Fix versions, Root cause category, Root cause analysis, Flagged | Status, Resolution |
| **Test** (7) | Summary, Description, Epic Link, Testing Phase, Environments, Assignee, Sprint | Fix versions | Status, Resolution |
| **Milestone** (9) | Summary, Description, Assignee, Value Stream and Sub-Value Stream, Due date, Baseline End Date, RAG Status, Labels, Linked work items | Path to Green, Date to Green, Executive Summary, Regulatory or Control ID, Fix versions | |
| **Delivery RAID** (9) | Summary, Description, RAID Type, Assignee, Value Stream and Sub-Value Stream, RAG Status, Due date, Impact, Linked work items | Risk: Probability, Risk Trigger Event, ROAM Response. Dependency: Dependency Type, Supplier Value Stream and Sub Value Stream, Baseline End Date. Issue: Impact Details, Path to Green, Date to Green. | |

**An open point on Epic.** From the standards page, Epic does not appear to carry Path to Green, Date to Green or Due date. Until that is confirmed or the fields are added, an Epic's expected go-live date is its End Date, and the recovery plan for an Amber or Red Epic is a comment starting "Path to green:". This is decision 7 in section 20.

**Two rules keep the list short.** A field joins the shortlist only when a filter, dashboard, report or decision reads it. And when one is added, another is reviewed for removal.

## 6. Workflows and gates

The existing statuses are enough. What is missing today is a shared meaning for each one and a rule for entering it.

![Figure 4: Feature lifecycle](charts/23_feature_lifecycle.png)

*Figure 4. The life of a Feature. The same pattern, with fewer statuses, applies to VS Epics and Epics.*

### VS Epic

| Status | Meaning | To enter it |
| --- | --- | --- |
| Idea | Someone has raised it. No commitment. | Summary, sponsor and the problem in two sentences |
| Review | The portfolio sync is deciding whether it is worth analysing | Triage owner assigned |
| Analysis | A named lead is shaping it: outcome, measure of success, sub value streams involved, rough size | Accepted at the portfolio sync |
| Ready | Approved to start. Split into Features for at least the next PI. | Outcome and success measure written, first Features created, sponsor sign-off |
| Implementing | At least one Feature is being built | First child Feature moves to Implementing |
| Released | Every planned Feature is live in production | All child Features Released or Done |
| Done | The outcome has been checked against the success measure | Benefit review recorded |

### Feature

| Status | Meaning | To enter it |
| --- | --- | --- |
| Idea | Raised, not yet triaged | Intake details filled in |
| Analysis | Product lead is writing acceptance criteria, naming the applications and agreeing the design | Parent VS Epic, sub value stream and Enabler Type set |
| Ready | Can be pulled into a PI | Definition of ready met (section 7) |
| Implementing | At least one child Epic is in progress | Target PI, commitment label and RAG Status set |
| Testing | All child Epics are built. End-to-end testing across applications is running. | Every story in every child Epic is Done and deployed to test |
| Validation | Business users are confirming it does what was asked | End-to-end test passed, no open severity 1 or 2 bug |
| Released | Live in production | Business sign-off recorded, change record linked, every child Epic Released, Done or closed as Won't Do |
| Done | Early-life support closed | Support period over with no open critical bug |

### Epic

| Status | Meaning | To enter it |
| --- | --- | --- |
| Idea | Placeholder created during Feature analysis | Parent Feature set |
| Analysis | Team is breaking it into stories and estimating | Product owner assigned |
| Ready | Stories for the first two sprints are written and estimated | Estimate recorded, dependencies linked |
| Implementing | Stories are being built or tested, or are finished and waiting for go-live | Sprint work started |
| Released | Live in production | Fix version set and released, Change Request ID set |
| Done | Nothing left, including clean-up | All child issues closed |

### Story, Task, Bug, Test, Delivery RAID, Milestone: Backlog, In Progress, Done

| Type | Backlog means | In Progress means | Done means |
| --- | --- | --- | --- |
| Story, Task, Bug, Test | Not started | Being worked on in a sprint | Meets the team's definition of done |
| Delivery RAID | Raised, owner not yet acting | Owner is actively managing it | Closed: mitigated, accepted, resolved or no longer relevant |
| Milestone | Date agreed, not started | Work towards it is under way | Date met, with the actual date in a comment |

### Four conventions that avoid new statuses

| Need | Convention |
| --- | --- |
| Blocked | The Jira flag, not a status. A flagged card turns yellow and can be filtered. |
| Cancelled | A resolution, not a status: Done with resolution "Won't Do". Only resolution "Done" counts as delivered. |
| On hold | A move back to Ready with a comment |
| A review or test step for stories | One optional extra status, "In Review", and only if teams need it |

### Definition of done at each level

| Level | Done means |
| --- | --- |
| Story | Acceptance criteria met, code reviewed, automated tests pass, tested in the team environment, no open severity 1 or 2 defect |
| Epic (to Released) | All stories Done; integration and regression tests passed; non-functional needs met or a waiver recorded; Fix version and Change Request ID set; support notes handed over |
| Feature (to Released) | Every Epic Released; end-to-end test across applications passed; business acceptance recorded; sign-offs closed; no open severity 1 or 2 defect |
| Feature (to Done) | Early-life support closed; Business Benefits reviewed against what was expected |
| VS Epic (to Done) | Outcome measured against its success measure and recorded |

---

# Part C: How work flows

## 7. Intake and design

### One front door for new demand

New demand has one front door, the DDT, and the DDT is used for nothing else. Next year's existing Epic lists do not go through it; they are stitched (section 4). Delivery is never tracked in the DDT.

| | In the DDT | In Jira |
| --- | --- | --- |
| What it holds | Demand that is not yet in anyone's backlog | Everything agreed, and everything being delivered |
| What is decided there | Whether to do it, the rough timeline, the proposed PI | Scope detail, the application split, the commitment, progress |
| What comes out | An agreed demand with a proposed PI | A Feature (or VS Epic) carrying the DDT reference, then its Epics |
| Who looks at it | Requesters, product leads, the value stream lead | Teams, product owners, delivery leads, sponsors |

The Idea status in Jira is therefore not a second front door. Only two things arrive there: candidate Features created during stitching, and demand already agreed in the DDT. A proposed PI from the DDT is a proposal: it becomes Target PI only at PI planning.

### From agreed demand to a Ready Feature

| Step | What happens | In Jira |
| --- | --- | --- |
| 1. Hand over | The demand is agreed in the DDT | Product lead creates a Feature in status Idea with the DDT reference, sponsor, problem and outcome, any hard date, and the applications likely to change. The DDT entry is closed. |
| 2. Triage, weekly | The product lead decides when there is capacity to shape it | Sets sub value stream, Enabler Type and parent VS Epic; moves the Feature to Analysis, or closes it as a duplicate or Won't Do |
| 3. Analyse and design | Scope, design and the application split are worked out | Acceptance Criteria and Business Benefits; design page linked; sign-off tasks raised; one placeholder Epic per application with an estimate; blocks links; Delivery RAID for outside dependencies |
| 4. Score and rank | The sub value stream scores its Features together | The four scores filled in; the Feature placed in order on the board |

### Definition of ready for a Feature

A Feature moves to Ready only when all of these are true:

- [ ] Parent VS Epic, sub value stream and Enabler Type are set.
- [ ] Acceptance Criteria and Business Benefits are filled in and agreed with the sponsor. T-Shirt Size and the four scores are filled in. (A regulatory Feature with a fixed date needs its Milestone and Regulatory or Control ID instead of scores.)
- [ ] Every application that must change has a child Epic, and each Epic has a rough size.
- [ ] Design is linked, with any architecture, risk or control approvals required.
- [ ] Dependencies are linked, and outside dependencies have a RAID ticket with an owner.
- [ ] It fits in one PI, or it is an agreed two-PI Feature. Otherwise it is split.

### Unplanned work

An urgent request after PI planning has closed still comes through the DDT. It enters the PI only by a decision of the product lead and delivery lead together (the value stream lead if it touches more than one sub value stream), and the decision names what moves out. What comes in gets Target PI and the `unplanned` label; what goes out gets `pi-descoped`. Production incidents stay in the incident tool; the fix becomes a Bug carrying the incident reference.

## 8. Roadmap, sizing and prioritisation

### Three levels of plan

| Level | Horizon | Grain | Dated by | Owner | View |
| --- | --- | --- | --- | --- | --- |
| **L0 roadmap** | 12 to 18 months | VS Epics, with Features as bars inside them, and Milestones | PI or quarter | Value stream lead | Plan view "L0 roadmap" |
| **L1 PI plan** | One PI, 12 weeks | Features and Epics | Sprint | Product and delivery leads | Plan view "Current PI" |
| **L2 sprint plan** | Two weeks | Stories | Day | Team | Team board |

### The L0 roadmap

![Figure 5: L0 roadmap](charts/03_l0_roadmap.png)

*Figure 5. The L0 roadmap. It is a saved view of the same plan used for PI planning, so it cannot drift from the detail beneath it.*

How it is built:

1. After stitching, every VS Epic and Feature gets a Start date and End Date at PI precision: the first day of the PI it should start in and the last day of the PI it should end in. Nothing finer.
2. In the plan, a view named "L0 roadmap" is saved: hierarchy from VS Epic to Feature only, timeline in quarters, coloured by RAG Status, with Milestones shown by Due date.
3. Confidence is marked by distance. The current PI is committed. The next PI is planned. Anything later is a forecast shown by PI only. A roadmap without this marking is read as a promise.
4. It is reviewed at the fortnightly portfolio sync and re-issued after every PI planning.

### Sizing a VS Epic

The size firms up in three stages, and the roadmap says which stage a number is at.

| Stage | When | Source of the number | Accuracy |
| --- | --- | --- | --- |
| 1. Rough | Stitching, or DDT agreement | T-Shirt Size on each Feature, turned into points with one conversion table calibrated from finished Features | Within a factor of two |
| 2. Planned | Feature in Analysis | Story Points on each Epic, given by the team that will build it | Good enough to commit a PI |
| 3. Detailed | Epic in Implementing | Sum of Story Points on its stories | Good enough to forecast a date |

### Prioritising: Weighted Shortest Job First

Features and VS Epics already carry four scores: User/Business Value, Time Criticality, Risk Reduction / Opportunity Enablement, and Job Size. The first three are added and divided by job size. A higher score goes first.

![Figure 6: WSJF ranking](charts/17_wsjf_ranking.png)

*Figure 6. Ready Features in score order. The list above the line is the proposal for the next PI.*

Two rules make scores comparable: each sub value stream scores its Features together in one session, against each other; and scores use one short scale (1, 2, 3, 5, 8, 13, 20). Regulatory work with a fixed date is not argued through the score: it gets a Milestone, and the date decides.

## 9. PI planning

Planning a PI means deciding which Ready Features, and which of their Epics, get that PI in the Target PI field.

![Figure 7: PI calendar](charts/24_pi_calendar.png)

*Figure 7. The PI calendar, with the Jira actions that fall on fixed days.*

### Before (weeks 7 to 10 of the current PI)

| Week | Must be true | In Jira |
| --- | --- | --- |
| 7 | Features proposed for the next PI are at least in Analysis; new demand for that PI has closed | |
| 9 | Proposed Features are Ready | Delivery lead creates the two per-PI filters. Product leads set Target PI on proposed Features (the draft). |
| 10 | Each team's capacity is known; dependencies are linked | Capacity entered in the plan; sprints created and named |

A Feature that is not Ready by week 9 does not enter planning.

### During (two days)

1. Carried-over work is placed first.
2. Each product owner sets Target PI on the Epics the team can take, and stories are dragged into sprints up to capacity.
3. For each Feature, the product lead checks that every child Epic, in every application, has the Target PI. If one application cannot take its share, the Feature is moved, cut down, or planned over two PIs on purpose.
4. New dependencies are linked in the room. Unresolved ones become Delivery RAID tickets with an owner before the day ends.
5. Each Epic that stays, then each Feature, gets `pi-committed` or `pi-stretch`, a date, and RAG Status Green.
6. A confidence vote is taken and recorded on the planning Milestone.

![Figure 8: Capacity against demand](charts/11_capacity_vs_demand.png)

*Figure 8. Load against capacity. The Drawdowns team is over capacity before stretch work is counted, which is settled in the room, not discovered in week 10.*

### What goes into a PI plan, in this order

1. Spillover from the PI that is ending. It uses capacity before anything new.
2. Epics tied to a regulatory or go-live Milestone that falls in or just after the PI.
3. Committed Features by score, each with all of its Epics.
4. Stretch Features, clearly labelled.

### Commitment is made twice

Each product owner commits the Epic for their application. The product lead commits the Feature only when every one of its Epics is committed. Both are measured, so one late application is visible without marking down the others.

### The lock, and the baseline

| Must be true to close planning | In Jira |
| --- | --- |
| Every committed Feature has all its Epics committed | Label and Target PI on each |
| Every team's load is within capacity | Capacity view in the plan |
| Every dependency has both ends planned, giver before receiver | Dependencies view in the plan |
| Risks raised in the room have an owner and a response | Delivery RAID tickets |
| Confidence vote taken | Comment on the planning Milestone |
| The delivery lead announces the lock | Committed list pasted into the PI scorecard page as a plain table |

**That pasted table is the baseline.** It is the only list predictability is counted from, and nobody edits it afterwards. After the lock, Target PI and the commitment labels change only by decision.

### What is touched in Jira at each PI

Filters are live: a saved filter is a question Jira answers again each time it is opened. When a product owner sets Target PI on an Epic, it appears in the PI filters, dashboards and Confluence pages straight away. Nothing is rebuilt. Four small edits are made per PI.

| When | What | Who |
| --- | --- | --- |
| Week 9, when drafting begins | Create two filters: `PI <next> planned Features` and `PI <next> planned Epics` | Delivery lead |
| The day planning closes | Paste the committed list into the new PI scorecard page | Delivery lead |
| Day 1 of the new PI | Repoint `VS: PI planned Features` and the first part of `VS: PI Epics` to the new PI's filters | Delivery lead |
| Day 1 of the new PI | Add the ended PI to the list in `VS: spillover`; change the PI value in automation rule 4 and the board quick filter | Delivery lead |

Old per-PI filters are kept and never edited, because old scorecards read them.

### The plan in Plans

One plan for the value stream is where the steps above are carried out.

| Setting | Value |
| --- | --- |
| Sources | The portfolio project and the board of every application team |
| Hierarchy | VS Epic down to Sub-task, with progress rolling up from stories |
| Columns | Target PI, Actual PI, RAG Status, Team, Due date, Weighted Shortest Job First Score |
| Dates | Start date and End Date schedule the bars. Due date stays the promise made outside the team. |
| Teams | One shared team per application team, tied to its board, with capacity from recent velocity |
| Releases | The release versions from the application projects |
| Dependencies | blocks links, drawn as lines; a link whose dates conflict is marked |
| Saved views | L0 roadmap; current PI; dependencies only; by team for capacity; Amber and Red only |

One habit to teach: changes made in a plan stay in the plan until someone presses Review changes and saves them to Jira. During PI planning, one named person per sub value stream saves at each break.

## 10. Delivery control

Four questions matter most in delivery, and each has one field, link or label that answers it.

| Question | Answered by | Seen in |
| --- | --- | --- |
| What blocks what? | blocks links between Epics and between Features; Delivery RAID dependencies across sub value streams | The plan's dependencies view; filter `VS: open blockers` |
| What is in the PI plan? | Target PI on the Epic and on the Feature | The plan filtered to the PI; filter `VS: PI Epics` |
| What spilled over? | Target PI is an earlier PI and the ticket is not finished | Filter `VS: spillover` |
| What was delivered late or in part? | Actual PI compared with Target PI, Epic by Epic | Confluence: Feature progress across applications; the PI scorecard |

### Which application is a Feature waiting for?

![Figure 9: Feature progress across applications](charts/04_feature_by_application.png)

*Figure 9. One row per Feature, one column per application. This view does not exist today; it is the main reason for the Feature-to-Epic join.*

### Spillover

- **Definition.** A committed Epic or Feature whose Target PI has ended and which has not reached Released. Nobody declares it; the fields show it.
- **Target PI is not edited to hide it.** The ticket keeps its original Target PI and gets its Actual PI when it finishes. Even if someone did edit it, the baseline table still holds the promise.
- **Where it sits in the next PI.** The current-PI filters and the plan's current view include it automatically, and it takes capacity first.
- **Every spillover gets a reason** at the PI review: Dependency, Capacity, Scope, Defect or Environment.
- **Every spillover gets a decision:** carry on (the default), stop, or split.
- **Early warning during the PI:** committed Epics not started by week 5; Amber and Red RAG; blockers past their date.

### Planned for one PI, delivered by one application only

A worked case. Feature "M&P across the platform" is committed for PI 2027.4 with two committed Epics.

| Ticket | Target PI | At the end of PI 2027.4 | Actual PI | Scorecard result for PI 2027.4 |
| --- | --- | --- | --- | --- |
| Epic: M&P for Credit Application | PI 2027.4 | Released | PI 2027.4 | Delivered |
| Epic: M&P for Drawdowns | PI 2027.4 | Implementing | PI 2028.1, when it finishes | Spilled |
| Feature: M&P across the platform | PI 2027.4 | Implementing | PI 2028.1, when its last Epic finishes | Spilled, 1 of 2 Epics delivered |

What each person sees:

- Credit Application's Epic figure counts its Epic as delivered. That team is not marked down for another team's delay.
- Drawdowns shows one spilled Epic, with a reason.
- The Feature figure counts the Feature as spilled, and the view in figure 9 shows which application it is waiting for.
- In planning for PI 2028.1, the Drawdowns Epic is already in the current-PI views and takes capacity first.

Then one decision at the PI review. If the Credit Application part is useful to users by itself, the Feature may be split so the delivered part can be released. **A split never improves the score:** the baseline line for the original Feature stays "spilled". If nothing is usable until both applications are live, the Feature simply carries on.

### The PI scorecard and predictability

For every committed line in the baseline, the scorecard shows one of four results: delivered, spilled, descoped by decision, or stopped.

![Figure 10: PI scorecard](charts/07_pi_scorecard.png)

*Figure 10. The PI scorecard by application.*

Three figures are reported side by side: committed Features delivered, committed Epics delivered, and the same weighted by story points. Stretch and unplanned results are listed beneath them, not hidden.

![Figure 11: Predictability trend](charts/06_predictability_trend.png)

*Figure 11. Predictability across PIs. Around 80% is a healthy level to learn from, not a target; a figure that sits at 100% usually means too little was committed.*

![Figure 12: Spillover reasons](charts/08_spillover_reasons.png)

*Figure 12. Spillover reasons. Five words are enough to show a pattern after two PIs; here, dependencies would be the thing to fix first.*

### Dependencies

- The ticket that must finish first **blocks** the other. Epic to Epic when two applications depend on each other; Feature to Feature when two capabilities do.
- A blocker must be planned to finish before the blocked ticket starts. A blocker with a later Target PI than the ticket it blocks is a planning error, fixed in the room.
- A dependency between teams inside one sub value stream is a link. It needs a Delivery RAID ticket when it crosses sub value streams, involves an outside party, or is at risk.
- When a team is actually stopped, it sets the flag. A link is a forecast; a flag is a fact.

![Figure 13: Dependency matrix](charts/15_dependency_matrix.png)

*Figure 13. Open cross-stream dependencies. Each side sees the same ticket from its own end: "what we are waiting for" and "what we owe".*

## 11. Release planning

A release is a version in an application project. A PI is a planning window; a release is a production deployment; one PI usually holds several releases. They are kept apart on purpose.

### Naming

| Case | Version name | Example |
| --- | --- | --- |
| One application goes live alone | `<APP> <year>.<month>` | `DRAW 2027.03` |
| Several applications go live together | Same name created in each project | `CLP 2027.03` in three projects |
| Emergency fix | `<APP> <year>.<month> HF<n>` | `DRAW 2027.03 HF1` |

### Entering and leaving a release

| Stage | Must be true | In Jira |
| --- | --- | --- |
| Enter | The release is on the change calendar | Delivery lead creates the version in each application project, same name, with the go-live date |
| | Scope is known | Fix version set on the Epics, Stories and Bugs going in, during sprint planning |
| | Two sprints before go-live | Release gadgets reviewed weekly |
| | One sprint before go-live: scope cut-off | Anything not Done is moved to the next version; the product lead is told |
| | Go or no-go decided through the change process | Decision recorded on the go-live Milestone; change record number in Change Request ID on the Epics |
| Exit | Deployed to production | Delivery lead marks the version as released in each project |
| | | Product owners move Epics to Released. Automation fills in Actual PI. |
| | Every Epic of a Feature is Released, Done or closed as Won't Do | Product lead moves the Feature to Released |
| | Milestone met | Milestone moved to Done, with the actual date in a comment |

![Figure 14: Release readiness](charts/22_release_readiness.png)

*Figure 14. Release readiness two sprints before go-live.*

**Two limits to know.** A released version in one project does not release the same-named version in another; each is marked. And version charts treat same-named versions in different projects as separate, so cross-application release views use filters on the shared name.

## 12. Delivery RAID and Milestones

Both live only in the portfolio project and are always linked to the work they affect, so they appear on that Feature or VS Epic and on every dashboard above it.

### Delivery RAID

| RAID Type | Raise it when | Fields that must be filled | Closes when |
| --- | --- | --- | --- |
| Risk | Something may go wrong and would move a Feature date or a Milestone | Probability, Impact, Impact Details, Risk Trigger Event, ROAM Response, Due date as the next review date | The response is Resolved or Accepted, or the event has passed |
| Assumption | A plan depends on something not yet confirmed | The assumption, who can confirm it, Due date as the confirm-by date | Confirmed, or converted to a risk or issue |
| Issue | Something has gone wrong and needs help from outside the team | Impact, Impact Details, Path to Green, Date to Green, RAG Status | Resolved |
| Dependency | Work is needed from another sub value stream, another value stream, or an outside party | Dependency Type, Supplier Value Stream and Sub Value Stream, Due date as the need-by date, Baseline End Date as the date first agreed | Delivered and accepted by the receiver |

ROAM Response on a risk means: **R**esolved, **O**wned (a named person is acting), **A**ccepted (the sponsor has agreed to live with it), **M**itigated. A risk with no response has not been reviewed. An accepted risk is not closed: it stays open with the name of the person who accepted it and a date for the next review.

![Figure 15: RAID overview](charts/14_raid_overview.png)

*Figure 15. Open Delivery RAID by type and RAG, and open risks by Probability and Impact.*

### Milestones

| Kind | Example | Label |
| --- | --- | --- |
| Regulatory or audit date | Remediation of an audit finding due | `ms-regulatory` |
| Go-live | A module live for a business line | `ms-golive` |
| PI boundary | PI planning, PI end demo | `ms-pi` |
| External commitment | A data feed from another division available | `ms-external` |

- **Baseline End Date** is the date first committed and is never changed. **Due date** is the current target. The gap is the slippage.
- When Due date moves, the reason goes in a comment, and Path to Green and Date to Green are updated.
- Every Feature or VS Epic that must finish for the date is linked with **blocks**, so the Milestone lists everything it is waiting for.
- Regulatory Milestones carry the Regulatory or Control ID. A regulatory Feature is planned before scored work and is never labelled stretch.

![Figure 16: Milestone slippage](charts/13_milestone_slippage.png)

*Figure 16. Milestone slippage, read from two existing date fields.*

## 13. Managing the portfolio

A large portfolio goes wrong in a few predictable ways: too much is started, nobody wrote down what an outcome was meant to achieve, and reports describe activity. Six practices at VS Epic level address those, using fields the VS Epic already has.

| Practice | What it is | How it runs |
| --- | --- | --- |
| A stated outcome and case on every VS Epic | Before analysis is approved, the VS Epic says what will improve, by how much, at what rough cost and risk | Business Benefits and the impact fields on the VS Epic, plus a one-page case in Confluence. Required to leave Analysis. |
| A limit on work in progress | A cap on how many VS Epics may be in Analysis and in Implementing at once | Column limits on the VS Epic board. Breaches are discussed at every portfolio sync. |
| A link to strategy | Every VS Epic names the objective it serves | Objective ID on the VS Epic |
| Investment mix | The share of capacity going to each kind of work, against the intended share | Confluence page: story points by objective and by Enabler Type |
| Benefits review | Three and six months after release, a named owner measures the promised benefit | A VS Epic stays at Released until the review is recorded, then moves to Done |
| A rule for stopping | Agreed grounds for stopping a VS Epic | Decided at the portfolio sync; closed as Won't Do with the reason |

![Figure 17: WIP limits](charts/21_wip_limits.png)

*Figure 17. Work-in-progress limits on the VS Epic board. Limits start from the number of people able to lead an analysis and the number of VS Epics the teams can carry in parallel.*

### Investment mix and capacity split

Before each PI, every team reserves capacity by kind of work, so urgent items cannot crowd out the rest. A starting split, to be adjusted from each team's own history after two PIs:

| Kind of work | Starting share | Counted from |
| --- | --- | --- |
| Committed Features, business | 50% | Epics whose Feature has no Enabler Type |
| Enablers, resilience and technical debt | 15% | Enabler Type; Contains Resiliency Work |
| Regulatory and control change | By demand, planned first | Regulatory or Control Change Type |
| Run work, production defects and incidents | 20% | Bugs, and Epics under "Run and improve" |
| Unplanned reserve | 15% | Tickets labelled `unplanned` |

The shares are a proposal, not a finding (decision 9 in section 20).

![Figure 18: Investment mix](charts/12_investment_mix.png)

*Figure 18. Intended split against what was actually done.*

### Size and forecast of a VS Epic

For each application under a VS Epic: remaining points divided by that team's PI velocity gives the PIs still needed. The VS Epic finishes when its slowest application does.

![Figure 19: Story points per VS Epic](charts/09_points_per_vs_epic.png)

*Figure 19. One line per VS Epic: total, done, remaining, PIs to go, and the application that limits it.*

![Figure 20: VS Epic burn-up](charts/20_vs_epic_burnup.png)

*Figure 20. Burn-up of one VS Epic. Scope growth is shown separately from progress, so a moving target is not mistaken for slow delivery.*

### Velocity above the team

| Measure | What it is | Used for |
| --- | --- | --- |
| Team velocity | Story points finished per sprint, average of the last three | Team capacity in the plan |
| PI velocity, per application | Story points finished in a PI by those teams | How much can be taken into the next PI |
| Planned against delivered | Points with this Target PI at the lock, against points finished | Whether plans are realistic |
| Feature throughput | Features reaching Released per PI | The outcome view; harder to inflate than points |

![Figure 21: PI velocity](charts/10_pi_velocity.png)

*Figure 21. PI velocity by application. Story points mean different things in different teams, so this chart compares each application with its own past only.*

![Figure 22: Created versus resolved](charts/16_created_vs_resolved.png)

*Figure 22. Features created against Features finished. A widening gap means the value stream is taking on more than it finishes.*

### Twelve questions the value stream lead answers every month

| # | Question | Answered from |
| --- | --- | --- |
| 1 | Which VS Epics are in progress, and are we inside the limit? | Jira: VS Epic board |
| 2 | Which VS Epics are Red or Amber, and what is the path to green? | Jira: dashboard 1 |
| 3 | Which Features under each VS Epic are late or spilled? | Confluence: portfolio tree |
| 4 | How far is each VS Epic, in Features and in story points? | Confluence: portfolio tree and forecast |
| 5 | Did we deliver what we committed last PI? | Confluence: PI scorecard |
| 6 | What is stuck, and for how long? | Jira: Analysis over 30 days; spillover |
| 7 | Where is capacity going, by objective and by kind of work? | Confluence: investment mix |
| 8 | Is demand for the next PI above capacity? | The plan: capacity view |
| 9 | Which dependencies across applications are open or overdue? | Jira: open blockers; cross-stream dependencies |
| 10 | Which risks and issues need a decision? | Jira: dashboard 4 |
| 11 | Which dates have moved? | Confluence: milestone slippage |
| 12 | Which released VS Epics are due a benefits review? | Jira: VS Epics at Released |

---

# Part D: Seeing it

## 14. Dashboards and reports

Reporting runs top-down in one line: VS Epics, then Features across the whole value stream, then Epics across applications, then the team. **There is no separate set of views per sub value stream.** The sub value stream is a column to sort or group by, never a filter that hides the rest.

Three places hold the views, each for what it does best.

| Place | Best for | Cannot do |
| --- | --- | --- |
| **Jira dashboards** (standard gadgets on saved filters) | Live lists and counts: what is Red, what is flagged, what is overdue, status by application | Roll up the hierarchy; compare today with what was planned; show trends across PIs |
| **The plan in Plans** | The hierarchy with progress rolled up; timeline and roadmap; capacity; dependencies | Be embedded widely; keep history |
| **Confluence** (Jira Issues macro, Table Transformer, Pivot Table, Chart from Table) | Roll-ups across applications; trends across PIs; slippage; the PI scorecard and its baseline | Show more than about 1,000 issues per macro; update without a page refresh |

### The five Jira dashboards

| # | Dashboard | For | Answers |
| --- | --- | --- | --- |
| 1 | Value stream portfolio | Value stream lead, sponsors | What are the outcomes, how is each going, what needs a decision, which dates are close |
| 2 | Features across the value stream | Product leads, delivery leads | What is being delivered this PI and under which VS Epic; what is off track; what is ready next |
| 3 | Epics across applications | Delivery leads, product owners | How far each application is with its share; which application spills; what is blocked or not started |
| 4 | Risks, dates and releases | Delivery leads | Serious risks and issues; who is waiting on whom; which dates moved; is the next release ready |
| 5 | Team (one per application team) | Product owner, scrum master | Sprint health; what is blocked today; what rolled over; which Epics are invisible to the portfolio |

Each dashboard uses ten gadgets or fewer, all standard: Filter Results, Pie Chart, Two Dimensional Filter Statistics, Created vs Resolved, Sprint Health, Sprint Burndown.

![Figure 23: Dashboard 1 mock-up](charts/27_dashboard_mockup.png)

*Figure 23. Mock-up of dashboard 1. The real page is assembled from standard gadgets; the layout will differ in detail.*

![Figure 24: Features by sub value stream and RAG](charts/26_features_rag_by_svs.png)

*Figure 24. Dashboard 2: Features across the value stream, grouped by sub value stream.*

![Figure 25: Epics by application and status](charts/05_epics_by_application.png)

*Figure 25. Dashboard 3: Epics across applications.*

### The two boards

| Board | Columns | Notes |
| --- | --- | --- |
| VS Epic board | The VS Epic statuses | Column limits for work in progress |
| Feature board | The Feature statuses | One swimlane per VS Epic; card colours by RAG Status; quick filters for Current PI, Committed, Red and Amber, Flagged |

Neither board is split by sub value stream. Each application team keeps its own Scrum or Kanban board.

### The Confluence portfolio pages

| Page | Built from | Shows |
| --- | --- | --- |
| Portfolio tree | VS Epics and Features joined on parent | Each VS Epic with its Features counted: released, Red, late |
| Feature progress across applications | Epics of the PI grouped by parent Feature | Figure 9: one row per Feature, its Epics by application, and the worst RAG among them |
| PI scorecard (one page per PI) | The pasted baseline table joined to that PI's own filter | Figure 10: what happened to every committed line; also holds the PI objectives |
| Predictability trend | Committed Features and Epics with Target PI and Actual PI | Figure 11 |
| Size and forecast by VS Epic | Epics under open VS Epics with Story Points, joined upward | Figure 19 |
| PI velocity | Stories and bugs resolved in the PI, summed by project | Figure 21 |
| Investment mix | Features with Enabler Type and their Epics' points | Figure 18 |
| Milestone slippage | Milestones with Baseline End Date and Due date | Figure 16 |
| Weekly status report | Red and Amber tickets with Executive Summary and Path to Green | The exceptions report for the portfolio sync, in the owners' own words |
| Roadmap | The shared plan view, or VS Epics drawn as a Gantt chart | Figure 5 |
| Dependencies | Delivery RAID dependencies pivoted by receiver and supplier | Figure 13 |

### Where each figure in this paper would be built

The figures in this paper were drawn for the paper. The table says where the live equivalent comes from. Three are marked as not available from standard tools without extra upkeep.

| Figure | Live source | Notes |
| --- | --- | --- |
| 1 Success measures | Confluence: a small table of counts from the hygiene filters, charted | Counts are typed in monthly; Jira keeps no history of them |
| 2 Hierarchy, 3 Field shortlist, 4 Lifecycle, 7 PI calendar, 27 Rollout | Explanatory diagrams | Not built from data |
| 5 L0 roadmap | Plans: saved view "L0 roadmap" | Fallback: Confluence Gantt with Chart from Table |
| 6 WSJF ranking | Jira: Filter Results sorted by score | As a bar chart: Confluence Chart from Table |
| 8 Capacity against demand | Plans: capacity view by team and sprint | The PI-level bar is a Confluence chart from Epic points and a typed capacity table |
| 9 Feature progress across applications | Confluence: Table Transformer and Pivot Table | Appears as a table; cell colours need the macro's conditional formatting |
| 10 PI scorecard, 11 Predictability trend | Confluence: baseline table joined to live Jira data | The core Confluence pages |
| 12 Spillover reasons | Confluence: counted from the reason column on the scorecard | |
| 13 Dependency matrix | Confluence: Pivot Table on Delivery RAID dependencies | Appears as a table of counts |
| 14 Release readiness | Jira: dashboard 4 gadgets | |
| 15 RAID overview | Jira: Two Dimensional Filter Statistics | Works if the fields are plain dropdowns; to be tested |
| 16 Milestone slippage | Confluence: date difference with Table Transformer | |
| 17 WIP limits | Jira: column limits on the VS Epic board | The board shows the breach; the bar chart is illustration |
| 18 Investment mix, 19 Points per VS Epic, 21 PI velocity | Confluence: Table Transformer sums, charted | |
| 20 VS Epic burn-up | **Not standard.** The plan shows progress now, not its history | Needs a small table updated each sprint on Confluence, or an add-on |
| 22 Created versus resolved | Jira: Created vs Resolved gadget | |
| 23 Dashboard mock-up, 24, 25 | Jira: dashboards 1, 2 and 3 | Figure 24 depends on the sub value stream field working as a gadget axis; fallback in section 17 |
| 26 Hygiene trend | Confluence: monthly counts typed into a table, charted | **Manual monthly entry**; Jira keeps no history |

### What standard Jira cannot show, and the way round it

| Wanted | Why a gadget cannot | Where it comes from |
| --- | --- | --- |
| Percentage complete of a Feature from its stories | Gadgets do not roll up the hierarchy | The plan: progress bar per Feature and per VS Epic |
| Feature progress across applications as a table | Same reason | Confluence |
| Predictability trend across PIs; scope added and removed | Jira keeps no snapshot of what was planned | Confluence, from the pasted baseline |
| Time spent waiting versus working | Needs time in each status | An add-on, or an export to a reporting tool |
| Deployment frequency and failure rate | That data sits in release and incident tools | Those tools |

### Data quality

The views are only as good as the tickets. Six hygiene filters are reviewed monthly, and the count per application is published.

| Filter | Why it matters |
| --- | --- |
| Epics without a parent Feature | Work the portfolio cannot see |
| Tickets without a sub value stream | Missing from every grouped view |
| Released without Actual PI | Predictability cannot be counted |
| In progress without Target PI | Work started outside the plan |
| Done without resolution | Missed by the trend gadgets |
| Open with a resolution | Wrongly counted as finished |

![Figure 26: Hygiene trend](charts/18_hygiene_trend.png)

*Figure 26. Hygiene exceptions over the first six months. The expected shape: a steep fall during stitching, then a low level held by the monthly check.*

---

# Part E: Running it

## 15. Roles: what changes for whom

### Before and after, by role

| Role | Stops | Starts | Keeps |
| --- | --- | --- | --- |
| **Value stream lead** | Asking for slide packs before each review | Running the portfolio sync from dashboard 1 and the VS Epic board; keeping VS Epic status, RAG and Executive Summary current fortnightly; deciding order and limits | Accountability for outcomes and priorities |
| **Head of product, product leads** | Tracking Features in spreadsheets; negotiating scope per application | Owning Features in the portfolio project; scoring and ranking them; committing a Feature only when every application has committed its Epic; weekly Feature RAG | Ownership of scope and acceptance |
| **Head of technology** | Receiving capacity and dependency news late and by word of mouth | Reading capacity against demand, investment mix and dependency views from one place; sponsoring the administrator requests; holding technology leads to the definition of done | Accountability for engineering capacity, quality and the platform |
| **Delivery leads** | Assembling status by hand; keeping a private list of what was committed | Owning Delivery RAID, Milestones, release versions and the per-PI filter edits; pasting the baseline at the lock; running the PI scorecard | Running delivery and release governance |
| **Application product owners** | Planning their application in isolation | Giving every Epic a parent Feature; setting Target PI and the commitment label at PI planning; ten minutes weekly on status, RAG, date and release | Ownership of the application backlog and its Epics |
| **Business analysts, designers** | Design decisions living only in documents | Building the Feature in Analysis: Acceptance Criteria, design link, the list of applications, sign-off tasks | Analysis and design work itself |
| **Scrum masters, team leads** | Rolling every unfinished story over by default | Sprint naming to the convention; checking every story has an Epic; closing sprints on the last day | Running the team's sprint events |
| **Engineers, testers** | Nothing | Using the flag when blocked, and removing it the same day; raising Bugs under the right Epic with Severity, Testing Phase and Environment | Daily story updates, as now |
| **Jira administrators** | Fielding one-off requests from each team | Six requests (section 17); a single framework owner as the point of contact | Central control of fields, statuses and schemes |

### The one-minute card for working-level people

| When | Do this |
| --- | --- |
| You start a piece of work | Move it to In Progress. Make sure it is assigned to you and is in the sprint. |
| You are stopped by something outside your control | Flag the ticket and add one line saying what you are waiting for and from whom |
| You are no longer stopped | Remove the flag the same day |
| You finish | Move it to Done, having checked the definition of done |
| You find a defect | Raise a Bug under the right Epic, with Severity, Testing Phase and Environment |
| You discover your work needs another team | Tell your product owner the same day, so the two Epics can be linked |
| You realise it will not finish this sprint | Say so at stand-up. Do not wait for the last day. |

Three things to remember: **status is true today, blocked means flagged, and every story has an Epic.**

Working-level people never need to touch Target PI, Actual PI, RAG Status, Parent Link, commitment labels or the Fix version on Epics.

### What is kept up to date, and how often

| How often | Epic (product owner) | Feature (product lead) | VS Epic (value stream lead) | Milestone and Delivery RAID (delivery lead) |
| --- | --- | --- | --- | --- |
| **The same day** | Flag on or off. Status when it changes. A new dependency linked. | Flag. Management Attention when a decision is needed now. | Flag | A new risk, issue or outside dependency raised with an owner |
| **Weekly** | Status. RAG. End Date still true. Fix versions. Recovery plan if Amber or Red. | Status against its Epics. RAG. Path to Green and Date to Green if Amber or Red. Due date. | | Blockers past their date chased. Flags reviewed. |
| **Fortnightly** | | | Status. RAG. Executive Summary. Rank order. | Every Red and Amber RAID ticket. Milestone dates and RAG. |
| **Monthly** | Hygiene: no Epic without a parent | Hygiene: no Feature without parent, sub value stream or Enabler Type | Work in progress against the limit | Every open RAID ticket reviewed or closed |
| **Each sprint** | Fix versions. Story Points revised once stories are estimated. | | | Release versions and dates |
| **Each PI, at planning** | Target PI. Commitment label. End Date. RAG to Green. | Target PI. Commitment label. Due date. RAG to Green. | Start date and End Date for the roadmap | Planning Milestone. Dependencies from the room. |
| **Each PI, at the close** | Reason for any spillover | Change Reason for anything descoped, split or carried over | Executive Summary reflects the PI result | Scorecard completed |
| **Once, then left alone** | Parent Link, Epic Name, Components, Team | Parent Link, sub value stream, Enabler Type, Acceptance Criteria, Business Benefits | Objective ID, Business Benefits | Baseline End Date, RAID Type |
| **Never typed** | Actual PI; sub value stream (copied from the Feature) | Actual PI; the calculated score | The calculated score | |

Nothing at Epic level or above needs a daily update unless something actually changed that day.

## 16. Operating rhythm and governance

### Seven recurring meetings

Each is held on a named Jira board or dashboard, so the ticket is updated in the room and not afterwards.

| Meeting | How often | Who | Held on | What changes in Jira |
| --- | --- | --- | --- | --- |
| Team daily and sprint events | Daily, per sprint | Application team | Team board | Stories move; blockers flagged |
| Backlog refinement | Weekly | Product owner, team | Team backlog | Epics move Analysis to Ready; stories estimated |
| Backlog triage | Weekly, 30 minutes | Product lead, delivery lead | Feature board, Idea column | New Features accepted into Analysis, merged or closed |
| Delivery sync | Weekly | Product lead, delivery lead, product owners | Dashboards 2 and 3 | Feature status checked against Epics; RAG and recovery plans refreshed; flags and links reviewed |
| Portfolio sync | Fortnightly | Value stream lead, product and delivery leads | VS Epic board and dashboard 1 | VS Epics move through the pipeline; Red and Amber RAID reviewed; Milestone dates confirmed |
| RAID review | Monthly | Delivery leads | Dashboard 4 | Every open RAID ticket gets a comment and a new review date, or is closed |
| PI planning and PI review | Every 12 weeks | Everyone | The plan and the PI scorecard | Target PI set for the next PI; the closing PI scored |

### Who decides

| Decision | Decided by | Where | Escalates to |
| --- | --- | --- | --- |
| Whether new demand is taken on | Owner of the DDT decision | DDT | Value stream lead |
| Order of VS Epics | Value stream lead | Portfolio sync | Sponsor |
| Order of Features in a sub value stream | Product lead, from the scores | Scoring session | Value stream lead |
| Whether an application takes an Epic into a PI | That application's product owner | PI planning | Product lead of the Feature |
| Two sub value streams want one team | Value stream lead | Portfolio sync | Sponsor |
| A fixed regulatory date against a higher-scored Feature | The date wins; value stream lead confirms what gives way | Portfolio sync | Sponsor |
| Scope in or out after the PI lock | Product lead and delivery lead together | Delivery sync | Portfolio sync |
| Carry on, stop or split a spillover | Product lead and delivery lead | PI review | Value stream lead |
| Go or no-go for a release | Per the change process; delivery lead records it | Release readiness review | Change authority |
| A change to this framework, a field, a status or a label | Framework owner | Monthly, with a change log | Value stream lead |

**One framework owner is named.** Without one, each team adjusts the model and the cross-application views stop working within a year.

### Sign-offs and audit evidence

A comment can be edited and is weak evidence. Each required approval is recorded as a Task or Sub-task on the Feature, named for the approval (architecture, risk, control, business acceptance), assigned to the approver and closed by the approver. Jira's history then shows who approved and when, and the person who built the change is not the person who closed the approval. Where the system of record for an approval is another tool, the Task holds the reference and that tool holds the evidence.

### Defects, testing and incidents

- A defect found in any test phase is a Bug under the Epic it belongs to, with Severity, Testing Phase and Environment.
- One severity scale is used everywhere. Priority is the order of work and is not used to mean severity.
- A Feature cannot leave Validation with an open severity 1 or 2 Bug under any of its Epics.
- A production defect is a Bug in the application project with the incident reference, under the Epic that introduced it if known, otherwise under "Run and improve".
- Bugs found in production against a Feature released in the last PI are counted as escaped defects on the PI scorecard.

### PI objectives and improvement

Each sub value stream writes three to six objectives for the PI in business language on the scorecard, each marked committed or uncommitted. The sponsor gives each a planned value at planning and an achieved value at the review. This sits beside the predictability count and is harder to inflate, because someone outside the team does the scoring. Each PI review ends with no more than five improvement actions, each a Task with an owner and a date.

### When the rules are not followed

The hygiene count per application is published monthly. The order of escalation is product owner, then product lead, then value stream lead. Two rules have teeth: **an Epic without a parent Feature is not planned into a PI, and a Feature that fails the definition of ready is not committed.**

### Five failure patterns to watch for

| Pattern | Countermeasure |
| --- | --- |
| Everything is Green until the week it turns Red | The RAG rules, and asking for the evidence behind a Green at the weekly sync |
| Epics that stay open for a year | The size limits; closing or splitting anything older than four PIs |
| New fields, statuses and labels added team by team | The framework owner and the change log |
| Dashboards that count activity | Lead with Features released, objectives achieved and Milestones met; keep story points for planning |
| A tool rollout with no coaching | A proof of concept, role briefings, and a named person each team can ask |

---

# Part F: Building it

## 17. Technology view

This section is for the head of technology, architecture, and the Jira and Confluence administrators.

### Footprint

| Item | Count | Notes |
| --- | --- | --- |
| New issue types | 0 | |
| New custom fields | 0 | All fields used are on the standards list |
| New statuses | 0 | One optional status, "In Review" for stories, only if teams ask |
| New link types | 0 | blocks, relates to, duplicates |
| New add-ons | 0 | Plans, Table Transformer and Chart from Table are already installed |
| Labels | 9 | In four groups; no others |
| Saved filters | About 45, plus 7 per application team | All hang off five base filters |
| Dashboards | 4 for the value stream, 1 per team | Standard gadgets only |
| Boards | 2 in the portfolio project | Team boards unchanged |
| Plans | 1 | With five saved views |
| Automation rules | 7 | Four of them inside a single project each |
| Confluence pages | About 12, plus one scorecard per PI | |

### Six requests to the Jira administrator

None adds a field or a status. The first four are needed to start; the last two can follow the proof of concept.

| # | Request | Why | Without it |
| --- | --- | --- | --- |
| 1 | Show Parent Link, Target PI, Actual PI, RAG Status and the sub value stream field on the create, edit and view screens of Epic in every application project | Product owners can set and see them. This is the join between applications. | The fields can only be set from inside the plan |
| 2 | A user group for the value stream that can create shared filters and dashboards and edit the plan and its shared teams | A dashboard is blank for anyone who cannot see the filter | Each person builds their own |
| 3 | A resolution screen on the transition to Done for every issue type, with resolutions Done and Won't Do; resolution cleared on reopen | Trend and predictability figures depend on resolution | Cancelled work counts as delivered |
| 4 | Automation rule 1, across the portfolio project and the application projects | Epics inherit the sub value stream of their Feature | Set by hand; gaps caught by the hygiene filter |
| 5 | Make Target PI, Actual PI, RAG Status and the sub value stream field available as columns and filters in Plans | The plan can be filtered and saved by PI, colour and sub value stream | Filter the plan by a saved Jira filter |
| 6 | Workflow checks: a Feature cannot leave Analysis without Parent Link, sub value stream and Enabler Type, and cannot enter Implementing without Target PI and RAG Status | The definition of ready enforces itself | Product leads check by hand |

One decision for the administrator, not a request: Released on Feature and Epic should sit in the green Done category only if a resolution is set at that point. The filters name the statuses directly, so they work either way.

### Automation rules

| # | Rule | Trigger | Action | Scope |
| --- | --- | --- | --- | --- |
| 1 | Copy sub value stream down | An Epic is created, or its Parent Link changes | Copies the sub value stream from the parent Feature to the Epic | Across projects (administrator) |
| 2 | Shadow label | The sub value stream changes on a portfolio ticket | Writes a matching `svs-` label. Needed only if the field fails as a gadget axis. | Portfolio project |
| 3 | Ask for a recovery plan | RAG changes to Amber or Red while Path to Green is empty | Comments on the ticket, naming the assignee | One project |
| 4 | Record the finishing PI | A Feature or Epic moves to Released with Actual PI empty | Sets Actual PI to the current PI | One project |
| 5 | Chase stale trouble | Every Monday | Emails the assignee of each Amber or Red ticket not updated in 14 days | One project |
| 6 | Chase overdue RAID | Every Monday | Comments on each overdue RAID ticket | Portfolio project |
| 7 | Keep Parent Link clean | An issue changes type | Clears Parent Link, which otherwise keeps a stale value | Administrator |

Rules 3 to 6 are built first; each sits inside one project. Rule 1 is the one to test carefully: vendor documentation describes copying from a parent to its children when the parent changes, and this rule works from the child's side.

### How the queries work on Data Center

| Need | Mechanism |
| --- | --- |
| Join Epic to Feature, and Feature to VS Epic | `"Parent Link"` |
| Join Story to Epic | `"Epic Link"` |
| Everything under one ticket | `issuekey in childIssuesOf("KEY")`, for one VS Epic at a time |
| Sub value stream, if a two-step dropdown | `cascadeOption("parent", "child")` |
| Epics of a PI across applications | Target PI on the Epic, set at PI planning |
| What changed, and when | Jira can search Status history, not custom field history. So "RAG not refreshed" uses the ticket's last update, and scope added after planning uses the `unplanned` label. |

### Known limits, and the fallbacks

| Limit | Status | Fallback |
| --- | --- | --- |
| A two-step dropdown is not supported as a column in Plans | Confirmed from documentation | Shadow label written by automation rule 2 |
| A two-step dropdown may not work as a dashboard gadget axis | Not confirmed either way; to be tested | Shadow label; or the Confluence page in place of the gadget |
| The Jira Issues macro in Confluence shows about 1,000 issues at most | From documentation; exact limit to be checked | Keep each macro's filter narrow: one PI, or one VS Epic |
| The Parent Link column in the macro showed raw text on some Jira versions | Reported for versions 10.5 to 10.7 | Check the installed version; use a helper column if affected |
| Importing Parent Link by CSV works only through the administrator's import route | From documentation | Stitch inside the plan by drag and drop; or ask the administrator to run the import |
| Jira cannot tell whether the far end of a blocks link is still open | By design | The plan's dependencies view is the accurate one; the filter is a chase list |
| Jira keeps no snapshot of a plan | By design | The baseline table pasted into Confluence at the lock |
| A released version in one project does not release the same name in another | By design | Mark each; search by the shared name |
| No program board (teams by sprints) in standard Plans | By design | Timeline grouped by team; a board add-on if wanted later |

### Permissions and security

| Topic | Approach |
| --- | --- |
| Who can see what | One user group for the value stream; every shared filter and dashboard is shared with it |
| Who can edit the plan | Product leads, delivery leads and the framework owner |
| Who can build automation | Project administrators for rules inside one project, if the central setting allows it; the central administrator for rules across projects |
| Sensitive tickets | The existing Security Level field |
| Filter ownership | The framework owner owns the shared filters; they are never renamed, because dashboards, the plan and Confluence pages refer to them by name |
| Separation of duties | An approval is a task closed by the approver, not by the person who built the change |

### Performance and scale

- Each Jira dashboard uses ten gadgets or fewer, against a default limit of twenty.
- The filters that walk the hierarchy (`childIssuesOf`) are used for one VS Epic at a time, since the vendor notes they can be slow or over-inclusive on very large parents.
- Confluence pages pull through the Jira Issues macro, so each is kept to one PI or one level of the hierarchy.

### What has and has not been verified

| Item | State |
| --- | --- |
| Internal consistency of the framework | Reviewed by an independent pass; contradictions found were fixed |
| Technical claims about Jira, Plans and the Confluence macros | Checked against vendor documentation where the pages could be read |
| Field names | Read from a photo of the standards page; to be checked letter for letter |
| Every query, import and Confluence recipe | **Not yet run on real data** |
| The sub value stream field as a gadget axis; the macro's row limit; automation rule 1 | Could not be confirmed from documentation; each has a fallback |

### The move to Jira Cloud

The migration date is set by the central Jira team. The framework treats it as a fixed event to plan around.

| Survives the move unchanged | Needs rework after the move |
| --- | --- |
| The hierarchy and the stitched parents | Saved filters that use Parent Link or Epic Link (rewritten with the single `parent` field) |
| Field meanings, RAG rules, commitment rules | Automation rules (re-tested) |
| Labels | The plan, its teams and saved views (may need rebuilding) |
| Ways of working, rhythm, decision rights | Confluence pages (re-tested against the Cloud editions of the add-ons) |
| PI scorecards pasted as tables | Dashboards (re-pointed at the rewritten filters) |
| People's habits | |

Two consequences for sequencing. Before the migration, the full set of rules and habits is put in place but only the minimum of Jira and Confluence machinery is built: the base filters, three dashboards and three Confluence pages. The rest is built once, on Cloud.

**One question for the migration team, to settle early:** on Jira Cloud, levels above Epic and Plans need the Premium plan. If the Cloud site is on a lower plan, VS Epic and Feature lose their place in the hierarchy and this design needs a different join. This is open question 3 in section 20.

## 18. Implementation path

![Figure 27: Rollout plan](charts/25_rollout_plan.png)

*Figure 27. The proposed path. Week numbers are relative; the last step should land on a PI planning date.*

### Step 0: Before anything is circulated (days 1 to 2)

| Action | Why |
| --- | --- |
| Agree who approves this paper, and by when | Without a named approver and a closing date, review does not end |
| Brief the Jira administrator and the sponsor in person | The six requests are the longest wait, and are better heard first in conversation than in a paper sent to everyone |
| Tell the Cloud migration team this is coming | So this work and theirs do not undo each other |

### Step 1: Proof of concept (weeks 1 to 2)

**Scope.** One real slice: one VS Epic, two or three Features, two or three applications. The access-control example in section 4 fits. It is run in the live Jira or a test project, with real field names.

**What it must prove.** These are the nine checks the framework depends on.

| # | Check | Pass when |
| --- | --- | --- |
| 1 | Field names match the standards page letter for letter | Every query in the filter library saves without error |
| 2 | Those fields are live in today's Data Center projects | Each can be set on a test ticket of the right type |
| 3 | Allowed values of Enabler Type, RAG Status, RAID Type, ROAM Response, Severity and the PI format are known | Written into the queries |
| 4 | Whether the sub value stream field is a two-step dropdown, and whether a gadget accepts it | One gadget built; shadow label switched on if it fails |
| 5 | The rule for when Actual PI is filled in, and whether Target PI may change | Confirmed with the owner of the standards |
| 6 | Each base filter returns the right tickets | Checked by hand against the slice |
| 7 | The Jira version, and the Parent Link column in Confluence | One Confluence page shows the parent correctly |
| 8 | Whether project administrators may create automation rules | Rule 3 built and fired once |
| 9 | What the DDT records and which Jira field holds its reference | Agreed with the DDT owner |

**What it must produce.** Dashboard 1 for the slice; the "Feature progress across applications" page in Confluence; the starting counts for the success measures; and a list of what did not work.

### Step 2: Review (end of week 1 to end of week 2)

This paper is circulated with screenshots from the proof of concept, with a fixed comment window of five to seven working days. No reply by the closing date counts as agreement. Comments are made against the decisions in section 20.

### Step 3: Decision (end of week 2)

One meeting: **go, go with changes, or stop.** The outcome and the changes are written into a decision record.

### Step 4: Stitch in waves, build the minimum, brief by role (from week 3)

| Wave | What | Done when |
| --- | --- | --- |
| 1 | VS Epics and Features created top-down in the portfolio project | Every VS Epic has an owner; every Feature has a parent |
| 2 | The first group of applications gives every open Epic a parent Feature | The hygiene filter returns nothing for those projects |
| 3 | The remaining applications do the same | The hygiene filter returns nothing for the value stream |
| Alongside | Base filters, dashboards 1 to 3, three Confluence pages (portfolio tree, Feature progress, PI scorecard) | A lead can answer "what are we delivering and where is it" from them |
| Alongside | Role briefings: working level (30 minutes), product owners (60), leads (90), each ending in a hands-on exercise | Each role has had its session and its guide |

Stitching in waves limits rework: if review changes the structure, only the wave in flight is redone.

### Step 5: The first PI planning by the rules

The rollout should end just before a PI planning, so that planning becomes the first baseline. Finishing mid-PI means the first scorecard is half-measured.

### The larger programme

| # | Chunk | Goal | Rough length |
| --- | --- | --- | --- |
| 0 | Mobilise | Agreement, owner, administrator requests raised, baseline counted | 3 to 4 weeks (steps 0 to 3 above) |
| 1 | Foundation on Data Center | Stitched, and run through one PI with the minimum build | 1 PI |
| 2 | Cloud migration | Arrive on Cloud with the hierarchy, fields and habits intact | Set by the migration team |
| 3 | Scale across the value stream | Full dashboards, filter library and Confluence portfolio | 1 to 2 PIs |
| 4 | Portfolio management | Limits on work in progress, cases on VS Epics, benefits reviews, forecasting | 1 to 2 PIs |
| 5 | Run and improve | The framework is owned, measured and changed like any other product | Ongoing |

### Communication still to be written

| Item | For whom | Length |
| --- | --- | --- |
| Sponsor message: this is how we work from date X, and why | Everyone | Half a page |
| What changes for you, by role (from section 15) | Each role | One page each |
| One-page picture with a real example | Everyone | One slide |
| Timeline with dates | Everyone | One slide |
| Decision record | Leads, auditors | One page, kept current |
| Glossary and questions and answers (appendices A and B) | Everyone | Three pages |
| Training, by role, with the mock data | Each role | Three short sessions |
| Proof of concept results | Sponsors, sceptics | One page |
| Where to get help | Everyone | A few lines |

## 19. Risks

| Risk | Sign | Response |
| --- | --- | --- |
| Administrator requests are not delivered | No date after two weeks | Sponsor raises it; meanwhile parents and fields are set from inside the plan |
| Product owners have no time for stitching | Sessions cancelled twice | Sponsor protects the time; do it in two half-days, not spread over weeks |
| Leaders keep asking for slides | A slide pack appears for the portfolio sync | The sponsor runs the next sync from the dashboard |
| A field does not behave as assumed | A proof-of-concept check fails | Each check has a fallback (section 17); the design is adjusted before rollout, not after |
| Structure changes after tickets are linked | Review comments arrive late | The fixed comment window, and stitching in waves |
| Migration lands mid-PI | Cut-over date inside sprints 1 to 5 | Ask for a move to a planning sprint, or freeze structure and accept a week of rework |
| The Cloud licence does not support levels above Epic | The migration team cannot confirm the plan tier | Design the fallback join (issue links) before cut-over |
| RAG and predictability are used to rank or blame | Teams stay Green; commitments shrink | The principles in section 3; leaders respond to an early Amber with help |
| The framework grows | New fields and labels each month | The framework owner says no by default, and retires as much as is added |
| The update burden is felt as more administration | Tickets go stale between syncs | Keep to the shortlist; measure the weekly time; remove what nobody reads |

## 20. Decisions requested and open questions

### Decisions requested from reviewers

Please comment against the number.

| # | Decision | Proposed | Who decides |
| --- | --- | --- | --- |
| 1 | Adopt the hierarchy VS Epic > Feature > Epic > Story, with one portfolio project and one project per application | Yes | Value stream lead, head of product, head of technology |
| 2 | Adopt the status meanings and gates in section 6 without new statuses | Yes | Head of product, delivery leads |
| 3 | Adopt the RAG rules in section 5 at every level | Yes | Value stream lead |
| 4 | Commitment is made twice (Epic, then Feature), and the baseline is the table pasted at the lock | Yes | Product leads, delivery leads |
| 5 | Target PI is not edited for committed work; Actual PI is set at Released | Yes, subject to the standards owner | Standards owner |
| 6 | The DDT is the only front door for new demand, and is used for nothing else | Yes | DDT owner, value stream lead |
| 7 | Epic: add Path to Green, Date to Green and Due date to the screen, or keep End Date and a comment | Add them if they exist as fields | Jira administrator |
| 8 | Approve administrator requests 1 to 4 now, and 5 and 6 after the proof of concept | Yes | Head of technology, Jira administrator |
| 9 | The starting capacity split in section 13 | As a starting point for two PIs | Head of technology, head of product |
| 10 | No views or filter sets per sub value stream; everything starts from the value stream | Yes | Value stream lead |
| 11 | Name the framework owner, the sponsor and the approver of this paper | Names to be given | Sponsor |
| 12 | The implementation path in section 18, ending on a PI planning | Yes; date to be set | Value stream lead |

### Open questions

| # | Question | For |
| --- | --- | --- |
| 1 | When is Actual PI meant to be filled in, and may Target PI change after planning? | Owner of the Jira standards |
| 2 | May project administrators create automation rules? | Jira administrator |
| 3 | Which plan tier will the Cloud site be on, and does it include levels above Epic and Plans? | Cloud migration team |
| 4 | What is the Cloud cut-over date, and can it fall in a planning sprint? | Cloud migration team |
| 5 | Is recording sign-offs as Jira tasks acceptable evidence, or must another system hold it? | Risk, control, audit |
| 6 | What does the DDT record, and which Jira field holds its reference? | DDT owner |
| 7 | What is the date of the next PI planning? | Delivery leads |
| 8 | What early-life support period applies before a Feature moves to Done? | Head of technology |

### How to comment

Comment against a decision number or a section number. Say whether the point blocks agreement or is a suggestion. Comments close on the date given in the covering note.

---

# Appendices

## Appendix A: Glossary

| Term | Meaning |
| --- | --- |
| Value stream (VS) | The whole chain of work that delivers credit and lending to customers |
| Sub value stream | One part of that chain, with its own product lead |
| VS Epic | A business outcome for the value stream, lasting two to four PIs |
| Feature | A slice of a VS Epic that one sub value stream can deliver in one PI, possibly needing several applications |
| Epic | One application's share of a Feature |
| Stitching | Joining existing Epics upward to Features and VS Epics, without re-entering them |
| Program Increment (PI) | A 12-week planning window: five two-week sprints and a planning sprint |
| Target PI | The PI a Feature or Epic was planned for |
| Actual PI | The PI it finished in |
| Committed, stretch | A firm promise for the PI, or a goal that is not promised |
| Baseline | The list of committed work, pasted as a table when PI planning closes, and never edited |
| Spillover | Committed work whose Target PI has ended and which is not yet Released |
| Predictability | The share of committed work delivered in its Target PI |
| RAG | Red, Amber, Green: the owner's judgement of whether the date will be met |
| Path to Green | The recovery plan for an Amber or Red ticket |
| Delivery RAID | A ticket for a Risk, Assumption, Issue or Dependency managed above team level |
| ROAM | How a risk is being handled: Resolved, Owned, Accepted, Mitigated |
| Milestone | A ticket for a date that people outside the teams care about |
| DDT | The tool where new demand is raised and agreed before it enters Jira |
| WSJF | Weighted Shortest Job First: a score that puts high-value, small jobs first |
| L0 roadmap | The year view of VS Epics and Milestones |
| Plans | Jira's planning tool (formerly Advanced Roadmaps): hierarchy, timeline, capacity |
| Flag | Jira's marker for a ticket that is blocked right now |
| Fix version | Jira's field for the production release a ticket ships in |
| Hygiene filter | A saved search that lists tickets breaking a rule |
| Framework owner | The one person who owns the rules, the shared filters and the change log |

## Appendix B: Questions people will ask

| # | Question | Answer |
| --- | --- | --- |
| 1 | Why are we doing this, and why now? | Because nobody can see an initiative across applications, plans are made per application, and dates slip without warning. Now, because next year's Epic lists exist and the Cloud migration is easier from one structure than from many. |
| 2 | Is this more administration for my team? | For engineers and testers: no change beyond using the flag. For a product owner: about ten minutes a week. This will be measured. |
| 3 | Do we have to re-enter our Epics? | No. Existing Epics get a parent Feature. Nothing is retyped. |
| 4 | Who decides which Feature my Epic belongs to? | The product lead and product owners together, in the stitching session |
| 5 | What if my Epic does not fit any Feature? | If users will notice it, it gets a Feature of its own. If it is upkeep, it goes under "Run and improve". |
| 6 | Will my team be compared with others on story points or predictability? | No. Each group is measured against its own past. |
| 7 | What happens if we miss a committed Epic? | It shows as spilled, gets a reason and a decision at the PI review, and is planned first in the next PI. Around 80% delivered is a healthy level. |
| 8 | Is RAG going to be used against me? | The rule works the other way: an early Amber with a plan is the right behaviour, and a late Red is the failure. |
| 9 | We have our own board and labels. Do we lose them? | Team boards stay. Team labels stay, but the nine framework labels are reserved and no filter reads any other. |
| 10 | How does this relate to the DDT? | The DDT is where new demand is agreed. Jira is where agreed work is planned and delivered. |
| 11 | What changes when we move to Cloud? Will we do this twice? | The structure, rules and habits carry over. Filters, dashboards and the plan are rebuilt once, which is why only the minimum is built before the move. |
| 12 | Who do I tell if a rule does not work for my team? | The framework owner. Proposals are decided monthly, and what changed is published. |

## Appendix C: Key saved filters

Placeholders: `CLP` is the portfolio project; `CA, DRAW, FL` stand for the application projects; `PI 2027.1` is the current PI as the Target PI field writes it. Every query is to be tested once on real data.

**The five base filters**

| Save as | Query | At each PI change |
| --- | --- | --- |
| PI 2027.1 planned Features | `project = CLP AND issuetype = Feature AND "Target PI" = "PI 2027.1"` | Create a new one. Never edit an old one. |
| PI 2027.1 planned Epics | `issuetype = Epic AND project in (CA, DRAW, FL) AND "Target PI" = "PI 2027.1"` | Create a new one |
| VS: PI planned Features | `filter = "PI 2027.1 planned Features"` | Repoint |
| VS: spillover | `issuetype in (Feature, Epic) AND project in (CLP, CA, DRAW, FL) AND "Target PI" in ("PI 2026.3", "PI 2026.4") AND labels = pi-committed AND status not in (Released, Done)` | Add the PI that has just ended |
| VS: PI Epics | `filter = "PI 2027.1 planned Epics" OR (filter = "VS: spillover" AND issuetype = Epic) OR (issuetype = Epic AND project in (CA, DRAW, FL) AND status = Implementing)` | Repoint the first part |

`VS: PI Epics` means "every Epic the value stream is working on in this PI". Its three parts pick up the plan, the carried-over work, and anything in progress outside the plan.

**A selection of the rest**

| Save as | Query |
| --- | --- |
| VS: open VS Epics | `project = CLP AND issuetype = "VS Epic" AND status not in (Idea, Done) ORDER BY Rank` |
| VS: current PI Features | `filter = "VS: PI planned Features" OR (project = CLP AND issuetype = Feature AND status in (Implementing, Testing, Validation))` |
| VS: committed Features | `filter = "VS: PI planned Features" AND labels = pi-committed` |
| VS: Ready, no Target PI | `project = CLP AND issuetype = Feature AND status = Ready AND "Target PI" is EMPTY ORDER BY "Weighted Shortest Job First Score" DESC` |
| VS: Analysis over 30 days | `project = CLP AND issuetype = Feature AND status = Analysis AND NOT status changed AFTER -30d` |
| VS: PI Epics not started | `filter = "VS: PI Epics" AND status in (Idea, Analysis, Ready)` |
| VS: open blockers | `(filter = "VS: current PI Features" OR filter = "VS: PI Epics") AND issueLinkType = blocks AND status not in (Released, Done) ORDER BY duedate` |
| VS: flagged | `(project = CLP OR filter = "VS: PI Epics") AND Flagged = Impediment` |
| VS: open RAID | `project = CLP AND issuetype = "Delivery RAID" AND statusCategory != Done` |
| VS: Milestones next 90 days and overdue | `project = CLP AND issuetype = Milestone AND statusCategory != Done AND duedate <= endOfDay("+90d") ORDER BY duedate` |
| VS: hygiene exceptions | `project in (CA, DRAW, FL) AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` |
| Release: scope | `fixVersion = "CLP 2027.03"` |
| Team: Epics without Feature | `project = DRAW AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` |

The complete library is in the framework document (appendix D).

## Appendix D: Detailed guides

This paper is the overview. The working detail is in the companion documents in the same repository.

| Document | What it adds |
| --- | --- |
| [FRAMEWORK.md](../FRAMEWORK.md) | The full framework, including the complete filter library and every dashboard's gadget list |
| [WAYS_OF_WORKING.md](../WAYS_OF_WORKING.md) | Day-to-day practice: principles, roles, rhythm, a weekly hygiene check and a 30-day start list |
| [JIRA_UPDATE_GUIDE.md](../JIRA_UPDATE_GUIDE.md) | What to update and when, by role, with common mistakes |
| [FIELDS.md](../FIELDS.md) | The field shortlist, field by field: who fills each in, and when |
| [PHASE_GATES.md](../PHASE_GATES.md) | How to enter and exit each stage in Jira, and what is edited at each PI |
| [PROGRAMME_PLAN.md](../PROGRAMME_PLAN.md) | The communication kit and the six chunks in detail |
| [dashboards/DASHBOARD_BUILD_GUIDE.md](../dashboards/DASHBOARD_BUILD_GUIDE.md) | Click-by-click steps for the filters, dashboards and boards |
| [confluence/CONFLUENCE_PORTFOLIO_GUIDE.md](../confluence/CONFLUENCE_PORTFOLIO_GUIDE.md) | The Confluence page tree and the SQL for each page, with a playground that needs no Jira |
| [import/IMPORT_GUIDE.md](../import/IMPORT_GUIDE.md) and the workbook | Loading a spreadsheet of summaries into Jira as a joined hierarchy, with mock data |
| [charts/](charts/) and [charts.py](charts.py) | The figures in this paper as image files, and the script that draws them |

## Appendix E: Sources

Checked on 26 November 2026. Some vendor pages loaded only in part; the points that could not be confirmed are listed in section 17.

- [Configure custom hierarchy levels in Plans](https://support.atlassian.com/jira-software-cloud/docs/configure-custom-hierarchy-levels-in-advanced-roadmaps/) (Atlassian)
- [Epic Link replaced with Parent](https://support.atlassian.com/jira-software-cloud/docs/upcoming-changes-epic-link-replaced-with-parent/) (Atlassian)
- [Configuring the Parent Link field in Jira Data Center](https://confluence.atlassian.com/roadmaps-kb/how-to-properly-configure-the-parent-link-field-on-screens-in-jira-data-center-1295682320.html) (Atlassian)
- [Hierarchy search functions returning wrong results](https://support.atlassian.com/jira/kb/searching-for-child-or-parent-issues-using-jql-functions-report-wrong-results-in-jira/) (Atlassian)
- [Searching Plans fields in JQL](https://confluence.atlassian.com/jiraportfoliocloud/searching-for-portfolio-for-jira-custom-fields-in-jql-941619014.html) (Atlassian)
- [Plan and view cross-project work](https://support.atlassian.com/jira-software-cloud/docs/plan-and-view-cross-project-work-with-advanced-roadmaps/) (Atlassian)
- [Gadgets for Jira applications](https://confluence.atlassian.com/jirasoftwareserver0917/gadgets-for-jira-applications-1431245257.html) (Atlassian, Data Center)
- [Gadget limit on a dashboard](https://support.atlassian.com/jira/kb/modifying-gadget-limit-on-a-dashboard/) (Atlassian)
- [Best practices on using the Resolution field](https://support.atlassian.com/jira/kb/best-practices-on-using-the-resolution-field-in-jira-cloud/) (Atlassian)
- [Accelerating flow with SAFe](https://framework.scaledagile.com/accelerating-flow-with-safe) (Scaled Agile)
- [Milestones](https://v5.scaledagileframework.com/milestones/) (Scaled Agile)
