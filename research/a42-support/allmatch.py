"""Matching-complete census at SIG: for each census partition pair (column blocks, row classes), every matching of the
row classes (which rows share the index a) for which SIG satisfies the relaxed Dita conditions exactly. The equation
matrices of all of them (both forms) are saved as the extended family F_all."""
import itertools, pickle, numpy as np
from lib42 import *
from matching import relaxed_ok
fam = []
for (nm, tr, s) in STRUCTS:
    if tr: continue
    (m, n), cp, rows = s
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}
    good = []
    for perms in itertools.product(itertools.permutations(range(m)), repeat=n - 1):
        row = {}
        for a in range(m): row[(a, 0)] = rows[0][a]
        for b in range(1, n):
            for a in range(m): row[(a, b)] = rows[b][perms[b - 1][a]]
        if relaxed_ok(SIG, m, n, row, col):
            good.append(tuple(tuple(row[(a, b)] for b in range(n)) for a in range(m)))
    print(nm, (m, n), 'valid matchings', len(good), flush=True)
    for g in good:
        rows2 = tuple(tuple(g[a][b] for a in range(m)) for b in range(n))
        for trf in (False, True):
            fam.append((nm, trf, g, np.array(struct_eqs((m, n), cp, rows2, True, trf), dtype=np.int64)))
print('family size (both forms)', len(fam))
pickle.dump(fam, open('Fall.pkl', 'wb'))
