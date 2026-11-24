"""Replacement regions at T1' for non-HP sites, and hit lines in them (sec. 14 'b3' definition,
reimplemented from the design text). Variants: touching test; removed sites' offset lines."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_hp as hp, rv_prof as pr
res = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-hp.json')))
SPL = collections.defaultdict(list)
for s in hp.LED['splices']: SPL[s['file']].append(s)
# sanity: T1' == H + splices for every ledger file
bad = []
for f, ss in SPL.items():
    hb = g.blob(g.H, f); tb = g.blob(g.T, f)
    out = bytearray(); pos = 0
    for s in sorted(ss, key=lambda s: (s['start'], s['end'])):
        out += hb[pos:s['start']]; out += s['new'].encode('utf-8'); pos = s['end']
    out += hb[pos:]
    if bytes(out) != tb: bad.append(f)
print('files where T1p != H+splices:', bad)

def ov(sp, a, b, touching):
    s, e = sp['start'], sp['end']
    if touching:
        return s <= b and e >= a
    return hp.overlaps(sp, a, b)

def tline_of(tb, off):
    return tb[:off].count(b'\n') + 1

def run(touching, removed_lines):
    counts = collections.Counter(); regionlines = set(); prof_lines = collections.defaultdict(set)
    for r in res:
        if r['status'] != 'unchanged': continue
        f = r['file']; s = hp.SM[r['idx']]
        LE = g.lines(g.E, f); pin = LE[s['line'] - 1]
        LH = g.lines(g.H, f)
        idx = [i for i, l in enumerate(LH) if l == pin]
        assert len(idx) == 1, (f, s['line'])
        spans = hp.line_spans(g.text(g.H, f))
        a, b = spans[idx[0]]
        o = [sp for sp in SPL[f] if ov(sp, a, b, touching)]
        if not o:
            counts['unchanged'] += 1; continue
        A = min([a] + [sp['start'] for sp in o]); B = max([b] + [sp['end'] for sp in o])
        def d(sp): return len(sp['new'].encode('utf-8')) - (sp['end'] - sp['start'])
        A2 = A + sum(d(sp) for sp in SPL[f] if sp['end'] <= A and sp not in o)
        B2 = B + sum(d(sp) for sp in SPL[f] if (sp['end'] <= B and sp['start'] < B) or sp in o)
        tb = g.blob(g.T, f)
        if B2 == A2:
            counts['removed'] += 1
            if removed_lines:
                regionlines.add((f, tline_of(tb, A2)))
            continue
        counts['replaced'] += 1
        l1 = tline_of(tb, A2); l2 = tline_of(tb, B2 - 1 if B2 > A2 else B2)
        for x in range(l1, l2 + 1): regionlines.add((f, x))
    hits = {}
    for f, x in regionlines:
        line = g.lines(g.T, f)[x - 1]
        h = pr.hits(line, ('p0-core', 'p0-para', 'ledger-ext', 'count-grep'))
        if h: hits[(f, x)] = h
    p0ext = {k for k, v in hits.items() if set(v) & set(pr.P0EXT)}
    allh = set(hits)
    return counts, len(regionlines), p0ext, allh

base = None
for touching, rl in ((False, False), (True, False), (False, True), (True, True)):
    c, nl, p0ext, allh = run(touching, rl)
    print('touching' if touching else 'strict', '+removed-lines' if rl else '', dict(c), 'region lines', nl, 'p0+ext', len(p0ext), 'with count-grep', len(allh))
    if base is None:
        base = (p0ext, allh)
        print('   count-grep extra:', sorted(allh - p0ext))
        json.dump(sorted(p0ext), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-84.json'), 'w'))
    else:
        print('   extra vs strict p0ext:', sorted(p0ext - base[0]))
