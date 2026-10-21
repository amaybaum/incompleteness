"""Reviewer driver: copy_search.py's owner-form block at n = 4, ops = none only (the block the
committed copy_search_n4.out never reached).  Mirrors copy_search.main() for mode 'owner'."""
import sys, time
sys.path.insert(0, sys.argv[1])
from itertools import product
import copy_search as cs
n, cls = 4, "none"
tally, ex, ncfg = {}, {}, 0
t0 = time.time()
for edges in cs.all_graphs(n):
    for cl in [("a", "a") + c for c in product("VHab", repeat=n - 2)]:
        vis = []
        for x, c in enumerate(cl):
            vis += {"V": [x, n + x], "H": [], "a": [x], "b": [n + x]}[c]
        hidc = [c for c in range(2 * n) if c not in vis]
        if len(vis) < 2 or len(hidc) < 2:
            continue
        for (P, Yc) in [(n + 1, n + 2)]:
            ncfg += 1
            out, hid, vs, Z = cs.run(n, edges, vis, P, Yc, cls)
            for k in range(1, cs.KMAX + 1):
                bestk = None
                for (Qc, Xc) in [(1, 2)]:
                    b = cs.check(out[k], hid, vs, Z, P, Yc, Qc, Xc, cls)
                    if b and (bestk is None or "E AV AH".split().index(b) < "E AV AH".split().index(bestk)):
                        bestk = b
                if bestk:
                    tally[(k, bestk)] = tally.get((k, bestk), 0) + 1
                    ex.setdefault((k, bestk), (edges, cl))
print(f"[owner] n=4 ops=none: cases={ncfg}")
for k in range(1, cs.KMAX + 1):
    c = [f"{x}:{tally[(k, x)]}" for x in ("E", "AV", "AH") if (k, x) in tally]
    print(f"    k={k}: record-safe copy realizations: {', '.join(c) if c else 'none'}")
for key, e in sorted(ex.items()):
    print("   example", key, e)
print(f"elapsed {time.time()-t0:.1f}s")
