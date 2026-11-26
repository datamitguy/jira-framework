# Jira framework for a value stream portfolio

A working set of documents for running product and delivery operations across many applications in Jira Data Center, with the PI plan, dependencies and portfolio reporting in Confluence. Plans is used for the roadmap only.

The line everything follows is top-down: **VS Epic > Feature > Epic > Story**. Views start at the value stream, then show Features across the whole value stream, then Epics across applications. There are no separate views per sub value stream.

All project keys, names, dates and numbers in these files are placeholders or mock data.

## What is here

| File | What it is for | Read it when |
| --- | --- | --- |
| [whitepaper/WHITE_PAPER.md](whitepaper/WHITE_PAPER.md) | The white paper: the whole proposal in one structured document for every audience, from the value stream lead and heads of product and technology to teams and Jira administrators. 20 sections, 35 example charts and mock-ups (mock data), a reading guide by role, the decisions requested, and the implementation path. The chart images are in [whitepaper/charts/](whitepaper/charts/). A Word copy is at [whitepaper/One_Jira_White_Paper.docx](whitepaper/One_Jira_White_Paper.docx). | To circulate for review. Start here if you are new to the proposal. |
| [FRAMEWORK.md](FRAMEWORK.md) | The framework itself: structure, fields, workflows, RAID and milestones, portfolio practices, governance, operating rhythm, intake, PI planning, delivery control, release planning, dashboards, filter library, automation rules. | For the full detail behind the white paper. |
| [WAYS_OF_WORKING.md](WAYS_OF_WORKING.md) | What people do day to day: principles, who owns what, the weekly and PI rhythm, how work flows from demand to done, RAG rules, decisions, a weekly hygiene check and a 30-day start list. | To share with teams. It is the short companion to the framework. |
| [JIRA_UPDATE_GUIDE.md](JIRA_UPDATE_GUIDE.md) | For working-level people: what to update in Jira and when, by role, with a one-minute card, a field-by-field owner table and common mistakes. | To hand to engineers, testers, scrum masters and product owners. |
| [FIELDS.md](FIELDS.md) | The shortlist of fields the framework uses for each issue type, who fills each in and when, and which fields on the screen to leave alone. | When setting up screens, or when someone asks "do I need to fill this in?" |
| [PHASE_GATES.md](PHASE_GATES.md) | How to enter and exit each stage in Jira: new demand, triage, design, PI planning, delivery, testing, release, close. Also when the filters are created, what is edited at each PI, and what is kept up to date daily, weekly and per PI from Epic level upward. | When someone asks "what do I need to move this forward?" |
| [PROGRAMME_PLAN.md](PROGRAMME_PLAN.md) | How to land the change: the communication kit still to be written, the questions people will ask, success measures, and the work broken into six chunks, with Cloud migration as the second. | When planning the rollout. |
| [dashboards/DASHBOARD_BUILD_GUIDE.md](dashboards/DASHBOARD_BUILD_GUIDE.md) | Click-by-click steps to create the saved filters, the five dashboards and the two boards. | When you sit down to build in Jira. |
| [confluence/CONFLUENCE_PORTFOLIO_GUIDE.md](confluence/CONFLUENCE_PORTFOLIO_GUIDE.md) | The Confluence page tree and the SQL for each portfolio page, using the Jira Issues macro, Table Transformer, Pivot Table and Chart from Table. Includes a playground that works with mock tables and no Jira. | When you build the portfolio pages. |
| [import/IMPORT_GUIDE.md](import/IMPORT_GUIDE.md) | How to load a spreadsheet of summaries into Jira as a joined hierarchy, with the issue type mapping. | When you load real or mock data. |
| [import/jira-import-template.xlsx](import/jira-import-template.xlsx) | The workbook: one sheet per level with mock data, an issue type map, and a key map that fills in parent links. | With the import guide. |
| [import/csv/](import/csv/) | The same mock data as CSV files. | If you cannot open the workbook. |

## Suggested order for a first try

1. Read the first four sections of FRAMEWORK.md (at a glance, set-up, structure, stitching).
2. Build the Confluence playground with the mock tables (Confluence guide, section 3). It needs no Jira access and shows what the portfolio pages will look like.
3. Load the mock data into a test project (import guide).
4. Build the base filters and dashboard 1 (dashboard guide, steps 1 to 6).
5. Point the Confluence recipes at the live filters.

## What has and has not been checked

- The framework was reviewed by an independent pass for contradictions, and its technical claims were checked against Atlassian and add-on vendor documentation where those pages could be read.
- No query, import or Confluence recipe has been run against a real Jira or Confluence. Each guide ends with a checklist of what to test.
- Field names follow one organisation's standards list and were read from a photo of it. Check them letter for letter.
- Several behaviours could not be confirmed from documentation: whether a two-step dropdown works as a dashboard gadget axis, the exact row limit of the Jira Issues macro, and the automation rule that copies a field from a parent to a child. Each is flagged where it is used.
