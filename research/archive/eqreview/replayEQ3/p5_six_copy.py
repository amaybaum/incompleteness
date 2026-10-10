"""EQ3-P probe p5 -- what the six-copy instance gives at three copies (exact link identities).  Research only; base
bcbc516f.  Usage (from scratchpad/eq3/P):
  python3 -I -B p5_six_copy.py <base>/.../OIBridge/CompositeDimension.lean

Instance KT(6): triples (0,1,2) and (3,4,5) with cones K_012, K_345 (closed, full IsEffectOn effect sets); link pairs
(0,3), (1,4), (2,5), each a standalone pair composite with its native gate (so, by the four-copy result, Q3 or the twin
in its token charts).  Groupings used: 012|345 (state products X(012) Y(345); effect products e(012) f(345);
conditioning), 03|1425 and 14|25 (to form the link product L(03) L'(14) L''(25) as a state, or the effect product
E(03) F(14) G(25)).  Three-copy tables T[m0,m1,m2] (index 0 the unit), operator pauli3 = (1/8) sum T sigma (x) sigma (x)
sigma, coords3(rho) = tr(rho sigma (x) sigma (x) sigma); effect tables pair by the Euclidean pairing.
CLAIMS:
  S1 family (i3): sum X[a,b,c] Y[d,e,f] E[a,d] F[b,e] G[c,f] = <X, (E (x) F (x) G) . Y> (symbolic)
  S2 family (ii3): conditioning L(03) L'(14) L''(25) on f(345) leaves (L (x) L' (x) L'') . f on (0,1,2) (symbolic)
  S3 Bell links: (Delta (x) Delta (x) Delta) . f = T3 f (signs s_m0 s_m1 s_m2) and pauli3(T3 f) = pauli3(f)^T
     (symbolic f): (I3) T3(K_345*) <= K_012 [Bell STATES on 03, 14, 25; effect products on 012|345; conditioning] and
     (II3) K_012 <= T3(K_345*) [state products on 012|345; Bell EFFECTS on 03, 14, 25]
  S4 filter links: (L_a (x) Delta (x) Delta) . f = 2 coords3(Ad(D (x) 1 (x) 1)(pauli3(T3 f))) with D = diag(1, u) (symbolic
     f, u), and the same on the third copy: with K_012 = T3(K_345*) every local diagonal filter (and, through the general
     links of p3, every local filter) maps K_012 into itself: SLOCC invariance of the three-copy cone
  S5 twin links: (idW (x) idW (x) idW) . f = f; a mixed set (Delta (x) idW (x) idW) gives PT on copy 0:
     pauli3((Delta (x) 1 (x) 1) . f) = PT_0(pauli3 f) (symbolic)
  S6 operator cross-check of S1 by explicit 6-qubit placement and trace (one random exact instance)
  S7 GHZ-class invariant: the Cayley hyperdeterminant Det is 1 on |000> + |111>, 0 on |001> + |010> + |100> and on a
     biseparable |0>(|00> + |11>), and Det(C psi) = det(C0)^2 det(C1)^2 det(C2)^2 Det(psi) (two random exact instances)
DECISION RULE (fixed before the first run): verdict `P5-SIX-COPY-EXACT` iff all pass.  Exact arithmetic only.
"""
import itertools
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq3_lib as L  # noqa: E402

check = L.check
cnot = L.cnot_from(L.parse_cnot(sys.argv[1]))
DEL = L.DELTA
idW = eye(4)
IDX = list(itertools.product(range(4), repeat=3))
rng = random.Random(606)


def symtab3(name):
    return {t: sp.Symbol(f"{name}{t[0]}{t[1]}{t[2]}", real=True) for t in IDX}


def apply3(M0, M1, M2, Tb):
    return {(a, b, c): sp.expand(sum(M0[a, d] * M1[b, e] * M2[c, f] * Tb[(d, e, f)]
                                     for d in range(4) for e in range(4) for f in range(4)
                                     if M0[a, d] != 0 and M1[b, e] != 0 and M2[c, f] != 0))
            for (a, b, c) in IDX}


def eucl3(A, B):
    return sp.expand(sum(A[t] * B[t] for t in IDX))


def T3(Tb):
    return {t: L.SGNY[t[0]] * L.SGNY[t[1]] * L.SGNY[t[2]] * Tb[t] for t in IDX}


def pauli3(Tb):
    out = zeros(8, 8)
    for t, v in Tb.items():
        if v != 0:
            out += v * L.kron(L.PAULI[t[0]], L.PAULI[t[1]], L.PAULI[t[2]])
    return (out / 8).applyfunc(sp.expand)


def coords3(rho):
    return {t: sp.expand((rho * L.kron(L.PAULI[t[0]], L.PAULI[t[1]], L.PAULI[t[2]])).trace()) for t in IDX}


def zero3(A, B):
    return all(sp.expand(A[t] - B[t]) == 0 for t in IDX)


def pair_sym(name):
    return Matrix(4, 4, lambda m, n: sp.Symbol(f"{name}{m}{n}", real=True))


# ---------------------------------------------------------------- S1, S2
X, Y = symtab3("X"), symtab3("Y")
E, F, G = pair_sym("E"), pair_sym("F"), pair_sym("G")
lhs1 = sp.expand(sum(X[(a, b, c)] * Y[(d, e, f)] * E[a, d] * F[b, e] * G[c, f]
                     for (a, b, c) in IDX for (d, e, f) in IDX))
check("S1 family (i3): sum X[abc] Y[def] E[ad] F[be] G[cf] = <X, (E (x) F (x) G).Y> (symbolic)",
      sp.expand(lhs1 - eucl3(X, apply3(E, F, G, Y))) == 0)
fT = symtab3("f")
La_, Lb_, Lc_ = pair_sym("l"), pair_sym("m"), pair_sym("n")
cond = {(a, b, c): sp.expand(sum(La_[a, d] * Lb_[b, e] * Lc_[c, g] * fT[(d, e, g)]
                                 for d in range(4) for e in range(4) for g in range(4))) for (a, b, c) in IDX}
check("S2 family (ii3): conditioning L(03) L'(14) L''(25) on f(345) leaves (L (x) L' (x) L'').f on (0,1,2) (symbolic)",
      zero3(cond, apply3(La_, Lb_, Lc_, fT)))

# ---------------------------------------------------------------- S3 Bell links
check("S3 (Delta (x) Delta (x) Delta).f = T3 f and pauli3(T3 f) = pauli3(f)^T (symbolic f)",
      zero3(apply3(DEL, DEL, DEL, fT), T3(fT)) and L.zero(pauli3(T3(fT)) - pauli3(fT).T))
check("S3 Bell links come from the standalone pair gate: cnot(prodState xplus z3) = Delta (state) and "
      "cnot(prodState xplus z3)/4 = cnot(sharp (x) sharp) (effect, dual action)", cnot(L.prod_state(L.XPLUS, L.Z3)) == DEL)

# ---------------------------------------------------------------- S4 filter links
ur, ui, wr, wi = sp.symbols("ur ui wr wi", real=True)
u, w = ur + I * ui, wr + I * wi


def proj(v):
    return (v * v.H).applyfunc(sp.expand)


def link(z):
    ca = L.coords1(proj(Matrix([1, z])))
    hz = L.hom(L.Z3)
    return cnot(Matrix(4, 4, lambda m, n: ca[m] * hz[n]))


D0 = L.kron(sp.diag(1, u), L.S0, L.S0)
lhs4 = apply3(link(u), DEL, DEL, fT)
rhs4 = {t: 2 * v for t, v in coords3(L.ad(D0, pauli3(T3(fT)))).items()}
check("S4 (L_a (x) Delta (x) Delta).f = 2 coords3(Ad(diag(1,u) (x) 1 (x) 1)(pauli3(T3 f))) (symbolic f, u)",
      zero3(lhs4, rhs4))
D2 = L.kron(L.S0, L.S0, sp.diag(1, w))
lhs4b = apply3(DEL, DEL, link(w), fT)
rhs4b = {t: 2 * v for t, v in coords3(L.ad(D2, pauli3(T3(fT)))).items()}
check("S4 the same on the third copy: (Delta (x) Delta (x) L_a'').f = 2 coords3(Ad(1 (x) 1 (x) diag(1,w))(pauli3(T3 f)))",
      zero3(lhs4b, rhs4b))

# ---------------------------------------------------------------- S5 twin and mixed links
check("S5 twin links: (idW (x) idW (x) idW).f = f; mixed (Delta (x) idW (x) idW).f has operator PT_0(pauli3 f) "
      "(symbolic)", zero3(apply3(idW, idW, idW, fT), fT)
      and L.zero(pauli3(apply3(DEL, idW, idW, fT)) - L.pt_copy(pauli3(fT), 0, 3)))

# ---------------------------------------------------------------- S6 operator cross-check
rX, rY = L.rand_herm(rng, 8), L.rand_herm(rng, 8)
oE, oF, oG = (L.rand_herm(rng, 4) for _ in range(3))
Xt, Yt = coords3(rX), coords3(rY)
Et, Ft, Gt = L.coordsW(oE) / 4, L.coordsW(oF) / 4, L.coordsW(oG) / 4
Mst = L.place([((0, 1, 2), rX), ((3, 4, 5), rY)], 6)
Mef = L.place([((0, 3), oE), ((1, 4), oF), ((2, 5), oG)], 6)
opval = sp.expand((Mef * Mst).trace())
check("S6 explicit 6-qubit trace tr((E(03) F(14) G(25)) (rho_X(012) rho_Y(345))) equals <X, (E (x) F (x) G).Y> with "
      "state tables coords3(rho) and effect tables coordsW(op)/4 (random exact instance)",
      sp.expand(opval - eucl3(Xt, apply3(Et, Ft, Gt, Yt))) == 0)

# ---------------------------------------------------------------- S7 hyperdeterminant
def hdet(a):
    g = lambda i, j, k: a[4 * i + 2 * j + k]  # noqa: E731
    return sp.expand(g(0, 0, 0) ** 2 * g(1, 1, 1) ** 2 + g(0, 0, 1) ** 2 * g(1, 1, 0) ** 2
                     + g(0, 1, 0) ** 2 * g(1, 0, 1) ** 2 + g(1, 0, 0) ** 2 * g(0, 1, 1) ** 2
                     - 2 * (g(0, 0, 0) * g(0, 0, 1) * g(1, 1, 0) * g(1, 1, 1) + g(0, 0, 0) * g(0, 1, 0) * g(1, 0, 1) * g(1, 1, 1)
                            + g(0, 0, 0) * g(1, 0, 0) * g(0, 1, 1) * g(1, 1, 1) + g(0, 0, 1) * g(0, 1, 0) * g(1, 0, 1) * g(1, 1, 0)
                            + g(0, 0, 1) * g(1, 0, 0) * g(0, 1, 1) * g(1, 1, 0) + g(0, 1, 0) * g(1, 0, 0) * g(0, 1, 1) * g(1, 0, 1))
                     + 4 * (g(0, 0, 0) * g(0, 1, 1) * g(1, 0, 1) * g(1, 1, 0) + g(0, 0, 1) * g(0, 1, 0) * g(1, 0, 0) * g(1, 1, 1)))


ghz = [1, 0, 0, 0, 0, 0, 0, 1]
wst = [0, 1, 1, 0, 1, 0, 0, 0]
bis = [1, 0, 0, 1, 0, 0, 0, 0]
okinv = True
for _ in range(2):
    psi = Matrix([L.rng_rat(rng) + I * L.rng_rat(rng) for _ in range(8)])
    Cs = [L.rand_gauss(rng, 2, 2) for _ in range(3)]
    Cpsi = L.kron(*Cs) * psi
    okinv = okinv and sp.expand(hdet(list(Cpsi)) - (Cs[0].det() * Cs[1].det() * Cs[2].det()) ** 2 * hdet(list(psi))) == 0
check("S7 Cayley hyperdeterminant: Det(GHZ) = 1, Det(W) = 0, Det(|0>(|00>+|11>)) = 0, and Det((C0 (x) C1 (x) C2) psi) = "
      "(det C0 det C1 det C2)^2 Det(psi) (two random exact instances)",
      hdet(ghz) == 1 and hdet(wst) == 0 and hdet(bis) == 0 and okinv)

ok = L.summary("p5_six_copy")
print("VERDICT " + ("P5-SIX-COPY-EXACT" if ok else "NOT RENDERED"))
sys.exit(0 if ok else 1)
