"""Detail of the copy-rule realizations: for every (configuration, k) with a record-safe E/AV
realization (strict partition; n = 3 all classes, n = 4 ops = none), whether the P/Y hidden sites
lie in a connected component that contains any visible site."""
from itertools import product
import copy_search as cs
def comp(n, edges, x):
    adj = {i: set() for i in range(n)}
    for a, b in edges: adj[a].add(b); adj[b].add(a)
    seen, st = {x}, [x]
    while st:
        y = st.pop()
        for z in adj[y]:
            if z not in seen: seen.add(z); st.append(z)
    return seen
rows = []
for (n, classes) in ((3, ("none", "cell", "GL")), (4, ("none",))):
    for cls in classes:
        for edges in cs.all_graphs(n):
            for cl in product("VH", repeat=n):
                if "V" not in cl or "H" not in cl: continue
                vis = [c for x, ch in enumerate(cl) if ch == "V" for c in (x, n + x)]
                if cls == "GL" and len(vis) > 3: continue
                hid = [c for c in range(2 * n) if c not in vis]
                for P in hid:
                    for Y in hid:
                        if P == Y: continue
                        out, hid_, vs, Z = cs.run(n, edges, vis, P, Y, cls)
                        for k in range(1, 5):
                            hit = any(cs.check(out[k], hid_, vs, Z, P, Y, Qc, Xc, cls) in ("E", "AV")
                                      for Qc in vis for Xc in vis if Qc != Xc)
                            if not hit: continue
                            touch = any(cl[z] == "V" for z in comp(n, edges, P % n) | comp(n, edges, Y % n))
                            rows.append((n, cls, k, edges, "".join(cl), P, Y, touch))
touching = [r for r in rows if r[7]]
print(f"(config, k) cases with an E/AV copy realization: {len(rows)}; P/Y sites connected to any visible site: {len(touching)}")
for r in touching:
    print("  ", r)
