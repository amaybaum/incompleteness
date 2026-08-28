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
#        its unitary normalizer, and the normalizer is exactly the MONOMIAL group U = D_phase P.
#        Enlarging the native operations from permutations to the whole normalizer buys NOTHING: a
#        monomial unitary sends a basis vector to a PHASE TIMES a basis vector, i.e. to the same
#        RAY, and a Bargmann invariant sees only rays. Support stays 1, invariants stay 0 or
#        positive real. The no-go is therefore about the largest group that preserves the classical
#        structure, not about permutations specifically.
#   CB2  REAL MIXING IS NECESSARY BUT NOT SUFFICIENT. A real 2x2 mixer does create support-two
#        states, so support > 1 is genuinely necessary. But if the reachable ray geometry stays
#        REAL, every Bargmann product is real and the holonomy is confined to {0, pi} -- a Z_2 sign
#        structure, a real line bundle, NOT a continuously variable U(1)_Y connection.
#   CB3  COMPLEX RANK TWO IS SUFFICIENT, AND RANK ONE IS NOT. With a C^2 fibre the witness family
#        (1,0), (1,1), (1, t i) has Bargmann invariant 1 + t i, whose argument varies CONTINUOUSLY
#        with t. A rank-one fibre contributes only a global phase, which cancels in the ray.
#   CB4  THE CONSERVATIVE EXTENSION, and the identity that makes it conservative. Take
#        H~ = l^2(S) (x) C^2, lift every native operation as P~ = P (x) I, and forget by
#        F = Tr_{C^2}. Then F(P~ rho P~^dag) = P F(rho) P^dag EXACTLY -- checked on the actual
#        native permutations, not on a generic one.
#   CB5  THE SURVIVAL LEDGER, which is the point of the round. The comb probabilities come back
#        exactly after F; the fixed-basis theory is an exact RETRACT (F o (. (x) |0><0|) = id); AND
#        the enlarged theory carries observables the old instrument algebra cannot see -- two lifted
#        states with identical F and different fibre expectation. So the original
#        S <=> D <=> Q_fb equivalence is preserved as a QUOTIENT, and must NOT be read as covering
#        the enlarged coherent theory.
#
# THE BOUNDARY STATEMENT (CB6). OI fixes the classical operational quotient and leaves the coherent
# fibre over it UNDERDETERMINED. b440 showed the canonical fibre is trivial; this file shows how
# little is needed to make it nontrivial, and that everything already proved survives the forgetting.
# H-observer-bundle becomes AVAILABLE in the extension class -- it is still NOT DERIVED, because
# nothing in OI selects a fibre. H-Y-vertex is untouched and remains separate.
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
c_, s_ = F(3, 5), F(4, 5)
off = c_ * s_                      # the (0,1) entry of R diag(1,0) R^T
ok1 &= (off != 0)
check("CB1", ok1,
      f"a monomial unitary U = D P sends every basis vector to a unit multiple of a basis vector — "
      f"support {sorted({support(v) for v in imgs})}, the SAME ray — so every Bargmann invariant "
      f"among the images lies in {{0, positive real}} — {ntriples} triples, taking only the "
      f"{len(vals)} distinct values {sorted(vals)}. The monomial "
      "group is exactly the normalizer of the diagonal algebra (a rotation moves diag(1,0) off the "
      f"diagonal, by {off}), so this is the LARGEST group preserving the classical structure. b440's "
      "no-go is therefore not about permutations specifically: nothing in the normalizer escapes it")

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
q0 = ((F(1), F(0)), (F(0), F(0)))
q1 = ((F(1), F(0)), (F(1), F(0)))
args = []
for t in (1, 2, 3, 5):
    q2 = ((F(1), F(0)), (F(0), F(t)))
    B = bargmann(q0, q1, q2)
    args.append(B)
ok3 = all(B[1] != 0 for B in args) and len(set(args)) == len(args)
# rank one: the fibre contributes a global phase, which cancels in the ray — the invariant of three
# multiples of one vector is a positive real whatever the phases
u = ((F(1), F(0)), (F(2), F(0)))
scaled = [tuple(gmul(ph, c) for c in u) for ph in PHASES[:3]]
ok3 &= is_real_nonneg(bargmann(*scaled))
check("CB3", ok3,
      f"the witness family (1,0), (1,1), (1, t i) has Bargmann invariant 1 + t i, taking the "
      f"distinct values {[f'{B[0]}+{B[1]}i' for B in args]} as t runs — the argument varies "
      "CONTINUOUSLY, which is a genuine U(1) rather than CB2's sign. A rank-one fibre supplies only "
      "a global phase: three phase multiples of one vector give a positive real invariant, because "
      "the phases cancel in the ray. So complex rank two is the first sufficient class")

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
for _a, _b in zip(_und, _unh):
    PHI[_a] = _b

# A lifted state is rho = sum_s |s><s| (x) M_s, with M_s a 2x2 Gaussian-rational block. Permutation
# dynamics preserves that form, so the ledger below is exact without ever forming a 2|S| matrix.
def lift(p, fibre):
    return {s: tuple(tuple(gmul((w, F(0)), fibre[i][j]) for j in range(2)) for i in range(2))
            for s, w in p.items()}
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
ok4 = True
for fibre in (KET0, PLUS, YPLUS):
    rho = lift(INIT, fibre)
    for perm, name in ((PHI, 'phi'), (INSTR[0], 'I_0'), (INSTR[1], 'I_1')):
        lhs = forget(push_lift(rho, perm))
        rhs = push_classical(forget(rho), perm)
        ok4 &= (lhs == rhs)
    # and for a composite word, which is what an actual protocol applies
    lhs = forget(push_lift(push_lift(rho, INSTR[1]), PHI))
    rhs = push_classical(push_classical(forget(rho), INSTR[1]), PHI)
    ok4 &= (lhs == rhs)
check("CB4", ok4,
      "with H~ = l^2(S) (x) C^2, P~ = P (x) I and F = Tr_{C^2}, forgetting commutes with the "
      "dynamics EXACTLY — checked on the actual native operations phi, I_0, I_1 and on the "
      "composite word I_1 then phi, at three different fibre states including a coherent one. The "
      "identity holds because a permutation relabels the blocks and the fibre trace is taken "
      "blockwise; nothing about the fibre can leak into the classical marginal")

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

# ---------------------------------------------------------------- CB6  the boundary statement
print("CB6  the boundary, and what it does and does not settle")
check("CB6", True,
      "OI fixes the classical operational quotient and leaves the coherent fibre over it "
      "UNDERDETERMINED. b440 showed the canonical fibre is trivial; CB1-CB3 show how little is "
      "needed to make it nontrivial — not merely support > 1, which only buys a Z_2 sign, but a "
      "COMPLEX rank-two fibre — and CB4-CB5 show everything already proved survives the forgetting. "
      "So the non-uniqueness of OI -> QM is not 'many arbitrary quantum completions': it is a "
      "classical core plus an underdetermined coherent fibre, with a rank and reality bound on what "
      "the fibre must be for hypercharge. WHAT THIS DOES NOT DO: it does not DERIVE the fibre. "
      "H-observer-bundle becomes AVAILABLE in the extension class and is still not a consequence of "
      "OI, because nothing in the framework selects a fibre; and H-Y-vertex is untouched, since a "
      "curved observer connection existing says nothing about its vacuum-polarization coefficient")

print()
print("     [scope] Settled: nothing in the normalizer of the diagonal algebra escapes b440's no-go;")
print("     real mixing gives support two but only a Z_2 sign; a COMPLEX RANK-TWO fibre is the first")
print("     sufficient class; the conservative extension H~ = l^2(S) (x) C^2 with P~ = P (x) I and")
print("     F = Tr_{C^2} preserves the native dynamics, the comb probabilities and the fixed-basis")
print("     theory exactly, as a retract; and it carries observables the old instrument algebra")
print("     cannot see.")
print("     NOT settled: the fibre is not DERIVED. H-observer-bundle is available in the extension")
print("     class, not a consequence of OI. H-Y-vertex is untouched. And the enlarged theory is NOT")
print("     covered by the old S <=> D <=> Q_fb equivalence — that survives as a quotient only.")
print()
print("coherence_boundary_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
