#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Physical C4, round 2, target CS6 -- the lattice toy instance under the storage-time reading.

EVIDENCE LEVEL 3 BY DESIGN, NOT BY FALLBACK. The round's preregistration,
`verification/programmes/physical-realization/round-c4-2-storage-readback/preregistration.md`
(blob 16cfd1303e7c279c8d6bab68b7112c3f25a7460e), targets `CS6` at evidence level 3 from the
start and records why: the read clauses are real-valued sums over sixty-four hidden states
indexed by a dependent function type over a subtype of the torus, which round 1's result note
records as not `decide`-reachable, and repeating a target whose obstruction is on the record
would spend the round's effort on a known wall. The kernel module
`OIBridge/PhysicalC4StorageReadback.lean` therefore carries NO theorem about this instance.
This file is that probe. Its arithmetic is exact (`fractions.Fraction` throughout); no floating
point enters any assertion.

THE OBJECT, reused from round 1 and not redefined. The manuscripts' discrete wave rule on a
one-dimensional torus of four sites over the alphabet Z/2, coupling alpha = 1 -- the kernel's
`waveSubstratum 1 4 2 1` -- in the phase-space form the kernel uses,
`leap F (p, c) = (c, F(c) - p)` with `F(c)(i) = alpha * (c(i+1) + c(i-1))`. The observer's region
is the single site 0, so the visible carrier is that site's pair `(previous, current)` -- four
states -- and the hidden carrier is the other three sites' pairs, sixty-four states, with the
uniform prior 1/64 that [Main] Lemma 3 selects and that #537 proves the architecture does not
determine by invariance. `cutRealization (waveSubstratum 1 4 2 1) {0} uniform` is reused, not
redefined.

THE PREDICATE, transcribed from the module and not reshaped. `rootedStatePosterior R a s x` is
the root-conditioned law of the hidden state AT THE STORAGE TIME `s`, `Law(H_s | X_s = x,
X_0 = a)`; `RoutedReadbackAtStorage K R` asks for roots a != b, times 0 < w <= s < t <= K and a
visible value x with

  W   some seed of positive prior whose hidden component after w steps differs under the two
      roots;
  S   x carrying positive probability under both roots, with the two root-conditioned
      STORAGE-TIME hidden laws differing;
  R1  those two laws, pushed forward through t - s steps from (x, -), giving different visible
      laws;
  R2  the rooted rows at t differing.

Round 1's `rootedPosterior` -- the root-conditioned law of the initial hidden SEED -- is carried
alongside for the comparison the round's provenance records, under the name round 1 gave it. Both
predicates are evaluated here; neither is renamed and neither is re-proved.

WHAT IS CERTIFIED, and only this:

  CS6-a  `RoutedReadbackAtStorage 3 (cutRealization (waveSubstratum 1 4 2 1) {0} uniform)`
         holds, by round 1's own frozen witness a = (0, 0), b = (1, 0), (w, s, t) = (2, 2, 3),
         x = (1, 0) -- checked clause by clause, then re-derived by exhaustive search.
  CS6-b  the same at window 2 does NOT hold, by exhaustive search over every root pair, every
         admissible (w, s, t) and every visible value.

THE READING, frozen in the control plane's terms, and the readings FORBIDDEN. Under the
storage-time reading the lattice predicate is not vacuous on the manuscripts' own dynamics: on a
four-site torus with a one-site region the routed readback fires at window 3 and not at window 2,
with round 1's frozen witness among those found. That is the entire content. It is NOT [SM]
Theorem 22's genericity lemma -- the lemma quantifies over connected regions with |V| <= N/3 and
this fixes one region, one size and one alphabet. It is not a physical statement: L = 4 is no
lattice cut of our universe and no accessibility clock is attached. It moves the P1 row's status
by nothing. The sentences "C4 holds at the lattice cut", "the lattice cut is discharged" and
"the genericity lemma holds in an instance" are forbidden in terms.
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
    """The cut realization's step: the substratum's phi transported along the split."""
    vis, hid = state
    nxt = leap((vis,) + hid)
    return (nxt[REGION], nxt[REGION + 1:])


_ITER = {0: {(v, h): (v, h) for v in VIS for h in HID}}


def iterate(state, n):
    if n not in _ITER:
        prev = _ITER[n - 1] if (n - 1) in _ITER else None
        if prev is None:
            iterate(state, n - 1)
            prev = _ITER[n - 1]
        _ITER[n] = {p: step(prev[p]) for p in prev}
    return _ITER[n][state]


def rooted_map(t, a, j):
    return sum((PRIOR[h] for h in HID if iterate((a, h), t)[0] == j), Fraction(0))


def seed_posterior(a, s, x):
    """Round 1's object: the root-conditioned law of the initial hidden SEED."""
    den = rooted_map(s, a, x)
    if den == 0:
        return None
    return {h: (PRIOR[h] if iterate((a, h), s)[0] == x else Fraction(0)) / den for h in HID}


def state_posterior(a, s, x):
    """This round's object: Law(H_s | X_s = x, X_0 = a), the STORAGE-TIME hidden law."""
    den = rooted_map(s, a, x)
    if den == 0:
        return None
    out = {k: Fraction(0) for k in HID}
    for h in HID:
        v, k = iterate((a, h), s)
        if v == x:
            out[k] += PRIOR[h]
    return {k: out[k] / den for k in HID}


def marg(weight, s_time, t_time, x):
    out = {}
    for k in HID:
        j = iterate((x, k), t_time - s_time)[0]
        out[j] = out.get(j, Fraction(0)) + weight[k]
    return out


def clauses(a, b, w, s, t, x, posterior):
    """The five clauses, each returned separately so a failure is located."""
    write = any(
        PRIOR[h] > 0 and iterate((a, h), w)[1] != iterate((b, h), w)[1] for h in HID
    )
    ga, gb = rooted_map(s, a, x), rooted_map(s, b, x)
    overlap = ga > 0 and gb > 0
    if not overlap:
        return write, overlap, False, False, False
    pa, pb = posterior(a, s, x), posterior(b, s, x)
    store = pa != pb
    ma, mb = marg(pa, s, t, x), marg(pb, s, t, x)
    read = any(ma.get(j, Fraction(0)) != mb.get(j, Fraction(0)) for j in VIS)
    rows = any(rooted_map(t, a, j) != rooted_map(t, b, j) for j in VIS)
    return write, overlap, store, read, rows


def witnesses(K, posterior):
    """Every witness of the predicate within the window K, exhaustively."""
    found = []
    for a, b in itertools.permutations(VIS, 2):
        for w in range(1, K + 1):
            for s in range(w, K + 1):
                for t in range(s + 1, K + 1):
                    for x in VIS:
                        if all(clauses(a, b, w, s, t, x, posterior)):
                            found.append((a, b, w, s, t, x))
    return found


def main():
    t0 = time.time()
    print("physical_c4_storage_readback_probe -- CS6, the toy instance under the storage-time")
    print("reading of the store clause")
    print("=" * 78)
    print("EVIDENCE LEVEL 3 BY DESIGN, not by fallback. No kernel claim is made for this")
    print("instance; `OIBridge/PhysicalC4StorageReadback.lean` carries no theorem about it.")
    print("All arithmetic below is exact rational arithmetic.")
    print()

    print("the object -- reused from round 1, not redefined")
    print("-" * 78)
    check("carriers", len(VIS) == 4 and len(HID) == 64,
          f"visible {len(VIS)} states (site 0's pair), hidden {len(HID)} states (sites 1-3)")
    check("prior normalized", sum(PRIOR.values()) == 1 and all(p > 0 for p in PRIOR.values()),
          "uniform 1/64, [Main] Lemma 3's selection -- a selection, not a derivation")
    check("step is a bijection",
          len({step((v, h)) for v in VIS for h in HID}) == len(VIS) * len(HID),
          "the transported wave rule permutes the 256 cut states")
    print()

    print("the storage-time law is a probability law, and the two roots' supports are disjoint")
    print("-" * 78)
    a, b, w, s, t, x = (0, 0), (1, 0), 2, 2, 3, (1, 0)
    pa, pb = state_posterior(a, s, x), state_posterior(b, s, x)
    check("Law(H_s | X_s = x, X_0 = a) sums to one",
          sum(pa.values()) == 1 and all(v >= 0 for v in pa.values()),
          f"support of size {sum(1 for v in pa.values() if v > 0)}")
    check("Law(H_s | X_s = x, X_0 = b) sums to one",
          sum(pb.values()) == 1 and all(v >= 0 for v in pb.values()),
          f"support of size {sum(1 for v in pb.values() if v > 0)}")
    check("the two supports do not meet",
          not any(pa[k] > 0 and pb[k] > 0 for k in HID),
          "the update is a bijection, so the preimage at time s determines the root")
    print()

    print("CS6-a -- round 1's frozen witness, clause by clause, under the storage-time reading")
    print("-" * 78)
    check("timing 0 < w <= s < t <= 3", 0 < w <= s < t <= 3, f"(w, s, t) = ({w}, {s}, {t})")
    write, overlap, store, read, rows = clauses(a, b, w, s, t, x, state_posterior)
    check("W, write", write,
          "a seed of positive prior whose hidden state at w separates the roots")
    check("S, overlap", overlap,
          f"Gamma_{s}(a, x) = {rooted_map(s, a, x)}, Gamma_{s}(b, x) = {rooted_map(s, b, x)}")
    check("S, store", store, "the root-conditioned STORAGE-TIME hidden laws at x differ")
    check("R(1), causal read", read,
          "the two storage-time laws, propagated from (x, -), give different visible laws at t")
    check("R(2), rooted reappearance", rows, f"the rooted rows at t = {t} differ")
    check("CS6-a: RoutedReadbackAtStorage 3 on the cut realization",
          all(clauses(a, b, w, s, t, x, state_posterior)),
          f"witness a = {a}, b = {b}, (w, s, t) = ({w}, {s}, {t}), x = {x}")
    print()

    print("CS6-a and CS6-b -- exhaustive search at both windows, both readings")
    print("-" * 78)
    at3 = witnesses(3, state_posterior)
    at3_seed = witnesses(3, seed_posterior)
    check("round 1's frozen witness is among the window-3 witnesses",
          (a, b, w, s, t, x) in at3, f"{len(at3)} witnesses at K = 3, storage-time reading")
    check("round 1's frozen witness is among them under round 1's reading too",
          (a, b, w, s, t, x) in at3_seed,
          f"{len(at3_seed)} witnesses at K = 3, round 1's reading -- consumed, not re-proved")
    check("the counts agree at K = 3", len(at3) == len(at3_seed),
          f"{len(at3)} under each reading; the round claims nothing general from the agreement")
    check("the storage-time witness tuples at K = 3",
          sorted({(u[2], u[3], u[4]) for u in at3}) == [(1, 2, 3), (2, 2, 3)],
          f"{sorted({(u[2], u[3], u[4]) for u in at3})}")
    at2 = witnesses(2, state_posterior)
    at2_seed = witnesses(2, seed_posterior)
    check("CS6-b: no witness at window 2, storage-time reading", at2 == [],
          "every root pair, every admissible (w, s, t) and every visible value checked")
    check("no witness at window 2 under round 1's reading either", at2_seed == [],
          "recorded for the comparison; round 1's own result stands as merged")
    print()

    print("what this does NOT show")
    print("-" * 78)
    print("  Under the storage-time reading the lattice predicate is not vacuous on the")
    print("  manuscripts' own dynamics: it fires at window 3 and not at window 2 on a four-site")
    print("  torus with a one-site region, with round 1's frozen witness among those found.")
    print("  That is the entire content. This is NOT [SM] Theorem 22's readback genericity")
    print("  lemma -- the lemma quantifies over connected regions with |V| <= N/3, and the")
    print("  instance fixes one region, one size and one alphabet. It is not a physical")
    print("  statement: L = 4 is no lattice cut of our universe, and no accessibility clock is")
    print("  attached to it. It moves the P1 row's status by nothing, and it says nothing about")
    print("  the cosmological cut. Forbidden in terms: 'C4 holds at the lattice cut', 'the")
    print("  lattice cut is discharged', 'the genericity lemma holds in an instance'.")
    print()

    if FAILURES:
        print(f"physical_c4_storage_readback_probe: FAILED -> {', '.join(FAILURES)}  "
              f"[{time.time() - t0:.1f}s]")
        return 1
    print(f"physical_c4_storage_readback_probe: ALL CHECKS PASS  [{time.time() - t0:.1f}s]")
    return 0


if __name__ == '__main__':
    sys.exit(main())
