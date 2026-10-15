"""P0 subsystem locality: the exact runs fixed by RULES.md.

Every decisive quantity is an element of Q(zeta_16), held exactly as integer coefficients over a
positive integer denominator. No floating point is used. Run with `python3 -I p0_exact.py`.
"""
import itertools as it
from math import gcd

# ---------------------------------------------------------------- exact arithmetic in Q(zeta_16)


class C16:
    """(sum_k c[k] zeta^k) / d with zeta^8 = -1, normalized."""
    __slots__ = ("c", "d")

    def __init__(self, c, d=1):
        if d < 0:
            c, d = tuple(-x for x in c), -d
        g = gcd(d, *c)
        if g > 1:
            c, d = tuple(x // g for x in c), d // g
        if not any(c):
            d = 1
        self.c, self.d = tuple(c), d

    def __add__(s, o):
        return C16(tuple(a * o.d + b * s.d for a, b in zip(s.c, o.c)), s.d * o.d)

    def __sub__(s, o):
        return C16(tuple(a * o.d - b * s.d for a, b in zip(s.c, o.c)), s.d * o.d)

    def __neg__(s):
        return C16(tuple(-a for a in s.c), s.d)

    def __mul__(s, o):
        a, b = s.c, o.c
        if not any(a) or not any(b):
            return ZERO
        r = [0] * 16
        for i in range(8):
            ai = a[i]
            if ai:
                for j in range(8):
                    if b[j]:
                        r[i + j] += ai * b[j]
        return C16(tuple(r[k] - r[k + 8] for k in range(8)), s.d * o.d)

    def conj(s):
        c = s.c
        return C16((c[0], -c[7], -c[6], -c[5], -c[4], -c[3], -c[2], -c[1]), s.d)

    def __eq__(s, o):
        return s.c == o.c and s.d == o.d

    def __hash__(s):
        return hash((s.c, s.d))

    def iszero(s):
        return not any(s.c)

    def __repr__(s):
        terms = []
        for k, x in enumerate(s.c):
            if x:
                terms.append(f"{x}" + ("" if k == 0 else f"z^{k}"))
        num = "+".join(terms) if terms else "0"
        return num if s.d == 1 else f"({num})/{s.d}"


ZERO = C16((0,) * 8)
ONE = C16((1,) + (0,) * 7)


def q(p, r=1):
    return C16((p,) + (0,) * 7, r)


def zeta(k):
    k %= 16
    c = [0] * 8
    if k < 8:
        c[k] = 1
    else:
        c[k - 8] = -1
    return C16(tuple(c))


I_ = zeta(4)


def csum(xs):
    r = ZERO
    for x in xs:
        r = r + x
    return r


# ---------------------------------------------------------------- matrices (lists of lists)

def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    R = [[ZERO] * p for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ri = R[i]
        for k in range(m):
            a = Ai[k]
            if a.iszero():
                continue
            Bk = B[k]
            for j in range(p):
                b = Bk[j]
                if not b.iszero():
                    Ri[j] = Ri[j] + a * b
    return R


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def meq(A, B):
    return all(a == b for ra, rb in zip(A, B) for a, b in zip(ra, rb))


def is_unitary(U):
    return meq(matmul(dag(U), U), eye(len(U)))


def perm_matrix(f, n):
    """Column i maps to row f(i)."""
    M = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        M[f(i)][i] = ONE
    return M


def diag(v):
    n = len(v)
    return [[v[i] if i == j else ZERO for j in range(n)] for i in range(n)]


def key(M):
    return tuple(tuple(r) for r in M)


# ---------------------------------------------------------------- configurations

class Conf:
    def __init__(self, name, d1, n1, d2, n2, gamma):
        self.name, self.d1, self.n1, self.d2, self.n2 = name, d1, n1, d2, n2
        self.d, self.n = d1 * d2, n1 * n2
        self.D = self.d * self.n
        self.gamma = gamma           # d x d matrix of C16

    def cidx(self, i1, i2, a1, a2):
        return (i1 * self.d2 + i2) * self.n + a1 * self.n2 + a2

    def split_v(self, i):
        return divmod(i, self.d2)

    def prod(self, U1, U2):
        s = self
        M = [[ZERO] * s.D for _ in range(s.D)]
        rows = list(it.product(range(s.d1), range(s.n1), range(s.d2), range(s.n2)))
        for (i1, a1, i2, a2) in rows:
            r = s.cidx(i1, i2, a1, a2)
            for (j1, b1, j2, b2) in rows:
                x = U1[i1 * s.n1 + a1][j1 * s.n1 + b1]
                if x.iszero():
                    continue
                y = U2[i2 * s.n2 + a2][j2 * s.n2 + b2]
                if not y.iszero():
                    M[r][s.cidx(j1, j2, b1, b2)] = x * y
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
        R = [[ZERO] * s.d for _ in range(s.d)]
        for i in range(s.d):
            for j in range(s.d):
                R[i][j] = csum(M[i * s.n + a][j * s.n] * M[i * s.n + a][j * s.n].conj()
                               for a in range(s.n))
        return R

    def choi(self, M):
        """C[i][ip][j][k] = sum_a M[(i,a),(j,a0)] conj M[(ip,a),(k,a0)]; a0 = (0,0) has index 0."""
        s = self
        cols = [[M[i * s.n + a][j * s.n] for j in range(s.d)] for i in range(s.d) for a in range(s.n)]
        ccols = [[x.conj() for x in row] for row in cols]
        C = [[[[ZERO] * s.d for _ in range(s.d)] for _ in range(s.d)] for _ in range(s.d)]
        for i in range(s.d):
            for ip in range(s.d):
                for a in range(s.n):
                    r, rp = cols[i * s.n + a], ccols[ip * s.n + a]
                    for j in range(s.d):
                        x = r[j]
                        if x.iszero():
                            continue
                        Cj = C[i][ip][j]
                        for k in range(s.d):
                            y = rp[k]
                            if not y.iszero():
                                Cj[k] = Cj[k] + x * y
        return C

    def choi_by_dilation(self, M):
        """Independent route: M (E_jk (x) |a0><a0|) M^dag, then the partial trace over A."""
        s = self
        C = [[[[ZERO] * s.d for _ in range(s.d)] for _ in range(s.d)] for _ in range(s.d)]
        Md = dag(M)
        for j in range(s.d):
            for k in range(s.d):
                E = [[ZERO] * s.D for _ in range(s.D)]
                E[j * s.n][k * s.n] = ONE
                out = matmul(matmul(M, E), Md)
                for i in range(s.d):
                    for ip in range(s.d):
                        C[i][ip][j][k] = csum(out[i * s.n + a][ip * s.n + a] for a in range(s.n))
        return C

    def cut_choi(self, C):
        s = self
        d1, d2 = s.d1, s.d2
        T = [[ZERO] * (d2 ** 4) for _ in range(d1 ** 4)]
        for i, ip, j, k in it.product(range(s.d), repeat=4):
            i1, i2 = s.split_v(i)
            ip1, ip2 = s.split_v(ip)
            j1, j2 = s.split_v(j)
            k1, k2 = s.split_v(k)
            T[((i1 * d1 + ip1) * d1 + j1) * d1 + k1][((i2 * d2 + ip2) * d2 + j2) * d2 + k2] = C[i][ip][j][k]
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

    def gram(self, M):
        s = self
        G = []
        for i in range(s.d):
            X = [[M[i * s.n + a][j * s.n] for j in range(s.d)] for a in range(s.n)]
            G.append([[csum(X[a][j].conj() * X[a][k] for a in range(s.n)) for k in range(s.d)]
                      for j in range(s.d)])
        return G


def rank_ge2(T):
    """None if rank <= 1 (exact), else a certificate (p, q, r, c) with a nonzero 2x2 minor."""
    p = q_ = None
    for r, row in enumerate(T):
        for c, x in enumerate(row):
            if not x.iszero():
                p, q_ = r, c
                break
        if p is not None:
            break
    if p is None:
        return None
    Tp, tpq = T[p], T[p][q_]
    for r, row in enumerate(T):
        trq = row[q_]
        for c, x in enumerate(row):
            if not (tpq * x == trq * Tp[c]):
                return (p, q_, r, c)
    return None


# ---------------------------------------------------------------- witness matrices

def H(z):
    h = q(1, 2)
    rows = [[ONE, ONE, ONE, ONE], [ONE, z, -ONE, -z], [ONE, -ONE, ONE, -ONE], [ONE, -z, -ONE, z]]
    return [[h * x for x in r] for r in rows]


H1, Hi = H(ONE), H(I_)
F16 = [[zeta(n * m) * q(1, 4) for m in range(16)] for n in range(16)]


def tau(i):          # V = Fin4 x Fin4 with index 4 i1 + i2; exchange (0,1) and (1,0)
    return {1: 4, 4: 1}.get(i, i)


Ptau = perm_matrix(tau, 16)
wd = [ONE] * 15 + [I_]                        # w(3,3) = i
Wd = diag(wd)
wp = [x for x in (ONE, ONE, ONE, I_) for _ in range(4)]     # diag(1,1,1,i) (x) 1
Wp = diag(wp)

# CT4 factor carrier Fin2 x Fin2, index 2 i + a
X = perm_matrix(lambda k: {1: 3, 3: 1}.get(k, k), 4)        # swap((0,1),(1,1))
W = perm_matrix(lambda k: {0: 1, 1: 0}.get(k, k), 4)        # swap((0,0),(0,1))
I4, I16 = eye(4), eye(16)


def rot(s):          # [[3/5, -4s/5],[4s/5, 3/5]]
    return [[q(3, 5), q(-4 * s, 5)], [q(4 * s, 5), q(3, 5)]]


# ---------------------------------------------------------------- configurations and lifts

def const(n, x):
    return [[x] * n for _ in range(n)]


C21 = Conf("C21", 4, 1, 4, 1, const(16, q(1, 16)))
CCT4 = Conf("CCT4", 2, 2, 2, 2, eye(4))
C1A = Conf("C1A", 4, 1, 1, 1, const(4, q(1, 4)))
C1B = Conf("C1B", 2, 2, 1, 1, eye(2))
CELIM = Conf("CELIM", 2, 1, 1, 2, eye(2))
CENT = Conf("CENT", 2, 1, 2, 1, perm_matrix(lambda j: {2: 3, 3: 2}.get(j, j), 4))
CCC = Conf("CCC", 2, 2, 2, 2, [[q(9, 25) if i == j else (q(16, 25) if i == 3 - j else ZERO)
                                for j in range(4)] for i in range(4)])
TJ3f = Conf("TJ3", 4, 1, 1, 1, const(4, q(1, 4)))
CT4f = Conf("CT4", 2, 2, 1, 1, eye(2))
ONE1 = [[ONE]]

P_, Q_ = C21.prod(H1, H1), C21.prod(Hi, H1)
Utau = matmul(matmul(Ptau, C21.prod(H1, Hi)), dag(Ptau))
QDn, QDp = matmul(Q_, Wd), matmul(Q_, Wp)

L21 = {   # name: (U0, U1, declared SL-U)
    "P": (P_, P_, True), "Q": (Q_, Q_, True), "PQ": (P_, Q_, True),
    "F": (F16, F16, False), "T": (Utau, Utau, False), "PF": (P_, F16, False),
    "Wd.P": (matmul(Wd, P_), matmul(Wd, P_), False), "Wp.P": (matmul(Wp, P_), matmul(Wp, P_), True),
    "Wd.PQ": (matmul(Wd, P_), matmul(Wd, Q_), False), "Wp.PQ": (matmul(Wp, P_), matmul(Wp, Q_), True),
    "PQ.Dn": (P_, QDn, False), "PQ.Dp": (P_, QDp, True),
}

c = CCT4
XX, W1, WW, X1 = c.prod(X, X), c.prod(W, I4), c.prod(W, W), c.prod(X, I4)


def comp_perm(conf, f):
    idx = list(it.product(range(conf.d1), range(conf.d2), range(conf.n1), range(conf.n2)))
    M = [[ZERO] * conf.D for _ in range(conf.D)]
    for (i1, i2, a1, a2) in idx:
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
    for (x, ax), (y, ay) in it.product(((0, 0), (1, 3)), repeat=2):   # ancilla (0,0)->0, (1,1)->3
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
    "I": (I16, I16, True), "X": (I16, XX, True), "W1.X": (W1, matmul(W1, XX), True),
    "We.X": (We, matmul(We, XX), False), "Lcc": (Lcc, Lcc, False), "Llp": (Llp, Llp, True),
    "WW": (WW, WW, True), "WW.Ke": (WW, matmul(WW, Ke), False), "WW.X1": (WW, matmul(WW, X1), True),
}
L1A = {"P'": (C1A.prod(H1, ONE1), C1A.prod(H1, ONE1), True),
       "Q'": (C1A.prod(Hi, ONE1), C1A.prod(Hi, ONE1), True),
       "PQ'": (C1A.prod(H1, ONE1), C1A.prod(Hi, ONE1), True)}
L1B = {"X'": (C1B.prod(I4, ONE1), C1B.prod(X, ONE1), True),
       "WX'": (C1B.prod(W, ONE1), C1B.prod(matmul(W, X), ONE1), True)}


def to_elim(M):      # CT4 carrier (i, a) -> CELIM ((i1,0),(0,a2)) with i1 = i, a2 = a
    E = [[ZERO] * 4 for _ in range(4)]
    for i, a, j, b in it.product(range(2), repeat=4):
        E[CELIM.cidx(i, 0, 0, a)][CELIM.cidx(j, 0, 0, b)] = M[2 * i + a][2 * j + b]
    return E


LELIM = {"I''": (eye(4), eye(4), True), "X''": (to_elim(I4), to_elim(X), False),
         "WX''": (to_elim(W), to_elim(matmul(W, X)), False)}
CN = perm_matrix(lambda j: {2: 3, 3: 2}.get(j, j), 4)
LENT = {"CN": (CN, CN, False)}
Ucv = [[ZERO] * 16 for _ in range(16)]
for i1, i2 in it.product(range(2), repeat=2):
    a, b = CCC.cidx(i1, i2, 0, 0), CCC.cidx(1 - i1, 1 - i2, 1, 1)
    Ucv[a][a], Ucv[b][a], Ucv[a][b], Ucv[b][b] = q(3, 5), q(4, 5), q(-4, 5), q(3, 5)
    for a1, a2 in ((0, 1), (1, 0)):
        k = CCC.cidx(i1, i2, a1, a2)
        Ucv[k][k] = ONE
LCCC = {"Ucv": (Ucv, Ucv, False)}

CONFS = [(C21, L21), (CCT4, LCT4), (C1A, L1A), (C1B, L1B), (CELIM, LELIM), (CENT, LENT), (CCC, LCCC)]

PAIRS = {
    ("C21", "TRAJ"): [("P", "F"), ("P", "T"), ("P", "PF"), ("P", "Q"), ("P", "PQ")],
    ("C21", "THREAD"): [("P", "Wd.P"), ("P", "Wp.P"), ("PQ", "Wd.PQ"), ("PQ", "Wp.PQ"),
                        ("PQ", "PQ.Dn"), ("PQ", "PQ.Dp")],
    ("CCT4", "THREAD"): [("I", "Lcc"), ("I", "Llp"), ("X", "We.X"), ("X", "W1.X"),
                         ("WW", "WW.Ke"), ("WW", "WW.X1")],
    ("C1A", "TRAJ"): [("P'", "Q'"), ("P'", "PQ'")],
    ("C1B", "THREAD"): [("X'", "WX'")],
    ("CELIM", "THREAD"): [("I''", "X''"), ("I''", "WX''")],
}
TAG = {"Wd.P": "L", "Wp.P": "L", "Wd.PQ": "L", "Wp.PQ": "L", "PQ.Dn": "D", "PQ.Dp": "D",
       "Lcc": "L", "Llp": "L", "We.X": "L", "W1.X": "L", "WW.Ke": "S", "WW.X1": "S",
       "WX'": "L", "X''": "", "WX''": "L"}
# exhibited anchored phases D_t (per t in {0,1}) for THREAD pairs; None means D = 1
DPH = {("PQ", "PQ.Dn"): (None, wd), ("PQ", "PQ.Dp"): (None, wp)}

# ---------------------------------------------------------------- bookkeeping

FAIL = []
OUT = []


def say(*a):
    OUT.append(" ".join(str(x) for x in a))


def check(name, ok, detail=""):
    say(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)
    return ok


_choi, _rb = {}, {}


def choi(conf, M):
    k = (conf.name, key(M))
    if k not in _choi:
        _choi[k] = conf.choi(M)
    return _choi[k]


def readback(conf, M):
    k = (conf.name, key(M))
    if k not in _rb:
        _rb[k] = conf.readback(M)
    return _rb[k]


def rel(L, t, s):
    U = (L[0], L[1])
    return matmul(U[t], dag(U[s]))


TIMES = {1: ["t=0", "t=1"], 2: ["(1,0)", "(0,1)"], 3: ["(1,0)", "(0,1)"]}


_vals = {}


def values(conf, L, x):
    k = (conf.name, id(L), x)
    if k not in _vals:
        _vals[k] = _values(conf, L, x)
    return _vals[k]


def _values(conf, L, x):
    if x == 1:
        return [choi(conf, L[0]), choi(conf, L[1])]
    if x == 2:
        return [readback(conf, rel(L, 1, 0)), readback(conf, rel(L, 0, 1))]
    return [choi(conf, rel(L, 1, 0)), choi(conf, rel(L, 0, 1))]


def vkey(x, v):
    if x == 2:
        return key(v)
    return tuple(key(m) for row in v for m in row)


_prod = {}


def nonproduct(conf, x, v):
    k = (conf.name, x, vkey(x, v))
    if k not in _prod:
        T = conf.cut_stoch(v) if x == 2 else conf.cut_choi(v)
        _prod[k] = rank_ge2(T)
    return _prod[k]


# ---------------------------------------------------------------- K0: exact arithmetic

say("== K0 exact arithmetic")
z = zeta(1)
k0 = [zeta(8) == -ONE, zeta(16) == ONE, (z * z.conj()) == ONE]
samples = [C16((1, -2, 0, 3, 0, 0, 5, -1), 7), C16((0, 4, -1, 0, 2, 0, 0, 9), 3), q(3, 5) + I_ * q(4, 5)]
for a, b in it.product(samples, repeat=2):
    k0.append((a * b).conj() == a.conj() * b.conj())
    k0.append(a.conj().conj() == a)
    k0.append((a + b) - b == a)
check("K0 field operations", all(k0))
for nm, U in [("H1", H1), ("Hi", Hi), ("F16", F16), ("P_tau", Ptau), ("W_d", Wd), ("W_p", Wp),
              ("L_cc", Lcc), ("U_cv", Ucv), ("W_e", We), ("K_e", Ke), ("L (x) L", Llp)]:
    check(f"K0 {nm} exactly unitary", is_unitary(U))

# ---------------------------------------------------------------- status checks

say("== status: admissibility, SL-U status, horizon")
STATUS, ADM = {}, {}
for conf, lifts in CONFS:
    for nm, L in lifts.items():
        adm = all(is_unitary(L[t]) and meq(readback(conf, L[t]), conf.gamma) for t in (0, 1))
        sl = all(rank_ge2(conf.cut_operator(L[t])) is None for t in (0, 1))
        STATUS[(conf.name, nm)] = sl
        ADM[(conf.name, nm)] = adm
        check(f"status {conf.name}:{nm} admissible at t=0,1", adm)
        check(f"status {conf.name}:{nm} computed SL-U = {sl}, declared {L[2]}", sl == L[2])

say("== class relations")
CONF = {cf.name: (cf, ls) for cf, ls in CONFS}


def psi(conf, M):
    G = conf.gram(M)
    f00, f10 = 0, 1 * conf.d2
    return G[f00][1 * conf.d2 + 0][0] * G[f10][0][1 * conf.d2 + 0]


def a28_violation(conf, M):
    G = conf.gram(M)
    for i1, i1p, i2, j1, j2, k2 in it.product(range(4), repeat=6):
        a = G[i1 * 4 + i2][j1 * 4 + j2][j1 * 4 + k2]
        b = G[i1p * 4 + i2][j1 * 4 + j2][j1 * 4 + k2]
        if not a == b:
            return (i1, i1p, i2, j1, j2, k2, a, b)
    return None


for (cn, fr), prs in PAIRS.items():
    conf, lifts = CONF[cn]
    for a, b in prs:
        La, Lb = lifts[a], lifts[b]
        if fr == "TRAJ":
            pa, pb = psi(conf, La[1]), psi(conf, Lb[1])
            if not pa == pb:
                check(f"class {cn}:({a},{b}) inequivalent at t=1 by Psi", True, f"{pa} vs {pb}")
            else:
                v = a28_violation(conf, Lb[1]) if cn == "C21" and not STATUS[(cn, b)] else None
                check(f"class {cn}:({a},{b}) inequivalent at t=1 by a28_s_locus_first_index", v is not None,
                      f"fibres ({v[0]},{v[2]}),({v[1]},{v[2]}) indices ({v[3]},{v[4]}),({v[3]},{v[5]}): "
                      f"{v[6]} vs {v[7]}" if v else "no violation found")
        else:
            ok = True
            for t in (0, 1):
                ga, gb = conf.gram(La[t]), conf.gram(Lb[t])
                dv = DPH.get((a, b), (None, None))[t]
                dv = dv if dv is not None else [ONE] * conf.d
                ok &= all(gb[i][j][k] == dv[j].conj() * ga[i][j][k] * dv[k]
                          for i in range(conf.d) for j in range(conf.d) for k in range(conf.d))
            check(f"class {cn}:({a},{b}) equivalent at t=0,1 by the exhibited D_t", ok)

# ---------------------------------------------------------------- K-frozen

say("== K-frozen")
gH1, gHi = TJ3f.gram(H1), TJ3f.gram(Hi)
check("K-frozen act 17 G^(0)_10 G^(1)_01: 1/16 (H1) vs i/16 (Hi)",
      gH1[0][1][0] * gH1[1][0][1] == q(1, 16) and gHi[0][1][0] * gHi[1][0][1] == I_ * q(1, 16))
r_u = CT4f.readback(matmul(X, dag(I4)))[0][0]
r_up = CT4f.readback(matmul(matmul(W, X), dag(W)))[0][0]
check("K-frozen CT4 relative-candidate entry (0,0): 1 (U) vs 0 (U')", r_u == ONE and r_up == ZERO,
      f"{r_u} vs {r_up}")
gT = C21.gram(Utau)
e1, e2 = gT[0 * 4 + 1][2 * 4 + 0][2 * 4 + 1], gT[1 * 4 + 1][2 * 4 + 0][2 * 4 + 1]
check("K-frozen act 28 entries at fibres (0,1),(1,1), indices (2,0),(2,1): 1/16 vs i/16",
      e1 == q(1, 16) and e2 == I_ * q(1, 16), f"{e1} vs {e2}")

# ---------------------------------------------------------------- K-indep

say("== K-indep")
ok_rb, ok_rel = True, True
for conf, lifts in CONFS:
    for nm, L in lifts.items():
        for t in (0, 1):
            C = choi(conf, L[t])
            ok_rb &= all(readback(conf, L[t])[i][j] == C[i][i][j][j] for i in range(conf.d) for j in range(conf.d))
        for (t, s) in ((1, 0), (0, 1)):
            M = rel(L, t, s)
            C = choi(conf, M)
            ok_rel &= all(readback(conf, M)[i][j] == C[i][i][j][j] for i in range(conf.d) for j in range(conf.d))
check("K-indep O0 is the diagonal action of O1 on every lift at t=0,1", ok_rb)
check("K-indep O2 is the diagonal action of O3 on every lift at (1,0),(0,1)", ok_rel)
ok_dil, cover = True, []
for conf, lifts in CONFS:
    for nm, L in lifts.items():
        if conf.n == 1 and not (conf.name == "C21" and nm in ("P", "F")):
            continue
        for t in (0, 1):
            ok_dil &= (conf.choi_by_dilation(L[t]) == choi(conf, L[t]))
        cover.append(f"{conf.name}:{nm}")
check("K-indep O1 by the defining sum equals O1 by dilation and partial trace", ok_dil,
      "on " + ", ".join(cover))

# ---------------------------------------------------------------- K-cert

say("== K-cert")
ok = True
for conf, lifts in CONFS:
    for nm, L in lifts.items():
        if STATUS[(conf.name, nm)]:
            for x in (1, 2, 3):
                ok &= all(nonproduct(conf, x, v) is None for v in values(conf, L, x))
check("K-cert PC reports rank 1 on every admitted lift's O1, O2, O3 values", ok)
check("K-cert PC reports rank >= 2 on F16 as an operator", rank_ge2(C21.cut_operator(F16)) is not None)
mut = [row[:] for row in P_]
mut[0][0] = -mut[0][0]
check("K-cert PC reports rank >= 2 on H1(x)H1 with entry (0,0) negated", rank_ge2(C21.cut_operator(mut)) is not None)

# ---------------------------------------------------------------- pair verdicts and cells

say("== pair verdicts")
POINT = {("CELIM", 2): [eye(2), eye(2)]}      # [W]: SL-U lifts at CELIM have O2 = 1 at every time pair
VERD = {}
for (cn, fr), prs in PAIRS.items():
    conf, lifts = CONF[cn]
    admitted = [n for n in lifts if STATUS[(cn, n)]]
    for a, b in prs:
        for x in (1, 2, 3):
            va, vb = values(conf, lifts[a], x), values(conf, lifts[b], x)
            if STATUS[(cn, b)]:
                diff = [TIMES[x][k] for k in range(2) if not vkey(x, va[k]) == vkey(x, vb[k])]
                v = "KEEP-BOTH" if diff else "SAME"
                det = ("differ at " + ",".join(diff)) if diff else ""
            else:
                cert = None
                for k in range(2):
                    r = nonproduct(conf, x, vb[k])
                    if r is not None:
                        cert = f"non-product at {TIMES[x][k]} (minor rows {r[0]},{r[2]} cols {r[1]},{r[3]})"
                        break
                if cert is None and (cn, x) in POINT:
                    pt = POINT[(cn, x)]
                    for k in range(2):
                        if not vkey(x, vb[k]) == vkey(x, pt[k]):
                            cert = f"differs from the single admitted value at {TIMES[x][k]}"
                            break
                if cert is not None:
                    v, det = "SEP-PHYS", cert
                else:
                    rep = [n for n in admitted
                           if all(vkey(x, values(conf, lifts[n], x)[k]) == vkey(x, vb[k]) for k in range(2))]
                    v, det = ("SEP-REP", "value attained by " + ",".join(rep)) if rep else ("SEP-OPEN", "")
            VERD[(cn, fr, a, b, x)] = v
            tag = TAG.get(b, "")
            say(f"{cn} {fr} ({a},{b}){'[' + tag + ']' if tag else ''} O{x}: {v}" + (f"  {det}" if det else ""))

say("== cells")
ALL_SL = {"C1A", "C1B"}           # [W] RL: every operator with a one-point second factor is a product
CELL = {}
for (cn, fr), prs in PAIRS.items():
    for x in (1, 2, 3):
        vs = [VERD[(cn, fr, a, b, x)] for a, b in prs]
        if cn in ALL_SL:
            out = "UNCHANGED (present)" if "KEEP-BOTH" in vs else "UNCHANGED (absent)"
            if any(v.startswith("SEP") for v in vs):
                out = "UNDETERMINED"
        elif "SEP-PHYS" in vs and (cn, x) in POINT:
            out = "ELIMINATES"
        elif "SEP-PHYS" in vs and "KEEP-BOTH" in vs:
            out = "REDUCES"
        else:
            out = "UNDETERMINED"
        CELL[(cn, fr, x)] = out
        say(f"cell {cn} {fr} O{x}: {out}")
# CCT4 TRAJ: one class by SH1-C2; checked exactly
conf, lifts = CONF["CCT4"]
closed = [[[conf.gamma[i][j] if j == k else ZERO for k in range(conf.d)] for j in range(conf.d)]
          for i in range(conf.d)]
k_unique = all(conf.gram(L[t]) == closed for L in lifts.values() for t in (0, 1))
for x in (1, 2, 3):
    CELL[("CCT4", "TRAJ", x)] = "UNCHANGED (absent)" if k_unique else "UNDETERMINED"
    say(f"cell CCT4 TRAJ O{x}: {CELL[('CCT4', 'TRAJ', x)]}  (SH1-C2 closed form on every lift: {k_unique})")
for cn in ("CENT", "CCC"):
    conf = CONF[cn][0]
    r = rank_ge2(conf.cut_stoch(conf.gamma))
    CELL[(cn, "*", 0)] = "EXCLUDES-ALL" if r is not None else "UNDETERMINED"
    say(f"cell {cn}: {CELL[(cn, '*', 0)]}  (Gamma reshuffled rank >= 2: {r is not None})")

# ---------------------------------------------------------------- controls on the cells

say("== K-17-embed, K-single, K-unique, K-reach")
check("K-17-embed act 17's lifts tensored with H1 (P, Q) are coherent and SL-U",
      STATUS[("C21", "P")] and STATUS[("C21", "Q")])
check("K-17-embed F, T, PF are coherent lifts of Gamma = 1/16", all(ADM[("C21", n)] for n in ("F", "T", "PF")))
check("K-17-embed Psi(P) = 1/256 and Psi(Q) = i/256",
      psi(C21, P_) == q(1, 256) and psi(C21, Q_) == I_ * q(1, 256))
c1 = [CELL[k] for k in CELL if k[0] in ALL_SL]
present = any(VERD[k] == "KEEP-BOTH" for k in VERD if k[0] in ALL_SL)
check("K-single every C1A/C1B cell UNCHANGED, every lift SL-U, some pair differs",
      all(v.startswith("UNCHANGED") for v in c1) and present
      and all(STATUS[(cn, n)] for cn in ALL_SL for n in CONF[cn][1]))
check("K-unique CCT4 tuples equal the SH1-C2 closed form; TRAJ cell UNCHANGED (absent)", k_unique)
check("K-reach CELIM THREAD O2 = ELIMINATES", CELL[("CELIM", "THREAD", 2)] == "ELIMINATES")
check("K-reach CENT and CCC = EXCLUDES-ALL", CELL[("CENT", "*", 0)] == CELL[("CCC", "*", 0)] == "EXCLUDES-ALL")
check("K-reach C1A = UNCHANGED", all(CELL[("C1A", "TRAJ", x)].startswith("UNCHANGED") for x in (1, 2, 3)))

# ---------------------------------------------------------------- no-signalling

say("== no-signalling")


def ptrace_blocks(conf, M, direction):
    """For every matrix unit E_jk of V: the reduced output, traced over V2 (direction '2>1') or V1."""
    s = conf
    out = {}
    for j in range(s.d):
        for k in range(s.d):
            if direction == "2>1":
                r = [[csum(M[(i1 * s.d2 + i2) * s.n + a][j * s.n] * M[(ip1 * s.d2 + i2) * s.n + a][k * s.n].conj()
                           for i2 in range(s.d2) for a in range(s.n))
                      for ip1 in range(s.d1)] for i1 in range(s.d1)]
            else:
                r = [[csum(M[(i1 * s.d2 + i2) * s.n + a][j * s.n] * M[(i1 * s.d2 + ip2) * s.n + a][k * s.n].conj()
                           for i1 in range(s.d1) for a in range(s.n))
                      for ip2 in range(s.d2)] for i2 in range(s.d2)]
            out[(j, k)] = r
    return out


def ns_prep(conf, M):
    """None if prep no-signalling holds both ways, else (direction, j, k)."""
    s = conf
    for direction in ("2>1", "1>2"):
        B = ptrace_blocks(conf, M, direction)
        for j, k in it.product(range(s.d), repeat=2):
            j1, j2 = s.split_v(j)
            k1, k2 = s.split_v(k)
            if direction == "2>1":
                ref = B[(j1 * s.d2, k1 * s.d2)] if j2 == k2 else None
            else:
                ref = B[(j2, k2)] if j1 == k1 else None
            got = B[(j, k)]
            if ref is None:
                if any(not x.iszero() for row in got for x in row):
                    return (direction, j, k)
            elif not meq(got, ref):
                return (direction, j, k)
    return None


def visible_op(conf, Rv, direction):
    """R acting on V (as R1 (x) 1 or 1 (x) R2) and as the identity on A."""
    s = conf
    M = [[ZERO] * s.D for _ in range(s.D)]
    for i1, i2, j1, j2 in it.product(range(s.d1), range(s.d2), range(s.d1), range(s.d2)):
        if direction == "2>1":
            x = Rv[i2][j2] if i1 == j1 else ZERO
        else:
            x = Rv[i1][j1] if i2 == j2 else ZERO
        if not x.iszero():
            for a in range(s.n):
                M[(i1 * s.d2 + i2) * s.n + a][(j1 * s.d2 + j2) * s.n + a] = x
    return M


def ns_int_perms(conf, L):
    """Intervention at s=0, read at t=1, over every permutation of V2 (resp. V1)."""
    base = rel(L, 1, 0)
    for direction, dk in (("2>1", conf.d2), ("1>2", conf.d1)):
        ref = ptrace_blocks(conf, matmul(base, L[0]), direction)
        for p in it.permutations(range(dk)):
            Rv = perm_matrix(lambda i: p[i], dk)
            got = ptrace_blocks(conf, matmul(base, matmul(visible_op(conf, Rv, direction), L[0])), direction)
            if any(not meq(got[jk], ref[jk]) for jk in ref):
                return (direction, p)
    return None


def ns_int_all(conf, L):
    """Sesquilinear certificate covering every unitary intervention, both directions."""
    base = rel(L, 1, 0)
    s = conf
    for direction, dk in (("2>1", s.d2), ("1>2", s.d1)):
        Ms = {}
        for c_, d_ in it.product(range(dk), repeat=2):
            E = [[ONE if (r, cc) == (c_, d_) else ZERO for cc in range(dk)] for r in range(dk)]
            Ms[(c_, d_)] = matmul(base, matmul(visible_op(conf, E, direction), L[0]))
        for j, k in it.product(range(s.d), repeat=2):
            def B(cd, ef):
                M1, M2 = Ms[cd], Ms[ef]
                if direction == "2>1":
                    return [[csum(M1[(i1 * s.d2 + i2) * s.n + a][j * s.n] * M2[(ip1 * s.d2 + i2) * s.n + a][k * s.n].conj()
                                  for i2 in range(s.d2) for a in range(s.n))
                             for ip1 in range(s.d1)] for i1 in range(s.d1)]
                return [[csum(M1[(i1 * s.d2 + i2) * s.n + a][j * s.n] * M2[(i1 * s.d2 + ip2) * s.n + a][k * s.n].conj()
                              for i1 in range(s.d1) for a in range(s.n))
                         for ip2 in range(s.d2)] for i2 in range(s.d2)]
            for c_, d_, e_, f_ in it.product(range(dk), repeat=4):
                val = B((c_, d_), (e_, f_))
                if c_ != e_:
                    if any(not x.iszero() for row in val for x in row):
                        return (direction, j, k, (c_, d_, e_, f_))
                elif not meq(val, B((0, d_), (0, f_))):
                    return (direction, j, k, (c_, d_, e_, f_))
    return None


NS = {}
for cn, names in (("C21", list(L21)), ("CCT4", list(LCT4)), ("CENT", ["CN"]), ("CCC", ["Ucv"])):
    conf, lifts = CONF[cn]
    for nm in names:
        L = lifts[nm]
        prep = [ns_prep(conf, L[t]) for t in (0, 1)]
        if cn == "C21" and not (STATUS[(cn, nm)] or nm == "PF"):
            intr, cover = None, "not run"
        elif cn == "C21":
            intr, cover = ns_int_perms(conf, L), "permutations"
        else:
            intr, cover = ns_int_all(conf, L), "every unitary"
        NS[(cn, nm)] = (prep, intr)
        say(f"{cn}:{nm} (SL-U {STATUS[(cn, nm)]}) prep t=0 {'holds' if prep[0] is None else 'violated ' + str(prep[0])}"
            f"; prep t=1 {'holds' if prep[1] is None else 'violated ' + str(prep[1])}"
            + (f"; int (s=0,t=1; {cover}) {'holds' if intr is None else 'violated ' + str(intr)}"
               if cover != "not run" else ""))


def ns_ok(k):
    p, i = NS[k]
    return p[0] is None and p[1] is None and i is None


tok_hold = all(ns_ok((cn, n)) for cn in ("C21", "CCT4") for n in CONF[cn][1] if STATUS[(cn, n)])
tok_nonvac = (NS[("C21", "F")][0][0] is not None and NS[("C21", "PF")][1] is not None
              and NS[("CCT4", "We.X")][0][0] is not None and NS[("CENT", "CN")][0][0] is not None)
eq1 = all(not (NS[("C21", n)][0][0] is None and NS[("C21", n)][0][1] is None)
          for n in L21 if not STATUS[("C21", n)])
check("EQ1 consistency: every C21 lift not admitted violates prep no-signalling at some t", eq1)
weaker = [f"CCT4:{n}" for n in LCT4 if not STATUS[("CCT4", n)] and ns_ok(("CCT4", n))
          and any(VERD.get(("CCT4", "THREAD", a, b, x)) == "SEP-PHYS"
                  for (a, b) in PAIRS[("CCT4", "THREAD")] if b == n for x in (1, 2, 3))]
if ns_ok(("CCC", "Ucv")) and CELL[("CCC", "*", 0)] == "EXCLUDES-ALL":
    weaker.append("CCC:Ucv")

# ---------------------------------------------------------------- verdicts

say("== verdicts")
say("controls and status checks failed:", len(FAIL))
if FAIL:
    say("VERDICT VOID:", ", ".join(FAIL))
else:
    main = [k for k in CELL if k[0] in ("C21", "CCT4")]
    for fr in ("TRAJ", "THREAD"):
        seps = {x: sorted({f"{cn}:({a},{b})" for (cn, f_, a, b, xx), v in VERD.items()
                           if cn in ("C21", "CCT4") and f_ == fr and xx == x and v == "SEP-PHYS"})
                for x in (1, 2, 3)}
        tok = f"P0-SL-DISTINGUISHES-{fr}" if seps[1] else f"P0-SL-NO-PHYSICAL-SEPARATION-{fr}"
        say(tok, "  O1:", "; ".join(seps[1]) or "none")
        say("   beside it  O2:", "; ".join(seps[2]) or "none", "  O3:", "; ".join(seps[3]) or "none")
    outs = [CELL[k] for k in main]
    if "ELIMINATES" in outs:
        say("P0-SL-SELECTS")
    elif "REDUCES" in outs:
        say("P0-SL-REDUCES-ONLY  (main cells:", ", ".join(f"{k[0]} {k[1]} O{k[2]} {CELL[k]}" for k in sorted(main)) + ")")
    else:
        say("P0-SL-INERT")
    say("P0-NS-HOLDS" if tok_hold else "P0-NS-FAILS-ON-AN-ADMITTED-LIFT")
    say("P0-NS-NONVACUOUS" if tok_nonvac else "P0-NS-VACUOUS-ON-THESE-WITNESSES")
    say("P0-NS-EQUIV-A1")
    say(("P0-NS-WEAKER  witnesses: " + ", ".join(weaker)) if weaker else "P0-NS-NOT-SEPARATED")

print("\n".join(OUT))
