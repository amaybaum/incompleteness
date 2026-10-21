"""For every record-safe E/AV realization of the owner's copy rule found by copy_search.py
(strict partition; n = 3 all classes, n = 4 ops = none), test whether the hidden kick P' = P + Y
is CAUSED by the recording: rerun the same number of update steps with every observer operation
removed and the visible sector replaced by an arbitrary state, and check whether the hidden
output rows of P' and Y' (restricted to hidden inputs) are unchanged.  'Unconditional' means the
kick happens whether or not anything is recorded."""
from itertools import product
import copy_search as cs
from f2 import lattice_update, compose, identity

def hidden_rows_free(n, edges, vis, k):
    M = lattice_update(n, edges)
    T = identity(2 * n)
    for _ in range(k):
        T = compose(M, T)
    return T

tot = uncond = 0
for (n, classes) in ((3, ("none", "cell", "GL")), (4, ("none",))):
    for cls in classes:
        for edges in cs.all_graphs(n):
            for cl in product("VH", repeat=n):
                if "V" not in cl or "H" not in cl:
                    continue
                vis = [c for x, ch in enumerate(cl) if ch == "V" for c in (x, n + x)]
                if cls == "GL" and len(vis) > 3:
                    continue
                hid = [c for c in range(2 * n) if c not in vis]
                hmask = sum(1 << c for c in hid)
                for P in hid:
                    for Y in hid:
                        if P == Y:
                            continue
                        out, hid_, vs, Z = cs.run(n, edges, vis, P, Y, cls)
                        for k in range(1, 5):
                            for Qc in vis:
                                for Xc in vis:
                                    if Qc == Xc:
                                        continue
                                    b = cs.check(out[k], hid_, vs, Z, P, Y, Qc, Xc, cls)
                                    if b not in ("E", "AV"):
                                        continue
                                    tot += 1
                                    T = hidden_rows_free(n, edges, vis, k)
                                    # unconditional iff some pair of hidden outputs carries P+Y and Y using hidden inputs
                                    # only, under free evolution with NO observer operation and arbitrary visible state:
                                    rowsH = [T[o] for o in hid]
                                    hasPY = any((r & hmask) == ((1 << P) | (1 << Y)) and not (r & ~hmask) for r in rowsH)
                                    hasY = any(r == (1 << Y) for r in rowsH)
                                    uncond += hasPY and hasY
print(f"E/AV copy realizations checked: {tot}; kick P' = P + Y produced by free evolution alone "
      f"(no observer operation, visible sector arbitrary): {uncond}")
