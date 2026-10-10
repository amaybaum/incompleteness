import json, re, sys
OUT="/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/"
def load(p):
    d=json.load(open(p))
    c=d["logs_content"].lstrip("﻿")
    lines=c.split("\n")
    strip=[]
    for l in lines:
        parts=l.split(None,1) if l.strip() else []
        # strip first whitespace-delimited token (timestamp), keep remaining text including leading spaces
        m=re.match(r'^\S+ ?', l)
        strip.append(l[m.end():] if m else l)
    return d, lines, strip
mode, path, label = sys.argv[1:4]
d, raw, lines = load(path)
print("original_length", d.get("original_length"), "nlines", len(raw))
print("first:", raw[0][:100])
if mode=="probes":
    out=[]; last=None
    for l in lines:
        m=re.match(r'^\s+(PASS|FAIL)\s+(\S+?):', l)
        if m: out.append(f"{m.group(1)} {m.group(2)}")
        if l.startswith("edge_rigidity_probe:"): last=l
    out.append("LAST: "+(last if last is not None else "none"))
    open(OUT+f"verdicts-{label}.txt","w").write("\n".join(out)+"\n")
    print("PASS",sum(x.startswith("PASS ") for x in out),"FAIL",sum(x.startswith("FAIL ") for x in out))
    print(out[-1])
    print("edge lines:", sum(l.startswith("edge_rigidity_probe:") for l in lines))
else:
    idx=[i for i,l in enumerate(lines) if l=="release gate"]
    print("release gate count", len(idx))
    i=idx[0]
    j=next(k for k in range(i,len(lines)) if lines[k].startswith("release gate: "))
    seg=lines[i:j+1]
    open(OUT+f"gate-{label}.txt","w").write("\n".join(seg)+"\n")
    print(seg[-1])
    print("  PASS",sum(x.startswith("  PASS") for x in seg),"  FAIL",sum(x.startswith("  FAIL") for x in seg), "len", len(seg))
