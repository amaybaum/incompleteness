#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/C3Necessity.lean.

[Main]'s C3-necessity theorem — I(X_<t ; X_>t | X_t) <= log2 m — and its per-process capacity
corollary m >= 2^(I*) are kernel-proved there, as instances of the hidden-memory layer's
`capacity_floor_of_fun` rather than as a second data-processing argument. This file is the
independent executable layer, and its controls are aimed at the two ways C3 gets misread.

  THE HYPOTHESIS is that X_>t is a FUNCTION of (X_t, H_t) — determinism, which is what makes
      X_<t -> H_t -> X_>t a Markov chain given X_t. C1 removes it: a future that reads the visible
      history directly, past the hidden state, blows the bound.

  THE TWO MISREADINGS are both denied in the manuscript, and both get a control.
      C5: C3 is NOT m >= n. A two-hidden-state, three-visible-state bijection with full
          distinguishability revival has m = 2 < n = 3 and satisfies the bound comfortably.
      C6: sustained backflow does NOT force m >~ 2^(K I_0). That reading needs per-event
          contributions to accumulate without hidden-state reuse, which P-indivisibility does not
          supply; C6 exhibits a realization where K events each carry backflow I_0 > 0 and the
          accumulated K*I_0 exceeds log2 m, while the true per-process bound holds throughout.

  C1  the theorem, at horizons L = 1..4, over an exhaustive family of small realizations.
  C2  COUNTERCONTROL: break the Markov chain and the bound fails.
  C3  the manuscript's full chain, in order: the one-step memory M_t, the future information, the
      hidden information, and log2 m — each below the next, with the future term monotone in L.
  C4  I* over a finite family of slices sharing a hidden alphabet, and the corollary m >= 2^(I*).
  C5  COUNTERCONTROL: m = 2 < n = 3 with full distinguishability revival. C3 is not a visible count.
  C6  COUNTERCONTROL: K events of backflow I_0 with K*I_0 > log2 m, under hidden-state reuse.
  C7  the bound is TIGHT and therefore not vacuous: a realization attaining I = log2 m exactly.
  C8  lint: the Lean file is imported by the gated bridge root, carries no sorry, derives C3 from
      `capacity_floor_of_fun` rather than reproving data processing, and records what it does not
      prove.

Usage:  python3 c3_necessity_probe.py
"""
import itertools
import math
import os
import random
import re
import sys
from fractions import Fraction as F

CHECKS = []
TOL = 1e-12


def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.join(HERE, os.pardir, 'lean-mathlib')
rng = random.Random(3172)

LOG2 = math.log(2.0)


# ----------------------------------------------------------------- information
def entropy_nats(weights):
    tot = float(sum(weights))
    h = 0.0
    for w in weights:
        w = float(w)
        if w > 0:
            h -= w * math.log(w / tot)
    return h


def marg_entropy(joint, keys):
    """H of the pushforward of `joint` onto the coordinates in `keys`."""
    acc = {}
    for s, w in joint.items():
        k = tuple(s[i] for i in keys)
        acc[k] = acc.get(k, F(0)) + w
    return entropy_nats(list(acc.values()))


def cmi_bits(joint, A, B, C):
    """I(A ; C | B) = H(A,B) + H(B,C) - H(A,B,C) - H(B), in bits."""
    return (marg_entropy(joint, A + B) + marg_entropy(joint, B + C)
            - marg_entropy(joint, A + B + C) - marg_entropy(joint, B)) / LOG2


# ----------------------------------------------------------------- realizations
def random_bijection(nv, nh):
    states = [(x, h) for x in range(nv) for h in range(nh)]
    img = states[:]
    rng.shuffle(img)
    return dict(zip(states, img))


def random_law(npast, nv, nh):
    raw = {(p, x, h): F(rng.randint(0, 4))
           for p in range(npast) for x in range(nv) for h in range(nh)}
    tot = sum(raw.values())
    if tot == 0:
        raw[(0, 0, 0)] = F(1)
        tot = F(1)
    return {k: v / tot for k, v in raw.items()}


def future_of(phi, q, L):
    """`futureOf`: the visible future, L steps, obtained by ITERATING the bijection from (x, h)."""
    out, cur = [], q
    for _ in range(L):
        cur = phi[cur]
        out.append(cur[0])
    return tuple(out)


def sample_space(w, phi, L):
    """The joint law of (X_<t, X_t, H_t, X_>t) with the future DEFINED from the bijection.

    Coordinates: 0 = history, 1 = X_t, 2 = H_t, 3 = X_>t at horizon L."""
    joint = {}
    for (p, x, h), val in w.items():
        key = (p, x, h, future_of(phi, (x, h), L))
        joint[key] = joint.get(key, F(0)) + val
    return joint


# ----------------------------------------------------------------- C1  the theorem
ok1 = True
worst1 = 0.0
n1 = 0
for nv, nh, npast in ((2, 2, 2), (2, 3, 2), (3, 2, 3), (3, 3, 2)):
    bound = math.log2(nh)
    for _ in range(30):
        phi = random_bijection(nv, nh)
        w = random_law(npast, nv, nh)
        for L in (1, 2, 3, 4):
            j = sample_space(w, phi, L)
            val = cmi_bits(j, (0,), (1,), (3,))
            ok1 &= val <= bound + TOL
            ok1 &= val >= -TOL
            worst1 = max(worst1, val - bound)
            n1 += 1
check("C1", ok1,
      f"THE THEOREM. I(X_<t ; X_>t | X_t) <= log2 m on {n1} (realization, horizon) pairs across "
      f"four alphabet shapes and horizons L = 1..4, with the future DEFINED by iterating the "
      f"bijection rather than posited to be a function of the pair. Worst excess over the bound: "
      f"{worst1:.2e}. The quantity is also nonnegative throughout, as conditional mutual "
      f"information must be")

# ----------------------------------------------------------------- C2  countercontrol
# break the Markov chain: let the "future" read the visible history directly, past the hidden state
ok2 = False
best2 = 0.0
for _ in range(200):
    nv, nh, npast = 2, 2, 4
    phi = random_bijection(nv, nh)
    w = random_law(npast, nv, nh)
    broken = {}
    for (p, x, h), val in w.items():
        broken[(p, x, h, p)] = broken.get((p, x, h, p), F(0)) + val   # future = the history itself
    val = cmi_bits(broken, (0,), (1,), (3,))
    best2 = max(best2, val)
    if val > math.log2(nh) + 1e-9:
        ok2 = True
check("C2", ok2,
      f"COUNTERCONTROL for the MARKOV HYPOTHESIS. Replace the future by one that reads the visible "
      f"history directly rather than through (X_t, H_t) — exactly the dependence determinism "
      f"forbids — and I(X_<t ; X_>t | X_t) reaches {best2:.4f} bits against a bound of "
      f"{math.log2(2):.4f}. The bound is therefore a consequence of the functional dependence and "
      f"not an identity; `capacity_floor_of_fun` consumes that dependence in its very signature, "
      f"where the readout is a function of the pair")

# ----------------------------------------------------------------- C3  the manuscript's chain
ok3 = True
n3 = 0
tight_gap = 1.0
for nv, nh, npast in ((2, 2, 3), (3, 2, 3), (2, 3, 3)):
    bound = math.log2(nh)
    for _ in range(40):
        phi = random_bijection(nv, nh)
        w = random_law(npast, nv, nh)
        hid = {(p, x, h, h): v for (p, x, h), v in w.items()}
        i_hidden = cmi_bits(hid, (0,), (1,), (3,))
        prev = None
        for L in (1, 2, 3, 4, 5):
            j = sample_space(w, phi, L)
            val = cmi_bits(j, (0,), (1,), (3,))
            if prev is not None:
                ok3 &= val >= prev - TOL          # monotone in the horizon
            prev = val
            ok3 &= val <= i_hidden + TOL          # data processing
            n3 += 1
        ok3 &= i_hidden <= bound + TOL            # the alphabet bound
        # M_t, the one-step memory clause, is the L = 1 term of the same chain
        one = cmi_bits(sample_space(w, phi, 1), (0,), (1,), (3,))
        ok3 &= one <= prev + TOL
check("C3", ok3,
      f"THE MANUSCRIPT'S CHAIN, in order and end to end on {n3} slices: the one-step memory M_t is "
      f"the L = 1 term of the future information; the future information is nondecreasing in the "
      f"horizon; it never exceeds I(X_<t ; H_t | X_t); and that never exceeds log2 m. This is the "
      f"same order the Lean file proves, and it is why `capacity_floor` and `c3_necessity` are two "
      f"instances of one lemma rather than two proofs")

# ----------------------------------------------------------------- C4  I* and the corollary
ok4 = True
n4 = 0
for nv, nh, npast in ((2, 2, 3), (3, 2, 2), (2, 3, 3)):
    for _ in range(25):
        phi = random_bijection(nv, nh)                # ONE hidden sector, several slices
        slices = [(random_law(npast, nv, nh), rng.choice([1, 2, 3, 4])) for _ in range(5)]
        istar = max(cmi_bits(sample_space(w, phi, L), (0,), (1,), (3,)) for w, L in slices)
        ok4 &= istar <= math.log2(nh) + TOL
        ok4 &= 2.0 ** istar <= nh + 1e-9             # the corollary, m >= 2^(I*)
        n4 += 1
check("C4", ok4,
      f"I* AND THE COROLLARY on {n4} processes, each a family of five accessible slices sharing "
      f"ONE hidden alphabet and one bijection — which is what makes m >= 2^(I*) a statement about a "
      f"single hidden sector rather than about unrelated ones. The maximum over slices and horizons "
      f"obeys the same bound as each slice, and 2^(I*) <= m throughout")

# ----------------------------------------------------------------- C5  countercontrol: not m >= n
# the manuscript's own counterexample: m = 2 < n = 3 with full distinguishability revival
NV5, NH5 = 3, 2
found5 = None
states5 = [(x, h) for x in range(NV5) for h in range(NH5)]
for img in itertools.permutations(states5):
    phi = dict(zip(states5, img))
    # two hidden posteriors over H, conditioned on two different visible histories at the same x
    for x in range(NV5):
        mu = {0: F(1), 1: F(0)}
        nu = {0: F(0), 1: F(1)}

        def fut_law(post, L):
            out = {}
            for h, p in post.items():
                if p == 0:
                    continue
                key = future_of(phi, (x, h), L)
                out[key] = out.get(key, F(0)) + p
            return out

        def tv(a, b):
            keys = set(a) | set(b)
            return sum(abs(a.get(k, F(0)) - b.get(k, F(0))) for k in keys) / 2

        if tv(fut_law(mu, 1), fut_law(nu, 1)) == 0 and tv(fut_law(mu, 2), fut_law(nu, 2)) > 0:
            found5 = (phi, x)
            break
    if found5:
        break
ok5 = found5 is not None
if ok5:
    phi5, x5 = found5
    # and the C3 bound still holds on this system, with m = 2 < n = 3
    worst5 = 0.0
    for _ in range(40):
        w = random_law(3, NV5, NH5)
        for L in (1, 2, 3, 4):
            worst5 = max(worst5, cmi_bits(sample_space(w, phi5, L), (0,), (1,), (3,)))
    ok5 &= worst5 <= math.log2(NH5) + TOL
check("C5", ok5,
      f"COUNTERCONTROL: C3 IS NOT m >= n. A three-visible-state, two-hidden-state bijection with "
      f"FULL DISTINGUISHABILITY REVIVAL — two hidden posteriors whose one-step futures coincide "
      f"exactly and whose two-step futures differ — exists, so m = {NH5} < n = {NV5} is compatible "
      f"with genuine backflow. The C3 bound holds on it at every horizon (worst observed "
      f"{worst5:.4f} bits against log2 m = {math.log2(NH5):.4f}), which is the point: the necessity "
      f"content is capacity for the OBSERVED backflow, not a bound set by the visible count")

# ----------------------------------------------------------------- C6  countercontrol: no accumulation
# a one-bit hidden sector REUSED at every event: phi(x, h) = (h, x), so the next visible value is
# the hidden bit and the same bit carries backflow at every slice
PHI6 = {(0, 0): (0, 0), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (1, 1)}
assert len(set(PHI6.values())) == 4
assert all(PHI6[(x, h)] == (h, x) for x in range(2) for h in range(2))
K6 = 4
slice6 = None
for _ in range(4000):
    w = random_law(2, 2, 2)
    i0 = cmi_bits(sample_space(w, PHI6, 1), (0,), (1,), (3,))
    if K6 * i0 > 1.0 + 1e-6 and i0 < 1.0 - 1e-6:
        slice6 = (w, i0)
        break
ok6 = slice6 is not None
if ok6:
    w6, i0 = slice6
    # K slices of ONE process: the same bijection, the same one hidden bit, backflow at each
    # I* is the maximum over the K slices and their horizons; the slices share one bijection and
    # one hidden bit, which is the reuse the accumulated reading ignores
    istar6 = max(cmi_bits(sample_space(w6, PHI6, L), (0,), (1,), (3,))
                 for L in (1, 2, 3, 4, 5, 6))
    ok6 &= all(cmi_bits(sample_space(w6, PHI6, L), (0,), (1,), (3,)) > 1e-9 for L in (1, 2, 3, 4))
    ok6 &= K6 * i0 > math.log2(2) + 1e-9          # the accumulated reading overshoots m
    ok6 &= istar6 <= math.log2(2) + TOL           # the per-process bound does not
    ok6 &= 2.0 ** istar6 <= 2 + 1e-9
check("C6", ok6,
      f"COUNTERCONTROL: SUSTAINED BACKFLOW DOES NOT ACCUMULATE. On phi(x, h) = (h, x) — a hidden "
      f"sector of a single bit, REUSED at every event — each of {K6} coupling events carries "
      f"backflow I_0 = {i0:.4f} bits, so the accumulated reading K*I_0 = {K6 * i0:.4f} would demand "
      f"a hidden alphabet of 2^{K6 * i0:.2f} = {2.0 ** (K6 * i0):.2f} states. The true per-process "
      f"quantity is I* = {istar6:.4f} and m = 2 satisfies m >= 2^(I*) = {2.0 ** istar6:.4f}. The "
      f"manuscript says the accumulated form needs per-event contributions to add WITHOUT "
      f"hidden-state reuse, and that P-indivisibility does not supply that hypothesis; nothing in "
      f"the Lean file proves the accumulated form")

# ----------------------------------------------------------------- C7  tightness
# X_<t determines H_t, and the next visible value IS H_t: the bound is attained exactly
PHI7 = {(0, 0): (0, 0), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (1, 1)}
assert len(set(PHI7.values())) == 4
W7 = {(p, x, h): (F(1, 2) if (p == h and x == 0) else F(0))
      for p in range(2) for x in range(2) for h in range(2)}
i7 = cmi_bits(sample_space(W7, PHI7, 1), (0,), (1,), (3,))
ok7 = abs(i7 - math.log2(2)) < 1e-9
ok7 &= abs(2.0 ** i7 - 2) < 1e-9
check("C7", ok7,
      f"TIGHTNESS, so the bound is not vacuous. A realization in which the visible history "
      f"determines the hidden bit and the next visible value reveals it attains "
      f"I(X_<t ; X_>t | X_t) = {i7:.6f} bits against log2 m = {math.log2(2):.6f} — equality — and "
      f"the corollary reads m >= 2^(I*) = {2.0 ** i7:.4f} with m = 2. A theorem that could only be "
      f"satisfied slackly would not be the capacity statement the manuscript claims")

# ----------------------------------------------------------------- C8  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'C3Necessity.lean'), encoding='utf-8').read()
mem = open(os.path.join(BRIDGE, 'OIBridge', 'HiddenMemory.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
NAMES = ('c3_necessity', 'c3_necessity_via_hidden', 'Istar_le_log_card',
         'card_hidden_ge_two_pow_Istar', 'c3_necessity_and_capacity')
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
ok8 = ('import OIBridge.C3Necessity' in root
       and re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
       and re.search(r'(?m)^axiom ', body) is None
       and all(f'theorem {n}' in src for n in NAMES)
       and all(f'#print axioms {n}' in src for n in NAMES))
# C3 must be a COROLLARY of the hidden-memory layer, not a second data-processing argument
ok8 &= 'import OIBridge.HiddenMemory' in src
ok8 &= src.count('capacity_floor_of_fun') >= 2
ok8 &= 'cmi_le_of_deterministic' not in body     # the data-processing step is not repeated here
ok8 &= 'theorem capacity_floor_of_fun' in mem
ok8 &= 'capacity_floor_of_fun R (fun q : V × H => nextVis R q.1 q.2)' in mem
# the future must be DEFINED by iterating the bijection
ok8 &= 'def futureOf' in src and 'R.step^[(j : ℕ) + 1] q' in src
# and the file must record what it does not prove
header = src[:src.index('import ')]
ok8 &= 'WHAT IS NOT PROVED HERE' in header
ok8 &= 'without hidden-state reuse or' in header and 'is NOT claimed' in header
check("C8", ok8,
      f"the Lean file is IMPORTED BY OIBridge.lean, so CI builds it and the theorems are gated; it "
      f"carries no `sorry` and no `axiom`; all {len(NAMES)} named results print their axiom "
      f"dependencies; C3 is derived from `capacity_floor_of_fun` and does NOT reproduce the "
      f"data-processing step, while `capacity_floor` is rewritten as the one-step instance of the "
      f"same lemma — so Lean checks the dependency between the two manuscript theorems; the future "
      f"is DEFINED by iterating the bijection; and the header records both things the manuscript "
      f"denies and this file therefore does not prove")

print()
print('     [scope] Settled: [Main]\'s C3-necessity theorem I(X_<t ; X_>t | X_t) <= log2 m and its')
print('     per-process capacity corollary m >= 2^(I*) are kernel-proved, as INSTANCES of the')
print('     hidden-memory layer\'s capacity_floor_of_fun rather than as a second data-processing')
print('     argument — the one-step memory clause is the same lemma at the one-step readout. I* is')
print('     the maximum over a finite family of accessible slices sharing one hidden alphabet.')
print('     NOT settled here, because the manuscript denies both: C3 is not m >= n (C5 exhibits')
print('     m = 2 < n = 3 with full distinguishability revival), and sustained backflow does not')
print('     force m >~ 2^(K I_0) (C6 exhibits K*I_0 above log2 m under hidden-state reuse). The')
print('     accumulation reading needs an independence hypothesis that P-indivisibility does not')
print('     supply, and it is not proved anywhere in the formal development.')
print()
print("c3_necessity_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
