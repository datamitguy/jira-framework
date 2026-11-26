# Loading a list of summaries into Jira

This guide explains how to turn a spreadsheet of summaries into VS Epics, Features, Epics and Stories in Jira Data Center, joined into the hierarchy. It goes with `jira-import-template.xlsx` and the CSV files in `csv/`.

Nothing here has been run in your Jira. Try it first with five rows in a test project.

## How each level maps to Jira

| Framework level | Jira issue type | Project | Joined to its parent by | What goes in that column |
| --- | --- | --- | --- | --- |
| Value stream outcome | VS Epic | Portfolio project | (top level) | |
| Capability across applications | Feature | Portfolio project | Parent Link | The **key** of the VS Epic, for example `CLP-12` |
| One application's share | Epic | Application project | Parent Link | The **key** of the Feature |
| Team work | Story, Task, Bug, Test | Application project | Epic Link | The **Epic Name** of the Epic, as text |
| Step in a story | Sub-task | Application project | Parent Id | The Issue Id of the parent row in the same file |
| A date that matters | Milestone | Portfolio project | Issue link "blocks" | Key of the Feature or VS Epic, in a second pass |
| Risk, assumption, issue, dependency | Delivery RAID | Portfolio project | Issue link "relates to" | Key of the ticket it concerns, in a second pass |

The same table is in the workbook on the **IssueTypeMap** sheet.

## Why it takes several passes

Parent Link needs the parent's key, and a key exists only after the parent has been created. So you import top-down: VS Epics, then Features, then Epics, then Stories. After each pass you bring the new keys back into the workbook, and the next sheet fills in its Parent Link column by itself.

## Two import routes

| Route | Where | Who | Use it for |
| --- | --- | --- | --- |
| Import issues from CSV | **Issues > Import issues from CSV** | Any user with create permission | Simple lists. Atlassian's guidance says not to use it for the hierarchy import. |
| External System Import | **Administration > System > External system import > CSV** | Jira admin | The hierarchy. This is the route Atlassian documents for Parent Link. |

If you are not an admin, you have two choices: ask the admin to run the files you prepare, or import the tickets with the user route without Parent Link and then set the parents in the plan by dragging each ticket under its parent (changes in a plan are saved to Jira with **Review changes**).

## Step by step

**Before you start**

1. In the workbook, replace the mock data with your own. Keep the header names, or change them to match your field names exactly.
2. Check that every value you use exists in Jira: issue type names, project keys, Target PI values, RAG values, Enabler Type values, component and version names. The import can fail on a value that does not exist.
3. Check that the fields are on the create screen of that issue type in that project. A field that is not on the screen is not offered in the mapping step.
4. Keep summaries unique. The workbook matches parents by summary.

**Pass 1: VS Epics**

1. Open the **VS_Epics** sheet. **File > Save As > CSV UTF-8**. Jira takes CSV, not .xlsx.
2. Start the import, choose the file, and choose the portfolio project.
3. Map the columns: Summary to Summary, Issue Type to Issue Type, and each field column to its field. Leave helper columns ("check only", "helper") unmapped.
4. Tick **Map field value** for Issue Type if the wizard asks, and confirm "VS Epic" maps to your VS Epic type.
5. Enter the date format the file uses: `yyyy-MM-dd` for the mock data.
6. Run it. At the end, **save the configuration**: the next file with the same columns can reuse it.

**Bring the keys back**

1. In Jira, search `project = CLP AND issuetype = "VS Epic" AND created >= -1d`.
2. **Export > CSV (current fields)** with just Summary and Key, or copy the two columns from the list.
3. Paste into the **KeyMap** sheet: Summary in column A, Key in column B. Add to the bottom each time; do not replace earlier rows.

**Pass 2: Features**

1. Open the **Features** sheet. The yellow **Parent Link** column now shows VS Epic keys. If a cell is blank, the parent summary does not match a row in KeyMap exactly.
2. Save as CSV and import into the portfolio project. Map **Parent Link** to Parent Link.
3. Bring the Feature keys back into KeyMap.

**Pass 3: Epics**

1. Open the **Epics** sheet. Parent Link shows Feature keys.
2. Epics need **Epic Name**. The mock data sets it equal to the summary.
3. Epics go to different application projects. The **Project Key** column carries the project; map it in the wizard so one file can feed several projects, or split the file by project if your wizard asks for a single project.
4. Import. Bring the Epic keys back into KeyMap only if you will link Milestones or RAID to Epics.

**Pass 4: Stories**

1. Open the **Stories** sheet. **Epic Link** holds the Epic Name as text, not a key.
2. Import into the application projects.

**Pass 5: Milestones and Delivery RAID**

1. Import the tickets first, without links.
2. Then import the links in a second file: one column with the key of the ticket, one column with the key it links to. In the mapping step, map the second column to the link type ("blocks" or "relates to"). Only the outward direction can be imported, so for "Feature blocks Milestone" the row is the Feature's key with the Milestone's key in the link column.
3. A link to a key that does not exist is skipped without a message, and running the same link file twice creates duplicate links.

## How values are written in the file

| Kind of field | How to write it |
| --- | --- |
| Labels | Several labels in one cell separated by spaces: `pi-committed ms-golive` |
| Components, Fix versions, other multi-value fields | One column per value, repeating the same header |
| Dates | One format for the whole file, declared in the wizard (`yyyy-MM-dd` in the mock data) |
| Two-step dropdown (value stream, then sub value stream) | `Value stream -> Sub value stream` in one cell. Confirm on one row; some set-ups need two columns. |
| Status | Only the admin route can set a status on import. Otherwise tickets start in the first status. |
| Clearing a value on update | `<<!clear!>>` |
| Updating existing tickets | Add an Issue Key column. Columns you do not map are left alone only if unmapped; mapped blank cells can reset values. Test on one ticket. |

Text encoding is UTF-8 by default.

## If it fails

| Message or symptom | Usual cause |
| --- | --- |
| The Next button stays greyed out | No column is mapped to Summary |
| A field is missing from the mapping list | The field is not on the create screen for that issue type |
| "Value is not valid" | The cell holds a value that is not an option of that dropdown, or the wrong capitals |
| Parent Link is ignored or errors | The parent key does not exist yet, the parent is not one level above, or the user route was used |
| Stories are not attached to their Epic | Epic Link holds a key or a summary that is not the Epic Name |
| Tickets land in the wrong project with new keys | Project key in the file does not match |
| Rows are skipped | Duplicate Issue Id in the file |

## After the import

1. Run `"Parent Link" is EMPTY` for Features and Epics in the projects you loaded. It should return nothing.
2. Open the plan. Each VS Epic should open to its Features, and each Feature to its Epics across applications.
3. Open the dashboards. With the mock data, two Features are Amber and one is Red, and several Epics are Released while their Features are still open, so the spillover and partial-delivery views have something to show once you set an older Target PI on one of them.
