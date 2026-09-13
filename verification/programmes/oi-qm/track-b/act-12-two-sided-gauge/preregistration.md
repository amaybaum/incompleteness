# Track B act 12 — the two-sided invisible gauge and the fibre-Gram classification: CONTROL PLANE

Owner-called. This file is the whole of act 12's control plane and is merged **alone**, before any
execution object exists. It is a **classification round**, not a fork: every target below is
predicted positive, and the round's purpose is to determine the exact kinematic shape of the lift
freedom act 11 left open — before anyone asks what dynamical principle selects among it.

**Blob identity is authoritative.** The execution guard pins this file by content.

## Start state

| | |
| --- | --- |
| Merged `main` | `ba4524e886adb5954cb229d7ce4df216deec5a92` (PR #590) |
| Act 11's control plane | `../act-11-coherent-lift-gauge/preregistration.md`, blob `0f6d37fafd857d9e54d5dbff6d062cc360ea08e5` |
| Act 11's result (`GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`) | `../act-11-coherent-lift-gauge/result.md`, blob `7b24353ad626de6f930e41242334cb09945ae303` |
| Act 11's module | `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`, blob `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| Act 10's module (`one_admissible_at_every_anchor`) | `verification/lean-mathlib/OIBridge/AnchorRobustness.lean`, blob `b74202bc160918b32ca1b333da532a141ea8015d` |
| Act 7 layer 2's module (`AdmissibleDilationAt`, `admissible_permMatrix`) | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 7's governing preregistration (incl. `D3`) | `../act-07-dilation-choice/preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| Act 11's propagation freeze and amendment | `verification/audits/foundations/act11-scope-propagation-audit.md`, blob `cc6d5adb5682cd560d9342496fbaeeb957b760b9`; `…-open-frontier-amendment.md`, blob `50f74a0869789dd7188f850cf5ceee125596fb9b` |

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists

Act 11 left one target open in its result note, its `ROADMAP` row, and — after PR #590 — in the
manuscript's open-frontier inventory: a pair of coherent lifts of one visible family that is
**outside the maximal uniform weak stabilizer `𝒢ʷ_{a₀}` and different in relative evolution**. The
owner review that shaped this freeze established two facts about that target, and both are recorded
here as **corollaries of merged results**, not as targets of this round.

**First, the target as stated is positive, by a two-line construction on `GI2`'s own pair.** Take
`U_t = P(σ)` for every `t`, and `U'_0 = P(ρ·σ)`, `U'_t = P(σ)` for `t ≥ 1`. Each slice is one of
the two dilations `GI2` already proved admissible for `Aᵀ`, so both are coherent lifts. The forced
`K_0 = P(ρ) ∉ 𝒢ʷ_{a₀}`, so they are not weak-gauge-related. And
`U'_1 U'_0ᴴ = P(σ)P(ρσ)ᴴ ≠ 1 = U_1 U_0ᴴ`. `GL3` cancelled `GI2`'s relative difference only because
`GI2` held its orbit choice constant in time; letting the choice vary produces the difference. The
same pair **refutes** the converse "relative difference ⇒ weak-gauge-related". A symmetric
existence/impossibility freeze on this target would therefore predict at the wrong strength.

**Second, the reason it is positive is that act 11's gauge is one-sided.** Act 11 classified the
maximal uniform **right** visibility-preserving action `U ↦ U·K`. It never asked about the **left**.
Every left action `U ↦ L·U` with `L` block-diagonal across the visible fibres — a unitary mixing
of the ancilla *within* each fibre — preserves admissibility for **every** `U` and **every** family,
because the anchored readback `Σ_a |U_{(i,a),(j,a₀)}|²` sums over exactly the index `L` mixes. Yet
such `L` lie generically outside the right weak orbit. `GI2`'s own pair is a left in-fibre swap.
Physically the left action is output-side ancilla relabelling within a visible fibre; the right
action is input-side. Both are invisible.

**Third, the two-sided existence version is also positive, at `|A| = 1`, independently of `GI2`.**
There the two-sided gauge is row phases times column phases, `U ↦ D_L U D_R`. The exact family

```
H(z) = ½ · [[1, 1, 1, 1], [1, z, −1, −z], [1, −1, 1, −1], [1, −z, −1, z]],   |z| = 1
```

is unitary with every entry of modulus `½`, so every `H(z)` realizes the visible law `Γ_{ij} = ¼`.
The cross-ratio `C(U) = U_{00}U_{11} / (U_{01}U_{10})` is invariant under row and column phases,
and `C(H(1)) = 1`, `C(H(i)) = i`. So `U_t = H(1)` and `U'_0 = H(1), U'_t = H(i)` (`t ≥ 1`) are
coherent lifts of one constant family, not two-sided related, with `U'_1 U'_0ᴴ = H(i)H(1)ᴴ ≠ 1`.
The owner checked the matrix identities independently; the execution re-derives them in the kernel.

So neither the one-sided nor the two-sided existence question is a fork. What remains — and what
this round is — is the **classification**: there is a natural two-sided uniform invisible gauge;
its orbits are determined by a computable invariant; the visible law fixes exactly the diagonal of
that invariant; and the residual lift freedom is exactly the rest of it.

## The structural correction, FROZEN BEFORE ANYTHING ELSE

**Act 11's `𝒢ʷ_{a₀}` is the right factor of the two-sided uniform gauge classified here, not the
whole of it.** The statements "`𝒢ʷ_{a₀}` is the maximal uniform visibility-preserving right action
for `|V| ≥ 2`" and "the maximal uniform invisible gauge" are not the same statement, and the
second is not what act 11 proved. This round supplies the left factor and classifies the quotient
by the two-sided action the two factors generate. Nothing in act 11's merged record is revised;
its `GL1w` is consumed as the right-factor theorem it is.

## The objects, FROZEN

Throughout, `V` and `A` are finite types, `a₀ : A` the anchor, `P_i` the orthogonal projection
onto the visible fibre `i` — the span of `{e_{(i,a)} : a ∈ A}` — and `AdmissibleDilationAt`,
`CoherentLift`, `WeakAnchorStabilizer` and `GaugeRelated` are act 11's and act 7's, **unmodified**.

**The left fibre group `𝒢_L`.** Unitaries `L` on `V × A` that commute with every `P_i` —
equivalently, block-diagonal across visible fibres, `L ≅ Π_{i ∈ V} U(A)`. It is a group. It is
**anchor-independent**, unlike `𝒢ʷ_{a₀}`.

**Two-sided relatedness `∼₂`.** For lifts `U, U'` of one family:
`U' ∼₂ U ⟺ ∃ L : ℕ → 𝒢_L, ∃ K : ℕ → 𝒢ʷ_{a₀}, ∀ t, U'_t = L_t · U_t · K_t`. Time-dependent on both
sides, matching `GaugeRelated`'s convention. `GaugeRelated 𝒢ʷ_{a₀}` is the special case `L ≡ 1`.

**Fibre-Gram data.** For a single unitary `U`, and each visible fibre `i`, the `V × V` matrix
`G^{(i)}(U)_{jk} = ⟨P_i U e_{(j,a₀)}, P_i U e_{(k,a₀)}⟩`. Its diagonal is the anchored readback:
`G^{(i)}(U)_{jj} = readback(U)_{ij}`.

**Phase equivalence of Gram data `∼_D`.** `{G^{(i)}} ∼_D {G'^{(i)}} ⟺ ∃ D = diag(c), |c_j| = 1,
∀ i, G'^{(i)} = Dᴴ G^{(i)} D`. This is the action of the anchored phases of `𝒢ʷ_{a₀}`.

**Realizable Gram tuples.** A family `{G^{(i)}}_{i ∈ V}` of `V × V` matrices with
`G^{(i)} ⪰ 0`, `rank G^{(i)} ≤ |A|`, `Σ_i G^{(i)} = I`, and `G^{(i)}_{jj} = Γ_{ij}`.

## Five targets, FROZEN, all predicted positive

### `LG1` — the left group is invisible, maximal among uniform left actions, and not the right class

1. **Invisibility.** For every `L ∈ 𝒢_L`, every `Γ`, every `a₀`, every admissible `U`: `L·U` is
   admissible. Universal, over every family.
2. **Maximality under uniformity.** If a unitary `L` satisfies "`L·U` admissible for every
   admissible `U` of every family", then `L ∈ 𝒢_L`. The test family is the identity slice at every
   anchor, act 10's `one_admissible_at_every_anchor`: its admissible dilations have one anchored
   column in each fibre and range over every unit vector there, so an `L` preserving all of them
   maps each fibre into itself. **No `|V| ≥ 2` hypothesis is expected** — at `|V| = 1` there is one
   fibre and `𝒢_L` is everything. Record whichever hypothesis the proof needs.
3. **Escape from the right orbit.** A concrete `L ∈ 𝒢_L` and admissible `U` with `L·U` not
   `GaugeRelated 𝒢ʷ_{a₀}` to `U`, **on a carrier with `|V| ≥ 2`** so that act 11's maximality of
   `𝒢ʷ_{a₀}` applies and "the right orbit" means the maximal uniform one. The in-fibre anchor swap
   `L = P(swap((0,a₀),(0,a₁)))` on the identity family with `U = 1`, frozen on `V = Fin 2`,
   `A = Fin 2`, suffices, and this is the same object as the identity-family instance of `RO1`.

**Bounded reading:** `LG1` says there is a left invisible factor act 11 did not classify, and that
it is maximal *among uniform left actions considered alone*. It does **not** say the two-sided
action is jointly maximal — see hazard 5 — and it does not say it is the maximal invisible action
*of every kind*: non-uniform, family-specific invisible freedoms are neither asserted nor excluded.

### `RO1` — right-only insufficiency: the originally stated target, closed and bounded

Formalize the first corollary above as a theorem in act 11's vocabulary: two coherent lifts of one
family **on a carrier with `|V| ≥ 2`**, `¬ GaugeRelated (WeakAnchorStabilizer a₀) U U'`, with
`U'_t U'_sᴴ ≠ U_t U_sᴴ` for some `t, s`. **The `|V| ≥ 2` hypothesis is part of the statement**, because
the advertised reading names the *maximal uniform* right weak gauge, and act 11 proved `𝒢ʷ_{a₀}`
maximal only there — at `|V| = 1` it is explicitly not maximal, so a `|V| = 1` witness would be
formally valid and semantically mis-scoped. Either the `GI2` orbit-switching pair (already on
`V = Fin 2`) or the identity-family in-fibre swap frozen on `V = Fin 2`, `A = Fin 2` discharges it;
the execution records which, and may record both.

**The reading is fixed exactly:** quotienting by the maximal uniform **right** weak gauge is
insufficient to determine the relative evolution. **It is not** a statement about every gauge or
connection description, and the freeze forbids that inflation in terms. The relating element in
each instance is a **left** move, and the result note must say so — that is why `RO1` is closed
and why `LG1` is the right next object.

### `TG2` — the fibre-Gram orbit theorem

For single-slice dilations `U, U'` of the same `Γ` at the same anchor:

```
∃ L ∈ 𝒢_L, K ∈ 𝒢ʷ_{a₀}: U' = L·U·K   ⟺   {G^{(i)}(U')} ∼_D {G^{(i)}(U)}.
```

- **Forward.** Left `L` leaves every `G^{(i)}` invariant (it commutes with `P_i` and is unitary on
  the fibre); right `K ∈ 𝒢ʷ_{a₀}` acts on anchored columns by the phases `c_j`, so
  `G^{(i)} ↦ Dᴴ G^{(i)} D`. Both directions of the forward implication are one-line.
- **Converse.** Given `∼_D`, absorb `D` into a weak `K`; then the fibre-Gram families are equal.
  Equal Gram matrices give, for each `i`, a unitary `L_i` on the fibre mapping
  `{P_i U e_{(j,a₀)}}_j` to `{P_i U' e_{(j,a₀)}}_j` — the **Gram-isometry lemma**, the round's
  load-bearing technical step. Then `L·U·K` and `U'` **agree on the anchored columns**, and act
  11's `gaugeRelated_strong_iff_agree_on_anchor` absorbs the off-anchor freedom into a strong —
  hence weak — element. So the converse rides on act 11's orbit theorem and one lemma.

The **lifted form** over `ℕ`-indexed lifts follows slice-wise: `U' ∼₂ U ⟺ ∀ t, Gram data
`∼_D`-equivalent at `t`. State it; it is a corollary.

### `TG3` — the two-sided quotient is nontrivial for a single law, and dynamically distinct

Exhibit, on a single visible family, two admissible dilations with **inequivalent** fibre-Gram
data — so by `TG2` in different two-sided orbits — and two coherent lifts built from them with
`U'_t U'_sᴴ ≠ U_t U_sᴴ`. The intended witness is `H(1)`, `H(i)` at `|A| = 1`, `|V| = 4`, where
`𝒢_L` and `𝒢ʷ_{a₀}` are both diagonal phases and the cross-ratio `C` is the separating invariant;
`|A| = 1` is chosen precisely because the two-sided gauge is smallest there and the witness is
therefore strongest. A `|A| ≥ 2` instance may be recorded additionally but is not required.

**`GL2`'s pair and `GI2`'s pair are not `TG3` witnesses and are recorded as controls:** `GL2`'s is
right-related (inside one two-sided orbit by construction), and `GI2`'s is left-related (the
forced element is an in-fibre swap). Both lie **inside a single two-sided orbit**, and the execution
proves that of at least `GI2`'s, so the witness table shows the new quotient separating something
the old one could not.

### `SH1` — the shape theorem: exactly which Gram data are realizable

For a single slice: a family `{G^{(i)}}` is the fibre-Gram data of some admissible dilation of `Γ`
at `a₀` **iff** it is a realizable Gram tuple — `G^{(i)} ⪰ 0`, `rank G^{(i)} ≤ |A|`,
`Σ_i G^{(i)} = I`, `G^{(i)}_{jj} = Γ_{ij}`.

- **Necessity** is immediate: Gram matrices are PSD; a fibre has dimension `|A|`; the anchored
  columns are orthonormal so the fibre-Grams sum to `I`; the diagonal is the readback.
- **Sufficiency** is the content: factor each `G^{(i)} = W_iᴴ W_i` with `W_i` of `|A|` rows (PSD
  with rank bound), stack the `W_i` into `|V|` orthonormal columns indexed by `V × A`, and extend
  to a unitary. Each step is standard; the formal cost is in the factorization and the
  orthonormal-basis extension, and the execution reports honestly which is reached.

Together with `TG2`, `SH1` gives the statement the round is for:

> **The visible law is exactly the diagonal of the fibre-Gram data. The residual lift freedom,
> after the two-sided uniform gauge `𝒢_L × 𝒢ʷ_{a₀}`, is exactly the off-diagonal fibre-Gram data modulo
> the anchored phases — per time slice.**

## The preregistered predictions, and their strengths

| target | prediction | strength | what would falsify it |
| --- | --- | --- | --- |
| `LG1` (1), (3) | positive | full | nothing plausible; (1) is a one-line computation |
| `LG1` (2) | positive | high | a subtlety in the "every admissible `U`" quantifier at small `|A|`; record any hypothesis needed |
| `RO1` | positive | full | already verified numerically in the module's conventions on both instances |
| `TG2` forward | positive | full | — |
| `TG2` converse | positive | high | only the Gram-isometry lemma's formalization; the mathematics is standard |
| `TG3` | positive | full | the identities were checked independently by the owner and numerically here |
| `SH1` necessity | positive | full | — |
| `SH1` sufficiency | positive | **medium at kernel level** | the factorization or basis-extension may exceed the round formally; see the fallback below |

**`SH1` sufficiency fallback, frozen now.** If the kernel proof of sufficiency is not reached, the
execution reports `SH1` as **necessity at evidence level 2 plus sufficiency at evidence level 3**
(exact numerical certification on a stated finite family), labels it so, and does **not** promote
the combined statement. The shape sentence above is then asserted at the strength actually
reached. No other target has a fallback: each is level 2 or UNDECIDED.

**UNDECIDED remains a permitted label for every target**, reported with the obstruction.

## What none of these outcomes licenses

- **Nothing here says OI and QM are inequivalent.** The classification describes the lift space of
  a visible family; the finite observable-law correspondence is untouched.
- **The fibre-Gram data is a coordinate on the lift space, not a physical quantity.** The round
  does not claim it is observable, meaningful, or selected by anything.
- **Nothing here is a cross-time statement.** `TG2` and `SH1` are per slice. At the current
  `CoherentLift` level, coherence does not couple Gram data across time — act 11 recorded the
  cocycle as vacuous — and this round does **not** change that level or introduce a regularity,
  homogeneity, generated-evolution, or source-level coherence condition.
- **No selection principle is named, endorsed or excluded**, and nothing is said about
  connections or gauge fixings **in either direction**.
- **`P0` is not closed.** It moves: after this round the open question is **what additional
  condition selects or constrains the fibre-Gram trajectory across time**. That is the **next**
  frontier and is **not** this round's.
- **`D3`, `D5`, the direct-branch statement, and every merged label** are consumed unmodified.

## The relation to act 11, frozen to prevent two labels for one question

- Act 11's `GL1w` **stands as stated**: `𝒢ʷ_{a₀}` is the maximal uniform *right* visibility-preserving
  action for `|V| ≥ 2`. This round names it the right factor. The `|V| = 1` exception is inherited
  and untouched.
- Act 11's open target (outside `𝒢ʷ_{a₀}` **and** different relative evolution) is **closed
  positively by `RO1`**, and the result note, `ROADMAP`, and census must say so with the bounded
  reading — right-only insufficiency, carried by left moves — and nothing stronger.
- Act 11's `GI2` is re-read: it is a left in-fibre move, hence inside one two-sided orbit, hence
  precisely the case `TG2` predicts has *identical* Gram data. That is why its relative objects
  coincided. `GI2` is not revised; it is explained.
- **No manuscript is edited by this round.** The manuscript's §19.3.9 frontier statement remains
  accurate at its own level; whether to propagate the classification is a separate owner call.

## Immutable inputs

Cited and consumed **unmodified**:

- act 7 layer 2's `AdmissibleDilationAt`, `admissible_permMatrix`, `permMatrix_apply_eq`, and
  `admissible_mul_of_fixes_anchor`;
- act 10's `one_admissible_at_every_anchor`;
- act 11's `WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`, `weak_anchor_coeff_norm_one`,
  `gaugeRelated_strong_iff_agree_on_anchor`, `weak_of_preserves_every_admissible`,
  `gl3_constant_gauge_preserves_relative`, and `gi2_lifts_not_weakly_gauge_related` with its
  fourth conjunct;
- acts 1–10's labels; act 7 layer 2's `D5` control, which stands **NOT CERTIFIED**.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct
branch; `T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim
about what fraction of OI lies in the direct sector.**

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name

1. **This preregistration blob is merged into `main` before any execution-specific act 12 object
   enters the repository tree** — any Lean definition or proof about the left group, two-sided
   relatedness, fibre-Gram data or realizability, any search, any probe guard, any result artifact.
   **The single permitted exception is the analysis recorded inside this control-plane blob
   itself**, merged *as* the freeze — including the two corollary constructions and the Hadamard
   identities, which are recorded here so that no execution-specific artifact needs to precede it.
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

**The claim is scoped to the repository record.**

## Definition budget

The execution introduces **at most six** top-level definitions, and these are the six:

1. **`LeftFibreGroup`** (`𝒢_L`), as a predicate on unitaries. *Needed.*
2. **`TwoSidedRelated`** (`∼₂`), over `ℕ`-indexed lifts. *Needed.*
3. **`FibreGram`**, the per-fibre Gram matrix of the anchored columns. *Needed.*
4. **`GramPhaseEquiv`** (`∼_D`). *Needed* — `TG2` is stated over it.
5. **`RealizableGram`**, the four-condition predicate of `SH1`. *Needed if `SH1` is attempted at
   kernel level in either direction; unused otherwise.* *Conditional.*
6. **A relative-object or Hadamard-family abbreviation**, *if* `TG3` cannot be stated readably
   without one. *Conditional.*

**A seventh definition requires its own append-only amendment.** **No lift, gauge element, witness,
carrier or Gram tuple is a top-level definition** — each is a bound variable pinned by an equation
in the statement that needs it, as acts 10 and 11 did. Act 11's four definitions are **reused, not
redefined**.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide` — for every
target, with the single preregistered exception of `SH1` sufficiency under its frozen fallback.

## Named hazards

1. **Reading `TG3` as an inequivalence.** Two lifts differing is not two theories differing.
2. **Promoting the Gram data to physics.** It is the coordinate the two-sided gauge leaves; nothing
   here makes it observable or selected.
3. **Sliding from per-slice to cross-time.** `TG2`/`SH1` classify one slice. Any sentence about
   "the trajectory" that is not the explicit next-frontier statement is out of scope.
4. **Re-inflating `RO1`.** "Right-only quotient insufficient" is the claim; "gauge fixing cannot
   suffice" and "a connection cannot suffice" remain forbidden, exactly as after PR #589's review.
5. **Joint maximality is not claimed.** `LG1` (2) and act 11's `GL1w` establish maximality of the
   left and right factors *separately*. They do not by themselves establish that every uniformly
   invisible two-sided transformation `U ↦ L·U·K` factorizes through `𝒢_L × 𝒢ʷ_{a₀}`: in principle
   non-invisible effects of the two factors could cancel, and excluding that needs a separate
   joint-maximality theorem this round does not attempt. The round therefore calls `𝒢_L × 𝒢ʷ_{a₀}`
   **the two-sided uniform gauge generated by the separately maximal factors**, never "the maximal
   uniform two-sided action". Joint maximality is neither asserted nor excluded. `TG2` and `SH1` are
   unaffected: they classify the quotient by the *defined* action exactly, and need no theorem that
   it exhausts every conceivable invisible equivalence.
6. **Forgetting the anchor.** `𝒢ʷ_{a₀}` and the Gram data depend on `a₀`; `𝒢_L` does not. State
   which objects carry the anchor.
7. **Using `GL2`'s or `GI2`'s pair as a `TG3` witness.** Both lie inside one two-sided orbit; they
   are controls showing the quotient is *coarser* than act 11's, not witnesses that it is nontrivial.
8. **The `|A| = 1` witness read as a `|A| = 1` limitation.** `TG3` at `|A| = 1` is the *strongest*
   case, not a degenerate one: the gauge is smallest there.
9. **Rank.** Dropping `rank G^{(i)} ≤ |A|` from `SH1` makes sufficiency false; the constraint is
   load-bearing and must be stated.
10. **The Gram-isometry lemma stated for spanning families only.** It must handle linearly
    dependent anchored components in a fibre, which occur whenever `Γ_{ij} = 0` for some `j`.
11. **`SH1` sufficiency reported at level 2 when only level 3 was reached.** The fallback label is
    frozen; use it.
12. **Any sentence beginning "the selection principle is".** None is named. `C5` is neither named
    nor adopted.

## Non-doings

The round does not: choose or constrain the cross-time Gram trajectory; introduce regularity,
homogeneity, generated evolution or source-level coherence; say anything about connections or
gauge fixings in either direction; revise `GL1w`, `GL2`, `GL3`, `GI2` or any merged label; change
`D3`, `D5`, the direct-branch statement or the readback convention; compare Source A with B or C;
edit any manuscript; or say anything about Track I.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.**
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean, the
  result note, the probe guard (pinning this blob and certifying clause 5's ancestry), the
  `ROADMAP` propagation, and the census entry. **No manuscript changes.**
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. **`LG1`** — invisibility of `𝒢_L` universally; maximality among uniform left actions with the
   hypothesis actually needed; the escape witness;
2. **`RO1`** — the originally stated act 11 target closed positively, with the instance(s) used, the
   relating element shown to be a **left** move, and the bounded reading in this file's words;
3. **`TG2`** — the orbit theorem in both directions, the Gram-isometry lemma named, and the lifted
   slice-wise corollary;
4. **`TG3`** — the Hadamard witness with the cross-ratio invariant computed in the kernel, and the
   record that `GL2`'s and `GI2`'s pairs lie inside single two-sided orbits;
5. **`SH1`** — necessity at level 2; sufficiency at level 2, or at level 3 under the frozen
   fallback with the label stated, or UNDECIDED with the obstruction;
6. the shape sentence, asserted at the strength jointly reached by `TG2` and `SH1`;
7. what the outcomes do **not** license, in this file's wording, and the next frontier — cross-time
   selection of the Gram trajectory — named as **open and not this round's**;
8. the re-reading of `GI2` as a left move with identical Gram data;
9. the definition count against the six-slot budget, with conditional slots marked fired or unused;
10. the chronology certification, and the axiom table with one line per named result.
