"""resid on added text at T1': lines of .md ledger files containing a non-empty splice image."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_prof as pr, rv_hp as hp, rv_rules as r
SPL = collections.defaultdict(list)
for s in hp.LED['splices']: SPL[s['file']].append(s)
lines = set()
for f, ss in SPL.items():
    if not f.endswith('.md'): continue
    tsp = hp.line_spans(g.text(g.T, f)); delta = 0
    for s in sorted(ss, key=lambda s: (s['start'], s['end'])):
        a = s['start'] + delta; n = len(s['new'].encode('utf-8')); b = a + n
        delta += n - (s['end'] - s['start'])
        if n == 0: continue
        for k, (u, v) in enumerate(tsp, 1):
            if u < b and v + 1 > a:   # line content plus its LF intersects the image
                lines.add((f, k))
OTHER = ('p0-core', 'p0-para', 'ledger-ext', 'ptr', 'repo', 'count-grep')
hitr = []; only = []
for f, k in sorted(lines):
    l = g.lines(g.T, f)[k - 1]
    if r.RESID.search(l):
        hitr.append((f, k))
        if not pr.hits(l, OTHER):
            only.append((f, k))
print('added-text lines', len(lines), 'resid', len(hitr), 'resid-only', len(only))
for f, k in only:
    l = g.lines(g.T, f)[k - 1]
    m = r.RESID.search(l)
    print('%s:%d | ...%s...' % (f, k, l[max(0, m.start() - 80): m.end() + 60]))
json.dump(only, open('out-resid13.json', 'w'))
# variant: content-only intersection
lines2 = set()
for f, ss in SPL.items():
    if not f.endswith('.md'): continue
    tsp = hp.line_spans(g.text(g.T, f)); delta = 0
    for s in sorted(ss, key=lambda s: (s['start'], s['end'])):
        a = s['start'] + delta; n = len(s['new'].encode('utf-8')); b = a + n
        delta += n - (s['end'] - s['start'])
        if n == 0: continue
        for k, (u, v) in enumerate(tsp, 1):
            if u < b and v > a: lines2.add((f, k))
print('variant content-only lines', len(lines2))
