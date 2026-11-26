import csv, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

out = sys.argv[1]
VS = "Credit and Lending"
def svs(x): return f"{VS} -> {x}"

vs_epics = [
 ("Avoid audit risk through access control","Access to every credit decision step is controlled and evidenced, closing the open audit points.","Governance and Conditions","Green","2027-12-17","regulatory",13,13,8,8),
 ("One view of conditions from approval to drawdown","Conditions set at approval are visible and enforced at drawdown without re-keying.","Drawdown","Amber","2027-09-24","",8,5,5,13),
 ("Earlier warning on deteriorating exposures","Relationship managers see watch-list triggers a month sooner.","Monitoring","Green","2028-03-31","",8,8,5,8),
 ("Run and improve 2027","Standing home for upkeep work. No Target PI, no commitment.","Underwriting","Green","2027-12-31","",1,1,1,1),
]
features = [
 # summary, parent, svs, enabler, target PI, RAG, due, label, tshirt, scores(bv,tc,rr,js)
 ("M&P across the platform","Avoid audit risk through access control","Governance and Conditions","","PI 2027.1","Green","2027-03-26","pi-committed","L",13,13,8,8),
 ("Access review evidence pack","Avoid audit risk through access control","Governance and Conditions","Compliance","PI 2027.2","Green","2027-06-18","pi-committed","M",8,13,8,5),
 ("Conditions carried into drawdown checks","One view of conditions from approval to drawdown","Drawdown","","PI 2027.1","Amber","2027-03-26","pi-committed","L",8,5,5,8),
 ("Facility letter generated from approved terms","One view of conditions from approval to drawdown","Facility Letter","","PI 2027.2","Green","2027-06-18","pi-stretch","M",5,3,3,5),
 ("Watch-list triggers from covenant breaches","Earlier warning on deteriorating exposures","Monitoring","","PI 2027.1","Red","2027-03-26","pi-committed","L",8,8,5,8),
 ("Forbearance cases linked to problem exposures","Earlier warning on deteriorating exposures","Forbearance","","PI 2027.2","Green","2027-06-18","pi-committed","M",5,5,3,5),
 ("Shared event stream for exposure changes","Earlier warning on deteriorating exposures","Monitoring","Architecture","PI 2027.1","Green","2027-03-26","pi-committed","M",3,5,8,5),
 ("Run and improve: platform upkeep","Run and improve 2027","Underwriting","","","Green","2027-12-31","","",1,1,1,1),
]
epics = [
 # summary, project, parent feature, target PI, RAG, SP, label, component, fixVersion, due
 ("M&P for Credit Application","CA","M&P across the platform","PI 2027.1","Green",40,"pi-committed","Approval","CA 2027.03","2027-03-12"),
 ("M&P for Drawdowns","DRAW","M&P across the platform","PI 2027.1","Amber",55,"pi-committed","Drawdown Request","DRAW 2027.03","2027-03-19"),
 ("M&P for Facility Letter","FL","M&P across the platform","PI 2027.1","Green",21,"pi-committed","Letter Generation","FL 2027.03","2027-03-19"),
 ("Access evidence export for Credit Application","CA","Access review evidence pack","PI 2027.2","Green",21,"pi-committed","Approval","CA 2027.06","2027-06-11"),
 ("Access evidence export for Governance and Conditions","GC","Access review evidence pack","PI 2027.2","Green",34,"pi-committed","Conditions","GC 2027.06","2027-06-11"),
 ("Conditions API in Governance and Conditions","GC","Conditions carried into drawdown checks","PI 2027.1","Amber",34,"pi-committed","Conditions","GC 2027.03","2027-02-26"),
 ("Drawdown pre-checks read conditions","DRAW","Conditions carried into drawdown checks","PI 2027.1","Amber",40,"pi-committed","Drawdown Request","DRAW 2027.03","2027-03-19"),
 ("Letter template reads approved terms","FL","Facility letter generated from approved terms","PI 2027.2","Green",30,"pi-stretch","Letter Generation","FL 2027.06","2027-06-11"),
 ("Approved terms published by Credit Application","CA","Facility letter generated from approved terms","PI 2027.2","Green",21,"pi-stretch","Facility","CA 2027.06","2027-05-28"),
 ("Covenant breach trigger in Watch and Worry Monitor","WWM","Watch-list triggers from covenant breaches","PI 2027.1","Red",55,"pi-committed","Triggers","WWM 2027.03","2027-03-19"),
 ("Covenant data feed from Governance and Conditions","GC","Watch-list triggers from covenant breaches","PI 2027.1","Amber",21,"pi-committed","Conditions","GC 2027.03","2027-02-26"),
 ("Problem exposure link in Forbearance","FORB","Forbearance cases linked to problem exposures","PI 2027.2","Green",30,"pi-committed","Case","FORB 2027.06","2027-06-11"),
 ("Case reference exposed by Problem Exposure Management","PEM","Forbearance cases linked to problem exposures","PI 2027.2","Green",21,"pi-committed","Exposure","PEM 2027.06","2027-05-28"),
 ("Exposure change events published by Watch and Worry Monitor","WWM","Shared event stream for exposure changes","PI 2027.1","Green",34,"pi-committed","Events","WWM 2027.03","2027-03-12"),
 ("Exposure change events consumed by Problem Exposure Management","PEM","Shared event stream for exposure changes","PI 2027.1","Green",21,"pi-committed","Exposure","PEM 2027.03","2027-03-19"),
 ("Library upgrades for Drawdowns","DRAW","Run and improve: platform upkeep","","Green",13,"","Platform","DRAW 2027.03","2027-03-19"),
]
stories = [
 ("Second approver must differ from first approver","CA","M&P for Credit Application",5,"Story"),
 ("Approval history shows both approvers","CA","M&P for Credit Application",3,"Story"),
 ("Reject own submission at approval step","CA","M&P for Credit Application",3,"Story"),
 ("Drawdown request needs a second approver","DRAW","M&P for Drawdowns",8,"Story"),
 ("Approver cannot edit amount after first approval","DRAW","M&P for Drawdowns",5,"Story"),
 ("Second approver sees stale amount after edit","DRAW","M&P for Drawdowns",3,"Bug"),
 ("Trigger fires when covenant test fails","WWM","Covenant breach trigger in Watch and Worry Monitor",8,"Story"),
 ("Trigger suppressed for waived covenants","WWM","Covenant breach trigger in Watch and Worry Monitor",5,"Story"),
]
milestones = [
 ("Audit point AP-12 remediation due","Governance and Conditions","2027-06-30","2027-06-30","Green","ms-regulatory","Avoid audit risk through access control"),
 ("M&P live in all origination applications","Governance and Conditions","2027-03-26","2027-03-26","Amber","ms-golive","M&P across the platform"),
 ("Covenant triggers live for pilot business line","Monitoring","2027-04-09","2027-03-26","Red","ms-golive","Watch-list triggers from covenant breaches"),
 ("PI 2027.2 planning","Underwriting","2027-03-22","2027-03-22","Green","ms-pi",""),
]
raid = [
 # summary, raid type, svs (receiver), supplier svs, RAG, probability, impact, roam, due, relates to
 ("Drawdowns team loses two engineers in February","Risk","Drawdown","", "Amber","High","High","Owned","2027-01-29","M&P for Drawdowns"),
 ("Conditions API needed by Drawdowns before sprint 3","Dependency","Drawdown","Governance and Conditions","Amber","","High","","2027-02-12","Drawdown pre-checks read conditions"),
 ("Covenant data quality is unknown for legacy facilities","Assumption","Monitoring","","Amber","","Medium","","2027-01-22","Watch-list triggers from covenant breaches"),
 ("Covenant feed test environment not available","Issue","Monitoring","Governance and Conditions","Red","","High","","2027-01-15","Covenant breach trigger in Watch and Worry Monitor"),
 ("Audit may widen scope of AP-12 to drawdown approvals","Risk","Governance and Conditions","","Green","Low","High","Accepted","2027-03-05","Avoid audit risk through access control"),
]

wb = Workbook()
hdr_font = Font(bold=True, color="FFFFFF"); hdr_fill = PatternFill("solid", fgColor="1F4E78")
calc_fill = PatternFill("solid", fgColor="FFF2CC")
def sheet(name, headers, rows, calc_cols=()):
    ws = wb.create_sheet(name)
    ws.append(headers)
    for c in range(1, len(headers)+1):
        cell = ws.cell(row=1, column=c); cell.font = hdr_font; cell.fill = hdr_fill
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    for r in rows: ws.append(list(r))
    for i, h in enumerate(headers, 1):
        width = max([len(str(h))] + [len(str(r[i-1])) for r in rows if not str(r[i-1]).startswith("=")])
        ws.column_dimensions[get_column_letter(i)].width = min(max(width + 2, 12), 60)
        if h in calc_cols:
            for rr in range(2, len(rows)+2): ws.cell(row=rr, column=i).fill = calc_fill
    ws.freeze_panes = "A2"
    return ws

def lookup(col, row): return f'=IFERROR(INDEX(KeyMap!$B:$B,MATCH({col}{row},KeyMap!$A:$A,0)),"")'

# README
ws = wb.active; ws.title = "README"
lines = [
 "Jira import template and mock data",
 "",
 "What this is: one sheet per level of the hierarchy, top-down. Each sheet is a list of summaries with the Jira issue type and the fields the framework uses.",
 "All names, dates and numbers are invented mock data. Replace them with your own.",
 "",
 "How to use it (details in import/IMPORT_GUIDE.md):",
 "1. Check the IssueTypeMap sheet against your Jira: issue type names, project keys and field names must match exactly.",
 "2. Import top-down, one sheet at a time: VS_Epics, then Features, then Epics, then Stories. Save the sheet as CSV (UTF-8) and import it. Jira accepts CSV, not .xlsx.",
 "3. After each import, export Summary and Key of the new issues from Jira and paste them into the KeyMap sheet (column A Summary, column B Key).",
 "4. The yellow 'Parent Link' columns then fill in by themselves from KeyMap, using the 'Parent summary' column. Summaries must be unique.",
 "   Stories are different: their 'Epic Link' column holds the Epic Name as text, not a key, so it needs no lookup.",
 "5. Milestones and Delivery_RAID are imported last. Their 'Linked to' column fills in the same way.",
 "",
 "Yellow cells are formulas. Do not type over them. Before saving a sheet as CSV, check they show issue keys, not blanks.",
 "The 'Parent summary' and 'Linked to (summary)' columns are helpers for you; leave them unmapped when importing.",
 "Sub value stream is written as 'Value stream -> Sub value stream', the form Jira's CSV import uses for a two-step dropdown. Confirm on one row first.",
 "",
 "To play with Confluence before Jira is ready: paste the Features and Epics sheets into a Confluence page as tables and follow confluence/CONFLUENCE_PORTFOLIO_GUIDE.md.",
]
for l in lines: ws.append([l])
ws["A1"].font = Font(bold=True, size=14); ws.column_dimensions["A"].width = 140

sheet("IssueTypeMap",
 ["Framework level","Jira issue type","Jira project","Joined to its parent by","Parent is a","Sheet in this workbook","Must have before import"],
 [("L1 Value stream outcome","VS Epic","Portfolio project (CLP)","Parent Link: none (top level)","-","VS_Epics","Summary, Issue Type"),
  ("L2 Capability across applications","Feature","Portfolio project (CLP)","Parent Link = key of the VS Epic","VS Epic","Features","Summary, Issue Type, Parent Link"),
  ("L3 One application's share","Epic","Application project (CA, DRAW, FL, GC, WWM, PEM, FORB)","Parent Link = key of the Feature","Feature","Epics","Summary, Epic Name, Issue Type, Parent Link"),
  ("L4 Team work","Story / Task / Bug / Test","Application project","Epic Link = Epic Name of the Epic (text, not key)","Epic","Stories","Summary, Issue Type, Epic Link"),
  ("L5 Step inside a story","Sub-task","Application project","Parent Id column (same file as its parent)","Story","(not in the mock data)","Summary, Issue Type, Issue Id, Parent Id"),
  ("Side: a date that matters","Milestone","Portfolio project (CLP)","Issue link 'blocks' from the Feature or VS Epic","-","Milestones","Summary, Issue Type, Due Date"),
  ("Side: risk, assumption, issue, dependency","Delivery RAID","Portfolio project (CLP)","Issue link 'relates to'","-","Delivery_RAID","Summary, Issue Type, RAID Type")])

FIELD_ROWS = [('VS Epic (16 core)', 'Summary, Description, Assignee, Value Stream and Sub-Value Stream, Objective ID, Business Benefits, the four scores, Start date, End Date, Due date, RAG Status, Executive Summary, Linked work items', 'Path to Green, Date to Green, Financial Benefit (USD), Regulatory or Control ID, Change Reason, Flagged', 'Weighted Shortest Job First Score'), ('Feature (17 core)', 'Summary, Description, Assignee, Parent Link, Value Stream and Sub-Value Stream, Enabler Type, Acceptance Criteria, Business Benefits, T-Shirt Size, the four scores, Target PI, Labels, Due date, RAG Status', 'Start date, End Date, Path to Green, Date to Green, Management Attention, Executive Summary, Regulatory or Control Change Type, Regulatory or Control ID, Architectural Governance, Contains Resiliency Work, Change Reason, Linked work items, Flagged', 'Actual PI, Weighted Shortest Job First Score'), ('Epic (14 core)', 'Summary, Epic Name, Description, Assignee, Parent Link, Components, Team, Story Points, Target PI, Labels, End Date, RAG Status, Fix versions, Linked work items', 'Start date, Change Request ID, Regulatory or Control Change Type, Flagged', 'Actual PI, Value Stream and Sub-Value Stream'), ('Story (8 core)', 'Summary, Description, Epic Link, Acceptance Criteria, Story Points, Assignee, Sprint, Components', 'Fix versions, Story Type, Flagged', 'Status, Resolution'), ('Task (6 core)', 'Summary, Description, Epic Link, Assignee, Sprint, Story Points', 'Acceptance Criteria, Flagged', 'Status, Resolution'), ('Sub-task (3 core)', 'Summary, Assignee, Parent', 'Flagged', 'Status'), ('Bug (11 core)', 'Summary, Description, Epic Link, Severity, Priority, Testing Phase, Environment, Affects versions, Assignee, Sprint, Components', 'Fix versions, Root cause category, Root cause analysis, Flagged', 'Status, Resolution'), ('Test (7 core)', 'Summary, Description, Epic Link, Testing Phase, Environments, Assignee, Sprint', 'Fix versions', 'Status, Resolution'), ('Milestone (9 core)', 'Summary, Description, Assignee, Value Stream and Sub-Value Stream, Due date, Baseline End Date, RAG Status, Labels, Linked work items', 'Path to Green, Date to Green, Executive Summary, Regulatory or Control ID, Fix versions', ''), ('Delivery RAID (10 core)', 'Summary, Description, RAID Type, Assignee, Value Stream and Sub-Value Stream, Components, RAG Status, Due date, Impact, Linked work items', 'Risk: Probability, Risk Trigger Event, ROAM Response. Dependency: Dependency Type, Supplier Value Stream and Sub Value Stream, Baseline End Date. Issue: Impact Details, Path to Green, Date to Green. Any: Executive Summary', '')]
sheet("Fields",["Issue type","Core fields (always)","Only when it applies","Set by Jira or automation"],FIELD_ROWS)
sheet("KeyMap", ["Summary (paste from Jira export)","Key (paste from Jira export)"], [("(example) M&P across the platform","CLP-101")])

vs_extra = {vs_epics[0][0]:("Implementing","2027-01-04","2027-12-17"), vs_epics[1][0]:("Implementing","2027-01-04","2027-09-24"),
            vs_epics[2][0]:("Implementing","2027-01-04","2028-03-31"), vs_epics[3][0]:("Implementing","2027-01-04","2027-12-31")}
rows = [(s,"VS Epic","CLP",vs_extra[s][0],d,svs(v),rag,vs_extra[s][1],vs_extra[s][2],due,lab,bv,tc,rr,js,f"=ROUND((L{i}+M{i}+N{i})/O{i},1)") for i,(s,d,v,rag,due,lab,bv,tc,rr,js) in enumerate(vs_epics,2)]
sheet("VS_Epics",["Summary","Issue Type","Project Key","Status","Description","Value Stream and Sub-Value Stream","RAG Status","Start Date","End Date","Due Date","Labels","User/Business Value Score","Time Criticality Score","Risk Reduction / Opportunity Enablement Score","Job Size Score","WSJF (check only)"],rows,calc_cols=("WSJF (check only)",))

pi_dates = {"PI 2027.1":("2027-01-04","2027-03-26"), "PI 2027.2":("2027-03-29","2027-06-18"), "":("2027-01-04","2027-12-31")}
f_status = ["Implementing","Ready","Implementing","Ready","Implementing","Ready","Implementing","Implementing"]
rows = [(s,"Feature","CLP",f_status[i-2],p,lookup("E",i),svs(v),en,pi,"",rag,pi_dates[pi][0],pi_dates[pi][1],due,lab,ts,bv,tc,rr,js,f"=ROUND((Q{i}+R{i}+S{i})/T{i},1)") for i,(s,p,v,en,pi,rag,due,lab,ts,bv,tc,rr,js) in enumerate(features,2)]
sheet("Features",["Summary","Issue Type","Project Key","Status","Parent summary (helper)","Parent Link","Value Stream and Sub-Value Stream","Enabler Type","Target PI","Actual PI","RAG Status","Start Date","End Date","Due Date","Labels","T-Shirt Size","User/Business Value Score","Time Criticality Score","Risk Reduction / Opportunity Enablement Score","Job Size Score","WSJF (check only)"],rows,calc_cols=("Parent Link","WSJF (check only)"))

feat_svs = {f[0]: f[2] for f in features}
e_status = ["Released","Implementing","Released","Ready","Ready","Implementing","Implementing","Ready","Ready","Implementing","Released","Ready","Analysis","Released","Implementing","Implementing"]
rows = [(s,s,"Epic",proj,e_status[i-2],p,lookup("F",i),svs(feat_svs[p]),pi,(pi if e_status[i-2]=="Released" else ""),rag,sp,lab,comp,fv,due) for i,(s,proj,p,pi,rag,sp,lab,comp,fv,due) in enumerate(epics,2)]
sheet("Epics",["Summary","Epic Name","Issue Type","Project Key","Status","Parent summary (helper)","Parent Link","Value Stream and Sub-Value Stream","Target PI","Actual PI","RAG Status","Story Points","Labels","Component","Fix Version","End Date"],rows,calc_cols=("Parent Link",))

sheet("Velocity",["Project Key","PI velocity (story points per PI)"],[("CA",60),("DRAW",45),("FL",40),("GC",50),("WWM",55),("PEM",40),("FORB",35)])

rows = [(s,t,proj,p,sp) for i,(s,proj,p,sp,t) in enumerate(stories,2)]
sheet("Stories",["Summary","Issue Type","Project Key","Epic Link","Story Points"],rows)

rows = [(s,"Milestone","CLP",svs(v),due,base,rag,lab,link,lookup("I",i)) for i,(s,v,due,base,rag,lab,link) in enumerate(milestones,2)]
sheet("Milestones",["Summary","Issue Type","Project Key","Value Stream and Sub-Value Stream","Due Date","Baseline End Date","RAG Status","Labels","Blocked by (summary, helper)","Blocked by (key)"],rows,calc_cols=("Blocked by (key)",))

# On a dependency: Due Date = the date the receiver needs it; Baseline End Date = the date the supplier promised.
# Status Backlog = asked, not agreed; In Progress = agreed.
RAID_EXTRA = {"Conditions API needed by Drawdowns before sprint 3": ("In Progress", "2027-02-26"),
              "Covenant feed test environment not available": ("In Progress", ""),
              "Drawdowns team loses two engineers in February": ("In Progress", ""),
              "Audit may widen scope of AP-12 to drawdown approvals": ("In Progress", "")}
raid = raid + [("Exposure identifiers shared with Forbearance","Dependency","Forbearance","Monitoring","Green","","Medium","","2027-03-12","Forbearance cases linked to problem exposures"),
               ("Approved terms available to the facility letter template","Dependency","Facility Letter","Underwriting","Green","","Medium","","2027-02-19","Facility letter generated from approved terms")]
RAID_EXTRA["Approved terms available to the facility letter template"] = ("In Progress", "2027-02-05")
rows = [(s,"Delivery RAID","CLP",t,svs(v),(svs(sup) if sup else ""),RAID_EXTRA.get(s,("Backlog",""))[0],rag,prob,imp,roam,due,RAID_EXTRA.get(s,("Backlog",""))[1],link,lookup("N",i)) for i,(s,t,v,sup,rag,prob,imp,roam,due,link) in enumerate(raid,2)]
sheet("Delivery_RAID",["Summary","Issue Type","Project Key","RAID Type","Value Stream and Sub-Value Stream","Supplier Value Stream and Sub Value Stream","Status","RAG Status","Probability","Impact","ROAM Response","Due Date","Baseline End Date","Relates to (summary, helper)","Relates to (key)"],rows,calc_cols=("Relates to (key)",))

wb.save(out + "/jira-import-template.xlsx")

# plain CSVs of the mock data (formula columns left blank, to fill after KeyMap)
for ws in wb.worksheets:
    if ws.title in ("README","IssueTypeMap","KeyMap","Fields"): continue
    with open(f"{out}/csv/{ws.title}.csv","w",newline="",encoding="utf-8") as f:
        w = csv.writer(f)
        for row in ws.iter_rows(values_only=True):
            w.writerow(["" if (isinstance(v,str) and v.startswith("=")) else ("" if v is None else v) for v in row])
print("ok", [ws.title for ws in wb.worksheets])
