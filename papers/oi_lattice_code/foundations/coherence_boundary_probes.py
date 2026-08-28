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
# TWO SENSES OF CONSERVATIVE, used throughout and never interchangeably. OI-CONSERVATIVE is the
# definition just given: what OI actually supplies comes back exactly. STRONGLY CONSERVATIVE adds
# that the forgetting intertwines the dynamics on the ENTIRE coherent state space, coherences
# included -- data the enlarged theory has and OI never supplied, so it is an extra hypothesis and
# not a consequence. CB4-CB5 establish the first for P (x) I; CB5c shows a state-dependent rotation
# keeps the first and loses the second.
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
#   CB5b THE NATIVE TRANSPORT IS FLAT. P~ = P (x) I moves a block from s to P(s) without touching
#        it, so the fibre is INERT: no native operation rotates any ray anywhere on the support,
#        and along the word s, I_0 s, phi I_0 s the ray DELIVERED at the third state is the one
#        that started at the first, not the one the section names there. The dynamically realized
#        triple is one ray three times, whose invariant is a positive real. The word is not closed
#        either -- no native operation supplies the edge back to the start, which a three-point
#        Bargmann invariant inserts silently through its third overlap. SCOPE: this rules out
#        holonomy OF THE NATIVE TRANSPORT. It does NOT rule out a SECTION-INDUCED Bargmann/Berry
#        connection, which [SM §6.5] defines through overlaps and which needs no rotation by the
#        transport; that object is untouched here, because the construction supplies no local graph
#        to evaluate it on. Flat transport and no connection are different statements.
#   CB5c TWO CONDITIONS, kept apart. OI-CONSERVATIVE is this file's definition, used by CB4-CB5:
#        the native classical state, the readout and every comb probability OI supplies come back
#        exactly. STRONGLY CONSERVATIVE additionally demands the intertwining on the ENTIRE coherent
#        state space. Coherences are data the enlarged theory has and OI never supplied, so the
#        second is an extra hypothesis, not a consequence of the first. P~ = sum_s |P(s)><s| (x) U_s
#        is OI-CONSERVATIVE and fails only STRONG conservativity: a coherence carries
#        U_s rho_st U_t^dag, of trace Tr(U_t^dag U_s rho_st), equal to Tr(rho_st) for every rho_st
#        only when U_t^dag U_s = I. That forces state-independence, nothing about the common value,
#        and nothing about different native OPERATIONS carrying different global rotations.
#   CB5d THE OPERATION-DEPENDENT LIFT IS CONSERVATIVE, AND THE RELATIONS STILL KILL THE HOLONOMY.
#        Lift each operation o as P_o (x) U_o with a single global U_o: the same U sits on both
#        sides of every block, so the fibre trace is preserved on every coherence unconditionally,
#        and CB5c's obstruction does not apply. The native RELATIONS then bind it only
#        PROJECTIVELY: the fibre acts by conjugation, which is blind to an overall phase, so an
#        involution forces U^2 = scalar and NOT U^2 = I -- the quarter turn J with J^2 = -I is a
#        legitimate lift that the strict reading would wrongly exclude. Demanding strictness imposes
#        a non-projective representation as a hidden hypothesis, which begs the question when the
#        target structure is Bargmann geometry. NO HOLONOMY WITNESS IS CLAIMED HERE: for the ONE
#        TESTED WORD the holonomy is a scalar, trivial as a channel, and that scalar's value is
#        GAUGE -- J and iJ give the same channel with squares -I and +I -- so no Z_2 datum follows
#        from it either. An invariant would be the 2-cocycle class in H^2(G, U(1)), uncomputed. The
#        question is live -- words fixing the base state without being the identity map exist, some
#        using no phi -- and deciding it needs the PROJECTIVE representations (2-cocycles, Schur
#        multiplier) of the group the three native permutations generate, uncomputed here.
#
# THE BOUNDARY STATEMENT (CB6). OI fixes the classical operational quotient and leaves the coherent
# fibre over it UNDERDETERMINED. b440 showed the canonical fibre is trivial; this file shows how
# little is needed to make it nontrivial, and that everything already proved survives the forgetting.
#
# THIS IS AN EXISTENCE STATEMENT, NOT A CLASSIFICATION, and the file must not read as one. Nothing
# here shows that every quantum completion preserving the quotient has tensor-product-fibre form,
# so "a classical core plus a coherent fibre" describes how THIS witness is built and is not a
# theorem about the alternatives. b441 does not classify all possible quantum completions.
#
# H-OBSERVER-BUNDLE IS NOT MADE AVAILABLE BY ANY OF THIS. The condition as [SM §6.5] states it asks
# for a LOCAL observer-state bundle with nonzero projective curvature IN THE HYPERCHARGE CHANNEL.
# Three independent gaps stand between this file and it -- not DERIVED (nothing in OI selects a
# section), not LOCAL (two visible values, no neighbour relation, so the plaquette is absent), not
# IDENTIFIED with the hypercharge channel (H-Y-vertex, untouched). CB5b-CB5d map where the freedom
# can and cannot live: the native P (x) I transport is flat, a STATE-dependent rotation is not
# conservative on coherences, and an OPERATION-dependent one is conservative but is pinned by the
# native relations, which force the tested loop's holonomy to be trivial. NO HOLONOMY WITNESS IS
# CLAIMED IN THIS CONSTRUCTION. A section-induced Berry connection is a separate untested route.
#
# NOTHING HERE IS PROPAGATED TO THE MANUSCRIPT. These are round results pending acceptance; the
# scope block says so, and §A.25 propagation is a merge-time step, not something this file asserts.
#
# CB6 and the scope block are GATED on CB1-CB5b, and the gate withholds the MESSAGE as well as
# flipping the label: check() prints its text whatever the label says, so gating alone would render
# the whole verdict under a FAIL heading -- exactly what the gate exists to prevent.
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

def verdict(label, ok, msg):
    """A TERMINAL SUMMARY: it has no computation of its own, it only states what the checks above
    have established. Gating the label is not enough -- check() prints its msg whatever the label
    says, so a bare gate renders the entire verdict text under a FAIL heading, which is the thing
    the gate exists to prevent. The message itself is therefore withheld when a control has failed."""
    check(label, ok, msg if ok else
          "WITHHELD — a prerequisite control above failed, so this summary is not asserted")

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
      "ray. SCOPE, and it is narrow: this is a statement about BARGMANN PHASES OF RAY OVERLAPS "
      "inside ONE globally identified ambient space. It is NOT a lower bound on connection "
      "holonomy in general — a complex LINE bundle carries perfectly good non-flat U(1) "
      "connections, and a rank-one transport can accumulate holonomy while the fibre trace sees "
      "nothing. Rank two is the smallest fibre that carries an overlap phase between DISTINCT "
      "rays here, and nothing more than that is claimed")

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
    and the one the CAPACITY claim needs -- a constant fibre is exactly b439's GS17, zero."""
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
print("CB5b a varying section is NOT a connection — P (x) I is inert, so there is no curvature")
# The constant fibre of CB4/CB5 cannot carry curvature: a state-independent ray gives a real
# positive loop product, which is exactly b439's GS17. So the claim needs a lift whose ray VARIES,
# and that lift has to be shown conservative in its own right.
#
# But a VARYING SECTION IS NOT A CONNECTION, and this check now says so rather than trading on the
# confusion. P~ = P (x) I moves a block from s to P(s) and does not touch it, so the ray that starts
# at s is the ray that arrives at P(s) -- the fibre is INERT under the whole native algebra. A
# Bargmann product formed by reading ASSIGN at three states of a word is then a property of the
# hand-imposed section evaluated at three points, NOT a holonomy: the dynamics never realizes those
# three rays together. Two earlier versions of this check made exactly that substitution.
ok5b = NATIVE_ARE_BIJECTIONS
for act in range(nA):
    native = comb_from(INIT, act, False)
    ok5b &= (comb_from(lift_varying(INIT, ASSIGN), act, True) == native)
ok5b &= (forget(lift_varying(INIT, ASSIGN)) == INIT)          # the retract still holds
W0 = min(INIT)                                    # a state the initial law actually charges
W1 = INSTR[0][W0]                                 # ... write action 0
W2 = PHI[W1]                                      # ... then step the comb
WORD = (W0, W1, W2)
ok5b &= (len(set(WORD)) == 3 and len({s[3] for s in WORD}) == 1)
ok5b &= (W1[4] < K and wf_x(W1[1], W1[4]) and wf_a(W1[2], W1[4], wrote=True))
def ray_index(block):
    """Which RAY this block carries, whatever its weight. None if it is not a ray block."""
    tot = gadd(block[0][0], block[1][1])[0]
    for i, R in enumerate(RAYS):
        if tot != 0 and block == ray_block(R, tot):
            return i
    return None
RHO = lift_varying(INIT, ASSIGN)
DELIVERED = ray_index(push_lift(push_lift(RHO, INSTR[0]), PHI)[W2])
ok5b &= (DELIVERED == ASSIGN(W0))       # what arrives at W2 is the ray that STARTED at W0 ...
ok5b &= (DELIVERED != ASSIGN(W2))       # ... and NOT the one the section names there
# inertness is not special to this word: no native operation rotates any ray, anywhere on the support
for op in (PHI, INSTR[0], INSTR[1]):
    moved = push_lift(RHO, op)
    ok5b &= all(ray_index(moved[op[s]]) == ray_index(RHO[s]) for s in RHO)
# and the word is not closed either: nothing in the native algebra supplies the edge W2 -> W0 that
# a three-point Bargmann invariant silently inserts through its third overlap
ok5b &= all(op[W2] != W0 for op in (PHI, INSTR[0], INSTR[1]))
# so the DYNAMICALLY REALIZED triple is one ray three times, and its invariant is a positive real
ok5b &= is_real_nonneg(bargmann(*[RAYS[DELIVERED]] * 3))
# Separately: the construction has nV visible values and no neighbour relation at all, so "three
# connected local SITES" -- the spatial plaquette a hypercharge curvature would live on -- does not
# exist in it to be exhibited even if the fibre were not inert.
NO_SPATIAL_PLAQUETTE = (len({s[0] for s in STATES}) < 3)
ok5b &= NO_SPATIAL_PLAQUETTE
check("CB5b", ok5b,
      f"THE NATIVE TRANSPORT IS FLAT. This is a statement about the transport P~ = P (x) I and "
      f"about the tested word, and NOT about every connection the extension could carry — [SM "
      f"§6.5]'s Bargmann connection W_xy = <psi_x|psi_y>/|<psi_x|psi_y>| is induced by a SECTION "
      f"through overlaps and does not need the transport to rotate anything, so it is untouched "
      f"here. The state-dependent lift does reproduce the comb exactly at both actions "
      f"and still retracts onto the fixed-basis theory. But P~ = P (x) I moves a block without "
      f"touching it, so the fibre is INERT: no native operation rotates any ray anywhere on the "
      f"support, and along the word s, I_0 s, phi I_0 s the ray DELIVERED at the third state is "
      f"ray {DELIVERED}, the one that started at the first — not ray {ASSIGN(W2)}, which is merely "
      f"what the section names there. The dynamically realized triple is therefore one ray three "
      f"times and its Bargmann invariant is a positive real. The word is not even closed: no native "
      f"operation supplies the edge back to the start, which a three-point invariant inserts "
      f"silently through its third overlap. So a nonzero phase read off ASSIGN at three states is a "
      f"property of the SECTION and is not a holonomy OF THE NATIVE TRANSPORT — which is the only "
      f"thing ruled out. Independently, the "
      f"construction has {len({s[0] for s in STATES})} visible values and no neighbour relation, so "
      "the spatial plaquette the condition lives on does not exist here either, which is why the "
      "section-induced connection is not evaluated: there is no local graph here to evaluate it on")

# ------------------------------------------ CB5c  where the richer lift's conservativity fails
print("CB5c  P (x) U_s is OI-CONSERVATIVE; what it fails is the STRONGER intertwining condition")
# TWO CONDITIONS, and they must not be run together. This file's definition of conservative --
# stated in the header and used by CB4-CB5 -- is OI-CONSERVATIVE: the native classical state and
# readout are preserved and every comb probability OI actually supplies comes back exactly. STRONGLY
# CONSERVATIVE is the different, stronger demand that F o (lifted op) = (op) o F on the ENTIRE
# coherent state space, coherences included. The coherences are new data the enlarged theory has and
# OI never supplied, so the stronger condition is a legitimate extra hypothesis and NOT a
# consequence of the definition. What follows fails STRONG conservativity only; state-dependent
# rotations remain OI-conservative, which is what CB4-CB5 were about.
#
# The escape from CB5b's flat transport is a state-dependent fibre rotation,
# P~ = sum_s |P(s)><s| (x) U_s, on the grounds that the fibre trace forgets a unitary anyway. That
# reasoning holds only for BLOCK-DIAGONAL inputs. On a coherence between two native states the
# block (s,t) carries U_s rho_st U_t^dag, whose fibre trace is Tr(U_t^dag U_s rho_st) -- equal to
# Tr(rho_st) for EVERY rho_st only when U_t^dag U_s = I, since X -> Tr(AX) agrees with the trace
# on all X exactly when A = I. What that forces is exactly STATE-INDEPENDENCE: U_s = U_t. It does
# NOT force the common value to be the identity -- conjugating a nonidentity unitary cannot make it
# one -- and it says nothing about different native OPERATIONS carrying different global rotations.
# CB5d takes up what that freedom does and does not buy.
def bmul(A, B):
    return tuple(tuple(gadd(gmul(A[i][0], B[0][j]), gmul(A[i][1], B[1][j])) for j in range(2))
                 for i in range(2))
def bdag(A): return tuple(tuple(gconj(A[j][i]) for j in range(2)) for i in range(2))
def btr(A):  return gadd(A[0][0], A[1][1])
def is_scalar(A):
    """A multiple of the identity. Conjugation cannot see one, which is why the native relations
    bind a fibre lift only up to a scalar and CB5d reads them projectively."""
    return A[0][1] == GZ and A[1][0] == GZ and A[0][0] == A[1][1]
U_I = ((GO, GZ), (GZ, GO))
U_D = (((F(0), F(1)), GZ), (GZ, (F(0), F(-1))))       # diag(i, -i): unitary, and not a phase times I
RHO_ST = ((GO, (F(1), F(1))), ((F(0), F(2)), (F(3), F(0))))    # an arbitrary off-diagonal block
ok5c = (bmul(U_D, bdag(U_D)) == U_I)                  # U_D really is unitary
# (a) on a DIAGONAL block any single U is forgotten by the trace — this is why CB4 passed
ok5c &= all(btr(bmul(bmul(U, RHO_ST), bdag(U))) == btr(RHO_ST) for U in (U_I, U_D))
# (b) on an OFF-DIAGONAL block two different U's are NOT forgotten
ok5c &= (btr(bmul(bmul(U_I, RHO_ST), bdag(U_D))) != btr(RHO_ST))
# (c) the general statement, on a basis of the 2x2 blocks: Tr(AX) = Tr(X) for all X iff A = I
BASIS = [((GO, GZ), (GZ, GZ)), ((GZ, GO), (GZ, GZ)), ((GZ, GZ), (GO, GZ)), ((GZ, GZ), (GZ, GO))]
A_NE = bmul(bdag(U_D), U_I)
ok5c &= (A_NE != U_I) and any(btr(bmul(A_NE, X)) != btr(X) for X in BASIS)
ok5c &= all(btr(bmul(U_I, X)) == btr(X) for X in BASIS)
check("CB5c", ok5c,
      "TWO CONDITIONS, and the finding is about the stronger one. OI-CONSERVATIVE — this file's "
      "definition, the one CB4-CB5 use — asks that the native classical state, the readout and "
      "every comb probability OI supplies come back exactly. The state-dependent rotation "
      "P (x) U_s MEETS that: on a diagonal block any single U is forgotten by the fibre trace, and "
      "the block-diagonal states are all the dynamics produces. STRONGLY CONSERVATIVE is the "
      "separate, stronger demand that the intertwining hold on the ENTIRE coherent state space; "
      "the coherences are data the enlarged theory has and OI never supplied, so it is an extra "
      "hypothesis rather than a consequence. What follows fails STRONG conservativity ONLY. "
      "But a coherence between two native states carries U_s rho_st U_t^dag, whose trace is "
      "Tr(U_t^dag U_s rho_st); with U_s = I and U_t = diag(i, -i) that differs from Tr(rho_st) "
      "exactly. And on a basis of the 2x2 blocks, Tr(AX) = Tr(X) for every X only when A = I — "
      "checked both ways here. WHAT THIS FORCES, exactly: U_t^dag U_s = I, i.e. the fibre rotation "
      "cannot depend on the STATE. It does NOT force the common value to be the identity, and it "
      "says nothing about different NATIVE OPERATIONS carrying different global rotations. That "
      "check closes the state-dependent case for STRONG conservativity and leaves it OPEN for "
      "OI-conservativity; CB5d takes up what the remaining freedom does and does not buy")

# ------------------------------- CB5d  the freedom CB5c leaves, and the underdetermination it gives
print("CB5d  operation-dependent rotations are conservative; the ONE TESTED WORD carries no holonomy")
# CB5c forbids the rotation from depending on the STATE. It leaves untouched a rotation depending on
# the OPERATION: lift each native operation o as P_o (x) U_o with U_o a single global unitary. Every
# block (s,t) then carries U_o rho_st U_o^dag -- the SAME U on both sides -- so the fibre trace is
# preserved on every coherence, not merely on the block-diagonal states. Conservativity is exact and
# unconditional here.
#
# A lift must respect the native RELATIONS -- but only PROJECTIVELY, and the difference matters.
# Each instrument is an involution ON ALL STATES, so I_a o I_a is the identity MAP. The fibre acts by
# CONJUGATION, rho -> U rho U^dag, which is blind to an overall phase, so what the relation forces is
# U_(I_a)^2 = e^{i theta} I -- a SCALAR -- and NOT U_(I_a)^2 = I. Demanding the strict equality is
# imposing a non-projective representation as an extra hypothesis, and an earlier version of this
# check did that silently. Since the target structure is itself Bargmann/projective geometry, the
# projective reading is the right one and the strict one would beg the question.
#
# What the projective relation still gives is that the tested word's holonomy is a SCALAR, and a
# scalar acts trivially by conjugation. So the withdrawn witness stays withdrawn -- for that ONE
# WORD, which is all that is tested here.
#
# And the scalar's VALUE carries no invariant content: J and (i J) implement the SAME conjugation
# channel while their squares are -I and +I. Reading -1 off a chosen representative as a Z_2 datum
# is reading a gauge choice; an earlier version of this check did that and tied it to CB2's real
# line bundle, wrongly. An invariant would be the class of the 2-cocycle, which is not computed.
U_OP = {'I_0': (((F(3, 5), F(0)), (F(-4, 5), F(0))),        # a rational rotation: unitary over Q(i)
                ((F(4, 5), F(0)), (F(3, 5), F(0)))),
        'I_1': U_I, 'phi': U_I}
ok5d = all(bmul(U, bdag(U)) == U_I for U in U_OP.values())
# conservative on EVERY block, coherences included: Tr(U X U^dag) = Tr(X) for all X, both U's equal
ok5d &= all(btr(bmul(bmul(U, X), bdag(U))) == btr(X) for U in U_OP.values() for X in BASIS)
OPMAP = {'phi': PHI, 'I_0': INSTR[0], 'I_1': INSTR[1]}
# the relation: each instrument is an involution ON EVERY STATE, so I_a o I_a is the identity map
INVOLUTIVE = {a: all(m[m[s]] == s for s in STATES) for a, m in INSTR.items()}
ok5d &= all(INVOLUTIVE.values())
# hence the length-four word is the identity OPERATION, not a loop
WORD_OPS = ('I_0', 'I_0', 'I_1', 'I_1')
def apply_word(ops, s):
    for o in ops:
        s = OPMAP[o][s]
    return s
WORD_IS_GLOBAL_IDENTITY = all(apply_word(WORD_OPS, s) == s for s in STATES)
ok5d &= WORD_IS_GLOBAL_IDENTITY
# so a relation-respecting lift is FORCED to give it the identity rotation, whatever U_(I_0) is
def hol(ops, U):
    H = U_I
    for o in ops:
        H = bmul(U.get(o, U_I), H)
    return H
ok5d &= (hol(WORD_OPS, {'I_0': U_I, 'I_1': U_I}) == U_I)
# The PROJECTIVE lift is strictly larger than the strict one, and a Gaussian-rational witness shows
# it: J is a quarter turn, J^2 = -I. Strictly that violates the involution; projectively it does not,
# because conjugating by -I is the identity on every density matrix. So J is a legitimate lift of an
# involution that the strict reading would have excluded.
J = ((GZ, GO), ((F(-1), F(0)), GZ))
ok5d &= (bmul(J, bdag(J)) == U_I)                            # unitary
J2 = bmul(J, J)
ok5d &= (J2 != U_I) and is_scalar(J2)                        # not I, but a SCALAR: projectively fine
ok5d &= all(bmul(bmul(J2, X), bdag(J2)) == X for X in BASIS)  # and conjugation by it is the identity
# The word's holonomy under that projective lift is J^2 = -I: a scalar, hence trivial as a CHANNEL.
HOLJ = hol(WORD_OPS, {'I_0': J, 'I_1': U_I})
ok5d &= (HOLJ == J2) and is_scalar(HOLJ)
# But that -1 is GAUGE, not a datum. Rescaling the representative by a phase leaves the conjugation
# channel identical and moves the squared scalar: (iJ)^2 = +I while J^2 = -I. So no Z_2 sign is
# established by choosing J, and none is claimed. An invariant would be the class of the 2-cocycle
# in H^2(G, U(1)) for a consistent projective representation, which this file does not compute.
iJ = tuple(tuple(gmul((F(0), F(1)), J[i][j]) for j in range(2)) for i in range(2))
ok5d &= (bmul(iJ, bdag(iJ)) == U_I)                                   # still unitary
ok5d &= all(bmul(bmul(J, X), bdag(J)) == bmul(bmul(iJ, X), bdag(iJ)) for X in BASIS)   # same channel
ok5d &= (bmul(iJ, iJ) == U_I) and (J2 != U_I)                         # ... different squared scalar
# the 3-4-5 rotation the withdrawn witness used is excluded even projectively: R^2 is NOT a scalar
R35 = U_OP['I_0']
ok5d &= (not is_scalar(bmul(R35, R35)))
# Is the question even live? Words fixing W0 that are NOT the identity map do exist, and some avoid
# phi entirely -- so they cannot be dismissed as steps through the bijection padding the way a lone
# phi at W0 can (W0 fails phi's constructed-branch guard). Whether a CONSISTENT lift can be
# nontrivial on any of them needs the presentation of the group these permutations generate, which
# this file does not compute. It is recorded as live and left open, not decided in either direction.
CAND = [w for L in range(1, 5) for w in itertools.product(OPMAP, repeat=L)
        if apply_word(w, W0) == W0 and any(apply_word(w, s) != s for s in STATES)]
PHI_FREE = [w for w in CAND if 'phi' not in w]
ok5d &= (len(CAND) > 0 and len(PHI_FREE) > 0)
ok5d &= (WORD_OPS not in CAND)          # the withdrawn witness is NOT one of them: it is the identity
ok5d &= not (W0[4] < K and wf_x(W0[1], W0[4]) and wf_a(W0[2], W0[4], wrote=True))   # W0 is padding
check("CB5d", ok5d,
      f"lifting each native operation o as P_o (x) U_o with a single GLOBAL U_o IS conservative on "
      f"every block, coherences included — the same U sits on both sides, so Tr(U X U^dag) = Tr(X) "
      f"unconditionally and CB5c's obstruction does not apply. The remaining constraint is the "
      f"native RELATIONS, and they bind only PROJECTIVELY. Both instruments are verified involutions "
      f"ON EVERY STATE, so I_0 I_0 I_1 I_1 is the identity MAP (checked on all {len(STATES)} "
      f"states) — but the fibre acts by conjugation, which is blind to a phase, so what is forced is "
      f"U^2 = scalar, NOT U^2 = I. The quarter turn J with J^2 = -I is exhibited as a legitimate "
      f"projective lift of an involution that the strict reading would wrongly exclude, and "
      f"conjugation by J^2 is verified to be the identity on every block. Demanding strictness would "
      f"impose a non-projective representation as a hidden hypothesis — question-begging, since the "
      f"target structure is itself Bargmann geometry. The withdrawn witness stays withdrawn on the "
      f"weaker ground: the 3-4-5 rotation's square is not even a scalar, so it fails projectively "
      f"too. For THIS ONE WORD the holonomy is then the scalar -I, trivial as a channel — and that "
      f"is the whole scope of the negative result. The -1 is GAUGE, not a datum: J and iJ implement "
      f"the SAME conjugation channel (verified on a basis) while their squares are -I and +I, so "
      f"reading a Z_2 sign off a chosen representative would be reading a gauge choice, and no such "
      f"sign is claimed. An invariant would be the class of the 2-cocycle in H^2(G, U(1)), not "
      f"computed here. Nothing is claimed about the extension class at large: the question is LIVE "
      f"rather than closed, since at length "
      f"<= 4 there are {len(CAND)} words fixing the base state that are not the identity map, and "
      f"{len(PHI_FREE)} of them use no phi at all, so they cannot be dismissed as steps through the "
      f"bijection padding the way a lone phi at the base state can. Deciding it needs the PROJECTIVE "
      f"representations — the 2-cocycles, the Schur multiplier — of the finite group these three "
      f"permutations generate, which this file does not compute. OPEN, and claimed in neither "
      f"direction; the projective reading makes the available freedom LARGER than the strict one, "
      f"not smaller")

# ---------------------------------------------------------------- CB6  the boundary statement
print("CB6  the boundary, and what it does and does not settle")
# Gated on CB1-CB5b: an unconditional True would print PASS beside red controls and the
# scope block below would assert conclusions drawn from failed checks.
verdict("CB6", all(CHECKS),
      "OI ADMITS AT LEAST ONE CONSERVATIVE COHERENT EXTENSION AND DOES NOT DETERMINE ITS COHERENT "
      "GEOMETRY. That is the whole claim, and it is an EXISTENCE statement, not a classification. "
      "S <=> D <=> Q_fb remains the exact classical / fixed-basis quotient; H~ = l^2(S) (x) C^2 "
      "with P~ = P (x) I and F = Tr_{C^2} is ONE explicit conservative completion of it (CB4-CB5), "
      "preserving the dynamics, the comb probabilities and the fixed-basis theory as a retract "
      "while carrying observables the old instrument algebra cannot see. THIS FILE DOES NOT "
      "CLASSIFY ALL QUANTUM COMPLETIONS: nothing here shows every completion preserving the "
      "quotient has tensor-product-fibre form, and 'a classical core plus a coherent fibre' is "
      "therefore how this witness is built, not a theorem about the alternatives. Its geometry is "
      "undetermined in the SPECIFIC senses CB5b-CB5d establish, and NO holonomy witness is claimed "
      "in this construction. The native P (x) I transport is FLAT and the tested word was open "
      "(CB5b). A STATE-dependent rotation stays OI-CONSERVATIVE and fails only the stronger "
      "intertwining on coherences, which is a separate hypothesis and not a consequence of the "
      "definition (CB5c). An OPERATION-dependent one is conservative in both senses, and the native "
      "relations bind it only PROJECTIVELY — conjugation is blind to a phase, so involutions force "
      "U^2 = scalar rather than U^2 = I. For the ONE TESTED WORD the holonomy is then a scalar and "
      "that witness stays withdrawn; the scalar's value is GAUGE, since J and iJ give the same "
      "channel with squares -I and +I, so no Z_2 datum follows from it (CB5d). Nothing is claimed "
      "about the extension class at large. "
      "Words fixing the base state without being the identity map do exist, some using no "
      "phi at all, so the question is LIVE; deciding it needs the PROJECTIVE representations of the "
      "group the native permutations generate, which is not computed here and is claimed in neither "
      "direction — and the projective reading makes that freedom LARGER, not smaller. "
      "Rank bounds are narrow too: CB2-CB3 bound BARGMANN PHASES OF RAY OVERLAPS in a "
      "fixed ambient space, not connection holonomy, and a complex line bundle can be non-flat. "
      "H-OBSERVER-BUNDLE REMAINS OPEN — not derived, not local (no neighbour relation, two visible "
      "values, so the plaquette it lives on is absent), not identified with the hypercharge "
      "channel, which is H-Y-vertex and untouched")

print()
if not all(CHECKS):
    print("     [scope] VERDICT WITHHELD: a control above failed, so the boundary statement below")
    print("     is not asserted. Fix the failing check before reading any conclusion from this run.")
else:
    print("     [scope] Established IN THIS PROBE, and NOT yet propagated to the manuscript — this")
    print("     is a round result pending acceptance, not a recorded corpus status:")
    print("     OI ADMITS AT LEAST ONE CONSERVATIVE COHERENT EXTENSION AND DOES NOT DETERMINE ITS")
    print("     COHERENT GEOMETRY. S <=> D <=> Q_fb remains the exact classical / fixed-basis")
    print("     quotient, and H~ = l^2(S) (x) C^2 with P~ = P (x) I and F = Tr_{C^2} is ONE explicit")
    print("     conservative completion of it: the dynamics, the comb probabilities and the")
    print("     fixed-basis retract all survive, and it carries observables the old instrument")
    print("     algebra cannot see. Nothing in the normalizer of the diagonal algebra escapes b440's")
    print("     no-go. The native transport is FLAT. A STATE-dependent rotation stays")
    print("     OI-CONSERVATIVE and fails only the STRONGER intertwining on coherences — a separate")
    print("     hypothesis, not a consequence of the definition. An OPERATION-dependent one is")
    print("     conservative in both senses, and the native relations bind it only PROJECTIVELY:")
    print("     conjugation is blind to a phase, so an involution forces U^2 = scalar, not U^2 = I.")
    print("     NO HOLONOMY WITNESS IS CLAIMED in this construction. For the ONE TESTED WORD the")
    print("     holonomy is a scalar, trivial as a channel, and that scalar's value is GAUGE — J")
    print("     and iJ give the same channel with squares -I and +I — so no Z_2 datum follows from")
    print("     it. An invariant would be the 2-cocycle class in H^2(G, U(1)), uncomputed. Nothing")
    print("     is claimed about the extension class at large. Words fixing the base state without")
    print("     being the identity map do exist, some using no phi at all, so the question is LIVE:")
    print("     deciding it needs the PROJECTIVE representations — 2-cocycles, Schur multiplier —")
    print("     of the group the native permutations generate, uncomputed here and claimed in")
    print("     neither direction. The projective reading makes that freedom LARGER, not smaller.")
    print("     NOT settled — and this is the important boundary. b441 does NOT classify all")
    print("     possible quantum completions: it exhibits one, and nothing here shows every")
    print("     completion of the quotient has tensor-product-fibre form. The rank bounds are")
    print("     bounds on BARGMANN PHASES OF RAY OVERLAPS in a fixed ambient space, not on")
    print("     connection holonomy — a complex line bundle can be non-flat. Flat native transport")
    print("     is not the same as no section-induced Berry connection, which is untouched here")
    print("     because the construction has no local graph to evaluate one on. H-OBSERVER-BUNDLE")
    print("     REMAINS OPEN: not derived, not local, not identified with hypercharge (H-Y-vertex).")
    print("     And the enlarged theory is NOT covered by the old S <=> D <=> Q_fb equivalence —")
    print("     that survives as a quotient only.")
print()
print("coherence_boundary_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
