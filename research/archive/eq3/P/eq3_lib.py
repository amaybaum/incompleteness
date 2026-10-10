"""EQ3-P shared exact library (research only; base bcbc516f; nothing here is kernel-checked).

Own code: imports nothing from scratchpad/eq2 or scratchpad/eqreview.  Everything is exact (sympy Rationals, the
Gaussian unit I, symbols); no floating point anywhere in this module.

Conventions read from the base (NOTES N1.0):
  * W 3 = Fin 4 -> Fin 4 -> R (CompositeDimension.lean:97), stored as a 4x4 sympy Matrix, row = first copy.
  * index 0 is the unit; homogeneous index j+1 is Bloch coordinate j (hom, CD:100).
  * homMap N = 1 (+) N (CD:112); actT N w = w * homMap(N)^T (CD:198); actC N w = homMap(N) * w (CD:201).
  * Pauli order 0 -> 1, 1 -> X, 2 -> Y, 3 -> Z (the Pauli dictionary, used only as a cross-check).
  * reflY = diag(1, -1, 1) on Bloch coordinates (K2Guard.lean:46), i.e. homMap reflY = diag(1, 1, -1, 1).
  * Effect tables E pair with state tables X by the Euclidean pairing <E, X> = sum E_mn X_mn; for a product effect
    E = a b^T this is pairVal a b X (CD:164).
"""
import itertools
import re
import sys

import sympy as sp
from sympy import I, Matrix, Rational as R, eye, zeros

# ---------------------------------------------------------------- reporting
CHECKS = []


def check(name, cond, detail=None):
    ok = bool(cond)
    CHECKS.append((name, ok))
    line = ("PASS " if ok else "FAIL ") + name
    if detail is not None:
        line += "  [" + str(detail) + "]"
    print(line)
    sys.stdout.flush()
    return ok


def note(text):
    print("NOTE " + text)
    sys.stdout.flush()


def summary(tag):
    npass = sum(1 for _, c in CHECKS if c)
    print(f"--- {tag}: {npass}/{len(CHECKS)} checks pass")
    return npass == len(CHECKS)


def zero(M):
    return M.applyfunc(sp.expand).is_zero_matrix


# ---------------------------------------------------------------- Pauli objects
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


def coordsW(rho):
    """Pauli table of a two-qubit operator: w_mn = tr(rho sigma_m (x) sigma_n)."""
    return Matrix(4, 4, lambda m, n: sp.expand((rho * kron(PAULI[m], PAULI[n])).trace()))


def pauliW(w):
    """Operator of a state table: (1/4) sum w_mn sigma_m (x) sigma_n (inverse of coordsW)."""
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if w[m, n] != 0:
                out += w[m, n] * kron(PAULI[m], PAULI[n])
    return (out / 4).applyfunc(sp.expand)


def coords1(rho):
    return Matrix([sp.expand((rho * P).trace()) for P in PAULI])


def ad(U, X):
    return (U * X * U.H).applyfunc(sp.expand)


# ---------------------------------------------------------------- the carrier W 3 and its maps
def hom(x):
    return [sp.Integer(1)] + list(x)


def hom_map(N):
    M = eye(4)
    M[1:, 1:] = Matrix(N)
    return M


def prod_state(x, y):
    hx, hy = hom(x), hom(y)
    return Matrix(4, 4, lambda m, n: hx[m] * hy[n])


def pair_val(a, b, w):
    return sp.expand(sum(a[m] * w[m, n] * b[n] for m in range(4) for n in range(4)))


def eucl(A, B):
    """Euclidean pairing of two 4x4 tables."""
    return sp.expand(sum(A[m, n] * B[m, n] for m in range(4) for n in range(4)))


def actT(N, w):
    return w * hom_map(N).T


def actC(N, w):
    return hom_map(N) * w


REFLY = sp.diag(1, -1, 1)
NFLIP = sp.diag(1, -1, -1)
SGNY = [1, 1, -1, 1]
DELTA = sp.diag(1, 1, -1, 1)          # = homMap reflY = phiW (as a table)


def transposeW(w):
    """Global transpose on Pauli tables: w_mn -> s_m s_n w_mn, s = (1, 1, -1, 1)."""
    return Matrix(4, 4, lambda m, n: SGNY[m] * SGNY[n] * w[m, n])


def swapW(w):
    return w.T


# ---------------------------------------------------------------- parsing the base sources (own regexes)
def parse_cnot(cd_path):
    """Parse sgn, pc, pt from CompositeDimension.lean (CD:741-755); return the gate as a function on tables."""
    src = open(cd_path, encoding="utf-8").read()
    m = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if (.*?) then -1 else 1", src)
    neg = {(int(a), int(b)) for a, b in re.findall(r"μ = (\d) ∧ ν = (\d)", m.group(1))}
    sgn = [[(-1 if (i, j) in neg else 1) for j in range(4)] for i in range(4)]

    def table(name):
        blk = re.search(r"def " + name + r" : Fin 4 → Fin 4 → Fin 4\n((?:\s*\|.*\n){4})", src).group(1)
        t = [[None] * 4 for _ in range(4)]
        for a, b, c in re.findall(r"\| (\d), (\d) => (\d)", blk):
            t[int(a)][int(b)] = int(c)
        return t
    pc, pt = table("pc"), table("pt")
    return sgn, pc, pt


def cnot_from(tabs):
    sgn, pc, pt = tabs
    return lambda w: Matrix(4, 4, lambda m, n: sgn[m][n] * w[pc[m][n], pt[m][n]])


def parse_phiW(cd_path):
    src = open(cd_path, encoding="utf-8").read()
    m = re.search(r"def phiW : W 3 := fun μ ν => if μ = ν then \(if μ = (\d) then -1 else 1\) else 0", src)
    k = int(m.group(1))
    return Matrix(4, 4, lambda i, j: (0 if i != j else (-1 if i == k else 1)))


def parse_k2guard(k2_path):
    src = open(k2_path, encoding="utf-8").read()

    def mat(name):
        blk = re.search(r"def " + name + r" : W 3 := !\[(.*?)\]\n", src).group(1)
        rows = re.findall(r"!\[([^\]]*)\]", blk)
        return Matrix([[sp.Integer(int(v.strip())) for v in r.split(",")] for r in rows])
    refl = re.search(r"def reflY.*?toFun x := fun i => \(!\[([^\]]*)\]", src, re.S).group(1)
    return mat("idW"), mat("chainW"), [int(v.strip()) for v in refl.split(",")]


HAND_SGN_NEG = {(1, 3), (2, 2)}
HAND_PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
HAND_PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
HAND_PHIW = sp.diag(1, 1, -1, 1)
HAND_IDW = eye(4)
HAND_CHAINW = Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
XPLUS = [1, 0, 0]
Z3 = [0, 0, 1]

CNOT_U = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])   # control = first copy


# ---------------------------------------------------------------- n-copy operators (explicit tensor placement)
def place(ops_by_copy, n):
    """Tensor product of single-copy or multi-copy operators placed on given copies.
    ops_by_copy: list of (copies tuple, operator on those copies in the tuple's order).  Missing copies get the
    identity.  Returns the 2^n x 2^n matrix in the basis index sum_k x_k 2^(n-1-k)."""
    dim = 2 ** n
    covered = [c for cs, _ in ops_by_copy for c in cs]
    rest = [c for c in range(n) if c not in covered]
    full = list(ops_by_copy) + [((c,), S0) for c in rest]
    M = zeros(dim, dim)
    for a in itertools.product(range(2), repeat=n):
        for b in itertools.product(range(2), repeat=n):
            v = sp.Integer(1)
            for cs, op in full:
                ia = sum(a[c] * 2 ** (len(cs) - 1 - t) for t, c in enumerate(cs))
                ib = sum(b[c] * 2 ** (len(cs) - 1 - t) for t, c in enumerate(cs))
                v = v * op[ia, ib]
                if v == 0:
                    break
            if v != 0:
                M[sum(a[k] * 2 ** (n - 1 - k) for k in range(n)), sum(b[k] * 2 ** (n - 1 - k) for k in range(n))] = v
    return M


def ptrace_keep(M, keep, n):
    """Partial trace of a 2^n operator keeping the copies in `keep` (in that order)."""
    k = len(keep)
    out = zeros(2 ** k, 2 ** k)
    others = [c for c in range(n) if c not in keep]
    for a in itertools.product(range(2), repeat=k):
        for b in itertools.product(range(2), repeat=k):
            s = 0
            for r in itertools.product(range(2), repeat=len(others)):
                ia, ib = [0] * n, [0] * n
                for t, c in enumerate(keep):
                    ia[c], ib[c] = a[t], b[t]
                for t, c in enumerate(others):
                    ia[c], ib[c] = r[t], r[t]
                s += M[sum(ia[q] * 2 ** (n - 1 - q) for q in range(n)), sum(ib[q] * 2 ** (n - 1 - q) for q in range(n))]
            out[sum(a[t] * 2 ** (k - 1 - t) for t in range(k)), sum(b[t] * 2 ** (k - 1 - t) for t in range(k))] = s
    return out.applyfunc(sp.expand)


def pt_copy(M, which, n):
    """Partial transpose of a 2^n operator on copy `which`."""
    out = zeros(2 ** n, 2 ** n)
    for a in itertools.product(range(2), repeat=n):
        for b in itertools.product(range(2), repeat=n):
            a2, b2 = list(a), list(b)
            a2[which], b2[which] = b[which], a[which]
            out[sum(a2[q] * 2 ** (n - 1 - q) for q in range(n)), sum(b2[q] * 2 ** (n - 1 - q) for q in range(n))] = \
                M[sum(a[q] * 2 ** (n - 1 - q) for q in range(n)), sum(b[q] * 2 ** (n - 1 - q) for q in range(n))]
    return out


# ---------------------------------------------------------------- deterministic exact random objects
def rng_rat(rng, lo=-5, hi=5, dmax=4):
    return R(rng.randint(lo, hi), rng.randint(1, dmax))


def rand_gauss(rng, n, m):
    return Matrix(n, m, lambda i, j: rng_rat(rng) + I * rng_rat(rng))


def rand_herm(rng, n):
    A = rand_gauss(rng, n, n)
    return (A + A.H).applyfunc(sp.expand)


def rand_psd(rng, n, rank=None):
    A = rand_gauss(rng, n, rank or n)
    return (A * A.H).applyfunc(sp.expand)
