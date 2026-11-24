"""Deny counts (v5 active set; with and without the retired DR-1d/DR-2) at E, H, W, T1', line level and
sentence level under splitter v1 and v2; AGENTS.md witness for DR-3."""
import sys, os, collections, hashlib, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv5_rules as r
W = '413b0bb88f39cad901befcf4684355c7ee39480b'
out = {}
for name, c in (('E', g.E), ('H', g.H), ('W', W), ('T1p', g.T)):
    for retired in (False, True):
        per = collections.defaultdict(set); allines = set()
        for f in g.corpus(c):
            for i, l in enumerate(g.lines(c, f), 1):
                for k in r.deny_line(l, retired):
                    per[k].add((f, i)); allines.add((f, i))
        res = {k: len(v) for k, v in sorted(per.items())}
        print(name, 'retired-incl' if retired else 'active', 'lines', res, 'distinct', len(allines))
        if not retired: out[name] = sorted(allines)
    for v in (1, 2):
        sent = collections.Counter()
        for f in g.corpus(c):
            for lns, p in r.paragraphs(g.lines(c, f), v):
                for s in r.split_sentences(p, v):
                    for k in r.deny_sentence(s, True): sent[k] += 1
        print(name, 'sentences splitter v%d (incl. retired)' % v, dict(sorted(sent.items())))
json.dump(out, open('out5-denylines.json', 'w'))
for name, c in (('H', g.H), ('T1p', g.T)):
    b = g.blob(c, 'AGENTS.md'); bid = g.git('rev-parse', '%s:AGENTS.md' % c).strip()
    L = b.decode().split('\n'); hits = []
    for v in (1, 2):
        for lns, p in r.paragraphs(L, v):
            for s in r.split_sentences(p, v):
                d = r.deny_sentence(s, True)
                if d: hits.append((v, lns[0], lns[-1], d, s[:120]))
    print('AGENTS.md', name, 'blob', bid, 'sha256', hashlib.sha256(b).hexdigest())
    for h in hits: print('   ', h)
