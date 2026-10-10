#!/usr/bin/env python3
"""Thread C (FOUR-COMP) -- c2: four-token carriers, regrouping invariance and the product-level token clauses.

Research only. Exact arithmetic (sympy Rationals and polynomial identities); no floating point, no randomness, no time
in stdout. Reads landed and design Lean sources read-only to check the statements the checks rest on. Usage:
    python3 -I -B c2_carrier_models.py <base>/verification/lean-mathlib/OIBridge <inputs>/fourcopy

Setting (transcribed; S0 checks the Lean text). A pair chart point is x in Q^16 (flat table, index 4a + b for entry
(a, b), as finProdFinEquiv); hat x = (1, x) in Q^17; an affine functional e(x) = e0 + E.x has coefficient vector
ehat = (e0, E), so e(x) = ehat . hat x. COMP-1 ProductData (CompositeInterface.lean): a bi-affine prodState and a
bilinear prodEff with prodEff e f (prodState x y) = e x * f y for ALL chart points x, y. In every model below each
grouping's product effect is a bilinear form ehat^T N(v) fhat with N linear on the carrier V, so the evaluation law
is the identity N(prodState x y) = hat x hat y^T.

Token order (a, b, c, d) = tokens (0, 1, 2, 3). Grouping A = 01|23, grouping B = 02|13. Readouts:
    T_A(v)[a,b,c,d] = PA.prodEff (tabCoord a b) (tabCoord c d) v = N_A(v)[1+4a+b][1+4c+d],
    T_B(v)[a,b,c,d] = PB.prodEff (tabCoord a c) (tabCoord b d) v = N_B(v)[1+4a+c][1+4b+d].
Token products: tp x y = flat(prodState x y); p_A(x) = PA.prodState (tp x0 x1) (tp x2 x3);
p_B(x) = PB.prodState (tp x0 x2) (tp x1 x3); H(x)[a,b,c,d] = hom x0_a hom x1_b hom x2_c hom x3_d.
Predicates:
  TPS     p_A(x) = p_B(x) for all token vectors x (state-level regrouping invariance of independent preparation);
  IP1_BA  the single-token marginal entries of T_A(p_B(x)) are hom x_t (B's token products read by A, first order);
  IP1_AB  the same for T_B(p_A(x));
  tokA    T_B(PA.prodState x y)[a,b,c,d] = x[4a+b] y[4c+d] for normalized x, y (KT4Core.tokA via the evaluation law);
  tokB    T_A(PB.prodState l l')[a,b,c,d] = l[4a+c] l'[4b+d] for normalized l, l' (KT4Core.tokB).
Each predicate is checked as a universal polynomial identity in symbolic arguments; a failure is reported with an exact
witness at a point of S^4, S = {e_x, e_y, e_z, -e_z} (pure states).

The regrouping sigma on the 17x17 carrier (EQ5-SOURCE's construction, re-implemented here): iota embeds a 4-token
table Z (iota Z [0][0] = Z0000, [0][1+4c+d] = Z00cd, [1+4a+b][0] = Zab00, [1+4a+b][1+4c+d] = Zabcd), pi reads the
inner block, R exchanges the middle indices (R Z)abcd = Zacbd, sigma = iota R pi + (id - iota pi).

Models (cones in the order 01, 23, 02, 13; body-level claims are written notes resting on c1 and the landed probe):
  MSIG  PA = modelData, PB = sigma o modelData on V = Q^{17x17}; uniform Q3: the satisfiability control.
  SEPH  the MSIG maps with separate bodies PA.Omega = minBody A, PB.Omega = minBody B, on (Q3, Q3, Q3, twin).
  ANC   the anchor sum on V = (Q^{17x17})^2, anchors at the flattened E00, on (Q3, Q3, Q3, twin).
  MTW   PB = (sigma o modelData) with token 3 read through rho = actT reflY on pair 13, on (Q3, Q3, Q3, twin).
  MTH   the same with theta = actT(-I).
  MRHO  EQ5-SOURCE's M_rho: PB.prodState l l' = pState l (rho l'), no regrouping.
  MT    the transposed-factor model: pair 02 read token-exchanged, uniform Q3.
  HBA   hybrid on V = (Q^{17x17})^2: A reads component 1, B reads component 2 (in B order); A's products carry a
        B-anchor in component 2, B's products are (sigma b, b): on (Q3, Q3, K_c, K_c).
  HAB   the mirror hybrid, on (K_c, K_c, Q3, Q3).
  PAD   the MSIG maps on V = Q^{17x17} x Q with an extra body point at height 1 that B reads through a shift: uniform Q3.

DECISION RULE (fixed before the first run). Every line below is a check that prints PASS or FAIL; a [countercontrol]
passes exactly when the mutated object gives the opposite verdict. The script prints
'VERDICT C2-CARRIER-MODELS-EXACT' if and only if every check passes; otherwise 'VERDICT NOT RENDERED' with the failed
ids, and exit status 1. A claim that a predicate HOLDS is checked as a universal polynomial identity; a claim that it
FAILS is checked by an exact witness. Written steps (positivity of cross values from cone facts; the affine-extension
argument of the route) are printed as NOTE [written] lines and are not checks.
"""
import re
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
    print('usage: c2_carrier_models.py <OIBridge dir> <inputs/fourcopy dir>')
    sys.exit(2)
OIB = Path(sys.argv[1])
FCP = Path(sys.argv[2])

# ---------------------------------------------------------------------------------------------------------------
# arrays: a 17x17 array is a list of 17 lists; a 4-token table is a dict (a,b,c,d) -> value


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


def colsign17(P, sg):
    """P . diag(sg) with sg a length-17 sign vector"""
    return [[P[i][j] * sg[j] for j in R17] for i in R17]


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


def TA(NA_v):
    return {(a, b, c, d): NA_v[1 + 4 * a + b][1 + 4 * c + d] for a, b, c, d in product(R4, repeat=4)}


def TB(NB_v):
    return {(a, b, c, d): NB_v[1 + 4 * a + c][1 + 4 * b + d] for a, b, c, d in product(R4, repeat=4)}


def flat_table(M):
    return [M[a, b] for a in R4 for b in R4]


# sign vectors on hat indices for one-copy charts acting on the SECOND token of a pair (index d of flat 4b+d)
def second_token_signs(sg4):
    return [sp.Integer(1)] + [sg4[j % 4] for j in range(16)]


def apply_second_token(sg4, l):
    return [l[j] * sg4[j % 4] for j in range(16)]


def swap_pair(l):
    """token exchange inside a pair table: (tau l)[4a+c] = l[4c+a]"""
    return [l[4 * (j % 4) + j // 4] for j in range(16)]


RHO = [1, 1, -1, 1]       # homMap reflY
THETA = [1, -1, -1, -1]   # homMap (-I)

S_states = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]]
S_states = [[sp.Integer(v) for v in s] for s in S_states]

# symbolic arguments
Xs = sp.symbols('x0:16', real=True)
Ys = sp.symbols('y0:16', real=True)
Ls = sp.symbols('l0:16', real=True)
Ms = sp.symbols('m0:16', real=True)
Xn = [sp.Integer(1)] + list(Xs[1:])
Yn = [sp.Integer(1)] + list(Ys[1:])
Ln = [sp.Integer(1)] + list(Ls[1:])
Mn = [sp.Integer(1)] + list(Ms[1:])
tok = [sp.symbols(f't{t}_1:4', real=True) for t in range(4)]

# ---------------------------------------------------------------------------------------------------------------
# models. Each: stA(x, y), stB(l, l') -> V; NA(v), NB(v) -> 17x17 array; V is a tuple of components.

E00flat = [sp.Integer(1)] + [sp.Integer(0)] * 15          # flat E00 = tp(0, 0): in every admissible pair body
ANCH = outer(hat(E00flat), hat(E00flat))                  # anchor array (A order = B order for E00 x E00)
xstar = [S_states[2]] * 4                                 # (e_z, e_z, e_z, e_z)
xprime = [S_states[3], S_states[2], S_states[2], S_states[2]]   # (-e_z, e_z, e_z, e_z)
DELTA = sub17(iota(Htab(*xprime)), iota(Htab(*xstar)))


def mk_msig():
    return dict(
        stA=lambda x, y: (outer(hat(x), hat(y)),),
        stB=lambda l, m: (sigma(outer(hat(l), hat(m))),),
        NA=lambda v: v[0],
        NB=lambda v: sigma(v[0]))


def mk_twist(sg4):
    sgh = second_token_signs(sg4)
    return dict(
        stA=lambda x, y: (outer(hat(x), hat(y)),),
        stB=lambda l, m: (sigma(outer(hat(l), hat(apply_second_token(sg4, m)))),),
        NA=lambda v: v[0],
        NB=lambda v: colsign17(sigma(v[0]), sgh))


def mk_mrho():
    sgh = second_token_signs(RHO)
    return dict(
        stA=lambda x, y: (outer(hat(x), hat(y)),),
        stB=lambda l, m: (outer(hat(l), hat(apply_second_token(RHO, m))),),
        NA=lambda v: v[0],
        NB=lambda v: colsign17(v[0], sgh))


def mk_mt():
    # pair 02 read token-exchanged: PB.prodState l l' = sigma(pState (tau l) l'), PB.prodEff e f = pEff (e o tau) f o sigma
    perm = [0] + [1 + 4 * (j % 4) + j // 4 for j in range(16)]   # hat index permutation of tau

    def NB(v):
        S_ = sigma(v[0])
        return [[S_[perm[i]][j] for j in R17] for i in R17]
    return dict(
        stA=lambda x, y: (outer(hat(x), hat(y)),),
        stB=lambda l, m: (sigma(outer(hat(swap_pair(l)), hat(m))),),
        NA=lambda v: v[0],
        NB=NB)


def mk_anc():
    return dict(
        stA=lambda x, y: (outer(hat(x), hat(y)), ANCH),
        stB=lambda l, m: (ANCH, outer(hat(l), hat(m))),
        NA=lambda v: v[0],
        NB=lambda v: v[1])


def mk_hba():
    return dict(
        stA=lambda x, y: (outer(hat(x), hat(y)), ANCH),
        stB=lambda l, m: (sigma(outer(hat(l), hat(m))), outer(hat(l), hat(m))),
        NA=lambda v: v[0],
        NB=lambda v: v[1])


def mk_hab():
    return dict(
        stA=lambda x, y: (outer(hat(x), hat(y)), sigma(outer(hat(x), hat(y)))),
        stB=lambda l, m: (ANCH, outer(hat(l), hat(m))),
        NA=lambda v: v[0],
        NB=lambda v: v[1])


def mk_pad():
    return dict(
        stA=lambda x, y: (outer(hat(x), hat(y)), sp.Integer(0)),
        stB=lambda l, m: (sigma(outer(hat(l), hat(m))), sp.Integer(0)),
        NA=lambda v: v[0],
        NB=lambda v: sigma(add17(v[0], scale17(v[1], DELTA))))


MODELS = {'MSIG': mk_msig(), 'MTW': mk_twist(RHO), 'MTH': mk_twist(THETA), 'MRHO': mk_mrho(), 'MT': mk_mt(),
          'ANC': mk_anc(), 'HBA': mk_hba(), 'HAB': mk_hab(), 'PAD': mk_pad()}


def veq(u, v):
    if len(u) != len(v):
        return False
    for cu, cv in zip(u, v):
        if isinstance(cu, list):
            if not eq17(cu, cv):
                return False
        elif ex(cu - cv) != 0:
            return False
    return True


# ---------------------------------------------------------------------------------------------------------------
def eval_law(M):
    okA = eq17(M['NA'](M['stA'](Xs, Ys)), outer(hat(Xs), hat(Ys)))
    okB = eq17(M['NB'](M['stB'](Ls, Ms)), outer(hat(Ls), hat(Ms)))
    return okA and okB


def biaffine(M):
    def ok_entry(e, va, vb):
        e = ex(e)
        if e.free_symbols - set(va) - set(vb):
            return False
        pa = sp.Poly(e, *va) if e.free_symbols & set(va) else None
        pb = sp.Poly(e, *vb) if e.free_symbols & set(vb) else None
        return (pa is None or pa.total_degree() <= 1) and (pb is None or pb.total_degree() <= 1)
    for st, va, vb in ((M['stA'](Xs, Ys), Xs, Ys), (M['stB'](Ls, Ms), Ls, Ms)):
        for comp in st:
            entries = [comp[i][j] for i in R17 for j in R17] if isinstance(comp, list) else [comp]
            if not all(ok_entry(e, va, vb) for e in entries):
                return False
    return True


def pA(M, x):
    return M['stA'](tp(x[0], x[1]), tp(x[2], x[3]))


def pB(M, x):
    return M['stB'](tp(x[0], x[2]), tp(x[1], x[3]))


def tps(M):
    if veq(pA(M, tok), pB(M, tok)):
        return True, ''
    for x in product(S_states, repeat=4):
        if not veq(pA(M, list(x)), pB(M, list(x))):
            return False, f'differs at x = {[list(map(int, s)) for s in x]}'
    return False, 'differs symbolically'


def marg(T, t, i):
    idx = [0, 0, 0, 0]
    idx[t] = i
    return T[tuple(idx)]


def ip1(M, direction, x):
    T = TA(M['NA'](pB(M, x))) if direction == 'BA' else TB(M['NB'](pA(M, x)))
    bad = []
    for t in R4:
        for i in R4:
            if ex(marg(T, t, i) - homv(x[t])[i]) != 0:
                bad.append(t)
                break
    return sorted(set(bad))


def ip1_check(M, direction):
    bad = ip1(M, direction, tok)
    if not bad:
        return True, ''
    wit = []
    for x in product(S_states, repeat=4):
        b = ip1(M, direction, list(x))
        if b:
            wit = (b, [list(map(int, s)) for s in x])
            break
    return False, f'symbolic failure at tokens {bad}; witness tokens {wit[0]} at x = {wit[1]}' if wit else \
        f'symbolic failure at tokens {bad}'


def tokA(M, x, y):
    T = TB(M['NB'](M['stA'](x, y)))
    return all(ex(T[(a, b, c, d)] - x[4 * a + b] * y[4 * c + d]) == 0 for a, b, c, d in product(R4, repeat=4))


def tokB(M, l, m):
    T = TA(M['NA'](M['stB'](l, m)))
    return all(ex(T[(a, b, c, d)] - l[4 * a + c] * m[4 * b + d]) == 0 for a, b, c, d in product(R4, repeat=4))


def tok_check(M, which):
    f = tokA if which == 'A' else tokB
    a1, a2 = (Xn, Yn) if which == 'A' else (Ln, Mn)
    if f(M, a1, a2):
        return True, ''
    for s0, s1, s2, s3 in product(S_states, repeat=4):
        u = tp(s0, s1) if which == 'A' else tp(s0, s2)
        w = tp(s2, s3) if which == 'A' else tp(s1, s3)
        if not f(M, u, w):
            return False, f'fails at the token product {[list(map(int, s)) for s in (s0, s1, s2, s3)]}'
    return False, 'fails symbolically'


# ===============================================================================================================
section('S0  transcription of the statements used')

CI = (OIB / 'CompositeInterface.lean').read_text(encoding='utf-8')
FCORE = (FCP / 'FourCopyCore.lean').read_text(encoding='utf-8')
FBR = (FCP / 'FourCopyBridge.lean').read_text(encoding='utf-8')
chk('S0.combo', 'landed ProductData combo laws: for all chart points and all a + b = 1 (CompositeInterface.lean)',
    'prodState_combo_left : ∀ (x x\' : Fin dA → ℝ) (y : Fin dB → ℝ) (a b : ℝ), a + b = 1 →' in CI
    and 'prodState_combo_right : ∀ (x : Fin dA → ℝ) (y y\' : Fin dB → ℝ) (a b : ℝ), a + b = 1 →' in CI
    and 'prodEff_apply : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (x : Fin dA → ℝ)' in CI, 'source')
chk('S0.pre', 'landed PreComposite fields: Omega, convex, prod_mem, prodEff_effect (all IsEffectOn effects), '
    'prodEff_unit', all(s in CI for s in (
        'prod_mem : ∀ x ∈ ΩA, ∀ y ∈ ΩB, prodState x y ∈ Ω',
        'IsEffectOn ΩA e → IsEffectOn ΩB f → IsEffectOn Ω (prodEff e f)',
        'prodEff_unit : ∀ ω ∈ Ω, prodEff (unitEff dA) (unitEff dB) ω = 1')), 'source')
chk('S0.core', 'design KT4Core: tokA quantified over x in pairBody K01, y in pairBody K23 at stA x y, and tokB over '
    'pairBody K02 x pairBody K13 at stB x y (product states only)', all(s in FCORE for s in (
        'tokA : ∀ a b c d : Fin 4, ∀ x ∈ pairBody K01, ∀ y ∈ pairBody K23,',
        'effA (tabCoord a b) (tabCoord c d) (stA x y) = effB (tabCoord a c) (tabCoord b d) (stA x y)',
        'tokB : ∀ a b c d : Fin 4, ∀ x ∈ pairBody K02, ∀ y ∈ pairBody K13,',
        'effA (tabCoord a b) (tabCoord c d) (stB x y) = effB (tabCoord a c) (tabCoord b d) (stB x y)')), 'source')
chk('S0.tok', 'design TokenCoherent (KT4.tok) is quantified over the whole body PA.Omega', '∀ a b c d : Fin 4, ∀ ω ∈ PA.Ω,'
    in FCORE and 'PA.prodEff (tabCoord a b) (tabCoord c d) ω = PB.prodEff (tabCoord a c) (tabCoord b d) ω' in FCORE,
    'source')
chk('S0.toCore', 'design KT4.toCore: posBA from PB.prodEff_effect at PA.prod_mem via one_body; tokA from tok at '
    'PA.prod_mem', 'posBA e f he hf x hx y hy :=' in FBR and 'H.PB.prodEff_effect e f he hf _ (by rw [← H.one_body]; '
    'exact H.PA.prod_mem x hx y hy)' in FBR and 'tokA a b c d x hx y hy := H.tok a b c d _ (H.PA.prod_mem x hx y hy)'
    in FBR, 'source')

# ===============================================================================================================
section('S1  the regrouping sigma and the spanning sets')


def basis17(i, j):
    P = zeros17()
    P[i][j] = sp.Integer(1)
    return P


ok_inv = all(eq17(sigma(sigma(basis17(i, j))), basis17(i, j)) for i in R17 for j in R17)
chk('G1', 'sigma is an involution of Q^{17x17} (on all 289 basis arrays)', ok_inv, 'enumerate')
Zs = {k: sp.Symbol('z%d%d%d%d' % k, real=True) for k in product(R4, repeat=4)}
chk('G2', 'sigma iota = iota R and pi iota = id (symbolic 4-token table)', eq17(sigma(iota(Zs)), iota(Rg(Zs)))
    and all(ex(pi_(iota(Zs))[k] - Zs[k]) == 0 for k in Zs), 'identity')
hS = sp.Matrix([homv(s) for s in S_states])
chk('G3', 'hom e_x, hom e_y, hom e_z, hom -e_z are linearly independent (det != 0)', hS.det() != 0, 'witness',
    f'det {hS.det()}')
TPmat = sp.Matrix([tp(s, t) for s in S_states for t in S_states])
chk('G4', 'the 16 flat token products tp s t (s, t in S) are linearly independent in Q^16 and all have coordinate '
    '(0,0) equal to 1', TPmat.rank() == 16 and all(r[0] == 1 for r in TPmat.tolist()), 'witness')
note('G.W', 'by G4 the token products affinely span the hyperplane {v : v_(0,0) = 1}, which contains every pairBody. '
     'A bi-affine map on Q^16 x Q^16 (affine in each argument for every a + b = 1, as the landed combo laws state) is '
     'determined on that hyperplane by its values on the 16 x 16 token-product pairs.')
chk('G4c', 'countercontrol: the 9 token products tp s t with s, t in {e_x, e_y, e_z} do not span (rank < 16)',
    sp.Matrix([tp(s, t) for s in S_states[:3] for t in S_states[:3]]).rank() < 16, 'countercontrol')

# ===============================================================================================================
section('S2  ProductData laws of every model')

for name, M in MODELS.items():
    chk(f'P.{name}', f'{name}: evaluation laws N_A(stA x y) = hat x hat y^T and N_B(stB l l\') = hat l hat l\'^T for all '
        'chart points (symbolic), and both product maps bi-affine (degree <= 1 in each argument)',
        eval_law(M) and biaffine(M), 'identity')

# ===============================================================================================================
section('S3  regrouping invariance and the token clauses, model by model')

CLAIMS = {
    # name: (TPS, IP1_BA, IP1_AB, tokA, tokB)
    'MSIG': (True, True, True, True, True),
    'PAD': (True, True, True, True, True),
    'ANC': (False, False, False, False, False),
    'MTW': (False, False, False, False, False),
    'MTH': (False, False, False, False, False),
    'MRHO': (False, False, False, False, False),
    'MT': (False, False, False, False, False),
    'HBA': (False, True, False, False, True),
    'HAB': (False, False, True, True, False),
}
results = {}
for name, M in MODELS.items():
    r_tps, d_tps = tps(M)
    r_ba, d_ba = ip1_check(M, 'BA')
    r_ab, d_ab = ip1_check(M, 'AB')
    r_ta, d_ta = tok_check(M, 'A')
    r_tb, d_tb = tok_check(M, 'B')
    got = (r_tps, r_ba, r_ab, r_ta, r_tb)
    results[name] = got
    lab = lambda b: 'holds' if b else 'fails'
    detail = '; '.join(f'{k} {lab(v)}' + (f' ({d})' if d else '') for k, v, d in zip(
        ('TPS', 'IP1_BA', 'IP1_AB', 'tokA', 'tokB'), got, (d_tps, d_ba, d_ab, d_ta, d_tb)))
    chk(f'M.{name}', f'{name}: (TPS, IP1_BA, IP1_AB, tokA, tokB) = {tuple(lab(b) for b in CLAIMS[name])}',
        got == CLAIMS[name], 'identity' if all(CLAIMS[name]) else 'witness', detail)

chk('M.route', 'in every model in which TPS holds, tokA and tokB hold; in every model in which IP1_BA (IP1_AB) holds, '
    'tokB (tokA) holds', all((not g[0]) or (g[3] and g[4]) for g in results.values())
    and all(((not g[1]) or g[4]) and ((not g[2]) or g[3]) for g in results.values()), 'enumerate')
twist_tokens = {}
for name in ('MTW', 'MTH'):
    M = MODELS[name]
    twist_tokens[name] = (ip1(M, 'BA', tok), ip1(M, 'AB', tok))
chk('M.tw3', 'MTW and MTH: first-order token identity fails at token 3 only, in both directions (symbolic)',
    all(v == ([3], [3]) for v in twist_tokens.values()), 'witness', f'{twist_tokens}')

# ===============================================================================================================
section('S4  what the premises do not force: local tomography and body-level token coherence (PAD)')

Mp = MODELS['PAD']
vstar = (iota(Htab(*xstar)), sp.Integer(1))
pa_star = pA(Mp, xstar)
pa_prime = pA(Mp, xprime)
TAv, TBv = TA(Mp['NA'](vstar)), TB(Mp['NB'](vstar))
chk('L1', 'PAD: at the extra body point v* = (iota H(x*), 1), A reads H(x*) and B reads H(x\') (x* = (e_z,e_z,e_z,e_z), '
    'x\' = (-e_z,e_z,e_z,e_z)); so the readouts differ there: TokenCoherent and single-token marginal coherence fail at '
    'token 0', all(ex(TAv[k] - Htab(*xstar)[k]) == 0 and ex(TBv[k] - Htab(*xprime)[k]) == 0 for k in TAv)
    and ex(marg(TAv, 0, 3) - marg(TBv, 0, 3)) != 0, 'witness')
chk('L2', 'PAD: LT(PA) fails (v* and p_A(x*) are distinct with equal N_A) and LT(PB) fails (v* and p_A(x\') = p_B(x\') '
    'are distinct with equal N_B)', (not veq(vstar, pa_star)) and eq17(Mp['NA'](vstar), Mp['NA'](pa_star))
    and (not veq(vstar, pa_prime)) and eq17(Mp['NB'](vstar), Mp['NB'](pa_prime)) and veq(pa_prime, pB(Mp, xprime)),
    'witness')
chk('L2c', 'countercontrol: MSIG separates the same two points (N_A differs between iota H(x*) and iota H(x\'))',
    not eq17(MODELS['MSIG']['NA']((iota(Htab(*xstar)),)), MODELS['MSIG']['NA']((iota(Htab(*xprime)),))),
    'countercontrol')
note('L.W', 'PAD (uniform Q3): body Omega = conv(A products, B products, v*). Every readout of a body point is a '
     'readout of a valid state (products as in MSIG; at v*: A sees H(x*), B sees H(x\')), so prodEff_effect, '
     'prodEff_unit and one body hold; TPS, tokA, tokB hold (S3) and FCC holds (uniform Q3). PAD satisfies the route\'s '
     'premises with neither local tomography of either grouping nor TokenCoherent on the body.')

# ===============================================================================================================
section('S5  cross values: positivity rests on the cones, not on the maps')


def tabEff_hat(E):
    return [sp.Integer(0)] + flat_table(E)


def prodEff_val(N, v, ehat, fhat):
    return ex(sum(ehat[i] * N(v)[i][j] * fhat[j] for i in R17 for j in R17))


phiW = sp.diag(1, 1, -1, 1)
Lp = sp.diag(1, -1, 1, -1)
Ms_ = MODELS['MSIG']
vA = Ms_['stA'](flat_table(phiW), flat_table(phiW))
cv = prodEff_val(Ms_['NB'], vA, tabEff_hat(phiW / 4), tabEff_hat(Lp / 4))
chk('X1', 'SEPH (the MSIG maps on (Q3, Q3, Q3, twin)): B\'s product effect of the dual tables phiW/4 (dualW Q3) and '
    'L\'/4 (dualW twin) at A\'s product of phiW, phiW is -1/8: A\'s products are not in a body on which B\'s product '
    'effects are effects, so one body fails', cv == Q(-1, 8), 'witness', f'value {cv}')
Ma = MODELS['ANC']
cva = prodEff_val(Ma['NB'], Ma['stA'](flat_table(phiW), flat_table(phiW)), tabEff_hat(phiW / 4), tabEff_hat(Lp / 4))
chk('X2', 'ANC: the same cross value is the anchor value e(anchor) f(anchor) = 1/16 >= 0 (one body is vacuous there)',
    cva == Q(1, 16), 'witness', f'value {cva}')
gh = [sp.symbols(f'g{t}_0:4', real=True) for t in range(4)]


def t_eff(g, h):
    return [sp.Integer(0)] + [g[a] * h[b] for a in R4 for b in R4]


cvr = prodEff_val(Ms_['NB'], Ms_['stA'](Xn, Yn), t_eff(gh[0], gh[2]), t_eff(gh[1], gh[3]))
Xt = sp.Matrix(4, 4, lambda a, b: Xn[4 * a + b])
Yt = sp.Matrix(4, 4, lambda a, b: Yn[4 * a + b])
fac = (sp.Matrix(gh[0]).T * Xt * sp.Matrix(gh[1]))[0, 0] * (sp.Matrix(gh[2]).T * Yt * sp.Matrix(gh[3]))[0, 0]
chk('X3', 'restricted effects: B\'s product of token-product effects t(g0,g2) x t(g1,g3) at A\'s product of normalized '
    'x, y equals (g0^T X g1)(g2^T Y g3), symbolic', ex(cvr - fac) == 0, 'identity')
note('X.W', 'by X3 each factor pairs Lorentz vectors through a maxCone table, so it is >= 0 for every admissible cone: '
     'a version of the composite structure whose effect quantifier ranges only over products of token effects, with '
     'one body and TPS (the MSIG maps with Omega = conv(A products u B products)), holds on (Q3, Q3, Q3, twin), where '
     'FCC fails. The full COMP-1 quantifier (all IsEffectOn effects of each pair body, entangled ones included) is what '
     'carries the entangled positivity.')
note('X.B', 'body-level claims of the models (written, from c1 and the landed probe): MSIG on uniform Q3, HBA on '
     '(Q3, Q3, K_c, K_c) (A\'s readout of B\'s products is the famII form, which holds there since K_c lies in Q3), HAB '
     'on (K_c, K_c, Q3, Q3) (famI form), MTW and MTH on (Q3, Q3, Q3, twin) (B\'s readout composes with rho or theta, '
     'which maps twin onto Q3 at the level of the pair-13 slot), ANC on every quadruple, and PAD on uniform Q3 each '
     'have cross values in [0, 1] on their bodies (lower bound from the cone fact, upper bound from the complement '
     'identity), so with Omega the convex hull of their product states (and v* for PAD) both groupings are COMP-1 '
     'pre-composites with one body. FCC fails for HBA (c1 K7), HAB (c1 K8), MTW, MTH, ANC (c1 W2, W3); it holds for '
     'MSIG and PAD.')

# ===============================================================================================================
print()
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'witness', 'enumerate', 'source', 'countercontrol')), flush=True)
failed = [c[0] for c in CHECKS if not c[2]]
if failed:
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks; failed: {', '.join(failed)}", flush=True)
    print('VERDICT NOT RENDERED', flush=True)
    sys.exit(1)
print(f'{len(CHECKS)}/{len(CHECKS)} checks', flush=True)
print('VERDICT C2-CARRIER-MODELS-EXACT', flush=True)
