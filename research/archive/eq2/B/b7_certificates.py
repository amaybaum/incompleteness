"""B7 (node N7 inputs) -- exact l-module facts for the lemma tree, and the sizes of the exact certificates a governed round
would carry.

Decision rule (fixed before the run):
  * Hom_l(A, B) for A, B in {l, M1, M2, N} is reported from exact rank computations of the intertwiner equations
    (C ad_A(Y) = ad_B(Y) C for the six generators Y of l), with the controls dim End_l(M1) = 1 (EQ-C 2.5a) and
    dim Hom_l(M1, M2) = 1 (EQ-C 2.5b) reproduced;
  * certificate sizes are reported only for exact rank certificates that reproduce the known ranks: V1's sampled system
    rank 207 (EQ-C P2) and the native tangent-block system rank 124 = 128 - 4 (B1), each from a greedily minimized set
    of rational sample points, with the height (largest numerator or denominator) of the sampled rows.
Usage: python3 -I -B b7_certificates.py <base>/verification/lean-mathlib/OIBridge/CompositeDimension.lean
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eq2b_lib import *  # noqa

rep = Report("B7 module facts and certificate sizes")
CNOT = parse_kernel_cnot(sys.argv[1])[0]
L_ = [ad_herm(SIG2[(i, 0)]) for i in (1, 2, 3)] + [ad_herm(SIG2[(0, j)]) for j in (1, 2, 3)]
M1 = [ad_herm(SIG2[(i, j)]) for i in (1, 2, 3) for j in (1, 2, 3)]
M2 = [mmul(mmul(RB, m), RB) for m in M1]


def so3gen(k):
    J = [[Fr(0)] * 3 for _ in range(3)]
    i, j = [(1, 2), (2, 0), (0, 1)][k]
    J[i][j], J[j][i] = Fr(-1), Fr(1)
    return J


def corr_tensor(A, B):
    X = zeros(16, 16)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l_ in range(3):
                    v = A[i][k] * B[j][l_]
                    if v != 0:
                        X[4 * (i + 1) + (j + 1)][4 * (k + 1) + (l_ + 1)] += v
    return X


NN = [corr_tensor(so3gen(a), so3gen(b)) for a in range(3) for b in range(3)]
fl = lambda S: [flat(X) for X in S]  # noqa


def coords(basis, X):
    n = len(basis)
    rows = [list(r) + [x] for r, x in zip(zip(*fl(basis)), flat(X))]
    piv, R = rref(rows, n + 1)
    assert n not in piv, "not in span"
    c = [Fr(0)] * n
    for k, p in enumerate(piv):
        c[p] = R[k][n]
    return c


def ad_matrices(basis):
    """for each generator Y of l, the matrix of ad_Y on span(basis) (requires invariance)."""
    out = []
    for Y in L_:
        cols = [coords(basis, bracket(Y, b)) for b in basis]
        out.append([[cols[j][i] for j in range(len(basis))] for i in range(len(basis))])
    return out


AD = {name: ad_matrices(B) for name, B in [("l", L_), ("M1", M1), ("M2", M2), ("N", NN)]}


def hom_dim(A, B):
    """dim {C : C ad_A = ad_B C} for C a (dim B) x (dim A) matrix."""
    da, db = len(AD[A][0]), len(AD[B][0])
    nv = da * db
    rows = []
    for k in range(6):
        DA, DB = AD[A][k], AD[B][k]
        for i in range(db):
            for j in range(da):
                row = [Fr(0)] * nv
                for t in range(da):
                    if DA[t][j] != 0:
                        row[i * da + t] += DA[t][j]
                for t in range(db):
                    if DB[i][t] != 0:
                        row[t * da + j] -= DB[i][t]
                rows.append(row)
    return nv - rank(rows, nv)


names = ["l", "M1", "M2", "N"]
table = {(a, b): hom_dim(a, b) for a in names for b in names}
rep.note("dim Hom_l(A, B) (rows A, columns B): " + "; ".join(
    f"{a}: " + ", ".join(f"{b}={table[(a, b)]}" for b in names) for a in names))
rep.check("M.1 controls: dim End_l(M1) = 1 and dim Hom_l(M1, M2) = 1 (EQ-C 2.5a-b reproduced)",
          table[("M1", "M1")] == 1 and table[("M1", "M2")] == 1)
rep.check("M.2 Hom_l(M1, l) = Hom_l(M2, l) = 0 and Hom_l(l, M1) = 0: the su(4) part has no l-equivariant map to or from l "
          "(used in step e: an l-submodule strictly containing l inside l + M1 is l + M1)",
          table[("M1", "l")] == 0 and table[("M2", "l")] == 0 and table[("l", "M1")] == 0)
rep.check("M.3 N is isomorphic to M1 as an l-module (dim Hom_l(M1, N) = 1 = dim End_l(N)): V1's (3,3)-isotypic part has "
          "multiplicity 3, so N must be removed (by the invariant form) before the submodule analysis",
          table[("M1", "N")] == 1 and table[("N", "N")] == 1 and table[("N", "l")] == 0)


# ---------------------------------------------------------------- certificate sizes
def unit_vec(s, t):
    s, t = F(s), F(t)
    d = 1 + s * s + t * t
    return [2 * s / d, 2 * t / d, (s * s + t * t - 1) / d]


POOLP = [(0, 0), (1, 0), (0, 1), (2, 0), (0, 3), (1, 1), (Fr(1, 2), 2), (3, -1), (-2, Fr(1, 3)), (Fr(2, 5), Fr(-3, 4)),
         (5, 7), (-1, -4), ("e1",), ("e2",), ("e3",), ("-e1",), ("-e2",)]


def pt(p):
    if len(p) == 1:
        return {"e1": [1, 0, 0], "e2": [0, 1, 0], "e3": [0, 0, 1], "-e1": [-1, 0, 0], "-e2": [0, -1, 0]}[p[0]]
    return unit_vec(*p)


def v1_rows(x, y):
    w = vec(prodState(x, y))
    hx, hy = [Fr(1)] + [-F(c) for c in x], [Fr(1)] + [-F(c) for c in y]
    rows = []
    for n in range(4):
        row = [Fr(0)] * 240
        for m in range(4):
            r = 4 * m + n
            if r:
                for c in range(16):
                    if w[c] != 0:
                        row[(r - 1) * 16 + c] += hx[m] * w[c]
        rows.append(row)
    for m in range(4):
        row = [Fr(0)] * 240
        for n in range(4):
            r = 4 * m + n
            if r:
                for c in range(16):
                    if w[c] != 0:
                        row[(r - 1) * 16 + c] += hy[n] * w[c]
        rows.append(row)
    return rows


class Inc:
    """Incremental exact echelon basis over Q (pivot -> normalized row)."""

    def __init__(self, n):
        self.n, self.basis = n, {}

    def add(self, v):
        v = list(v)
        for c in sorted(self.basis):
            if v[c] != 0:
                f = v[c]
                v = [a - f * b for a, b in zip(v, self.basis[c])]
        for c in range(self.n):
            if v[c] != 0:
                inv = 1 / v[c]
                v = [x * inv for x in v]
                for c2 in list(self.basis):
                    if self.basis[c2][c] != 0:
                        f = self.basis[c2][c]
                        self.basis[c2] = [a - f * b for a, b in zip(self.basis[c2], v)]
                self.basis[c] = v
                return True
        return False


def greedy(row_fn, pool, target, ncols):
    inc, chosen, rows = Inc(ncols), [], []
    for p in pool:
        for q in pool:
            new = row_fn(pt(p), pt(q))
            gained = [inc.add(r) for r in new]
            if any(gained):
                chosen.append((p, q))
                rows += new
            if len(inc.basis) == target:
                return chosen, rows, len(inc.basis)
    return chosen, rows, len(inc.basis)


chosen, rowsV, rV = greedy(v1_rows, POOLP, 207, 240)
height = max(max(abs(x.numerator), x.denominator) for row in rowsV for x in row)
rep.check(f"C.1 V1 certificate: {len(chosen)} rational sphere pairs ({len(rowsV)} rows of length 240) already give the exact "
          f"rank 207 of EQ-C P2 (dim V1 <= 33); row height {height}", rV == 207, f"pairs {chosen[:4]}...")


def tangent_rows(y, _unused=None):
    """B1's C3 rows (tightness at P = 0) for the unit target y, over the 128 tangent unknowns."""
    hy = hom(y)
    b = hom([-F(c) for c in y])
    rows = []
    for ti in (0, 1):
        for mu in range(4):
            row = [Fr(0)] * 128
            for l in range(4):
                for nu in range(4):
                    if hy[l] != 0 and b[nu] != 0:
                        row[(ti * 4 + l) * 16 + 4 * mu + nu] += hy[l] * b[nu]
            rows.append(row)
    return rows


NT = homMap(NFLIP)
ACN, ATN = actC(NFLIP), actT(NFLIP)
base_rows = []
for ti in (0, 1):
    A = madd(mscale(ACN, NT[ti + 1][ti + 1]), ATN, 1, -1)
    for l in range(4):
        for r in range(16):
            base_rows.append([A[r][o] if k == (ti * 4 + l) else Fr(0) for k in range(8) for o in range(16)])
for ti in (0, 1):
    for l in range(4):
        for nu in range(4):
            for mu in (0, 3):
                row = [Fr(0)] * 128
                row[(ti * 4 + l) * 16 + 4 * mu + nu] = Fr(1)
                base_rows.append(row)
r0 = rank(base_rows, 128)
chosenT, rowsT = [], list(base_rows)
rT = r0
for p in POOLP:
    new = tangent_rows(pt(p))
    rr = rank(rowsT + new, 128)
    if rr > rT:
        chosenT.append(p)
        rowsT += new
        rT = rr
    if rT == 124:
        break
rep.check(f"C.2 native-class certificate: relC + corner rows (rank {r0}) plus the tightness rows of {len(chosenT)} rational "
          f"targets give rank 124 = 128 - 4 (B1's 4-parameter family)", rT == 124 and r0 == 96, f"targets {chosenT}")
rep.verdict("MODULE-FACTS-AND-CERTIFICATES: Hom_l(M1, l) = 0, N ~ M1 as l-modules; V1's upper bound needs a few dozen "
            "rational sample pairs, the native class only a handful of targets")
