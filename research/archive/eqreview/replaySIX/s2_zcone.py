"""EQ4-SIX probe s2 -- Z and the K_A orbit hull: exact GD-sector certificates.  Research only.

Usage:  python3 -I -B s2_zcone.py <base>/verification/lean-mathlib/OIBridge
Imports only the copied library eq4_lib.py (sha256 cc2c6aca94007ac8).

Z = {X : PT_j X >= 0, j = 1, 2, 3}; Z* = cone(PT_1 PSD, PT_2 PSD, PT_3 PSD) (closed; GL^3-, S_3- and T-invariant).
Written (NOTES N2.3).  For a GHZ-diagonal g, g is in Z* iff <g, z> >= 0 for every z in Z^GD := Z cap GD, because the
GHZ-stabilizer twirl is an average of local unitaries, self-adjoint, fixing g and mapping Z onto Z^GD.  In fibre
coordinates (P_b = x_{b+} + x_{b-}, C_b = x_{b+} - x_{b-}, b = 2 b1 + b2) PT_1, PT_2, PT_3 map the coherence of fibre b
to fibre b xor 3, b xor 2, b xor 1 and keep the populations, so Z^GD = {|C_c| <= P_b for all b != c}.
Consequence: if every generator of K_A lies in Z*, then Lift(K_A) <= Z* (Z* closed, convex, filter-invariant) and
hence Z <= Lift(K_A)*: every element of Z is admissible against the whole orbit hull of K_A.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `S2-ZCONE-EXACT` iff all:
  K  transcription control.
  P  operator check of the fibre rule: for each j and each GHZ projector P_i (8), PT_j(P_i) is GHZ-diagonal with the
     predicted (P, C) (exact, eq4_lib operators); countercontrol: the rule with b xor 3 and b xor 1 exchanged fails.
  D  exact double description of Z^GD (constraints P_b +- C_c >= 0, b != c, and P_b >= 0; standard incremental DD
     from a simplicial start with the rank adjacency test) in two constraint orders: same ray set; every ray satisfies
     all constraints with a tight set of rank 7; control: the same code on the orthant returns the 8 unit vectors.
  G  every one of the 92 K_A generators pairs >= 0 with every extreme ray of Z^GD (so K_A <= Z* cap GD); the minimum
     pairing value is printed; countercontrol: GHZ+ = e_0 pairs < 0 with some ray (GHZ not in Z*).
  C  every extreme ray of Z^GD satisfies the 92 inequalities of K_A (Z^GD <= K_A = K_A*); countercontrol: the vector
     nu = I - 2 GHZ+ + 4 GHZ- (in BS* cap Z*) violates some K_A inequality.
"""
import itertools
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("s2_zcone")
rep.check("K0 transcription control", L.transcription_control(BASE)[0])
X3 = (0, 1, 2)


def idx(x, y, z):
    return 4 * x + 2 * y + z


PJ = []
VEC = []
for b in range(4):
    b1, b2 = b >> 1, b & 1
    for t in range(2):
        v = [0] * 8
        v[idx(0, b1, b2)] = 1
        v[idx(1, 1 - b1, 1 - b2)] = 1 if t == 0 else -1
        VEC.append(v)
        PJ.append(L.ket_op(v, X3).scale(Fr(1, 2)))


def gd_coords(X):
    """GHZ-basis coordinates if X is GHZ-diagonal, else None."""
    xs = [L.pair(Pj, X) for Pj in PJ]
    Y = L.Op(X3, {})
    for c, Pj in zip(xs, PJ):
        Y = Y + Pj.scale(c)
    return [c.re for c in xs] if Y == X else None


def fib(x):
    return [x[2 * b] + x[2 * b + 1] for b in range(4)], [x[2 * b] - x[2 * b + 1] for b in range(4)]


ok_p = True
ok_pc = False
XOR = {0: 3, 1: 2, 2: 1}   # token index -> xor applied to the fibre label of the coherence
for j in range(3):
    for i in range(8):
        Y = L.ptranspose(PJ[i], [j])
        xc = gd_coords(Y)
        if xc is None:
            ok_p = False
            continue
        P0, C0 = fib([1 if k == i else 0 for k in range(8)])
        P1, C1 = fib(xc)
        ok_p &= P1 == P0 and all(C1[b] == C0[b ^ XOR[j]] for b in range(4))
        wrong = {0: 1, 1: 2, 2: 3}[j]
        if not all(C1[b] == C0[b ^ wrong] for b in range(4)):
            ok_pc = True
rep.check("P fibre rule: PT_1, PT_2, PT_3 keep P_b and move C_b to fibre b xor 3, 2, 1 (exact on all 8 GHZ projectors); "
          "countercontrol with the labels permuted fails", ok_p and ok_pc)


# ------------------------------------------------------------------------------------------------ exact DD
def to_x(P, C):
    out = []
    for b in range(4):
        out += [Fr(P[b] + C[b], 2), Fr(P[b] - C[b], 2)]
    return out


def lin_from_PC(cP, cC):
    """linear functional in x-coordinates equal to sum cP_b P_b + cC_b C_b."""
    out = []
    for b in range(4):
        out += [Fr(cP[b] + cC[b]), Fr(cP[b] - cC[b])]
    return out


CONS = []
for b in range(4):
    e = [0] * 4
    e[b] = 1
    CONS.append(lin_from_PC(e, [0] * 4))
for b in range(4):
    for c in range(4):
        if b == c:
            continue
        for s in (1, -1):
            cp = [0] * 4
            cc = [0] * 4
            cp[b] = 1
            cc[c] = s
            CONS.append(lin_from_PC(cp, cc))


def dot(a, b):
    return sum(Fr(x) * Fr(y) for x, y in zip(a, b))


def rank(rows):
    M = [[Fr(x) for x in r] for r in rows]
    rk = 0
    if not M:
        return 0
    for c in range(len(M[0])):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]
                M[i] = [M[i][k] - f * M[rk][k] for k in range(len(M[0]))]
        rk += 1
    return rk


def normalize(v):
    m = max(abs(x) for x in v)
    return tuple(Fr(x) / m for x in v)


def inv_cols(B):
    """columns of the inverse of the square matrix B (rows = constraints): r_k with B r_k = e_k."""
    n = len(B)
    M = [[Fr(x) for x in B[i]] + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][k] - f * M[c][k] for k in range(2 * n)]
    return [tuple(M[i][n + k] for i in range(n)) for k in range(n)]


def dd(cons, dim):
    """extreme rays of the pointed cone {x : c.x >= 0 for c in cons}: start from a simplicial cone on dim linearly
    independent constraints (rays = columns of the inverse), then add the remaining constraints one at a time; a new ray
    is formed from a (positive, negative) pair only if their common tight set among the used constraints has rank
    dim - 2 (adjacency in a pointed cone)."""
    basis = []
    for c in cons:
        if rank(basis + [c]) > len(basis):
            basis.append(c)
        if len(basis) == dim:
            break
    gens = [normalize(r) for r in inv_cols(basis)]
    used = list(basis)
    for c in cons:
        if c in basis:
            continue
        pos = [g for g in gens if dot(c, g) > 0]
        zer = [g for g in gens if dot(c, g) == 0]
        neg = [g for g in gens if dot(c, g) < 0]
        new = []
        for gp in pos:
            for gn in neg:
                tight = [u for u in used if dot(u, gp) == 0 and dot(u, gn) == 0]
                if rank(tight) != dim - 2:
                    continue
                a = dot(c, gp)
                bneg = -dot(c, gn)
                new.append(normalize(tuple(bneg * x + a * y for x, y in zip(gp, gn))))
        gens = list(dict.fromkeys(pos + zer + new))
        used.append(c)
    return set(gens)


R1 = dd(CONS, 8)
R2 = dd(list(reversed(CONS)), 8)
orth = dd([[Fr(1 if i == k else 0) for i in range(8)] for k in range(8)], 8)
ok_d = (R1 == R2 and all(all(dot(c, r) >= 0 for c in CONS) for r in R1)
        and all(rank([c for c in CONS if dot(c, r) == 0]) == 7 for r in R1)
        and orth == {tuple(Fr(1 if i == k else 0) for i in range(8)) for k in range(8)})
rep.check("D exact double description of Z^GD: %d extreme rays, two constraint orders agree, all feasible with tight rank "
          "7; orthant control returns the 8 unit vectors" % len(R1), ok_d)
RAYS = sorted(R1)

# K_A generators
KA = []
for j, k in itertools.combinations(range(8), 2):
    KA.append([Fr(1 if i in (j, k) else 0) for i in range(8)])
for j in range(8):
    KA.append([Fr(1 - 2 * (i == j)) for i in range(8)])
for j in range(8):
    for p in range(8):
        if p != j:
            KA.append([Fr(1 - 2 * (i == j) + 2 * (i == p)) for i in range(8)])
minval = min(dot(g, r) for g in KA for r in RAYS)
e0 = [Fr(1 if i == 0 else 0) for i in range(8)]
ce0 = min(dot(e0, r) for r in RAYS)
rep.check("G all %d K_A generators pair >= 0 with all extreme rays of Z^GD (min %s): K_A <= Z* cap GD, hence "
          "Lift(K_A) <= Z* and Z <= Lift(K_A)*; countercontrol GHZ+ pairs to %s < 0" % (len(KA), minval, ce0),
          minval >= 0 and ce0 < 0)
ok_c = all(dot(g, r) >= 0 for r in RAYS for g in KA)
nu = [Fr(-1), Fr(5)] + [Fr(1)] * 6
cnu = min(dot(nu, g) for g in KA)
rep.check("C every extreme ray of Z^GD satisfies the 92 K_A inequalities (Z^GD <= K_A); countercontrol nu = (-1, 5, 1^6) "
          "violates one (min %s < 0)" % cnu, ok_c and cnu < 0)
rep.note("extreme rays of Z^GD (x-coordinates): %s" % [tuple(str(v) for v in r) for r in RAYS])
rep.verdict("S2-ZCONE-EXACT")
