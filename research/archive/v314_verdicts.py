import json, re, sys
src, label = sys.argv[1], sys.argv[2]
out = "/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/"
d = json.load(open(src))
log = d["logs_content"].lstrip("﻿")
raw = log.split("\n")
print("first:", raw[0][:80], "| original_length:", d.get("original_length"), "| lines:", len(raw))
assert "Current runner version" in raw[0]
lines = []
for l in raw:
    parts = l.split(None, 1)
    if parts and re.match(r'^\d{4}-\d\d-\d\dT', parts[0]):
        l = l.split(parts[0], 1)[1]
        l = l[1:] if l.startswith(" ") else l
    lines.append(l)
rx = re.compile(r'^\s+(PASS|FAIL)\s+(\S+?):')
res = []; np = nf = 0
for l in lines:
    m = rx.match(l)
    if m:
        res.append(f"{m.group(1)} {m.group(2)}")
        if m.group(1) == "PASS": np += 1
        else: nf += 1
last = [l for l in lines if l.startswith("edge_rigidity_probe:")]
lastline = "LAST: " + (last[-1] if last else "none")
print("edge_rigidity count:", len(last))
res.append(lastline)
open(out + f"verdicts-{label}.txt", "w").write("\n".join(res) + "\n")
print("PASS", np, "FAIL", nf); print(lastline)
