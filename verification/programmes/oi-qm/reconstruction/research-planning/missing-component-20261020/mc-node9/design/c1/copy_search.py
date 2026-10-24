"""Check (i) of the owner's recording mechanism: does a short composition of Main.md l.290 update
steps, with observer operations on visible coordinates, realize the copy rule
        X' = X + Q,   P' = P + Y,   Q' = Q,   Y' = Y
(Q, X visible; P, Y hidden) record-safely, i.e. with NOTHING about P or Y learnable from any
visible record at any time (uniform hidden idle inputs eliminated, known visible inputs dropped)?

Same word, operation classes, class quotient and monotone pruning as search3.py (reference,
pure Python).  Outputs may be relabelled: P', Y' at any two distinct hidden coordinates, Q', X'
at any two distinct visible coordinates.  Categories: E exact; AV equal when every visible input other than
the reading Q is 0 (Q must appear in Q' and in X'); AH needs a hidden idle input known.
Causality column: whether P's hidden row (P + Y) depends on any visible input or on the observer
operations at all -- if P and Y sit on hidden sites with no visible neighbour and no path to the
visible sector within k steps, the kick P += Y happens whether or not anything is recorded.
Partitions: strict (Main.md region partition; Q, X any distinct visible coordinates, P, Y any
distinct hidden coordinates) and owner (coordinate-level: pointer site 1 = (Q vis, P hid),
memory site 2 = (X vis, Y hid), the owner's literal form; other sites V/H/split).
"""
import sys, time
from itertools import combinations, product, permutations
from f2 import rowmul, compose, lattice_update, identity
from search2 import all_graphs, basis_key, span_list, ordered_bases, eliminate

KMAX = 4
OB, PC = {}, {}


def vkey(cls, v):
    return basis_key(v) if cls == "GL" else (tuple(sorted(v)) if cls == "cell" else tuple(v))


def vch(cls, key):
    if cls == "GL":
        if key not in OB:
            OB[key] = ordered_bases(key)
        return OB[key]
    if cls == "cell":
        if key not in PC:
            PC[key] = list(set(permutations(key)))
        return PC[key]
    return [key]


def run(n, edges, vis, P, Y, cls):
    N = 2 * n
    M = lattice_update(n, edges)
    vis = sorted(vis)
    hid = [c for c in range(N) if c not in vis]
    D = (1 << P) | (1 << Y)
    Z = sum(1 << c for c in hid) & ~D
    X0 = identity(N)
    L0 = basis_key([X0[c] for c in vis])
    lev = {(tuple(X0[c] for c in hid), vkey(cls, [X0[c] for c in vis]), L0)}
    out = {}
    for k in range(1, KMAX + 1):
        nxt = set()
        for (H, Vk, L) in lev:
            for vr in vch(cls, Vk):
                Yr = [0] * N
                for c, r in zip(hid, H):
                    Yr[c] = r
                for c, r in zip(vis, vr):
                    Yr[c] = r
                Xn = compose(M, Yr)
                Vn = [Xn[c] for c in vis]
                Ln = basis_key(list(L) + Vn)
                if any(f & D for f in eliminate(Ln, Z)):
                    continue          # something about P or Y is learnable: never recovers
                nxt.add((tuple(Xn[c] for c in hid), vkey(cls, Vn), Ln))
        lev = nxt
        out[k] = lev
    return out, hid, vis, Z


def check(lev, hid, vis, Z, P, Y, Qc, Xc, cls):
    """Best category over classes and output relabellings.  Every designated row must match its
    target in the P, Y and Q columns exactly (Q is the reading: it must be copied, not zeroed);
    deviations elsewhere are AV (visible clean inputs, e.g. X = 0) or AH (hidden idle)."""
    tP, tY, tQ, tX = (1 << P) | (1 << Y), 1 << Y, 1 << Qc, (1 << Xc) | (1 << Qc)
    hard = (1 << P) | (1 << Y) | (1 << Qc)
    best = None
    rk = "E AV AH".split()
    for (H, V, L) in lev:
        Hd = dict(zip(hid, H))
        Vrows = [f for f in (span_list(V) if cls == "GL" else list(V)) if f]
        for Po in hid:
            dP = Hd[Po] ^ tP
            if dP & hard:
                continue
            for Yo in hid:
                if Yo == Po:
                    continue
                dY = Hd[Yo] ^ tY
                if dY & hard:
                    continue
                for fQ in Vrows:
                    dQ = fQ ^ tQ
                    if dQ & hard:
                        continue
                    for fX in Vrows:
                        if fX == fQ:
                            continue
                        dX = fX ^ tX
                        if dX & hard:
                            continue
                        a = dP | dY | dQ | dX
                        c = "E" if a == 0 else ("AH" if a & Z else "AV")
                        if best is None or rk.index(c) < rk.index(best):
                            best = c
    return best


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    t0 = time.time()
    for mode in ("strict", "owner"):
        for n in range(2, nmax + 1):
            for cls in ("none", "cell", "GL"):
                tally, ex, ncfg = {}, {}, 0
                for edges in all_graphs(n):
                    if mode == "strict":
                        parts = [cl for cl in product("VH", repeat=n) if "V" in cl and "H" in cl]
                    else:
                        if n < 2:
                            continue
                        parts = [("a", "a") + cl for cl in product("VHab", repeat=n - 2)]
                    for cl in parts:
                        vis = []
                        for x, c in enumerate(cl):
                            vis += {"V": [x, n + x], "H": [], "a": [x], "b": [n + x]}[c]
                        dv = len(vis)
                        if (cls == "GL" and dv > 3) or (cls == "cell" and dv > 6):
                            continue
                        hidc = [c for c in range(2 * n) if c not in vis]
                        if len(vis) < 2 or len(hidc) < 2:
                            continue
                        if mode == "owner":
                            PYs = [(n + 1, n + 2)]           # P = v1, Y = v2 (hidden conjugates)
                            QXs = [(1, 2)]                   # Q = u1, X = u2
                        else:
                            PYs = [(a, b) for a in hidc for b in hidc if a != b]
                            QXs = [(a, b) for a in vis for b in vis if a != b]
                        for (P, Yc) in PYs:
                            ncfg += 1
                            out, hid, vs, Z = run(n, edges, vis, P, Yc, cls)
                            for k in range(1, KMAX + 1):
                                bestk = None
                                for (Qc, Xc) in QXs:
                                    b = check(out[k], hid, vs, Z, P, Yc, Qc, Xc, cls)
                                    if b and (bestk is None or "E AV AH".split().index(b) < "E AV AH".split().index(bestk)):
                                        bestk = b
                                if bestk:
                                    tally[(k, bestk)] = tally.get((k, bestk), 0) + 1
                                    ex.setdefault((k, bestk), (edges, cl, P, Yc))
                print(f"[{mode}] n={n} ops={cls}: (graph, partition, P, Y) cases={ncfg}", flush=True)
                for k in range(1, KMAX + 1):
                    cs = [f"{c}:{tally[(k, c)]}" for c in ("E", "AV", "AH") if (k, c) in tally]
                    print(f"    k={k}: record-safe copy realizations: {', '.join(cs) if cs else 'none'}")
                for (k, c), e in sorted(ex.items()):
                    print(f"      example k={k} {c}: edges={e[0]} sites={''.join(e[1])} P=coord{e[2]} Y=coord{e[3]}")
    print(f"elapsed {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
