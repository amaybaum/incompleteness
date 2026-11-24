"""Illustration: cost at T1' (287 added-text lines) of extending resid with a finite-set / finite-substratum
alternative that catches the rv_fn.py false negatives."""
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_prof as pr, rv_hp as hp, rv_rules as r
EXT = re.compile(r"(?i)\bfinite\s+(?:\w+\s+)?set\b|\b(?:substratum|universe|world)\b[^.;]{0,40}\b(?:is|be|being|are)\s+(?:a\s+)?(?:\w+\s+)?finite\b")
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
            if u < b and v + 1 > a: lines.add((f, k))
OTHER = ('p0-core', 'p0-para', 'ledger-ext', 'ptr', 'repo', 'count-grep')
new = []
for f, k in sorted(lines):
    l = g.lines(g.T, f)[k - 1]
    if EXT.search(l) and not r.RESID.search(l) and not pr.hits(l, OTHER):
        m = EXT.search(l); new.append('%s:%d ...%s...' % (f, k, l[max(0, m.start() - 60): m.end() + 40]))
print('extra REVIEW lines at T1p from the extension:', len(new))
for x in new: print('  ', x)
tests = ['a finite set with a deterministic bijection on it', 'the substratum is a finite set with a bijection on it', 'We take the substratum to be finite.', 'the universe is assumed finite']
for t in tests: print(bool(EXT.search(t)), t)
