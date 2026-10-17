"""EXPLORATORY (not a recorded result). Are P0's subsystem-locality exclusions at |A| >= 2 invariant
under re-identification of the declared decomposition?

P0 (#834, p0-subsystem-locality/RESULT.md) declares V = V1 x V2 and A = A1 x A2 and finds that
Lcc and We.X (CCT4) are SEP-PHYS on O1, WW.Ke is SEP-REP on O1 and SEP-PHYS on O2/O3, and Ucv (CCC)
is EXCLUDES-ALL.  Here every set-level identification of V = Fin4 and of A = Fin4 with Fin2 x Fin2
(3 classes each; on A the anchor is kept at (0,0)) is swept, and each verdict is recomputed in the
new coordinates.  All entries are rational; arithmetic is exact (Fraction).  Standard library only.

Conventions are those of p0_exact.py: composite index (i1*d2+i2)*n + a1*n2 + a2, anchor index 0,
factor carrier index i*n_k + a."""
import itertools as it
from fractions import Fraction as Fr

ZERO, ONE = Fr(0), Fr(1)
OUT, FAIL = [], []


def say(*a):
    OUT.append(" ".join(str(x) for x in a))


def check(name, ok, detail=""):
    say(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)
    return ok


def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m) if A[i][k]), ZERO) for j in range(p)] for i in range(n)]


def dag(A):                                   # real entries: transpose
    return [list(r) for r in zip(*A)]


def perm_matrix(f, n):
    M = [[ZERO] * n for _ in range(n)]
    for j in range(n):
        M[f(j)][j] = ONE
    return M


def key(M):
    return tuple(tuple(r) for r in M)


def rank_le1(T):
    p = next(((r, c) for r, row in enumerate(T) for c, x in enumerate(row) if x), None)
    if p is None:
        return True
    pr, pc = p
    for r, row in enumerate(T):
        for c, x in enumerate(row):
            if T[pr][pc] * x != row[pc] * T[pr][c]:
                return False
    return True


class Conf:
    def __init__(self, name, d1, n1, d2, n2, gamma):
        self.name, self.d1, self.n1, self.d2, self.n2 = name, d1, n1, d2, n2
        self.d, self.n = d1 * d2, n1 * n2
        self.D = self.d * self.n
        self.gamma = gamma

    def cidx(self, i1, i2, a1, a2):
        return (i1 * self.d2 + i2) * self.n + a1 * self.n2 + a2

    def split_v(self, i):
        return divmod(i, self.d2)

    def prod(self, U1, U2):
        s = self
        M = [[ZERO] * s.D for _ in range(s.D)]
        rows = list(it.product(range(s.d1), range(s.n1), range(s.d2), range(s.n2)))
        for (i1, a1, i2, a2) in rows:
            for (j1, b1, j2, b2) in rows:
                x = U1[i1 * s.n1 + a1][j1 * s.n1 + b1]
                y = U2[i2 * s.n2 + a2][j2 * s.n2 + b2]
                if x and y:
                    M[s.cidx(i1, i2, a1, a2)][s.cidx(j1, j2, b1, b2)] = x * y
        return M

    def cut_operator(self, M):
        s = self
        N1, N2 = s.d1 * s.n1, s.d2 * s.n2
        T = [[ZERO] * (N2 * N2) for _ in range(N1 * N1)]
        idx = list(it.product(range(s.d1), range(s.n1), range(s.d2), range(s.n2)))
        for (i1, a1, i2, a2) in idx:
            for (j1, b1, j2, b2) in idx:
                x1, y1 = i1 * s.n1 + a1, j1 * s.n1 + b1
                x2, y2 = i2 * s.n2 + a2, j2 * s.n2 + b2
                T[x1 * N1 + y1][x2 * N2 + y2] = M[s.cidx(i1, i2, a1, a2)][s.cidx(j1, j2, b1, b2)]
        return T

    def readback(self, M):
        s = self
        return [[sum((M[i * s.n + a][j * s.n] ** 2 for a in range(s.n)), ZERO) for j in range(s.d)]
                for i in range(s.d)]

    def choi(self, M):
        s = self
        C = {}
        for i, ip, j, k in it.product(range(s.d), repeat=4):
            C[(i, ip, j, k)] = sum((M[i * s.n + a][j * s.n] * M[ip * s.n + a][k * s.n] for a in range(s.n)), ZERO)
        return C

    def choi_by_dilation(self, M):
        s = self
        C = {}
        Md = dag(M)
        for j in range(s.d):
            for k in range(s.d):
                E = [[ZERO] * s.D for _ in range(s.D)]
                E[j * s.n][k * s.n] = ONE
                out = matmul(matmul(M, E), Md)
                for i in range(s.d):
                    for ip in range(s.d):
                        C[(i, ip, j, k)] = sum((out[i * s.n + a][ip * s.n + a] for a in range(s.n)), ZERO)
        return C

    def cut_choi(self, C):
        s = self
        d1, d2 = s.d1, s.d2
        T = [[ZERO] * (d2 ** 4) for _ in range(d1 ** 4)]
        for (i, ip, j, k), v in C.items():
            i1, i2 = s.split_v(i)
            ip1, ip2 = s.split_v(ip)
            j1, j2 = s.split_v(j)
            k1, k2 = s.split_v(k)
            T[((i1 * d1 + ip1) * d1 + j1) * d1 + k1][((i2 * d2 + ip2) * d2 + j2) * d2 + k2] = v
        return T

    def cut_stoch(self, R):
        s = self
        T = [[ZERO] * (s.d2 ** 2) for _ in range(s.d1 ** 2)]
        for i in range(s.d):
            for j in range(s.d):
                i1, i2 = s.split_v(i)
                j1, j2 = s.split_v(j)
                T[i1 * s.d1 + j1][i2 * s.d2 + j2] = R[i][j]
        return T


def rot(s):
    return [[Fr(3, 5), Fr(-4 * s, 5)], [Fr(4 * s, 5), Fr(3, 5)]]


# ------------------------------------------------------------------ P0's configurations and lifts (ported)
CCT4 = Conf("CCT4", 2, 2, 2, 2, eye(4))
CCC = Conf("CCC", 2, 2, 2, 2, [[Fr(9, 25) if i == j else (Fr(16, 25) if i == 3 - j else ZERO)
                                for j in range(4)] for i in range(4)])
CENT = Conf("CENT", 2, 1, 2, 1, perm_matrix(lambda j: {2: 3, 3: 2}.get(j, j), 4))
X = perm_matrix(lambda k: {1: 3, 3: 1}.get(k, k), 4)
W = perm_matrix(lambda k: {0: 1, 1: 0}.get(k, k), 4)
I4, I16 = eye(4), eye(16)
c = CCT4
XX, W1, WW, X1 = c.prod(X, X), c.prod(W, I4), c.prod(W, W), c.prod(X, I4)


def comp_perm(conf, f):
    M = [[ZERO] * conf.D for _ in range(conf.D)]
    for (i1, i2, a1, a2) in it.product(range(conf.d1), range(conf.d2), range(conf.n1), range(conf.n2)):
        M[conf.cidx(*f(i1, i2, a1, a2))][conf.cidx(i1, i2, a1, a2)] = ONE
    return M


We = comp_perm(c, lambda i1, i2, a1, a2: (i1, i2, 1 - a1, 1 - a2) if (i1, i2) == (0, 0) and a1 == a2
               else (i1, i2, a1, a2))
Ke = comp_perm(c, lambda i1, i2, a1, a2: {(0, 0, 1, 1): (1, 1, 1, 1), (1, 1, 1, 1): (0, 0, 1, 1)}
               .get((i1, i2, a1, a2), (i1, i2, a1, a2)))
Lcc = [[ZERO] * 16 for _ in range(16)]
for i1, i2 in it.product(range(2), repeat=2):
    R = rot((-1) ** (i1 + i2))
    base = (i1 * 2 + i2) * 4
    for (x, ax), (y, ay) in it.product(((0, 0), (1, 3)), repeat=2):
        Lcc[base + ax][base + ay] = R[x][y]
    for a in (1, 2):
        Lcc[base + a][base + a] = ONE
Lf = [[ZERO] * 4 for _ in range(4)]
for i in range(2):
    R = rot((-1) ** i)
    for x, y in it.product(range(2), repeat=2):
        Lf[2 * i + x][2 * i + y] = R[x][y]
Llp = c.prod(Lf, Lf)
LCT4 = {
    "I": (I16, I16), "X": (I16, XX), "W1.X": (W1, matmul(W1, XX)), "We.X": (We, matmul(We, XX)),
    "Lcc": (Lcc, Lcc), "Llp": (Llp, Llp), "WW": (WW, WW), "WW.Ke": (WW, matmul(WW, Ke)),
    "WW.X1": (WW, matmul(WW, X1)),
}
DECLARED = {"I": True, "X": True, "W1.X": True, "We.X": False, "Lcc": False, "Llp": True, "WW": True,
            "WW.Ke": False, "WW.X1": True}
Ucv = [[ZERO] * 16 for _ in range(16)]
for i1, i2 in it.product(range(2), repeat=2):
    a, b = CCC.cidx(i1, i2, 0, 0), CCC.cidx(1 - i1, 1 - i2, 1, 1)
    Ucv[a][a], Ucv[b][a], Ucv[a][b], Ucv[b][b] = Fr(3, 5), Fr(4, 5), Fr(-4, 5), Fr(3, 5)
    for a1, a2 in ((0, 1), (1, 0)):
        k = CCC.cidx(i1, i2, a1, a2)
        Ucv[k][k] = ONE
CN = perm_matrix(lambda j: {2: 3, 3: 2}.get(j, j), 4)

# hand-built product lifts, used only as candidate admitted lifts in any decomposition
R1 = [[ZERO] * 4 for _ in range(4)]          # factor carrier (i, a), index 2 i + a
for (u, v) in ((0, 3), (2, 1)):               # pairs {(0,0),(1,1)} and {(1,0),(0,1)}
    R1[u][u], R1[v][u], R1[u][v], R1[v][v] = Fr(3, 5), Fr(4, 5), Fr(-4, 5), Fr(3, 5)
EXTRA = {"1(x)Lf": c.prod(I4, Lf), "Lf(x)1": c.prod(Lf, I4), "R1(x)1": c.prod(R1, I4), "1(x)R1": c.prod(I4, R1)}

# ------------------------------------------------------------------ controls on the port
is_unit = lambda U: key(matmul(dag(U), U)) == key(eye(len(U)))
check("K-unit every ported and hand-built operator is exactly unitary",
      all(is_unit(U) for L in LCT4.values() for U in L) and is_unit(Ucv) and is_unit(CN)
      and all(is_unit(U) for U in EXTRA.values()) and is_unit(R1))
check("K-indep O1 by the defining sum equals O1 by dilation (CCT4 lifts, Ucv)",
      all(CCT4.choi(U) == CCT4.choi_by_dilation(U) for L in LCT4.values() for U in L)
      and CCC.choi(Ucv) == CCC.choi_by_dilation(Ucv))


# ------------------------------------------------------------------ identifications
def classes(fix0):
    """one representative bijection Fin4 -> Fin4 per 2x2 decomposition class (optionally fixing 0)"""
    seen, reps = set(), []
    for p in it.permutations(range(4)):
        if fix0 and p[0] != 0:
            continue
        inv_ = {p[i]: i for i in range(4)}     # new index -> old index
        rows = frozenset(frozenset(inv_[k] for k in blk) for blk in ((0, 1), (2, 3)))
        cols = frozenset(frozenset(inv_[k] for k in blk) for blk in ((0, 2), (1, 3)))
        cls = frozenset((rows, cols))
        if cls not in seen:
            seen.add(cls)
            reps.append(p)
    return reps


VREPS, AREPS = classes(False), classes(True)
check("K-classes 3 decomposition classes of V and 3 of A (anchor fixed)", len(VREPS) == 3 and len(AREPS) == 3)


def relabel(conf, U, sv, sa):
    n = conf.n
    P = [[ZERO] * conf.D for _ in range(conf.D)]
    for i in range(conf.d):
        for a in range(n):
            P[sv[i] * n + sa[a]][i * n + a] = ONE
    return matmul(matmul(P, U), dag(P))


def relabel_gamma(G, sv):
    P = perm_matrix(lambda j: sv[j], len(G))
    return matmul(matmul(P, G), dag(P))


def carriers(conf, L):
    U0, U1 = L
    r10, r01 = matmul(U1, dag(U0)), matmul(U0, dag(U1))
    return {1: [conf.choi(U0), conf.choi(U1)], 2: [conf.readback(r10), conf.readback(r01)],
            3: [conf.choi(r10), conf.choi(r01)]}


def is_prod_value(conf, x, v):
    return rank_le1(conf.cut_stoch(v) if x == 2 else conf.cut_choi(v))


def vk(x, v):
    return key(v) if x == 2 else tuple(sorted(v.items()))


def sweep(conf, lifts, extra, sv, sa):
    new = {n: tuple(relabel(conf, U, sv, sa) for U in L) for n, L in lifts.items()}
    G = relabel_gamma(conf.gamma, sv)
    gprod = rank_le1(conf.cut_stoch(G))
    status = {n: all(rank_le1(conf.cut_operator(U)) for U in L) for n, L in new.items()}
    # admissibility in the new coordinates: readback equals the relabelled Gamma
    adm = all(key(conf.readback(U)) == key(G) for L in new.values() for U in L)
    cands = {n: new[n] for n in new if status[n]}
    for n, U in extra.items():
        if all(rank_le1(conf.cut_operator(V)) for V in (U,)) and key(conf.readback(U)) == key(G):
            cands[n] = (U, U)
    cv = {n: carriers(conf, L) for n, L in list(new.items())}
    candv = {n: carriers(conf, L) for n, L in cands.items()}
    verd = {}
    for n in new:
        for x in (1, 2, 3):
            if status[n]:
                verd[(n, x)] = "ADMITTED"
                continue
            vals = cv[n][x]
            if not all(is_prod_value(conf, x, v) for v in vals):
                verd[(n, x)] = "SEP-PHYS"
                continue
            rep = [m for m in candv if all(vk(x, candv[m][x][k]) == vk(x, vals[k]) for k in range(2))]
            verd[(n, x)] = ("SEP-REP by " + ",".join(rep)) if rep else "SEP-OPEN"
    return gprod, status, adm, verd


# ------------------------------------------------------------------ CCT4
say("== CCT4: every V-class x A-class")
RES = {}
for sv in VREPS:
    for sa in AREPS:
        gprod, status, adm, verd = sweep(CCT4, LCT4, EXTRA, sv, sa)
        RES[(sv, sa)] = (gprod, status, verd)
        check(f"K-adm CCT4 sv={sv} sa={sa}: every relabelled lift is admissible for the relabelled Gamma", adm)
        say(f"sv={sv} sa={sa} Gamma product={gprod}; " +
            "; ".join(f"{n}: " + "/".join(verd[(n, x)].split(' ')[0] for x in (1, 2, 3))
                      for n in LCT4 if not DECLARED[n] or not status[n]))
ID = ((0, 1, 2, 3), (0, 1, 2, 3))
g0, st0, v0 = RES[ID]
check("K-repro at the declared decomposition, computed SL-U status equals P0's table",
      all(st0[n] == DECLARED[n] for n in LCT4))
check("K-repro at the declared decomposition, Lcc O1 SEP-PHYS, We.X SEP-PHYS on O1-O3, WW.Ke O1 SEP-REP and O2,O3 SEP-PHYS",
      v0[("Lcc", 1)] == "SEP-PHYS" and all(v0[("We.X", x)] == "SEP-PHYS" for x in (1, 2, 3))
      and v0[("WW.Ke", 1)].startswith("SEP-REP") and v0[("WW.Ke", 2)] == "SEP-PHYS" and v0[("WW.Ke", 3)] == "SEP-PHYS")

for n in ("Lcc", "We.X", "WW.Ke"):
    for x in (1, 2, 3):
        phys = [(sv, sa) for (sv, sa), (g, s, v) in RES.items() if g and v[(n, x)] == "SEP-PHYS"]
        rep = [(sv, sa) for (sv, sa), (g, s, v) in RES.items() if g and (v[(n, x)].startswith("SEP-REP") or v[(n, x)] == "ADMITTED")]
        say(f"{n} O{x}: SEP-PHYS in {len(phys)}/9 decompositions, rep-or-admitted in {len(rep)}/9")

# ------------------------------------------------------------------ CCC
say("== CCC: every V-class x A-class")
for sv in VREPS:
    for sa in AREPS:
        gprod, status, adm, verd = sweep(CCC, {"Ucv": (Ucv, Ucv)}, EXTRA, sv, sa)
        check(f"K-adm CCC sv={sv} sa={sa}", adm)
        say(f"sv={sv} sa={sa} Gamma product={gprod}; Ucv SL-U={status['Ucv']}; " +
            "/".join(verd[("Ucv", x)] for x in (1, 2, 3)))
        RES[("CCC", sv, sa)] = (gprod, status, verd)
check("K-repro CCC at the declared decomposition: Gamma is not a product (EXCLUDES-ALL)",
      not RES[("CCC",) + ID][0])
ucv_prod = [(sv, sa) for (tag, sv, sa) in [k for k in RES if k[0] == "CCC"] if RES[("CCC", sv, sa)][0]]
say(f"CCC: Gamma is a product in {len(ucv_prod)}/9 decompositions")

# ------------------------------------------------------------------ countercontrol: CENT, the CNOT law
say("== CENT (countercontrol): every V-class")
cent = []
for sv in VREPS:
    G = relabel_gamma(CENT.gamma, sv)
    cent.append(rank_le1(CENT.cut_stoch(G)))
check("K-robust-neg CENT's CNOT law is a non-product under every identification of V "
      "(so the sweep can return an invariant exclusion)", not any(cent), str(cent))

say("== summary")
say("failures:", len(FAIL))
lcc_rel = any(g and v[("Lcc", 1)] != "SEP-PHYS" for k, (g, s, v) in RES.items() if k[0] != "CCC")
ucv_rel = len(ucv_prod) > 0
say("EXPLORATORY-VERDICT", "VOID" if FAIL else
    ("DECOMPOSITION-RELATIVE" if (lcc_rel or ucv_rel) else "DECOMPOSITION-INVARIANT-HERE"))
print("\n".join(OUT))
