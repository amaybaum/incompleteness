#!/usr/bin/env python3
"""G3-HOM node 1: real-valued additive conserved quantities of the RD6 rule class.

A real additive quantity on a ring of L sites is E_h(x) = sum_i h(window_i(x)),
with h an arbitrary real function of the two time slices on w consecutive sites.
It is conserved iff E_h(U x) = E_h(x) for every configuration x.  With M the
integer matrix h -> E_h and D = (P_U - I) M, the number of independent
non-constant conserved functions of this form is rank(M) - rank(D) - 1.
Ranks are exact: they are computed by fraction-free (Bareiss) elimination of
the integer Gram matrices M^T M and D^T D, whose rank over Q equals that of M
and D.  No floating point value enters a verdict.

Run:  python3 -I local_conservation_probe.py   (exit status 0 iff every check holds)
"""
import random
import sys
from itertools import product

import numpy as np

RESULTS = []


def check(name, ok):
    RESULTS.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}")


def bareiss_rank(G):
    """Exact rank of an integer matrix (list of lists of Python ints)."""
    A = [list(map(int, row)) for row in G]
    n = len(A)
    m = len(A[0]) if A else 0
    prev, r = 1, 0
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        p = A[r][c]
        row_r = A[r]
        for i in range(r + 1, n):
            row_i = A[i]
            a_ic = row_i[c]
            for j in range(c + 1, m):
                row_i[j] = (p * row_i[j] - a_ic * row_r[j]) // prev
            row_i[c] = 0
        prev = p
        r += 1
        if r == n:
            break
    return r


def exact_rank(M):
    # The Gram product is formed in int64 only when every entry is provably below 2^62;
    # otherwise in Python integers.  Either way G is exact and rank_Q(G) = rank_Q(M).
    bound = int(np.abs(M).max()) ** 2 * M.shape[0] if M.size else 0
    if bound < 2 ** 62:
        G = (M.T @ M).astype(object)
    else:
        G = M.T.astype(object).dot(M.astype(object))
    return bareiss_rank(G.tolist())


def count_conserved(states, step, windows_of, nfeat):
    """Number of independent non-constant additive conserved functions."""
    index = {s: k for k, s in enumerate(states)}
    M = np.zeros((len(states), nfeat), dtype=np.int64)
    for k, s in enumerate(states):
        for f in windows_of(s):
            M[k, f] += 1
    image = np.array([index[step(s)] for s in states])
    D = M[image] - M
    rM, rD = exact_rank(M), exact_rank(D)
    return rM - rD - 1, rM, rD


# ---------------------------------------------------------------- the rule class
def second_order_rule(L, q, alpha=1):
    """RD6 class: (u, v) -> (v, alpha*(v_{i-1}+v_{i+1}) - u) mod q on Z/L."""
    def step(s):
        u, v = s[:L], s[L:]
        nv = tuple((alpha * (v[(i - 1) % L] + v[(i + 1) % L]) - u[i]) % q for i in range(L))
        return v + nv
    return step


def windows_two_slice(L, q, w):
    def wf(s):
        u, v = s[:L], s[L:]
        out = []
        for i in range(L):
            f = 0
            for j in range(w):
                f = f * q * q + u[(i + j) % L] * q + v[(i + j) % L]
            out.append(f)
        return out
    return wf, (q * q) ** w


def probe_rule(L, q, w):
    states = list(product(range(q), repeat=2 * L))
    wf, nfeat = windows_two_slice(L, q, w)
    return count_conserved(states, second_order_rule(L, q), wf, nfeat)


# ---------------------------------------------------------------- controls
def control_rule184(L, w):
    """Positive control: rule 184 conserves the number of 1s."""
    states = list(product(range(2), repeat=L))

    def step(s):
        return tuple(1 if (s[(i - 1) % L] == 1 and s[i] == 0) or (s[i] == 1 and s[(i + 1) % L] == 1) else 0
                     for i in range(L))

    def wf(s):
        out = []
        for i in range(L):
            f = 0
            for j in range(w):
                f = f * 2 + s[(i + j) % L]
            out.append(f)
        return out
    return count_conserved(states, step, wf, 2 ** w)


def control_random_bijection(L, q, w, seed):
    """Countercontrol: a seeded random bijection of the same configuration set."""
    states = list(product(range(q), repeat=2 * L))
    perm = states[:]
    random.Random(seed).shuffle(perm)
    table = dict(zip(states, perm))
    wf, nfeat = windows_two_slice(L, q, w)
    return count_conserved(states, table.__getitem__, wf, nfeat)


def control_shift(L, q, w):
    """Positive control: the lattice translation conserves every additive quantity."""
    states = list(product(range(q), repeat=2 * L))

    def step(s):
        u, v = s[:L], s[L:]
        return tuple(u[(i + 1) % L] for i in range(L)) + tuple(v[(i + 1) % L] for i in range(L))
    wf, nfeat = windows_two_slice(L, q, w)
    n, rM, rD = count_conserved(states, step, wf, nfeat)
    return n, rM, rD


def cycle_count(L, q):
    states = list(product(range(q), repeat=2 * L))
    step = second_order_rule(L, q)
    seen, cycles = set(), 0
    for s in states:
        if s in seen:
            continue
        cycles += 1
        x = s
        while x not in seen:
            seen.add(x)
            x = step(x)
    return cycles, len(states)


def main():
    # Solver controls first: verdicts print only over green controls.
    n184, _, _ = control_rule184(10, 2)
    check("positive control: rule 184 has exactly one non-constant additive conserved quantity at w=2, L=10",
          n184 == 1)
    nsh, rMs, rDs = control_shift(5, 2, 2)
    check("positive control: translation conserves every additive quantity (rank D = 0, count = rank M - 1)",
          rDs == 0 and nsh == rMs - 1 and nsh > 0)
    nrand, _, _ = control_random_bijection(5, 2, 2, seed=20261119)
    check("countercontrol: seeded random bijection on (Z/2)^(2*5) has no additive conserved quantity at w=2",
          nrand == 0)

    for L, q in [(4, 2), (6, 2), (5, 3)]:
        states = list(product(range(q), repeat=2 * L))
        step = second_order_rule(L, q)
        check(f"rule is a bijection on L={L}, q={q}", len({step(s) for s in states}) == len(states))

    cyc, tot = cycle_count(4, 2)
    print(f"RD6 (L=4, q=2): {tot} configurations, {cyc} cycles")
    check("RD6: real conserved functions (constant on cycles) span more than the constants", cyc > 1)

    controls_green = all(ok for _, ok in RESULTS)
    print("CONTROLS", "GREEN" if controls_green else "RED")
    if not controls_green:
        sys.exit(1)

    table = {}
    plan = [(2, 1, [3, 4, 5, 6, 7, 8]), (2, 2, [4, 5, 6, 7, 8]), (2, 3, [5, 6, 7, 8]),
            (3, 1, [3, 4, 5, 6]), (3, 2, [4, 5, 6])]
    for (q, w, Ls) in plan:
        for L in Ls:
            n, rM, rD = probe_rule(L, q, w)
            table[(q, w, L)] = n
            print(f"q={q} w={w} L={L}: rank M={rM}, rank D={rD}, non-constant additive conserved = {n}", flush=True)
    for (q, w, Ls) in plan:
        vals = [table[(q, w, L)] for L in Ls]
        print(f"MEASURED q={q} w={w}: counts over L={Ls} -> {vals}")
    sys.exit(0)


if __name__ == "__main__":
    main()
