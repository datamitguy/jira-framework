# Building the dashboards in Jira Data Center

This guide builds the five dashboards from the framework, top-down: value stream portfolio, Features across the value stream, Epics across applications, risks dates and releases, and the team dashboard.

Nothing here has been run in your Jira. Menu names differ slightly between Jira versions; where yours differs, the idea is the same. All names in the examples are placeholders.

Time needed: about half a day for the filters, one to two hours per dashboard.

## The order to build in

1. Saved filters (a dashboard gadget shows what a saved filter returns).
2. Share the filters.
3. Dashboards and gadgets.
4. Share the dashboards.
5. Boards (optional, for the meetings).

Build with mock data first. The import template in `import/` creates a small set of VS Epics, Features, Epics and stories you can point the filters at.

## Step 1: Replace the placeholders

Write down your real values before you start. Every query in the framework uses these stand-ins.

| Placeholder | Meaning | Your value |
| --- | --- | --- |
| `CLP` | Key of the portfolio project (holds VS Epic, Feature, Milestone, Delivery RAID) | |
| `CA, DRAW, FL` | Keys of the application projects | |
| `PI 2027.1` | The current PI, written exactly as your Target PI field shows it | |
| `Red`, `Amber`, `Green` | Values of RAG Status | |
| `Risk`, `Dependency` | Values of RAID Type | |
| `CLP 2027.03` | A release (Fix Version) name | |

Check the field names too. Open one Feature, and compare each field name in the framework with what you see on screen, letter for letter: `Target PI`, `Actual PI`, `RAG Status`, `Parent Link`, `Enabler Type`, `Value Stream and Sub-Value Stream`, `Path to Green`.

## Step 2: Create the saved filters

For each filter:

1. Top menu: **Issues > Search for issues**.
2. If you see dropdowns instead of a text box, click **Advanced** to switch to the query box.
3. Paste the query, replace the placeholders, press Enter.
4. Check the result looks right. An error in red under the box usually means a field name or value does not match.
5. Click **Save as**, and give it the exact name from the framework (for example `VS: open VS Epics`). The names matter: other filters refer to them.
6. Click **Columns** (top right of the results) and tick the columns that dashboard needs, for example Key, Summary, Status, RAG Status, Due date, Target PI. Save the filter again so the columns are kept for the gadget.

Build them in this order, because later filters refer to earlier ones by name.

**A. Base filters (five)**

| Save as | Query |
| --- | --- |
| `PI 2027.1 planned Features` | `project = CLP AND issuetype = Feature AND "Target PI" = "PI 2027.1"` |
| `PI 2027.1 planned Epics` | `issuetype = Epic AND project in (CA, DRAW, FL) AND "Target PI" = "PI 2027.1"` |
| `VS: PI planned Features` | `filter = "PI 2027.1 planned Features"` |
| `VS: spillover` | `issuetype in (Feature, Epic) AND project in (CLP, CA, DRAW, FL) AND "Target PI" in ("PI 2026.3", "PI 2026.4") AND labels = pi-committed AND status not in (Released, Done)` |
| `VS: PI Epics` | `filter = "PI 2027.1 planned Epics" OR (filter = "VS: spillover" AND issuetype = Epic) OR (issuetype = Epic AND project in (CA, DRAW, FL) AND status = Implementing)` |

**B. VS Epic level**

| Save as | Query |
| --- | --- |
| `VS: open VS Epics` | `project = CLP AND issuetype = "VS Epic" AND status not in (Idea, Done) ORDER BY Rank` |
| `VS: Management Attention and Red` | `project = CLP AND issuetype in (Feature, "VS Epic") AND status not in (Released, Done) AND ("Management Attention" is not EMPTY OR "RAG Status" = Red)` |
| `VS: intake waiting` | `project = CLP AND issuetype in (Feature, "VS Epic") AND status = Idea ORDER BY created` |

**C. Feature level**

| Save as | Query |
| --- | --- |
| `VS: all Features` | `project = CLP AND issuetype = Feature` |
| `VS: current PI Features` | `filter = "VS: PI planned Features" OR (project = CLP AND issuetype = Feature AND status in (Implementing, Testing, Validation))` |
| `VS: committed Features` | `filter = "VS: PI planned Features" AND labels = pi-committed` |
| `VS: unplanned in PI` | `filter = "VS: PI planned Features" AND labels = unplanned` |
| `VS: Red and Amber` | `(filter = "VS: current PI Features" OR filter = "VS: PI Epics" OR filter = "VS: open VS Epics") AND "RAG Status" in (Red, Amber) AND status not in (Released, Done)` |
| `VS: Red and Amber Features` | `filter = "VS: Red and Amber" AND issuetype = Feature` |
| `VS: Ready, no Target PI` | `project = CLP AND issuetype = Feature AND status = Ready AND "Target PI" is EMPTY ORDER BY "Weighted Shortest Job First Score" DESC` |
| `VS: Analysis over 30 days` | `project = CLP AND issuetype = Feature AND status = Analysis AND NOT status changed AFTER -30d` |
| `VS: regulatory Features` | `project = CLP AND issuetype = Feature AND "Regulatory or Control Change Type" is not EMPTY AND status not in (Released, Done) ORDER BY duedate` |
| `VS: Features with gaps` | `project = CLP AND issuetype = Feature AND status not in (Idea, Analysis, Done) AND ("Parent Link" is EMPTY OR "Enabler Type" is EMPTY OR "RAG Status" is EMPTY OR "Value Stream and Sub-Value Stream" is EMPTY)` |

**D. Epic level**

| Save as | Query |
| --- | --- |
| `VS: PI Epics not started` | `filter = "VS: PI Epics" AND status in (Idea, Analysis, Ready)` |
| `VS: open blockers` | `(filter = "VS: current PI Features" OR filter = "VS: PI Epics") AND issueLinkType = blocks AND status not in (Released, Done) ORDER BY duedate` |
| `VS: flagged` | `(project = CLP OR filter = "VS: PI Epics") AND Flagged = Impediment` |
| `VS: Amber or Red without a plan` | `filter = "VS: Red and Amber" AND "Path to Green" is EMPTY` |
| `VS: hygiene exceptions` | `project in (CA, DRAW, FL) AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` |

**E. Risks, dates, releases**

| Save as | Query |
| --- | --- |
| `VS: open RAID` | `project = CLP AND issuetype = "Delivery RAID" AND statusCategory != Done` |
| `VS: open Red and Amber RAID` | `filter = "VS: open RAID" AND "RAG Status" in (Red, Amber) ORDER BY duedate` |
| `VS: cross-stream dependencies` | `filter = "VS: open RAID" AND "RAID Type" = Dependency ORDER BY duedate` |
| `VS: risks not reviewed` | `filter = "VS: open RAID" AND "RAID Type" = Risk AND "ROAM Response" is EMPTY` |
| `VS: RAID past its date` | `filter = "VS: open RAID" AND duedate < now()` |
| `VS: Milestones next 90 days and overdue` | `project = CLP AND issuetype = Milestone AND statusCategory != Done AND duedate <= endOfDay("+90d") ORDER BY duedate` |
| `Release: scope` | `fixVersion = "CLP 2027.03"` |
| `Release: open bugs` | `fixVersion = "CLP 2027.03" AND issuetype = Bug AND statusCategory != Done` |

**F. Team (one set per application project; `DRAW` is the example)**

| Save as | Query |
| --- | --- |
| `Team DRAW: flagged in sprint` | `project = DRAW AND sprint in openSprints() AND Flagged = Impediment` |
| `Team DRAW: carried over` | `project = DRAW AND sprint in openSprints() AND sprint in closedSprints() AND statusCategory != Done` |
| `Team DRAW: open Epics` | `project = DRAW AND issuetype = Epic AND statusCategory != Done` |
| `Team DRAW: Epics blocked by others` | `project = DRAW AND issuetype = Epic AND issueLinkType = "is blocked by" AND statusCategory != Done` |
| `Team DRAW: open bugs` | `project = DRAW AND issuetype = Bug AND statusCategory != Done` |
| `Team DRAW: Epics without Feature` | `project = DRAW AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` |

If a query fails, the usual causes are, in order: a field name that differs by a letter; a value that differs (for example `Amber` against `AMBER`); a field that is not on that issue type; `Flagged` not existing yet because nobody has ever flagged an issue.

## Step 3: Share the filters

A gadget is blank for anyone who cannot see its filter.

1. **Issues > Manage filters > My**.
2. For each filter: the **...** menu > **Edit**.
3. Under **Viewers**, add the group for the value stream (or the projects). Save.

Do this for every filter, including the base filters that other filters refer to.

## Step 4: Create a dashboard

1. Top menu: **Dashboards > Manage dashboards > Create new dashboard**.
2. Name it, for example `CLP 1 Value stream portfolio`. Numbering the names keeps them in order.
3. Under **Viewers**, add the same group. Save.
4. Open the dashboard. Click **Edit layout** and choose two columns.
5. Click **Add gadget**. If the list is short, click **Load all gadgets**.

A dashboard holds 20 gadgets by default. Each design below uses 10 or fewer.

## Step 5: Add and configure gadgets

Three gadgets do most of the work.

**Filter Results** (a list)

1. Add gadget > search `Filter Results` > Add.
2. **Saved filter**: type the filter name and pick it.
3. **Number of results**: 10 to 20.
4. **Columns to display**: pick the fields named in the dashboard table.
5. **Auto refresh**: every 15 minutes. Save.
6. Click the gadget's title > **Rename**, and give it the question it answers.

**Two Dimensional Filter Statistics** (a count table)

1. Add gadget > `Two Dimensional Filter Statistics`.
2. **Saved filter**: pick the filter.
3. **X axis** and **Y axis**: the two fields named in the dashboard table, for example Y = Project, X = Status.
4. **Sort by**: Natural. **Number of results**: 20. Save.

This gadget accepts dropdown fields, project, status, assignee, labels and versions. It does not accept text, number or date fields. A two-step dropdown (such as Value Stream and Sub-Value Stream, if that is how yours is built) may not be offered; if it is missing from the list, use the Confluence portfolio pages for that split.

**Pie Chart** (shares)

1. Add gadget > `Pie Chart`.
2. **Saved filter**, then **Statistic type**: the field to split by, for example RAG Status. Save.

Other gadgets used: **Created vs Resolved Chart** (filter, period, days back), **Sprint Health** and **Sprint Burndown** (pick the team's board).

## Step 6: The five dashboards

Build each from its table. "2D" means Two Dimensional Filter Statistics.

**1. Value stream portfolio**

| Gadget | Filter | Settings |
| --- | --- | --- |
| Filter Results | VS: open VS Epics | Columns: Key, Summary, Status, RAG Status, Due date, Executive Summary |
| Pie Chart | VS: open VS Epics | Statistic: RAG Status |
| 2D | VS: open VS Epics | Y = Status, X = RAG Status |
| Filter Results | VS: Management Attention and Red | Columns: Key, Summary, Issue Type, Path to Green, Date to Green |
| Filter Results | VS: Milestones next 90 days and overdue | Columns: Key, Summary, Due date, Baseline End Date, RAG Status |
| 2D | VS: open RAID | Y = RAID Type, X = RAG Status |
| Filter Results | VS: intake waiting | Columns: Key, Summary, Created, Reporter |
| Created vs Resolved | VS: all Features | Period: Monthly, 180 days |

**2. Features across the value stream**

| Gadget | Filter | Settings |
| --- | --- | --- |
| Filter Results | VS: current PI Features | Columns: Key, Summary, Parent Link, sub value stream, Status, RAG Status, Target PI, Due date |
| 2D | VS: current PI Features | Y = Status, X = RAG Status |
| Pie Chart | VS: committed Features | Statistic: Status |
| 2D | VS: current PI Features | Y = Enabler Type, X = Status |
| Filter Results | VS: Red and Amber Features | Columns: Key, Summary, RAG Status, Path to Green, Date to Green |
| Filter Results | VS: Ready, no Target PI | Columns: Key, Summary, Weighted Shortest Job First Score, T-Shirt Size |
| Filter Results | VS: Analysis over 30 days | Columns: Key, Summary, Assignee, Updated |
| Filter Results | VS: regulatory Features | Columns: Key, Summary, Due date, Regulatory or Control ID |
| Filter Results | VS: unplanned in PI | Columns: Key, Summary, Status |
| Filter Results | VS: Features with gaps | Columns: Key, Summary, Assignee |

**3. Epics across applications**

| Gadget | Filter | Settings |
| --- | --- | --- |
| 2D | VS: PI Epics | Y = Project, X = Status |
| 2D | VS: PI Epics | Y = Project, X = RAG Status |
| 2D | VS: spillover | Y = Project, X = Target PI |
| Filter Results | VS: PI Epics not started | Columns: Key, Summary, Project, Parent Link, Due date |
| Filter Results | VS: open blockers | Columns: Key, Summary, Project, Status, Due date, Linked issues |
| Filter Results | VS: flagged | Columns: Key, Summary, Project, Assignee |
| Filter Results | VS: Amber or Red without a plan | Columns: Key, Summary, RAG Status, Assignee |
| Filter Results | VS: hygiene exceptions | Columns: Key, Summary, Project, Assignee |

**4. Risks, dates and releases**

| Gadget | Filter | Settings |
| --- | --- | --- |
| Filter Results | VS: open Red and Amber RAID | Columns: Key, Summary, RAID Type, RAG Status, ROAM Response, Due date |
| Filter Results | VS: cross-stream dependencies | Columns: Key, Summary, sub value stream, Supplier Value Stream and Sub Value Stream, Due date |
| Filter Results | VS: risks not reviewed | Columns: Key, Summary, Assignee |
| Filter Results | VS: RAID past its date | Columns: Key, Summary, RAID Type, Due date |
| Filter Results | VS: Milestones next 90 days and overdue | Columns: Key, Summary, Baseline End Date, Due date, RAG Status |
| 2D | Release: scope | Y = Project, X = Status |
| Pie Chart | Release: open bugs | Statistic: Priority |

**5. Team** (copy per team)

| Gadget | Filter or source | Settings |
| --- | --- | --- |
| Sprint Health | Team board | Active sprint |
| Sprint Burndown | Team board | Active sprint |
| Filter Results | Team: flagged in sprint | Columns: Key, Summary, Assignee |
| Filter Results | Team: carried over | Columns: Key, Summary, Sprint |
| 2D | Team: open Epics | Y = Status, X = Fix Version |
| Filter Results | Team: Epics blocked by others | Columns: Key, Summary, Linked issues |
| Pie Chart | Team: open bugs | Statistic: Priority |
| Filter Results | Team: Epics without Feature | Columns: Key, Summary |

To make the team dashboard for a second team: **Dashboards > Manage dashboards**, find the first one, **...** > **Copy dashboard**, then point each gadget at that team's filters.

## Step 6b: Dashboard 6, Dependencies

Added on 27 November 2026. For delivery leads and product owners; it opens the weekly delivery sync. The method behind it is section 12 of the white paper.

Create these filters first (they build on `VS: open RAID`):

| Save as | Query |
| --- | --- |
| VS: open dependencies | `filter = "VS: open RAID" AND "RAID Type" = Dependency ORDER BY duedate` |
| VS: dependencies not agreed | `filter = "VS: open dependencies" AND status = Backlog ORDER BY duedate` |
| VS: dependencies agreed | `filter = "VS: open dependencies" AND status = "In Progress"` |
| VS: dependencies late or due soon | `filter = "VS: open dependencies" AND duedate <= endOfDay("+28d") ORDER BY duedate` |
| VS: dependencies at risk | `filter = "VS: open dependencies" AND "RAG Status" in (Amber, Red)` |
| VS: dependencies without an owner or date | `filter = "VS: open dependencies" AND (assignee is EMPTY OR duedate is EMPTY)` |

| Gadget | Filter | Settings |
| --- | --- | --- |
| Filter Results | VS: dependencies not agreed | Columns: Key, Summary, Linked Issues, Supplier Value Stream and Sub Value Stream, Assignee, Due date, Created |
| Two Dimensional Filter Statistics | VS: open dependencies | X axis Status, Y axis Supplier Value Stream and Sub Value Stream |
| Two Dimensional Filter Statistics | VS: open dependencies | X axis RAG Status, Y axis Value Stream and Sub-Value Stream |
| Filter Results | VS: dependencies late or due soon | Columns: Key, Summary, Due date, Baseline End Date, RAG Status, Assignee |
| Filter Results | VS: flagged | Columns: Key, Summary, Project, Assignee, Updated |
| Filter Results | VS: dependencies at risk | Columns: Key, Summary, RAG Status, Path to Green, Due date |
| Filter Results | VS: dependencies without an owner or date | Columns: Key, Summary, Reporter |

If a two-step dropdown is refused as a gadget axis, use recipe 4.16 in the Confluence guide for those two panels.

**A change to how Plans is used.** Plans is now used for the L0 roadmap only. The PI plan, capacity and the dependency board are Confluence pages (recipes 4.14 to 4.16 in the Confluence guide), and there is a Confluence page for each role (recipe 4.17). Where this guide mentions a plan view other than the roadmap, use those pages.

## Step 7: Two boards for the meetings

**Feature board** (one for the whole value stream)

1. **Boards > View all boards > Create board > Kanban > Board from an existing saved filter**.
2. Filter: `VS: all Features` (add `AND status != Done` if it gets long).
3. **Board settings > Columns**: map each Feature status to its own column.
4. **Swimlanes**: base on **Queries**; add one query per VS Epic: `"Parent Link" = CLP-12`, named after the VS Epic.
5. **Card colours**: base on **Queries**: red for `"RAG Status" = Red`, amber for `"RAG Status" = Amber`, green for `"RAG Status" = Green`. The first matching query wins, so put Red first.
6. **Quick filters**: `Current PI` = `"Target PI" = "PI 2027.1"`; `Committed` = `labels = pi-committed`; `Red and Amber` = `"RAG Status" in (Red, Amber)`; `Flagged` = `Flagged = Impediment`.

**VS Epic board**: the same, with filter `project = CLP AND issuetype = "VS Epic"`, columns as the VS Epic statuses, and a maximum set on the Analysis and Implementing columns (**Columns > Max**) for the work-in-progress limit.

## Step 8: At each PI change

1. Create `PI <new> planned Features` and `PI <new> planned Epics`.
2. Edit `VS: PI planned Features` and the first part of `VS: PI Epics` to name the new ones.
3. Add the PI that has just ended to the list in `VS: spillover`.
4. Edit the PI value in automation rule 4 and in the board quick filter.

Nothing else changes. Old per-PI filters are never edited, because old PI scorecards in Confluence read them.

## Checks before you show anyone

- [ ] Every gadget shows data when you are logged in as a colleague, not only as yourself.
- [ ] Each 2D gadget offered the fields you wanted. Note any that were missing.
- [ ] `VS: open blockers` shows tickets that block others. It cannot tell whether the ticket on the other end is still waiting, so treat it as a list to check.
- [ ] `VS: spillover` is empty on mock data until you set an older Target PI on a committed, unfinished ticket. Do that once to see it work.
