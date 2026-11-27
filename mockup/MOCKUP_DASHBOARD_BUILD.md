# Building the dashboards and Confluence pages on the mock tickets

Step-by-step instructions for building every Jira dashboard and every Confluence page from the white paper, using the 38 mock tickets in [MOCKUP_GUIDE.md](MOCKUP_GUIDE.md). Each step says what you should see when it works.

Do the parts in order: A (Jira) first, then B (Confluence), because the Confluence pages read the Jira filters.

Nothing here has been run on your Jira or Confluence. Where a step does not behave as described, write down what happened in part C; that is the purpose of a mock-up.

**Three things differ from the white paper because everything is in one project:**

- The issue types are **Capability** (VS Epic) and **Initiative** (Feature).
- The application is the **Component**, not the project.
- A Milestone is a **Task** labelled `milestone`.

**Before you start:** the 38 tickets exist, with their parents, links, flags and sprint set (MOCKUP_GUIDE.md, sections 3 and 4).

---

# Part A: Jira

## A1. Create the saved filters (about 45 minutes)

For each row:

1. Top menu: **Issues > Search for issues**. If you see dropdowns and not a text box, click **Advanced**.
2. Paste the query. Press Enter.
3. Check the number of results against the last column.
4. **Save as**, with the exact name in the table. The names matter: later filters refer to earlier ones.

Create them in this order.

| # | Save as | Query | Results |
| --- | --- | --- | --- |
| 1 | `MOCK: all` | `project = CL123 AND labels = mock` | 38 |
| 2 | `MOCK PI planned Initiatives` | `filter = "MOCK: all" AND issuetype = Initiative AND "Target PI" = "PI 2026.4"` | 5 |
| 3 | `MOCK PI planned Epics` | `filter = "MOCK: all" AND issuetype = Epic AND "Target PI" = "PI 2026.4"` | 7 |
| 4 | `MOCK: spillover` | `filter = "MOCK: all" AND issuetype in (Initiative, Epic) AND "Target PI" in ("PI 2026.3") AND labels = pi-committed AND status not in (Released, Done)` | 2 |
| 5 | `MOCK: PI Epics` | `filter = "MOCK PI planned Epics" OR (filter = "MOCK: spillover" AND issuetype = Epic) OR (filter = "MOCK: all" AND issuetype = Epic AND status = Implementing)` | 9 |
| 6 | `MOCK: current PI Initiatives` | `filter = "MOCK PI planned Initiatives" OR (filter = "MOCK: all" AND issuetype = Initiative AND status in (Implementing, Testing, Validation))` | 6 |
| 7 | `MOCK: committed Initiatives` | `filter = "MOCK PI planned Initiatives" AND labels = pi-committed` | 4 |
| 8 | `MOCK: committed and released` | `filter = "MOCK: committed Initiatives" AND status in (Released, Done)` | 1 |
| 9 | `MOCK: unplanned in PI` | `filter = "MOCK PI planned Initiatives" AND labels = unplanned` | 1 |
| 10 | `MOCK: open Capabilities` | `filter = "MOCK: all" AND issuetype = Capability AND status not in (Idea, Done) ORDER BY Rank` | 3 |
| 11 | `MOCK: all Initiatives` | `filter = "MOCK: all" AND issuetype = Initiative` | 8 |
| 12 | `MOCK: Red and Amber` | `(filter = "MOCK: current PI Initiatives" OR filter = "MOCK: PI Epics" OR filter = "MOCK: open Capabilities") AND "RAG Status" in (Red, Amber) AND status not in (Released, Done)` | 8 |
| 13 | `MOCK: Management Attention and Red` | `filter = "MOCK: all" AND issuetype in (Initiative, Capability) AND status not in (Released, Done) AND ("Management Attention" is not EMPTY OR "RAG Status" = Red)` | 2 |
| 14 | `MOCK: Amber or Red without a plan` | `filter = "MOCK: Red and Amber" AND issuetype != Epic AND "Path to Green" is EMPTY` | 1 |
| 15 | `MOCK: intake waiting` | `filter = "MOCK: all" AND issuetype in (Initiative, Capability) AND status = Idea ORDER BY created` | 1 |
| 16 | `MOCK: Ready, no Target PI` | `filter = "MOCK: all" AND issuetype = Initiative AND status = Ready AND "Target PI" is EMPTY ORDER BY "Weighted Shortest Job First Score" DESC` | 1 |
| 17 | `MOCK: Initiatives with gaps` | `filter = "MOCK: all" AND issuetype = Initiative AND status not in (Idea, Analysis, Done) AND ("Parent Link" is EMPTY OR "RAG Status" is EMPTY OR "Value Stream and Sub-Value Stream" is EMPTY)` | 1 |
| 18 | `MOCK: regulatory Initiatives` | `filter = "MOCK: all" AND issuetype = Initiative AND "Regulatory or Control Change Type" is not EMPTY AND status not in (Released, Done)` | 1 |
| 19 | `MOCK: PI Epics not started` | `filter = "MOCK: PI Epics" AND status in (Idea, Analysis, Ready)` | 1 |
| 20 | `MOCK: flagged` | `filter = "MOCK: all" AND Flagged = Impediment` | 2 |
| 21 | `MOCK: hygiene exceptions` | `filter = "MOCK: all" AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done` | 1 |
| 22 | `MOCK: open RAID` | `filter = "MOCK: all" AND issuetype = "Delivery RAID" AND statusCategory != Done` | 8 |
| 23 | `MOCK: open Red and Amber RAID` | `filter = "MOCK: open RAID" AND "RAG Status" in (Red, Amber) ORDER BY duedate` | 5 |
| 24 | `MOCK: risks not reviewed` | `filter = "MOCK: open RAID" AND "RAID Type" = Risk AND "ROAM Response" is EMPTY` | 1 |
| 25 | `MOCK: RAID past its date` | `filter = "MOCK: open RAID" AND duedate < now()` | 2 |
| 26 | `MOCK: milestones next 90 days and overdue` | `filter = "MOCK: all" AND labels = milestone AND statusCategory != Done AND duedate <= endOfDay("+90d") ORDER BY duedate` | 2 |
| 27 | `MOCK: open dependencies` | `filter = "MOCK: open RAID" AND "RAID Type" = Dependency ORDER BY duedate` | 4 |
| 28 | `MOCK: dependencies not agreed` | `filter = "MOCK: open dependencies" AND status = Backlog ORDER BY duedate` | 2 |
| 29 | `MOCK: dependencies agreed` | `filter = "MOCK: open dependencies" AND status = "In Progress"` | 2 |
| 30 | `MOCK: dependencies late or due soon` | `filter = "MOCK: open dependencies" AND duedate <= endOfDay("+28d") ORDER BY duedate` | 3 |
| 31 | `MOCK: dependencies at risk` | `filter = "MOCK: open dependencies" AND "RAG Status" in (Amber, Red)` | 3 |
| 32 | `MOCK: dependencies without an owner or date` | `filter = "MOCK: open dependencies" AND (assignee is EMPTY OR duedate is EMPTY)` | 1 |
| 33 | `MOCK release: scope` | `filter = "MOCK: all" AND fixVersion = "CL123 2027.01"` | 5 |
| 34 | `MOCK release: not finished` | `filter = "MOCK: all" AND fixVersion = "CL123 2027.01" AND status not in (Released, Done)` | 3 |
| 35 | `MOCK release: open bugs` | `filter = "MOCK: all" AND fixVersion = "CL123 2027.01" AND issuetype = Bug AND statusCategory != Done` | 1 |
| 36 | `MOCK team: flagged in sprint` | `filter = "MOCK: all" AND sprint in openSprints() AND Flagged = Impediment` | 1 |
| 37 | `MOCK team: open Epics` | `filter = "MOCK: all" AND issuetype = Epic AND status not in (Released, Done)` | 7 |
| 38 | `MOCK team: open bugs` | `filter = "MOCK: all" AND issuetype = Bug AND statusCategory != Done` | 1 |
| 39 | `MOCK team: Stories without Epic` | `filter = "MOCK: all" AND issuetype = Story AND "Epic Link" is EMPTY AND statusCategory != Done` | 1 |

If a query shows a red error, the usual causes are: a field name that differs by a letter; a value that differs (for example `AMBER` for `Amber`); a field that is not on that issue type; or `Flagged` not being known until at least one ticket has been flagged.

If the count is wrong but there is no error, open the Expected results sheet of the workbook, see which ticket is missing or extra, and compare its fields with the ticket list.

## A2. Share the filters

A gadget shows nothing to a person who cannot see its filter.

1. **Issues > Manage filters > My**.
2. For each MOCK filter: **... > Edit**, and under **Viewers** add the group or project you will show the dashboards to. Save.

## A3. Set the columns once

Open `MOCK: all`, click **Columns**, and tick: Key, Issue Type, Summary, Status, RAG Status, Due date, Target PI, Component/s, Parent Link, Linked Issues, Assignee. The Filter Results gadgets below can then show any of them.

## A4. How to make a dashboard and add a gadget

1. **Dashboards > Create dashboard**. Name it as below. Share it with the same group as the filters.
2. **Add gadget**. If the list is short, click **Load all gadgets**.
3. Find the gadget by name, **Add gadget**, then fill in its settings:
   - **Filter Results**: Saved filter; Number of results (10); Columns to display.
   - **Two Dimensional Filter Statistics** ("2D" below): Saved filter; X axis; Y axis.
   - **Pie Chart**: Saved filter; Statistic type.
4. **Save** the gadget. Drag it into place.

## A5. The six dashboards

### MOCK 1: Value stream portfolio

| # | Gadget | Filter | Settings | You should see |
| --- | --- | --- | --- | --- |
| 1 | Filter Results | MOCK: open Capabilities | Columns: Key, Summary, Status, RAG Status, Due date | 3: C1, C2, C3 |
| 2 | Pie Chart | MOCK: open Capabilities | Statistic type: RAG Status | Three equal slices: Green, Amber, Red |
| 3 | 2D | MOCK: open Capabilities | X axis: RAG Status. Y axis: Status. | Implementing: Amber 1, Red 1. Analysis: Green 1. |
| 4 | Filter Results | MOCK: Management Attention and Red | Columns: Key, Issue Type, Summary, RAG Status, Path to Green | 2: C2, I3 |
| 5 | Filter Results | MOCK: milestones next 90 days and overdue | Columns: Key, Summary, Due date, RAG Status | 2: M1, M2. M2 is overdue. |
| 6 | 2D | MOCK: open RAID | X axis: RAG Status. Y axis: RAID Type. | Dependency: Green 1, Amber 2, Red 1. Risk: Green 1, Amber 1. Issue: Red 1. Assumption: Green 1. |
| 7 | Filter Results | MOCK: intake waiting | Columns: Key, Summary, Created | 1: I6 |
| 8 | Created vs Resolved Chart | MOCK: all Initiatives | Period: Daily. Days previously: 30. | One step up on the day you created the tickets. It becomes useful only with history. |

### MOCK 2: Initiatives across the value stream

| # | Gadget | Filter | Settings | You should see |
| --- | --- | --- | --- | --- |
| 1 | Filter Results | MOCK: current PI Initiatives | Columns: Key, Summary, Parent Link, Value Stream and Sub-Value Stream, RAG Status, Target PI, Due date | 6: I1, I2, I3, I4, I5, I7 |
| 2 | 2D | MOCK: current PI Initiatives | X axis: RAG Status. Y axis: Status. | Implementing: Green 2, Amber 2, Red 1. Released: Green 1. |
| 3 | Pie Chart | MOCK: committed Initiatives | Statistic type: Status | Implementing 3, Released 1 |
| 4 | Filter Results | MOCK: Red and Amber | Columns: Key, Issue Type, Summary, RAG Status, Path to Green | 8: C1, C2, I1, I3, I7, E2, E4, E7 |
| 5 | Filter Results | MOCK: Ready, no Target PI | Columns: Key, Summary, Weighted Shortest Job First Score | 1: I8 |
| 6 | Filter Results | MOCK: regulatory Initiatives | Columns: Key, Summary, Due date | 1: I1 |
| 7 | Filter Results | MOCK: unplanned in PI | Columns: Key, Summary | 1: I5 |
| 8 | Filter Results | MOCK: Initiatives with gaps | Columns: Key, Summary | 1: I5 |
| 9 | 2D | MOCK: current PI Initiatives | X axis: RAG Status. Y axis: Value Stream and Sub-Value Stream. | Governance and Conditions: Green 1, Amber 1. Monitoring: Red 1. Drawdown: Green 1, Amber 1. None: Green 1. **If the gadget refuses this field, note it (check 4).** |

### MOCK 3: Epics across applications

| # | Gadget | Filter | Settings | You should see |
| --- | --- | --- | --- | --- |
| 1 | 2D | MOCK: PI Epics | X axis: Status. Y axis: Component. | Credit Application: Released 1, Implementing 2. Drawdowns: Implementing 2, Ready 1. Governance and Conditions: Released 1, Implementing 2. |
| 2 | 2D | MOCK: PI Epics | X axis: RAG Status. Y axis: Component. | Credit Application: Green 2, Amber 1. Drawdowns: Green 2, Amber 1. Governance and Conditions: Green 2, Red 1. |
| 3 | 2D | MOCK: spillover | X axis: Target PI. Y axis: Issue Type. | Initiative 1 and Epic 1, both under the previous PI |
| 4 | Filter Results | MOCK: PI Epics not started | Columns: Key, Summary, Component/s, Parent Link, End Date | 1: E5 |
| 5 | Filter Results | MOCK: flagged | Columns: Key, Issue Type, Summary, Assignee | 2: E4, S1 |
| 6 | Filter Results | MOCK: Amber or Red without a plan | Columns: Key, Summary, RAG Status, Assignee | 1: I3 |
| 7 | Filter Results | MOCK: hygiene exceptions | Columns: Key, Summary, Component/s | 1: E8 |

### MOCK 4: Risks, dates and releases

| # | Gadget | Filter | Settings | You should see |
| --- | --- | --- | --- | --- |
| 1 | Filter Results | MOCK: open Red and Amber RAID | Columns: Key, Summary, RAID Type, RAG Status, ROAM Response, Due date | 5: R1, R2, R4, R5, R7 |
| 2 | Filter Results | MOCK: risks not reviewed | Columns: Key, Summary, Assignee | 1: R6 |
| 3 | Filter Results | MOCK: RAID past its date | Columns: Key, Summary, RAID Type, Due date | 2: R4, R6 |
| 4 | 2D | MOCK: open RAID | X axis: Impact. Y axis: Probability. | Only the two risks have a Probability: High and High 1; Low and High 1 |
| 5 | Filter Results | MOCK: milestones next 90 days and overdue | Columns: Key, Summary, Due date, RAG Status, Linked Issues | 2: M1, M2 |
| 6 | 2D | MOCK release: scope | X axis: Status. Y axis: Component. | Credit Application: Released 1. Drawdowns: Implementing 1, In Progress 2, Done 1. |
| 7 | Filter Results | MOCK release: not finished | Columns: Key, Issue Type, Summary, Status | 3: E2, S1, B1 |
| 8 | Pie Chart | MOCK release: open bugs | Statistic type: Severity (or Priority) | One bug, B1 |

### MOCK 5: Team

Needs the board and the running sprint `PI 2026.4 S3 mock`.

| # | Gadget | Source | Settings | You should see |
| --- | --- | --- | --- | --- |
| 1 | Sprint Health Gadget | The board | Sprint: next sprint due | 6 tickets: 2 Done, 3 In Progress, 1 to do |
| 2 | Sprint Burndown Gadget | The board | The same sprint | A line starting at 26 story points |
| 3 | Filter Results | MOCK team: flagged in sprint | Columns: Key, Summary, Assignee | 1: S1 |
| 4 | 2D | MOCK team: open Epics | X axis: Fix Version. Y axis: Status. | Implementing 6 (one in the release, five with no version), Ready 1 |
| 5 | Pie Chart | MOCK team: open bugs | Statistic type: Severity (or Priority) | One bug, B1 |
| 6 | Filter Results | MOCK: hygiene exceptions | Columns: Key, Summary | 1: E8 |
| 7 | Filter Results | MOCK team: Stories without Epic | Columns: Key, Summary | 1: S5 |

### MOCK 6: Dependencies

| # | Gadget | Filter | Settings | You should see |
| --- | --- | --- | --- | --- |
| 1 | Filter Results | MOCK: dependencies not agreed | Columns: Key, Summary, Linked Issues, Supplier Value Stream and Sub Value Stream, Assignee, Due date, Created | 2: R2, R4 |
| 2 | 2D | MOCK: open dependencies | X axis: Status. Y axis: Supplier Value Stream and Sub Value Stream. | Governance and Conditions: Backlog 1, In Progress 2. None: Backlog 1. |
| 3 | 2D | MOCK: open dependencies | X axis: RAG Status. Y axis: Value Stream and Sub-Value Stream. | Drawdown: Green 1, Red 1. Monitoring: Amber 2. |
| 4 | Filter Results | MOCK: dependencies late or due soon | Columns: Key, Summary, Due date, Baseline End Date, RAG Status, Assignee | 3: R1, R2, R4 |
| 5 | Filter Results | MOCK: flagged | Columns: Key, Summary, Assignee | 2: E4, S1 |
| 6 | Filter Results | MOCK: dependencies at risk | Columns: Key, Summary, RAG Status, Due date | 3: R1, R2, R4 |
| 7 | Filter Results | MOCK: dependencies without an owner or date | Columns: Key, Summary, Reporter | 1: R4 |

Gadgets 2 and 3 are the ones most likely to be refused, because the two fields may be two-step dropdowns. If they are, use page B6 in Confluence for those two views.

## A6. The two boards

1. **Boards > Create board > Kanban > Board from an existing saved filter**: filter `MOCK: open Capabilities`. Name it "MOCK Capabilities". In **Board settings > Columns**, make one column per status.
2. The same with filter `MOCK: all Initiatives`. Name it "MOCK Initiatives". In **Board settings > Swimlanes**, base swimlanes on **Queries**, one per Capability: `"Parent Link" = <key of C1>`, and so on. In **Card colours**, colour by query: `"RAG Status" = Red`, `"RAG Status" = Amber`, `"RAG Status" = Green`.

You should see I6 alone in the Idea column, I8 in Ready, five cards in Implementing, and I2 in Released.

---

# Part B: Confluence

## B1. The same steps for every page

1. Edit the page. Insert the outer macro first, then the inner ones inside its body. The order, outermost first, is: **Chart from Table > Table Transformer (or Pivot Table) > Jira Issues**.
2. In the **Jira Issues** macro: type `filter = "<the filter name>"`, choose **Table** display, set Maximum issues to 100, and list the columns the step names.
3. Save the page. Look at the plain table first.
4. Open the **Table Transformer** settings: **Presets > Custom transformation**, paste the SQL, and set the date format to match how dates look in the table.
5. Check the result as a table against "You should see".
6. Only then open **Chart from Table** and set the chart.

In the SQL, the first table inside the macro is `T1`, the second is `T2`. Column names go in single quotes and text in double quotes. **Use each column header exactly as your Jira Issues macro shows it**: on Data Center the component column is usually headed `Component/s`, the due date `Due`, and the fix version `Fix Version/s`. If yours differ, change the SQL to match.

Suggested page tree: one parent page "MOCK portfolio", with pages B2 to B10 beneath it.

## B2. Portfolio tree: each Capability with its Initiatives

- T1 = Jira Issues on `MOCK: open Capabilities`. Columns: Key, Summary, Status, RAG Status, Due.
- T2 = Jira Issues on `MOCK: all Initiatives`. Columns: Key, Summary, Status, RAG Status, Parent Link.

```sql
SELECT T1.'Summary' AS 'Capability', T1.'RAG Status' AS 'Capability RAG', T1.'Due' AS 'Due',
  COUNT(T2.'Key') AS 'Initiatives',
  SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", 1, 0)) AS 'Released',
  SUM(IF(T2.'RAG Status' = "Red", 1, 0)) AS 'Red',
  SUM(IF(T2.'RAG Status' = "Amber", 1, 0)) AS 'Amber'
FROM T1
LEFT JOIN T2 ON T2.'Parent Link' = T1.'Key'
GROUP BY T1.'Summary', T1.'RAG Status', T1.'Due'
```

**You should see**

| Capability | Initiatives | Released | Red | Amber |
| --- | --- | --- | --- | --- |
| Avoid audit risk through access control | 3 | 1 | 0 | 1 |
| Earlier warning on deteriorating exposures | 2 | 0 | 1 | 0 |
| One view of conditions from approval to drawdown | 2 | 0 | 0 | 1 |

If every count is 0, the join found nothing: the Parent Link column is showing something other than the bare key. Look at it in the plain table. If it shows the parent's summary, join on `T2.'Parent Link' = T1.'Summary'`.

## B3. Initiative progress across applications (figure 9)

**First, without SQL.** Pivot Table around a Jira Issues macro on `MOCK: PI Epics` (columns Key, Summary, Component/s, Status, Parent Link). Row labels: Parent Link. Column labels: Component/s. Calculated column: Status. Operation: Literal. Totals off.

**Then with SQL**, for the progress and "still open in" columns:

- T1 = Jira Issues on `MOCK: PI Epics`. Columns: Key, Summary, Component/s, Status, Parent Link.
- T2 = Jira Issues on `MOCK: current PI Initiatives`. Columns: Key, Summary.

```sql
SELECT T2.'Summary' AS 'Initiative',
  GROUP_CONCAT(IF(T1.'Component/s' = "Credit Application", T1.'Status', NULL)) AS 'Credit Application',
  GROUP_CONCAT(IF(T1.'Component/s' = "Drawdowns", T1.'Status', NULL)) AS 'Drawdowns',
  GROUP_CONCAT(IF(T1.'Component/s' = "Governance and Conditions", T1.'Status', NULL)) AS 'Governance and Conditions',
  SUM(IF(T1.'Status' = "Released" OR T1.'Status' = "Done", 1, 0)) AS 'Released',
  COUNT(*) AS 'Epics',
  GROUP_CONCAT(IF(T1.'Status' = "Released" OR T1.'Status' = "Done", NULL, T1.'Component/s')) AS 'Still open in'
FROM T1
JOIN T2 ON T1.'Parent Link' = T2.'Key'
GROUP BY T2.'Summary'
ORDER BY T2.'Summary'
```

**You should see**

| Initiative | Credit Application | Drawdowns | Governance and Conditions | Released | Epics | Still open in |
| --- | --- | --- | --- | --- | --- | --- |
| Access review evidence pack | | | Released | 1 | 1 | |
| Conditions carried into drawdown checks | | | Implementing | 0 | 1 | Governance and Conditions |
| Covenant breach alerts by email | Implementing | | | 0 | 1 | Credit Application |
| Facility letter generated from approved terms | Implementing | | | 0 | 1 | Credit Application |
| M&P across the platform | Released | Implementing | | 1 | 2 | Drawdowns |
| Watch-list triggers from covenant breaches | | Ready | Implementing | 0 | 2 | Drawdowns, Governance and Conditions |

"M&P across the platform" is the case the whole design exists for: one application has delivered and the Initiative is waiting for the other. E8 (no parent) does not appear, which is correct.

## B4. Epics by application and status, as a chart

- Pivot Table around Jira Issues on `MOCK: PI Epics` (Key, Component/s, Status). Row labels: Component/s. Column labels: Status. Operation: Count.
- Wrap it in **Chart from Table**: Type Stacked Bar (or Stacked Column). Labels column: Component/s. Values columns: Ready, Implementing, Released.

**You should see** three bars of 3 Epics each: Credit Application (1 Released, 2 Implementing), Drawdowns (2 Implementing, 1 Ready), Governance and Conditions (1 Released, 2 Implementing).

## B5. PI plan page

Three parts on one page.

**Part 1: Epics by application and sprint.** T1 = Jira Issues on `MOCK: PI Epics` (Key, Summary, Component/s, End Date, Status, Labels). The date in the query is the first day of the PI; for the mock use 9 November 2026.

```sql
SELECT T1.'Component/s' AS 'Application',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2026-11-09", T1.'End Date') / 14) + 1 <= 1, T1.'Summary', NULL)) AS 'Sprint 1',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2026-11-09", T1.'End Date') / 14) + 1 = 2, T1.'Summary', NULL)) AS 'Sprint 2',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2026-11-09", T1.'End Date') / 14) + 1 = 3, T1.'Summary', NULL)) AS 'Sprint 3',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2026-11-09", T1.'End Date') / 14) + 1 = 4, T1.'Summary', NULL)) AS 'Sprint 4',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2026-11-09", T1.'End Date') / 14) + 1 >= 5, T1.'Summary', NULL)) AS 'Sprint 5 or later'
FROM T1
GROUP BY T1.'Component/s'
```

**You should see** (if you kept the dates in the ticket list)

| Application | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 | Sprint 5 or later |
| --- | --- | --- | --- | --- | --- |
| Credit Application | M&P for Credit Application | | Approved terms feed for the facility letter | | Alert emails from Credit Application |
| Drawdowns | | | | Limit check rewrite | M&P for Drawdowns, Covenant alerts shown in Drawdowns |
| Governance and Conditions | Evidence pack for conditions | | | Covenant trigger rules, Conditions API v2 | |

If the sprint columns are empty or wrong, the date format is the cause: set it in the Table Transformer to match how End Date looks in the plain table.

**Part 2: load against capacity.** T1 = the same macro with Story Points added. T2 = a table you type on the page:

| Component/s | Capacity |
| --- | --- |
| Credit Application | 45 |
| Drawdowns | 40 |
| Governance and Conditions | 60 |

```sql
SELECT T1.'Component/s' AS 'Application',
  SUM(IF(T1.'Labels' LIKE "%pi-committed%", T1.'Story Points', 0)) AS 'Committed',
  SUM(IF(T1.'Labels' LIKE "%pi-stretch%", T1.'Story Points', 0)) AS 'Stretch',
  T2.'Capacity' AS 'Capacity',
  T2.'Capacity' - SUM(IF(T1.'Labels' LIKE "%pi-committed%", T1.'Story Points', 0)) AS 'Room left after committed'
FROM T1
LEFT JOIN T2 ON T2.'Component/s' = T1.'Component/s'
GROUP BY T1.'Component/s', T2.'Capacity'
```

**You should see**

| Application | Committed | Stretch | Capacity | Room left after committed |
| --- | --- | --- | --- | --- |
| Credit Application | 34 | 8 | 45 | 11 |
| Drawdowns | 34 | 13 | 40 | 6 |
| Governance and Conditions | 55 | 0 | 60 | 5 |

Chart from Table: Stacked Bar. Labels column: Application. Values columns: Committed, Stretch. Drawdowns shows the point of the page: 34 committed fits in 40, but with 13 stretch it would not.

**Part 3: the dependency board.** See B6; put the same table here.

## B6. Dependency board (figure 17) and dependencies by supplier (figure 19)

T1 = Jira Issues on `MOCK: open dependencies`. Columns: Key, Summary, Value Stream and Sub-Value Stream, Supplier Value Stream and Sub Value Stream, Assignee, Due, Baseline End Date, Status, RAG Status, Linked Issues.

```sql
SELECT T1.'Key', T1.'Summary' AS 'What is needed',
  T1.'Value Stream and Sub-Value Stream' AS 'Waiting',
  T1.'Supplier Value Stream and Sub Value Stream' AS 'Supplier',
  T1.'Due' AS 'Need-by',
  T1.'Baseline End Date' AS 'Promised',
  DATEDIFF(DAY, T1.'Baseline End Date', T1.'Due') AS 'Margin (days)',
  CASE
    WHEN T1.'Status' = "Backlog" THEN "Asked, not agreed"
    WHEN T1.'Baseline End Date' IS NULL THEN "Agreed, no date"
    WHEN DATEDIFF(DAY, T1.'Baseline End Date', T1.'Due') < 0 THEN "Date conflict"
    ELSE "Agreed"
  END AS 'State',
  T1.'RAG Status' AS 'RAG',
  T1.'Linked Issues' AS 'Linked work'
FROM T1
ORDER BY T1.'Due'
```

**You should see**

| What is needed | Margin (days) | State |
| --- | --- | --- |
| Covenant test environment needed from Group IT | empty | Asked, not agreed |
| Credit Application needs the covenant event feed for alert emails | empty | Asked, not agreed |
| Drawdowns needs Conditions API v2 before sprint 3 | -14 | Date conflict |
| Drawdowns needs the evidence export format agreed | 15 | Agreed |

**By supplier, as a chart.** A second Table Transformer on the same macro:

```sql
SELECT T1.'Supplier Value Stream and Sub Value Stream' AS 'Supplier',
  SUM(IF(T1.'Status' = "Backlog", 1, 0)) AS 'Asked, not agreed',
  SUM(IF(T1.'Status' = "In Progress" AND DATEDIFF(DAY, T1.'Baseline End Date', T1.'Due') >= 0, 1, 0)) AS 'Agreed',
  SUM(IF(T1.'Status' = "In Progress" AND DATEDIFF(DAY, T1.'Baseline End Date', T1.'Due') < 0, 1, 0)) AS 'Date conflict'
FROM T1
GROUP BY T1.'Supplier Value Stream and Sub Value Stream'
```

**You should see** Governance and Conditions: 1 asked, 1 agreed, 1 conflict. No supplier: 1 asked. Chart from Table: Stacked Bar; Labels column: Supplier; Values columns: the three counts.

**Who waits on whom (figure 13).** Pivot Table on the same macro. Row labels: Value Stream and Sub-Value Stream. Column labels: Supplier Value Stream and Sub Value Stream. Operation: Count. You should see Drawdown 2 and Monitoring 1 under Governance and Conditions, and Monitoring 1 under the empty supplier.

## B7. PI scorecard

1. Open the filter `MOCK: committed Initiatives` in Jira. Copy the four rows (Key and Summary) and paste them onto the page as a plain table with the headers `Key` and `Committed item`. This pasted table is the baseline: it is T1.
2. Below it, inside the same Table Transformer, T2 = Jira Issues on `MOCK PI planned Initiatives` (Key, Summary, Status, RAG Status, Target PI, Actual PI).

```sql
SELECT T1.'Key', T1.'Committed item', T2.'Status', T2.'RAG Status',
  CASE
    WHEN T2.'Key' IS NULL THEN "Removed after the lock"
    WHEN T2.'Status' = "Released" OR T2.'Status' = "Done" THEN "Delivered"
    ELSE "Not yet delivered"
  END AS 'Result'
FROM T1
LEFT JOIN T2 ON T2.'Key' = T1.'Key'
```

**You should see** four rows: Access review evidence pack "Delivered", the other three "Not yet delivered". To see the baseline working, remove the `pi-committed` label from one Initiative in Jira and reload: the page still shows four rows, because the baseline was pasted.

## B8. RAID by type and RAG

T1 = Jira Issues on `MOCK: open RAID` (Key, RAID Type, RAG Status).

```sql
SELECT T1.'RAID Type',
  SUM(IF(T1.'RAG Status' = "Green", 1, 0)) AS 'Green',
  SUM(IF(T1.'RAG Status' = "Amber", 1, 0)) AS 'Amber',
  SUM(IF(T1.'RAG Status' = "Red", 1, 0)) AS 'Red'
FROM T1
GROUP BY T1.'RAID Type'
```

**You should see** Dependency 1, 2, 1. Risk 1, 1, 0. Issue 0, 0, 1. Assumption 1, 0, 0. Chart from Table: Stacked Bar; Labels column: RAID Type; Values columns: Green, Amber, Red.

## B9. Capabilities in progress against a limit

T1 = Jira Issues on `MOCK: open Capabilities` (Key, Status). T2 = a typed table: `Status`, `Limit`, with rows Analysis 2 and Implementing 1.

```sql
SELECT T1.'Status', COUNT(*) AS 'Capabilities', T2.'Limit'
FROM T1
LEFT JOIN T2 ON T2.'Status' = T1.'Status'
GROUP BY T1.'Status', T2.'Limit'
```

**You should see** Analysis 1 against a limit of 2, and Implementing 2 against a limit of 1: over the limit. Chart from Table: Column; Labels column: Status; Values columns: Capabilities, Limit.

## B10. Delivery lead page

Use page layout columns to put several small macros side by side.

**Headline row.** T1 = Jira Issues on `MOCK: PI Epics` (Key, Status, Labels, Flagged).

```sql
SELECT COUNT(*) AS 'Epics this PI',
  SUM(IF(T1.'Status' = "Released" OR T1.'Status' = "Done", 1, 0)) AS 'Released',
  SUM(IF(T1.'Status' = "Implementing", 1, 0)) AS 'In progress',
  SUM(IF(T1.'Status' = "Ready" OR T1.'Status' = "Analysis" OR T1.'Status' = "Idea", 1, 0)) AS 'Not started',
  SUM(IF(T1.'Labels' LIKE "%pi-committed%", 1, 0)) AS 'Committed',
  SUM(IF(T1.'Flagged' = "Impediment", 1, 0)) AS 'Flagged'
FROM T1
```

**You should see** 9, 2, 6, 1, 6, 1.

**Panels beneath**, each a Jira Issues macro with no transformation:

| Panel | Filter | You should see |
| --- | --- | --- |
| What is blocked | MOCK: flagged | 2: E4, S1 |
| What is progressing | The chart from B4 | Three bars |
| Dependencies needing action | The table from B6 | Three rows that are not "Agreed" |
| Off track without a recovery plan | MOCK: Amber or Red without a plan | 1: I3 |
| Committed or planned but not started | MOCK: PI Epics not started | 1: E5 |
| Next release | MOCK release: not finished | 3: E2, S1, B1 |
| Next dates | MOCK: milestones next 90 days and overdue | 2: M1, M2 |

The platform owner page and the product owner page are built the same way from recipe 4.17 of the Confluence guide. For the product owner page, add `AND component = "Drawdowns"` to each filter: you should see three Epics (E2, E5, E8), two dependencies where Drawdowns waits (R1, R3), and one bug.

---

# Part C: What to write down as you go

Each row answers one of the proof-of-concept checks in the white paper.

| What you tried | Record | Check |
| --- | --- | --- |
| Creating the tickets | Any field in the list that was missing from a screen, by issue type | 1, 2 |
| The values you had to change | The real values of Target PI, RAG Status, RAID Type, ROAM Response, Severity | 3 |
| Dashboard MOCK 2 gadget 9, MOCK 6 gadgets 2 and 3 | Whether a 2D gadget accepts the sub value stream and supplier fields | 4 |
| The filters in A1 | Any query that gave an error, and the message | 6 |
| Pages B2 and B3 | What the Parent Link column shows in the Jira Issues macro: a key, a summary, or raw text | 7 |
| The `issueLinkType` test in MOCKUP_GUIDE.md, section 6 | Works, or the error message | 10 |
| Page B6 | Whether the margin and the state came out as listed | 10 |
| Setting Parent Link | Whether it can be set on the ticket screen, and by bulk change | 10 |
| Creating a Delivery RAID ticket | Whether you could create and move it | 11 |
| Any SQL that failed | The function it stopped on (for example GROUP_CONCAT with IF, DATEDIFF, CASE) | |
