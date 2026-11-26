"""White paper charts. All data is illustrative mock data. Usage: charts.py <outdir>"""
import sys, os, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon
import numpy as np

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

S, T, T2, T3, G = "#fcfcfb", "#0b0b0b", "#52514e", "#8a8983", "#e6e5e0"
BLUE, ORANGE, AQUA, YELLOW, MAGENTA = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"
GOOD, WARN, CRIT = "#0ca30c", "#fab219", "#d03b3b"
RAG = {"Green": GOOD, "Amber": WARN, "Red": CRIT}
B250, B400, B500, B600, B700 = "#86b6ef", "#3987e5", "#256abf", "#184f95", "#0d366b"
B100 = "#cde2fb"
NEUT, NEUT2 = "#d9d8d2", "#b4b3ac"
APPS = ["CA", "DRAW", "FL", "GC", "WWM", "PEM", "FORB"]

plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Arial", "DejaVu Sans"], "font.size": 10,
    "figure.facecolor": S, "axes.facecolor": S, "savefig.facecolor": S,
    "text.color": T, "axes.labelcolor": T2, "xtick.color": T2, "ytick.color": T2,
    "axes.edgecolor": NEUT2, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": False, "grid.color": G, "grid.linewidth": 0.8,
    "legend.frameon": False, "axes.axisbelow": True,
})


def new(w, h, **kw):
    return plt.subplots(figsize=(w, h), **kw)


def save(f, name, title, sub="Illustrative data, not real figures"):
    w, h = f.get_size_inches()
    f.text(0.15 / w, 1 - 0.14 / h, title, fontsize=13, weight="bold", va="top", ha="left")
    f.text(0.15 / w, 1 - 0.44 / h, sub, fontsize=9.5, color=T2, va="top", ha="left")
    f.tight_layout(rect=[0, 0, 1, 1 - 0.72 / h])
    f.savefig(os.path.join(OUT, name + ".png"), dpi=160)
    plt.close(f)


def clean(ax, value_axis="x"):
    ax.tick_params(length=0)
    if value_axis == "x":
        ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
        ax.xaxis.grid(True)
    else:
        ax.spines["left"].set_visible(False)
        ax.yaxis.grid(True)


def hstack(ax, cats, series, colors, fmt="{:.0f}", minlab=1, textcols=None, height=0.62):
    left = np.zeros(len(cats))
    y = np.arange(len(cats))
    for i, (name, vals) in enumerate(series.items()):
        vals = np.array(vals, float)
        ax.barh(y, vals, left=left, color=colors[i], edgecolor=S, linewidth=1.6, height=height, label=name)
        for j, v in enumerate(vals):
            if v >= minlab:
                tc = (textcols[i] if textcols else "white")
                ax.text(left[j] + v / 2, y[j], fmt.format(v), ha="center", va="center", fontsize=8.5, color=tc)
        left += vals
    ax.set_yticks(y); ax.set_yticklabels(cats); ax.invert_yaxis()
    return left


def legend(ax, ncol=4, y=-0.16, **kw):
    ax.legend(loc="upper left", bbox_to_anchor=(0, y), ncol=ncol, fontsize=9, handlelength=1.1,
              handleheight=0.9, columnspacing=1.4, **kw)


def box(ax, x, y, w, h, text, fc, ec=None, tc=T, fs=9, weight="normal", wrap=None, r=0.8):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc,
                                ec=ec or fc, lw=1.2))
    if wrap:
        text = "\n".join(textwrap.wrap(text, wrap))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=tc, weight=weight,
            linespacing=1.25)


def canvas(w, h, xmax, ymax):
    f, ax = new(w, h)
    ax.set_xlim(0, xmax); ax.set_ylim(0, ymax); ax.axis("off")
    return f, ax


# ---------------------------------------------------------------- 01 hierarchy
f, ax = canvas(11, 6.6, 110, 62)
ax.add_patch(Rectangle((0, 33), 110, 27, fc="#f1f5fb", ec="none"))
ax.add_patch(Rectangle((0, 1), 110, 31, fc="#f6f5f1", ec="none"))
ax.text(1, 58.4, "PORTFOLIO PROJECT (one for the value stream)", fontsize=9, color=T2, weight="bold")
ax.text(109, 30.3, "APPLICATION PROJECTS (one per application)", fontsize=9, color=T2, weight="bold", ha="right")
box(ax, 26, 49, 38, 7, "VS EPIC\nAvoid audit risk through access control", B700, tc="white", fs=9.5, weight="bold")
box(ax, 8, 36, 32, 7, "FEATURE\nM&P across the platform", B500, tc="white", fs=9.5, weight="bold")
box(ax, 50, 36, 32, 7, "FEATURE\nAccess review evidence pack", B500, tc="white", fs=9.5, weight="bold")
for (x, t) in [(2, "EPIC  ·  Credit Application\nM&P for Credit Application"),
               (28, "EPIC  ·  Drawdowns\nM&P for Drawdowns"),
               (56, "EPIC  ·  Governance and Conditions\nEvidence pack for conditions")]:
    box(ax, x, 20, 24 if x < 50 else 30, 7, t, B250, tc=T, fs=8.8)
for x, w in [(2, 24), (28, 24), (56, 30)]:
    box(ax, x, 8, w, 6, "Stories, tasks, bugs, tests\n(sub-tasks optional)", "white", ec=NEUT2, fs=8.5, tc=T2)
    ax.plot([x + w / 2, x + w / 2], [14, 20], color=T2, lw=1.3)
ln = dict(color=T2, lw=1.3)
ax.plot([45, 24], [49, 43], **ln); ax.plot([45, 66], [49, 43], **ln)
ax.plot([24, 14], [36, 27], **ln); ax.plot([24, 40], [36, 27], **ln); ax.plot([66, 71], [36, 27], **ln)
box(ax, 88, 49, 20, 7, "MILESTONE\nAudit point AP-12\nremediation due", "white", ec=ORANGE, fs=8.3)
box(ax, 88, 36, 20, 7, "DELIVERY RAID\nRisk: audit may widen\nthe scope of AP-12", "white", ec=ORANGE, fs=8.3)
dl = dict(color=ORANGE, lw=1.3, ls=(0, (3, 2)))
ax.plot([64, 88], [52.5, 52.5], **dl); ax.plot([82, 88], [39.5, 39.5], **dl); ax.plot([82, 88], [41, 49], **dl)
ax.text(4, 46, "Parent Link", fontsize=8.5, color=T2, style="italic")
ax.text(1, 3.2, "Solid line = parent and child (one parent, many children): Parent Link above Epic, Epic Link below.     "
        "Dashed line = issue link (many to many): blocks, relates to.", fontsize=8.5, color=T2)
ax.text(42, 31.5, "Parent Link, across projects", fontsize=8.5, color=T2, style="italic")
ax.text(15, 16.4, "Epic Link", fontsize=8.5, color=T2, style="italic")
save(f, "01_hierarchy", "One line of work from the value stream to the story",
     "Worked example: one Feature delivered by two applications. Names are placeholders.")

# ---------------------------------------------------------------- 02 today vs target
f, ax = new(9.5, 3.6)
m = ["Epics with a parent Feature", "Features with a parent VS Epic", "In-progress work with RAG\nrefreshed in the last two weeks",
     "Portfolio sync run from the\ndashboard, no slide pack (share of meetings)"]
now, tgt = [38, 55, 47, 0], [95, 100, 90, 100]
y = np.arange(len(m))
for i in y:
    ax.plot([now[i], tgt[i]], [i, i], color=NEUT2, lw=2.2, zorder=1)
ax.scatter(now, y, s=90, color=ORANGE, zorder=2, label="Example starting point (count the real one in the proof of concept)")
ax.scatter(tgt, y, s=90, color=BLUE, zorder=2, label="Target after two PIs")
for i in y:
    ax.text(now[i] - 2.5, i, f"{now[i]}%", ha="right", va="center", fontsize=9, color=T2)
    ax.text(tgt[i] + 2.5, i, f"{tgt[i]}%", ha="left", va="center", fontsize=9, color=T2)
ax.set_yticks(y); ax.set_yticklabels(m); ax.invert_yaxis(); ax.set_xlim(-10, 112)
ax.set_xticks([0, 25, 50, 75, 100]); ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
clean(ax); legend(ax, ncol=1, y=-0.14)
save(f, "02_success_measures", "How the change will be judged", "Starting figures are examples only; targets are the framework's proposal")

# ---------------------------------------------------------------- 03 L0 roadmap
PIS = ["PI 2027.1", "PI 2027.2", "PI 2027.3", "PI 2027.4", "PI 2028.1", "PI 2028.2"]
rows = [  # (label, start, end, rag, level)
    ("Avoid audit risk through access control", 0, 3, "Amber", 0),
    ("M&P across the platform", 0, 2, "Amber", 1),
    ("Access review evidence pack", 1, 3, "Green", 1),
    ("One view of conditions from approval to drawdown", 0, 4, "Green", 0),
    ("Conditions carried into drawdown checks", 0, 1, "Green", 1),
    ("Facility letter generated from approved terms", 1, 2, "Green", 1),
    ("Conditions change history for auditors", 2, 4, "Green", 1),
    ("Earlier warning on deteriorating exposures", 0, 6, "Red", 0),
    ("Watch-list triggers from covenant breaches", 0, 1, "Red", 1),
    ("Shared event stream for exposure changes", 1, 3, "Amber", 1),
    ("Forbearance cases linked to problem exposures", 3, 5, "Green", 1),
    ("Portfolio early-warning dashboard", 4, 6, "Green", 1),
]
f, ax = new(12, 6.6)
ax.axvspan(0, 1, color="#eef3fb", lw=0); ax.axvspan(1, 2, color="#f5f7fb", lw=0)
for i, (lab, s, e, rag, lvl) in enumerate(rows):
    h = 0.62 if lvl == 0 else 0.42
    ax.barh(i, e - s - 0.04, left=s + 0.02, height=h, color=RAG[rag], alpha=1 if lvl == 0 else 0.55, edgecolor=S, lw=1.2)
    ax.text(e + 0.06, i, rag, va="center", fontsize=8, color=T2)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([(r[0] if r[4] == 0 else "      " + r[0]) for r in rows])
for lab, r in zip(ax.get_yticklabels(), rows):
    lab.set_weight("bold" if r[4] == 0 else "normal"); lab.set_color(T if r[4] == 0 else T2)
ax.invert_yaxis()
for x, yy, name in [(1.6, 1, "M&P live in all\norigination apps"), (2.9, 0, "Audit point AP-12 due"), (0.8, 8, "Covenant triggers pilot")]:
    ax.scatter([x], [yy - 0.48], marker="D", s=55, color=T, zorder=5)
    ax.text(x + 0.08, yy - 0.5, name.replace("\n", " "), fontsize=8, va="center", color=T)
ax.set_xlim(0, 6.6); ax.set_xticks(np.arange(6) + 0.5); ax.set_xticklabels(PIS)
ax.xaxis.tick_top(); ax.tick_params(length=0)
for x in range(7):
    ax.axvline(x, color=G, lw=0.8, zorder=0)
for s_ in ["left", "bottom"]:
    ax.spines[s_].set_visible(False)
ax.text(0.5, len(rows) - 0.25, "Committed", ha="center", fontsize=8.5, color=T2, weight="bold")
ax.text(1.5, len(rows) - 0.25, "Planned", ha="center", fontsize=8.5, color=T2, weight="bold")
ax.text(4, len(rows) - 0.25, "Forecast: by PI only, not a promise", ha="center", fontsize=8.5, color=T2, weight="bold")
ax.set_ylim(len(rows) + 0.1, -1.1)
save(f, "03_l0_roadmap", "L0 roadmap: VS Epics and their Features by PI",
     "Illustrative data. Bar colour is RAG Status (also written at the bar end). Diamonds are Milestones.")

# ---------------------------------------------------------------- 04 feature x application
feats = ["M&P across the platform", "Access review evidence pack", "Conditions carried into drawdown checks",
         "Facility letter generated from approved terms", "Watch-list triggers from covenant breaches",
         "Shared event stream for exposure changes", "Forbearance cases linked to problem exposures"]
# 0 none, 1 not started, 2 implementing, 3 released
M = np.array([[3, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0], [2, 3, 0, 3, 0, 0, 0], [3, 0, 2, 0, 0, 0, 0],
              [0, 0, 0, 0, 2, 1, 0], [0, 0, 0, 0, 2, 2, 1], [0, 0, 0, 0, 0, 2, 2]])
cmap = {0: S, 1: NEUT, 2: B250, 3: B500}
txt = {0: "", 1: "Not started", 2: "Implementing", 3: "Released"}
f, ax = new(11.5, 4.8)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        v = M[i, j]
        ax.add_patch(Rectangle((j + 0.04, i + 0.07), 0.92, 0.86, fc=cmap[v], ec=G if v == 0 else "none", lw=0.8))
        ax.text(j + 0.5, i + 0.5, txt[v], ha="center", va="center", fontsize=7.2, color="white" if v == 3 else T)
    done = (M[i] == 3).sum(); tot = (M[i] > 0).sum()
    ax.text(7.15, i + 0.5, f"{done} of {tot} released", va="center", fontsize=9, color=T, weight="bold" if 0 < done < tot else "normal")
    if 0 < done < tot:
        ax.text(8.75, i + 0.5, "waiting for " + ", ".join(a for a, v in zip(APPS, M[i]) if v in (1, 2)), va="center", fontsize=8.5, color=CRIT)
ax.set_xlim(0, 10.6); ax.set_ylim(M.shape[0], 0)
ax.set_xticks(np.arange(7) + 0.5); ax.set_xticklabels(APPS); ax.xaxis.tick_top()
ax.set_yticks(np.arange(len(feats)) + 0.5); ax.set_yticklabels(feats); ax.tick_params(length=0)
for s_ in ax.spines.values():
    s_.set_visible(False)
save(f, "04_feature_by_application", "Feature progress across applications: which application is a Feature waiting for?",
     "Illustrative data. One row per Feature, one column per application project; each filled cell is that application's Epic.")

# ---------------------------------------------------------------- 05 epics by application and status
f, ax = new(9.5, 4)
ser = {"Ready (not started)": [1, 3, 1, 0, 2, 2, 1], "Implementing": [4, 5, 3, 4, 5, 3, 3], "Released": [3, 1, 2, 3, 1, 1, 0], "Done": [1, 0, 1, 1, 0, 0, 0]}
hstack(ax, ["Credit Application (CA)", "Drawdowns (DRAW)", "Facility Letter (FL)", "Governance and Conditions (GC)",
            "Watch and Worry Monitor (WWM)", "Problem Exposure Mgmt (PEM)", "Forbearance (FORB)"],
       ser, [NEUT, B250, B500, B700], textcols=[T, T, "white", "white"])
clean(ax); ax.set_xlabel("Epics in the current PI (planned, carried over or in progress)"); legend(ax, y=-0.2)
save(f, "05_epics_by_application", "Dashboard 3: how far is each application with its share of the PI?",
     "Illustrative data. Standard gadget: Two Dimensional Filter Statistics on the filter VS: PI Epics, Project by Status.")

# ---------------------------------------------------------------- 06 predictability trend
f, ax = new(9.5, 4.2)
x = np.arange(6)
lines = [("Committed Features delivered", [58, 64, 71, 75, 79, 82], BLUE), ("Committed Epics delivered", [69, 73, 80, 81, 86, 88], ORANGE),
         ("Committed story points delivered", [74, 76, 83, 85, 87, 90], AQUA)]
ax.plot([-0.4, 5.05], [80, 80], color=T3, lw=1, ls=(0, (4, 3))); ax.text(-0.35, 81, "80%: a healthy level, not a target", fontsize=8.5, color=T2)
for (n, v, c), dy in zip(lines, [0, -2.5, 4]):
    ax.plot(x, v, color=c, lw=2, marker="o", ms=6, mec=S, mew=1.5, label=n)
    ax.text(5.12, v[-1] + dy * 0.4, f"{v[-1]}%  {n.replace('Committed ', '').replace(' delivered', '')}", va="center", fontsize=9, color=T)
ax.set_xticks(x); ax.set_xticklabels(PIS); ax.set_ylim(40, 100); ax.set_xlim(-0.4, 6.9)
ax.set_yticks([40, 60, 80, 100]); ax.set_yticklabels(["40%", "60%", "80%", "100%"])
clean(ax, "y"); legend(ax, ncol=3, y=-0.12)
save(f, "06_predictability_trend", "PI predictability: three figures, side by side",
     "Illustrative data. Features lag Epics because a Feature counts only when every application has delivered its Epic.")

# ---------------------------------------------------------------- 07 PI scorecard
f, ax = new(9.5, 4)
ser = {"Delivered": [7, 4, 5, 6, 5, 4, 3], "Spilled": [1, 4, 1, 1, 2, 2, 1], "Descoped by decision": [0, 1, 1, 0, 1, 0, 0], "Stopped": [0, 0, 0, 1, 0, 0, 0]}
tot = hstack(ax, APPS, ser, [B500, ORANGE, NEUT2, T3], textcols=["white", "white", T, "white"])
d = np.array(ser["Delivered"])
for i, t in enumerate(tot):
    ax.text(t + 0.2, i, f"{d[i] / t:.0%} delivered", va="center", fontsize=9, color=T2)
ax.set_xlim(0, 12.5); clean(ax); ax.set_xlabel("Committed Epics in the baseline for PI 2027.1"); legend(ax, y=-0.2)
save(f, "07_pi_scorecard", "PI scorecard: what happened to every committed Epic",
     "Illustrative data. Counted from the baseline table pasted at the lock, so later edits in Jira cannot change the result.")

# ---------------------------------------------------------------- 08 spillover reasons
f, ax = new(8, 3.3)
r = ["Dependency", "Capacity", "Scope", "Defect", "Environment"]; v = [11, 7, 4, 3, 2]
ax.barh(r, v, color=BLUE, height=0.6)
for i, n in enumerate(v):
    ax.text(n + 0.2, i, str(n), va="center", fontsize=9.5)
ax.invert_yaxis(); clean(ax); ax.set_xlim(0, 13); ax.set_xlabel("Spilled Epics over the last two PIs")
save(f, "08_spillover_reasons", "Why committed work spilled", "Illustrative data. Each spillover gets one of five reasons at the PI review.")

# ---------------------------------------------------------------- 09 points per VS Epic
f, ax = new(11, 3.6)
vs = ["Avoid audit risk through access control", "One view of conditions from approval to drawdown", "Earlier warning on deteriorating exposures", "Run and improve 2027"]
done, rem = [140, 210, 95, 160], [85, 160, 330, 120]
note = ["1.9 PIs to go · limited by DRAW", "2.4 PIs to go · limited by FL", "4.7 PIs to go · limited by PEM", "standing work, no forecast"]
tot = hstack(ax, vs, {"Story points done": done, "Story points remaining": rem}, [B500, B100], textcols=["white", T])
for i, t in enumerate(tot):
    ax.text(t + 8, i, f"{t:.0f} total · {note[i]}", va="center", fontsize=9, color=T2)
ax.set_xlim(0, 700); clean(ax); legend(ax, y=-0.14)
save(f, "09_points_per_vs_epic", "Size and forecast of each VS Epic in story points",
     "Illustrative data. Remaining points for each application divided by that team's PI velocity; the slowest application sets the date.")

# ---------------------------------------------------------------- 10 PI velocity
f, ax = new(10, 3.9)
vel = {"PI 2026.2": [52, 40, 36, 44, 49, 35, 30], "PI 2026.3": [57, 43, 38, 48, 52, 38, 33], "PI 2026.4": [55, 47, 41, 51, 56, 41, 34], "PI 2027.1": [60, 45, 40, 50, 55, 40, 35]}
x = np.arange(7); w = 0.19
for i, ((n, v), c) in enumerate(zip(vel.items(), [B250, B400, B500, B700])):
    ax.bar(x + (i - 1.5) * (w + 0.015), v, w, color=c, label=n)
for xi, v in zip(x, vel["PI 2027.1"]):
    ax.text(xi + 1.5 * (w + 0.015), v + 1.2, str(v), ha="center", fontsize=8.5)
ax.set_xticks(x); ax.set_xticklabels(APPS); clean(ax, "y"); ax.set_ylabel("Story points finished in the PI"); legend(ax, y=-0.1)
save(f, "10_pi_velocity", "PI velocity by application",
     "Illustrative data. Used to forecast one application against its own past; never to rank teams against each other.")

# ---------------------------------------------------------------- 11 capacity vs demand
f, ax = new(9.5, 4)
ser = {"Carried over from last PI": [5, 14, 4, 0, 8, 6, 3], "Committed": [38, 30, 26, 34, 34, 26, 22], "Stretch": [8, 9, 5, 8, 6, 4, 6]}
tot = hstack(ax, APPS, ser, [ORANGE, B500, B100], textcols=["white", "white", T], minlab=3)
cap = [60, 45, 40, 50, 55, 40, 35]
for i, c in enumerate(cap):
    ax.plot([c, c], [i - 0.42, i + 0.42], color=T, lw=2.4)
    over = tot[i] - c
    ax.text(max(tot[i], c) + 1.2, i, ("over capacity by %d" % over) if over > 0 else "fits", va="center", fontsize=9,
            color=CRIT if over > 0 else T2, weight="bold" if over > 0 else "normal")
ax.plot([], [], color=T, lw=2.4, label="Team capacity for the PI")
ax.set_xlim(0, 75); clean(ax); ax.set_xlabel("Story points for PI 2027.2"); legend(ax, y=-0.2)
save(f, "11_capacity_vs_demand", "PI planning: load against capacity for each team",
     "Illustrative data. Carried-over work is loaded first. Stretch work may exceed capacity; committed work may not.")

# ---------------------------------------------------------------- 12 investment mix
f, ax = new(10, 3.2)
kinds = {"Business Features": [50, 44, 47], "Enablers and resilience": [15, 9, 12], "Regulatory and control": [10, 16, 14],
         "Run work and defects": [15, 22, 19], "Unplanned reserve used": [10, 9, 8]}
hstack(ax, ["Intended split", "Actual, PI 2026.4", "Actual, PI 2027.1"], kinds, [BLUE, ORANGE, AQUA, YELLOW, MAGENTA], fmt="{:.0f}%",
       textcols=["white", "white", T, T, T], height=0.55)
ax.set_xlim(0, 100); ax.set_xticks([]); clean(ax); ax.xaxis.grid(False); legend(ax, ncol=3, y=-0.05)
save(f, "12_investment_mix", "Investment mix: where the capacity went against where it was meant to go",
     "Illustrative data. Share of story points by kind of work, from Enabler Type and the regulatory fields.")

# ---------------------------------------------------------------- 13 milestone slippage
f, ax = new(10, 3.8)
ms = [("Audit point AP-12 remediation due", 120, 120), ("M&P live in all origination applications", 75, 96), ("Covenant triggers live for pilot business line", 40, 82),
      ("Facility letter go-live, business line 1", 105, 112), ("Conditions data feed available from Group", 55, 55), ("PI 2027.2 planning", 77, 77)]
for i, (n, b, c) in enumerate(ms):
    ax.plot([b, c], [i, i], color=ORANGE if c > b else NEUT2, lw=3, zorder=1)
    ax.scatter([b], [i], s=70, color=NEUT2, zorder=2); ax.scatter([c], [i], s=70, color=T if c == b else ORANGE, zorder=3)
    ax.text(c + 3, i, "on baseline" if c == b else f"+{c - b} days", va="center", fontsize=9, color=T2 if c == b else T, weight="normal" if c == b else "bold")
ax.scatter([], [], s=70, color=NEUT2, label="Baseline End Date (first commitment, never changed)")
ax.scatter([], [], s=70, color=ORANGE, label="Due date (current target)")
ax.set_yticks(range(len(ms))); ax.set_yticklabels([m_[0] for m_ in ms]); ax.invert_yaxis()
ax.set_xticks([0, 28, 56, 84, 112, 140]); ax.set_xticklabels(["4 Jan", "1 Feb", "1 Mar", "29 Mar", "26 Apr", "24 May"]); ax.set_xlim(0, 150)
clean(ax); legend(ax, ncol=2, y=-0.12)
save(f, "13_milestone_slippage", "Milestone slippage: which dates have moved since they were first promised",
     "Illustrative data for 2027. The gap between the two fields is the slippage; no manual tracking.")

# ---------------------------------------------------------------- 14 RAID
f, (a1, a2) = new(11.5, 4, ncols=2, gridspec_kw={"width_ratios": [1.25, 1]})
ser = {"Green": [6, 4, 2, 5], "Amber": [4, 1, 3, 4], "Red": [1, 0, 2, 2]}
hstack(a1, ["Risk", "Assumption", "Issue", "Dependency"], ser, [GOOD, WARN, CRIT], textcols=["white", T, "white"])
clean(a1); a1.set_xlabel("Open Delivery RAID tickets"); a1.set_title("By RAID Type and RAG Status", fontsize=10, loc="left", color=T2)
legend(a1, ncol=3, y=-0.22)
heat = np.array([[0, 1, 2], [1, 2, 1], [2, 1, 1]])  # rows prob High..Low, cols impact Low..High
ramp = {0: "#eef4fd", 1: B250, 2: B500}
for i in range(3):
    for j in range(3):
        sev = (2 - i) + j
        col = [B100, B100, B250, B500, B700][sev]
        a2.add_patch(Rectangle((j + 0.03, i + 0.03), 0.94, 0.94, fc=col, ec="none"))
        a2.text(j + 0.5, i + 0.5, str(heat[i, j]), ha="center", va="center", fontsize=13, color="white" if sev >= 3 else T, weight="bold")
a2.set_xlim(0, 3); a2.set_ylim(3, 0); a2.set_xticks([0.5, 1.5, 2.5]); a2.set_xticklabels(["Low", "Medium", "High"])
a2.set_yticks([0.5, 1.5, 2.5]); a2.set_yticklabels(["High", "Medium", "Low"]); a2.set_xlabel("Impact"); a2.set_ylabel("Probability")
a2.tick_params(length=0); a2.set_title("Open risks: Probability by Impact (count)", fontsize=10, loc="left", color=T2)
for s_ in a2.spines.values():
    s_.set_visible(False)
save(f, "14_raid_overview", "Delivery RAID: how much is open, and how serious", "Illustrative data. Darker cells are the risks reviewed first.")

# ---------------------------------------------------------------- 15 dependency matrix
svs = ["Underwriting", "Governance and Conditions", "Facility Letter", "Drawdown", "Monitoring", "Forbearance"]
D = np.array([[0, 1, 0, 0, 0, 0], [2, 0, 1, 0, 0, 0], [1, 2, 0, 0, 0, 0], [1, 4, 2, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 3, 0]])
f, ax = new(9.5, 4.6)
for i in range(6):
    for j in range(6):
        v = D[i, j]
        col = S if i == j else {0: "#f3f2ee", 1: B100, 2: B250, 3: B500, 4: B700}[v]
        ax.add_patch(Rectangle((j + 0.03, i + 0.05), 0.94, 0.9, fc=col, ec="none"))
        if i == j:
            ax.plot([j + 0.2, j + 0.8], [i + 0.8, i + 0.2], color=G, lw=1)
        elif v:
            ax.text(j + 0.5, i + 0.5, str(v), ha="center", va="center", fontsize=11, weight="bold", color="white" if v >= 3 else T)
ax.set_xlim(0, 6); ax.set_ylim(6, 0); ax.set_xticks(np.arange(6) + 0.5); ax.set_xticklabels([s_.replace(" and ", "\nand ") for s_ in svs], fontsize=8.5)
ax.xaxis.tick_top(); ax.set_yticks(np.arange(6) + 0.5); ax.set_yticklabels(svs); ax.tick_params(length=0)
ax.set_ylabel("Receiver (waiting)"); ax.xaxis.set_label_position("top"); ax.set_xlabel("Supplier (owes the work)", labelpad=8)
for s_ in ax.spines.values():
    s_.set_visible(False)
save(f, "15_dependency_matrix", "Who is waiting on whom across the value stream",
     "Illustrative data. Open Delivery RAID dependencies: receiver sub value stream by supplier sub value stream.")

# ---------------------------------------------------------------- 16 created vs resolved
rng = np.random.default_rng(7)
wk = np.arange(27)
created = np.cumsum(np.r_[0, rng.poisson(2.3, 26)]); resolved = np.cumsum(np.r_[0, rng.poisson(1.3, 26)])
f, ax = new(9, 3.6)
ax.fill_between(wk, resolved, created, color=ORANGE, alpha=0.12, lw=0)
ax.plot(wk, created, color=ORANGE, lw=2, label="Features created"); ax.plot(wk, resolved, color=BLUE, lw=2, label="Features finished")
ax.text(26.4, created[-1], f"{created[-1]} created", va="center", fontsize=9); ax.text(26.4, resolved[-1], f"{resolved[-1]} finished", va="center", fontsize=9)
ax.annotate("the gap is the growing backlog", xy=(20, (created[20] + resolved[20]) / 2), xytext=(19, 6), fontsize=9, color=T2, ha="center", arrowprops=dict(arrowstyle="-", color=T3))
ax.set_xlim(0, 31); ax.set_xlabel("Weeks (last 180 days)"); clean(ax, "y"); legend(ax, ncol=2, y=-0.2)
save(f, "16_created_vs_resolved", "Is the value stream finishing Features as fast as it takes them on?",
     "Illustrative data. Standard gadget: Created vs Resolved on the filter VS: all Features.")

# ---------------------------------------------------------------- 17 WSJF
f, ax = new(10, 4)
wf = [("Conditions change history for auditors", 13.0, 5), ("Covenant breach alerts by email", 10.5, 3), ("Drawdown checklist pre-filled from approval", 8.7, 8),
      ("Single sign-on for facility letter review", 6.5, 5), ("Forbearance case timeline", 5.2, 8), ("Exposure roll-up by client group", 4.3, 13),
      ("Archive of expired conditions", 2.6, 5), ("Redesign of watch-list screen", 1.9, 13)]
cum = np.cumsum([w_[2] for w_ in wf]); fits = cum <= 21
ax.barh([w_[0] for w_ in wf], [w_[1] for w_ in wf], color=[BLUE if ok else NEUT for ok in fits], height=0.62)
for i, w_ in enumerate(wf):
    ax.text(w_[1] + 0.2, i, f"{w_[1]:.1f}   (job size {w_[2]})", va="center", fontsize=9, color=T)
k = fits.sum()
ax.axhline(k - 0.5, color=T, lw=1, ls=(0, (4, 3))); ax.text(15.6, k - 0.58, "capacity for the next PI ends here", fontsize=9, color=T, va="bottom", ha="right")
ax.invert_yaxis(); ax.set_xlim(0, 16); clean(ax); ax.set_xlabel("Weighted Shortest Job First Score = (value + time criticality + risk reduction) / job size")
save(f, "17_wsjf_ranking", "Ready Features in priority order for the next PI", "Illustrative data. Filter: VS: Ready, no Target PI, sorted by score.")

# ---------------------------------------------------------------- 18 hygiene trend
f, ax = new(9.5, 3.9)
mo = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
hy = [("Epics without a parent Feature", [64, 41, 22, 11, 6, 3], BLUE), ("Tickets without a sub value stream", [38, 30, 17, 9, 5, 4], ORANGE),
      ("Amber or Red without a recovery plan", [19, 16, 12, 6, 4, 2], AQUA), ("Released without Actual PI", [12, 9, 9, 4, 1, 0], YELLOW)]
for n, v, c in hy:
    ax.plot(mo, v, color=c, lw=2, marker="o", ms=6, mec=S, mew=1.5, label=n)
for (n, v, c), yy in zip(hy, [64, 38, 22, 10]):
    ax.text(-0.12, yy, str(v[0]), ha="right", va="center", fontsize=9)
ax.set_xlim(-0.5, 5.3); clean(ax, "y"); ax.set_ylabel("Tickets failing the check"); legend(ax, ncol=2, y=-0.1)
save(f, "18_hygiene_trend", "Data quality: hygiene exceptions month by month", "Illustrative data. One hygiene filter per line; the count is published per application every month.")

# ---------------------------------------------------------------- 19 fields per issue type
f, ax = new(9.5, 4.4)
it = ["VS Epic", "Feature", "Epic", "Story", "Task", "Sub-task", "Bug", "Test", "Milestone", "Delivery RAID"]
off = [60, 55, 30, 25, 22, 18, 35, 28, 22, 32]; core = [16, 17, 14, 8, 6, 3, 11, 7, 9, 9]; when = [6, 13, 4, 3, 2, 1, 4, 1, 5, 10]
y = np.arange(len(it))
ax.barh(y, off, color="#eeede8", height=0.74, label="Offered on the screen (approximate)")
ax.barh(y, core, color=B500, height=0.5, edgecolor=S, lw=1.2, label="Core: always filled in")
ax.barh(y, when, left=core, color=B250, height=0.5, edgecolor=S, lw=1.2, label="Only when it applies")
for i in y:
    ax.text(core[i] / 2, i, str(core[i]), ha="center", va="center", color="white", fontsize=8.5)
    if when[i] >= 3:
        ax.text(core[i] + when[i] / 2, i, str(when[i]), ha="center", va="center", color=T, fontsize=8.5)
    ax.text(off[i] + 0.8, i, f"about {off[i]}", va="center", fontsize=8.5, color=T2)
ax.set_yticks(y); ax.set_yticklabels(it); ax.invert_yaxis(); clean(ax); ax.set_xlim(0, 68); ax.set_xlabel("Number of fields"); legend(ax, ncol=3, y=-0.16)
save(f, "19_fields_per_issue_type", "The field shortlist: what people actually have to fill in",
     "Counts from the field shortlist. Screen totals were read from a photo of the standards page and are approximate.")

# ---------------------------------------------------------------- 20 burn-up
f, ax = new(9.5, 3.9)
sp = np.arange(0, 6); scope = [300, 300, 320, 345, 370, 370]; dn = [0, 38, 81, 120, 166, 210]
ax.step(sp, scope, where="post", color=T2, lw=2, label="Scope (total story points)")
ax.plot([5, 11.3], [370, 370], color=T2, lw=2, ls=(0, (1, 2)))
ax.plot(sp, dn, color=BLUE, lw=2.2, marker="o", ms=5, mec=S, mew=1.2, label="Done")
fx = np.array([5, 6, 7, 8, 9, 10, 11]); fy = 210 + np.clip(fx - 6, 0, None) * 42
ax.plot(fx, fy, color=BLUE, lw=1.6, ls=(0, (4, 3)), label="Forecast at recent velocity")
ax.fill_between(fx, 210 + np.clip(fx - 6, 0, None) * 34, 210 + np.clip(fx - 6, 0, None) * 50, color=BLUE, alpha=0.12, lw=0)
ax.axvline(6, color=G, lw=1); ax.text(3, 398, "PI 2027.1", ha="center", fontsize=9, color=T2); ax.text(9, 398, "PI 2027.2", ha="center", fontsize=9, color=T2)
ax.annotate("scope grew by 70 points", xy=(4, 370), xytext=(0.3, 388), fontsize=9, color=T2, arrowprops=dict(arrowstyle="-", color=T3))
ax.annotate("forecast finish:\nsprint 4 of PI 2027.2", xy=(9.8, 370), xytext=(9.3, 230), fontsize=9, arrowprops=dict(arrowstyle="-", color=T3))
ax.text(5.1, 195, "today", fontsize=9, color=T2)
ax.set_xticks(range(1, 12)); ax.set_xticklabels(["S1", "S2", "S3", "S4", "S5", "planning", "S1", "S2", "S3", "S4", "S5"])
ax.set_xlim(0, 11.4); ax.set_ylim(0, 415); clean(ax, "y"); ax.set_ylabel("Story points"); legend(ax, ncol=3, y=-0.1)
save(f, "20_vs_epic_burnup", "Burn-up of one VS Epic: scope, progress and forecast",
     "Illustrative data for 'One view of conditions from approval to drawdown'. Points summed from Epics and stories under the VS Epic.")

# ---------------------------------------------------------------- 21 WIP
f, ax = new(9, 3.7)
stt = ["Idea", "Review", "Analysis", "Ready", "Implementing", "Released", "Done"]; n = [9, 4, 6, 2, 6, 3, 4]; lim = [None, 4, 4, 3, 6, None, None]
cols = [CRIT if (l is not None and v > l) else B500 for v, l in zip(n, lim)]
ax.bar(range(7), n, color=cols, width=0.58)
ax.set_xticks(range(7)); ax.set_xticklabels([s_ + (f"\nlimit {l}" if l is not None else "\nno limit") for s_, l in zip(stt, lim)])
for i, (v, l) in enumerate(zip(n, lim)):
    ax.text(i, v + 0.25, str(v), ha="center", fontsize=10, weight="bold")
    if l is not None:
        ax.plot([i - 0.42, i + 0.42], [l, l], color=T, lw=2.2)
ax.text(2, 7.6, "over the limit:\nnothing new enters\nAnalysis", ha="center", fontsize=8.5, color=CRIT)
ax.plot([], [], color=T, lw=2.2, label="Column limit"); ax.legend(loc="upper right", fontsize=9)
ax.set_ylim(0, 10.5); ax.set_xlim(-0.6, 6.6); clean(ax, "y"); ax.set_ylabel("VS Epics")
save(f, "21_wip_limits", "Work-in-progress limits on the VS Epic board", "Illustrative data. The limit is a column limit on the board; a breach is discussed at every portfolio sync.")

# ---------------------------------------------------------------- 22 release readiness
f, (a1, a2) = new(11.5, 3.6, ncols=2, gridspec_kw={"width_ratios": [1.5, 1]})
ser = {"Done": [18, 11, 14], "In progress": [3, 7, 2], "Not started": [0, 3, 1]}
hstack(a1, ["Credit Application", "Drawdowns", "Facility Letter"], ser, [B500, B250, NEUT], textcols=["white", T, T])
clean(a1); a1.set_xticks(range(0, 25, 5)); a1.set_xlabel("Stories and bugs in the release"); a1.set_title("Scope by application", fontsize=10, loc="left", color=T2); legend(a1, ncol=3, y=-0.26)
sv = ["Severity 1", "Severity 2", "Severity 3", "Severity 4"]; bv = [0, 2, 7, 11]
a2.barh(sv, bv, color=[CRIT, CRIT, B250, B250], height=0.6)
for i, v in enumerate(bv):
    a2.text(v + 0.25, i, str(v) + ("  blocks go-live" if i == 1 else ""), va="center", fontsize=9, color=CRIT if i == 1 else T)
a2.invert_yaxis(); a2.set_xlim(0, 16); clean(a2); a2.set_title("Open bugs", fontsize=10, loc="left", color=T2)
save(f, "22_release_readiness", "Release readiness for CLP 2027.03, two sprints before go-live",
     "Illustrative data. One release name shared by three application projects; filters Release: scope and Release: open bugs.")

# ---------------------------------------------------------------- 23 lifecycle
f, ax = canvas(12.5, 5.3, 125, 52)
sts = ["Idea", "Analysis", "Ready", "Implementing", "Testing", "Validation", "Released", "Done"]
stage = ["Triage", "Design", "Waiting for a PI", "Delivery", "Testing and acceptance", "", "Release", "Close"]
gates = ["Demand agreed in the DDT; reference on the Feature", "Parent VS Epic, sub value stream, Enabler Type", "Definition of ready met",
         "Target PI, commitment label, RAG; all Epics have Target PI; plan locked", "All stories of all Epics Done and in test",
         "End-to-end test passed; no severity 1 or 2 Bug", "Business acceptance; sign-offs closed; every Epic Released", "Early-life support over; benefits reviewed"]
w = 14.2
for i, s_ in enumerate(sts):
    x = 2 + i * 15.3
    col = [NEUT, B100, B250, B400, B400, B500, B600, B700][i]
    pts = [(x, 30), (x + w - 2.5, 30), (x + w, 34), (x + w - 2.5, 38), (x, 38), (x + 2.5, 34)] if i else [(x, 30), (x + w - 2.5, 30), (x + w, 34), (x + w - 2.5, 38), (x, 38)]
    ax.add_patch(Polygon(pts, closed=True, fc=col, ec="none"))
    ax.text(x + w / 2 + (1 if i else 0), 34, s_, ha="center", va="center", fontsize=9.5, weight="bold", color="white" if i >= 3 else T)
    ax.text(x + w / 2, 41.5, stage[i], ha="center", fontsize=8.5, color=T2)
    ax.plot([x + 0.6, x + 0.6], [29.2, 22.5], color=T3, lw=0.9)
    ax.text(x + 0.6, 21.5, "\n".join(textwrap.wrap(gates[i], 21)), ha="left", va="top", fontsize=7.9, color=T, linespacing=1.3)
ax.set_ylim(1, 45)
ax.text(2, 3.5, "Blocked is the flag, not a status.   Cancelled is resolution Won't Do, not a status.   On hold is a move back to Ready with a comment.", fontsize=8.8, color=T2)
save(f, "23_feature_lifecycle", "The life of a Feature: eight statuses and the gate into each", "Above each status: the stage. Below: what is needed to enter it. Existing statuses only; no new status is requested.")

# ---------------------------------------------------------------- 24 PI calendar
f, ax = canvas(12.5, 4.9, 125, 40)
ax.set_ylim(-6, 40)
x0, ww = 3, 9.9
for k in range(12):
    ax.text(x0 + k * ww + ww / 2, 37.5, f"Week {k + 1}", ha="center", fontsize=8.5, color=T2)
for sidx in range(5):
    box(ax, x0 + sidx * 2 * ww + 0.3, 29, 2 * ww - 0.6, 6, f"Sprint {sidx + 1}", B250, fs=9.5, weight="bold")
box(ax, x0 + 10 * ww + 0.3, 29, 2 * ww - 0.6, 6, "Planning and\nimprovement sprint", B600, tc="white", fs=8.8, weight="bold")
ev = [(5, "Week 5\nCheck committed Epics\nnot yet started"), (7, "Week 7\nNext PI's Features in\nAnalysis; intake closes"),
      (9, "Week 9\nNext PI's Features Ready.\nCreate the two per-PI\nfilters; draft Target PI"),
      (10, "Week 10\nTeam capacity\nconfirmed;\ndependencies linked"), (11, "Week 11\nPI review and demo;\npredictability scored"),
      (12, "Weeks 11 to 12\nPI planning. Lock: paste\nthe baseline table")]
for k, t in ev:
    xx = x0 + (k - 0.5) * ww
    low = k in (10, 12)
    ax.plot([xx, xx], [28.4, 11.5 if low else 22], color=T3, lw=0.9); ax.scatter([xx], [28.4], s=22, color=T, zorder=4)
    ax.text(xx, 10.5 if low else 21, t, ha="center", va="top", fontsize=7.9, linespacing=1.3, bbox=dict(fc=S, ec="none", pad=1.5))
ax.text(3, -1.8, "Day 1 of the next PI: repoint the current-PI filters, add the ended PI to the spillover filter, update automation rule 4 and the board quick filter.",
        fontsize=8.8, color=T)
ax.text(3, -4.8, "Nothing else is rebuilt. Filters, dashboards and Confluence pages are live and follow the tickets.", fontsize=8.8, color=T2)
save(f, "24_pi_calendar", "The 12-week PI calendar and what happens in Jira on which day", "Five two-week sprints and one planning sprint")

# ---------------------------------------------------------------- 25 rollout
f, ax = new(11.5, 4.4)
tasks = [("Agree approver; brief Jira admin and sponsor", 0, 0.4, B700), ("Proof of concept on one slice (real Jira)", 0, 2, B500), ("Write the white paper", 0, 1, B250),
         ("Review and comment window", 1, 2, B250), ("Decision meeting: go, go with changes, stop", 2, 2.15, B700),
         ("Wave 1: VS Epics and Features created top-down", 2.2, 3.2, ORANGE), ("Wave 2: first group of applications stitched", 3, 4.5, ORANGE),
         ("Wave 3: remaining applications stitched", 4.3, 6, ORANGE), ("Dashboards 1 to 3 and three Confluence pages", 2.2, 5, AQUA),
         ("Role briefings (30, 60 and 90 minutes)", 3, 6, AQUA), ("First PI planning by the rules = first baseline", 6.2, 7, B700)]
for i, (n, s_, e, c) in enumerate(tasks):
    ax.barh(i, e - s_, left=s_, color=c, height=0.56)
ax.set_yticks(range(len(tasks))); ax.set_yticklabels([t_[0] for t_ in tasks]); ax.invert_yaxis()
ax.set_xticks(np.arange(8)); ax.set_xticklabels([f"Wk {i + 1}" for i in range(7)] + [""], ha="left"); ax.set_xlim(0, 7.3)
clean(ax); ax.axvline(2.08, color=T, lw=1, ls=(0, (4, 3))); ax.text(2.14, -0.42, "decision gate", fontsize=8.5, color=T)
for c, n in [(B500, "Prove and agree"), (ORANGE, "Stitch in waves"), (AQUA, "Build and brief")]:
    ax.barh([-5], [0], color=c, label=n)
ax.set_ylim(len(tasks) - 0.3, -0.7); legend(ax, ncol=3, y=-0.1)
save(f, "25_rollout_plan", "Proposed path: prove it, agree it, then stitch in waves",
     "Proposal. Week numbers are relative; the last step should land on the next PI planning date.")

# ---------------------------------------------------------------- 26 features RAG by sub value stream
f, ax = new(9.5, 3.9)
ser = {"Green": [4, 5, 3, 2, 3, 2], "Amber": [1, 2, 1, 3, 2, 1], "Red": [0, 1, 0, 1, 2, 0]}
hstack(ax, svs, ser, [GOOD, WARN, CRIT], textcols=["white", T, "white"])
clean(ax); ax.set_xlabel("Features in the current PI"); legend(ax, ncol=3, y=-0.2)
save(f, "26_features_rag_by_svs", "Dashboard 2: Features across the value stream, by sub value stream and RAG",
     "Illustrative data. One view for the whole value stream; the sub value stream is a grouping, never a separate dashboard.")

# ---------------------------------------------------------------- 27 dashboard mock-up
f, ax = canvas(12.5, 6.2, 125, 60)
ax.add_patch(Rectangle((0, 0), 125, 60, fc="#f3f2ee", ec="none"))
def panel(x, y, w, h, title):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.8", fc="white", ec=G, lw=1))
    ax.text(x + 1.5, y + h - 2.6, title, fontsize=9, weight="bold")
panel(2, 31, 76, 27, "Open VS Epics (filter: VS: open VS Epics, in rank order)")
hdr = [(3.5, "VS Epic"), (41, "Status"), (53, "RAG"), (61, "Due"), (69, "Features")]
for x, t in hdr:
    ax.text(x, 51.5, t, fontsize=8, color=T2, weight="bold")
vrows = [("Avoid audit risk through access control", "Implementing", "Amber", "30 Sep 27", "1 of 2"), ("One view of conditions from approval to drawdown", "Implementing", "Green", "17 Dec 27", "1 of 3"),
         ("Earlier warning on deteriorating exposures", "Implementing", "Red", "30 Jun 28", "0 of 4"), ("Run and improve 2027", "Implementing", "Green", "31 Dec 27", "standing work"),
         ("Faster credit decisions for small facilities", "Analysis", "Green", "to be set", "none yet")]
for i, r in enumerate(vrows):
    yy = 47.5 - i * 3.6
    ax.plot([3, 77], [yy + 2.2, yy + 2.2], color=G, lw=0.7)
    ax.text(3.5, yy, r[0], fontsize=8.2, va="center"); ax.text(41, yy, r[1], fontsize=8.2, va="center")
    ax.scatter([54], [yy], s=60, color=RAG[r[2]]); ax.text(55.5, yy, r[2], fontsize=8, va="center", color=T2)
    ax.text(61, yy, r[3], fontsize=8.2, va="center"); ax.text(69, yy, r[4] + (" released" if " of " in r[4] else ""), fontsize=8.2, va="center")
panel(80, 31, 43, 27, "Portfolio health (by RAG Status)")
tot = 0
for n, v in [("Green", 6), ("Amber", 3), ("Red", 1)]:
    ax.add_patch(Rectangle((82 + tot * 3.9, 42), v * 3.9 - 0.5, 6, fc=RAG[n], ec="none"))
    ax.text(82 + tot * 3.9 + v * 1.95, 45, f"{v}", ha="center", va="center", fontsize=10, weight="bold", color=T if n == "Amber" else "white")
    ax.text(82 + tot * 3.9, 39.5, n, fontsize=8, color=T2); tot += v
ax.text(82, 35, "10 open VS Epics · 6 Implementing (limit 6)", fontsize=8.2, color=T2)
panel(2, 2, 40, 27, "Needs a decision (Management Attention and Red)")
for i, (a, b) in enumerate([("Watch-list triggers from covenant breaches", "Red · needs covenant data owner named by Group Data"),
                            ("Conditions API needed by Drawdowns before sprint 3", "Red dependency · supplier: Governance and Conditions"),
                            ("M&P across the platform", "Amber · Drawdowns short of two engineers in February")]):
    yy = 21.5 - i * 6.3
    ax.scatter([4.5], [yy], s=45, color=CRIT if "Red" in b else WARN)
    ax.text(6.5, yy + 0.2, a, fontsize=8.2, va="center"); ax.text(6.5, yy - 2.5, b, fontsize=7.4, va="center", color=T2)
panel(44, 2, 37, 27, "Milestones: next 90 days and overdue")
for i, (a, b, c) in enumerate([("Covenant triggers live for pilot", "15 Feb · overdue by 12 days", CRIT), ("PI 2027.2 planning", "22 Mar", GOOD),
                               ("M&P live in all origination apps", "10 Apr · moved +21 days", WARN), ("Facility letter go-live, line 1", "26 Apr", GOOD)]):
    yy = 22 - i * 5
    ax.scatter([46.5], [yy], marker="D", s=40, color=c); ax.text(48.5, yy + 0.2, a, fontsize=8.2, va="center"); ax.text(48.5, yy - 2.2, b, fontsize=7.4, va="center", color=T2)
panel(83, 2, 40, 27, "Open RAID (RAID Type by RAG Status)")
ax.text(97, 22.3, "Green", fontsize=7.6, color=T2, ha="center"); ax.text(105, 22.3, "Amber", fontsize=7.6, color=T2, ha="center"); ax.text(113, 22.3, "Red", fontsize=7.6, color=T2, ha="center")
for i, (n, vals) in enumerate([("Risk", [6, 4, 1]), ("Assumption", [4, 1, 0]), ("Issue", [2, 3, 2]), ("Dependency", [5, 4, 2])]):
    yy = 18.5 - i * 4
    ax.text(85, yy, n, fontsize=8.2, va="center")
    for j, v in enumerate(vals):
        ax.text(97 + j * 8, yy, str(v), fontsize=9, va="center", ha="center", weight="bold" if (j == 2 and v) else "normal", color=CRIT if (j == 2 and v) else T)
save(f, "27_dashboard_mockup", "Dashboard 1, Value stream portfolio: a mock-up of the finished page",
     "Illustrative layout and data. Built only from standard gadgets on saved filters.")

print("charts:", len([x for x in os.listdir(OUT) if x.endswith(".png")]))
