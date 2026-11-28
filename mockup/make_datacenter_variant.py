"""Builds mockup/datacenter/: the same mock-up with the field names and values of today's Data Center.
Usage: python3 make_datacenter_variant.py
Edit the three blocks below (PI values, field names, how 'needs attention' is marked) and run again."""
import os, re, csv, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "datacenter")
os.makedirs(OUT, exist_ok=True)

# 1. PI values as the Target PI dropdown offers them
CUR, PREV = "PI 5", "PI 4"

# 2. Field names: name in the white paper -> name on today's Jira
FIELDS = [
    ("Regulatory or Control Change Type", "Is it Regulatory"),
    ("Management Attention", "Is it Regulatory"),
    ("Weighted Shortest Job First Score", "WSJF"),
    ("Path to Green", "RAG Description"),
    ("Baseline End Date", "Baseline End"),
    ("Enabler Type", "Enabler"),
]
# Probability -> Risk Probability and Impact -> Priority are handled separately (they are also ordinary words)

def must(s, a, b, count=0):
    assert a in s, a[:70]
    return s.replace(a, b)

# ---------------------------------------------------------------- patch the data and the queries
src = open(os.path.join(HERE, "build_mockup.py")).read()
src = must(src, 'CUR, PREV = "PI 2026.4", "PI 2026.3"', f'CUR, PREV = "{CUR}", "{PREV}"')
# one Yes/No field stands for both "regulatory" and "needs management attention"
src = must(src, 'svs=svs("Governance and Conditions"), reg="Audit", scores="8,13,5,5"', 'svs=svs("Governance and Conditions"), reg="Yes", mgmt="Yes", scores="5.2"')
src = must(src, 'svs=svs("Monitoring"), mgmt="Yes", scores="13,8,8,8")', 'svs=svs("Monitoring"), mgmt="Yes", reg="Yes", scores="3.6")')
for a, b in [('scores="5,8,3,3"', 'scores="5.3"'), ('scores="8,5,5,5"', 'scores="3.6"'), ('scores="5,3,2,3"', 'scores="3.3"'),
             ('scores="8,8,3,5"', 'scores="3.8"'), ('scores="8,13,5,3"', 'scores="8.7"')]:
    src = must(src, a, b)
src = must(src, 'enabler="Enabler"', 'enabler="Yes"')
# wording of the ticket tables
src = must(src, '''f'Scores {t["scores"]}' if t["scores"] else "", "Management Attention set" if t["mgmt"] else "", f'Regulatory type: {t["reg"]}' if t["reg"] else "",''',
           '''f'WSJF {t["scores"]}' if t["scores"] else "", "Is it Regulatory: Yes" if (t["mgmt"] or t["reg"]) else "",''')
src = must(src, '''f'Enabler Type: {t["enabler"]}' if t["enabler"] else ""''', '''f'Enabler: {t["enabler"]}' if t["enabler"] else ""''')
src = must(src, '''f'Path to Green: {t["ptg"]}' if t["ptg"] else ""''', '''f'RAG Description: {t["ptg"]}' if t["ptg"] else ""''')
# queries
src = must(src, '''("Management Attention" is not EMPTY OR "RAG Status" = Red)''', '''("Is it Regulatory" = Yes OR "RAG Status" = Red)''')
src = must(src, '''"Regulatory or Control Change Type" is not EMPTY''', '''"Is it Regulatory" = Yes''')
src = must(src, '''"Path to Green" is EMPTY''', '''"RAG Description" is EMPTY''')
src = must(src, '''ORDER BY "Weighted Shortest Job First Score" DESC''', '''ORDER BY WSJF DESC''')
src = must(src, '"MOCK: Management Attention and Red"', '"MOCK: Regulatory and Red"')
# columns of the ticket file
src = must(src, '"Enabler Type", "Scores (value, time, risk, size)", "Management Attention",\n        "Regulatory or Control Change Type", "Path to Green",',
           '"Enabler", "WSJF", "Is it Regulatory",\n        "(unused)", "RAG Description",')
src = must(src, 't["enabler"], t["scores"], t["mgmt"], t["reg"], t["ptg"],', 't["enabler"], t["scores"], ("Yes" if (t["mgmt"] or t["reg"]) else ""), "", t["ptg"],')
src = must(src, '"RAID Type", "Supplier Value Stream and Sub Value Stream", "Probability", "Impact",\n        "ROAM Response", "Baseline End Date",',
           '"RAID Type", "Supplier Value Stream and Sub Value Stream", "Risk Probability", "Priority",\n        "ROAM Response", "Baseline End",')
src = must(src, '"Baseline End Date", "Sub value stream (waiting)", "Supplier", "Component", "Probability", "Impact", "ROAM Response"',
           '"Baseline End", "Sub value stream (waiting)", "Supplier", "Component", "Risk Probability", "Priority", "ROAM Response"')
src = must(src, '"Path to Green", "Labels"],', '"RAG Description", "Labels"],')
open(os.path.join(OUT, "build_mockup.py"), "w").write(src)

g = open(os.path.join(HERE, "build_guide.py")).read()
d = open(os.path.join(HERE, "build_dashboard_guide.py")).read()
for name, text in (("build_guide.py", g), ("build_dashboard_guide.py", d)):
    text = text.replace("MOCK: Management Attention and Red", "MOCK: Regulatory and Red")
    open(os.path.join(OUT, name), "w").write(text)

run = lambda *a: subprocess.run([sys.executable, *a], cwd=OUT, check=True, capture_output=True, text=True).stdout
log = run("build_mockup.py", ".")
run("build_guide.py")
run("build_mockup.py", ".")          # fragments again for the second guide's module load
run("build_dashboard_guide.py")
for f in ("_fragments.json", "_expected.json"):
    p = os.path.join(OUT, f)
    if os.path.exists(p): os.remove(p)

# ---------------------------------------------------------------- post-process the two guides
def fix(text):
    for a, b in FIELDS:
        text = text.replace(a, b)
    text = text.replace("PI 2026.4 S3 mock", f"{CUR} S3 mock").replace("`PI 2026.4` and `PI 2026.3`", f"`{CUR}` and `{PREV}`")
    text = text.replace("PI 2026.4", CUR).replace("PI 2026.3", PREV)
    # Probability and Impact as field names
    text = re.sub(r"(?<!Risk )\bProbability\b", "Risk Probability", text)
    text = re.sub(r"\bImpact\b", "Priority", text)
    text = text.replace('"Scores" are the four scoring fields in the order value, time criticality, risk reduction, job size.',
                        "WSJF is the single score field; a higher number goes first.")
    text = text.replace("Target PI, RAG Status, RAID Type, ROAM Response, Risk Probability, Priority, Severity, Enabler, Is it Regulatory, Is it Regulatory.",
                        "Target PI, RAG Status, RAID Type, ROAM Response, Risk Probability, Priority, Severity, Enabler, Is it Regulatory.")
    return text
banner = ("> **Data Center edition.** This copy uses the field names and values of today's Jira: Target PI values `%s` and `%s`, "
          "WSJF, Enabler, Is it Regulatory, RAG Description, Risk Probability, Priority and Baseline End. "
          "What changed and why is in [FIELD_MAPPING.md](FIELD_MAPPING.md).\n\n" % (CUR, PREV))
for name in ("MOCKUP_GUIDE.md", "MOCKUP_DASHBOARD_BUILD.md"):
    p = os.path.join(OUT, name); t = fix(open(p).read())
    i = t.index("\n", t.index("# ")) + 1
    t = t[:i] + "\n" + banner + t[i:].lstrip("\n")
    t = t.replace("](../confluence/", "](../../confluence/")
    open(p, "w").write(t)

# ---------------------------------------------------------------- tidy the ticket file: drop the unused column
p = os.path.join(OUT, "mock_tickets.csv")
rows = list(csv.reader(open(p)))
k = rows[0].index("(unused)")
rows = [r[:k] + r[k + 1:] for r in rows]
with open(p, "w", newline="") as f: csv.writer(f).writerows(rows)
try:
    from openpyxl import load_workbook
    wb = load_workbook(os.path.join(OUT, "mock_tickets.xlsx")); ws = wb["Tickets"]; ws.delete_cols(k + 1); wb.save(os.path.join(OUT, "mock_tickets.xlsx"))
except ImportError:
    pass
for f in ("build_mockup.py", "build_guide.py", "build_dashboard_guide.py"):
    os.remove(os.path.join(OUT, f))
print(log.split("\n")[0])
print("written to", OUT, sorted(os.listdir(OUT)))
