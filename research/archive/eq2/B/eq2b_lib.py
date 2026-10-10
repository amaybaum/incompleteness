"""eq2b_lib -- exact helpers for thread EQ2-B (Theorem A', two Bloch balls on DIM-1's carrier W 3).

Conventions (CompositeDimension.lean at bcbc516f):
  * W 3 = Fin 4 -> Fin 4 -> R; w[mu][nu], mu = control (copy A), nu = target (copy B); index 0 is the unit and
    1, 2, 3 are the Bloch coordinates x, y, z (hom x = vecCons 1 x, CD:100).
  * vec(w)[4*mu + nu] = w[mu][nu]; a linear map of W 3 is a 16x16 matrix acting on vec.
  * prodState x y = hom x (x) hom y (CD:161); pairVal a b w = sum a_mu w_{mu nu} b_nu (CD:164).
  * actT N acts on the target index and actC N on the control index through homMap N (CD:198, CD:201, CD:112).
  * The Pauli dictionary (matrix model, evidence about QM only): w_{mu nu} = Tr((s_mu (x) s_nu) rho).
Everything is exact: Fractions and Gaussian rationals. No floating point anywhere.
"""
from fractions import Fraction as Fr
import re

IDX = [(m, n) for m in range(4) for n in range(4)]


def F(x):
    return x if isinstance(x, Fr) else Fr(x)


# ------------------------------------------------------------------ dense exact linear algebra over Q
def zeros(r, c):
    return [[Fr(0)] * c for _ in range(r)]


def eye(n):
    M = zeros(n, n)
    for i in range(n):
        M[i][i] = Fr(1)
    return M


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    out = []
    for i in range(n):
        Ai = A[i]
        nz = [t for t in range(k) if Ai[t] != 0]
        out.append([sum((Ai[t] * Bt[j][t] for t in nz), Fr(0)) for j in range(m)])
    return out


def mvec(A, v):
    return [sum((A[i][t] * v[t] for t in range(len(v)) if A[i][t] != 0 and v[t] != 0), Fr(0))
            for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def madd(A, B, a=1, b=1):
    a, b = F(a), F(b)
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(A, c):
    c = F(c)
    return [[c * x for x in r] for r in A]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def is_zero(A):
    return all(x == 0 for r in A for x in r)


def flat(A):
    return [x for r in A for x in r]


def bracket(X, Y):
    return madd(mmul(X, Y), mmul(Y, X), 1, -1)


def rref(rows, ncols):
    """Exact reduced row echelon form over Q: (pivot columns, reduced nonzero rows)."""
    M = [list(map(F, r)) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = 1 / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return piv, M[:r]


def rank(rows, ncols=None):
    if not rows:
        return 0
    return len(rref(rows, ncols if ncols is not None else len(rows[0]))[0])


def nullspace(rows, ncols):
    """Exact basis of {x : r . x = 0 for every row r}."""
    piv, R = rref(rows, ncols) if rows else ([], [])
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for f in free:
        x = [Fr(0)] * ncols
        x[f] = Fr(1)
        for k, p in enumerate(piv):
            x[p] = -R[k][f]
        out.append(x)
    return out


def minv(A):
    """Exact inverse by Gauss-Jordan; raises if singular."""
    n = len(A)
    M = [list(map(F, A[i])) + [Fr(1) if j == i else Fr(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next((i for i in range(c, n) if M[i][c] != 0), None)
        if p is None:
            raise ValueError("singular")
        M[c], M[p] = M[p], M[c]
        inv = 1 / M[c][c]
        M[c] = [x * inv for x in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[c])]
    return [r[n:] for r in M]


def det(A):
    M = [list(map(F, r)) for r in A]
    n = len(M)
    d = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            if M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return d


# ------------------------------------------------------------------ W 3 objects (kernel-literal)
def vec(w):
    return [F(w[m][n]) for (m, n) in IDX]


def unvec(v):
    return [[v[4 * m + n] for n in range(4)] for m in range(4)]


def apply(M, w):
    return unvec(mvec(M, vec(w)))


def hom(x):
    return [Fr(1)] + [F(t) for t in x]


def lift(x):
    return [Fr(0)] + [F(t) for t in x]


def tens(X, Y):
    return [[F(X[m]) * F(Y[n]) for n in range(4)] for m in range(4)]


def prodState(x, y):
    return tens(hom(x), hom(y))


def pairVal(a, b, w):
    return sum((F(a[m]) * w[m][n] * F(b[n]) for m in range(4) for n in range(4)), Fr(0))


def lor(v):
    """Kernel Lor (CD:869): 0 <= v0 and |v_vec|^2 <= v0^2."""
    return v[0] >= 0 and sum(t * t for t in v[1:]) <= v[0] * v[0]


def homMap(N):
    H = zeros(4, 4)
    H[0][0] = Fr(1)
    for i in range(3):
        for j in range(3):
            H[i + 1][j + 1] = F(N[i][j])
    return H


def actT(N):
    H = homMap(N)
    M = zeros(16, 16)
    for (m, n) in IDX:
        for l in range(4):
            if H[n][l] != 0:
                M[4 * m + n][4 * m + l] = H[n][l]
    return M


def actC(N):
    H = homMap(N)
    M = zeros(16, 16)
    for (m, n) in IDX:
        for k in range(4):
            if H[m][k] != 0:
                M[4 * m + n][4 * k + n] = H[m][k]
    return M


def onT(H4):
    """16x16 matrix of w -> (w[mu] mapped by an arbitrary 4x4 H4 on the target index)."""
    M = zeros(16, 16)
    for (m, n) in IDX:
        for l in range(4):
            if H4[n][l] != 0:
                M[4 * m + n][4 * m + l] = F(H4[n][l])
    return M


def onC(H4):
    M = zeros(16, 16)
    for (m, n) in IDX:
        for k in range(4):
            if H4[m][k] != 0:
                M[4 * m + n][4 * k + n] = F(H4[m][k])
    return M


def diag3(a, b, c):
    return [[F(a), Fr(0), Fr(0)], [Fr(0), F(b), Fr(0)], [Fr(0), Fr(0), F(c)]]


NFLIP = diag3(1, -1, -1)     # CompositeDimension.nflip (CD:797): pi-rotation about Bloch x
REFLY = diag3(1, -1, 1)      # K2Guard.reflY (K2G:46)
Z3 = [Fr(0), Fr(0), Fr(1)]   # CompositeDimension.z3
I3 = diag3(1, 1, 1)
I16 = eye(16)
RA = actC(REFLY)             # one-copy reflection of the control (partial transpose on A in the dictionary)
RB = actT(REFLY)             # one-copy reflection of the target (partial transpose on B)
TT = mmul(RA, RB)            # global transpose

SWAP16 = zeros(16, 16)
for (_m, _n) in IDX:
    SWAP16[4 * _n + _m][4 * _m + _n] = Fr(1)


def rot_from_quat(q):
    """Rational rotation matrix R(q) (det +1) of a nonzero rational quaternion q = (q0, q1, q2, q3)."""
    a, b, c, d = map(F, q)
    n = a * a + b * b + c * c + d * d
    R = [[a * a + b * b - c * c - d * d, 2 * (b * c - a * d), 2 * (b * d + a * c)],
         [2 * (b * c + a * d), a * a - b * b + c * c - d * d, 2 * (c * d - a * b)],
         [2 * (b * d - a * c), 2 * (c * d + a * b), a * a - b * b - c * c + d * d]]
    return [[x / n for x in r] for r in R]


def rot_axis(axis, c, s):
    """Rotation by the angle with cos = c, sin = s about Bloch axis 0 (x), 1 (y) or 2 (z)."""
    c, s = F(c), F(s)
    R = diag3(1, 1, 1)
    i, j = [(1, 2), (2, 0), (0, 1)][axis]
    R[i][i], R[i][j], R[j][i], R[j][j] = c, -s, s, c
    return R


def m3mul(A, B):
    return [[sum(F(A[i][k]) * F(B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]


def m3det(A):
    return det(A)


# ------------------------------------------------------------------ the kernel cnot, parsed from the base source
def parse_kernel_cnot(path):
    """Parse the tables pc, pt, sgn of CompositeDimension.cnot (CD:741-760) and return the 16x16 matrix of
    cnotFun w mu nu = sgn mu nu * w (pc mu nu) (pt mu nu), together with the parsed tables."""
    src = open(path, encoding="utf-8").read()

    def table(name):
        i = src.index(f"def {name} : Fin 4 → Fin 4 → Fin 4")
        j = src.index("\n\n", i)
        ent = re.findall(r"\|\s*(\d)\s*,\s*(\d)\s*=>\s*(\d)", src[i:j])
        assert len(ent) == 16, (name, len(ent))
        return {(int(a), int(b)): int(c) for a, b, c in ent}

    pc, pt = table("pc"), table("pt")
    i = src.index("def sgn (μ ν : Fin 4) : ℝ :=")
    line = src[i: src.index("\n", i)]
    neg = {(int(a), int(b)) for a, b in re.findall(r"μ = (\d) ∧ ν = (\d)", line)}
    assert "then -1 else 1" in line and len(neg) == 2, line
    M = zeros(16, 16)
    for (m, n) in IDX:
        M[4 * m + n][4 * pc[(m, n)] + pt[(m, n)]] = Fr(-1) if (m, n) in neg else Fr(1)
    return M, pc, pt, neg


# ------------------------------------------------------------------ Gaussian rationals and the Pauli dictionary
class G:
    __slots__ = ("re", "im")

    def __init__(self, re_, im_=0):
        self.re, self.im = F(re_), F(im_)

    def __add__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.re + o.re, s.im + o.im)

    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.re - o.re, s.im - o.im)

    def __rsub__(s, o):
        return G(o) - s

    def __mul__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)

    __rmul__ = __mul__

    def __neg__(s):
        return G(-s.re, -s.im)

    def conj(s):
        return G(s.re, -s.im)

    def __truediv__(s, o):
        o = o if isinstance(o, G) else G(o)
        n = o.re * o.re + o.im * o.im
        return s * G(o.re / n, -o.im / n)

    def __eq__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s.re == o.re and s.im == o.im

    def __hash__(s):
        return hash((s.re, s.im))

    def nz(s):
        return s.re != 0 or s.im != 0

    def __repr__(s):
        return f"({s.re}+{s.im}i)"


def cm(rows):
    return [[x if isinstance(x, G) else G(x) for x in r] for r in rows]


def cmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            s = G(0)
            for t in range(k):
                a, b = A[i][t], B[t][j]
                if a.nz() and b.nz():
                    s = s + a * b
            row.append(s)
        out.append(row)
    return out


def cadd(A, B, a=1, b=1):
    a = a if isinstance(a, G) else G(a)
    b = b if isinstance(b, G) else G(b)
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def cdag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def ctrace(A):
    s = G(0)
    for i in range(len(A)):
        s = s + A[i][i]
    return s


def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def cdet(A):
    M = [list(r) for r in A]
    n = len(M)
    d = G(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c].nz()), None)
        if p is None:
            return G(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d = d * M[c][c]
        for r in range(c + 1, n):
            if M[r][c].nz():
                f = M[r][c] / M[c][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return d


def is_psd_herm(R):
    """Exact PSD test of a Hermitian matrix over Q(i): every principal minor is >= 0 (and real)."""
    import itertools
    n = len(R)
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            d = cdet([[R[i][j] for j in S] for i in S])
            if d.im != 0 or d.re < 0:
                return False
    return True


SIG = [cm([[1, 0], [0, 1]]), cm([[0, 1], [1, 0]]), [[G(0), G(0, -1)], [G(0, 1), G(0)]], cm([[1, 0], [0, -1]])]
SIG2 = {(m, n): kron(SIG[m], SIG[n]) for m in range(4) for n in range(4)}


def rho_of_w(w):
    R = [[G(0)] * 4 for _ in range(4)]
    for (m, n) in IDX:
        if w[m][n] != 0:
            R = cadd(R, SIG2[(m, n)], 1, G(F(w[m][n]) / 4))
    return R


def w_of_rho(R):
    w = [[Fr(0)] * 4 for _ in range(4)]
    for (m, n) in IDX:
        t = ctrace(cmul(SIG2[(m, n)], R))
        assert t.im == 0, "non-real coordinate"
        w[m][n] = t.re
    return w


def superop(f):
    """16x16 matrix of a real-linear map f on 4x4 arrays w."""
    M = zeros(16, 16)
    for c, (k, l) in enumerate(IDX):
        e = [[Fr(0)] * 4 for _ in range(4)]
        e[k][l] = Fr(1)
        out = f(e)
        for r, (m, n) in enumerate(IDX):
            M[r][c] = F(out[m][n])
    return M


def conj_map(U, scale=1):
    """W-coordinate matrix of rho -> scale * U rho U^dagger (layer [M])."""
    Ud = cdag(U)
    sc = G(F(scale))

    def f(w):
        X = cmul(cmul(U, rho_of_w(w)), Ud)
        return w_of_rho([[sc * x for x in r] for r in X])
    return superop(f)


def transpose_map():
    """W-coordinate matrix of rho -> rho^T."""
    def f(w):
        R = rho_of_w(w)
        return w_of_rho([[R[j][i] for j in range(4)] for i in range(4)])
    return superop(f)


def ad_herm(H):
    """W-coordinate matrix of rho -> -i[H, rho] (generator of Ad exp(-itH))."""
    def f(w):
        R = rho_of_w(w)
        C = cadd(cmul(H, R), cmul(R, H), 1, -1)
        return w_of_rho([[G(0, -1) * x for x in r] for r in C])
    return superop(f)


def su2_of_quat(q):
    """Unnormalized SU(2) lift q0 I - i (q1 X + q2 Y + q3 Z); U U^dag = |q|^2 I."""
    a, b, c, d = map(F, q)
    return cadd(cadd(cadd(cm([[a, 0], [0, a]]), SIG[1], 1, G(0, -b)), SIG[2], 1, G(0, -c)), SIG[3], 1, G(0, -d))


def qnorm2(q):
    return sum(F(t) * F(t) for t in q)


CNOT_U = cm([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])   # control = copy A (first factor)
I2 = cm([[1, 0], [0, 1]])


class Report:
    """Check accumulator: the verdict line is printed only when every check passed (rule R7)."""

    def __init__(self, name):
        self.name, self.n, self.fail = name, 0, 0

    def check(self, label, cond, detail=""):
        self.n += 1
        ok = bool(cond)
        if not ok:
            self.fail += 1
        print(f"{'PASS' if ok else 'FAIL'} {label}" + (f"  [{detail}]" if detail else ""))
        return ok

    def note(self, s):
        print(f"NOTE {s}")

    def verdict(self, text):
        print(f"--- {self.name}: {self.n} checks, {self.fail} failures")
        print(f"VERDICT {text}" if self.fail == 0 else "VERDICT NOT RENDERED (a check failed)")
