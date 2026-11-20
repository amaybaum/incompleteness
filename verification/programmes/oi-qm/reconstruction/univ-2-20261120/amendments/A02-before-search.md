# UNIV-2 amendment A02 (before any search or control run on Q)

Committed after A01 (`80121d45`) and before the controls N1–N4 or any family is run. Since A01,
the only computation run is the analytic item A2 on the alphabet `{−1,0,1}` (and its
countercontrol on the linear update), together with a scaling run on `{−2,…,2}`. PREREG §4 places
A2 before the gadget search.

1. **N3 (input that never reaches the junction).** A01 item 3 claimed that a signal launched on
   A and moving away from the junction "does not reach A's far end before `T₁`" when A runs to
   `x = −40`. That is wrong: at speed 1/3 the signal covers 40 sites in 120 ticks. In addition, the
   signal construction used here (flipping an adjacent `(+1,+1)` pair of A's background) gives a
   signal that moves toward the junction (K0); a signal moving away would need a different
   construction. N3 is
   therefore replaced: on A extended to `x = −80`, the same signal type is launched with its
   window at `[−67, −60]`, moving toward the junction. It cannot arrive before `t ≈ 150 > T₁`.
   Required outcome: classified fail, at every B phase.
2. **P1b (added countercontrol).** The same lattice billiard with the mirror removed: the
   particle runs straight past the junction. Required outcome: classified fail. The P1 timing is
   `T₁ = 30`, with the second particle 12 sites behind and checked at `T₂ = 42`, inside far B.
3. **P2 through the shared logic.** P2 runs through the same generic decision function as P1. That
   rule depends on the partition parity, so the state carries the tick count, and equality ignores
   it.
4. **A2 on `{−2,…,2}`.** This computation takes several minutes, so it runs under `--search`
   together with the families; the alphabet `{−1,0,1}` runs by default.

No other part of PREREG or A01 changes.
