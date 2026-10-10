"""eqclib -- exact helpers for thread EQ-C (two Bloch balls on DIM-1's carrier W 3 = R^4 (x) R^4).

Conventions (match CompositeDimension.lean at bcbc516f):
  * a joint vector w in W 3 is a 4x4 array w[mu][nu]; mu = control (copy A) index, nu = target (copy B)
    index; index 0 is the unit, 1,2,3 are Bloch x,y,z  (hom x = vecCons 1 x, CD:100).
  * vec(w)[4*mu+nu] = w[mu][nu].  A linear map of W 3 is a 16x16 matrix acting on vec.
  * prodState x y = hom x (x) hom y (CD:161); pairVal a b w = a^T w b (CD:164).
  * actC N acts on the control index, actT N on the target index (CD:198, CD:201), via homMap N
    (unit coordinate fixed, CD:112).
  * The Pauli dictionary (matrix model, layer [M]): w_{mu nu} = Tr((s_mu (x) s_nu) rho).

Everything is exact: Fractions, and Gaussian rationals as pairs of Fractions. No floats.
"""
from fractions import Fraction as Fr
import itertools

N4 = 4
IDX = [(m, n) for m in range(4) for n in range(4)]


def F(x):
    return x if isinstance(x, Fr) else Fr(x)


# ---------------------------------------------------------------- dense exact linear algebra
def zeros(r, c):
    return [[Fr(0)] * c for _ in range(r)]


def eye(n):
    M = zeros(n, n)
    for i in range(n):
        M[i][i] = Fr(1)
    return M


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    return [[sum((A[i][t] * Bt[j][t] for t in range(k) if A[i][t] != 0), Fr(0)) for j in range(m)]
            for i in range(n)]


def matvec(A, v):
    return [sum((A[i][t] * v[t] for t in range(len(v)) if A[i][t] != 0 and v[t] != 0), Fr(0))
            for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def madd(A, B, a=1, b=1):
    a, b = F(a), F(b)
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(A, c):
    c = F(c)
    return [[c * x for x in row] for row in A]


def bracket(X, Y):
    return madd(matmul(X, Y), matmul(Y, X), 1, -1)


def is_zero(A):
    return all(x == 0 for row in A for x in row)


def flat(A):
    return [x for row in A for x in row]


def rref(rows, ncols):
    """Exact reduced row echelon form over Q. Returns (pivot_cols, reduced_rows)."""
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


def rank(rows, ncols):
    return len(rref(rows, ncols)[0])


class IncRank:
    """Incremental exact row space (echelon basis) over Q, for growing constraint systems."""

    def __init__(self, ncols):
        self.n = ncols
        self.basis = {}  # pivot col -> row (normalized, pivot 1, reduced against earlier pivots partially)

    def reduce(self, v):
        v = list(map(F, v))
        for c in sorted(self.basis):
            if v[c] != 0:
                f = v[c]
                b = self.basis[c]
                v = [a - f * x for a, x in zip(v, b)]
        return v

    def add(self, v):
        v = self.reduce(v)
        for c in range(self.n):
            if v[c] != 0:
                inv = 1 / v[c]
                v = [x * inv for x in v]
                # keep basis reduced w.r.t. new pivot
                for c2 in list(self.basis):
                    b = self.basis[c2]
                    if b[c] != 0:
                        f = b[c]
                        self.basis[c2] = [a - f * x for a, x in zip(b, v)]
                self.basis[c] = v
                return True
        return False

    @property
    def rank(self):
        return len(self.basis)

    def nullspace(self):
        """Basis of {x : row . x = 0 for all rows} (exact)."""
        piv = sorted(self.basis)
        free = [c for c in range(self.n) if c not in self.basis]
        out = []
        for f in free:
            x = [Fr(0)] * self.n
            x[f] = Fr(1)
            for p in piv:
                x[p] = -self.basis[p][f]
            out.append(x)
        return out


def span_rank(vectors):
    if not vectors:
        return 0
    return rank(vectors, len(vectors[0]))


def in_span(vectors, v):
    return span_rank(vectors + [v]) == span_rank(vectors)


# ---------------------------------------------------------------- Gaussian rationals and Paulis
class G:
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = F(re), F(im)

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

    def __eq__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s.re == o.re and s.im == o.im

    def __hash__(s):
        return hash((s.re, s.im))

    def __repr__(s):
        return f"({s.re}+{s.im}i)"


I_ = G(0, 1)


def cmat(rows):
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
                if (a.re != 0 or a.im != 0) and (b.re != 0 or b.im != 0):
                    s = s + a * b
            row.append(s)
        out.append(row)
    return out


def cadd(A, B, a=1, b=1):
    a = a if isinstance(a, G) else G(a)
    b = b if isinstance(b, G) else G(b)
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def ctrace(A):
    s = G(0)
    for i in range(len(A)):
        s = s + A[i][i]
    return s


def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def cdag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


SIG = [cmat([[1, 0], [0, 1]]), cmat([[0, 1], [1, 0]]), [[G(0), G(0, -1)], [G(0, 1), G(0)]],
       cmat([[1, 0], [0, -1]])]
SIG2 = {(m, n): kron(SIG[m], SIG[n]) for m in range(4) for n in range(4)}


def rho_of_w(w):
    """Inverse dictionary: rho = (1/4) sum w_{mu nu} s_mu (x) s_nu  (layer [M])."""
    R = [[G(0)] * 4 for _ in range(4)]
    for (m, n) in IDX:
        if w[m][n] != 0:
            R = cadd(R, SIG2[(m, n)], 1, G(w[m][n] / 4))
    return R


def w_of_rho(R):
    """Dictionary: w_{mu nu} = Re Tr((s_mu (x) s_nu) rho)  (layer [M]); asserts the imaginary part is 0."""
    w = [[Fr(0)] * 4 for _ in range(4)]
    for (m, n) in IDX:
        t = ctrace(cmul(SIG2[(m, n)], R))
        assert t.im == 0, "dictionary produced a non-real coordinate"
        w[m][n] = t.re
    return w


def superop_matrix(f):
    """16x16 real matrix of a real-linear map f: W3 -> W3 given on 4x4 arrays."""
    M = zeros(16, 16)
    for c, (k, l) in enumerate(IDX):
        e = [[Fr(0)] * 4 for _ in range(4)]
        e[k][l] = Fr(1)
        out = f(e)
        for r, (m, n) in enumerate(IDX):
            M[r][c] = F(out[m][n])
    return M


def ad_herm(H):
    """W-coordinate matrix of rho -> -i[H, rho] for a Hermitian 4x4 H (layer [M])."""
    def f(w):
        R = rho_of_w(w)
        C = cadd(cmul(H, R), cmul(R, H), 1, -1)
        C = [[G(0, -1) * x for x in row] for row in C]
        return w_of_rho(C)
    return superop_matrix(f)


def conj_unitary(U):
    """W-coordinate matrix of rho -> U rho U^dagger (layer [M])."""
    Ud = cdag(U)

    def f(w):
        return w_of_rho(cmul(cmul(U, rho_of_w(w)), Ud))
    return superop_matrix(f)


# ---------------------------------------------------------------- kernel-literal objects on W 3
def homMap(N):
    """4x4 homogenized matrix of a 3x3 linear map N (unit coordinate fixed), CD:112."""
    H = zeros(4, 4)
    H[0][0] = Fr(1)
    for i in range(3):
        for j in range(3):
            H[i + 1][j + 1] = F(N[i][j])
    return H


def actT_mat(N):
    """16x16 matrix of actT N (CD:198): (actT N w)[mu] = homMap N (w[mu])."""
    H = homMap(N)
    M = zeros(16, 16)
    for (m, n) in IDX:
        for l in range(4):
            if H[n][l] != 0:
                M[4 * m + n][4 * m + l] = H[n][l]
    return M


def actC_mat(N):
    """16x16 matrix of actC N (CD:201): acts on the control index."""
    H = homMap(N)
    M = zeros(16, 16)
    for (m, n) in IDX:
        for k in range(4):
            if H[m][k] != 0:
                M[4 * m + n][4 * k + n] = H[m][k]
    return M


def diag3(a, b, c):
    return [[F(a), 0, 0], [0, F(b), 0], [0, 0, F(c)]]


NFLIP = diag3(1, -1, -1)      # CompositeDimension.nflip (CD:797)
REFLY = diag3(1, -1, 1)       # K2Guard.reflY (K2G:46)
MINUS = diag3(-1, -1, -1)     # point reflection
RYPI = diag3(-1, 1, -1)       # rotation by pi about y

SWAP16 = zeros(16, 16)
for (m, n) in IDX:
    SWAP16[4 * n + m][4 * m + n] = Fr(1)


def vec(w):
    return [F(w[m][n]) for (m, n) in IDX]


def unvec(v):
    return [[v[4 * m + n] for n in range(4)] for m in range(4)]


def hom(x):
    return [Fr(1)] + [F(t) for t in x]


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in range(4)] for m in range(4)]


def pairVal(a, b, w):
    return sum((F(a[m]) * w[m][n] * F(b[n]) for m in range(4) for n in range(4)), Fr(0))


def unit_vector(s, t):
    """Rational point of S^2 by inverse stereographic projection."""
    s, t = F(s), F(t)
    d = 1 + s * s + t * t
    return [2 * s / d, 2 * t / d, (s * s + t * t - 1) / d]


def apply(M, w):
    return unvec(matvec(M, vec(w)))


# ---------------------------------------------------------------- the kernel cnot (parsed, not transcribed)
def parse_kernel_cnot(path):
    """Parse the pc, pt, sgn tables of CompositeDimension.cnot (CD:741-760) from the Lean source and
    return the 16x16 matrix of cnotFun w mu nu = sgn mu nu * w (pc mu nu) (pt mu nu)."""
    import re
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
        s = Fr(-1) if (m, n) in neg else Fr(1)
        M[4 * m + n][4 * pc[(m, n)] + pt[(m, n)]] = s
    return M, pc, pt, neg


def det_frac(M):
    """Exact determinant by fraction Gaussian elimination."""
    A = [list(map(F, r)) for r in M]
    n = len(A)
    d = Fr(1)
    for c in range(n):
        p = None
        for r in range(c, n):
            if A[r][c] != 0:
                p = r
                break
        if p is None:
            return Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        inv = 1 / A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] * inv
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return d


class Report:
    """Check accumulator: a verdict line is printed only when every check passed."""

    def __init__(self, name):
        self.name = name
        self.n = 0
        self.fail = 0

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
        if self.fail == 0:
            print(f"VERDICT {text}")
        else:
            print("VERDICT NOT RENDERED (a check failed)")


# ---------------------------------------------------------------- Gaussian-rational rank and Choi matrices
def ginv(z):
    n = z.re * z.re + z.im * z.im
    assert n != 0
    return G(z.re / n, -z.im / n)


def gnonzero(z):
    return z.re != 0 or z.im != 0


def crank(M):
    """Exact rank of a matrix over Q(i)."""
    A = [[x if isinstance(x, G) else G(x) for x in row] for row in M]
    rows, cols = len(A), len(A[0])
    r = 0
    for c in range(cols):
        p = None
        for i in range(r, rows):
            if gnonzero(A[i][c]):
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = ginv(A[r][c])
        A[r] = [x * inv for x in A[r]]
        for i in range(rows):
            if i != r and gnonzero(A[i][c]):
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
        if r == rows:
            break
    return r


def superop_on_herm(g16):
    """The dictionary transport of a W-map g: Herm(4) -> Herm(4), H -> rho(g w(H))  (layer [M])."""
    def f(H):
        return rho_of_w(unvec(matvec(g16, vec(w_of_rho(H)))))
    return f


def choi(g16):
    """Choi matrix sum_ij E_ij (x) Phi(E_ij) of the C-linear extension of the dictionary transport of g."""
    Phi = superop_on_herm(g16)
    C = [[G(0)] * 16 for _ in range(16)]
    for i in range(4):
        for j in range(4):
            E = [[G(0)] * 4 for _ in range(4)]
            Et = [[G(0)] * 4 for _ in range(4)]
            E[i][j] = G(1)
            Et[j][i] = G(1)
            H1 = [[(E[a][b] + Et[a][b]) * G(Fr(1, 2)) for b in range(4)] for a in range(4)]
            H2 = [[(E[a][b] - Et[a][b]) * G(0, Fr(-1, 2)) for b in range(4)] for a in range(4)]  # (E - E^T)/(2i)
            P1, P2 = Phi(H1), Phi(H2)
            PE = [[P1[a][b] + G(0, 1) * P2[a][b] for b in range(4)] for a in range(4)]
            for a in range(4):
                for b in range(4):
                    C[4 * i + a][4 * j + b] = PE[a][b]
    return C
