# Track B act 8 — result: the continuous-extension round

## Outcome: **`CE1`**

**An admissible off-direct continuous extension of act 6's frozen witness EXISTS**, exhibited and
kernel-checked as `OIBridge.ContinuousExtension.admissible_offDirect_continuous_extension`.

Frozen preregistration: `preregistration.md` in this directory, blob
`6517f4dc7b884cb59223a685d5f3a05d4c291e36`, merged by PR #578. Executed from `main` at
`ac2907ae27ce608bbbda489bf23a876e83c606ba`. The layer records are `layer-0-checkpoint.md` and
`layer-1-checkpoint.md`; this note is the round's result and does not restate them.

**`CE1` is EXISTENTIAL and is never restated as a classification.** One witness, one extension. It
does **not** say that every off-direct `PPer` member has an admissible continuous extension, and no
sentence here may be read that way — the discipline `UB2` already carries.

## The route to the label, stated plainly — including why it was cheap

The freeze routes `CE1` to: a Source-A-admissible continuous extension is **exhibited**, its discrete
restriction is identified and proved a lawful `PPer` member, and off-directness is preserved at the
frozen location (`O-B` **and** `O-C`). All four are proved.

**The honest account of why the round reached `CE1` rather than `CE5` is that the contract layer 1
transcribed is WEAK, not that the construction is clever.** Source A places three conditions on a
continuous-time family — non-negativity and first-index normalization at each pair of times (2)–(3)
p. 4, the root condition p. 4, and the limit `Γ(t ← t₀) → Γ(t₀ ← t₀)` as `t → t₀` p. 4 — and nothing
further. It requires no continuity away from the conditioning time, no differentiability of the
transition family, and no indivisibility. The continuous object was already available from layer 0's
convex interpolation; what layer 2 added is the proof that it meets that contract and carries
off-directness where E5 fixed it.

**The ordering is what makes this reportable rather than circular.** The contract was transcribed in
layer 1, reviewed and accepted, **before** any construction was attempted, and it is unchanged here —
neither narrowed nor widened, in either direction. That sequencing is the whole point of the layer
order, and it is the reason a weak contract can be reported as a finding instead of as a convenience.

**The freeze's triviality control is respected, not evaded.** Control 9 says a rooted continuous
interpolation is **not** a `CE1`, and `CE1` is not claimed on that basis. Layer 0's
`screening_continuous_extension` remains labelled a screening result wherever it appears. What earns
the label is the conjunction the freeze names: the transcribed contract, `O-B`, and `O-C`.

## E7 — the construction

`admissible_offDirect_continuous_extension` carries, in one object:

| Clause | Status |
| --- | --- |
| `PPer Γ` — the restriction is a lawful `PPer` member | **proved** (preservation clause 1) |
| `Γ 1 = A`, act 6's collapsing slice — the restriction **is** the merged witness | **proved** (preservation clause 3) |
| `Extends Γ̂ Γ` — the layer-0 relation holds | **proved** |
| `SourceAAdmissible Γ̂` — layer 1's transcription of the contract | **proved** |
| entrywise `Continuous` at **every** time | **proved** — more than the contract asks |
| `¬ IsUnistochastic ((Γ̂ 1)ᵀ)` — **`O-B`** | **proved** (preservation clause 2) |
| every `Θ` compatible with that slice is non-unitary ⟹ **`O-C`** | **proved** (preservation clause 4) |

**The witness was frozen before it was used.** It is act 6's merged `UB2` witness, and **no
append-only amendment was taken** — the freeze anticipated one by name in case a different witness
were needed, and none was. Substitution at execution time did not occur and was foreclosed.

**The extension is a SELECTION, not a canonical object**, as layer 0's `E2` requires of every
extension this round exhibits. `extension_not_unique_visible` settled that the relation does not
determine an extension, and nothing here upgrades the exhibited one to canonical status.

**The target domain is `ℝ≥0`, and the round says so rather than eliding it.** The contract is
instantiated on the non-negative half-line. Source A's target-time convention, §2.1 p. 3, is that
target times will "**usually**" be assumed isomorphic to `ℝ` — hedged on its face, and act 7's `D2`
already read it as a domain mismatch rather than an independent prerequisite. **Nothing here is
claimed to satisfy or to fail a real-line requirement**, because the source states none. The route
taken is the second of the two layer 1 left open, and it is reported, not assumed away.

## E5 — off-directness, at the location layer 1 fixed

| | Proposition | Status |
| --- | --- | --- |
| **`O-A`** | the continuous family is somewhere non-unistochastic | **not separately claimed.** It is available from `O-B` and is not needed; the freeze says `O-A` alone is never sufficient, and nothing here rests on it. |
| **`O-B`** | the discrete restriction is off-direct at an embedded time | **proved at `n = 1`**, the index layer 1 fixed as `L1` before construction, through act 6's `collapsed_slice_not_unistochastic` |
| **`O-C`** | the `Θ(t ← 0)` §3.4 consumes is not already unitary | **discharged**, at the same index |

**`O-C` KEPT ITS FROZEN FORM AND WAS DISCHARGED BY PROVING MORE.** The freeze states `O-C` *de re* —
about the particular potential §3.4 takes as input. Source A's `Θ` is not unique (p. 7) and carries a
time-dependent phase gauge (fn. 6 p. 7), so a claim about one selected `Θ` would leave open whether
some other admissible choice is unitary and §3.4's dilated branch therefore avoidable.

`compatible_theta_nonunitary` closes that by a universal statement rather than by a redefinition: a
unitary `Θ` compatible with `M` through (12) p. 6 would itself witness `IsUnistochastic M`, so when
`M` is not unistochastic **no** compatible `Θ` is unitary. The frozen `O-C` follows for whichever
potential §3.4 selects, because the selected one is among the compatible ones.

**An earlier draft of the layer-1 record proposed adopting that universal statement as the
definition of `O-C`. That would have strengthened `CE1`'s condition after the freeze, and it is not
what happened**: the proposal was repaired under review, the freeze is unamended, and the universal
statement appears here as a theorem.

**The entailment is proved in-round, as control 7 requires**, and no entailment among `O-A`, `O-B`
and `O-C` is assumed anywhere.

## E6 — the footnote-11 negative control: RUN, and NON-APPLICABLE

The control was run and returns **non-applicable**, which the freeze names as a live answer. The
reason is structural rather than an accident of the witness.

`fn11_output_unistochastic`: footnote 11's recipe (p. 12) forms `|(Σ^{t/δt})_ij|²` from a permutation
matrix, and its output is by construction the entrywise modulus-squared of a unitary — which is
exactly act 6's `IsUnistochastic`. **So a footnote-11 interpolation is on the direct branch at every
time, whatever permutation it starts from.**

`fn11_not_applicable_to_frozen_witness`: act 6's collapsing slice, in Source A's orientation, is not
the modulus-squared of any unitary. So **no footnote-11 interpolation can produce this round's
discrete restriction**, and the hazard act 7 recorded from the source's own text cannot reach the
frozen witness.

**How `CE1` differs from footnote 11**, which the freeze requires a `CE1` to state. The difference is
**not** a clause of the contract that one satisfies and the other does not — both would satisfy it.
It is in what each recipe accepts as input. Footnote 11 interpolates through real powers of a
**permutation** matrix and cannot accept an off-direct discrete process at all. This construction
interpolates through the **convex** structure of the row-stochastic matrices, which contains matrices
that are not doubly stochastic — act 6's slice among them — and requires its input to be neither
deterministic, nor unitary, nor doubly stochastic.

**The control is reported the same way under every outcome**, and would have been reported had the
round landed on `CE2`, `CE4` or `CE5`.

## No completion shortcut, and no density statement

**Nothing in this round invokes the project's topological completion machinery**, so the freeze's
three-part disclosure has nothing to discharge. The extension is the closed-form convex interpolation
of the module's Section B, built inside the proof that needs it, per act 3's lesson. No
`KrausDense`/`DenseFiniteQM` result, no `ChanWithin`-style approximation, and no limiting object is
used anywhere. **`CE1` rests on no density statement.**

`RegionLimit.continuous_extension_not_unique` is cited as **analogy and control only**, at exactly the
strength the freeze allows, and `regionLimit_analogue_has_equal_visible_shadows` proves in-round that
its two flows have identical visible shadows.

## The predictions, and whether each held

| Prediction | Held? |
| --- | --- |
| E0 positive, and its positivity not presentable as the result | **Held.** E0 came out positive at layer 0, was labelled a screening result, and `CE1` is not claimed on it. |
| "The live uncertainty is E3 and E4"; the two-time reading "roughly even money" | **Did not hold in the direction the freeze leaned toward.** E4 returned **rooted**, and the freeze's hardest anticipated cost — a second construction with no composition theorem to determine it — did not arrive. |
| "the honest prior is tilted toward `CE1` or `CE5`, not toward `CE4`" | **Held.** The round landed on `CE1`. |
| `CE3` "the outcome this freeze considers least likely" | **Held.** `CE3` was not triggered at layer 0. |

**The predictions are reported as predictions.** None is a finding, and `CE1` is earned by the
exhibited extension rather than by the prior that favoured it.

## Definitions and axioms

**THREE top-level definitions, against a frozen budget of five.**

| Definition | Layer | Freeze slot |
| --- | --- | --- |
| `restrict` | 0 | the restriction map, E1(d) |
| `Extends` | 0 | the extension relation, E1(c)+(e) |
| `SourceAAdmissible` | 2 | the Source-A admissibility predicate, E3 |

**Two budgeted slots are unused and are recorded as unused.** The continuous-time visible family
datum was not needed, the family being a plain function type; and the off-directness proposition
needed no new name, act 6's `IsUnistochastic` stating `O-B` directly and `O-C` being statable inline.
The `CE4` proposition was not reached. **No append-only amendment was taken.**

**TWENTY-FIVE named results, each carrying its OWN `#print axioms` line**, all printing exactly
`[propext, Classical.choice, Quot.sound]`. No `sorry`, no `axiom`, no `native_decide`. The module is
`verification/lean-mathlib/OIBridge/ContinuousExtension.lean`, registered in
`verification/lean-manuscript-census.json` and imported in `OIBridge.lean`.

Layer 2's seven additions: `collapsingSlice_isRowStochastic`, `collapsingSlice_of_extends`,
`sourceAAdmissible_of_extends`, `fn11_output_unistochastic`,
`fn11_not_applicable_to_frozen_witness`, `compatible_theta_nonunitary`, and the headline
`admissible_offDirect_continuous_extension`.

## Act 7 reopens — at the ADJUDICATION, with the signs UNSET

**`CE1` reopens act 7**, and the freeze fixes where: `D2` is repaired, and act 7 resumes at the
**`D4a`/`D4b` adjudication** — those two questions asked and answered on the source, as act 7 froze
them. **The signs are not preselected, and nothing in this round sets them.**

**Act 7's conditional `D4a`-positive/`D4b`-negative reading is a PREDICTION and a source reading
only** — the position act 7 is likely to resume to, never the position it resumes *at*. Act 7's own
note records `D4a`/`D4b` as *not reached* and says of that reading that it "settles nothing in this
round". **`CE1` establishes that a testable object exists; it does not establish what the test
returns.**

**If** that adjudication returns `D4a` positive and `D4b` negative, act 7's frozen stop table routes
to the **readback-amendment path** at **reduced strength**: its layer 2 pauses for a merged
append-only amendment fixing the readback map before any layer-2 formalization or witness
calculation. Any other combination routes as that same table says, and **this round fixes none of
it.**

**`DC2a` is not revised.** It said act 7's own off-direct witness was outside §3.4's input contract,
because the inherited continuity condition is uninstantiated on `ℕ`. That remains exactly true of the
**discrete** witness. This round supplies a **different** object — a continuous-time family on which
that condition has content — and does not contradict `DC2a` in any part.

## What this round does NOT say

- **No classification.** `UB2` and `CE1` are both existential and neither is restated as a statement
  about all off-direct members or about the OI class.
- **No claim that Source A is applicable or inapplicable**, and none that the external correspondence
  succeeds or fails. `CE1` says one admissible off-direct extension exists; the adequacy of the
  correspondence is untouched.
- **No candidate-selection principle** is adopted or proposed, and act 5's gauge-versus-empirical
  tension is not adjudicated. `F1` versus `F2` is undecided.
- **Nothing about interference**, and no sourcing inference in either track direction. That Track B
  needed this construction is a motive and never evidence.
- **Nothing about divisibility or indivisibility of the extension.** The contract requires neither
  (layer 1's `F-4`), and `BD3` governs: class membership neither entails nor is entailed by failure
  of divisibility.
- **Act 7's `D3` gap is unreopened.** Stinespring's pointwise existence with no coherent family
  derived or selected, and the absence of a stated link from `Γ̂`'s regularity to `Θ`'s or `U`'s
  (layer 1's `F-2`), are recorded as inherited and open. **`CE1` does not close them**, and the
  adjudication act 7 resumes at is where they are next handled.
- **`BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1`, `UB2` and `DC2a` are cited and unrevised.**
  Acts 1 through 6 are not reopened.
- **No manuscript edit**, per the freeze.
- **`C5` is neither named nor adopted**, and Source A is not compared with Source B or Source C on
  any axis.

## What remains open, and what would settle it

1. **`O-A` at non-embedded times** is unclaimed. The exhibited family's behaviour strictly between
   embedded times is not characterised, and a statement about it would need its own theorem.
2. **The `D4a`/`D4b` adjudication** — whether the dilation choice moves the induced candidate. This
   is what act 7 now resumes to, and it is settled by asking those two questions on the source, not
   by anything here.
3. **Act 7's `D3` gap**, at the regularity level: Source A assumes differentiability of the
   post-(28) unitary family at (33) p. 12 without showing an admissible Stinespring choice meeting it
   exists, and states no link from `Γ̂`'s regularity to `Θ`'s. Settling it needs either a derivation
   of a coherent regular dilation family or a countermodel.
4. **Uniformity over the class.** `CE1` is existential. A statement covering all off-direct `PPer`
   members would be a different theorem with a different quantifier, and nothing here supplies it.
5. **The real-line target domain.** Whether an admissible extension exists over all of `ℝ` is not
   asked here. Source A states no such requirement, so this is a question about reach rather than a
   gap in the result.
