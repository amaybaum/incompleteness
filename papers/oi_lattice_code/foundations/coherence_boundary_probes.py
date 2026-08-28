#!/usr/bin/env python3
# coherence_boundary_probes.py — b441 (2026-08-28)
#
# The observer-coherence boundary: OI fixes the classical operational quotient, but not the
# coherent fibre over it.
#
# b440 showed the native (S, phi, mu_H, {I_a}) cannot supply the observer states H-observer-bundle
# needs. This file asks the classification question that replaces the construction hunt: how little
# extra structure suffices, and what does the extension cost? "Minimal" is taken CONSERVATIVELY --
# the native classical state and readout, and every existing comb probability, must be preserved
# EXACTLY -- and the question is what is first capable of continuous U(1) projective curvature.
#
# THE HIERARCHY.
#   CB1  NORMALIZER NO-GO. Let D be the diagonal algebra in the native basis. Permutations lie in
#        its unitary normalizer, and the normalizer is exactly the MONOMIAL group U = D_phase P --
#        the standard characterization, CITED here and not certified by the check, which exhibits
#        non-monomial unitaries outside it as a countercontrol but proves no converse.
#        Enlarging the native operations from permutations to the whole monomial group buys
#        NOTHING: a monomial unitary sends a basis vector to a PHASE TIMES a basis vector, i.e. to
#        the same RAY, and a Bargmann invariant sees only rays. Support stays 1, invariants stay 0
#        or positive real.
#   CB2  REAL MIXING IS NECESSARY BUT NOT SUFFICIENT. A real 2x2 mixer does create support-two
#        states, so support > 1 is genuinely necessary. But if the reachable ray geometry stays
#        REAL, every Bargmann product is real and the holonomy is confined to {0, pi} -- a Z_2 sign
#        structure, a real line bundle, NOT a continuously variable U(1)_Y connection.
#   CB3  COMPLEX RANK TWO IS SUFFICIENT, AND RANK ONE IS NOT. With a C^2 fibre the witness family
#        (1,0), (1,1), (1, t i) has Bargmann invariant 1 + t i as an IDENTITY IN t -- carried as
#        polynomials in t over the Gaussian rationals, so the continuity of arctan(t) is algebra
#        rather than sampling. A rank-one fibre contributes only a global phase, which cancels in
#        the ray.
#   CB4  THE CONSERVATIVE EXTENSION, and the identity that makes it conservative. Take
#        H~ = l^2(S) (x) C^2, lift every native operation as P~ = P (x) I, and forget by
#        F = Tr_{C^2}. Then F(P~ rho P~^dag) = P F(rho) P^dag EXACTLY -- checked on the actual
#        native permutations, not on a generic one, and after verifying that phi and both
#        instruments really are BIJECTIONS, which is what entitles the reading as permutations.
#   CB5  THE SURVIVAL LEDGER, which is the point of the round. The comb probabilities come back
#        exactly after F; the fixed-basis theory is an exact RETRACT (F o (. (x) |0><0|) = id); AND
#        the enlarged theory carries observables the old instrument algebra cannot see -- two lifted
#        states with identical F and different fibre expectation. So the original
#        S <=> D <=> Q_fb equivalence is preserved as a QUOTIENT, and must NOT be read as covering
#        the enlarged coherent theory.
#   CB5b THE STATE-DEPENDENT LIFT, which is what the availability claim actually needs. A CONSTANT
#        fibre -- the same ray at every state -- cannot carry curvature: P~ = P (x) I leaves it
#        untouched and the loop product is a positive real, which is b439's GS17 exactly. So CB5b
#        builds a lift whose ray VARIES with the native state, shows it reproduces the comb and
#        retracts just as the constant one does, and exhibits a NONZERO Bargmann phase. The witness
#        is a WORD THE DYNAMICS TRAVERSES -- s, I_0 s, phi I_0 s, distinct, in ONE sector, with the
#        phi step taken in the constructed branch rather than the bijection padding -- and NOT three
#        states drawn from sectors the dynamics keeps disjoint, whose rays would again be an
#        arbitrary assignment on configuration space. The ray assignment therefore has to depend on
#        what the native operations MOVE, not only on the sector label they preserve.
#
# THE BOUNDARY STATEMENT (CB6). OI fixes the classical operational quotient and leaves the coherent
# fibre over it UNDERDETERMINED. b440 showed the canonical fibre is trivial; this file shows how
# little is needed to make it nontrivial, and that everything already proved survives the forgetting.
# H-observer-bundle becomes AVAILABLE-IN-THE-CLASS -- the conservative extension class CONTAINS a
# curved configuration (CB5b) -- and is still NOT DERIVED, because the assignment is imposed by hand
# and nothing in OI selects it. The curvature is also OPERATIONAL, not SPATIAL: the construction has
# two visible values and no neighbour relation, so the plaquette a hypercharge curvature lives on
# cannot be exhibited in it at all, and CB5b records that as a computed fact rather than a caveat.
# H-Y-vertex is untouched and remains separate. CB6 and the scope block are GATED on CB1-CB5b: an
# unconditional verdict would print PASS beside red controls.
#
# ARITHMETIC. Exact throughout: Gaussian rationals for the ray geometry, Fractions for the states.
# The lifted state is carried as a block form rho = sum_s |s><s| (x) M_s with M_s a 2x2 Gaussian
# rational matrix -- which is what a permutation dynamics preserves -- so the whole ledger is exact
# without ever building a matrix of size 2|S|.
#
# Self-contained by this directory's convention: none of its probes imports another, which is what
# lets each be run alone from an archived copy. The native construction is rebuilt by b76B's recipe.
import itertools
import sys
from fractions import Fraction as F

CHECKS = []

def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)

# ---------------------------------------------------------------- Gaussian rationals
def gadd(x, y): return (x[0] + y[0], x[1] + y[1])
def gsub(x, y): return (x[0] - y[0], x[1] - y[1])
def gmul(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def gconj(x):   return (x[0], -x[1])
GZ, GO = (F(0), F(0)), (F(1), F(0))

def inner(u, v):
    tot = GZ
    for a, b in zip(u, v):
        tot = gadd(tot, gmul(gconj(a), b))
    return tot

def bargmann(u, v, w):
    return gmul(gmul(inner(u, v), inner(v, w)), inner(w, u))

def is_real_nonneg(z): return z[1] == 0 and z[0] >= 0
def support(v):        return sum(1 for c in v if c != GZ)

# ---------------------------------------------------------------- CB1  the normalizer no-go
print("CB1  monomial unitaries — the whole normalizer of the diagonal algebra — buy nothing")
n = 4
PERM = [1, 2, 3, 0]
PHASES = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(0), F(1)), (F(-1), F(0))]
def monomial_image(i):
    """U = D P applied to the basis vector e_i: a PHASE times a basis vector."""
    v = [GZ] * n
    v[PERM[i]] = PHASES[PERM[i]]
    return v
imgs = [monomial_image(i) for i in range(n)]
ok1 = all(support(v) == 1 for v in imgs)
# each phase is a unit, so the image is a unit vector on a coordinate axis: the SAME ray as a basis
ok1 &= all(inner(v, v) == GO for v in imgs)
# every Bargmann invariant among monomial images is 0 (distinct rays) or positive real (same ray)
vals, ntriples = set(), 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            vals.add(bargmann(imgs[a], imgs[b], imgs[c])); ntriples += 1
ok1 &= all(is_real_nonneg(z) for z in vals)
# countercontrol: a NON-monomial unitary does not normalize the diagonal algebra. A real rotation
# conjugates diag(1,0) to a matrix with nonzero off-diagonal entries.
# Several structurally different non-monomial unitaries, each conjugating diag(1,0) off the
# diagonal. This is a countercontrol on the tested matrices; it is NOT a proof that every
# non-monomial unitary fails to normalize, and the verdict below does not claim one.
NONMONO = ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17)))
offs = [c_ * s_ for c_, s_ in NONMONO]        # the (0,1) entry of R diag(1,0) R^T in each case
ok1 &= all(o != 0 for o in offs)
check("CB1", ok1,
      f"a monomial unitary U = D P sends every basis vector to a unit multiple of a basis vector — "
      f"support {sorted({support(v) for v in imgs})}, the SAME ray — so every Bargmann invariant "
      f"among the images lies in {{0, positive real}} — {ntriples} triples, taking only the "
      f"{len(vals)} distinct values {sorted(vals)}. The monomial "
      f"group is CONTAINED in the normalizer of the diagonal algebra, and {len(NONMONO)} "
      f"non-monomial rotations are exhibited outside it (each moves diag(1,0) off the diagonal, by "
      f"{offs}). That the normalizer is EXACTLY the monomial group is the standard characterization "
      "— for a diagonal with distinct entries, conjugation preserving diagonality permutes its "
      "eigenlines, which are the coordinate axes — and it is cited here, not certified by this "
      "check. What the check establishes is the part it computes: monomial images stay on one ray, "
      "so b440's no-go survives the enlargement from permutations to monomials")

# ---------------------------------------------------------------- CB2  real is not enough
print("CB2  real mixing makes support two — necessary, but it only ever gives a Z_2 sign")
r0 = ((F(1), F(0)), (F(0), F(0)))
r1 = ((F(1), F(0)), (F(2), F(0)))
r2 = ((F(1), F(0)), (F(-1), F(0)))
Br = bargmann(r0, r1, r2)
ok2 = (support(r1) == 2)                                   # real mixers DO create support two
ok2 &= (Br[1] == 0 and Br[0] < 0)                          # ... and give a nontrivial SIGN
# but never anything else: any triple of REAL vectors has a real invariant
reals = [((F(a), F(0)), (F(b), F(0))) for a in (1, 2) for b in (-1, 0, 1, 3)]
ok2 &= all(bargmann(u, v, w)[1] == 0 for u in reals for v in reals for w in reals)
check("CB2", ok2,
      f"a real mixer reaches support two, so support > 1 is genuinely NECESSARY — but the invariant "
      f"of the real triple (1,0), (1,2), (1,-1) is {Br[0]}, real and negative: argument pi. Every "
      f"triple drawn from {len(reals)} real vectors has a real invariant, so the holonomy of a real "
      "ray geometry is confined to {0, pi}. That is a Z_2 sign structure — a real line bundle — and "
      "NOT the continuously variable U(1) a hypercharge connection needs. Support > 1 is necessary "
      "and not sufficient")

# ---------------------------------------------------------------- CB3  complex rank two suffices
print("CB3  a complex rank-two fibre gives a continuously variable phase; rank one gives nothing")
# Four samples cannot certify that the argument VARIES CONTINUOUSLY. Do it as an identity in t:
# carry each number as a POLYNOMIAL in t with Gaussian-rational coefficients and verify the
# invariant is exactly 1 + t i, with every higher coefficient zero. Continuity of arctan then makes
# the continuous statement algebra rather than sampling.
def padd(a, b):
    n = max(len(a), len(b))
    return [gadd(a[i] if i < len(a) else GZ, b[i] if i < len(b) else GZ) for i in range(n)]
def pmul(a, b):
    out = [GZ] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = gadd(out[i + j], gmul(x, y))
    return out
def pconj(a): return [gconj(x) for x in a]
def pinner(u, v):
    tot = [GZ]
    for a, b in zip(u, v):
        tot = padd(tot, pmul(pconj(a), b))
    return tot
def ptrim(a):
    while len(a) > 1 and a[-1] == GZ:
        a = a[:-1]
    return a
ONE_P, ZERO_P, T_I = [GO], [GZ], [GZ, (F(0), F(1))]      # 1, 0, and t*i as polynomials in t
P0 = (ONE_P, ZERO_P)
P1 = (ONE_P, ONE_P)
P2 = (ONE_P, T_I)                                        # (1, t i), t a free real parameter
Bpoly = ptrim(pmul(pmul(pinner(P0, P1), pinner(P1, P2)), pinner(P2, P0)))
ok3 = (Bpoly == [GO, (F(0), F(1))])                      # exactly 1 + t i, identically in t
# the four samples are kept as a spot check of the identity, not as the evidence for it
args = []
for t in (1, 2, 3, 5):
    q2 = ((F(1), F(0)), (F(0), F(t)))
    B = bargmann(((F(1), F(0)), (F(0), F(0))), ((F(1), F(0)), (F(1), F(0))), q2)
    args.append(B)
    ok3 &= (B == (F(1), F(t)))
# rank one: the fibre contributes a global phase, which cancels in the ray — the invariant of three
# multiples of one vector is a positive real whatever the phases
u = ((F(1), F(0)), (F(2), F(0)))
scaled = [tuple(gmul(ph, c) for c in u) for ph in PHASES[:3]]
ok3 &= is_real_nonneg(bargmann(*scaled))
check("CB3", ok3,
      "the witness family (1,0), (1,1), (1, t i) has Bargmann invariant EXACTLY 1 + t i as an "
      "IDENTITY IN t — verified by carrying the whole computation as polynomials in t over the "
      "Gaussian rationals, with every coefficient above the linear one zero — so its argument is "
      "arctan(t), which is continuous and sweeps (-pi/2, pi/2). That is a parameterized algebraic "
      f"statement, not four samples; the samples {[f'{B[0]}+{B[1]}i' for B in args]} are kept only "
      "as a spot check of the identity. A rank-one fibre supplies only a global phase: three phase "
      "multiples of one vector give a positive real invariant, because the phases cancel in the "
      "ray. So complex rank two is the smallest fibre rank that can carry a phase at all")

# ---------------------------------------------------------------- the native construction (b76B)
nV, nA, BLANK, K = 2, 2, -1, 1
def kern(ctx):
    xs, as_ = ctx
    p = F((1 + sum(xs) + 2 * sum(as_) + 3 * len(xs) + (xs[-1] ^ as_[-1])) % 7 + 1, 9)
    return {0: 1 - p, 1: p}
CTXS = [((x,), (a,)) for x in range(nV) for a in range(nA)]
tabs = [{}]
for c in CTXS:
    nxt = []
    for tb in tabs:
        for y in range(nV):
            if kern(c)[y] > 0:
                t2 = dict(tb); t2[c] = y; nxt.append(t2)
    tabs = nxt
UTAB = [tuple(sorted(tb.items())) for tb in tabs]
MU = {}
for ui, tb in enumerate(UTAB):
    w = F(1)
    for c, y in tb:
        w *= kern(c)[y]
    MU[ui] = w
XH = list(itertools.product(list(range(nV)) + [BLANK], repeat=K))
AH = list(itertools.product(list(range(nA)) + [BLANK], repeat=K))
STATES = [(x, h, a, u, c) for x in range(nV) for h in XH for a in AH
          for u in range(len(UTAB)) for c in range(K + 1)]
def wf_x(h, c): return all(h[i] != BLANK for i in range(c)) and all(h[i] == BLANK for i in range(c, K))
def wf_a(a, c, wrote):
    m = c + (1 if wrote else 0)
    return all(a[i] != BLANK for i in range(m)) and all(a[i] == BLANK for i in range(m, K))
def instrument(act):
    d = {}
    for s in STATES:
        x, h, a, u, c = s
        if c < K:
            al = list(a)
            if al[c] == BLANK: al[c] = act
            elif al[c] == act: al[c] = BLANK
            d[s] = (x, h, tuple(al), u, c)
        else:
            d[s] = s
    return d
INSTR = {act: instrument(act) for act in range(nA)}
PHI = {}
for s in STATES:
    x, h, a, u, c = s
    if c < K and wf_x(h, c) and wf_a(a, c, wrote=True):
        ctx = (tuple(list(h[:c]) + [x]), tuple(a[:c + 1]))
        PHI[s] = (dict(UTAB[u])[ctx], tuple(list(h[:c]) + [x] + [BLANK] * (K - c - 1)), a, u, c + 1)
_und = sorted(set(STATES) - set(PHI)); _unh = sorted(set(STATES) - set(PHI.values()))
# zip() truncates silently if the two complements differ in size, which would leave PHI a
# non-bijection while every downstream comparison still passed on the tested support. Check the
# sizes, then check bijectivity outright: CB4 reads these maps as permutation matrices and is
# entitled to nothing until that is established.
assert len(_und) == len(_unh), (len(_und), len(_unh))
for _a, _b in zip(_und, _unh):
    PHI[_a] = _b
NATIVE_ARE_BIJECTIONS = (sorted(PHI.values()) == sorted(STATES)
                         and all(sorted(m.values()) == sorted(STATES) for m in INSTR.values()))

# A lifted state is rho = sum_s |s><s| (x) M_s, with M_s a 2x2 Gaussian-rational block. Permutation
# dynamics preserves that form, so the ledger below is exact without ever forming a 2|S| matrix.
RAYS = (((F(1), F(0)), (F(0), F(0))),        # |0>
        ((F(1), F(0)), (F(1), F(0))),        # (|0> + |1>)/sqrt2
        ((F(1), F(0)), (F(0), F(1))),        # (|0> + i|1>)/sqrt2
        ((F(1), F(0)), (F(2), F(0))))
def ray_block(psi, w):
    """w * |psi><psi| / <psi|psi>: exact, since <psi|psi> is a positive RATIONAL for Gaussian psi."""
    nrm = inner(psi, psi)
    assert nrm[1] == 0 and nrm[0] > 0
    return tuple(tuple(gmul((w / nrm[0], F(0)), gmul(psi[i], gconj(psi[j]))) for j in range(2))
                 for i in range(2))

def lift(p, fibre):
    """Constant fibre: one state at every site. Retained because CB4/CB5 must hold for it too."""
    return {s: tuple(tuple(gmul((w, F(0)), fibre[i][j]) for j in range(2)) for i in range(2))
            for s, w in p.items()}

def lift_varying(p, assign):
    """SITE-DEPENDENT fibre: a different ray per state. This is the lift that can carry curvature,
    and the one the availability claim needs -- a constant fibre is exactly b439's GS17, zero."""
    return {s: ray_block(RAYS[assign(s)], w) for s, w in p.items()}
def forget(rho):
    return {s: gadd(M[0][0], M[1][1])[0] for s, M in rho.items()}     # Tr over the fibre
def push_lift(rho, perm):
    out = {}
    for s, M in rho.items():
        t = perm[s]
        out[t] = M if t not in out else tuple(tuple(gadd(out[t][i][j], M[i][j]) for j in range(2))
                                              for i in range(2))
    return out
def push_classical(p, perm):
    out = {}
    for s, w in p.items():
        out[perm[s]] = out.get(perm[s], F(0)) + w
    return out

INIT = {(x, (BLANK,) * K, (BLANK,) * K, u, 0): MU[u] / nV
        for x in range(nV) for u in range(len(UTAB))}
KET0 = ((GO, GZ), (GZ, GZ))                                   # |0><0| on the fibre
PLUS = ((F(1, 2), F(0)), (F(1, 2), F(0))), ((F(1, 2), F(0)), (F(1, 2), F(0)))
YPLUS = (((F(1, 2), F(0)), (F(0), F(-1, 2))), ((F(0), F(1, 2)), (F(1, 2), F(0))))

# ---------------------------------------------------------------- CB4  the intertwining identity
print("CB4  the extension is conservative: F(P~ rho P~^dag) = P F(rho) P^dag on the native ops")
ok4 = NATIVE_ARE_BIJECTIONS          # CB4 reads these as permutation matrices; establish that first
def ASSIGN(st):
    """A ray per native state. It must depend on the parts of the state the NATIVE OPERATIONS
    MOVE -- the action register and the step counter, not only the sector label u, which the
    instruments and the constructed branch of phi both preserve. An assignment constant along a
    native word attaches the same ray at every step of it and can carry no phase."""
    x, h, a, u, c = st
    aw = 0 if a[0] == BLANK else a[0] + 1
    return (x + u + c + aw) % len(RAYS)
for rho in ([lift(INIT, f) for f in (KET0, PLUS, YPLUS)] + [lift_varying(INIT, ASSIGN)]):
    for perm, name in ((PHI, 'phi'), (INSTR[0], 'I_0'), (INSTR[1], 'I_1')):
        lhs = forget(push_lift(rho, perm))
        rhs = push_classical(forget(rho), perm)
        ok4 &= (lhs == rhs)
    # and for a composite word, which is what an actual protocol applies
    lhs = forget(push_lift(push_lift(rho, INSTR[1]), PHI))
    rhs = push_classical(push_classical(forget(rho), INSTR[1]), PHI)
    ok4 &= (lhs == rhs)
check("CB4", ok4,
      "phi and both instruments are verified BIJECTIONS first, so reading them as permutation "
      "matrices is earned rather than assumed. Then with H~ = l^2(S) (x) C^2, P~ = P (x) I and "
      "F = Tr_{C^2}, forgetting commutes with the dynamics EXACTLY — on the actual operations phi, "
      "I_0, I_1 and on the composite word I_1 then phi, at three constant fibre states AND at a "
      "STATE-DEPENDENT one. The identity holds because a permutation relabels the blocks and the "
      "fibre trace is taken blockwise, so it is blind to which ray sits where; nothing about the "
      "fibre can leak into the classical marginal")

# ---------------------------------------------------------------- CB5  the survival ledger
print("CB5  the ledger: comb probabilities survive, Q_fb is a retract, and something new appears")
# (a) the comb probability P(x_1 | a_0) is reproduced exactly through the lift
def comb_from(p_or_rho, act, lifted):
    st = p_or_rho
    for perm in (INSTR[act], PHI):
        st = push_lift(st, perm) if lifted else push_classical(st, perm)
    cl = forget(st) if lifted else st
    out = [F(0)] * nV
    for s, w in cl.items():
        out[s[0]] += w
    return out
ok5 = True
for act in range(nA):
    native = comb_from(INIT, act, False)
    for fibre in (KET0, PLUS, YPLUS):
        ok5 &= (comb_from(lift(INIT, fibre), act, True) == native)
combs = [comb_from(INIT, a, False) for a in range(nA)]
ok5 &= (combs[0] != combs[1])                       # the comb is non-degenerate, so this has content
# (b) Q_fb is an exact RETRACT: forget after embedding is the identity
ok5 &= (forget(lift(INIT, KET0)) == INIT)
# (c) but the enlarged theory sees more: two lifted states with the SAME F and different fibre
rA, rB = lift(INIT, PLUS), lift(INIT, YPLUS)
same_classical = (forget(rA) == forget(rB))
sy = ((GZ, (F(0), F(-1))), ((F(0), F(1)), GZ))      # sigma_y on the fibre
def fibre_expect(rho):
    tot = GZ
    for M in rho.values():
        for i in range(2):
            for j in range(2):
                tot = gadd(tot, gmul(M[i][j], sy[j][i]))
    return tot
eA, eB = fibre_expect(rA), fibre_expect(rB)
ok5 &= same_classical and (eA != eB)
check("CB5", ok5,
      f"(a) the comb P(x_1 | a_0) comes back EXACTLY through the lift, at every fibre state and both "
      f"actions, and the two combs differ ({combs[0][0]} vs {combs[1][0]} on x=0) so the check has "
      f"content. (b) the fixed-basis theory is an exact RETRACT: forgetting after embedding with "
      f"|0><0| is the identity. (c) but two lifted states with IDENTICAL classical marginals give "
      f"different fibre expectations ({eA[0]}+{eA[1]}i vs {eB[0]}+{eB[1]}i) — so the enlarged theory "
      "carries observables the old instrument algebra cannot see. S <=> D <=> Q_fb survives as a "
      "QUOTIENT and must not be read as covering the extension")

# -------------------------------------- CB5b  the varying lift, along a word the dynamics traverses
print("CB5b a STATE-DEPENDENT fibre preserves everything AND is curved ALONG A NATIVE WORD")
# The constant fibre of CB4/CB5 cannot carry curvature: a state-independent ray gives a real
# positive loop product, which is exactly b439's GS17. So the claim needs a lift whose ray VARIES,
# and that lift has to be shown conservative in its own right.
#
# It also has to be curved over states the theory can actually VISIT. Three states drawn from
# three different sectors u -- which both instruments and the constructed branch of phi preserve --
# are mutually inaccessible, and a Bargmann product among their rays is a statement about an
# arbitrary assignment on configuration space, not a holonomy of anything the dynamics traverses.
# So the witness here is a WORD in the native generators: s, then I_0 applied to it, then phi.
ok5b = NATIVE_ARE_BIJECTIONS
for act in range(nA):
    native = comb_from(INIT, act, False)
    ok5b &= (comb_from(lift_varying(INIT, ASSIGN), act, True) == native)
ok5b &= (forget(lift_varying(INIT, ASSIGN)) == INIT)          # the retract still holds
W0 = min(INIT)                                    # a state the initial law actually charges
W1 = INSTR[0][W0]                                 # ... write action 0
W2 = PHI[W1]                                      # ... then step the comb
WORD = (W0, W1, W2)
ok5b &= (len(set(WORD)) == 3)                     # three DISTINCT states, so the triangle is real
ok5b &= (len({s[3] for s in WORD}) == 1)          # all in ONE sector: connected, not disjoint
# W2 must come from the CONSTRUCTED branch of phi, not from the padding completion that only
# exists to make phi a bijection -- a step through the padding is not a step of the dynamics.
ok5b &= (W1[4] < K and wf_x(W1[1], W1[4]) and wf_a(W1[2], W1[4], wrote=True))
Bword = bargmann(*[RAYS[ASSIGN(s)] for s in WORD])
ok5b &= (Bword[1] != 0 or Bword[0] < 0)                        # a genuine phase, not 0 or positive
# What is NOT available here, stated as a computed fact rather than a caveat: the construction has
# nV visible values and no neighbour relation at all, so "three connected local SITES" -- the
# spatial plaquette a hypercharge curvature would live on -- does not exist to be exhibited.
NO_SPATIAL_PLAQUETTE = (len({s[0] for s in STATES}) < 3)
ok5b &= NO_SPATIAL_PLAQUETTE
check("CB5b", ok5b,
      f"the state-dependent lift reproduces the comb EXACTLY at both actions and still retracts "
      f"onto the fixed-basis theory, so it is conservative in exactly the sense CB4-CB5 established "
      f"for the constant one — the intertwining is blind to which ray sits where. And its rays are "
      f"curved along a WORD THE DYNAMICS TRAVERSES: the three distinct states s, I_0 s, phi I_0 s — "
      f"one sector throughout, with the phi step taken in the constructed branch and not in the "
      f"padding — carry Bargmann invariant {Bword[0]} + {Bword[1]}i, not a non-negative real. That "
      f"is what a constant fibre could never supply, b439's GS17 exactly. What it is NOT: the "
      f"construction has {len({s[0] for s in STATES})} visible values and NO neighbour relation, so "
      "three connected local SITES — the spatial plaquette a hypercharge curvature would live on — "
      "do not exist in it to be exhibited, and this witness is a loop in OPERATIONAL HISTORY rather "
      "than in space. The spatial statement stays inside H-observer-bundle, undischarged")

# ---------------------------------------------------------------- CB6  the boundary statement
print("CB6  the boundary, and what it does and does not settle")
# Gated on CB1-CB5b: an unconditional True would print PASS beside red controls and the
# scope block below would assert conclusions drawn from failed checks.
check("CB6", all(CHECKS),
      "OI fixes the classical operational quotient and leaves the coherent fibre over it "
      "UNDERDETERMINED. b440 showed the canonical fibre is trivial; CB1-CB3 show how little is "
      "needed to make it nontrivial — not merely support > 1, which only buys a Z_2 sign, but a "
      "COMPLEX rank-two fibre — and CB4-CB5 show everything already proved survives the forgetting. "
      "So the non-uniqueness of OI -> QM is not 'many arbitrary quantum completions': it is a "
      "classical core plus an underdetermined coherent fibre, with a rank and reality bound on what "
      "the fibre must be for hypercharge. WHAT IS EARNED, and only this: the conservative extension "
      "class CONTAINS a configuration that preserves the comb, the retract and the dynamics exactly "
      "and is curved along a word the dynamics actually traverses (CB5b) — kinematic capacity, "
      "demonstrated inside the construction rather than on free-floating vectors. WHAT IS NOT, in "
      "three separate respects: nothing here DERIVES the fibre, since the assignment is imposed by "
      "hand and nothing in OI selects it; the curvature exhibited is along an OPERATIONAL word, "
      "while the construction has no neighbour relation and only two visible values, so the SPATIAL "
      "plaquette a hypercharge curvature lives on cannot be exhibited in it at all; and nothing "
      "identifies that phase with the HYPERCHARGE channel, which is H-Y-vertex and is untouched. "
      "'Available' therefore means available-in-the-class, not derived and not local, and the "
      "readings must not be run together")

print()
if not all(CHECKS):
    print("     [scope] VERDICT WITHHELD: a control above failed, so the boundary statement below")
    print("     is not asserted. Fix the failing check before reading any conclusion from this run.")
else:
    print("     [scope] Settled: nothing in the normalizer of the diagonal algebra escapes b440's no-go;")
    print("     real mixing gives support two but only a Z_2 sign; a COMPLEX RANK-TWO fibre is the first")
    print("     sufficient class; the conservative extension H~ = l^2(S) (x) C^2 with P~ = P (x) I and")
    print("     F = Tr_{C^2} preserves the native dynamics, the comb probabilities and the fixed-basis")
    print("     theory exactly, as a retract; and it carries observables the old instrument algebra")
    print("     cannot see.")
    print("     Settled at b441a: a state-dependent fibre is curved along a word the dynamics")
    print("     traverses — s, I_0 s, phi I_0 s, one sector throughout — while still reproducing the")
    print("     comb and the retract exactly. Capacity is inside the construction, not beside it.")
    print("     NOT settled: the fibre is not DERIVED. H-observer-bundle is available in the extension")
    print("     class, not a consequence of OI. The curvature shown is OPERATIONAL, not SPATIAL: the")
    print("     construction has two visible values and no neighbour relation, so the plaquette a")
    print("     hypercharge curvature lives on cannot be exhibited in it. H-Y-vertex is untouched.")
    print("     And the enlarged theory is NOT covered by the old S <=> D <=> Q_fb equivalence —")
    print("     that survives as a quotient only.")
print()
print("coherence_boundary_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
