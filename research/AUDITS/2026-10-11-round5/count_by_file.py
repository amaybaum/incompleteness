"""Count '#print axioms' results per SOURCE FILE in a saved Mathlib-bridge job log (wrapped lines joined).
Attribution is by the info line's file path `OIBridge/<File>.lean:<line>:<col>`, not by namespace, because a design
module may reuse another module's namespace.
Usage: python3 -I -B count_by_file.py <saved-log> [File ...]
Prints per file: prints, standard ([propext, Classical.choice, Quot.sound]), subset-of-standard without sorryAx,
sorryAx, and the names of every non-standard print.
"""
import re, sys
path = sys.argv[1]; want = set(sys.argv[2:])
lines = [re.sub(r'^\S*\d{4}-\d{2}-\d{2}T[\d:.]+Z\s?', '', ln) for ln in open(path, encoding='utf-8', errors='replace').read().split('\n')]
text = '\n'.join(lines)
pat = re.compile(r"OIBridge/(\w+)\.lean:(\d+):\d+:\s+'(\S+)'\s+depends\s+on\s+axioms:\s*\[([^\]]*)\]", re.S)
pat0 = re.compile(r"OIBridge/(\w+)\.lean:(\d+):\d+:\s+'(\S+)'\s+does\s+not\s+depend\s+on\s+any\s+axioms")
STD = 'propext, Classical.choice, Quot.sound'
per = {}
for f, ln, n, a in pat.findall(text):
    per.setdefault(f, []).append((int(ln), n, re.sub(r'\s+', ' ', a).strip()))
for f, ln, n in pat0.findall(text):
    per.setdefault(f, []).append((int(ln), n, '(none)'))
for f in sorted(per):
    if want and f not in want: continue
    rows = per[f]
    std = [r for r in rows if r[2] == STD]
    sorry = [r for r in rows if 'sorryAx' in r[2]]
    sub = [r for r in rows if r[2] != STD and 'sorryAx' not in r[2]]
    print(f'FILE {f}: prints={len(rows)} standard={len(std)} subset-no-sorry={len(sub)} sorryAx={len(sorry)}')
    for r in sub: print(f'   SUBSET {r[1]} [{r[2]}] (line {r[0]})')
    for r in sorry: print(f'   SORRY  {r[1]} (line {r[0]})')
missing = sorted(want - set(per))
if missing: print('FILES WITH NO PRINTS IN THE TAIL:', missing)
