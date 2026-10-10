import sys, itertools
from collections import Counter
src = open('bridge_probe.py').read()
src = src[:src.index("# ---- integer lattices")]
exec(src)
def gdiv(x, y): n = y.norm2(); c = x * y.conj(); return G(c.a / n, c.b / n)
def transpose(H): return [list(c) for c in zip(*H)]
for name in ('O1(v1,v2,v3)', 'F1+(1,v2,v3)', 'O5(v5,v6,v4)'):
    H = H3(PTS[name])
    for orient, M in (('rows', H), ('cols', transpose(H))):
        for m, n in ((4, 4), (8, 2), (2, 8)):
            deg = Counter()
            for r, r2 in itertools.combinations(range(16), 2):
                lv = Counter(gdiv(M[r][c], M[r2][c]).key() for c in range(16))
                if min(lv.values()) >= n: deg[r] += 1; deg[r2] += 1
            print(name, orient, (m, n), sorted(deg.values()))

def level_key(M, r, r2): return tuple(gdiv(M[r][c], M[r2][c]).key() for c in range(16))
def class_partitions(M, m, n):
    lk = {}
    adj = {r: set() for r in range(16)}
    for r, r2 in itertools.combinations(range(16), 2):
        k = level_key(M, r, r2)
        if min(Counter(k).values()) >= n: adj[r].add(r2); adj[r2].add(r); lk[(r, r2)] = k
    out = []
    def rec(unassigned, classes):
        if not unassigned: out.append(list(classes)); return
        r = min(unassigned)
        cand = sorted(adj[r] & unassigned)
        for rest in itertools.combinations(cand, m - 1):
            if all(b in adj[a] for a, b in itertools.combinations(rest, 2)):
                rec(unassigned - {r, *rest}, classes + [(r,) + rest])
    rec(set(range(16)), [])
    passing = []
    for P in out:
        keys = [lk[tuple(sorted(pr))] for cl in P for pr in itertools.combinations(cl, 2)]
        meet = Counter(tuple(k[c] for k in keys) for c in range(16))
        if all(v % n == 0 for v in meet.values()): passing.append(P)
    return len(out), len(passing)
for name in ('O1(v1,v2,v3)', 'F1+(1,v2,v3)', 'O5(v5,v6,v4)', 'O2 absent face (v1,-1,v3)', 'F2(v1,1,v3)'):
    H = H3(PTS[name])
    res = []
    for orient, M in (('rows', H), ('cols', transpose(H))):
        for m, n in ((4, 4), (8, 2), (2, 8)):
            res.append((orient, (m, n), class_partitions(M, m, n)))
    print(name, res)
