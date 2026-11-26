# Jira Framework for the Credit and Lending Value Stream

As of 26 November 2026. All names and figures in examples are placeholders.

One portfolio project holds every VS Epic, Feature, Milestone and Delivery RAID; each application keeps its own project for Epics and below; and fields you already have (sub value stream, Target PI, Actual PI, RAG Status) connect the two, so any initiative can be followed across applications.

## At a glance

```text
PORTFOLIO PROJECT (one for the value stream)
  VS Epic  (business outcome, 2 to 4 PIs)  ..... linked to many Milestones and many Delivery RAID tickets
    |-- Feature  (one sub value stream, one PI)  ..... linked to many Milestones and many Delivery RAID tickets
    |     |-- Epic in Credit Application project   (that application's share)
    |     |     `-- Stories, tasks, bugs, tests
    |     `-- Epic in Drawdowns project
    |           `-- Stories, tasks, bugs, tests
    `-- Feature
          `-- Epic in Facility Letter project
                `-- Stories, tasks, bugs, tests

Solid tree lines = parent (one parent, many children).   Dotted = links (many to many).
```

Solid lines are parent relationships: one VS Epic has many Features, one Feature has Epics in many applications, and each child has one parent. Dashed lines are links: a VS Epic or a Feature can have several Milestones and several Delivery RAID tickets, and one Milestone or RAID ticket can be linked to several of them. The highlighted Feature is delivered by two applications. Sub value stream and Target PI are fields on the Feature and on each Epic, and a release is a version in each application project.

## The set-up this framework assumes

The framework is written for Jira Data Center with Plans and for the field list in the bank's Jira standards page, as confirmed on 26 November 2026.

| Confirmed | What it means here |
| --- | --- |
| The hierarchy VS Epic > Feature > Epic > Story exists, and VS Epic and Feature sit in one project. | That project is the portfolio project. A Feature is the parent of Epics in application projects through Parent Link. |
| Each application has its own Jira project. | Application is read from the project. Component is free for modules. |
| Plans is available and you can create plans. | PI planning, dependencies, capacity and Feature progress run in one plan. |
| A PI is 12 weeks. | Five two-week sprints and one planning sprint. |
| Your fields already cover sub value stream, PI, status colour and prioritisation. | The framework uses them as they are: Value Stream and Sub-Value Stream, Target PI, Actual PI, RAG Status, Path to Green, Date to Green, Executive Summary, the four scoring fields, Enabler Type, Team. No labels or versions stand in for them. |
| Delivery RAID has RAID Type, Probability, Impact, ROAM Response, Dependency Type and a supplier sub value stream field. | RAID reporting uses those fields. |
| Almost every ticket has RAG Status, and Due date is the target date. | RAG and Due date drive the dashboards. |
| No ScriptRunner. Project automation is available. | No scripted queries. A few automation rules keep fields in step. |
| Confluence has Chart from Table and Table Transformer and can pull Jira data. | Trend and roll-up reports are built there. |

Checks to complete before this document is circulated (remove the list once done):

- [ ] Field names in this document match the standards page letter for letter. They were read from a photo of that page.
- [ ] All of those fields are live in today's Data Center projects. The standards page is titled for Jira Cloud.
- [ ] The allowed values of Enabler Type, RAG Status, RAID Type, ROAM Response and Severity, and the way PI values are written, are filled into the queries.
- [ ] Whether Value Stream and Sub-Value Stream is a two-step dropdown, and whether a dashboard gadget accepts it. If not, switch on the shadow label.
- [ ] The bank's own rule for when Actual PI is filled in, and whether Target PI may change. This document assumes "at Released" and "only by decision".
- [ ] Each query in the filter library run once on real data.
- [ ] The Jira version, to check the Parent Link column in Confluence and which plan features exist.
- [ ] Whether project admins may create automation rules.
- [ ] What the DDT records and which Jira field holds its reference.

## Structure: two layers, one join

The join between applications is the Feature. A Feature lives in the portfolio project and is the parent of one Epic in each application that must change to deliver it.

**Portfolio layer: one Jira project for the whole value stream.** Suggested name: Credit and Lending Portfolio. It holds only VS Epics, Features, Milestones and Delivery RAID. No team does sprint work here.

**Team layer: one Jira project per application.** Credit Application, Drawdowns, Facility Letter, Governance and Conditions, Watch and Worry Monitor, Problem Exposure Management, Forbearance and so on. Each holds Epics, Stories, Tasks, Bugs, Tests and Sub-tasks.

| Level | Issue type | Lives in | What it is | Size | Owner |
| --- | --- | --- | --- | --- | --- |
| 1 | VS Epic | Portfolio project | A business outcome for the value stream, usually crossing sub value streams. Example: "One view of conditions from approval to drawdown". | 2 to 4 PIs | Value stream lead |
| 2 | Feature | Portfolio project | A slice of a VS Epic that one sub value stream can deliver and show to users. May need several applications. | One PI; two only when planned that way and agreed at the portfolio sync | Sub value stream product lead |
| 3 | Epic | Application project | One application's share of a Feature. | 1 to 5 sprints | Application product owner |
| 4 | Story, Task, Bug, Test | Application project | A piece of work one team finishes in a sprint. | Under one sprint | Team |
| 5 | Sub-task | Application project | A step inside a story. Optional. | Days | Individual |
| Side | Milestone | Portfolio project | A date that matters: regulatory deadline, go-live, PI boundary. | A date | Delivery lead |
| Side | Delivery RAID | Portfolio project | A risk, assumption, issue or dependency that needs managing above team level. | Until closed | Delivery lead |

Five rules keep the structure honest:

1. Every Epic has a parent Feature. An Epic with no parent is invisible to the portfolio, shows on an exceptions dashboard, and is not planned into a PI.
2. Every Feature has a parent VS Epic. Upkeep goes under one standing Feature per sub value stream per year, "Run and improve". That Feature is the one exception to the sizing rules: it has no Target PI and no commitment label, is left out of predictability, and is closed at year end when a new one is opened.
3. A Feature belongs to exactly one sub value stream: the one accountable for the result. Its Epics may sit in any application, including one owned by another sub value stream. The product owner of that application accepts the Epic at PI planning by giving it a Target PI; until then it is a request, not a plan. Split a Feature in two only when each sub value stream would deliver something usable by itself.
4. A Feature is never split by application. The application split is the Epic's job.
5. Stories never sit in the portfolio project, and Features never sit in an application project.

Boards in the portfolio project: one Kanban board for the value stream showing VS Epics, and one Kanban board per sub value stream showing its Features. Each application team keeps its own Scrum or Kanban board.

**How the ticket types relate.** Parent relationships are strict, one parent only. Everything else is a link, and links can be many to many.

| From | To | How many | Recorded as |
| --- | --- | --- | --- |
| VS Epic | Feature | One VS Epic has many Features. A Feature has one VS Epic. | Parent Link on the Feature |
| Feature | Epic | One Feature has many Epics, often in different applications. An Epic has one Feature. | Parent Link on the Epic |
| Epic | Story, Task, Bug, Test | One Epic has many. Each has one Epic. | Epic Link |
| Story | Sub-task | One Story has many. Each has one Story. | Built-in parent |
| VS Epic | Milestone | Many to many. A VS Epic usually has several Milestones (design approved, first go-live, regulatory date, full rollout). One Milestone, such as a regulatory date, can serve several VS Epics. | blocks link, VS Epic blocks Milestone |
| Feature | Milestone | Many to many. A go-live Milestone waits for several Features. A Feature can serve two dates, for example a pilot and a full launch. | blocks link, Feature blocks Milestone |
| Delivery RAID | VS Epic, Feature, Milestone | Many to many. One risk can threaten several Features and a Milestone. One Feature can carry several risks. | relates to link |
| Feature | Feature | Many to many. | blocks link |
| Epic | Epic | Many to many, usually across applications. | blocks link |
| Feature | Sub value stream | Many Features to one sub value stream. | Value Stream and Sub-Value Stream field |
| VS Epic | Sub value stream | Many to many. | The field holds the lead sub value stream; the others are read from its Features |
| Feature | Program Increment | Many Features to one PI. | Target PI field |
| Epic, Story, Bug | Release | Many to one release. An Epic that ships in two stages is split into two Epics. | Fix Version in the application project |
| Feature | Application | Many to many. | Read from the child Epics' projects |

Two guards keep the many-to-many links readable. Link a Milestone at the highest level that is true: to the VS Epic if the whole outcome is due, to specific Features if only they are. And when one Feature seems to need two parents, it is two Features.

## Stitching next year's Epics up to the value stream

The starting point is what already exists: each application product owner has a list of Epics for next year. The first job is to join those lists upward, application to platform to value stream, without asking anyone to re-enter their demand.

Your example, as it would sit in Jira:

| Level | Ticket | Where | Named as |
| --- | --- | --- | --- |
| VS Epic | Avoid audit risk through access control | Portfolio project | An outcome: what gets better, for whom |
| Feature | M&P across the platform | Portfolio project | A capability, with no application name in it |
| Epic | M&P for Credit Application | Credit Application project | The capability plus the application |
| Epic | M&P for Drawdowns | Drawdowns project | The capability plus the application |

Steps, timed to finish before planning for the first PI of the year:

1. **List.** Each product owner makes sure every Epic they want next year exists in their application project, in status Idea or Analysis, with a one-line purpose, a rough size and the quarter they hope for. Nothing else is needed yet.
2. **Cluster.** Each sub value stream holds one working session with its product owners. Open the plan, show all those Epics, and group the ones that deliver the same capability in different applications. Each group becomes one Feature in the portfolio project, and the Epics get it as their Parent Link. In the plan this is a drag of the Epic under the Feature.
3. **Lift.** The value stream lead and product leads group the Features by the outcome they serve. Each group becomes a VS Epic. Features from different sub value streams can sit under one VS Epic; this is where the cross-stream picture first appears.
4. **Place the leftovers.** An Epic that shares a capability with nobody is still valid. If it delivers something users will notice, it gets a Feature of its own. If it is upkeep, it goes under one standing Feature per sub value stream, "Run and improve", under the standing VS Epic of the same name. Do not invent a grand parent to make a small Epic look strategic.
5. **Look down from the top.** For each Feature, ask which applications must change for it to work end to end. Where an application has no Epic for it, that is a gap: the product owner adds a placeholder Epic, or the Feature is honestly marked as partial. For each VS Epic, ask whether its Features really add up to the outcome.
6. **Spot clashes.** Two applications building the same thing differently, or two Epics that cannot both be done, show up once they sit under one Feature. Record each as a Delivery RAID issue or a blocks link.
7. **Check.** The stitching is finished when "VS: hygiene exceptions" returns nothing, every Feature has a parent VS Epic, and every VS Epic has a named owner.

What this produces is the candidate backlog for the year: every Epic reachable from a VS Epic. It is not yet a plan. Sequencing and Target PI come from PI planning.

## Roadmap, L0 plan and sizing

Planning happens at three levels, and each level has its own horizon, its own ticket type and its own view. The L0 plan is the year view of VS Epics; it is the roadmap.

| Level | Horizon | Grain | Dated by | Owner | View |
| --- | --- | --- | --- | --- | --- |
| L0 roadmap | 12 to 18 months | VS Epics, with Features as bars inside them, and Milestones | PI or quarter | Value stream lead | Plan view "L0 roadmap" |
| L1 PI plan | One PI, 12 weeks | Features and Epics | Sprint | Sub value stream product and delivery leads | Plan view "Current PI" |
| L2 sprint plan | Two weeks | Stories | Day | Team | Team board |

**Building the L0 plan.** It is a saved view of the same plan used for PI planning, so it never drifts from the detail beneath it.

1. After stitching, give every VS Epic and Feature a Start date and End Date at PI precision: the first day of the PI it should start in and the last day of the PI it should end in. Nothing finer.
2. In the plan, save a view named "L0 roadmap": hierarchy from VS Epic to Feature only, timeline set to quarters, grouped by sub value stream, coloured by RAG Status, with Milestones shown by their Due date.
3. Mark confidence by distance. The current PI is committed. The next PI is planned. Anything later is a forecast and is shown by quarter only. Say this on the page; a roadmap without it is read as a promise.
4. Review it at the fortnightly portfolio sync, and re-issue it after every PI planning.
5. Publish it where sponsors read: share the plan view on a Confluence page, with report 6 (Red and Amber) beneath it.

**Sizing a VS Epic in story points.** The size firms up in three stages, and the roadmap should say which stage a number is at.

| Stage | When | Source of the number | Accuracy |
| --- | --- | --- | --- |
| 1. Rough | Stitching, or DDT agreement | T-Shirt Size on each Feature, turned into points with one conversion table agreed for the value stream and calibrated from Features already finished | Within a factor of two |
| 2. Planned | Feature in Analysis | Story Points on each Epic, given by the team that will build it | Good enough to commit a PI |
| 3. Detailed | Epic in Implementing | Sum of Story Points on its stories | Good enough to forecast a date |

The plan adds these up: with estimates set to story points and roll-up switched on, each Feature shows the total of its Epics and each VS Epic the total of its Features, with the done share as a progress bar. Check once how your plan treats an Epic that has its own figure and estimated stories, so nothing is counted twice.

**Velocity above the team.** Four measures, from team to value stream. Story points mean different things in different teams, so the totals are for forecasting one group against its own past, never for ranking teams.

| Measure | What it is | Used for |
| --- | --- | --- |
| Team velocity | Story points finished per sprint, average of the last three | Team capacity in the plan |
| PI velocity, per application and per sub value stream | Story points finished in a PI by those teams | How much a sub value stream can take into the next PI |
| Planned against delivered | Story points with this Target PI at planning close, against points finished in the PI | Whether plans are realistic |
| Feature throughput | Features reaching Released per PI | The outcome view; harder to inflate than points |

**Forecasting a VS Epic.** For each application under it: remaining points divided by that team's PI velocity gives the PIs still needed. The VS Epic finishes when its slowest application does. That one line per VS Epic (total, done, remaining, PIs to go, limiting application) is Confluence report 7.

**Confluence reports for this section** (they continue the numbering of Reports in Confluence)

| # | Page | Built from | Shows |
| --- | --- | --- | --- |
| 7 | Size and forecast by VS Epic | Jira Issues macro on Epics under open VS Epics, with Parent Link, Project, Story Points and Status; a second macro on Features with their Parent Link. Table Transformer joins Epic to Feature to VS Epic and sums. | Per VS Epic: total, done and remaining points, PIs to go, and the application that limits it. |
| 8 | PI velocity | Jira Issues macro on stories and bugs resolved as Done between the PI's first and last day, with Project and Story Points. Table Transformer sums by project and by PI. Chart from Table as bars. | Points delivered per application and sub value stream, PI after PI. |
| 9 | Roadmap page | The shared "L0 roadmap" plan view; or, if sharing a plan view is not allowed, a Jira Issues macro on VS Epics with Start date, End Date and RAG Status drawn as a Gantt chart with Chart from Table. | The year on one page. |

## The connecting tags

Your existing fields carry every cross-application view. Each one has a single meaning and a named person who keeps it right; that is what makes the filters reliable.

| Question it answers | Field | On which tickets | Rule |
| --- | --- | --- | --- |
| Which sub value stream? | Value Stream and Sub-Value Stream | VS Epic, Feature, Epic, Milestone, Delivery RAID, Bug, Test | Required from Analysis onward. An Epic takes the value of its parent Feature, even when the Epic sits in another sub value stream's application. That is how a Feature's work is found across applications. |
| Which application? | Project | Epic and below | The project itself. For a Feature, read it from the child Epics. |
| Which module? | Component | Epic and below | One component per module: Facility, Collateral, Certification, Approval. |
| Which PI was it planned for? | Target PI | Feature, Epic | Set at PI planning. Not changed afterwards for committed work, so the record of the promise survives. |
| Which PI did it finish in? | Actual PI | Feature, Epic | Set when the ticket reaches Released. |
| Which production release? | Fix versions | Epic, Story, Bug | One version per release in each application project, named `<APP> 2027.03`. |
| Which team? | Team | Epic, Story, Task, Bug | The shared team from Plans. |
| What kind of work? | Enabler Type, with Regulatory or Control Change Type | Feature | Set at triage. Drives the investment mix. |
| How is it going? | RAG Status, Path to Green, Date to Green, Executive Summary | VS Epic, Feature, Epic, Milestone, Delivery RAID | Reviewed weekly by the owner. See the RAG rules below. |
| What comes first? | The four scoring fields and Weighted Shortest Job First Score, then Rank | VS Epic, Feature | Scored in Analysis. See Intake and design. |
| When is it due? | Due date; Start date and End Date for the plan | All | Due date is the target date people outside the team are told. |

**RAG rules.** One meaning for each colour, at every level:

- **Green:** on track for its Due date. No help needed.
- **Amber:** the Due date is at risk and the owner has a recovery plan. Path to Green and Date to Green must be filled in.
- **Red:** the Due date will be missed unless someone outside the team decides or acts. Path to Green says what is needed and from whom. On a Feature, also set Management Attention.

A parent is never greener than the facts beneath it: a Feature with a Red Epic is at least Amber. RAG is a judgement by the owner, not a calculation, and it is refreshed at the weekly sync. A RAG nobody has touched for two weeks is treated as unknown.

Four small groups of labels remain, because no field covers them. Nobody invents others.

| Label | Used on | Meaning | Set by |
| --- | --- | --- | --- |
| `pi-committed` or `pi-stretch` | Feature, and each of its Epics | Firm commitment for the Target PI, or a stretch goal. An Epic is committed when its own product owner says so at PI planning. A Feature is committed only when all of its Epics are. | Product owner on the Epic, product lead on the Feature, at PI planning only |
| `unplanned` | Feature, Epic | Entered a PI after planning closed, by decision. | Delivery lead |
| `pi-descoped` | Feature, Epic | Taken out of a PI after planning closed, by decision. The reason goes in Change Reason on a Feature, or in a comment on an Epic. | Delivery lead |
| `ms-regulatory`, `ms-golive`, `ms-pi`, `ms-external` | Milestone | The kind of Milestone. | Delivery lead |

**Rank** (the drag order on a board) settles sequence between tickets with similar scores. The top of the board is done first.

Issue links, three types only:

- **blocks / is blocked by**: a real dependency between two Features or two Epics. This is the main way to record a dependency.
- **relates to**: ties a Delivery RAID ticket or a Milestone to the work it concerns.
- **duplicates**: used at intake to close repeat requests.

## Field shortlist per issue type

Each issue type offers between 18 and 60 fields; the framework reads only the ones below. Core fields are always filled in. The others are filled in only when the situation applies. Any field not listed is left as the bank's standards require and is read by no filter, dashboard or report here.

| Issue type | Core fields | Filled in only when it applies | Set by Jira or automation |
| --- | --- | --- | --- |
| VS Epic (16 core) | Summary, Description, Assignee, Value Stream and Sub-Value Stream, Objective ID, Business Benefits, the four scores, Start date, End Date, Due date, RAG Status, Executive Summary, Linked work items | Path to Green, Date to Green, Financial Benefit (USD), Regulatory or Control ID, Change Reason, Flagged | Weighted Shortest Job First Score |
| Feature (17 core) | Summary, Description, Assignee, Parent Link, Value Stream and Sub-Value Stream, Enabler Type, Acceptance Criteria, Business Benefits, T-Shirt Size, the four scores, Target PI, Labels, Due date, RAG Status | Start date, End Date, Path to Green, Date to Green, Management Attention, Executive Summary, Regulatory or Control Change Type, Regulatory or Control ID, Architectural Governance, Contains Resiliency Work, Change Reason, Linked work items, Flagged | Actual PI, Weighted Shortest Job First Score |
| Epic (14 core) | Summary, Epic Name, Description, Assignee, Parent Link, Components, Team, Story Points, Target PI, Labels, End Date, RAG Status, Fix versions, Linked work items | Start date, Change Request ID, Regulatory or Control Change Type, Flagged | Actual PI, Value Stream and Sub-Value Stream |
| Story (8 core) | Summary, Description, Epic Link, Acceptance Criteria, Story Points, Assignee, Sprint, Components | Fix versions, Story Type, Flagged | Status, Resolution |
| Task (6 core) | Summary, Description, Epic Link, Assignee, Sprint, Story Points | Acceptance Criteria, Flagged | Status, Resolution |
| Sub-task (3 core) | Summary, Assignee, Parent | Flagged | Status |
| Bug (11 core) | Summary, Description, Epic Link, Severity, Priority, Testing Phase, Environment, Affects versions, Assignee, Sprint, Components | Fix versions, Root cause category, Root cause analysis, Flagged | Status, Resolution |
| Test (7 core) | Summary, Description, Epic Link, Testing Phase, Environments, Assignee, Sprint | Fix versions | Status, Resolution |
| Milestone (9 core) | Summary, Description, Assignee, Value Stream and Sub-Value Stream, Due date, Baseline End Date, RAG Status, Labels, Linked work items | Path to Green, Date to Green, Executive Summary, Regulatory or Control ID, Fix versions |  |
| Delivery RAID (9 core) | Summary, Description, RAID Type, Assignee, Value Stream and Sub-Value Stream, RAG Status, Due date, Impact, Linked work items | Risk: Probability, Risk Trigger Event, ROAM Response. Dependency: Dependency Type, Supplier Value Stream and Sub Value Stream, Baseline End Date. Issue: Impact Details, Path to Green, Date to Green. Any: Executive Summary |  |

Who fills in each field, and when, is set out field by field in [FIELDS.md](FIELDS.md).

**A gap on Epic.** From the standards page, Epic does not appear to carry Path to Green, Date to Green or Due date. Until that is confirmed or the fields are added, an Epic's expected go-live date is its End Date, and the recovery plan for an Amber or Red Epic is a comment starting "Path to green:". Filters that test Path to Green therefore apply to Features, VS Epics, Milestones and Delivery RAID, not to Epics.

Two rules keep the list short. A field joins it only when a filter, dashboard, report or decision reads it. And when one is added, another is reviewed for removal.

## Workflows and gates

Your existing statuses are enough. What is missing today is a shared meaning for each one and a rule for entering it. The tables give both.

**VS Epic**

| Status | Meaning | To enter it |
| --- | --- | --- |
| Idea | Someone has raised it. No commitment. | Summary, sponsor and the problem in two sentences. |
| Review | The portfolio sync is deciding whether it is worth analysing. | Triage owner assigned. |
| Analysis | A named lead is shaping it: outcome, measure of success, sub value streams involved, rough size. | Accepted at the portfolio sync. |
| Ready | Approved to start. Split into Features for at least the next PI. | Outcome and success measure written, first Features created, sponsor sign-off. |
| Implementing | At least one Feature is being built. | First child Feature moves to Implementing. |
| Released | Every planned Feature is live in production. | All child Features Released or Done. |
| Done | The outcome has been checked against the success measure. | Benefit review recorded in a comment. |

**Feature**

| Status | Meaning | To enter it |
| --- | --- | --- |
| Idea | Raised, not yet triaged. | Intake template filled in. |
| Analysis | Product lead is writing acceptance criteria, naming the applications and agreeing the design. | Parent VS Epic, Value Stream and Sub-Value Stream, and Enabler Type set. |
| Ready | Can be pulled into a PI. | Definition of ready met (see Intake and design). |
| Implementing | At least one child Epic is in progress. | Target PI set, committed or stretch label set, RAG Status set. |
| Testing | All child Epics are built. End-to-end testing across applications is running. | Every story in every child Epic is Done and deployed to the test environment. The Epics stay at Implementing until go-live. |
| Validation | Business users are confirming it does what was asked. | End-to-end test passed, no open severity 1 or 2 bugs. |
| Released | Live in production. | Business sign-off recorded, change record linked, and every child Epic is Released, Done or closed as Won't Do. Actual PI is then filled in by automation. |
| Done | Early-life support closed. No further work expected. | Two weeks live with no open critical bugs, or as your support policy states. |

**Epic**

| Status | Meaning | To enter it |
| --- | --- | --- |
| Idea | Placeholder created during Feature analysis. | Parent Feature set. |
| Analysis | Team is breaking it into stories and estimating. | Product owner assigned. |
| Ready | Stories for the first two sprints are written and estimated. | Estimate recorded, dependencies linked. |
| Implementing | Stories are being built or tested, or are finished and waiting for go-live. | Sprint work started. |
| Released | Live in production. | Fix version set and released, Change Request ID set. Actual PI is then filled in by automation. |
| Done | Nothing left, including clean-up. | All child issues closed. |

**Story, Task, Bug, Test, Delivery RAID, Milestone**: Backlog, In Progress, Done.

| Type | Backlog means | In Progress means | Done means |
| --- | --- | --- | --- |
| Story, Task, Bug, Test | Not started | Being worked on in a sprint | Meets the team's definition of done |
| Delivery RAID | Raised, owner not yet acting | Owner is actively managing it | Closed: mitigated, accepted, resolved or no longer relevant, stated in the closing comment |
| Milestone | Date agreed, more than one PI away or not started | Work towards it is under way | Date met, with the actual date in a comment |

Four conventions that avoid new statuses:

- **Blocked** is the Jira flag, not a status. A flagged card turns yellow on the board and can be filtered.
- **Cancelled** is a resolution, not a status. Move the ticket to Done with resolution "Won't Do". Dashboards count only resolution "Done" as delivered.
- **On hold** is a move back to Ready with a comment.
- **Team board columns** can be finer than statuses only if the admin adds statuses. If stories need a review or test step, ask for one extra status, "In Review".

## Delivery RAID and Milestones

Both live only in the portfolio project and are always linked to the work they affect, so they appear on that Feature or VS Epic and on every dashboard above it.

**Delivery RAID.** One ticket per risk, assumption, issue or dependency that a team cannot settle alone.

| RAID Type | Raise it when | Fields that must be filled | Closes when |
| --- | --- | --- | --- |
| Risk | Something may go wrong and would move a Feature date or a Milestone. | Probability, Impact, Impact Details, Risk Trigger Event, ROAM Response, Due date as the next review date. | The ROAM Response is Resolved or Accepted, or the event has passed. |
| Assumption | A plan depends on something not yet confirmed. | Description of the assumption, who can confirm it, Due date as the confirm-by date. | Confirmed, or converted to a risk or issue. |
| Issue | Something has gone wrong and needs help from outside the team. | Impact, Impact Details, Path to Green, Date to Green, RAG Status. | Resolved. |
| Dependency | Work is needed from another sub value stream, another value stream, or a party outside Jira. | Dependency Type, Supplier Value Stream and Sub Value Stream, Due date as the need-by date, Baseline End Date as the date first agreed. | Delivered and accepted by the receiver. |

Rules for RAID:

- A dependency between two teams inside one sub value stream is a **blocks** link between their Epics. It needs a Delivery RAID ticket when it crosses sub value streams, involves an outside party, or is at risk.
- On a dependency, Value Stream and Sub-Value Stream is the receiver and Supplier Value Stream and Sub Value Stream is the giver. Each side then sees it on its own dashboard: one as "what we are waiting for", the other as "what we owe".
- ROAM Response on a risk means: Resolved (no longer a risk), Owned (a named person is acting), Accepted (the sponsor has agreed to live with it), Mitigated (action taken, impact reduced). A risk with no ROAM Response has not been reviewed.
- Every Delivery RAID ticket has an assignee, a Due date, a RAG Status, and a **relates to** link to at least one Feature, VS Epic or Milestone.
- Red and Amber tickets are reviewed at the fortnightly portfolio sync, the rest monthly.

**Milestone.** One ticket per date that people outside the teams care about.

| Kind | Example | Label |
| --- | --- | --- |
| Regulatory or audit date | Remediation of an audit finding due | `ms-regulatory` |
| Go-live | Forbearance module live for a business line | `ms-golive` |
| PI boundary | PI planning, PI end demo | `ms-pi` |
| External commitment | Data feed from another division available | `ms-external` |

Rules for Milestones:

- Baseline End Date is the date first committed and is never changed. Due date is the current target. The gap between them is the slippage, shown in the Confluence milestone report.
- When Due date moves, say why in a comment and update Path to Green and Date to Green.
- Link every Feature or VS Epic that must finish for the date using **blocks** (the Feature blocks the Milestone). The Milestone then lists everything it is waiting for.
- RAG Status on a Milestone follows the RAG rules. It is Amber or Red when a linked Feature is Red, or a linked risk is open with high Probability and Impact.
- Regulatory Milestones carry the Regulatory or Control ID.

## Managing the portfolio at VS Epic level

A large portfolio goes wrong in a few predictable ways: too much is started, nobody wrote down what an outcome was meant to achieve, and reports describe activity. Six practices at VS Epic level address those, using fields the VS Epic already has.

| Practice | What it is | How it runs here |
| --- | --- | --- |
| A stated outcome and case on every VS Epic | Before analysis is approved, the VS Epic says what will improve, by how much, at what rough cost and with what risk. | Business Benefits, Financial Benefit (USD), Customer Impact, Regulatory Impact and Operational Resilience Impact on the VS Epic, plus a one-page case in Confluence linked from it. Required to leave Analysis. |
| A limit on work in progress | A cap on how many VS Epics may be in Analysis and in Implementing at once. New work waits until something finishes. | Column limits on the VS Epic board. Start with the number of people able to lead an analysis, and the number of VS Epics the teams can truly carry in parallel; both are usually single digits. Breaches are discussed at every portfolio sync. |
| A link to strategy | Every VS Epic names the objective it serves. One that serves none is questioned. | Objective ID on the VS Epic, with the list of objectives and their owners on a Confluence page. |
| Investment mix | The share of capacity going to each objective, and to business, enabler, regulatory and run work, against the intended share. | Confluence portfolio page 5: story points by objective and by Enabler Type. |
| Benefits review | Three and six months after release, a named owner measures the promised benefit and records the result. | A VS Epic stays at Released until the review is recorded, then moves to Done. Due date on a `ms-external` Milestone carries the review date. |
| A rule for stopping | Agreed grounds for stopping a VS Epic: the case no longer holds, or cost has outrun benefit. | Decided at the portfolio sync; closed with resolution Won't Do and the reason in Change Reason. |

**VS Epic statuses as a portfolio pipeline**

| Status | Purpose | To leave it | Limit |
| --- | --- | --- | --- |
| Idea | Anything may be raised | Outcome stated in one or two sentences | None |
| Review | Decide whether it deserves analysis | Objective ID set, a named lead | About the number of leads |
| Analysis | Build the case and split into Features | Case linked, benefit and scores filled in, first Features created | The number of leads available |
| Ready | Approved, waiting for capacity | Capacity confirmed at PI planning, Features have Target PI | Small, so the queue does not go stale |
| Implementing | Features are being delivered | All planned Features Released | What the teams can carry in parallel |
| Released | Delivered, benefit not yet measured | Benefits review recorded | None |
| Done | Outcome measured |  |  |

**Twelve questions the value stream lead answers every month.** The portfolio pages in Confluence are built to answer exactly these and nothing more.

| # | Question | Answered from |
| --- | --- | --- |
| 1 | Which VS Epics are in progress, and are we inside the limit? | Jira: VS Epic board |
| 2 | Which VS Epics are Red or Amber, and what is the path to green? | Jira: dashboard 1 |
| 3 | Which Features under each VS Epic are late or spilled? | Confluence: portfolio tree |
| 4 | How far is each VS Epic, in Features and in story points? | Confluence: portfolio tree and forecast |
| 5 | Did we deliver what we committed last PI? | Confluence: PI scorecard |
| 6 | What is stuck, and for how long? | Jira: Analysis over 30 days, spillover |
| 7 | Where is capacity going, by objective and by kind of work? | Confluence: investment mix |
| 8 | Is demand for the next PI above capacity? | The plan: capacity view |
| 9 | Which dependencies across applications are open or overdue? | Jira: open blockers, cross-stream dependencies |
| 10 | Which risks and issues need a decision? | Jira: dashboard 4 |
| 11 | Which dates have moved? | Confluence: milestone slippage |
| 12 | Which released VS Epics are due a benefits review, and what did past reviews show? | Jira: VS Epics at Released; Confluence table of results |

## Governance and working agreements

A shared Jira model fails less often from wrong fields than from unclear decisions. This section says who decides, what "done" means, how bank controls are evidenced, and what happens when the rules are not followed.

**Who decides**

| Decision | Decided by | Where | Escalates to |
| --- | --- | --- | --- |
| Whether new demand is taken on | Owner of the DDT decision | DDT | Value stream lead |
| Order of VS Epics | Value stream lead | Portfolio sync | Sponsor |
| Order of Features in a sub value stream | Product lead, from the scores | Scoring session | Value stream lead |
| Whether an application takes an Epic into a PI | That application's product owner | PI planning | Product lead of the Feature |
| Two sub value streams want one team | Value stream lead | Portfolio sync | Sponsor |
| A fixed regulatory date against a higher-scored Feature | The date wins; value stream lead confirms what gives way | Portfolio sync | Sponsor |
| Scope in or out after the PI lock | Product lead and delivery lead together; value stream lead if cross-stream | Weekly sync | Portfolio sync |
| Carry on, stop or split a spillover | Product lead and delivery lead | PI review | Value stream lead |
| Go or no-go for a release | Per your bank's change process; delivery lead records it | Release readiness review | Change authority |
| A change to this framework, a field, a status or a label | Framework owner | Monthly, with a change log on Confluence | Value stream lead |

Name one framework owner. Without one, each team adjusts the model and the cross-application views stop working within a year.

**Capacity split.** Before each PI, every team reserves capacity by kind of work, so that urgent items cannot crowd out the rest. A starting split to adjust from your own history after two PIs:

| Kind of work | Starting share | Counted from |
| --- | --- | --- |
| Committed Features, business | 50% | Epics whose Feature has no Enabler Type |
| Enablers, resilience and technical debt | 15% | Enabler Type; Contains Resiliency Work |
| Regulatory and control change | By demand, planned first | Regulatory or Control Change Type |
| Run work, production defects and incidents | 20% | Bugs, and Epics under "Run and improve" |
| Unplanned reserve | 15% | Tickets labelled `unplanned` |

The shares are a proposal, not a finding. Record each team's agreed split on the PI scorecard and compare it with what was actually done at the PI review.

**Definition of done**

| Level | Done means |
| --- | --- |
| Story | Acceptance criteria met, code reviewed, automated tests pass, tested in the team environment, no open severity 1 or 2 defect. |
| Epic (to Released) | All stories Done; integration and regression tests passed; non-functional needs met (performance, security, access control, resilience) or a waiver recorded; Fix version and Change Request ID set; support notes handed over. |
| Feature (to Released) | Every Epic Released; end-to-end test across applications passed; business acceptance recorded; required sign-offs closed; no open severity 1 or 2 defect. |
| Feature (to Done) | Early-life support closed; Business Benefits reviewed against what was expected. |
| VS Epic (to Done) | Outcome measured against its success measure and recorded. |

**Sign-offs and audit evidence.** A comment can be edited and is weak evidence. Record each required approval as a Task or Sub-task on the Feature, named for the approval (architecture, risk, control, business acceptance), assigned to the approver and closed by the approver. Jira's history then shows who approved and when, and the person who built the change is not the person who closed the approval. Use the fields you already have for the references: Architectural Governance, Risk Impact Assessment ID, Regulatory or Control ID, Change Request ID. Where your bank's system of record for an approval is another tool, the Task holds the reference and that tool holds the evidence.

**Regulatory and control work.** A Feature with a regulatory driver carries Regulatory or Control Change Type and Regulatory or Control ID, and is tied to a Milestone labelled `ms-regulatory` with the fixed date. It is planned before scored work, appears on its own dashboard list, and is never labelled stretch.

**Defects, testing and incidents**

- A defect found in any test phase is a Bug under the Epic it belongs to, with Severity, Testing Phase and Environment filled in. One severity scale is used everywhere; "priority" is not used to mean severity.
- A Feature cannot leave Validation with an open severity 1 or 2 Bug under any of its Epics.
- A defect found in production is a Bug in the application project, with the incident reference, under the Epic that introduced it if known, otherwise under "Run and improve". Root cause category is filled in at closure.
- Bugs found in production against a Feature released in the last PI are counted as escaped defects on the PI scorecard.

**Risk acceptance and sensitive tickets.** A risk with ROAM Response Accepted is not closed. It stays open with the name of the person who accepted it and a Due date for the next review, so accepted risk remains visible. Tickets that should not be seen by the whole value stream group use the Security Level field.

**PI objectives.** Each sub value stream writes three to six objectives for the PI in business language on the PI scorecard, each marked committed or uncommitted and tied to its Features. The sponsor gives each a planned value at planning and an achieved value at the PI review. This sits beside the predictability count and is harder to inflate, because someone outside the team does the scoring.

**Improvement items.** Each PI review ends with no more than five improvement actions. Each is a Task in the portfolio project labelled `improvement`, with an owner and a Due date, and is reviewed at the portfolio sync until closed.

**Bringing in a new application or team**

- [ ] Application project uses the standard issue types, workflows and screens, with Parent Link, Target PI, Actual PI, RAG Status and the sub value stream field visible on Epic.
- [ ] Board created; shared team created in Plans and tied to the board; sprints named to the convention.
- [ ] Project and board added to the plan and to the project lists in the base filters, hygiene filters and automation rule 1.
- [ ] Existing open Epics given a parent Feature.
- [ ] Team filter set and team dashboard copied from the template.
- [ ] Product owner walked through this document; first sync attended.

**When the rules are not followed.** The value stream dashboard shows a hygiene count per application every month: Epics without a parent, tickets without a sub value stream, Amber or Red without a plan, releases without Actual PI. The order of escalation is product owner, then product lead, then value stream lead. Two rules have teeth: an Epic without a parent Feature is not planned into a PI, and a Feature that fails the definition of ready is not committed.

**Five failure patterns to watch for**

- Everything is Green until the week it turns Red. Countermeasure: the RAG rules, and asking for the evidence behind a Green at the weekly sync.
- Epics that stay open for a year. Countermeasure: the size limits, and closing or splitting anything older than four PIs.
- New fields, statuses and labels added team by team. Countermeasure: the framework owner and the change log.
- Dashboards that count activity. Countermeasure: lead with Features released, objectives achieved and Milestones met; keep story points for planning.
- A tool rollout with no coaching. Countermeasure: the pilot, and a named person each team can ask.

## Operating rhythm

Seven recurring meetings run the framework, and each one is held on a named Jira board or dashboard so that the ticket is updated in the room, not afterwards.

| Meeting | How often | Who | Held on | What changes in Jira |
| --- | --- | --- | --- | --- |
| Team daily and sprint events | Daily, per sprint | Application team | Team board | Stories move; blockers flagged. |
| Backlog refinement | Weekly | Product owner, team | Team backlog | Epics move Analysis to Ready; stories estimated. |
| Backlog triage | Weekly, 30 minutes | Sub value stream product lead, delivery lead | Sub value stream Feature board, Idea column | New Features accepted into Analysis, merged as duplicates, or closed as Won't Do. |
| Sub value stream sync | Weekly | Product lead, delivery lead, product owners of its applications | Sub value stream dashboard | Feature status checked against child Epics; RAG Status, Path to Green and Date to Green refreshed; flags and blocks links reviewed. |
| Portfolio sync | Fortnightly | Value stream lead, all product and delivery leads | Value stream VS Epic board and dashboard | VS Epics move through Review, Analysis, Ready; Red and Amber RAID reviewed; Milestone dates confirmed. |
| RAID review | Monthly, or inside the portfolio sync | Delivery leads | RAID dashboard | Every open RAID ticket gets a comment and a new review date, or is closed. |
| PI planning and PI review | Every 12 weeks | Everyone | PI plan, or the Feature boards | Target PI set for the next PI; the closing PI scored on its scorecard. |

A 12-week PI calendar, counted in weeks from the start of the PI:

| Week | Event |
| --- | --- |
| 1 to 10 | Sprints 1 to 5. |
| 7 | Features for the next PI must be in Analysis. Intake for the next PI closes. |
| 9 | Features for the next PI must be Ready. Draft Target PI set by product leads. |
| 10 | Capacity confirmed by each team. Draft dependencies linked. |
| 11 | PI review and demo of the closing PI. Predictability scored. |
| 11 to 12 | PI planning for the next PI, then the planning and improvement sprint. |

Who keeps what up to date:

| Role | Keeps current |
| --- | --- |
| Value stream lead | VS Epic status, RAG Status, Executive Summary, rank order of VS Epics. |
| Sub value stream product lead | Feature status, RAG Status, scores, rank, Target PI, Enabler Type, Acceptance Criteria. |
| Delivery lead | Delivery RAID, Milestones, blocks links, release versions and dates. |
| Application product owner | Epic status, RAG Status, Parent Link, Target PI, Fix version, story backlog. |
| Team | Stories, bugs, flags, estimates. |

## Intake and design

New demand has one front door, the DDT, and the DDT is used for nothing else. Next year's existing Epic lists do not go through it; they are stitched as described above. Delivery is never tracked in the DDT.

|  | In the DDT | In Jira |
| --- | --- | --- |
| What it holds | Demand that is not yet in anyone's backlog | Everything agreed, and everything being delivered |
| What is decided there | Whether to do it, the rough timeline, the proposed PI | Scope detail, the application split, the commitment, progress |
| What comes out | An agreed demand with a proposed PI | A Feature (or VS Epic) carrying the DDT reference, then its Epics |
| Who looks at it | Requesters, product leads, the value stream lead | Teams, product owners, delivery leads, sponsors |

The Idea status in Jira is therefore not a second front door. Only two things arrive there: candidate Features created during stitching, and demand already agreed in the DDT. A "no" to new demand is given in the DDT, by whoever owns the DDT decision. In Jira, the product lead decides only when an agreed item is shaped, and may close a stitched candidate as a duplicate or Won't Do. A proposed PI from the DDT is a proposal: it becomes Target PI only at PI planning.

1. **Hand over from the DDT.** When a demand is agreed, the product lead creates the Feature in the portfolio project in status Idea, with the DDT reference, the sponsor, the problem and outcome in the description, any hard date and its source, and the applications likely to change. The DDT entry is then closed.
2. **Triage, weekly.** The product lead sets Value Stream and Sub-Value Stream, Enabler Type and the parent VS Epic, and moves the Feature to Analysis when there is capacity to shape it. Items that have waited more than a week are discussed, not ignored.
3. **Analyse and design.** The product lead owns the Feature through Analysis. The outputs are:
   - Acceptance Criteria and Business Benefits filled in.
   - A design or solution page in Confluence, linked on the Feature, with the sign-offs described under Governance.
   - One placeholder Epic in each application that must change, with the Feature as parent. This is the moment the cross-application picture becomes visible.
   - Story Points on each Epic as a planning estimate, given by the team that will build it.
   - blocks links between Epics that must be done in order, and a Delivery RAID ticket for anything needed from another sub value stream or from outside.
4. **Score and rank.** The four scores are filled in at the scoring session, and the product lead places the Feature on the sub value stream board. The order of the Ready column is the proposal for the next PI.

**Definition of ready for a Feature.** It moves to Ready only when all of these are true:

- [ ] Parent VS Epic, Value Stream and Sub-Value Stream, and Enabler Type are set.
- [ ] Acceptance Criteria and Business Benefits are filled in and agreed with the sponsor. T-Shirt Size and the four scores are filled in. A regulatory Feature with a fixed date needs its Milestone and Regulatory or Control ID instead of scores.
- [ ] Every application that must change has a child Epic, and each Epic has a rough size.
- [ ] Design is linked, with any architecture, risk or control approvals your bank requires.
- [ ] Dependencies are linked, and outside dependencies have a RAID ticket with an owner.
- [ ] It fits in one PI, or it is an agreed two-PI Feature. Otherwise split it.

**Prioritising.** Your Features and VS Epics already carry the four scores of weighted shortest job first: User/Business Value Score, Time Criticality Score, Risk Reduction / Opportunity Enablement Score and Job Size Score. The first three are added and divided by job size to give the Weighted Shortest Job First Score; a higher score goes first. Two rules make the scores comparable: each sub value stream scores its Features together in one session against each other, not one at a time, and scores use the same short scale (1, 2, 3, 5, 8, 13, 20). Regulatory work with a fixed date is not argued through the score: it gets a Milestone, and the date decides.

**Unplanned work.** An urgent request after PI planning has closed still comes through the DDT. It enters the PI only by a decision of the sub value stream product lead and delivery lead together, or of the value stream lead if it touches more than one sub value stream. The decision names what moves out. The delivery lead then sets Target PI and the `unplanned` label on what comes in, and the `pi-descoped` label on what goes out. Production incidents stay in the incident tool; the fix becomes a Bug carrying the incident reference, and counts against the team's reserve for run work.

## PI planning in Jira

Planning a PI means deciding which Ready Features, and which of their Epics, get that PI in the Target PI field. The plan is whatever carries the value when planning closes, and Actual PI later records what really happened.

**Before (weeks 7 to 10 of the current PI)**

1. The delivery lead checks the next PI exists as a value of Target PI, and creates a `ms-pi` Milestone for the planning day.
2. Each team creates its five sprints, named `PI27.2 S1 <team>` to `S5`, with dates.
3. Product leads set Target PI on the Ready Features they propose, highest Weighted Shortest Job First Score first. This is the draft.
4. Each team states its capacity for the PI in story points, from its average of the last three sprints less known leave. Enter it as the team's capacity in the plan.
5. The delivery lead opens the dependencies view of the plan and checks that every blocks link has both ends scheduled, with the blocker first. Cross-stream dependencies each have a Delivery RAID ticket naming the supplier.

**During (two days)**

1. Product leads present the draft Features from the plan view filtered to the Target PI.
2. Each team sets Target PI on the Epics it can take and drags their stories into sprints S1 to S5 until capacity is reached. Epics that do not fit are said so aloud.
3. For each Feature, the product lead checks in the plan that every child Epic, in every application, has the Target PI. If one application cannot fit its share, the Feature is cut down, marked `pi-stretch`, or moved out by clearing its Target PI.
4. New dependencies found in the room are linked on the spot with blocks. Anything unresolved becomes a Delivery RAID ticket with an owner before the day ends.
5. Each Epic that stays, and then each Feature, gets `pi-committed` or `pi-stretch`, a Due date, and RAG Status Green. Each sub value stream writes its PI objectives on the PI scorecard page in Confluence.
6. Confidence vote. Record the result as a comment on the `ms-pi` Milestone.

**After (within three working days)**

1. **Lock.** The delivery lead announces that planning is closed. On that day the committed and stretch Features and Epics are pasted as a plain table into the PI scorecard page: Key, Summary, Sub value stream, Application, Committed or Stretch, Story Points, Due date. That table is the baseline. It is the only list predictability is counted from, and nobody edits it afterwards.
2. **Changes after the lock** need a decision (see Unplanned work). Work that comes in gets `unplanned`; work that goes out gets `pi-descoped`. Nothing else changes Target PI or the commitment labels during the PI.
3. **Switch the filters.** The delivery lead creates the two per-PI filters and repoints the current-PI filters (see the filter library). Every dashboard follows.

**At PI end**

1. **Score against the baseline.** A PI runs its full 12 weeks, planning sprint included. For every committed line in the baseline table, the scorecard shows one of four results: delivered (Actual PI equals Target PI), spilled (not Released by the last day), descoped by decision, or stopped.
2. **Report three figures side by side**, per sub value stream and per application: committed Features delivered out of committed Features; committed Epics delivered out of committed Epics; and the same weighted by Story Points. Stretch and unplanned results are listed under them, not hidden. Treat 80% as a healthy level to learn from, not a target to hit; a figure that sits at 100% usually means too little was committed.
3. **Decide each spillover** at the PI review (see Delivery control).
4. **Re-plan stretch and unplanned leftovers:** Target PI moves to the next PI, or is cleared and the ticket returns to Ready.
5. The predictability trend report in Confluence is updated from the scorecard.

**The plan in Plans.** One plan for the value stream is where the steps above are carried out. Set it up once:

- **Sources:** the portfolio project and the board of every application team.
- **Hierarchy:** VS Epic down to Sub-task. Features show their Epics from every application beneath them, with a progress bar that rolls up from stories.
- **Fields shown as columns:** Target PI, Actual PI, RAG Status, Team, Due date, Weighted Shortest Job First Score. Plans accepts single-choice dropdowns, numbers, dates and labels as columns, but not two-step dropdowns, so the sub value stream appears in the plan through its shadow label. The admin adds custom fields to the plan.
- **Dates:** Start date and End Date schedule the bars. Due date stays the promise made outside the team.
- **Teams:** one shared team per application team, tied to its board, with two-week sprints and capacity from recent velocity. Capacity is per team, not per person.
- **Releases:** the release versions from the application projects. A cross-project release groups same-named versions for viewing.
- **Dependencies:** blocks links appear as lines on the timeline and, where your version has it, in the dependencies report. A link whose dates conflict is marked.
- **Saved views:** one per sub value stream, one for the current Target PI, one showing dependencies only, one grouped by team for capacity, and one showing only Amber and Red.

One habit to teach: changes made in a plan stay in the plan until someone presses Review changes and saves them to Jira. During PI planning, name one person per sub value stream who saves, and save at each break.

A wall-style program board, with teams down the side and sprints across, still needs an add-on such as Easy Agile Programs or BigPicture. The timeline grouped by team is the nearest standard view.

## Delivery control: blockers, the PI plan, spillover and partial delivery

Four questions matter most in delivery, and each has one field, link or label that answers it. Commitment is made twice: each product owner commits the Epic for their application, and the product lead commits the Feature once all of its Epics are committed. Both are measured, so one late application is visible without blaming the others.

| Question | Answered by | Seen in |
| --- | --- | --- |
| What blocks what? | blocks links between Epics and between Features; Delivery RAID dependencies across sub value streams | The plan's dependencies view; "VS: open blockers" |
| What is in the PI plan? | Target PI on the Epic and on the Feature | The plan filtered to the PI; "VS: PI Epics" |
| What spilled over? | Target PI is an earlier PI and the ticket is not finished | "VS: spillover" |
| What was delivered late or in part? | Actual PI compared with Target PI, Epic by Epic | Confluence report 3 and the PI scorecard |

**What blocks what**

- The ticket that must finish first **blocks** the other. Link Epic to Epic when two applications depend on each other, Feature to Feature when two capabilities do.
- The plan is the accurate view: it draws each link and marks in red the ones whose dates conflict.
- "VS: open blockers" is the chase list for dashboards: unfinished tickets that block something, soonest Due date first. A Jira query cannot see whether the ticket on the other end is still waiting, so read it as a list to check, not as proof.
- A blocker must be planned to finish before the blocked ticket starts. A blocker with a later Target PI than the ticket it blocks is a planning error, fixed in the room.
- When a team is actually stopped, it sets the flag on the blocked ticket. A link is a forecast; a flag is a fact.

**What goes into a PI plan, in this order**

1. Spillover from the PI that is ending. It is loaded first and uses capacity before anything new.
2. Epics tied to a regulatory or go-live Milestone that falls in or just after the PI.
3. Committed Features by Weighted Shortest Job First Score, each with all of its Epics.
4. Stretch Features, clearly labelled.

A Feature is committed for a PI only when every application it needs has committed its Epic. If one application cannot, there are three honest choices, made at planning and not discovered at the end: move the whole Feature to a later PI, cut the Feature down to what the available applications can deliver, or plan it across two PIs on purpose (next heading). When two sub value streams want the same team in the same PI, the value stream lead decides at the portfolio sync, using the scores and any Milestone dates.

**A Feature that spans two PIs on purpose.** Give the Feature the Target PI of its last Epic. Epics may carry an earlier Target PI than their Feature, never a later one. The early Epic counts as delivered on time in its own PI; the Feature counts in the later one.

**Spillover**

- **Definition.** A spillover is a committed Epic or Feature whose Target PI has ended and which has not reached Released. Nobody declares it; the fields show it.
- **Target PI is not edited to hide it.** The ticket keeps its original Target PI and gets its Actual PI when it finishes. Even if someone did edit it, the baseline table on the scorecard still holds the promise.
- **Where it sits in the next PI.** Spillover is carried work: the current-PI filters and the plan's current view include it automatically, next to the work planned for that PI, and it takes capacity first.
- **Every spillover gets a reason at the PI review**, as a comment on the Epic starting with one of five words: Dependency, Capacity, Scope, Defect, Environment. On the Feature, use the Change Reason field. Five words are enough to see a pattern after two PIs.
- **Every spillover gets a decision at the PI review**, by the sub value stream product lead and delivery lead: carry on (the default), stop (resolution Won't Do), or split (below).
- **Early warning during the PI.** Three lists catch a spillover before it happens: "VS: PI Epics not started" from week 5, Amber and Red RAG, and "VS: open blockers" past their Due date.

**Planned for one PI, delivered by one application only.** A worked case: Feature "M&P across the platform" is committed for PI 2027.4 with two committed Epics.

| Ticket | Target PI | At the end of PI 2027.4 | Actual PI | Scorecard result for PI 2027.4 |
| --- | --- | --- | --- | --- |
| Epic: M&P for Credit Application | PI 2027.4 | Released | PI 2027.4 | Delivered |
| Epic: M&P for Drawdowns | PI 2027.4 | Implementing | PI 2028.1, when it finishes | Spilled |
| Feature: M&P across the platform | PI 2027.4 | Implementing | PI 2028.1, when its last Epic finishes | Spilled, 1 of 2 Epics delivered |

What each person sees: Credit Application's Epic figure counts its Epic as delivered, so that team is not marked down for another team's delay. Drawdowns shows one spilled Epic with a reason. The sub value stream's Feature figure counts the Feature as spilled, and Confluence report 3 shows which application it is waiting for. In planning for PI 2028.1 the Drawdowns Epic is already in the current-PI views and takes capacity first.

Then one decision at the PI review. If the Credit Application part is useful to users by itself, the Feature may be split so the delivered part can be released: the original Feature is renamed to what was delivered and moves to Released, and a new Feature is created for the remainder, with the Drawdowns Epic under it and a relates to link between the two. A split never improves the score. The baseline line for the original Feature stays "spilled" for PI 2027.4, with a note that part was released. If nothing is usable until both applications are live, do not split: the Feature simply carries on.

A Feature moves to Released only when every one of its Epics is Released, Done, or closed as Won't Do. Jira cannot enforce this across projects, so Confluence report 3 lists any Released Feature that still has an unreleased Epic, and the delivery lead checks it weekly.

**Filters for this section** (they belong to the filter library; the first is edited at each PI change by adding the PI that has just ended)

| Save as | Query |
| --- | --- |
| VS: spillover | `issuetype in (Feature, Epic) AND project in (CLP, CA, DRAW, FL) AND "Target PI" in ("PI 2026.3", "PI 2026.4") AND labels = pi-committed AND status not in (Released, Done)` |
| VS: open blockers | `(filter = "VS: current PI Features" OR filter = "VS: PI Epics") AND issueLinkType = blocks AND status not in (Released, Done) ORDER BY duedate` |
| VS: PI Epics not started | `filter = "VS: PI Epics" AND status in (Idea, Analysis, Ready)` |
| VS: Features with a late application | Not possible as a Jira query. Use Confluence report 3, filtered to Features where some Epics are Released and some are not. |

The spillover query names the PIs that have ended, because Jira cannot compare one PI value with another. Keep the list to the last four PIs; anything older that is still open is a zombie and belongs in the hygiene review.

**Gadgets to add to the delivery lead and sub value stream dashboards:** Two Dimensional Filter Statistics on "VS: spillover", Project by Target PI (which application spills, and from when); Filter Results on "VS: open blockers"; Filter Results on "VS: PI Epics not started".

## Release planning

A release is a version in an application project, and a Feature is released when every one of its child Epics is in a released version. PI and release are kept apart on purpose: a PI is a planning window, a release is a production deployment, and one PI usually holds several releases.

**Naming.** Versions belong to one project in Jira, so a shared name is what ties them together.

| Case | Version name | Example |
| --- | --- | --- |
| One application goes live alone | `<APP> <year>.<month>` | `DRAW 2027.03` |
| Several applications go live together | Same name created in each project | `CLP 2027.03` in Credit Application, Drawdowns and Facility Letter |
| Emergency fix | `<APP> <year>.<month> HF<n>` | `DRAW 2027.03 HF1` |

Every version carries its go-live date in the release date field. A search on the version name finds its tickets in every project that has it.

**Steps for each release**

1. The delivery lead creates the version, with its date, as soon as the release is on the bank's change calendar, and creates an `ms-golive` Milestone if business users are waiting for it.
2. Product owners set the version on the Epics, and on the Stories and Bugs, going into it. Do this during sprint planning, not at the end.
3. Two sprints before go-live, the release gadgets on the delivery lead dashboard are reviewed weekly: open work, open bugs by priority, flagged items, open RAID linked to the Features in scope.
4. Scope cut-off: one sprint before go-live. Anything not Done is moved to the next version, and the Feature's product lead is told.
5. Go or no-go is recorded as a comment on the Milestone, and the change record number goes in Change Request ID on the Epics.
6. After deployment, the delivery lead marks the version as released in each project, and Epics move to Released. Features whose Epics are all Released move to Released.
7. After the early-life support period, Epics and Features move to Done.

**Release notes** come from a filter on the version name limited to Stories and Bugs with resolution Done.

**What Jira does not do here.** A released version in one project does not release the same-named version in another; mark each one. Version charts treat same-named versions in different projects as separate, so cross-application release views use filters, or a cross-project release in Plans, which exists only inside the plan.

## Dashboards by level

Reporting runs top-down in one line: VS Epics, then Features across the whole value stream, then Epics across applications, then the team. There is no separate set of views per sub value stream; the sub value stream is a column to sort or group by, never a filter that hides the rest. Five dashboards follow that line, each built only from standard Jira gadgets on saved filters. Filter names refer to the filter library.

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
| Filter Results, with the supplier and receiver sub value streams | VS: cross-stream dependencies | Who is waiting on whom across the value stream? |
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

**What standard Jira cannot show, and the way round it**

| Wanted | Why a gadget cannot | Where you get it |
| --- | --- | --- |
| Percentage complete of a Feature from its stories | Gadgets do not roll up the hierarchy. | The plan: progress bar per Feature and per VS Epic. |
| Feature progress across applications as a table | Same reason. | Confluence report 3 below. |
| Predictability trend across PIs | Jira keeps no snapshot of what was planned. | Confluence reports 1 and 2 below. |
| Scope added and removed during a PI | Same reason. | Confluence report 1 below. |
| Time spent waiting versus working | Needs time in each status. | An add-on (Time in Status, eazyBI) or an export to Power BI. |
| Team velocity as a gadget | Velocity is a board report. | The Velocity report on the team board; the plan uses it for capacity. |
| Deployment frequency and failure rate | That data sits in release and incident tools. | Those tools, not Jira. |

**Boards complement the dashboards.** Two boards serve the whole value stream. The VS Epic board has the VS Epic statuses as columns. The Feature board has the Feature statuses as columns, one swimlane per VS Epic, card colours by RAG Status, and quick filters for Current PI, Committed, Red and Amber, and Flagged. Neither board is split by sub value stream.

The view Jira cannot give is the roll-up along the line: each VS Epic with its Features, and each Feature with its Epics, counted and coloured. That lives in the plan and in the Confluence portfolio pages.

**A known limit, and its fix.** If Value Stream and Sub-Value Stream is a two-step dropdown, Plans cannot show it as a column, and dashboard gadgets may not accept it as an axis (Atlassian's pages do not confirm it for current versions). Test one gadget first. If it fails, use the shadow label: automation rules 1 and 2 write a label such as `svs-monitoring` on every ticket to match the field. Labels work as a gadget axis, a plan filter, a board swimlane and a Confluence column. People keep filling in the field; only automation writes the label.

## Reports in Confluence

Six Confluence pages cover what Jira dashboards cannot: roll-ups across applications, trends across PIs, date slippage, and a status report that writes itself. Each uses the Jira Issues macro on a saved filter, with Table Transformer or Chart from Table around it.

| # | Page | Built from | Shows |
| --- | --- | --- | --- |
| 1 | PI scorecard, one page per PI | A plain table pasted in when PI planning closes (Key, Summary, Sub value stream, Committed or Stretch). Beside it, a Jira Issues macro on that PI's own filter, such as "PI 2027.1 planned Features", so an old scorecard keeps showing its own PI. Table Transformer joins the two on Key. | For each committed Feature, its status and RAG now. Features in the live list only were added; Features in the pasted list only were removed. Also holds the PI objectives. |
| 2 | Predictability trend | Jira Issues macro on all Features labelled `pi-committed`, with Target PI and Actual PI. Table Transformer counts, per Target PI and sub value stream, how many have Actual PI equal to Target PI. Chart from Table as a line. | Whether each sub value stream delivers what it commits, PI after PI. No manual upkeep. |
| 3 | Feature progress across applications | Jira Issues macro on "VS: PI Epics" with Parent Link, Project, Status and RAG Status. Table Transformer groups by Parent Link. | One row per Feature: its Epics by application, how many are done, and the worst RAG among them. |
| 4 | PI health by sub value stream | Jira Issues macro on "VS: current PI Features" with the sub value stream, RAG Status, Status and Enabler Type. Table Transformer pivots; Chart from Table as stacked bars. | RAG, progress and investment mix per sub value stream. Use this where a dashboard gadget cannot split by the sub value stream field. |
| 5 | Milestone slippage | Jira Issues macro on Milestones with Baseline End Date and Due date. Table Transformer subtracts one from the other. | Days slipped per Milestone, and which have moved since baseline. |
| 6 | Weekly status report | Jira Issues macro on "VS: Red and Amber" with Executive Summary, Path to Green, Date to Green and Due date. No transformation. | The exceptions report for the portfolio sync, in the owners' own words. |

Three practical limits. The Jira Issues macro shows at most 1,000 issues and an admin cannot raise that, so keep each macro's filter narrow: one PI, or one sub value stream. On Jira versions 10.5 to 10.7 the Parent Link column in the macro showed raw text instead of the parent's key, fixed in later versions; check yours before building reports 3 and 7. And check the first join by hand: users have reported joins that silently dropped unmatched rows. The scorecard baseline is the figure of record; report 2 is the live trend drawn from it.

Use the same pages for the PI review: the scorecard is the agenda.

## Saved filter library

The library has about 45 value stream, release and hygiene filters, plus one set of about 12 per sub value stream and 8 per application team. All of them hang off five base filters. At each PI change the delivery lead creates two, repoints two and extends one, and edits the PI value in automation rule 4; nothing else changes. Filters are owned by the framework owner, shared with the value stream group, and never renamed, because dashboards, the plan and Confluence pages refer to them by name.

Placeholders to replace: `CLP` is the portfolio project key; `CA, DRAW, FL` stand for your application project keys; `Credit and Lending` and `Monitoring` stand for a value stream and a sub value stream; `PI 2027.1` is the current PI as your Target PI field writes it; `CLP 2027.03` is a release name; `Red`, `Amber`, `Risk` and `Dependency` stand for your field values. Test each query once before sharing it.

**Base filters (the last column says what to do at each PI change)**

| Save as | Query | At each PI change |
| --- | --- | --- |
| PI 2027.1 planned Features | `project = CLP AND issuetype = Feature AND "Target PI" = "PI 2027.1"` | Create a new one for the new PI. Never edit an old one: past scorecards read it. |
| PI 2027.1 planned Epics | `issuetype = Epic AND project in (CA, DRAW, FL) AND "Target PI" = "PI 2027.1"` | Create a new one. |
| VS: PI planned Features | `filter = "PI 2027.1 planned Features"` | Repoint to the new PI's filter. |
| VS: spillover | See Delivery control. | Add the PI that has just ended to its list. |
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
| VS: Red and Amber | `(filter = "VS: current PI Features" OR filter = "VS: PI Epics" OR filter = "VS: open VS Epics") AND "RAG Status" in (Red, Amber)` AND status not in (Released, Done) |
| VS: Management Attention and Red | `project = CLP AND issuetype in (Feature, "VS Epic") AND status not in (Released, Done) AND ("Management Attention" is not EMPTY OR "RAG Status" = Red)` |
| VS: Amber or Red without a plan | `filter = "VS: Red and Amber" AND "Path to Green" is EMPTY` |
| VS: RAG not refreshed in 14 days | `(filter = "VS: current PI Features" OR filter = "VS: PI Epics") AND status not in (Released, Done) AND updated <= -14d` |
| VS: open RAID | `project = CLP AND issuetype = "Delivery RAID" AND statusCategory != Done` |
| VS: open Red and Amber RAID | `filter = "VS: open RAID" AND "RAG Status" in (Red, Amber) ORDER BY duedate` |
| VS: cross-stream dependencies | `filter = "VS: open RAID" AND "RAID Type" = Dependency ORDER BY duedate` |
| VS: risks not reviewed | `filter = "VS: open RAID" AND "RAID Type" = Risk AND "ROAM Response" is EMPTY` |
| VS: RAID past its date | `filter = "VS: open RAID" AND duedate < now()` |
| VS: Milestones next 90 days and overdue | `project = CLP AND issuetype = Milestone AND statusCategory != Done AND duedate <= endOfDay("+90d") ORDER BY duedate` |
| VS: intake waiting | `project = CLP AND issuetype in (Feature, "VS Epic") AND status = Idea ORDER BY created` |
| VS: flagged | `(project = CLP OR filter = "VS: PI Epics") AND Flagged = Impediment` |

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
| Team: Epics blocked by others | `project = DRAW AND issuetype = Epic AND issueLinkType = "is blocked by" AND statusCategory != Done` |
| Team: open bugs | `project = DRAW AND issuetype = Bug AND statusCategory != Done` |
| Team: Epics without Feature | `project = DRAW AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` |
| Team: Stories without Epic | `project = DRAW AND issuetype in (Story, Task) AND "Epic Link" is EMPTY AND statusCategory != Done` |

**Hygiene (review monthly)**

| Save as | Query | Why it matters |
| --- | --- | --- |
| VS: hygiene exceptions | `project in (CA, DRAW, FL) AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` | Work the portfolio cannot see. |
| Hygiene: no sub value stream | `(project = CLP OR filter = "VS: PI Epics") AND "Value Stream and Sub-Value Stream" is EMPTY AND status != Idea` | Missing from every sub value stream view. |
| Hygiene: released without Actual PI | `issuetype in (Feature, Epic) AND project in (CLP, CA, DRAW, FL) AND status in (Released, Done) AND "Target PI" is not EMPTY AND "Actual PI" is EMPTY` | Predictability cannot be counted. |
| Hygiene: in progress without Target PI | `issuetype in (Feature, Epic) AND project in (CLP, CA, DRAW, FL) AND status = Implementing AND "Target PI" is EMPTY` | Work started outside the plan. |
| Hygiene: done without resolution | `project in (CLP, CA, DRAW, FL) AND statusCategory = Done AND resolution is EMPTY` | Missed by the trend gadgets. |
| Hygiene: open with resolution | `project in (CLP, CA, DRAW, FL) AND statusCategory != Done AND resolution is not EMPTY` | Wrongly counted as finished. |

**Notes for Data Center with Plans**

- **Parent.** `"Parent Link"` joins Epic to Feature and Feature to VS Epic. `"Epic Link"` joins Story to Epic. `"Parent Link" = CLP-123` returns the Features of a VS Epic, or the Epics of a Feature.
- **Everything under one ticket.** `issuekey in childIssuesOf("CLP-123")` returns all levels below it. Atlassian notes it can return too much when a ticket has changed type and kept an old Parent Link, and can fail on very large parents. Use it for one VS Epic at a time.
- **Sub value stream.** `cascadeOption("parent", "child")` is the query form for a two-step dropdown. If your field is a plain dropdown, write `"Value Stream and Sub-Value Stream" = "Monitoring"` instead.
- **Epics of a PI across applications.** This works because Epics carry Target PI and the sub value stream of their Feature. The sub value stream is copied down by automation rule 1. Target PI is set by the team at PI planning.
- **History.** Jira can search when Status changed, but not when RAG Status or Target PI changed. "RAG not refreshed" therefore uses the last update of the ticket, and scope added after planning uses the `unplanned` label.

## Automation rules

Seven automation rules keep the fields in step and chase missing updates, so that people are not asked to type the same thing twice or to police each other.

| # | Rule | When it runs | What it does | Who can build it |
| --- | --- | --- | --- | --- |
| 1 | Copy sub value stream down | An Epic is created, or its Parent Link changes | Looks up the parent Feature with `key in parentIssuesOf("<the Epic>") AND issuetype = Feature`, copies Value Stream and Sub-Value Stream to the Epic, and writes the matching `svs-` label. | Jira admin: it spans projects |
| 2 | Shadow label | Value Stream and Sub-Value Stream changes on a VS Epic, Feature, Milestone or Delivery RAID | Writes the matching `svs-` label and removes the old one. Needed only if the test of the field in gadgets fails. | Portfolio project admin |
| 3 | Ask for a recovery plan | RAG Status changes to Amber or Red while Path to Green is empty | Comments on the ticket, naming the assignee, asking for Path to Green and Date to Green. | Project admin |
| 4 | Record the finishing PI | A Feature or Epic moves to Released with Actual PI empty | Sets Actual PI to the current PI. The value in the rule is edited on the first day of each PI. | Project admin |
| 5 | Chase stale trouble | Every Monday | Emails the assignee of each Amber or Red ticket not updated in 14 days. Green tickets are not chased. | Project admin, one rule per project |
| 6 | Chase overdue RAID | Every Monday | Comments on each ticket in "VS: RAID past its date", naming the assignee. | Portfolio project admin |
| 7 | Keep Parent Link clean | An issue changes type | Clears Parent Link, which otherwise keeps a stale value and corrupts the hierarchy queries. This is Atlassian's own recommended fix. | Jira admin |

Build rules 3 to 6 first; they sit inside one project each. Whether a project admin may create rules is a setting the Jira admin controls, so confirm it. Rule 1 is the one to test carefully: Atlassian documents copying from a parent down to its children when the parent changes, and this rule works from the child's side, which I could not find a published example for. Until rule 1 exists, product owners set the sub value stream on Epics by hand, and the hygiene filter catches the gaps.

## What to ask the Jira admin for

Six requests, none of which adds a field or a status. The first four are needed to start; the last two can follow the pilot.

| # | Request | Why | Without it |
| --- | --- | --- | --- |
| 1 | Show Parent Link, Target PI, Actual PI, RAG Status and Value Stream and Sub-Value Stream on the create, edit and view screens of Epic in every application project. | Product owners can set and see them. This is the join between applications. | Fields can only be set from inside the plan. |
| 2 | A user group for the value stream that can create shared filters and dashboards and edit the plan and its shared teams. | Dashboards are blank for anyone who cannot see the filter. | Each person builds their own. |
| 3 | A resolution screen on the transition to Done for every issue type, with resolutions Done and Won't Do; resolution cleared on reopen. | Trend and predictability figures depend on resolution. | Cancelled work counts as delivered. |
| 4 | Automation rule 1, across the portfolio project and the application projects. | Epics inherit the sub value stream of their Feature. | Set by hand; gaps caught by the hygiene filter. |
| 5 | Make Target PI, Actual PI, RAG Status and the sub value stream field available as columns and filters in Plans. | The plan can be filtered and saved by PI, colour and sub value stream. | Filter the plan by a saved Jira filter instead. |
| 6 | Workflow checks: a Feature cannot leave Analysis without Parent Link, sub value stream and Enabler Type, and cannot enter Implementing without Target PI and RAG Status. | The definition of ready enforces itself. | Product leads check by hand, using "SVS: Features with gaps". |

Also ask the owner of the standards page two questions: when is Actual PI meant to be filled in, and is Target PI allowed to change after planning? This framework assumes "at Released" and "no, for committed work".

One status to consider: "In Review" for stories, only if teams need to see work waiting for test or review. No other new statuses are needed.

One decision for the admin, not a request: the status Released on Feature and Epic should sit in the green Done category only if a resolution is set at that point. Otherwise keep it in the blue In Progress category. The filters above name the statuses directly, so they work either way.

## Cloud version: later

This document is for Jira Data Center as it runs today; a Cloud version will follow once this one is working.

The design should travel well, because it rests on your standard fields and not on scripts. The known changes are small: the queries that use Parent Link and Epic Link are rewritten with the single `parent` field, the automation rules are re-tested, and the Confluence reports are re-tested with the Cloud editions of the add-ons.

One thing is worth asking the migration team early: on Cloud, Plans and the levels above Epic need the Premium plan.

## Rollout in three steps

Start with one sub value stream for one PI, then extend; the framework asks people to change habits, and one working example persuades faster than a mandate.

1. **Set up (weeks 1 to 3).** Agree this document with the product and delivery leads. Raise admin requests 1 to 4. Agree the RAG rules, the Target PI and Actual PI rules and the three labels. Build the base filters, the plan and automation rules 3 to 6. Build the value stream board and one sub value stream board.
2. **Pilot (one PI).** Pick the sub value stream with the most cross-application work; Monitoring is a likely candidate, with three applications. Move its in-flight initiatives into VS Epics and Features, parent its Epics, and run intake triage, the weekly sync and PI planning as written. Build dashboards 1 to 4 for it. Keep a list of what did not work.
3. **Extend (next PI).** Adjust the framework from the pilot list, bring in the other sub value streams, build the value stream dashboard, and start the fortnightly portfolio sync. Raise admin requests 5 and 6 with evidence from the pilot.

Two things will decide whether it holds: every Epic gets a parent Feature, and the meetings are run from the boards. The hygiene filters show the first; the second is yours to insist on.

## Sources

Checked on 26 November 2026. Some Atlassian pages loaded only in part, so the Jira Cloud gadget list and the behaviour of `parent` above Epic on a site without Plans are not confirmed; both are covered by the test-first note in the filter library.

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
- [Accelerating flow with SAFe](https://framework.scaledagile.com/accelerating-flow-with-safe) (Scaled Agile)
- [Milestones](https://v5.scaledagileframework.com/milestones/) (Scaled Agile)
- [Labels, components or custom fields](https://community.atlassian.com/forums/App-Central-articles/Labels-Component-or-Custom-Field-Which-one-is-best-for-your/ba-p/2809685) (Atlassian Community)
- [Jira link types: practice and misuse](https://community.atlassian.com/forums/App-Central-articles/Jira-Link-Types-Best-Practices-Common-Misuse-and-How-to-Control/ba-p/3155484) (Atlassian Community)
