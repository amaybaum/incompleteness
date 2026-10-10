import re, sys, collections
log = open(sys.argv[1], encoding="utf-8").read()
pat = re.compile(r"info: OIBridge/(FourCopy\w+)\.lean:(\d+):\d+: '(.+)' depends on axioms: (\[.*\])\s*$")
pat0 = re.compile(r"info: OIBridge/(FourCopy\w+)\.lean:(\d+):\d+: '(.+)' does not depend on any axioms")
STD = {"propext", "Classical.choice", "Quot.sound"}
per = collections.defaultdict(lambda: {"std": [], "sorry": [], "other": []})
for line in log.splitlines():
    m = pat.search(line)
    if m:
        mod, ln, name, ax = m.groups()
        axs = {a.strip() for a in ax.strip("[]").split(",") if a.strip()}
        key = "sorry" if "sorryAx" in axs else ("std" if axs <= STD else "other")
        per[mod][key].append(name.split(".")[-1]); continue
    m = pat0.search(line)
    if m:
        per[m.group(1)]["std"].append(m.group(3).split(".")[-1])
for mod in sorted(per):
    d = per[mod]
    print(f"{mod}: std {len(d['std'])}, sorryAx {len(d['sorry'])}, other {len(d['other'])}"
          + (f"  sorryAx: {d['sorry']}" if d['sorry'] else "") + (f"  other: {d['other']}" if d['other'] else ""))
warn = collections.Counter()
for line in log.splitlines():
    m = re.search(r"OIBridge/(FourCopy\w+)\.lean:\d+:\d+: declaration uses 'sorry'", line)
    if m: warn[m.group(1)] += 1
print("declaration uses 'sorry':", dict(warn))
errs = [l for l in log.splitlines() if re.search(r"(^|\s)error:", l)]
print("error lines:", len(errs))
for l in errs[:10]: print("  ", l[:200])
want = ["ie1_all", "parity_all", "kt4_general_ie1", "kt4_forward_ie1", "kt4_forward_ie1_kt4", "kt4_forward_ie1_lt"]
for line in log.splitlines():
    m = pat.search(line)
    if m and m.group(1) == "FourCopyHeadline":
        print("  HEADLINE", m.group(3), m.group(4))
for line in log.splitlines():
    m = pat.search(line)
    if m and m.group(1) == "FourCopyIE1" and m.group(3).split(".")[-1] in (
            "cross_rel_symm", "cnot_prodState_rot", "actC_rotWord_phiW", "link_mem", "parity_witnesses"):
        print("  IE1", m.group(3), m.group(4))
