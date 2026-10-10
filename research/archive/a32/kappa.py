"""Exploration only. (a) Is phi realized by a permutation of the 4096 coordinates?  (b) search
slot-permutation-twisted bilinear forms B_k(x,y) = sum_p x_p y_{k p} (k permutes the six index slots
within the i-triple and within the j-triple) that every family generator preserves (or conjugates,
for the antilinear ones) but phi does not."""
import cmath, itertools, random
from circles import COORDS, R, coord_data
import numpy as np
cidx = {p: n for n, p in enumerate(COORDS)}
data = [coord_data(*r) for r in R]
Sm = np.array([[data[r][p][0] for p in COORDS] for r in range(9)])
mm = np.array([[data[r][p][1] for p in COORDS] for r in range(9)])
# (a) signature of a coordinate: its (S,m) across all nine circles; phi flips m on circle 0
sig = {}
for n in range(4096):
    sig.setdefault(tuple(zip(Sm[:, n], mm[:, n])), []).append(n)
ok = True
for key, lst in sig.items():
    k2 = ((key[0][0], -key[0][1]),) + key[1:]
    if k2 not in sig or len(sig[k2]) != len(lst):
        ok = False
print("(a) phi is a coordinate permutation on the union:", ok, "; signature classes:", len(sig))

def feat(r, z):
    return Sm[r] * z ** mm[r] / 64.0
def phi(r, x):
    return np.conj(x) if r == 0 else x
slotperms = [(a, b) for a in itertools.permutations(range(3)) for b in itertools.permutations(range(3))]
def kmap(a, b):
    idx = np.zeros(4096, dtype=int)
    for n, p in enumerate(COORDS):
        i, j = p
        q = ((i[a[0]], i[a[1]], i[a[2]]), (j[b[0]], j[b[1]], j[b[2]]))
        idx[n] = cidx[q]
    return idx
perms4 = list(itertools.permutations(range(4)))
def relabel_idx(pi, tau):
    idx = np.zeros(4096, dtype=int)
    for n, p in enumerate(COORDS):
        idx[n] = cidx[((pi[p[0][0]], pi[p[0][1]], pi[p[0][2]]), (tau[p[1][0]], tau[p[1][1]], tau[p[1][2]]))]
    return idx
rho = np.array([cidx[((p[1][1], p[1][2], p[1][0]), p[0])] for p in COORDS])
gens = [("R", relabel_idx((1,0,2,3),(0,1,2,3)), False), ("R", relabel_idx((1,2,3,0),(0,1,2,3)), False),
        ("R", relabel_idx((0,1,2,3),(1,0,2,3)), False), ("R", relabel_idx((0,1,2,3),(1,2,3,0)), False),
        ("C", np.arange(4096), True), ("T", rho, True)]
def apply(g, x):
    _, idx, cj = g
    y = x[idx]
    return np.conj(y) if cj else y
random.seed(1)
samples = [(r, cmath.exp(1j*random.uniform(0, 6.28))) for r in range(9) for _ in range(3)]
good = []
for (a, b) in slotperms:
    K = kmap(a, b)
    for herm in (False, True):
        def B(x, y):
            yy = y[K]
            return np.sum(x * (np.conj(yy) if herm else yy))
        inv = True
        for g in gens:
            for _ in range(10):
                (r, z), (s, w) = random.choice(samples), random.choice(samples)
                x, y = feat(r, z), feat(s, w)
                v0, v1 = B(x, y), B(apply(g, x), apply(g, y))
                target = np.conj(v0) if (g[2] and not herm) else v0
                if g[2] and herm:
                    target = np.conj(v0)
                if abs(v1 - target) > 1e-12:
                    inv = False; break
            if not inv: break
        if not inv:
            continue
        sep = 0
        for (r, z) in samples:
            for (s, w) in samples:
                x, y = feat(r, z), feat(s, w)
                sep = max(sep, abs(B(phi(r, x), phi(s, y)) - B(x, y)))
        good.append(((a, b), herm, sep))
print("(b) family-invariant twisted forms and phi's defect:")
for g in good: print("  ", g)
