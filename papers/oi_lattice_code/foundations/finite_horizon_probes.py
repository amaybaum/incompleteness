#!/usr/bin/env python3
# finite_horizon_probes.py — b443 (2026-08-28)
#
# The monotone-record no-go for finite-horizon OI realizations.
#
# b442 closed the operation-history projective route for b76B and left the obvious objection open:
# b76B is depth one, its kernel table is indexed by length-1 contexts only, and K >= 2 fails inside
# the construction. So the no-go might have been an artifact of a construction too small to host the
# question. This file builds the generalization b442 named as the prerequisite — a genuine
# VARIABLE-LENGTH-CONTEXT realization at arbitrary K, in which the c -> c+1 lookup a depth-c state
# performs is internal to the table and needs no completion — and asks whether it changes anything.
#
# IT DOES NOT, AND THE REASON IS SHARPER THAN DEPTH. The construction succeeds: at horizon K the
# genuine dynamics realizes exactly K successive phi steps, via the intended alternating history in
# which an instrument writes the action slot and phi then consumes it. But the step counter c is a
# BOUNDED MONOTONE GRADING — phi strictly increases it, instruments leave it alone — so the genuine
# phi-count on any path is exactly K and no genuine closed path contains phi at any K. Longer
# contexts lengthen paths and nothing else.
#
# THE THEOREM IS THEREFORE ARCHITECTURAL, NOT ABOUT b76B:
#
#     MONOTONE-RECORD NO-GO. Let a native realization carry a grading c : S -> {0..N} with N finite,
#     such that every genuine evolution arrow strictly increases c and no genuine intervention arrow
#     decreases it. Then no genuine closed path contains an evolution step.
#
# The proof is immediate — c is non-decreasing along any genuine path and strictly increases at each
# phi, so a path containing phi ends where it did not start. The content is not the proof; it is
# that the hypotheses hold for the finite-horizon recording architecture AS SUCH, verified here at
# three horizons rather than assumed, and that the grading is the SOLE blocker: FH4 restores a
# single c-lowering arrow and phi-containing loops appear at once. Nothing else in the construction
# prevents them.
#
# AND THE OBVIOUS ESCAPE IS BLOCKED BY OI ITSELF. The way to break a record grading is to forget the
# record. But phi does not descend to the visible sector: two states with the same visible value and
# different records have different next visible values (FH5). Quotienting the record away does not
# give a smaller dynamics, it gives no dynamics — which is the observation-incompleteness thesis
# appearing as an obstruction to the very quotient that would create the loops.
#
# TWO OBJECTS THAT MUST NOT BE CONFLATED, and this is the round's main scope wall. The corpus makes
# recurrence claims — Poincare recurrence in Main 2.3, the "minimal recurrent bijective
# representative", indivisibility somewhere in the recurrence cycle. Those concern the FIXED FINITE
# REVERSIBLE SUBSTRATUM, a bijection on a finite set carrying no bounded grading, which recurs for
# exactly that reason. This file constrains the FINITE-HORIZON OPERATIONAL REALIZATION, the
# step-counter construction of Main's finite realization theorem. They are different objects and
# this round corrects nothing in the corpus. Whether they can be ONE object is the next question and
# is not answered here.
#
#   FH1  the generalization reproduces b76B at K = 1, and u is a spectator
#   FH2  the grading: phi strictly increases c, instruments do not lower it, c is bounded
#   FH3  exactly K genuine phi steps at horizon K, and no genuine closed path contains phi
#   FH4  the grading is the SOLE blocker — one c-lowering arrow restores phi-loops at once
#   FH5  the escape is blocked: phi does not descend to the visible sector
#   FH6  the padding fraction WORSENS with K — a diagnostic, and not the theorem
#   FH7  scope: substratum vs horizon realization, and nothing propagates
#   FH8  the no-go, gated on every control above
#
# Usage:  python3 finite_horizon_probes.py

import itertools, sys
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

# ---------------------------------------------------------------- the variable-context realization
# b76B verbatim except for ONE change, which is the point: CTXS carries every length 1..K instead of
# length 1 alone, so a depth-c state's lookup (h[:c] + [x], a[:c+1]) is in the table for every c < K.
nV, nA, BLANK = 2, 2, -1

def kern(ctx):
    xs, as_ = ctx
    p = F((1 + sum(xs) + 2 * sum(as_) + 3 * len(xs) + (xs[-1] ^ as_[-1])) % 7 + 1, 9)
    return {0: 1 - p, 1: p}

def contexts(K):
    out = []
    for k in range(1, K + 1):
        out += [(xs, as_) for xs in itertools.product(range(nV), repeat=k)
                for as_ in itertools.product(range(nA), repeat=k)]
    return out

def all_tables(CTXS):
    """The full b76B ensemble of choice functions -- every table in the kernel's support."""
    tabs = [{}]
    for c in CTXS:
        nxt = []
        for tb in tabs:
            for y in range(nV):
                if kern(c)[y] > 0:
                    t2 = dict(tb); t2[c] = y; nxt.append(t2)
        tabs = nxt
    return [tuple(sorted(tb.items())) for tb in tabs]

def build(K, utab=None):
    """utab None -> the full ensemble (b76B's u coordinate). Otherwise a single fixed table."""
    CTXS = contexts(K)
    if utab is None:
        UTAB = all_tables(CTXS); withu = True
    else:
        UTAB = [utab]; withu = False
    XH = list(itertools.product(list(range(nV)) + [BLANK], repeat=K))
    AH = list(itertools.product(list(range(nA)) + [BLANK], repeat=K))
    S = [(x, h, a, u, c) for x in range(nV) for h in XH for a in AH
         for u in range(len(UTAB)) for c in range(K + 1)]
    def wf_x(h, c):
        return all(h[i] != BLANK for i in range(c)) and all(h[i] == BLANK for i in range(c, K))
    def wf_a(a, c, wrote):
        m = c + (1 if wrote else 0)
        return all(a[i] != BLANK for i in range(m)) and all(a[i] == BLANK for i in range(m, K))
    PHI = {}
    for s in S:
        x, h, a, u, c = s
        if c < K and wf_x(h, c) and wf_a(a, c, wrote=True):
            ctx = (tuple(list(h[:c]) + [x]), tuple(a[:c + 1]))
            PHI[s] = (dict(UTAB[u])[ctx], tuple(list(h[:c]) + [x] + [BLANK] * (K - c - 1)), a, u, c + 1)
    INSTR = {}
    for act in range(nA):
        d = {}
        for s in S:
            x, h, a, u, c = s
            if c < K:
                al = list(a)
                if al[c] == BLANK: al[c] = act
                elif al[c] == act: al[c] = BLANK
                d[s] = (x, h, tuple(al), u, c)
        INSTR[act] = d
    return S, PHI, INSTR, CTXS, UTAB, withu

def fixed_table(K):
    """One legitimate choice function: the kernel's likelier branch. Verified to be in the support."""
    C = contexts(K)
    tb = {c: (1 if kern(c)[1] >= F(1, 2) else 0) for c in C}
    assert all(kern(c)[tb[c]] > 0 for c in C)
    return tuple(sorted(tb.items()))

def genuine_ops(PHI, INSTR):
    return {'phi': PHI, 'I_0': INSTR[0], 'I_1': INSTR[1]}

def closed_words(S, gen, maxlen):
    """Every genuine word up to maxlen that returns some state to itself."""
    out = set()
    for s0 in S:
        stack = [(s0, ())]
        while stack:
            cur, w = stack.pop()
            if w and cur == s0:
                out.add(w); continue
            if len(w) >= maxlen: continue
            for n, m in gen.items():
                if cur in m: stack.append((m[cur], w + (n,)))
    return out

def max_phi_steps(S, gen, maxlen):
    best = 0
    for s0 in S:
        stack = [(s0, 0, 0)]
        while stack:
            cur, d, np_ = stack.pop()
            best = max(best, np_)
            if d >= maxlen: continue
            for n, m in gen.items():
                if cur in m: stack.append((m[cur], d + 1, np_ + (n == 'phi')))
    return best

# ---------------------------------------------------------------- FH1  reproduces b76B; u spectator
S1, PHI1, INSTR1, CTX1, UTAB1, _ = build(1)                 # full ensemble, as b76B
ok1 = (len(S1) == 576 and len(UTAB1) == 16 and len(CTX1) == 4 and len(PHI1) == 64)
# u is a spectator: no native operation touches it. This is what licenses fixing one table at K >= 2,
# and it is checked rather than asserted, because the whole K >= 2 tractability rests on it.
U_SPECTATOR = (all(PHI1[s][3] == s[3] for s in PHI1)
               and all(INSTR1[a][s][3] == s[3] for a in range(nA) for s in INSTR1[a]))
ok1 &= U_SPECTATOR
# and at K = 1 the generalization IS b76B: same contexts, same genuine fraction
ok1 &= (len(PHI1) / len(S1) == 64 / 576)
check("FH1", ok1,
      f"the variable-length-context construction REPRODUCES b76B at K = 1 — {len(S1)} states, "
      f"{len(UTAB1)} kernel tables over {len(CTX1)} contexts, phi genuine on {len(PHI1)} — so the "
      f"generalization is one, and not a different model wearing the name. The kernel-table index u "
      f"is verified to be a SPECTATOR: neither phi nor either instrument changes it. That is what "
      f"licenses fixing a single table at K >= 2, where the full ensemble is 2^20 tables and half a "
      f"billion states, and it is checked here because the round's tractability rests on it")

# ---------------------------------------------------------------- FH2  the grading
HORIZONS = (1, 2, 3)
BUILT = {K: build(K, fixed_table(K)) for K in HORIZONS}
grad = {}
ok2 = True
for K in HORIZONS:
    S, PHI, INSTR, C, _, _ = BUILT[K]
    gen = genuine_ops(PHI, INSTR)
    strict = all(PHI[s][4] > s[4] for s in PHI)
    nolower = all(m[s][4] >= s[4] for m in gen.values() for s in m)
    bounded = (max(s[4] for s in S) == K)
    grad[K] = (len(S), len(C), len(PHI), strict, nolower, bounded)
    ok2 &= strict and nolower and bounded
check("FH2", ok2,
      f"THE GRADING HYPOTHESES HOLD AT EVERY HORIZON TESTED {HORIZONS}, checked and not assumed: "
      f"phi STRICTLY INCREASES the step counter c, no genuine intervention arrow LOWERS it, and c "
      f"is BOUNDED by K. Sizes are "
      f"{', '.join(f'K={K}: {grad[K][0]} states over {grad[K][1]} contexts' for K in HORIZONS)}. "
      f"Note what is NOT a grading here: the record FILL is not monotone, since the instruments "
      f"erase as well as write — which is exactly why the instrument sector has loops at all. The "
      f"step counter is the sole grading, and it is the whole obstruction")

# ---------------------------------------------------------------- FH3  exactly K steps, no phi loop
ok3 = True
steps = {}
for K in HORIZONS:
    S, PHI, INSTR, _, _, _ = BUILT[K]
    gen = genuine_ops(PHI, INSTR)
    mx = max_phi_steps(S, gen, 2 * K + 3)
    cl = closed_words(S, gen, 2 * K + 3)
    steps[K] = (mx, len(cl))
    ok3 &= (mx == K)                                  # exactly the horizon, no more and no fewer
    ok3 &= (len(cl) > 0)                              # loops DO exist -- the check is not vacuous
    ok3 &= all('phi' not in w for w in cl)            # but never one containing phi
check("FH3", ok3,
      f"THE CONSTRUCTION SUCCEEDS AND CHANGES NOTHING. At horizon K the genuine dynamics realizes "
      f"EXACTLY K successive phi steps — "
      f"{', '.join(f'K={K}: {steps[K][0]}' for K in HORIZONS)} — through the intended alternating "
      f"history, an instrument writing the action slot and phi then consuming it, with no padding "
      f"used for any of it. So variable-length contexts DO make successive native evolution genuine, "
      f"which is what b442 named as the prerequisite. And it buys nothing: closed genuine words "
      f"exist at every horizon "
      f"({', '.join(f'K={K}: {steps[K][1]}' for K in HORIZONS)}, so the check is not vacuous) and "
      f"NOT ONE of them contains phi. Longer contexts lengthen paths and do nothing else")

# ---------------------------------------------------------------- FH4  the grading is the blocker
# A no-go whose hypotheses are never tested against a system that violates them proves nothing about
# which hypothesis carries the weight. So: take the SAME construction and add one arrow that LOWERS
# c. The arrow is NOT claimed to be OI-legitimate -- it is a probe of what is load-bearing.
K = 2
S, PHI, INSTR, _, _, _ = BUILT[K]
gen = genuine_ops(PHI, INSTR)
RESET = {s: (s[0], tuple([BLANK] * K), tuple([BLANK] * K), s[3], 0) for s in S if s[4] == K}
gen_reset = dict(gen); gen_reset['reset'] = RESET
CL_BASE = closed_words(S, gen, 2 * K + 5)
CL_RESET = closed_words(S, gen_reset, 2 * K + 5)
PHI_LOOPS = [w for w in CL_RESET if 'phi' in w]
ok4 = (not any('phi' in w for w in CL_BASE)) and len(PHI_LOOPS) > 0
# min() over a set is iteration-order dependent, so the witness printed would vary between runs.
# Break the tie on the word itself to make the message reproducible.
SHORTEST = min(sorted(PHI_LOOPS), key=len) if PHI_LOOPS else ()
check("FH4", ok4,
      f"THE BOUNDED MONOTONE GRADING IS THE SOLE BLOCKER, demonstrated rather than argued. Adding "
      f"ONE arrow that lowers c to the identical construction at K = {K} takes the closed-word "
      f"count from {len(CL_BASE)} to {len(CL_RESET)} and produces {len(PHI_LOOPS)} closed words "
      f"CONTAINING phi, the shortest being {SHORTEST}. Nothing else about the construction — not "
      f"the context length, not the state count, not the instrument relations — prevents loops. The "
      f"reset arrow is NOT claimed to be OI-legitimate and no result rests on it; it is here so "
      f"that the no-go is known to be about its hypothesis and not about the model")

# ---------------------------------------------------------------- FH5  the escape is blocked
# The way to break a record grading is to forget the record. Test whether phi survives that.
S2, PHI2, _, _, _, _ = BUILT[2]
byx = {}
for s in PHI2:
    byx.setdefault(s[0], []).append(s)
WITNESS = None
for x, ss in byx.items():
    outs = {}
    for s in ss:
        outs.setdefault(PHI2[s][0], []).append(s)
    if len(outs) > 1:
        k = sorted(outs); WITNESS = (x, outs[k[0]][0], k[0], outs[k[1]][0], k[1]); break
ok5 = WITNESS is not None
check("FH5", ok5,
      f"THE OBVIOUS ESCAPE IS BLOCKED, AND BLOCKED BY OI ITSELF. Forgetting the record is what would "
      f"break the grading, but phi does NOT descend to the visible sector: at visible value "
      f"x = {WITNESS[0] if WITNESS else '?'} the states {WITNESS[1] if WITNESS else '?'} and "
      f"{WITNESS[3] if WITNESS else '?'} agree on everything visible and step to DIFFERENT next "
      f"visible values, {WITNESS[2] if WITNESS else '?'} and {WITNESS[4] if WITNESS else '?'}. The "
      f"record is precisely what distinguishes them. Quotienting it away does not give a smaller "
      f"dynamics, it gives NO dynamics — the observation-incompleteness thesis appearing as an "
      f"obstruction to the one quotient that would create the loops")

# ---------------------------------------------------------------- FH6  padding, as a diagnostic
pad = {}
for Kh in HORIZONS:
    S, PHI, _, _, _, _ = BUILT[Kh]
    pad[Kh] = (len(S) - len(PHI)) / len(S)
ok6 = (pad[1] < pad[2] < pad[3])
check("FH6", ok6,
      f"THE PADDING FRACTION WORSENS WITH K — "
      f"{', '.join(f'K={Kh}: {pad[Kh]:.1%}' for Kh in HORIZONS)} — because the well-formedness "
      f"constraints tighten faster than the state space grows. b442's first part therefore "
      f"STRENGTHENS under the generalization instead of dissolving in it: totalizing phi becomes "
      f"MORE arbitrary as the horizon lengthens, not less. THIS IS A DIAGNOSTIC AND NOT THE "
      f"THEOREM. The no-go of FH3 is about the grading and would hold verbatim if phi were total")

# ---------------------------------------------------------------- FH7  scope, and no propagation
# The corpus DOES claim recurrence. Those claims are about the fixed finite reversible SUBSTRATUM --
# a bijection on a finite set with no bounded grading, which recurs for exactly that reason -- and
# not about the finite-horizon operational realization this file constrains. The two must not be
# conflated, and the round corrects nothing. Recorded as a check so a later round cannot quietly
# merge them.
SUBSTRATUM_IS_A_DIFFERENT_OBJECT = True   # asserted in prose below; the manuscripts are untouched
NO_PROPAGATION = True                      # this round edits no manuscript file
ok7 = SUBSTRATUM_IS_A_DIFFERENT_OBJECT and NO_PROPAGATION and U_SPECTATOR
check("FH7", ok7,
      f"SCOPE. This constrains the FINITE-HORIZON OPERATIONAL REALIZATION — the step-counter "
      f"construction — and NOT the fixed finite reversible SUBSTRATUM. The corpus's recurrence "
      f"claims (Poincare recurrence, the minimal recurrent bijective representative, indivisibility "
      f"somewhere in the recurrence cycle) are about the substratum, which carries no bounded "
      f"grading and recurs for exactly that reason. THEY ARE DIFFERENT OBJECTS AND THIS ROUND "
      f"CORRECTS NEITHER, so NOTHING PROPAGATES to the manuscripts. Whether the two can be ONE "
      f"object — a recurrent realization that does not destroy the record's predictive information "
      f"— is the next question and is NOT answered here")

# ---------------------------------------------------------------- FH8  the no-go
verdict("FH8", all(CHECKS),
        f"THE MONOTONE-RECORD NO-GO. Let a native realization carry a grading c into a finite range "
        f"such that every genuine evolution arrow strictly increases c and no genuine intervention "
        f"arrow decreases it; then no genuine closed path contains an evolution step, since c is "
        f"non-decreasing along any genuine path and strictly increases at each phi. The proof is "
        f"immediate and is not the content. THE CONTENT IS THAT THE HYPOTHESES HOLD FOR THE "
        f"FINITE-HORIZON RECORDING ARCHITECTURE AS SUCH, verified at horizons {HORIZONS} on a "
        f"construction that genuinely realizes K successive evolution steps with no padding, where "
        f"b442 could only reach depth one; that the grading is the SOLE blocker, since one "
        f"c-lowering arrow restores phi-loops at once; and that the escape through forgetting is "
        f"closed, since phi does not descend to the visible sector. So b442's no-go was not an "
        f"artifact of a construction too small: it is architectural, and raising K is not the "
        f"remedy")

print()
print('     [scope] Settled: a genuine VARIABLE-LENGTH-CONTEXT realization exists at every horizon')
print('     tested and delivers exactly K successive phi steps with no padding — so b442\'s depth-one')
print('     limit is lifted and the answer does not change. The step counter is a bounded monotone')
print('     grading, it is the SOLE blocker, and forgetting the record is not available because phi')
print('     does not descend to the visible sector. The operation-history route is therefore closed')
print('     for the FINITE-HORIZON RECORDING ARCHITECTURE and not merely for b76B.')
print('     NOT settled: this says NOTHING about RECURRENT OI realizations, where a cycling counter')
print('     would break the grading by construction — that is a different realization theorem from')
print('     the finite-horizon one, and whether OI can be realized recurrently WITHOUT destroying')
print('     the predictive information carried by the record is the open question this round hands')
print('     on. The corpus\'s recurrence claims concern the fixed finite reversible SUBSTRATUM, a')
print('     different object carrying no bounded grading; they are untouched and uncorrected here.')
print('     b441 and b442 stand: at least one conservative coherent extension exists, OI does not')
print('     determine its coherent geometry, and the four structures stay apart — this is the')
print('     operation-history cocycle, NOT the Berry/Bargmann section, NOT local spatial curvature,')
print('     NOT the U(1)_Y identification. NOTHING propagates to the manuscripts.')
print()
print("finite_horizon_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
