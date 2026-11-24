"""Attempt the 16/7 split of the 23 lines: for each, the splices whose T1' image intersects the line,
and whether each such splice's H lines were p0+ext hit lines (unheld) at H."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_hp as hp, rv_prof as pr
rest = [tuple(x) for x in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-23.json')))]
SPL = collections.defaultdict(list)
for s in hp.LED['splices']: SPL[s['file']].append(s)
def tmap(f):
    out = []; delta = 0
    for s in sorted(SPL[f], key=lambda s: (s['start'], s['end'])):
        ts = s['start'] + delta; n = len(s['new'].encode('utf-8'))
        out.append((s, ts, ts + n)); delta += n - (s['end'] - s['start'])
    return out
sitelinesH = collections.defaultdict(set)
res = json.load(open('out-hp.json'))
for r in res:
    if r['status'] == 'unchanged':
        pin = g.lines(g.E, r['file'])[r['line'] - 1]; LH = g.lines(g.H, r['file'])
        sitelinesH[r['file']].add(LH.index(pin) + 1)
    elif r.get('H_lines'):
        for x in range(r['H_lines'][0], r['H_lines'][1] + 1): sitelinesH[r['file']].add(x)
cls = collections.Counter()
for f, x in rest:
    tsp = hp.line_spans(g.text(g.T, f))[x - 1]
    ids = []; hsite = False; hhit = False
    for s, a, b in tmap(f):
        if (a < tsp[1] and b > tsp[0]) or (a == b and tsp[0] <= a <= tsp[1]):
            ids.append(s['id'])
            hs = hp.line_spans(g.text(g.H, f))
            for k, (u, v) in enumerate(hs, 1):
                if u <= s['end'] and v >= s['start']:
                    if k in sitelinesH[f]: hsite = True
                    if pr.hits(g.lines(g.H, f)[k - 1], pr.P0EXT): hhit = True
    key = 'in-splice' if ids else 'no-splice'
    key += '/H-site-line' if hsite else '/H-non-site'
    key += '/H-hit' if hhit else '/H-nohit'
    cls[key] += 1
    print(f, x, ids, key)
print(cls)
