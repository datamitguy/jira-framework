# Bringing the portfolio into Confluence

Jira dashboards count tickets in one list. They cannot walk the line VS Epic > Feature > Epic and add things up along it. Confluence can, using the Jira Issues macro for the data and Table Transformer for the roll-up, which works like SQL over the tables on the page.

This guide gives the page tree, the building blocks, a playground you can build today with mock tables and no Jira, and the query for each portfolio page.

**Status of the queries.** They are written from the vendor's documentation for Table Transformer (Data Center edition) and have not been run. Build each one on a scratch page first. Where a pattern is not shown in the vendor's documentation, it is marked "untested pattern".

## 1. The page tree

One parent page per value stream, top-down, same order as the Jira dashboards.

```text
Credit and Lending portfolio                 (landing page: roadmap + exceptions)
├── 1 VS Epics: outcomes and health          (portfolio tree, level 1 to 2)
├── 2 Features across the value stream       (level 2 to 3, by application)
├── 3 Epics across applications              (pivot by application and status)
├── 4 PI scorecards
│     ├── PI 2027.1 scorecard                (one page per PI, never edited after PI end)
│     └── PI 2027.2 scorecard
├── 5 Investment mix
├── 6 Predictability trend
├── 7 Milestones and slippage
├── 8 Size and forecast by VS Epic
├── 9 Weekly status (Red and Amber)
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
  T2.'Project Key' AS 'Application', T2.'Status', T2.'RAG Status', T2.'Due Date'
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

T1 = Jira Issues macro on `VS: cross-stream dependencies`, columns Key, Summary, Value Stream and Sub-Value Stream, Supplier Value Stream and Sub Value Stream, Due date, RAG Status. A **Pivot Table** with Row labels = the receiver field, Column labels = the supplier field, Operation = Count, shows who is waiting on whom at a glance.

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
