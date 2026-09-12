# Track B act 10 — anchor robustness (`P0b`): RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`2e92464dca3809558959d240314dbaf9eaa1c500`, merged into `main` as
`93c2ca63c6cd7a61388d577b8baf22c3c1fdb41f` (PR #586) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `93c2ca63c6cd7a61388d577b8baf22c3c1fdb41f` (merge of PR #586) |
| This round's frozen control plane | `preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |
| Act 7 layer 2's result (`DC1`) | `../act-07-dilation-choice/layer-2-result.md`, blob `02f93a1c3ec485b5f46b8e02ff52ca4f73e0ee89` |
| Act 7 layer 2's module | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 9's result (`RB3`, `RB1-A`, `RB1-B`) | `../act-09-readback-robustness/result.md`, blob `f918e7b405dec35e01e9d53ca0dd90eb56c34df4` |
| This round's module | `verification/lean-mathlib/OIBridge/AnchorRobustness.lean` |

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Availability answered FIRST, as the freeze required

The freeze makes joint-anchor availability **an explicit prerequisite with its own obligation**,
discharged before any label may be assigned, and refuses to let it be inferred from an unsuccessful
search. **It is answered here first, and answered in the negative on both witnesses.**

`no_second_jointlyReproducing_anchor_witnessA` and `no_second_jointlyReproducing_anchor_witnessB`
prove that no jointly reproducing anchor other than act 7's `a₀ = 0` exists, per witness, separately.

## Outcome: **`AB0-A`** and **`AB0-B`**, and no other label is assigned

The preregistered prediction was `AB0` on both witnesses. **That is the outcome.**

`jointlyReproducing_iff_anchor_zero_witnessA` and `jointlyReproducing_iff_anchor_zero_witnessB`
characterize the jointly reproducing anchors of each compared configuration as **exactly** the
singleton `{a₀ = 0}`. Each is **proved by exhaustion over the finite anchor domain, never by an
unsuccessful search**, which is the discipline act 7 applied to `DC4` and act 9 to `RB1`, here
applied to the negative.

**The `↔` carries both halves, and the converse half is load-bearing rather than decorative.**
`AB0`'s claim is that the question *collapses to the anchor already used*, and that presupposes the
used anchor still works. So the domain is proved to be a **singleton and not empty** — the
difference between a collapse and a vacuity.

**The witnesses are reported separately and never merged.** Witness A is rank-one degenerate;
witness B is full rank and its `G₁`-side dilation is a non-permutation unitary, so neither result is
an artifact of the other's structure. `ab0_on_both_witnesses` places the two beside each other as a
conjunction and **proves nothing that either does not already prove alone**.

| Witness | Jointly reproducing anchors | Label earned | `AB1` | `AB2` |
| --- | --- | --- | --- | --- |
| **A** (rank-one, permutation dilations) | exactly `{0}` | **`AB0-A`** | **withheld** | **false** |
| **B** (full rank, non-permutation dilation) | exactly `{0}` | **`AB0-B`** | **withheld** | **false** |

## The `AB1` label is WITHHELD on both witnesses, and the proposition's truth is why

This is the round's sharpest control, and it is stated formally rather than left to prose.

**`AB1`'s proposition is TRUE on both witnesses** — `anchorInvariantDivergence_trivial_witnessA` and
`anchorInvariantDivergence_trivial_witnessB`. Every jointly reproducing anchor preserves the
divergence, because there is only one such anchor and act 7's merged `DC1` already established the
divergence there.

**The `AB1-A` and `AB1-B` labels are NOT EARNED AND ARE NOT ASSIGNED.** The freeze requires, before
any `AB1` label, an exhibited jointly reproducing anchor **distinct** from act 7's, and this round
proves none exists. A universal quantifier satisfied only because its domain has no new element is
not a robustness result. The freeze's block quote — **`AB1` is not earnable vacuously** — is
therefore honoured against a case where the universal is *true*, which is the case it was written
for.

## `AB2` is false on both witnesses

`not_ab2_witnessA` and `not_ab2_witnessB`. Recorded so that `AB0` is not mistaken for an undecided
middle: the collapse is **not** concealing an agreement that a finer analysis would find. Both
follow from the slot-4 elimination theorem applied to the propositions above.

## Where the collapse localizes: entirely on the `G₁` side

`one_admissible_at_every_anchor` proves that the identity dilation of the identity slice is
admissible **at every anchor**, for any visible and ancilla carrier. Both of act 7's exhibitions
dilate `G₂ = 𝟙` by exactly that, at both dilation choices, so **half of each configuration is
indifferent to the anchor** and the failure is entirely on the `G₁` side.

The deciding entries, one per witness:

| Witness | `G₁` slice | Entry | Slice value | Reproduced at `a₀′ = 1` |
| --- | --- | --- | --- | --- |
| **A** | `Aᵀ` | `(1, 0)` | `0` | `1` |
| **B** | `Bᵀ` | `(0, 0)` | `1` | `1/2` |

**The structural reason, recorded in the freeze before any of this was proved.** For a permutation
dilation the reproduced slice's single occupied row index is `(σ.symm (j, a₀)).1`, so moving the
anchor moves which preimage fibre is read. Anchor and reproduced slice are coupled; joint
reproduction at two anchors is a coincidence rather than the default. The forward reading of act 7's
merged closed form, `admissible_permMatrix_apply`, is the whole engine of `AB0-A`.

## `P0` is NOT closed. The anchor axis is RECLASSIFIED, not resolved

The freeze fixed this wording before the outcome was known, because the temptation runs the other
way. It is restated here unchanged.

- `AB0` says the anchoring convention **cannot be varied downstream** on these witnesses with these
  dilations held fixed. It does **not** say the convention makes no difference, and it does **not**
  say the divergence is convention-independent.
- The **upstream** choice remains a choice. Act 7's dilations were built around `a₀ = 0`; a different
  anchor chosen upstream would have produced **different dilations**, and whether that pairing
  diverges is the out-of-scope question. `AB0` is silent on it.
- Act 7 layer 2's caveat, as act 9 sharpened it, **stands unchanged**: dependence on the anchoring
  convention **remains open**. If anything `AB0` makes the caveat more necessary, not less — the
  convention could not even be varied to test it.

**`P0` is not closed and the anchor-axis dependence is not resolved.** It is **reclassified** as not
reachable by this construction, with the upstream anchor choice named as the live remainder.

### The control that makes the reclassification precise, and it is a theorem

`exists_admissible_dilation_at_other_anchor` exhibits an admissible dilation of witness A's `G₁`
slice **at the other anchor** — the four-cycle `(0,0) → (0,1) → (1,1) → (1,0) → (0,0)`, whose
inverse carries both anchored columns into the visible fibre over `0`, which is where `Aᵀ`'s mass
sits.

**So `AB0` is a fact about the compared configuration, not about the anchor.** Anchor `1` is
perfectly serviceable in principle; what fails is joint reproduction by *these* dilations. The move
that would exploit this — adjusting a dilation until the new anchor becomes admissible — is
**exactly** what the freeze puts out of scope for `P0b`, and it lands in dilation-choice / coherence
territory. This theorem marks that boundary from the inside: it shows the out-of-scope question is
**nonvacuous**, and it stops there.

## The structural boundary held: this round did not become a dilation search

The freeze's first frozen section named the one way this round could silently become a different
round. **It did not.** Every compared dilation is act 7 layer 2's, **pinned by an equation in the
statement** to the same expression the merged exhibitions build it from, on the same ancilla
`A = Fin 2`. No dilation was replaced, composed with anything, or re-derived on different data; the
ancilla was not enlarged; the visible pairs are act 7's.

**It does not close or use act 7's `D3` coherent-dilation gap.** `D3` is **separately open,
untouched** — still the route by which a `DC4`-shaped invariance could hold on a narrower,
coherence-restricted class. The out-of-scope "change the dilation to admit a new anchor" move lands
squarely in that territory, which is a second reason the boundary was frozen first.

## The chronology control, and the property it actually certifies

The freeze strengthened act 9's guard after review found head-only ancestry too weak: a commit `E`
made **before** the control-plane merge `B` and later merged alongside `B` into the execution head
`H` leaves `B` an ancestor of `H` while `E` is reachable from `H` and never descended from `B`.

**`R7-ABR` certifies the strong property**, fail-closed:

- the preregistration blob is pinned **by content** to `2e92464dca3809558959d240314dbaf9eaa1c500`;
- the real execution head `H` is resolved from `pull_request.head.sha` in a PR run — **never** the
  synthetic merge commit `refs/pull/<n>/merge`, whose parents include the base, which would make the
  check vacuous — and an unresolvable head fails closed with no fallback;
- `B = 93c2ca63c6cd7a61388d577b8baf22c3c1fdb41f` is required to be an ancestor of `H`; **and**
- **every commit in `git rev-list H ^B` is required to be a descendant of `B`**, which is what
  excludes pre-freeze side history rather than merely certifying the final head;
- history recovery — deepening a shallow clone, fetching an absent object — is performed by the
  guard itself for `B`, for `H` **and for every enumerated commit**, and a failed recovery **fails**
  the check rather than skipping it.

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.**

**The claim is scoped to the repository record.** Git certifies what entered the tree and when, not
what anyone thought, drafted outside the tree, or worked out privately. As in act 9, the central
prediction was written into the freeze before merge, so **the merged blob is itself the record** of
what was expected — and in this round the prediction and the outcome agree.

## Definition budget: **TWO of act 10's frozen four slots fire**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 | `JointlyReproducingAnchor` — the property cut | **fired** |
| 2 (conditional) | a carrier for the compared configuration | **unused** |
| 3 | `AnchorInvariantDivergence` — `AB1`'s proposition | **fired** |
| 4 (conditional) | `AB2`'s proposition | **unused** |

Slot 2 did not fire: every proposition states its configuration as explicit arguments, so no bundle
is needed. **Slot 4's non-firing is proved rather than claimed** —
`ab2_iff_not_anchorInvariantDivergence` shows `AB2` is exactly the negation of slot 3, so a
definition for it would be budget spent on `¬`. **`AB0` gets no slot**, as the freeze specifies: it
is a theorem over slot 1. **No fifth definition was introduced**, and no anchor, dilation, witness
or configuration is a top-level definition — each is a bound variable pinned by an equation, exactly
as act 7 layer 2 binds witness B's unitary and permutation inside its own exhibition.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked. Thirteen named results, **no `sorry`, no `axiom`, no
`native_decide`**, every one printing only `[propext, Classical.choice, Quot.sound]`:

| Result | Axioms |
| --- | --- |
| `ab2_iff_not_anchorInvariantDivergence` | `[propext, Classical.choice, Quot.sound]` |
| `admissible_permMatrix_apply` | `[propext, Classical.choice, Quot.sound]` |
| `one_admissible_at_every_anchor` | `[propext, Classical.choice, Quot.sound]` |
| `jointlyReproducing_iff_anchor_zero_witnessA` | `[propext, Classical.choice, Quot.sound]` |
| `no_second_jointlyReproducing_anchor_witnessA` | `[propext, Classical.choice, Quot.sound]` |
| `anchorInvariantDivergence_trivial_witnessA` | `[propext, Classical.choice, Quot.sound]` |
| `not_ab2_witnessA` | `[propext, Classical.choice, Quot.sound]` |
| `jointlyReproducing_iff_anchor_zero_witnessB` | `[propext, Classical.choice, Quot.sound]` |
| `no_second_jointlyReproducing_anchor_witnessB` | `[propext, Classical.choice, Quot.sound]` |
| `anchorInvariantDivergence_trivial_witnessB` | `[propext, Classical.choice, Quot.sound]` |
| `not_ab2_witnessB` | `[propext, Classical.choice, Quot.sound]` |
| `exists_admissible_dilation_at_other_anchor` | `[propext, Classical.choice, Quot.sound]` |
| `ab0_on_both_witnesses` | `[propext, Classical.choice, Quot.sound]` |

## What this round does not do

- **It does not revise any merged result.** Act 7's `DC1` (existential, reduced strength, under
  `R_{a₀}` on anchored dilations), act 9's `RB3`/`RB1-A`/`RB1-B`, act 7's `DC2a`/`D4a`/`D4b`, act 8's
  existential `CE1`, and acts 1–6's labels are cited and consumed unmodified.
- **Act 7 layer 2's `D5` chronological-ordering control stands NOT CERTIFIED.** Nothing here repairs
  it retroactively, and nothing here depends on it.
- **It claims no candidate-selection principle**, proposes none, and does not name or adopt `C5`.
- **It compares Source A with neither Source B nor Source C**, on any axis.
- **It touches no manuscript.** No propagation in this round.
- **It says nothing about Track I**, and nothing here is evidence for anything there.
