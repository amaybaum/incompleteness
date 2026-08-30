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
# TWO DIMENSION NOTIONS THAT MUST NOT BE CONFLATED, and conflating them was this round's error.
#
#   N_resp(M) is PER-REALIZATION. For one realization M it bounds that realization's own support:
#   |supp mu_M| >= N_resp(M). It is NOT an intrinsic property of the comb, and it is NOT a lower
#   bound on any OTHER realization of the same comb. Minimizing over realizations runs the other
#   way: D_strat(C) <= N_resp(M) for every M realizing C.
#
#   D_strat(C) is INTRINSIC: the minimum number of deterministic strategies needed to realize the
#   comb C, minimized over decompositions. A strategy RETAINS THE INITIAL VISIBLE LABEL,
#   sigma = (x_0, r) with r : A -> V, because the comb constrains P(X_1 | X_0, a) and a decomposition
#   that forgets X_0 is answering a weaker question.
#
# THE CORRECTED HIERARCHY:
#
#   per realization M:   |S_M| >= |supp mu_M| >= N_resp(M) >= max_a N_words(M,a) >= max_a 2^{H_a}
#   intrinsic:           d_rev-comb(C) >= D_strat(C) >= max_a N_words(C,a) >= max_a 2^{H(X^(a))}
#
# WHAT THIS ROUND GOT WRONG, recorded rather than quietly repaired. An earlier version derived
# "d_latent = 4" by aggregating the CANONICAL realization's response functions and treating the
# result as intrinsic. That argument shows four atoms SUFFICE; it does not show four are MINIMAL,
# and the same reasoning applied to K = 2..4 would have licensed "d_latent(K) >= 22", which does not
# follow at all. The canonical counts are response DIVERSITY of that construction and an UPPER bound
# on D_strat -- nothing more.
#
# AND THE L4 MINIMUM WAS WRONG. An earlier version reported that pointwise action separation forces
# five states. That search required the state space to exhibit all four counterfactual response
# pairs, which is STRICTLY STRONGER than reproducing the comb: the comb constrains action-conditioned
# probabilities, not the joint occurrence of counterfactual pairs. Under the correct criterion four
# states suffice under L4, exhibited in CD5. THE MINIMUM IS 4 AND L4 COSTS NOTHING HERE.
#
# WHAT SURVIVES, and it is the substance of the round: the per-realization hierarchy; D_strat(1) = 4
# proved by a genuine lower bound and attained; d_rev-comb(1) = 4 by an explicit reversible witness
# now checked against the FULL CONDITIONAL comb rather than unconditional marginals; and a canonical
# realization using 576 states against an intrinsic minimum of 4.
#
#   CD1  the PER-REALIZATION hierarchy on b76B against the true initial support, each step forced
#   CD2  the canonical response counts are an UPPER bound on D_strat, never a lower bound
#   CD3  D_strat(1) = 4: a genuine lower bound from the conditional comb, and it is attained
#   CD4  d_rev-comb(1) = 4, the witness verified against the FULL CONDITIONAL comb
#   CD5  L4 COSTS NOTHING: the minimum is 4, and the earlier claim of 5 is WITHDRAWN
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
      f"THE PER-REALIZATION HIERARCHY HOLDS AGAINST THE TRUE INITIAL SUPPORT, and every step is a theorem rather "
      f"than an observation: s_0 determines the whole response table, that table evaluated at a "
      f"fixed action sequence gives one trajectory word, and entropy never exceeds log support. On "
      f"b76B: |S| = {len(STATES)} >= |supp mu| = {len(OMEGA)} >= N_resp = {N_RESP} >= "
      f"max_a N_words = {MAX_W} >= max_a 2^H = {MAX_E:.2f}. THE SHARP OBJECT IS |supp mu| AND NOT "
      f"|S|: counting all {len(STATES)} states instead of the {len(OMEGA)} supported ones inflates "
      f"the response count, which is how an earlier draft of this round reported 9 where the "
      f"supported answer is {N_RESP}. THIS BOUNDS THIS REALIZATION'S OWN SUPPORT AND NOTHING ELSE: "
      f"N_resp(M) is a property of M, not of the comb, and it is NOT a lower bound on any other "
      f"realization of the same comb")

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
      f"THE CANONICAL RESPONSE COUNTS ARE AN UPPER BOUND ON D_strat, NEVER A LOWER BOUND. With a "
      f"genuine seed ensemble at K = 1..4 this realization's response count is "
      f"{', '.join(str(SCAN[Kh][1]) for Kh in (1,2,3,4))} against its own single-sequence entropy "
      f"bound of {', '.join(f'{SCAN[Kh][3]:.2f}' for Kh in (1,2,3,4))}. Both statements are about "
      f"THIS realization: they say its support must be at least that large, and they say the comb "
      f"admits a deterministic decomposition into at most that many strategies. THEY DO NOT SAY "
      f"D_strat(K) >= 22 — an earlier draft of this round read them that way, and the same reasoning "
      f"at K = 1 would have given 4 as an intrinsic minimum by luck rather than by proof. Within "
      f"this realization the ratio runs {', '.join(f'{r:.1f}x' for r in RATIOS)}: strict at every "
      f"horizon, PEAKING at an intermediate one and then narrowing as the count SATURATES at "
      f"{SCAN[2][1]} against the ceiling |supp mu| = {SCAN[1][0]} while single-sequence support "
      f"({', '.join(str(SCAN[Kh][2]) for Kh in (1,2,3,4))}) catches up. The non-monotonicity is a "
      f"fact about this realization, and a claim that the gap widens with K would be false")

# ---------------------------------------------------------------- CD3  D_strat, minimised
# THE INTRINSIC QUANTITY. A deterministic strategy RETAINS THE INITIAL VISIBLE LABEL: sigma =
# (x_0, r) with r : A -> V, because the comb constrains P(X_1 | X_0, a). Aggregating a particular
# realization's response functions while forgetting X_0 answers a weaker question and gives an upper
# bound only -- that is the error this check replaces.
VS, AS_ = [0, 1], [0, 1]
RSET = list(itertools.product(VS, repeat=len(AS_)))
STRATS = [(x0, r) for x0 in VS for r in RSET]

def decomposable(subset):
    """Can nonnegative weights on this strategy set reproduce P(X_1 | X_0, a) = 1/2 exactly?"""
    for x0 in VS:
        rs = [r for (y, r) in subset if y == x0]
        if not rs: return False
        D = 2 * len(rs)
        if not any(sum(w) == D and all(
                sum(w[i] for i, r in enumerate(rs) if r[a] == v) * 2 == D for a in AS_ for v in VS)
                for w in itertools.product(range(D + 1), repeat=len(rs))):
            return False
    return True

D_STRAT = None
for k in range(1, len(STRATS) + 1):
    if any(decomposable(sub) for sub in itertools.combinations(STRATS, k)):
        D_STRAT = k; break
# THE LOWER BOUND, as an argument and not only as a search: for each visible value x_0 and each
# action the target puts positive weight on BOTH outcomes, so no single deterministic strategy can
# serve an x_0 alone -- at least two are needed per x_0, and strategies for different x_0 are
# distinct because they carry the label. Two visible values give at least four.
LB = len(VS) * 2
ok3 = (D_STRAT == 4 == LB)
check("CD3", ok3,
      f"D_strat(1) = {D_STRAT}, BY MINIMISATION AND WITH A MATCHING LOWER BOUND. The lower bound is "
      f"an argument, not a search: for each visible value x_0 and each action the comb puts positive "
      f"weight on BOTH outcomes, so no single deterministic strategy serves an x_0 by itself; at "
      f"least two are needed per x_0, strategies for different x_0 are distinct because a strategy "
      f"carries the initial visible label, and {len(VS)} visible values therefore force at least "
      f"{LB}. Exhaustive minimisation over deterministic decompositions attains exactly that. THIS "
      f"REPLACES an earlier argument that aggregated the canonical realization's response functions "
      f"and read the result as intrinsic — that showed four atoms SUFFICE, never that four are "
      f"MINIMAL")

# ---------------------------------------------------------------- CD4  d_rev-comb(1) = 4
# pi reads the SAME visible register before and after phi, so X_0 = pi(s) and X_1 = pi(phi(I_a s)).
# The comb to reproduce is the CONDITIONAL law P(X_1 | X_0, a) -- an earlier version of this check
# tested only the unconditional marginals, which is weaker and would accept machines the comb
# rejects.
def reproduces_conditional(pi, I0, I1, phi, n):
    """P(X_1 = v | X_0 = x_0, a) = 1/2 for every x_0, a, v, under the uniform prior."""
    I = {0: I0, 1: I1}
    cls = defaultdict(list)
    for s in range(n): cls[pi[s]].append(s)
    if len(cls) < 2: return False
    for x0, ss in cls.items():
        for a in (0, 1):
            m = Counter(pi[phi[I[a][s]]] for s in ss)
            if not (len(m) == 2 and m[0] == m[1]): return False
    return True

PI4, I0_4, I1_4, PHI4 = (0, 0, 1, 1), (0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)
R4 = range(4)
ok4 = sorted(PHI4) == list(R4) and sorted(I0_4) == list(R4) and sorted(I1_4) == list(R4)
ok4 &= all(I0_4[I0_4[i]] == i for i in R4) and all(I1_4[I1_4[i]] == i for i in R4)
ok4 &= all(PI4[I0_4[i]] == PI4[i] and PI4[I1_4[i]] == PI4[i] for i in R4)
ok4 &= reproduces_conditional(PI4, I0_4, I1_4, PHI4, 4)
ok4 &= (D_STRAT == 4)                                    # so the witness attains the intrinsic min
OVERHEAD = len(STATES) // 4
check("CD4", ok4,
      f"d_rev-comb(1) = 4, ATTAINING D_strat. The four-state realization — readout {PI4}, "
      f"instruments {I0_4} and {I1_4}, evolution {PHI4} — is verified to have a bijective evolution "
      f"and bijective, INVOLUTIVE, READOUT-PRESERVING instruments, and to reproduce THE FULL "
      f"CONDITIONAL COMB P(X_1 | X_0, a) = 1/2 at every visible value and action, not merely the "
      f"unconditional marginals an earlier version of this check tested. Since D_strat(1) = "
      f"{D_STRAT} is a lower bound for every realization, the witness is MINIMAL. THE CANONICAL b76B "
      f"REALIZATION USES {len(STATES)} STATES — a {OVERHEAD}x state-count overhead against the "
      f"intrinsic minimum")

# ---------------------------------------------------------------- CD5  L4 costs nothing
# L4, POINTWISE ACTION SEPARATION: I_a(s) != I_b(s) for every supported s and a != b -- the
# post-intervention state distinguishes which action occurred. THE EARLIER CLAIM THAT L4 FORCES FIVE
# STATES IS WITHDRAWN. That search demanded the state space exhibit all four counterfactual response
# pairs, which is STRICTLY STRONGER than reproducing the comb: the comb constrains action-conditioned
# probabilities, not the joint occurrence of counterfactual pairs. Under the correct criterion four
# states suffice, and the witness below has only TWO distinct response pairs.
PI4L, I0_4L, I1_4L, PHI4L = (0, 0, 1, 1), (0, 1, 2, 3), (1, 0, 3, 2), (0, 2, 1, 3)
ok5 = sorted(PHI4L) == list(R4) and sorted(I0_4L) == list(R4) and sorted(I1_4L) == list(R4)
ok5 &= all(I0_4L[I0_4L[i]] == i for i in R4) and all(I1_4L[I1_4L[i]] == i for i in R4)
ok5 &= all(PI4L[I0_4L[i]] == PI4L[i] and PI4L[I1_4L[i]] == PI4L[i] for i in R4)
ok5 &= all(I0_4L[s] != I1_4L[s] for s in R4)                          # L4 itself
ok5 &= all(PHI4L[I0_4L[s]] != PHI4L[I1_4L[s]] for s in R4)            # persistence, free from phi
ok5 &= reproduces_conditional(PI4L, I0_4L, I1_4L, PHI4L, 4)
PAIRS_L4 = len({(PI4L[PHI4L[I0_4L[s]]], PI4L[PHI4L[I1_4L[s]]]) for s in R4})
ok5 &= (PAIRS_L4 == 2)                       # exactly why the old all-four-pairs criterion rejected it
# and no smaller n can work at all, L4 or not: D_strat is a lower bound on any realization
ok5 &= (D_STRAT == 4)
check("CD5", ok5,
      f"L4 COSTS NOTHING, AND THE EARLIER MINIMUM OF 5 IS WITHDRAWN. The four-state machine — "
      f"readout {PI4L}, instruments {I0_4L} and {I1_4L}, evolution {PHI4L} — satisfies POINTWISE "
      f"ACTION SEPARATION at every state, keeps bijectivity, involutivity and readout preservation, "
      f"carries persistence phi(I_0 s) != phi(I_1 s) free from injectivity, and REPRODUCES THE FULL "
      f"CONDITIONAL COMB. It exhibits only {PAIRS_L4} distinct counterfactual response pairs, which "
      f"is exactly why the earlier all-four-pairs criterion rejected it — that criterion was "
      f"STRICTLY STRONGER than comb equivalence and the result it produced was an artefact of it. "
      f"With D_strat(1) = {D_STRAT} as a lower bound for every realization, d_L4(1) = 4 EXACTLY. "
      f"Action distinguishability is free here, and NO dimension overhead is forced by it")

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
      f"no later conditional response for an action trace to serve. THIS FILE NEVER CLAIMS "
      f"d_rev-comb < d_OI AND NEVER MEASURES d_OI. The corrected chain is "
      f"d_rev-comb(C) >= D_strat(C) >= max_a N_words(C,a) >= max_a 2^H, intrinsic to the comb, with "
      f"the per-realization chain |S_M| >= |supp mu_M| >= N_resp(M) >= ... a SEPARATE statement about "
      f"one machine. At K = 1 the intrinsic minimum is {D_STRAT} and it is attained, so those two "
      f"rungs coincide HERE; nothing follows about K >= 2, where D_strat has not been computed. "
      f"NOTHING PROPAGATES to the manuscripts")

# ---------------------------------------------------------------- CD8  the verdict
verdict("CD8", all(CHECKS),
        f"THE COMB-DIMENSION BOUND, WITH ITS TWO DIMENSION NOTIONS KEPT APART. Per realization, a "
        f"single initial state fixes an entire intervention-response table, so |supp mu_M| >= "
        f"N_resp(M) >= max_a N_words >= max_a 2^H — b444's bound is the weakest rung. That is a "
        f"statement about ONE machine: N_resp(M) is NOT intrinsic and is NEVER a lower bound on "
        f"another realization of the same comb. The intrinsic quantity is D_strat(C), minimised over "
        f"deterministic decompositions whose strategies retain the initial visible label. AT K = 1 "
        f"ON THE b76B COMB, D_strat = {D_STRAT} by a genuine lower bound — both outcomes carry "
        f"positive weight at every (x_0, a), so two strategies are needed per visible value — and it "
        f"is ATTAINED by an explicit four-state reversible realization checked against the FULL "
        f"CONDITIONAL comb, against a canonical {len(STATES)} states, a {OVERHEAD}x overhead. L4 "
        f"COSTS NOTHING: a four-state machine satisfies pointwise action separation and reproduces "
        f"the comb, so the earlier minimum of 5 is WITHDRAWN — it came from demanding all four "
        f"counterfactual response pairs, which is strictly stronger than comb equivalence. d_OI is "
        f"NOT measured, and D_strat(K) for K >= 2 is NOT computed: the canonical counts of 22 bound "
        f"it from ABOVE only")

print()
print('     [scope] Settled and PER REALIZATION: a single initial state fixes an entire')
print('     intervention-response table, so |supp mu_M| >= N_resp(M) >= max_a N_words >= max_a 2^H,')
print('     with b444 as the weakest rung and |supp mu| — not |S| — as the sharp object. N_resp(M)')
print('     is a property of that machine and is NEVER a lower bound on another realization.')
print('     Settled and INTRINSIC, at K = 1 for the b76B comb: D_strat = 4 by a matching lower')
print('     bound and exhaustive minimisation; d_rev-comb = 4 by an explicit four-state reversible')
print('     witness verified against the FULL CONDITIONAL comb P(X_1 | X_0, a); and L4 COSTS')
print('     NOTHING, a four-state machine satisfying pointwise action separation reproducing the')
print('     same comb. The canonical realization uses 576 states: a 144x overhead.')
print('     WITHDRAWN THIS ROUND: the L4 minimum of 5, which came from demanding all four')
print('     counterfactual response pairs — strictly stronger than comb equivalence; and the')
print('     reading of canonical response counts as intrinsic minima, which showed only that four')
print('     atoms SUFFICE and would have licensed "D_strat(K) >= 22" at K = 2..4, which does not')
print('     follow.')
print('     NOT settled: D_strat(K) for K >= 2 is NOT COMPUTED — the canonical counts of 22 bound')
print('     it from ABOVE only, and computing it is the first task of the next round, BEFORE')
print('     asking whether reversible or OI constraints add overhead. d_OI is not measured; L4 is')
print('     a strengthening under study and is NOT derived from the OI conditions. The K = 1')
print('     results are ONE comb at ONE horizon and that comb is maximally symmetric.')
print('     b441-b444 stand; NOTHING propagates to the manuscripts.')
print()
print("comb_dimension_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
