# NOTES-C19 — the clause's continuous group forces `Q3`; the Clifford chain above `Stab_C(Z⊗1)`

Round-4 node C19, opened 2026-10-11T05:06Z (`date -u`). Two parts, in the node's order. (i) The block-diagonal
`SU(2) × SU(2)` fixing `Z⊗1` (HO-22 item 3) forces `Q3`: its product orbit is every pure state, so every candidate
defect is carried to a product; written as a theorem with the group's definition. (ii) For `Stab_C(Z⊗1)` (order 384;
HO-24's cone with 192 defects), which defects survive each further Clifford generator (`actC S`, `actC J`,
`actC nflip`, …), the first generator killing every surgery-type exotic cone, and whether the order-11520 Clifford cone
(HO-25 item 1) is the only survivor pattern. Conventions as in NOTES-C11 and NOTES-C15 (computational basis
`|00⟩, |01⟩, |10⟩, |11⟩`, control first; `S = diag(1, i)`, `U_J = (I − i(X + Y + Z))/2`, `actC g = Ad(g ⊗ I)`,
`actT g = Ad(I ⊗ g)`, `nflip` = NOT, by HO-21's conjugation formulas; group elements mod scalars).

Hypothesis classification (standing rule 1): the groups are (b)-instances under test (invariance under the operations
named); H1–H3 are the composite-cone conditions (introduced, not OI premises); no OI inventory item is used. C21's
reading of these results is left to C21.

## S0 — predictions and decision rules, written before the first run of any C19 script (2026-10-11T05:06Z, `date -u`)

### Part (i) — Theorem C19-1 (written claim)
`H = {P₀ ⊗ U₀ + P₁ ⊗ U₁ : U₀, U₁ ∈ SU(2)}` (`P₀, P₁` the control's `Z` projectors). Every element commutes with `Z ⊗ 1`.
*(a) For every `ψ ≠ 0` there is `g ∈ H` with `gψ` a product. (b) If `K ⊆ Herm(4)` is a closed convex cone containing every
pure product state, invariant under conjugation by `H`, and self-dual for `tr(AB)`, then `K = Q3`. (c) The same holds for
every group containing `H`, and for every group whose orbit of the pure product states is all pure states; no defect
`I − cP_h` (`c > 1`) lies in such a `K`.* Proof plan: write `ψ = |0⟩⊗a + |1⟩⊗b`; `SU(2)` is transitive on spheres, so
`U₀a = |a|e`, `U₁b = |b|e` for one unit `e`, and `gψ = (|a|, |b|) ⊗ e`. So every pure state is in `K`, `Q3 = cone(pure
states) ⊆ K`, and `K = K* ⊆ Q3* = Q3`.

Checks (`experiments/c19_groups.py`): T1 — for exact `ψ` with Pythagorean norms, the explicit `U₀ = [[ā₀, ā₁], [−a₁, a₀]]/|a|`
(and `U₁` from `b`) lie in `SU(2)` and `gψ` has `det Ψ = 0`; edge cases `a = 0`, `b = 0`; HO-13's `φ₀ = (1, 2, 3i, −1 + i)`
with sympy's exact square roots. T2 — countercontrol: the finite `G₃₈₄` carries `φ₀` to no product (its orbit has minimum
normalised `|det Ψ|² > 0`). T3 — the carried defect `I − cP_{gψ}` pairs `1 − c < 0` with the product `P_{gψ}`.
Prediction: T1–T3 pass. Decision rule: T1–T3 pass ⇒ Theorem C19-1 recorded CONDITIONAL ([W], this NOTES; exact
instances); a failure of T1 voids the theorem.

### Part (ii) — the Clifford chain (exact computation)
Checks: K1 — orders, as signed permutations of the 16 table coordinates (lifted matrices for the state actions):
`G₃₈₄ = ⟨cnot, actT S, actT J⟩` has order 384 and equals the stabilizer of the coordinate `Z⊗1` (with its sign) in
`C₂ = ⟨cnot, actC J, actT J, actC S, actT S⟩` (order 11520); `actC S ∈ G₃₈₄`; `⟨G₃₈₄, actC nflip⟩` has order 768 (the
stabilizer of `±Z⊗1`); `⟨G₃₈₄, actC J⟩ = ⟨G₇₆₈, actC J⟩ = C₂`. K2 — HO-24's seed `h* = (10, 2 − 2i, −1 − 3i, 3 − i)` along
the chain: its orbit under `G₃₈₄`, `G₇₆₈`, `C₂` (sizes, stabilizer orders), minimum normalised `|det Ψ|²` (products) and the
minimum squared overlap with the seed (orthogonal pairs); a seed **survives** a step iff its orbit has no product and no
orthogonal pair (then S′ gives an invariant self-dual surgery with H1–H3 at every `c > 1` below the H1 and (CC) bounds,
recorded), and **dies** iff an exact product or orthogonal partner is found. K3 — the top of the chain keeps an explicit
cone: C15.2's `h_C` (recomputed orbit of 11520 rays, no product, no orthogonal pair), so no Clifford generator kills every
surgery cone. K4 — survivors with a nontrivial stabilizer at `C₂`: for representatives `g` of the conjugacy classes of
`C₂` (as signed permutations, lifted), every eigenspace of `g` defined over `ℚ(i)` is sampled at exact points and the
`C₂`-orbit tested; Pauli eigenvectors serve as countercontrol (they die: an anticommuting Pauli is an orthogonal partner).

Predictions (the K2–K4 outcomes are not known before the run; stated with low confidence): K1 as stated. K2: `h*` has
192 rays under `G₃₈₄`; under `actC nflip` its image has `⟨Z⊗1⟩ = −88/128` against `+88/128`, so the `G₇₆₈`-orbit has 384
rays; guess: it survives `G₇₆₈` and dies at `C₂` (an orthogonal partner appears once all Paulis act). K3 passes. K4: guess:
survivors with a nontrivial stabilizer exist (generic points of a multidimensional eigenspace of a non-Pauli element), so
the free-orbit pattern of `h_C` is not the only one.

Decision rules: the step at which `h*` dies (if any) is the answer for HO-24's cone; "the first generator killing every
surgery-type exotic cone" is recorded as *none in the Clifford chain* iff K3 passes, and the killing is then located at
the non-Clifford generator through Theorem C19-1 (the clause's group with `actT R_z(θ₀)` has `H` as identity component,
HO-22 item 3 [W]); "only survivor pattern" is decided negatively iff K4 exhibits an exact survivor with stabilizer of
order `> 1`, and otherwise recorded as not found within the searched family (no claim that the pattern is unique).
`VERDICT C19-EXACT` iff every check's computation completes with its controls behaving as stated (the survival outcomes
are recorded, not required).

## Runs (written 2026-10-11T05:12Z, `date -u`)
Run 1 (05:09:21Z, 35 s): 7/7, `VERDICT C19-EXACT`; replay byte-identical (`cmp`). Predictions: T1–T3, K1, K3 as stated;
K2 as guessed (`h*` survives `G₇₆₈`, dies at `C₂`); K4's guess ("survivors with a nontrivial stabilizer exist") FAILED —
none was found.

## Results

### C19-1 — the block-diagonal `SU(2) × SU(2)` forces `Q3` [W + X T1–T3]
**Definition.** `H = {P₀⊗U₀ + P₁⊗U₁ : U₀, U₁ ∈ SU(2)}`, `P₀ = |0⟩⟨0|`, `P₁ = |1⟩⟨1|` on the control; every element commutes with
`Z⊗1`. By HO-22 item 3 ([W] there) `H` is the identity component of the closed group generated by `cnot`, `actT J` and
`actT R_z(θ₀)`.
**Theorem C19-1.** *(a) For every nonzero `ψ ∈ ℂ²⊗ℂ²` there is `g ∈ H` with `gψ` a product. (b) Let `K ⊆ Herm(4)` be a
closed convex cone that contains every pure product state, is invariant under `X ↦ gXg†` for every `g ∈ H`, and is
self-dual for `tr(AB)`. Then `K = Q3`. (c) (b) holds for every group containing `H` and for every group whose orbit of the
pure product states is the set of all pure states; in particular no defect `I − cP_h` (`c > 1`) lies in such a cone.*
*Proof.* (a) Write `ψ = |0⟩⊗a + |1⟩⊗b`. For `a ≠ 0`, `U₀ = [[ā₀, ā₁], [−a₁, a₀]]/|a| ∈ SU(2)` has `U₀a = |a|e₀`; likewise
`U₁b = |b|e₀` (take `U = I` for a zero block). Then `(P₀⊗U₀ + P₁⊗U₁)ψ = (|a|, |b|) ⊗ e₀`. (b) By (a) and invariance,
`P_ψ = g†P_{gψ}g ∈ K` for every pure `ψ`; every PSD matrix is a nonnegative combination of pure states, so `Q3 ⊆ K`, and
`K = K* ⊆ Q3* = Q3` (PSD self-duality, JordanClassification.lean:84 [K]). (c) The proof of (b) uses only that every pure
state is a group image of a product; a defect `d = I − cP_h` in `K` would give `gdg† = I − cP_{gh} ∈ K` with `gh` a
product, pairing `1 − c < 0` with the product state `P_{gh} ∈ K`. ∎
Exact instances: T1 (five states, `φ₀ = (1, 2, 3i, −1 + i)` with exact square roots and the edge cases `a = 0`, `b = 0`);
countercontrol T2 (the finite `G₃₈₄` carries `φ₀` to no product: 384 rays, minimum `|det Ψ|² = 5/256`); T3.
Hypothesis classification (standing rule 1): the conclusion `Q3` follows from {invariance under `H` ((b)-instances for
the operations of `H`), H1, H3}; H1 and H3 are introduced (not OI premises); invariance under `H` is the (b)-question,
whose sourcing in OI is the bridge and origin threads' (S1)–(S4) (HO-22 item 5) and is not decided here.

### C19-2 — the Clifford chain above `Stab_C(Z⊗1)` [X K1]
As signed permutations of the 16 table coordinates: `C₂ = ⟨cnot, actC J, actT J, actC S, actT S⟩` has order 11520;
`G₃₈₄ = ⟨cnot, actT S, actT J⟩` is exactly the stabilizer of `Z⊗1` with its sign; `actC S ∈ G₃₈₄` (it adds nothing);
`G₇₆₈ = ⟨G₃₈₄, actC nflip⟩` is exactly the stabilizer of `±Z⊗1`, order 768; `⟨G₃₈₄, actC J⟩ = ⟨G₇₆₈, actC J⟩ = C₂`.

### C19-3 — HO-24's cone along the chain [X K2 + S′]
`h* = (10, 2 − 2i, −1 − 3i, 3 − i)` (HO-24's seed):
- `G₃₈₄` (and `actC S`): 192 rays, stabilizer 2, `min |det Ψ|² = 85/2048`, minimum squared overlap `25/2048` — survives;
  HO-24's cone is `actC S`-invariant (`actC S ∈ G₃₈₄`).
- `actC nflip`: HO-24's defect set is not invariant (its image has `⟨Z⊗1⟩ = −88/128` against `+88/128`); the `G₇₆₈`-orbit has
  384 rays (stabilizer 2), no product (`85/2048`), no orthogonal pair (minimum overlap `1/1024`), so with
  `c = 10001/10000` (H1 and (CC) exact) **`K(G₇₆₈·(I − cP_{h*}))` is an explicit `G₇₆₈`-invariant self-dual cone with H1–H3,
  `≠ Q3`** — EXOTIC-X for the stabilizer of `±Z⊗1`, CONDITIONAL on Theorem S′ in its finite form (C17.1: CONJECTURE
  [D], design run `38112813276` built) and on the Schmidt bound for H1 ([W], as C11.5). Weaker alternative it defeats:
  invariance under `Stab_C(±Z⊗1)` (the finite half with the control's NOT) with H1–H3 does not force `Q3`. The cone is
  invariant under the group's action; nothing is said about the operational availability of its operations.
- `actC J` (`C₂`): 5760 rays (stabilizer 2), two orthogonal partners of `h*` — `h*` dies: no rank-one surgery on its
  `C₂`-orbit with a common `c` is self-dual (Lemma C13-O; C18-1 for several values of `c`).

### C19-4 — no Clifford generator kills every surgery cone; the first that does is non-Clifford [X K3 + W]
At the top of the chain C15.2's `h_C` survives (recomputed: 11520 rays, `min |det Ψ|² = 198406621629/9790484550625`,
minimum overlap `164178929/3916193820250`, `c = 100001/100000`). So along `G₃₈₄ ⊂ G₇₆₈ ⊂ C₂` no Clifford generator kills
every surgery-type exotic cone (`actC S` adds nothing, `actC nflip` keeps a cone, `actC J` kills `h*` but keeps `h_C`). The
first generator that kills every exotic cone — surgery-type or not — is non-Clifford: with `actT R_z(θ₀)` the closure
contains `H` (HO-22 item 3, [W]) and Theorem C19-1 forces `Q3`. CONDITIONAL on HO-22 item 3 at its label for the
identification of the closure.

### C19-5 — survivor patterns at the top [X K4]
`C₂` has 21 conjugacy classes (mod scalars). For the 12 nontrivial class representatives with an eigenvalue in `ℚ(i)`,
every such eigenspace was sampled (one or two exact points each, 39 samples): 26 orbits reach a product, 13 contain an
orthogonal partner; the Pauli eigenvectors die as they must (4/4). No survivor with a nontrivial stabilizer was found;
the 8 classes without a Gaussian eigenvalue were not sampled. Whether `h_C`'s free-orbit pattern is the only survivor
pattern at `C₂` is not decided (OPEN; the search is not exhaustive).

## Verdict on node C19
- (i) Theorem C19-1: the block-diagonal `SU(2) × SU(2)` fixing `Z⊗1` forces `Q3` — its product orbit is every pure state,
  so every defect is carried to a product. With HO-22 item 3 this is the structural reason the clause with the gate
  forces `Q3` while its finite part does not.
- (ii) Along the Clifford chain above `Stab_C(Z⊗1)`: `actC S` adds nothing; `actC nflip` doubles HO-24's orbit and keeps an
  explicit cone (new, for `Stab_C(±Z⊗1)`); `actC J` reaches `C₂`, where HO-24's seed dies but `h_C` survives. No Clifford
  generator kills every surgery cone; the kill needs the non-Clifford, infinite-order datum.

## Gem classification (§A.31)
- NEW: Theorem C19-1 (sufficiency of the continuous block-diagonal group, with a one-line mechanism); the explicit
  `G₇₆₈` cone; the chain classification.
- CONFIRMING: HO-22 items 1 and 3 (orders; the product orbit of the block-diagonal group) recomputed.
- Assumption-watch marker: "more finite Clifford symmetry eventually forces `Q3`" is false along this chain — the full
  two-qubit Clifford group keeps explicit exotic cones (C15.2); forcing comes from the continuous half.

## What is not claimed
No kernel statement for C19-1 or the chain (exact computation and written proof); the identification of the clause's
closure with a group containing `H` is HO-22 item 3's [W]; nothing about the operational availability of the operations
of `H` or of the Clifford generators (invariance only); survivor patterns beyond the sampled eigenspaces.
