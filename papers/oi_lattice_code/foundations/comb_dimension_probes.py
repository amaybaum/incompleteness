#!/usr/bin/env python3
# comb_dimension_probes.py — b445 (2026-08-28)
#
# The comb-dimension bound: response-function support as a capacity law, and what attains it.
#
# b444 bounded the state space of a finite deterministic realization by the entropy of ONE visible
# trajectory. That is the wrong instrument for an intervention-driven theory. A single initial state
# fixes an entire INTERVENTION-RESPONSE TABLE -- a function R_s : A^K -> V^K -- not one trajectory,
# so every distinct deterministic response strategy represented in the comb needs at least one
# distinct supported initial state. That gives a strictly stronger hierarchy, and b444's bound falls
# out as its weakest rung.
#
# THE SHARP OBJECT IS THE SUPPORT OF THE INITIAL PRIOR, not |S|. A realization may carry arbitrarily
# many unreachable states, which are irrelevant to its capacity; |S| >= |supp mu| is then a trivial
# corollary. Counting over all states instead of supported ones inflates the response count and is
# the error this file is written to avoid -- an earlier draft of this round reported 9 response
# classes where the supported count is 4.
#
#   THE HIERARCHY, each step a theorem and none an observation:
#
#       |S| >= |supp mu| >= N_resp(K) >= max_a N_words(K, a) >= max_a 2^{H(X^(a)_1..K)}
#
#   s_0 determines R_s; R_s evaluated at a fixed a gives one trajectory word; entropy never exceeds
#   log support. The last rung is b444.
#
# THREE RESULTS, KEPT SEPARATE, because they are established against different constraint sets:
#
#   (1) THE GENERAL BOUND. Response-function support is a comb-capacity lower bound at least as
#       strong as every fixed-intervention trajectory-support or entropy bound. Architecture-free.
#
#   (2) K = 1 TIGHTNESS. N_resp = d_latent = d_rev-comb = 4 for the b76B comb. d_latent = N_resp is
#       FREE -- aggregate the prior weight of all supported states sharing a response function and
#       the resulting four-atom ensemble reproduces the response distribution by construction, no
#       search. d_rev-comb = 4 is a SEARCHED result: an explicit four-state realization with
#       bijective phi, bijective involutive readout-preserving instruments, and the exact comb. The
#       canonical b76B realization uses 576 states -- a 144x state-count overhead.
#
#   (3) THE L4 ROBUSTNESS BOUNDARY. Impose POINTWISE ACTION SEPARATION -- I_a(s) != I_b(s) for every
#       supported s and a != b -- and four states become exhaustively impossible while five suffice.
#       So the minimum rises to exactly 5 under that strengthening.
#
# L4 IS A STRENGTHENING UNDER STUDY AND IS NOT AN OI CONDITION. The manuscript's C2/C4 do not
# generically require every intervention to write a persistent action label into fresh memory; C4
# concerns history-sensitive hidden mediation and readback, and a construction may PRE-ENCODE a
# response table rather than record the action. At K = 1 there is no later conditional response for
# an action trace to serve, so the four-state witness having no written record is a property of the
# horizon and not a defect. THIS FILE THEREFORE NEVER WRITES d_rev-comb < d_OI, and never identifies
# the L4 minimum with d_OI. The chain
#
#       N_resp = d_latent <= d_rev-comb <= d_OI <= d_canonical
#
# collapses only where the corresponding conditions have actually been checked, and d_OI is not
# measured here at all.
#
#   CD1  the hierarchy holds on b76B against the TRUE initial support, each step forced
#   CD2  the separation is strict but NOT monotone in K, and saturates against |supp mu|
#   CD3  d_latent = N_resp, free by aggregation — the four-atom ensemble reproduces the comb
#   CD4  K = 1 tightness: an explicit four-state reversible realization attains the bound
#   CD5  L4: four states exhaustively impossible, five sufficient, both verified
#   CD6  the canonical realization carries operationally redundant microstates
#   CD7  scope: L4 is not OI, d_OI is not claimed, nothing propagates
#   CD8  the verdict, gated on every control above
#
# Usage:  python3 comb_dimension_probes.py

import itertools, math, sys
from collections import Counter, defaultdict
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

def H(counts):
    t = sum(counts.values())
    return -sum(v / t * math.log2(v / t) for v in counts.values() if v)

# ---------------------------------------------------------------- the b76B realization (K = 1)
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

# THE SUPPORT: the experiment starts with an empty record at c = 0; the seed index u carries the
# ensemble. Unreachable and ill-formed states are not part of the capacity question.
OMEGA = [s for s in STATES if s[4] == 0 and all(v == BLANK for v in s[1])
         and all(v == BLANK for v in s[2])]
SEQS = list(itertools.product(range(nA), repeat=K))

def word(s0, q):
    s = s0; w = []
    for act in q:
        s = INSTR[act][s]
        w.append(PHI[s][0] if s in PHI else None)
        s = PHI.get(s, s)
    return tuple(w)

RESP = {s: tuple(word(s, q) for q in SEQS) for s in OMEGA}

# ---------------------------------------------------------------- CD1  the hierarchy
per = [(2 ** H(Counter(word(s, q) for s in OMEGA)), len({word(s, q) for s in OMEGA})) for q in SEQS]
MAX_E = max(p[0] for p in per)
MAX_W = max(p[1] for p in per)
N_RESP = len(set(RESP.values()))
ok1 = (len(STATES) >= len(OMEGA) >= N_RESP >= MAX_W >= MAX_E - 1e-9)
check("CD1", ok1,
      f"THE HIERARCHY HOLDS AGAINST THE TRUE INITIAL SUPPORT, and every step is a theorem rather "
      f"than an observation: s_0 determines the whole response table, that table evaluated at a "
      f"fixed action sequence gives one trajectory word, and entropy never exceeds log support. On "
      f"b76B: |S| = {len(STATES)} >= |supp mu| = {len(OMEGA)} >= N_resp = {N_RESP} >= "
      f"max_a N_words = {MAX_W} >= max_a 2^H = {MAX_E:.2f}. THE SHARP OBJECT IS |supp mu| AND NOT "
      f"|S|: counting all {len(STATES)} states instead of the {len(OMEGA)} supported ones inflates "
      f"the response count, which is how an earlier draft of this round reported 9 where the "
      f"supported answer is {N_RESP}")

# ---------------------------------------------------------------- CD2  strict but NOT monotone
# An order-1 kernel with a depth-K record keeps |UTAB| = 16 at every K, so the seed ensemble stays
# genuine and tractable while the horizon grows. This is b76B's kernel with a longer record.
def build_order1(Kh):
    def step(s, act):
        x, h, a, c = s
        if c >= Kh: return None
        al = list(a); al[c] = act
        y = dict(UTAB[x[1]])[((x[0],), (act,))]
        return ((y, x[1]), tuple(list(h[:c]) + [x[0]] + [BLANK] * (Kh - c - 1)), tuple(al), c + 1)
    Om = [((x, u), tuple([BLANK] * Kh), tuple([BLANK] * Kh), 0)
          for x in range(nV) for u in range(len(UTAB))]
    Sq = list(itertools.product(range(nA), repeat=Kh))
    def wd(s0, q):
        s = s0; w = []
        for act in q:
            s = step(s, act)
            w.append(None if s is None else s[0][0])
            if s is None: break
        return tuple(w)
    return Om, Sq, wd

SCAN = {}
ok2 = True
for Kh in (1, 2, 3, 4):
    Om, Sq, wd = build_order1(Kh)
    pr = [(2 ** H(Counter(wd(s, q) for s in Om)), len({wd(s, q) for s in Om})) for q in Sq]
    mE, mW = max(p[0] for p in pr), max(p[1] for p in pr)
    nr = len({tuple(wd(s, q) for q in Sq) for s in Om})
    SCAN[Kh] = (len(Om), nr, mW, mE, nr / mE)
    ok2 &= (len(Om) >= nr >= mW >= mE - 1e-9)
    ok2 &= (nr > mE)                                     # STRICTLY stronger at every horizon
RATIOS = [SCAN[Kh][4] for Kh in (1, 2, 3, 4)]
NON_MONOTONE = not (RATIOS[0] <= RATIOS[1] <= RATIOS[2] <= RATIOS[3])
SATURATES = (SCAN[2][1] == SCAN[3][1] == SCAN[4][1])
ok2 &= NON_MONOTONE and SATURATES
check("CD2", ok2,
      f"THE SEPARATION IS STRICT AT EVERY HORIZON BUT DOES NOT GROW MONOTONICALLY, which is the "
      f"honest form of this result. With a genuine seed ensemble at K = 1..4 the response count is "
      f"{', '.join(str(SCAN[Kh][1]) for Kh in (1,2,3,4))} against a single-sequence entropy bound "
      f"of {', '.join(f'{SCAN[Kh][3]:.2f}' for Kh in (1,2,3,4))}, so the ratio runs "
      f"{', '.join(f'{r:.1f}x' for r in RATIOS)} — it PEAKS AT AN INTERMEDIATE HORIZON and then "
      f"narrows. The reason is visible: N_resp SATURATES at {SCAN[2][1]} against the ceiling "
      f"|supp mu| = {SCAN[1][0]}, while single-sequence trajectory support keeps growing "
      f"({', '.join(str(SCAN[Kh][2]) for Kh in (1,2,3,4))}) and catches up. A claim that the gap "
      f"widens with K would be false")

# ---------------------------------------------------------------- CD3  d_latent, free
CLS = Counter(RESP.values())
TOT = len(OMEGA)
WEIGHTS = {r: F(c, TOT) for r, c in CLS.items()}
D_LATENT = len(CLS)
ok3 = (D_LATENT == N_RESP)
ok3 &= (sum(WEIGHTS.values()) == 1)
# the aggregated ensemble reproduces every fixed-sequence marginal exactly, by construction
for i, q in enumerate(SEQS):
    direct = defaultdict(F)
    for s in OMEGA: direct[word(s, q)] += F(1, TOT)
    viaR = defaultdict(F)
    for r, w in WEIGHTS.items(): viaR[r[i]] += w
    ok3 &= (dict(direct) == dict(viaR))
check("CD3", ok3,
      f"d_latent = N_resp = {D_LATENT}, AND IT IS FREE. Aggregating the prior weight of every "
      f"supported state sharing a response function gives a {D_LATENT}-atom latent ensemble with "
      f"weights {', '.join(str(WEIGHTS[r]) for r in sorted(WEIGHTS))}, and it is verified to "
      f"reproduce every fixed-sequence marginal EXACTLY. No search is involved: as an abstract "
      f"deterministic-strategy decomposition the support bound is attained by construction. What "
      f"remains open at that point is only whether those atoms can be carried by a DYNAMICAL "
      f"machine, which is a different and stronger question")

# ---------------------------------------------------------------- CD4  K = 1 tightness
# The searched constraint class, stated rather than implied: a common finite state space, bijective
# phi, bijective and involutive instruments, instruments preserving the readout, and exact
# reproduction of the comb.
PI4, I0_4, I1_4, PHI4 = (0, 0, 1, 1), (0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)
R4 = range(4)
ok4 = sorted(PHI4) == list(R4) and sorted(I0_4) == list(R4) and sorted(I1_4) == list(R4)
ok4 &= all(I0_4[I0_4[i]] == i for i in R4) and all(I1_4[I1_4[i]] == i for i in R4)
ok4 &= all(PI4[I0_4[i]] == PI4[i] and PI4[I1_4[i]] == PI4[i] for i in R4)
resp4 = {i: (PI4[PHI4[I0_4[i]]], PI4[PHI4[I1_4[i]]]) for i in R4}
ok4 &= (len(set(resp4.values())) == 4)
for a in (0, 1):
    m = Counter(resp4[i][a] for i in R4)
    ok4 &= (m[0] == 2 and m[1] == 2)                     # uniform mu gives 1/2, 1/2 as required
TARGET_MARG = all(len({word(s, q)[0] for s in OMEGA}) == 2 for q in SEQS)
ok4 &= TARGET_MARG
OVERHEAD = len(STATES) // 4
check("CD4", ok4,
      f"K = 1 TIGHTNESS: d_rev-comb = 4, ATTAINING the bound. An explicit four-state realization — "
      f"readout {PI4}, instruments {I0_4} and {I1_4}, evolution {PHI4} — is verified to have a "
      f"bijective evolution, bijective and INVOLUTIVE instruments that PRESERVE THE READOUT, all "
      f"four response classes one state apiece, and both comb marginals exactly 1/2, 1/2 under the "
      f"uniform prior. So N_resp = d_latent = d_rev-comb = 4 for this comb, and THE CANONICAL b76B "
      f"REALIZATION USES {len(STATES)} STATES — a {OVERHEAD}x state-count overhead. The constraint "
      f"class is the one named above and nothing more")

# ---------------------------------------------------------------- CD5  the L4 boundary
# L4, POINTWISE ACTION SEPARATION: I_a(s) != I_b(s) for every supported s and a != b. A neutral
# mathematical condition -- the post-intervention state distinguishes which action occurred -- and
# NOT the syntactic ban on I_0 = id. Persistence to the next stage, phi(I_0 s) != phi(I_1 s), is
# free once phi is injective, and is checked rather than assumed.
def invols_preserving(pi, n):
    R = range(n)
    return [p for p in itertools.permutations(R)
            if all(p[p[i]] == i for i in R) and all(pi[p[i]] == pi[i] for i in R)]

def minimal_n(L4):
    """Only phi o I_a matters for the response, and c = pi o phi ranges over every colouring with
    the same class sizes as pi as phi ranges over bijections. That reduction makes the search
    exhaustive rather than a sample."""
    for n in range(4, 8):
        R = list(range(n))
        for pi in itertools.product((0, 1), repeat=n):
            k = sum(pi)
            if k == 0 or k == n: continue                # constant readout: degenerate comb
            IV = invols_preserving(pi, n)
            cols = [c for c in itertools.product((0, 1), repeat=n) if sum(c) == k]
            for I0 in IV:
                for I1 in IV:
                    if L4 and any(I0[s] == I1[s] for s in R): continue
                    for c in cols:
                        if len({(c[I0[s]], c[I1[s]]) for s in R}) == 4:
                            return n, pi, I0, I1, c
    return None

NO_L4 = minimal_n(False)
WITH_L4 = minimal_n(True)
ok5 = (NO_L4 is not None and NO_L4[0] == 4)
ok5 &= (WITH_L4 is not None and WITH_L4[0] == 5)
# and the five-state witness is verified directly, independently of the search
PI5, I0_5, I1_5, PHI5 = (0, 0, 0, 1, 1), (0, 2, 1, 3, 4), (1, 0, 2, 4, 3), (0, 3, 4, 1, 2)
R5 = range(5)
ok5 &= sorted(PHI5) == list(R5) and sorted(I0_5) == list(R5) and sorted(I1_5) == list(R5)
ok5 &= all(I0_5[I0_5[i]] == i for i in R5) and all(I1_5[I1_5[i]] == i for i in R5)
ok5 &= all(PI5[I0_5[i]] == PI5[i] and PI5[I1_5[i]] == PI5[i] for i in R5)
ok5 &= all(I0_5[s] != I1_5[s] for s in R5)                            # L4 itself
ok5 &= all(PHI5[I0_5[s]] != PHI5[I1_5[s]] for s in R5)                # persistence, free from phi
resp5 = {s: (PI5[PHI5[I0_5[s]]], PI5[PHI5[I1_5[s]]]) for s in R5}
ok5 &= (len(set(resp5.values())) == 4)
MU5 = {0: F(1, 4), 1: F(1, 4), 2: F(1, 4), 3: F(1, 8), 4: F(1, 8)}
ok5 &= (sum(MU5.values()) == 1)
byc = defaultdict(F)
for s in R5: byc[resp5[s]] += MU5[s]
ok5 &= all(v == F(1, 4) for v in byc.values())
for a in (0, 1):
    m = defaultdict(F)
    for s in R5: m[resp5[s][a]] += MU5[s]
    ok5 &= (m[0] == F(1, 2) and m[1] == F(1, 2))
check("CD5", ok5,
      f"THE L4 BOUNDARY. Imposing POINTWISE ACTION SEPARATION — I_a(s) != I_b(s) at every supported "
      f"state, a neutral condition and not a ban on I_0 = id — makes FOUR STATES EXHAUSTIVELY "
      f"IMPOSSIBLE and FIVE sufficient. The search is exhaustive rather than sampled: only phi o "
      f"I_a affects the response, and pi o phi ranges over every colouring of the same class sizes, "
      f"so all readouts, all readout-preserving involution pairs and all colourings are covered. "
      f"The five-state witness — readout {PI5}, instruments {I0_5} and {I1_5}, evolution {PHI5} — "
      f"is verified INDEPENDENTLY of the search: bijections, involutions, readout-preserving, L4 at "
      f"every state, persistence phi(I_0 s) != phi(I_1 s) free from injectivity, four response "
      f"classes, weights 1/4 each under mu = (1/4, 1/4, 1/4, 1/8, 1/8), and both marginals exactly "
      f"1/2. So the minimum rises from 4 to 5 under that strengthening, and the source of the extra "
      f"state is NOT reversibility but the demand that the intervention be distinguishable in the "
      f"post-intervention state")

# ---------------------------------------------------------------- CD6  redundancy in the canonical
Om2, Sq2, wd2 = build_order1(2)
CLASSES2 = len({tuple(wd2(s, q) for q in Sq2) for s in Om2})
ok6 = (CLASSES2 < len(Om2))
check("CD6", ok6,
      f"THE CANONICAL REALIZATION CARRIES OPERATIONALLY REDUNDANT MICROSTATES: {len(Om2)} supported "
      f"seeds collapse to {CLASSES2} response classes at K = 2, so {len(Om2) - CLASSES2} supported "
      f"states are response-equivalent to another. That redundancy is exactly what a minimal-"
      f"realization theorem would want to quotient — but b443 and b444 are the standing warning not "
      f"to assume such a quotient respects the dynamics, and NO quotient is performed here")

# ---------------------------------------------------------------- CD7  scope
ok7 = True
check("CD7", ok7,
      f"SCOPE, and the wall this round must not breach. L4 IS A STRENGTHENING UNDER STUDY AND IS "
      f"NOT AN OI CONDITION: C2/C4 do not generically require every intervention to write a "
      f"persistent action label into fresh memory — C4 concerns history-sensitive hidden mediation "
      f"and readback, and a construction may PRE-ENCODE a response table instead. At K = 1 there is "
      f"no later conditional response for an action trace to serve, so the four-state witness "
      f"having no written record is a property of the horizon, not a defect. THIS FILE THEREFORE "
      f"NEVER CLAIMS d_rev-comb < d_OI AND NEVER MEASURES d_OI. The chain N_resp = d_latent <= "
      f"d_rev-comb <= d_OI <= d_canonical collapses only where conditions have been checked, and "
      f"only the first two collapses are established here. NOTHING PROPAGATES to the manuscripts")

# ---------------------------------------------------------------- CD8  the verdict
verdict("CD8", all(CHECKS),
        f"THE COMB-DIMENSION BOUND. A single initial state fixes an entire intervention-response "
        f"table, so |supp mu| >= N_resp(K) >= max_a N_words >= max_a 2^H — a capacity law strictly "
        f"at least as strong as every fixed-intervention trajectory bound, with b444 as its weakest "
        f"rung, and strict at every horizon tested though NOT monotonically so. At K = 1 on the "
        f"b76B comb the bound is ATTAINED: d_latent = {D_LATENT} free by aggregation, and "
        f"d_rev-comb = 4 by an explicit reversible realization, against a canonical {len(STATES)} "
        f"states — a {OVERHEAD}x overhead. Under the L4 strengthening four states become "
        f"exhaustively impossible and the minimum is exactly 5, which localizes the cost to action "
        f"distinguishability rather than to reversibility. d_OI IS NOT MEASURED and the multi-step "
        f"question at K >= 2 — where past interventions can first matter to later responses, and "
        f"where a pre-encoded response table, an action trace, a persistent record and readback "
        f"stop collapsing into one-step bookkeeping — IS OPEN")

print()
print('     [scope] Settled and GENERAL: response-function support is a comb-capacity lower bound')
print('     at least as strong as every fixed-intervention trajectory-support or entropy bound;')
print('     the sharp object is |supp mu| and not |S|; and the separation is strict at every')
print('     horizon tested but PEAKS AT AN INTERMEDIATE HORIZON rather than growing.')
print('     Settled at K = 1 FOR THE b76B COMB: d_latent = N_resp = 4 free by aggregation, and')
print('     d_rev-comb = 4 by an explicit four-state reversible realization, so the bound is')
print('     ATTAINED and the canonical 576-state construction carries a 144x overhead. Under the')
print('     L4 strengthening the minimum is exactly 5.')
print('     NOT settled: d_OI IS NOT MEASURED HERE. L4 is a strengthening under study, NOT derived')
print('     from the OI conditions, and this round never claims d_rev-comb < d_OI. The K = 1')
print('     tightness is ONE comb at ONE horizon, and that comb is maximally symmetric — two')
print('     uniform marginals and four equiprobable classes — which is the easy case for a lift.')
print('     Whether the L4 cost is one state in general is untested. K >= 2 is the open frontier:')
print('     it is the first horizon at which past interventions can matter to later responses, and')
print('     the first place a pre-encoded response table, an action trace, a persistent record and')
print('     readback can stop collapsing into one-step bookkeeping. b441-b444 stand; NOTHING')
print('     propagates to the manuscripts.')
print()
print("comb_dimension_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
