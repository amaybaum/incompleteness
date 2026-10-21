"""Reviewer control for owner_n4_none.py's use of copy_search: reproduce the committed strict
n = 4 ops = none tally (E:12, AH:24 at k = 1; E:12 at k = 2, 4) with the same calling pattern."""
import sys
sys.path.insert(0, sys.argv[1])
from itertools import product
import copy_search as cs
n, cls = 4, "none"; tally = {}; ncfg = 0
for edges in cs.all_graphs(n):
    for cl in [c for c in product("VH", repeat=n) if "V" in c and "H" in c]:
        vis = [c for x, ch in enumerate(cl) if ch == "V" for c in (x, n + x)]
        hidc = [c for c in range(2 * n) if c not in vis]
        if len(vis) < 2 or len(hidc) < 2: continue
        for P in hidc:
            for Y in hidc:
                if P == Y: continue
                ncfg += 1
                out, hid, vs, Z = cs.run(n, edges, vis, P, Y, cls)
                for k in range(1, 5):
                    best = None
                    for Qc in vis:
                        for Xc in vis:
                            if Qc == Xc: continue
                            b = cs.check(out[k], hid, vs, Z, P, Y, Qc, Xc, cls)
                            if b and (best is None or "E AV AH".split().index(b) < "E AV AH".split().index(best)): best = b
                    if best: tally[(k, best)] = tally.get((k, best), 0) + 1
print("cases", ncfg, sorted(tally.items()))
