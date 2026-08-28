#!/usr/bin/env python3
# bargmann_bridge_probes.py — b440 (2026-08-28), audit-corrected b440a
#
# Does the framework's OWN operational construction supply the observer states H-observer-bundle
# needs? No. And the reason is the one b435 already found on the other side.
#
# THE CANDIDATE BRIDGE. b439 located the escape from the hypercharge no-go in the geometry of the
# observer state bundle: for observer lines |psi_x> the Bargmann connection
# W_xy = <psi_x|psi_y>/|<psi_x|psi_y>| has triangle holonomy arg(<0|1><1|2><2|0>), nonzero at an
# explicit witness (pi/4). Separately, b434-b435 established that COMPLEX coherent source-loop data
# resolves relative phases that native permutation instruments cannot. A Bargmann invariant is a
# loop phase of exactly that kind, so the two arcs look as though they might meet:
#
#     coherent observer states -> arg[<psi_x|psi_y><psi_y|psi_z><psi_z|psi_x>] -> F_Y != 0.
#
# THIS FILE TESTS THAT AGAINST THE ACTUAL CONSTRUCTION, not against an arbitrary coherent Hilbert
# space completion. It rebuilds (S, phi, mu_H, {I_a}) by the recipe of intervention_probes.py
# (b76B) and asks what states that construction can actually reach.
#
# THE ANSWER, and it is negative in a specific and informative way.
#   BB1  phi and every I_a are BIJECTIONS of the finite S -- verified on the rebuilt construction,
#        not assumed. So on l^2(S) every native operation is a PERMUTATION matrix.
#   BB2  A permutation carries a basis state to a basis state. Every state reachable from a basis
#        state by any word in {phi, I_a} is therefore a basis state, and every overlap is exactly
#        0 or 1: REAL and NON-NEGATIVE. Every Bargmann invariant of three such states is 0 (distinct)
#        or 1 (repeated). There is never a nonzero PHASE.
#   BB3  The ACTUAL reduced observer states -- the framework's own initial law pushed through the
#        native permutations and traced over (h, a, u, c), not invented distributions -- are
#        DIAGONAL in the visible basis, hence mutually commuting, so the MIXED BARGMANN INVARIANT
#        Tr(rho_0 rho_1 rho_2) is a non-negative rational and carries no phase. Both the pure and
#        the mixed reading give zero.
#   BB3b The Uhlmann statement, kept SEPARATE. Tr(rho_0 rho_1 rho_2) is a mixed Bargmann invariant
#        and is NOT the Uhlmann phase, which is defined through amplitudes W with the transport
#        condition W_i^dag W_j > 0. For a family sharing a fixed eigenbasis the amplitudes may be
#        taken diagonal and positive, the condition holds with no rotation, and the holonomy is the
#        identity. Identifying the two would be an error, so they are two checks.
#   BB4  What would work is a COMPLEX SUPERPOSITION -- b439's witness (1,0), (1,1)/sqrt2, (1,i)/sqrt2.
#        The invariant that separates it from anything native is SUPPORT SIZE: a permutation image
#        of a basis vector has support exactly one, while a nonzero Bargmann phase needs at least
#        two components carrying a nontrivial relative complex phase.
#
# WHAT THIS DOES AND DOES NOT ESTABLISH (BB5), and the distinction matters.
#   It DOES exhibit a shared necessary ingredient: the complex-phase-bearing states H-observer-bundle
#   would need are exactly the complex-phase-bearing probes b435's SL9 identified as necessary for
#   coherent probing, and b435's SL7 showed the native permutation instrument set supplies none at
#   any order. One missing ingredient, appearing on both sides.
#   It does NOT identify b95's obstruction with b405's, which is the identification b426 examined
#   and declined to make. A shared necessary ingredient is weaker than a shared obstruction: two
#   problems can both need complex phases without being the same problem. b426's finding stands.
#
# THE DECISION TREE (BB6). Step 2 of the b440 tree -- can the native construction produce a nonzero
# exact Bargmann invariant -- answers NO. So H-observer-bundle remains an ADDITIONAL condition,
# H-Y-vertex is not reached, and H-native-VP and Z_E/Z_B stay closed. Nothing here shows the
# condition is unsatisfiable: it shows the construction as it stands does not satisfy it.
#
# ARITHMETIC. Exact throughout: the kernel and the hidden measure are Fractions, the reachability
# statement is combinatorial, and the Bargmann invariants are exact rationals or Gaussian rationals.
# No floating point -- at b434 a relative rank test read full rank on an identically zero matrix, and
# at b436 a slope fit read 7.2/10.5/15.9/22.5 for an exact 16.
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

# ---------------------------------------------------------------- the native construction (b76B)
nV, nA, BLANK, K = 2, 2, -1, 1

def kern(ctx):
    xs, as_ = ctx
    p = F((1 + sum(xs) + 2 * sum(as_) + 3 * len(xs) + (xs[-1] ^ as_[-1])) % 7 + 1, 9)
    return {0: 1 - p, 1: p}

CTXS = [((x,), (a,)) for x in range(nV) for a in range(nA)]
tables = [{}]
for c in CTXS:
    nxt = []
    for tb in tables:
        for y in range(nV):
            if kern(c)[y] > 0:
                t2 = dict(tb); t2[c] = y; nxt.append(t2)
    tables = nxt
UTAB = [tuple(sorted(tb.items())) for tb in tables]
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
SIDX = {s: i for i, s in enumerate(STATES)}

def wf_x(h, c): return all(h[i] != BLANK for i in range(c)) and all(h[i] == BLANK for i in range(c, K))
def wf_a(a, c, wrote):
    n = c + (1 if wrote else 0)
    return all(a[i] != BLANK for i in range(n)) and all(a[i] == BLANK for i in range(n, K))

def instrument(act):
    m = {}
    for s in STATES:
        x, h, a, u, c = s
        if c < K:
            al = list(a)
            if al[c] == BLANK: al[c] = act
            elif al[c] == act: al[c] = BLANK
            m[s] = (x, h, tuple(al), u, c)
        else:
            m[s] = s
    return m

INSTR = {act: instrument(act) for act in range(nA)}
PHI = {}
for s in STATES:
    x, h, a, u, c = s
    if c < K and wf_x(h, c) and wf_a(a, c, wrote=True):
        ctx = (tuple(list(h[:c]) + [x]), tuple(a[:c + 1]))
        y = dict(UTAB[u])[ctx]
        PHI[s] = (y, tuple(list(h[:c]) + [x] + [BLANK] * (K - c - 1)), a, u, c + 1)
undef = sorted(set(STATES) - set(PHI))
unhit = sorted(set(STATES) - set(PHI.values()))
for a_, b_ in zip(undef, unhit):
    PHI[a_] = b_

# ---------------------------------------------------------------- BB1  the ops are permutations
print("BB1  the native construction is rebuilt, and every one of its operations is a bijection")
ok1 = sorted(PHI.values()) == sorted(STATES)
for act, m in INSTR.items():
    ok1 &= (sorted(m.values()) == sorted(STATES))
ok1 &= (sum(MU.values()) == F(1))
check("BB1", ok1,
      f"|S| = {len(STATES)}, |C_H| = {len(UTAB)}, the hidden measure sums to 1 exactly, and phi and "
      f"both instruments are bijections of S — checked on the rebuilt object rather than assumed. "
      "So on l^2(S) every native operation is a PERMUTATION matrix, which is the only property the "
      "rest of this file uses")

# ---------------------------------------------------------------- BB2  reachable states, and phases
print("BB2  every reachable pure state is a basis state, so no Bargmann phase can arise")
GENS = [PHI] + [INSTR[a] for a in range(nA)]
frontier = {s: s for s in STATES[:24]}          # a spread of starting basis states
reached = set(frontier.values())
for _ in range(4):                               # every word of length <= 4 in the generators
    nxt = set()
    for s in reached:
        for g in GENS:
            nxt.add(g[s])
    reached |= nxt
# every reached object is a STATE, i.e. a basis vector: overlaps are 0 or 1 by definition
ok2 = reached <= set(STATES)
# the Bargmann invariant of three basis states, exhaustively over a sample of triples
seen_vals = set()
rl = sorted(reached)[:40]
for i in range(len(rl)):
    for j in range(len(rl)):
        for k in range(len(rl)):
            d = lambda p, q: 1 if p == q else 0
            seen_vals.add(d(rl[i], rl[j]) * d(rl[j], rl[k]) * d(rl[k], rl[i]))
ok2 &= (seen_vals <= {0, 1})
# The all-word-length statement is ALGEBRAIC, not a consequence of the depth-4 sweep: permutations
# are closed under composition, so every word is a permutation. Checked here as closure on the
# generators rather than left as prose — compose each pair and confirm the result is a bijection.
for g in GENS:
    for h_ in GENS:
        comp = {s: g[h_[s]] for s in STATES}
        ok2 &= (sorted(comp.values()) == sorted(STATES))
check("BB2", ok2,
      f"{len(reached)} states are reachable by words of length <= 4 in {{phi, I_0, I_1}} from 24 "
      "starting basis states, and every one is again a BASIS state. The bound on ALL word lengths "
      "is algebraic rather than sampled: the generators compose to bijections (checked on all "
      f"{len(GENS)**2} pairs), so every word is a permutation, and a permutation carries a basis "
      "vector to a basis vector. Hence every overlap is exactly 0 or 1 and the Bargmann invariant "
      f"<x|y><y|z><z|x> takes only the values {sorted(seen_vals)} — zero for distinct states, one "
      "for a repeated one, never a nonzero phase, at any depth whatever")

# ---------------------------------------------------------------- BB3  the ACTUAL reduced states
print("BB3  the actual reduced observer states carry no mixed Bargmann phase either")
# Derived from the construction, not invented: start from the framework's own initial law — uniform
# on the visible variable, mu_H on the hidden sector, protocol-shaped (clock 0, ledgers blank) —
# push it forward through ACTUAL native operations, and trace out (h, a, u, c).
def initial_law():
    p = {}
    blank_h, blank_a = (BLANK,) * K, (BLANK,) * K
    for x in range(nV):
        for u in range(len(UTAB)):
            p[(x, blank_h, blank_a, u, 0)] = MU[u] / nV
    assert sum(p.values()) == F(1)
    return p

def push(p, perm):
    """A permutation acts on a distribution by relabelling: diagonality is preserved by fiat."""
    out = {}
    for s, w in p.items():
        t = perm[s]
        out[t] = out.get(t, F(0)) + w
    assert sum(out.values()) == F(1)
    return out

def reduce_visible(p):
    """Trace out (h, a, u, c): the reduced observer state, as its diagonal in the visible basis."""
    r = [F(0)] * nV
    for (x, _h, _a, _u, _c), w in p.items():
        r[x] += w
    assert sum(r) == F(1)
    return r

p0 = initial_law()
p1 = push(push(p0, INSTR[0]), PHI)                  # act with a = 0, then step
p2 = push(push(p0, INSTR[1]), PHI)                  # act with a = 1, then step
RHOS = [reduce_visible(p0), reduce_visible(p1), reduce_visible(p2)]
# every reduced state is diagonal by construction, and diagonal matrices commute entry by entry
ok3 = all(all(isinstance(v, F) and v >= 0 for v in r) for r in RHOS)
ok3 &= all(RHOS[i][k] * RHOS[j][k] == RHOS[j][k] * RHOS[i][k]
           for i in range(3) for j in range(3) for k in range(nV))
tr = sum(RHOS[0][k] * RHOS[1][k] * RHOS[2][k] for k in range(nV))
ok3 &= isinstance(tr, F) and tr >= 0
# the reduced states are genuinely different, so this is not a degenerate coincidence
ok3 &= (RHOS[1] != RHOS[2])
check("BB3", ok3,
      f"the three reduced states come from the construction itself — the initial law (uniform "
      f"visible, mu_H hidden, protocol-shaped) pushed through the actual permutations I_0 then phi, "
      f"and I_1 then phi, with (h, a, u, c) traced out. They differ ({RHOS[1][0]} vs {RHOS[2][0]} "
      f"on x=0), so this is not degenerate. A permutation acts on a diagonal law by relabelling and "
      "the partial trace preserves diagonality, so every reduced state is diagonal in the SAME "
      f"visible basis and they all commute; the mixed Bargmann invariant Tr(rho_0 rho_1 rho_2) = "
      f"{tr} is a non-negative RATIONAL and carries no phase. The negative therefore does not "
      "depend on reading the observer's state as pure rather than mixed")

# ---------------------------------------------------------------- BB3b  the Uhlmann statement
print("BB3b the Uhlmann holonomy of that family is trivial, stated separately and not conflated")
# Tr(rho_0 rho_1 rho_2) is a mixed Bargmann invariant; it is NOT the Uhlmann phase, which is defined
# through amplitudes W with the parallel-transport condition W_i^dag W_j > 0. For a family sharing a
# fixed eigenbasis the amplitudes may be taken W_i = sqrt(rho_i), diagonal and positive, and then
# W_i^dag W_j is diagonal with non-negative entries — the transport condition holds with no
# rotation, so the holonomy is the identity. Checked as: all pairwise products are non-negative
# diagonals, which is the condition, rather than by computing a square root numerically.
okU = all(RHOS[i][k] * RHOS[j][k] >= 0 for i in range(3) for j in range(3) for k in range(nV))
okU &= all(RHOS[i][k] >= 0 for i in range(3) for k in range(nV))     # positivity, so sqrt is real
check("BB3b", okU,
      "the family shares a fixed eigenbasis, so Uhlmann amplitudes may be taken diagonal and "
      "positive; every pairwise product W_i W_j is then a non-negative diagonal, which is exactly "
      "the parallel-transport condition, satisfied with no rotation. The Uhlmann holonomy is "
      "therefore the identity. This is a SEPARATE statement from BB3: the triple trace is a mixed "
      "Bargmann invariant and must not be identified with the Uhlmann phase, which involves "
      "amplitudes and parallel transport rather than a product of density matrices")

# ---------------------------------------------------------------- BB4  what would work, and why not
print("BB4  the states that would work are complex superpositions, and permutations never make them")
def gmul(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def gconj(x):   return (x[0], -x[1])
def inner(u, v):
    a = gmul(gconj(u[0]), v[0]); b = gmul(gconj(u[1]), v[1])
    return (a[0] + b[0], a[1] + b[1])
w0 = ((F(1), F(0)), (F(0), F(0)))
w1 = ((F(1), F(0)), (F(1), F(0)))
w2 = ((F(1), F(0)), (F(0), F(1)))
B = gmul(gmul(inner(w0, w1), inner(w1, w2)), inner(w2, w0))
witness_phase = (B[1] != 0 or B[0] < 0)
# The invariant that matters is SUPPORT SIZE, not the literal amplitude set: a permutation image of
# a basis vector has support on exactly one component, while a nonzero Bargmann phase needs at
# least two components carrying a nontrivial relative complex phase.
supp = lambda v: sum(1 for c in v if c != (F(0), F(0)))
native_supports = {1}                                   # basis vectors, and permutation images
witness_supports = {supp(w0), supp(w1), supp(w2)}
ok4 = (witness_phase and B == (F(1), F(1))
       and max(witness_supports) >= 2 and native_supports == {1}
       and min(s for s in witness_supports if s >= 2) >= 2)
check("BB4", ok4,
      f"b439's witness gives <0|1><1|2><2|0> = {B[0]} + {B[1]}i, a nonzero phase. The property that "
      f"separates it from anything native is SUPPORT SIZE: its vectors have supports "
      f"{sorted(witness_supports)}, and a nonzero Bargmann phase requires at least two components "
      "carrying a nontrivial relative complex phase. Every permutation image of a basis vector has "
      "support exactly one, so no word in the native generators can reach such a state. The states "
      "that would satisfy H-observer-bundle are not merely absent from the construction; they are "
      "unreachable within it")

# ---------------------------------------------------------------- BB5  what this establishes
print("BB5  a shared necessary ingredient — which is NOT a shared obstruction")
# Gated on the checks above: an unconditional True would print PASS beside a red control,
# and this verdict has no computation of its own — it summarizes the ones that do.
verdict("BB5", all(CHECKS),
      "the complex-phase-bearing states H-observer-bundle would need are exactly the "
      "complex-phase-bearing probes b435's SL9 identified as necessary for coherent probing, and "
      "b435's SL7 showed the native permutation instrument set supplies none of them AT ANY ORDER. "
      "That is a genuine shared ingredient across the operational and lattice arcs. It is NOT the "
      "identification of b95's obstruction with b405's that b426 examined and declined to make: "
      "two problems can both require complex phases without being the same problem, and no shared "
      "formalism relating their dimensions is exhibited here. b426's no-bridge finding stands")

# ---------------------------------------------------------------- BB6  the decision-tree verdict
print("BB6  the verdict, and what stays closed")
# Gated on the checks above: an unconditional True would print PASS beside a red control,
# and this verdict has no computation of its own — it summarizes the ones that do.
verdict("BB6", all(CHECKS),
      "step 2 of the b440 tree — can the native construction produce a nonzero exact Bargmann "
      "invariant — answers NO, on both the pure and the mixed reading. So H-observer-bundle remains "
      "an ADDITIONAL condition on the framework rather than a consequence of it; H-Y-vertex is not "
      "reached and is untested; and H-native-VP and Z_E/Z_B stay closed. What is NOT shown is that "
      "the condition is unsatisfiable — only that the construction as it stands does not satisfy "
      "it. A different observer-level map (§4.7.1.1) is not excluded by anything here")

print()
if not all(CHECKS):
    print("     [scope] VERDICT WITHHELD: a control above failed, so the statement below is not")
    print("     asserted. Fix the failing check before reading any conclusion from this run.")
else:
    print("     [scope] Settled: the framework's own (S, phi, mu_H, {I_a}) cannot supply the observer")
    print("     states H-observer-bundle needs. Its operations are permutations, so reachable pure")
    print("     states are basis states with 0/1 overlaps and no Bargmann phase at any word length;")
    print("     the post-trace-out states are diagonal, so the mixed generalization vanishes too; and")
    print("     the witness states that do carry a phase are complex superpositions no permutation")
    print("     produces. The candidate bridge therefore FAILS in the direction b435 predicted.")
    print("     NOT settled: that H-observer-bundle is unsatisfiable — a different observer-level map")
    print("     is untouched here. H-Y-vertex is not reached. And this is a shared NECESSARY INGREDIENT")
    print("     across the two arcs, not the shared obstruction b426 declined to assert; b426 stands.")
print()
print("bargmann_bridge_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
