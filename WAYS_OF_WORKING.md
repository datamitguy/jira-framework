# Ways of working

How the value stream plans, delivers and reports work in Jira, day to day. This is the short, practical companion to [FRAMEWORK.md](FRAMEWORK.md): the framework says how Jira is set up, this page says what people do.

It applies to everyone who raises, plans, builds, tests, releases or reports on work in the value stream. All names and numbers in examples are placeholders.

## 1. Seven principles

1. **One line of work.** Everything sits on the line VS Epic > Feature > Epic > Story. Work that is not on the line is not planned.
2. **Top-down view, bottom-up truth.** We read the portfolio from the VS Epic down. The facts come from the teams' tickets, never from a separate slide.
3. **Jira is the only record of delivery.** If it is not in Jira, it is not happening. Status is updated in the meeting, on the screen, not afterwards.
4. **A commitment is recorded once, in the open.** It is made at PI planning (the Epic first, then the Feature), written down on the day, and measured against that record.
5. **Bad news early.** Amber with a plan is good practice. Green that turns Red overnight is the failure.
6. **Finish before starting.** Carried-over work is planned first. We limit how much is in progress.
7. **Few rules, kept.** We add a field, status or label only by an agreed change, and we remove what nobody uses.

## 2. Who owns what

| Role | Owns | Keeps up to date | Decides |
| --- | --- | --- | --- |
| Value stream lead | VS Epics and the roadmap | VS Epic status, RAG Status, Executive Summary, rank order | Order of VS Epics; clashes between sub value streams; what gives way to a fixed date |
| Product lead (sub value stream) | Features | Feature status, RAG, scores, Target PI, Acceptance Criteria, commitment label | Order of Features; whether a Feature is ready; scope of a Feature |
| Delivery lead | The PI plan, RAID, Milestones, releases | Delivery RAID, Milestones, blocks links, release versions, the PI scorecard | With the product lead: changes after the PI lock, and what happens to spillover |
| Application product owner | Epics and the team backlog | Epic status, RAG, Parent Link, Target PI, Fix version, Story Points on the Epic | Whether the application takes an Epic into a PI; order of stories |
| Team | Stories, tasks, bugs, tests | Status, estimates, flags | How the work is done |
| Framework owner | These ways of working and the Jira set-up | Filters, dashboards, label list, change log | Changes to fields, statuses, labels and rules |

One person can hold more than one role. Every ticket has exactly one assignee, and that person is answerable for its status being true.

## 3. The line of work

| Level | Ticket | Says | Size | Lives in |
| --- | --- | --- | --- | --- |
| 1 | VS Epic | What gets better, and for whom | 2 to 4 PIs | Portfolio project |
| 2 | Feature | A capability, across applications | One PI | Portfolio project |
| 3 | Epic | One application's share of a Feature | 1 to 5 sprints | Application project |
| 4 | Story, Task, Bug, Test | A piece of work for one team | Under one sprint | Application project |

Five rules:

1. Every Epic has a parent Feature. Every Feature has a parent VS Epic.
2. A Feature is split by outcome, never by application. The application split is the Epic.
3. A Feature belongs to one sub value stream; its Epics can be in any application.
4. Upkeep goes under the standing "Run and improve" Feature. It is not committed and not scored.
5. An Epic without a parent is not planned into a PI.

## 4. What a good ticket looks like

| Ticket | Must have, from the status shown | Updated |
| --- | --- | --- |
| VS Epic | From Review: owner, objective. From Analysis: benefit stated, case linked, scores. From Implementing: RAG, Due date, Executive Summary. | Fortnightly, before the portfolio sync |
| Feature | From Analysis: parent VS Epic, sub value stream, Enabler Type. From Ready: Acceptance Criteria, scores, size, child Epics. From Implementing: Target PI, commitment label, RAG, Due date. | Weekly, before the sync |
| Epic | From Ready: Parent Link, Story Points, dependencies linked. From Implementing: Target PI, commitment label, RAG, Fix version. At Released: Change Request ID. | Weekly |
| Story | Acceptance criteria, estimate, Epic. | Daily |
| Delivery RAID | RAID Type, owner, Due date, RAG, a link to the work it affects. Risks: Probability, Impact, ROAM Response. | At each review |
| Milestone | Due date, Baseline End Date, kind label, links to what must finish for it. | When anything changes |

The shortlist of fields for each issue type, with who fills each one in and when, is in [FIELDS.md](FIELDS.md).

Summaries are written so a stranger understands them: VS Epics as outcomes ("Avoid audit risk through access control"), Features as capabilities ("M&P across the platform"), Epics as capability plus application ("M&P for Drawdowns").

## 5. The rhythm

| When | What | Who | Held on | Leaves behind |
| --- | --- | --- | --- | --- |
| Daily | Team stand-up | Team | Team board | Stories moved; blockers flagged |
| Weekly | Backlog refinement | Product owner, team | Team backlog | Epics made Ready; stories estimated |
| Weekly | Backlog triage, 30 minutes | Product lead, delivery lead | Feature board, Idea column | Features moved to Analysis or closed |
| Weekly | Delivery sync | Product leads, delivery leads, product owners | Dashboard 6 first, then 2 and 3 (or the delivery lead page in Confluence) | RAG, Path to Green and Date to Green refreshed; blockers and flags dealt with |
| Fortnightly | Portfolio sync | Value stream lead, product and delivery leads | Dashboard 1 and the Confluence landing page | VS Epics moved; Red and Amber decided; Milestones confirmed; limit on work in progress checked |
| Monthly | RAID review and hygiene check | Delivery leads, framework owner | Dashboard 4 and the hygiene filters | Every open RAID ticket reviewed; hygiene count per application published |
| Every 12 weeks | PI review, then PI planning | Everyone | PI scorecard, then the PI plan page in Confluence | Last PI scored; next PI committed and locked |

**The 12 weeks of a PI**

| Week | What happens |
| --- | --- |
| 1 to 10 | Five two-week sprints |
| 5 | Check committed Epics that have not started |
| 7 | Features for the next PI are in Analysis; new demand for the next PI closes |
| 8 | Every ask to another team for the next PI has been raised |
| 9 | Features for the next PI are Ready; draft Target PI set |
| 10 | Team capacity confirmed; every ask answered; dependencies linked |
| 11 | PI review: scorecard, spillover decisions, improvement actions |
| 11 to 12 | PI planning and lock; planning and improvement sprint |

Meeting rules: start from the board or dashboard, not from slides. Walk exceptions first (Red, Amber, flagged, overdue), then the rest only if time allows. Update the ticket in the room. End with the decisions read back.

## 6. How work flows

**1. New demand comes through the DDT.** The DDT is used only for demand that is in nobody's backlog yet: to discuss it, agree whether to do it, and agree a rough timeline and proposed PI. Once agreed, the product lead creates the Feature in Jira and closes the DDT entry. Existing Epic lists are not put through the DDT; they are stitched up to Features and VS Epics.

**2. A Feature is made ready.** In Analysis the product lead writes the acceptance criteria and benefits, links the design, creates one Epic in each application that must change, gets each team's estimate, links dependencies, and scores the Feature. It is Ready when:

- [ ] Parent VS Epic, sub value stream and Enabler Type are set
- [ ] Acceptance Criteria and Business Benefits are agreed with the sponsor
- [ ] Every application that must change has an Epic with an estimate
- [ ] Design is linked and required sign-offs are raised
- [ ] Dependencies are linked; outside dependencies have a RAID ticket with an owner
- [ ] It fits in one PI, or is an agreed two-PI Feature

**3. Work is committed at PI planning.** Carried-over work goes in first, then work tied to fixed dates, then Features in score order, then stretch. Each product owner commits the Epic for their application by setting Target PI and the committed label. A Feature is committed only when all its Epics are. If one application cannot take its share, the choice is made in the room: move the Feature, cut it down, or plan it over two PIs on purpose.

**4. The plan is locked.** When planning closes, the committed list is pasted into the PI scorecard. That table is the record of the promise and is not edited.

**5. Changes after the lock need a decision.** Work comes in or goes out only by decision of the product lead and delivery lead together (the value stream lead if more than one sub value stream is affected), and the decision names what moves out. What comes in is labelled `unplanned`; what goes out is labelled `pi-descoped` with a reason.

**6. Spillover is handled in the open.** A committed Epic or Feature not Released when its PI ends is a spillover. Its Target PI is left alone. At the PI review it gets a reason (Dependency, Capacity, Scope, Defect or Environment) and a decision: carry on, stop, or split. It is planned first in the next PI.

**7. Release.** Each release is a Fix version in each application project. Scope is cut off one sprint before go-live. A Feature moves to Released only when every one of its Epics is Released.

**8. Close.** A Feature is Done when early-life support has ended and the benefits have been looked at. A VS Epic is Done when its outcome has been measured.

## 7. Status and RAG

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

## 8. Dependencies and risks

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

## 9. Done means done

| Level | Done means |
| --- | --- |
| Story | Acceptance criteria met; reviewed; tests pass; no open severity 1 or 2 defect |
| Epic, Released | All stories Done; integration and regression tested; non-functional needs met or waived; in a released Fix version with its change record |
| Feature, Released | Every Epic Released; end-to-end test passed; business acceptance and sign-offs recorded |
| Feature, Done | Early-life support closed; benefits reviewed |
| VS Epic, Done | Outcome measured against what was promised |

Approvals are recorded as a task assigned to and closed by the approver, not as a comment.

## 10. Decisions and escalation

| Question | Who decides | If not settled, goes to |
| --- | --- | --- |
| Do we take on this new demand? | Owner of the DDT decision | Value stream lead |
| Which VS Epic comes first? | Value stream lead | Sponsor |
| Which Feature comes first? | Product lead, from the scores | Value stream lead |
| Will this application take the Epic this PI? | Its product owner | Product lead of the Feature |
| Two sub value streams want the same team | Value stream lead | Sponsor |
| Change the PI after the lock | Product lead and delivery lead | Portfolio sync |
| Carry on, stop or split a spillover | Product lead and delivery lead | Value stream lead |
| Change these ways of working | Framework owner | Value stream lead |

Escalate when a decision is needed that you cannot make, when a date outside the team is at risk, or when a blocker has stood for more than a week. Escalate by setting Red with what you need, and raising it at the next sync; do not wait for the sync if a Milestone is at stake.

## 11. Ten minutes a week: the hygiene habit

Each role runs its own short check before the weekly sync.

**Product owner**
- [ ] Every open Epic has a parent Feature
- [ ] Every Epic in progress has Target PI, RAG and a Fix version
- [ ] Flags are still true; stale ones are removed

**Product lead**
- [ ] Every Feature in progress has RAG refreshed this week
- [ ] Amber and Red Features have a Path to Green and a date
- [ ] Nothing has sat in Analysis for more than 30 days without a reason
- [ ] The Ready column is in the order you would plan it

**Delivery lead**
- [ ] No RAID ticket is past its date
- [ ] Every open blocker has an owner and a date
- [ ] Milestone dates are current; moved dates have a comment
- [ ] Committed Epics that have not started are known

**Value stream lead (fortnightly)**
- [ ] Each VS Epic's Executive Summary says something new
- [ ] Work in progress is inside the limit
- [ ] Each Red has a decision or a date for one

## 12. What we do not do

- Start work that has no parent on the line.
- Keep a second status list in a spreadsheet or a slide.
- Move a date or a Target PI quietly to keep a ticket Green.
- Split a Feature to protect a score. Splits are for releasing something useful sooner.
- Mark a Feature Released while one application is still open.
- Add a field, status or label for one team's convenience.
- Compare teams by story points. Points are for a team's own planning.
- Leave an Epic open for a year. Close it or split it.

## 13. What we look at, and how we use it

| Measure | Tells us | Not used for |
| --- | --- | --- |
| Committed work delivered in its PI, for Features and for Epics | Whether our plans are realistic | Ranking teams or people |
| Spillover by application and by reason | Where plans break, and why | Blame |
| Features released per PI | How much reaches users | A target to maximise |
| Red and Amber with a plan | Whether problems are raised early | Counting "bad" tickets |
| Asks not agreed and their age; dependencies met by the need-by date; RAID past its date | Whether dependencies and risks are being managed | |
| Hygiene count per application | Whether the data can be trusted | |
| Benefits reviewed against promised | Whether the work was worth doing | |

Around 80% of commitments delivered is healthy. A steady 100% usually means too little was committed. A falling figure is a prompt to look at capacity and dependencies, not to push harder.

## 14. Changing these ways of working

Anyone can propose a change. The framework owner collects proposals, the leads decide monthly, and the change is written in the change log with its date and reason. Each PI review ends with no more than five improvement actions, each with an owner and a date, tracked like any other work.

## 15. Starting out

The path is set out in section 18 of the white paper. In short:

- [ ] Agree who approves the proposal, and brief the Jira administrator and the sponsor before anything is circulated
- [ ] Run the two-week proof of concept on one slice (one VS Epic, two or three Features, two or three applications) while the white paper is reviewed
- [ ] Hold the decision meeting: go, go with changes, or stop
- [ ] Name the framework owner, and the product lead and delivery lead for each sub value stream
- [ ] Stitch in waves, top-down: VS Epics and Features first, then each group of applications, until no Epic is without a parent
- [ ] Build the base filters, dashboards 1 to 3 and 6, and the five minimum Confluence pages (portfolio tree, Feature progress, PI plan with dependency board, PI scorecard, delivery lead view)
- [ ] Brief every role, and tell every team the RAG meanings and the label list
- [ ] Put the weekly delivery sync and the fortnightly portfolio sync in the diary, each tied to its dashboard, and run one with tickets updated in the room
- [ ] Fix the date of the first PI planning and work back the week 7, 8, 9 and 10 checkpoints. That planning is the first baseline.
