#!/usr/bin/env python3
"""Apply every module-level regex of edits_check.py at P to the lines PR #1553 adds (M..47e23023)."""
import re, subprocess
R="<repo>"; P="4c79be642ca631573f06b444903be75ec4f5e2b6"
X="verification/audits/foundations/a1exit-deletion-20261121"
src=subprocess.check_output(["git","-C",R,"show",f"{P}:{X}/edits_check.py"]).decode()
d=subprocess.check_output(["git","-C",R,"diff","-U0","4fb2c1eed350edf95da2b316abcca93717246589","47e23023450fb8fcbd61b5c776a69ba61897f267","--","AGENTS.md"]).decode()
added=[l[1:] for l in d.splitlines() if l.startswith("+") and not l.startswith("+++")]
print("added lines",len(added))
for m in re.finditer(r'^([A-Z_0-9]+) = (re\.compile\(.*?\))\n(?=\S)',src,re.M|re.S):
    try: p=eval(m.group(2),{"re":re})
    except Exception as e: print(m.group(1),"eval error",e); continue
    hits=[(i,x.group(0)) for i,l in enumerate(added) for x in p.finditer(l)]
    print(m.group(1),len(hits),hits[:5])
