import json,re,sys
OUT="/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/"
def load(p):
    d=json.load(open(p)); c=d["logs_content"]
    lines=c.split("\n")
    first=lines[0].lstrip("﻿")
    ok=first.split(None,1)[1].startswith("Current runner version") if len(first.split(None,1))>1 else False
    strip=[]
    for l in lines:
        l=l.lstrip("﻿")
        parts=l.split(" ",1)
        if re.match(r'^\d{4}-\d\d-\d\dT',parts[0]): l=parts[1] if len(parts)>1 else ""
        strip.append(l)
    return d.get("original_length"),ok,strip
def verdicts(p,label):
    n,ok,L=load(p)
    rx=re.compile(r'^\s+(PASS|FAIL)\s+(\S+?):')
    out=[];P=F=0
    for l in L:
        m=rx.match(l)
        if m:
            out.append(f"{m.group(1)} {m.group(2)}")
            if m.group(1)=="PASS":P+=1
            else:F+=1
    last=[l for l in L if l.startswith("edge_rigidity_probe:")]
    out.append("LAST: "+(last[-1] if last else "none"))
    open(OUT+f"verdicts-{label}.txt","w").write("\n".join(out)+"\n")
    print(label,"orig_len",n,"starts_ok",ok,"PASS",P,"FAIL",F,"n_last",len(last))
    print(out[-1]); print("Traceback:",any("Traceback" in l for l in L))
def gate(p,label):
    n,ok,L=load(p)
    idx=[i for i,l in enumerate(L) if l=="release gate"]
    print(label,"orig_len",n,"starts_ok",ok,"release gate count",len(idx))
    i=idx[0]; j=next(k for k in range(i+1,len(L)) if L[k].startswith("release gate: "))
    txt="\n".join(L[i:j+1])+"\n"
    open(OUT+f"gate-{label}.txt","w").write(txt); print(txt)
{"v":verdicts,"g":gate}[sys.argv[1]](sys.argv[2],sys.argv[3])
