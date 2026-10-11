#!/usr/bin/env python3
"""Coordinator's job-log parser for the round-4 bridge runs.  Input: the saved job-log tool result (JSON with
logs_content, or raw text).  Prints: the step headers, Build summary lines, 'Built OIBridge.*' lines, error lines,
the per-module `#print axioms` counts (wrapped lines joined; names with primes counted by raw line), the gate table
and the lean-axioms line.  Writes the unescaped log to <raw>.txt."""
import json, re, sys
raw = open(sys.argv[1]).read()
txt = None
try:
    j = json.loads(raw)
    if isinstance(j, dict):
        for k in ('logs_content', 'content', 'log'):
            if k in j: txt = j[k]; break
        if txt is None:
            for v in j.values():
                if isinstance(v, str) and 'OIBridge' in v: txt = v; break
except Exception:
    pass
if txt is None:
    txt = raw
    if '\\n' in raw and raw.count('\n') < 5: txt = raw.encode().decode('unicode_escape')
out = sys.argv[1].rsplit('.', 1)[0] + '.txt'
open(out, 'w').write(txt)
lines = txt.splitlines()
print('LINES', len(lines), '->', out)
# strip timestamps
def body(l):
    return re.sub(r'^\S*\d{4}-\d\d-\d\dT[\d:.]+Z\s?', '', l)
B = [body(l) for l in lines]
print('--- step headers ---')
for l in B:
    if l.startswith('##[group]Run ') or l.startswith('##[group]') and ('Build' in l or 'gate' in l.lower() or 'Restore' in l):
        print('  ', l[:120])
print('--- build summary ---')
for l in B:
    if 'Build completed' in l or 'Some required targets' in l or 'build failed' in l.lower() or 'Some builds logged failures' in l:
        print('  ', l[:160])
print('--- Built OIBridge.* (design + listed) ---')
for l in B:
    m = re.search(r'\[(\d+)/(\d+)\] (Built|Building|Replayed) OIBridge\.(\w+)', l)
    if m and m.group(4) in ('BridgeAvail','BridgeAvailFull','BridgeConverge','BridgeReachDim','BridgeDictionary','BridgeReach','EqvK2Schema'):
        print('  ', l.strip()[:140])
print('--- error lines (first 60) ---')
n=0
for l in B:
    if re.search(r'error:', l) and 'warning' not in l[:20]:
        print('  ', l.strip()[:220]); n+=1
        if n>=60: print('   ...'); break
print('--- #print axioms per module (joined wrapped lines) ---')
# join: a line that starts with "'" or with "OIBridge." continuing a prior "depends on axioms" line w/o closing bracket
joined=[]; buf=None
for l in B:
    s=l.rstrip()
    if buf is not None:
        buf += ' ' + s.strip()
        if ']' in s: joined.append(buf); buf=None
        continue
    if "depends on axioms" in s or 'does not depend on any axioms' in s:
        if 'depends on axioms' in s and ']' not in s: buf=s; continue
        joined.append(s)
from collections import defaultdict, Counter
per=defaultdict(Counter); names=defaultdict(list)
for s in joined:
    m=re.search(r"'([^']*)' (depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", s)
    if not m:
        m2=re.search(r"'(\S+?)' depends", s)
        print('  UNPARSED', s[:160]); continue
    name=m.group(1); ax=m.group(3) if m.group(3) else 'NONE'
    mod=name.split('.')[1] if name.startswith('OIBridge.') and name.count('.')>=2 else name.split('.')[0]
    key='std' if ax.replace(' ','')=='propext,Classical.choice,Quot.sound' else ('sorry' if 'sorryAx' in ax else ax)
    per[mod][key]+=1; names[mod].append((name,key))
for mod in sorted(per):
    if mod in ('BridgeAvail','BridgeAvailFull','BridgeConverge','BridgeReachDim','BridgeDictionary','BridgeReach','EqvK2Schema'):
        print('  ', mod, dict(per[mod]))
        bad=[n for n,k in names[mod] if k!='std']
        if bad: print('      non-standard:', bad[:20])
print('  (raw "depends on axioms" lines:', sum(1 for l in B if 'depends on axioms' in l), '; joined entries:', len(joined), ')')
print('--- gate ---')
for l in B:
    s=l.strip()
    if re.search(r'^\|?\s*(PASS|FAIL|OK|ERROR)\b', s) or 'named result' in s or 'lean-axioms' in s or 'lean-manuscript' in s or 'Release gate' in s or 'release gate' in s.lower() or 'v3-receipts' in s or 'legacy-records' in s:
        print('  ', s[:170])
