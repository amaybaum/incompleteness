#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/HiddenMemory.lean and OIBridge/FiniteEntropy.lean.

[Main] §3.4's unavoidable-hidden-predictive-memory theorem is kernel-proved there, all three
clauses. This file is the independent executable layer, and its job is not to repeat the proof but
to TEST THE HYPOTHESES SEPARATELY: each clause gets a countercontrol that removes exactly the
assumption its proof consumes and exhibits the failure.

  (a) is consumed by DETERMINISM. M2 replaces the deterministic next-visible map by a genuinely
      stochastic channel and the pushforward identity fails.
  (b) is consumed by MONOTONICITY UNDER CHANNELS, which is a property of total variation and not
      of "distance" in general. M4 exhibits a perfectly reasonable distance that INCREASES under a
      coarse-graining, so the clause is about TV specifically.
  (c) is consumed by the conditional MARKOV CHAIN X_<t -> H_t -> X_{t+1} given X_t. M6 breaks the
      chain by letting the next visible value read the history directly, and the data-processing
      inequality fails.

The 1,464-realization census in `papers/oi_lattice_code/foundations/memory_probes.py` remains the
independent finite layer for the clauses themselves; this file is deliberately about the walls.

  M1 clause (a), exact, over an exhaustive family of small realizations.
  M2 COUNTERCONTROL for (a): a nondeterministic channel breaks the pushforward identity.
  M3 clause (b), exact.
  M4 COUNTERCONTROL for (b): squared Euclidean distance is NOT monotone under a channel.
  M5 clause (c), both inequalities, over the same family.
  M6 COUNTERCONTROL for (c): break the Markov chain and data processing fails.
  M7 the finite Shannon layer itself: Gibbs, the uniform bound, and CMI nonnegativity, checked
     numerically against the definitions the Lean file uses.
  M8 lint: both Lean files are imported by the gated bridge root, carry no sorry, and state the
     theorems the coverage ledger attributes to them.

Usage:  python3 hidden_memory_probe.py
"""
import itertools
import math
import os
import random
import re
import sys
from fractions import Fraction as F

CHECKS = []


def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.join(HERE, os.pardir, 'lean-mathlib')
rng = random.Random(4481)

NP, NV, NH = 2, 2, 3          # |histories|, |C_V|, |C_H|


def rand_law():
    """A random rational law on (history, visible, hidden), normalized exactly."""
    raw = {(p, x, h): F(rng.randint(0, 4))
           for p in range(NP) for x in range(NV) for h in range(NH)}
    tot = sum(raw.values(), F(0))
    if tot == 0:
        raw[(0, 0, 0)] = F(1); tot = F(1)
    return {k: v / tot for k, v in raw.items()}


def rand_bijection():
    """A bijection of C_V x C_H, as the manuscript's phi."""
    pairs = [(x, h) for x in range(NV) for h in range(NH)]
    img = pairs[:]
    rng.shuffle(img)
    return dict(zip(pairs, img))


def next_vis(phi, x, h):
    return phi[(x, h)][0]


def tv(p, q, keys):
    return F(1, 2) * sum((abs(p.get(k, F(0)) - q.get(k, F(0))) for k in keys), F(0))


# ---------------------------------------------------------------- M1  clause (a)
ok1 = True
trials = 0
for _ in range(200):
    w = rand_law(); phi = rand_bijection()
    for p in range(NP):
        for x in range(NV):
            pr = sum((w[(p, x, h)] for h in range(NH)), F(0))
            if pr == 0:
                continue
            trials += 1
            post = {h: w[(p, x, h)] / pr for h in range(NH)}
            for v in range(NV):
                lhs = sum((w[(p, x, h)] for h in range(NH) if next_vis(phi, x, h) == v), F(0)) / pr
                rhs = sum((post[h] for h in range(NH) if next_vis(phi, x, h) == v), F(0))
                ok1 &= (lhs == rhs)
check("M1", ok1 and trials > 0,
      f"CLAUSE (a), THE PUSHFORWARD IDENTITY, exactly. Over {trials} positive-probability "
      f"(history, endpoint) pairs drawn from 200 random rational laws and random bijections of a "
      f"{NV} x {NH} configuration space, the next-step conditional law equals the pushforward of "
      f"the hidden posterior through f_x, entry for entry in exact rational arithmetic")

# ---------------------------------------------------------------- M2  countercontrol for (a)
# Replace the deterministic f_x by a stochastic kernel K(v | x, h). The conditional law is then a
# MIXTURE and no longer any pushforward of the posterior, because pushforwards of a distribution
# supported on the fibers cannot produce weight the fibers do not carry.
K = {(0, 0): {0: F(1, 2), 1: F(1, 2)}, (0, 1): {0: F(1), 1: F(0)},
     (0, 2): {0: F(0), 1: F(1)}}
w2 = {(0, 0, 0): F(1, 3), (0, 0, 1): F(1, 3), (0, 0, 2): F(1, 3)}
pr2 = sum(w2.values(), F(0))
post2 = {h: w2[(0, 0, h)] / pr2 for h in range(NH)}
mix = {v: sum((post2[h] * K[(0, h)][v] for h in range(NH)), F(0)) for v in range(NV)}
# every deterministic pushforward assigns each posterior atom entirely to one visible value
push_options = set()
for assign in itertools.product(range(NV), repeat=NH):
    push_options.add(tuple(sum((post2[h] for h in range(NH) if assign[h] == v), F(0))
                           for v in range(NV)))
check("M2", tuple(mix[v] for v in range(NV)) not in push_options,
      f"COUNTERCONTROL FOR (a) — DETERMINISM IS WHAT MAKES IT AN IDENTITY. Replace f_x by a "
      f"stochastic kernel that splits one hidden state's weight across two visible values: the "
      f"conditional law becomes {tuple(str(mix[v]) for v in range(NV))}, which is NOT among the "
      f"{len(push_options)} distributions any deterministic pushforward of the same posterior can "
      f"produce. Clause (a) is an equality only because the realization is deterministic")

# ---------------------------------------------------------------- M3  clause (b)
ok3 = True
pairs3 = 0
for _ in range(200):
    w = rand_law(); phi = rand_bijection()
    for x in range(NV):
        prs = [sum((w[(p, x, h)] for h in range(NH)), F(0)) for p in range(NP)]
        if any(pr == 0 for pr in prs):
            continue
        pairs3 += 1
        posts = [{h: w[(p, x, h)] / prs[p] for h in range(NH)} for p in range(NP)]
        pushes = [{v: sum((posts[p][h] for h in range(NH) if next_vis(phi, x, h) == v), F(0))
                   for v in range(NV)} for p in range(NP)]
        ok3 &= tv(pushes[0], pushes[1], range(NV)) <= tv(posts[0], posts[1], range(NH))
check("M3", ok3 and pairs3 > 0,
      f"CLAUSE (b), THE DISTINGUISHABILITY FLOOR, exactly. Over {pairs3} pairs of "
      f"positive-probability histories sharing an endpoint, the total-variation gap between the "
      f"observed next-step laws never exceeds the gap between the hidden posteriors")

# ---------------------------------------------------------------- M4  countercontrol for (b)
# Squared Euclidean distance is a perfectly good distance and is NOT monotone under channels.
pA = {0: F(1, 2), 1: F(1, 2), 2: F(0)}
pB = {0: F(0), 1: F(0), 2: F(1)}
coarse = {0: 0, 1: 0, 2: 1}                       # the channel: merge the first two outcomes
qA = {0: pA[0] + pA[1], 1: pA[2]}
qB = {0: pB[0] + pB[1], 1: pB[2]}
sq = lambda p, q, ks: sum(((p[k] - q[k]) ** 2 for k in ks), F(0))
before, after = sq(pA, pB, range(3)), sq(qA, qB, range(2))
check("M4", after > before and tv(qA, qB, range(2)) <= tv(pA, pB, range(3)),
      f"COUNTERCONTROL FOR (b) — MONOTONICITY IS A PROPERTY OF TOTAL VARIATION, NOT OF DISTANCE. "
      f"Squared Euclidean distance between the same two distributions INCREASES from {before} to "
      f"{after} under a coarse-graining channel, while total variation does not increase. Clause "
      f"(b) would be false with a different metric, so the metric is load-bearing")


# ---------------------------------------------------------------- M5  clause (c)
def entropy_nats(pmf):
    return -sum(v * math.log(v) for v in pmf if v > 0)


def cmi_bits(joint, ia, ib, ic):
    """I(A;C|B) in bits from a joint dict keyed by tuples, projecting with index tuples."""
    from collections import defaultdict
    pAB, pCB, pABC, pB = (defaultdict(float) for _ in range(4))
    for k, v in joint.items():
        f = float(v)
        pAB[tuple(k[i] for i in ia + ib)] += f
        pCB[tuple(k[i] for i in ic + ib)] += f
        pABC[tuple(k[i] for i in ia + ib + ic)] += f
        pB[tuple(k[i] for i in ib)] += f
    val = (entropy_nats(pAB.values()) + entropy_nats(pCB.values())
           - entropy_nats(pABC.values()) - entropy_nats(pB.values()))
    return val / math.log(2)


ok5 = True
worst = 0.0
for _ in range(200):
    w = rand_law(); phi = rand_bijection()
    joint = {(p, x, h, next_vis(phi, x, h)): w[(p, x, h)]
             for p in range(NP) for x in range(NV) for h in range(NH)}
    m_t = cmi_bits(joint, (0,), (1,), (3,))         # I(X_<t ; X_{t+1} | X_t)
    i_h = cmi_bits(joint, (0,), (1,), (2,))         # I(X_<t ; H_t  | X_t)
    ok5 &= (m_t <= i_h + 1e-12) and (i_h <= math.log2(NH) + 1e-12)
    worst = max(worst, m_t - i_h)
check("M5", ok5,
      f"CLAUSE (c), THE CAPACITY FLOOR, both inequalities. Over 200 random realizations, "
      f"M_t = I(X_<t; X_(t+1) | X_t) never exceeds I(X_<t; H_t | X_t) — the largest violation "
      f"found is {worst:.2e}, i.e. none beyond floating-point noise — and the hidden term never "
      f"exceeds log2({NH}) = {math.log2(NH):.4f} bits")

# ---------------------------------------------------------------- M6  countercontrol for (c)
# Break the Markov chain: let the next visible value read the HISTORY directly rather than only
# through the hidden state. Data processing then fails.
bad = None
for _ in range(4000):
    w = rand_law()
    joint = {(p, x, h, (p + x) % NV): w[(p, x, h)]      # X_{t+1} reads p, not h
             for p in range(NP) for x in range(NV) for h in range(NH)}
    m_t = cmi_bits(joint, (0,), (1,), (3,))
    i_h = cmi_bits(joint, (0,), (1,), (2,))
    if m_t > i_h + 1e-9:
        bad = (m_t, i_h)
        break
check("M6", bad is not None,
      f"COUNTERCONTROL FOR (c) — THE MARKOV CHAIN IS THE HYPOTHESIS. Let X_(t+1) read the HISTORY "
      f"directly instead of only through the hidden state, and data processing fails: "
      f"M_t = {bad[0]:.4f} bits exceeds I(X_<t; H_t | X_t) = {bad[1]:.4f} bits. The chain "
      f"X_<t -> H_t -> X_(t+1) given X_t is not a modelling convenience — it is what a FAITHFUL "
      f"DETERMINISTIC realization supplies, and clause (c) is false without it")

# ---------------------------------------------------------------- M7  the Shannon layer itself
ok7 = True
for _ in range(400):
    n = rng.choice([2, 3, 4])
    p = [rng.random() for _ in range(n)]; sp = sum(p); p = [x / sp for x in p]
    q = [rng.random() + 1e-3 for _ in range(n)]; sq2 = sum(q); q = [x / sq2 for x in q]
    # Gibbs
    ok7 &= sum(a * math.log(b) for a, b in zip(p, q)) <= \
        sum(a * math.log(a) for a in p if a > 0) + 1e-12
    # the uniform bound
    ok7 &= entropy_nats(p) <= math.log(n) + 1e-12
for _ in range(200):
    w = rand_law(); phi = rand_bijection()
    joint = {(p, x, h, next_vis(phi, x, h)): w[(p, x, h)]
             for p in range(NP) for x in range(NV) for h in range(NH)}
    ok7 &= cmi_bits(joint, (0,), (1,), (2,)) >= -1e-12
check("M7", ok7,
      "THE FINITE SHANNON LAYER, checked against the definitions the Lean file uses rather than "
      "assumed. Gibbs' inequality holds on 400 random distribution pairs; entropy never exceeds "
      "the log of the alphabet size; and conditional mutual information is nonnegative on 200 "
      "random realizations. Mathlib supplies none of this, which is why the layer exists")

# ---------------------------------------------------------------- M8  lint
mem = open(os.path.join(BRIDGE, 'OIBridge', 'HiddenMemory.lean'), encoding='utf-8').read()
ent = open(os.path.join(BRIDGE, 'OIBridge', 'FiniteEntropy.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
MEM_THMS = ('pushforward_identity', 'distinguishability_floor', 'capacity_floor',
            'unavoidable_hidden_predictive_memory')
ENT_THMS = ('sum_mul_log_le', 'entropy_le_log_card', 'cmi3_nonneg', 'cmi_le_of_deterministic',
            'cmi_le_log_card')
nosorry = lambda t: re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])',
                              re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', t, flags=re.S))) is None
ok8 = ('import OIBridge.HiddenMemory' in root and 'import OIBridge.FiniteEntropy' in root
       and nosorry(mem) and nosorry(ent)
       and all(f'theorem {t}' in mem for t in MEM_THMS)
       and all(f'theorem {t}' in ent for t in ENT_THMS)
       and all(f'#print axioms {t}' in mem for t in MEM_THMS)
       and all(f'#print axioms {t}' in ent for t in ENT_THMS)
       # the next visible value must be DEFINED from the bijection, not assumed to be a function
       and 'def nextVis' in mem and '(R.step (x, h)).1' in mem)
check("M8", ok8,
      f"both Lean files are IMPORTED BY OIBridge.lean, so CI builds them and the theorems are "
      f"gated rather than merely present; neither carries a `sorry`; all {len(MEM_THMS)} theorems "
      f"of the memory file and all {len(ENT_THMS)} of the Shannon layer are present and print "
      f"their axiom dependencies; and the next visible value is DEFINED as the visible component "
      f"of the bijection rather than assumed to be a function of the pair — which is what makes "
      f"the Markov chain of clause (c) a consequence rather than a hypothesis")

print()
print('     [scope] Settled: [Main] §3.4\'s unavoidable-hidden-predictive-memory theorem is')
print('     kernel-proved in ALL THREE CLAUSES — the pushforward identity, the distinguishability')
print('     floor, and the capacity floor M_t <= I(X_<t; H_t | X_t) <= log2|C_H|. The third')
print('     required building finite Shannon entropy, conditional mutual information and the')
print('     data-processing inequality, none of which Mathlib carries.')
print('     Each clause has a countercontrol removing exactly the hypothesis its proof consumes:')
print('     a stochastic channel breaks (a), a non-TV distance breaks (b), and reading the')
print('     history directly rather than through the hidden state breaks (c).')
print('     NOT settled here: the theorem is UNIVERSAL over realizations, and it is deliberately')
print('     SEPARATE from the S <=> D <=> Q equivalence rather than a lemma of it — the')
print('     equivalence is existential and holds for Markov laws too, which is exactly why it')
print('     cannot do this theorem\'s work. The variational identity M_det = M_t remains OPEN and')
print('     is FALSE in its fixed-hidden-dimension reading (memory_probes.py).')
print()
print("hidden_memory_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
