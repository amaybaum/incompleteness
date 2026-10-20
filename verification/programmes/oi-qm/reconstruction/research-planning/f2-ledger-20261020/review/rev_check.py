"""rev_check.py -- reviewer's independent exact re-derivation of the core of LEDGER.md claim (3)
and of the monomial-branch lemma.  Written without reference to the author's helpers: operators are
built as dicts / explicit loops over configuration tuples; SymPy is used only for symbolic identities,
Groebner elimination and exact eigen-data.  Each check prints PASS/FAIL; rc != 0 iff any FAIL.
"""
import itertools
import random
import sys

import sympy as sp

OUT = []
FAILS = []


def chk(label, cond):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        FAILS.append(label)


I = sp.I
CONF3 = list(itertools.product((0, 1), repeat=3))   # (x1,x2,x3)
CONF2 = list(itertools.product((0, 1), repeat=2))
ix3 = {c: n for n, c in enumerate(CONF3)}
ix2 = {c: n for n, c in enumerate(CONF2)}


def perm_from_fn(f):
    """bijection on CONF3 given as python fn -> dict"""
    d = {c: tuple(f(c)) for c in CONF3}
    assert sorted(d.values()) == CONF3
    return d


def adP(sig, M8):
    """(P M P^dag)[sig(i), sig(j)] = M[i, j]  -- native conjugation (fixed identification)"""
    out = sp.zeros(8, 8)
    for i in CONF3:
        for j in CONF3:
            out[ix3[sig[i]], ix3[sig[j]]] = M8[ix3[i], ix3[j]]
    return out


def attach0(X4):
    """X (x) |0><0| on token 3, built by loops"""
    out = sp.zeros(8, 8)
    for (p, q) in itertools.product(CONF2, repeat=2):
        out[ix3[p + (0,)], ix3[q + (0,)]] = X4[ix2[p], ix2[q]]
    return out


def prod_vec(a, b, c):
    return sp.Matrix([a[x[0]] * b[x[1]] * c[x[2]] for x in CONF3])


def test_value(M8, phi):
    return sp.expand((phi.H * M8 * phi)[0, 0])


def tr3(M8):
    out = sp.zeros(4, 4)
    for p in CONF2:
        for q in CONF2:
            out[ix2[p], ix2[q]] = sum(M8[ix3[p + (k,)], ix3[q + (k,)]] for k in (0, 1))
    return out


def pt_tok2(X4):
    out = sp.zeros(4, 4)
    for (a, b) in CONF2:
        for (c, d) in CONF2:
            out[ix2[(a, b)], ix2[(c, d)]] = X4[ix2[(a, d)], ix2[(c, b)]]
    return out


def pt_tok2_3(M8):
    out = sp.zeros(8, 8)
    for (a, b, e) in CONF3:
        for (c, d, f) in CONF3:
            out[ix3[(a, b, e)], ix3[(c, d, f)]] = M8[ix3[(a, d, e)], ix3[(c, b, f)]]
    return out


pauli = {"I": sp.eye(2), "X": sp.Matrix([[0, 1], [1, 0]]), "Y": sp.Matrix([[0, -I], [I, 0]]),
         "Z": sp.Matrix([[1, 0], [0, -1]])}


def two(p, q):
    A, B = pauli[p], pauli[q]
    return sp.Matrix(4, 4, lambda r, s: A[r // 2, s // 2] * B[r % 2, s % 2])


def zdef(s, t):
    return (sp.eye(4) + s * two("X", "Z") + t * two("Y", "Y") - s * t * two("Z", "X")) / 4


ZF = {(s, t): zdef(s, t) for s in (1, -1) for t in (1, -1)}

# native permutations
Cpar = perm_from_fn(lambda x: (x[0], x[1], x[2] ^ x[0] ^ x[1]))            # CNOT13 then CNOT23
C13 = perm_from_fn(lambda x: (x[0], x[1], x[2] ^ x[0]))
slice0 = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0)]
Tset = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
rest_s = [c for c in CONF3 if c not in slice0]
rest_t = [c for c in CONF3 if c not in Tset]
SIG = dict(zip(slice0 + rest_s, Tset + rest_t))   # reviewer's own completion of the author's sigma idea

print("== R1 general form of the 3-token protocol's effective pair test ==")
xs = sp.symbols("m0:16")
Xg = sp.Matrix(4, 4, xs)
a0, a1, b0, b1, c0, c1 = sp.symbols("a0 a1 b0 b1 c0 c1")
phi = prod_vec((a0, a1), (b0, b1), (c0, c1))


def u_of(sig, ph):
    """effective vector: u(x) = phi(sig(x,0))"""
    return sp.Matrix([ph[ix3[sig[p + (0,)]]] for p in CONF2])


for name, sg in [("Cpar", Cpar), ("SIG", SIG), ("CNOT13", C13)]:
    lhs = test_value(adP(sg, attach0(Xg)), phi)
    uu = u_of(sg, phi)
    chk(f"R1 [{name}] <phi| Ad_P(X(x)|0><0|) |phi> == <u|X|u>, u(x)=phi(sigma(x,0)) (symbolic X, a, b, c)",
        sp.expand(lhs - (uu.H * Xg * uu)[0, 0]) == 0)
uC = u_of(Cpar, phi)
chk("R1b for Cpar, u = (a0b0c0, a0b1c1, a1b0c1, a1b1c0) = diag(c0,c1,c1,c0)(a(x)b)",
    sp.expand(uC - sp.Matrix([a0 * b0 * c0, a0 * b1 * c1, a1 * b0 * c1, a1 * b1 * c0])) == sp.zeros(4, 1))
u13 = u_of(C13, phi)
chk("R1c control: CNOT13 alone gives u = (a0c0, a1c1)(x)(b0,b1), a product vector (u00 u11 == u01 u10)",
    sp.expand(u13[0] * u13[3] - u13[1] * u13[2]) == 0)

# exhaustive numeric-exact version of R1 over ALL of S_8 with a fixed random Gaussian-integer X and phi
random.seed(20261020)


def gi():
    return complex(random.randint(-3, 3), random.randint(-3, 3))


Xn = [[0] * 4 for _ in range(4)]
for r in range(4):
    for s_ in range(r, 4):
        v = gi() if r != s_ else complex(random.randint(-3, 3), 0)
        Xn[r][s_] = v
        Xn[s_][r] = v.conjugate()
an, bn, cn = (gi(), gi()), (gi(), gi()), (gi(), gi())
phin = {x: an[x[0]] * bn[x[1]] * cn[x[2]] for x in CONF3}
bad = 0
for img in itertools.permutations(CONF3):
    sg = dict(zip(CONF3, img))
    # direct: sum_{i,j} conj(phi(sig i)) M8[i,j] phi(sig j) over the attached block
    direct = 0
    for p in CONF2:
        for q in CONF2:
            direct += phin[sg[p + (0,)]].conjugate() * Xn[ix2[p]][ix2[q]] * phin[sg[q + (0,)]]
    uu = [phin[sg[p + (0,)]] for p in CONF2]
    quad = sum(uu[r].conjugate() * Xn[r][s_] * uu[s_] for r in range(4) for s_ in range(4))
    if direct != quad:   # Gaussian integers in floats are exact at this size
        bad += 1
chk(f"R1d exhaustive over all 40320 sigma in S_8 (Gaussian-integer X, a, b, c): u(x)=phi(sigma(x,0)) form holds ({bad} mismatches)",
    bad == 0)

print("== R2 which u are reached by the CNOT (parity) route; closure; sigma route ==")
# generic u with nonzero entries: exact preimage
ok = True
for trial in range(25):
    uu = [sp.Integer(random.choice([-3, -2, -1, 1, 2, 3])) + I * random.randint(-3, 3) for _ in range(4)]
    ratio = sp.nsimplify(uu[1] * uu[2] / (uu[0] * uu[3]))
    cc = (sp.Integer(1), sp.sqrt(ratio))
    aa = (sp.Integer(1), uu[2] / (cc[1] * uu[0]))   # a1 = u10 / (c1 b0) with b0 = u00
    bb = (uu[0], uu[1] / cc[1])
    rec = [aa[0] * bb[0] * cc[0], aa[0] * bb[1] * cc[1], aa[1] * bb[0] * cc[1], aa[1] * bb[1] * cc[0]]
    if any(sp.simplify(rec[k] - uu[k]) != 0 for k in range(4)):
        ok = False
chk("R2a 25 random Gaussian-integer u with nonzero entries are reached exactly by the parity route", ok)
# u with zeros: (0,1,1,1) and (1,0,1,1) are NOT reached (Groebner basis = [1])
for target in [(0, 1, 1, 1), (1, 0, 1, 1)]:
    eqs = [a0 * b0 * c0 - target[0], a0 * b1 * c1 - target[1], a1 * b0 * c1 - target[2], a1 * b1 * c0 - target[3]]
    G = sp.groebner(eqs, a0, a1, b0, b1, c0, c1, order="lex")
    chk(f"R2b u = {target} is NOT reached by the parity route (Groebner basis is [1]): closure is needed on the CNOT-only route",
        list(G.exprs) == [1])
# sigma route: every u with u00 != 0 exactly; u00 = 0 needs a pair permutation (PC24) first
uu = sp.Matrix([0, 1, 1, 1])
perm2 = {(0, 0): (0, 1), (0, 1): (0, 0), (1, 0): (1, 0), (1, 1): (1, 1)}     # native transposition 00<->01
up = sp.zeros(4, 1)
for p in CONF2:
    up[ix2[perm2[p]]] = uu[ix2[p]]
chk("R2c a native pair transposition moves u=(0,1,1,1) to u'=(1,0,1,1) with u'00 != 0", up[0] != 0)
# reach u' exactly via the sigma route: test (1,u'_{01})(1,u'_{10})(1,u'_{11}) in the author's ordering
ph = prod_vec((1, up[1]), (1, up[2]), (1, up[3]))   # SIG maps 00->000, 01->100, 10->010, 11->001: u=(1,a1,b1,c1)
chk("R2d sigma route reaches u' exactly: u(x)=phi(SIG(x,0)) == u'",
    sp.expand(u_of(SIG, ph) - up) == sp.zeros(4, 1))

print("== R3 exact witnesses (upper route) ==")
zm = ZF[(1, 1)]
pi, mi = (1, I), (1, -I)
v = test_value(adP(Cpar, attach0(zm)), prod_vec(pi, mi, pi))
chk(f"R3a z(1,1) on |+i>|-i>|+i> after attach, CNOT13, CNOT23: {v} == -2 (normalized -1/4)", v == -2)
v = test_value(adP(Cpar, attach0(zm)), prod_vec((2, 1), (1, 2), (3, 1)))
chk(f"R3b z(1,1) on real test (2,1)(1,2)(3,1): {v} == -47/4 (normalized {v / 250})", v == sp.Rational(-47, 4))
# for every defect and Gamma(Phi+): take an exact negative eigenvector w, reach it through a native
# pair permutation + SIG, value must equal lambda |w|^2 < 0
phip = sp.Matrix([1, 0, 0, 1])
GB = pt_tok2(phip * phip.T / 2)
fixtures = {**{f"z{k}": z for k, z in ZF.items()}, "Gamma(Phi+)": GB}
for nm, Xf in fixtures.items():
    lam_neg = [lam for lam in Xf.eigenvals() if sp.re(lam) < 0]
    lam = lam_neg[0]
    w = (Xf - lam * sp.eye(4)).nullspace()[0]
    k0 = next(k for k in range(4) if w[k] != 0)
    # native pair transposition (k0 <-> 0) to bring a nonzero entry to position 00, then SIG
    tp = list(range(4)); tp[0], tp[k0] = tp[k0], tp[0]
    Xp = sp.Matrix(4, 4, lambda r, s: Xf[tp[r], tp[s]])      # Ad of the transposition
    wp = sp.Matrix([w[tp[r]] for r in range(4)])
    wp = wp / wp[0]
    ph = prod_vec((1, wp[1]), (1, wp[2]), (1, wp[3]))
    val = sp.simplify(test_value(adP(SIG, attach0(Xp)), ph))
    target = sp.simplify(lam * (wp.H * wp)[0, 0])
    chk(f"R3c {nm}: exact negative value {val} = lambda|w|^2 via pair transposition + SIG (lambda={lam})",
        sp.simplify(val - target) == 0 and val < 0)

print("== R4 lower route: selective readout 0 on token 3 + discard ==")


def lower(sig_inv, a, b, c):
    """state |a b c>, apply P_{sig_inv}, keep x3 = 0 (Lueders branch), discard token 3."""
    ph = prod_vec(a, b, c)
    out = sp.zeros(8, 1)
    for x in CONF3:
        out[ix3[sig_inv[x]]] = ph[ix3[x]]
    for x in CONF3:
        if x[2] == 1:
            out[ix3[x]] = 0
    return sp.simplify(tr3(out * out.H))


SIGinv = {v_: k for k, v_ in SIG.items()}
Cinv = Cpar   # involution
singlet = sp.Matrix([0, 1, -1, 0])
r = lower(Cinv, (1, 1), (1, -1), (0, 1))
chk("R4a singlet (reviewer's own parameters a=(1,1), b=(1,-1), c=(0,1)) via parity route", sp.simplify(r - singlet * singlet.H) == sp.zeros(4, 4))
r = lower(SIGinv, (1, 0), (1, 0), (1, 1))   # u = (1, a1, b1, c1) = (1,0,0,1)
chk("R4b Phi+ via sigma route, a=b=(1,0), c=(1,1)", sp.simplify(r - phip * phip.H) == sp.zeros(4, 4))
czpp = sp.Matrix([1, 1, 1, -1])
r = lower(SIGinv, (1, 1), (1, 1), (1, -1))   # u = (1, 1, 1, -1)
chk("R4c CZ|++> via sigma route, a=(1,1), b=(1,1), c=(1,-1)", sp.simplify(r - czpp * czpp.H) == sp.zeros(4, 4))
Pm = sp.eye(4) / 2 - zm
chk("R4d P_m = I/2 - z(1,1) is a rank-one projector and Tr(z P_m) = -1/2",
    sp.simplify(Pm * Pm - Pm) == sp.zeros(4, 4) and Pm.trace() == 1 and sp.simplify((zm * Pm).trace()) == sp.Rational(-1, 2))
wv = Pm.columnspace()[0]
k0 = next(k for k in range(4) if wv[k] != 0)
wv = wv / wv[k0]
chk(f"R4e P_m's vector has nonzero 00 entry (k0={k0})", k0 == 0)
r = lower(SIGinv, (1, wv[1]), (1, wv[2]), (1, wv[3]))
chk("R4f P_m generated exactly (up to scale) via sigma route", sp.simplify(r * Pm - r) == sp.zeros(4, 4) and r != sp.zeros(4, 4))
# P_m also by the parity route? (all entries nonzero?)
chk(f"R4g P_m vector entries {list(wv)}: all nonzero -> parity route also reaches it exactly",
    all(e != 0 for e in wv))

print("== R5 controls ==")
# Q3 survives: Ad_P unitary, RO_3 branch and Tr_3 CP -> (Q3, QK3) satisfies Sigma_3 (existence converse)
rho = sp.Matrix([[3, 1, 0, I], [1, 2, 1, 0], [0, 1, 2, 0], [-I, 0, 0, 1]])
chk("R5a positive control input PSD", rho.is_positive_semidefinite)
img = adP(Cpar, attach0(rho))
chk("R5b native image PSD; Tr3 of image PSD; RO_3 branch PSD", img.is_positive_semidefinite and tr3(img).is_positive_semidefinite)
# Gamma-transported identification: Gamma(Q3) survives the upper route under Gamma2 o Ad_C o Gamma2
lhsG = test_value(pt_tok2_3(adP(Cpar, pt_tok2_3(attach0(pt_tok2(Xg))))), phi)
bc = (sp.conjugate(b0), sp.conjugate(b1))
phic = prod_vec((a0, a1), bc, (c0, c1))
rhsG = test_value(adP(Cpar, attach0(Xg)), phic)
chk("R5c transported action: test value on Gamma(X) equals the fixed-identification value on X with b -> conj(b); so Gamma(Q3) survives the transported Sigma_3 upper route (transport of structure)",
    sp.expand(lhsG - rhsG) == 0)
# configuration tests read diagonal entries only
cfgmin = min(test_value(adP(Cpar, attach0(Xf)), prod_vec(*[(1, 0) if bit == 0 else (0, 1) for bit in x]))
             for Xf in fixtures.values() for x in CONF3)
chk(f"R5d configuration-only tests give min {cfgmin} >= 0 on all fixtures (they read diagonal entries)", cfgmin >= 0)
# real tests do NOT suffice in general: complex block-positive, non-PSD X with PSD real part
psi = sp.Matrix([1, 0, 0, I])
Xc = pt_tok2(psi * psi.H / 2)
chk("R5e mutation: X = Gamma(|psi><psi|), psi=(1,0,0,i)/sqrt2, is non-PSD (eigenvalue -1/2) ...",
    sp.Rational(-1, 2) in Xc.eigenvals())
ReX = (Xc + Xc.conjugate()) / 2
chk("R5f ... but its real part is PSD, so every REAL product test after any native permutation reads u^T Re(X) u >= 0: real token tests cannot exclude it",
    ReX.is_positive_semidefinite)
# block positivity of the defects, exhaustively symbolic: <ab|z|ab> = (1 + a.Mb)/4 with M orthogonal
# K(Z_F) pair-level readout and discard closure: readout branch of each defect on token 1 or 2 is a PSD product
okRO = True
for z in ZF.values():
    for tok in (0, 1):
        for kk in (0, 1):
            Pi = sp.zeros(4, 4)
            for p in CONF2:
                if p[tok] == kk:
                    Pi[ix2[p], ix2[p]] = 1
            br = Pi * z * Pi
            if not br.is_positive_semidefinite:
                okRO = False
chk("R5g K(Z_F): every single-token configuration readout branch of every defect is PSD (lands in SEP: product of a basis state and a PSD 2x2)", okRO)

print("== R6 monomial-branch lemma: symbolic ancilla, feed-forward, and a non-vacuous control ==")
al = sp.symbols("al0:4")   # arbitrary complex ancilla vector on 2 ancilla tokens


def branch_matrix(perm, nS, nA, alpha, cout):
    K = sp.zeros(nS, nS)
    for y in range(nS):
        for c in range(nA):
            x, cp = divmod(perm[y * nA + c], nA)
            if cp == cout:
                K[x, y] += alpha[c]
    return K


def row_monomial(K):
    return all(sum(1 for j in range(K.cols) if sp.expand(K[i, j]) != 0) <= 1 for i in range(K.rows))


okm = True
for trial in range(300):
    perm = list(range(8)); random.shuffle(perm)
    for cout in range(4):
        K = branch_matrix(perm, 2, 4, al, cout)
        if not row_monomial(K) or any(len(sp.Add.make_args(sp.expand(e))) > 1 for e in K if e != 0):
            okm = False
chk("R6a 300 random permutations of S x A (|S|=2,|A|=4), symbolic ancilla amplitudes: every branch is row-monomial, entries single terms", okm)
# two-round protocol with feed-forward: perm1, read ancilla token A1 (outcome k), controlled perm2_k, read all
okf = True
for trial in range(100):
    p1 = list(range(8)); random.shuffle(p1)
    p2 = [list(range(8)) for _ in range(2)]
    for q in p2:
        random.shuffle(q)
    for k in (0, 1):
        for cout in range(4):
            K = sp.zeros(2, 2)
            for y in range(2):
                for c in range(4):
                    x1, c1_ = divmod(p1[y * 4 + c], 4)
                    if (c1_ >> 1) != k:            # read ancilla token A1 (high bit)
                        continue
                    x2, c2 = divmod(p2[k][x1 * 4 + c1_], 4)
                    if c2 == cout:
                        K[x2, y] += al[c]
            if not row_monomial(K):
                okf = False
chk("R6b 100 random two-round feed-forward protocols: every branch row-monomial", okf)
# non-vacuous control through the SAME computation: replace perm2 by a Hadamard on the system (non-native)
H = sp.Matrix([[1, 1], [1, -1]])
p1 = list(range(8))
K = sp.zeros(2, 2)
for y in range(2):
    for c in range(4):
        x1, c1_ = divmod(p1[y * 4 + c], 4)
        if c1_ == 0:
            for x2 in range(2):
                K[x2, y] += H[x2, x1] * al[c]
chk("R6c control: same branch computation with a Hadamard inserted yields a non-row-monomial invertible branch (detector fires)",
    (not row_monomial(K)) and sp.simplify(K.det()) != 0)

print(f"== SUMMARY: {len(FAILS)} FAIL ==")
sys.exit(1 if FAILS else 0)
