#!/usr/bin/env python3
"""Coordinator's independent check of thread S2 (stage 2, PAIR-CONS). Written without the thread's code.

Decision rule, fixed before the first run:
- each check prints CONFIRMED or MISMATCH; each countercontrol prints CONFIRMED only if the
  predicted failure occurs;
- the verdict line is INDEP-S2-CONFIRMED iff every line is CONFIRMED, else INDEP-S2-MISMATCH
  (exit status 1).

Pre-registered convention latitude (C1, C2): the frame-covariance words are confirmed if they equal a
local rotation about the stated axis by +2*phi or -2*phi; the sign is printed, since the thread's
rotation convention is not reproduced here.

Exact arithmetic only (integers, Fractions, sympy rationals). Nothing nondeterministic is printed.

The landed predicates are re-implemented from CompositeDimension.lean:218-224:
- NativeGate.frame, relT, relC with z = z3 and N = nflip;
- posFwd and posInv hold for every signed-diagonal dressing by orthogonality [W].
"""
import itertools
import sys
from fractions import Fraction

import sympy as sp

RESULTS = []


def record(cid, kind, ok, text, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    line = f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} [{kind}] {text}"
    if detail != "":
        line += f" -- {detail}"
    print(line)


# ---------- integer tables: 4x4 lists, maps as functions on tables ----------
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot_t(w):
    return tuple(tuple((-1 if (m, n) in ((1, 3), (2, 2)) else 1) * w[PC[m][n]][PT[m][n]] for n in range(4)) for m in range(4))


def hm(diag3):
    return (1,) + tuple(diag3)


def actC_d(dg, w):
    h = hm(dg)
    return tuple(tuple(h[m] * w[m][n] for n in range(4)) for m in range(4))


def actT_d(dg, w):
    h = hm(dg)
    return tuple(tuple(w[m][n] * h[n] for n in range(4)) for m in range(4))


def basis(m, n):
    return tuple(tuple(1 if (i, j) == (m, n) else 0 for j in range(4)) for i in range(4))


BASIS = [basis(m, n) for m in range(4) for n in range(4)]


def as_matrix(f):
    """16x16 integer matrix of a linear map on tables (column k = image of basis k, flattened)."""
    cols = [f(b) for b in BASIS]
    return tuple(tuple(cols[k][i // 4][i % 4] for k in range(16)) for i in range(16))


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(16)) for j in range(16)) for i in range(16))


def apply(A, w):
    v = [w[i // 4][i % 4] for i in range(16)]
    out = [sum(A[i][k] * v[k] for k in range(16)) for i in range(16)]
    return tuple(tuple(out[4 * m + n] for n in range(4)) for m in range(4))


ID16 = tuple(tuple(1 if i == j else 0 for j in range(16)) for i in range(16))
SIGNS = list(itertools.product([1, -1], repeat=3))
NFLIP = (1, -1, -1)
REFLY = (1, -1, 1)
Z3 = (0, 0, 1)


def hom(x):
    return (1,) + tuple(x)


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return tuple(tuple(hx[m] * hy[n] for n in range(4)) for m in range(4))


def det_d(dg):
    return dg[0] * dg[1] * dg[2]


AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
AXPROD = [prodState(x, y) for x in AXES for y in AXES]
CNOT_M = as_matrix(cnot_t)


def dressing(D, E, Dp, Ep):
    return lambda w: actC_d(D, actT_d(E, cnot_t(actC_d(Dp, actT_d(Ep, w)))))


def corner(a):
    return tuple(((-1) ** a) * t for t in Z3)


print("== N  the fixed-frame native family under the landed NativeGate predicates (z3, nflip)")
gates = {}
for D, E, Dp, Ep in itertools.product(SIGNS, repeat=4):
    f = dressing(D, E, Dp, Ep)
    M = as_matrix(f)
    frame = all(apply(M, prodState(corner(a), corner(b))) == prodState(corner(a), corner((a + b) % 2))
                for a in range(2) for b in range(2))
    if not frame:
        continue
    relT = all(actT_d(NFLIP, apply(M, actT_d(NFLIP, b))) == apply(M, b) for b in BASIS)
    relC = all(actC_d(NFLIP, apply(M, actC_d(NFLIP, b))) == actT_d(NFLIP, apply(M, b)) for b in BASIS)
    if relT and relC:
        orient_pre = det_d(Dp) * det_d(Ep) == -1
        orient_post = det_d(D) * det_d(E) == -1
        gates.setdefault(M, set()).add((orient_pre, orient_post))
G_LIST = sorted(gates)
record("N1", "enumerate", len(G_LIST) == 32 and CNOT_M in gates,
       "of the 4096 signed-diagonal dressings of cnot, those meeting frame, relT and relC give exactly 32 distinct gates, cnot among them",
       f"{len(G_LIST)} gates")
pairs = {M: next(iter(s)) for M, s in gates.items()}
per_pair = {}
for M in G_LIST:
    per_pair[pairs[M]] = per_pair.get(pairs[M], 0) + 1
record("N2", "enumerate", all(len(s) == 1 for s in gates.values()) and sorted(per_pair.values()) == [8, 8, 8, 8]
       and pairs[CNOT_M] == (False, False),
       "each gate has one orientation pair (pre, post) over all its dressings; 8 gates per pair; cnot is (even, even)",
       str(sorted((str(k), v) for k, v in per_pair.items())))
LOCALS = {}
for D, E in itertools.product(SIGNS, repeat=2):
    LOCALS[as_matrix(lambda w, D=D, E=E: actC_d(D, actT_d(E, w)))] = (D, E)
okN3 = True
for Lm, (D, E) in LOCALS.items():
    conj = matmul(CNOT_M, matmul(Lm, CNOT_M))
    is_local = conj in LOCALS
    even = det_d(D) * det_d(E) == 1
    if is_local != even:
        okN3 = False
record("N3", "enumerate", okN3 and len(LOCALS) == 64,
       "absorption: cnot . L . cnot is a signed-diagonal local exactly for the 32 orientation-even locals L among the 64")


def has_negative(M):
    for p in AXPROD:
        q = apply(M, p)
        for a in AXES:
            ha = hom(a)
            for b in AXES:
                hb = hom(b)
                if sum(ha[m] * q[m][n] * hb[n] for m in range(4) for n in range(4)) < 0:
                    return True
    return False


okN4, n_odd = True, 0
for Gi in G_LIST:
    for Gj in G_LIST:
        odd = pairs[Gi][0] != pairs[Gj][1]
        n_odd += odd
        if has_negative(matmul(Gi, Gj)) != odd:
            okN4 = False
record("N4", "enumerate", okN4 and n_odd == 512,
       "over all 1024 ordered pairs, G_i . G_j has a negative product-effect value on axis data exactly when orient_pre(G_i) != orient_post(G_j)",
       f"odd pairs {n_odd}")
even_class = [M for M in G_LIST if pairs[M] == (False, False)]
group = {ID16}
frontier = [ID16]
while frontier:
    new = []
    for A in frontier:
        for g in even_class:
            B = matmul(g, A)
            if B not in group:
                group.add(B)
                new.append(B)
    frontier = new
CNOT_LOCALS = {matmul(CNOT_M, Lm) for Lm in LOCALS}
record("N5", "enumerate", len(group) == 16 and all(g in LOCALS or g in CNOT_LOCALS for g in group),
       "the even class generates a group of order 16, each element a local or cnot . local, so the generated cone is SEP + cnot SEP = K_gen",
       f"order {len(group)}")
SIG = as_matrix(lambda w: actT_d(REFLY, w))
odd_class = {M for M in G_LIST if pairs[M] == (True, True)}
record("N6", "enumerate", {matmul(SIG, matmul(M, SIG)) for M in even_class} == odd_class,
       "sigma = actT reflY conjugates the (even, even) class onto the (odd, odd) class")

print()
print("== R  carrier models for local tomography and finite rank")
Xs = sp.symbols("w0:16")
Wsym = sp.Matrix(4, 4, Xs)


def cnot_s(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in ((1, 3), (2, 2)) else 1) * w[PC[m][n], PT[m][n]])


CN = sp.Matrix(16, 16, lambda i, k: CNOT_M[i][k])
I16 = sp.eye(16)
Z16 = sp.zeros(16, 16)
Nreg = sp.BlockMatrix([[CN, I16 - CN], [CN, -CN]]).as_explicit()
N2 = Nreg * Nreg
record("R1", "identity", N2 == sp.diag(CN, CN) and N2 * N2 == sp.eye(32) and N2 != sp.eye(32),
       "register model N = [[cnot, I - cnot], [cnot, -cnot]]: N^2 = cnot (+) cnot, N^4 = I, N^2 != I")
pxz = prodState((1, 0, 0), (0, 0, 1))
v0 = sp.Matrix([pxz[i // 4][i % 4] for i in range(16)] + [0] * 16)
s1 = Nreg * v0
s2 = Nreg * s1
tab = lambda v: v[:16, 0]
okR2 = (tab(s1) == tab(s2) and tab(Nreg * s1) != tab(Nreg * s2)
        and tab(Nreg * v0) == CN * tab(v0) and all(tab(Nreg ** k * v0) in (tab(v0), CN * tab(v0)) for k in range(4)))
record("R2", "witness", okR2,
       "register model: product action holds; every generated table is p or cnot p (valid); s = N(pxz,0) and s' = N^2(pxz,0) have equal tables but N separates them: not LT")
h = sp.symbols("b0:16"), sp.symbols("c0:16")
Bv = sp.Matrix(16, 1, h[0])
Cv = sp.Matrix(1, 16, h[1])
dd = sp.Symbol("dd")
Nblk = sp.BlockMatrix([[CN, Bv], [Cv, sp.Matrix([[dd]])]]).as_explicit()
u = sp.Matrix(16, 1, sp.symbols("u0:16"))
vv = sp.Matrix(16, 1, sp.symbols("v0:16"))
emb = lambda x: x.col_join(sp.zeros(1, 1))
s_ = emb(u) + Nblk * emb(vv)
defect = (Nblk * s_)[:16, 0] - CN * s_[:16, 0] - Bv * (Cv * vv)
blockNN = (Nblk * Nblk)[:16, :16] - (I16 + Bv * Cv)
record("R3", "identity", all(sp.expand(e) == 0 for e in defect) and all(sp.expand(e) == 0 for e in blockNN),
       "block lemma (one hidden coordinate, symbolic B, C, D): on span(products u N.products) the table defect of N is exactly B C v, and the W3 block of N.N is I + B C")
Delta = sp.zeros(4, 4)
Delta[1, 1], Delta[1, 0] = 1, -1
Dl = sp.Matrix(16, 1, [Delta[i // 4, i % 4] for i in range(16)])
Nhid = sp.BlockMatrix([[CN, Dl], [sp.zeros(1, 16), sp.Matrix([[1]])]]).as_explicit()
E00v = sp.Matrix([1] + [0] * 15)
p_plus = E00v.col_join(sp.Matrix([[sp.Rational(1, 4)]]))
p_minus = E00v.col_join(sp.Matrix([[-sp.Rational(1, 4)]]))
tp, tm = (Nhid * p_plus)[:16, 0], (Nhid * p_minus)[:16, 0]
xs3, ys3 = sp.symbols("x1:4"), sp.symbols("y1:4")
form_t = sp.expand((sp.Matrix([1, *xs3]).T * (sp.Matrix(4, 4, list(tp)) - sp.Matrix(4, 4, list(E00v)) ) * sp.Matrix([1, *ys3]))[0, 0])
okR4 = (CN * Dl == -Dl and Nhid * Nhid == sp.eye(17) and p_plus[:16, 0] == p_minus[:16, 0] and tp != tm
        and form_t == sp.Rational(1, 4) * (xs3[0] * ys3[0] - xs3[0]))
record("R4", "witness", okR4,
       "hidden-parameter model N = [[cnot, Delta], [0, 1]] with Delta = E11 - E10 (cnot Delta = -Delta): N^2 = I; the ungenerated (E00, +-1/4) share a table and N separates them; images E00 +- Delta/4 are valid (|x1 y1 - x1| <= 2)")
SX, SZ = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[1, 0], [0, -1]])
SYr = sp.Matrix([[0, -1], [1, 0]])  # i*Y, real; Y (x) Y = -(iY) (x) (iY)
YY = -sp.kronecker_product(SYr, SYr)
OB = {"I": sp.eye(2), "X": SX, "Z": SZ}
UC = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


def rtab(rho):
    return {(a, b): sp.simplify((sp.kronecker_product(OB[a], OB[b]) * rho).trace()) for a in OB for b in OB}


def from_tab(t):
    return sum((t[(a, b)] * sp.kronecker_product(OB[a], OB[b]) for a in OB for b in OB), sp.zeros(4, 4)) / 4


XZ = sp.kronecker_product(SX, SZ)
tXZ = rtab(XZ / 4)
CC = rtab(UC * from_tab(rtab(UC * from_tab(tXZ) * UC.T)) * UC.T)
rho1 = (sp.eye(4) + YY) / 4
rho0 = sp.eye(4) / 4
mix = (sp.eye(4) - XZ) / 4
okR5 = (YY == YY.T and UC * XZ * UC.T == -YY and all(v == 0 for v in CC.values()) and any(v != 0 for v in tXZ.values())
        and rtab(rho1) == rtab(rho0) and rtab(UC * rho1 * UC.T) != rtab(UC * rho0 * UC.T)
        and UC * mix * UC.T == rho1 and all(ev >= 0 for ev in rho1.eigenvals()))
record("R5", "witness", okR5,
       "rebit control: Ad(CNOT) sends X(x)Z to -Y(x)Y, so its action on product tables kills X(x)Z (C.C != I); (I + Y(x)Y)/4 = CNOT image of a product mixture and I/4 share tables, CNOT tests separate them")
Dh = sp.Matrix([[0, -1], [1, -1]])  # order 3 on the hidden plane
N3m = sp.diag(CN, Dh)
okR6 = Dh ** 3 == sp.eye(2) and N3m * N3m != sp.eye(18) and all((N3m ** k * sp.Matrix(list(pxz[0]) + list(pxz[1]) + list(pxz[2]) + list(pxz[3]) + [0, 0]))[16:, 0] == sp.zeros(2, 1) for k in range(6))
record("R6", "witness", okR6,
       "order-type model N = cnot (+) D with D^3 = I on a hidden plane and generated preparations with zero hidden part: hidden part stays 0 (LT on the generated system) while N^2 != I on the carrier")


def is_square(k):
    r = int(round(k ** 0.5))
    return any((r + t) ** 2 == k for t in (-1, 0, 1) if r + t >= 0)


def sig(j):
    return sum(1 for k in range(j) if is_square(k)) % 2


def qrank(rows):
    A = [[Fraction(x) for x in r] for r in rows]
    rank, ncol = 0, len(A[0])
    for c in range(ncol):
        piv = next((r for r in range(rank, len(A)) if A[r][c] != 0), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        for r in range(len(A)):
            if r != rank and A[r][c] != 0:
                fct = A[r][c] / A[rank][c]
                A[r] = [x - fct * y for x, y in zip(A[r], A[rank])]
        rank += 1
    return rank


seq = [sig(j) for j in range(300)]
runs, cur, cnt = [], seq[1], 0
for v in seq[1:]:
    if v == cur:
        cnt += 1
    else:
        runs.append(cnt)
        cur, cnt = v, 1
ranks = {L: qrank([[seq[i + j] for j in range(L)] for i in range(L)]) for L in (8, 16, 32, 48, 64)}
period4 = [((j // 2) % 2) for j in range(300)]
rank_per = qrank([[period4[i + j] for j in range(64)] for i in range(64)])
rk = [ranks[L] for L in (8, 16, 32, 48, 64)]
record("R7", "enumerate", runs[:8] == [1, 3, 5, 7, 9, 11, 13, 15] and all(a < b for a, b in zip(rk, rk[1:])),
       "clock model (cnot at square clock times): the parity sequence has run lengths 1, 3, 5, ... from j = 1, and its L x L Hankel sections have strictly increasing rank over L = 8, 16, 32, 48, 64 (unboundedness is the written Kronecker/pigeonhole step)",
       f"ranks {ranks}")
record("R7c", "countercontrol", rank_per <= 4, "a periodic clock (period 4) gives a bounded Hankel rank (predicted)", f"rank {rank_per}")

print()
print("== M  the monomial and finite-group witnesses")
amp = [sp.Integer(3), sp.Integer(4), sp.Integer(0), sp.Integer(5)]
pat = [a ** 2 for a in amp]
okM1 = all(not (p[0] * p[3] == p[1] * p[2]) for p in itertools.permutations(pat))
record("M1", "enumerate", okM1, "psi_w = (3|00> + 4|01> + 5|11>)/sqrt 50: no arrangement of its modulus pattern (9,16,0,25)/50 is a rank-one 2x2 pattern")
psi = sp.Matrix(amp) / sp.sqrt(50)
C2 = sp.Matrix([[amp[0], amp[1]], [amp[2], amp[3]]]) / sp.sqrt(50)
rA = C2 * C2.T
bloch2 = sp.simplify((2 * rA[0, 1]) ** 2 + (rA[0, 0] - rA[1, 1]) ** 2)
a35 = sp.Matrix([[sp.Rational(3, 5)], [0], [sp.Rational(4, 5)]])
th = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
qa = sp.Matrix([sp.sqrt((1 + a35[2]) / 2), a35[0] / sp.sqrt(2 * (1 + a35[2]))])  # Bloch (3/5, 0, 4/5)
phi = th * sp.kronecker_product(qa, sp.Matrix([1, 0]))
Cphi = sp.Matrix([[phi[0], phi[1]], [phi[2], phi[3]]])
rB = Cphi * Cphi.T
bloch2b = sp.simplify((2 * rB[0, 1]) ** 2 + (rB[0, 0] - rB[1, 1]) ** 2)
record("M2", "witness", sp.simplify((psi.T * psi)[0, 0]) == 1 and bloch2 == sp.Rational(16, 25) and bloch2b == sp.Rational(16, 25),
       "psi_w is normalized with reduced Bloch length^2 16/25, equal to that of CNOT(|a>|0>) with Bloch(a) = (3/5, 0, 4/5): Schmidt-equivalent (Schmidt [L])",
       f"{bloch2}, {bloch2b}")
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
grp = {sp.ImmutableMatrix(sp.eye(4))}
front = [sp.eye(4)]
while front:
    nxt = []
    for A in front:
        for g in (th, SWAP):
            B = sp.ImmutableMatrix(g * A)
            if B not in grp:
                grp.add(B)
                nxt.append(B)
    front = nxt
okM3 = len(grp) == 6 and all(sp.Matrix([[x[0], x[1]], [x[2], x[3]]]).det() != 0 for x in (g.T * psi for g in grp))
record("M3", "witness", okM3, "<CNOT, SWAP> has order 6 and no element maps psi_w to a product vector: psi_w lies in no g(SEP) as a pure state", f"order {len(grp)}")

print()
print("== E  generated versus full effects, and the dual witness F")
CNs = CN
record("E1", "identity", CNs == CNs.T and CNs * CNs == I16,
       "cnot is a symmetric orthogonal involution on W3: the table of 'cnot then e(x)f' is cnot of the effect table, so generated effects = generated states (E_gen = K_gen)")
phiW = sp.Matrix(4, 4, lambda m, n: cnot_t(prodState((1, 0, 0), (0, 0, 1)))[m][n])
RH = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0], [0, 1, 0, 0]])
Tpsi = phiW * RH.T
F = sp.zeros(4, 4)
F[0, 0] = sp.Rational(1, 2)
F = F - Tpsi / 4
SG = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def pauliW(w):
    return sum((w[m, n] * sp.kronecker_product(SG[m], SG[n]) for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4


PT_ = pauliW(Tpsi)
okE2 = (Tpsi == sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]) and PT_ * PT_ == PT_ and PT_.trace() == 1)
record("E2", "witness", okE2, "T_psi = actT R_H phiW = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]] is a pure state (pauliW a rank-one projector)")
xv, yv = sp.Matrix([1, *xs3]), sp.Matrix([1, *ys3])
fF = sp.expand((xv.T * F * yv)[0, 0])
cF = sp.Matrix(4, 4, lambda m, n: cnot_t(tuple(tuple(int(4 * F[i, j]) for j in range(4)) for i in range(4)))[m][n]) / 4
fcF = sp.expand((xv.T * cF * yv)[0, 0])
M1 = sp.Matrix(3, 3, lambda i, j: -sp.Rational(1, 4) * Tpsi[i + 1, j + 1])
M2 = sp.Matrix(3, 3, lambda i, j: cF[i + 1, j + 1])
lin1 = sp.expand(fF - sp.Rational(1, 4) - (sp.Matrix(xs3).T * M1 * sp.Matrix(ys3))[0, 0])
lin2 = sp.expand(fcF - sp.Rational(1, 4) - (sp.Matrix(xs3).T * M2 * sp.Matrix(ys3))[0, 0])
sv1, sv2 = (M1.T * M1).eigenvals(), (M2.T * M2).eigenvals()
okE3 = lin1 == 0 and lin2 == 0 and max(sv1) <= sp.Rational(1, 16) and max(sv2) <= sp.Rational(1, 16) and cF[0, 0] == sp.Rational(1, 4)
record("E3", "identity", okE3,
       "F = E00/2 - T_psi/4: on products and on cnot images of products its value is 1/4 + x^T M y with |M| <= 1/4, so F is in dualW K_gen",
       f"M^T M eigenvalues {sv1}, {sv2}")
trFT = sp.simplify((pauliW(F) * PT_).trace())
record("E4", "witness", trFT == -sp.Rational(1, 8), "tr(rho(F) rho(T_psi)) = -1/8: F is not in Q3, so F is a non-generated effect", str(trFT))


def fourVal(X, Y, E, Fm):
    return sp.expand(sum(X[a, b] * Y[c, d] * E[a, c] * Fm[b, d]
                         for a in range(4) for b in range(4) for c in range(4) for d in range(4)))


v4 = fourVal(phiW, phiW, Tpsi / 4, F)
record("E5", "witness", v4 == -sp.Rational(1, 8),
       "uniform K_gen: famI(phiW, phiW, T_psi/4, F) = -1/8 with two non-generated effects (T_psi in Q3 is not in K_gen; F not in Q3)", str(v4))
v4c = fourVal(phiW, phiW, phiW / 4, phiW / 4)
record("E5c", "countercontrol", v4c >= 0, "with the generated effects phiW/4 in both slots the value is nonnegative (predicted)", str(v4c))

print()
print("== C  frame-covariance words")
c, s = sp.symbols("c s")
w16 = sp.Matrix(4, 4, Xs)


def homS(R):
    H = sp.eye(4)
    H[1:, 1:] = R
    return H


def aC(R, w):
    return homS(R) * w


def aT(R, w):
    return w * homS(R).T


def Cg(R, S):
    return lambda w: aC(R, aT(S, cnot_s(aC(R.T, aT(S.T, w)))))


I3 = sp.eye(3)
Rx = sp.Matrix([[1, 0, 0], [0, c, -s], [0, s, c]])
Rz = sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])
Xpi = sp.diag(1, -1, -1)
Zpi = sp.diag(-1, -1, 1)


def modc(expr):
    return sp.expand(sp.rem(sp.expand(expr), s ** 2 + c ** 2 - 1, s))


w1 = cnot_s(Cg(Rx, I3)(Cg(I3, Zpi)(Cg(Rx, Zpi)(w16))))
w2 = cnot_s(Cg(I3, Rz)(Cg(Xpi, I3)(Cg(Xpi, Rz)(w16))))
found1 = found2 = None
for sgn in (-1, 1):
    R2x = sp.Matrix([[1, 0, 0], [0, c ** 2 - s ** 2, -sgn * 2 * c * s], [0, sgn * 2 * c * s, c ** 2 - s ** 2]])
    R2z = sp.Matrix([[c ** 2 - s ** 2, -sgn * 2 * c * s, 0], [sgn * 2 * c * s, c ** 2 - s ** 2, 0], [0, 0, 1]])
    if found1 is None and all(modc(e) == 0 for e in (w1 - aC(R2x, w16))):
        found1 = sgn
    if found2 is None and all(modc(e) == 0 for e in (w2 - aT(R2z, w16))):
        found2 = sgn
record("C1", "identity", found1 is not None,
       "cnot . C(Rx,I) . C(I,Zpi) . C(Rx,Zpi) = actC(rotation about x by 2*sgn*phi), symbolic modulo c^2 + s^2 = 1",
       f"sgn {found1}")
record("C2", "identity", found2 is not None,
       "cnot . C(I,Rz) . C(Xpi,I) . C(Xpi,Rz) = actT(rotation about z by 2*sgn*phi), symbolic modulo c^2 + s^2 = 1",
       f"sgn {found2}")
inst = {c: sp.Rational(3, 5), s: sp.Rational(4, 5)}
pz = sp.Matrix(4, 4, lambda m, n: prodState((0, 0, 1), (1, 0, 0))[m][n])
img = cnot_s(Cg(Rx.subs(inst), I3)(pz))
record("C1c", "countercontrol", img.rank() > 1,
       "cnot . C(Rx,I) alone sends a product to a table of rank > 1 at phi = atan(4/3): it is not local (predicted)", f"rank {img.rank()}")

n_ok = sum(RESULTS)
print()
print(f"checks: {len(RESULTS)}, confirmed: {n_ok}")
verdict = "INDEP-S2-CONFIRMED" if n_ok == len(RESULTS) else "INDEP-S2-MISMATCH"
print(f"VERDICT {verdict}")
sys.exit(0 if verdict == "INDEP-S2-CONFIRMED" else 1)
