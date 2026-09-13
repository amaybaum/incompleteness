#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Physical C4 discharge, round 1, target RD6 -- the toy instance of the lattice predicate.

EVIDENCE LEVEL 3 BY THE CONTROL PLANE'S OWN FROZEN FALLBACK. The round's preregistration,
`verification/programmes/physical-realization/round-c4-1-physical-discharge/preregistration.md`
(blob a80334a5d5f19125b69459523acf723b607f97e1), targets `RD6-a` at kernel level with the
prediction "positive as mathematics, medium at kernel level", and freezes the fallback: if
`RD6-a` is not reached at level 2, BOTH halves are reported at level 3 by one exact probe,
labelled so, and no kernel claim is made for the instance. The kernel module
`OIBridge/PhysicalC4Discharge.lean` therefore carries `LatticeCutReadback` as a definition and
carries NO theorem about this instance. This file is that probe. Its arithmetic is exact
(`fractions.Fraction` throughout); no floating point enters any assertion.

THE OBJECT. The manuscripts' discrete wave rule on a one-dimensional torus of four sites over
the alphabet Z/2, coupling alpha = 1 -- the kernel's `waveSubstratum 1 4 2 1` -- in the
phase-space form the kernel uses, `leap F (p, c) = (c, F(c) - p)` with
`F(c)(i) = alpha * (c(i+1) + c(i-1))`. The observer's region is the single site 0, so the
visible carrier is that site's pair `(previous, current)` -- four states -- and the hidden
carrier is the other three sites' pairs, sixty-four states, with the uniform prior 1/64 that
[Main] Lemma 3 selects and that #537 proves the architecture does not determine by invariance.

THE PREDICATE, transcribed from the module and not reshaped. `rootedPosterior R a s x` is the
root-conditioned prior weight of a hidden SEED compatible with the visible value x at time s,
divided by the rooted probability of x; `RoutedReadback K R` asks for roots a != b, times
0 < w <= s < t <= K and a visible value x with

  W   some seed of positive prior whose hidden component after w steps differs under the two
      roots;
  S   x carrying positive probability under both roots, with the two root-conditioned seed
      weights differing;
  R1  those two weights, pushed forward through t - s steps from (x, -), giving different
      visible laws;
  R2  the rooted rows at t differing.

WHAT IS CERTIFIED, and only this:

  RD6-a  `LatticeCutReadback 1 4 2 1 {0} uniform 3` holds, by the control plane's frozen
         witness a = (0, 0), b = (1, 0), (w, s, t) = (2, 2, 3), x = (1, 0) -- checked clause by
         clause, and then re-derived by exhaustive search over all witnesses.
  RD6-b  `LatticeCutReadback 1 4 2 1 {0} uniform 2` does NOT hold, by exhaustive search over
         every root pair, every admissible (w, s, t) and every visible value.

THE READING, frozen in the control plane's terms, and the readings FORBIDDEN. What this shows is
that the lattice predicate is not vacuous on the manuscripts' own dynamics: on a four-site torus
with a one-site region the routed readback fires at window 3 and not at window 2. That is the
entire content. It is NOT [SM] Theorem 22's genericity lemma -- the lemma quantifies over
connected regions with |V| <= N/3 and this fixes one region, one size and one alphabet. It is
not a physical statement: L = 4 is no lattice cut of our universe and no accessibility clock is
attached. It moves the P1 row's status by nothing. The sentences "C4 holds at the lattice cut",
"the lattice cut is discharged" and "the genericity lemma holds in an instance" are forbidden in
terms.
"""
import itertools
import sys
import time
from fractions import Fraction

FAILURES = []
L = 4                       # sites on the one-dimensional torus
Q = 2                       # alphabet Z/q
ALPHA = 1                   # the manuscripts' coupling
REGION = 0                  # the observer's one-site region


def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  -- {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def leap(conf):
    """The kernel's phase-space step on a full configuration, sites in order."""
    cur = [conf[i][1] for i in range(L)]
    return tuple(
        (conf[i][1], (ALPHA * (cur[(i + 1) % L] + cur[(i - 1) % L]) - conf[i][0]) % Q)
        for i in range(L)
    )


VIS = [(p, c) for p in range(Q) for c in range(Q)]
HID = [tuple(z) for z in itertools.product(VIS, repeat=L - 1)]
PRIOR = {h: Fraction(1, len(HID)) for h in HID}


def step(state):
    """The cut realization's step: 𝒮.φ transported along the region/complement split."""
    vis, hid = state
    nxt = leap((vis,) + hid)
    return (nxt[REGION], nxt[REGION + 1:])


def iterate(state, n):
    for _ in range(n):
        state = step(state)
    return state


def rooted_map(t, a, j):
    return sum((PRIOR[h] for h in HID if iterate((a, h), t)[0] == j), Fraction(0))


def rooted_posterior(a, s, x):
    den = rooted_map(s, a, x)
    if den == 0:
        return None
    return {h: (PRIOR[h] if iterate((a, h), s)[0] == x else Fraction(0)) / den for h in HID}


def marg(weight, s_time, t_time, x):
    out = {}
    for h in HID:
        j = iterate((x, h), t_time - s_time)[0]
        out[j] = out.get(j, Fraction(0)) + weight[h]
    return out


def clauses(a, b, w, s, t, x):
    """The five clauses, each returned separately so a failure is located."""
    write = any(
        PRIOR[h] > 0 and iterate((a, h), w)[1] != iterate((b, h), w)[1] for h in HID
    )
    ga, gb = rooted_map(s, a, x), rooted_map(s, b, x)
    overlap = ga > 0 and gb > 0
    if not overlap:
        return write, overlap, False, False, False
    pa, pb = rooted_posterior(a, s, x), rooted_posterior(b, s, x)
    store = pa != pb
    ma, mb = marg(pa, s, t, x), marg(pb, s, t, x)
    read = any(ma.get(j, Fraction(0)) != mb.get(j, Fraction(0)) for j in VIS)
    rows = any(rooted_map(t, a, j) != rooted_map(t, b, j) for j in VIS)
    return write, overlap, store, read, rows


def routed_readback(K):
    """Every witness of the predicate within the window K, exhaustively."""
    found = []
    for a, b in itertools.permutations(VIS, 2):
        for w in range(1, K + 1):
            for s in range(w, K + 1):
                for t in range(s + 1, K + 1):
                    for x in VIS:
                        if all(clauses(a, b, w, s, t, x)):
                            found.append((a, b, w, s, t, x))
    return found


def main():
    t0 = time.time()
    print("physical_c4_toy_instance_probe -- RD6, the toy instance of the lattice predicate")
    print("=" * 78)
    print("EVIDENCE LEVEL 3, by the control plane's frozen fallback for RD6. No kernel claim is")
    print("made for this instance; `OIBridge/PhysicalC4Discharge.lean` carries no theorem about")
    print("it. All arithmetic below is exact rational arithmetic.")
    print()

    print("the object")
    print("-" * 78)
    check("carriers", len(VIS) == 4 and len(HID) == 64,
          f"visible {len(VIS)} states (site 0's pair), hidden {len(HID)} states (sites 1-3)")
    check("prior normalized", sum(PRIOR.values()) == 1 and all(p > 0 for p in PRIOR.values()),
          "uniform 1/64, [Main] Lemma 3's selection -- a selection, not a derivation")
    check("step is a bijection",
          len({step((v, h)) for v in VIS for h in HID}) == len(VIS) * len(HID),
          "the transported wave rule permutes the 256 cut states")
    print()

    print("RD6-a -- the frozen witness, clause by clause")
    print("-" * 78)
    a, b, w, s, t, x = (0, 0), (1, 0), 2, 2, 3, (1, 0)
    check("timing 0 < w <= s < t <= 3", 0 < w <= s < t <= 3, f"(w, s, t) = ({w}, {s}, {t})")
    write, overlap, store, read, rows = clauses(a, b, w, s, t, x)
    check("W, write", write, "a seed of positive prior whose hidden state at w separates the roots")
    check("S, overlap", overlap,
          f"Gamma_{s}(a, x) = {rooted_map(s, a, x)}, Gamma_{s}(b, x) = {rooted_map(s, b, x)}")
    check("S, store", store, "the root-conditioned seed weights at x differ")
    check("R(1), causal read", read,
          "the two weights, propagated from (x, -), give different visible laws at t")
    check("R(2), rooted reappearance", rows, f"the rooted rows at t = {t} differ")
    check("RD6-a: LatticeCutReadback 1 4 2 1 {0} uniform 3",
          all(clauses(a, b, w, s, t, x)),
          f"witness a = {a}, b = {b}, (w, s, t) = ({w}, {s}, {t}), x = {x}")
    print()

    print("RD6-a and RD6-b -- exhaustive search at both windows")
    print("-" * 78)
    at3 = routed_readback(3)
    check("the frozen witness is among the window-3 witnesses",
          (a, b, w, s, t, x) in at3, f"{len(at3)} witnesses at K = 3")
    at2 = routed_readback(2)
    check("RD6-b: no witness at window 2", at2 == [],
          "every root pair, every admissible (w, s, t) and every visible value checked")
    print()

    print("what this does NOT show")
    print("-" * 78)
    print("  The lattice predicate is not vacuous on the manuscripts' own dynamics: it fires at")
    print("  window 3 and not at window 2 on a four-site torus with a one-site region. That is")
    print("  the entire content. This is NOT [SM] Theorem 22's readback genericity lemma -- the")
    print("  lemma quantifies over connected regions with |V| <= N/3, and the instance fixes one")
    print("  region, one size and one alphabet. It is not a physical statement: L = 4 is no")
    print("  lattice cut of our universe, and no accessibility clock is attached to it. It moves")
    print("  the P1 row's status by nothing, and it says nothing about the cosmological cut.")
    print("  Forbidden in terms: 'C4 holds at the lattice cut', 'the lattice cut is discharged',")
    print("  'the genericity lemma holds in an instance'.")
    print()

    if FAILURES:
        print(f"physical_c4_toy_instance_probe: FAILED -> {', '.join(FAILURES)}  "
              f"[{time.time() - t0:.1f}s]")
        return 1
    print(f"physical_c4_toy_instance_probe: ALL CHECKS PASS  [{time.time() - t0:.1f}s]")
    return 0


if __name__ == '__main__':
    sys.exit(main())
