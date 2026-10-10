#!/usr/bin/env python3
"""S3 node S3.2(a) -- self-duality under composition (SDC): exact ingredients, drop-one models, strictness.

Run: python3 -I -B s3_selfdual.py

The route (written in RESULT.md; the identities it rests on are checked here):
  P3   state-level regrouping: one four-token cone K4 contains prodA K01 K23 and prodB K02 K13;
  OVL4 four-token overlap positivity: <Om, Om'> >= 0 for Om, Om' in K4 (K4 <= K4*, half of self-duality of K4
       for the composed pairing);
  CSD2 pair effects are states: dualW K_p <= K_p (half of self-duality of each pair).
  P3 & OVL4 & CSD2 => FCC, by the cross-pairing identity <prodA X Y, prodB E F> = fourVal X Y E F (s1 B2.7).

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. One PASS/FAIL line per check; [identity] exact symbolic, [witness] exact value at stated tables, [enumerate]
      exhaustive over a named finite set, [countercontrol] a mutated object that must fail.
  R2. VERDICT only if all checks pass; else 'S3-SELFDUAL: FAILED -- <ids>' and exit 1.
  R3. Exact arithmetic; no floating point, randomness or timing in stdout.
  R4. A drop-one model is reported as showing insufficiency of the remaining conjuncts only (never necessity).
"""
import sys
from itertools import product

import sympy as sp

Q = sp.Rational
iu = sp.I
R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def note(cid, text):
    print(f"NOTE [written] {cid}  -- {text}", flush=True)


def section(t):
    print()
    print(f"== {t}", flush=True)


def ex(v):
    return sp.expand(v)


def zero(v):
    return ex(v) == 0


def mzero(M):
    return all(ex(v) == 0 for v in M)


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in NEG else 1) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


def fourVal(X, Y, E, F):
    return sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d] for a, b, c, d in product(R4, repeat=4))


def symtab(nm):
    return sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'{nm}{m}{n}', real=True))


S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
kron = sp.kronecker_product


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * kron(S[m], S[n])
    return out / 4


IDX4 = list(product(R4, repeat=4))
P4 = {s: kron(kron(S[s[0]], S[s[1]]), kron(S[s[2]], S[s[3]])) for s in IDX4}


def pauli4(Om):
    out = sp.zeros(16, 16)
    for s in IDX4:
        if Om[s] != 0:
            out += Om[s] * P4[s]
    return out / 16


def prodA(X, Y):
    return {(a, b, c, d): X[a, b] * Y[c, d] for a, b, c, d in IDX4}


def prodB(L, Lp):
    return {(a, b, c, d): L[a, c] * Lp[b, d] for a, b, c, d in IDX4}


def pair4(Om, Om2):
    return sum(Om[k] * Om2[k] for k in IDX4)


reflY = sp.diag(1, -1, 1)
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
sing4 = sp.diag(1, -1, -1, -1)
Lp = actT(reflY, sing4)
xplus, z3 = [1, 0, 0], [0, 0, 1]
# qubit permutation (q0, q2, q1, q3) -> (q0, q1, q2, q3)
Pi = sp.zeros(16, 16)
for i0, i1, i2, i3 in product(range(2), repeat=4):
    Pi[i0 * 8 + i1 * 4 + i2 * 2 + i3, i0 * 8 + i2 * 4 + i1 * 2 + i3] = 1

# ================================================================================================================
section('S1  the four-qubit dictionary (the quantum model of P3 and OVL4)')
chk('Q1', 'tr(s_m s_n) = 2 delta_mn for the four Pauli matrices (so Pauli strings on four qubits are trace-orthogonal '
    'with tr(s_s s_t) = 16 delta_st, by multiplicativity of the trace under Kronecker products)',
    all((S[m] * S[n]).trace() == (2 if m == n else 0) for m in R4 for n in R4), 'enumerate', '16 pairs')
note('Q1.W', 'hence for four-token tables tr(pauli4 Om pauli4 Om\') = (1/256) sum_s,t Om_s Om\'_t tr(s_s s_t) = '
     '(1/16) <Om, Om\'>: the Euclidean W4 pairing is 16 times the trace pairing of the Pauli presentation.')
X, Y = symtab('X'), symtab('Y')
chk('Q2', 'pauli4 (prodA X Y) = pauliW X (x) pauliW Y, symbolic X, Y', mzero(pauli4(prodA(X, Y)) - kron(pauliW(X), pauliW(Y))),
    'identity')
chk('Q3', 'pauli4 (prodB L L\') = Pi (pauliW L (x) pauliW L\') Pi^T, symbolic (Pi exchanges qubits 1 and 2)',
    mzero(pauli4(prodB(X, Y)) - Pi * kron(pauliW(X), pauliW(Y)) * Pi.T) and Pi * Pi.T == sp.eye(16), 'identity')
chk('Q3c', 'countercontrol: without Pi the grouping-B product is not the Kronecker product',
    not mzero(pauli4(prodB(X, Y)) - kron(pauliW(X), pauliW(Y))), 'countercontrol')
note('Q.W', 'with K4 = PSD16 := {Om : pauli4 Om PSD}: by Q2, Q3 and Mathlib Matrix.PosSemidef.kronecker '
     '(Analysis/Matrix/Order.lean:213) prodA Q3 Q3 and prodB Q3 Q3 lie in K4 (P3 for uniform Q3); by Q1.W and the '
     'self-duality of the PSD cone under the trace pairing (landed psd_iff_trace_nonneg, JordanClassification.lean:84; '
     'psd_trace_mul_nonneg, OperationalRigidity.lean:917) K4 = K4* for the W4 pairing (OVL4 and its converse); and '
     'dualW Q3 = Q3 (s2 D4 with the same fact; CSD2). So uniform Q3 satisfies P3, SD4 and SD2: the route is '
     'satisfiable with FCC.')

# ================================================================================================================
section('S2  per-token charts on four tokens: the even twist patterns')
SG = [1, 1, -1, 1]


def chart4(eps, Om):
    return {s: Om[s] * sp.prod([SG[s[i]] if eps[i] else 1 for i in range(4)]) for s in IDX4}


def chartR(ei, ej, w):
    out = w
    if ej:
        out = actT(reflY, out)
    if ei:
        out = actC(reflY, out)
    return out


ok_ch = True
for eps in product((0, 1), repeat=4):
    lhsA, rhsA = chart4(eps, prodA(X, Y)), prodA(chartR(eps[0], eps[1], X), chartR(eps[2], eps[3], Y))
    lhsB, rhsB = chart4(eps, prodB(X, Y)), prodB(chartR(eps[0], eps[2], X), chartR(eps[1], eps[3], Y))
    ok_ch = ok_ch and all(zero(lhsA[s] - rhsA[s]) and zero(lhsB[s] - rhsB[s]) for s in IDX4)
chk('T1', 'for all 16 token charts eps: chart4 eps (prodA X Y) = prodA (chartR e0 e1 X) (chartR e2 e3 Y) and '
    'chart4 eps (prodB L L\') = prodB (chartR e0 e2 L) (chartR e1 e3 L\'), symbolic', ok_ch, 'enumerate')
chk('T2', 'transpose acts on the Pauli basis as reflY: s_m^T = SG_m s_m (so chart4 eps is the partial transpose on the '
    'qubits with eps_i = 1, an orthogonal involution of W4)', all(S[m].T == SG[m] * S[m] for m in R4), 'enumerate')
note('T.W', 'chart4 eps is a signed permutation of the 256 entries, hence W4-orthogonal; by T2 it is the partial '
     'transpose on the qubits with eps_i = 1, so K4_eps := chart4 eps (PSD16) is self-dual (orthogonal image of a '
     'self-dual cone). chartR ei ej Q3 = twistQ3(ei xor ej) (twin = actT reflY Q3; the full reflection preserves Q3, '
     'landed C4). By T1, K4_eps contains prodA and prodB of the cones twistQ3(ei xor ej): for every even twist '
     'pattern tau = coboundary(eps) the configuration (twistQ3 tau_p)_p satisfies P3, SD4 and SD2 with K4 = K4_eps.')

# ================================================================================================================
section('S3  drop-one models (each shows that the remaining conjuncts do not suffice)')
v_tok = fourVal(phiW, phiW, phiW, Lp)
chk('D1', 'drop OVL4: on the M_tok cones (Q3, Q3, Q3, twin), K4 = cone(prodA Q3 Q3 u prodB Q3 twin) satisfies P3 and '
    'CSD2 holds (Q3, twin self-dual); the overlap <prodA phiW phiW, prodB phiW L\'> = fourVal phiW phiW phiW L\' = -2: '
    'OVL4 fails for EVERY K4 containing both groupings\' products, and FCC fails (-1/8, s1 A3)',
    v_tok == -2 and zero(pair4(prodA(phiW, phiW), prodB(phiW, Lp)) - v_tok), 'witness', f'overlap {v_tok}')
ev = pauliW(Lp).eigenvals()
chk('D2', 'drop P3: M_tok cones with K4 = PSD16 satisfy OVL4 and CSD2, but prodB phiW L\' is not in PSD16: pauliW L\' '
    'has the eigenvalue -1/2 and pauliW phiW is a rank-one projector, so their Kronecker product is not PSD',
    Q(-1, 2) in ev and (pauliW(phiW) * pauliW(phiW) - pauliW(phiW)).is_zero_matrix and pauliW(phiW).rank() == 1,
    'witness', f'eigenvalues of pauliW L\': {ev}')
E0 = sp.zeros(4, 4)
E0[0, 0], E0[1, 3], E0[2, 2] = 1, 1, -1
psi = sp.Matrix([1, -1, -1, -1]) / 2
G = sp.Matrix(4, 4, lambda m, n: ex((kron(S[m], S[n]) * psi * psi.T).trace()))
vg = fourVal(phiW, phiW, E0, G)
chk('D3', 'drop CSD2: uniform K_gen with K4 = PSD16 satisfies P3 and OVL4 (K_gen <= Q3, Q.W); E0 lies in dualW K_gen '
    '(s2 G1-G3) but not in K_gen (ipW E0 G = -1 with G in Q3 = dualW Q3 >= K_gen), so CSD2 fails; FCC fails: '
    'fourVal phiW phiW E0 G = -1', vg == -1 and ipW(E0, G) == -1 and (pauliW(G) - psi * psi.T).is_zero_matrix, 'witness',
    f'value {vg}')
chk('D3c', 'countercontrol: with E0 replaced by the Q3 table E00 + E33 the value is >= 0',
    fourVal(phiW, phiW, sp.diag(1, 0, 0, 1), G) >= 0, 'countercontrol',
    f'value {fourVal(phiW, phiW, sp.diag(1, 0, 0, 1), G)}')

# ================================================================================================================
section('S4  strictness: uniform maxCone satisfies FCC and CSD2 but no K4 gives P3 and OVL4')
v_mx = pair4(prodA(idW, idW), prodB(phiW, Lp))
chk('X1', 'uniform maxCone: <prodA idW idW, prodB phiW L\'> = -2 (idW, phiW, L\' in maxCone, s2 M2): P3 forces two '
    'states with negative overlap into K4, so P3 and OVL4 cannot hold together', v_mx == -2, 'witness',
    f'overlap {v_mx}')
note('X.W', 'uniform maxCone satisfies FCC (landed F.max) and CSD2 (dualW maxCone = SEP <= maxCone) and fails '
     'P3 & OVL4 (X1). So P3 & OVL4 & CSD2 is strictly stronger than FCC on admissible closed cones (maxCone fails '
     'hgate: it is not a model of the full pair hypotheses).')

# ================================================================================================================
section('S5  the abstract-carrier form (no four-copy local tomography): the cross inner product on token products')
p = [[sp.Symbol(f'{c}{i}', real=True) for i in range(3)] for c in 'pqrs']
chk('C1', 'fourVal X Y (prodState x0 x2) (prodState x1 x3) = ipW X (prodState x0 x1) * ipW Y (prodState x2 x3), '
    'symbolic X, Y, x0..x3', zero(fourVal(X, Y, prodState(p[0], p[2]), prodState(p[1], p[3]))
                                   - ipW(X, prodState(p[0], p[1])) * ipW(Y, prodState(p[2], p[3]))), 'identity')
SPTS = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]]
TPm = sp.Matrix([[prodState(s, t)[m, n] for m in R4 for n in R4] for s in SPTS for t in SPTS])
chk('C2', 'the 16 token products prodState s t (s, t in {e_x, e_y, e_z, -e_z}) are linearly independent (they span '
    'R^16; every one has unit entry 1)', TPm.det() != 0 and all(TPm[i, 0] == 1 for i in range(16)), 'witness',
    f'det {TPm.det()}')
note('C.W', 'abstract carrier V with an inner product <.,.>: suppose (i) each grouping\'s product state map is bi-affine '
     'on the pair chart (COMP-1 ProductData combo laws), (ii) TPS: PB.prodState (tp x0 x2) (tp x1 x3) = '
     'PA.prodState (tp x0 x1) (tp x2 x3) on token products, (iii) multiplicativity on grouping A: '
     '<PA.prodState x y, PA.prodState x\' y\'> = ipW x x\' * ipW y y\'. Writing l, l\' in the hyperplane {u_00 = 1} as '
     'affine combinations of token products (C2), bi-affinity, TPS and (iii) give <PA.prodState x y, PB.prodState l l\'> '
     '= sum of coefficient products times ipW X (tp x0 x1) ipW Y (tp x2 x3), which is fourVal X Y L L\' by C1 and '
     'bilinearity of fourVal. So OVL4 for one body containing both groupings\' products, with CSD2, gives famI in the '
     'abstract carrier with no four-copy local tomography; famII is symmetric. The COMP-1 effect field prodEff_effect '
     '(where the cross-positivity sits in thread C\'s N0) is not used.')

# ================================================================================================================
print()
failed = [c[0] for c in CHECKS if not c[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'witness', 'enumerate', 'countercontrol')), flush=True)
if failed:
    print(f"S3-SELFDUAL: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT S3-SELFDUAL-EXACT -- {len(CHECKS)} checks', flush=True)
