"""compare two control reports by id: status, actual (paths/time-normalised), expected, predicate. usage: cmp.py A B [ignore-key ...]"""
import json, re, sys
def load(f):
    d = json.load(open(f)); L = d['controls'] if isinstance(d, dict) and 'controls' in d else d
    return {x['id']: x for x in L}
NORM = [(re.compile(r'<tmp>/claude-0/[^"\s\']*?/(rv-corr2|v60e-repro-corr2|v60e-repro-corr1|rv-corr1)/(out/)?'), '<OUT>/'),
        (re.compile(r'<tmp>/[A-Za-z0-9_.-]+'), '<TMP>')]
IGN = set(sys.argv[3:])
def strip(x):
    if isinstance(x, dict): return {k: strip(v) for k, v in x.items() if k not in IGN}
    if isinstance(x, list): return [strip(v) for v in x]
    if isinstance(x, str):
        for r, s in NORM: x = r.sub(s, x)
    return x
a, b = load(sys.argv[1]), load(sys.argv[2])
print('ids', len(a), len(b), 'same set', set(a) == set(b))
for k in sorted(set(a) | set(b)):
    if k not in a or k not in b: print('MISSING', k); continue
    for f in ('status', 'expected', 'predicate', 'actual'):
        if strip(a[k].get(f)) != strip(b[k].get(f)): print('DIFF', k, f)
