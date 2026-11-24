"""All deny rules over the ledgered files that lie outside papers/*.md and book/*.md, at H and T1'."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_rules as r
files = sorted(f for f in g.load('ledger.json')['files'] if f not in g.corpus(g.H))
print('ledgered non-corpus files:', files)
for n, c in (('H', g.H), ('T1p', g.T)):
    for f in files:
        if not (f.endswith('.md') or f.endswith('.py') or f.endswith('.json') or f.endswith('.lean')): pass
        t = g.text(c, f)
        if t is None: continue
        L = t.split('\n')
        for i, l in enumerate(L, 1):
            d = r.deny_line(l)
            if d: print(n, 'line', f, i, d, l[:150])
        for lns, p in r.paragraphs(L):
            for s in r.split_sentences(p):
                d = r.deny_sentence(s)
                if d: print(n, 'sent', f, lns[0], d, s[:220])
