import re, os, json, sys
OI='/home/user/incompleteness/verification/lean-mathlib'
ML='/home/user/leanprover-community/mathlib4'
mods = json.load(open('decls_parity.json'))['modules']
start=set()
for m in mods:
    s=open(os.path.join(OI,*m.split('.'))+'.lean').read()
    start |= set(re.findall(r'^import (Mathlib[\w.]*)', s, re.M))
seen=set(); stack=list(start)
while stack:
    m=stack.pop()
    if m in seen: continue
    seen.add(m)
    p=os.path.join(ML,*m.split('.'))+'.lean'
    if not os.path.exists(p): print('missing', m); continue
    s=open(p).read()
    for x in re.findall(r'^(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?(Mathlib[\w.]*)', s, re.M):
        stack.append(x)
print(len(seen))
for t in sys.argv[1:]:
    print(t, t in seen)
