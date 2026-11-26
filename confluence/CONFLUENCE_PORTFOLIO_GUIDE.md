# Bringing the portfolio into Confluence

Jira dashboards count tickets in one list. They cannot walk the line VS Epic > Feature > Epic and add things up along it. Confluence can, using the Jira Issues macro for the data and Table Transformer for the roll-up, which works like SQL over the tables on the page.

This guide gives the page tree, the building blocks, a playground you can build today with mock tables and no Jira, and the query for each portfolio page.

**Status of the queries.** They are written from the vendor's documentation for Table Transformer (Data Center edition) and have not been run. Build each one on a scratch page first. Where a pattern is not shown in the vendor's documentation, it is marked "untested pattern".

## 1. The page tree

One parent page per value stream, top-down, same order as the Jira dashboards.

```text
Credit and Lending portfolio                 (landing page: roadmap + exceptions)
├── 1 VS Epics: outcomes and health          (portfolio tree, level 1 to 2; recipe 4.1)
├── 2 Features across the value stream       (level 2 to 3, by application; recipes 4.2, 4.3)
├── 3 Epics across applications              (pivot by application and status; recipe 4.4)
├── 4 PI plans
│     ├── PI 2027.1 plan                     (one page per PI: Epics by sprint, capacity,
│     └── PI 2027.2 plan                      dependency board; recipes 4.14 to 4.16)
├── 5 PI scorecards
│     ├── PI 2027.1 scorecard                (one page per PI, never edited after PI end; 4.7)
│     └── PI 2027.2 scorecard
├── 6 Dependencies                           (who waits on whom, and the trend; recipe 4.13)
├── 7 Investment mix                         (recipe 4.9)
├── 8 Predictability trend                   (recipe 4.8)
├── 9 Milestones and slippage                (recipe 4.10)
├── 10 Size and forecast by VS Epic          (recipes 4.5, 4.6)
├── 11 Weekly status (Red and Amber)         (recipe 4.11)
├── Role pages                               (recipe 4.17)
│     ├── Delivery lead
│     ├── Platform owner
│     └── Product owner: one page per application
└── Reference: objectives, label list, framework change log
```

## 2. The building blocks

**Jira Issues macro** (brings Jira rows onto the page)

1. Edit the page. **Insert > Other macros > Jira** (or type `{jira`).
2. Enter a saved filter as `filter = "VS: current PI Features"`, or paste JQL. Search.
3. **Display options**: choose **Table**, set **Maximum issues**, and under **Columns to display** add the fields you need, including custom fields by name.
4. Insert.

Limits to know: the macro shows at most 1,000 issues (reported in Atlassian's tracker; check yours), and Table Transformer only sees rows the macro displays. Keep each filter narrow: one PI, or open items only. On Jira 10.5 to 10.7 the Parent Link column in this macro showed raw text instead of the parent's key; check one page before building on it.

**Table Transformer** (SQL over the tables inside it)

1. Insert the **Table Transformer** macro.
2. Put the source tables inside its body: a typed table, a Jira Issues macro, or a Table Excerpt Include. The first table is `T1`, the second `T2`, and so on.
3. Save the page, then use the macro's **Edit** control > **Presets > Custom transformation > Next**, type the SQL, **Next**, set the date format, save.

Syntax rules that differ from ordinary SQL:

| Rule | Example |
| --- | --- |
| Column names go in single quotes | `T1.'Story Points'` |
| Text and dates go in double quotes | `"Released"`, `"2027-03-26"` |
| Prefix the table when a name appears in two tables | `T1.'Key' = T2.'Key'` |
| Conditional count | `SUM(IF(T1.'RAG Status' = "Red", 1, 0))` |
| Cast when a comparison misbehaves | `T1.'Story Points'::number`, `T1.'Due Date'::Date` |
| Join many values into one cell | `GROUP_CONCAT(T2.'Project Key')` (comma only) |

**Pivot Table** (counts without SQL): set **Row labels**, **Column labels**, **Calculated column** and the **Operation** (Count, Sum, Average, Min/Max, Literal).

**Chart from Table**: wrap it around a table (or around a Table Transformer or Pivot Table), then pick the chart type and set **Labels column** and **Values column**. It does not add up for you; aggregate first. Types include Column, Stacked Column, Bar, Stacked Bar, Line, Pie, Donut, Time Line and Gantt.

**Table Excerpt and Table Excerpt Include**: wrap a table in Table Excerpt with a name on one page; show it on another page with Table Excerpt Include. This is how a PI baseline pasted on a scorecard page can be reused on the trend page.

**Nesting order**, outermost first: Chart from Table > Table Transformer (or Pivot Table) > Jira Issues macro or table.

## 3. Playground with mock data (no Jira needed)

1. Create a page called "Portfolio playground".
2. Open `import/jira-import-template.xlsx`. Copy the whole **VS_Epics** sheet and paste it into the page; it becomes a table. Do the same for **Features**, **Epics**, **Velocity** and **Milestones**.
3. Cut each table into the body of the Table Transformer for the recipe you are trying. Table order matters: the recipe says which table is T1, T2, T3.

In the mock tables the join is on the summary text: an Epic's `Parent summary (helper)` equals its Feature's `Summary`. In live Jira tables the join is on the key: an Epic's `Parent Link` equals its Feature's `Key`. Each recipe shows the mock form; the line to change for Jira is given under it.

## 4. Recipes

### 4.1 Portfolio tree: each VS Epic with its Features and their health

Tables: T1 = VS Epics, T2 = Features.

```sql
SELECT T1.'Summary' AS 'VS Epic',
  T1.'RAG Status' AS 'VS Epic RAG',
  T1.'Due Date' AS 'Due',
  COUNT(T2.'Summary') AS 'Features',
  SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", 1, 0)) AS 'Released',
  SUM(IF(T2.'RAG Status' = "Red", 1, 0)) AS 'Red',
  SUM(IF(T2.'RAG Status' = "Amber", 1, 0)) AS 'Amber',
  SUM(IF(T2.'RAG Status' = "Green", 1, 0)) AS 'Green'
FROM T1
LEFT JOIN T2 ON T2.'Parent summary (helper)' = T1.'Summary'
GROUP BY T1.'Summary', T1.'RAG Status', T1.'Due Date'
```

For Jira: `LEFT JOIN T2 ON T2.'Parent Link' = T1.'Key'`, and select `T1.'Key'` as well.

Answers: which outcomes are in trouble, and how many of their Features are done.

### 4.2 Feature progress across applications

Tables: T1 = Features, T2 = Epics.

```sql
SELECT T1.'Parent summary (helper)' AS 'VS Epic',
  T1.'Summary' AS 'Feature',
  T1.'Target PI' AS 'Target PI',
  T1.'RAG Status' AS 'Feature RAG',
  COUNT(T2.'Summary') AS 'Epics',
  SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", 1, 0)) AS 'Epics released',
  SUM(T2.'Story Points') AS 'Points',
  SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", T2.'Story Points', 0)) AS 'Points released',
  SUM(IF(T2.'RAG Status' = "Red", 1, 0)) AS 'Red Epics',
  GROUP_CONCAT(T2.'Project Key') AS 'Applications'
FROM T1
LEFT JOIN T2 ON T2.'Parent summary (helper)' = T1.'Summary'
GROUP BY T1.'Parent summary (helper)', T1.'Summary', T1.'Target PI', T1.'RAG Status'
ORDER BY T1.'Parent summary (helper)'
```

For Jira: `LEFT JOIN T2 ON T2.'Parent Link' = T1.'Key'`; use `T2.'Project'` for the application.

Answers: for each Feature, how many applications are involved and how far each has got. This is the cross-application view Jira cannot produce.

### 4.3 Features waiting on one late application

Same tables as 4.2. Add this at the end, before `ORDER BY` (untested pattern):

```sql
HAVING SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", 1, 0)) > 0
   AND SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", 1, 0)) < COUNT(T2.'Summary')
```

If `HAVING` is not accepted, keep 4.2 as it is and put a **Table Filter** macro around it, filtering on the two count columns.

To list the late Epics themselves (T1 = Features, T2 = Epics):

```sql
SELECT T1.'Summary' AS 'Feature', T2.'Summary' AS 'Epic still open',
  T2.'Project Key' AS 'Application', T2.'Status', T2.'RAG Status', T2.'End Date'
FROM T2
JOIN T1 ON T2.'Parent summary (helper)' = T1.'Summary'
WHERE T2.'Status' != "Released" AND T2.'Status' != "Done"
  AND T1.'Target PI' = "PI 2027.1"
ORDER BY T1.'Summary'
```

### 4.4 Epics by application and status (no SQL)

Put the Epics table inside a **Pivot Table** macro: Row labels = `Project Key`, Column labels = `Status`, Operation = Count. Wrap that in **Chart from Table**, type Stacked Bar, for the picture.

For points instead of counts: Calculated column = `Story Points`, Operation = Sum.

### 4.5 Whole-line roll-up: story points per VS Epic

Tables: T1 = Features, T2 = Epics.

```sql
SELECT T1.'Parent summary (helper)' AS 'VS Epic',
  COUNT(T2.'Summary') AS 'Epics',
  SUM(T2.'Story Points') AS 'Total points',
  SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", T2.'Story Points', 0)) AS 'Released points',
  ROUND(SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", T2.'Story Points', 0)) / SUM(T2.'Story Points') * 100) AS 'Percent released'
FROM T1
LEFT JOIN T2 ON T2.'Parent summary (helper)' = T1.'Summary'
GROUP BY T1.'Parent summary (helper)'
```

For Jira: the Features table carries the VS Epic's key in its own `Parent Link` column, so group by `T1.'Parent Link'`. To show the VS Epic's name instead of its key, add the VS Epics table as T3 and `LEFT JOIN T3 ON T1.'Parent Link' = T3.'Key'`.

### 4.6 Forecast: PIs to go, and the application that limits each VS Epic

Tables: T1 = Features, T2 = Epics, T3 = Velocity (a small typed table: `Project Key`, `PI velocity (story points per PI)`).

```sql
SELECT T1.'Parent summary (helper)' AS 'VS Epic',
  T2.'Project Key' AS 'Application',
  SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", 0, T2.'Story Points')) AS 'Remaining points',
  T3.'PI velocity (story points per PI)' AS 'PI velocity',
  ROUND(SUM(IF(T2.'Status' = "Released" OR T2.'Status' = "Done", 0, T2.'Story Points')) / T3.'PI velocity (story points per PI)', 1) AS 'PIs to go'
FROM T2
JOIN T1 ON T2.'Parent summary (helper)' = T1.'Summary'
LEFT JOIN T3 ON T3.'Project Key' = T2.'Project Key'
GROUP BY T1.'Parent summary (helper)', T2.'Project Key', T3.'PI velocity (story points per PI)'
ORDER BY T1.'Parent summary (helper)'
```

Read it as: a VS Epic finishes when its slowest application does, so the largest "PIs to go" in each group is the forecast. A team works on several things at once, so this is a floor, not a promise.

### 4.7 PI scorecard: baseline against today

On the scorecard page for the PI: T1 = the baseline table pasted at the PI lock (`Key`, `Summary`, `Committed or Stretch`, `Story Points`, `Due Date`), T2 = Jira Issues macro on that PI's own filter (`PI 2027.1 planned Features`).

```sql
SELECT T1.'Key', T1.'Summary', T1.'Committed or Stretch',
  T2.'Status' AS 'Status now', T2.'RAG Status' AS 'RAG now', T2.'Actual PI',
  CASE
    WHEN T2.'Key' IS NULL THEN "Removed from the PI"
    WHEN T2.'Actual PI' = T2.'Target PI' THEN "Delivered"
    WHEN T2.'Status' = "Released" OR T2.'Status' = "Done" THEN "Delivered late"
    ELSE "Open"
  END AS 'Result'
FROM T1
LEFT JOIN T2 ON T1.'Key' = T2.'Key'
```

Work added after the lock, in a second Table Transformer with the same two tables (untested pattern):

```sql
SELECT T2.'Key', T2.'Summary', T2.'Status', T2.'Labels'
FROM T2
LEFT JOIN T1 ON T2.'Key' = T1.'Key'
WHERE T1.'Key' IS NULL
```

The score line:

```sql
SELECT COUNT(T1.'Key') AS 'Committed',
  SUM(IF(T2.'Actual PI' = T2.'Target PI', 1, 0)) AS 'Delivered',
  ROUND(SUM(IF(T2.'Actual PI' = T2.'Target PI', 1, 0)) / COUNT(T1.'Key') * 100) AS 'Predictability percent'
FROM T1
LEFT JOIN T2 ON T1.'Key' = T2.'Key'
WHERE T1.'Committed or Stretch' = "Committed"
```

Wrap the baseline table in **Table Excerpt** named `baseline-PI-2027-1` so other pages can reuse it. To try this in the playground, copy five rows of the Features table as the "baseline", then change a row in the main table and watch the result change.

### 4.8 Predictability trend across PIs

T1 = Jira Issues macro on `project = CLP AND issuetype = Feature AND labels = pi-committed AND "Target PI" is not EMPTY`, columns Key, Target PI, Actual PI. In the playground, use the Features table.

```sql
SELECT T1.'Target PI' AS 'PI',
  COUNT(*) AS 'Committed',
  SUM(IF(T1.'Actual PI' = T1.'Target PI', 1, 0)) AS 'Delivered in PI',
  ROUND(SUM(IF(T1.'Actual PI' = T1.'Target PI', 1, 0)) / COUNT(*) * 100) AS 'Predictability percent'
FROM T1
WHERE T1.'Labels' LIKE "%pi-committed%"
GROUP BY T1.'Target PI'
ORDER BY T1.'Target PI'
```

Wrap in **Chart from Table**, type Line, Labels column = `PI`, Values column = `Predictability percent`. This is the live trend; the scorecards remain the figure of record, because Target PI can be edited and the pasted baseline cannot.

### 4.9 Investment mix

T1 = Features for the PI. Simplest is a **Pivot Table**: Row labels = `Enabler Type`, Operation = Count, then **Chart from Table**, type Pie. Empty Enabler Type means business work.

By points, joining Epics (T1 = Features, T2 = Epics):

```sql
SELECT CASE WHEN T1.'Enabler Type' IS NULL OR T1.'Enabler Type' = "" THEN "Business" ELSE T1.'Enabler Type' END AS 'Kind of work',
  SUM(T2.'Story Points') AS 'Points'
FROM T1
LEFT JOIN T2 ON T2.'Parent summary (helper)' = T1.'Summary'
GROUP BY CASE WHEN T1.'Enabler Type' IS NULL OR T1.'Enabler Type' = "" THEN "Business" ELSE T1.'Enabler Type' END
```

### 4.10 Milestone slippage

T1 = Milestones with `Baseline End Date` and `Due Date`.

```sql
SELECT T1.'Summary' AS 'Milestone', T1.'RAG Status',
  T1.'Baseline End Date', T1.'Due Date',
  DATEDIFF(DAY, T1.'Baseline End Date', T1.'Due Date') AS 'Days slipped'
FROM T1
ORDER BY DATEDIFF(DAY, T1.'Baseline End Date', T1.'Due Date') DESC
```

After typing the SQL, click **Next** and set the date format to match the cells (`yyyy-mm-dd` for the mock data; your Jira macro may show `dd/MMM/yy`). If the result is empty or wrong, the date format is the first thing to check.

### 4.11 Weekly status: the exceptions, in the owners' words

No SQL. One Jira Issues macro on `VS: Red and Amber`, columns: Type, Key, Summary, RAG Status, Executive Summary, Path to Green, Date to Green, Due date, Assignee. Put it at the top of the landing page; it is the agenda for the portfolio sync.

### 4.12 Roadmap as a Gantt chart

T1 = VS Epics with `Start Date` and `End Date` (or Features, for the next level down). Wrap the table in **Chart from Table**, type **Gantt**: Labels column = `Summary` as the Phase; Values columns = `Start Date` and `End Date`. Set the date format on the chart's date tab.

Where sharing a plan view is allowed, prefer the plan's own "L0 roadmap" view: in the plan, **Share as** offers a link, an embed and a CSV export. The Gantt above is the fallback.

### 4.13 Dependencies across applications

T1 = Jira Issues macro on `VS: open dependencies`, columns Key, Summary, Value Stream and Sub-Value Stream, Supplier Value Stream and Sub Value Stream, Due date, RAG Status. A **Pivot Table** with Row labels = the receiver field, Column labels = the supplier field, Operation = Count, shows who is waiting on whom at a glance.

### 4.14 PI plan page, part 1: Epics by application and sprint

This and the next three recipes replace the views that would otherwise need Plans. They have not yet been run on real data; prove them in the proof of concept.

T1 = Jira Issues macro on `VS: PI Epics`, columns Key, Summary, Project, End Date, Status, Labels. Change the date in the query to the first day of the PI; nothing else changes from PI to PI.

```sql
SELECT T1.'Project' AS 'Application',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2027-03-29", T1.'End Date') / 14) + 1 <= 1, T1.'Summary', NULL) SEPARATOR "; ") AS 'Sprint 1',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2027-03-29", T1.'End Date') / 14) + 1 = 2, T1.'Summary', NULL) SEPARATOR "; ") AS 'Sprint 2',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2027-03-29", T1.'End Date') / 14) + 1 = 3, T1.'Summary', NULL) SEPARATOR "; ") AS 'Sprint 3',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2027-03-29", T1.'End Date') / 14) + 1 = 4, T1.'Summary', NULL) SEPARATOR "; ") AS 'Sprint 4',
  GROUP_CONCAT(IF(FLOOR(DATEDIFF(DAY, "2027-03-29", T1.'End Date') / 14) + 1 >= 5, T1.'Summary', NULL) SEPARATOR "; ") AS 'Sprint 5 or later',
  SUM(IF(T1.'End Date' IS NULL, 1, 0)) AS 'No end date'
FROM T1
GROUP BY T1.'Project'
```

An Epic with no End Date is counted in the last column: it is in the PI but nobody has said when. If the date arithmetic misbehaves, add `::Date` after the column name.

### 4.15 PI plan page, part 2: load against capacity

T1 = the same macro, with Story Points. T2 = a small typed table on the page: `Project`, `Capacity (story points)`. Each team gives one number per PI.

```sql
SELECT T1.'Project' AS 'Application',
  SUM(IF(T1.'Labels' LIKE "%pi-committed%", T1.'Story Points', 0)) AS 'Committed',
  SUM(IF(T1.'Labels' LIKE "%pi-stretch%", T1.'Story Points', 0)) AS 'Stretch',
  SUM(T1.'Story Points') AS 'Total planned',
  T2.'Capacity (story points)' AS 'Capacity',
  T2.'Capacity (story points)' - SUM(IF(T1.'Labels' LIKE "%pi-committed%", T1.'Story Points', 0)) AS 'Room left after committed'
FROM T1
LEFT JOIN T2 ON T2.'Project' = T1.'Project'
GROUP BY T1.'Project', T2.'Capacity (story points)'
```

A negative number in the last column means the team has committed more than it can carry. Wrap the result in Chart from Table (stacked bar, with Capacity as a line) to get the picture in the white paper. Load per sprint stays on each team's board.

### 4.16 PI plan page, part 3: the dependency board

T1 = Jira Issues macro on `VS: open dependencies`, columns Key, Summary, Value Stream and Sub-Value Stream, Supplier Value Stream and Sub Value Stream, Assignee, Due Date, Baseline End Date, Status, RAG Status, Linked Issues (`issuelinks`).

On a dependency ticket, Due Date is the date the receiver needs it and Baseline End Date is the date the supplier has promised.

```sql
SELECT T1.'Key', T1.'Summary' AS 'What is needed',
  T1.'Value Stream and Sub-Value Stream' AS 'Waiting',
  T1.'Supplier Value Stream and Sub Value Stream' AS 'Supplier',
  T1.'Assignee' AS 'Supplier owner',
  T1.'Due Date' AS 'Need-by',
  T1.'Baseline End Date' AS 'Promised',
  DATEDIFF(DAY, T1.'Baseline End Date', T1.'Due Date') AS 'Margin (days)',
  CASE
    WHEN T1.'Status' = "Backlog" THEN "Asked, not agreed"
    WHEN T1.'Baseline End Date' IS NULL THEN "Agreed, no date"
    WHEN DATEDIFF(DAY, T1.'Baseline End Date', T1.'Due Date') < 0 THEN "Date conflict"
    ELSE "Agreed"
  END AS 'State',
  T1.'RAG Status' AS 'RAG',
  T1.'Linked Issues' AS 'Linked work'
FROM T1
ORDER BY T1.'Due Date'
```

Use the macro's conditional formatting to colour the State column. Before the PI lock, this table should show no "Asked, not agreed", "Agreed, no date" or "Date conflict" behind a committed Epic. Paste a copy into the PI scorecard at the lock.

A count by supplier, for "what we owe":

```sql
SELECT T1.'Supplier Value Stream and Sub Value Stream' AS 'Supplier',
  COUNT(*) AS 'Open',
  SUM(IF(T1.'Status' = "Backlog", 1, 0)) AS 'Not agreed',
  SUM(IF(DATEDIFF(DAY, T1.'Baseline End Date', T1.'Due Date') < 0, 1, 0)) AS 'Date conflict',
  SUM(IF(DATEDIFF(DAY, NOW(), T1.'Due Date') < 0, 1, 0)) AS 'Past need-by'
FROM T1
GROUP BY T1.'Supplier Value Stream and Sub Value Stream'
```

### 4.17 A page for each role

Each role page is a set of small macros side by side (use page layout columns), built from saved filters that already exist.

**Headline counts.** One row of numbers at the top of a page:

```sql
SELECT COUNT(*) AS 'Epics this PI',
  SUM(IF(T1.'Status' = "Released" OR T1.'Status' = "Done", 1, 0)) AS 'Done',
  SUM(IF(T1.'Status' = "Implementing", 1, 0)) AS 'In progress',
  SUM(IF(T1.'Status' = "Idea" OR T1.'Status' = "Analysis" OR T1.'Status' = "Ready", 1, 0)) AS 'Not started',
  SUM(IF(T1.'Labels' LIKE "%pi-committed%", 1, 0)) AS 'Committed',
  SUM(IF(T1.'Flagged' = "Impediment", 1, 0)) AS 'Flagged'
FROM T1
```

| Page | Panels, and the filter behind each |
| --- | --- |
| **Delivery lead** | Headline counts on `VS: PI Epics`. Blocked: `VS: flagged`, sorted by Updated. Progressing: Pivot Table on `VS: PI Epics`, Project by Status. Dependencies needing action: recipe 4.16, filtered to states other than "Agreed". Off track without a plan: `VS: Amber or Red without a plan`. Committed but not started: `VS: PI Epics not started`. Release and dates: `Release: not finished`, `VS: Milestones next 90 days and overdue`. |
| **Platform owner** | Pipeline: Pivot Table on `VS: all Features`, count by Status. What came in: `project = CLP AND issuetype = Feature AND created >= -30d`, pivoted by Enabler Type. In and out by month: the same filter widened to 180 days, with Created and Resolved formatted as months, counted, and drawn with Chart from Table. Stuck: `VS: intake waiting`, `VS: Analysis over 30 days`. Ready next: `VS: Ready, no Target PI`. Adoption: the hygiene filters, each counted. |
| **Product owner** (one page per application) | Headline counts on `filter = "VS: PI Epics" AND project = DRAW`. My Epics: the same filter with Parent Link, Status, RAG Status, End Date, sorted by Parent Link. Waiting on: `filter = "VS: open dependencies" AND component = Drawdowns`. We owe: `filter = "VS: open dependencies" AND assignee = <the product owner>`. Sprint: `project = DRAW AND sprint in openSprints()`, pivoted by Status. Bugs: `Team: open bugs`, pivoted by Severity. Tidy up: `Team: Epics without Feature`, `Team: Stories without Epic`. |

Build the product owner page once, save it as a template, and copy it per application, changing the project key and the component.

## 5. Putting the landing page together

Top to bottom:

1. One line: the PI, the date, and the three predictability figures from the last scorecard.
2. Roadmap (4.12, or the embedded plan view).
3. Portfolio tree (4.1).
4. Weekly status (4.11).
5. Links to the child pages.

Keep the landing page to what the value stream lead needs each month. The detail lives one click down.

## 6. Things that go wrong

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| "Table T2 not found" or an empty result | The Jira macro is not recognised as a table, or tables are in a different order | Check the order of tables in the macro body. If the Jira macro is not picked up, put it on a helper page inside Table Excerpt and bring it in with Table Excerpt Include. |
| A column is "not found" | The name in the SQL differs from the table header | Copy the header text exactly, including capitals and spaces. |
| Numbers add up as text, or sums are zero | The column is read as text | Use `T2.'Story Points'::number`. |
| Join returns no matches | Keys differ (a link, a trailing space, summary edited) | Run `SELECT T1.'Key' FROM T1` and `SELECT T2.'Parent Link' FROM T2` side by side and compare. |
| Rows missing from totals | The Jira macro shows fewer rows than the filter returns | Raise Maximum issues, or narrow the filter. |
| Dates compare wrongly | Date format not set | Set it in the step after the SQL. |
| Page is slow | Too many live macros on one page | Split across child pages; keep the landing page light. |
| Unmatched rows vanish from a LEFT JOIN | Reported by some users in preview | Check the first join by hand against a known example. |

## 7. Check before you rely on a page

- [ ] Run each query on mock data and compare the result with a hand count.
- [ ] Re-run on live Jira data and compare three rows with Jira itself.
- [ ] Open the page as a colleague: a Jira macro shows only what that person may see in Jira.
- [ ] Note the row count of each Jira macro against its filter's count in Jira.

## 8. Every figure in the white paper: can these macros build it, and how

The white paper has 35 figures. With the Jira Issues macro, Table Transformer, Pivot Table and Chart from Table:

- **30 can be built on a Confluence page.** Most are fully live from Jira. Four need a small table that someone types into, because Jira keeps no history. Several appear as a table or a plain bar chart, not in the exact styling of the paper.
- **5 are explanatory diagrams** (figures 2, 4, 7, 15, 16). They are not data. Use the image files in `whitepaper/charts/`: attach the PNG to the page.
- **1 detail is not possible:** arrows drawn between cards (a program board). Figure 17 was designed as a table with a margin column for that reason.

None of this has been run on your Confluence yet. Build the Feature progress page and the PI plan page with its dependency board in the proof of concept before promising the rest.

### The same six steps for every chart

1. Create or pick the saved filter in Jira. Share it with the value stream group.
2. On the Confluence page, insert **Chart from Table** (skip this if you want a table, not a chart).
3. Inside it, insert **Table Transformer** or **Pivot Table**.
4. Inside that, insert the **Jira Issues** macro on the filter, with exactly the columns the recipe names. Add a typed table too if the recipe says T2.
5. Save the page. Open the Table Transformer and paste the SQL (or set the Pivot Table rows, columns and operation). Check the result as a table first.
6. Open Chart from Table: choose the type, the **Labels column** and the **Values column(s)**. Save.

Always look at the table before the chart. If the table is wrong, the chart will be wrong more prettily.

### Figure by figure

| Fig. | What it shows | Buildable | Source | How | Chart from Table settings |
| --- | --- | --- | --- | --- | --- |
| 1 | Success measures, start against target | Yes, typed | A typed table: Measure, Start %, Target % | No SQL | Bar; Labels = Measure; Values = Start %, Target % |
| 2 | Hierarchy | Image | `01_hierarchy.png` | Attach the image | |
| 3 | Field shortlist | Yes, typed | A typed table: Issue type, Core, When it applies, Offered | No SQL | Stacked Bar; Labels = Issue type; Values = Core, When it applies |
| 4 | Feature lifecycle | Image | `23_feature_lifecycle.png` | Attach the image | |
| 5 | L0 roadmap | Yes | `VS: open VS Epics` and `VS: all Features` (not Done) with Start Date, End Date, RAG Status | Recipe 4.12. Or share the Plans roadmap view on the page. | Gantt; Labels = Summary; start and end = the two dates |
| 6 | WSJF ranking | Yes | `VS: Ready, no Target PI` with Summary and Weighted Shortest Job First Score | No SQL; the filter is already sorted | Bar; Labels = Summary; Values = the score |
| 7 | PI calendar | Image | `24_pi_calendar.png` | Attach the image | |
| 8 | Load against capacity | Yes | `VS: PI Epics` with Story Points and Labels; typed capacity table | Recipe 4.15 | Stacked Bar; Labels = Application; Values = Committed, Stretch. Show Capacity as a column beside the chart. |
| 9 | Feature progress across applications | Yes, as a table | `VS: PI Epics` with Parent Link, Project, Status | Recipe 4.2, or Pivot Table: rows = Parent Link, columns = Project, operation = Literal on Status | None; colour cells with conditional formatting |
| 10 | PI scorecard | Yes | The pasted baseline table, and that PI's own filter | Recipe 4.7 | Stacked Bar; Labels = Application; Values = Delivered, Spilled, Descoped, Stopped |
| 11 | Predictability trend | Yes | Committed Features and Epics with Target PI and Actual PI | Recipe 4.8 | Line; Labels = Target PI; Values = the three percentages |
| 12 | Spillover reasons | Yes | The scorecard table, with its Reason column | Pivot Table: rows = Reason, operation = Count | Bar; Labels = Reason; Values = Count |
| 13 | Who waits on whom | Yes, as a table | `VS: open dependencies` | Recipe 4.13 (Pivot Table) | None; conditional formatting for the shading |
| 14 | Release readiness | Yes | `Release: scope`; `Release: open bugs` | Recipe 8.3 below | Stacked Bar by Project; Bar by Severity |
| 15, 16 | Escalation ladder; dependency linking | Images | `28_escalation_ladder.png`, `32_dependency_linking.png` | Attach the images | |
| 17 | PI plan page with dependency board | Yes, as two tables | `VS: PI Epics`; `VS: open dependencies` | Recipes 4.14 and 4.16 | None. The "owes" and "waits for" tags in the paper's cells are not produced; the board beneath carries that. |
| 18 | Dependency dashboard | Yes | The dependency filters | As a Jira dashboard (dashboard guide, step 6b), or on a page with recipe 4.16 filtered by State | None |
| 19 | Dependencies by supplier and state | Yes | `VS: open dependencies` | Recipe 4.16, second query | Stacked Bar; Labels = Supplier; Values = the state counts |
| 20 | RAID overview | Yes | `VS: open RAID` | Recipe 8.2 below | Stacked Bar for type by RAG; the risk grid stays a table |
| 21 | Milestone slippage | Yes, as bars | Milestones with Baseline End Date and Due Date | Recipe 4.10 | Bar; Labels = Milestone; Values = Days slipped. The two-dot style of the paper is not available. |
| 22 | WIP limits | Yes | `VS: open VS Epics` with Status; typed table of limits | Recipe 8.1 below | Column; Labels = Status; Values = VS Epics, Limit |
| 23 | Investment mix | Yes | Features with Enabler Type; Epics with Story Points | Recipe 4.9 | Stacked Bar, shown as percentages |
| 24 | Points per VS Epic | Yes | Features and Epics with Story Points | Recipes 4.5 and 4.6 | Stacked Bar; Labels = VS Epic; Values = Done, Remaining |
| 25 | VS Epic burn-up | Yes, typed | A typed table, one row per sprint: Sprint, Scope, Done | No SQL. Someone adds a row each sprint from recipe 4.5. | Line; Labels = Sprint; Values = Scope, Done. No forecast cone. |
| 26 | PI velocity | Yes | Stories and bugs resolved in the PI, with Project and Story Points | Recipe 8.4 below | Column; Labels = Application; Values = one column per PI |
| 27 | Created against finished | Yes | `VS: all Features` with Created and Resolved | Recipe 8.5 below; or the Jira gadget Created vs Resolved | Line; Labels = Month; Values = Created, Finished |
| 28 | Dashboard 1 | Yes | Dashboard 1 filters | As a Jira dashboard; or on a page: recipe 4.1 with lists beneath | None |
| 29 | Features by sub value stream and RAG | Yes | `VS: current PI Features` | Pivot Table: rows = sub value stream, columns = RAG Status, Count | Stacked Bar; Labels = sub value stream; Values = Green, Amber, Red |
| 30 | Epics by application and status | Yes | `VS: PI Epics` | Recipe 4.4 (Pivot Table) | Stacked Bar; Labels = Project; Values = one per status |
| 31, 32, 33 | Role pages | Yes | Existing filters | Recipe 4.17: several small macros in page layout columns | A chart per panel where the paper shows one |
| 34 | Hygiene trend | Yes, typed | A typed table, one row per month: Month, and one column per hygiene filter | No SQL. Someone types the counts monthly. | Line; Labels = Month |
| 35 | Rollout plan | Yes, typed | A typed table: Task, Start, End | No SQL | Gantt |

Check the list of chart types in your version of Chart from Table before promising a style; the names above are the common ones.

### 8.1 WIP against limits

T1 = Jira Issues macro on `VS: open VS Epics` with Status. T2 = typed table: `Status`, `Limit`.

```sql
SELECT T1.'Status', COUNT(*) AS 'VS Epics', T2.'Limit'
FROM T1
LEFT JOIN T2 ON T2.'Status' = T1.'Status'
GROUP BY T1.'Status', T2.'Limit'
```

### 8.2 RAID by type and RAG, and the risk grid

T1 = Jira Issues macro on `VS: open RAID` with RAID Type, RAG Status, Probability, Impact.

```sql
SELECT T1.'RAID Type',
  SUM(IF(T1.'RAG Status' = "Green", 1, 0)) AS 'Green',
  SUM(IF(T1.'RAG Status' = "Amber", 1, 0)) AS 'Amber',
  SUM(IF(T1.'RAG Status' = "Red", 1, 0)) AS 'Red'
FROM T1
GROUP BY T1.'RAID Type'
```

For the risk grid, use a Pivot Table on the same macro filtered to risks: rows = Probability, columns = Impact, operation = Count.

### 8.3 Release readiness

T1 = Jira Issues macro on `Release: scope` with Project, Status, Issue Type, Severity.

```sql
SELECT T1.'Project' AS 'Application',
  SUM(IF(T1.'Status' = "Done", 1, 0)) AS 'Done',
  SUM(IF(T1.'Status' = "In Progress", 1, 0)) AS 'In progress',
  SUM(IF(T1.'Status' = "Backlog", 1, 0)) AS 'Not started'
FROM T1
GROUP BY T1.'Project'
```

Open bugs by severity: a Pivot Table on `Release: open bugs`, rows = Severity, operation = Count.

### 8.4 PI velocity by application

One Jira Issues macro per PI is the simplest way to stay under the row limit. T1 = `issuetype in (Story, Bug) AND resolution = Done AND resolved >= "2027-01-04" AND resolved <= "2027-03-26"` with Project and Story Points.

```sql
SELECT T1.'Project' AS 'Application', SUM(T1.'Story Points') AS 'PI 2027.1'
FROM T1
GROUP BY T1.'Project'
```

Paste the result into a typed "Velocity" table with one column per PI at each PI close. That table then feeds recipe 4.6 and the chart.

### 8.5 Created against finished, by month

T1 = Jira Issues macro on `project = CLP AND issuetype = Feature AND created >= -180d` with Created. T2 = the same with `resolved >= -180d` and Resolved. Set both date columns to display as year and month in the Table Transformer date settings, or use FORMATDATE if your version has it.

```sql
SELECT FORMATDATE(T1.'Created', "yyyy-MM") AS 'Month', COUNT(*) AS 'Created'
FROM T1
GROUP BY FORMATDATE(T1.'Created', "yyyy-MM")
ORDER BY 'Month'
```

Run the same query on T2 for 'Finished', and chart the two side by side. If the date function is not available in your version, the Jira gadget Created vs Resolved shows the same thing with no build.

### What to tell people who expect "every chart"

| Expectation | Answer |
| --- | --- |
| Every data chart in the paper can be on Confluence | Yes, with the caveats in the table above |
| They will look exactly like the paper | No. Expect standard bars, lines and tables. The paper's figures were drawn to explain, not exported from Confluence. |
| They are all live | Most are. Four rely on a typed table: success measures, burn-up, hygiene trend, velocity history. |
| They update as people type | No. A page shows fresh data when it is reloaded. |
| Any size of data | No. Each Jira Issues macro shows about 1,000 issues at most, so each is kept to one PI or one level. |
