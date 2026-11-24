"""Widened resid (a/b/c): whole-corpus matches at E, H, T1' and added-text matches at T1'; new review total."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv5_rules as r, rv_prof as pr, rv_hp as hp
OTHER = ('p0-core', 'p0-para', 'ledger-ext', 'ptr', 'repo', 'count-grep')
for name, c in (('E', g.E), ('H', g.H), ('T1p', g.T)):
    a = bc = bc_noother = conly = 0
    for f in g.corpus(c):
        for l in g.lines(c, f):
            A = bool(r.RESID_A.search(l)); B = bool(r.RESID_B.search(l)); C = bool(r.RESID_C.search(l))
            a += A
            if (B or C) and not A:
                bc += 1
                if not pr.hits(l, OTHER): bc_noother += 1
            conly += C
    print(name, 'resid-a', a, 'b/c-only', bc, 'of those no other profile', bc_noother, 'resid-c any', conly)
SPL = collections.defaultdict(list)
for s in hp.LED['splices']: SPL[s['file']].append(s)
lines = set()
for f, ss in SPL.items():
    if not f.endswith('.md'): continue
    tsp = hp.line_spans(g.text(g.T, f)); delta = 0
    for s in sorted(ss, key=lambda s: (s['start'], s['end'])):
        a0 = s['start'] + delta; n = len(s['new'].encode('utf-8')); b0 = a0 + n
        delta += n - (s['end'] - s['start'])
        if n == 0: continue
        for k, (u, v) in enumerate(tsp, 1):
            if u < b0 and v + 1 > a0: lines.add((f, k))
cnt = collections.Counter(); only = []; new4 = []
for f, k in sorted(lines):
    l = g.lines(g.T, f)[k - 1]
    A = bool(r.RESID_A.search(l)); X = r.resid(l)
    if not X: continue
    cnt['resid'] += 1; cnt['resid-a'] += A
    if not A: cnt['b/c only'] += 1
    if r.RESID_C.search(l): cnt['c'] += 1
    if not pr.hits(l, OTHER):
        only.append((f, k))
        if not A: new4.append((f, k))
    if r.deny_line(l): cnt['deny!'] += 1
print('added-text lines', len(lines), dict(cnt), 'no-other', len(only), 'new', new4)
json.dump(only, open('out5-resid17.json', 'w'))
for t in ['a finite set with a deterministic bijection on it', 'the substratum is a finite set with a bijection on it', 'We take the substratum to be finite.', 'the universe is assumed finite', 'The substratum is assumed to have a finite number of states.', 'uses a finite set with a deterministic bijection', "the substratum's sixth axiom, finiteness", "the framework's sixth structural property, finiteness of the bijection"]:
    print(bool(r.RESID_A.search(t)), bool(r.RESID_B.search(t)), bool(r.RESID_C.search(t)), r.deny_line(t), pr.hits(t, OTHER), '|', t)
