#!/usr/bin/env python3
"""Thread C (FOUR-COMP) -- c3: exact ingredients of the sufficiency route and of its converse.

Research only. Exact arithmetic (sympy Rationals, polynomial identities); no floating point, no randomness, no time in
stdout. Reads design and landed Lean sources read-only to check the statements cited. Usage:
    python3 -I -B c3_route_ingredients.py <base>/verification/lean-mathlib/OIBridge <inputs>/fourcopy

Conventions as in c2_carrier_models.py (flat index 4a + b; hat x = (1, x); token order (0, 1, 2, 3); grouping A = 01|23,
grouping B = 02|13; T_A, T_B the coordinate readouts; sigma the regrouping of the 17x17 carrier).

The route (written in RESULT.md, node A): from two COMP-1 pre-composites PA, PB of the pair bodies with one body and
TokProdState (TPS), the KT4Core fields follow; tokB follows because Phi(u, w) := T_A(PB.prodState u w)[a,b,c,d] is
bi-affine (landed combo laws) and equals Psi(u, w) := u[4a+c] w[4b+d] at the 16 x 16 token-product pairs (TPS and the
evaluation law). This script checks the exact linear algebra that turns that agreement into agreement on the
hyperplane H00 = {u : u[0] = 1} containing every pair body, and the ingredients of the variant with first-order
independent preparation (IP1) in place of TPS.

DECISION RULE (fixed before the first run). Every check prints PASS or FAIL; a [countercontrol] passes exactly when
the mutated object gives the opposite verdict. 'VERDICT C3-ROUTE-INGREDIENTS-EXACT' is printed if and only if every
check passes; otherwise 'VERDICT NOT RENDERED' with the failed ids, and exit status 1. Written steps are NOTE [written]
lines and are not checks.

Sections:
  S0  transcription of the cited statements (Lemma B1, KT4Core fields, exists_effect_rescale).
  S1  extension step: a bi-affine map restricted to H00 x H00 is a bilinear form u^T C w (symbolic), so its values at
      the token-product pairs determine it (the token-product matrix is invertible), with a countercontrol.
  S2  the IP1 variant: the purity core identity; the two-token countercontrols (purity, positivity); a four-token model
      CORR in which first-order independent preparation holds in both directions, the token clauses fail, and the
      positivity that one body would supply fails.
  S3  the converse: in the canonical model MSIG the cross values are exactly the FCC forms, so FCC gives KT4- with TPS.
  S4  relabelling covariance in the anchor sum on uniform cones (a candidate that holds where FCC can fail).
"""
import sys
from itertools import product
from pathlib import Path

import sympy as sp

Q = sp.Rational
R4 = range(4)
R17 = range(17)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def note(cid, text):
    print(f"NOTE [written] {cid}  -- {text}", flush=True)


def section(title):
    print()
    print(f"== {title}", flush=True)


def ex(v):
    return sp.expand(v)


if len(sys.argv) != 3:
    print('usage: c3_route_ingredients.py <OIBridge dir> <inputs/fourcopy dir>')
    sys.exit(2)
OIB = Path(sys.argv[1])
FCP = Path(sys.argv[2])


def zeros17():
    return [[sp.Integer(0)] * 17 for _ in R17]


def outer(u, v):
    return [[u[i] * v[j] for j in R17] for i in R17]


def add17(P, Q_):
    return [[P[i][j] + Q_[i][j] for j in R17] for i in R17]


def sub17(P, Q_):
    return [[P[i][j] - Q_[i][j] for j in R17] for i in R17]


def scale17(c, P):
    return [[c * P[i][j] for j in R17] for i in R17]


def eq17(P, Q_):
    return all(ex(P[i][j] - Q_[i][j]) == 0 for i in R17 for j in R17)


def hat(x):
    return [sp.Integer(1)] + list(x)


def iota(Z):
    P = zeros17()
    for a, b, c, d in product(R4, repeat=4):
        P[1 + 4 * a + b][1 + 4 * c + d] = Z[(a, b, c, d)]
    for c, d in product(R4, repeat=2):
        P[0][1 + 4 * c + d] = Z[(0, 0, c, d)]
    for a, b in product(R4, repeat=2):
        P[1 + 4 * a + b][0] = Z[(a, b, 0, 0)]
    P[0][0] = Z[(0, 0, 0, 0)]
    return P


def pi_(P):
    return {(a, b, c, d): P[1 + 4 * a + b][1 + 4 * c + d] for a, b, c, d in product(R4, repeat=4)}


def Rg(Z):
    return {(a, b, c, d): Z[(a, c, b, d)] for a, b, c, d in product(R4, repeat=4)}


def sigma(P):
    Z = pi_(P)
    return add17(sub17(P, iota(Z)), iota(Rg(Z)))


def homv(x):
    return [sp.Integer(1)] + list(x)


def tp(x, y):
    hx, hy = homv(x), homv(y)
    return [hx[a] * hy[b] for a in R4 for b in R4]


def Htab(x0, x1, x2, x3):
    h = [homv(x0), homv(x1), homv(x2), homv(x3)]
    return {(a, b, c, d): h[0][a] * h[1][b] * h[2][c] * h[3][d] for a, b, c, d in product(R4, repeat=4)}


def TA(P):
    return {(a, b, c, d): P[1 + 4 * a + b][1 + 4 * c + d] for a, b, c, d in product(R4, repeat=4)}


def TB(P):
    return {(a, b, c, d): P[1 + 4 * a + c][1 + 4 * b + d] for a, b, c, d in product(R4, repeat=4)}


def marg(T, t, i):
    idx = [0, 0, 0, 0]
    idx[t] = i
    return T[tuple(idx)]


S_states = [[sp.Integer(v) for v in s] for s in ([1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1])]

# ===============================================================================================================
section('S0  transcription of the cited statements')

FBR = (FCP / 'FourCopyBridge.lean').read_text(encoding='utf-8')
FCORE = (FCP / 'FourCopyCore.lean').read_text(encoding='utf-8')
CI = (OIB / 'CompositeInterface.lean').read_text(encoding='utf-8')
chk('S0.B1', 'design Lemma B1: fourCopyCoherent_of_kt4Core takes the maxCone bound and nonnegative scaling of each '
    'cone and H : KT4Core, and gives FourCopyCoherent', all(s in FBR for s in (
        'theorem fourCopyCoherent_of_kt4Core',
        '(m01 : K01 ⊆ maxCone (eball 3))',
        '(s01 : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K01, c • ω ∈ K01)',
        '(H : KT4Core K01 K23 K02 K13 V) : FourCopyCoherent K01 K23 K02 K13 where')), 'source')
chk('S0.core', 'design KT4Core fields: stA, stB, effA, effB, effA_apply, effB_apply, posBA, posAB, tokA, tokB',
    all(f'  {nm} :' in FCORE for nm in ('stA', 'stB', 'effA', 'effB', 'effA_apply', 'effB_apply', 'posBA', 'posAB',
                                         'tokA', 'tokB')), 'source')
chk('S0.resc', 'landed exists_effect_rescale: an affine functional bounded on Omega is a e\' + c unitEff with e\' an '
    'effect (used by the vanishing step of the IP1 variant)', 'theorem exists_effect_rescale {Ω : Set (Fin d → ℝ)} '
    '(hb : BoundedAffine Ω)' in CI and 'IsEffectOn Ω e\' ∧ e = a • e\' + c • unitEff d' in CI, 'source')

# ===============================================================================================================
section('S1  the extension step is exact linear algebra')

us = sp.symbols('u1:16', real=True)
ws = sp.symbols('w1:16', real=True)
u = [sp.Integer(1)] + list(us)              # a point of H00
w = [sp.Integer(1)] + list(ws)
al = sp.Symbol('alpha', real=True)
be = sp.symbols('beta0:16', real=True)
ga = sp.symbols('gamma0:16', real=True)
De = sp.Matrix(16, 16, lambda i, j: sp.Symbol(f'D{i}_{j}', real=True))
Phi = al + sum(be[i] * u[i] for i in range(16)) + sum(ga[j] * w[j] for j in range(16)) + \
    sum(u[i] * De[i, j] * w[j] for i in range(16) for j in range(16))
C = De + al * sp.Matrix(16, 16, lambda i, j: 1 if (i, j) == (0, 0) else 0) + \
    sp.Matrix(16, 16, lambda i, j: be[i] if j == 0 else 0) + sp.Matrix(16, 16, lambda i, j: ga[j] if i == 0 else 0)
uM, wM = sp.Matrix(u), sp.Matrix(w)
chk('E1', 'on H00 x H00 the general bi-affine map alpha + beta.u + gamma.w + u^T D w equals u^T C w with '
    'C = D + alpha e0 e0^T + beta e0^T + e0 gamma^T (symbolic, 289 coefficients)', ex(Phi - (uM.T * C * wM)[0, 0]) == 0,
    'identity')
TPm = sp.Matrix([tp(s, t) for s in S_states for t in S_states])
chk('E2', 'the 16 x 16 matrix of token products (rows tp s t, s, t in S) is invertible, and each row lies in H00',
    TPm.det() != 0 and all(TPm[k, 0] == 1 for k in range(16)), 'witness', f'det {TPm.det()}')
note('E.W', 'by E1, a bi-affine map Phi on Q^16 x Q^16 (affine in each argument in the combo sense of the landed '
     'ProductData laws, hence of the form alpha + beta.u + gamma.w + u^T D w) agrees on H00 x H00 with the bilinear form '
     'u^T C_Phi w. Two such maps that agree at the 256 pairs (tp s t, tp s\' t\') have TPm C TPm^T equal, hence by E2 '
     'C equal, hence agree on all of H00 x H00, which contains pairBody K x pairBody K\' for any cones (pairBody points '
     'have coordinate (0,0) equal to 1). This is the step tokB (and tokA) of the route takes from TPS.')
# countercontrol: a nonzero bilinear form vanishing on the 9 products from {e_x,e_y,e_z}^2 exists (they do not span)
sub9 = sp.Matrix([tp(s, t) for s in S_states[:3] for t in S_states[:3]])
ns = sub9.nullspace()
chk('E2c', 'countercontrol: the 9 token products of {e_x, e_y, e_z} leave a nonzero linear functional vanishing on '
    'them (agreement there would not determine the map)', len(ns) > 0 and any(v != 0 for v in ns[0]), 'countercontrol',
    f'kernel dimension {len(ns)}')

# ===============================================================================================================
section('S2  the IP1 variant: purity and positivity')

c0 = sp.Symbol('c0', real=True)
cv = sp.symbols('c1:4', real=True)
xv = sp.symbols('x1:4', real=True)
lhs = sum((cv[i] - c0 * xv[i]) ** 2 for i in range(3))
rhs = sum(c ** 2 for c in cv) - 2 * c0 * sum(cv[i] * xv[i] for i in range(3)) + c0 ** 2 * sum(x ** 2 for x in xv)
cx = sum(cv[i] * xv[i] for i in range(3))
xx = sum(x ** 2 for x in xv)
chk('U1', 'purity core: |cvec - c0 x|^2 = |cvec|^2 - c0^2 + c0^2 (|x|^2 - 1) - 2 c0 (cvec.x - c0), so with |x| = 1 and '
    'c0 = cvec.x it is |cvec|^2 - c0^2, which is <= 0 for c in the Lorentz cone L (symbolic)', ex(lhs - rhs) == 0
    and ex(lhs - (sum(c ** 2 for c in cv) - c0 ** 2 + c0 ** 2 * (xx - 1) - 2 * c0 * (cx - c0))) == 0, 'identity')
note('U.W', 'purity lemma (written; core U1): let T be an n-token table with T(u,...,u) = 1, T(v1,...,vn) >= 0 for all '
     'v_i in L, and pure single-token marginals hom x_t. For w = (1, -x_1) in L, T(w, u, ..., u) = 1 - |x_1|^2 = 0, and '
     'a linear functional >= 0 on L that vanishes at the interior point u vanishes identically; slot by slot this gives '
     'T(w, v2, ..., vn) = 0 for all v_i in L. Then c := T(., v2, ..., vn) lies in L* = L with c.w = 0, so by U1 '
     'c = c_0 hom x_1: T = hom x_1 (x) T(u, ., ..., .). Induct on n. Every v in L is a nonnegative multiple of the '
     'coefficient vector of an effect of the ball, so positivity on products of ball effects is positivity on L^n.')
hz = sp.Matrix(homv(S_states[2]))
hmz = sp.Matrix(homv(S_states[3]))
Tc = (hz * hz.T + hmz * hmz.T) / 2
chk('U2', 'countercontrol (purity load-bearing): T = (hom z hom z^T + hom -z hom -z^T)/2 has mixed marginals (1,0,0,0), '
    'is a nonnegative combination of products (so >= 0 on L x L), and is not a product (rank 2)',
    list(Tc[:, 0]) == [1, 0, 0, 0] and list(Tc[0, :]) == [1, 0, 0, 0] and Tc.rank() == 2, 'countercontrol')
Tp = hz * hz.T
Tp[1, 1] += 2
vv, ww = sp.Matrix([1, 1, 0, 0]), sp.Matrix([1, -1, 0, 0])
chk('U3', 'countercontrol (positivity load-bearing): T = hom z hom z^T + 2 e1 e1^T has pure marginals hom z, is not a '
    'product (rank 2), and takes -1 at v = (1,1,0,0), w = (1,-1,0,0) in L', list(Tp[:, 0]) == list(hz)
    and list(Tp[0, :]) == list(hz.T) and Tp.rank() == 2 and (vv.T * Tp * ww)[0, 0] == -1, 'countercontrol')

# the four-token model CORR: B's token products are read by A with an added correlation of zero marginals
KAP = sp.Integer(2)
C0 = {k: sp.Integer(0) for k in product(R4, repeat=4)}
C0[(1, 1, 0, 0)] = sp.Integer(1)
IC0 = iota(C0)
IRC0 = iota(Rg(C0))


def corr_stA(x, y):
    return outer(hat(x), hat(y))


def corr_stB(l, m):
    return add17(sigma(outer(hat(l), hat(m))), scale17(KAP * l[0] * m[0], IC0))


def corr_NA(v):
    return v


def corr_NB(v):
    S_ = sigma(v)
    return sub17(S_, scale17(KAP * S_[1][1], IRC0))


Ls = sp.symbols('l0:16', real=True)
Ms = sp.symbols('m0:16', real=True)


def biaff_ok(P, va, vb):
    for i in R17:
        for j in R17:
            e = ex(P[i][j])
            for vs in (va, vb):
                if e.free_symbols & set(vs) and sp.Poly(e, *vs).total_degree() > 1:
                    return False
    return True


chk('U4', 'CORR: evaluation laws N_A(stA x y) = hat x hat y^T and N_B(stB l l\') = hat l hat l\'^T for all chart '
    'points, and both product maps bi-affine (degree <= 1 in each argument), symbolic',
    eq17(corr_NA(corr_stA(Ls, Ms)), outer(hat(Ls), hat(Ms))) and eq17(corr_NB(corr_stB(Ls, Ms)), outer(hat(Ls), hat(Ms)))
    and biaff_ok(corr_stA(Ls, Ms), Ls, Ms) and biaff_ok(corr_stB(Ls, Ms), Ls, Ms), 'identity')
tok = [sp.symbols(f't{t}_1:4', real=True) for t in range(4)]
pAt = corr_stA(tp(tok[0], tok[1]), tp(tok[2], tok[3]))
pBt = corr_stB(tp(tok[0], tok[2]), tp(tok[1], tok[3]))
TApB = TA(corr_NA(pBt))
TBpA = TB(corr_NB(pAt))
H = Htab(*tok)
ip1ba = all(ex(marg(TApB, t, i) - homv(tok[t])[i]) == 0 for t in R4 for i in R4)
ip1ab = all(ex(marg(TBpA, t, i) - homv(tok[t])[i]) == 0 for t in R4 for i in R4)
dev_ba = {k: ex(TApB[k] - H[k]) for k in H if ex(TApB[k] - H[k]) != 0}
dev_ab = {k: ex(TBpA[k] - H[k]) for k in H if ex(TBpA[k] - H[k]) != 0}
chk('U5', 'CORR: IP1 holds in both directions (symbolic), while T_A(p_B(x)) = H(x) + 2 C0 and T_B(p_A(x)) = H(x) - 2 C0 '
    '(C0 the x-x correlation of tokens 0, 1, zero marginals): the token clauses fail and TPS fails', ip1ba and ip1ab
    and dev_ba == {(1, 1, 0, 0): KAP} and dev_ab == {(1, 1, 0, 0): -KAP}, 'witness',
    f'deviations {dev_ba} and {dev_ab}')
gx_up = [Q(1, 2), Q(1, 2), 0, 0]
gx_dn = [Q(1, 2), Q(-1, 2), 0, 0]
unitv = [1, 0, 0, 0]
xs_ = [S_states[2]] * 4
TApB_z = TA(corr_NA(corr_stB(tp(xs_[0], xs_[2]), tp(xs_[1], xs_[3]))))
val = ex(sum(gx_up[a] * gx_dn[b] * unitv[c] * unitv[d] * TApB_z[(a, b, c, d)] for a, b, c, d in product(R4, repeat=4)))
chk('U6', 'CORR: A\'s product of the token effects (x-up on token 0, x-down on token 1, unit on 2, 3) takes -1/4 at B\'s '
    'token product of (e_z, e_z, e_z, e_z): A\'s product effects are not effects on any body containing B\'s products, '
    'so one body (with COMP-1 positivity) fails', val == Q(-1, 4), 'witness', f'value {val}')
note('U.R', 'CORR shows the positivity input of the purity step is load-bearing in four tokens: first-order independent '
     'preparation in both directions without the positivity that one body supplies does not give the token clauses. In '
     'the route, that positivity is PA.prodEff_effect on PB\'s products, available because PB.Omega = PA.Omega.')

# ===============================================================================================================
section('S3  the converse: in MSIG the cross values are the FCC forms')

eh = sp.symbols('e0:17', real=True)
fh = sp.symbols('f0:17', real=True)
Xs = [sp.Integer(1)] + list(sp.symbols('x1:16', real=True))
Ys = [sp.Integer(1)] + list(sp.symbols('y1:16', real=True))


def Ttab(hv):
    return sp.Matrix(4, 4, lambda a, b: hv[1 + 4 * a + b] + (hv[0] if (a, b) == (0, 0) else 0))


def table(v):
    return sp.Matrix(4, 4, lambda a, b: v[4 * a + b])


def fourVal(X, Y, E, F):
    return sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d] for a, b, c, d in product(R4, repeat=4))


def g2(e, f, L, Lp):
    return sum(e[a, b] * f[c, d] * L[a, c] * Lp[b, d] for a, b, c, d in product(R4, repeat=4))


def bil(ev, P, fv):
    return sum(ev[i] * P[i][j] * fv[j] for i in R17 for j in R17)


NBA = sigma(outer(hat(Xs), hat(Ys)))      # B's readout array of A's product (MSIG: N_B = sigma)
chk('V1', 'MSIG: PB.prodEff e f (PA.prodState x y) = fourVal X Y Et Ft for normalized x, y and all affine e, f '
    '(symbolic; Et the table of e on the normalized slice)', ex(bil(eh, NBA, fh) - fourVal(table(Xs), table(Ys), Ttab(eh),
                                                                                     Ttab(fh))) == 0, 'identity')
NAB = sigma(outer(hat(Xs), hat(Ys)))      # A's readout array of B's product of (l, l') = (x, y)
chk('V2', 'MSIG: PA.prodEff e f (PB.prodState l l\') = g2 Et Ft L L\' for normalized l, l\' (symbolic)',
    ex(bil(eh, NAB, fh) - g2(Ttab(eh), Ttab(fh), table(Xs), table(Ys))) == 0, 'identity')
chk('V2c', 'countercontrol: without the regrouping (reading B\'s product array in A order) the value is not g2',
    ex(bil(eh, outer(hat(Xs), hat(Ys)), fh) - g2(Ttab(eh), Ttab(fh), table(Xs), table(Ys))) != 0, 'countercontrol')
note('V.W', 'converse (written, ingredients V1, V2 and c2 M.MSIG): given FCC for admissible cones, take the MSIG maps and '
     'Omega = conv(A products u B products). An effect of a pair body has its table in the dual cone (landed note H.W), '
     'so by V1, V2 and FCC every cross value is >= 0, and <= 1 by the complement identity; own-grouping values are '
     'e(x) f(y); so both groupings are COMP-1 pre-composites with one body, and TPS holds (c2). Hence, relative to hadm, '
     'the existence of a carrier with KT4- and TPS is equivalent to FCC: this direction, and the route for the other.')

# ===============================================================================================================
section('S4  relabelling covariance in the anchor sum')

E00flat = [sp.Integer(1)] + [sp.Integer(0)] * 15
ANCH = outer(hat(E00flat), hat(E00flat))


def anc_stA(x, y):
    return (outer(hat(x), hat(y)), ANCH)


def anc_stB(l, m):
    return (ANCH, outer(hat(l), hat(m)))


def swap(v):
    return (v[1], v[0])


Vs0 = [[sp.Symbol(f'p{i}_{j}', real=True) for j in R17] for i in R17]
Vs1 = [[sp.Symbol(f'q{i}_{j}', real=True) for j in R17] for i in R17]
okL = all(eq17(c1_, c2_) for c1_, c2_ in zip(swap(anc_stA(Ls, Ms)), anc_stB(Ls, Ms)))
okL = okL and eq17(swap((Vs0, Vs1))[1], Vs0)     # N_B(swap v) = (swap v)[1] = v[0] = N_A(v)
chk('L1', 'anchor sum on uniform cones: the swap of the two carrier components maps PA.prodState to PB.prodState and '
    'PB.prodEff o swap = PA.prodEff (symbolic): relabelling covariance holds', okL, 'identity')
chk('L1c', 'countercontrol: the identity map does not carry PA.prodState to PB.prodState in the anchor sum',
    not all(eq17(c1_, c2_) for c1_, c2_ in zip(anc_stA(Ls, Ms), anc_stB(Ls, Ms))), 'countercontrol')
note('L.W', 'the swap maps Omega = conv(A products u B products) onto itself when the pair bodies coincide (uniform '
     'cones). With uniform K_c (c1 K7: FCC fails at -1) the anchor sum is KT4- with relabelling covariance, so '
     'relabelling covariance with KT4- does not imply FCC.')

# ===============================================================================================================
print()
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'witness', 'source', 'countercontrol')), flush=True)
failed = [c[0] for c in CHECKS if not c[2]]
if failed:
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks; failed: {', '.join(failed)}", flush=True)
    print('VERDICT NOT RENDERED', flush=True)
    sys.exit(1)
print(f'{len(CHECKS)}/{len(CHECKS)} checks', flush=True)
print('VERDICT C3-ROUTE-INGREDIENTS-EXACT', flush=True)
