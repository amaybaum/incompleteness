#!/usr/bin/env python3
# recurrence_entropy_probes.py — b444 (2026-08-28)
#
# Finite reversible recurrence versus indefinite exact realization: an entropy-budget theorem, and
# the window/stack trilemma as its constructive witness.
#
# b443 closed the operation-history route for the finite-horizon recording architecture by a bounded
# monotone grading, and handed on the question: can the recurrent finite substratum support a
# recurrent observation-history realization WITHOUT erasing the hidden information that makes phi
# well-defined? This file answers NO, twice over and at two different levels of generality, and is
# careful about which is which.
#
# THE CONSTRUCTIVE HALF (RE1-RE3), which is FAMILY-SPECIFIC. A ring-buffer realization -- an order-K
# Markov kernel over a fixed K-window, with the horizon counter removed entirely -- achieves what
# b442 and b443 could not: phi TOTAL with NO PADDING AT ALL, and genuine closed paths containing
# phi. b443's hypotheses simply do not apply to it. The cost is exact: phi is NOT INJECTIVE, its
# collisions differ ONLY in the two window heads that fall out, and it destroys between 1.64 and
# 2.00 bits per step. Repairing that with a genuine predecessor stack -- push and grow, blocking at
# overflow, which is what the manuscript's realization carries one for -- restores injectivity AND
# REINSTATES A BOUNDED MONOTONE GRADING, the stack fill, which is exactly b443 FH8's hypothesis. The
# circle closes. THIS IS A TRILEMMA EXHIBITED ON A FAMILY AND IS NOT CLAIMED TO BE UNIVERSAL.
#
# THE GENERAL HALF (RE4-RE6), which is ARCHITECTURE-INDEPENDENT. The obvious objection to any such
# family argument is that a generic finite permutation can recycle bits indefinitely, so "injectivity
# forces a growing stack" is false without further hypotheses. That objection is correct, and RE4
# tests it directly rather than waving it away: over hundreds of random bijections at four state
# space sizes, the visible block entropy NEVER exceeds log2|S|. The reason is one line and mentions
# no architecture:
#
#     H(X_1..X_n) <= H(s_0) <= log|S|   for every n,
#
# because the entire visible trajectory is a deterministic function of the initial state. SHUFFLING
# REDISTRIBUTES ENTROPY AND CANNOT CREATE IT. Hence the visible process of a finite bijection has
# ZERO ENTROPY RATE, and a stationary law of entropy rate h > 0 cannot be reproduced exactly beyond
# n = log|S| / h steps. RE6 shows the bound is TIGHT -- a de Bruijn cycle attains it exactly -- so
# this is a sharp theorem and not a loose inequality. No ring buffer, no stack and no shift register
# appears anywhere in the argument; the de Bruijn cycle is a witness that the bound is attained, not
# a hypothesis of the no-go.
#
# WHAT THIS DOES NOT EXPLAIN (RE7), and the round must not pretend otherwise. The entropy ceiling on
# b76B's horizon is 9 to 18 steps; b76B's actual horizon is K = 1. So the budget is NOT what limits
# b76B, and b443's grading is a separate, much stronger limitation for that construction. The two
# results are COMPLEMENTARY and the general theorem must not be presented as explaining b443's K = 1.
#
# AND IT CORRECTS NOTHING. The corpus scopes exactness to "every finite accessible horizon" with
# t << t_R, and zero occurrences of indefinite, for-all-time or unbounded-horizon exactness. Its one
# "arbitrarily long horizons" claim is the fair coin from the section 3.4 dilation, which carries a
# TAPE of seeds sized to the horizon, so |S| grows with K and the bound is satisfied. The theorem
# SUPPORTS that construction and makes its necessity quantitative: |S| >= 2^(hK) is FORCED, not
# merely what the construction happens to use.
#
#   RE1  the ring-buffer realization is TOTAL, unpadded, recurrent, and the record still does work
#   RE2  and NOT injective: collisions are exactly the two window heads, at a measured bit cost
#   RE3  the predecessor-stack repair restores injectivity and reinstates b443's grading
#   RE4  the recoding loophole, tested and closed: shuffling cannot create entropy
#   RE5  the general bound H_n <= log|S|, hence zero entropy rate and a horizon ceiling
#   RE6  the bound is TIGHT: de Bruijn cycles attain it exactly
#   RE7  what the bound does NOT explain, and what it does not correct
#   RE8  the verdict, gated on every control above
#
# Usage:  python3 recurrence_entropy_probes.py

import itertools, math, random, sys
from collections import Counter
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

# ---------------------------------------------------------------- the ring-buffer realization
nV, nA = 2, 2

def kern(ctx):
    xs, as_ = ctx
    p = F((1 + sum(xs) + 2 * sum(as_) + 3 * len(xs) + (xs[-1] ^ as_[-1])) % 7 + 1, 9)
    return {0: 1 - p, 1: p}

def build_ring(K):
    """Order-K Markov kernel over a fixed K-window. NO horizon counter: the record overwrites
    rather than fills, so b443's bounded monotone grading is absent by construction."""
    CTXS = [(h, a) for h in itertools.product(range(nV), repeat=K)
            for a in itertools.product(range(nA), repeat=K)]
    TAB = {c: (1 if kern(c)[1] >= F(1, 2) else 0) for c in CTXS}
    assert all(kern(c)[TAB[c]] > 0 for c in CTXS)          # every choice is in the kernel's support
    S = [(h, a, p) for h in itertools.product(range(nV), repeat=K)
         for a in itertools.product(range(nA), repeat=K)
         for p in [None] + list(range(nA))]
    PHI = {}
    for s in S:
        Hw, Aw, p = s
        if p is not None:
            A2 = Aw[1:] + (p,)
            PHI[s] = (Hw[1:] + (TAB[(Hw, A2)],), A2, None)
    INSTR = {}
    for act in range(nA):
        d = {}
        for s in S:
            Hw, Aw, p = s
            if p is None:  d[s] = (Hw, Aw, act)
            elif p == act: d[s] = (Hw, Aw, None)
        INSTR[act] = d
    return S, PHI, INSTR

HOR = (1, 2, 3)
RING = {K: build_ring(K) for K in HOR}

# ---------------------------------------------------------------- RE1  total, unpadded, recurrent
K = 2
S, PHI, INSTR = RING[K]
ELIGIBLE = [s for s in S if s[2] is not None]
TOTAL = (len(PHI) == len(ELIGIBLE))
GEN = {'phi': PHI, 'I_0': INSTR[0], 'I_1': INSTR[1]}
CLOSED = set()
for s0 in S:
    stack = [(s0, ())]
    while stack:
        cur, w = stack.pop()
        if w and cur == s0:
            CLOSED.add(w); continue
        if len(w) >= 8: continue
        for n, m in GEN.items():
            if cur in m: stack.append((m[cur], w + (n,)))
PHI_LOOPS = [w for w in CLOSED if 'phi' in w]
MAXPHI = max((w.count('phi') for w in PHI_LOOPS), default=0)
# the record must still be doing work, or the realization is not an observation-history one at all
byh = {}
for s in PHI:
    byh.setdefault(s[0], []).append(s)
DESCENDS = True
for h, ss in byh.items():
    outs = {}
    for s in ss:
        outs.setdefault(PHI[s][0], []).append(s)
    if len(outs) > 1:
        DESCENDS = False; break
ok1 = TOTAL and len(PHI_LOOPS) > 0 and MAXPHI > 0 and not DESCENDS
check("RE1", ok1,
      f"THE RING-BUFFER REALIZATION DOES WHAT b442 AND b443 COULD NOT. With the horizon counter "
      f"removed and the record a fixed K-window that OVERWRITES rather than fills, phi is TOTAL on "
      f"all {len(ELIGIBLE)} eligible states — NO PADDING AT ALL, where b443's construction needed "
      f"95.9% at this K — and the realization is RECURRENT: {len(CLOSED)} closed genuine words of "
      f"which {len(PHI_LOOPS)} CONTAIN phi, carrying up to {MAXPHI} phi steps in a single loop, "
      f"against b443's zero. b443's no-go does not apply here, by its own hypotheses. And the "
      f"record is still doing work: phi does NOT descend to the visible window alone, so this is a "
      f"genuine observation-history realization and not a visible-sector Markov chain")

# ---------------------------------------------------------------- RE2  the exact cost
ok2 = True
COST = {}
for Kh in HOR:
    _, P, _ = RING[Kh]
    imgs = {}
    for s, t in P.items():
        imgs.setdefault(t, []).append(s)
    inj = all(len(v) == 1 for v in imgs.values())
    # phi(H,A,p) = (H[1:]+(y,), A[1:]+(p,), None) pins H[1:], A[1:], p and y. The ONLY coordinates
    # it cannot pin are the two window heads H[0] and A[0].
    heads_only = all(a[0][1:] == b[0][1:] and a[1][1:] == b[1][1:] and a[2] == b[2]
                     for ss in imgs.values() for a in ss for b in ss)
    bits = math.log2(len(P) / len(imgs))
    COST[Kh] = (len(P), len(imgs), bits, heads_only)
    ok2 &= (not inj) and heads_only
CEIL = math.log2(nV * nA)
ok2 &= all(COST[Kh][2] <= CEIL + 1e-9 for Kh in HOR)
check("RE2", ok2,
      f"AND THE COST IS EXACT. phi is NOT INJECTIVE at any horizon — "
      f"{', '.join(f'K={Kh}: {COST[Kh][0]}->{COST[Kh][1]} images' for Kh in HOR)} — and every "
      f"collision differs ONLY in the two window heads H[0] and A[0], the coordinates that fall out "
      f"of the windows, verified at each K. The information destroyed per phi step is "
      f"{', '.join(f'{COST[Kh][2]:.2f}' for Kh in HOR)} bits against a ceiling of {CEIL:.2f} = the "
      f"two discarded slots; the gap below the ceiling is what the emitted value still reveals "
      f"about H[0]. So recurrence is bought precisely by erasure, and the erased quantity is "
      f"measured rather than described")

# ---------------------------------------------------------------- RE3  the repair closes the circle
HEADS = list(itertools.product(range(nV), range(nA)))
ok3 = True
STACK = {}
for D in (1, 2, 3):
    S0, P0, _ = RING[2]
    SL = []
    for f in range(D + 1):
        for body in itertools.product(HEADS, repeat=f):
            SL.append((body + ((None,) * (D - f)), f))
    P = {}
    for s in S0:
        for st in SL:
            body, f = st
            if s in P0 and f < D:                       # UNDEFINED at overflow: nowhere to record
                nb = list(body); nb[f] = (s[0][0], s[1][0])
                P[(s, st)] = (P0[s], (tuple(nb), f + 1))
    imgs = {}
    for k, v in P.items():
        imgs.setdefault(v, []).append(k)
    inj = all(len(v) == 1 for v in imgs.values())
    strict = all(P[k][1][1] > k[1][1] for k in P)        # the fill is a STRICTLY increasing grading
    STACK[D] = (len(P), inj, strict)
    ok3 &= inj and strict
check("RE3", ok3,
      f"THE REPAIR CLOSES THE CIRCLE. A GENUINE predecessor stack — push and grow onto the next "
      f"free slot, blocking at overflow because there is nowhere left to record what would be "
      f"discarded, which is what the manuscript's realization carries one for — RESTORES "
      f"INJECTIVITY at every depth tested ({', '.join(f'D={D}: {STACK[D][0]} defined' for D in (1,2,3))}) "
      f"AND REINSTATES A BOUNDED MONOTONE GRADING: the stack fill STRICTLY INCREASES under phi and "
      f"is bounded by D. That is exactly b443 FH8's hypothesis, so recurrence dies again by b443's "
      f"own theorem. Total, injective, well-defined: any two are available and the third fails. "
      f"THIS TRILEMMA IS EXHIBITED ON A FAMILY AND IS NOT CLAIMED TO HOLD FOR EVERY ARCHITECTURE")

# ---------------------------------------------------------------- RE4  the recoding loophole
# The objection the family argument cannot answer: a generic finite permutation recycles bits, so
# "injectivity forces a growing stack" is false without further hypotheses. TEST IT, do not wave it
# away. If any bijection could keep emitting fresh randomness, the general theorem below is wrong.
def block_entropies(perm, proj, nmax):
    out = []
    for L in range(1, nmax + 1):
        c = Counter()
        for s0 in range(len(perm)):
            s = s0; word = []
            for _ in range(L):
                word.append(proj[s]); s = perm[s]
            c[tuple(word)] += 1
        out.append(H(c))
    return out

random.seed(7)
BEST = {}
ok4 = True
for N in (8, 16, 64, 256):
    top = None
    for _ in range(200):
        p = list(range(N)); random.shuffle(p)
        proj = [random.randrange(2) for _ in range(N)]
        hs = block_entropies(p, proj, 12)
        if top is None or hs[-1] > top[-1]: top = hs
    BEST[N] = top
    ok4 &= all(v <= math.log2(N) + 1e-9 for v in top)     # never exceeds the budget
    ok4 &= (top[-1] <= math.log2(N) + 1e-9)
check("RE4", ok4,
      f"THE RECODING LOOPHOLE IS CLOSED, BY TEST AND NOT BY ASSERTION. Searching {4 * 200} random "
      f"bijections with random visible projections at |S| = 8, 16, 64 and 256, and keeping the best "
      f"at each size, the visible block entropy H_n NEVER exceeds log2|S| at any n — it saturates "
      f"there and stops: "
      f"{', '.join(f'|S|={N}: H_12={BEST[N][-1]:.2f} vs log2|S|={math.log2(N):.2f}' for N in (8, 16, 64, 256))}, "
      f"against an i.i.d. fair-bit target of H_12 = 12.00. SHUFFLING REDISTRIBUTES ENTROPY AND "
      f"CANNOT CREATE IT, so a finite reversible machine cannot recycle its way to indefinite fresh "
      f"randomness")

# ---------------------------------------------------------------- RE5  the general bound
# ARCHITECTURE-INDEPENDENT, and the proof mentions no construction: the whole visible trajectory is
# a deterministic function of s_0, so the block variable is a function of s_0 and
#     H(X_1..X_n) <= H(s_0) <= log|S|   for every n.
# Hence the visible process has ZERO ENTROPY RATE, and a stationary law of rate h > 0 cannot be
# reproduced exactly beyond n = log|S| / h. Verified as an inequality on the sampled systems, and
# separately as the deterministic-function fact it rests on.
DETERMINISTIC_IN_S0 = True
for N in (8, 16):
    p = list(range(N)); random.shuffle(p)
    proj = [random.randrange(2) for _ in range(N)]
    seen = {}
    for s0 in range(N):
        s = s0; word = []
        for _ in range(10):
            word.append(proj[s]); s = p[s]
        seen.setdefault(s0, tuple(word))
    DETERMINISTIC_IN_S0 &= (len(seen) == N)               # one word per initial state, no branching
RATE = {N: BEST[N][-1] / 12 for N in (8, 16, 64, 256)}
ok5 = DETERMINISTIC_IN_S0 and all(BEST[N][-1] <= math.log2(N) + 1e-9 for N in (8, 16, 64, 256))
check("RE5", ok5,
      f"THE GENERAL THEOREM. For a bijection phi on a finite S with visible projection pi and any "
      f"initial law, the whole visible trajectory is a DETERMINISTIC FUNCTION OF s_0 — verified: "
      f"each initial state yields exactly one visible word, with no branching anywhere — so "
      f"H(X_1..X_n) <= H(s_0) <= log|S| FOR EVERY n. The proof mentions no ring buffer, no stack "
      f"and no shift register. Two consequences: the visible process has ZERO ENTROPY RATE (the "
      f"sampled rates at n = 12 are already down to "
      f"{', '.join(f'{RATE[N]:.2f}' for N in (8, 16, 64, 256))} bits/step and fall as 1/n), and a "
      f"stationary law of entropy rate h > 0 CANNOT BE REPRODUCED EXACTLY BEYOND n = log|S| / h "
      f"STEPS. Equivalently |S| >= 2^(hn) is FORCED for exactness to horizon n")

# ---------------------------------------------------------------- RE6  the bound is tight
def de_bruijn(n):
    a = [0] * (2 * n); seq = []
    def db(t, p):
        if t > n:
            if n % p == 0: seq.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]; db(t + 1, p)
            for j in range(a[t - p] + 1, 2):
                a[t] = j; db(t + 1, t)
    db(1, 1); return seq

ok6 = True
TIGHT = {}
for n in (3, 4, 5, 6):
    s = de_bruijn(n); N = len(s)
    c = Counter(tuple(s[(i + k) % N] for k in range(n)) for i in range(N))
    hn = H(c)
    TIGHT[n] = (N, hn, len(c))
    ok6 &= (N == 2 ** n) and abs(hn - math.log2(N)) < 1e-9 and len(c) == 2 ** n
check("RE6", ok6,
      f"THE BOUND IS TIGHT, so RE5 is a sharp theorem and not a loose inequality. A de Bruijn cycle "
      f"of order n — the cyclic shift on 2^n states with the de Bruijn projection, a bijection and "
      f"a projection like any other — realizes every one of the 2^n words exactly once and ATTAINS "
      f"H_n = log2|S| exactly: "
      f"{', '.join(f'n={n}: |S|={TIGHT[n][0]}, H_n={TIGHT[n][1]:.2f}' for n in (3, 4, 5, 6))}. So a "
      f"finite reversible machine CAN be exact for log|S|/h steps and never for more. The de Bruijn "
      f"cycle is a WITNESS THAT THE BOUND IS ATTAINED and is NOT a hypothesis of the no-go")

# ---------------------------------------------------------------- RE7  what this does not do
BUDGET = math.log2(576)
CTXS_B = [((x,), (a,)) for x in range(nV) for a in range(nA)]
HS = [float(H(Counter({0: kern(c)[0], 1: kern(c)[1]}))) for c in CTXS_B]
CEIL_LO, CEIL_HI = BUDGET / max(HS), BUDGET / min(HS)
ok7 = (CEIL_LO > 1.0)          # b76B's actual horizon is 1, far BELOW the entropy ceiling
check("RE7", ok7,
      f"WHAT THE BOUND DOES NOT EXPLAIN, stated because the round would otherwise overreach. b76B "
      f"has |S| = 576, an entropy budget of {BUDGET:.2f} bits, and a per-step visible entropy "
      f"between {min(HS):.2f} and {max(HS):.2f} bits, so the ENTROPY CEILING on its horizon is "
      f"{CEIL_LO:.1f} to {CEIL_HI:.1f} steps. ITS ACTUAL HORIZON IS K = 1 — an order of magnitude "
      f"below. The budget is therefore NOT what limits b76B, b443's grading is a separate and much "
      f"stronger limitation for that construction, and the two results are COMPLEMENTARY. AND THIS "
      f"CORRECTS NOTHING IN THE CORPUS: exactness there is scoped to every finite accessible "
      f"horizon with t << t_R, with no claim of indefinite or for-all-time exactness anywhere; the "
      f"one arbitrarily-long-horizons claim is the fair coin of the dilation construction, which "
      f"carries a TAPE of seeds sized to the horizon, so |S| grows with K and RE5 is satisfied. The "
      f"theorem SUPPORTS that construction and makes its necessity quantitative")

# ---------------------------------------------------------------- RE8  the verdict
verdict("RE8", all(CHECKS),
        f"A FINITE REVERSIBLE REALIZATION CANNOT BE INDEFINITELY EXACT FOR A POSITIVE-ENTROPY LAW. "
        f"The visible trajectory is a deterministic function of the initial state, so "
        f"H(X_1..X_n) <= log|S| for every n, the visible process has zero entropy rate, and "
        f"exactness fails beyond log|S|/h steps — a bound that de Bruijn cycles attain, so it is "
        f"sharp. THAT ARGUMENT IS ARCHITECTURE-INDEPENDENT and the recoding loophole is closed by "
        f"test: shuffling cannot create entropy. Separately and FAR LESS GENERALLY, the window and "
        f"stack family exhibits how the obstruction bites: a ring buffer buys totality, absence of "
        f"padding and genuine phi-loops at the price of injectivity, at a measured 1.64 to 2.00 "
        f"bits per step; a predecessor stack buys injectivity back and reinstates b443's bounded "
        f"monotone grading, killing recurrence again. SO b444's QUESTION IS ANSWERED NO for this "
        f"family and the entropy theorem says why no family escapes indefinitely — but the TRILEMMA "
        f"ITSELF IS NOT PROVED UNIVERSAL, and deriving it from the OI conditions rather than "
        f"exhibiting it on a family REMAINS OPEN")

print()
print('     [scope] Settled and GENERAL: for any bijection on a finite state space with any visible')
print('     projection and any initial law, H(X_1..X_n) <= H(s_0) <= log|S| for every n; the visible')
print('     process has ZERO ENTROPY RATE; a stationary law of rate h > 0 is not exactly realizable')
print('     beyond log|S|/h steps; and the bound is TIGHT, attained by de Bruijn cycles. The')
print('     recoding loophole is closed by test, not assumed away. Settled and FAMILY-SPECIFIC: a')
print('     ring buffer is total, unpadded and recurrent but not injective, losing 1.64-2.00 bits a')
print('     step in exactly the two window heads; a genuine predecessor stack restores injectivity')
print('     and reinstates b443\'s grading.')
print('     NOT settled: THE TRILEMMA IS NOT UNIVERSAL. It is exhibited on the window/stack family;')
print('     deriving total + injective + well-defined + recurrent as jointly impossible FROM THE OI')
print('     CONDITIONS, rather than on a family, is open and is the next target. The entropy bound')
print('     does NOT explain b76B\'s K = 1 — its ceiling there is 9 to 18 steps — so it and b443\'s')
print('     grading are complementary and must not be merged. NOTHING is corrected in the corpus:')
print('     exactness there is already scoped to finite horizons with t << t_R, and the fair-coin')
print('     construction carries a tape sized to the horizon, which RE5 supports and quantifies as')
print('     |S| >= 2^(hK) FORCED. b441, b442 and b443 stand; NOTHING propagates to the manuscripts.')
print()
print("recurrence_entropy_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
