#!/usr/bin/env python3
"""Thread A (PAIR-COMP), node A3: closedness of a completed body does not reach its product-test shadow in
W 3 without finite rank. Exact checks on the finite skeleton of the pair directed system D_cl whose
completion's shadow is the landed closedness foil K_cl = int Q3 u (SEP + cnot SEP) (written argument
W-A3 in RESULT.md). Exact arithmetic only. Run as:  python3 -I -B a3_shadow_countermodel.py

The system D_cl (index n = 1, 2, 3, ...; the skeleton below is n <= 4):
  preparations at stage n:  c_1..c_n  (members of C = SEP + cnot SEP: products of rational ball points and
                            their cnot images), and rho_1..rho_{2n} with rho_{2k-1} = tau_k = (1 - t_k) T_psi +
                            t_k E00 and rho_{2k} = cnot tau_k, t_k = 1/(k+1)  (in the written argument the
                            rho-family is any enumeration of a countable dense subset of int Q3's normalized
                            slice containing these);
  labels at stage n:        the unit; product labels (a, b) for the first 3 + n one-ball effects of a fixed list
                            (it starts with the four basis effects); joint labels b_S for S a subset of
                            {1..2n};
  table:                    a product label reads pairVal(ehom e_a, ehom e_b, w) on a preparation with table w
                            (TAB holds by construction); b_S reads 1 on rho_J if J in S, else 0; b_S reads 0 on
                            every c_j;  stage maps: inclusions.

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1 STAGES: for n = 1..4 every table entry lies in [0, 1] and the unit reads 1 (exact); for n <= m every
     label of stage n is a label of stage m with the same values on the preparations of stage n
     (SC-infinity with inclusions); the 16 basis product labels read back every preparation's table exactly.
  R2 RANK: for n = 1..4 the values of rho_1..rho_{2n} on the joint labels of stage n form a matrix of rank 2n.
  R3 NO CONVERGENT SUBSEQUENCE: at stage 4, for J != K the sup-distance of the value vectors of rho_J and
     rho_K is >= 1 (exact, at the label b_{J}). Countercontrol C3: on the product labels alone the
     sup-distance from tau_k to T_psi is t_k times a fixed positive rational (so with product labels only,
     T_psi is a limit of preparations and lies in the completed body).
  R4 SHADOW EXCLUDES T_psi: (a) tau_k and cnot tau_k are positive definite (Sylvester: the leading principal
     minors of pauliW are > 0) for k = 1..4; (b) pauliW T_psi has determinant 0 (T_psi is not in int Q3);
     (c) T_psi is not in C: F = E00/2 - T_psi/4 is nonnegative on both generator families of C (exact SOS
     identity) and ipW(F, T_psi) < 0; (d) sample: the mixtures (1 - s) c + s (sum of lambda_J rho_J) with
     s > 0 listed in the script are positive definite (Sylvester).
  R5 NORMING: for each listed rational vector c with finite support, max over finite S of |sum_{J in S} c_J|
     >= (1/2) sum_J |c_J| (exact enumeration of S).
  R6 M_int VARIANT: for t in the listed rationals, tau'_t = (1 - t) idW + t E00 satisfies the identity
     a^T tau'_t b = (1 - t)(a.b) + t a0 b0 (symbolic), lies outside Q3 for the listed t < 2/3
     (<singlet| pauliW tau'_t |singlet> < 0), and idW is not in Q3 while idW lies in maxCone (landed probe M_int.1,
     M_max.3 re-checked by the identity pairVal a b idW = a.b).
  COUNTERCONTROL C4: the joint labels are load-bearing for R2: with them removed, the value vectors of
     rho_1..rho_8 (product labels of stage 4 only) have rank strictly smaller than 8, the rank they have on
     the joint labels.
  VERDICT: printed iff all checks and countercontrols pass; otherwise 'VERDICT: not rendered', exit 1.
Deterministic output; no timing.
"""
import re
import sys
from fractions import Fraction as Fr
from itertools import combinations, product
from pathlib import Path

import sympy as sp

R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def note(cid, text):
    print(f'NOTE [written] {cid}  -- {text}', flush=True)


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}
BASE = Path(__file__).resolve().parent.parent / 'base' / 'verification' / 'lean-mathlib' / 'OIBridge'
CD = (BASE / 'CompositeDimension.lean').read_text(encoding='utf-8')
msg = re.search(r'^def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) '
                r'then -1 else 1$', CD, re.M)
neg_src = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))} if msg else None


def lean_table(nm):
    mm = re.search(rf'^def {nm} : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){{4}})', CD, re.M)
    if not mm:
        return None
    T = [[None] * 4 for _ in R4]
    for a, b, v in re.findall(r'\|\s*(\d),\s*(\d)\s*=>\s*(\d)', mm.group(1)):
        T[int(a)][int(b)] = int(v)
    return T


print('== S0 transcription')
chk('S0.tables', 'sgn, pc, pt, phiW transcribed from the base', neg_src == NEG and lean_table('pc') == PC
    and lean_table('pt') == PT
    and 'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD, 'source')


def sgn(m, n):
    return -1 if (m, n) in NEG else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = R
    return M


def actT(R, w):
    return w * homMap(R).T


def prodState(x, y):
    return hom(x) * hom(y).T


def pairVal(a, b, w):
    return (sp.Matrix(a).T * w * sp.Matrix(b))[0, 0]


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


iu = sp.I
S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * sp.kronecker_product(S[m], S[n])
    return out / 4


def pos_def(H):
    """Sylvester's criterion for a Hermitian matrix: all leading principal minors are > 0 (exact)."""
    if (H - H.H).applyfunc(sp.expand) != sp.zeros(*H.shape):
        return False
    for k in range(1, H.shape[0] + 1):
        m = sp.nsimplify(sp.expand(H[:k, :k].det()))
        if not (sp.im(m) == 0 and sp.re(m) > 0):
            return False
    return True


Q = sp.Rational
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
E00 = sp.zeros(4, 4)
E00[0, 0] = 1
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
Tpsi = actT(RH, phiW)


def eff(a0, a):
    return [Q(a0)] + [Q(v) for v in a]


EFFECTS = [eff(1, [0, 0, 0]), eff(Q(1, 2), [Q(1, 2), 0, 0]), eff(Q(1, 2), [0, Q(1, 2), 0]),
           eff(Q(1, 2), [0, 0, Q(1, 2)]), eff(Q(1, 2), [Q(-1, 2), 0, 0]), eff(Q(1, 2), [0, Q(-1, 2), 0]),
           eff(Q(1, 2), [0, 0, Q(-1, 2)]), eff(Q(1, 2), [Q(3, 10), Q(2, 5), 0])]
CPTS = [([1, 0, 0], [0, 0, 1]), ([0, 0, 1], [Q(3, 5), Q(4, 5), 0]), ([Q(2, 3), Q(2, 3), Q(1, 3)], [0, -1, 0]),
        ([0, Q(3, 5), Q(4, 5)], [-1, 0, 0])]
CPREP = []
for (x, y) in CPTS:
    CPREP.append(prodState(x, y))
    CPREP.append(cnot(prodState(x, y)))


def t_(k):
    return Q(1, k + 1)


def tau(k):
    return (1 - t_(k)) * Tpsi + t_(k) * E00


RHO = []
for k in range(1, 5):
    RHO.append(tau(k))
    RHO.append(cnot(tau(k)))


def stage(n):
    preps = [('c', j) for j in range(n)] + [('r', J) for J in range(1, 2 * n + 1)]
    labs = [('p', a, b) for a in range(3 + n) for b in range(3 + n)]
    labs += [('b', Sset) for r in range(0, 2 * n + 1) for Sset in combinations(range(1, 2 * n + 1), r)]
    return preps, labs


def table(prep):
    return CPREP[prep[1]] if prep[0] == 'c' else RHO[prep[1] - 1]


def val(lab, prep):
    if lab[0] == 'p':
        return pairVal(EFFECTS[lab[1]], EFFECTS[lab[2]], table(prep))
    if prep[0] == 'c':
        return 0
    return 1 if prep[1] in lab[1] else 0


print()
print('== S1 the stages (R1)')
okV = True
for n in range(1, 5):
    P, L = stage(n)
    okV = okV and all(0 <= val(l, p) <= 1 for l in L for p in P) and all(val(('p', 0, 0), p) == 1 for p in P)
chk('A3.1', 'R1: stages n = 1..4 are valid (values in [0,1], unit reads 1)', okV, 'enumerate')
okSC = True
for n in range(1, 5):
    for m in range(n, 5):
        Pn, Ln = stage(n)
        Pm, Lm = stage(m)
        okSC = okSC and set(Ln) <= set(Lm) and set(Pn) <= set(Pm)
chk('A3.2', 'R1: labels and preparations of stage n are those of stage m >= n (inclusions; one global table, so '
    'SC-infinity holds)', okSC, 'enumerate')
BAS = [EFFECTS[i] for i in range(4)]
M16 = sp.Matrix(16, 16, lambda r, c: BAS[r // 4][c // 4] * BAS[r % 4][c % 4])
M16inv = M16.inv()
okRead = True
for p in stage(4)[0]:
    v = sp.Matrix([val(('p', r // 4, r % 4), p) for r in range(16)])
    w = M16inv * v
    okRead = okRead and sp.Matrix(4, 4, lambda i, j: w[4 * i + j]) == table(p)
chk('A3.3', 'R1: the 16 basis product labels read back the table of every preparation of stage 4 (TAB read-out)',
    okRead, 'enumerate', '12 preparations')

print()
print('== S2 rank growth (R2) and no convergent subsequence (R3)')
ranks = []
for n in range(1, 5):
    P, L = stage(n)
    Lb = [l for l in L if l[0] == 'b']
    Mb = sp.Matrix([[val(l, ('r', J)) for l in Lb] for J in range(1, 2 * n + 1)])
    ranks.append(Mb.rank())
chk('A3.4', 'R2: the joint-label values of rho_1..rho_2n have rank 2n for n = 1..4', ranks == [2, 4, 6, 8], 'witness',
    f'ranks {ranks}')
P4, L4 = stage(4)
okSep = True
for J in range(1, 9):
    for K in range(1, 9):
        if J != K:
            okSep = okSep and abs(val(('b', (J,)), ('r', J)) - val(('b', (J,)), ('r', K))) >= 1
chk('A3.5', 'R3: at stage 4 the value vectors of rho_J, rho_K (J != K) are at sup-distance >= 1 (label b_{J})', okSep,
    'enumerate', '56 ordered pairs')
Lp = [l for l in L4 if l[0] == 'p']
D0 = max(abs(pairVal(EFFECTS[l[1]], EFFECTS[l[2]], E00 - Tpsi)) for l in Lp)
dists = [max(abs(pairVal(EFFECTS[l[1]], EFFECTS[l[2]], tau(k) - Tpsi)) for l in Lp) for k in range(1, 5)]
chk('C3', 'countercontrol: on product labels the sup-distance from tau_k to T_psi is t_k * D0 with D0 > 0 '
    '(so without joint labels T_psi is a limit point of the preparations)',
    D0 > 0 and dists == [t_(k) * D0 for k in range(1, 5)], 'countercontrol', f'D0 = {D0}, distances {dists}')
Mprod = sp.Matrix([[val(l, ('r', J)) for l in Lp] for J in range(1, 9)])
rkp = Mprod.rank()
chk('C4', 'countercontrol: without the joint labels the value vectors of rho_1..rho_8 have rank < 8 (their rank on '
    'the joint labels, A3.4)', rkp < ranks[3], 'countercontrol', f'rank {rkp} vs {ranks[3]}')

print()
print('== S3 the shadow excludes T_psi (R4)')
okPD = all(pos_def(pauliW(tau(k))) and pos_def(pauliW(cnot(tau(k)))) for k in range(1, 5))
chk('A3.6', 'R4(a): tau_k and cnot tau_k are positive definite for k = 1..4 (Sylvester)', okPD, 'witness')
dT = sp.simplify(pauliW(Tpsi).det())
chk('A3.7', 'R4(b): det pauliW(T_psi) = 0 (T_psi is not in int Q3)', dT == 0, 'witness', f'det {dT}')
xs = sp.symbols('x1 x2 x3', real=True)
ys = sp.symbols('y1 y2 y3', real=True)
X3, Y3 = sp.Matrix(xs), sp.Matrix(ys)
P13 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
OC = cnot(Tpsi)[1:4, 1:4]
Fw = E00 / 2 - Tpsi / 4


def sos(O):
    v = X3 - O * Y3
    return Q(1, 8) * v.dot(v) + Q(1, 8) * (1 - X3.dot(X3)) + Q(1, 8) * (1 - Y3.dot(Y3))


okF = sp.expand(ipW(Fw, prodState(xs, ys)) - sos(P13)) == 0
okF = okF and sp.expand(ipW(Fw, cnot(prodState(xs, ys))) - sos(OC)) == 0
okF = okF and OC.T * OC == sp.eye(3)
vF = ipW(Fw, Tpsi)
chk('A3.8', 'R4(c): F = E00/2 - T_psi/4 is >= 0 on both generator families of C (exact SOS identity) and '
    'ipW(F, T_psi) < 0, so T_psi is not in C', okF and vF < 0, 'witness', f'value {vF}')
mixes = [(Q(1, 2), CPREP[0], [Q(1, 2), Q(1, 2), 0, 0]), (Q(1, 3), CPREP[1], [Q(1, 4), 0, Q(1, 4), Q(1, 2)]),
         (Q(9, 10), CPREP[3], [0, 0, 0, 1]), (Q(99, 100), CPREP[5], [Q(1, 3), Q(1, 3), Q(1, 3), 0])]
okMix = True
for s_, c_, lam in mixes:
    avg = sum((lam[J] * RHO[J] for J in range(4)), sp.zeros(4, 4))
    okMix = okMix and pos_def(pauliW((1 - s_) * c_ + s_ * avg))
chk('A3.9', 'R4(d): sample mixtures (1 - s) c + s sum lambda_J rho_J (s > 0, c in C) are positive definite', okMix,
    'sample', f'{len(mixes)} mixtures')

print()
print('== S4 the norming inequality (R5)')
vecs = [[Q(1), Q(-1)], [Q(1, 2), Q(-1, 3), Q(1, 6), Q(-1, 4)], [Q(3), Q(-1), Q(-1), Q(-1)],
        [Q(1, 5), Q(1, 5), Q(-2, 5), Q(1, 10), Q(-1, 10)], [Q(-7), Q(2), Q(5), Q(-1), Q(1), Q(0)]]
okN = True
for c in vecs:
    idx = range(len(c))
    m = max(abs(sum(c[i] for i in Ssub)) for r in range(len(c) + 1) for Ssub in combinations(idx, r))
    okN = okN and m >= Q(1, 2) * sum(abs(v) for v in c)
chk('A3.10', 'R5: max over S of |sum_{J in S} c_J| >= (1/2) sum |c_J| on the listed vectors', okN, 'sample',
    f'{len(vecs)} vectors')
note('A3.W1', 'the inequality holds for every finitely supported c (take S the support of its positive part or of its '
     'negative part) and passes to l^1 limits; it makes lambda -> (sum_{J in S} lambda_J)_S an isomorphic embedding '
     'of l^1 into the joint-label coordinates, so sup-norm Cauchy sequences of convex combinations have l^1-convergent '
     'rho-weights.')

print()
print('== S5 the M_int variant (R6)')
asym = sp.symbols('a0:4', real=True)
bsym = sp.symbols('b0:4', real=True)
tt = sp.Symbol('t', real=True)
taup = (1 - tt) * idW + tt * E00
okI = sp.expand(pairVal(asym, bsym, taup) - ((1 - tt) * sum(asym[i] * bsym[i] for i in R4) + tt * asym[0] * bsym[0])) == 0
singlet = sp.Matrix([0, 1, -1, 0])
okI = okI and all(sp.simplify((singlet.H * pauliW(taup.subs(tt, tv)) * singlet)[0, 0]) < 0
                  for tv in (Q(1, 10), Q(1, 3), Q(1, 2), Q(13, 20)))
okI = okI and sp.expand(pairVal(asym, bsym, idW) - sum(asym[i] * bsym[i] for i in R4)) == 0
okI = okI and (singlet.H * pauliW(idW) * singlet)[0, 0] == -1
chk('A3.11', 'R6: a^T tau\'_t b = (1-t) a.b + t a0 b0 (symbolic); tau\'_t is outside Q3 for t = 1/10, 1/3, 1/2, 13/20; '
    'pairVal a b idW = a.b and idW is outside Q3 (singlet value -1)', okI, 'identity')
note('A3.W2', 'for a, b in the Lorentz cone L with a0, b0 > 0, a.b >= a0 b0 - |a||b| >= 0, so a^T tau\'_t b >= t a0 b0 > 0: '
     'tau\'_t lies in int maxCone for 0 < t, and tau\'_t -> idW, which lies in maxCone and not in Q3. With C = the '
     'normalized slice of Q3 in place of SEP + cnot SEP and a rho-family dense in int maxCone, the written argument '
     'W-A3 realizes M_int\'s cone int maxCone u Q3 as the shadow of a completed body in the same way.')

print()
kinds = {}
for _, k, _ in CHECKS:
    kinds[k] = kinds.get(k, 0) + 1
print('kinds: ' + ', '.join(f'{k} {v}' for k, v in sorted(kinds.items())))
failed = [c for c, _, ok in CHECKS if not ok]
if failed:
    print(f'a3_shadow_countermodel: FAILED -- {len(failed)} of {len(CHECKS)}: {", ".join(failed)}')
    print('VERDICT: not rendered')
    sys.exit(1)
print(f'a3_shadow_countermodel: OK -- {len(CHECKS)} checks')
print('VERDICT A3: the finite skeleton of D_cl is a valid system of finite stages with one global table and bi-affine '
      'product tables; its rank grows without bound; its rho-preparations are pairwise at sup-distance >= 1 while '
      'their product tables converge to T_psi, which lies outside C and outside int Q3. These are the exact inputs of '
      'the written argument W-A3 that the shadow of the completed body of D_cl is K_cl.')
