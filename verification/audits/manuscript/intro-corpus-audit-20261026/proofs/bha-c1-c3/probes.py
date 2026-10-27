#!/usr/bin/env python3
"""Reviewer probes beyond the BH-01 checked domains (own code; nothing imported from checks.py)."""
import itertools
import random
from collections import defaultdict
from fractions import Fraction as Fr

rng = random.Random(20261027)


def digits(x, sizes):
    d = []
    for q in sizes:
        d.append(x % q)
        x //= q
    return tuple(d)


def psucc_general(weights_by_m, rec_of):
    """weights_by_m: {m: {x0: weight}} (joint P(m, x0)); rec_of(x0) -> record. Bayes success."""
    joint = defaultdict(lambda: defaultdict(Fr))
    for m, wx in weights_by_m.items():
        for x0, w in wx.items():
            joint[rec_of(x0)][m] += w
    return sum(max(v.values()) for v in joint.values())


# ---------------------------------------------------------------- Probe 1
# C2 under conditions outside the checked domain: mixed alphabets (2,3,4,5), time-inhomogeneous
# random bijections, T up to 4, arbitrary read schedules (cumulative), NON-uniform message prior,
# NON-uniform and message-DEPENDENT hidden distributions, blank registers. Bound: P_succ >= 1/|K|.
viol = 0
trials = 0
min_ratio = None
for trial in range(4000):
    r = rng.randint(2, 4)
    sizes = [rng.choice([2, 3, 4, 5]) for _ in range(r)]
    n = 1
    for q in sizes:
        n *= q
    if n > 400:
        continue
    T = rng.randint(1, 4)
    maps = []
    for _ in range(T):
        p = list(range(n))
        rng.shuffle(p)
        maps.append(p)
    nmsg = rng.randint(1, r - 1)
    msg_regs = rng.sample(range(r), nmsg)
    others = [j for j in range(r) if j not in msg_regs]
    kinds = {j: rng.choice(["blank", "hidden"]) for j in others}
    msgs = list(itertools.product(*[range(sizes[j]) for j in msg_regs]))
    pm = [Fr(rng.randint(1, 9)) for _ in msgs]
    s = sum(pm)
    pm = [x / s for x in pm]
    weights = {}
    for mi, m in enumerate(msgs):
        wx = {}
        hid = [j for j in others if kinds[j] == "hidden"]
        cfgs = list(itertools.product(*[range(sizes[j]) for j in hid]))
        hw = [Fr(rng.randint(0, 5)) for _ in cfgs]  # message-dependent, possibly zero weights
        if sum(hw) == 0:
            hw[0] = Fr(1)
        hs = sum(hw)
        for c, w in zip(cfgs, hw):
            if w == 0:
                continue
            d = [0] * r
            for j, v in zip(msg_regs, m):
                d[j] = v
            for j, v in zip(hid, c):
                d[j] = v
            x = 0
            mul = 1
            for j in range(r):
                x += d[j] * mul
                mul *= sizes[j]
            wx[x] = pm[mi] * w / hs
        weights[mi] = wx
    sched = [set(rng.sample(range(r), rng.randint(0, r))) for _ in range(T)]
    endpoint = set(rng.sample(range(r), rng.randint(0, r)))
    sched.append(endpoint)
    sched[0] = set(j for j in sched[0] if j not in msg_regs)
    K = 1
    for j in range(r):
        if j not in endpoint:
            K *= sizes[j]

    def rec_of(x0):
        x = x0
        out = [tuple(digits(x, sizes)[j] for j in sorted(sched[0]))]
        for t in range(T):
            x = maps[t][x]
            out.append(tuple(digits(x, sizes)[j] for j in sorted(sched[t + 1])))
        return tuple(out)

    ps = psucc_general(weights, rec_of)
    trials += 1
    if ps < Fr(1, K):
        viol += 1
    ratio = ps * K
    if min_ratio is None or ratio < min_ratio:
        min_ratio = ratio
print("Probe 1 (C2, general priors/alphabets/schedules): trials", trials, "violations", viol,
      "min P_succ*|K|", min_ratio)

# ---------------------------------------------------------------- Probe 2
# Corollary 'zero advantage requires |K| >= |M|' with a coarse-grained (unequal-support) message.
# X = {0,1}^2, registers a (read) and k (unread), identity dynamics, uniform over X.
# message m(x): m=0 on (a,k) in {(0,0),(1,0)}, m=1 on (0,1), m=2 on (1,1). |M| = 3, |K| = 2.
w = {0: {}, 1: {}, 2: {}}
for a in (0, 1):
    for k in (0, 1):
        m = 0 if k == 0 else 1 + a
        w[m][(a, k)] = Fr(1, 4)
ps = psucc_general(w, lambda x0: x0[0])
pmax = max(sum(v.values()) for v in w.values())
print("Probe 2 (coarse message, identity bijection): |M|=3 |K|=2 P_succ =", ps, " blind (max prior) =", pmax,
      " zero advantage:", ps == pmax)

# ---------------------------------------------------------------- Probe 2b
# Equal-size supports with non-uniform message prior: exhaustive over S_6 on Z3 x Z2,
# message = ternary register (prior 1/2,1/4,1/4), hidden bit uniform, read ternary register at t=1.
cnt_zero = 0
for p in itertools.permutations(range(6)):
    wt = {m: {(m + 3 * h): Fr([2, 1, 1][m], 4) / 2 for h in (0, 1)} for m in range(3)}
    ps = psucc_general(wt, lambda x0: p[x0] % 3)
    if ps == Fr(1, 2):
        cnt_zero += 1
print("Probe 2b (equal supports, prior 1/2,1/4,1/4, |K|=2): bijections of S_6 with zero advantage:", cnt_zero)

# ---------------------------------------------------------------- Probe 3
# 'A single B-D coupling step defeats recovery': registers V(0) blank, B(1) message, D(2) hidden.
# step 1 = a coupling between B and D; step 2 = emission swap V<->B; W = {V,B} read at t=2.
def run_two_step(step1):
    swapVB = lambda d: (d[1], d[0], d[2])
    dists = []
    for m in (0, 1):
        recs = defaultdict(int)
        for dd in (0, 1):
            x0 = (0, m, dd)
            x1 = step1(x0)
            x2 = swapVB(x1)
            recs[((x1[0],), (x2[0], x2[1]))] += 1
        dists.append(recs)
    keys = set(dists[0]) | set(dists[1])
    return Fr(sum(abs(dists[0].get(k, 0) - dists[1].get(k, 0)) for k in keys), 4)


couplings = {
    "swap B<->D (package's leak)": lambda d: (d[0], d[2], d[1]),
    "D ^= B (CNOT B->D)": lambda d: (d[0], d[1], d[2] ^ d[1]),
    "B ^= D (CNOT D->B)": lambda d: (d[0], d[1] ^ d[2], d[2]),
    "identity (no coupling)": lambda d: d,
}
for name, f in couplings.items():
    print("Probe 3: %-28s TV with all of W read = %s" % (name, run_two_step(f)))
# count all 24 bijections of the (B,D) pair as single coupling steps (V untouched)
pair_perms = list(itertools.permutations(range(4)))
res = defaultdict(int)
for pp in pair_perms:
    def f(d, pp=pp):
        y = pp[d[1] + 2 * d[2]]
        return (d[0], y & 1, y >> 1)
    res[run_two_step(f)] += 1
print("Probe 3b: over all 24 bijections of (B,D) as the coupling step, TV histogram:",
      {str(k): v for k, v in sorted(res.items())})

# ---------------------------------------------------------------- Probe 4
# Tightness of C2 when |K| does not divide |I|: ternary message register (read at the end? no:
# message register written, blank binary register), X = Z3 x Z2, N = 1, endpoint reads the
# ternary register, K = the binary register (|K| = 2 < |M| = 3). Exhaustive min P_succ over S_6.
mn = None
for p in itertools.permutations(range(6)):
    wt = {m: {m: Fr(1, 3)} for m in range(3)}  # x0 = m + 3*0 (blank = 0)
    ps = psucc_general(wt, lambda x0: p[x0] % 3)
    mn = ps if mn is None or ps < mn else mn
print("Probe 4 (|K|=2, |M|=3, N=1, blank register): min P_succ over S_6 =", mn, "(bound 1/|K| = 1/2)")
# same with a uniform hidden bit (N = 2): bound attained?
mn = None
for p in itertools.permutations(range(6)):
    wt = {m: {m + 3 * h: Fr(1, 6) for h in (0, 1)} for m in range(3)}
    ps = psucc_general(wt, lambda x0: p[x0] % 3)
    mn = ps if mn is None or ps < mn else mn
print("Probe 4b (same, hidden bit, N=2): min P_succ over S_6 =", mn)

# ---------------------------------------------------------------- Probe 5
# Existence direction 'zero-advantage bijections exist whenever |K| >= |M|' (MANUSCRIPT-AUDIT ch07 L12):
# X = Z2 (message register, read at the end) x Z3 (hidden uniform, unread), |M| = 2, |K| = 3 >= |M|.
# Endpoint snapshot reads register 0 (Z2); exhaustive over all 720 bijections, also with cumulative
# t=1 snapshot only (T = 1). Index x = a + 2*k.
from collections import Counter
hist = Counter()
for p in itertools.permutations(range(6)):
    d = [Counter(p[m + 2 * k] % 2 for k in range(3)) for m in (0, 1)]
    tvv = Fr(sum(abs(d[0][y] - d[1][y]) for y in (0, 1)), 6)
    hist[tvv] += 1
print("Probe 5 (|M|=2, |K|=3, read Z2 register): TV histogram over S_6:", {str(k): v for k, v in sorted(hist.items())})

# ---------------------------------------------------------------- Probe 6
# Corollary under a UNIFORM message prior but unequal supports and arbitrary weights:
# random coarse messages (functions of x0) on random product spaces, identity-free random bijections,
# endpoint read set with |K| < |M|; zero advantage must never occur.
hits = 0
tested = 0
for trial in range(3000):
    sizes = [rng.choice([2, 3]) for _ in range(rng.randint(2, 4))]
    n = 1
    for q in sizes:
        n *= q
    p = list(range(n)); rng.shuffle(p)
    r = len(sizes)
    read = set(rng.sample(range(r), rng.randint(1, r - 1)))
    K = 1
    for j in range(r):
        if j not in read:
            K *= sizes[j]
    M = rng.randint(K + 1, min(n, K + 4)) if K + 1 <= n else None
    if M is None:
        continue
    lab = [rng.randrange(M) for _ in range(n)]
    for i in range(M):
        lab[i] = i  # every message has support
    wts = [Fr(rng.randint(1, 5)) for _ in range(n)]
    weights = {m: {} for m in range(M)}
    for m in range(M):
        pts = [x for x in range(n) if lab[x] == m]
        s = sum(wts[x] for x in pts)
        for x in pts:
            weights[m][x] = Fr(1, M) * wts[x] / s
    ps = psucc_general(weights, lambda x0: tuple(digits(p[x0], sizes)[j] for j in sorted(read)))
    tested += 1
    if ps == Fr(1, M):
        hits += 1
print("Probe 6 (uniform message prior, unequal supports, |K| < |M|): tested", tested, "zero-advantage hits", hits)
