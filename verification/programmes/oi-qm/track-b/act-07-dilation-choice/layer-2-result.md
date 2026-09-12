# Track B act 7 — layer 2 result: the dilation-choice test at REDUCED STRENGTH

## Outcome: **`DC1`, at reduced strength, on each witness separately**

**Two source-admissible anchored dilations of one off-direct visible pair yield DIFFERENT visible
candidates under the frozen readback** — exhibited twice, once on each of act 7's two preregistered
witnesses, and kernel-checked as

- `OIBridge.DilationChoice.witnessA_moves_visible_candidate` (witness A, rank one), and
- `OIBridge.DilationChoice.witnessB_moves_visible_candidate` (witness B, full rank).

**`DC4` is REFUTED at each exhibited visible pair and anchor**
(`dc4_refuted_witnessA`, `dc4_refuted_witnessB`), by the universal statement act 7 required `DC4` to
take and not by a paraphrase of it.

### The bound, stated before anything else

**`D4b` came back NEGATIVE.** Source A supplies no general map carrying the relative candidate on the
dilated carrier back to `V`. The readback used here is **ours**, frozen in advance by the readback
amendment, and so is the convention that the distinguished ancilla configuration belongs to the
dilation datum. Therefore, in the exact words act 7's `T3` and the amendment fixed:

> **`DC1` here states divergence UNDER THE FROZEN READBACK `R_{a₀}` ON ANCHORED DILATIONS.** It does
> **not** state that Source A's own visible prediction is underdetermined by the visible data, and it
> does **not** demonstrate that a candidate-selection principle is required.

**A divergence found under `R_{a₀}` could still be an artifact of the map or of the anchoring
convention rather than of the dilation freedom.** Nothing here closes that possibility; the deferred
robustness round is what would address it. This paragraph is the result, not a caveat appended to it.

## Provenance

| | |
| --- | --- |
| Act 7's governing preregistration | `preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| Resumption control plane | `resumption-preregistration.md`, blob `3bb88717267a4adb45125b6277edae4e56c5cf26` |
| Resumption result (`D4a`/`D4b`) | `resumption-result.md`, blob `216cb9e65cda9b2f3b9777c2ecfcdf8d8bb58df0` |
| Readback amendment (`T3`) | `readback-amendment.md`, blob `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |
| Executed from `main` at | `4ac6a7fce76949ba37634499a8ed456bddecd01c` |
| Formal module | `verification/lean-mathlib/OIBridge/DilationChoice.lean` |
| Frozen `D5` chronological-ordering control | **NOT CERTIFIED** — procedurally deviated from; see below |

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated**, and every coordinate below is read off
its PDF, the authoritative surface. Sources B and C are not compared with it on any axis.

**Track I is not touched, in either direction.** Neither branch is evidence for the other.

## `D5a` and `D5b` — answered, with the frozen ordering control NOT CERTIFIED

**The `D5` chronological-ordering control is NOT CERTIFIED for this round, and the round deviated
from it procedurally.** Act 7 froze the condition in terms:

> This question must be answered before any witness is examined, so that the answer is not selected
> by the outcome.

**This round cannot certify that.** The layer-2 formalization and the `D5` determinations were
developed within one execution, and no independent record of the actual chronology exists. So the
frozen procedural condition is recorded here as **deviated from**, not as satisfied — and not as
satisfied in some other sense. A frozen control cannot be re-specified after the outcome is known,
and nothing below should be read as re-specifying it.

**What IS available is a different fact, and it is stated as a different fact.** `D5a` and `D5b` are
**outcome-independent, corpus-level determinations**: checkable from their statements alone, and
incapable of having come out differently on a different witness result. That is useful evidence that
the conclusions are not witness-specific. **It is not the frozen control, it is not a substitute for
it, and it does not discharge it.**

Consequently **this round is NOT fully preregistration-compliant**, and may not be described as
such. The `D5a`/`D5b` determinations and the `DC1` exhibitions stand on their own statements and
proofs; the procedural certification does not.

Both parts of `D5` fail.

### `D5a` — the shape condition: **FAILS**, on two independent mismatches

Act 3's `padData` (`OIBridge/OperationalSourcing.lean:259`) fixes the dilated datum to: basis
`Q.Bas × Anc`, **unitary the Kronecker product `Q.U ⊗ₖ W`**, initial law the product weight, readout
ignoring the ancilla. The theorem
`candidateOf_uniformWeight_padData_eq` (`OIBridge/CandidateSelection.lean:343`) is quantified over
every finite ancilla, every ancilla unitary `W` and every weight `w`, at `uniformWeight`
specifically.

**Mismatch 1 — the shape is not merely unnecessary, it is UNAVAILABLE.** §3.4 p. 10 asks only for a
unitary on the enlarged carrier whose anchored marginal reproduces the visible slice; it never
requires that unitary to factorize. And a factorizing one cannot do the job here:
`kronecker_admissible_isUnistochastic` proves that if `U ⊗ₖ W` is an admissible anchored dilation of
`G`, then `G` is **unistochastic** — because the anchored column of a unitary has unit norm, so
`∑_a ‖(U ⊗ₖ W)_{(i,a),(j,a₀)}‖² = ‖U_{ij}‖²`. Both witnesses are off the direct branch, so neither
admits a Kronecker-product dilation at all. **This is a theorem about the padding form, proved
in-round, and it mentions no witness.**

**Mismatch 2 — the ancilla treatment.** §3.4 p. 10's marginalization holds with the input ancilla
held at **one** distinguished configuration `j′` ("for at least some choices"), which is exactly what
the amendment made the anchor. `uniformWeight` (`OIBridge/CandidateSelection.lean:69`) instead
weights **every** basis point over a visible configuration equally, averaging uniformly over the
whole ancilla. A single-anchor marginalization and a uniform average over the fibre are different
operations, and the padding theorem is proved about the second.

### `D5b` — the quantity condition: **FAILS**

The amendment adopted **act 5's (42)-type stochastic readout** as what `R_{a₀}` acts on and
**declined `candidateOf`** — the choice is recorded in the amendment's own "what the map acts on"
section and is not revisited here. Act 3's `candidateOf` is built by weighting source fibres and
summing target fibres of `bornPow`; the object under test is built from (39) p. 13's relative unitary
`U(t ← 0) U†(t′ ← 0)` through (42) p. 14. **No merged theorem identifies the two, or proves them
equivalent.** Act 7 froze that as the exact test, and it comes back negative.

### Consequence

**Act 3's padding theorem is recorded as ANALOGY AND CONTROL ONLY, never as evidence for `DC3` or
`DC4`**, and the round proceeds as though it did not exist — act 7's clause 6, applied. It is useful
for seeing what *kind* of enlargement leaves a candidate fixed, and for nothing more here.

**And it forbids nothing about `DC1`.** Act 7 states that in no case does `D5` make `DC1` forbidden:
a merged theorem about a different quantity forbids nothing about this one.

**Where the outcome-independence comes from**, for the reader who wants to check it rather than take
it: `D5a` fails on a property of the padding *form* — now a theorem about `U ⊗ₖ W` — and on
`uniformWeight`'s definition; `D5b` fails on the absence of an identification theorem in the merged
corpus. Neither mentions a witness. **This is offered as corpus-level evidence and nothing more**;
the frozen ordering control remains **NOT CERTIFIED**, per the section head above.

## The layer-1 questions, carried not re-derived

`D1`, `D2`, `D3`, `D4a`, `D4b` and `D6` are merged findings and are **cited, not re-answered** — the
resumption freeze forbids re-asking them as outcome-bearing questions.

- **`D1`** — the dilated object is `Θ(t ← 0)`, §3.4 p. 10.
- **`D2`** — the input contract, in Source A's external orientation, with its inherited continuity
  condition (p. 4, after (5)). It **failed** on act 7's own `ℕ`-indexed witness, which is `DC2a`.
- **`D3`** — the derivation-and-selection gap: Stinespring supplies **pointwise** existence, with no
  coherent time-indexed family derived or selected and no stated link from the visible family's
  regularity to `Θ`'s or `U`'s. **This gap is NOT closed and is NOT used here.** `T2` is stated at a
  single time for exactly that reason, and (39) p. 13 consumes two independent such choices.
  `D3` remains **separately OPEN**.
- **`D4a`** — **POSITIVE**: a candidate is formed from the dilated unitary, via (28) p. 11's
  tilde-dropping into (39) p. 13 and (42) p. 14.
- **`D4b`** — **NEGATIVE**: no general map back to `V`. This is why the round runs at reduced
  strength.
- **`D6`** — answered in act 7, corroboration only, and no admissibility judgement rests on it.

## `DC2a` is not revised, and each witness's contract standing is stated separately

**`DC2a` remains correct of the family it was about** — act 7's `ℕ`-indexed off-direct witness lies
outside §3.4's input contract. Nothing here revises it. What changed is which object is under test.

- **Witness A** is act 8's frozen object. `CE1` exhibited a Source-A-admissible continuous extension
  of exactly this family, and `dc1_runs_on_act8_frozen_object` ties the two together in one
  statement: the visible pair the witness-A exhibition runs on is the pair of that admissible
  continuous family. **That conjunction adds no strength to either conjunct.**
- **Witness B** is act 7's own second preregistered witness (`T4`), and **`CE1` says nothing about
  it** — `CE1` is existential, one witness, one extension, and is not restated here as though it
  covered a class. Witness B's contract standing is therefore proved in-round as a **second,
  independent existential instance**, by applying act 8's two *general* merged lemmas —
  `screening_continuous_extension` and `sourceAAdmissible_of_extends` — to `B`'s slice
  (`witnessB_admissible_continuous_extension`). Off-directness survives to the extension at act 8's
  frozen index `n = 1`.

**Neither statement is a classification.** Two existential instances of one construction are two
instances; they do not say every off-direct `PPer` member has an admissible continuous extension, and
no sentence here may be read that way.

## `T1` — the visible screen: necessary, and NOT sufficient

`not_isUnistochastic_of_not_isColStochastic` and `not_isUnistochastic_of_not_isRowStochastic` are the
two contrapositives of act 6's structural lemma — Source A's own p. 11 observation, proved in act 6
rather than cited. Under `PPer` the row half of `Γ` is already carried, so on the **external** object
`Γᵀ` the half that can still fail is the **row** half, and that is the one both witnesses run through.
Act 6 recorded that orientation and corrected an earlier draft on it; the reading is inherited.

**Not sufficient, and the `n = 2` coincidence is proved in-round without external citation**:
`isUnistochastic_two_of_symmetric` shows every `2 × 2` doubly stochastic `[[a, 1−a], [1−a, a]]` is the
entrywise modulus-squared of the real orthogonal `[[√a, √(1−a)], [√(1−a), −√a]]`.

**At `n = 3` the inclusion is proper** — the unistochastic matrices are a proper subset of the
Birkhoff polytope. That is external literature (Bengtsson–Ericsson–Kuś–Tadej–Życzkowski;
Dunkl–Życzkowski), cited at act 1's **evidence level 3** and **not proved here**. **Nothing in this
round's outcome rests on it**; it is recorded so the screen is not over-read as a characterization.

## `T2` — source admissibility, transcribed

    AdmissibleDilationAt G a₀ U  :=  U ∈ unitaryGroup (V × A) ℂ
                                     ∧ ∀ i j, G i j = ∑ a, ‖U (i, a) (j, a₀)‖²

Two clauses and exactly two: **unitarity**, §3.4 p. 10's Stinespring output; and **reproduction of the
visible slice** under the frozen readback at the datum's anchor, §3.4 p. 10's marginalization
condition in the source's own form. Stated about the **external** object `(Γ t)ᵀ`, per act 7's clause
7; act 2's `RT1` licenses the orientation move and is consumed, never re-proved.

**No condition was added because it makes an outcome come out.** Two things are recorded as findings
rather than smuggled in as hypotheses:

1. **The anchor is a component of the datum**, not a property discovered afterwards. That is the
   amendment's convention, not Source A's — the source's "for at least some choices of `j′`" selects
   no anchor canonically — and it is a reason the strength is reduced.
2. **The predicate is stated at ONE time.** §3.4 gives pointwise existence; nothing derives a
   coherent time-indexed family. This is `D3`'s open gap, left open.

**Both dilations in every comparison below carry the SAME anchor**, which is stricter than the
amendment requires (it permits each compared dilation its own anchor, fixed in advance). The
divergence is therefore not produced by varying the anchor.

## `T3` — the frozen readback, and its three structural controls

    readback a₀ M i j  =  ∑ a, M (i, a) (j, a₀)

Input ancilla held at the datum's anchor; sum over the output ancilla. **The shape is Source A's
(§3.4 p. 10); extending it off the root is ours.** It acts on the (42)-type **stochastic** candidate,
and the type enforces that: `readback` takes a real matrix, so it cannot be applied to an amplitude or
to a unitary. No renormalization, no postselection, no anchor averaging, no §3.7 (45)/(46) import, no
alternative convention, no family — every prohibition the amendment listed holds in the formalization
by construction rather than by promise.

All three controls the amendment requires are proved:

| Control | Result | What it says, and what it does not |
| --- | --- | --- |
| **`R-1`** orientation and stochasticity | `readback_isColStochastic` | Column-stochastic on `V × A` in Source A's orientation ⟹ column-stochastic on `V`. |
| **`R-2`** agreement with §3.4 at the root | `readback_of_admissible` | An admissible dilation's rooted candidate reads back to the visible slice it dilates — so the frozen map **coincides with Source A's own readback wherever the source has one**, and departs only where the source supplies nothing. This is the load-bearing provenance control. |
| **`R-3`** equivariance under ancilla relabelling | `readback_relabel` | Proved for **any bijection of label sets** `σ : A ≃ A′`, carrying the anchor along — the amendment's form, not merely a permutation of one set. It says the map depends on the ancilla's structure and not on its names. It does **NOT** say the map is independent of *which* configuration is anchored, and may not be read that way. |

## `T4` — the two witnesses, each proved lawful, off-direct and realized

Nothing in this section is carried by a freeze; act 7 required all of it to be proved in-round.

| | Witness A | Witness B |
| --- | --- | --- |
| Odd slice | `A = ![![1,0],![1,0]]` (**rank one**) | `B = ![![1,0],![1/2,1/2]]` |
| `PPer` membership | `witnessA_lawful` | `witnessB_lawful` |
| Rank | rank one — collapses both configurations | `det = 1/2`, **full rank** |
| Off the direct branch | `¬ IsUnistochastic (Γ 1)ᵀ` | `¬ IsUnistochastic (Γ 1)ᵀ`, column sums `3/2` and `1/2` |
| `RootedRealization` lift | via merged `pper_has_responseRealization` | via merged `pper_has_responseRealization` |
| Contract standing | act 8's `CE1`, tied by `dc1_runs_on_act8_frozen_object` | proved in-round: `witnessB_admissible_continuous_extension` |

**Why two.** Witness A is rank-one degenerate, so a dilation result on it alone could be an artifact
of rank collapse rather than a fact about the dilation. Witness B separates the two. **Their results
are reported separately below and are never merged into one claim.**

## The two `DC1` exhibitions, reported separately

### The mechanism, stated plainly before the numbers

`admissible_mul_of_fixes_anchor` is the whole engine. **The anchored marginal reads only the
`a₀`-columns.** So right-multiplying an admissible dilation by any unitary that fixes those columns
leaves admissibility exactly intact — the rooted reproduction condition cannot see the change. But the
relative candidate of (39) p. 13 is built from `U(t ← 0) U†(t′ ← 0)`, and the **adjoint brings the
unread columns into the anchored one**. The rooted data therefore does not pin the relative candidate.

That is a statement about the interaction between §3.4's single-anchor marginalization and (39)'s
adjoint. It is not a statement about Source A's visible predictions, which is why the bound at the top
of this note is the operative one.

### Witness A — `witnessA_moves_visible_candidate`

Visible pair `(G₂, G₁) = (𝟙, Aᵀ)`, anchor `a₀ = 0`, ancilla `Fin 2`, dilated carrier `Fin 2 × Fin 2`.
Both dilations of `Aᵀ` are **permutation** matrices of the dilated carrier:

- `σ = prodComm`, giving relative-candidate readback `Aᵀ` (row 0 all ones);
- `σ′ = prodComm * swap((1,0),(1,1))`, giving relative-candidate readback `𝟙`.

Both reproduce `Aᵀ` at the same anchor (`admissible_permMatrix`, whose content is §3.4's
marginalization in the closed form `sum_indicator_perm` supplies). The readbacks differ at
`(i, j) = (0, 1)`: `1` versus `0`.

**Inside §3.4's stated bounds**: ancilla `N′ = 2 ≤ N² = 4`, dilated size `Ñ = 4 ≤ N³ = 8`.

### Witness B — `witnessB_moves_visible_candidate`

Visible pair `(G₂, G₁) = (𝟙, Bᵀ)`, anchor `a₀ = 0`, same carrier. Here the first dilation is an
explicit non-permutation unitary with `s = √(1/2)`,

    U (0,0)→(0,0) = 1,   U (0,1)→(0,1) = s,   U (0,1)→(1,0) = s,
    U (1,0)→(0,1) = −s,  U (1,0)→(1,0) = s,   U (1,1)→(1,1) = 1,

and the second is `U · P(swap((0,1),(1,1)))`, admissible by
`admissible_mul_of_fixes_anchor` because that permutation **fixes every anchored column**. The
readbacks differ at `(i, j) = (0, 1)`: `1/2` versus `0`.

**Witness B is full rank**, so the divergence is not an artifact of witness A's rank collapse. A
non-permutation dilation was necessary here rather than decorative: permutation dilations always read
back to `0/1` matrices (`readback_permMatrix_apply`), which cannot reproduce `Bᵀ`'s `1/2` entries.

### What the exhibitions are, at the level they are claimed

**Visible level, never operator level** — act 4's earned control, load-bearing here as in act 5. What
differs is the readback of the relative candidate on `V`, not the dilations, the unitaries or the
hidden carriers.

**`DC1` is EXISTENTIAL.** One pair of dilation choices, one time pair, one anchor, per witness. It
does **not** say that every off-direct OI process has choice-dependent visible predictions, and no
sentence here may be read that way.

## `DC4` — refuted, and at exactly the scope of the refutation

`VisibleInvariance G₂ G₁ a₀` is the universal statement act 7 required `DC4` to take — invariance over
**all** admissible anchored dilations of the visible pair. `not_visibleInvariance` turns each `DC1`
exhibition into a refutation of it, recorded separately per witness rather than left implicit.

**The scope, stated so it is not over-read.** What is refuted is `DC4` **for the admissible class the
statement names**: all admissible anchored dilations over the dilated carrier `Fin 2 × Fin 2` of that
visible pair at anchor `0`, under `R_{a₀}`. **A narrower class could still satisfy invariance** — for
instance one cut down by a coherence condition on the time-indexed family, which is exactly `D3`'s
open gap. Nothing here rules that out, and nothing here should be read as refuting every
`DC4`-shaped statement.

## The predictions, and whether each held

The freeze recorded its prior openly and at a stated strength — "tilted toward `DC1` rather than
balanced", at about one in three that `D4` would stop the round before layer 2.

| Prediction | Outcome |
| --- | --- |
| `D4` stopping the round at `DC2b` (~1 in 3) | **Did not happen.** `D4a` positive. |
| `D4b` negative, forcing an amendment and reduced strength | **Held.** This is the branch the round ran. |
| Tilted toward `DC1`, because act 5's unitary-lift freedom sits inside any dilated unitary | **Held**, and by a related but distinct mechanism: the anchor's blindness to the unread columns, combined with (39)'s adjoint. |
| Act 3's padding theorem arguing the other way **only if** `D5a` and `D5b` both hold | **Neither held**, so it shifted nothing — as the freeze specified in advance. |
| Slot 2 (the dilated carrier/datum definition) "likely to fire" once the anchor joined the datum | **Did not fire.** The anchor is carried as a parameter of `AdmissibleDilationAt`, so no separate datum definition was needed. |

**A prediction held is not a finding, and the freeze said so.** `DC1` is earned by the exhibitions, not
by the prior.

## Definitions, budget and axioms

**Four top-level definitions, from act 7's frozen six-slot budget:**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 — source-admissible dilation predicate (`T2`) | `AdmissibleDilationAt` | used |
| 2 — dilated-family carrier or datum, *if* the predicate cannot be stated without one | — | **not used**: the anchor is a parameter |
| 3 — visible readback (`T3`) | `readback` | used |
| 4 — `DC1`'s proposition | `MovesVisibleCandidate` | used |
| 5 — `DC4`'s proposition | `VisibleInvariance` | used |
| 6 — double-stochasticity screen, *if* needed | — | **not used**: act 6's merged lemma and act 2's `RT1` suffice |

**No seventh definition was introduced**, and none would have been without a further separately frozen
amendment. **No witness or dilation is a top-level definition** — each is built inside the proof that
needs it, per act 3's lesson.

**Axiom discipline: 25 named results, each with its own `#print axioms` line, every one printing
exactly `[propext, Classical.choice, Quot.sound]`.** No `sorry`, no `axiom`, no `native_decide`.

## What this round does NOT say

- **It does not say Source A's visible prediction is underdetermined.** `D4b` is negative; the
  readback is ours. This is the bound at the top of the note and it governs every sentence here.
- **It does not demonstrate that a candidate-selection principle is required**, does not adopt or
  propose one, does not adjudicate act 5's gauge-versus-empirical tension, and leaves `F1` versus `F2`
  undecided.
- **It does not name or adopt `C5`.**
- **It does not close `D3`'s coherent-dilation gap, and does not silently use it.** `T2` is stated at
  one time precisely so that the gap stays visible. `D3` remains **separately OPEN**.
- **It does not claim uniqueness, and `DC3` never arose.** Agreement on both witnesses would have
  earned only *not exhibited on these witnesses*; divergence on both earns two existentials, not a
  universal.
- **It does not claim `DC4` is false for every admissible class** — only for the class its statement
  names, at the exhibited pairs and anchor.
- **It does not restate `CE1` as a classification**, and witness B's contract standing is a second
  instance rather than an extension of `CE1`.
- **It does not revise `DC2a`**, `D4a`, `D4b`, `CE1`, or any act-1-through-6 finding. `BD3`, `BR3`,
  `RT1`, `CU1a`, `MP4`, `SA2`, `TI1`, `UB2`, `DC2a` and `CE1` are cited and unrevised.
- **It does not claim Source A's correspondence succeeds or fails**, is applicable or inapplicable. A
  construction that supplies no general readback is a fact about its reach; supplying one ourselves is
  a fact about our convention.
- **It does not use act 3's padding theorem as evidence.** Analogy and control only.
- **It claims nothing about the `n = 3` unistochasticity inclusion** beyond the level-3 citation, and
  nothing in the outcome rests on it.
- **It does not claim to be fully preregistration-compliant.** The `D5` chronological-ordering
  control is **NOT CERTIFIED** and was deviated from; outcome-independence is recorded as separate
  corpus-level evidence and never as that control's discharge.
- **It touches no manuscript.** No propagation in this round.
- **It says nothing about Track I**, and nothing here is evidence for anything there.

## What remains open, and what would settle it

1. **Robustness of the divergence under other readbacks.** Whether the `DC1` exhibitions survive a
   class of reasonable readback conventions is the question that would separate a fact about the
   dilation freedom from an artifact of `R_{a₀}` and the anchor. The amendment **deferred this to a
   separate later round with its own freeze**, deliberately run after this result so that an
   alternative convention could not be introduced while a result was in view. It is not preregistered
   yet.
2. **`D3` — the coherent-dilation gap.** Stinespring's pointwise existence, with no coherent
   time-indexed family derived or selected and no stated link from the visible family's regularity to
   `Θ`'s or `U`'s. Settling it would also decide whether a coherence-restricted admissible class
   restores invariance, which is the live way `DC4` could still hold on a narrower class.
3. **Whether Source A can select an anchor canonically.** The source's "for at least some choices of
   `j′`" does not. If something in the source did, the anchoring convention would stop being ours and
   the strength reduction on that axis would lift.
4. **Whether the exhibitions extend beyond two witnesses.** They are existential twice over. A
   statement about the OI class would need a universal theorem, and none is claimed.
