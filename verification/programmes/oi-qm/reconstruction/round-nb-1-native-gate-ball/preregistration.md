# Reconstruction round NB-1 — the finite native-gate ball theorem: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> Round NB-1 proves statements about finite native gates on two copies of a d-ball and adopts none of them as anything but mathematics. A `CORE-PROVED` verdict settles in the kernel the dimension-free steps of the ball theorem, certifies in exact arithmetic the S1 and S2 solution spaces for d = 2 to 7, the S4 value identity for d = 5 and 7 and the three minimality countermodels, and leaves the theorem for general d resting on the round's written proof; that theorem is not a kernel theorem. Its reading for OI is conditional on identical-copy covariance, `Σ(N⊗I)Σ⁻¹ = I⊗N`, a premise the corpus does not derive and this round does not supply, stated as a covariance and not as the availability of SWAP. The round does not claim that OI selects d = 3; it uses no SWAP, composite unitary control, continuous local group, `G² = I`, normalization of `G` or intermediate cone; and it edits no manuscript and no roadmap row.

## The declarations

```v3-round
round NB-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/
record AM verification/receipts/NB-1.json
execution A verification/lean-mathlib/OIBridge/NativeGateBall.lean
execution A verification/lean/native_gate_ball_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

The record directory holds three files: this preregistration, the round's frozen controls `controls.py`, and the
result note. The receipt path is `verification/receipts/NB-1.json`. Every other path the round changes is an execution
path listed above. The paths are the same under both outcomes. **No manuscript, no built artifact and
`verification/ROADMAP.md` change under either outcome.**

The workflow changes by one frozen edit in five places: the round's probe runs in a shard of its own, `probes_nb1`,
`Numerical probes / NB-1 native-gate ball`, inserted after the act 45 shard, and the aggregate `Numerical probes` job
lists it in its `needs`, reads its result into its environment, echoes it and tests it for `success`. `controls.py`
checks that the workflow at `E` is `D`'s with exactly that edit.

## The objects

- **`D`** = `fdebc6e39498367e15a8352fe0f01f8f75ab3671`: the head of `main` after act 42's landing, receipt
  `verification/receipts/A42.json`; its parents are `0e87c4a1` and `31b5bd77`. It is certified by push run
  36674034894, overall conclusion `success`: every job succeeded (the act 42 exclusion matrix skipped on a push event, as the workflow requires), the
  release gate passing 21 of 21 steps with nineteen receipts holding and the 303 legacy records intact, `lean-axioms`
  at 5278 named results and no sorry. Every measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only `verification/receipts/NB-1.json`.

No other round runs beside NB-1 at this freeze. Should one land first, its movement of `main` enters NB-1 only by
reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — three certification layers, never merged.** The round certifies one theorem in three layers that do not
substitute for one another (`AGENTS.md`, *Keep verification layers distinct*):

| layer | what it carries | where |
| --- | --- | --- |
| **kernel** (evidence level 2) | S3 (`averaging_bound`, `vanish_of_bound`), the Lorentz test (`lorentz_of_effects`), S4 given its value identity (`blocks_vanish`, `p_le_one`), S5 (`parity`), the isometry step of S1 (`isometry_of_contractions`), the count (`dim_of_bounds`); verdict `nb1_kernel_core` | `NativeGateBall.lean` |
| **exact computation**, replayed in CI | the S1 and S2 solution spaces for `d = 2, …, 7` and every split `p + q = d − 1` (exact ranks over `ℚ`); the S3 identity as a polynomial identity on a fixed determining set, with a countercontrol; the S4 value identity for `d = 5` (`p = 2`) and `d = 7` (`p = 3`) on every basis block entry; the three minimality countermodels and the `d = 3` positive control | `native_gate_ball_probe.py` |
| **written proof** | the derivation of S1 and S2 from the hypotheses for every `d`, the S4 value identity for every `d`, the reduction of the countermodels' positivity to the complex CNOT, and the assembly of the steps into the theorem | this file, *The theorem and its proof* |

The theorem for general `d` is **not a kernel theorem**, and nothing in the result note, the census or the module says
it is. It holds by the written proof; the kernel certifies the dimension-free steps it rests on, and the exact layer
certifies the dimension-dependent steps for `d ≤ 7`. If S1 and S2 are later formalized end to end, that is a new
round.

**Hazard 2 — the OI reading is conditional on one `N`.** The theorem assumes **one** NOT involution `N` acting on both
factors. As an OI premise this is **identical-copy covariance**: for the exchange `Σ` of the two identical copies,
`Σ(N⊗I)Σ⁻¹ = I⊗N` — a covariance or identification statement about the distinguished off-classical NOT, not the
availability of SWAP as an operation. The round's source audit, run at `D` before this freeze, found that the corpus
does not derive it:

- `FactorExchange.lean`: `conjChannel_swapMat_tensor` is algebra with no availability premise; `HasQubitFactorExchange`
  is a premise, obtained from `HasCompositeUnitaryControl` by `compositeControl_hasFactorExchange`. Using that exchange
  to justify one `N` would be circular, since composite unitary control is downstream of what the theorem is about.
- `EmbeddedObservation.lean`: `RelabellingInvariant` transports availability along carrier bijections; the module's own
  countercontrol states that bare OI does not supply that principle, and
  `verification/audits/operational/completion-assumption-audit.md` records the gap as relabelling invariance, which
  observer recursion does not carry. Even where assumed, it makes `I⊗N` available when `N⊗I` is; it does not make the
  second copy's distinguished NOT equal to the transported `N`. The same holds for `ImplementationLocality.lean` and
  `TypedCompletion.lean`, whose admissibility statements cover permutations with phases.
- `LiftAudit.lean`: `gateFlow σ t` is a function of the classical permutation, so it is covariant by construction; it
  is a chosen extension, available only of control (`layerFlowExecutable_of_control`), and other monomial extensions
  of the same truth table remain admissible.
- What the corpus does supply is classical: native exchanges of basis states and the same NOT truth table on both
  copies.

So the round states the premise explicitly and leaves it unsourced. **No outcome licenses "OI selects `d = 3`" or
"OI ⇒ `d = 3`"**; the most any outcome licenses for OI is the conditional *OI-supplied finite gate algebra, plus
identical-copy covariance, plus the ball and local-tomography assumptions, gives `d = 3`*.

**Hazard 3 — scope.** Two copies of the `d`-ball with the full self-dual effect cone; a locally tomographic composite
with the product cone `min` and its dual `max`; one invertible linear `G`. The statement is about this setting and no
other: it says nothing about non-ball systems, about restricted effect cones, about two different NOTs whose
relations are not imposed, or about the one-sided variant (injective `G` with `G(min) ⊆ max` alone), which is open.

**Hazard 4 — the countermodels are scientific content.** Each of the three minimality countermodels shows one
hypothesis load-bearing: one `N`, the control-NOT relation, and positivity. They are frozen below as part of the
result, with their exact checks and the written parts of their arguments named, and not as regression tests.

**Hazard 5 — manuscripts.** None. The owner's direction for this round is a governed abstract theorem, with the source
audit for its OI reading run before any manuscript propagation. The census family is `kernel-only` with no anchor,
under both outcomes. Propagation, if any, is a later round with its own freeze.

**Hazard 6 — history.** Act 42 and every earlier round stand as recorded. The research notes behind this round, from
`D`, are design evidence only; none is a record of this round.

***

## Provenance

The module imports Mathlib only, and consumes no corpus declaration:

- `Mathlib.Analysis.SpecialFunctions.Pow.Real`, `Mathlib.LinearAlgebra.FiniteDimensional.Basic`,
  `Mathlib.Tactic.Linarith`, `Mathlib.Tactic.Ring`; among the lemmas used, `Finset.sum_congr`, `Finset.sum_add_distrib`,
  `Finset.sum_ite_eq'`, `Finset.mul_sum`, `Finset.sum_mul`, `Finset.sum_le_sum`, `Finset.sum_nonneg`,
  `Finset.sum_eq_zero_iff_of_nonneg`, `Finset.sum_neg_distrib`, `Real.sqrt_pos`, `Real.sq_sqrt`, `mul_inv_cancel₀`,
  `pow_eq_zero_iff`, `LinearMap.restrict`, `LinearMap.finrank_le_finrank_of_injective`, `eq_neg_of_add_eq_zero_left`,
  `neg_inj`, and the tactics `simp`, `rw`, `ring`, `linarith`, `nlinarith`, `omega`, `positivity`, `ext`, `subst`.

The probe imports nothing but the Python standard library (`sys`, `fractions`).

## Locating controls — at `D`

The sources of Hazard 2's audit:

| what | where | line |
| --- | --- | --- |
| `conjChannel_swapMat_tensor` | `verification/lean-mathlib/OIBridge/FactorExchange.lean` | 87 |
| `HasQubitFactorExchange` | `verification/lean-mathlib/OIBridge/FactorExchange.lean` | 126 |
| `compositeControl_hasFactorExchange` | `verification/lean-mathlib/OIBridge/FactorExchange.lean` | 131 |
| the countercontrol *"Bare OI does not supply the principle"* | `verification/lean-mathlib/OIBridge/EmbeddedObservation.lean` | 50 |
| `RelabellingInvariant` | `verification/lean-mathlib/OIBridge/EmbeddedObservation.lean` | 106 |
| *"The gap is relabelling invariance, which observer recursion does not"* | `verification/audits/operational/completion-assumption-audit.md` | 38 |
| `gateFlow` | `verification/lean-mathlib/OIBridge/LiftAudit.lean` | 47 |
| `layerFlowExecutable_of_control` | `verification/lean-mathlib/OIBridge/LiftAudit.lean` | 117 |

| file at `D` | blob |
| --- | --- |
| `FactorExchange.lean` | `c7e0776bc00e2920565ee0f11ed02c74d89e12c5` |
| `EmbeddedObservation.lean` | `be7ff0941430925a27f1eb29561d27a69bfd3993` |
| `ImplementationLocality.lean` | `d96b65bd262e658baf0be52cfaf4b6e33de0dd28` |
| `TypedCompletion.lean` | `7ff39e64a2b0a6ae2fb8b60e267a2efb8bb77e5d` |
| `LiftAudit.lean` | `deca05869ff4ed2f131d7e6fb77e5c900048e18f` |
| `completion-assumption-audit.md` | `c9de6c032ae9c5415aea856083c397111bc41de7` |
| `verification/lean-mathlib/OIBridge.lean` | `0c400130d920b0b8bad9c70d6dab5cdf2f156ad3` |
| `verification/lean-manuscript-census.json` | `bd4258a761ec0a533fb7fb6b9d25bae588d6811c` |
| `.github/workflows/verify.yml` | `508a6ea8b6986c42ef0f26bfd30b84f4679c6213` |

The names this round introduces return nothing from `git grep -l` at `D`: `NativeGateBall`, `native_gate_ball`,
`nb1_`, `NB-1`, `round-nb-1` and `identical-copy`.

***

## Why this round exists

Every finite reconstruction of quantum theory from gates reaches for a composite gate on two copies of a system and a
local symmetry on each. The research thread behind this round, from `D`, asked which ball dimensions admit a
reversible CNOT built from native classical data: a NOT on each bit and the CNOT truth table, extended off the
classical frame, with no continuous local group, no SWAP and no composite unitary control. It found a uniform answer —
only `d = 1` and `d = 3` — with the dimension-free steps short enough to formalize and the dimension-dependent steps
checkable exactly. It also found that the answer needs every hypothesis it uses: each of one `N`, the control-NOT
relation and positivity has a countermodel without it. Prior art (Krumm–Müller's connected-group setting,
Al-Safi–Richens on maximal composites, Barnum–Wilce on Jordan structure) does not contain this statement; its novelty
is recorded as *not known to be novel globally, but not contained in those works*. This round freezes the theorem, its
layered certification, its countermodels, and the conditional OI reading.

***

## The theorem and its proof — FROZEN as mathematics

**Setting.** For `d ≥ 1`, the `d`-ball system has vector space `ℝⁿ = ℝu ⊕ T ⊕ ℝz`, `n = d + 1`, `T = ℝ^{d−1}`, with
the Euclidean pairing. Its state cone is the Lorentz cone `L = {x₀u + x : |x| ≤ x₀}`, and its effect cone is **all of
`L`** (self-dual). The corners `k_a = u + (−1)^a z`, `a ∈ {0, 1}`, are antipodal pure states and also effects. The
composite of two copies is locally tomographic, `ℝⁿ ⊗ ℝⁿ`, with `min = cone(L ⊗ L)` and `max` its dual.

**The one NOT.** `N` is a ball involution: orthogonal on `T ⊕ ℝz`, fixing `u`, with `Nz = −z`, so `N k_a = k_{1−a}`.
Its `±1` eigenspaces in `T` have dimensions `p` and `q`, `p + q = d − 1`. Write `V₊ ⊂ T` for the `+1` space,
`E₊ = ℝu ⊕ V₊`, and `V₋ = (−1 space in T) ⊕ ℝz`. The **same** `N` acts on both factors.

**Hypotheses on a linear map `G` of `ℝⁿ ⊗ ℝⁿ`.**

| label | hypothesis |
| --- | --- |
| **F** | `G(k_a ⊗ k_b) = k_a ⊗ k_{a⊕b}` — the CNOT truth table on the corners |
| **P±** | `G` is invertible, `G(min) ⊆ max` and `G⁻¹(min) ⊆ max` |
| **Rt** | `(I⊗N) G (I⊗N) = G` — the target NOT relation |
| **Rc** | `(N⊗I) G (N⊗I) = (I⊗N) G` — the control NOT relation |

**Conclusion.** `d ∈ {1, 3}`.

**Not used**, each checked against every step below: `G² = I`; any normalization of `G`, such as
`(u⊗u)ᵀG = (u⊗u)ᵀ`; an intermediate cone `C` with `min ⊆ C ⊆ max` and `G(C) = C`; any continuous or other local group
beyond `N`; SWAP or any exchange relation; composite or full unitary control.

**The proof.** Each step names its layer.

- **S1, the controlled form** *(written proof; exact for `d ≤ 7`; last step in the kernel)*. The corner effects
  `k_{1−a}ᵀ ⊗ ·` and `· ⊗ k_bᵀ`, which vanish on `G(k_a ⊗ k_b)` by F and are nonnegative on `G(k_a ⊗ t)` for every
  pure `t` by P, and the equator effect curve, force `G(k_a ⊗ t) = k_a ⊗ M_a t` for `t ∈ T`, with `M_a` a contraction
  (positivity of `G`). The same argument for `G⁻¹` makes `M_a⁻¹` a contraction, so `M_a` is an isometry
  (`isometry_of_contractions`). Rt gives `N M_a N = M_a`; F and Rc give `M₁ = N M₀`. P⁻ enters here only.
- **S2, the block structure** *(written proof; exact for `d ≤ 7` and every split)*. Positivity at the corners' tangent
  directions forces `G̃ = G (I ⊗ M₀⁻¹)` to act on `T ⊗ E₊` as `[[0, A_r],[A_r, B_rs]]` — the **same** `A_r` in the
  `(r, u)` and `(u, r)` places, `B_rs = −B_sr` — and to map `T ⊗ V₋` into itself antisymmetrically. The transposed
  form is excluded.
- **S3, the averaging bound** *(kernel: `averaging_bound`, `vanish_of_bound`)*. If `[[1, gᵀ],[g, I + K]]` with `K`
  antisymmetric passes the Lorentz test at the `2p` points `t = ±eᵢ`, then `(p − 1)|g|² + ‖K‖² ≤ 0`; for `p ≥ 2`,
  `g = 0` and `K = 0`.
- **S4, the `E₊` block vanishes for `p ≥ 2`** *(value identity: written proof, exact for `d = 5, 7`; conclusion:
  kernel, `lorentz_of_effects`, `blocks_vanish`, `p_le_one`)*. For a product state `s ⊗ t` and product effect
  `f ⊗ g`, `(f ⊗ g)(G(s ⊗ t)) = (1, b)(I + Γ_ac)(1, M₀t₊)` with `Γ_ac = [[0, γᵀ],[γ, K]]`, `γ_r = a·A_r c`,
  `K_rs = a·B_rs c`. P makes `I + Γ_ac` Lorentz-positive for all `a, c`, so S3 gives `A_r = 0` and `B_rs = 0` when
  `p ≥ 2`. Then `ker G ⊇ T ⊗ E₊`, of dimension `(d − 1)(p + 1) > 0` for `d ≥ 2`, against invertibility: `p ≤ 1`.
- **S5, parity** *(kernel: `parity`)*. By S2 and Rt, `G` maps `T ⊗ V₋` into itself, where Rc reads
  `(N⊗I) G (N⊗I) = −G`. An injective map anticommuting with `Π = N⊗I` exchanges its `±1` eigenspaces
  `V₊ ⊗ V₋` and `T₋ ⊗ V₋`, so `p·dim V₋ = q·dim V₋`: `p = q`. Only injectivity is used.
- **The count** *(kernel: `dim_of_bounds`)*. `p ≤ 1`, `p = q`, `p + q + 1 = d`: `d ∈ {1, 3}`.

**Which hypotheses each step consumes.**

| step | F | P | P⁻ | Rt | Rc | invertible |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S2 | | ✓ | via S1 | | via S1 | |
| S3 | | | | | | |
| S4 | | ✓ | | ✓ | via S1 | ✓ |
| S5 | | | | ✓ | ✓ | ✓ |

### The three minimality countermodels, FROZEN as content

| hypothesis dropped | countermodel | what holds | what is exact, and what is written |
| --- | --- | --- | --- |
| **Rc**, the control-NOT relation | `d = 5`, the J/K map: basis `u, x, y, w₁, w₂, z`, `N = diag(1, 1, −1, −1, −1, −1)`; `G(k_a ⊗ t) = k_a ⊗ Nᵃt`; on `E₊ = ⟨u, x⟩` the target is exchanged `u ↔ x`; on `V₋` `G(c ⊗ t) = Jc ⊗ Kt`, with `J: x→y, y→−x, w₁→w₂, w₂→−w₁` and `K: y→z, z→−y, w₁→w₂, w₂→−w₁` | F, P±, Rt, `G² = I`, the S1/S2 form with `p = 1`, `q = 3`; Rc fails | exact: F, `G² = I`, the S1/S2 form, Rt, the failure of Rc, `J` and `K` orthogonal complex structures, and the value formula `(1 + s_z a_z)(1 + b_x t_x) + (s_z + a_z)(b₋·t₋) + (a·s)(t_x + b_x) + (a·Js)(b₋·Kt₋)` on the multi-affine grid, the same formula holding for the complex CNOT. Written: the pairs `(a·s, a·Js)` and `(b₋·t₋, b₋·Kt₋)` range over discs of the Bloch radii, the value is affine in each pair, so its minimum is on the boundary circles, which is the `d = 3` configuration space, where the value is the complex CNOT's and is `≥ 0`. P⁻ follows from `G² = I` |
| **one `N`**, the same NOT on both factors | `d = 5`, the same J/K map with `N_A = diag(1, 1, −1, 1, −1, −1)` (`p = q = 2`) on the control and `N_B = N` (`p = 1`) on the target | F, P±, `G² = I`, Rt with `N_B`, Rc with `(N_A, N_B)` | exact: both relations. Written: positivity is the J/K map's, unchanged. With two NOTs, S4 bounds `p_B ≤ 1` and S5 balances `p_A = q_A`, so every odd `d` survives this pair of steps; identifying the NOTs is what couples S4 to S5 |
| **P±**, keeping all the algebra | `d = 7`: basis `u, x, v₂, v₃, y₁, y₂, y₃, z`, `N = diag(1, 1, 1, 1, −1, −1, −1, −1)` (`p = q = 3`), `M₀` flipping `v₂`, `M₁ = N M₀`, on `E₊` the exchanges `u ↔ x`, `v₂ ↔ v₃`, on `V₋` a `J ⊗ K` block | F, `G² = I`, Rt, Rc, the S1/S2 form; S4 fails (`A_x ≠ 0`) | exact: all of the algebra, and for the pure product state `(u + x) ⊗ (u + v₃)` and control effect `u + x` the target covector `w = (1; 1, 1, 1, 0, 0, 0, 0)`, so the minimum over target effects `u + b`, `|b| ≤ 1`, is `1 − |w_T| = 1 − √3 < 0`; the rational effect `b = (−2/3, −2/3, −1/3)` on `x, v₂, v₃` gives the value `−2/3` |

**Positive control:** `d = 3`, the complex CNOT in Pauli coordinates, meets every hypothesis with `p = q = 1`; S3 is
vacuous at `p = 1`. **Negative control:** `d = 2`, where `p + q = 1` admits no `p = q`.

***

## The frozen Lean text

The module is `verification/lean-mathlib/OIBridge/NativeGateBall.lean`. Its header, up to `namespace OIBridge`, is
frozen byte for byte:

```lean
/-
  OIBridge/NativeGateBall.lean — round NB-1: the dimension-free core of the finite native-gate
  ball no-go.

  The theorem this module serves. For two locally tomographic d-ball systems with their full
  self-dual effect cones and one common NOT involution `N`, an invertible linear map `G` with the
  classical CNOT action on the corners, the two native relations `(I⊗N) G (I⊗N) = G` and
  `(N⊗I) G (N⊗I) = (I⊗N) G`, and `G`, `G⁻¹` both sending product states into the maximal tensor
  cone, force `d ∈ {1, 3}`. That theorem is not a kernel theorem: its proof is layered, and this
  module certifies one layer of it.

  Proved here, the steps whose reasoning does not depend on `d`:
    §A  the averaging bound (S3) and its consequence for `p ≥ 2`;
    §B  the Lorentz test: a vector every unit effect keeps nonnegative lies in the cone;
    §C  the E₊ block vanishes for `p ≥ 2` (S4, entrywise), hence `p ≤ 1` given a nonzero block;
    §D  parity (S5): an injective map anticommuting with a linear map equates its ±1 eigenspaces;
    §E  a contraction with a contracting left inverse is an isometry (the last step of S1);
    §F  the count: `p ≤ 1`, `p = q`, `p + q + 1 = d` give `d = 1 ∨ d = 3`;
    `nb1_kernel_core`, the conjunction of `p_le_one`, `parity` and `dim_of_bounds`.

  Not proved here. The controlled form (S1), the block structure (S2) and the value identity that
  turns positivity of `G` into the hypothesis of `blocks_vanish` (S4) are proved by hand for every
  `d`; the round's probe checks the S1 and S2 solution spaces in exact arithmetic for `d = 2,…,7`
  and the value identity for `d = 5, 7`. Nothing here concerns whether OI supplies the common `N`
  on both factors (identical-copy covariance).

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
```

**Definition budget: zero.** The module carries no `def`, `abbrev`, `instance`, `structure`, `class` or `inductive`.

**The statements, FROZEN** — each theorem's text from `theorem` to the `:=` that opens its proof, byte for byte, shown
here with its proof elided:

```lean
theorem col_sq (p : ℕ) (K : Matrix (Fin p) (Fin p) ℝ) (i : Fin p) :
    (∑ j, ((if j = i then (1:ℝ) else 0) + K j i) ^ 2) = 1 + 2 * K i i + ∑ j, K j i ^ 2 := …

theorem averaging_bound (p : ℕ) (g : Fin p → ℝ) (K : Matrix (Fin p) (Fin p) ℝ)
    (hK : ∀ i j, K i j = - K j i)
    (h : ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →
      (∑ j, (g j + s * ((if j = i then (1:ℝ) else 0) + K j i)) ^ 2) ≤ (1 + s * g i) ^ 2) :
    ((p : ℝ) - 1) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0 := …

theorem vanish_of_bound (p : ℕ) (hp : 2 ≤ p) (g : Fin p → ℝ) (K : Matrix (Fin p) (Fin p) ℝ)
    (h : ((p : ℝ) - 1) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0) :
    (∀ j, g j = 0) ∧ (∀ i j, K j i = 0) := …

theorem lorentz_of_effects (p : ℕ) (hp : 1 ≤ p) (x0 : ℝ) (v : Fin p → ℝ)
    (h : ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 → 0 ≤ x0 + ∑ j, b j * v j) :
    0 ≤ x0 ∧ (∑ j, v j ^ 2) ≤ x0 ^ 2 := …

theorem blocks_vanish (p m : ℕ) (hp : 2 ≤ p)
    (A : Fin p → Matrix (Fin m) (Fin m) ℝ) (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ)
    (hB : ∀ r s, B r s = - B s r)
    (hpos : ∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →
      ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →
        0 ≤ (1 + s * A i k l)
          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) :
    (∀ r, A r = 0) ∧ (∀ r s, B r s = 0) := …

theorem p_le_one (p m : ℕ)
    (A : Fin p → Matrix (Fin m) (Fin m) ℝ) (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ)
    (hB : ∀ r s, B r s = - B s r)
    (hpos : ∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →
      ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →
        0 ≤ (1 + s * A i k l)
          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l)))
    (hne : ∃ r k l, A r k l ≠ 0) : p ≤ 1 := …

theorem parity {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]
    (P L : V →ₗ[ℝ] V) (hL : Function.Injective L)
    (hanti : ∀ v, L (P v) = - P (L v)) :
    Module.finrank ℝ (LinearMap.ker (P - LinearMap.id))
      = Module.finrank ℝ (LinearMap.ker (P + LinearMap.id)) := …

theorem isometry_of_contractions {E : Type*} [SeminormedAddCommGroup E] (M M' : E → E)
    (hM : ∀ v, ‖M v‖ ≤ ‖v‖) (hM' : ∀ v, ‖M' v‖ ≤ ‖v‖) (hinv : ∀ v, M' (M v) = v) :
    ∀ v, ‖M v‖ = ‖v‖ := …

theorem dim_of_bounds (p q d : ℕ) (hp : p ≤ 1) (hpq : p = q) (hd : p + q + 1 = d) :
    d = 1 ∨ d = 3 := …

theorem nb1_kernel_core :
    (∀ (p m : ℕ) (A : Fin p → Matrix (Fin m) (Fin m) ℝ)
      (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ),
      (∀ r s, B r s = - B s r) →
      (∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →
        ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →
          0 ≤ (1 + s * A i k l)
            + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) →
      (∃ r k l, A r k l ≠ 0) → p ≤ 1) ∧
    (∀ (V : Type) [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V] (P L : V →ₗ[ℝ] V),
      Function.Injective L → (∀ v, L (P v) = - P (L v)) →
      Module.finrank ℝ (LinearMap.ker (P - LinearMap.id))
        = Module.finrank ℝ (LinearMap.ker (P + LinearMap.id))) ∧
    (∀ p q d : ℕ, p ≤ 1 → p = q → p + q + 1 = d → d = 1 ∨ d = 3) := …
```

### The theorems, FROZEN by name and role

| role | theorem |
| --- | --- |
| verdict, `NB-1-CORE-PROVED` | `nb1_kernel_core` |
| S3 | `averaging_bound`, `vanish_of_bound`, `col_sq` |
| S4 given its value identity | `lorentz_of_effects`, `blocks_vanish`, `p_le_one` |
| S5 | `parity` |
| the last step of S1 | `isometry_of_contractions` |
| the count | `dim_of_bounds` |

Every theorem is followed, after the namespace closes, by its `#print axioms OIBridge.NativeGateBall.…` line. A
proof-only repair may add theorems named `nb1_shared_…`.

### The reference implementation

**Frozen**, and checked by `controls.py` at `E`: the header, the ten statement texts, the theorem names, one
`#print axioms` line per theorem, no definition, the forbidden tokens (`sorry`, `admit`, `native_decide`, `axiom`,
`unsafe`, `opaque`, `implemented_by`, `extern`), and no `set_option` but `linter.unusedSectionVars false`.

**Not frozen: the proofs.** The reference implementation is blob **`6d3ad5e7a1eb28bb327e9f2212519a2b80e5187a`**: ten theorems, no definition. A
proof-only repair — a change that leaves every frozen surface unchanged — is permitted as a later linear commit before
`E`; the result note names the reference blob and the module's blob at `E`, and, if they differ, states the departure
from the reference implementation and justifies it, which `controls.py` checks.

### Pre-freeze evidence — design evidence, not attestation

Each run is a `workflow_dispatch` run whose `head_sha` is the commit named, on the disposable branches `claude/nb1-dev`
and `claude/nb1-predicted`, never landed. None is a `check-run` attestation, and no predicate of the round reads them.
**GitHub records every one of them with the overall conclusion `cancelled`**: each was cancelled by hand once the jobs
it was dispatched to test had finished, and in each the aggregate `Numerical probes` job failed at its step
*Require every probe shard*, because shards it requires were cancelled. The table therefore records, job by job, what
finished and how; no run is described as green as a whole.

| run | head | what the head carries | the jobs that finished |
| --- | --- | --- | --- |
| 36708282201 | `509aeb75` on `claude/nb1-dev` | the first kernel module, nine theorems; no probe | `Mathlib bridge` failed at `Build`: `lorentz_of_effects` and `parity` did not elaborate (their `#print axioms` lines show `sorryAx`, inherited by `blocks_vanish` and `p_le_one`), the other five theorems compiled; `Lean kernel check` succeeded |
| 36708644229 | `1391b9a6` on `claude/nb1-dev` | the two proofs repaired; the first probe, 49 checks, with a seeded pseudo-random S3 replay; the workflow shard | `Mathlib bridge` built, `lean-axioms` at 5287 named results and no sorry, each of the nine theorems within `[propext, Classical.choice, Quot.sound]` (`dim_of_bounds` within `[propext, Quot.sound]`), and failed at the release gate's `lean-manuscript` step alone (the module unclassified); `Numerical probes / NB-1 native-gate ball` and `Lean kernel check` succeeded |
| 36709099600 | `5e5a529c` on `claude/nb1-dev` | the census family; `parity` without an involution hypothesis | `Lean kernel check` succeeded; the bridge and the NB-1 probe job were cancelled before they finished |
| 36709510536 | `7c66d5a4` on `claude/nb1-dev` | the probe made deterministic, 50 checks | `Numerical probes / NB-1 native-gate ball` and `Lean kernel check` succeeded; the bridge was cancelled before it finished |
| 36709850033 | `4f0fe7fb` on `claude/nb1-dev` | ten theorems with the verdict `nb1_kernel_core`; the deterministic probe, 51 checks; the workflow shard; the census family, whose note then named the verdict | `Mathlib bridge` succeeded, the release gate passing all 21 steps, `lean-manuscript` among them, `lean-axioms` at 5288 named results and no sorry, each of the module's ten axiom lines within `[propext, Classical.choice, Quot.sound]`, nineteen receipts holding and the 303 legacy records intact; `Numerical probes / NB-1 native-gate ball` and `Lean kernel check` succeeded |
| 36710673482 | `f4194631` on `claude/nb1-predicted`, tree `112b18e2cf3d9bd0996e0141c81145789c6e3069` | **the predicted execution tree less the result note**, as two linear commits from `D` — the first `63958435`, `D` plus this file's draft `7b9c1ecf1ce2d95e8069ec41036354dfe0db7e6f` alone — carrying the reference implementation `6d3ad5e7a1eb28bb327e9f2212519a2b80e5187a`, the probe `203446ece72e4420d32007e0d79f78f401279337`, `controls.py` `9b0bf6897b5db8dacc815ad552cebce4d4c6750d`, the workflow `df249b7c9c3ca8f3fd7a07ffdcdc5a28c176036d` (`D`'s with the frozen edit), `OIBridge.lean` `5143e4bc6320773d0e1b5578fc267ea4cb5960cd` and the census `242443c63a4a0183e8495fd2b86b39b222b54002` | overall conclusion `cancelled`. Twenty-five jobs succeeded: `Mathlib bridge` (job 109871436278), the release gate passing all 21 steps, `lean-manuscript` among them, `lean-axioms` at 5288 named results and no sorry, nineteen receipts holding and the 303 legacy records intact; `Numerical probes / NB-1 native-gate ball` (job 109871436330); `Lean kernel check`; every probe shard that runs on every event; and ten of act 42's fifteen dispatch-only exclusion shards. The other five exclusion shards — `n18:0`, `n18:1`, `n18:2`, `dfs:4` and `cubes:0` — were cancelled in progress, and the aggregate `Numerical probes` job consequently failed at *Require every probe shard*. Design evidence, not an exact-head attestation |

The run 36710673482 is evidence for the blobs it names and nothing else: it did not test this file's final text, which
differs from the draft it carried in four places only: this section's per-job record of the runs and this paragraph,
the wording of `D`'s certification, the recorded reason for the prediction, and the rule, in the execution and its checkpoint table, that attestation runs are
left to finish. On that branch, with a temporary result note carrying the
`NB-1-CORE-PROVED` sentence, the clause, the probe's line and the reference blob, `controls.py check HEAD --freeze
63958435` printed `controls: check OK`, and the same check at the execution commit without the note failed with
`note:absent`; the note was not kept. At the same tree, locally: `controls.py --self-test` OK,
`legacy_records_check.py` 303 records intact, `v3_verifier.py --receipts` nineteen receipts holding, and the census,
placement, voice and claims checks green.

***

## The exact-computation layer — the frozen probe

`verification/lean/native_gate_ball_probe.py`, blob **`203446ece72e4420d32007e0d79f78f401279337`**, is written before `F` and added by the
execution at stage 1 with exactly this blob, and the workflow runs it in its own shard at every execution commit from
stage 1 on. It uses Python integers and `Fraction`s for every value it asserts: **no floating point, no randomness and
no modular arithmetic.** Every rank is computed by exact Gaussian elimination over `ℚ`, and every point at which an
identity is tested is fixed in the file, so two runs print the same bytes. It exits 1 on any mismatch. Its statements
are exact arithmetic replayed; they are not kernel-certified, and the result note names them as this layer's.
Fifty-one checks:

1. **S1** (12): for `d = 2, …, 7` and `a = 0, 1`, the linear conditions of the corner and equator arguments cut
   `G(k_a ⊗ t)` down to exactly `span{k_a} ⊗ T`: nullity `d − 1`, the family inside it and of full rank.
2. **S2** (27): for `d = 2, …, 7` and every split, the exact solution space of the two tangent conditions on the unit
   sphere, read off as a polynomial (odd part zero, even part a multiple of `|t|²`), equals the family
   `α_r` at `(r, u)` and `(u, r)` `+ so(V₊) + so(V₋)`, of dimension `p + p(p − 1)/2 + q(q + 1)/2`; the transposed
   form is not a solution whenever `p ≥ 1`.
3. **S3** (2): for `p = 1, …, 8` the averaging identity
   `Σᵢ,ₛ [(1 + s gᵢ)² − |g + s(eᵢ + K eᵢ)|²] = −2[(p − 1)|g|² + ‖K‖²]` holds as an identity of polynomials of degree
   at most 2 in `g` and `K_{ij}` (`i < j`), proved by agreement on the fixed determining set `{0, e_v, 2e_v, e_v + e_w}`
   of the variables, 1634 points in all; and the same set rejects the identity with `p − 1` replaced by `p`.
4. **S4** (2): for `d = 5` (`p = 2`) and `d = 7` (`p = 3`), with the S2 family at every basis block entry, the value
   identity `(f ⊗ g)(G(s ⊗ t)) = (1, b)(I + Γ_ac)(1, t)` on the multi-affine grid, which determines it.
5. **The controls** (8): C3, the complex CNOT (Gaussian-integer arithmetic), meets F, `G² = I`, the S1/S2 form and both
   relations; C5, the J/K map, meets F, `G² = I`, the S1/S2 form and Rt, and fails Rc; C5, `J` and `K` are
   orthogonal complex structures and the value formula holds; C3, the same formula holds for the complex CNOT; C2N,
   the J/K map with `(N_A, N_B)` meets both relations; C7, the `d = 7` candidate meets F, `G² = I`, the S1/S2 form and
   both relations; C7, `w = (1; 1, 1, 1, 0, 0, 0, 0)`, `|w_T|² = 3 > 1`, and the rational effect's value is `−2/3`;
   C2, `p + q = 1` admits no `p = q`.

It ends with the line `native_gate_ball_probe: OK -- 51 checks: S1 d=2..7, S2 d=2..7 all p, S3 replay, S4 identity, controls C3 C5 C2N C7
C2` on success, which the result note carries verbatim, and `native_gate_ball_probe: FAILED …` otherwise. It runs in
about ten seconds.

***

## The question, FROZEN — one target

### `NB-1` — the finite native-gate ball theorem, certified in layers

**Do the dimension-free steps of the finite native-gate ball theorem hold in the kernel, as the frozen statements and
the verdict `nb1_kernel_core` state; and, with the frozen probe green at `E`, do the exact layer and the written proof
join them into the theorem that two locally tomographic `d`-balls with one common NOT and a native, two-sided positive
CNOT have `d ∈ {1, 3}`? The frozen answer is yes, in the three layers Hazard 1 names.**

| part | statement | witness | layer |
| --- | --- | --- | --- |
| S3 | `(p − 1)|g|² + ‖K‖² ≤ 0`; `p ≥ 2` forces `g = 0`, `K = 0` | `averaging_bound`, `vanish_of_bound` | kernel |
| S4 conclusion | the `E₊` block vanishes for `p ≥ 2`; `p ≤ 1` given a nonzero entry | `blocks_vanish`, `p_le_one` | kernel |
| S5 | equal `±1` eigenspace dimensions under an injective anticommuting map | `parity` | kernel |
| count | `d ∈ {1, 3}` | `dim_of_bounds` | kernel |
| S1, S2 for `d ≤ 7` | the solution spaces | the probe, sections 1 and 2 | exact computation |
| S4 value identity for `d = 5, 7` | the identity on every block entry | the probe, section 4 | exact computation |
| the countermodels' algebra and the `1 − √3` witness | as frozen above | the probe, section 5 | exact computation |
| S1, S2, the S4 identity for every `d`; the countermodels' positivity; the assembly | as frozen above | this file | written proof |

The answer is reported as one of two labels: `NB-1-CORE-PROVED`, the verdict `nb1_kernel_core` in the kernel with the
probe green at `E`; `NB-1-UNDECIDED`. The probe is not a label: green at `E`, it certifies its layer; red at `E`, the
round halts as a freeze failure.

## The controls

| role | object | what it is for |
| --- | --- | --- |
| the theorem is not vacuous | C3, the complex CNOT at `d = 3` | every hypothesis holds |
| the control-NOT relation is load-bearing | C5, the J/K map at `d = 5` | everything but Rc holds, and the map survives |
| one `N` is load-bearing | C2N, the J/K map with `N_A ≠ N_B` | both relations hold with two NOTs, and the map survives |
| positivity is load-bearing | C7 at `d = 7` | all of the algebra holds, and positivity fails at `1 − √3` |
| the count excludes even `d` | C2 | `p + q = 1` admits no `p = q` |
| the S3 certificate is not vacuous | the probe's S3 countercontrol | the determining set rejects a wrong identity |
| the S2 solution space is the stated one | the transposed form | excluded at every split with `p ≥ 1` |
| the frozen surfaces | `controls.py check E` | the statements, the header, the note, the surfaces and the paths |

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `NB-1` | `NB-1-CORE-PROVED` | **very high** | the nine non-verdict theorems built within the three axioms in design run 36708644229; the verdict is their conjunction, built with them in 36709850033 and at the predicted tree in 36710673482; the NB-1 probe job succeeded at the predicted tree; each of these runs was otherwise cancelled, as recorded above |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `NB-1-CORE-PROVED`

> In the kernel, at evidence level 2: the averaging bound and its consequence for `p ≥ 2` (`averaging_bound`, `vanish_of_bound`), the Lorentz test (`lorentz_of_effects`), the vanishing of every `E₊` block entry for `p ≥ 2` and hence `p ≤ 1` whenever an entry is nonzero (`blocks_vanish`, `p_le_one`), the equality of the `±1` eigenspace dimensions of a linear map under an injective map anticommuting with it (`parity`), the isometry step (`isometry_of_contractions`) and the count (`dim_of_bounds`), joined in the verdict `nb1_kernel_core`. In exact rational arithmetic replayed in CI, and not in the kernel, the round's probe computes the S1 and S2 solution spaces for `d = 2, …, 7` and every split `p + q = d − 1`, the S4 value identity for `d = 5` and `d = 7`, and the three minimality countermodels: without the control-NOT relation, the `d = 5` J/K map meets the frame, `G² = I` and the target relation, and its value on product states and effects obeys the complex CNOT's reduction formula exactly; with different NOTs `N_A ≠ N_B`, the same map meets both native relations; keeping the frame, `G² = I` and both relations, the `d = 7` candidate sends the product state `(u + x)⊗(u + v₃)` outside the maximal tensor cone, with minimum `1 − √3` over target effects. The theorem these layers serve — two locally tomographic `d`-balls with their full self-dual effect cones, one common NOT involution `N`, and an invertible `G` acting as CNOT on the corners, satisfying `(I⊗N)G(I⊗N) = G` and `(N⊗I)G(N⊗I) = (I⊗N)G`, with `G` and `G⁻¹` sending product states into the maximal tensor cone, force `d ∈ {1, 3}` — holds by the round's written proof, in which S1, S2 and the S4 value identity are proved by hand for every `d`; it is not a kernel theorem, and the two surviving countermodels are positive by the written reduction to the complex CNOT. Read for OI, the theorem is conditional on identical-copy covariance, `Σ(N⊗I)Σ⁻¹ = I⊗N`, which the corpus does not derive; nothing here claims that OI selects `d = 3`.

### `NB-1-UNDECIDED`

> The kernel verdict `nb1_kernel_core` was not obtained. The step at which the proof stopped is named, with what would settle it; the exact layer stands as computed, and the theorem for general `d` is not stated as a result of this round.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label, the label's sentence, the clause at
its mention `**THE CLAUSE, carried at this mention — the result.**`, the probe's summary line from the run at `E`, and
the reference blob and the module's blob at `E`. Outside the frozen sentence and the clause it does not contain any of
the phrases *OI selects*, *OI implies d*, *OI forces d*, *OI ⇒ d*, *OI => d*, *kernel theorem for every d*,
*kernel-proved for every d* or *kernel proof of the theorem for every d*, which `controls.py` checks.

| row | outcome |
| --- | --- |
| 1 | `NB-1-CORE-PROVED` |
| 2 | `NB-1-UNDECIDED` |

## The census, FROZEN

`verification/lean-manuscript-census.json` gains one family, appended last, the same under both outcomes: modules
`["NativeGateBall"]`, status `kernel-only`, no manuscript anchor, named

```text
the dimension-free core of the finite native-gate ball no-go: the averaging bound, the Lorentz test, the vanishing of the E+ block for p >= 2, parity, and the count d in {1, 3} (round NB-1, reconstruction)
```

with the note

```text
Round NB-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/preregistration.md. The kernel layer of the finite native-gate ball theorem: the steps whose reasoning does not depend on d, averaging_bound and vanish_of_bound (S3), lorentz_of_effects, blocks_vanish and p_le_one (S4), parity (S5), isometry_of_contractions (the last step of S1) and dim_of_bounds. The controlled form, the block structure and the S4 value identity are proved by hand for every d, and checked in exact arithmetic by native_gate_ball_probe.py (S1 and S2 for d = 2..7, the value identity for d = 5, 7); they are not kernel statements, and the theorem for general d is not a kernel theorem. Carried by no manuscript. Its reading for OI is conditional on identical-copy covariance of the local NOT, which the corpus does not derive.
```

## The workflow edit, FROZEN

After the act 45 shard, the job

```yaml
  probes_nb1:
    name: Numerical probes / NB-1 native-gate ball
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: NB-1 native-gate ball probe
        working-directory: verification/lean
        run: |
          echo "=== native_gate_ball_probe.py ==="
          python3 native_gate_ball_probe.py
```

and, in the aggregate `Numerical probes` job, `probes_nb1` after `probes_a45` in `needs`,
`NB1_RESULT: ${{ needs.probes_nb1.result }}` after `A45_RESULT`, `echo "nb1=${NB1_RESULT}"` after the act 45 echo, and
`test "${NB1_RESULT}" = success` after the act 45 test. `OIBridge.lean` gains `import OIBridge.NativeGateBall` directly
after `import OIBridge.HydroClosureBridge`.

***

## What no outcome licenses

- **No outcome says that OI selects `d = 3`**, that OI implies `d = 3`, or that OI supplies one `N` on both copies.
  The OI reading is conditional on identical-copy covariance, which stays an explicit, unsourced premise.
- **No outcome calls the theorem for general `d` a kernel theorem.** The kernel certifies the dimension-free steps;
  the exact layer certifies S1 and S2 for `d ≤ 7`; the rest is the written proof.
- **No outcome reads SWAP availability or composite unitary control into the premise**, nor justifies the premise by
  `HasQubitFactorExchange`, `RelabellingInvariant` or `gateFlow`.
- **No outcome extends the theorem** to non-ball systems, restricted effect cones, unrelated NOTs, or the one-sided
  variant, which stays open.
- **No outcome revises any earlier verdict, edits any manuscript or changes any roadmap row.**

## Non-doings

This round does not do any of the following:
- define anything in the module;
- import into the module anything beyond the four frozen Mathlib imports;
- edit any closed round's record, any manuscript, any built artifact or `verification/ROADMAP.md`;
- change the workflow beyond the frozen edit that adds the probe's shard;
- start the unrelated-NOTs or non-ball questions, or the one-sided variant.

## Evidence level

**2** for the kernel layer — Lean theorems, kernel-checked, every named result printing its axioms, each within
`propext`, `Classical.choice` and `Quot.sound`. The probe's statements are exact arithmetic replayed in CI, and the
written proof is a proof on paper; each is named as its own layer wherever it is cited.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/controls.py`, blob **`9b0bf6897b5db8dacc815ad552cebce4d4c6750d`**,
is written before `F` and added by the execution with exactly this blob. It imports nothing from the repository and
changes nothing; it reads `D` and the commit under check through `git`; it embeds every frozen text it compares
against.

`controls.py check <commit> [--freeze F]` fails unless all of the following hold:
- **the module**: the frozen header, no definition, no forbidden token or option, every theorem named in the frozen
  list or `nb1_shared_…` with one `#print axioms` line, each frozen statement byte for byte, and the verdict present
  exactly under `NB-1-CORE-PROVED`;
- **the result note**: the outcome line once; the label's sentence once and no other label's; the clause after its
  mention; the probe's summary line; the reference blob and the module's blob at `E` in backticks, and, if they differ,
  the words *departure from the reference implementation*; none of the forbidden phrases outside the frozen texts;
- **the probe** has its frozen blob; **the workflow** is `D`'s with the frozen edit; **`OIBridge.lean`** is `D`'s with
  the frozen import line; **the census** is `D`'s with the frozen family appended;
- **the paths** changed from `D` are exactly the governed ones; with `--freeze F`, `F` is `D` plus this file alone and
  this file is unchanged at the commit.

`controls.py --self-test` checks its constants against this file (the sentences, the clause, the header, every frozen
statement, the workflow job, the census family, both blobs and the probe's line); builds a synthetic execution for
each of the two rows and requires both to hold; and applies 31 mutation controls, each of which must fail with
its named code. Run at `D` beside this file, it prints:

```text
controls: the frozen constants match the preregistration beside this file
controls: 2 rows hold as frozen
controls: 31 mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear commits from `F`, each
with one parent:

1. **Stage 1 — the controls, the probe and the shard.** `controls.py` with its frozen blob; the probe with its frozen
   blob; the frozen workflow edit. No Lean changes.
2. **Stage 2 — the module without its verdict, and the census.** The reference implementation without
   `nb1_kernel_core` and its `#print axioms` line; the import line; the census family.
3. **Stage 3 — the verdict.** `nb1_kernel_core`, making the module the reference implementation; or, if it cannot be
   obtained, no verdict.
4. **The result note** `result.md`, whose commit is `E`; it carries the probe's summary line from the run at `E`'s
   predecessor and is confirmed by the run at `E`.

**Every attestation run is left to finish.** The dispatch runs whose `head_sha` is `F` and `E` run to completion, act
42's dispatch-only exclusion shards included; no job of either is cancelled, and each stands as exact-head evidence only
with every job, the aggregate `Numerical probes` job among them, concluded `success`.

**Lean is run in CI only** (`AGENTS.md` §A.40), and so is the probe as a CI job. A stage whose build fails is followed by
a fixing commit, never rewritten, and a fix may touch proofs only.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the probe is the frozen one, deterministic, and green in its own shard | `C3`: the probe's blob at stage 1 and at `E`; `Numerical probes / NB-1 native-gate ball` green at every execution commit and at `E` with the probe's `OK` line; the aggregate `Numerical probes` job green |
| every frozen statement is kernel-checked within the three axioms | `C8`: the dispatch run at `E`, run to completion with no job cancelled and every job concluded `success`; its `Mathlib bridge` build and the release gate's `lean-axioms` step |
| the module is classified and no manuscript changes | `C8`: the release gate at `E` — `lean-manuscript`, `staleness`, `voice`, `claims`, `mirror` — all green; `C7` |
| the frozen surfaces, the note and the paths | `C9`: `controls.py check E --freeze F` prints `controls: check OK` |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen surfaces unchanged** is repaired by later linear commits before `E`,
  and reported in the result note as a departure from the reference implementation.
- **A verdict that cannot be obtained** is reported `NB-1-UNDECIDED`, with the step named.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target or any frozen
  surface: a frozen statement ill-typed or false as frozen; the probe red at `E` with the frozen blob; a frozen
  surface that the release gate rejects. The round then halts under the specification's `S12`, with the result note
  naming the failure.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
