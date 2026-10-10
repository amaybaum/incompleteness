"""EQ4-P own exact library (research only; base bcbc516f).  Imports nothing from scratchpad/eq3/ or eqreview/.

Arithmetic: Gaussian rationals `G` (pairs of fractions.Fraction).  No floating point anywhere: every constructor
rejects float input.

Operators: `Op(qs, d)` is an operator on the ordered tuple `qs` of qubit labels (tokens).  Basis index r of an
operator on qs = (q_0, ..., q_{n-1}) has bit (n - 1 - i) equal to the value of qubit q_i (q_0 is the most
significant bit).  `d` maps (row, col) -> G and stores nonzero entries only.

Conventions (fixed here, used by every script):
  * Pairing of an effect operator E with a state operator X on the same token set: tr(E X) = sum_{r,c} E[r,c] X[c,r].
  * Conditional state: cond(e, X) = tr_A[(e_A (x) 1) X] for an effect e on a subset A of X's tokens; it is the
    operator on the remaining tokens (in X's order) with cond[b, b'] = sum_{a,a'} e[a, a'] X[(a', b), (a, b')].
  * Link map of a state x on P u R read from R to P:  Lam(x, R)(g) = tr_R[(g_R (x) 1_P) x]  (= cond(g, x)).
    Its Choi matrix sum_ij |i><j|_R (x) Lam(|i><j|) is PT_R(x)  (checked in the scripts, not assumed).
  * Pauli dictionary: s0 = 1, s1 = X, s2 = Y, s3 = Z; state table of a pair operator rho:
    coords(rho)[m][n] = tr(rho (s_m (x) s_n)); one-qubit coords1(rho)[m] = tr(rho s_m).
"""
import itertools
import re
from fractions import Fraction as Fr


# ---------------------------------------------------------------------------------------------- Gaussian rationals
class G:
    __slots__ = ("re", "im")

    def __init__(self, re_=0, im_=0):
        if isinstance(re_, float) or isinstance(im_, float):
            raise TypeError("float input refused (exact arithmetic only)")
        if isinstance(re_, G):
            self.re, self.im = re_.re, re_.im
            return
        self.re = Fr(re_)
        self.im = Fr(im_)

    @staticmethod
    def of(v):
        if isinstance(v, G):
            return v
        if isinstance(v, float):
            raise TypeError("float input refused (exact arithmetic only)")
        return G(v, 0)

    def __add__(self, o):
        o = G.of(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = G.of(o)
        return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return G.of(o) - self

    def __neg__(self):
        return G(-self.re, -self.im)

    def __mul__(self, o):
        o = G.of(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = G.of(o)
        n = o.re * o.re + o.im * o.im
        if n == 0:
            raise ZeroDivisionError
        return self * G(o.re / n, -o.im / n)

    def conj(self):
        return G(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def is_zero(self):
        return self.re == 0 and self.im == 0

    def __eq__(self, o):
        o = G.of(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        if self.im == 0:
            return str(self.re)
        return "(%s%+s*i)" % (self.re, self.im) if self.re != 0 else "%s*i" % self.im


ZERO, ONE, I_ = G(0), G(1), G(0, 1)


# ---------------------------------------------------------------------------------------------- operators
class Op:
    __slots__ = ("qs", "d")

    def __init__(self, qs, d):
        self.qs = tuple(qs)
        if len(set(self.qs)) != len(self.qs):
            raise ValueError("repeated qubit label")
        self.d = {k: v for k, v in d.items() if not v.is_zero()}

    @property
    def n(self):
        return len(self.qs)

    def get(self, r, c):
        return self.d.get((r, c), ZERO)

    def __add__(self, o):
        o = reorder(o, self.qs)
        out = dict(self.d)
        for k, v in o.d.items():
            out[k] = out.get(k, ZERO) + v
        return Op(self.qs, out)

    def __sub__(self, o):
        return self + o.scale(-1)

    def scale(self, s):
        s = G.of(s)
        return Op(self.qs, {k: v * s for k, v in self.d.items()})

    def __eq__(self, o):
        if set(self.qs) != set(o.qs):
            return False
        o = reorder(o, self.qs)
        return self.d.keys() == o.d.keys() and all(self.d[k] == o.d[k] for k in self.d)

    def is_zero(self):
        return not self.d

    def dense(self):
        N = 2 ** self.n
        return [[self.get(r, c) for c in range(N)] for r in range(N)]


def op(M, qs):
    """Operator from a square nested list of exact numbers (int, Fraction or G)."""
    N = 2 ** len(qs)
    if len(M) != N or any(len(row) != N for row in M):
        raise ValueError("shape")
    return Op(qs, {(r, c): G.of(M[r][c]) for r in range(N) for c in range(N) if not G.of(M[r][c]).is_zero()})


def ket_op(vec, qs, bra=None):
    """|vec><bra| (bra defaults to vec) for exact coefficient lists of length 2^n."""
    bra = vec if bra is None else bra
    v = [G.of(a) for a in vec]
    w = [G.of(a).conj() for a in bra]
    return Op(qs, {(r, c): v[r] * w[c] for r in range(len(v)) for c in range(len(w))
                   if not (v[r] * w[c]).is_zero()})


def identity(qs):
    return Op(qs, {(r, r): ONE for r in range(2 ** len(qs))})


def unit(qs, r, c):
    return Op(qs, {(r, c): ONE})


def units(qs):
    N = 2 ** len(qs)
    for r in range(N):
        for c in range(N):
            yield (r, c), unit(qs, r, c)


def _perm_index(old_qs, new_qs):
    """table t with t[i_old] = i_new for basis indices."""
    n = len(old_qs)
    pos_new = {q: k for k, q in enumerate(new_qs)}
    t = []
    for i in range(2 ** n):
        j = 0
        for k, q in enumerate(old_qs):
            bit = (i >> (n - 1 - k)) & 1
            j |= bit << (n - 1 - pos_new[q])
        t.append(j)
    return t


def reorder(A, new_qs):
    new_qs = tuple(new_qs)
    if new_qs == A.qs:
        return A
    if set(new_qs) != set(A.qs) or len(new_qs) != len(A.qs):
        raise ValueError("reorder: label sets differ %s %s" % (A.qs, new_qs))
    t = _perm_index(A.qs, new_qs)
    return Op(new_qs, {(t[r], t[c]): v for (r, c), v in A.d.items()})


def relabel(A, mapping):
    return Op(tuple(mapping.get(q, q) for q in A.qs), A.d)


def tensor(*ops_):
    out = ops_[0]
    for B in ops_[1:]:
        if set(out.qs) & set(B.qs):
            raise ValueError("tensor: overlapping labels")
        nb = B.n
        d = {}
        for (r1, c1), v1 in out.d.items():
            for (r2, c2), v2 in B.d.items():
                d[((r1 << nb) | r2, (c1 << nb) | c2)] = v1 * v2
        out = Op(out.qs + B.qs, d)
    return out


def dag(A):
    return Op(A.qs, {(c, r): v.conj() for (r, c), v in A.d.items()})


def matmul(A, B):
    B = reorder(B, A.qs)
    rows = {}
    for (r, c), v in B.d.items():
        rows.setdefault(r, []).append((c, v))
    d = {}
    for (r, k), v in A.d.items():
        for c, w in rows.get(k, ()):
            d[(r, c)] = d.get((r, c), ZERO) + v * w
    return Op(A.qs, d)


def trace(A):
    s = ZERO
    for (r, c), v in A.d.items():
        if r == c:
            s = s + v
    return s


def pair(E, X):
    """tr(E X) for operators on the same token set (any order)."""
    X = reorder(X, E.qs)
    s = ZERO
    for (r, c), v in E.d.items():
        w = X.d.get((c, r))
        if w is not None:
            s = s + v * w
    return s


def _split(i, n, pos_list):
    """extract bits at positions pos_list (positions in an n-bit index, 0 = MSB) as an integer (in list order)."""
    out = 0
    for p in pos_list:
        out = (out << 1) | ((i >> (n - 1 - p)) & 1)
    return out


def ptrace(A, keep):
    keep = tuple(keep)
    n = A.n
    kpos = [A.qs.index(q) for q in keep]
    tpos = [k for k in range(n) if A.qs[k] not in keep]
    d = {}
    for (r, c), v in A.d.items():
        if _split(r, n, tpos) == _split(c, n, tpos):
            key = (_split(r, n, kpos), _split(c, n, kpos))
            d[key] = d.get(key, ZERO) + v
    return Op(keep, d)


def ptranspose(A, S):
    S = set(S)
    n = A.n
    mask = 0
    for k, q in enumerate(A.qs):
        if q in S:
            mask |= 1 << (n - 1 - k)
    d = {}
    for (r, c), v in A.d.items():
        r2 = (r & ~mask) | (c & mask)
        c2 = (c & ~mask) | (r & mask)
        d[(r2, c2)] = v
    return Op(A.qs, d)


def transpose(A):
    return Op(A.qs, {(c, r): v for (r, c), v in A.d.items()})


def cond(e, X):
    """tr_A[(e_A (x) 1) X] with A = e.qs a subset of X.qs; result on the other tokens, in X's order."""
    A = e.qs
    if not set(A) <= set(X.qs):
        raise ValueError("cond: effect tokens not in state")
    n = X.n
    apos = [X.qs.index(q) for q in A]
    bqs = tuple(q for q in X.qs if q not in A)
    bpos = [X.qs.index(q) for q in bqs]
    d = {}
    for (R, C), v in X.d.items():
        ra, rb = _split(R, n, apos), _split(R, n, bpos)
        ca, cb = _split(C, n, apos), _split(C, n, bpos)
        w = e.d.get((ca, ra))
        if w is not None:
            d[(rb, cb)] = d.get((rb, cb), ZERO) + w * v
    return Op(bqs, d)


def lam(x, R, g):
    """Link map of the state x read from tokens R to the other tokens: Lam_x(g) = tr_R[(g_R (x) 1) x]."""
    if tuple(g.qs) != tuple(R):
        g = reorder(g, R)
    return cond(g, x)


def choi(linmap, in_qs, out_qs):
    """Choi matrix sum_ij |i><j|_in (x) linmap(|i><j|_in) on in_qs + out_qs."""
    d = {}
    nin = len(in_qs)
    nout = len(out_qs)
    for (i, j), u in units(in_qs):
        img = reorder(linmap(u), out_qs)
        for (r, c), v in img.d.items():
            d[((i << nout) | r, (j << nout) | c)] = v
    return Op(tuple(in_qs) + tuple(out_qs), d)


def apply_choi(J, in_qs, out_qs, g):
    """The linear map with Choi matrix J (in_qs first) applied to g on in_qs:  out = tr_in[(g^T (x) 1) J]."""
    gT = transpose(reorder(g, in_qs))
    return reorder(cond(gT, reorder(J, tuple(in_qs) + tuple(out_qs))), out_qs)


def is_herm(A):
    return all(A.d.get((c, r), ZERO) == v.conj() for (r, c), v in A.d.items())


def psd(A):
    """Exact PSD test of a Hermitian operator by symmetric elimination; returns (bool, reason)."""
    if not is_herm(A):
        return False, "not Hermitian"
    M = [row[:] for row in A.dense()]
    N = len(M)
    alive = list(range(N))
    while alive:
        k = alive[0]
        p = M[k][k]
        if p.im != 0:
            return False, "complex pivot"
        if p.re < 0:
            return False, "negative pivot"
        if p.re == 0:
            if any(not M[k][j].is_zero() for j in alive):
                return False, "zero pivot with nonzero row"
            alive.pop(0)
            continue
        alive.pop(0)
        for i in alive:
            if M[i][k].is_zero():
                continue
            f = M[i][k] / p
            for j in alive:
                if not M[k][j].is_zero():
                    M[i][j] = M[i][j] - f * M[k][j]
    return True, "psd"


def eigvec_check(A, vec, lam_):
    """A |vec> == lam |vec> exactly (vec a list of exact numbers in A's basis)."""
    v = [G.of(a) for a in vec]
    N = 2 ** A.n
    out = [ZERO] * N
    for (r, c), w in A.d.items():
        out[r] = out[r] + w * v[c]
    return all(out[i] == G.of(lam_) * v[i] for i in range(N))


# ---------------------------------------------------------------------------------------------- standard objects
def bits_index(bits):
    i = 0
    for b in bits:
        i = (i << 1) | b
    return i


def basis_vec(bits):
    v = [0] * (2 ** len(bits))
    v[bits_index(bits)] = 1
    return v


def phi_plus(a, b):
    """|Phi+><Phi+| (normalized) on tokens (a, b)."""
    return ket_op([1, 0, 0, 1], (a, b)).scale(Fr(1, 2))


def swap_half(a, b):
    """PT_b(Phi+) = SWAP/2 on (a, b): the twin link."""
    return ptranspose(phi_plus(a, b), [b])


def ghz(qs):
    n = len(qs)
    v = [0] * (2 ** n)
    v[0] = 1
    v[-1] = 1
    return ket_op(v, qs).scale(Fr(1, 2))


def w3(qs):
    """W3 = 1/2 - |GHZ><GHZ| on three tokens."""
    return identity(qs).scale(Fr(1, 2)) - ghz(qs)


S0 = [[1, 0], [0, 1]]
SX = [[0, 1], [1, 0]]
SY = [[0, G(0, -1)], [G(0, 1), 0]]
SZ = [[1, 0], [0, -1]]
SIG = [S0, SX, SY, SZ]
CNOT = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]


def unitary_op(U, qs):
    return op(U, qs)


def ad(U, X):
    """U X U^dag for U an Op on a subset of X's tokens (extended by identity)."""
    rest = tuple(q for q in X.qs if q not in U.qs)
    Ufull = tensor(U, identity(rest)) if rest else U
    Ufull = reorder(Ufull, X.qs)
    return matmul(matmul(Ufull, X), dag(Ufull))


def sig_op(m, q):
    return op(SIG[m], (q,))


def coords1(rho):
    q = rho.qs[0]
    return [pair(sig_op(m, q), rho) for m in range(4)]


def coords2(rho):
    a, b = rho.qs
    return [[pair(tensor(sig_op(m, a), sig_op(n, b)), rho) for n in range(4)] for m in range(4)]


def pauli2(T, qs):
    out = Op(qs, {})
    for m in range(4):
        for n in range(4):
            t = G.of(T[m][n])
            if not t.is_zero():
                out = out + tensor(sig_op(m, qs[0]), sig_op(n, qs[1])).scale(t)
    return out.scale(Fr(1, 4))


def pauli1(v, q):
    out = Op((q,), {})
    for m in range(4):
        t = G.of(v[m])
        if not t.is_zero():
            out = out + sig_op(m, q).scale(t)
    return out.scale(Fr(1, 2))


def homtab(Rm):
    """homMap(R) as a 4x4 table: 1 at (0,0), R in the lower block."""
    H = [[Fr(0)] * 4 for _ in range(4)]
    H[0][0] = Fr(1)
    for i in range(3):
        for j in range(3):
            H[i + 1][j + 1] = Fr(Rm[i][j])
    return H


def mat_mul(A, B):
    return [[sum((Fr(A[i][k]) * Fr(B[k][j]) for k in range(len(B))), Fr(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def mat_T(A):
    return [list(r) for r in zip(*A)]


def det3(M):
    a = [[Fr(x) for x in r] for r in M]
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def quat_rot(a, b, c):
    """Rational rotation matrix of the quaternion (1, a, b, c) (Euler-Rodrigues), in SO(3)."""
    w, x, y, z = Fr(1), Fr(a), Fr(b), Fr(c)
    n = w * w + x * x + y * y + z * z
    return [[(w * w + x * x - y * y - z * z) / n, 2 * (x * y - w * z) / n, 2 * (x * z + w * y) / n],
            [2 * (x * y + w * z) / n, (w * w - x * x + y * y - z * z) / n, 2 * (y * z - w * x) / n],
            [2 * (x * z - w * y) / n, 2 * (y * z + w * x) / n, (w * w - x * x - y * y + z * z) / n]]


def quat_unitary(a, b, c):
    """Unnormalized U = 1 - i(a X + b Y + c Z); Ad(U)/(1 + a^2 + b^2 + c^2) is the rotation quat_rot(a, b, c)."""
    return [[G(1, -Fr(c)), G(-Fr(b), -Fr(a))], [G(Fr(b), -Fr(a)), G(1, Fr(c))]]


REFLY = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]


# ---------------------------------------------------------------------------------------------- hyperdeterminant
def hyperdet(p):
    """Cayley hyperdeterminant of a 2x2x2 tensor p[4 i + 2 j + k] (own transcription)."""
    a = lambda i, j, k: G.of(p[4 * i + 2 * j + k])
    t1 = (a(0, 0, 0) * a(0, 0, 0) * a(1, 1, 1) * a(1, 1, 1) + a(0, 0, 1) * a(0, 0, 1) * a(1, 1, 0) * a(1, 1, 0)
          + a(0, 1, 0) * a(0, 1, 0) * a(1, 0, 1) * a(1, 0, 1) + a(1, 0, 0) * a(1, 0, 0) * a(0, 1, 1) * a(0, 1, 1))
    t2 = (a(0, 0, 0) * a(1, 1, 1) * a(0, 0, 1) * a(1, 1, 0) + a(0, 0, 0) * a(1, 1, 1) * a(0, 1, 0) * a(1, 0, 1)
          + a(0, 0, 0) * a(1, 1, 1) * a(1, 0, 0) * a(0, 1, 1) + a(0, 0, 1) * a(1, 1, 0) * a(0, 1, 0) * a(1, 0, 1)
          + a(0, 0, 1) * a(1, 1, 0) * a(1, 0, 0) * a(0, 1, 1) + a(0, 1, 0) * a(1, 0, 1) * a(1, 0, 0) * a(0, 1, 1))
    t3 = (a(0, 0, 0) * a(0, 1, 1) * a(1, 0, 1) * a(1, 1, 0) + a(1, 1, 1) * a(1, 0, 0) * a(0, 1, 0) * a(0, 0, 1))
    return t1 - G(2) * t2 + G(4) * t3


# ---------------------------------------------------------------------------------------------- kernel parse
def parse_kernel(base):
    """Parse the kernel conventions from the base text; returns a dict of parsed objects (transcription control)."""
    cd = open(base + "/CompositeDimension.lean", encoding="utf-8").read()
    k2 = open(base + "/K2Guard.lean", encoding="utf-8").read()
    es = open(base + "/EffectSpace.lean", encoding="utf-8").read()
    kf = open(base + "/KInfFoundations.lean", encoding="utf-8").read()
    ci = open(base + "/CompositeInterface.lean", encoding="utf-8").read()
    out = {}

    def table(name):
        i = cd.index("def " + name + " : Fin 4 → Fin 4 → Fin 4")
        blk = cd[i:i + 420]
        t = [[None] * 4 for _ in range(4)]
        for m, n_, v in re.findall(r"\|\s*(\d),\s*(\d)\s*=>\s*(\d)", blk)[:16]:
            t[int(m)][int(n_)] = int(v)
        return t

    out["pc"], out["pt"] = table("pc"), table("pt")
    i = cd.index("def sgn (μ ν : Fin 4) : ℝ :=")
    line = cd[i:cd.index("\n", i)]
    neg = sorted((int(a), int(b)) for a, b in re.findall(r"μ = (\d) ∧ ν = (\d)", line))
    out["sgn_neg"] = neg if "then -1 else 1" in line else None
    i = cd.index("def phiW : W 3 :=")
    out["phiW_line"] = cd[i:cd.index("\n", i)].strip()
    for nm, src in (("idW", k2), ("chainW", k2)):
        i = src.index("def " + nm + " : W 3 := ")
        ln = src[i:src.index("\n", i)]
        out[nm] = [[int(v) for v in r.split(",")] for r in re.findall(r"!\[([-\d, ]+)\]", ln)]
    out["reflY_ok"] = "toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i" in k2
    out["sharp_ok"] = ("def sharpVec (b : Fin d → ℝ) : HVec d := Matrix.vecCons (1 / 2) fun j => b j / 2" in es)
    out["xplus_ok"] = "def xplus : Fin 3 → ℝ := ![1, 0, 0]" in cd
    out["z3_ok"] = "def z3 : Fin 3 → ℝ := ![0, 0, 1]" in cd
    out["prodState_ok"] = "def prodState (x y : Fin d → ℝ) : W d := fun μ ν => hom x μ * hom y ν" in cd
    out["isEffectOn_ok"] = "∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1" in kf
    out["prodEff_ok"] = ("prodEff_effect : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ)," in ci
                         and "prod_mem : ∀ x ∈ ΩA, ∀ y ∈ ΩB, prodState x y ∈ Ω" in ci)
    out["condA_compact"] = "theorem condA_mem (hcA : IsCompact ΩA)" in ci
    out["cnot_landed"] = "theorem cnot_prodState_xplus_z3 : cnot (prodState xplus z3) = phiW" in cd
    return out


HAND = {
    "pc": [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]],
    "pt": [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]],
    "sgn_neg": [(1, 3), (2, 2)],
    "phiW_line": "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0",
    "idW": [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    "chainW": [[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]],
}


def kernel_cnot_tab(T):
    """The kernel cnot on a 4x4 state table (hand transcription of CD:741-781)."""
    sg = lambda m, n: -1 if (m, n) in ((1, 3), (2, 2)) else 1
    return [[sg(m, n) * G.of(T[HAND["pc"][m][n]][HAND["pt"][m][n]]) for n in range(4)] for m in range(4)]


PHIW = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]


def transcription_control(base):
    """True iff every parsed kernel object equals its hand transcription."""
    k = parse_kernel(base)
    ok = (k["pc"] == HAND["pc"] and k["pt"] == HAND["pt"] and k["sgn_neg"] == HAND["sgn_neg"]
          and k["phiW_line"] == HAND["phiW_line"] and k["idW"] == HAND["idW"] and k["chainW"] == HAND["chainW"]
          and k["reflY_ok"] and k["sharp_ok"] and k["xplus_ok"] and k["z3_ok"] and k["prodState_ok"]
          and k["isEffectOn_ok"] and k["prodEff_ok"] and k["condA_compact"] and k["cnot_landed"])
    return ok, k


# ---------------------------------------------------------------------------------------------- random exact
def rand_gauss(rng, lo=-3, hi=3, dens=(1, 2, 3)):
    return G(Fr(rng.randint(lo, hi), rng.choice(dens)), Fr(rng.randint(lo, hi), rng.choice(dens)))


def rand_op(rng, qs, herm=True):
    N = 2 ** len(qs)
    M = [[rand_gauss(rng) for _ in range(N)] for _ in range(N)]
    if herm:
        M = [[M[r][c] + M[c][r].conj() for c in range(N)] for r in range(N)]
    return op(M, qs)


def rand_psd(rng, qs, rank=None):
    N = 2 ** len(qs)
    rank = N if rank is None else rank
    out = Op(qs, {})
    for _ in range(rank):
        v = [rand_gauss(rng) for _ in range(N)]
        out = out + ket_op(v, qs)
    return out


# ---------------------------------------------------------------------------------------------- reporting
class Report:
    def __init__(self, name):
        self.name = name
        self.checks = []

    def check(self, label, cond_):
        cond_ = bool(cond_)
        self.checks.append((label, cond_))
        print(("PASS " if cond_ else "FAIL ") + label, flush=True)
        return cond_

    def note(self, text):
        print("NOTE " + text, flush=True)

    def verdict(self, tag):
        npass = sum(1 for _, c in self.checks if c)
        print("--- %s: %d/%d checks pass" % (self.name, npass, len(self.checks)), flush=True)
        print(("VERDICT " + tag) if npass == len(self.checks) else "VERDICT NOT RENDERED", flush=True)
        return npass == len(self.checks)
