"""Builds the single-project mock-up: import CSV, workbook, and the expected result of every filter.
Usage: python3 build_mockup.py <output dir>
Change KEY, CUR and PREV below to match the real project key and the real Target PI values, then run again."""
import csv, os, sys, datetime as dt

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
KEY = "CL123"                      # project key
CUR, PREV = "PI 2026.4", "PI 2026.3"   # current and previous PI, as the Target PI field writes them
REL = f"{KEY} 2027.01"             # release (Fix version) name
TODAY = dt.date(2026, 11, 27)
VS = "Credit and Lending"
def svs(x): return f"{VS} -> {x}"
def d(days): return (TODAY + dt.timedelta(days=days)).isoformat()

T = []  # tickets
def add(id, type, summary, status, **k):
    t = dict(id=id, type=type, summary=summary, status=status, parent="", comp="", target="", actual="", rag="", labels=["mock"],
             due="", end="", sp="", svs="", enabler="", scores="", mgmt="", reg="", ptg="", raid="", supplier="", prob="", impact="",
             roam="", baseline="", flag=False, fix="", epic="", sev="", links=[], assignee=True, sprint=False, resolution="")
    labels = k.pop("labels", [])
    t.update(k); t["labels"] = ["mock"] + labels
    if status in ("Done", "Released") and type not in ("Capability",): t["resolution"] = "Done"
    T.append(t)

# ---- Capabilities (the VS Epic level): 3
add("C1", "Capability", "Avoid audit risk through access control", "Implementing", rag="Amber", due=d(200), svs=svs("Governance and Conditions"),
    ptg="Drawdowns to borrow one engineer from Credit Application in January")
add("C2", "Capability", "Earlier warning on deteriorating exposures", "Implementing", rag="Red", due=d(300), svs=svs("Monitoring"),
    ptg="Group Data to name a covenant data owner by mid December")
add("C3", "Capability", "One view of conditions from approval to drawdown", "Analysis", rag="Green", due=d(380), svs=svs("Drawdown"))

# ---- Initiatives (the Feature level): 8
add("I1", "Initiative", "M&P across the platform", "Implementing", parent="C1", target=CUR, rag="Amber", labels=["pi-committed"], due=d(45),
    svs=svs("Governance and Conditions"), reg="Audit", scores="8,13,5,5", ptg="Drawdowns to borrow one engineer in January")
add("I2", "Initiative", "Access review evidence pack", "Released", parent="C1", target=CUR, actual=CUR, rag="Green", labels=["pi-committed"], due=d(-5),
    svs=svs("Governance and Conditions"), scores="5,8,3,3")
add("I3", "Initiative", "Watch-list triggers from covenant breaches", "Implementing", parent="C2", target=CUR, rag="Red", labels=["pi-committed"], due=d(30),
    svs=svs("Monitoring"), mgmt="Yes", scores="13,8,8,8")
add("I4", "Initiative", "Conditions carried into drawdown checks", "Implementing", parent="C3", target=CUR, rag="Green", labels=["pi-committed"], due=d(50),
    svs=svs("Drawdown"), scores="8,5,5,5")
add("I5", "Initiative", "Covenant breach alerts by email", "Implementing", parent="C2", target=CUR, rag="Green", labels=["pi-stretch", "unplanned"], due=d(55),
    svs="", enabler="Enabler", scores="5,3,2,3")
add("I6", "Initiative", "Exposure roll-up by client group", "Idea", svs="", due="")
add("I7", "Initiative", "Facility letter generated from approved terms", "Implementing", parent="C3", target=PREV, rag="Amber", labels=["pi-committed"], due=d(20),
    svs=svs("Drawdown"), scores="8,8,3,5", ptg="Credit Application feed to finish in sprint 2")
add("I8", "Initiative", "Conditions change history for auditors", "Ready", parent="C1", rag="Green", svs=svs("Governance and Conditions"), scores="8,13,5,3")

# ---- Epics: 9. The application is the Component, because everything is in one project.
CA, DRAW, GC = "Credit Application", "Drawdowns", "Governance and Conditions"
add("E1", "Epic", "M&P for Credit Application", "Released", parent="I1", comp=CA, target=CUR, actual=CUR, rag="Green", labels=["pi-committed"], end=d(-10), sp=21, fix=REL, epic="M&P CA")
add("E2", "Epic", "M&P for Drawdowns", "Implementing", parent="I1", comp=DRAW, target=CUR, rag="Amber", labels=["pi-committed"], end=d(40), sp=34, fix=REL, epic="M&P DRAW",
    links=[("is blocked by", "E1")])
add("E3", "Epic", "Evidence pack for conditions", "Released", parent="I2", comp=GC, target=CUR, actual=CUR, rag="Green", labels=["pi-committed"], end=d(-6), sp=13, epic="Evidence GC")
add("E4", "Epic", "Covenant trigger rules", "Implementing", parent="I3", comp=GC, target=CUR, rag="Red", labels=["pi-committed"], end=d(28), sp=21, epic="Triggers GC", flag=True)
add("E5", "Epic", "Covenant alerts shown in Drawdowns", "Ready", parent="I3", comp=DRAW, target=CUR, rag="Green", labels=["pi-stretch"], end=d(42), sp=13, epic="Alerts DRAW",
    links=[("is blocked by", "E9")])
add("E6", "Epic", "Alert emails from Credit Application", "Implementing", parent="I5", comp=CA, target=CUR, rag="Green", labels=["pi-stretch", "unplanned"], end=d(50), sp=8, epic="Emails CA")
add("E7", "Epic", "Approved terms feed for the facility letter", "Implementing", parent="I7", comp=CA, target=PREV, rag="Amber", labels=["pi-committed"], end=d(18), sp=13, epic="Terms feed CA")
add("E8", "Epic", "Limit check rewrite", "Implementing", comp=DRAW, rag="Green", end=d(35), sp=8, epic="Limit check DRAW")
add("E9", "Epic", "Conditions API v2", "Implementing", parent="I4", comp=GC, target=CUR, rag="Green", labels=["pi-committed"], end=d(36), sp=21, epic="Conditions API GC")

# ---- Stories and Bugs: 8 (statuses Backlog, In Progress, Done)
add("S1", "Story", "Role checks on the drawdown approval screen", "In Progress", epic_link="E2", comp=DRAW, sp=5, fix=REL, sprint=True, flag=True)
add("S2", "Story", "Role model read from the shared service", "Done", epic_link="E2", comp=DRAW, sp=8, fix=REL, sprint=True)
add("S3", "Story", "Trigger rule for a missed covenant test", "In Progress", epic_link="E4", comp=GC, sp=5, sprint=True)
add("S4", "Story", "Email template for a covenant breach", "Backlog", epic_link="E6", comp=CA, sp=3, sprint=True)
add("S5", "Story", "Tidy up logging in limit checks", "Backlog", comp=DRAW, sp=2)
add("S6", "Story", "Approved terms mapped to letter fields", "Done", epic_link="E7", comp=CA, sp=5, sprint=True)
add("B1", "Bug", "Approver role not applied to joint facilities", "In Progress", epic_link="E2", comp=DRAW, sev="2", fix=REL, sprint=True)
add("B2", "Bug", "Evidence export misses archived conditions", "Done", epic_link="E3", comp=GC, sev="3")

# ---- Delivery RAID: 8. On a Dependency: Due = need-by date, Baseline End Date = date the supplier promised.
add("R1", "Delivery RAID", "Drawdowns needs Conditions API v2 before sprint 3", "In Progress", raid="Dependency", svs=svs("Drawdown"), supplier=svs("Governance and Conditions"),
    comp=DRAW, rag="Red", due=d(21), baseline=d(35), impact="High", links=[("relates to", "E5"), ("relates to", "E9")])
add("R2", "Delivery RAID", "Credit Application needs the covenant event feed for alert emails", "Backlog", raid="Dependency", svs=svs("Monitoring"), supplier=svs("Governance and Conditions"),
    comp=CA, rag="Amber", due=d(14), impact="Medium", links=[("relates to", "E6")])
add("R3", "Delivery RAID", "Drawdowns needs the evidence export format agreed", "In Progress", raid="Dependency", svs=svs("Drawdown"), supplier=svs("Governance and Conditions"),
    comp=DRAW, rag="Green", due=d(40), baseline=d(25), impact="Low", links=[("relates to", "E2"), ("relates to", "E3")])
add("R4", "Delivery RAID", "Covenant test environment needed from Group IT", "Backlog", raid="Dependency", svs=svs("Monitoring"), supplier="",
    comp=GC, rag="Amber", due=d(-4), impact="High", assignee=False, links=[("relates to", "E4")])
add("R5", "Delivery RAID", "Drawdowns loses two engineers in January", "In Progress", raid="Risk", svs=svs("Drawdown"), comp=DRAW, rag="Amber", due=d(10),
    prob="High", impact="High", roam="Owned", links=[("relates to", "I1")])
add("R6", "Delivery RAID", "Audit may widen the scope of the access finding", "Backlog", raid="Risk", svs=svs("Governance and Conditions"), comp=GC, rag="Green", due=d(-7),
    prob="Low", impact="High", links=[("relates to", "C1")])
add("R7", "Delivery RAID", "Covenant data for legacy facilities is incomplete", "In Progress", raid="Issue", svs=svs("Monitoring"), comp=GC, rag="Red", due=d(12),
    impact="High", ptg="Data owner to supply a corrected extract", links=[("relates to", "E4")])
add("R8", "Delivery RAID", "Group IT will keep the current role service until June", "Backlog", raid="Assumption", svs=svs("Governance and Conditions"), comp=CA, rag="Green", due=d(60),
    impact="Medium", links=[("relates to", "I1")])

# ---- Milestone stand-ins: 2 Tasks, because the Milestone issue type arrives with Jira Cloud
add("M1", "Task", "MILESTONE: audit point AP-12 remediation due", "In Progress", labels=["milestone", "ms-regulatory"], due=d(70), rag="Green", links=[("is blocked by", "I1")])
add("M2", "Task", "MILESTONE: M&P live in all origination applications", "In Progress", labels=["milestone", "ms-golive"], due=d(-3), rag="Amber", links=[("is blocked by", "I1")])

BY = {t["id"]: t for t in T}
for t in T: t.setdefault("epic_link", "")

# ------------------------------------------------------------------ expected results of each filter
def lab(t, l): return l in t["labels"]
def open_(t): return t["status"] not in ("Done", "Released")
def notdone(t): return t["status"] != "Done"          # statusCategory != Done, with Released kept in progress
F = {}
F["planned Initiatives"] = lambda t: t["type"] == "Initiative" and t["target"] == CUR
F["planned Epics"] = lambda t: t["type"] == "Epic" and t["target"] == CUR
F["MOCK: spillover"] = lambda t: t["type"] in ("Initiative", "Epic") and t["target"] == PREV and lab(t, "pi-committed") and open_(t)
F["MOCK: PI Epics"] = lambda t: F["planned Epics"](t) or (F["MOCK: spillover"](t) and t["type"] == "Epic") or (t["type"] == "Epic" and t["status"] == "Implementing")
F["MOCK: current PI Initiatives"] = lambda t: F["planned Initiatives"](t) or (t["type"] == "Initiative" and t["status"] in ("Implementing", "Testing", "Validation"))
F["MOCK: committed Initiatives"] = lambda t: F["planned Initiatives"](t) and lab(t, "pi-committed")
F["MOCK: committed and released"] = lambda t: F["MOCK: committed Initiatives"](t) and not open_(t)
F["MOCK: unplanned in PI"] = lambda t: F["planned Initiatives"](t) and lab(t, "unplanned")
F["MOCK: open Capabilities"] = lambda t: t["type"] == "Capability" and t["status"] not in ("Idea", "Done")
F["MOCK: all Initiatives"] = lambda t: t["type"] == "Initiative"
F["MOCK: Red and Amber"] = lambda t: (F["MOCK: current PI Initiatives"](t) or F["MOCK: PI Epics"](t) or F["MOCK: open Capabilities"](t)) and t["rag"] in ("Red", "Amber") and open_(t)
F["MOCK: Management Attention and Red"] = lambda t: t["type"] in ("Initiative", "Capability") and open_(t) and (t["mgmt"] or t["rag"] == "Red")
F["MOCK: Amber or Red without a plan"] = lambda t: F["MOCK: Red and Amber"](t) and t["type"] != "Epic" and not t["ptg"]
F["MOCK: intake waiting"] = lambda t: t["type"] in ("Initiative", "Capability") and t["status"] == "Idea"
F["MOCK: Ready, no Target PI"] = lambda t: t["type"] == "Initiative" and t["status"] == "Ready" and not t["target"]
F["MOCK: Initiatives with gaps"] = lambda t: t["type"] == "Initiative" and t["status"] not in ("Idea", "Analysis", "Done") and (not t["parent"] or not t["rag"] or not t["svs"])
F["MOCK: regulatory Initiatives"] = lambda t: t["type"] == "Initiative" and t["reg"] and open_(t)
F["MOCK: PI Epics not started"] = lambda t: F["MOCK: PI Epics"](t) and t["status"] in ("Idea", "Analysis", "Ready")
F["MOCK: flagged"] = lambda t: t["flag"]
F["MOCK: hygiene exceptions"] = lambda t: t["type"] == "Epic" and not t["parent"] and notdone(t)
F["MOCK: open RAID"] = lambda t: t["type"] == "Delivery RAID" and notdone(t)
F["MOCK: open Red and Amber RAID"] = lambda t: F["MOCK: open RAID"](t) and t["rag"] in ("Red", "Amber")
F["MOCK: risks not reviewed"] = lambda t: F["MOCK: open RAID"](t) and t["raid"] == "Risk" and not t["roam"]
F["MOCK: RAID past its date"] = lambda t: F["MOCK: open RAID"](t) and t["due"] and t["due"] < TODAY.isoformat()
F["MOCK: milestones next 90 days and overdue"] = lambda t: lab(t, "milestone") and notdone(t) and t["due"] <= d(90)
F["MOCK: open dependencies"] = lambda t: F["MOCK: open RAID"](t) and t["raid"] == "Dependency"
F["MOCK: dependencies not agreed"] = lambda t: F["MOCK: open dependencies"](t) and t["status"] == "Backlog"
F["MOCK: dependencies agreed"] = lambda t: F["MOCK: open dependencies"](t) and t["status"] == "In Progress"
F["MOCK: dependencies late or due soon"] = lambda t: F["MOCK: open dependencies"](t) and t["due"] <= d(28)
F["MOCK: dependencies at risk"] = lambda t: F["MOCK: open dependencies"](t) and t["rag"] in ("Red", "Amber")
F["MOCK: dependencies without an owner or date"] = lambda t: F["MOCK: open dependencies"](t) and (not t["assignee"] or not t["due"])
F["MOCK release: scope"] = lambda t: t["fix"] == REL
F["MOCK release: not finished"] = lambda t: t["fix"] == REL and open_(t)
F["MOCK release: open bugs"] = lambda t: t["fix"] == REL and t["type"] == "Bug" and notdone(t)
F["MOCK team: flagged in sprint"] = lambda t: t["sprint"] and t["flag"]
F["MOCK team: open Epics"] = lambda t: t["type"] == "Epic" and open_(t)
F["MOCK team: open bugs"] = lambda t: t["type"] == "Bug" and notdone(t)
F["MOCK team: Stories without Epic"] = lambda t: t["type"] in ("Story", "Task") and not t["epic_link"] and notdone(t) and not lab(t, "milestone")
EXPECT = {n: [t["id"] for t in T if f(t)] for n, f in F.items()}

# ------------------------------------------------------------------ files
os.makedirs(OUT, exist_ok=True)
COLS = ["Mock ID", "Issue Type", "Summary", "Status", "Epic Name", "Component", "Labels", "Target PI", "Actual PI", "RAG Status", "Due Date", "End Date",
        "Story Points", "Value Stream and Sub-Value Stream", "Enabler Type", "Scores (value, time, risk, size)", "Management Attention",
        "Regulatory or Control Change Type", "Path to Green", "RAID Type", "Supplier Value Stream and Sub Value Stream", "Probability", "Impact",
        "ROAM Response", "Baseline End Date", "Fix Version", "Severity", "Resolution",
        "SET BY HAND: parent (Parent Link)", "SET BY HAND: Epic Link", "SET BY HAND: links", "SET BY HAND: flag", "SET BY HAND: sprint", "SET BY HAND: leave unassigned"]
def row(t):
    return [t["id"], t["type"], t["summary"], t["status"], t["epic"], t["comp"], " ".join(t["labels"]), t["target"], t["actual"], t["rag"], t["due"], t["end"],
            t["sp"], t["svs"], t["enabler"], t["scores"], t["mgmt"], t["reg"], t["ptg"], t["raid"], t["supplier"], t["prob"], t["impact"], t["roam"],
            t["baseline"], t["fix"], t["sev"], t["resolution"],
            (f'{t["parent"]}: {BY[t["parent"]]["summary"]}' if t["parent"] else ""),
            (f'{t["epic_link"]}: {BY[t["epic_link"]]["summary"]}' if t["epic_link"] else ""),
            "; ".join(f"{k} {v}" for k, v in t["links"]), "Yes" if t["flag"] else "", "Yes" if t["sprint"] else "", "" if t["assignee"] else "Yes"]
with open(os.path.join(OUT, "mock_tickets.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(COLS); [w.writerow(row(t)) for t in T]

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    wb = Workbook(); ws = wb.active; ws.title = "Tickets"
    ws.append(COLS); [ws.append(row(t)) for t in T]
    for c in ws[1]:
        c.font = Font(bold=True); c.fill = PatternFill("solid", fgColor="FFF2CC" if c.value.startswith("SET BY HAND") else "DCE6F5"); c.alignment = Alignment(wrap_text=True, vertical="top")
    for col, wdt in zip("ABCDEFGHIJKLMN", [8, 14, 52, 14, 18, 26, 30, 12, 12, 10, 12, 12, 8, 44]): ws.column_dimensions[col].width = wdt
    ws.freeze_panes = "D2"
    w2 = wb.create_sheet("Expected results"); w2.append(["Filter", "Count", "Mock IDs it should return"])
    for n, ids in EXPECT.items(): w2.append([n, len(ids), ", ".join(ids)])
    for c in w2[1]: c.font = Font(bold=True); c.fill = PatternFill("solid", fgColor="DCE6F5")
    w2.column_dimensions["A"].width = 46; w2.column_dimensions["C"].width = 60
    w3 = wb.create_sheet("Key map"); w3.append(["Mock ID", "Summary", "Real Jira key (type it here after creating)"])
    [w3.append([t["id"], t["summary"], ""]) for t in T]
    for c in w3[1]: c.font = Font(bold=True); c.fill = PatternFill("solid", fgColor="DCE6F5")
    w3.column_dimensions["B"].width = 60; w3.column_dimensions["C"].width = 40
    wb.save(os.path.join(OUT, "mock_tickets.xlsx"))
except ImportError:
    print("openpyxl not installed: workbook skipped, CSV written")


# ------------------------------------------------------------------ JQL for one project
A = '"MOCK: all"'
JQL = {
 "MOCK: all": f"project = {KEY} AND labels = mock",
 "MOCK PI planned Initiatives": f'filter = {A} AND issuetype = Initiative AND "Target PI" = "{CUR}"',
 "MOCK PI planned Epics": f'filter = {A} AND issuetype = Epic AND "Target PI" = "{CUR}"',
 "MOCK: spillover": f'filter = {A} AND issuetype in (Initiative, Epic) AND "Target PI" in ("{PREV}") AND labels = pi-committed AND status not in (Released, Done)',
 "MOCK: PI Epics": f'filter = "MOCK PI planned Epics" OR (filter = "MOCK: spillover" AND issuetype = Epic) OR (filter = {A} AND issuetype = Epic AND status = Implementing)',
 "MOCK: current PI Initiatives": f'filter = "MOCK PI planned Initiatives" OR (filter = {A} AND issuetype = Initiative AND status in (Implementing, Testing, Validation))',
 "MOCK: committed Initiatives": 'filter = "MOCK PI planned Initiatives" AND labels = pi-committed',
 "MOCK: committed and released": 'filter = "MOCK: committed Initiatives" AND status in (Released, Done)',
 "MOCK: unplanned in PI": 'filter = "MOCK PI planned Initiatives" AND labels = unplanned',
 "MOCK: open Capabilities": f'filter = {A} AND issuetype = Capability AND status not in (Idea, Done) ORDER BY Rank',
 "MOCK: all Initiatives": f'filter = {A} AND issuetype = Initiative',
 "MOCK: Red and Amber": '(filter = "MOCK: current PI Initiatives" OR filter = "MOCK: PI Epics" OR filter = "MOCK: open Capabilities") AND "RAG Status" in (Red, Amber) AND status not in (Released, Done)',
 "MOCK: Management Attention and Red": f'filter = {A} AND issuetype in (Initiative, Capability) AND status not in (Released, Done) AND ("Management Attention" is not EMPTY OR "RAG Status" = Red)',
 "MOCK: Amber or Red without a plan": 'filter = "MOCK: Red and Amber" AND issuetype != Epic AND "Path to Green" is EMPTY',
 "MOCK: intake waiting": f'filter = {A} AND issuetype in (Initiative, Capability) AND status = Idea ORDER BY created',
 "MOCK: Ready, no Target PI": f'filter = {A} AND issuetype = Initiative AND status = Ready AND "Target PI" is EMPTY ORDER BY "Weighted Shortest Job First Score" DESC',
 "MOCK: Initiatives with gaps": f'filter = {A} AND issuetype = Initiative AND status not in (Idea, Analysis, Done) AND ("Parent Link" is EMPTY OR "RAG Status" is EMPTY OR "Value Stream and Sub-Value Stream" is EMPTY)',
 "MOCK: regulatory Initiatives": f'filter = {A} AND issuetype = Initiative AND "Regulatory or Control Change Type" is not EMPTY AND status not in (Released, Done)',
 "MOCK: PI Epics not started": 'filter = "MOCK: PI Epics" AND status in (Idea, Analysis, Ready)',
 "MOCK: flagged": f'filter = {A} AND Flagged = Impediment',
 "MOCK: hygiene exceptions": f'filter = {A} AND issuetype = Epic AND "Parent Link" is EMPTY AND statusCategory != Done',
 "MOCK: open RAID": f'filter = {A} AND issuetype = "Delivery RAID" AND statusCategory != Done',
 "MOCK: open Red and Amber RAID": 'filter = "MOCK: open RAID" AND "RAG Status" in (Red, Amber) ORDER BY duedate',
 "MOCK: risks not reviewed": 'filter = "MOCK: open RAID" AND "RAID Type" = Risk AND "ROAM Response" is EMPTY',
 "MOCK: RAID past its date": 'filter = "MOCK: open RAID" AND duedate < now()',
 "MOCK: milestones next 90 days and overdue": f'filter = {A} AND labels = milestone AND statusCategory != Done AND duedate <= endOfDay("+90d") ORDER BY duedate',
 "MOCK: open dependencies": 'filter = "MOCK: open RAID" AND "RAID Type" = Dependency ORDER BY duedate',
 "MOCK: dependencies not agreed": 'filter = "MOCK: open dependencies" AND status = Backlog ORDER BY duedate',
 "MOCK: dependencies agreed": 'filter = "MOCK: open dependencies" AND status = "In Progress"',
 "MOCK: dependencies late or due soon": 'filter = "MOCK: open dependencies" AND duedate <= endOfDay("+28d") ORDER BY duedate',
 "MOCK: dependencies at risk": 'filter = "MOCK: open dependencies" AND "RAG Status" in (Amber, Red)',
 "MOCK: dependencies without an owner or date": 'filter = "MOCK: open dependencies" AND (assignee is EMPTY OR duedate is EMPTY)',
 "MOCK release: scope": f'filter = {A} AND fixVersion = "{REL}"',
 "MOCK release: not finished": f'filter = {A} AND fixVersion = "{REL}" AND status not in (Released, Done)',
 "MOCK release: open bugs": f'filter = {A} AND fixVersion = "{REL}" AND issuetype = Bug AND statusCategory != Done',
 "MOCK team: flagged in sprint": f'filter = {A} AND sprint in openSprints() AND Flagged = Impediment',
 "MOCK team: open Epics": f'filter = {A} AND issuetype = Epic AND status not in (Released, Done)',
 "MOCK team: open bugs": f'filter = {A} AND issuetype = Bug AND statusCategory != Done',
 "MOCK team: Stories without Epic": f'filter = {A} AND issuetype = Story AND "Epic Link" is EMPTY AND statusCategory != Done',
}
ALIAS = {"MOCK PI planned Initiatives": "planned Initiatives", "MOCK PI planned Epics": "planned Epics"}
def exp(n):
    if n == "MOCK: all": return [t["id"] for t in T]
    return EXPECT[ALIAS.get(n, n)]

def table(heads, rows):
    out = ["| " + " | ".join(heads) + " |", "| " + " | ".join("---" for _ in heads) + " |"]
    for r in rows: out.append("| " + " | ".join(str(x) if x != "" else "" for x in r) + " |")
    return "\n".join(out)
def par(t): return f'{t["parent"]} {BY[t["parent"]]["summary"]}' if t["parent"] else "none (on purpose)"
def labs(t): return ", ".join(f"`{l}`" for l in t["labels"])
def of(tp): return [t for t in T if t["type"] == tp]
G = {}
G["cap"] = table(["ID", "Summary", "Status", "RAG Status", "Due date", "Value Stream and Sub-Value Stream", "Path to Green", "Labels"],
    [[t["id"], t["summary"], t["status"], t["rag"], t["due"], t["svs"], t["ptg"], labs(t)] for t in of("Capability")])
G["ini"] = table(["ID", "Summary", "Parent (Parent Link)", "Status", "Target PI", "Actual PI", "RAG Status", "Labels", "Due date", "Sub value stream", "Other"],
    [[t["id"], t["summary"], par(t), t["status"], t["target"], t["actual"], t["rag"], labs(t), t["due"], t["svs"].replace(VS + " -> ", ""),
      "; ".join(x for x in [f'Scores {t["scores"]}' if t["scores"] else "", "Management Attention set" if t["mgmt"] else "", f'Regulatory type: {t["reg"]}' if t["reg"] else "",
                             f'Enabler Type: {t["enabler"]}' if t["enabler"] else "", f'Path to Green: {t["ptg"]}' if t["ptg"] else ""] if x)] for t in of("Initiative")])
G["epic"] = table(["ID", "Summary", "Epic Name", "Parent (Parent Link)", "Component", "Status", "Target PI", "Actual PI", "RAG Status", "Labels", "End Date", "Story Points", "Fix version"],
    [[t["id"], t["summary"], t["epic"], par(t), t["comp"], t["status"], t["target"], t["actual"], t["rag"], labs(t), t["end"], t["sp"], t["fix"]] for t in of("Epic")])
G["story"] = table(["ID", "Type", "Summary", "Epic Link", "Component", "Status", "Story Points", "Severity", "Fix version", "In the sprint"],
    [[t["id"], t["type"], t["summary"], (f'{t["epic_link"]} {BY[t["epic_link"]]["summary"]}' if t["epic_link"] else "none (on purpose)"), t["comp"], t["status"], t["sp"], t["sev"], t["fix"], "Yes" if t["sprint"] else ""] for t in of("Story") + of("Bug")])
G["raid"] = table(["ID", "Summary", "RAID Type", "Status", "RAG Status", "Due date", "Baseline End Date", "Sub value stream (waiting)", "Supplier", "Component", "Probability", "Impact", "ROAM Response", "Assignee"],
    [[t["id"], t["summary"], t["raid"], t["status"], t["rag"], t["due"], t["baseline"], t["svs"].replace(VS + " -> ", ""), t["supplier"].replace(VS + " -> ", ""), t["comp"], t["prob"], t["impact"], t["roam"], "anyone" if t["assignee"] else "leave empty"] for t in of("Delivery RAID")])
G["ms"] = table(["ID", "Summary", "Status", "Labels", "Due date", "RAG Status"], [[t["id"], t["summary"], t["status"], labs(t), t["due"], t["rag"]] for t in of("Task")])
G["parents"] = table(["Set Parent Link on", "To"], [[f'{t["id"]} {t["summary"]}', f'{t["parent"]} {BY[t["parent"]]["summary"]}'] for t in T if t["parent"]])
G["links"] = table(["On this ticket", "Add link", "To"], [[f'{t["id"]} {t["summary"]}', k, f'{v} {BY[v]["summary"]}'] for t in T for k, v in t["links"]])
G["jql"] = table(["Save as", "Query", "Should return", "Which"], [[f"`{n}`", f"`{q}`", len(exp(n)), ", ".join(exp(n)) if n != "MOCK: all" else "all 38"] for n, q in JQL.items()])
def e(n): return f'{len(exp(n))}: {", ".join(exp(n))}' if exp(n) else "0"
G["e"] = e
import json
json.dump({k: v for k, v in G.items() if k != "e"}, open(os.path.join(OUT, "_fragments.json"), "w"))
json.dump({n: exp(n) for n in JQL}, open(os.path.join(OUT, "_expected.json"), "w"))
counts = {}
for t in T: counts[t["type"]] = counts.get(t["type"], 0) + 1
print("tickets", len(T), counts)
for n, ids in EXPECT.items(): print(f"{n} | {len(ids)} | {', '.join(ids)}")
