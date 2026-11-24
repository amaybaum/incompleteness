"""Line-attributed overlap (sec. 3.4 diagnostic): carry the site's line range through
git diff -U0 --no-renames (myers) hunks per first-parent step, then intersect splices at H."""
import sys, os, json, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_hp as hp
res = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-hp.json')))
def hunks(p, c, f, algo):
    out = g.git('diff', '-U0', '--no-renames', '--diff-algorithm=' + algo, p, c, '--', f)
    hs = []
    for m in re.finditer(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', out, re.M):
        a, b, c2, d = int(m.group(1)), int(m.group(2) or 1), int(m.group(3)), int(m.group(4) or 1)
        hs.append((a, b, c2, d))
    return hs
def carry(rng, hs):
    lo, hi = rng  # inclusive line numbers, 1-based
    nlo = nhi = None; shift_lo = shift_hi = 0; touched = False
    newlo, newhi = lo, hi
    delta = 0; out_lo = out_hi = None
    for a, b, c, d in hs:
        old_start = a if b > 0 else a + 1   # for b == 0, insertion after line a
        old_end = a + b - 1
        if b > 0 and old_start <= hi and old_end >= lo:
            touched = True
            cand_lo = c if d > 0 else None
            cand_hi = c + d - 1 if d > 0 else None
            if cand_lo is not None:
                out_lo = cand_lo if out_lo is None else min(out_lo, cand_lo)
                out_hi = cand_hi if out_hi is None else max(out_hi, cand_hi)
    # unchanged parts of range: map with deltas
    def mapline(x):
        dl = 0
        for a, b, c, d in hs:
            end = a + b - 1 if b > 0 else a
            if (b > 0 and end < x) or (b == 0 and a < x):
                dl += d - b
        return x + dl
    parts = []
    for x in range(lo, hi + 1):
        inside = any(b > 0 and a <= x <= a + b - 1 for a, b, c, d in hs)
        if not inside: parts.append(mapline(x))
    for a, b, c, d in hs:
        if b > 0 and a <= hi and a + b - 1 >= lo and d > 0:
            parts += [c, c + d - 1]
        # insertions strictly inside the range
        if b == 0 and lo <= a < hi:
            parts += [c, c + d - 1]
    if not parts: return None, touched
    return (min(parts), max(parts)), touched
out = {}
for algo in ('myers', 'histogram'):
    sites = {}; n_spl = set()
    for r in res:
        if r['status'] != 'changed': continue
        rng = (r['line'], r['line'])
        for c in hp.chain:
            p = hp.parents[c]
            if g.blob(p, r['file']) == g.blob(c, r['file']): continue
            rng, t = carry(rng, hunks(p, c, r['file'], algo))
            if rng is None: break
        if rng is None: continue
        spans = hp.line_spans(g.text(g.H, r['file']))
        a = spans[rng[0] - 1][0]; b = spans[rng[1] - 1][1]
        ov = [sp['id'] for sp in hp.LED['splices'] if sp['file'] == r['file'] and hp.overlaps(sp, a, b)]
        if ov:
            sites[(r['file'], r['line'])] = ov; n_spl |= set(ov)
    print(algo, 'sites', len(sites), 'splices', len(n_spl))
    reg = {(r['file'], r['line']) for r in res if r.get('overlap')}
    print('  region-only', sorted(reg - set(sites)), 'line-only', sorted(set(sites) - reg))
