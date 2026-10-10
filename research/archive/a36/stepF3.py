"""Step F3: hull absorption in R-coordinates (fast, exact). Rebuilds the hull list as step F, then works in the 23 coordinates of R."""
import pickle, time, itertools, importlib.util, sys
from lib36 import *
t0 = time.time()
# reuse step F's constructions by importing its code up to the hull list
src = open('stepF.py', encoding='utf-8').read()
src = src[:src.index("print('hulls through the point:'")]
ns = {}; exec(src, ns)
hulls = ns['hulls']; spaces = ns['spaces']; Gb, Tb, Rb = ns['Gb'], ns['Tb'], ns['Rb']
print('hulls:', len(hulls), '(%.0fs)' % (time.time() - t0))
pickle.dump({'hulls': hulls, 'secs': None}, open('stepF.pkl', 'wb'))
basis = Gb + Tb + Rb
Rr, piv = rref(basis, 256); PIV = piv[:80]
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); INV = [r[80:] for r in Ri]
def coords_R(v): return [sum(INV[j][i] * v[PIV[i]] for i in range(80)) for j in range(80)][57:]     # image in R = ker/(gauge+T)
imgs = []
for nm, vecs in hulls:
    cs = [coords_R(v) for v in vecs]
    cs = [c for c in cs if any(x != 0 for x in c)]
    Rh, ph = rref(cs, 23) if cs else ([], [])
    imgs.append((nm, Rh, ph))
print('hull images in R computed (%.0fs)' % (time.time() - t0))
from collections import Counter
print('image dims in R by orientation:', Counter((nm, len(Rh)) for nm, Rh, ph in imgs))
allimg = [r for _, Rh, _ in imgs for r in Rh]
print('span of all hull images in R:', rank(allimg, 23) if allimg else 0, 'of 23')
distinct = Counter(tuple(tuple(x) for x in Rh) for _, Rh, _ in imgs)
print('distinct absorbed subspaces of R:', len(distinct))
def in_span(v, Rh, ph):
    v = [Fr(x) for x in v]
    for i, p in enumerate(ph):
        if v[p] != 0:
            f = v[p]; v = [x - f * y for x, y in zip(v, Rh[i])]
    return all(x == 0 for x in v)
for si, V in enumerate(spaces):
    full = [hi for hi, (nm, Rh, ph) in enumerate(imgs) if all(in_span(a, Rh, ph) for a in V)]
    best = 0; bestn = None
    for hi, (nm, Rh, ph) in enumerate(imgs):
        d = len(V) + len(Rh) - rank([list(a) for a in V] + [list(r) for r in Rh], 23)
        if d > best: best, bestn = d, nm
    names = sorted(set(imgs[h][0] for h in full))
    print('  sector %d (dim %d): absorbed entirely by %d hulls %s | largest overlap with a single hull: %d (%s)' % (si, len(V), len(full), names, best, bestn))
    # overlap with the union of the fixed-orientation families: swapped, mixed, parity
    for tag in ('column ((0, 4, 8, 12)', 'row ((0, 4, 8, 12)', 'column ((0, 2, 9, 11)', 'row ((0, 2, 9, 11)', 'column ((0, 2, 8, 10)', 'row ((0, 2, 8, 10)'):
        rows_ = [r for nm, Rh, ph in imgs if nm.startswith(tag) for r in Rh]
        if rows_:
            d = len(V) + rank(rows_, 23) - rank([list(a) for a in V] + rows_, 23)
            print('      overlap with the span of %s hulls (dim %d): %d' % (tag, rank(rows_, 23), d))
pickle.dump({'hulls': hulls, 'imgs': imgs}, open('stepF.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
