import json, re, sys
src, label = sys.argv[1], sys.argv[2]
out = "/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/"
d = json.load(open(src))
log = d["logs_content"].lstrip("﻿")
raw = log.split("\n")
print("lines:", len(raw), "original_length:", d.get("original_length"), "first:", raw[0][:90])
lines = []
for l in raw:
    parts = l.split(None, 1)
    if parts and re.match(r'^\d{4}-\d\d-\d\dT', parts[0]):
        l = l.split(parts[0], 1)[1]
        l = l[1:] if l.startswith(" ") else l
    lines.append(l)
starts = [i for i, l in enumerate(lines) if l == "release gate"]
print("'release gate' count:", len(starts))
assert len(starts) == 1
s = starts[0]
e = next(i for i in range(s + 1, len(lines)) if lines[i].startswith("release gate: "))
seg = lines[s:e + 1]
open(out + f"gate-{label}.txt", "w").write("\n".join(seg) + "\n")
print("seg lines:", len(seg))
print("final:", seg[-1])
print("  PASS:", sum(l.startswith("  PASS") for l in seg), "  FAIL:", sum(l.startswith("  FAIL") for l in seg))
