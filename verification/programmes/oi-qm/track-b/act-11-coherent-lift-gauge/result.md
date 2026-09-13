# Track B act 11 — the coherent-lift stabilizer no-go: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`0f6d37fafd857d9e54d5dbff6d062cc360ea08e5`, merged into `main` as
`6cff07cc0655124f1f29e04b156cc05a3d717a48` (PR #588) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `6cff07cc0655124f1f29e04b156cc05a3d717a48` (merge of PR #588) |
| This round's frozen control plane | `preregistration.md`, blob `0f6d37fafd857d9e54d5dbff6d062cc360ea08e5` |
| Act 5's result (the diagonal-phase countercontrol) | `../act-05-source-a-candidate/result.md`, blob `c8cdd11a96f547d10763caf1922f84b2afaae92f` |
| Act 7 layer 2's result (`DC1`) | `../act-07-dilation-choice/layer-2-result.md`, blob `02f93a1c3ec485b5f46b8e02ff52ca4f73e0ee89` |
| Act 7 layer 2's module | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 9's result | `../act-09-readback-robustness/result.md`, blob `f918e7b405dec35e01e9d53ca0dd90eb56c34df4` |
| Act 10's result | `../act-10-anchor-robustness/result.md`, blob `ec9a6e0d8a7019805aca069abc39f90d632b6a2b` |
| This round's module | `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` |

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Outcome, in one line

**`GL1s`, `GL1w`, `GL2` and `GL3` all landed, and `GI2` landed — which the freeze predicted at no
strength on either side.** Ordinary coherent lifting does not restore uniqueness of the relative
evolution (`GL2`), and the **lift space** is not exhausted by the maximal uniform weak stabilizer
(`GI2`).

**Two scope statements belong in the headline, not the footnotes.** First, `GI2` is about the lift
space **only**: its witness is proved to have the *same* relative object at every pair of times, so
it is not evidence of non-gauge ambiguity in the relative evolution, and `GL2` is the round's only
relative-evolution no-go. Second, "all targets landed" means the **structural** content of each
target; the Lie-group identifications and dimensions that `GL1s` and `GL1w` state are recorded as
arithmetic and are **not** kernel-certified here. Both are made precise below.

## `GL1s` — the strong stabilizer

`strong_mem_weak`, `weak_anchor_coeff_norm_one`, `strong_column_offAnchor_eq_zero`,
`strong_eq_one_of_ancilla_subsingleton`, `card_offAnchor`,
`gaugeRelated_strong_iff_agree_on_anchor`.

The strong class is the identity on `S_{a₀}` by definition, and
`strong_column_offAnchor_eq_zero` proves the complementary half: every off-anchor column is
orthogonal to `S_{a₀}`. That is the `S_{a₀}^⊥`-invariance which makes the block structure, and
`card_offAnchor` proves the complement's index set has exactly `|V| · (|A| − 1)` elements.
`strong_eq_one_of_ancilla_subsingleton` gives the **`|A| = 1` triviality**. The orbit classification
holds in both directions, the reverse via the forced element `K = Uᴴ U'`.

**`GL1s`'S DIMENSION IS A LOWER BOUND ON INVISIBLE FREEDOM, NOT ITS MEASURE.** The freeze says so and
the module's docstring repeats it.

**A scope statement about what is and is not kernel-checked here.** What the module proves is the
**block characterization** — identity on `S_{a₀}`, unitary on `S_{a₀}^⊥` — together with the
complement's **cardinality**. The isomorphism type `U(|V|(|A| − 1))` and its real dimension
`(|V|(|A| − 1))²` follow from the standard dimension of a unitary group and are **recorded here as
arithmetic, not as theorems of this module**. Nothing in the round's conclusions rests on the
dimension count.

## `GL1w` — the weak stabilizer, its invisibility, and its maximality for `|V| ≥ 2`

`weak_preserves_admissible` is the invisibility direction: right multiplication by the weak class
preserves admissibility, hence the whole visible family. This is what makes "invisible freedom" the
right name for the weak class and not the strong one.

**`weak_of_preserves_every_admissible` is the maximality theorem, and it is proved by exactly two
test dilations** rather than by a search over unitaries:

1. the **identity** dilation of the identity slice — admissible at every anchor by act 10's merged
   `one_admissible_at_every_anchor` — forces each anchored column into its own visible fibre;
2. for each off-anchor `a`, the **transposition** `swap((j,a), (j',a))` with `j' ≠ j` — admissible for
   its own closed-form marginal by act 7's merged `admissible_permMatrix` — moves that one slot into
   a different fibre, where step 1 has already shown the mass is zero. Subtracting leaves
   `‖K (j,a) (j,a₀)‖ = 0`.

**`|V| ≥ 2` is where the force comes from**, and the hypothesis is structural rather than cosmetic:
the argument needs a second fibre to move mass into.

**`|V| = 1` IS A GENUINE EXCEPTION AND IS PROVED TO BE ONE.**
`visible_marginal_eq_one_of_visible_subsingleton` shows the single visible entry is the squared norm
of an anchored column of a unitary, hence **identically `1`**; so
`all_preserve_admissible_of_visible_subsingleton` shows **every** unitary preserves it. The maximal
uniform class there is all of `U(|A|)`, which strictly contains the weak class whenever `|A| ≥ 2`.
**`𝒢ʷ` is not maximal at `|V| = 1`, and this round does not claim it is.**

**Uniformity is part of the claim.** Maximal among classes preserving the marginal of *every*
admissible `U`; a single fixed `U` admits more.

**Scope of the evidence, stated as explicitly as for `GL1s`.** What the module certifies is the
**structural** content: membership, the unit-circle coefficients (`weak_anchor_coeff_norm_one`),
maximality for `|V| ≥ 2`, and the `|V| = 1` exception. The **Lie-group identification**
`𝒢ʷ_{a₀} ≅ U(1)^{|V|} × U(|V|(|A| − 1))` and its real dimension `|V| + (|V|(|A| − 1))²` are
**arithmetic recorded in this note, not theorems of the module** — exactly the status `GL1s`'s
dimension has. Nothing in the round rests on either formula, and "`GL1w` landed" means the
structural theorems landed, **not** that the group identity is kernel-certified.

## `GL2` — the no-go

`gl2_strong_gauge_moves_relative_candidate`. Two coherent lifts of the **same** visible family, on
one fixed carrier and anchor, related by a **time-dependent** element of the **strong** class, with
exact cross-time composition for both, whose relative candidates **differ** — from `1/2` to `0` at
the entry `(0,1)`.

**The strong class is deliberately the weaker choice**, and it suffices: a nontrivial *invisible*
subgroup that moves relative candidates is already enough, and using the smaller group makes the
statement stronger.

**The cocycle condition is vacuous, and nothing in the round uses it.** With relatives *defined* as
`U t (U s)ᴴ`, the identity `U'_{t←s} U'_{s←r} = U'_{t←r}` holds for **every** family whatsoever, so
no force may be drawn from it and none is.

**`GL2` is scoped to `ℕ`-indexed coherence**, which is what `CoherentLift` expresses. **No regularity
result is claimed about it.** Act 5's smooth diagonal-phase construction is a **prior merged
countercontrol on the continuous side** — it lies in `𝒢ʷ_{a₀}` and **not** in `𝒢ˢ_{a₀}`, so it is
evidence that regularity does not rescue uniqueness rather than an instance of `GL2`'s statement.

**Bounded exactly as act 7's `DC1` is bounded**, and inheriting all of its bounds: one visible pair,
one anchor, one time pair, under the frozen readback.

## `GL3` — necessity, and only necessity

`gl3_constant_gauge_preserves_relative`: a constant gauge leaves **every** relative object
unchanged, so time-dependence is **necessary** for this right action to move a relative object.

**This is one direction.** `GL2` supplies that time-dependence **can be** sufficient, existentially,
at one exhibited lift. **Neither says every time-dependent gauge moves every relative candidate** —
a gauge whose consecutive ratios act trivially on the readback would not — and the round does not
say it. Any two-sided reading of the form "the obstruction is exactly time-dependence" is wrong.

## The witness controls: BOTH act 7 witnesses are `GL2` instances

`forced_gauge_witnessB`, `forced_gauge_perm`, `forced_gauge_witnessA_is_strong`.

Witness B's forced element is `P(ρ)` directly, since `Uᴴ U = 1`. Witness A's **conjugates**: under
act 7's convention `permMatrix σ p q = if q = σ p then 1 else 0` the product rule is
`P(g) P(h) = P(h * g)` — Mathlib's own `permMatrix_mul` — so

    K = P(σ)ᴴ P(σ · τ) = P(σ⁻¹) P(σ · τ) = P( (σ · τ) · σ⁻¹ ) = P( σ τ σ⁻¹ )

and with `σ = prodComm`, `τ = swap((1,0),(1,1))` that is `swap((0,1),(1,1))` — the **same** element
as witness B's. It fixes both anchored columns, so it is in the strong class.

**Reading the constructor's `τ` off directly is wrong, and the freeze recorded that trap in
advance.** `τ` moves the anchored vector `e_{(1,0)}`; its conjugate does not. The forced element must
be **computed**, and `forced_gauge_perm` is the general identity that computes it.

**Consequence: neither merged witness is a `GI2` candidate.** They are controls, not discoveries —
exactly as the freeze assigned them.

## `GI2` — the LIFT SPACE is not exhausted by the maximal uniform weak stabilizer

`gi2_lifts_not_weakly_gauge_related`. **The freeze predicted this fork at no strength on either
side, and the round settled it** — in the lift space, and there only. The section title says "lift
space" rather than "the ambiguity" deliberately: the difference between those two readings is the
whole content of the scope paragraph below.

Two coherent lifts of the **same** visible family, on a carrier with `|V| = 2` so `GL1w`'s
maximality applies and the reading is licensed, whose forced element lies **outside the weak class**:

- the visible family is act 7 witness A's `G₁` slice `Aᵀ`, whose mass sits entirely in row `0`;
- the two dilations are `P(prodComm)` — act 7's own — and `P(swap((0,0),(1,0)) · prodComm)`;
- both are admissible at `a₀ = 0`, because admissibility constrains only the **fibre-summed**
  modulus, so row `0`'s mass may be carried by either ancilla slot and the two differ in which;
- the forced element is `P(swap((0,0),(1,0)))`, a transposition of **two anchored basis vectors**. It
  maps the anchored line at `j = 0` onto the anchored line at `j = 1`, and **no** element of the weak
  class does that: weak membership requires each anchored column to be a multiple of its own basis
  vector.

**Why this was reachable when act 7's witnesses were not.** Act 7 built its second dilation by
right-multiplying the first by an anchor-fixing permutation, which is a strong-class move by
construction. The `GI2` pair instead uses two dilations that were **independently** admissible for
the same slice — available because admissibility sees only a fibre sum.

**The `GI2` label is earned in the form the freeze requires**: the forced element
`K t = (U t)ᴴ (U' t)` is computed and proved to fall outside `𝒢ʷ_{a₀}`. It is **not** a failed
search, and no universal over the class was needed, because the relating element is forced and
membership is therefore decidable.

**And the witness bounds its own reading — provably.** Both lifts are **constant in `t`**, so the
forced element `P(swap((0,0),(1,0)))` is constant, and `gl3_constant_gauge_preserves_relative`
applies to it: the two lifts have the **same relative object at every pair of times** (each is
identically `1`). That is the theorem's **final conjunct**, kernel-checked rather than asserted
here. A nonmember of the weak class is therefore *not* by itself a difference in relative evolution,
and this witness is a concrete demonstration of the gap. See *What `GI2` does say* below.

## What these outcomes do NOT license

- **`P0` is NOT closed.** Act 7 layer 2's caveat, as act 9 sharpened it, **stands unchanged** —
  `GL2` makes it structural rather than provisional, which is not the same as retiring it.
- **`GL2` and `GI2` are NOT a proof that OI and QM are inequivalent.** The statement is that the
  visible family does not *by itself* fix the relative quantum evolution. A conditional equivalence
  with an additional stated principle is untouched, in either direction.
- **No candidate-selection principle is claimed or shown to be required.** Some additional structure
  would be needed for relative uniqueness; naming one is out of scope, and `C5` is neither named nor
  adopted.
- **`GL1s`'s dimension is not the size of the invisible freedom.**
- **`GI2` is NOT evidence of non-gauge ambiguity in the relative quantum evolution.** It is about
  the **lift space**, not about relative evolution. The exhibited pair is **proved** to have the
  same relative object at every pair of times — see the next section, where the point is made
  precise. `GL2` is the round's only relative-evolution no-go.
- **`GI2` does not license any claim that the structure needed to pin the relative evolution must
  be larger than a gauge fixing**, or that a connection could not suffice. Those readings are
  refuted by `GI2`'s own witness.
- **The direct-branch statement is exactly** act 7's and no more: `D4a` positive on the direct
  branch, `T1` **necessary, not sufficient**, `n = 3` properness at **evidence level 3**, and **no
  claim about what fraction of OI lies in the direct sector.**

## What `GI2` does say, stated once and carefully — and the reading it does not support

**`GI2` is a statement about the lift space, not about relative evolution.** Under `GL1w`'s
maximality (`|V| ≥ 2`), it says the set of coherent lifts of a fixed visible family is **not
exhausted by the orbit of the maximal uniform weak stabilizer**. That is its whole content.

**It is not evidence that the relative quantum evolution carries non-gauge ambiguity, and the
witness itself shows why.** Both `GI2` lifts are **constant in `t`** — `U t = P(σ)` and
`U' t = P(ρ·σ)` for every `t` — so the forced element `K t = P(ρ)` is constant, and this module's
own `gl3_constant_gauge_preserves_relative` applies to it. The two lifts therefore have **identical
relative objects at every pair of times**; each is identically `1`. This is not an observation left
to prose: it is the **final conjunct of `gi2_lifts_not_weakly_gauge_related`**, kernel-checked.

So `GI2` **does not** license "the structure needed to pin the relative evolution is larger than a
gauge fixing", and **does not** license "a connection alone would not suffice". Those readings do
not follow from a nonmember of the weak class; they would need a nonmember that *also* moves the
relative evolution, and `GI2`'s witness is the opposite of one. **`GL2` remains the round's only
relative-evolution no-go**, and it is a strong-class statement that stands on its own.

**The stronger target is open and is named here so it is not mistaken for settled**: a pair of
coherent lifts of the same visible family that lies **outside the weak class** *and* **differs in
relative evolution**. Act 11 does not supply one, does not show one exists, and does not show one
cannot. That pair, not `GI2`, is what would bear on the shape of the missing structure.

## `D3` — the split held

**Act 11 subsumed `D3` as a proposed uniqueness mechanism and did not close `D3`'s source-level
existence/regularity audit.** That audit **remains open**: whether the source supplies a coherent
lift, and with what regularity, is untouched here.

**Coherent-lift existence was not presumed and was not needed in general.** The round exhibits
concrete coherent lifts on `A = Fin 2` within Source A's stated bounds, which is what `GL2` and
`GI2` require; no general existence theorem was proved or assumed, and none is claimed.

## The chronology control

**`R7-CLG` certifies the strong property**, reusing act 10's mechanism:

- the preregistration blob is pinned **by content** to `0f6d37fafd857d9e54d5dbff6d062cc360ea08e5`;
- the real execution head `H` is resolved from `pull_request.head.sha` in a PR run — **never** the
  synthetic merge commit — failing closed with no fallback;
- `B = 6cff07cc0655124f1f29e04b156cc05a3d717a48` must be an ancestor of `H`; **and**
- **every commit in `git rev-list H ^B` must be a descendant of `B`**, which excludes pre-freeze side
  history rather than merely certifying the final head;
- history recovery is performed by the guard itself for `B`, for `H` **and for every enumerated
  commit**, and a failed recovery **fails** the check rather than skipping it.

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** The claim is scoped to the repository record — git certifies what entered the tree and
when, not what anyone thought or drafted outside it.

## Definition budget: **FOUR of the frozen six slots fire**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 | `StrongAnchorStabilizer` | **fired** |
| 2 | `WeakAnchorStabilizer` | **fired** |
| 3 | `CoherentLift` | **fired** |
| 4 | `GaugeRelated`, class-parameterized | **fired** |
| 5 (conditional) | a relative-candidate abbreviation | **unused** |
| 6 (conditional) | `GI1`'s or `GI2`'s proposition | **unused** |

Slot 5 did not fire: the propositions read acceptably with the readback written out, as act 7 writes
it. Slot 6 did not fire: `GI2` is statable directly from slots 3 and 4 as the negation of
`GaugeRelated (WeakAnchorStabilizer a₀)`, so a separate proposition would have been budget spent on
`¬`. **No seventh definition was introduced**, and no lift, stabilizer element, witness or carrier is
a top-level definition — each is a bound variable pinned by an equation, as act 10 did.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked. Eighteen named results, **no `sorry`, no `axiom`, no
`native_decide`**, every one printing only `[propext, Classical.choice, Quot.sound]`:

| Result | Axioms |
| --- | --- |
| `strong_mem_weak` | `[propext, Classical.choice, Quot.sound]` |
| `weak_anchor_coeff_norm_one` | `[propext, Classical.choice, Quot.sound]` |
| `strong_column_offAnchor_eq_zero` | `[propext, Classical.choice, Quot.sound]` |
| `strong_eq_one_of_ancilla_subsingleton` | `[propext, Classical.choice, Quot.sound]` |
| `card_offAnchor` | `[propext, Classical.choice, Quot.sound]` |
| `conjTranspose_mul_mem_unitaryGroup` | `[propext, Classical.choice, Quot.sound]` |
| `gaugeRelated_strong_iff_agree_on_anchor` | `[propext, Classical.choice, Quot.sound]` |
| `weak_preserves_admissible` | `[propext, Classical.choice, Quot.sound]` |
| `permMatrix_mul_apply` | `[propext, Classical.choice, Quot.sound]` |
| `weak_of_preserves_every_admissible` | `[propext, Classical.choice, Quot.sound]` |
| `visible_marginal_eq_one_of_visible_subsingleton` | `[propext, Classical.choice, Quot.sound]` |
| `all_preserve_admissible_of_visible_subsingleton` | `[propext, Classical.choice, Quot.sound]` |
| `gl3_constant_gauge_preserves_relative` | `[propext, Classical.choice, Quot.sound]` |
| `forced_gauge_witnessB` | `[propext, Classical.choice, Quot.sound]` |
| `forced_gauge_perm` | `[propext, Classical.choice, Quot.sound]` |
| `forced_gauge_witnessA_is_strong` | `[propext, Classical.choice, Quot.sound]` |
| `gl2_strong_gauge_moves_relative_candidate` | `[propext, Classical.choice, Quot.sound]` |
| `gi2_lifts_not_weakly_gauge_related` | `[propext, Classical.choice, Quot.sound]` |

## What this round does not do

- **It revises no merged result.** Act 7's `DC1`, `DC2a`, `D4a`, `D4b` and
  `admissible_mul_of_fixes_anchor`; act 8's existential `CE1`; act 9's `RB3`/`RB1-A`/`RB1-B` and the
  sharpened caveat; act 10's `AB0-A`/`AB0-B` and `one_admissible_at_every_anchor` — all cited and
  consumed unmodified.
- **Act 7 layer 2's `D5` chronological-ordering control stands NOT CERTIFIED.** Nothing here repairs
  it retroactively, and nothing here depends on it.
- **It claims no candidate-selection principle**, proposes none, and does not name or adopt `C5`.
- **It does not exhibit a same-visible lift pair that lies outside the weak class AND differs in
  relative evolution**, and does not show one exists or cannot. That pair — not `GI2` — is what
  would bear on whether the missing structure exceeds a gauge fixing. It stays **open**.
- **It does not kernel-certify the Lie-group identifications or dimensions** that `GL1s` and `GL1w`
  state. Those are arithmetic recorded in this note; the module proves the structural
  characterizations and `card_offAnchor`'s cardinality.
- **It compares Source A with neither Source B nor Source C**, on any axis.
- **It touches no manuscript.** No propagation in this round.
- **It says nothing about Track I**, and nothing here is evidence for anything there.
