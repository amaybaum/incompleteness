import json,re,sys
kind,label,path=sys.argv[1:4]
out="/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/"
d=json.load(open(path))
raw=d["logs_content"].lstrip("﻿")
lines=raw.split("\n")
print("first:",lines[0][:90],"| orig_len",d.get("original_length"),"| nlines",len(lines))
if kind=="v": assert "Current runner version" in lines[0]
def strip(l):
    p=l.split(None,1)
    return p[1] if len(p)>1 else ""
# preserve leading whitespace after timestamp: strip only first token and single space
def strip2(l):
    m=re.match(r'^\S+ ?',l)
    return l[m.end():] if m else l
L=[strip2(l.rstrip("\r")) for l in lines]
if kind=="v":
    rx=re.compile(r'^\s+(PASS|FAIL)\s+(\S+?):')
    res=[]
    for l in L:
        m=rx.match(l)
        if m: res.append(f"{m.group(1)} {m.group(2)}")
    last=[l for l in L if l.startswith("edge_rigidity_probe:")]
    res.append("LAST: "+(last[-1] if last else "none"))
    open(out+f"verdicts-{label}.txt","w").write("\n".join(res)+"\n")
    print("PASS",sum(r.startswith("PASS ") for r in res),"FAIL",sum(r.startswith("FAIL ") for r in res))
    print(res[-1]); print("n edge lines",len(last))
else:
    i=next(k for k,l in enumerate(L) if l=="release gate")
    j=next(k for k in range(i,len(L)) if L[k].startswith("release gate: "))
    seg=L[i:j+1]
    open(out+f"gate-{label}.txt","w").write("\n".join(seg)+"\n")
    print(seg[-1]); print("PASS",sum(s.startswith("  PASS") for s in seg),"FAIL",sum(s.startswith("  FAIL") for s in seg), "count 'release gate' lines", sum(l=="release gate" for l in L))
