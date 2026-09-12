# Track B act 8 — layer 0 checkpoint (Track I)

**The round is IN PROGRESS and is paused after layer 0 at owner direction.** Layers 1 and 2 are
**not yet executed**, which is a different status from the *not reached* a stop produces: nothing
has stopped the round, and **no outcome label `CE1`–`CE5` is assigned or may be inferred from this
checkpoint.**

Frozen preregistration: `preregistration.md` in this directory, blob
`6517f4dc7b884cb59223a685d5f3a05d4c291e36`, merged by PR #578. Executed from `main` at
`ac2907ae27ce608bbbda489bf23a876e83c606ba`.

**Source A was not read for this layer.** Its continuity condition, its rooted-versus-two-time
quantifier, its differentiability demand and its dilation contract are untouched and belong to
layer 1.

## Outcome of layer 0: no Track I obstruction. `CE3` is NOT reached, and layer 1 is licensed

The freeze routes `CE3` to "the extension relation **cannot be defined** from current OI structure
without an extra principle, and the principle is **named**". The relation is defined below from
nothing but a finite carrier, a time domain, an embedding and row-stochasticity — all of which the
OI visible class already carries — so **no extra principle was needed and none is named**. Layer 0
therefore produces **no genuine Track I obstruction** and the round proceeds to layer 1.

That matches the freeze's own prediction, which called `CE3` "the outcome this freeze considers
least likely, since E1's ingredients — a time domain, an embedding, an agreement condition and a
restriction — look statable without a new principle." They were.

## E1 — the relation, all five returns fixed

| Return | Settled as |
| --- | --- |
| **(a) time domain** | `ℝ≥0` (`NNReal`) |
| **(b) embedding** | `ι : ℕ → ℝ≥0`, `ι n = (n : ℝ≥0)` — the unit-step cast |
| **(c) agreement** | `restrict Γ̂ = Γ`, an equality of `ℕ`-indexed families |
| **(d) restriction** | `restrict Γ̂ = fun n => Γ̂ (ι n)`; the restriction of an extension of `Γ` **is** `Γ`, on the nose |
| **(e) away from embedded times** | **row-stochasticity, and nothing else** |

**(a) is a choice and is recorded as one.** The discrete family is `ℕ`-indexed and rooted at `0`.
Extending below zero would invent structure the visible data does not carry. Indexing by `ℝ` and
constraining only `0 ≤ t` was rejected for a specific reason: it would make any two families
differing at negative times count as distinct extensions, manufacturing a non-uniqueness of
bookkeeping that would have contaminated E2's answer with an artifact.

**(b) the unit step is a normalisation, not a restriction.** A step `δ > 0` gives the same relation
after rescaling time by `δ`, and nothing in the layer depends on the scale.

**(e) is the load-bearing decision of layer 0, and it is a REFUSAL.** Continuity is **not** part of
the extension relation. Neither is differentiability, nor periodicity of the continuous family.

The reason is the round's track-separation control rather than taste. Continuity is precisely what
Source A's contract was found to want when act 7 stopped at `DC2a`. Writing it into a **Track I**
relation would be letting a Track B need shape a Track I definition — the one thing the freeze's
layer-0 control forbids structurally. Regularity is therefore carried by **separate** predicates and
conjoined only where a theorem needs it; layer 1 is where the source's own demands get transcribed,
and it can then be read off which of them the relation does and does not already supply.

**Periodicity was asked, not assumed.** The relation requires no periodicity of `Γ̂`. `PPer`
constrains the **restriction**. The witness of Section D happens to be periodic in continuous time;
that is a property of that witness, not of the relation.

**The track separation is checkable, not promised.** Both definitions can be read in full below.
Neither mentions `Θ`, dilation, Stinespring, or unistochasticity. A clause shaped to make a Source-A
obligation succeed could not be stated in their vocabulary at all.

## E2 — the extension is a SELECTION, not a canonical object

**Settled: OI structure admits a CLASS of extensions, not a unique one.**

`extension_not_unique_visible` exhibits, for any row-stochastic `A ≠ 1`, **two** entrywise-continuous
extensions of the constant identity family — a lawful `PPer` member — that agree at **every**
embedded time and differ half a step in.

**Consequence the round now carries:** every extension this round exhibits, here and in layers 1–2,
is a **selection**. No result may be stated as though the extension were canonical.

**The separation is at the VISIBLE level, and that is what makes it new.** The freeze admitted the
merged `RegionLimit.continuous_extension_not_unique` as **analogy and control only**, and required
that anything citing it prove the accompanying arithmetic in-round.
`regionLimit_analogue_has_equal_visible_shadows` is that proof: the two flows of that theorem have
the **same** entrywise modulus-squared at every time, so the merged precedent exhibits **no** visible
non-uniqueness whatsoever. Layer 0's separation is therefore not a restatement of it, and the
precedent is cited here at exactly the strength the freeze allows.

## E0 — the screening question: POSITIVE, and it is NOT `CE1`

`screening_continuous_extension` builds, for any row-stochastic `A`, a closed-form
entrywise-continuous extension of the period-two alternating family `1, A, 1, A, …` which is the
identity at time zero and agrees at every embedded time.
`screening_extension_nonunistochastic_slice` adds the slice clause on act 6's collapsing witness:
the extension is non-unistochastic at the embedded time `t = 1`, because agreement hands that slice
over unchanged and act 6 already refuted it there.

**This is a screening result and is not `CE1`.** The freeze predicted a positive E0 **in advance**
and recorded why — the row-stochastic matrices form a convex set containing the identity, so
continuous paths from `1` are cheap and a path returning to `1` concatenates to match a periodic
family. `isRowStochastic_convex` is that observation, proved rather than cited, as the freeze
required. `CE1` additionally needs the whole of the contract layer 1 transcribes and off-directness
at the location E5 fixes; **neither is touched here.**

The prediction held, and it held in the direction that costs the round nothing: the easy question is
easy, and the round's difficulty is elsewhere.

## Definitions introduced — TWO, both mandated by E1

| Definition | E1 return |
| --- | --- |
| `restrict` | (d), and (b) is written out inside it |
| `Extends` | (c) together with (e) |

**The freeze's budget slot for "the continuous-time visible family datum" is UNUSED**, because the
datum is a plain function type `ℝ≥0 → Matrix V V ℝ` and the relation is statable without a carrier
structure. Layer 0 therefore leaves three of the five budgeted definitions for layers 1 and 2 — the
source-admissibility predicate, the off-directness proposition, and the `CE4` proposition.

Witnesses are built **inside** the proofs that need them, per act 3's lesson; there are no top-level
witness definitions.

## Named results and their axiom dependencies

All **eighteen** carry their own `#print axioms` line and print exactly
`[propext, Classical.choice, Quot.sound]`.

| Result | What it settles |
| --- | --- |
| `restriction_of_extends` | E1(d): restriction of an extension is the family, on the nose |
| `extends_apply` | E1(c) pointwise: agreement at every embedded time |
| `extends_root` | the root condition transports to `Γ̂ 0 = 1` |
| `isRowStochastic_restrict` | the restriction inherits stochasticity |
| `isRowStochastic_one` | the identity is row-stochastic |
| `isRowStochastic_convex` | the freeze's convexity observation, **proved** |
| `cos_nat_mul_pi` | `cos(nπ) = (-1)^n`, by induction from the addition formula |
| `weight_mem_unitInterval` | the interpolating weight lies in `[0,1]` |
| `weight_continuous` | the interpolating weight is continuous |
| `weight_pi_nat` | half-period weight: `0` at even steps, `1` at odd |
| `weight_twoPi_nat` | full-period weight vanishes at every embedded time |
| `weight_twoPi_half` | and equals `1` half a step in |
| `interp_rowStochastic` | the interpolation is row-stochastic at every time |
| `interp_continuous` | the interpolation is entrywise continuous |
| `extension_not_unique_visible` | **E2**: two continuous extensions, visible separation |
| `regionLimit_analogue_has_equal_visible_shadows` | the merged precedent's visible shadows coincide |
| `screening_continuous_extension` | **E0**: the screening extension exists |
| `screening_extension_nonunistochastic_slice` | E0's slice clause on act 6's witness |

The axiom report at the tail of the module carries **one line per named result**, all eighteen. The first draft reported only twelve and was corrected before review: a lemma consumed by a headline theorem is still a named result, and the standing constraint admits no quorum.

## What layer 0 does NOT establish

- **No outcome label.** `CE1`, `CE2`, `CE3`, `CE4` and `CE5` are all unassigned.
- **No `CE1`.** The screening extension is not a `CE1` construction and is never reported as one.
- **No Source A reading.** The contract of layer 1 is untranscribed; E3, E4 and E5 are unanswered.
- **No off-directness determination at the frozen location.** `O-A`, `O-B` and `O-C` are E5's, and
  E5 is layer 1. The slice theorem answers E0's own wording and nothing beyond it.
- **Nothing about act 7.** `D4a`/`D4b` remain *not reached*; this checkpoint neither reopens act 7
  nor bears on the adjudication.
- **`BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1`, `UB2` and `DC2a` are cited and unrevised.**
- **No manuscript edit, and no roadmap change** — the `P0` propagation is reserved for the round's
  single execution PR, per the freeze's execution discipline.

## The one Track B object used, and where

`IsUnistochastic` (act 6) appears in exactly one theorem,
`screening_extension_nonunistochastic_slice`, which answers the freeze's **own** screening question
E0 — a question, not a definition. The two definitions of the relation remain free of it, which is
where the separation control actually bites.
