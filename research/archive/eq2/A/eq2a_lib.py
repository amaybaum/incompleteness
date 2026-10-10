"""EQ2-A shared exact library (research only; base bcbc516f; nothing here is kernel-checked).

Transcriptions of the kernel definitions used by the EQ2-A probes.  Everything is exact: sympy Rationals, the Gaussian
unit I, and symbols.  No floating point is used anywhere in this module.

Conventions (read from the source, NOTES N2):
  * W 3 = Fin 4 -> Fin 4 -> R  (CompositeDimension.lean:97), stored as a 4x4 sympy Matrix, row = first copy.
  * index 0 is the unit; homogeneous index j+1 is Bloch coordinate j (hom, CD:100).
  * homMap N = 1 (+) N (CD:112);  actT N w = w * homMap(N)^T (CD:198);  actC N w = homMap(N) * w (CD:201).
  * Pauli order 0 -> 1, 1 -> X, 2 -> Y, 3 -> Z.
  * reflY = diag(1,-1,1) (K2Guard.lean:46): flips Bloch coordinate 1 = homogeneous index 2 (the Y index).
The cnot tables sgn/pc/pt and the tables phiW, idW, chainW are PARSED from the base files given on the command line,
and are cross-checked against independent hand transcriptions (a transcription control).
"""
import itertools
import re
import sys

import sympy as sp
from sympy import I, Matrix, Rational as R, eye, zeros

CHECKS = []


def check(name, cond):
    ok = bool(cond)
    CHECKS.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name)
    sys.stdout.flush()
    return ok


def summary(tag):
    npass = sum(1 for _, c in CHECKS if c)
    print(f"{tag}: {npass}/{len(CHECKS)} checks pass")
    return npass == len(CHECKS)


# ---------------------------------------------------------------- Pauli matrices and qubit objects
S0 = eye(2)
SX = Matrix([[0, 1], [1, 0]])
SY = Matrix([[0, -I], [I, 0]])
SZ = Matrix([[1, 0], [0, -1]])
PAULI = [S0, SX, SY, SZ]


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out


def rho1(x):
    """Bloch state (1 + x.sigma)/2 for a Bloch vector x (list of 3)."""
    return (S0 + x[0] * SX + x[1] * SY + x[2] * SZ) / 2


def effop1(a):
    """Effect operator of a homogenized functional a (list of 4): a0*1 + a1 X + a2 Y + a3 Z (value tr(A rho) = a.hom x)."""
    return a[0] * S0 + a[1] * SX + a[2] * SY + a[3] * SZ


# ---------------------------------------------------------------- the carrier W 3 and its maps
def hom(x):
    return [sp.Integer(1)] + list(x)


def hom_map(N):
    """homMap N as a 4x4 matrix: 1 (+) N."""
    M = eye(4)
    M[1:, 1:] = Matrix(N)
    return M


def prod_state(x, y):
    hx, hy = hom(x), hom(y)
    return Matrix(4, 4, lambda m, n: hx[m] * hy[n])


def pair_val(a, b, w):
    return sum(a[m] * w[m, n] * b[n] for m in range(4) for n in range(4))


def actT(N, w):
    return w * hom_map(N).T


def actC(N, w):
    return hom_map(N) * w


def swapW(w):
    return w.T


REFLY = sp.diag(1, -1, 1)
NFLIP = sp.diag(1, -1, -1)
ID3 = eye(3)
SGNY = [1, 1, -1, 1]


def transposeW(w):
    """The global transpose on Pauli tables: omega_{mu nu} -> s_mu s_nu omega_{mu nu}, s = (1,1,-1,1)."""
    return Matrix(4, 4, lambda m, n: SGNY[m] * SGNY[n] * w[m, n])


def chart2(a, b, w):
    """chart2 a b = actC a . actT b (design v2 Sec. 6.1)."""
    return actC(a, actT(b, w))


def pauliW(w):
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if w[m, n] != 0:
                out += w[m, n] * kron(PAULI[m], PAULI[n])
    return out / 4


def coordsW(rho):
    return Matrix(4, 4, lambda m, n: sp.expand((rho * kron(PAULI[m], PAULI[n])).trace()))


def is_psd_exact(M):
    """Exact PSD test for a Hermitian matrix with exact entries: all principal minors >= 0.
    Used only on small matrices (<= 8x8 would be 255 minors; we restrict callers to <= 4x4)."""
    n = M.shape[0]
    if not (M - M.H).is_zero_matrix:
        return False
    for k in range(1, n + 1):
        for idx in itertools.combinations(range(n), k):
            d = sp.simplify(M.extract(list(idx), list(idx)).det())
            if sp.re(d) < 0 or sp.im(d) != 0:
                return False
    return True


def cayley(A):
    return (eye(A.shape[0]) - A) * (eye(A.shape[0]) + A).inv()


# ---------------------------------------------------------------- n-copy tables (dict idx-tuple -> value)
def pauliN(tab, n):
    out = zeros(2 ** n, 2 ** n)
    for idx, c in tab.items():
        if c != 0:
            out += c * kron(*[PAULI[i] for i in idx])
    return out / (2 ** n)


def coordsN(rho, n):
    return {idx: sp.expand((rho * kron(*[PAULI[i] for i in idx])).trace())
            for idx in itertools.product(range(4), repeat=n)}


def idle_ext(g2, tab3, pair):
    """Idle extension of a two-copy map g2 (function on 4x4 tables) acting on the copies `pair` of a 3-copy table,
    identity on the remaining copy.  pair is an ordered pair of copy positions; g2's first index is pair[0]."""
    other = [c for c in range(3) if c not in pair][0]
    out = {}
    for k in range(4):
        def get(m, n, k=k):
            idx = [0, 0, 0]
            idx[pair[0]], idx[pair[1]], idx[other] = m, n, k
            return tab3[tuple(idx)]
        sl = Matrix(4, 4, get)
        im = g2(sl)
        for m in range(4):
            for n in range(4):
                idx = [0, 0, 0]
                idx[pair[0]], idx[pair[1]], idx[other] = m, n, k
                out[tuple(idx)] = im[m, n]
    return out


# ---------------------------------------------------------------- parsing the base sources
def parse_cnot_tables(cd_path):
    """Parse sgn, pc, pt from CompositeDimension.lean (CD:741-755)."""
    src = open(cd_path, encoding="utf-8").read()
    m = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if (.*?) then -1 else 1", src)
    pairs = re.findall(r"μ = (\d) ∧ ν = (\d)", m.group(1))
    neg = {(int(a), int(b)) for a, b in pairs}
    sgn = [[(-1 if (i, j) in neg else 1) for j in range(4)] for i in range(4)]

    def table(name):
        blk = re.search(r"def " + name + r" : Fin 4 → Fin 4 → Fin 4\n((?:\s*\|.*\n){4})", src).group(1)
        t = [[None] * 4 for _ in range(4)]
        for a, b, c in re.findall(r"\| (\d), (\d) => (\d)", blk):
            t[int(a)][int(b)] = int(c)
        return t
    return sgn, table("pc"), table("pt")


def cnot_fun(tabs):
    sgn, pc, pt = tabs
    return lambda w: Matrix(4, 4, lambda m, n: sgn[m][n] * w[pc[m][n], pt[m][n]])


def parse_k2guard_tables(k2_path):
    src = open(k2_path, encoding="utf-8").read()

    def mat(name):
        blk = re.search(r"def " + name + r" : W 3 := !\[(.*?)\]\n", src).group(1)
        rows = re.findall(r"!\[([^\]]*)\]", blk)
        return Matrix([[sp.Integer(int(v.strip())) for v in r.split(",")] for r in rows])
    refl = re.search(r"def reflY.*?toFun x := fun i => \(!\[([^\]]*)\]", src, re.S).group(1)
    return mat("idW"), mat("chainW"), [int(v.strip()) for v in refl.split(",")]


def parse_phiW(cd_path):
    src = open(cd_path, encoding="utf-8").read()
    m = re.search(r"def phiW : W 3 := fun μ ν => if μ = ν then \(if μ = (\d) then -1 else 1\) else 0", src)
    k = int(m.group(1))
    return Matrix(4, 4, lambda i, j: (0 if i != j else (-1 if i == k else 1)))


# hand transcriptions (the transcription control compares these with the parsed tables)
HAND_PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
HAND_PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
HAND_NEG = {(1, 3), (2, 2)}
HAND_IDW = eye(4)
HAND_CHAINW = Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
HAND_PHIW = sp.diag(1, 1, -1, 1)
XPLUS = [1, 0, 0]
Z3 = [0, 0, 1]


def sharp_vec(b):
    """EffectSpace.sharpVec b = (1/2, b/2) (EffectSpace.lean:57)."""
    return [R(1, 2)] + [sp.Rational(v) / 2 for v in b]


# ---------------------------------------------------------------- Gaussian-rational unitaries
def rand_gauss_skew(n, seed):
    """Deterministic anti-Hermitian Gaussian-rational matrix (for exact unitaries via the Cayley transform)."""
    import random
    rng = random.Random(seed)
    A = zeros(n, n)
    for i in range(n):
        A[i, i] = I * R(rng.randint(-5, 5), rng.randint(1, 4))
        for j in range(i + 1, n):
            z = R(rng.randint(-5, 5), rng.randint(1, 4)) + I * R(rng.randint(-5, 5), rng.randint(1, 4))
            A[i, j] = z
            A[j, i] = -sp.conjugate(z)
    return A


def exact_unitary(n, seed):
    """Cayley transform of an anti-Hermitian Gaussian-rational matrix: an exact unitary over Q(i)."""
    U = cayley(rand_gauss_skew(n, seed))
    return U.applyfunc(sp.expand)


def is_unitary(U):
    return (U.H * U - eye(U.shape[0])).applyfunc(sp.simplify).is_zero_matrix


def ad(U, X):
    return U * X * U.H


def pt(M, which, dims):
    """Partial transpose of M on tensor factor `which` (0-based) of factors with sizes dims."""
    n = len(dims)
    idxs = list(itertools.product(*[range(d) for d in dims]))
    pos = {t: i for i, t in enumerate(idxs)}
    out = zeros(M.shape[0], M.shape[1])
    for a in idxs:
        for b in idxs:
            a2, b2 = list(a), list(b)
            a2[which], b2[which] = b[which], a[which]
            out[pos[tuple(a2)], pos[tuple(b2)]] = M[pos[a], pos[b]]
    return out


def swap_matrix(dims, perm):
    """Permutation matrix sending tensor factor i to position perm[i]."""
    idxs = list(itertools.product(*[range(d) for d in dims]))
    pos = {t: i for i, t in enumerate(idxs)}
    N = len(idxs)
    P = zeros(N, N)
    for a in idxs:
        b = [None] * len(a)
        for i, p in enumerate(perm):
            b[p] = a[i]
        P[pos[tuple(b)], pos[a]] = 1
    return P
