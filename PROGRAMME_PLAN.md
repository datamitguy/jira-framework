# Jira unification: programme plan

Two parts: what is still needed to communicate and land the change, and how to break the work into chunks that can each be finished and shown.

The documents so far describe the design. This page is about getting people to use it. Durations are estimates to adjust, not commitments.

## Part 1: What is still missing to communicate the project

The framework explains *how*. Nothing yet explains *why now*, *what changes for me*, or *who decided*. Those three are what people ask first.

### The communication kit

| # | Item | For whom | What it says | Length | Have it? |
| --- | --- | --- | --- | --- | --- |
| 1 | The case for change | Sponsors, leads | The problem in their terms (nobody can see an initiative across applications; plans are made per app; dates slip without warning), what unifying Jira fixes, and what it costs teams | One page | No |
| 2 | Sponsor message | Everyone | A short note from the most senior sponsor: this is how we work from date X, and why | Half a page | No |
| 3 | What changes for you, by role | Each role | Before and after, in a table: what I stop doing, start doing, keep doing | One page per role | Partly, in JIRA_UPDATE_GUIDE.md |
| 4 | One-page picture | Everyone | The line VS Epic > Feature > Epic > Story with one real example from your platform | One slide | The diagram exists; needs a real example |
| 5 | Timeline | Everyone | The chunks below, with dates, and when each team is affected | One slide | Draft in Part 2 |
| 6 | Decision record | Leads, auditors | What was decided, by whom, when: hierarchy, field meanings, RAG rules, commitment rules | One page, kept current | No |
| 7 | Glossary | Everyone | Twenty terms at most: VS Epic, Feature, Epic, PI, Target PI, Actual PI, spillover, committed, stretch, RAG, RAID, DDT | One page | No |
| 8 | Questions and answers | Everyone | The awkward questions answered plainly (list below) | Two pages | No |
| 9 | Quick reference card | Working level | The one-minute card from the update guide | Half a page | Yes |
| 10 | Training | By role | Three short sessions: working level (30 min), product owners (60 min), leads (90 min), each ending in a hands-on exercise with the mock data | Slides plus exercise | No |
| 11 | Pilot results | Sponsors, sceptics | What the pilot showed: one cross-application view that did not exist before, and what was changed after feedback | One page | After chunk 1 |
| 12 | Where to get help | Everyone | The framework owner, a chat channel, weekly office hours for the first two PIs | A few lines | No |

### The questions people will ask

Write the answers before the first briefing. If an answer is "not decided yet", say so and give the date it will be.

1. Why are we doing this, and why now?
2. Is this more admin for my team? How many minutes a week?
3. Do we have to re-enter our existing Epics? (No: they are stitched upward.)
4. Who decides which Feature my Epic belongs to?
5. What if my Epic does not fit any Feature?
6. Will my team be compared with others on story points or predictability? (No.)
7. What happens if we miss a committed Epic?
8. Is RAG going to be used against me?
9. We already have our own board and labels. Do we lose them?
10. How does this relate to the DDT?
11. What changes when we move to Jira Cloud? Will we do this twice?
12. Who do I tell if a rule does not work for my team?

### The people side

| Need | What to set up |
| --- | --- |
| A sponsor who is seen to back it | One senior name on the message, present at the first PI planning, and using the dashboard in their own meetings |
| A named framework owner | One person with time set aside, not a committee |
| Champions | One person in each sub value stream who knows the rules well and is the first place colleagues ask |
| A stakeholder map | Who must agree (sponsors, product leads, delivery leads), who must be consulted (Jira admin, architecture, risk and control, audit, the DDT owner, the Cloud migration team), who must be told (teams) |
| A feedback route | One place to raise problems, reviewed monthly, with what was changed published |
| Leaders using it | The fastest way to make the data good is for leaders to run their meetings from the dashboards. The fastest way to kill it is to keep asking for slides. |

### Other things not yet in place

| Gap | Why it matters | Suggested owner |
| --- | --- | --- |
| Agreement from the Jira admin team, in writing, on the six requests | Four of them block the start | Framework owner |
| Agreement with the owner of the bank's Jira standards on Target PI, Actual PI and RAG meanings | The framework assumes meanings the standards may define differently | Framework owner |
| Agreement with the DDT owner on the hand-off point | Otherwise there are two front doors again | Value stream lead |
| A check with risk, control or audit on evidence | Sign-offs as tasks, and public or external storage of these documents, may be covered by policy | Delivery lead |
| A baseline of today | Without "before" numbers (how many Epics have no parent, how many initiatives span applications, how long status reporting takes) you cannot show improvement | Framework owner |
| Success measures for the project itself | See below | Sponsor |
| A line to the Cloud migration team | So this work and theirs do not undo each other | Framework owner |
| A budget of people's time | Stitching and the first PI planning take real hours from product owners | Sponsor |

### How to know the project is working

| Measure | At the start | Target after two PIs |
| --- | --- | --- |
| Epics with a parent Feature | Count it now | Above 95% |
| Features with a parent VS Epic | Count it now | 100% |
| In-progress Features and Epics with RAG refreshed in the last two weeks | Count it now | Above 90% |
| Portfolio sync run from the dashboard with no separate slide pack | No | Yes |
| Time spent each month assembling status reports | Ask the delivery leads | Halved |
| A cross-application dependency found at planning instead of during the PI | Count from the first PI | Rising |
| Teams saying the weekly update takes under ten minutes | Survey | Most |

## Part 2: Breaking the work into chunks

### A note on putting Cloud migration second

It makes sense as the second chunk, with one caution. The migration date is set by the central Jira team, not by this project, so treat it as a fixed event to plan around and not as work you control.

That shapes the first chunk: do the things that survive the move unchanged, and keep the things that must be redone to a minimum.

| Survives the move unchanged | Needs rework after the move |
| --- | --- |
| The hierarchy and the stitched parents | Saved filters that use Parent Link or Epic Link (rewritten with the single parent field) |
| Field meanings, RAG rules, commitment rules | Automation rules (re-tested) |
| Labels | The plan, its teams and saved views (may need rebuilding) |
| Ways of working, rhythm, decision rights | Confluence pages (re-tested against the Cloud editions of the add-ons) |
| PI scorecards pasted as tables | Dashboards (re-pointed at the rewritten filters) |
| People's habits | |

So before the migration, build the full set of rules and habits but only the minimum of Jira and Confluence machinery: the base filters, three dashboards and three Confluence pages. Build the rest once, on Cloud.

One question to settle early with the migration team: on Jira Cloud, levels above Epic and Plans need the Premium plan. If the bank's Cloud site is on a lower plan, VS Epic and Feature lose their place in the hierarchy and this design needs a different join.

### The chunks

| # | Chunk | Goal | Rough length |
| --- | --- | --- | --- |
| 0 | Mobilise | Agreement, owner, admin requests raised, baseline counted | 3 to 4 weeks |
| 1 | Foundation on Data Center | One sub value stream stitched and run through one PI with the minimum build | 1 PI |
| 2 | Cloud migration | Arrive on Cloud with the hierarchy, fields and habits intact | Set by the migration team |
| 3 | Scale across the value stream | Every sub value stream on the line; full dashboards and Confluence portfolio | 1 to 2 PIs |
| 4 | Portfolio management | Limits on work in progress, cases on VS Epics, benefits reviews, forecasting | 1 to 2 PIs |
| 5 | Run and improve | The framework is owned, measured and changed like any other product | Ongoing |

### Chunk 0: Mobilise

| Work | Done when |
| --- | --- |
| Name the sponsor, the framework owner and the pilot sub value stream | Names are written down and agreed |
| Complete the nine checks at the top of FRAMEWORK.md | Each is ticked or has an owner and date |
| Raise admin requests 1 to 4 | Each has a ticket and a date from the admin team |
| Agree field meanings with the standards owner and the hand-off with the DDT owner | Written into the decision record |
| Count the baseline | Numbers recorded for the measures in Part 1 |
| Write the case for change, sponsor message, glossary and questions and answers | Reviewed by two people who were not involved |
| Meet the Cloud migration team | You know their date, their licence tier, and what they will and will not carry over |
| Try the mock data | The import, three dashboards and three Confluence recipes work in a test project |

### Chunk 1: Foundation on Data Center

| Work | Done when |
| --- | --- |
| Stitch the pilot sub value stream's Epics to Features and VS Epics | No Epic in the pilot is without a parent |
| Brief the pilot teams by role | Each role has had its session and the update guide |
| Build the minimum: base filters, dashboards 1 to 3, Confluence pages for the portfolio tree, Feature progress and the PI scorecard | A lead can answer "what are we delivering and where is it" from them |
| Run the weekly delivery sync and fortnightly portfolio sync from the dashboards | Four in a row with tickets updated in the room |
| Run one PI planning by the rules, lock it, and paste the baseline | The scorecard page exists with its baseline table |
| Run the PI, then score it and hold the review | Three predictability figures and a spillover list with reasons |
| Collect what did not work | A list of changes, each decided, in the change log |
| Stitch the other sub value streams' Epics in the background | Ready for chunk 3, even if those teams have not changed how they work yet |

Do not build in this chunk: the full filter library, automation beyond rules 3 to 6, the forecast and velocity pages, limits on work in progress.

### Chunk 2: Cloud migration

Your part is readiness and re-pointing, not the migration itself.

| Work | Done when |
| --- | --- |
| Give the migration team a list of what must survive: issue types, hierarchy levels, the custom fields the framework uses, link types, labels, the portfolio project | They confirm each in writing |
| Confirm the licence tier supports levels above Epic and Plans | Confirmed, or an alternative join is designed |
| Export what may not carry over: the list of filters with their queries, plan settings, dashboard layouts, automation rules | Stored in this repository |
| Agree a freeze: no PI planning and no structural change in the weeks around cut-over | Dates in the calendar; ideally cut-over falls in a planning sprint |
| After cut-over: check the hierarchy on ten tickets, rewrite the filters, rebuild the plan, re-point dashboards, re-test Confluence pages and automation | The chunk 1 views work again, and one weekly sync has been run on Cloud |
| Write the Cloud edition of the build guides | Guides updated; Data Center versions archived |
| Tell teams what changed for them | A half-page note: what looks different, what is the same |

### Chunk 3: Scale across the value stream

| Work | Done when |
| --- | --- |
| Bring in the remaining sub value streams, one or two at a time, with a champion in each | Each has run a weekly sync and one PI planning by the rules |
| Build the full filter library, dashboards 4 and 5, and all Confluence portfolio pages | The twelve monthly questions can be answered from them |
| Build the L0 roadmap view and publish it | Sponsors use it in place of a slide |
| Add the remaining automation rules | Rule 1 tested and running |
| Run the first value stream wide PI planning | One plan, one lock, one scorecard |
| Publish the hygiene count per application monthly | Three months in a row |

### Chunk 4: Portfolio management

| Work | Done when |
| --- | --- |
| Outcome and case on every VS Epic | No VS Epic in Analysis or beyond without one |
| Limits on work in progress on the VS Epic board | Limits set and discussed at each portfolio sync |
| Capacity split agreed per team and compared with actuals | On each PI scorecard |
| Size and forecast per VS Epic | Confluence page live and checked against one finished VS Epic |
| Benefits reviews | First two released VS Epics reviewed and recorded |
| PI objectives scored by sponsors | One PI planned and reviewed with them |

### Chunk 5: Run and improve

| Work | Rhythm |
| --- | --- |
| Review feedback and proposals; decide changes; update the change log | Monthly |
| Review the project's own measures | Each PI |
| Onboard new applications and teams with the checklist | As needed |
| Retire fields, labels, filters and dashboards nobody uses | Twice a year |
| Refresh training for new joiners | Each PI |

### What depends on what

```text
Chunk 0 Mobilise
   └─> Chunk 1 Foundation on Data Center
          ├─> Chunk 2 Cloud migration   (date fixed by others; plan chunk 1 to end before it)
          │       └─> Chunk 3 Scale     (full build happens once, on Cloud)
          │               └─> Chunk 4 Portfolio management
          │                       └─> Chunk 5 Run and improve
          └─> stitching of the other sub value streams can run alongside chunks 1 and 2
```

If the migration date slips a long way, do not wait: start chunk 3 on Data Center with the next one or two sub value streams, and accept that their filters will be rewritten later. Habits are the slow part, and they carry over.

### Risks to the plan

| Risk | Sign | Response |
| --- | --- | --- |
| Admin requests are not delivered | No date after two weeks | Sponsor raises it; meanwhile set parents and fields from inside the plan |
| Product owners have no time for stitching | Sessions cancelled twice | Sponsor protects the time; do it in two half-days, not spread over weeks |
| Leaders keep asking for slides | A slide pack appears for the portfolio sync | Sponsor runs the next sync from the dashboard |
| The pilot is treated as optional | Tickets not updated between syncs | Champion and framework owner sit in two stand-ups; fix the friction |
| Migration lands mid-PI | Cut-over date inside sprints 1 to 5 | Ask for a move to a planning sprint, or freeze structure and accept a week of rework |
| Cloud licence does not support the hierarchy | Migration team cannot confirm Premium | Design the fallback join (issue links) before cut-over, not after |
| The framework grows | New fields and labels each month | The framework owner says no by default; retire as much as is added |
