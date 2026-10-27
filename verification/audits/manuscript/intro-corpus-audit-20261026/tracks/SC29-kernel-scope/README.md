# SC-29: kernel scope of the continuous-time path and of the memory/C3 theorems

Source-correction unit of audit #942, gate issue #946 (final consolidated audit at `55e3217b`).
Base: `main` at `0d917665`. Line numbers below are at that base; every Lean edit in this unit is
comment-only and line-preserving, so the Lean line numbers hold on this branch too.

## What the kernel proves

**The drive path.** `verification/lean-mathlib/OIBridge/SecondOrderDrive.lean:225`

```lean
theorem driveQ_isContinuousPath :
    driveQ R 0 = (id : Quasilocal ι (V × V) → Quasilocal ι (V × V)) ∧
      (∀ t : ℝ, Function.Bijective (driveQ R t : Quasilocal ι (V × V) → Quasilocal ι (V × V)) ∧
        (∀ x y, driveQ R t (x * y) = driveQ R t x * driveQ R t y) ∧
        (∀ x y, driveQ R t (x + y) = driveQ R t x + driveQ R t y) ∧
        (∀ x, driveQ R t (star x) = star (driveQ R t x)) ∧
        (∀ x, ‖driveQ R t x‖ = ‖x‖)) ∧
      (∀ x : Quasilocal ι (V × V), Continuous fun t : ℝ => driveQ R t x)
```

with `SecondOrderDrive.lean:829`, `driveQ_one_eq_heisQ : driveQ R 1 x = heisQ (ruleDynamics R) x`.
The continuity clause is `∀ x, Continuous fun t => driveQ R t x` (`continuous_driveQ_time`,
`SecondOrderDrive.lean:199`). That is strong (pointwise) continuity. No kernel theorem gives
continuity of `t ↦ driveQ R t` in the operator norm, uniformly over the unit ball.

**Locality.** The kernel's predicate is `LocalityPreserving` (`QuasilocalCharacterization.lean:475`:
every stage is carried into some stage). It is proved for the discrete dynamics
(`oi_localityPreserving`, `:479`) and, through `driveQ_one_eq_heisQ`, therefore holds at `t = 1`.
Each layer separately maps local observables to local ones (`SecondOrderLayer.lean:685`
`layerQ_stage` with `:899` `layerAct_mem_range`; `SwapLayer.lean:384` `swapQ_stage` with `:255`
`swapAct_mem_range_self`). No kernel theorem states locality preservation for `driveQ R t` at
general `t`, and `driveQ_isContinuousPath` carries no locality clause. The composite case would
follow from the two layer results in two steps, but it is not stated in the kernel, so the
manuscripts do not claim it.

**Memory and C3.** `HiddenMemory.lean:54`

```lean
structure Realization (Hist V H : Type*) [Fintype Hist] [Fintype V] [Fintype H] where
  step : V × H ≃ V × H
  w : Hist × V × H → ℝ
  nonneg : ∀ s, 0 ≤ w s
  total : ∑ s, w s = 1
```

`unavoidable_hidden_predictive_memory` (`HiddenMemory.lean:185`), `c3_necessity`
(`C3Necessity.lean:80`), `card_hidden_ge_two_pow_Istar` (`C3Necessity.lean:117`) and
`c3_necessity_and_capacity` (`C3Necessity.lean:130`) are proved for every `Realization`, meaning a
bijection together with an arbitrary joint law `w` of `(X_<t, X_t, H_t)`. No field ties `w` to
`step`, to an initial law or to a horizon. The manuscript reads a faithful realization's time-`t`
law as such a joint law, and that reading is not formalized. `Istar` (`C3Necessity.lean:103`) is a
maximum over a finite nonempty family of `Realization`s that share one hidden alphabet.

## Ledger (`verification/coverage/LEDGER.json`)

The ledger's level definitions are K3 "the exact manuscript statement is proved in Lean" and K2
"the main structural content is Lean-proved; named ancillary steps remain external".
`coverage_check.py` requires an empty `delta` at K3 and a non-empty one at K2.

| entry | was | now | delta (named ancillary step) |
|---|---|---|---|
| `MAIN:T-unavoidable-hidden-predictive-memory` | K3 | K2 | time-`t` reading of a realization's law as the joint law |
| `MAIN:T-c3-necessity` | K3 | K2 | the same step |
| `MAIN:C-per-process-capacity-bound` | P (“no Lean statement”) | K2, Lean check `C3Necessity.lean` added | the same step; the revival witness and the independence-hypothesis clause are probe-certified |

No fingerprint moves: the edited Main text lies outside the fingerprinted statement blocks
(`proof_census.py` fingerprints the header line through the first blank line). No ID is added or
retired. Memory-conditions row: K3 2→0, K2 0→3, P 10→9. Total: K3 23→21, K2 6→9, P 28→27.
Kernel coverage 30/116 → 31/116. No coverage count is quoted elsewhere in the corpus (grep for
`30/116`, `25.9%`, `58/116` and K3 totals: 0 hits).

## Site table

| site (at `55e3217b`) | was | anchor | now |
|---|---|---|---|
| Main :268 | exact norm-continuous path of local `*`-automorphisms | `driveQ_isContinuousPath` (`∀ x, Continuous fun t => driveQ R t x`; no locality clause) | exact strongly continuous path of `*`-automorphisms |
| Main :584 | … norm-continuous path of local `*`-automorphisms of that algebra | same | … strongly continuous path of `*`-automorphisms of that algebra |
| GR :292 | norm-continuous path of isometric `*`-automorphisms | same | strongly continuous path of isometric `*`-automorphisms |
| Explainer :381 | as Main :584 | same | as Main :584 (also drops “to keep the claim honest”, a §A.32 hit on the edited line) |
| FULL :509, :5286 | as Main :584 | same | as Main :584 |
| ch01 :165 | as Main :584 | same | as Main :584 |
| ch19 :126 | as Main :584 | same | as Main :584 |
| Main :510 | C3 kernel citation with no scope | `Realization` (`w` not tied to `step`); `Istar` | adds: for joint laws of history, present and hidden state, `I*` the maximum over a finite family of such laws on one hidden alphabet; reading a realization's time-`t` laws as those joint laws is not formalized |
| Main :608 | `(kernel: c3_necessity …)` | same | adds “in the joint-law form of (c)” |
| Main :610 | “stated there for bijective realizations” | same | “… for bijective realizations in joint-law form” |

Companion surfaces corrected in the same way: `verification/README.md` (two sites), the CT2 note
in `verification/lean-manuscript-census.json`, `verification/audits/manuscript/lean-manuscript-census.md`
(two sites), the `R7-CTN` pins in `verification/lean/edge_rigidity_probe.py`, the docstring of
`verification/lean/static_generator_probe.py`, and the docstrings and scope prints of
`hidden_memory_probe.py` and `c3_necessity_probe.py`. Lean comments (comment-only; with comments
stripped, the code is byte-identical to the base): `SecondOrderDrive.lean` :35, :195–198, :222–223,
:826 now say strongly continuous; `HiddenMemory.lean` :26–30 and :48–53 no longer say the law is
“induced” by the bijection; `C3Necessity.lean` :24–28 states the joint-law reading, :75 and :112
change §3.3 to §3.4, and :127 changes “as the manuscript states it” to “in joint-law form”.

Left unchanged: `verification/audits/physical-realization/continuous-time-audit.md` :200, :211,
:264, :279 and `verification/audits/foundations/exec-source-audit.md` :44. These are dated audit
entries, and the continuous-time audit defines the property it records as `t ↦ driveQ R t A`
norm-continuous for every `A` (strong continuity). `SecondOrderDrive.lean:34` says the same and is
accurate. Main :733 (“C3 necessity | Proved …”) is accurate for the paper proof.

## Re-grep (this branch)

- `norm[- ]continu` in `papers/*.{md,tex}`, `book/*.{md,tex}`: 0 (was 8 md sites).
- `path of local` in the same files: 0.
- `strongly continuous path` (md): Main 2, GR 1, Explainer 1, ch01 1, ch19 1, FULL 2. In the
  `.tex` files, after whitespace normalisation: Main 2, GR 1, Explainer 1, FULL 2.
- `norm[- ]continu` elsewhere under `verification/` and `tools/`: 6, all of them on the
  left-unchanged list above.

## Checks

`python3 -I tools/release_gate.py`: every step passes except `lean-axioms`, which has no local
toolchain. `edge_rigidity_probe.py`, `c3_necessity_probe.py` and `hidden_memory_probe.py`: all
checks pass. `coverage_check.py`: OK. The §A.32/§A.33 added-lines scan and the secrets scan of
added lines: 0 hits. `sh ./build.sh Main GR Explainer` and `--book` succeed with no dropped glyphs,
and page counts are unchanged (96, 88, 70, 558). The three Lean files are not built locally, so
CI's `lake build` must confirm them.
