import sys, os, collections, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_rules as r
res = {}
for name, c in (('E', g.E), ('H', g.H), ('T1p', g.T)):
    per = collections.defaultdict(set); sent = collections.Counter(); allines = set()
    for f in g.corpus(c):
        L = g.lines(c, f)
        for i, l in enumerate(L, 1):
            for k in r.deny_line(l):
                per[k].add((f, i)); allines.add((f, i))
        for lns, ptxt in r.paragraphs(L):
            for s in r.split_sentences(ptxt):
                for k in r.deny_sentence(s):
                    sent[k] += 1
    dr1 = per['DR-1a'] | per['DR-1b'] | per['DR-1c'] | per['DR-1d']
    print(name, 'lines:', {k: len(v) for k, v in sorted(per.items())}, 'DR-1 union', len(dr1), 'distinct all', len(allines))
    print(name, 'sentences:', dict(sorted(sent.items())))
    res[name] = {k: sorted(v) for k, v in per.items()}
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-dr.json'), 'w'), indent=1)
for k in ('DR-1a', 'DR-1b', 'DR-4', 'DR-5'):
    print(k, res['H'].get(k))
