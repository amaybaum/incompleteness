"""Independent brute-force check of the ops = none, relabelled-output results (no quotient, no
pruning, no learnable-subspace algebra).  For each graph, partition and k <= 4 it forms M^k and
the record sequence explicitly and decides record-safety from exact distributions:
  for every (h, P), D(h, P) = law of the full visible record sequence (times 1..k) over uniform
  hidden idle inputs, with every visible input 0.  R_u-safe iff D(h,P) depends on (h,P) only
  through w(h) = omega(u,h), and D for w = 0 and w = 1 have disjoint supports.
Designated rows: compared with the target on the declared inputs (visible inputs 0), i.e. as
AV; a deviation in a hidden idle coordinate is reported as AH.  Prints the same tallies as
search5.py (strict and relaxed; best category per configuration, k and read functional)."""
import sys
from fractions import Fraction
from itertools import combinations, product
from f2 import lattice_update, compose, apply, identity

def graphs(n):
    pairs = list(combinations(range(n), 2))
    for m in range(1 << len(pairs)):
        yield tuple(p for i, p in enumerate(pairs) if m >> i & 1)

def cfgs(n, mode):
    if mode == "relaxed":
        for po in "AB":
            Qc, Pc = (1, n + 1) if po == "A" else (n + 1, 1)
            for cl in product("VHab", repeat=n - 2):
                vis = [Qc]
                for x, c in zip(range(2, n), cl):
                    vis += {"V": [x, n + x], "H": [], "a": [x], "b": [n + x]}[c]
                yield vis, Qc, Pc, cl
    elif n >= 3:
        for Qc in (1, n + 1):
            for Pc in (2, n + 2):
                for cl in product("VH", repeat=n - 3):
                    vis = [1, n + 1]
                    for x, c in zip(range(3, n), cl):
                        if c == "V":
                            vis += [x, n + x]
                    yield vis, Qc, Pc, cl

def canon(n, edges, cl, fixed):
    from itertools import permutations
    others = [x for x in range(n) if x not in fixed]
    best = None
    for perm in permutations(others):
        mp = {x: x for x in fixed}
        mp.update(dict(zip(others, perm)))
        e2 = tuple(sorted(tuple(sorted((mp[a], mp[b]))) for a, b in edges))
        c2 = {mp[x]: cl[i] for i, x in enumerate(others)}
        key = (e2, tuple(c2[x] for x in others))
        best = key if best is None or key < best else best
    return best

def outs(n, vis, mode):
    vs = set(vis)
    hs = [x for x in range(n) if x not in vs and n + x not in vs]
    sp = [x for x in range(n) if (x in vs) != (n + x in vs)]
    for a in hs:
        for qo, po in ((a, n + a), (n + a, a)):
            if mode == "relaxed":
                for b in sp:
                    if b != a:
                        yield qo, po, (b if b in vs else n + b), (n + b if b in vs else b)
            else:
                for Qo in vis:
                    for c in hs:
                        if c != a:
                            for Po in (c, n + c):
                                yield qo, po, Qo, Po

RK = {"E": 0, "AV": 1, "AH": 2}
nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 4
for mode in ("strict", "relaxed"):
    for n in range(2, nmax + 1):
        N = 2 * n
        tally = {}
        for edges in graphs(n):
            M = lattice_update(n, edges)
            for vis, Qc, Pc, cl in cfgs(n, mode):
                fixed = [0, 1] if mode == "relaxed" else [0, 1, 2]
                if canon(n, edges, cl, fixed) != (tuple(sorted(edges)), tuple(cl)):
                    continue
                vmask = sum(1 << c for c in vis)
                hid = [c for c in range(N) if not vmask >> c & 1]
                idle = [c for c in hid if c not in (0, n, Pc)]
                powers = [identity(N)]
                for k in range(1, 5):
                    powers.append(compose(M, powers[-1]))
                for k in range(1, 5):
                    T = powers[k]
                    # record distributions
                    D = {}
                    for hq, hp, P in product((0, 1), repeat=3):
                        dist = {}
                        for z in product((0, 1), repeat=len(idle)):
                            s = (hq << 0) | (hp << n) | (P << Pc)
                            for c, b in zip(idle, z):
                                s |= b << c
                            rec = tuple(apply(powers[t], s) & vmask for t in range(1, k + 1))
                            dist[rec] = dist.get(rec, Fraction(0)) + Fraction(1, 1 << len(idle))
                        D[(hq, hp, P)] = dist
                    best = {}
                    for (wq, wp, fn) in ((1, 0, "u_toy"), (0, 1, "v_toy"), (1, 1, "u_toy+v_toy")):
                        w = lambda hq, hp: (wq * hq + wp * hp) & 1
                        groups = {0: [], 1: []}
                        for (hq, hp, P), d in D.items():
                            groups[w(hq, hp)].append(d)
                        safe = all(g == grp[0] for grp in groups.values() for g in grp)
                        safe &= not (set(groups[0][0]) & set(groups[1][0]))
                        if not safe:
                            continue
                        # target rows (input coords) for both toy orientations giving this functional
                        for (q, p) in ((0, n), (n, 0)):
                            # omega(u,h) = uq*p + up*q equals w  ->  uq, up
                            uq = wq if p == 0 else wp
                            up = wp if p == 0 else wq
                            # check: w = up*q + uq*p with q,p coordinates
                            tQ = (1 << Qc) | (up << q) | (uq << p)
                            tq = (1 << q) | (uq << Pc)
                            tp = (1 << p) | (up << Pc)
                            tP = 1 << Pc
                            for qo, po, Qo, Po in outs(n, vis, mode):
                                dev = 0
                                bad = False
                                for o, t in ((qo, tq), (po, tp), (Po, tP), (Qo, tQ)):
                                    d = T[o] ^ t
                                    if d & ((1 << 0) | (1 << n) | (1 << Pc)):
                                        bad = True
                                        break
                                    dev |= d
                                if bad:
                                    continue
                                cat = "E" if dev == 0 else ("AH" if any(dev >> c & 1 for c in idle) else "AV")
                                if fn not in best or RK[cat] < RK[best[fn]]:
                                    best[fn] = cat
                    for fn, cat in best.items():
                        tally[(k, cat, fn)] = tally.get((k, cat, fn), 0) + 1
        print(f"[brute, {mode}] n={n} ops=none")
        for k in range(1, 5):
            cs = [f"{c} read {f}:{v}" for (kk, c, f), v in sorted(tally.items()) if kk == k]
            print(f"    k={k}: {', '.join(cs) if cs else 'none'}")
