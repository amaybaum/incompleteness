"""EQ4-P audit -- independent exact checks (research only).

Usage:  python3 -I -B audit_eq4p.py

Independence: imports nothing from scratchpad/eq4/ (no eq4_lib), nothing from the thread's probes.  Own operator
calculus on int64 tensors with tracked scale factors, own exact rank / determinant / PSD tests, own double-description
vertex enumeration, own written decomposition for K_A; sympy only for symbolic identities.

DECISION RULE (fixed before the first run; rules, not expected numbers).  Print `VERDICT AUDIT-EQ4P-INDEPENDENT-EXACT`
iff every check below passes (each favourable check carries its countercontrol); otherwise `VERDICT NOT RENDERED`.
 T  Lemma T (one-token teleportation).  T1: on all 64 matrix units y of (p,s,t),
    tr_zp[(2Phi+_zp (x) 1)(2Phi+_zq (x) y)] = y renamed p->q.  T2 (countercontrol): with the product link
    2|00><00|_zq in place of 2Phi+_zq the identity fails on some unit.
 U  Six-token chain.  U1: three steps (z=4: 0->3; z=5: 1->4; z=0: 2->5) carry a random integer operator y on (0,1,2)
    to y on (3,4,5) with labels 0->3, 1->4, 2->5, each step with factor 1/4 (unscaled Phi+).  U2: the five-token pairing
    tr[(Phi+_02 (x) W3_534)(Phi+_05 (x) GHZ_342)] equals (1/4) tr(W3 GHZ) and is negative.  U3: each single-token marginal
    of GHZ is I/2 (so <phi|GHZ|phi> <= 1/2 on every product across a 1|2 cut: W3 in BS*), and <GHZ|W3|GHZ> < 0
    (W3 not PSD, so not in BS).  U4 (control): with GHZ as the effect the U2 value is positive.
 P  3|3 Bell links.  P1: tr[(W3_012 (x) GHZ_345)(Phi+_03 Phi+_14 Phi+_25)] < 0.  P2 (control): GHZ (x) GHZ gives > 0.
 N  Five-token countermodel lemma.  N1: for 24 random integer PSD effects e on (0,1) and PSD blocks on (0,a), (1,b),
    the contraction tr_01[(e (x) 1)(sigma_0a (x) sigma'_1b)] on (a,b) is PSD (all principal minors >= 0, exact).
    N2 (countercontrol): e = SWAP (not PSD) with Bell blocks gives a non-PSD contraction.
 S  Sector.  S1: the group <XXX, ZZ1, 1ZZ> has 8 elements and its average equals the GHZ-basis pinching on all 64
    units.  S2: for a symbolic filter A = [[a,b],[c,d]] on token k (k = 1,2,3), |<GHZ_m'|A_k|GHZ_m>|^2 equals
    (1/4)|a+d|^2 [m'=m] + (1/4)|a-d|^2 [m'=Z_k m] + (1/4)|b+c|^2 [m'=X_k m] + (1/4)|b-c|^2 [m'=X_kZ_k m]; countercontrol:
    the same with |b+c|^2 and |b-c|^2 exchanged is false.  S3: Z1, X1, X2, X3, S1S2, SWAP12, SWAP23 each permute the GHZ
    projectors (phases only) and generate a permutation group of order 192.
 A  K_A = cone{e_j+e_k, 1-2e_j, 1-2e_j+2e_p}.  A1: 92 generators, pairwise >= 0.  A2: own double description of
    K_A* returns exactly the 92 generators (up to positive scale).  A3: own written decomposition (sorted chamber)
    writes 400 random exact points of K_A* as nonnegative combinations of generators, verified by reconstruction.
    A4: the extreme rays of K_A n R^8_+ are exactly the 28 e_j+e_k.  A5: GHZ+ pairs negatively with a generator;
    2 W3 and 2 kappa (coordinates computed from the operators) are generators.  A6 (countercontrol):
    cone{e_j+e_k, 1-2e_j} has two dual elements with negative pairing, so it is not self-dual.
 W  K_tw.  W1: the S3 group orbit of t has 24 elements; the 36-vector set {p_b, orbit(t), k_m} is invariant.
    W2: pairwise >= 0.  W3: own double description of K_tw* returns exactly the 36 generators.  W4: GHZ+ pairs
    negatively with a generator; 2 W3 is in cone(p_b, orbit(t)) by an explicit combination.  W5 (sample): twirls of 60
    random B_tw generators PT_j(sigma_ij) (x) rho_k (Gaussian-integer sigma, rho; all six (cut, j)) pair >= 0 with every
    generator; countercontrol: the twirl of GHZ+ pairs negatively with one.
 M  Maximality.  M1: PT_k (k = 1,2,3) of a symbolic GHZ-diagonal z splits into 2x2 blocks [[u, v], [v, u]]; the forms
    u +- v are collected.  M2: 2<nu,z>, 2<F,z>, 2<G,z> equal explicit nonnegative combinations of collected forms
    (expand == 0).  M3: nu = 2 W3 + 4 GHZ-; <nu, Z1 nu Z1> < 0; nu = nu^T; tr(F G) < 0.  M4 (countercontrol): W3 in Z
    (PT_k(W3) PSD, k = 1,2,3) and <GHZ+, W3> < 0, so GHZ+ is not nonnegative on Z.
 E  E3 ingredients.  E1: Cayley hyperdeterminant: CNOT_01(|+> Phi+) has Det != 0, as do GHZ and psi3; W, |000> and
    |0>Phi+ have Det = 0.  E2: the seven-token contraction (Bell (0,4), (1,5); |000>+|111> on (6,2,3); effect psi3 on
    (4,5,6)) is the vector sum_ij |i>_0 |i+j>_1 |j>_2 |j>_3, the Choi vector of a CNOT (inputs 0, 2; outputs 1, 3).
 C  Owner's distinction.  C1: C = c c^T (CNOT Choi) has C^2 = 4C and C^T = C.  C2: on all 7 cuts the reduced state
    of C/4 has largest eigenvalue <= 1/2 (so <phi|C|phi> <= 2 for unit product vectors across the cut and w >= 0 on
    them); the cuts attaining 1/2 are printed.  C3: w = I/16 - C/32 has tr(Cw)/tr(w) < 0 (value printed).
 J  E2 crossing calculus, crossing (01|234, 02|134).  J1: Choi(Lambda_x) = PT_R(x) for random integer x.  J2: on all 64
    units f of (2,3,4) the conditional tr_B[(f (x) 1_A)(x (x) y)] equals Lambda'_x(f_R) (x) Lambda'_y(f_U), with
    Lambda' rebuilt from the Choi matrices PT_R(x), PT_U(y).  J3 (countercontrol): rebuilt from x without PT_R it fails.
"""
import random
from fractions import Fraction as Fr
from itertools import combinations, product
from math import gcd

import numpy as np
import sympy as sp

rng = random.Random(20261009)
RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""), flush=True)


# ----------------------------------------------------------------------------------------------- operator calculus
class Op:
    """Integer operator on labelled qubits: tensor of shape (2,)*2n, ket axes then bra axes."""

    def __init__(self, t, labels):
        self.t = np.asarray(t, dtype=np.int64)
        self.labels = tuple(labels)

    @staticmethod
    def mat(M, labels):
        n = len(labels)
        return Op(np.asarray(M, dtype=np.int64).reshape((2,) * (2 * n)), labels)

    def matrix(self):
        n = len(self.labels)
        return self.t.reshape(2 ** n, 2 ** n)

    def reorder(self, labels):
        labels = tuple(labels)
        assert sorted(labels) == sorted(self.labels)
        perm = [self.labels.index(lab) for lab in labels]
        n = len(labels)
        return Op(self.t.transpose(perm + [n + p for p in perm]), labels)

    def rename(self, mapping):
        return Op(self.t, [mapping.get(lab, lab) for lab in self.labels])


def tensor(*ops):
    t, labels = ops[0].t, list(ops[0].labels)
    for o in ops[1:]:
        n1, n2 = len(labels), len(o.labels)
        assert not set(labels) & set(o.labels)
        tt = np.multiply.outer(t, o.t)
        perm = (list(range(n1)) + list(range(2 * n1, 2 * n1 + n2)) + list(range(n1, 2 * n1))
                + list(range(2 * n1 + n2, 2 * n1 + 2 * n2)))
        t = tt.transpose(perm)
        labels += list(o.labels)
    return Op(t, labels)


def ident(labels):
    return Op.mat(np.eye(2 ** len(labels), dtype=np.int64), labels)


def extend(A, full):
    missing = [lab for lab in full if lab not in A.labels]
    if missing:
        A = tensor(A, ident(missing))
    return A.reorder(full)


def mul(A, B):
    B = B.reorder(A.labels)
    n = len(A.labels)
    return Op((A.matrix() @ B.matrix()).reshape((2,) * (2 * n)), A.labels)


def ptrace(A, drop):
    t, labels = A.t, list(A.labels)
    for lab in drop:
        k = labels.index(lab)
        n = len(labels)
        t = np.trace(t, axis1=k, axis2=n + k)
        labels.pop(k)
    return Op(t, labels)


def ptranspose(A, on):
    n = len(A.labels)
    perm = list(range(2 * n))
    for lab in on:
        k = A.labels.index(lab)
        perm[k], perm[n + k] = n + k, k
    return Op(A.t.transpose(perm), A.labels)


def tr(A):
    return int(np.trace(A.matrix()))


def pair(E, X):
    full = E.labels
    return tr(mul(E, X.reorder(full)))


def same(A, B):
    return bool(np.array_equal(A.t, B.reorder(A.labels).t))


def ket(amps, labels):
    v = np.asarray(amps, dtype=np.int64).reshape(-1, 1)
    return Op.mat(v @ v.T, labels)


def basis(bits):
    v = [0] * (2 ** len(bits))
    v[int("".join(map(str, bits)), 2)] = 1
    return v


BELLV = [1, 0, 0, 1]                      # |00> + |11>  (2 Phi+ = BELLV BELLV^T)


def bell2(a, b):
    return ket(BELLV, (a, b))


GHZV = [1, 0, 0, 0, 0, 0, 0, 1]


def ghz2(*labs):
    return ket(GHZV, labs)                # 2 GHZ


def w3_2(*labs):                          # 2 W3 = I - 2 GHZ
    return Op.mat(np.eye(8, dtype=np.int64) - ghz2(*labs).matrix(), labs)


def unit(i, j, labels):
    n = len(labels)
    M = np.zeros((2 ** n, 2 ** n), dtype=np.int64)
    M[i, j] = 1
    return Op.mat(M, labels)


def rand_int_op(labels, lo=-3, hi=3):
    n = len(labels)
    return Op.mat([[rng.randint(lo, hi) for _ in range(2 ** n)] for _ in range(2 ** n)], labels)


def rand_psd(labels, lo=-3, hi=3):
    n = len(labels)
    M = np.array([[rng.randint(lo, hi) for _ in range(2 ** n)] for _ in range(2 ** n)], dtype=np.int64)
    return Op.mat(M @ M.T, labels)


# ------------------------------------------------------------------------------------ exact linear-algebra helpers
def det_int(M):
    """Bareiss fraction-free determinant of an integer matrix (list of lists)."""
    A = [list(map(int, r)) for r in M]
    n = len(A)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if sw is None:
                return 0
            A[k], A[sw] = A[sw], A[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def is_psd_int(M):
    M = [list(map(int, r)) for r in M]
    n = len(M)
    if any(M[i][j] != M[j][i] for i in range(n) for j in range(n)):
        return False
    for k in range(1, n + 1):
        for S in combinations(range(n), k):
            if det_int([[M[i][j] for j in S] for i in S]) < 0:
                return False
    return True


def rank_int(rows):
    M = [list(map(int, r)) for r in rows]
    if not M:
        return 0
    rank, ncols = 0, len(M[0])
    for c in range(ncols):
        piv = next((r for r in range(rank, len(M)) if M[r][c] != 0), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        for r in range(len(M)):
            if r != rank and M[r][c] != 0:
                f, g = M[r][c], M[rank][c]
                row = [g * x - f * y for x, y in zip(M[r], M[rank])]
                d = 0
                for x in row:
                    d = gcd(d, abs(x))
                M[r] = [x // d for x in row] if d else row
        rank += 1
    return rank


def normalize(v):
    d = 0
    for x in v:
        d = gcd(d, abs(int(x)))
    return tuple(int(x) // d for x in v) if d else tuple(int(x) for x in v)


def dot(a, b):
    return sum(int(x) * int(y) for x, y in zip(a, b))


def double_description(A, n):
    """Extreme rays of the pointed cone {x in R^n : a.x >= 0 for a in A} (integer rows), exact."""
    basis_idx = []
    for i, a in enumerate(A):
        if rank_int([A[j] for j in basis_idx] + [a]) > len(basis_idx):
            basis_idx.append(i)
        if len(basis_idx) == n:
            break
    assert len(basis_idx) == n, "cone not pointed / constraints not full rank"
    Binv = sp.Matrix([list(A[i]) for i in basis_idx]).inv()
    rays = []
    for k in range(n):
        col = [Binv[r, k] for r in range(n)]
        den = 1
        for x in col:
            den = sp.ilcm(den, sp.Rational(x).q)
        rays.append(normalize([int(x * den) for x in col]))
    processed = list(basis_idx)
    for i in range(len(A)):
        if i in basis_idx:
            continue
        a = A[i]
        vals = [dot(a, r) for r in rays]

        def tight(r):
            return frozenset(j for j in processed if dot(A[j], r) == 0)

        pos = [(r, v, tight(r)) for r, v in zip(rays, vals) if v > 0]
        neg = [(r, v, tight(r)) for r, v in zip(rays, vals) if v < 0]
        new = [r for r, v in zip(rays, vals) if v >= 0]
        for rp, vp, Tp in pos:
            for rn, vn, Tn in neg:
                common = Tp & Tn
                if len(common) < n - 2:
                    continue
                if rank_int([A[j] for j in common]) == n - 2:
                    new.append(normalize([vp * y - vn * x for x, y in zip(rp, rn)]))
        rays = list(dict.fromkeys(new))
        processed.append(i)
    return set(rays)


# ============================================================================================ T  teleportation
def teleport(Y, z, p, q):
    """tr_zp[(2Phi+_zp (x) 1)(2Phi+_zq (x) Y)] for Y on labels containing p."""
    rest = [lab for lab in Y.labels if lab != p]
    full = [z, p, q] + rest
    X = extend(tensor(bell2(z, q), Y), full)
    E = extend(bell2(z, p), full)
    return ptrace(mul(E, X), [z, p])


ok_t1 = True
for i in range(8):
    for j in range(8):
        y = unit(i, j, ("p", "s", "t"))
        c = teleport(y, "z", "p", "q")
        ok_t1 &= same(c, y.rename({"p": "q"}))
check("T1 teleportation identity on all 64 units (scaled Bell factors 2x2 = 4 = 1/(1/4))", ok_t1)


def teleport_product(Y, z, p, q):
    rest = [lab for lab in Y.labels if lab != p]
    full = [z, p, q] + rest
    X = extend(tensor(Op(ket([1, 0, 0, 0], (z, q)).t * 2, (z, q)), Y), full)
    E = extend(bell2(z, p), full)
    return ptrace(mul(E, X), [z, p])


fails = 0
for i in range(8):
    for j in range(8):
        y = unit(i, j, ("p", "s", "t"))
        if not same(teleport_product(y, "z", "p", "q"), y.rename({"p": "q"})):
            fails += 1
check("T2 countercontrol: a product link does not teleport", fails > 0, "%d/64 units fail" % fails)

# ============================================================================================ U  six-token chain
y0 = rand_int_op(("0", "1", "2"))
c1 = teleport(y0, "4", "0", "3")
c2 = teleport(c1, "5", "1", "4")
c3 = teleport(c2, "0", "2", "5")
check("U1 three five-token steps carry y on (0,1,2) to y on (3,4,5) (0->3, 1->4, 2->5), factor (1/4)^3",
      same(c3, y0.rename({"0": "3", "1": "4", "2": "5"})), "labels after: %s" % (c3.labels,))

full5 = ("0", "2", "5", "3", "4")
state = extend(tensor(bell2("0", "5"), ghz2("3", "4", "2")), full5)
eff = extend(tensor(bell2("0", "2"), w3_2("5", "3", "4")), full5)
scaled = tr(mul(eff, state))                                # = 16 x true value
ref = pair(w3_2("3", "4", "5"), ghz2("3", "4", "5"))       # = tr(2W3 2GHZ) = 4 tr(W3 GHZ)
true_val = Fr(scaled, 16)
check("U2 five-token pairing = (1/4) tr(W3 GHZ) < 0", scaled == ref and true_val < 0, "value %s" % true_val)
marg_ok = all(same(ptrace(ghz2("0", "1", "2"), [o for o in "012" if o != k]), ident((k,))) for k in "012")
w3ghz = Fr(pair(w3_2("0", "1", "2"), ghz2("0", "1", "2")), 4)
check("U3 single-token marginals of 2GHZ are I (GHZ marginals I/2: W3 in BS*); <GHZ|W3|GHZ> < 0 (W3 not in BS)",
      marg_ok and w3ghz < 0, "tr(W3 GHZ) = %s" % w3ghz)
eff_c = extend(tensor(bell2("0", "2"), ghz2("5", "3", "4")), full5)
ctrl = Fr(tr(mul(eff_c, state)), 16)
check("U4 control: with GHZ as the effect the value is positive", ctrl > 0, "value %s" % ctrl)

# ============================================================================================ P  3|3 Bell links
full6 = ("0", "1", "2", "3", "4", "5")
links = extend(tensor(bell2("0", "3"), bell2("1", "4"), bell2("2", "5")), full6)
v_bad = Fr(tr(mul(extend(tensor(w3_2("0", "1", "2"), ghz2("3", "4", "5")), full6), links)), 32)
v_ok = Fr(tr(mul(extend(tensor(ghz2("0", "1", "2"), ghz2("3", "4", "5")), full6), links)), 32)
check("P1 3|3 Bell-link value of W3 (x) GHZ is negative", v_bad < 0, "value %s" % v_bad)
check("P2 control: GHZ (x) GHZ gives a positive value", v_ok > 0, "value %s" % v_ok)

# ============================================================================================ N  PN contraction lemma
ok_n = True
for _ in range(24):
    e = rand_psd(("0", "1"))
    s1, s2 = rand_psd(("0", "a")), rand_psd(("1", "b"))
    full = ("0", "1", "a", "b")
    cnd = ptrace(mul(extend(e, full), extend(tensor(s1, s2), full)), ["0", "1"]).reorder(("a", "b"))
    ok_n &= is_psd_int(cnd.matrix().tolist())
check("N1 contraction of a PSD 2-token effect with two PSD pair blocks is PSD (24 random exact instances)", ok_n)
SWAP = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
full = ("0", "1", "a", "b")
cnd = ptrace(mul(extend(Op.mat(SWAP, ("0", "1")), full), extend(tensor(bell2("0", "a"), bell2("1", "b")), full)),
             ["0", "1"]).reorder(("a", "b"))
check("N2 countercontrol: SWAP (not PSD) gives a non-PSD contraction", not is_psd_int(cnd.matrix().tolist()))

# ============================================================================================ S  sector
I2 = np.eye(2, dtype=np.int64)
PX = np.array([[0, 1], [1, 0]], dtype=np.int64)
PZ = np.array([[1, 0], [0, -1]], dtype=np.int64)


def k3(a, b, c):
    return np.kron(np.kron(a, b), c)


def idx3(x, y, z):
    return 4 * x + 2 * y + z


GV = []                                   # GHZ basis: m = 2*b + s, b = 2*b1 + b2, s = 0 (+), 1 (-)
for b in range(4):
    b1, b2 = b >> 1, b & 1
    for s in range(2):
        v = np.zeros(8, dtype=np.int64)
        v[idx3(0, b1, b2)] = 1
        v[idx3(1, 1 - b1, 1 - b2)] = 1 if s == 0 else -1
        GV.append(v)

gens = [k3(PX, PX, PX), k3(PZ, PZ, I2), k3(I2, PZ, PZ)]
group = {tuple(np.eye(8, dtype=np.int64).ravel())}
frontier = [np.eye(8, dtype=np.int64)]
while frontier:
    nxt = []
    for g in frontier:
        for h in gens:
            m = g @ h
            key = tuple(m.ravel())
            if key not in group:
                group.add(key)
                nxt.append(m)
    frontier = nxt
group_m = [np.array(k, dtype=np.int64).reshape(8, 8) for k in group]
ok_s1 = len(group_m) == 8
for i in range(8):
    for j in range(8):
        Y = np.zeros((8, 8), dtype=np.int64)
        Y[i, j] = 1
        lhs = sum(g @ Y @ g.T for g in group_m)
        rhs = 2 * sum(int(v @ Y @ v) * np.outer(v, v) for v in GV)
        ok_s1 &= np.array_equal(lhs, rhs)
check("S1 <XXX, ZZ1, 1ZZ> has 8 elements; its average is the GHZ-basis pinching on all 64 units", ok_s1)

ar, ai, br, bi, cr, ci, dr, di = sp.symbols("ar ai br bi cr ci dr di", real=True)
a_, b_, c_, d_ = ar + sp.I * ai, br + sp.I * bi, cr + sp.I * ci, dr + sp.I * di
Asym = sp.Matrix([[a_, b_], [c_, d_]])


def perm_of(U):
    """U (sympy or int 8x8, possibly complex) maps each GHZ vector to a phase times a GHZ vector: return the map."""
    out = []
    for v in GV:
        w = sp.Matrix(U) * sp.Matrix(v)
        hit = None
        for m2, v2 in enumerate(GV):
            for ph in (1, -1, sp.I, -sp.I):
                if all(sp.expand(w[r] - ph * v2[r]) == 0 for r in range(8)):
                    hit = m2
        if hit is None:
            return None
        out.append(hit)
    return out


def emb(op2, k):
    mats = [sp.eye(2), sp.eye(2), sp.eye(2)]
    mats[k] = op2
    return sp.kronecker_product(sp.kronecker_product(mats[0], mats[1]), mats[2])


Xs, Zs = sp.Matrix(PX.tolist()), sp.Matrix(PZ.tolist())
ok_s2, ok_s2c = True, True
for k in range(3):
    pZ, pX, pXZ = perm_of(emb(Zs, k)), perm_of(emb(Xs, k)), perm_of(emb(Xs * Zs, k))
    Ak = emb(Asym, k)
    for m in range(8):
        for m2 in range(8):
            o = (sp.Matrix(GV[m2]).T * Ak * sp.Matrix(GV[m]))[0, 0] / 2
            lhs = sp.expand(o * sp.conjugate(o))
            rhs = (sp.Rational(1, 4) * ((a_ + d_) * sp.conjugate(a_ + d_)) * int(m2 == m)
                   + sp.Rational(1, 4) * ((a_ - d_) * sp.conjugate(a_ - d_)) * int(m2 == pZ[m])
                   + sp.Rational(1, 4) * ((b_ + c_) * sp.conjugate(b_ + c_)) * int(m2 == pX[m])
                   + sp.Rational(1, 4) * ((b_ - c_) * sp.conjugate(b_ - c_)) * int(m2 == pXZ[m]))
            wrong = (sp.Rational(1, 4) * ((a_ + d_) * sp.conjugate(a_ + d_)) * int(m2 == m)
                     + sp.Rational(1, 4) * ((a_ - d_) * sp.conjugate(a_ - d_)) * int(m2 == pZ[m])
                     + sp.Rational(1, 4) * ((b_ - c_) * sp.conjugate(b_ - c_)) * int(m2 == pX[m])
                     + sp.Rational(1, 4) * ((b_ + c_) * sp.conjugate(b_ + c_)) * int(m2 == pXZ[m]))
            ok_s2 &= sp.expand(lhs - rhs) == 0
            if sp.expand(lhs - wrong) != 0:
                ok_s2c = False
check("S2 twirled single-token filter = (1/4)|a+d|^2 id + (1/4)|a-d|^2 Z_k + (1/4)|b+c|^2 X_k + (1/4)|b-c|^2 X_kZ_k "
      "(symbolic, k = 1, 2, 3); countercontrol (|b+c|^2 <-> |b-c|^2) false", ok_s2 and not ok_s2c)

Ssym = sp.Matrix([[1, 0], [0, sp.I]])
SW12 = sp.zeros(8, 8)
SW23 = sp.zeros(8, 8)
for x, y_, z in product(range(2), repeat=3):
    SW12[idx3(y_, x, z), idx3(x, y_, z)] = 1
    SW23[idx3(x, z, y_), idx3(x, y_, z)] = 1
gen_ops = {"Z1": emb(Zs, 0), "X1": emb(Xs, 0), "X2": emb(Xs, 1), "X3": emb(Xs, 2),
           "S1S2": sp.kronecker_product(sp.kronecker_product(Ssym, Ssym), sp.eye(2)), "SWAP12": SW12, "SWAP23": SW23}
gperms = {}
for name, U in gen_ops.items():
    gperms[name] = perm_of(U)
okperm = all(p is not None and sorted(p) == list(range(8)) for p in gperms.values())
Gset = {tuple(range(8))}
frontier = [tuple(range(8))]
while frontier:
    nxt = []
    for g in frontier:
        for p in gperms.values():
            h = tuple(p[g[i]] for i in range(8))
            if h not in Gset:
                Gset.add(h)
                nxt.append(h)
    frontier = nxt
check("S3 the seven local operations permute the GHZ projectors; generated group order", okperm and len(Gset) == 192,
      "order %d" % len(Gset))

# ============================================================================================ A  K_A
E8 = [tuple(1 if i == j else 0 for i in range(8)) for j in range(8)]
ONE = (1,) * 8


def vadd(*vs):
    return tuple(sum(x) for x in zip(*vs))


def vsc(c, v):
    return tuple(c * x for x in v)


KA = set()
for j, k in combinations(range(8), 2):
    KA.add(normalize(vadd(E8[j], E8[k])))
for j in range(8):
    KA.add(normalize(vadd(ONE, vsc(-2, E8[j]))))
    for p in range(8):
        if p != j:
            KA.add(normalize(vadd(ONE, vsc(-2, E8[j]), vsc(2, E8[p]))))
KA = sorted(KA)
check("A1 K_A: 92 generators, pairwise >= 0", len(KA) == 92 and all(dot(u, v) >= 0 for u in KA for v in KA),
      "%d generators" % len(KA))
raysA = double_description(KA, 8)
check("A2 own double description: extreme rays of K_A* = the 92 generators", raysA == set(KA),
      "%d rays" % len(raysA))


def decompose_pairs(y):
    """y >= 0 (Fractions), 2 max <= sum: weights w[(i,j)] >= 0 with sum_j w = y (greedy with star finish)."""
    y = list(y)
    w = {}
    for _ in range(64):
        s = sum(y)
        if s == 0:
            return w
        order = sorted(range(len(y)), key=lambda i: -y[i])
        i1, i2, i3 = order[0], order[1], order[2]
        if 2 * y[i1] == s:
            for k in order[1:]:
                if y[k] > 0:
                    w[(i1, k)] = w.get((i1, k), 0) + y[k]
                    y[i1] -= y[k]
                    y[k] = 0
            continue
        delta = min(y[i2], (s - 2 * y[i3]) / 2)
        assert delta > 0
        w[(i1, i2)] = w.get((i1, i2), 0) + delta
        y[i1] -= delta
        y[i2] -= delta
    raise AssertionError("no termination")


def decompose_KA(x):
    """Own written decomposition: x in K_A* (sorted chamber argument) -> dict generator -> coefficient >= 0."""
    x = [Fr(v) for v in x]
    order = sorted(range(8), key=lambda i: x[i])
    lo, hi, second = order[0], order[7], order[6]
    s = sum(x)
    coeffs = {}
    a = -x[lo] if x[lo] < 0 else Fr(0)
    if a > 0:
        c = max(Fr(0), x[hi] + 2 * a - s / 2)
        assert c <= min(a, s / 2 - 2 * a - x[second], (x[hi] - a) / 2)
        b = a - c
        g_b = vadd(ONE, vsc(-2, E8[lo]))
        g_c = vadd(ONE, vsc(-2, E8[lo]), vsc(2, E8[hi]))
        coeffs[g_b] = b
        coeffs[g_c] = c
        y = [x[i] - b * g_b[i] - c * g_c[i] for i in range(8)]
    else:
        y = x
    assert min(y) >= 0 and 2 * max(y) <= sum(y)
    for (i, j), wt in decompose_pairs(y).items():
        g = vadd(E8[i], E8[j])
        coeffs[g] = coeffs.get(g, 0) + wt
    return coeffs


npts, nneg, okA3 = 0, 0, True
while npts < 400:
    x = [rng.randint(-6, 0)] + [rng.randint(0, 14) for _ in range(7)]
    rng.shuffle(x)
    if all(dot(g, x) >= 0 for g in KA):
        co = decompose_KA(x)
        rec = [sum(Fr(cf) * g[i] for g, cf in co.items()) for i in range(8)]
        okA3 &= rec == [Fr(v) for v in x] and all(cf >= 0 for cf in co.values())
        okA3 &= all(normalize(g) in set(KA) for g in co)
        npts += 1
        nneg += min(x) < 0
check("A3 own written decomposition reconstructs 400 random exact points of K_A*", okA3,
      "%d with a negative entry" % nneg)
raysA4 = double_description(KA + E8, 8)
check("A4 extreme rays of K_A n R^8_+ are exactly the 28 e_j + e_k",
      raysA4 == {normalize(vadd(E8[j], E8[k])) for j, k in combinations(range(8), 2)}, "%d rays" % len(raysA4))


def coords(Op3):
    """GHZ-basis eigenvalue coordinates of 2 x (operator) for an integer 8x8 matrix M: <v_m|M|v_m>/2 ... returned x2."""
    M = np.asarray(Op3, dtype=np.int64)
    return tuple(int(v @ M @ v) for v in GV)       # = 2 * lambda_m(M)


ghzp = normalize(coords(np.outer(GV[0], GV[0])))   # 2GHZ+ = v0 v0^T -> coordinates (4,0,..)/2 -> e_0
w3c = normalize(coords(w3_2("0", "1", "2").matrix()))
kap2 = np.eye(8, dtype=np.int64)
kap2[0, 7] = kap2[7, 0] = 2                        # 2 kappa = I + 2(|000><111| + h.c.)
kapc = normalize(coords(kap2))
neg_gen = [g for g in KA if dot(ghzp, g) < 0]
check("A5 GHZ+ pairs negatively with a generator; 2W3 and 2kappa are generators",
      bool(neg_gen) and w3c in set(KA) and kapc in set(KA), "GHZ+ %s, W3 %s, kappa %s" % (ghzp, w3c, kapc))
KAp = sorted({normalize(vadd(E8[j], E8[k])) for j, k in combinations(range(8), 2)}
             | {normalize(vadd(ONE, vsc(-2, E8[j]))) for j in range(8)})
xx = vadd(ONE, vsc(-2, E8[0]), vsc(2, E8[7]))
yy = (4, 1, 1, 1, 1, 1, 1, -1)
check("A6 countercontrol: cone{e_j+e_k, 1-2e_j} has dual elements x, y with <x,y> < 0 (not self-dual)",
      all(dot(g, xx) >= 0 for g in KAp) and all(dot(g, yy) >= 0 for g in KAp) and dot(xx, yy) < 0,
      "<x,y> = %d" % dot(xx, yy))

# ============================================================================================ W  K_tw
Gl = sorted(Gset)


def act(g, x):
    out = [0] * 8
    for i in range(8):
        out[g[i]] = x[i]
    return tuple(out)


tvec = (1, 1, 1, 1, 1, -1, 1, -1)
orbit = {act(g, tvec) for g in Gl}
pb = [vadd(E8[2 * b], E8[2 * b + 1]) for b in range(4)]
km = [vadd(ONE, vsc(-2, E8[m]), vsc(2, E8[m ^ 1])) for m in range(8)]
KTW = sorted({normalize(v) for v in pb} | {normalize(v) for v in orbit} | {normalize(v) for v in km})
inv = all(normalize(act(g, v)) in set(KTW) for g in Gl for v in KTW)
check("W1 orbit(t) has 24 elements; the 36-vector set is invariant under the group of S3",
      len(orbit) == 24 and len(KTW) == 36 and inv, "orbit %d, set %d" % (len(orbit), len(KTW)))
check("W2 K_tw generators pairwise >= 0", all(dot(u, v) >= 0 for u in KTW for v in KTW))
raysT = double_description(KTW, 8)
check("W3 own double description: extreme rays of K_tw* = the 36 generators", raysT == set(KTW),
      "%d rays" % len(raysT))
# 2W3 = (-1, 1, ..., 1): explicit combination in cone(p_b, orbit(t)).  For each P-pair {a, b} of fibres {1, 2, 3}
# with remaining fibre c, take the two orbit elements with fibre 00 at lambda (-1, 1) and fibre c at (+-1, -+1), weight 1/6
# each; then add p_b with weight 1/3 on fibres 1, 2, 3.
acc = [Fr(0)] * 8
for (fa, fb) in [(1, 2), (1, 3), (2, 3)]:
    fc = ({1, 2, 3} - {fa, fb}).pop()
    for sc_ in (1, -1):
        v = [0] * 8
        for f in (fa, fb):
            v[2 * f], v[2 * f + 1] = 1, 1          # P = 2, C = 0  (lambda = (1, 1))
        v[0], v[1] = -1, 1                         # fibre 00: lambda = (-1, 1): P = 0, C = -2
        v[2 * fc], v[2 * fc + 1] = sc_, -sc_       # fibre c: P = 0, C = +-2
        v = tuple(v)
        assert v in orbit
        for i in range(8):
            acc[i] += Fr(1, 6) * v[i]
# acc = (-1, 1, 2/3 ...): add p_b with coefficient 1/6 on fibres 1..3 to reach (-1, 1, 1, ..., 1)
for f in (1, 2, 3):
    for i in (2 * f, 2 * f + 1):
        acc[i] += Fr(1, 3)
check("W4 GHZ+ pairs negatively with a K_tw generator; 2W3 in cone(p_b, orbit t) (explicit combination)",
      any(dot(ghzp, g) < 0 for g in KTW) and tuple(acc) == tuple(Fr(v) for v in w3c), "combination %s" %
      ([str(v) for v in acc],))


def cmul(A, B):
    return (A[0] @ B[0] - A[1] @ B[1], A[0] @ B[1] + A[1] @ B[0])


def rand_herm_psd(n):
    Mr = np.array([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)], dtype=np.int64)
    Mi = np.array([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)], dtype=np.int64)
    return cmul((Mr, Mi), (Mr.T, -Mi.T))


def pt_on(M, k, n):
    """partial transpose of a 2^n x 2^n integer matrix on qubit k (0 = most significant)."""
    t = M.reshape((2,) * (2 * n))
    perm = list(range(2 * n))
    perm[k], perm[n + k] = n + k, k
    return t.transpose(perm).reshape(2 ** n, 2 ** n)


def place(M3, order):
    """M3 on qubits in 'order' (a permutation of 0,1,2) -> matrix in canonical order 0,1,2."""
    t = M3.reshape((2,) * 6)
    inv_ = [order.index(i) for i in range(3)]
    return t.transpose(inv_ + [3 + i for i in inv_]).reshape(8, 8)


okW5, nW5 = True, 0
for kcut in range(3):
    pair_ = [i for i in range(3) if i != kcut]
    for jpt in (0, 1):
        for _ in range(10):
            sr, si = rand_herm_psd(4)
            rr, ri = rand_herm_psd(2)
            sr, si = pt_on(sr, jpt, 2), pt_on(si, jpt, 2)
            Xr = np.kron(sr, rr) - np.kron(si, ri)          # real part of PT(sigma) (x) rho on (pair, k)
            Xr = place(Xr, pair_ + [kcut])
            lam2 = [int(v @ Xr @ v) for v in GV]            # 2 lambda_m (real part suffices: v real)
            okW5 &= all(dot(g, lam2) >= 0 for g in KTW)
            nW5 += 1
cc = any(dot(ghzp, g) < 0 for g in KTW)
check("W5 sample: twirls of 60 random B_tw generators pair >= 0 with every K_tw generator; countercontrol GHZ+ < 0",
      okW5 and nW5 == 60 and cc)

# ============================================================================================ M  maximality
lam = sp.symbols("l0:8", real=True)
zsym = sp.zeros(8, 8)
for m, v in enumerate(GV):
    zsym += lam[m] * sp.Matrix(v) * sp.Matrix(v).T / 2
forms = set()
ok_m1 = True
for k in range(3):
    Pk = sp.zeros(8, 8)
    for r in range(8):
        for c in range(8):
            rb, cb = [(r >> (2 - q)) & 1 for q in range(3)], [(c >> (2 - q)) & 1 for q in range(3)]
            rb[k], cb[k] = cb[k], rb[k]
            Pk[int("".join(map(str, rb)), 2), int("".join(map(str, cb)), 2)] = zsym[r, c]
    for r in range(8):
        offs = [c for c in range(8) if c != r and sp.expand(Pk[r, c]) != 0]
        if len(offs) != 1:
            ok_m1 = False
            continue
        c = offs[0]
        offs_c = [q for q in range(8) if q != c and sp.expand(Pk[c, q]) != 0]
        ok_m1 &= offs_c == [r] and sp.expand(Pk[r, r] - Pk[c, c]) == 0 and sp.expand(Pk[r, c] - Pk[c, r]) == 0
        forms.add(sp.expand(Pk[r, r] + Pk[r, c]))
        forms.add(sp.expand(Pk[r, r] - Pk[r, c]))
check("M1 PT_k of a symbolic GHZ-diagonal operator splits into 2x2 blocks [[u,v],[v,u]] (k = 1, 2, 3)", ok_m1,
      "%d distinct forms u +- v" % len(forms))
P_ = [lam[2 * b] + lam[2 * b + 1] for b in range(4)]
C_ = [lam[2 * b] - lam[2 * b + 1] for b in range(4)]


def is_form(e):
    return sp.expand(e) in forms


nu2 = np.eye(8, dtype=np.int64) - np.outer(GV[0], GV[0]) + 2 * np.outer(GV[1], GV[1])   # nu = I - 2GHZ+ + 4GHZ-
nu_c = [sp.Rational(int(v @ nu2 @ v), 2) for v in GV]
two_nu_z = sp.expand(2 * sum(nu_c[m] * lam[m] for m in range(8)))
pieces = [(P_[0] + C_[1]) / 2, (P_[0] - C_[1]) / 2] + [(P_[b] - C_[0]) / 2 for b in (1, 2, 3)]
combo_nu = 4 * pieces[0] + 4 * pieces[1] + 4 * (pieces[2] + pieces[3] + pieces[4])
F2 = np.eye(8, dtype=np.int64)
F2[0, 0] = F2[7, 7] = 0
G2 = F2.copy()
F2[0, 7] = F2[7, 0] = 2
G2[0, 7] = G2[7, 0] = -2                                   # 2F, 2G
F_c = [sp.Rational(int(v @ F2 @ v), 4) for v in GV]         # lambda(F) = <v|2F|v>/4
G_c = [sp.Rational(int(v @ G2 @ v), 4) for v in GV]
two_F_z = sp.expand(2 * sum(F_c[m] * lam[m] for m in range(8)))
two_G_z = sp.expand(2 * sum(G_c[m] * lam[m] for m in range(8)))
pf = [(P_[1] + C_[0]) / 2, (P_[2] + C_[0]) / 2, (P_[3] + C_[1]) / 2, (P_[3] - C_[1]) / 2]
pg = [(P_[1] - C_[0]) / 2, (P_[2] - C_[0]) / 2, (P_[3] + C_[1]) / 2, (P_[3] - C_[1]) / 2]
combo_F = 2 * pf[0] + 2 * pf[1] + 2 * (pf[2] + pf[3])
combo_G = 2 * pg[0] + 2 * pg[1] + 2 * (pg[2] + pg[3])
okm2 = (all(is_form(e) for e in pieces + pf + pg) and sp.expand(two_nu_z - combo_nu) == 0
        and sp.expand(two_F_z - combo_F) == 0 and sp.expand(two_G_z - combo_G) == 0)
check("M2 2<nu,z>, 2<F,z>, 2<G,z> are nonnegative combinations of the PT block forms (exact)", okm2)
w3m = w3_2("0", "1", "2").matrix()
ghzm = 2 * np.outer(GV[1], GV[1])                           # 4 GHZ-  (scaled by 2: v v^T = 2 GHZ-)
nu_ok = np.array_equal(nu2, w3m + ghzm)                     # nu = 2 W3 + 4 GHZ-   (2W3 = I - v0 v0^T)
Z1 = k3(PZ, I2, I2)
nzn = int(np.trace(nu2 @ (Z1 @ nu2 @ Z1)))
fg = Fr(int(np.trace(F2 @ G2)), 4)
check("M3 nu = 2W3 + 4GHZ-; nu = nu^T; <nu, Z1 nu Z1> < 0; tr(FG) < 0",
      nu_ok and np.array_equal(nu2, nu2.T) and nzn < 0 and fg < 0, "<nu,Z nu Z> = %d, tr(FG) = %s" % (nzn, fg))
w3_in_Z = all(is_psd_int(pt_on(w3m, k, 3).tolist()) for k in range(3))
check("M4 countercontrol: W3 in Z (PT_k(W3) PSD, k = 1,2,3) and <GHZ+, W3> < 0", w3_in_Z and w3ghz < 0)

# ============================================================================================ E  E3 ingredients
def hyperdet(a):
    a = {(i, j, k): Fr(a[4 * i + 2 * j + k]) for i in range(2) for j in range(2) for k in range(2)}
    g = lambda s: a[tuple(int(ch) for ch in s)]  # noqa: E731
    return (g("000") ** 2 * g("111") ** 2 + g("001") ** 2 * g("110") ** 2 + g("010") ** 2 * g("101") ** 2
            + g("100") ** 2 * g("011") ** 2
            - 2 * (g("000") * g("001") * g("110") * g("111") + g("000") * g("010") * g("101") * g("111")
                   + g("000") * g("100") * g("011") * g("111") + g("001") * g("010") * g("101") * g("110")
                   + g("001") * g("100") * g("011") * g("110") + g("010") * g("100") * g("011") * g("101"))
            + 4 * (g("000") * g("011") * g("101") * g("110") + g("001") * g("010") * g("100") * g("111")))


CNOT01 = np.zeros((8, 8), dtype=np.int64)
for x, y_, z in product(range(2), repeat=3):
    CNOT01[idx3(x, x ^ y_, z), idx3(x, y_, z)] = 1
plus_bell = np.kron(np.array([1, 1]), np.array(BELLV))       # 2 |+> Phi+ (unnormalized)
psi = CNOT01 @ plus_bell
psi3 = np.zeros(8, dtype=np.int64)
for i, j in product(range(2), repeat=2):
    psi3[idx3(i, i ^ j, j)] = 1
dets = {"CNOT(|+>Phi+) (x2)": hyperdet(psi), "GHZ (unnormalized)": hyperdet(GHZV), "psi3": hyperdet(psi3),
        "W": hyperdet([0, 1, 1, 0, 1, 0, 0, 0]), "|000>": hyperdet(basis([0, 0, 0])),
        "|0>Phi+": hyperdet([1, 0, 0, 1, 0, 0, 0, 0])}
check("E1 hyperdeterminants: nonzero for CNOT(|+>Phi+), GHZ, psi3; zero for W, |000>, |0>Phi+",
      dets["CNOT(|+>Phi+) (x2)"] != 0 and dets["GHZ (unnormalized)"] != 0 and dets["psi3"] != 0
      and dets["W"] == 0 and dets["|000>"] == 0 and dets["|0>Phi+"] == 0,
      "Det(CNOT(|+>Phi+)) = %s (normalized: /16), Det(GHZ unnorm.) = %s, Det(psi3) = %s"
      % (dets["CNOT(|+>Phi+) (x2)"], dets["GHZ (unnormalized)"], dets["psi3"]))
Bm = np.eye(2, dtype=np.int64)
Gh = np.zeros((2, 2, 2), dtype=np.int64)
Gh[0, 0, 0] = Gh[1, 1, 1] = 1
P3 = psi3.reshape(2, 2, 2)
vvec = np.einsum("aw,bx,kcd,wxk->abcd", Bm, Bm, Gh, P3)      # tokens (0,1,2,3); Gh on (6,2,3), psi3 on (4,5,6)
expect = np.zeros((2, 2, 2, 2), dtype=np.int64)
for i, j in product(range(2), repeat=2):
    expect[i, i ^ j, j, j] = 1
choi = np.zeros((2, 2, 2, 2), dtype=np.int64)                 # Choi of U|x,y> = |x+y, y>: in (0, 2), out (1, 3)
for x, y_ in product(range(2), repeat=2):
    choi[x, x ^ y_, y_, y_] = 1
check("E2 seven-token contraction = sum_ij |i>_0|i+j>_1|j>_2|j>_3 = Choi vector of a CNOT (in 0,2; out 1,3)",
      np.array_equal(vvec, expect) and np.array_equal(expect, choi))

# ============================================================================================ C  owner's distinction
cvec = np.zeros(16, dtype=np.int64)
for x, y_ in product(range(2), repeat=2):
    cvec[8 * x + 4 * y_ + 2 * x + (x ^ y_)] = 1               # |x y>_in |x, x+y>_out, order (a, b, c, d)
Cm = np.outer(cvec, cvec)
check("C1 C^2 = 4C and C^T = C", np.array_equal(Cm @ Cm, 4 * Cm) and np.array_equal(Cm, Cm.T))
Cop = Op.mat(Cm, ("a", "b", "c", "d"))
cuts = [("a", "b"), ("a", "c"), ("a", "d"), ("a",), ("b",), ("c",), ("d",)]
okc2, attain = True, []
for S in cuts:
    R4 = ptrace(Cop, [lab for lab in "abcd" if lab not in S]).reorder(S).matrix()   # = 4 x reduced state
    D = 2 * np.eye(R4.shape[0], dtype=np.int64) - R4                               # = 4 (I/2 - rho_S)
    okc2 &= is_psd_int(D.tolist())
    if det_int(D.tolist()) == 0:
        attain.append("".join(S))
check("C2 on all 7 cuts the reduced state of C/4 has largest eigenvalue <= 1/2", okc2,
      "cuts (in a,b; out c,d) attaining 1/2: %s" % attain)
trC, trC2 = int(np.trace(Cm)), int(np.trace(Cm @ Cm))
ratio = (Fr(trC, 16) - Fr(trC2, 32)) / (Fr(16, 16) - Fr(trC, 32))
check("C3 w = I/16 - C/32: tr(Cw)/tr(w) < 0", ratio < 0, "value %s" % ratio)

# ============================================================================================ J  E2 crossing calculus
xC = rand_int_op(("0", "2"))
yD = rand_int_op(("1", "3", "4"))


def lam_from(xop, R, P, g):
    """Lambda_x(g) = tr_R[(g_R (x) 1_P) x]."""
    full = tuple(xop.labels)
    return ptrace(mul(extend(g, full), xop.reorder(full)), list(R))


def lam_choi(J, R, P, g):
    """Lambda(g) = tr_R[(g^T (x) 1_P) J] from a Choi matrix J on (R, P)."""
    full = tuple(J.labels)
    gT = Op(g.t.transpose(list(range(len(g.labels), 2 * len(g.labels))) + list(range(len(g.labels)))), g.labels)
    return ptrace(mul(extend(gT, full), J.reorder(full)), list(R))


choi_x = None
okj1 = True
acc_t = np.zeros((2,) * 4, dtype=np.int64)
for i in range(2):
    for j in range(2):
        g = unit(i, j, ("2",))
        img = lam_from(xC, ("2",), ("0",), g)                         # operator on P = ("0",)
        acc_t = acc_t + tensor(g, img).reorder(("2", "0")).t
choi_x = Op(acc_t, ("2", "0"))
okj1 = same(choi_x, ptranspose(xC, ["2"]))
check("J1 Choi(Lambda_x) = PT_R(x) (R = token 2, P = token 0; random integer x)", okj1)
JX, JY = ptranspose(xC, ["2"]), ptranspose(yD, ["3", "4"])
fullS = ("0", "1", "2", "3", "4")
xy = extend(tensor(xC, yD), fullS)
okj2, failj3 = True, 0
for i in range(8):
    for j in range(8):
        f = unit(i, j, ("2", "3", "4"))
        cond = ptrace(mul(extend(f, fullS), xy), ["2", "3", "4"]).reorder(("0", "1"))
        iR, jR = i >> 2, j >> 2
        fR, fU = unit(iR, jR, ("2",)), unit(i & 3, j & 3, ("3", "4"))
        assert same(tensor(fR, fU), f)
        rebuilt = tensor(lam_choi(JX, ("2",), ("0",), fR), lam_choi(JY, ("3", "4"), ("1",), fU)).reorder(("0", "1"))
        okj2 &= same(cond, rebuilt)
        wrong = tensor(lam_choi(xC, ("2",), ("0",), fR), lam_choi(JY, ("3", "4"), ("1",), fU)).reorder(("0", "1"))
        failj3 += not same(cond, wrong)
check("J2 the crossing conditional equals Lambda'_x (x) Lambda'_y rebuilt from PT_R(x), PT_U(y), all 64 units", okj2)
check("J3 countercontrol: rebuilt from x without PT_R it fails", failj3 > 0, "%d/64 units fail" % failj3)

print("--- audit_eq4p: %d/%d checks pass" % (sum(RESULTS), len(RESULTS)))
print("VERDICT AUDIT-EQ4P-INDEPENDENT-EXACT" if all(RESULTS) else "VERDICT NOT RENDERED")
