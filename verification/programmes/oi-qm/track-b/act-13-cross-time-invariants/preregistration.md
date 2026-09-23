# Track B act 13 — cross-time invariants of the relative evolution: CONTROL PLANE

Owner-called. This file is the whole of act 13's control plane and is merged **alone**, before any
execution object exists. It is a **bounding round**: it freezes one family of cross-time data,
proves exactly which quotient of the lift each member of the family determines, and bounds the
family from both sides — the coarser members are blind to act 11's `GL2` mechanism by a universal
theorem, and the finest member is blind to a constant left move by an explicit pair. The round is
about **cross-time invariants**, not about a connection: nothing here asserts that a connection,
a gauge fixing or a selection principle exists, is needed, or is excluded.

**Blob identity is authoritative.** The execution guard pins this file by content.

## Start state

| | |
| --- | --- |
| Merged `main` | `aa4ac3a621a4967c1075fd129d49f88c724eecd0` (PR #599) |
| Act 12's control plane | `../act-12-two-sided-gauge/preregistration.md`, blob `5850238f290f0424ff677ff6d5cc2c039b1f58c2` |
| Act 12's result (`LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`) | `../act-12-two-sided-gauge/result.md`, blob `467d8be147b6ebd91f2eed12404566af74ac779f` |
| Act 12's module (`LeftFibreGroup`, `TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`) | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| Act 11's control plane | `../act-11-coherent-lift-gauge/preregistration.md`, blob `0f6d37fafd857d9e54d5dbff6d062cc360ea08e5` |
| Act 11's result (`GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`) | `../act-11-coherent-lift-gauge/result.md`, blob `7b24353ad626de6f930e41242334cb09945ae303` |
| Act 11's module (`StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`, `gl2_strong_gauge_moves_relative_candidate`, `gl3_constant_gauge_preserves_relative`) | `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`, blob `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| Act 10's module (`one_admissible_at_every_anchor`) | `verification/lean-mathlib/OIBridge/AnchorRobustness.lean`, blob `b74202bc160918b32ca1b333da532a141ea8015d` |
| Act 10's control plane (the strengthened chronology mechanism) | `../act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |
| Act 7 layer 2's module (`readback`, `AdmissibleDilationAt`, `admissible_permMatrix`, `admissible_mul_of_fixes_anchor`) | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 7's governing preregistration (incl. `D3`) | `../act-07-dilation-choice/preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| The live queue, `P0` row as act 12 left it | `verification/ROADMAP.md`, blob `5aa4235bf895b7c114feff406cc156d117bdb755` |

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists

Act 12 classified the per-slice quotient exactly: two dilations of one slice are related by the
two-sided uniform gauge `𝒢_L × 𝒢ʷ_{a₀}` iff their fibre-Gram data agree up to anchored phases
(`TG2`), the visible law is exactly the diagonal of that data and the residual per-slice freedom is
exactly its off-diagonal part (`SH1`). Its result note and the `P0` row record what that leaves:
**`P0` is two-part** — what selects or constrains the Gram/orbit trajectory across time, and what
determines the cross-time threading within those orbits — and act 11's `GL2` shows the second part
is not fixed even by the full per-time Gram trajectory, since a time-dependent strong right gauge
fixes every anchored column, hence every fibre-Gram matrix at every time, and changes the relative
evolution.

The question is therefore not what gauge freedom exists at a slice — act 12 answered that. It is
**temporal**: what data beyond all per-time Gram matrices are sufficient to determine the relative
evolution, and what least cross-time information distinguishes the `GL2`-type witnesses. This round asks exactly that,
in the following bounded form: it freezes **one** family of cross-time data — the two-time Gram data
of the dilation columns — and determines, for each member of the family, the exact quotient of the
lift it computes. Both answers this file predicts are earned by kernel objects, not by search.

**Three facts shape the freeze, and each is recorded here as a corollary of merged results or as a
frozen derivation, not as a target.**

**First, the relative evolution is exactly the lift modulo a constant right unitary.** Act 11's
`GL3` proves that a constant right gauge leaves every relative object `U_t U_sᴴ` unchanged. The
converse is one line: if `U'_t U'_sᴴ = U_t U_sᴴ` for all `t, s`, then with `K := U_0ᴴ U'_0`,
`U'_t = U'_t U'_0ᴴ U'_0 = U_t U_0ᴴ U'_0 = U_t K` for every `t`. So "determine the relative
evolution" means, exactly, "determine the lift up to one constant right unitary". This is the
quotient every statement below is measured against, and it is **not** act 12's two-sided action:
that action is time-dependent on both sides and does not preserve relative objects (`GL2` on the
right, `RO1` on the left), so "the relative evolution up to the two-sided action" is not a
well-formed quotient of relative evolutions and this file does not use the phrase.

**Second, every column-Gram datum is invariant under a constant left unitary, and a constant left
unitary can change the relative candidate.** For any unitary `W`, `(W U_t)ᴴ (W U_s) = U_tᴴ U_s`.
And on `V = Fin 2`, `A = Fin 2`, `a₀ = 0`, with the constant identity law, the lifts

```
U_0 = 𝟙,   U_t = X := P(swap((0,1),(1,1)))   (t ≥ 1)
U'_t = W · U_t,   W := P(swap((0,0),(0,1))) ∈ 𝒢_L
```

are both coherent: `𝟙` and `X` are admissible for the identity slice (`X` fixes both anchored
columns, so its anchored readback is the identity), and `W` is a left move, invisible by act 12's
`left_preserves_admissible`. Their column-Gram data agree at every pair of times, and their per-time
fibre-Gram data agree by act 12's `fibreGram_left_mul`. Their relative objects are `U_1 U_0ᴴ = X`
and `U'_1 U'_0ᴴ = W X Wᴴ = P(swap((0,0),(1,1)))`, the conjugate of `X` by `W`. The first fixes the
anchored column `e_{(0,0)}`; the second carries it to `e_{(1,1)}`, in the other visible fibre. So
the relative candidates differ at the entry `(0,0)`: `1` against `0`. The owner-side check is the
permutation arithmetic; the execution re-derives it in the kernel. **This pair is the reason the
family is bounded from above**: no datum invariant under constant left moves — and every member of
the column-Gram family is — can determine the relative candidate.

**Third, `GL2`'s pair has identical anchored columns at every time.** Its relating element is a
time-dependent element of the **strong** class, which fixes each anchored basis vector pointwise.
So every datum built from the anchored columns alone — the per-time fibre-Gram data, and their
cross-time extensions below — is identical for the two lifts, while their relative candidates
differ from `1/2` to `0` at the entry `(0,1)`. **This is the reason the family is bounded from
below**: the anchored-column members of the family are blind to `GL2`'s mechanism, and the freeze
says so as a universal theorem, not as an instance.

So the round is neither an existence fork nor a classification of a gauge. It is a **ladder**: a
frozen family of cross-time data, ordered by resolution, with the exact quotient each member
computes proved in both directions, and with the two obstructions above placed at the ends.

## The structural point, FROZEN BEFORE ANYTHING ELSE

**The two-sided action of act 12 does not act on relative evolutions.** `TwoSidedRelated` is
time-dependent on both sides; a time-dependent right factor changes relative objects (`GL2`) and a
time-dependent left factor changes them (`RO1`). The quotient in which the relative evolution lives
is the lift modulo a **constant right** unitary — any unitary, not a gauge class, since `GI2`'s pair
has identical relative objects with a constant relating element outside `𝒢ʷ_{a₀}`. Every "determines
the relative evolution" in this file means "determines the lift modulo constant right unitaries",
and every "determines up to" names the exact quotient it means. Nothing in act 12's merged record is
revised; `TG2`, `SH1`, `RO1` and `TG3` are consumed as the per-slice and existence results they are.

## The objects, FROZEN

Throughout, `V` and `A` are finite types, `a₀ : A` the anchor, `P_i` the orthogonal projection onto
the visible fibre `i`, and `readback`, `AdmissibleDilationAt`, `StrongAnchorStabilizer`,
`WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`, `LeftFibreGroup`, `TwoSidedRelated`,
`FibreGram`, `GramPhaseEquiv` and `RealizableGram` are act 7's, act 11's and act 12's,
**unmodified**. Lifts are `ℕ`-indexed families of unitaries `U : ℕ → U(V × A)`; the relative object
is `U_t U_sᴴ` and the relative candidate is `readback a₀` of its entrywise modulus squared, exactly
as acts 7 and 11 write them. For a single unitary `U` and a fibre `i`, `X_i(U)` is act 12's fibre
block `U.submatrix (fun a => (i, a)) (fun j => (j, a₀))`, so that `FibreGram a₀ U i = X_i(U)ᴴ X_i(U)`.

**The column cross-Gram `Ξ`.** For a lift `U` and times `t, s`, the `(V × A) × (V × A)` matrix

```
Ξ^{(t,s)}(U) := U_tᴴ · U_s,      Ξ^{(t,s)}_{pq} = ⟨U_t e_p, U_s e_q⟩.
```

It is the Gram matrix of the two column families `{U_t e_p}_p` and `{U_s e_q}_q`, and it is
**anchor-independent**. Its `(t,t)` slice is the identity for every unitary lift.

**The fibre cross-Gram `Ξ_i`.** For a lift `U`, a fibre `i` and times `t, s`, the `V × V` matrix

```
Ξ_i^{(t,s)}(U) := X_i(U_t)ᴴ · X_i(U_s),      (Ξ_i^{(t,s)})_{jk} = ⟨P_i U_t e_{(j,a₀)}, P_i U_s e_{(k,a₀)}⟩.
```

It **carries the anchor**. Its `(t,t)` slice is act 12's `FibreGram a₀ (U t) i`, definitionally, so
the per-time Gram trajectory is the diagonal `t = s` of this datum. Its fibre sum
`Σ_i Ξ_i^{(t,s)}` is the anchored-column block of `Ξ^{(t,s)}`, the matrix
`⟨U_t e_{(j,a₀)}, U_s e_{(k,a₀)}⟩`; that block is written as a submatrix of `Ξ` and is not a separate
definition.

**The family, ordered by resolution.** The round's frozen family is the column-Gram data at three
resolutions, each a function of the next:

| level | datum | what it sees |
| --- | --- | --- |
| 1 | the anchored block `Σ_i Ξ_i^{(t,s)} = (Ξ^{(t,s)})_{(j,a₀),(k,a₀)}` | anchored columns, fibre-summed |
| 2 | the fibre cross-Gram `Ξ_i^{(t,s)}`, all `i` | anchored columns, per fibre |
| 3 | the column cross-Gram `Ξ^{(t,s)}` | every column |

with the per-time fibre-Gram trajectory `{FibreGram a₀ (U t) i}_{t,i}` as **level 0**, the
`t = s` diagonal of level 2.

**Level 0 is read at two strengths, and the file keeps them apart.** The **raw** reading is
entrywise equality of the trajectory. The **phase-quotiented** reading is act 12's
`GramPhaseEquiv` at every `t` and every `i`. Act 12's two-sided action does not leave the raw datum
fixed: a weak right move with anchored phases `D` carries `FibreGram a₀ U i` to `Dᴴ · FibreGram a₀ U i · D`
(`fibreGram_mul_weak_apply`), so raw level-0 equality is **not** invariant under the whole
weak-right action and therefore does not itself compute act 12's per-slice quotient. What computes
that quotient exactly is the pointwise phase-equivalence class of the level-0 datum (`TG2`, both
directions). Raw level-0 equality is the **stronger, representative-level** equality: it is
sufficient to place two slices in one two-sided orbit, and it is not implied by membership in that
orbit. Every "level 0" below is the raw reading unless it says "modulo anchored phases".

**Nothing outside this family is frozen as a datum**: the dual
row-Gram data `U_t U_sᴴ` are the relative objects themselves and are not a "datum beyond" anything;
word or trace data of acts 11–12's objects are not adopted.

**Constant-right relatedness.** `U' ≈_R U ⟺ ∃ K ∈ U(V × A), ∀ t, U'_t = U_t K`. The relating
element is forced, `K = U_0ᴴ U'_0`, so membership is a computation.

**Constant-left relatedness.** `U' ≈_L U ⟺ ∃ W ∈ U(V × A), ∀ t, U'_t = W U_t`. Forced,
`W = U'_0 U_0ᴴ`.

Neither relation restricts the constant to a gauge class, and the freeze says why: the quotients
they name are the exact quotients of the relative evolution (`CT1`) and of `Ξ` (`CT2` (a)), and
neither theorem is true with the constant restricted.

## The frozen derivations, recorded as part of the freeze

These are recorded here so that no execution-specific artifact needs to precede this blob; they
are the analysis the round formalizes, not outcomes.

**The transformation laws.** Under the two-sided action `U_t ↦ L_t U_t K_t`:

```
Ξ^{(t,s)}  ↦  K_tᴴ · (U_tᴴ L_tᴴ L_s U_s) · K_s .
```

- If `L_t = W` is **constant**, `L_tᴴ L_s = 𝟙` and `Ξ ↦ K_tᴴ Ξ K_s`: `Ξ` is constant-left
  invariant.
- If `K_t` is **strong** (fixes each `e_{(j,a₀)}`), then so is `K_tᴴ`, and the anchored block of
  `K_tᴴ Ξ K_s` equals the anchored block of `Ξ`; the same holds fibre by fibre for `Ξ_i`, since
  `P_i U_t K_t e_{(j,a₀)} = P_i U_t e_{(j,a₀)}`. Levels 0, 1 and 2 are **strong-right invariant**.
- If `K_t` is **weak** with phases `c^t_j`, level 1 and level 2 transform by
  `(Ξ_i^{(t,s)})_{jk} ↦ conj(c^t_j) (Ξ_i^{(t,s)})_{jk} c^s_k`, the cross-time form of act 12's
  `fibreGram_mul_weak_apply`.
- A **time-dependent left** factor is not absorbed by any level: `L_tᴴ L_s` is a nontrivial in-fibre
  unitary and moves level 2 in general. This is why level 2 is predicted to pin the left factor to
  a constant.

**The exact quotients, derived.** With `U, U'` unitary lifts:

- `∀ t s, U'_t U'_sᴴ = U_t U_sᴴ ⟺ U' ≈_R U`. Forward: `K := U_0ᴴ U'_0` as above. Backward: `GL3`.
- `∀ t s, Ξ^{(t,s)}(U') = Ξ^{(t,s)}(U) ⟺ U' ≈_L U`. Forward: from `U'_tᴴ U'_0 = U_tᴴ U_0`,
  conjugate-transpose to `U'_0ᴴ U'_t = U_0ᴴ U_t` and multiply on the left by `U'_0`, giving
  `U'_t = U'_0 U_0ᴴ U_t = W U_t` with `W := U'_0 U_0ᴴ`. Backward: the first transformation law.
- `∀ i t s, Ξ_i^{(t,s)}(U') = Ξ_i^{(t,s)}(U) ⟺ ∃ W ∈ 𝒢_L constant, GaugeRelated (StrongAnchorStabilizer a₀) (W·U) U'`.
  Backward: the second transformation law. Forward, the load-bearing step: for each fibre `i` the
  two families `{P_i U_t e_{(j,a₀)}}_{(t,j)}` and `{P_i U'_t e_{(j,a₀)}}_{(t,j)}` in `ℂ^A` have the
  same Gram matrix, so they are related by one unitary `W_i` on the fibre; assembling the `W_i`
  gives `W ∈ 𝒢_L` with `U'_t e_{(j,a₀)} = W U_t e_{(j,a₀)}` for every `t` and `j`, and act 11's
  `gaugeRelated_strong_iff_agree_on_anchor` absorbs the off-anchor freedom into a time-dependent
  strong element. **The family here is `ℕ × V`-indexed, hence infinite**; act 12's
  `exists_unitary_of_gram_eq` is stated for finite families, and extending it — or reducing to a
  finite spanning subfamily, which exists since the span is at most `|A|`-dimensional — is the
  technical step whose formalization the freeze rates below `full`.

**The `GL2` separation entry.** `GL2`'s lifts are `U_0 = U_B`, `U_1 = 𝟙` and `U'_0 = U_B P(ρ)`,
`U'_1 = 𝟙`, with `ρ = swap((0,1),(1,1))` and `U_B` act 11's explicit matrix whose column `(0,1)`
is `s e_{(0,1)} − s e_{(1,0)}`, `s = √(1/2)`, and whose column `(1,1)` is `e_{(1,1)}`. Then
`Ξ^{(0,1)}(U) = U_Bᴴ` and `Ξ^{(0,1)}(U') = P(ρ)ᴴ U_Bᴴ = P(ρ) U_Bᴴ`, whose row `(0,1)` is row
`ρ(0,1) = (1,1)` of `U_Bᴴ`. So the two cross-Grams differ on the **off-anchor row `(0,1)`**: at the
entry `((0,1),(1,1))` the values are `0` and `1`, and at the entry `((0,1),(1,0))` — an off-anchor
row against an **anchored** column — the values are `−s` and `0`. Their anchored blocks agree.
**The permutation convention is act 7's**, `P(σ)_{pq} = if q = σ p then 1 else 0`, under which
`(P(σ) M)_{pq} = M_{σ p, q}` (act 11's `permMatrix_mul_apply`) and `P(g) P(h) = P(h·g)`; the
execution computes rather than reads off, as act 11's conjugation trap requires.

**The constant-lift variant of `GL2`.** `U_t = U_B` for every `t`; `U'_0 = U_B P(ρ)`, `U'_t = U_B`
for `t ≥ 1`. Both are coherent lifts of the constant family `Bᵀ`. The relating element is strong and
time-dependent, exactly as in `GL2`. Because the lift `U` is constant, every anchored column of
`Ξ^{(t,s)}(U') = K_tᴴ K_s` equals the corresponding anchored column of `Ξ^{(t,s)}(U) = 𝟙`; the two
cross-Grams differ only on the **off-anchor × off-anchor** block, `Ξ^{(0,1)}(U') = P(ρ) ≠ 𝟙` at the
entry `((0,1),(0,1))`, values `1` and `0` for `U` and `U'`. The relative objects are `U_1 U_0ᴴ = 𝟙` and
`U'_1 U'_0ᴴ = U_B P(ρ) U_Bᴴ`; the latter carries `e_{(1,0)}` to
`½ e_{(0,1)} + ½ e_{(1,0)} − s e_{(1,1)}`, so the relative candidates differ at the entry `(0,1)`:
`0` against `1/4`. This pair shows that the anchored *columns* of `Ξ` — the level-2 data together
with every off-anchor-row entry against an anchored column — do **not** separate every `GL2`-type
pair, which is why `CT3` (c) is frozen.

## Four targets, FROZEN

### `CT1` — the exact quotient of the relative evolution

For unitary lifts `U, U'`:

```
(∀ t s, U'_t U'_sᴴ = U_t U_sᴴ)   ⟺   U' ≈_R U.
```

**Directional witnesses, named separately** (§A.34): the backward direction is act 11's merged
`gl3_constant_gauge_preserves_relative`, consumed; the forward direction is this round's, by the
forced element `K = U_0ᴴ U'_0`. **Bounded reading:** the relative evolution is the lift modulo
constant right unitaries, and the threading question of `P0` is exactly the question of what pins a
lift modulo constant right unitaries. `CT1` does not say what pins it.

### `CT2` — what each level of the column-Gram family determines

**(a) Level 3.** For unitary lifts `U, U'`:

```
(∀ t s, Ξ^{(t,s)}(U') = Ξ^{(t,s)}(U))   ⟺   U' ≈_L U.
```

Both directions this round's; the forward by the forced element `W = U'_0 U_0ᴴ`, the backward by
the first transformation law. **Consequence, stated exactly:** the column cross-Gram determines the
lift up to one constant left unitary, hence the relative evolution up to **conjugation by one
constant unitary**, `U_t U_sᴴ ↦ W (U_t U_sᴴ) Wᴴ`. That quotient is finer than act 12's two-sided
one and is **not** the identity on relative candidates — `CT4` is the certificate.

**(b) Level 2.** For unitary lifts `U, U'`:

```
(∀ i t s, Ξ_i^{(t,s)}(U') = Ξ_i^{(t,s)}(U))
   ⟺   ∃ W, LeftFibreGroup W ∧ GaugeRelated (StrongAnchorStabilizer a₀) (fun t => W * U t) U'.
```

The backward direction is the second transformation law. The forward direction is the infinite-family
Gram-isometry step above, then act 11's orbit theorem. **Consequence, stated exactly:** the fibre
cross-Gram trajectory determines the lift up to a **constant** in-fibre left move and a
**time-dependent strong** right gauge — its residual is exactly `GL2`'s mechanism together with one
constant `𝒢_L` conjugation, and nothing else. With `CT1`: relative to the level-2 data, the
threading freedom of `P0` is exactly a strong-right family `K_t` modulo a constant, together with
one constant in-fibre frame.

**The phase-quotiented form is a corollary, not a target.** Allowing anchored phases `c^t_j` in the
level-2 equality replaces "strong" by "weak" on the right, by act 12's `weak_diagonal_phase` and
`weak_mul`, exactly as `TG2`'s converse absorbs `D`. It is stated only if the strict form lands, and
only if a cross-time phase-equivalence predicate is within the budget (slot 5).

**(c) The ladder sentence**, asserted at the strength jointly reached by (a) and (b):

> **Level 0 modulo anchored phases classifies the per-slice two-sided orbit of act 12 at every time,
> so it determines the lift up to act 12's time-dependent two-sided action, with raw level-0
> equality a stronger representative-level equality; level 2 up to a constant in-fibre left move
> and a time-dependent strong right gauge; level 3 up to a constant left unitary. No level
> determines the relative candidate.**

The first clause is act 12's `TG2` applied slice by slice and is consumed, not re-proved; the last
clause is `CT4`, and the sentence is not asserted without it.

### `CT3` — separation and blindness on the merged witnesses

**(G) Universal blindness of levels 0–2 to strong-right threading.** For every lift `U`, every
family `K : ℕ → StrongAnchorStabilizer a₀`, every `i, t, s`:
`Ξ_i^{(t,s)}(U·K) = Ξ_i^{(t,s)}(U)`, hence level 1 and level 0 agree as well. This is the second
transformation law as a theorem; it says no function of the anchored-column data at any resolution
separates any strong-right-related pair, so **the least separating column-Gram datum for
`GL2`-type pairs lies outside the anchored block**.

**(a) `GL2`'s pair is separated by level 3, at an off-anchor row.** The kernel certificate is one
entry of `Ξ^{(0,1)}`: the freeze expects `((0,1),(1,1))` with values `0` and `1` for `U` and `U'`,
and records that the off-anchor-row × anchored-column entry `((0,1),(1,0))` also separates, with
values `−s` and `0`. The execution may certify either entry and records which. Together with (G): **`GL2`'s pair
shares every per-time Gram matrix, every level-1 and every level-2 datum, and is separated by one
off-anchor entry of `Ξ`.**

**(b) The Hadamard pair is the trajectory-type control, not a threading witness.** Act 12's `TG3`
pair `U_t = H(1)`, `U'_0 = H(1)`, `U'_t = H(i)` (`t ≥ 1`) shares every per-time **visible law** and
has per-time Gram data already proved **inequivalent** at `t ≥ 1` (`hadamard_slices_not_twoSided`,
consumed). It is therefore not a pair sharing every per-time Gram matrix, and the freeze does not
present it as one. Its role here is the control on the other part of `P0`: at `|A| = 1` every
column is anchored, the three levels coincide, and `Ξ^{(0,1)}(U') = H(1)ᴴ H(i) ≠ 𝟙 = Ξ^{(0,1)}(U)` —
separated at the smallest level, because the difference is a difference of Gram trajectory, not of
threading. The certificate is the identity `H(1)ᴴ H(i) = 𝟙 ⟹ H(i) = H(1)`, refuted at the entry
`(1,1)`.

**(c) The anchored columns of `Ξ` do not separate every `GL2`-type pair.** The constant-lift variant
above: two coherent lifts of the constant family `Bᵀ`, strong-right related and time-dependent,
with every anchored column of `Ξ^{(t,s)}` equal at every `t, s` (so every level-2 datum and every
off-anchor-row × anchored-column entry equal), and relative candidates `0` against `1/4` at `(0,1)`.
The separating entry is off-anchor × off-anchor, `((0,1),(0,1))`, values `1` and `0`. **So the
least column-Gram datum separating all `GL2`-type pairs is not the anchored-column block of `Ξ`;
whether it is `Ξ` itself is the fork (d).**

**(d) Fork — does level 3 separate every `GL2`-type pair? NOT predicted.** By `CT2` (a), a
strong-right-related pair with equal `Ξ` at every `t, s` is constant-left related, `U' = C U` with
`U_tᴴ C U_t` strong for every `t`. The fork is whether such a pair can have distinct relative
candidates.

| Label | Statement | Earned only by |
| --- | --- | --- |
| **`CT3-d⁺`** | for every such pair the relative candidates agree at every `t, s` — level 3 separates every `GL2`-type pair | a universal theorem over strong-right-related, `Ξ`-equal pairs |
| **`CT3-d⁻`** | there is such a pair with distinct relative candidates — level 3 is blind to some `GL2`-type pair | an exhibited pair with the strong-right and `Ξ`-equality conjuncts proved and the candidates computed |

The freeze predicts **neither side at any strength**. `CT4`'s pair is not a candidate: its relating
element is a constant left `W ∈ 𝒢_L`, and the forced right element `U_tᴴ W U_t` is not strong at
`t = 0`. **Reporting the fork UNDECIDED is an allowed outcome.**

### `CT4` — insufficiency of the whole family, by the constant-left obstruction

Two coherent lifts of one family — the identity-law pair frozen above, on `V = Fin 2`, `A = Fin 2`,
`a₀ = 0` — with

- `Ξ^{(t,s)}(U') = Ξ^{(t,s)}(U)` for **all** `t, s`, hence equal level-2, level-1 and per-time Gram
  data;
- `U' ≈_L U` by a **constant** `W ∈ 𝒢_L`;
- relative candidates differing at the entry `(0,0)`: `1` against `0`.

**`CL1`, the mechanism, frozen with `CT4` as a corollary:** a **constant** left `𝒢_L` move can change
the relative candidate. This is the left counterpart of `GL3` failing: `GL3` says a constant right
gauge preserves every relative object; no analogue holds on the left, even for the invisible group,
because the readback of `W R Wᴴ` sees `Wᴴ` on the input side. `GI2`'s pair, a constant left move
with identical relative objects, is not a counterexample to `CL1` and `CL1` is not a revision of
`GI2`: `GI2`'s lifts are constant in time, so `W R Wᴴ = W Wᴴ = 𝟙 = R` there. **`CL1` is existential
and says nothing about every constant left move.**

**Bounded reading of `CT4`:** no member of the frozen family, up to and including the full column
cross-Gram, determines the relative candidate; any datum that does must fail to be constant-left
invariant, hence must depend on the dilation's rows, not only its columns. That is a statement about
the **shape** of a sufficient datum, not the naming of one; the row-Gram data `U_t U_sᴴ` are the
relative objects themselves and are not offered as an answer.

**`|A| = 1` is out of `CT4`'s reach, and the freeze says so.** There `𝒢_L` is the diagonal phases,
conjugation by which preserves every entrywise modulus, so the relative candidate is invariant under
constant `𝒢_L` moves and `CT4`'s obstruction is absent. `CT4` needs `|A| ≥ 2`; the witness has
`|A| = 2`. At `|A| = 1` the constant-left obstruction is carried only by `W ∉ 𝒢_L`, which `CT2` (a)
permits and `CT4` does not use.

## The preregistered predictions, and their strengths

| target | prediction | strength | what would falsify it |
| --- | --- | --- | --- |
| `CT1` forward | positive | full | nothing plausible; one forced element |
| `CT1` backward | positive | full | consumed from act 11's `GL3` |
| `CT2` (a), both directions | positive | full | — |
| `CT2` (b) backward | positive | full | the second transformation law |
| `CT2` (b) forward | positive | **medium at kernel level** | the infinite-family Gram-isometry step, or the finite-spanning-subfamily reduction, may exceed the round formally; see the fallback below |
| `CT2` (c) | asserted at the strength jointly reached by (a), (b) and `CT4` | — | — |
| `CT3` (G) | positive | full | — |
| `CT3` (a) | positive | full | the entry values were checked on act 11's explicit matrix; the execution computes them in the kernel |
| `CT3` (b) | positive | full | consumed from `TG3` plus one entry |
| `CT3` (c) | positive | full | the relative-candidate entry `1/4` was checked by hand; a slip there moves the certificate to another entry, not the label |
| `CT3` (d) | **not predicted** | — | — |
| `CT4`, `CL1` | positive | full | permutation arithmetic; the readback entries are integers |

**`CT2` (b) forward fallback, frozen now.** If the kernel proof is not reached, the execution reports
`CT2` (b) as **backward at evidence level 2 and forward UNDECIDED with the obstruction named**, and
the ladder sentence's level-2 clause is asserted as "at least up to" — the level-2 data are blind to
(at least) constant-left × strong-right moves — and not as an exact quotient. No level-3 numerical
fallback exists for a universal statement, and none is offered. No other target has a fallback:
each is level 2 or UNDECIDED.

**UNDECIDED remains a permitted label for every target**, reported with the obstruction.

## The frozen post-round sentence for `P0`, per outcome case

The `P0` row stays **OPEN** in every case. The sentence the execution appends to it is fixed here so
that the outcome cannot choose its own wording.

**Case A — `CT1`, `CT2` (a) and (b) in both directions, `CT3` (G), (a), (b), (c) and `CT4` land:**

> `P0` remains open and two-part, and the threading part is localized exactly: the fibre cross-Gram
> trajectory determines the lift up to one constant in-fibre left move and one time-dependent strong
> right gauge, and no column-Gram datum — up to and including the full two-time column Gram —
> determines the relative candidate, by a constant-left obstruction. The residual threading freedom
> relative to this datum is exactly a strong-right family modulo a constant together with one
> constant in-fibre frame; nothing in act 13 selects either, and no connection, gauge fixing or
> selection principle is asserted or excluded.

**Case B — as A, but `CT2` (b) forward UNDECIDED:**

> `P0` remains open and two-part. The fibre cross-Gram trajectory is blind to at least a constant
> in-fibre left move together with a time-dependent strong right gauge, and whether it is blind to
> nothing else is undecided; no column-Gram datum, up to and including the full two-time column
> Gram, determines the relative candidate, by a constant-left obstruction. No connection, gauge
> fixing or selection principle is asserted or excluded.

**Case C — `CT4` UNDECIDED (in either case above):** the clause "no column-Gram datum … determines
the relative candidate" is replaced by "the column cross-Gram determines the relative evolution up
to conjugation by one constant unitary, and whether that conjugation can move the relative
candidate is undecided", and the ladder sentence's last clause is not asserted.

**The fork `CT3` (d)** changes one clause only: `CT3-d⁺` adds "and the full column cross-Gram
separates every strong-right threading"; `CT3-d⁻` adds "and the full column cross-Gram is blind to
some strong-right threading"; UNDECIDED adds nothing.

**No case closes `P0`.** A characterization of what the frozen family determines is not a
selection of anything, and the row's label does not change.

## What none of these outcomes licenses

- **No selection principle is named**, endorsed or excluded. The round determines what the frozen
  data compute; it does not say what fixes them.
- **No connection and no gauge-fixing mechanism is asserted**, in either direction. "The threading
  freedom is exactly a strong-right family modulo a constant together with a constant in-fibre
  frame" is a statement about a quotient, not about a rule that picks a representative.
- **`P0` is not closed by a characterization.** It remains OPEN and two-part in every case above;
  what moves is the precision of the second part.
- **Nothing here says OI and QM are inequivalent.** Two lifts differing is not two theories
  differing; the finite observable-law correspondence is untouched.
- **The cross-Gram data are coordinates on the lift space, not physical quantities**, exactly as
  act 12 said of the per-time Gram data.
- **Nothing is imported from the substratum Lemma 24.1 round.** Its block-word traces, its
  `ST` labels and its "multi-time information" remark are objects of a different programme on a
  different carrier; this round neither consumes nor compares them, and a resemblance of vocabulary
  is not a bridge.
- **Nothing about Track I.**
- **`D3`, `D5`, the direct-branch statement, and every merged label** are consumed unmodified.

## The relation to acts 11 and 12, frozen to prevent two labels for one question

- Act 11's `GL2` **stands as stated** and is consumed as the threading witness; `CT3` (a) and (c)
  add the cross-Gram entries that separate it and its constant-lift variant, and revise nothing.
- Act 11's `GL3` is consumed as the backward direction of `CT1`; `CL1` is its left counterpart
  failing, and does not touch `GL3`.
- Act 11's `GI2` is **not revised** by `CL1`: its constant lifts have `W R Wᴴ = R` for the trivial
  reason, and act 12's reading of it as a left in-fibre move with identical Gram data stands.
- Act 12's `TG2` is consumed as the **phase-quotiented** reading of level 0 of the ladder: it
  classifies the per-slice two-sided orbit by the phase-equivalence class of the per-time
  fibre-Gram datum, not by its raw value, which the weak-right action moves by `Dᴴ G D`. `CT2` (b)
  is the cross-time extension of the raw reading and rides on the same orbit theorem. Act 12's `TG3` is consumed as the trajectory-type control; the
  freeze does not present the Hadamard pair as sharing per-time Gram data, because `TG3` proves it
  does not.
- Act 12's `RO1` is consumed as the time-dependent left move; `CL1` is the constant one.
- **No manuscript is edited by this round.** Whether to propagate the ladder is a separate owner
  call.

## Immutable inputs

Cited and consumed **unmodified**:

- act 7 layer 2's `readback`, `AdmissibleDilationAt`, `admissible_permMatrix`, `permMatrix_apply_eq`,
  `mul_permMatrix_apply` and `admissible_mul_of_fixes_anchor`;
- act 10's `one_admissible_at_every_anchor`;
- act 11's `StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`,
  `strong_mem_weak`, `conjTranspose_mul_mem_unitaryGroup`, `gaugeRelated_strong_iff_agree_on_anchor`,
  `permMatrix_mul_apply`, `gl3_constant_gauge_preserves_relative`, and
  `gl2_strong_gauge_moves_relative_candidate` with its explicit matrices;
- act 12's `LeftFibreGroup`, `TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
  `fibreGram_left_mul`, `fibreGram_mul_weak_apply`, `left_preserves_admissible`, `one_leftFibreGroup`,
  `inFibreSwap_leftFibreGroup`, `weak_diagonal_phase`, `weak_mul`, `exists_unitary_of_gram_eq`,
  `twoSidedRelated_iff`, `hadamard_slices_not_twoSided` and `hadamard_lifts_not_twoSided`;
- acts 1–12's labels; act 7 layer 2's `D5` control, which stands **NOT CERTIFIED**.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct
branch; `T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim
about what fraction of OI lies in the direct sector.**

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name, with the archive rule of PR #599

1. **This preregistration blob is merged into `main` before any execution-specific act 13 object
   enters the repository tree** — any Lean definition or proof about cross-Grams, constant
   relatedness or the frozen pairs, any search, any probe guard, any result artifact. **The single
   permitted exception is the analysis recorded inside this control-plane blob itself**, merged *as*
   the freeze — including the transformation laws, the exact quotients, the frozen pairs and their
   entry values, which are recorded here so that no execution-specific artifact needs to precede it.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR.**
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and
   `H` the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B`
   itself a descendant of `B`**, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
   `B`, for `H`, and for every enumerated commit alike.
7. **Archive mode, adopted 2026-09-13 (PR #599).** After the execution PR merges, neither `HEAD` on
   `main` nor the head of a later pull request is the execution head — both reach sibling rounds
   merged before or after, and a sibling branched before this freeze is exactly the side history
   clause 5 refuses. The predicate is a property of the object that was reviewed, so after the merge
   the guard **re-runs the same strong check against the sealed execution head pinned by SHA,
   together with the merge commit that carried it**: the pinned merge commit's second parent must
   be the sealed head; the sealed head must pass clause 5 against `B` exactly as in its own PR run;
   and **both the sealed head and the merge commit must be reachable from the current target** —
   the real `pull_request.head.sha` in PR CI, `HEAD` otherwise — each **fail-closed**. Nothing about
   `B` or the blob pin changes. The switch to archive mode is a pin-only change to the guard,
   recording the two SHAs and nothing else.

**The claim is scoped to the repository record.**

## Definition budget

The execution introduces **at most six** top-level definitions, and these are the six:

1. **`CrossGram`** (`Ξ^{(t,s)} = U_tᴴ U_s`), over `ℕ`-indexed lifts, anchor-free. *Needed.*
2. **`FibreCrossGram`** (`Ξ_i^{(t,s)} = X_i(U_t)ᴴ X_i(U_s)`), carrying the anchor; its `(t,t)`
   slice is act 12's `FibreGram` definitionally. *Needed.*
3. **`ConstRightRelated`** (`≈_R`), the constant unrestricted to a class. *Needed* — `CT1` is
   stated over it.
4. **`ConstLeftRelated`** (`≈_L`), likewise. *Needed* — `CT2` (a) is stated over it.
5. **A cross-time phase equivalence** on fibre cross-Gram data, *if* the phase-quotiented corollary
   of `CT2` (b) is attempted; unused otherwise. *Conditional.*
6. **A relative-object or relative-candidate abbreviation**, *if* the fork `CT3` (d) or `CT4`
   cannot be stated readably without one. *Conditional.*

**A seventh definition requires its own append-only amendment.** **No lift, gauge element, witness,
carrier, cross-Gram value or pair is a top-level definition** — each is a bound variable pinned by
an equation in the statement that needs it, as acts 10, 11 and 12 did. The level-1 anchored block
is a submatrix expression of slot 1 or a fibre sum of slot 2, not a definition. Acts 11's and 12's
definitions are **reused, not redefined**.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide` — for every
target, with the single preregistered exception of `CT2` (b) forward under its frozen fallback,
which is UNDECIDED-with-obstruction and not a lower evidence level.

## Named hazards

1. **Writing "up to the two-sided action" of a relative evolution.** That action does not preserve
   relative objects; the quotient is constant-right, by `CT1`, and every "up to" names its quotient.
2. **Reading `CT2` (a) as sufficiency.** The column cross-Gram determines the relative evolution up
   to conjugation by a constant unitary, and that conjugation moves the relative candidate (`CT4`).
   "Determines the lift up to `≈_L`" and "determines the relative candidate" are different claims,
   and only the first is made.
3. **Restricting the constants to a gauge class.** `CT1` and `CT2` (a) are false with `K` or `W`
   restricted; `GI2`'s constant element is outside `𝒢ʷ_{a₀}`.
4. **Presenting the Hadamard pair as sharing per-time Gram data.** `TG3` proves the opposite; the
   pair is the trajectory-type control and is labelled so.
5. **Using `CT4`'s pair as the fork witness.** Its relating element is a constant left move, and its
   forced right element is not strong; it is not a strong-right-related pair.
6. **Reading `CL1` against `GI2`.** `GI2`'s lifts are constant, so conjugation is trivial there;
   `CL1` is existential and revises nothing.
7. **Reading `CL1` at `|A| = 1`.** The in-fibre group is phases there and the obstruction is absent;
   the witness has `|A| = 2` and the scoping is part of the statement.
8. **Forgetting the anchor.** `Ξ` is anchor-free; `Ξ_i` and the level-1 block carry `a₀`. State
   which.
9. **The conjugation trap, again.** Under act 7's convention `P(g) P(h) = P(h·g)` and
   `(P(σ) M)_{pq} = M_{σ p, q}`; forced elements and separating entries are computed, never read off
   a constructor.
10. **The Gram-isometry step for an infinite family.** Act 12's lemma is finite; `CT2` (b) forward
    needs the `ℕ × V`-indexed version or a finite-spanning-subfamily reduction, and the freeze rates
    it medium for that reason. Reporting it at full when only the backward direction landed is the
    specific error the fallback exists to prevent.
11. **Sliding from "least separating datum" to "least sufficient datum".** `CT3` bounds what
    separates the merged witnesses; `CT4` says no member of the family is sufficient. Neither names
    a smallest sufficient datum, and the file does not.
12. **Promoting the shape remark to a datum.** "A sufficient datum must depend on rows" is a
    consequence of `CT4`, not a proposal; the row-Gram data are the relative objects and are not
    offered.
13. **Any sentence beginning "the selection principle is", "the connection is", or "the gauge
    fixing is".** None is named.
14. **Importing the substratum round's multi-time vocabulary.** Block-word traces and `ST` labels
    are not this round's objects; the word "cross-time" here refers to the frozen family only.
15. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after
    the merge.** See clauses 5 and 7.

## Non-doings

The round does not: name, endorse or exclude a selection principle; assert or deny that a
connection or gauge fixing exists or suffices; propose a sufficient cross-time datum; adopt any
datum outside the frozen column-Gram family; introduce regularity, homogeneity, generated evolution
or source-level coherence; change `CoherentLift`'s `ℕ`-indexing; revise `GL1s`, `GL1w`, `GL2`,
`GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1` or any merged label; change `D3`, `D5`, the
direct-branch statement or the readback convention; consume or compare anything from the substratum
Lemma 24.1 round; compare Source A with B or C; edit any manuscript; or say anything about Track I.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.**
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean, the
  result note, the probe guard (pinning this blob, certifying clause 5's ancestry, and carrying the
  clause-7 archive mode with its pins unset), the `ROADMAP` propagation, and the census entry.
  **No manuscript changes.**
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**
- **After the merge, one pin-only change** records the sealed execution head and its merge commit in
  the guard, switching it to archive mode per clause 7.

## Allowed final report

1. **`CT1`** — the exact quotient, with the forward direction's forced element and the backward
   direction cited to `GL3`;
2. **`CT2` (a)** — both directions, with the conjugation consequence stated exactly and its
   non-sufficiency cross-referenced to `CT4`;
3. **`CT2` (b)** — backward at level 2; forward at level 2, or UNDECIDED with the obstruction under
   the frozen fallback; the phase-quotiented corollary only if reached and within budget;
4. **`CT2` (c)** — the ladder sentence at the strength jointly reached, its last clause only with
   `CT4`;
5. **`CT3`** — (G) as a universal theorem; (a) with the certified entry of `Ξ^{(0,1)}` named; (b)
   as the trajectory-type control with `TG3` cited and the pair's per-time Gram inequivalence
   stated; (c) with the certified off-anchor × off-anchor entry and the relative-candidate values;
   (d) as `CT3-d⁺`, `CT3-d⁻` or UNDECIDED, with the route to the label;
6. **`CT4`** with **`CL1`** — the pair, the constant `W`, the equal cross-Grams at every `t, s`, the
   relative-candidate entries, and the `|A| ≥ 2` scoping;
7. the frozen `P0` sentence for the case reached, verbatim, and the row's label unchanged;
8. what the outcomes do **not** license, in this file's wording;
9. the relation to acts 11 and 12 as frozen — `GL2`, `GL3`, `GI2`, `TG2`, `TG3` and `RO1` consumed
   and none revised;
10. the definition count against the six-slot budget, with conditional slots marked fired or unused;
11. the chronology certification, naming the property certified and the archive-mode pins as unset
    at execution;
12. the axiom table with one line per named result.
