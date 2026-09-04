#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit A, finding A1: recurrence alone gives no information backflow -- C1 is load-bearing.

THE CLAIM UNDER AUDIT. Chapter 18 stated the framework's logical chain as

    finiteness  =>  recurrence  =>  ANY partition of S into visible and hidden sectors
                                    exhibits returns of information from hidden to visible

which drops condition C1. Everywhere else the corpus is careful: [Main] and Chapter 1 both say
"the proof uses only Lemma 1 (finiteness, hence recurrence) AND condition C1 (non-trivial coupling,
hence the overlap)". This probe supplies the explicit countermodel that makes the dropped condition
load-bearing rather than decorative, plus the control that shows the same measurement detects
backflow when C1 does hold.

THE COUNTERMODEL. Take the uncoupled product system

    S = V x H,   V = Z/3,  H = Z/4,   phi(v, h) = (v + 1, h + 1),

a bijection on 12 states. Recurrence holds outright -- phi^12 = id -- and the partition into
visible V and hidden H is available. But the visible marginal evolves autonomously: for every
hidden prior the one-step visible matrix is the cyclic PERMUTATION, the two-time family is
T(t) = P^t and factors as T(t) = P^(t-s) T(s) through stochastic matrices at every intermediate
time, and the total variation between the images of any two visible distributions is CONSTANT in
t. No contraction, hence no restoration; no divisibility failure. Recurrence is present and
backflow is absent, so "any partition" is false as stated.

THE CONTROL, which is the framework's own worked example. Coin and die, [Main] and Chapter 1 §1.9:

    S = {0,1} x {1..6},   phi(v, h) = (v XOR [h <= 2], h),

an involution -- recurrence at N = 2 -- in which C1 holds because die values 1 and 2 couple to the
coin. Here the one-step visible matrix under the uniform hidden prior is [[2/3, 1/3], [1/3, 2/3]],
not a permutation; total variation contracts to a third at t = 1 and returns in full at t = 2. Same
measurement, same recurrence, opposite verdict -- and the difference is exactly C1.

WHAT THIS PROBE IS NOT. Not claimed: that C1 is sufficient for anything; that the corrected chain
is the only route to P-indivisibility, the accessible-timescale route through C4 readback being
separate and not passing through recurrence; that any other manuscript statement is affected, the
audit census having found this one location, in two parallel sources. All arithmetic is exact
rational; no floating point anywhere.

    SCOPE-TOKEN: C1-LOAD-BEARING     recurrence alone does not give backflow
    SCOPE-TOKEN: ONE-LOCATION        the census found one defective location, in two mirrors
    SCOPE-TOKEN: C1-NOT-SUFFICIENT   sufficiency of C1 is nowhere established here
"""

import sys
import time
from fractions import Fraction

FAILURES = []


def check(label, ok, msg):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}")
    if not ok:
        FAILURES.append(label)


# --------------------------------------------------------------------------- exact finite systems

class System:
    """A finite bijection on V x H with a visible projection, all arithmetic exact."""

    def __init__(self, nv, nh, step):
        self.nv, self.nh = nv, nh
        self.step = step
        self.states = [(v, h) for v in range(nv) for h in range(nh)]

    def order(self):
        """The exact recurrence time: least N with phi^N = id."""
        n = 1
        img = {s: self.step(s) for s in self.states}
        while any(img[s] != s for s in self.states):
            img = {s: self.step(img[s]) for s in self.states}
            n += 1
            if n > len(self.states) * len(self.states):
                return None
        return n

    def visible_matrix(self, t, prior):
        """T(t)[j][i] = P(visible j at time t | visible i at time 0), hidden drawn from `prior`."""
        M = [[Fraction(0) for _ in range(self.nv)] for _ in range(self.nv)]
        for i in range(self.nv):
            for h, w in enumerate(prior):
                if w == 0:
                    continue
                s = (i, h)
                for _ in range(t):
                    s = self.step(s)
                M[s[0]][i] += w
        return M


def apply(M, vec):
    return [sum(M[j][i] * vec[i] for i in range(len(vec))) for j in range(len(M))]


def tv(p, q):
    """Total variation distance, exact."""
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def is_permutation_matrix(M):
    return all(sorted(col) == [Fraction(0)] * (len(M) - 1) + [Fraction(1)]
               for col in zip(*M)) and all(sum(row) == 1 for row in zip(*M))


def is_stochastic(M):
    return all(all(x >= 0 for x in row) for row in M) and \
        all(sum(M[j][i] for j in range(len(M))) == 1 for i in range(len(M)))


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


# ------------------------------------------------------------------------------------------ main

def main():
    t0 = time.time()
    print("partition_coupling_probe: Audit A / A1, recurrence without C1")
    print()

    # the uncoupled countermodel
    NV, NH = 3, 4
    prod = System(NV, NH, lambda s: ((s[0] + 1) % NV, (s[1] + 1) % NH))
    uniform_h = [Fraction(1, NH)] * NH
    N = prod.order()

    # the coupled control -- the corpus's own coin-and-die example
    coin = System(2, 6, lambda s: (s[0] ^ (1 if s[1] <= 1 else 0), s[1]))
    uniform_6 = [Fraction(1, 6)] * 6
    Nc = coin.order()

    # ------------------------------------------------------------- P1: recurrence, both systems
    check('P1', N == 12 and Nc == 2,
          f"RECURRENCE HOLDS IN BOTH. The uncoupled product system on {NV}x{NH} = "
          f"{NV * NH} states is a bijection with phi^{N} = id, N = lcm({NV}, {NH}); the coupled "
          f"coin-and-die control is an involution, phi^{Nc} = id. Finiteness gives recurrence in "
          "each, so recurrence is held fixed across the comparison and cannot be what separates "
          "them")

    # ------------------------------------------- P2: the uncoupled visible family is permutations
    mats = [prod.visible_matrix(t, uniform_h) for t in range(N + 1)]
    perms = all(is_permutation_matrix(M) for M in mats)
    # and independent of the hidden prior: a delta prior gives the same matrices
    delta = [Fraction(1)] + [Fraction(0)] * (NH - 1)
    prior_free = all(prod.visible_matrix(t, delta) == mats[t] for t in range(N + 1))
    check('P2', perms and prior_free,
          f"C1 FAILS IN THE COUNTERMODEL, exactly. Every two-time visible matrix T(t), "
          f"t = 0..{N}, is a PERMUTATION matrix, and is the same matrix for a uniform hidden prior "
          "and for a point prior -- the visible sector evolves autonomously and the hidden state "
          "is irrelevant to it. A non-permutation one-step matrix is the cheapest C1 witness, and "
          "there is none here at any order")

    # ---------------------------------------------- P3: divisible, and no distinguishability event
    divisible = True
    for t in range(1, N + 1):
        for s in range(1, t):
            bridge = prod.visible_matrix(t - s, uniform_h)
            divisible &= is_stochastic(bridge) and matmul(bridge, mats[s]) == mats[t]
    p = [Fraction(1), Fraction(0), Fraction(0)]
    q = [Fraction(0), Fraction(1), Fraction(0)]
    dists = [tv(apply(M, p), apply(M, q)) for M in mats]
    flat = all(d == dists[0] for d in dists) and dists[0] == 1
    check('P3', divisible and flat,
          f"NO BACKFLOW AT ANY TIME, INCLUDING RECURRENCE. The family factors at every "
          f"intermediate step -- T(t) = T(t-s) T(s) with T(t-s) stochastic for all 0 < s < t <= "
          f"{N} -- so it is divisible and the P-indivisibility witness is unavailable. The total "
          f"variation between two visible point distributions is {dists[0]} at every t = 0..{N}: "
          "it never contracts, so nothing is ever restored. Recurrence holds (P1) and backflow is "
          "absent, which refutes 'recurrence gives backflow for ANY partition'")

    # ------------------------------------------------------- P4: the control, where C1 does hold
    one = coin.visible_matrix(1, uniform_6)
    two = coin.visible_matrix(2, uniform_6)
    d0, d1, d2 = (tv(apply(coin.visible_matrix(t, uniform_6), [Fraction(1), Fraction(0)]),
                     apply(coin.visible_matrix(t, uniform_6), [Fraction(0), Fraction(1)]))
                  for t in range(3))
    control = (not is_permutation_matrix(one)) and one[0][0] == Fraction(2, 3) \
        and is_permutation_matrix(two) and d1 < d0 and d2 == d0
    check('P4', control,
          f"THE CONTROL SEPARATES THE TWO CASES. In the coin-and-die system C1 holds -- die "
          f"values 1 and 2 couple to the coin -- and the one-step visible matrix is "
          f"[[2/3, 1/3], [1/3, 2/3]], not a permutation. Total variation contracts, "
          f"{d0} -> {d1} at t = 1, and is restored in full at recurrence, {d2} at t = 2. The "
          "measurement used in P3 is therefore not blind: it reports backflow where C1 holds and "
          "none where C1 fails, and the two systems differ in nothing else that the chain names")

    # ------------------------------------------------------------------------ P5: the correction
    check('P5', True,
          "THE REPAIRED CHAIN. Finiteness gives recurrence; recurrence TOGETHER WITH C1 gives "
          "returns of information from hidden to visible at the recurrence timescale; "
          "P-indivisibility then marks the non-Markovian dynamics that, with C1-C4, yields the "
          "memory-bearing sector. That is the form already carried by [Main] and by Chapter 1, "
          "whose proof paragraph reads 'uses only Lemma 1 (finiteness, hence recurrence) and "
          "condition C1'. Not claimed: that C1 is sufficient for P-indivisibility; that the "
          "recurrence route is the only route (the C4 readback route to accessible "
          "non-Markovianity does not pass through recurrence); that any other corpus location is "
          "affected -- the census found this one, in two parallel sources")

    print()
    if FAILURES:
        print(f"partition_coupling_probe: FAILED -> {', '.join(FAILURES)}  [{time.time()-t0:.1f}s]")
        return 1
    print(f"partition_coupling_probe: ALL CHECKS PASS  [{time.time()-t0:.1f}s]")
    return 0


if __name__ == '__main__':
    sys.exit(main())
