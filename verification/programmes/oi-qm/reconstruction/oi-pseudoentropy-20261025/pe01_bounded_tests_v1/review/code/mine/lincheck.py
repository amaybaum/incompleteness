"""Per-observer check of the linear-filter class reduction (independent of the PE-01 sweep)."""
import sys, itertools
sys.path.insert(0, sys.argv[1])
from pe01 import observers as O, generators as G
def apply(cols, v):
    r = 0
    for j, c in enumerate(cols):
        if v >> j & 1: r ^= c
    return r
def tables(cols, b, m, X, Kmax):
    """per K: dict v -> [C0, C1], plus Q counts (2^K * q_K(v))."""
    V = 1 << m
    out = []
    vs = [0] * len(X)
    q = {0: 1}
    for K in range(Kmax + 1):
        C = {}
        for i, rec in enumerate(X):
            C.setdefault(vs[i], [0, 0])[rec[K]] += 1
        out.append((C, dict(q)))
        vs = [apply(cols, v) ^ (b if X[i][K] else 0) for i, v in enumerate(vs)]
        nq = {}
        for v, c in q.items():
            for x in (0, 1):
                w = apply(cols, v) ^ (b if x else 0)
                nq[w] = nq.get(w, 0) + c
        q = nq
    return out
def sig(out, m):
    """K-wise invariants: multiset of (C0, C1, Q) over occupied cells, and set of linear-chi hit counts."""
    V = 1 << m
    res = []
    for C, q in out:
        ms = tuple(sorted((tuple(C.get(v, [0, 0])), q.get(v, 0)) for v in set(C) | set(q)))
        lin = set()
        for c in range(V):
            for e in (0, 1):
                lin.add(sum(C[v][(bin(c & v).count("1") & 1) ^ e] for v in C))
        res.append((ms, frozenset(lin)))
    return res
for fam, n in (("clk", 3), ("filt", 4)):
    g = G.make(fam, n, G.p_n(n))
    X = g.records(14).tolist()
    for m in (1, 2, 3):
        reps = {key: (cols, b) for key, cols, b in O.linear_classes(m)}
        repsig = {key: sig(tables(cols, b, m, X, 14), m) for key, (cols, b) in reps.items()}
        bad = 0; tot = 0
        for cols in O.gl_matrices(m):
            for b in range(1 << m):
                r, gpoly = O.krylov_class(cols, b, m) if b else (0, 1)
                key = "r0" if b == 0 else "g=%s" % __import__("pe01.gf2", fromlist=["x"]).poly_str(gpoly)
                tot += 1
                if sig(tables(cols, b, m, X, 14), m) != repsig[key]:
                    bad += 1
        print(fam, n, "m=%d" % m, "observers", tot, "mismatching their class representative:", bad, "classes", len(reps))
