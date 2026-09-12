# Track B act 9 — result: readback robustness on the MAP axis (`P0a`)

## Outcome: **`RB3`**, and from it **`RB1-A`** and **`RB1-B`**

**`R-2` ALONE forces every same-interface readback to agree with the merged `R_{a₀}` on every
modulus-squared unitary matrix on the dilated carrier** — so `R-1` and `R-3` are **redundant for
this theorem**, and the forced domain contains **every** candidate the `DC1` test can generate.

From that, on each witness separately:

| Label | Result | Kernel name |
| --- | --- | --- |
| **`RB3`** | `R-2` alone forces the readback on every `|W|²` with `W` unitary | `rb3_forced_on_modulusSquared_unitary` |
| **`RB1-A`** | witness A's `DC1` divergence is preserved by **every** member of the frozen class | `rb1_witnessA` |
| **`RB1-B`** | the same on the **full-rank** witness B | `rb1_witnessB` |

**`RB2-A` and `RB2-B` are not this round's outcome**, since act 9's freeze declares `RB1-X` and
`RB2-X` contradictory for a fixed witness. Slot 4, `RB2`'s proposition, is therefore **unused**.

### The exact class IS representable, so the formalization stop was NOT invoked

Act 9's freeze made inability to encode the heterogeneous `R-3` a **formalization stop**, not a
reportable narrowing. **The stop did not fire.** The class is stated over the frozen cut exactly,
`R-3` quantified over a bijection of **two** label sets `σ : A ≃ A′`, via the freeze's preferred
route — conditional budget slot 2, the readback carrier. **No `RB1` label here is assigned against a
substitute class.**

## Provenance and the auditable chronology

| | |
| --- | --- |
| Frozen control plane | `preregistration.md` in this directory, blob `061fd38343185b4c6f764da0da9602367ad8f370` |
| **Mandated execution base** | `79872cbbb0e26188f619b8c6a99b379bb46b7b0c` — the merge commit of that control plane (PR #584) |
| Formal module | `verification/lean-mathlib/OIBridge/ReadbackRobustness.lean` |
| Act 7 layer 2's result (cited, unrevised) | `../act-07-dilation-choice/layer-2-result.md`, blob `02f93a1c3ec485b5f46b8e02ff52ca4f73e0ee89` |
| Act 7 layer 2's module (cited, unrevised) | `OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Readback amendment (`T3`, source of the cut) | `../act-07-dilation-choice/readback-amendment.md`, blob `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |

**The chronology control HELD, and what it certifies is stated exactly.** The preregistration blob —
including the property cut, the outcome grid **and the central forcing derivation** — was merged to
`main` at `79872cb` before any alternative-readback definition or robustness proof entered the
repository tree, and this round's work descends from that commit. Guard `R7-RBR` pins both: the blob
by content, and the ancestry by `git merge-base --is-ancestor`, **fail-closed** — if git is
unavailable the check fails rather than passing.

**The ancestry half has a precondition, and it is recorded rather than left to be discovered.** The
check can only be answered where the base commit is present, so the `Numerical probes` CI job
checks this repository out with `fetch-depth: 0`; the default depth-1 clone cannot see `79872cb` and
the guard **fails** there rather than skipping, which is the fail-closed behaviour working as
intended. A control that silently passed where it could not be evaluated would be no control, so the
CI history is part of the mechanism and not incidental to it.

**What it does not certify** is what anyone thought, drafted outside the tree, or worked out
privately. Git certifies what entered the tree and when; this round claims that and nothing more.
Act 7 layer 2's `D5` ordering control was recorded **NOT CERTIFIED** for exactly the want of such a
mechanism, and that status stands unrevised — this round repairs the practice going forward, not that
record.

**The prediction was preregistered, in full, in the merged blob.** Act 9's freeze wrote out the
forcing argument before execution and recorded in advance that the theorem would be **cheap** for a
named reason. Both held; see below.

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction.

## The class, as cut — and nonemptiness proved first

    R : (a₀ : A) → Matrix (V × A) (V × A) ℝ → Matrix V V ℝ

| | Condition, as frozen |
| --- | --- |
| **`R-1`** | column-stochastic on `V × A` in Source A's orientation ⟹ column-stochastic on `V` |
| **`R-2`** | for every `G`, `a₀`, unitary `W` with `AdmissibleDilationAt G a₀ W`: `R a₀ (|W|²) = G` |
| **`R-3`** | for every bijection of label sets `σ : A ≃ A′`, carrying the anchor: `R (σ a₀) M′ = R a₀ M` |

**`AdmissibleReadback` is that cut and nothing else** — no fourth condition, no enumeration.

**Nonemptiness is proved before any universal statement is made**
(`admissibleReadback_nonempty`): the merged `R_{a₀}` is a member, each condition discharged by the
corresponding merged theorem of act 7 layer 2 — `readback_isColStochastic` (`R-1`),
`readback_of_admissible` (`R-2`), `readback_relabel` (`R-3`, already merged in the heterogeneous
form the cut requires). **The member is constructed inside that proof**, not as a top-level
definition.

**The interface restriction is respected exactly, and the one place a reader might doubt it is named
here.** `Readback`'s field takes the ancilla **type** and its `Fintype`/`DecidableEq` instances in
addition to the anchor and the matrix. That is what makes a member a *family* rather than a map at
one fixed ancilla, and it is **required** to state `R-3` between two label sets at all. It supplies
**no information about the candidate**: a type and its finiteness say nothing about which time a
matrix came from or how it was produced. No time label, root flag, dilation datum or derivation
history enters, so no interface creep occurred.

## The mechanism, in one line

`AdmissibleDilationAt G a₀ W` constrains `G` **only** through the anchored marginalization. So for
any unitary `W`, setting `G` to that marginal makes `W` an admissible anchored dilation of it
**tautologically** — unitarity is the hypothesis, the marginalization clause is `G`'s own
definition — and universal `R-2` then pins the value.

`mul_conjTranspose_mem_unitaryGroup` supplies the coverage step as a proved fact rather than an
assumption: Source A (39) p. 13's relative candidate is built from `U₂ U₁†`, and a unitary times a
unitary's conjugate transpose is unitary, so every candidate `DC1` compares lies in the forced
domain.

`preservesDivergence_of_movesVisibleCandidate` is the transfer step, **stated once and applied
twice**, so neither witness result is an independent argument and the two stay exactly as separable
as act 7 layer 2 kept them.

## Why the theorem is cheap — recorded in the freeze, not discovered here

**The result is cheap, and act 9's freeze said so before it was proved.** What makes the
instantiation free is that the merged `AdmissibleDilationAt` imposes nothing on `G` beyond the
marginalization — not stochasticity, not a root condition. Universal `R-2`'s quantifier then does all
the work.

Act 8's result note had to record *after the fact* that its label was reached because the transcribed
contract was weak rather than because the construction was clever. **This round recorded the
analogous fact in advance**, which is what the merged blob is for.

**What the round bought, given that:** kernel certification of the forcing argument; the forced
domain identified and **proved** to contain every `DC1`-generable candidate; the `R-1`/`R-3`
redundancy **settled** rather than assumed, by a theorem whose hypothesis is the `R-2` clause alone;
the map-axis caveat sharpened; and `P0b` isolated as the live remainder.

## The predictions, and whether each held

| Prediction, from the merged freeze | Outcome |
| --- | --- |
| `RB3` — `R-2` alone forces agreement on every `\|W\|²`, `R-1`/`R-3` redundant | **Held**, exactly as derived |
| The forced domain contains every `DC1`-generable candidate | **Held**, proved via `mul_conjTranspose_mem_unitaryGroup` |
| The theorem would be cheap, for the named reason | **Held** |
| Failure mode: forced domain too small | Did not occur |
| Failure mode: class empty, making `RB1` vacuous | Did not occur — nonemptiness proved |
| The formalization stop might fire on heterogeneous `R-3` | **Did not fire**; the exact cut is representable via slot 2 |

**A prediction held is not a finding.** `RB3` is earned by the theorem, not by the prior; and the
freeze's own value is that the prior is checkable in git rather than asserted afterwards.

## The sharpened caveat — in the frozen wording, and no stronger

Act 7 layer 2's merged limitation read:

> A divergence found under `R_{a₀}` could still be an artifact **of the map or of the anchoring
> convention** rather than of the dilation freedom.

Act 9's freeze fixed, in advance, the exact wording `RB1` permits. That wording, and no more:

> **not an artifact of the readback map within the `R-1`/`R-2`/`R-3` same-interface class;
> dependence on the anchoring convention remains open.**

## `P0` is NOT closed. `P0b` is the live remainder

**The anchor axis survives this round untouched**, and `rb3_is_anchorwise` records why formally:
`RB3` forces the readback **at each anchor separately**, so the forced values at two anchors are the
anchored marginals at those anchors — **different matrices** in general. Nothing in the module
compares two reproducing anchors.

`P0b` therefore remains genuinely open, with the sub-obligation act 9's freeze already recorded: a
candidate alternative anchor must be one **both** compared dilations reproduce at, or the question is
vacuous there.

## What this round does NOT say

- **It does not close `P0`.** Only the map axis. No sentence here may be read as closing the anchor
  axis, and `rb3_is_anchorwise` exists to make that structural rather than promissory.
- **It does not revise act 7's merged `DC1`.** `DC1` stands exactly as merged at `e341563` —
  existential, reduced strength, under `R_{a₀}` on anchored dilations. This round adds **new
  labels** and **cites** `DC1`; `witnessA_moves_visible_candidate` and
  `witnessB_moves_visible_candidate` are consumed unmodified.
- **It does not upgrade `DC1`'s strength label.** The sharpening above is this round's finding about
  the map axis, carried here, never an amendment to act 7's record.
- **It does not say anything about maps of a different interface.** A readback receiving a time
  label, root flag, dilation datum or provenance is out of scope by the freeze, and `RB3` says
  nothing about one.
- **It does not claim `R-1` and `R-3` are redundant generally** — only for this theorem, on this
  domain. Both are still required for membership, and both were needed to prove nonemptiness.
- **It does not close or use act 7's `D3` coherent-dilation gap**, which remains **separately OPEN**
  and is still the live route by which a `DC4`-shaped invariance could hold on a narrower class.
- **It does not revise act 7 layer 2's `D5` NOT-CERTIFIED status.** That record stands; this round
  repairs the practice, not the past.
- **It does not adopt or propose a candidate-selection principle**, adjudicate act 5's
  gauge-versus-empirical tension, or decide `F1` versus `F2`.
- **It does not name or adopt `C5`.**
- **It does not claim Source A's correspondence succeeds or fails.**
- **It touches no manuscript.** No propagation in this round.
- **It says nothing about Track I**, and nothing here is evidence for anything there.

## Definitions, budget and axioms

**Three top-level definitions, from act 9's frozen four-slot budget:**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 — the admissible-readback class | `AdmissibleReadback` | used |
| 2 (conditional) — a carrier or bundle for a readback | `Readback` | **fired**, and necessarily: the class cannot be stated over bare functions at one fixed ancilla without losing heterogeneous `R-3`. The freeze named this the preferred route to encoding the exact cut. |
| 3 — `RB1`'s proposition | `PreservesDivergence` | used |
| 4 (conditional) — `RB2`'s proposition | — | **unused**: the freeze permits `RB2` as the negation of slot 3, and `RB1` landed on both witnesses |

**No fifth definition was introduced**, and none would have been without a further separately frozen
amendment. **No witness, dilation or alternative readback is a top-level definition** — the frozen
readback is built inside the nonemptiness proof, per the freeze and act 3's lesson.

**Axiom discipline: 8 named results, each with its own `#print axioms` line, every one printing
exactly `[propext, Classical.choice, Quot.sound]`.** No `sorry`, no `axiom`, no `native_decide`.

## What remains open, and what would settle it

1. **`P0b` — the anchor axis.** Whether some anchor both compared dilations reproduce at makes the
   two candidates agree. Now the live head of the queue; it needs its own freeze, including the
   nonemptiness sub-obligation on candidate anchors.
2. **`D3` — the coherent-dilation gap.** Stinespring's pointwise existence, with no coherent
   time-indexed family derived or selected. Separately open, untouched, and still the route by which
   invariance could hold on a coherence-restricted class.
3. **Interfaces richer than `T3`'s.** A readback receiving a time pair or provenance is a different
   question; `RB3` neither answers it nor forbids asking it in a later round with its own freeze.
