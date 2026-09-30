"""Exact description of each row-pair's vanishing family: antipodal class pairs (columns k with c(k) = v vs c(k) = -v),
and the vanishing subsets that are not antipodally balanced. Verified against the exact subset tables."""
import numpy as np
from lib42 import *
from dfs42 import VT, PC
def pair_structure(i, i2):
    c = [SIG[i][k] * SIG[i2][k].conj() for k in range(16)]
    classes = {}
    for k in range(16):
        key = c[k].key(); nkey = (-c[k]).key()
        if nkey in classes: classes[nkey][1].append(k)
        else: classes.setdefault(key, ([], []))[0].append(k)
    cps = [(sum(1 << k for k in a), sum(1 << k for k in b)) for a, b in classes.values()]
    allm = np.arange(1 << 16)
    bal = np.ones(1 << 16, dtype=bool)
    for a, b in cps: bal &= PC[allm & a] == PC[allm & b]
    V = VT[i, i2]
    assert not (bal & ~V).any()           # balanced => vanishing (antipodal pairs cancel)
    exc = np.flatnonzero(V & ~bal).tolist()
    return cps, exc
if __name__ == '__main__':
    import collections
    ty = collections.Counter()
    for i in range(16):
        for i2 in range(i + 1, 16):
            cps, exc = pair_structure(i, i2)
            ty[(tuple(sorted((PC[a], PC[b]) for a, b in cps)), len(exc))] += 1
    print(ty)
