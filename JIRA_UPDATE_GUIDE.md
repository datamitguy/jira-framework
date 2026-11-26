# Jira update guide: what to update, and when

For the people who do the work: engineers, testers, business analysts, scrum masters and product owners. It answers one question: what do I need to touch in Jira, and when?

The short version: keep your own ticket true, every day, in under two minutes. The portfolio views are built from your tickets, so nobody should need to ask you for a status.

All names in examples are placeholders. [WAYS_OF_WORKING.md](WAYS_OF_WORKING.md) explains why these rules exist.

## 1. The one-minute card

| When | Do this |
| --- | --- |
| You start a piece of work | Move it to In Progress. Make sure it is assigned to you and is in the sprint. |
| You are stopped by something outside your control | Flag the ticket and add one line saying what you are waiting for and from whom. |
| You are no longer stopped | Remove the flag the same day. |
| You finish | Move it to Done. Check it meets the definition of done first. |
| You find a defect | Raise a Bug under the right Epic, with Severity, Testing Phase and Environment. |
| You discover your work needs another team | Tell your product owner the same day, so the ask can be raised. Do not create a ticket in the other team's project. |
| A flag has been on for two working days | Ask your scrum master or product owner to raise a Delivery RAID ticket linked to the Epic. |
| You realise it will not finish this sprint | Say so at stand-up. Do not wait for the last day. |
| Scope or estimate changes a lot | Update the estimate and add a comment saying why. |

If you only remember three things: **status is true today, blocked means flagged, and every story has an Epic.**

## 2. If you build or test (engineer, tester, analyst)

**Every day, before or at stand-up (about two minutes)**

- [ ] Each ticket assigned to me shows its real status.
- [ ] Anything I am stopped on is flagged, with a comment.
- [ ] Anything I finished yesterday is Done.
- [ ] I have nothing In Progress that I have not touched for three days. If I do, I either move it back or say why.

**When a story is created or refined**

| Field | What to put |
| --- | --- |
| Summary | What will be true when it is done, in plain words |
| Epic Link | The Epic it belongs to. A story with no Epic is invisible to planning. |
| Acceptance Criteria | How we will know it works |
| Story Points | The team's estimate, agreed in refinement |
| Story Type | As your team uses it |
| Component | The module (for example Facility, Collateral, Approval) |

**During the sprint**

| Event | Update |
| --- | --- |
| Start work | Status to In Progress; assignee is you |
| Hand over to someone else | Change the assignee; one line in a comment about what is left |
| Blocked | Flag, plus a comment naming who or what |
| Ready for test or review | Use your team's convention (a sub-task, or the In Review status if your project has it) |
| Finished | Status to Done. Jira sets the resolution; do not leave it empty. |
| Will not be done after all | Close with resolution "Won't Do" and a one-line reason. Do not delete it. |

**When you raise a Bug**

| Field | What to put |
| --- | --- |
| Summary | What is wrong, where |
| Epic Link | The Epic that the defect belongs to. If it is a production defect with no clear Epic, use the "Run and improve" Epic. |
| Severity | The agreed scale. Severity is impact; Priority is order of work. Do not mix them. |
| Testing Phase | Where it was found: for example system test, UAT, production |
| Environment | Which environment |
| Fix versions | The release it must be fixed in, if known |
| Affects versions | The release it was found in |
| Description | Steps to reproduce, expected result, actual result |
| Root cause category | Filled in when the Bug is closed |

**At the end of the sprint**

- [ ] Everything finished is Done before the sprint is closed.
- [ ] Anything unfinished has a comment saying what is left. The scrum master moves it to the next sprint or back to the backlog.

**You never need to touch:** Target PI, Actual PI, RAG Status, Parent Link, commitment labels, Fix version on Epics. Those belong to your product owner.

## 3. If you are a scrum master or team lead

**Daily**

- [ ] The board shows what was said at stand-up. Fix it in the meeting.
- [ ] Every flag is still true. A flag that has been on for two working days becomes a Delivery RAID ticket, linked to the Epic.

**Sprint planning**

- [ ] Sprint is named to the convention: `PI 2027.1 S3 <team>`.
- [ ] Every story in the sprint has an Epic, an estimate and an assignee.
- [ ] Carried-over stories are planned first.
- [ ] Planned points are within the team's recent average.

**Sprint close**

- [ ] Complete the sprint in Jira on the last day, not the week after.
- [ ] Unfinished stories are moved deliberately, not all rolled over by default.
- [ ] Tell the product owner of anything that puts an Epic's date at risk.

**Monthly**

- [ ] Run the team's hygiene filters: stories without an Epic, Epics without a parent Feature, Done without a resolution.

## 4. If you are an application product owner

You own the Epics. Your Epics are how your application shows up in the portfolio, so these fields matter more than any others.

**When an Epic is created**

| Field | What to put | Why |
| --- | --- | --- |
| Summary and Epic Name | The capability plus your application: "M&P for Drawdowns" | People outside the team read it |
| Parent Link | The Feature it delivers | Without it the Epic is invisible to the portfolio and is not planned |
| Value Stream and Sub-Value Stream | Copied from the parent Feature by automation (rule 1). Set by hand, to the same value as the Feature, only until the rule exists. | So the Feature's work is found across applications |
| Story Points | A planning estimate from the team | Used for capacity and for sizing the VS Epic |
| Component | The module | |

**At PI planning**

| Field | What to put |
| --- | --- |
| Target PI | The PI you are taking the Epic into. Setting it is your acceptance of the work. |
| Label | `pi-committed` if you are promising it and every dependency it waits on is agreed and dated before you need it; otherwise `pi-stretch` |
| End Date | The date you expect it live |
| RAG Status | Green |
| Fix versions | The release it is aimed at, if known |
| Links | **blocks** or **is blocked by**, to an Epic under the same Feature in another application. For work from outside the Feature, raise an ask (see below). |

After planning is locked, do not change Target PI or the commitment label. If the plan has to change, talk to your product lead and delivery lead; they record the decision.

**When you need something from another team (an ask)**

| Step | What to do |
| --- | --- |
| Raise | Create a Delivery RAID ticket in the portfolio project: RAID Type Dependency; a summary saying who needs what by when; Due date = the date you need it; the supplier's sub value stream; Assignee = the supplier's product owner. Link it to your waiting Epic with **relates to**. |
| Chase | It is yours to chase. No answer after five working days: raise it at the delivery sync. |
| Keep true | The need-by date and the RAG Status are your judgement. |
| Close | When what was delivered is usable, move the ticket to Done. Only the receiver closes it. |

If the work is another application's share of the same Feature, there is no ask to raise: that product owner creates an Epic under the Feature, and you link the two Epics with **blocks** if one must finish first.

**When another team asks something of you**

| Step | What to do |
| --- | --- |
| Answer within five working days | Accept, propose another date, or decline with a reason, as a comment |
| Accept | Create or pick your own Epic or Story in your own project. Link it to the dependency ticket (**relates to**) and to the waiting Epic (**blocks**). Put the date you promise in Baseline End Date. Move the ticket to In Progress. |
| Plan | Give your ticket a Target PI and an end date before the need-by date |
| Deliver | Comment on the dependency ticket when it is ready |

**Every week, before the delivery sync (about ten minutes)**

- [ ] Each Epic in progress: is the status right? Move it if not.
- [ ] Each Epic in progress: is RAG still true? Change it today, not at the sync.
- [ ] Amber or Red: the recovery plan is written as a comment starting "Path to green:", with the date. (If your Epic screen has Path to Green and Date to Green fields, use those.)
- [ ] Any new dependency inside the Feature is linked with blocks; one from outside the Feature has an ask raised, and asks addressed to me are answered.
- [ ] Any Epic that will not finish in its PI has been raised with the product lead.
- [ ] No open Epic is without a Parent Link.

**How to choose RAG**

| Choose | When |
| --- | --- |
| Green | You expect to hit the date (End Date on an Epic) and need no help |
| Amber | The date is at risk and you have a plan. Write the plan down (see the weekly check above). |
| Red | You will miss the date unless someone outside the team does something. Say what and who. |

Raising Amber early is the right thing to do. Staying Green until the last week is the thing to avoid.

**When an Epic goes live**

| Field | What to put |
| --- | --- |
| Fix versions | The release, which the delivery lead then marks as released |
| Change Request ID | The change record |
| Status | Released |
| Actual PI | Set by automation when the Epic moves to Released. Check it is there. |

After early-life support, move the Epic to Done.

**If an Epic does not finish in its PI**

- Leave Target PI as it is. It is the record of the plan.
- Add a comment starting with the reason: Dependency, Capacity, Scope, Defect or Environment.
- It is planned first in the next PI.

## 5. If you are a business analyst or designer on a Feature

| When | Update |
| --- | --- |
| Analysis starts | Feature has Acceptance Criteria and Business Benefits in draft |
| Design is agreed | Link the Confluence design page on the Feature |
| Applications are identified | Ask each product owner to create their Epic under the Feature |
| A sign-off is needed | A task on the Feature, assigned to the approver, who closes it |
| Something in the design changes after Ready | Comment on the Feature and tell the product lead |

## 6. Who updates which field

| Field | On | Updated by | When |
| --- | --- | --- | --- |
| Status | Story, Task, Bug | The person doing the work | The day it changes |
| Flag | Any | The person who is stopped | Same day, on and off |
| Story Points | Story | Team | Refinement |
| Epic Link | Story, Task, Bug | Whoever creates it | At creation |
| Severity, Testing Phase, Environment | Bug | Whoever raises it | At creation |
| Status | Epic | Product owner | Weekly, or the day it changes |
| Parent Link | Epic | Product owner | At creation |
| Target PI, commitment label | Epic | Product owner | At PI planning only |
| RAG Status, End Date, recovery plan when Amber or Red | Epic | Product owner | Weekly |
| Story Points | Epic | Product owner, from the team | In analysis; revised when stories are estimated |
| Fix versions | Epic, Story, Bug | Product owner | Sprint planning |
| Change Request ID | Epic | Product owner | At release |
| Actual PI | Epic, Feature | Automation | At Released |
| Everything on a Feature | Feature | Product lead | Weekly |
| Everything on a VS Epic | VS Epic | Value stream lead | Fortnightly |
| A dependency ticket: need-by date (Due date), RAG, closing it | Delivery RAID | Product owner of the waiting team | When raised; weekly |
| A dependency ticket: the answer, the promised date (Baseline End Date), the link to their own work | Delivery RAID | Product owner of the supplying team | Within five working days of the ask |
| The RAID register, Milestones, release versions | | Delivery lead | Triage within two working days; at each review |
| `unplanned`, `pi-descoped` labels | Feature, Epic | Delivery lead | When a change is decided |

## 7. Common mistakes, and the fix

| Mistake | Why it matters | Do this instead |
| --- | --- | --- |
| Story has no Epic | It is not counted in any plan or progress figure | Set Epic Link when you create it |
| Epic has no parent Feature | The application's work disappears from the portfolio | Set Parent Link; ask the product lead if you do not know the Feature |
| "Blocked" written in a comment only | Nobody can find it | Use the flag |
| Flag left on after the block has gone | The blocked list becomes noise and is ignored | Remove it the same day |
| Everything In Progress at once | Hides what is really being worked on | Start less; finish first |
| Status updated in bulk on the last day of the sprint | Burndown and forecasts are wrong all sprint | Update daily |
| RAG kept Green to avoid questions | The problem surfaces too late to fix | Amber with a plan |
| Target PI changed after planning | Breaks the record of what was promised | Leave it; raise the change |
| Ticket deleted | History and audit trail are lost | Close with "Won't Do" |
| Done with no resolution | The ticket is missed by the reports | Use the normal Done transition |
| Severity and Priority used as the same thing | Release decisions are made on the wrong field | Severity = impact, Priority = order |
| New label invented | Filters miss it | Use only the agreed labels |

## 8. Where to ask

- A field or rule is unclear: your scrum master or product owner first, then the framework owner.
- The complete list of fields per issue type is in [FIELDS.md](FIELDS.md).
- Jira will not let you do something this guide says to do: the framework owner, with the ticket key and what you tried.
- You think a rule is wrong or wasteful: say so. Proposals go to the framework owner and are decided monthly.
