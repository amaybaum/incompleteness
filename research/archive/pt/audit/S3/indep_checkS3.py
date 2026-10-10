#!/usr/bin/env python3
"""Coordinator's independent check of thread S3 (stage 2, COMP-CONS). Written without the thread's code.

Decision rule, fixed before the first run:
- each check prints CONFIRMED or MISMATCH; each countercontrol prints CONFIRMED only if the
  predicted failure occurs;
- the verdict line is INDEP-S3-CONFIRMED iff every line is CONFIRMED, else INDEP-S3-MISMATCH
  (exit status 1).

Exact arithmetic only (sympy integers, rationals, Gaussian rationals). Nothing nondeterministic is printed.

Own conventions:
- tables are 4x4 over Pauli coordinates, pauliW(w) = (1/4) sum w_mn s_m (x) s_n;
- cnot is built as conjugation by the CNOT unitary (control on the first qubit) and compared with
  the landed sign/permutation tables only as a cross-check (P1);
- four-token tables are dicts over (a, b, c, d).
"""
import itertools
import sys

import sympy as sp

Rat = sp.Rational
Im = sp.I
S0 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -Im], [Im, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
SIG = [S0, SX, SY, SZ]
KRON2 = {(m, n): sp.kronecker_product(SIG[m], SIG[n]) for m in range(4) for n in range(4)}

RESULTS = []


def record(cid, kind, ok, text, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "CONFIRMED" if ok else "MISMATCH"
    line = f"{tag} {cid} [{kind}] {text}"
    if detail != "":
        line += f" -- {detail}"
    print(line)


def zero(expr):
    return sp.expand(expr) == 0


def mat_zero(M):
    return all(sp.expand(e) == 0 for e in M)


# ---------- pair-level primitives ----------
def pauliW(w):
    M = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if w[m, n] != 0:
                M += w[m, n] * KRON2[(m, n)]
    return M / 4


def coeffW(M):
    return sp.Matrix(4, 4, lambda m, n: sp.expand((KRON2[(m, n)] * M).trace()))


UCNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # |q0 q1>, control q0


def cnot(w):
    return coeffW(UCNOT * pauliW(w) * UCNOT.H)


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot_tab(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in ((1, 3), (2, 2)) else 1) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1, x[0], x[1], x[2]])


def prodState(x, y):
    return hom(x) * hom(y).T


def homMap(R):
    H = sp.zeros(4, 4)
    H[0, 0] = 1
    H[1:, 1:] = R
    return H


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def ipW(a, b):
    return sp.expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))


def fourVal(X, Y, E, F):
    """famI form: sum X_ab Y_cd E_ac F_bd."""
    return sp.expand(sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d]
                         for a in range(4) for b in range(4) for c in range(4) for d in range(4)))


def famII(L, Lp, e, f):
    """famII form as written in the package: sum e_ab f_cd L_ac L'_bd."""
    return sp.expand(sum(e[a, b] * f[c, d] * L[a, c] * Lp[b, d]
                         for a in range(4) for b in range(4) for c in range(4) for d in range(4)))


# ---------- four-token tables ----------
IDX4 = list(itertools.product(range(4), repeat=4))


def prodA(X, Y):
    return {(a, b, c, d): X[a, b] * Y[c, d] for (a, b, c, d) in IDX4}


def prodB(L, Lp):
    return {(a, b, c, d): L[a, c] * Lp[b, d] for (a, b, c, d) in IDX4}


def ip4(O1, O2):
    return sp.expand(sum(O1[k] * O2[k] for k in IDX4))


def effA(e, f, O):
    return sp.expand(sum(e[a, b] * f[c, d] * O[(a, b, c, d)] for (a, b, c, d) in IDX4))


def effB(E, F, O):
    return sp.expand(sum(E[a, c] * F[b, d] * O[(a, b, c, d)] for (a, b, c, d) in IDX4))


def sigma12(O):
    return {(a, b, c, d): O[(a, c, b, d)] for (a, b, c, d) in IDX4}


def dict_eq(O1, O2):
    return O1.keys() == O2.keys() and all(sp.expand(O1[k] - O2[k]) == 0 for k in O1)


def gen(name):
    return sp.Matrix(4, 4, sp.symbols(f"{name}0:16"))


def vec3(name):
    return list(sp.symbols(f"{name}1:4"))


e1, e2, e3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]


def neg(v):
    return [-t for t in v]


AXES = [e1, neg(e1), e2, neg(e2), e3, neg(e3)]
reflY = sp.diag(1, -1, 1)
E00 = sp.zeros(4, 4)
E00[0, 0] = 1


def is_psd_hermitian(M):
    if not mat_zero(M - M.H):
        return False
    ev = M.eigenvals()
    return all(sp.re(sp.nsimplify(k)) >= 0 for k in ev)


print("== P  primitives (own implementation)")
w = gen("w")
v = gen("v")
record("P1", "identity", mat_zero(cnot(w) - cnot_tab(w)),
       "cnot as conjugation by CNOT (control on the first qubit) equals the landed sign/permutation tables, symbolic w")
record("P2", "identity", mat_zero(cnot(cnot(w)) - w) and zero(ipW(cnot(w), cnot(v)) - ipW(w, v)),
       "cnot is an involution and ipW-orthogonal, symbolic")
record("P3", "identity", zero(ipW(w, v) - 4 * (pauliW(w) * pauliW(v)).trace()),
       "ipW w v = 4 tr(pauliW w pauliW v), symbolic (Euclidean pairing = trace pairing; with PSD self-duality, dualW Q3 = Q3)")
x, y = vec3("x"), vec3("y")
rho = lambda t: (S0 + t[0] * SX + t[1] * SY + t[2] * SZ) / 2
record("P4", "identity", mat_zero(pauliW(prodState(x, y)) - sp.kronecker_product(rho(x), rho(y))),
       "pauliW (prodState x y) = rho(x) (x) rho(y), symbolic: every product lies in Q3")
phiW = cnot(prodState(e1, e3))
idW = actT(reflY, phiW)
sing4 = sp.diag(1, -1, -1, -1)
Lp = actT(reflY, sing4)
psiminus = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)
ok5 = (phiW == sp.diag(1, 1, -1, 1) and idW == sp.eye(4) and Lp == sp.diag(1, -1, 1, -1)
       and mat_zero(pauliW(sing4) - psiminus * psiminus.H))
record("P5", "witness", ok5,
       "phiW = cnot(prodState e1 e3) = diag(1,1,-1,1); idW = actT reflY phiW = I; pauliW sing4 = |Psi-><Psi-|; L' = actT reflY sing4 = diag(1,-1,1,-1)")
record("P6", "identity", mat_zero(actT(reflY, actT(reflY, w)) - w) and zero(ipW(actT(reflY, w), actT(reflY, v)) - ipW(w, v)),
       "actT reflY is an ipW-orthogonal involution, symbolic: twin = actT reflY Q3 is self-dual")

print()
print("== X  the cross-pairing identity and the Lemma-B2 sub-identities (generic symbolic tables)")
X, Y, E, F = gen("X"), gen("Y"), gen("E"), gen("F")
PA = prodA(X, Y)
PB = prodB(E, F)
record("X1", "identity", zero(ip4(PA, PB) - fourVal(X, Y, E, F)),
       "<prodA X Y, prodB E F> = fourVal X Y E F (A-states against B-states)")
record("X2", "identity", zero(ip4(prodA(E, F), prodB(X, Y)) - famII(X, Y, E, F)),
       "<prodA e f, prodB L L'> = famII value sum e_ab f_cd L_ac L'_bd")
ok3 = (zero(effB(E, F, PA) - fourVal(X, Y, E, F)) and zero(effA(E, F, prodB(X, Y)) - famII(X, Y, E, F))
       and zero(effA(E, F, PA) - ipW(E, X) * ipW(F, Y)) and zero(effB(X, Y, PB) - ipW(X, E) * ipW(Y, F)))
record("X3", "identity", ok3,
       "effB E F (prodA X Y) = fourVal; effA e f (prodB L L') = famII; effA on prodA and effB on prodB factorize")
record("X4", "identity", dict_eq(sigma12(prodA(X, Y)), prodB(X, Y)),
       "the exchange of tokens 1 and 2 carries prodA L L' to prodB L L'")
inst = sp.Matrix(4, 4, lambda i, j: i + 2 * j + 1)
record("X4c", "countercontrol", not dict_eq(prodA(inst, inst), prodB(inst, inst)),
       "without the exchange, prodA and prodB differ on an instance (predicted failure occurs)")
record("X5", "identity", zero(fourVal(X, Y, E, F) - fourVal(E, F, X, Y)),
       "fourVal X Y E F = fourVal E F X Y, symbolic (state and effect slots exchange; famI = famII for uniform cones)")

print()
print("== O  orders and the token cycle (exhaustive)")
PAIRINGS = {"A": frozenset([frozenset([0, 1]), frozenset([2, 3])]),
            "B": frozenset([frozenset([0, 2]), frozenset([1, 3])]),
            "C": frozenset([frozenset([0, 3]), frozenset([1, 2])])}
KT4 = [frozenset(p) for p in ([0, 1], [2, 3], [0, 2], [1, 3])]
okO1, okO2 = True, True
for order in itertools.permutations(range(4)):
    split = frozenset([frozenset(order[:2]), frozenset(order[2:])])
    hits = [k for k, pm in PAIRINGS.items() if pm == split]
    if len(hits) != 1:
        okO1 = False
    adj = {frozenset(order[i:i + 2]) for i in range(3)}
    if all(p in adj for p in KT4):
        okO2 = False
record("O1", "enumerate", okO1,
       "each of the 24 linear orders has exactly one 2|2 split, so none makes both A and B contiguous")
record("O2", "enumerate", okO2,
       "every linear order leaves at least one KT4 pair non-adjacent (3 adjacencies, 4 pairs)")


def crossing(cyc, pm):
    pos = {t: i for i, t in enumerate(cyc)}
    (a, b), (c, d) = [sorted(pos[t] for t in p) for p in pm]
    return (a < c < b) != (a < d < b)


canon = set()
for order in itertools.permutations(range(4)):
    variants = []
    for r in range(4):
        rot = order[r:] + order[:r]
        variants += [rot, tuple(reversed(rot))]
    canon.add(min(variants))
noncross = {cyc: sorted(k for k, pm in PAIRINGS.items() if not crossing(cyc, pm)) for cyc in sorted(canon)}
both = [cyc for cyc, ks in noncross.items() if "A" in ks and "B" in ks]
cycle_edges = {frozenset([0, 1]), frozenset([1, 3]), frozenset([3, 2]), frozenset([2, 0])}
record("O3", "enumerate", len(canon) == 3 and both == [(0, 1, 3, 2)] and cycle_edges == set(KT4),
       "3 cyclic orders; A and B are both non-crossing only in 0-1-3-2; its edges are the four KT4 pairs", str(noncross))
EDGES = [(0, 1), (2, 3), (0, 2), (1, 3)]
cob = {tuple((eps[i] + eps[j]) % 2 for (i, j) in EDGES) for eps in itertools.product(range(2), repeat=4)}
even = {t for t in itertools.product(range(2), repeat=4) if sum(t) % 2 == 0}
record("O4", "enumerate", cob == even and len(cob) == 8,
       "the coboundaries of the 16 token-bit assignments are exactly the 8 even edge patterns (EvenCycle)")
record("O4c", "countercontrol", (0, 0, 0, 1) not in cob,
       "the single-twin pattern (0,0,0,1) is not a coboundary (predicted failure occurs)")

print()
print("== K  the two foils from below and above: uniform K_gen and uniform K_gen* = dualW K_gen")
E0 = sp.zeros(4, 4)
E0[0, 0], E0[1, 3], E0[2, 2] = 1, 1, -1
record("K1", "witness", cnot(E0) == E0, "cnot E0 = E0 (E0 = E00 + E13 - E22)")
Mbil = sp.Matrix([[0, 0, 1], [0, -1, 0], [0, 0, 0]])
form = (hom(x).T * E0 * hom(y))[0, 0]
lin = sp.expand(form - 1 - (sp.Matrix(x).T * Mbil * sp.Matrix(y))[0, 0])
sv = (Mbil.T * Mbil).eigenvals()
record("K2", "identity", lin == 0 and sv == {0: 1, 1: 2},
       "hom(x)^T E0 hom(y) = 1 + x^T M y with M^T M eigenvalues {0, 1, 1}: |x^T M y| <= |x||y| <= 1, so E0 is in maxCone; with K1 it lies in maxCone n cnot(maxCone) = K_gen*",
       f"M^T M eigenvalues {sv}")
evE0 = pauliW(E0).eigenvals()
record("K3", "witness", Rat(-1, 4) in evE0, "pauliW E0 has the eigenvalue -1/4: E0 is not in Q3, so not in K_gen (K_gen <= Q3)",
       str(dict(sorted(evE0.items(), key=lambda kv: sp.re(kv[0])))))
G = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0]])
psi = sp.Matrix([1, -1, -1, -1]) / 2
record("K4", "witness", mat_zero(pauliW(G) - psi * psi.H) and ipW(E0, G) == -1,
       "pauliW G = psi psi^T, psi = (1,-1,-1,-1)/2: G is a pure state in Q3 <= dualW K_gen; ipW E0 G = -1")
v6 = fourVal(phiW, phiW, E0, G)
record("K5", "witness", v6 == -1,
       "uniform K_gen, famI: fourVal phiW phiW E0 G = -1 (states phiW in K_gen; effects E0, G in dualW K_gen)", str(v6))
v6c = fourVal(phiW, phiW, E00, G)
record("K5c", "countercontrol", v6c >= 0, "with E00 in place of E0 the value is nonnegative (predicted failure of the witness occurs)", str(v6c))
v7 = fourVal(E0, G, phiW, phiW)
record("K6", "witness", v7 == -1,
       "uniform K_gen*, famI: fourVal E0 G phiW phiW = -1 (states E0, G in K_gen*; effects phiW in K_gen <= dualW K_gen*)", str(v7))
ROTS = [sp.Matrix(3, 3, lambda i, j: s[i] if p[i] == j else 0)
        for p in itertools.permutations(range(3)) for s in itertools.product([1, -1], repeat=3)]
ROTS = [R for R in ROTS if R.det() == 1]
CPROD = [(a, b, cnot(prodState(a, b))) for a in AXES for b in AXES]
found = None
for side in ("C", "T"):
    for k, R in enumerate(ROTS):
        wR = actC(R, E0) if side == "C" else actT(R, E0)
        for (a, b, cp) in CPROD:
            val = ipW(wR, cp)
            if val < 0:
                found = (side, k, list(R), a, b, val)
                break
        if found:
            break
    if found:
        break
record("K7", "witness", len(ROTS) == 24 and found is not None,
       "IE1 fails for K_gen*: some octahedral rotation R moves E0 (in K_gen*) to a table that pairs negatively with cnot(prodState a b) in K_gen",
       f"side {found[0]}, R = {found[2]}, a = {found[3]}, b = {found[4]}, value {found[5]}" if found else "none")
neg_id = [ipW(E0, cp) for (_, _, cp) in CPROD if ipW(E0, cp) < 0]
record("K7c", "countercontrol", neg_id == [], "the identity rotation gives no negative value on the same 36 generated tables (predicted)")

print()
print("== M  maxCone memberships, the maxCone strictness witness, M_tok and the induced pairs")
okM1 = True
for D in (idW, sing4, phiW, Lp):
    f = sp.expand((hom(x).T * D * hom(y))[0, 0] - 1 - sum(D[i + 1, i + 1] * x[i] * y[i] for i in range(3)))
    okM1 = okM1 and f == 0 and all(abs(D[i + 1, i + 1]) <= 1 for i in range(3)) and D[0, 0] == 1
record("M1", "identity", okM1,
       "idW, sing4, phiW, L' are diag(1, d) with |d_i| <= 1: hom(x)^T D hom(y) = 1 + sum d_i x_i y_i >= 1 - |x||y| >= 0, so all lie in maxCone")
vI4 = fourVal(phiW, phiW, idW, sing4)
record("M2", "witness", vI4 == -2, "induced pairs of an A-composite: fourVal phiW phiW idW sing4 = -2", str(vI4))
vI4c = fourVal(phiW, phiW, idW, prodState(e3, e3))
record("M2c", "countercontrol", vI4c >= 0, "with the product prodState e3 e3 in place of sing4 the value is nonnegative (predicted)", str(vI4c))
vX1 = ip4(prodA(idW, idW), prodB(phiW, Lp))
record("M3", "witness", vX1 == -2,
       "uniform maxCone: <prodA idW idW, prodB phiW L'> = -2 with all four in maxCone; FCC and CSD2 hold there (landed F.max; dualW maxCone = SEP), so P3 and OVL4 cannot both hold: SDC is strictly stronger than FCC on admissible closed cones",
       str(vX1))
vtok = fourVal(phiW, phiW, phiW / 4, Lp / 4)
twin_ok = actT(reflY, Lp) == sing4 and is_psd_hermitian(pauliW(sing4)) and is_psd_hermitian(pauliW(phiW))
record("M4", "witness", vtok == Rat(-1, 8) and twin_ok,
       "M_tok (Q3, Q3, Q3, twin): fourVal phiW phiW (phiW/4) (L'/4) = -1/8 with phiW in Q3 and L' in twin (actT reflY L' = sing4, PSD)", str(vtok))
vtokc = fourVal(phiW, phiW, phiW / 4, phiW / 4)
record("M4c", "countercontrol", vtokc >= 0, "with phiW/4 in place of L'/4 the value is nonnegative (predicted)", str(vtokc))
vD1 = ip4(prodA(phiW, phiW), prodB(phiW, Lp))
record("M5", "witness", vD1 == -2, "drop OVL4 (M_tok cones): <prodA phiW phiW, prodB phiW L'> = -2", str(vD1))


def pauli4(O):
    M = sp.zeros(16, 16)
    for k, val in O.items():
        if val != 0:
            M += val * sp.kronecker_product(SIG[k[0]], SIG[k[1]], SIG[k[2]], SIG[k[3]])
    return M / 16


vec = sp.zeros(16, 1)
for i in range(2):
    for j in range(2):
        vec[8 * i + 4 * j + 2 * i + j] = Rat(1, 2)
qD2 = sp.expand((vec.H * pauli4(prodB(phiW, Lp)) * vec)[0, 0])
record("M6", "witness", qD2 == Rat(-1, 2),
       "drop P3 (K4 = PSD16): prodB phiW L' is not in PSD16, since <v| pauli4(prodB phiW L') |v> = -1/2 for v = Phi+ on qubits (0,2) times Phi+ on (1,3), computed from the definition of pauli4",
       str(qD2))
qD2c = sp.expand((vec.H * pauli4(prodB(phiW, phiW)) * vec)[0, 0])
record("M6c", "countercontrol", qD2c >= 0, "with phiW in place of L' the same vector gives a nonnegative value (predicted)", str(qD2c))

print()
print("== S  entanglement-swapping witness on uniform K_gen")
Xg = cnot(prodState(e1, e2))
Fg = cnot(prodState(e2, e2))
Yg = cnot(prodState(neg(e1), e3))
vS3 = fourVal(Xg, Yg, E0, Fg)
record("S1", "identity", zero(fourVal(X, Y, E, F) - ipW(E, X * F * Y.T)),
       "fourVal X Y E F = ipW E (X F Y^T), symbolic (the conditioned 02 table)")
record("S2", "witness", vS3 == -1 and all(is_psd_hermitian(pauliW(T)) for T in (Xg, Fg, Yg)),
       "ESC fails on uniform K_gen: generated X, Y, F (cnot images of products, all in Q3) with the full effect E0 give -1", str(vS3))

print()
print("== L  Lorentz exclusion and the abstract-carrier identities")
axp = [prodState(a, b) for a in AXES for b in AXES]
avg = sum(axp, sp.zeros(4, 4)) / len(axp)
record("L1", "enumerate", len(axp) == 36 and all(ipW(p, p) == 4 for p in axp) and avg == E00,
       "the 36 axis products have |p| = 2 and average E00 (|E00| = 1): a 45-degree cone {<u, v> >= |v|/sqrt 2} cannot contain them, since <u, p> >= sqrt 2 for all would give <u, E00> >= sqrt 2 > 1")
okL2 = all(ipW(E00, p) ** 2 * 2 < ipW(p, p) for p in axp)
record("L2", "enumerate", okL2, "each axis product lies outside the 45-degree cone about E00 (<E00, p>^2 = 1 < |p|^2/2 = 2)")
x0, x1v, x2v, x3v = vec3("a"), vec3("b"), vec3("c"), vec3("d")
okC1 = zero(fourVal(X, Y, prodState(x0, x2v), prodState(x1v, x3v)) - ipW(X, prodState(x0, x1v)) * ipW(Y, prodState(x2v, x3v)))
record("C1", "identity", okC1,
       "fourVal X Y (prodState x0 x2) (prodState x1 x3) = ipW X (prodState x0 x1) * ipW Y (prodState x2 x3), symbolic")
toks = [e1, e2, e3, neg(e3)]
Mt = sp.Matrix([[prodState(s, t)[i, j] for i in range(4) for j in range(4)] for s in toks for t in toks])
record("C2", "witness", abs(Mt.det()) == 256, "the 16 token products prodState s t, s, t in {e1, e2, e3, -e3}, span R^16", f"|det| = {abs(Mt.det())}")
SGN = [1, 1, -1, 1]
okT1 = all(mat_zero(SIG[m].T - SGN[m] * SIG[m]) for m in range(4))
okT2 = True
for eps in itertools.product(range(2), repeat=4):
    def ch(O):
        return {k: O[k] * sp.prod([SGN[k[i]] ** eps[i] for i in range(4)]) for k in IDX4}
    def chR(a, b, T):
        return sp.Matrix(4, 4, lambda m, n: T[m, n] * SGN[m] ** a * SGN[n] ** b)
    if not dict_eq(ch(prodA(X, Y)), prodA(chR(eps[0], eps[1], X), chR(eps[2], eps[3], Y))):
        okT2 = False
    if not dict_eq(ch(prodB(E, F)), prodB(chR(eps[0], eps[2], E), chR(eps[1], eps[3], F))):
        okT2 = False
record("T1", "enumerate", okT1 and okT2,
       "transpose acts on the Pauli basis by the signs (1,1,-1,1), and for all 16 token charts the four-token chart carries prodA and prodB of charted pair tables")

n_ok = sum(RESULTS)
print()
print(f"checks: {len(RESULTS)}, confirmed: {n_ok}")
verdict = "INDEP-S3-CONFIRMED" if n_ok == len(RESULTS) else "INDEP-S3-MISMATCH"
print(f"VERDICT {verdict}")
sys.exit(0 if verdict == "INDEP-S3-CONFIRMED" else 1)
