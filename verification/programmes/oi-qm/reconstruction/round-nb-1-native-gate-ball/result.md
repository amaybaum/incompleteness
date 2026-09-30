# Reconstruction round NB-1 — the finite native-gate ball theorem: RESULT

**Outcome:** `NB-1-CORE-PROVED`

> In the kernel, at evidence level 2: the averaging bound and its consequence for `p ≥ 2` (`averaging_bound`, `vanish_of_bound`), the Lorentz test (`lorentz_of_effects`), the vanishing of every `E₊` block entry for `p ≥ 2` and hence `p ≤ 1` whenever an entry is nonzero (`blocks_vanish`, `p_le_one`), the equality of the `±1` eigenspace dimensions of a linear map under an injective map anticommuting with it (`parity`), the isometry step (`isometry_of_contractions`) and the count (`dim_of_bounds`), joined in the verdict `nb1_kernel_core`. In exact rational arithmetic replayed in CI, and not in the kernel, the round's probe computes the S1 and S2 solution spaces for `d = 2, …, 7` and every split `p + q = d − 1`, the S4 value identity for `d = 5` and `d = 7`, and the three minimality countermodels: without the control-NOT relation, the `d = 5` J/K map meets the frame, `G² = I` and the target relation, and its value on product states and effects obeys the complex CNOT's reduction formula exactly; with different NOTs `N_A ≠ N_B`, the same map meets both native relations; keeping the frame, `G² = I` and both relations, the `d = 7` candidate sends the product state `(u + x)⊗(u + v₃)` outside the maximal tensor cone, with minimum `1 − √3` over target effects. The theorem these layers serve — two locally tomographic `d`-balls with their full self-dual effect cones, one common NOT involution `N`, and an invertible `G` acting as CNOT on the corners, satisfying `(I⊗N)G(I⊗N) = G` and `(N⊗I)G(N⊗I) = (I⊗N)G`, with `G` and `G⁻¹` sending product states into the maximal tensor cone, force `d ∈ {1, 3}` — holds by the round's written proof, in which S1, S2 and the S4 value identity are proved by hand for every `d`; it is not a kernel theorem, and the two surviving countermodels are positive by the written reduction to the complex CNOT. Read for OI, the theorem is conditional on identical-copy covariance, `Σ(N⊗I)Σ⁻¹ = I⊗N`, which the corpus does not derive; nothing here claims that OI selects `d = 3`.

**THE CLAUSE, carried at this mention — the result.**

> Round NB-1 proves statements about finite native gates on two copies of a d-ball and adopts none of them as anything but mathematics. A `CORE-PROVED` verdict settles in the kernel the dimension-free steps of the ball theorem, certifies in exact arithmetic the S1 and S2 solution spaces for d = 2 to 7, the S4 value identity for d = 5 and 7 and the three minimality countermodels, and leaves the theorem for general d resting on the round's written proof; that theorem is not a kernel theorem. Its reading for OI is conditional on identical-copy covariance, `Σ(N⊗I)Σ⁻¹ = I⊗N`, a premise the corpus does not derive and this round does not supply, stated as a covariance and not as the availability of SWAP. The round does not claim that OI selects d = 3; it uses no SWAP, composite unitary control, continuous local group, `G² = I`, normalization of `G` or intermediate cone; and it edits no manuscript and no roadmap row.

## The layers at `E`

| layer | what it certifies | where |
| --- | --- | --- |
| kernel, evidence level 2 | `averaging_bound`, `vanish_of_bound`, `col_sq` (S3); `lorentz_of_effects`, `blocks_vanish`, `p_le_one` (S4 given its value identity); `parity` (S5); `isometry_of_contractions` (the last step of S1); `dim_of_bounds` (the count); the verdict `nb1_kernel_core` | `verification/lean-mathlib/OIBridge/NativeGateBall.lean` |
| exact computation, replayed in CI | the S1 and S2 solution spaces for `d = 2, …, 7` and every split; the S3 identity on a fixed determining set, with its countercontrol; the S4 value identity for `d = 5, 7`; the countermodels C5, C2N and C7 and the controls C3 and C2 | `verification/lean/native_gate_ball_probe.py` |
| written proof | S1, S2 and the S4 value identity for every `d`; the positivity of the J/K countermodels by reduction to the complex CNOT; the assembly of the steps | the preregistration, *The theorem and its proof* |

## The kernel layer

The module at `E` is blob `6d3ad5e7a1eb28bb327e9f2212519a2b80e5187a`, the reference implementation `6d3ad5e7a1eb28bb327e9f2212519a2b80e5187a`: no departure. It carries the frozen header,
no definition, and ten theorems, each followed by its `#print axioms` line. In the run at `E`'s predecessor, every
theorem reports axioms within `[propext, Classical.choice, Quot.sound]` (`dim_of_bounds` within `[propext, Quot.sound]`),
and `lean-axioms` reports 5288 named results and no sorry.

## The exact-computation layer

The probe has its frozen blob `203446ece72e4420d32007e0d79f78f401279337`. Its summary line in run 36743809499, on `25e6ec91410d0c70d2ebf10d0a7d76e897309ce4`:

`native_gate_ball_probe: OK -- 51 checks: S1 d=2..7, S2 d=2..7 all p, S3 replay, S4 identity, controls C3 C5 C2N C7 C2`

## The execution

| commit | content | run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `6fdeff77` | the preregistration, blob `40f9ab4c` | 36731516115 | `success`, all 30 jobs |
| `26c21fff` | stage 1: `controls.py` (`9b0bf689`), the probe (`203446ec`), the workflow shard | 36736601202 | `success`, all 31 jobs |
| `06702b99` | stage 2: the module without its verdict (`401caee3`), the import, the census family | 36740471750 | `success`, all 31 jobs; `lean-axioms` 5287 |
| `25e6ec91` | stage 3: the verdict; the module is the reference `6d3ad5e7` | 36743809499 | `success`, all 31 jobs; `lean-axioms` 5288 |

No run was cancelled. The paths changed from `D` are exactly the governed ones; no manuscript, built artifact or
`verification/ROADMAP.md` changed.

## What stays open

- Whether OI supplies one common NOT on identical copies (identical-copy covariance): not derived, not supplied here.
- Whether `G` injective with `G(min) ⊆ max` alone, without inverse positivity, forces `d ∈ {1, 3}`.
- Systems whose state space is not a ball, and effect cones smaller than the dual cone.
