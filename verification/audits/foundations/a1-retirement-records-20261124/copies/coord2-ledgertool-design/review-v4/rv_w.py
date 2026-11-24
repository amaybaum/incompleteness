"""W1/W2 placement and ptr/repo/count-grep hits in the corpus at T1'."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_prof as pr, rv_hp as hp
s84 = {tuple(x) for x in json.load(open('out-84.json'))}
pins = collections.defaultdict(set)
for s in hp.SM:
    pins[s['file']].add(g.lines(g.E, s['file'])[s['line'] - 1])
for prof in ('ptr', 'repo', 'count-grep'):
    hs = [(f, i) for f in g.corpus(g.T) for i, l in enumerate(g.lines(g.T, f), 1) if pr.hits(l, (prof,))]
    print(prof, len(hs))
    for f, i in hs:
        l = g.lines(g.T, f)[i - 1]
        print('   ', f, i, 'p0ext' if pr.hits(l, pr.P0EXT) else '-', 'in84' if (f, i) in s84 else '-', 'sitepin' if l in pins[f] else '-')
