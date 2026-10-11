"""C21 -- the round's explicit exotic cones against R6's Table A2. Exact checks and the row tables.

Node C21 (round 4, research/countermodels). S0 (cones, operations, checks, row rules, predictions) in NOTES-C21,
written 2026-10-11T05:34Z (`date -u`) before this script was first run.

Inputs (read-only): ../../archive/pt/R6/REASSESSMENT.md (Table A2; the blob authorized at research/archive 4dc0321c,
sha256 checked below) and ../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean (the blob at
L = 9f9f8257) for the transcription of the kernel's cnot.

Cones: K384 (HO-24, C11.5), KC (HO-25 item 1, C15.2), Kk (kappa with G16, C16.4), K768 (C19.3).
Exact arithmetic only (Fractions, Gaussian rationals). Deterministic.
"""
from fractions import Fraction as Fr
import hashlib
import re

RES = []


def rec(cid, ok, text, detail=""):
    ok = bool(ok)
    RES.append((cid, ok))
    print("CHECK %-14s %s %s%s" % (cid, "PASS" if ok else "FAIL", text, (" -- " + detail) if detail else ""))


# ---------------------------------------------------------------- Gaussian rationals and matrices
class GQ:
    __slots__ = ("r", "i")

    def __init__(self, r, i=0):
        self.r = r if isinstance(r, Fr) else Fr(r)
        self.i = i if isinstance(i, Fr) else Fr(i)

    def __add__(s, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return GQ(s.r + o.r, s.i + o.i)

    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return GQ(s.r - o.r, s.i - o.i)

    def __neg__(s):
        return GQ(-s.r, -s.i)

    def __mul__(s, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return GQ(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)

    __rmul__ = __mul__

    def conj(s):
        return GQ(s.r, -s.i)

    def n2(s):
        return s.r * s.r + s.i * s.i

    def __truediv__(s, o):
        o = o if isinstance(o, GQ) else GQ(o)
        d = o.n2()
        t = s * o.conj()
        return GQ(t.r / d, t.i / d)

    def iszero(s):
        return s.r == 0 and s.i == 0

    def __eq__(s, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return s.r == o.r and s.i == o.i

    def __hash__(s):
        return hash((s.r, s.i))

    def __repr__(s):
        if s.i == 0:
            return str(s.r)
        return "%s%s%si" % (s.r, "+" if s.i >= 0 else "-", abs(s.i))


ZERO, ONE, II = GQ(0), GQ(1), GQ(0, 1)


def M(rows):
    return [[x if isinstance(x, GQ) else GQ(x) for x in r] for r in rows]


def mmul(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), ZERO) for j in range(len(B[0]))] for i in range(len(A))]


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(c, A):
    return [[c * x for x in r] for r in A]


def mv(A, v):
    return [sum((A[i][t] * v[t] for t in range(len(v))), ZERO) for i in range(len(A))]


def ipv(u, v):
    return sum((u[t].conj() * v[t] for t in range(len(u))), ZERO)


def n2v(v):
    return sum((x.n2() for x in v), Fr(0))


def ovl(u, v):
    return ipv(u, v).n2() / (n2v(u) * n2v(v))


def detr(v):
    return (v[0] * v[3] - v[1] * v[2]).n2() / n2v(v) ** 2


def canon(v):
    k = next(t for t in range(len(v)) if not v[t].iszero())
    a = v[k]
    return tuple(x / a for x in v)


def V(*xs):
    return [x if isinstance(x, GQ) else GQ(x) for x in xs]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), ZERO)


def proj(v):
    n = n2v(v)
    return [[v[i] * v[j].conj() / n for j in range(len(v))] for i in range(len(v))]


def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


s0 = M([[1, 0], [0, 1]])
sx = M([[0, 1], [1, 0]])
sy = M([[0, GQ(0, -1)], [II, 0]])
sz = M([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
SS = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]


# ---------------------------------------------------------------- tables (the kernel's W 3) and their maps
def table(A):
    """t_mn = tr(A s_m (x) s_n); real for Hermitian A."""
    out = []
    for m in range(4):
        row = []
        for n in range(4):
            t = tr(mmul(A, SS[m][n]))
            assert t.i == 0, "non-real table entry"
            row.append(t.r)
        out.append(row)
    return out


def pW(t):
    A = [[ZERO] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            if t[m][n] != 0:
                A = madd(A, mscale(GQ(Fr(t[m][n]) / 4), SS[m][n]))
    return A


def ip(a, b):
    return sum((Fr(a[m][n]) * Fr(b[m][n]) for m in range(4) for n in range(4)), Fr(0))


def Hom(N):
    return [[Fr(1) if (i == 0 and j == 0) else (Fr(0) if (i == 0 or j == 0) else Fr(N[i - 1][j - 1]))
             for j in range(4)] for i in range(4)]


def rmul(A, B):
    return [[sum((Fr(A[i][t]) * Fr(B[t][j]) for t in range(4)), Fr(0)) for j in range(4)] for i in range(4)]


def rT(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


def actC(N, w):
    return rmul(Hom(N), w)


def actT(N, w):
    return rmul(w, rT(Hom(N)))


SGNS = {(1, 3), (2, 2)}
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnotW(w):
    return [[(-1 if (m, n) in SGNS else 1) * Fr(w[PC[m][n]][PT[m][n]]) for n in range(4)] for m in range(4)]


def transposeW(w):
    return [[(-1 if m == 2 else 1) * (-1 if n == 2 else 1) * Fr(w[m][n]) for n in range(4)] for m in range(4)]


def swapW(w):
    return rT(w)


def hom(x):
    return [Fr(1)] + [Fr(t) for t in x]


def prodW(x, y):
    a, b = hom(x), hom(y)
    return [[a[m] * b[n] for n in range(4)] for m in range(4)]


def Rof(Vm, kap):
    """rotation of U = Vm/sqrt(kap): R_ij = tr(s_i U s_j U^dag)/2."""
    R = []
    for i in range(3):
        row = []
        for j in range(3):
            t = tr(mmul(mmul(mmul(SIG[i + 1], Vm), SIG[j + 1]), dag(Vm)))
            assert t.i == 0
            row.append(t.r / (2 * kap))
        R.append(row)
    return R


def basisW(m, n):
    return [[Fr(1) if (a == m and b == n) else Fr(0) for b in range(4)] for a in range(4)]


BASIS = [basisW(m, n) for m in range(4) for n in range(4)]

# ---------------------------------------------------------------- operations
P0, P1 = M([[1, 0], [0, 0]]), M([[0, 0], [0, 1]])
CNOT = madd(kron(P0, s0), kron(P1, sx))
SWAP = M([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
mI = GQ(0, -1)
ONE_TOKEN = [  # name, V (2x2 Gaussian-integer), kappa with V V^dag = kappa I
    ("R_z(pi)", sz, 1),
    ("R_z(pi/2)", madd(s0, mscale(mI, sz)), 2),
    ("R_z(t0)", madd(mscale(GQ(2), s0), mscale(mI, sz)), 5),
    ("R_x(pi)", sx, 1),
    ("R_x(pi/2)", madd(s0, mscale(mI, sx)), 2),
    ("R_x(t0)", madd(mscale(GQ(2), s0), mscale(mI, sx)), 5),
    ("J", madd(s0, mscale(mI, madd(madd(sx, sy), sz))), 4),
    ("R_n(pi/2)", madd(mscale(GQ(5), s0), mscale(mI, madd(mscale(GQ(3), sx), mscale(GQ(4), sz)))), 50),
    ("R1", madd(mscale(GQ(3), s0), mscale(mI, madd(madd(mscale(GQ(5), sx), sy), sz))), 36),
]
CLIFFORD = {"R_z(pi)", "R_z(pi/2)", "R_x(pi)", "R_x(pi/2)", "J"}
OPS = []  # (name, token, kind, matrix): kind 'U' unitary on vectors, 'A' antiunitary (U o conj)
for nm, Vm, kap in ONE_TOKEN:
    OPS.append(("actC " + nm, "C", "U", kron(Vm, s0)))
    OPS.append(("actT " + nm, "T", "U", kron(s0, Vm)))
OPS.append(("cnot", "2", "U", CNOT))
OPS.append(("SWAP", "2", "U", SWAP))
OPS.append(("transposeW", "2", "A", eye(4)))


def apply_op(kind, U, v):
    if kind == "U":
        return mv(U, v)
    return mv(U, [x.conj() for x in v])


# ---------------------------------------------------------------- R0: Table A2
src_path = "../../archive/pt/R6/REASSESSMENT.md"
raw = open(src_path, "rb").read()
sha = hashlib.sha256(raw).hexdigest()
rea = raw.decode("utf-8")
blk = rea.split("### Table A2", 1)[1].split("\n### ", 1)[0]
A2 = []
for line in blk.split("\n"):
    if line.startswith("| I"):
        f = [x.strip() for x in line.strip().strip("|").split(" | ")]
        A2.append(dict(id=f[0], stmt=f[1], cls=f[2], verdict=f[3], ev=f[4]))
vt = {"SATISFIES": 0, "NOT REACHED": 0, "FAILS": 0}
for r in A2:
    for k in vt:
        if r["verdict"].startswith(k):
            vt[k] += 1
ct = {}
for r in A2:
    ct.setdefault(r["cls"], set()).add(r["verdict"].split(" [")[0].split(" (")[0])
cnt = {}
for r in A2:
    cnt[r["cls"]] = cnt.get(r["cls"], 0) + 1
KINDEP_S = ["def", "thm", "gate", "inh", "d4s"]
NR = ["nr", "hmg"]
KDEP_S = ["cone", "kthm", "b1", "d4v"]
KDEP_F = ["dna", "d4f", "cand"]
ok_r0 = (sha == "1ff62ad633fbd752f247d49b605e6cc8d984e23d8b7151b6497cdd60fa884ffe" and len(A2) == 199
         and len({r["id"] for r in A2}) == 199 and vt == {"SATISFIES": 118, "NOT REACHED": 68, "FAILS": 13}
         and sum(cnt.get(c, 0) for c in KINDEP_S) == 89 and all(ct[c] == {"SATISFIES"} for c in KINDEP_S if c in ct)
         and sum(cnt.get(c, 0) for c in NR) == 68 and all(ct[c] == {"NOT REACHED"} for c in NR)
         and (cnt["cone"], cnt["kthm"], cnt["b1"], cnt["d4v"]) == (12, 1, 13, 3)
         and all(ct[c] == {"SATISFIES"} for c in KDEP_S)
         and (cnt["dna"], cnt["d4f"], cnt["cand"]) == (9, 2, 2) and all(ct[c] == {"FAILS"} for c in KDEP_F)
         and set(cnt) == set(KINDEP_S + NR + KDEP_S + KDEP_F))
rec("R0", ok_r0, "Table A2 of R6 parsed from the authorized blob",
    "sha256 %s..., %d rows, verdicts %s, classes %s" % (sha[:16], len(A2), vt, dict(sorted(cnt.items()))))

# ---------------------------------------------------------------- D1-D3: K-independent transcription checks
d1 = True
for nm, Vm, kap in ONE_TOKEN:
    R = Rof(Vm, kap)
    UC, UT = kron(Vm, s0), kron(s0, Vm)
    for b in BASIS:
        A = pW(b)
        imC = table(mscale(GQ(Fr(1, kap)), mmul(mmul(UC, A), dag(UC))))
        imT = table(mscale(GQ(Fr(1, kap)), mmul(mmul(UT, A), dag(UT))))
        d1 &= imC == actC(R, b) and imT == actT(R, b)
R_named = {nm: Rof(Vm, kap) for nm, Vm, kap in ONE_TOKEN}
d1 &= R_named["R_z(pi)"] == [[-1, 0, 0], [0, -1, 0], [0, 0, 1]] and R_named["R_x(pi)"] == [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
d1 &= R_named["J"] == [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
d1 &= R_named["R_x(t0)"] == [[1, 0, 0], [0, Fr(3, 5), Fr(-4, 5)], [0, Fr(4, 5), Fr(3, 5)]]
rec("D1", d1, "actC R(U), actT R(U) = Ad(U(x)I), Ad(I(x)U) on the 16 basis tables, for the 9 one-token unitaries",
    "R(Z) = rot3(pi), R(X) = nflip, R(U_J) = cyc3, R_x(t0) with cos t0 = 3/5 (CompositeDimension.lean:198, :201)")

src = open("../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean", encoding="utf-8").read()


def lean_table(name):
    b = re.search(r"def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){4})" % name, src).group(1)
    tab = [[None] * 4 for _ in range(4)]
    for a, b2, v in re.findall(r"(\d), (\d) => (\d)", b):
        tab[int(a)][int(b2)] = int(v)
    return tab


sgn_src = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = 1 ∧ ν = 3\) ∨ \(μ = 2 ∧ ν = 2\) then -1 else 1", src)
d2 = lean_table("pc") == PC and lean_table("pt") == PT and sgn_src is not None
d2 &= all(table(mmul(mmul(CNOT, pW(b)), dag(CNOT))) == cnotW(b) for b in BASIS)
d2 &= all(table([[x.conj() for x in r] for r in pW(b)]) == transposeW(b) for b in BASIS)
d2 &= all(table(mmul(mmul(SWAP, pW(b)), SWAP)) == swapW(b) for b in BASIS)
rec("D2", d2, "cnot = Ad(CNOT) (pc, pt, sgn equal the Lean text at L), transposeW = complex conjugation, SWAP = "
              "table transpose, on the 16 basis tables")

z3, xplus = [0, 0, 1], [1, 0, 0]
reflY = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
phiW = [[Fr(1), 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]
idW = [[Fr(1) if i == j else Fr(0) for j in range(4)] for i in range(4)]
chain_end = cnotW(prodW([-1, 0, 0], [0, 0, -1]))
d3_val = ip(idW, chain_end)
d3 = (cnotW(prodW(xplus, z3)) == [[Fr(x) for x in r] for r in phiW] and actT(reflY, phiW) == idW and d3_val == -2)
rec("D3", d3, "the kernel chain: cnot prodState(xplus, z3) = phiW, actT reflY phiW = idW, "
              "ipW(idW, cnot prodState(-e1, -e3)) < 0", "value %s (K2Guard.lean:143's obstruction)" % d3_val)


# ---------------------------------------------------------------- cones
def orbit_rays(h, gens):
    start = canon(h)
    seen = {start}
    fr = [list(start)]
    while fr:
        nf = []
        for v in fr:
            for U in gens:
                w = canon(mv(U, v))
                if w not in seen:
                    seen.add(w)
                    nf.append(list(w))
        fr = nf
    return seen


S = M([[1, 0], [0, II]])
UJ = mscale(GQ(Fr(1, 2)), madd(s0, mscale(mI, madd(madd(sx, sy), sz))))
G_cnot, G_TS, G_TJ = CNOT, kron(s0, S), kron(s0, UJ)
G_CS, G_CJ, G_CX = kron(S, s0), kron(UJ, s0), kron(sx, s0)
hstar = V(10, GQ(2, -2), GQ(-1, -3), GQ(3, -1))
hC = V(GQ(-480, 7), GQ(357, 870), GQ(939, 834), GQ(448, 486))
hk = V(6, 2, 1, -1)


class FiniteCone:
    def __init__(self, tag, h, c, gens, size, src_vals):
        self.tag, self.h, self.c, self.gens = tag, h, c, gens
        self.orb = orbit_rays(h, gens)
        self.size_expected = size
        self.src_vals = src_vals
        self.rays = sorted(self.orb, key=lambda t: tuple((x.r, x.i) for x in t))
        self.n2 = {r: n2v(list(r)) for r in self.rays}

    def member(self, w):
        """P_w in K (P_w in Q3 and in Z*): c |<h_l|w>|^2 <= |h_l|^2 |w|^2 for every defect."""
        nw = n2v(w)
        return all(self.c * ipv(list(r), w).n2() <= self.n2[r] * nw for r in self.rays)

    def maxovl(self, w):
        return max(ovl(list(r), w) for r in self.rays)

    def data(self):
        hc = canon(self.h)
        dets = [detr(list(r)) for r in self.rays]
        ovs = [ovl(self.h, list(r)) for r in self.rays if r != hc]
        nperp = sum(1 for r in self.rays if r != hc and ipv(self.h, list(r)).iszero())
        dmin, smin, smax = min(dets), min(ovs), max(ovs)
        c = self.c
        h1 = 1 - 4 * dmin <= (2 / c - 1) ** 2
        cc = c * c * smin >= 4 * (c - 1)
        return dict(rays=len(self.rays), dmin=dmin, smin=smin, smax=smax, nperp=nperp, h1=h1, cc=cc)

    def decide(self, kind, U):
        imgs = [canon(apply_op(kind, U, list(r))) for r in self.rays]
        if set(imgs) == self.orb:
            return ("INVARIANT", None)
        for r, im in zip(self.rays, imgs):
            if im in self.orb:
                continue
            w = list(im)
            if self.member(w):
                # tr(g(d_l) P_w) with g(d_l) = I - c P_{g h_l}, w = g h_l (up to a scalar): 1 - c
                val = 1 - self.c * ovl(apply_op(kind, U, list(r)), w)
                return ("MOVED", (val, self.maxovl(w)))
        return ("UNDECIDED", None)


class KappaCone:
    """two circles {(6, 2s, x, -s x) : |x| = 1}, s = +1, -1; c = 103/100."""

    def __init__(self, c):
        self.tag, self.c, self.h = "Kk", c, hk
        self.A = {s: V(6, 2 * s, 0, 0) for s in (1, -1)}
        self.B = {s: V(0, 0, 1, -s) for s in (1, -1)}
        self.N2 = Fr(42)
        self.XPTS = [GQ(1), GQ(-1), II, GQ(0, -1), GQ(Fr(3, 5), Fr(4, 5)), GQ(Fr(4, 5), Fr(3, 5)),
                     GQ(Fr(-3, 5), Fr(4, 5)), GQ(Fr(5, 13), Fr(12, 13))]

    def point(self, s, x):
        return [self.A[s][t] + x * self.B[s][t] for t in range(4)]

    def member(self, w):
        """max over both circles of c |<h_x|w>|^2 <= 42 |w|^2: (|a| + |b|)^2 <= R with a = <A|w>, b = <B|w>."""
        R = self.N2 * n2v(w) / self.c
        for s in (1, -1):
            a2, b2 = ipv(self.A[s], w).n2(), ipv(self.B[s], w).n2()
            t = R - a2 - b2
            if t < 0 or 4 * a2 * b2 > t * t:
                return False
        return True

    def maxovl_bound(self, w):
        out = []
        for s in (1, -1):
            a2, b2 = ipv(self.A[s], w).n2(), ipv(self.B[s], w).n2()
            out.append((a2, b2))
        return out

    @staticmethod
    def on_circle_identically(a, b):
        """v = a + x b lies on one circle for every |x| = 1: returns s' or None."""
        for sp_ in (1, -1):
            l1 = (a[1] == a[0] * GQ(Fr(sp_, 3))) and (b[1] == b[0] * GQ(Fr(sp_, 3)))
            l2 = (a[3] == -sp_ * a[2]) and (b[3] == -sp_ * b[2])
            q1 = a[0].n2() + b[0].n2() == 36 * (a[2].n2() + b[2].n2())
            q2 = (a[0].conj() * b[0]) == 36 * (a[2].conj() * b[2])
            if l1 and l2 and q1 and q2:
                return sp_
        return None

    @staticmethod
    def on_circle_at(v):
        if v[0].iszero():
            return False
        for sp_ in (1, -1):
            if v[1] == v[0] * GQ(Fr(sp_, 3)) and v[3] == -sp_ * v[2] and v[0].n2() == 36 * v[2].n2():
                return True
        return False

    def data(self):
        # closed forms (NOTES-C16): same circle <h_x|h_y> = 40 + 2 conj(x) y, other circle 32; det = -8x; |h|^2 = 42.
        pts = [(s, x) for s in (1, -1) for x in self.XPTS]
        dets = [detr(self.point(s, x)) for s, x in pts]
        ovs = [ovl(self.point(1, GQ(1)), self.point(s, x)) for s, x in pts if not (s == 1 and x == GQ(1))]
        smin_closed = Fr(256, 441)
        same_min = Fr(38 * 38, 42 * 42)
        c = self.c
        h1 = 1 - 4 * Fr(16, 441) <= (2 / c - 1) ** 2
        cc = c * c * smin_closed >= 4 * (c - 1)
        ok = (all(d == Fr(16, 441) for d in dets) and min(ovs) == smin_closed and same_min > smin_closed
              and all(ovl(self.point(1, GQ(1)), self.point(-1, x)) == smin_closed for x in self.XPTS))
        return dict(rays="two circles", dmin=Fr(16, 441), smin=smin_closed, smax=None, nperp=0, h1=h1, cc=cc,
                    closed_forms=ok)

    def decide(self, kind, U):
        imgs = {}
        for s in (1, -1):
            if kind == "U":
                a, b = mv(U, self.A[s]), mv(U, self.B[s])
            else:
                a, b = mv(U, [x.conj() for x in self.A[s]]), mv(U, [x.conj() for x in self.B[s]])
            imgs[s] = self.on_circle_identically(a, b)
        if imgs[1] is not None and imgs[-1] is not None:
            return ("INVARIANT", None)
        for s in (1, -1):
            for x in self.XPTS:
                p = self.point(s, x)
                w = apply_op(kind, U, p)
                if self.on_circle_at(w):
                    continue
                if self.member(w):
                    val = 1 - self.c * ovl(apply_op(kind, U, p), w)
                    return ("MOVED", (val, None))
        return ("UNDECIDED", None)


CONES = [
    ("K384", lambda: FiniteCone("K384", hstar, Fr(401, 400), [G_cnot, G_TS, G_TJ], 192,
                                dict(dmin=Fr(85, 2048), smin=Fr(25, 2048), smax=Fr(13, 16)))),
    ("KC", lambda: FiniteCone("KC", hC, Fr(100001, 100000), [G_cnot, G_TS, G_TJ, G_CS, G_CJ], 11520,
                              dict(dmin=Fr(198406621629, 9790484550625), smin=Fr(164178929, 3916193820250)))),
    ("Kk", lambda: KappaCone(Fr(103, 100))),
    ("K768", lambda: FiniteCone("K768", hstar, Fr(10001, 10000), [G_cnot, G_TS, G_TJ, G_CX], 384,
                                dict(dmin=Fr(85, 2048), smin=Fr(1, 1024)))),
]
GEN_CONTROLS = {
    "K384": [("cnot", "U", G_cnot), ("actT S", "U", G_TS), ("actT J", "U", G_TJ)],
    "KC": [("cnot", "U", G_cnot), ("actT S", "U", G_TS), ("actT J", "U", G_TJ), ("actC S", "U", G_CS),
           ("actC J", "U", G_CJ)],
    "Kk": [("cnot", "U", G_cnot), ("Ad(Z(x)I)", "U", kron(sz, s0)), ("Ad(I(x)Z)", "U", kron(s0, sz)),
           ("T", "A", eye(4)),
           ("U(x), x = (3+4i)/5", "U", madd(kron(P0, s0), kron(P1, M([[GQ(Fr(4, 5), Fr(2, 5)), GQ(Fr(1, 5), Fr(-2, 5))],
                                                                        [GQ(Fr(1, 5), Fr(-2, 5)), GQ(Fr(4, 5), Fr(2, 5))]]))))],
    "K768": [("cnot", "U", G_cnot), ("actT S", "U", G_TS), ("actT J", "U", G_TJ), ("actC nflip", "U", G_CX)],
}
MOVED_CONTROLS = {"K384": ["actC R_x(pi)", "actC J"], "KC": [], "Kk": ["actT R_x(pi)"], "K768": ["actC J"]}
BELLS = [("Phi+", V(1, 0, 0, 1)), ("Psi+", V(0, 1, 1, 0)), ("Phi-", V(1, 0, 0, -1)), ("|00>+i|11>", V(1, 0, 0, II))]
CHIS = [M([[2, 1], [0, 1]]), M([[1, 1], [0, 2]]), M([[3, 1], [1, 2]]), M([[2, II], [1, 1]])]


def coeff(v):
    return [[v[0], v[1]], [v[2], v[3]]]


def flat(A):
    return [A[0][0], A[0][1], A[1][0], A[1][1]]


def inv2(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return [[A[1][1] / d, -A[0][1] / d], [-A[1][0] / d, A[0][0] / d]]


def ptrans_T(P):
    """partial transpose on the target of a 4x4 matrix (index 2a + b)."""
    out = [[ZERO] * 4 for _ in range(4)]
    for a in range(2):
        for b in range(2):
            for a2 in range(2):
                for b2 in range(2):
                    out[2 * a + b][2 * a2 + b2] = P[2 * a + b2][2 * a2 + b]
    return out


def famI(Xt, Yt, Et, Ft):
    return sum((Fr(Xt[m][n]) * Fr(Et[m][k]) * Fr(Yt[k][l]) * Fr(Ft[n][l])
                for m in range(4) for n in range(4) for k in range(4) for l in range(4)), Fr(0))


def fourtoken_trace(x, y, e, f):
    """16 tr[(x_ab (x) y_cd)(e_ac (x) f_bd)], qubit order a b c d (index 8a + 4b + 2c + d)."""
    def idx(a, b, c, d):
        return 8 * a + 4 * b + 2 * c + d
    P = [[ZERO] * 16 for _ in range(16)]
    Q = [[ZERO] * 16 for _ in range(16)]
    bits = [(a, b, c, d) for a in range(2) for b in range(2) for c in range(2) for d in range(2)]
    for (a, b, c, d) in bits:
        for (a2, b2, c2, d2) in bits:
            P[idx(a, b, c, d)][idx(a2, b2, c2, d2)] = x[2 * a + b][2 * a2 + b2] * y[2 * c + d][2 * c2 + d2]
            Q[idx(a, b, c, d)][idx(a2, b2, c2, d2)] = e[2 * a + c][2 * a2 + c2] * f[2 * b + d][2 * b2 + d2]
    t = sum((P[i][j] * Q[j][i] for i in range(16) for j in range(16)), ZERO)
    return t * 16


def sqrt_le(a, b, t):
    """sqrt(a) + sqrt(b) < sqrt(t) for nonnegative rationals, exactly."""
    u = t - a - b
    return u > 0 and 4 * a * b < u * u


# ---------------------------------------------------------------- per-cone computation
RESULTS = {}
for tag, mk in CONES:
    K = mk()
    dat = K.data()
    if tag == "Kk":
        ok0 = dat["closed_forms"] and dat["h1"] and dat["cc"]
        det_txt = "two circles, |det Psi|^2 = 16/441 throughout, overlaps >= 256/441 (closed forms at %d exact points)" % (
            2 * len(K.XPTS))
    else:
        sv = K.src_vals
        ok0 = (dat["rays"] == K.size_expected and dat["dmin"] == sv["dmin"] and dat["smin"] == sv["smin"]
               and ("smax" not in sv or dat["smax"] == sv["smax"]) and dat["nperp"] == 0 and dat["h1"] and dat["cc"])
        det_txt = "%d rays, min |det Psi|^2 = %s, overlaps in [%s, %s], orthogonal pairs %d" % (
            dat["rays"], dat["dmin"], dat["smin"], dat["smax"], dat["nperp"])
    rec(tag + "-0", ok0, "cone data reproduce the source; H1 (Schmidt bound) and (CC) exact at c = %s" % K.c, det_txt)

    # controls: generators INVARIANT; membership rejects P_h
    gc = [(nm, K.decide(kind, U)[0]) for nm, kind, U in GEN_CONTROLS[tag]]
    rec(tag + "-CG", all(v == "INVARIANT" for _, v in gc) and not K.member(K.h),
        "control: every generator of the cone's group is INVARIANT; the membership test rejects P_h",
        ", ".join("%s %s" % x for x in gc))

    # (b): the 21 operations (+ reflY through the chain)
    out = {}
    for nm, tok, kind, U in OPS:
        out[nm] = K.decide(kind, U)
    und = [nm for nm in out if out[nm][0] == "UNDECIDED"]
    mc = [(nm, out[nm][0]) for nm in MOVED_CONTROLS[tag]]
    rec(tag + "-B", not und and all(v == "MOVED" for _, v in mc),
        "every operation decided (INVARIANT, or MOVED with an exact witness); known moving maps MOVED",
        "undecided %s; controls %s" % (und, mc))
    for nm, tok, kind, U in OPS:
        st, wv = out[nm]
        print("OP   %-5s %-16s %-9s%s" % (tag, nm, st, "" if wv is None else (
            " witness tr(g(d) P_w) = %s%s" % (wv[0], "" if wv[1] is None else ", w's max overlap with Z %s" % wv[1]))))

    # Q3-level: K != Q3, K != twin, FCC
    qh = 1 - K.c  # tr(d_h P_h) for unit h
    ybell = next(((nm, y) for nm, y in BELLS if K.member(y)), None)
    twin_ok = False
    if ybell is not None:
        PG = ptrans_T(proj(ybell[1]))
        probes = BELLS + [("sing", V(0, 1, -1, 0)), ("x+", V(0, 1, GQ(0, 1), 0)), ("x-", V(0, 1, GQ(0, -1), 0))]
        negs = [ipv(u, mv(PG, u)).r / n2v(u) for _, u in probes]
        twin_ok = min(negs) == Fr(-1, 2)
    rec(tag + "-Q1", qh < 0 and not K.member(K.h) and twin_ok,
        "I3.144: P_h in Q3 is not in K (tr(d_h P_h) = 1 - c < 0); an entangled pure state in K is outside twin",
        "1 - c = %s; %s in K, its partial transpose has eigenvalue -1/2" % (qh, ybell[0] if ybell else None))
    fcc = None
    if ybell is not None:
        Hm, Ym = coeff(K.h), coeff(ybell[1])
        for xi, Xm in enumerate(CHIS):
            Ybar = [[Ym[i][j].conj() for j in range(2)] for i in range(2)]
            Psi = mmul(Hm, inv2(mmul(Ybar, [[Xm[j][i] for j in range(2)] for i in range(2)])))
            psi, chi = flat(Psi), flat(Xm)
            if K.member(psi) and K.member(chi):
                nh = n2v(K.h)
                dh = madd(eye(4), mscale(GQ(-K.c), proj(K.h)))
                Py, Pe, Pf = proj(ybell[1]), proj(psi), proj(chi)
                Xt, Yt, Et, Ft = table(dh), table(Py), table(Pe), table(Pf)
                fI = famI(Xt, Yt, Et, Ft)
                op = fourtoken_trace(dh, Py, Pe, Pf)
                fctrl = famI(table(proj(K.h)), Yt, Et, Ft)
                # the contraction of (Y, E, F) is the effect on the first pair: v = Psi Ybar X^T ~ H
                vmat = mmul(mmul(Psi, Ybar), [[Xm[j][i] for j in range(2)] for i in range(2)])
                fcc = dict(chi=xi, fI=fI, op=op, ctrl=fctrl, v_is_h=canon(flat(vmat)) == canon(K.h))
                break
    rec(tag + "-Q2", fcc is not None and fcc["fI"] < 0 and fcc["op"] == GQ(fcc["fI"]) and fcc["ctrl"] > 0 and fcc["v_is_h"],
        "I3.135 FCC (uniform): X = d_h, Y = P_y, E = P_psi, F = P_chi, all in K, famI < 0; famI = 16 tr[(x(x)y)(e(x)f)]; "
        "control X = P_h gives famI > 0",
        "chi #%s; famI = %s, operator route %s, control %s" % (
            fcc["chi"] if fcc else None, fcc["fI"] if fcc else None, fcc["op"] if fcc else None,
            fcc["ctrl"] if fcc else None))
    if tag != "Kk":
        tsup = sqrt_le(dat["smax"], 1 - 1 / K.c, 1 / K.c)
        print("RECORD %s-T T-support (sqrt s_max + sqrt(1 - 1/c) < sqrt(1/c)): %s (s_max = %s, c = %s)" % (
            tag, tsup, dat["smax"], K.c))
    else:
        tsup = None
    RESULTS[tag] = dict(K=K, dat=dat, ops=out, ybell=ybell, twin=twin_ok, fcc=fcc, tsup=tsup, qh=qh)

# ---------------------------------------------------------------- Q3 control for FCC (C1's instance pool)
axes = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
tabs72 = [prodW(a, b) for a in axes for b in axes]
tabs72 += [cnotW(t) for t in tabs72]


def I8(t):
    return [[int(8 * Fr(t[m][n])) for n in range(4)] for m in range(4)]


T72 = [I8(t) for t in tabs72]
Xq = [I8(phiW), I8(prodW(z3, z3)), I8(cnotW(prodW(xplus, xplus)))]
Aq = [[[sum(X[k][i] * Et[k][j] for k in range(4)) for j in range(4)] for i in range(4)] for X in Xq for Et in T72]
Bq = []
for Y in T72:
    for Ft in T72:
        b = [[sum(Y[i][k] * Ft[j][k] for k in range(4)) for j in range(4)] for i in range(4)]
        Bq.append([b[j][i] for i in range(4) for j in range(4)])
best = None
for a in Aq:
    af = [a[i][j] for i in range(4) for j in range(4)]
    for bf in Bq:
        v = sum(x * y for x, y in zip(af, bf))
        if best is None or v < best:
            best = v
rec("Q3-FCC", best >= 0, "Q3 control: C1's instance pool (3 quantum states x 72 product / cnot-product tables) has "
                         "min famI >= 0", "min %s" % Fr(best, 8 ** 4))

# ---------------------------------------------------------------- row decisions
OPN = [nm for nm, _, _, _ in OPS]
TOK = {"C": [n for n in OPN if n.startswith("actC ")], "T": [n for n in OPN if n.startswith("actT ")]}


def moved(o, nm):
    return o[nm][0] == "MOVED"


def inv(o, nm):
    return o[nm][0] == "INVARIANT"


def ops_txt(o, names):
    invs = [n.split(" ", 1)[1] for n in names if inv(o, n)]
    movs = [n.split(" ", 1)[1] for n in names if moved(o, n)]
    s = []
    if invs:
        s.append("satisfied: " + ", ".join(invs))
    if movs:
        s.append("failed: " + ", ".join(movs))
    return "; ".join(s)


ROW_TABLES = {}
for tag, _ in CONES:
    R = RESULTS[tag]
    o = R["ops"]
    anyC = any(moved(o, n) for n in TOK["C"])
    anyT = any(moved(o, n) for n in TOK["T"])
    drive = ["R_z(pi)", "R_z(pi/2)", "R_z(t0)", "J"]
    dj = ["R_z(pi)", "R_z(pi/2)", "R_z(t0)", "R_x(pi)", "R_x(pi/2)", "R_x(t0)", "J"]
    tokfail = lambda names, t: any(moved(o, "act%s %s" % (t, n)) for n in names)
    v = {}
    v["I3.137"] = ("FAILS" if (anyC or anyT) else "not refuted by the list",
                   "control — %s | target — %s" % (ops_txt(o, TOK["C"]), ops_txt(o, TOK["T"])))
    v["I3.142"] = ("FAILS" if (tokfail(drive, "C") or tokfail(drive, "T")) else "not refuted by the list",
                   "control — %s | target — %s" % (ops_txt(o, ["actC " + n for n in drive]),
                                                  ops_txt(o, ["actT " + n for n in drive])))
    v["I3.150"] = ("FAILS" if (anyC and anyT) else ("FAILS on one token" if (anyC or anyT) else "not refuted by the list"),
                   "control: %s | target: %s" % ("failed" if anyC else "not refuted", "failed" if anyT else "not refuted"))
    nC, nT = moved(o, "actC R_n(pi/2)"), moved(o, "actT R_n(pi/2)")
    v["I3.151"] = ("FAILS" if (nC and nT) else ("FAILS on one token" if (nC or nT) else "not refuted by the list"),
                   "control — %s | target — %s" % (ops_txt(o, ["actC R_n(pi/2)"]), ops_txt(o, ["actT R_n(pi/2)"])))
    r1C, r1T = o["actC R1"][0], o["actT R1"][0]
    v["I3.152"] = ("FAILS" if (r1C == "MOVED" and r1T == "MOVED") else
                   ("SATISFIED (%s reading)" % " and ".join(t for t, x in (("control", r1C), ("target", r1T))
                                                         if x == "INVARIANT") if "INVARIANT" in (r1C, r1T)
                    else "UNDECIDED"),
                   "control — %s | target — %s" % (ops_txt(o, ["actC R1"]), ops_txt(o, ["actT R1"])))
    v["I3.153"] = ("FAILS" if (tokfail(dj, "C") and tokfail(dj, "T")) else
                   ("FAILS on one token" if (tokfail(dj, "C") or tokfail(dj, "T")) else "not refuted by the list"),
                   "control — %s | target — %s" % (ops_txt(o, ["actC " + n for n in dj]),
                                                  ops_txt(o, ["actT " + n for n in dj])))
    v["I3.155"] = (v["I3.137"][0], "FC ⟺ IE1 given hgate (R6 I3.155 evidence; hgate: cnot %s)" % o["cnot"][0])
    v["I3.165"] = ("FAILS" if (anyC or anyT) else "not refuted by the list", "some local map moves K" if (anyC or anyT) else "")
    v["I3.144"] = ("FAILS" if (R["qh"] < 0 and R["twin"]) else "UNDECIDED",
                   "P_h in Q3 \\ K (1 - c = %s); %s in K \\ twin" % (R["qh"], R["ybell"][0] if R["ybell"] else None))
    fc = R["fcc"]
    v["I3.135"] = ("FAILS" if (fc and fc["fI"] < 0) else "UNDECIDED", "famI = %s at (d_h, P_y, P_psi, P_chi)" % (
        fc["fI"] if fc else None))
    v["I3.133"] = (v["I3.135"][0], "via I3.140 (KT4Core ⇒ FCC, [D]) and I3.135")
    v["I3.160"] = ("FAILS" if R["qh"] < 0 else "UNDECIDED", "homogeneity ⇒ Q3 (stage 4 Y6 [W + L]); K ≠ Q3")
    v["I3.161"] = ("FAILS", ("C3.3/C11.7 (finitely many non-PSD extreme rays: c = 15 on defects), c(P00) = 9 (C3.2); "
                             "T-support %s" % R["tsup"]) if tag != "Kk" else "C16.5 (c = 14 on defects), c(P00) = 9 (C3.2)")
    lev2 = all(inv(o, n) for n in ["cnot", "actC R_z(pi)", "actT R_z(pi)", "transposeW"])
    lev2_mov = [n for n in ["cnot", "actC R_z(pi)", "actT R_z(pi)", "transposeW"] if not inv(o, n)]
    R["lev2"], R["lev2_mov"] = lev2, lev2_mov
    ROW_TABLES[tag] = v

    # the 199 rows
    cone_ok = R["dat"]["h1"] and R["dat"]["cc"] and inv(o, "cnot")
    tally = {"SATISFIES": 0, "NOT REACHED": 0, "FAILS": 0, "other": 0}
    changed = []
    for r in A2:
        cls = r["cls"]
        if cls in KINDEP_S:
            verdict = "SATISFIES"
        elif cls in NR:
            verdict = "NOT REACHED"
        elif cls == "cone":
            verdict = "SATISFIES" if cone_ok else "UNDECIDED"
            if r["id"] == "I3.148" and not lev2:
                changed.append((r["id"], "SATISFIES at level (i); level (ii) FAILS (moved by %s)" % ", ".join(lev2_mov)))
        elif cls == "kthm":
            verdict = "SATISFIES" if (d3 and inv(o, "cnot")) else "UNDECIDED"
        elif cls == "b1":
            verdict = "SATISFIES" if cone_ok else "UNDECIDED"
        elif cls == "d4v":
            hyp = "I3.137" if r["id"] == "I3.187" else "I3.133"
            verdict = "SATISFIES" if v[hyp][0] == "FAILS" else "UNDECIDED"
        else:
            verdict = v[r["id"]][0]
        key = verdict if verdict in tally else "other"
        tally[key] += 1
        a2v = r["verdict"].split(" [")[0].split(" (")[0]
        if verdict != a2v:
            changed.append((r["id"], "%s -> %s" % (a2v, verdict)))
    R["tally"], R["changed"] = tally, changed
    print("ROWS %-5s %s; differences from Table A2: %s" % (tag, tally, changed if changed else "none"))

# ---------------------------------------------------------------- the tables (markdown, for NOTES-C21)
ORDER13 = ["I3.137", "I3.142", "I3.150", "I3.151", "I3.152", "I3.153", "I3.155", "I3.165",
           "I3.144", "I3.133", "I3.135", "I3.160", "I3.161"]
BROWS = set(ORDER13[:8])
ID2 = {r["id"]: r for r in A2}
for tag, _ in CONES:
    v = ROW_TABLES[tag]
    R = RESULTS[tag]
    print("TABLE %s" % tag)
    print("| item | (b)-instances: invariance under …, satisfied/failed, by operation | Q3-level rows: satisfied/failed |"
          " Table A2 (K(Z_F)) → this cone |")
    print("|---|---|---|---|")
    for rid in ORDER13:
        st = ID2[rid]["stmt"].split(" — ")[0]
        if rid in BROWS:
            q3 = ("K ≠ Q3 (entailed: a local unitary moves K; never the converse)"
                  if v[rid][0].startswith("FAILS") and rid not in ("I3.155",) else "—")
            print("| %s %s | %s | %s | FAILS → %s |" % (rid, st, v[rid][1], q3, v[rid][0]))
        else:
            print("| %s %s | — | %s: %s | FAILS → %s |" % (rid, st, "failed" if v[rid][0] == "FAILS" else v[rid][0],
                                                           v[rid][1], v[rid][0]))
    lv = "level (ii): satisfied" if R["lev2"] else "level (ii): failed (moved by %s)" % ", ".join(R["lev2_mov"])
    print("| I3.148 H2 | cnot: %s; %s | — | SATISFIES → %s |" % (
        R["ops"]["cnot"][0].lower(), lv, "SATISFIES" if R["lev2"] else "SATISFIES at level (i) only"))
    print("TWO-TOKEN %s: cnot %s, SWAP %s, transposeW %s" % (tag, R["ops"]["cnot"][0], R["ops"]["SWAP"][0],
                                                            R["ops"]["transposeW"][0]))

NRIDS = [r["id"] for r in A2 if r["cls"] in NR]
print("NOT-REACHED (%d, as in Table A2 for every cone; no theorem at L transfers one): %s" % (len(NRIDS), " ".join(NRIDS)))
KDEPS = [r["id"] for r in A2 if r["cls"] in KDEP_S]
print("K-DEPENDENT SATISFIES (%d): %s" % (len(KDEPS), " ".join(KDEPS)))

bad = [c for c, ok in RES if not ok]
print("CHECKS %d/%d" % (len(RES) - len(bad), len(RES)))
if not bad:
    print("VERDICT C21-EXACT")
else:
    print("NO VERDICT (failed: %s)" % ", ".join(bad))
