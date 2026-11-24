"""Distinct T1' corpus lines needing a record or rule under all review profiles (sec. 8.2 total 222)."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_prof as pr, rv_hp as hp, rv_rules as r
rows = g.load('rows.json')
held = collections.defaultdict(set)
for s in hp.SM: held[s['file']].add(g.lines(g.E, s['file'])[s['line'] - 1])
for x in rows['new_site_rules']:
    for k in x.get('read', []):
        f, _, ln = k.rpartition(':'); held[f].add(g.lines(g.E, f)[int(ln) - 1])
need = set(); why = collections.Counter()
for f in g.corpus(g.T):
    for i, l in enumerate(g.lines(g.T, f), 1):
        h = pr.hits(l, ('p0-core', 'p0-para', 'ledger-ext', 'ptr', 'repo', 'count-grep'))
        if not h: continue
        if set(h) & set(pr.P0EXT) and l not in held[f]:
            need.add((f, i)); why['unheld p0+ext'] += 1
        elif set(h) & {'ptr', 'repo', 'count-grep'}:
            need.add((f, i)); why['ptr/repo/count-grep (held or non-p0ext)'] += 1
r13 = {tuple(x) for x in json.load(open('out-resid13.json'))}
print(len(need), dict(why), 'plus resid-only', len(r13 - need), 'total', len(need | r13))
