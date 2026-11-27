# Ways of working

How the value stream takes in demand, plans, delivers and reports work, day to day, and what each person does in Jira and Confluence at each step. The design behind it is in the [white paper](whitepaper/WHITE_PAPER.md); this page is the practical companion.

It applies to everyone who raises, plans, builds, tests, releases or reports on work in the value stream. All names, times and numbers in examples are placeholders. Nothing here has yet been run on the real Jira; the proof of concept will test it.

**Contents:** [1 Principles](#1-seven-principles) · [2 Where things live](#2-where-things-live) · [3 Who owns what](#3-who-owns-what-and-who-creates-which-ticket) · [4 The line of work](#4-the-line-of-work) · [5 Intake](#5-intake-from-a-request-to-a-feature) · [6 Design](#6-design-making-a-feature-ready) · [7 PI planning](#7-pi-planning-step-by-step) · [8 Delivery](#8-delivery-the-weekly-loop) · [9 Dependencies and risks](#9-dependencies-and-risks) · [10 Release and close](#10-release-and-close) · [11 PI close](#11-pi-close) · [12 Rhythm](#12-the-rhythm) · [13 Status and RAG](#13-status-and-rag) · [14 Done](#14-done-means-done) · [15 Decisions](#15-decisions-and-escalation) · [16 Hygiene](#16-ten-minutes-a-week-the-hygiene-habit) · [17 What we do not do](#17-what-we-do-not-do) · [18 Measures](#18-what-we-look-at-and-how-we-use-it) · [19 Changing this](#19-changing-these-ways-of-working) · [20 Starting out](#20-starting-out)

## 1. Seven principles

1. **One line of work.** Everything sits on the line VS Epic > Feature > Epic > Story. Work that is not on the line is not planned.
2. **Top-down view, bottom-up truth.** We read the portfolio from the VS Epic down. The facts come from the teams' tickets, never from a separate slide.
3. **Jira is the only record of delivery.** If it is not in Jira, it is not happening. Status is updated in the meeting, on the screen, not afterwards.
4. **A commitment is recorded once, in the open.** It is made at PI planning (the Epic first, then the Feature), written down on the day, and measured against that record.
5. **Bad news early.** Amber with a plan is good practice. Green that turns Red overnight is the failure.
6. **Finish before starting.** Carried-over work is planned first. We limit how much is in progress.
7. **Few rules, kept.** We add a field, status or label only by an agreed change, and we remove what nobody uses.

## 2. Where things live

Four places, each with one job.

| Place | Tool | Holds | Who works there |
| --- | --- | --- | --- |
| **Demand intake project** | Jira Service Management | Requests: what someone has asked for, and the decision on it | Requesters (through the portal), the intake owner, product leads, the DDT |
| **Portfolio project** | Jira | VS Epics, Features, Milestones, Delivery RAID | Value stream lead, product leads, delivery leads; product owners and scrum masters for RAID |
| **Application projects**, one per application | Jira | Epics, Stories, Tasks, Bugs, Tests, Sub-tasks | Product owners and teams |
| **Portfolio pages** | Confluence | The PI plan, the dependency board, the PI scorecard, roll-ups, and a page for each role | Everyone reads; delivery leads and the framework owner maintain |

Plans (Advanced Roadmaps) is used for one thing only, the L0 roadmap. Nobody needs to open it to plan or to report.

**Where to look**

| I want to know | Look at |
| --- | --- |
| What has been asked for and not yet decided | The intake queue in the demand intake project |
| How the value stream's outcomes are going | Jira dashboard 1; the portfolio tree page |
| What we are delivering this PI, and whether it fits | The PI plan page |
| Which application a Feature is waiting for | The Feature progress page |
| Who is waiting on whom | Jira dashboard 6; the dependency board on the PI plan page |
| What is blocked today | The delivery lead page; the team board |
| Whether we delivered what we committed | The PI scorecard |
| My own application's Epics | The product owner page for the application |

## 3. Who owns what, and who creates which ticket

| Role | Owns | Keeps up to date | Decides |
| --- | --- | --- | --- |
| Value stream lead | VS Epics and the roadmap | VS Epic status, RAG Status, Executive Summary, rank order | Order of VS Epics; clashes between sub value streams; what gives way to a fixed date |
| Product lead (sub value stream) | Features | Feature status, RAG, scores, Target PI, Acceptance Criteria, commitment label | Order of Features; whether a Feature is ready; scope of a Feature |
| Delivery lead | The PI plan page, the RAID and dependency register, Milestones, releases | Delivery RAID triage, Milestones, release versions, the PI scorecard | With the product lead: changes after the PI lock, and what happens to spillover |
| Application product owner | Epics and the team backlog | Epic status, RAG, Parent Link, Target PI, End Date, Fix version, Story Points on the Epic | Whether the application takes an Epic into a PI; order of stories |
| Team | Stories, tasks, bugs, tests | Status, estimates, flags | How the work is done |
| Intake owner (in the platform team) | The intake queue | Screening, routing, the age of requests | Whether a request is complete; where it is routed |
| Framework owner (in the platform team) | These ways of working and the Jira set-up | Filters, dashboards, Confluence pages, label list, change log | Changes to fields, statuses, labels and rules |

One person can hold more than one role. Every ticket has exactly one assignee, and that person is answerable for its status being true.

**Who creates which ticket**

| Ticket | Created by | When | Where |
| --- | --- | --- | --- |
| Request | Anyone with a need, through the portal | When the need arises | Demand intake project |
| Feature | Created automatically when a request is approved; owned from then on by the product lead. During stitching, by the product lead. | At approval | Portfolio project |
| VS Epic | Value stream lead | When an approved request, or a group of Features, is an outcome larger than one PI | Portfolio project |
| Epic | The product owner of the application that will do the work. Never the requester, and never someone from another team. | While the Feature is in Analysis | That application's project |
| Story, Task, Test | The team: product owner, analyst, engineers, testers | Refinement | Application project |
| Bug | Whoever finds it | When found | Application project, under the Epic it belongs to |
| Delivery RAID | Product owner, scrum master, delivery lead or product lead | When it needs managing above the team | Portfolio project |
| Milestone | Delivery lead | When a date that matters outside the teams is agreed | Portfolio project |
| Release version | Delivery lead | When the release is on the change calendar | Each application project in the release |

The rule behind the table: **nobody creates work in another team's project.** You ask; the team that will do the work creates its own ticket.

## 4. The line of work

| Level | Ticket | Says | Size | Lives in |
| --- | --- | --- | --- | --- |
| 1 | VS Epic | What gets better, and for whom | 2 to 4 PIs | Portfolio project |
| 2 | Feature | A capability, across applications | One PI | Portfolio project |
| 3 | Epic | One application's share of a Feature | 1 to 5 sprints | Application project |
| 4 | Story, Task, Bug, Test | A piece of work for one team | Under one sprint | Application project |

Six rules:

1. Every Epic has a parent Feature. Every Feature has a parent VS Epic.
2. A Feature is split by outcome, never by application. The application split is the Epic.
3. A Feature belongs to one sub value stream; its Epics can be in any application.
4. Upkeep goes under the standing "Run and improve" Feature. It is not committed and not scored.
5. An Epic without a parent is not planned into a PI.
6. Nobody creates work in another team's project.

Summaries are written so a stranger understands them: VS Epics as outcomes ("Avoid audit risk through access control"), Features as capabilities ("M&P across the platform"), Epics as capability plus application ("M&P for Drawdowns").

**What a good ticket has**

| Ticket | Must have, from the status shown | Updated |
| --- | --- | --- |
| VS Epic | From Review: owner, objective. From Analysis: benefit stated, case linked, scores. From Implementing: RAG, Due date, Executive Summary. | Fortnightly |
| Feature | From Analysis: parent VS Epic, sub value stream, Enabler Type. From Ready: Acceptance Criteria, scores, size, child Epics. From Implementing: Target PI, commitment label, RAG, Due date. | Weekly |
| Epic | From Ready: Parent Link, Story Points, dependencies linked. From Implementing: Target PI, commitment label, RAG, End Date, Fix version. At Released: Change Request ID. | Weekly |
| Story | Acceptance criteria, estimate, Epic | Daily |
| Delivery RAID | RAID Type, owner, Due date, RAG, a link to the work it affects. Risks: Probability, Impact, ROAM Response. Dependencies: supplier, need-by date, promised date once agreed. | At each review |
| Milestone | Due date, Baseline End Date, kind label, links to what must finish for it | When anything changes |

The shortlist of fields for each issue type is in [FIELDS.md](FIELDS.md).

## 5. Intake: from a request to a Feature

### The front door

New demand comes in through one door: a request in the **demand intake project in Jira Service Management**. Requests are decided at the **DDT**, the advisory board forum that reviews new demand. The project is where a request is recorded; the DDT is where it is decided. The front door is used only for demand that is in nobody's backlog yet. Existing Epic lists do not go through it; they are stitched up to Features and VS Epics.

A request and the work that follows are **two tickets on purpose**:

| | The request | The Feature |
| --- | --- | --- |
| Belongs to | The requester | The product lead |
| Says | What was asked for, and why | What will be built, across which applications |
| Ends when | A decision is made and the requester has been told the outcome | The capability is live and its benefit looked at |
| Lives in | Demand intake project | Portfolio project |

Keeping them apart is what makes intake honest. A request can be declined without leaving a dead ticket in the delivery backlog. One request can become several Features, and several requests can be merged into one Feature. And the requester can follow their own request without needing access to the delivery projects.

What makes two tickets painless: **nothing is typed twice.** The Feature is created from the approved request by automation, with the text copied across and the two tickets linked. The requester is told the outcome on the request itself.

### The seven steps

| # | Step | Who | In Jira | By when |
| --- | --- | --- | --- | --- |
| 1 | **Raise** | Anyone with a need | A request through the portal form (below) | Any time; the cut-off for the next PI is week 7 of the current one |
| 2 | **Screen** | Intake owner | Checks the form is complete and looks for a duplicate. Routes it (table below). Assigns it to the product lead of the sub value stream that would be accountable. | Within 5 working days |
| 3 | **Assess** | Product lead, with the product owners likely to be involved | Adds to the request: which VS Epic it would serve, a T-Shirt Size, the applications likely to change, and a proposed PI | Within 10 working days of screening |
| 4 | **Decide** | The DDT, working from the intake queue on screen | Approve, decline, park, or merge with another request. Recorded as the approval on the request, with a one-line reason, in the meeting. | At the next DDT after assessment |
| 5 | **Hand over** | Automation, then the product lead | On approval, a Feature is created in the portfolio project in status Idea, with the summary, description and sponsor copied and a link back to the request. The request moves to its "approved" status and the requester is notified. | The same day |
| 6 | **Triage** | Product lead | On the Feature: sets Parent Link to the VS Epic, sub value stream and Enabler Type; moves it to Analysis when there is capacity to shape it | Weekly triage |
| 7 | **Close the loop** | Automation | When the Feature reaches Released, a comment is added to the request and it is closed | At release |

A proposed PI on a request is a proposal. It becomes a Target PI only at PI planning.

### The request form

Short enough that people will fill it in; complete enough to decide on.

| Field on the form | Why it is asked |
| --- | --- |
| What is the problem, and for whom? | So the need is stated, not a solution |
| What should be true when it is solved? | Becomes the outcome on the Feature |
| Who is the sponsor? | Someone who will accept the result and defend its priority |
| Is there a fixed date, and where does it come from? | Regulatory and audit dates are planned first |
| What happens if this is not done? | The cost of delay |
| Which business line or users are affected? | Helps find the accountable sub value stream |
| Is it regulatory, audit or control related? Reference? | Sets the route |
| Anything already known: applications, size, related work | Optional |

### How a request is routed at screening

Not everything needs a Feature. The intake owner routes each request once.

| The request is | Route | Result on the request |
| --- | --- | --- |
| A defect or a production problem | The incident tool, or a Bug in the application project | Closed: "routed to support", with the reference |
| A small change to one application, about a sprint or less | Straight to that application's product owner, who creates a Story or Epic under "Run and improve" | Closed: "routed to the team", with the link |
| A new capability, one PI or less, in one or more applications | Assessment, then a Feature | Steps 3 to 7 |
| An outcome larger than one PI, or across sub value streams | Assessment, then a VS Epic created by the value stream lead, with Features to follow | Linked to the VS Epic |
| Regulatory, audit or control work with a fixed date | Fast path: assessed within 5 working days; a Feature plus a Milestone | Steps 3 to 7, ahead of the queue |
| A duplicate | Linked to the earlier request with "duplicates" | Closed, pointing to the other |
| Urgent, and cannot wait for the next PI | The urgent path below | |

### The urgent path

An urgent request after PI planning has closed still starts as a request. The product lead and delivery lead decide together (the value stream lead if more than one sub value stream is affected), and **the decision names what moves out**. What comes in gets Target PI and the `unplanned` label; what goes out gets `pi-descoped` with a reason. Each team holds a reserve for this, so the first urgent item does not break the plan.

### What the requester sees

| Request status | Means |
| --- | --- |
| Waiting for screening | Received |
| Under assessment | A product lead is sizing it |
| Waiting for decision | On the agenda of the next DDT |
| Approved, in delivery | Accepted; the linked Feature shows progress |
| Declined, parked or routed | With the reason, or where it went |
| Closed | Delivered, or finished as above |

The exact status names are those of the demand intake project; the meanings are what matter. The intake queue is the DDT's agenda: nothing waits for screening more than 5 working days, and nothing that has been assessed waits for more than one DDT. The portfolio sync sees the queue and its ages, but does not decide requests.

### To settle before intake goes live

- How often the DDT sits, and who chairs it. If it sits less often than fortnightly, the 20 working days from request to decision cannot be kept, and regulatory items need a decision between sittings.
- Whether the Jira administrator will build the cross-project automation that creates the Feature and closes the loop. Until then, the product lead uses "Create linked issue" on the approved request, which also copies the text and links the two.
- Whether requesters need a Jira licence to use the portal. They normally do not.
- The approval step and the status names in the demand intake project's workflow.

## 6. Design: making a Feature ready

The product lead owns the Feature through Analysis.

| # | Step | Who | In Jira |
| --- | --- | --- | --- |
| 1 | Write the outcome | Product lead, analyst | Acceptance Criteria and Business Benefits on the Feature |
| 2 | Name the applications | Product lead with the product owners | Each product owner creates their own Epic in their own project, with Parent Link to the Feature |
| 3 | Design | Analyst, architects, the teams | Design page linked on the Feature; a sign-off task for each approval needed, assigned to the approver |
| 4 | Estimate | Each team | Story Points on each Epic; T-Shirt Size on the Feature |
| 5 | Find the dependencies | Product owners | Inside the Feature: a blocks link between the Epics. Outside the Feature: an ask raised as a Delivery RAID Dependency (section 9). |
| 6 | Score | The sub value stream's leads together, in one session | The four scores on the Feature; the Feature placed in order on the board |

A Feature is **Ready** when:

- [ ] Parent VS Epic, sub value stream and Enabler Type are set
- [ ] Acceptance Criteria and Business Benefits are agreed with the sponsor
- [ ] Every application that must change has an Epic with an estimate
- [ ] Design is linked and required sign-offs are raised
- [ ] Dependencies are linked, and every ask to another team has been raised
- [ ] It fits in one PI, or is an agreed two-PI Feature

## 7. PI planning, step by step

Planning a PI means deciding which Ready Features, and which of their Epics, get that PI in the Target PI field. Changes are made on the tickets. Everyone reads the result on one Confluence page, the PI plan page.

### Before: weeks 7 to 10 of the current PI

| Week | What | Who | In Jira and Confluence |
| --- | --- | --- | --- |
| 7 | Intake for the next PI closes. Features proposed for it are at least in Analysis. | Intake owner, product leads | Requests raised later wait for the PI after, unless urgent |
| 8 | Every ask to another team for the next PI is raised | Receiving product owners | Delivery RAID Dependency tickets, status Backlog |
| 9 | Proposed Features are Ready. A Feature that is not Ready does not enter planning. | Product leads | Draft Target PI on the proposed Features, best score first |
| 9 | The PI plan page is set up | Delivery lead | Two filters created (`PI <next> planned Features`, `PI <next> planned Epics`); the PI plan page copied and pointed at them |
| 10 | Capacity is known | Scrum masters | One number per team typed into the capacity table on the PI plan page: average of the last three sprints, times five, less known leave |
| 10 | Every ask has an answer | Supplying product owners | Accepted with a promised date, another date proposed, or declined |
| 10 | Sprints exist | Scrum masters | Five sprints per team, named `PI 2027.2 S1 <team>` to `S5` |
| 10 | The reserve is agreed | Each team with its product lead | The share held back for run work and urgent items, noted beside the capacity |

### In the room: two days

Times are a pattern to adapt. The PI plan page is on the main screen throughout and is reloaded at each checkpoint.

**Day 1**

| Time | What | Who | On screen |
| --- | --- | --- | --- |
| 09:00 | Where we are: the roadmap, the objectives for the PI, the result of the PI just ending | Value stream lead | L0 roadmap; last PI scorecard |
| 09:30 | The proposed Features, in score order, with what each needs from which application | Product leads | PI plan page, Features |
| 10:30 | What is carried over, capacity per team, dependencies already known | Delivery leads | PI plan page: capacity and dependency board |
| 11:00 | Team breakout 1 | Each team with its product owner | Team backlog |
| 15:00 | Draft plan review, five minutes a team: load against capacity, what did not fit, what we need from others | Product owners | PI plan page, reloaded |
| 16:00 | Dependency walk: asks not agreed, date conflicts, anything found today | Delivery leads | Dependency board |
| 16:30 | Leads' session: settle what is over capacity and what conflicts | Product leads, delivery leads, value stream lead | PI plan page |

**Day 2**

| Time | What | Who | On screen |
| --- | --- | --- | --- |
| 09:00 | Changes from the leads' session | Value stream lead | PI plan page |
| 09:30 | Team breakout 2: adjust, finish sprint loading | Each team | Team backlog |
| 12:00 | Final plan review, and risks reviewed one by one | Product owners; delivery leads run the risk review | PI plan page; open risks |
| 14:00 | Confidence vote | Everyone | |
| 14:30 | Commit: committed or stretch on each Epic, then each Feature | Product owners, then product leads | PI plan page |
| 15:30 | The lock | Delivery lead | PI scorecard |

**What a team does in a breakout**

1. Places carried-over work first.
2. Takes the proposed Epics in the order of their Features, and for each one it can take: the product owner sets **Target PI** and **End Date** on the Epic (on the Epic itself, or for several at once with bulk change from a search).
3. Puts the stories for the first sprints into sprints on the team backlog, up to capacity.
4. Says out loud what does not fit. An Epic that does not fit gets no Target PI.
5. Raises an ask for anything it needs from another team and has not yet asked for, and answers asks addressed to it.
6. Raises a Delivery RAID ticket for each risk it cannot handle itself.

**What goes in, in this order**

1. Carried-over work from the PI that is ending.
2. Work tied to a regulatory or go-live Milestone in or just after the PI.
3. Features in score order, each with all of its Epics.
4. Stretch Features, clearly labelled.

**When one application cannot take its share of a Feature**, the choice is made in the room, not discovered at the end: move the whole Feature to a later PI, cut the Feature down to what the available applications can deliver, or plan it across two PIs on purpose.

**Risks in the room.** Each risk is read out and given one of four responses, recorded in ROAM Response: Resolved, Owned (a named person will act), Accepted (the value stream lead agrees to live with it), or Mitigated.

### The lock

Planning is closed only when all of these are true.

| Check | Where it is seen |
| --- | --- |
| Every committed Feature has all its Epics committed | PI plan page |
| Every team's committed load is within its capacity | Capacity table on the PI plan page |
| Every dependency has a promised date on or before its need-by date | Dependency board: no negative or unknown margin |
| No committed Epic waits on an unagreed dependency. Such an Epic is stretch. | Dependency board |
| Every risk raised has an owner and a response | Open risks |
| The confidence vote is recorded | Comment on the planning Milestone |

Then the delivery lead announces the lock and pastes two tables into the new PI scorecard page: the committed and stretch list, and the dependency board. **The pasted list is the baseline.** It is the only thing predictability is counted from, and nobody edits it.

Commitment is made twice. Each product owner commits the Epic for their application with the label `pi-committed`. The product lead commits the Feature only when every one of its Epics is committed.

### After

| When | What | Who |
| --- | --- | --- |
| Within three working days | Objectives for the PI written on the scorecard, three to six, in business language | Product leads |
| Day 1 of the new PI | The current-PI filters repointed; the ended PI added to the spillover filter; the PI value changed in automation rule 4 and the board quick filter | Delivery lead |
| Day 1 | RAG set to Green on everything committed | Product owners, product leads |
| After the lock | Target PI and the commitment labels change only by decision (section 5, the urgent path) | Product lead and delivery lead |

## 8. Delivery: the weekly loop

| When | Who | Does |
| --- | --- | --- |
| Every day | Team | Moves stories; flags what is stopped and removes the flag the day it clears |
| Before the weekly sync | Product owner | Ten minutes: Epic status, RAG, End Date, Fix version; a recovery plan if Amber or Red; asks raised and answered |
| Before the weekly sync | Product lead | Feature status against its Epics; RAG; Path to Green and Date to Green if Amber or Red |
| Weekly delivery sync | Product leads, delivery leads, product owners | Opens on the dependency dashboard and the delivery lead page: what is blocked, which asks are unanswered, what is late. Then Features and Epics that are Red or Amber. Tickets are updated in the room. |
| From week 5 | Delivery lead | Reads out committed Epics that have not started |
| The DDT, as it sits | Its members, with the intake owner presenting | Decides every assessed request in the intake queue, on screen |
| Fortnightly portfolio sync | Value stream lead, product and delivery leads | VS Epics; Red items needing a decision; Milestones; work in progress against the limit; the age of the intake queue |
| Monthly | Delivery leads, framework owner | Every open RAID ticket reviewed or closed; the hygiene count published |

Meeting rules: start from the board, dashboard or page, not from slides. Walk exceptions first (Red, Amber, flagged, overdue), then the rest only if time allows. Update the ticket in the room. End with the decisions read back.

## 9. Dependencies and risks

The full method is section 12 of the white paper. The working rules:

- **Nobody creates work in another team's project.** If you need something from another team, raise an ask: a Delivery RAID ticket of type Dependency in the portfolio project, addressed to the supplier's product owner, with the date you need it. The supplier creates its own ticket in its own backlog.
- **An ask is answered within five working days:** accepted with a promised date, another date proposed, or declined with a reason.
- **Accepting means linking.** The supplier links its own Epic or Story to the dependency ticket, adds a **blocks** link to the waiting Epic, writes the promised date in Baseline End Date, and moves the ticket to In Progress.
- **Work inside one Feature needs no RAID ticket.** Each application's share is an Epic under the Feature, with a blocks link if one must finish first. Raise a RAID ticket only if it is not agreed or is at risk.
- **Blocked today means flagged today.** A flag that has been on for two working days becomes a Delivery RAID ticket, linked to the Epic.
- **No commitment on an unagreed dependency.** At PI planning, an Epic that waits on an ask with no promised date, or a promised date after the need-by date, is stretch, not committed.
- **Only the receiver closes a dependency,** when what was delivered is usable.
- A risk is raised when something might move a date. It has an owner, a response, and a review date. An accepted risk stays open and visible, with the name of the person who accepted it.
- **Who does what:** product owners own asks and promises; the delivery lead owns the register and the process and triages every new RAID ticket within two working days; product leads decide what gives; the value stream lead settles conflicts between sub value streams.

## 10. Release and close

| Step | Who | In Jira |
| --- | --- | --- |
| The release goes on the change calendar | Delivery lead | A Fix version with the same name and the go-live date in each application project in the release |
| Scope is set | Product owners | Fix version on the Epics, Stories and Bugs going in, at sprint planning |
| Two sprints before go-live | Delivery lead | Weekly review of open work, open bugs, flags and linked RAID |
| One sprint before go-live | Product owners | Scope cut-off: anything not Done moves to the next version, and the product lead is told |
| Go or no-go | Through the change process | The decision as a comment on the go-live Milestone; the change record number on the Epics |
| Go-live | Delivery lead, product owners | Version marked as released in each project; Epics moved to Released |
| The Feature | Product lead | Moved to Released only when every one of its Epics is Released |
| Early life | Product lead | Feature moved to Done when the support period has ended and the benefits have been looked at |
| The outcome | Value stream lead | VS Epic moved to Done when its outcome has been measured |

## 11. PI close

| Step | Who | Result |
| --- | --- | --- |
| Score every committed line of the baseline: delivered, spilled, descoped or stopped | Delivery lead | The PI scorecard, with three figures side by side: Features, Epics and story points |
| Give each spillover a reason: Dependency, Capacity, Scope, Defect or Environment | Product owner, as a comment on the Epic | A pattern after two PIs |
| Decide each spillover: carry on, stop or split | Product lead and delivery lead | Carried-over work goes first in the next PI. Its Target PI is left alone. |
| Score each dependency: met on time, met late, not met | Delivery lead | The dependency measures |
| Score the PI objectives | Sponsor | Planned value against achieved value |
| Agree no more than five improvement actions | Everyone, at the PI review | Each is a task with an owner and a date |

A split never improves a score: the baseline line stays as it was.

## 12. The rhythm

| When | What | Who | Held on |
| --- | --- | --- | --- |
| Daily | Team stand-up | Team | Team board |
| Weekly | Backlog refinement | Product owner, team | Team backlog |
| Weekly | Intake screening | Intake owner | Intake queue |
| Weekly | Backlog triage, 30 minutes | Product lead, delivery lead | Feature board, Idea column |
| Weekly | Delivery sync | Product leads, delivery leads, product owners | Dashboard 6 and the delivery lead page, then dashboards 2 and 3 |
| As it sits | DDT: decisions on new demand | Its members; the intake owner presents | Intake queue |
| Fortnightly | Portfolio sync | Value stream lead, product and delivery leads | Dashboard 1; the portfolio pages |
| Monthly | RAID review and hygiene check | Delivery leads, framework owner | Dashboard 4 and the hygiene filters |
| Every 12 weeks | PI review, then PI planning | Everyone | PI scorecard, then the PI plan page |

**The 12 weeks of a PI**

| Week | What happens |
| --- | --- |
| 1 to 10 | Five two-week sprints |
| 5 | Check committed Epics that have not started |
| 7 | Intake for the next PI closes; its Features are in Analysis |
| 8 | Every ask to another team for the next PI has been raised |
| 9 | Features for the next PI are Ready; draft Target PI set; PI plan page set up |
| 10 | Team capacity confirmed; every ask answered; sprints created |
| 11 | PI review: scorecard, spillover decisions, improvement actions |
| 11 to 12 | PI planning and lock; planning and improvement sprint |

## 13. Status and RAG

**Status says where the work is. RAG says whether it will hit its date.** They are different, and both are kept true.

| RAG | Means | The owner must |
| --- | --- | --- |
| Green | On track for its date (Due date; End Date on an Epic); no help needed | Be able to say why, if asked |
| Amber | The date is at risk and there is a recovery plan | Fill in Path to Green and Date to Green (on an Epic: a comment starting "Path to green:") |
| Red | The date will be missed unless someone outside the team acts | Say what is needed and from whom; set Management Attention on a Feature |

- A parent is never greener than what sits beneath it.
- RAG is the owner's judgement, refreshed weekly. Nobody is criticised for raising Amber early.
- Blocked is the flag on the ticket, set when the team is actually stopped.
- Cancelled work is closed with resolution "Won't Do", not left open and not marked Done.

## 14. Done means done

| Level | Done means |
| --- | --- |
| Story | Acceptance criteria met; reviewed; tests pass; no open severity 1 or 2 defect |
| Epic, Released | All stories Done; integration and regression tested; non-functional needs met or waived; in a released Fix version with its change record |
| Feature, Released | Every Epic Released; end-to-end test passed; business acceptance and sign-offs recorded |
| Feature, Done | Early-life support closed; benefits reviewed |
| VS Epic, Done | Outcome measured against what was promised |

Approvals are recorded as a task assigned to and closed by the approver, not as a comment.

## 15. Decisions and escalation

| Question | Who decides | If not settled, goes to |
| --- | --- | --- |
| Is this request complete, and where is it routed? | Intake owner | Product lead |
| Do we take on this new demand? | The DDT | Value stream lead, then the sponsor |
| Which VS Epic comes first? | Value stream lead | Sponsor |
| Which Feature comes first? | Product lead, from the scores | Value stream lead |
| Will this application take the Epic this PI? | Its product owner | Product lead of the Feature |
| Will we supply what another team has asked for, and by when? | The supplying product owner | The two product leads |
| Two sub value streams want the same team | Value stream lead | Sponsor |
| Change the PI after the lock | Product lead and delivery lead | Portfolio sync |
| Carry on, stop or split a spillover | Product lead and delivery lead | Value stream lead |
| Change these ways of working | Framework owner | Value stream lead |

Escalate when a decision is needed that you cannot make, when a date outside the team is at risk, or when a flag has been on for two working days. Escalate by setting Red with what you need, and raising it at the next sync; do not wait for the sync if a Milestone is at stake.

## 16. Ten minutes a week: the hygiene habit

Each role runs its own short check before the weekly sync.

**Product owner**
- [ ] Every open Epic has a parent Feature
- [ ] Every Epic in progress has Target PI, RAG, End Date and a Fix version
- [ ] Flags are still true; stale ones are removed
- [ ] Asks I raised are still needed; asks addressed to me are answered

**Product lead**
- [ ] Every Feature in progress has RAG refreshed this week
- [ ] Amber and Red Features have a Path to Green and a date
- [ ] Nothing has sat in Analysis for more than 30 days without a reason
- [ ] The Ready column is in the order you would plan it
- [ ] Requests assigned to me for assessment are not older than 10 working days

**Delivery lead**
- [ ] Every new RAID ticket has been triaged within two working days
- [ ] No ask is unanswered after five working days; no RAID ticket is past its date
- [ ] Milestone dates are current; moved dates have a comment
- [ ] Committed Epics that have not started are known

**Intake owner**
- [ ] Nothing has waited for screening more than five working days
- [ ] Every assessed request is on the agenda of the next DDT, with its assessment filled in

**Value stream lead (fortnightly)**
- [ ] Each VS Epic's Executive Summary says something new
- [ ] Work in progress is inside the limit
- [ ] Each Red has a decision or a date for one

## 17. What we do not do

- Start work that has no parent on the line.
- Ask another team for work by message, or by creating a ticket in their project.
- Take a request straight to a team, round the front door, unless it is a small change routed there at screening.
- Keep a second status list in a spreadsheet or a slide.
- Move a date or a Target PI quietly to keep a ticket Green.
- Commit an Epic that waits on a dependency nobody has agreed.
- Split a Feature to protect a score. Splits are for releasing something useful sooner.
- Mark a Feature Released while one application is still open.
- Add a field, status or label for one team's convenience.
- Compare teams by story points. Points are for a team's own planning.
- Leave an Epic open for a year. Close it or split it.

## 18. What we look at, and how we use it

| Measure | Tells us | Not used for |
| --- | --- | --- |
| Requests waiting, and their age at each step | Whether intake keeps its promises to requesters | |
| Committed work delivered in its PI, for Features and for Epics | Whether our plans are realistic | Ranking teams or people |
| Spillover by application and by reason | Where plans break, and why | Blame |
| Features released per PI | How much reaches users | A target to maximise |
| Red and Amber with a plan | Whether problems are raised early | Counting "bad" tickets |
| Asks not agreed and their age; dependencies met by the need-by date; RAID past its date | Whether dependencies and risks are being managed | |
| Hygiene count per application | Whether the data can be trusted | |
| Benefits reviewed against promised | Whether the work was worth doing | |

Around 80% of commitments delivered is healthy. A steady 100% usually means too little was committed. A falling figure is a prompt to look at capacity and dependencies, not to push harder.

## 19. Changing these ways of working

Anyone can propose a change. The framework owner collects proposals, the leads decide monthly, and the change is written in the change log with its date and reason. Each PI review ends with no more than five improvement actions, each with an owner and a date, tracked like any other work.

## 20. Starting out

The path is set out in section 18 of the white paper. In short:

- [ ] Agree who approves the proposal, and brief the Jira administrator and the sponsor before anything is circulated
- [ ] Run the two-week proof of concept on one slice (one VS Epic, two or three Features, two or three applications) while the white paper is reviewed. Put one real request through intake as part of it.
- [ ] Hold the decision meeting: go, go with changes, or stop
- [ ] Name the framework owner, the intake owner, and the product lead and delivery lead for each sub value stream
- [ ] Stitch in waves, top-down: VS Epics and Features first, then each group of applications, until no Epic is without a parent
- [ ] Build the base filters, dashboards 1 to 3 and 6, and the five minimum Confluence pages (portfolio tree, Feature progress, PI plan with dependency board, PI scorecard, delivery lead view)
- [ ] Brief every role, and tell every team the RAG meanings and the label list
- [ ] Put the weekly delivery sync and the fortnightly portfolio sync in the diary, each tied to its dashboard, and run one with tickets updated in the room
- [ ] Fix the date of the first PI planning and work back the week 7, 8, 9 and 10 checkpoints. That planning is the first baseline.
