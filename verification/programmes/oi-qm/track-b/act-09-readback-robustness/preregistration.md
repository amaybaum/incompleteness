# Track B act 9 — readback robustness (`P0a`): CONTROL PLANE

**This file is a preregistration and nothing else.** It carries no execution, no Lean, no probe
guard, no roadmap edit, no alternative readback, and no outcome label. It is merged before any
execution begins, and the execution PR descends from the commit that merges it.

## Start state

| | |
| --- | --- |
| Merged `main` | `e34156331d3c543785fccf5bcd560b67998115e1` (PR #583) |
| Act 7's governing preregistration | `../act-07-dilation-choice/preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| Act 7's resumption freeze | `../act-07-dilation-choice/resumption-preregistration.md`, blob `3bb88717267a4adb45125b6277edae4e56c5cf26` |
| Act 7's resumption result (`D4a`/`D4b`) | `../act-07-dilation-choice/resumption-result.md`, blob `216cb9e65cda9b2f3b9777c2ecfcdf8d8bb58df0` |
| **The readback amendment** (`T3`) | `../act-07-dilation-choice/readback-amendment.md`, blob `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |
| Act 7 layer 2's result | `../act-07-dilation-choice/layer-2-result.md`, blob `02f93a1c3ec485b5f46b8e02ff52ca4f73e0ee89` |
| Act 7 layer 2's module | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** Sources B and C are not compared with
it on any axis. **Track I is not touched, in either direction**; neither branch is evidence for the
other.

## The licence to run, and what exactly is being asked

The readback amendment deferred this question by name:

> **The robustness question is real, and it is deferred rather than dismissed.** Whether a layer-2
> finding survives a class of reasonable readbacks is a genuine and worthwhile question — it would
> tell us whether the result is an artifact of this convention. **It is a separate later round with
> its own freeze**, run *after* the main layer-2 result, so that it cannot contaminate the
> preregistered dilation-choice test by supplying an alternative convention while a result is in
> view.

Layer 2 has landed at `DC1`, reduced strength, on witnesses A and B separately. **This round asks
whether that divergence is an artifact of the frozen readback map** — and only that.

## Scope: `P0a` is the MAP axis. `P0b`, the ANCHOR axis, is NOT in scope

Act 7 layer 2's merged limitation has **two** halves, and they are not closed by the same argument:

> A divergence found under `R_{a₀}` could still be an artifact **of the map or of the anchoring
> convention** rather than of the dilation freedom.

| | Axis | This round |
| --- | --- | --- |
| **`P0a`** | the readback **map**, at a fixed anchor | **IN SCOPE** |
| **`P0b`** | the **anchoring convention** — whether a different reproducing anchor makes the pair agree | **NOT IN SCOPE** |

**`R-3` does not close `P0b` and may not be read as doing so.** `R-3` is equivariance under
relabelling that *carries* `a₀` along; it says the map does not depend on the ancilla's **names**. It
says nothing about two **different** reproducing anchors on the same ancilla, and the amendment states
that restriction in terms.

**Nor does this round's central argument close `P0b`.** The forcing argument below fixes the map at
**each** anchor separately: for anchors `a₀ ≠ a₀′` it forces `R a₀ (|W|²)` and `R a₀′ (|W|²)`, but
those are different matrices, so a divergence at `a₀` is consistent with agreement at `a₀′`. `P0b` is
therefore a genuinely open and separately answerable question, with its own nonemptiness
sub-obligation: a candidate alternative anchor must be one **both** compared dilations reproduce at,
or the question is vacuous there.

**Consequence for the caveat, and the exact wording permitted.** If this round lands `RB1`, the
merged limitation sharpens to — and no further than —

> not an artifact of the readback map within the `R-1`/`R-2`/`R-3` same-interface class; dependence
> on the **anchoring convention** remains open.

**`P0` as a whole is NOT closed by this round**, and no sentence in its result may say or imply that
it is. `P0b` succeeds this round in the queue if `RB1` lands.

## The chronology control, made objectively auditable

Act 7 layer 2 ended with its `D5` chronological-ordering control recorded **NOT CERTIFIED**, because
the order of work was unverifiable after the fact. That failure is not repeated here, and the repair
is mechanical rather than testimonial:

1. **This preregistration blob, including the property cut and the outcome grid below, is merged into
   `main` before any alternative-readback definition, implementation, or robustness proof enters the
   repository tree.**
2. **The execution PR's base must be exactly the merge commit of this control-plane PR**, and its
   first commit must descend from it.
3. **The execution round's probe guard pins both**: this file's blob SHA, and the base ancestry of the
   execution work.

**The claim this control supports is scoped to the repository record, and is stated that way.** Git
certifies what entered the tree and when. It does not certify what anyone thought, drafted outside
the tree, or worked out privately, and this round claims no more than the former. That is a weaker
claim than "nobody knew the answer in advance" — deliberately, because the stronger one is not
checkable.

**It is in fact weaker than what this round has**, which is the next section: the central prediction
is written into this freeze *before* merge, so the merged blob is itself the record. That is the
opposite of layer 2's problem.

### Verified at freeze time

At the commit that opens this control-plane PR, the **only** dilated-carrier readback anywhere in the
repository tree is the frozen `OIBridge.DilationChoice.readback`. `OIBridge.CausalReadback`'s `C4e`
and `C4r` are a **different object** — candidate causal-readback forms on rooted one-time visible
marginals on `V`, not maps out of the dilated carrier — and are **not** members of this round's class,
not alternatives to `R_{a₀}`, and not compared with it. They are named here so that no later reader
mistakes them for prior art in this class.

## The family: signature first, then the property cut

### The interface, FROZEN

The amendment's `T3` fixes the readback's signature, and the signature is what makes this round
well-posed:

    R  :  (a₀ : A)  →  Matrix (V × A) (V × A) ℝ  →  Matrix V V ℝ

**A member of this round's class is a map of exactly that signature.** It receives the anchor and the
candidate matrix on the dilated carrier. It receives **no time label, no root/off-root tag, and no
provenance of how the matrix was produced**, because `T3` supplies none.

**This is the load-bearing restriction of the round, and it is frozen here rather than discovered.** A
map that receives extra information is **a different interface, not another member of this class**,
and a result about it would be a result about a different question. Anything of the shape

    R  :  (t t′ : T)  →  (a₀ : A)  →  Matrix (V × A) (V × A) ℝ  →  Matrix V V ℝ

or carrying a root flag, a dilation datum, or a derivation history, is **out of scope**. Such an
interface may be a legitimate later round; it is not this one, and this round's outcome says nothing
about it.

### The property cut, FROZEN — `R-1`, `R-2`, `R-3` as MEMBERSHIP conditions

The amendment states `R-1`, `R-2` and `R-3` as **structural controls layer 2 must prove about
`R_{a₀}`**. This round **repurposes them as the defining conditions of a class**, and that
repurposing is declared rather than slipped in. Their content is carried verbatim; only their role
changes, from properties proved of one map to conditions of membership for any map.

A map `R` of the frozen signature is **admissible** exactly when:

| | Condition |
| --- | --- |
| **`R-1`** | If `M` is column-stochastic on `V × A` in Source A's orientation, then `R a₀ M` is column-stochastic on `V`. |
| **`R-2`** | For every visible `G`, anchor `a₀` and unitary `W` on `V × A` with `AdmissibleDilationAt G a₀ W`: `R a₀ (Matrix.of fun p q => ‖W p q‖²) = G`. |
| **`R-3`** | For every bijection of label sets `σ : A ≃ A′`, relabelling `M` along `σ` and carrying the anchor: `R (σ a₀) M′ = R a₀ M`. |

**The class is cut by these properties and by nothing else.** No enumeration of "reasonable"
readbacks is permitted, in this file or at execution time — an enumerated list is selectable after the
outcome is known, which is the defect one level up from the one the amendment closed. **No fourth
condition may be added at execution time**; a fourth would require its own append-only amendment,
merged before use.

**Nonemptiness is an obligation, not an assumption.** The execution must prove the merged
`OIBridge.DilationChoice.readback` is a member — `R-1` from `readback_isColStochastic`, `R-2` from
`readback_of_admissible`, `R-3` from `readback_relabel`, all three already merged. A class whose
nonemptiness is unproved makes every universal statement about it vacuously reportable, and that is
not a result.

### `R-2`'s two readings, and which one this round formalizes

The amendment's `R-2` row says the map "applied to the dilated **rooted** candidate returns the
original rooted candidate", "under the rooted reproduction hypothesis on the datum". Two readings:

- **Universal `R-2`** — the hypothesis is `AdmissibleDilationAt G a₀ W` and nothing more, quantified
  over all such data; the map sees only `|W|²`. **This is the reading this round formalizes**, and it
  is the only one the frozen signature can express: the merged Lean form is exactly
  `readback_of_admissible`, whose hypothesis is that predicate.
- **Provenance `R-2`** — the condition applies only when the input is *known* to have arisen at the
  root. **This is not expressible at the frozen signature**, since the map receives no such
  information. It is a condition on a different interface, per the previous section, and is out of
  scope.

**The freeze does not claim universal `R-2` is the amendment's only possible English reading.** It
claims that it is the only one that is a well-formed condition on a map of the frozen signature, and
it fixes that as the round's reading before any proof is attempted.

## The outcome grid — PER WITNESS, and asymmetric

Act 7 layer 2 reported witnesses A and B separately and never merged them. **This round keeps them
separate on the same rule.** Four labels, two per witness:

| Label | Statement |
| --- | --- |
| **`RB1-A`** | **Every** admissible readback (frozen signature, frozen property cut) preserves witness A's `DC1` divergence. |
| **`RB2-A`** | **There exists** an admissible readback under which witness A's compared pair **agrees**. |
| **`RB1-B`** | **Every** admissible readback preserves witness B's `DC1` divergence. |
| **`RB2-B`** | **There exists** an admissible readback under which witness B's compared pair **agrees**. |

`RB1-X` and `RB2-X` are contradictory for a fixed witness; **the pair across witnesses is not
required to match**, and a split outcome (`RB1-A` with `RB2-B`, or the reverse) is a permitted and
reportable result, not a sign of error.

**`RB1` is earned only by a universal theorem over the class as cut.** It is never earned by an
unsuccessful search for an erasing readback — act 7's `DC3`/`DC4` discipline, one round on.
**`RB2` is earned only by an exhibited member**, proved admissible against all three conditions, not
by failure to prove `RB1`.

### The stronger outcome, named in advance so it is not reported as a surprise

| Label | Statement |
| --- | --- |
| **`RB3`** | `R-2` **alone** forces every same-interface map to agree with the merged `R_{a₀}` on **every** modulus-squared unitary matrix on the dilated carrier — so `R-1` and `R-3` are **redundant** for this robustness theorem, and the forced domain contains every candidate the `DC1` test can generate. |

**`RB3` is a statement about which control does the work.** If it lands, `RB1-A` and `RB1-B` follow
from it, and the round must say that they follow from it rather than presenting three independent
findings. `RB3` does **not** say `R-1` and `R-3` are redundant generally — only for this theorem, on
this domain.

## The preregistered prediction, recorded at its actual strength

**`RB3` is predicted, and the prediction is a DERIVATION checked against the merged definitions
before this freeze was written — not a guess, and not a finding.** The argument, recorded in full so
the execution cannot quietly substitute a different one:

Let `W` be any unitary on `V × A` and put `G := readback a₀ (Matrix.of fun p q => ‖W p q‖²)`, that is
`G i j = ∑ₐ ‖W (i,a) (j,a₀)‖²`. Then `AdmissibleDilationAt G a₀ W` holds **tautologically**: its first
clause is `W`'s unitarity and its second is `G`'s definition. Universal `R-2` therefore forces
`R a₀ (|W|²) = G = readback a₀ (|W|²)`. Every candidate compared by `DC1` has the form `|U₂ U₁ᴴ|²`
with `U₂ U₁ᴴ` unitary, hence lies in that domain. So `RB1-A` and `RB1-B` both hold, and neither `R-1`
nor `R-3` is used.

**Why the round is still worth running, stated before it runs.** The theorem is **cheap** — the
merged `AdmissibleDilationAt` imposes nothing on `G` beyond the marginalization, which is exactly
what makes the instantiation free. Act 8's result note had to record, after the fact, that its label
was reached because the transcribed contract was weak rather than because the construction was
clever. **This freeze records the analogous fact in advance**: if `RB3` lands, it lands because
`R-2`'s universal quantifier is strong and the admissibility predicate is permissive, not because the
class was cleverly analysed. What the round buys is (i) kernel certification, (ii) the exact forced
domain and whether it covers every `DC1`-generable candidate, (iii) the `R-1`/`R-3` redundancy
question settled rather than assumed, (iv) the caveat sharpened on the map axis, and (v) `P0b`
isolated as the live remainder.

**The prediction could fail in two identified ways**, and each is a reportable finding rather than a
defect: the forced domain might not contain every `DC1`-generable candidate; or universal `R-2` might
turn out unsatisfiable in combination with `R-1` at the frozen signature, which would make the class
**empty** and every `RB1` vacuous — which is why nonemptiness is an obligation.

**A third possibility is NOT a reportable outcome but a STOP.** If the exact property cut cannot be
represented, the round does not continue against whatever class the encoding does express. See the
formalization stop condition below.

## The formalization STOP condition — the class is not negotiable at execution time

**The admissible family is EXACTLY the frozen property cut. If the exact cut cannot be represented,
the round STOPS; it does not proceed against a different class.**

`R-3` is stated for a bijection between **two** label sets. A Lean encoding that fixes one ancilla
type cannot express it; what it can express is the same-type restriction, which is **weaker** than
`R-3` and therefore admits a **WIDER** class of maps than the cut.

**The direction of the difference is not the point, and naming it makes the reason sharper.** Over a
wider class, `RB1` — a universal — would be a **stronger** statement than the frozen one, while `RB2`
— an existential — would be a **weaker** one. Substituting the encodable condition would therefore
strengthen one frozen label and weaken the other, in a way no reader could detect from the label
itself. That is why an execution-time substitution is unsafe whichever way it points, and why this is
a stop rather than a scope note.

**The permitted responses, and only these:**

1. **Encode the exact cut.** Conditional budget slot 2 — a carrier or bundle for a readback — exists
   for exactly this: use it to carry the polymorphic family so `R-3`'s heterogeneous form is stated as
   frozen. **This is the preferred route.**
2. **Stop and amend.** If slot 2 does not suffice, **no `RB1` or `RB2` label is assigned**, the
   execution halts, and the next artifact is a separately frozen append-only amendment fixing the
   class actually to be quantified over — reviewed and merged before any further execution, under this
   same split protocol. The halt is reported as a **formalization stop**, never as a robustness
   outcome.

**`RB3` is exempt, and the exemption is bounded.** `RB3` is a statement about every same-interface map
satisfying **`R-2` alone**; it mentions neither `R-1`, `R-3` nor the class, so it can be stated and
proved whether or not the cut is encodable. **`RB3` landing does NOT license assigning
`RB1-A`/`RB1-B`** when the class is not the frozen one: the per-witness labels are defined over the
cut and are assigned only against the cut. A round that proves `RB3` and stops short of the frozen
labels is a legitimate **partial** outcome and is reported as one.

## Named hazards

1. **Vacuity.** A universal statement over an empty or unexhibited class is not a result. Nonemptiness
   is proved first, from the three merged theorems.
2. **Interface creep.** The single most likely way to reach a wrong `RB2` is to admit a map that
   secretly receives provenance — a time index threaded through a structure field, a dilation datum
   passed alongside, a class indexed by the root. The signature above is the test.
3. **Reading `RB1` as closing `P0`.** It closes the map axis only. See the scope section.
4. **Reading `RB1` as strengthening `DC1`'s merged label.** See the revision rule.
5. **Assigning a frozen label against an unfrozen class.** See the stop condition above — the one
   hazard this round answers with a halt rather than a note.

## The revision rule

**Act 7's merged `DC1` never changes.** It stands as merged at `e341563`, existential, at reduced
strength, under `R_{a₀}` on anchored dilations. This round produces **new labels** in its own grid and
**cites** `DC1`; it does not rewrite, re-strengthen or re-scope it. The same discipline act 7's
resumption used when it declined to re-answer `D2`, and act 7 layer 2 used when it declined to stretch
`CE1` over witness B.

A sharpened *interpretation* of the merged limitation is permitted and is the point of the round — in
the exact wording fixed in the scope section, and carried as this round's finding rather than as an
amendment to act 7's.

## Definition budget

The execution introduces **at most four** top-level definitions, and these are the four:

1. **The admissible-readback class** — the property cut of the frozen signature. *Needed.*
2. **A carrier or bundle for a readback**, *if* the class cannot be stated over bare functions without
   one. *Conditional.*
3. **`RB1`'s proposition** — divergence preserved across the class, at one visible pair and anchor.
   *Needed.*
4. **`RB2`'s proposition** — some member makes the pair agree — *unless* it is stated as the negation
   of (3), in which case this slot is unused. *Conditional.*

**A fifth definition requires its own append-only amendment**, separately frozen and merged before
use. **No witness, dilation or alternative readback is a top-level definition**; each is built inside
the proof that needs it, per act 3's lesson and act 7 layer 2's practice.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide`.

## Non-doings

Do not: assign `RB1` or `RB2` against any class other than the frozen cut; run any part of the
execution before this file is merged; introduce an alternative readback,
or any definition or proof about one, before then; enumerate a family instead of cutting it by the
frozen properties; add a fourth membership condition; admit a map of a different signature; average
over anchors; postselect; renormalize; import §3.7's (45)/(46); apply any readback to amplitudes or to
a unitary; adopt `candidateOf`; touch `P0b`'s anchor axis; claim `P0` closed; revise `DC1`, `DC2a`,
`D4a`, `D4b`, `CE1`, act 7 layer 2's `D5` NOT-CERTIFIED status, or any act-1-through-8 finding; close
or silently use act 7's `D3` coherent-dilation gap; adopt or propose a candidate-selection principle;
name or adopt `C5`; compare Source A with Source B or Source C on any axis; source anything across to
Track I; edit manuscripts.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.** No Lean, no probe guard, no roadmap edit, no census edit.
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean, the
  result note, the probe guard (pinning this blob and the base ancestry), the `ROADMAP` `P0`
  propagation, and the census entry.
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. The class as cut, with nonemptiness **proved** from the three merged theorems, and the exact cut
   confirmed **represented as frozen** — or, failing that, the formalization stop reported with **no**
   `RB1`/`RB2` label assigned;
2. `R-2`'s reading, fixed here, stated as fixed here;
3. the per-witness outcome — `RB1-A`/`RB2-A` and `RB1-B`/`RB2-B` — **separately**, with the route to
   each label, and `RB3` recorded if it lands, with `RB1-A`/`RB1-B` presented as following from it
   rather than as independent findings;
4. the exact forced domain, and whether it contains every `DC1`-generable candidate;
5. whether `R-1` and `R-3` were load-bearing, answered rather than left implicit;
6. the sharpened caveat, in the wording the scope section fixes and no stronger;
7. **`P0b` stated as the live remainder**, with `P0` recorded NOT closed;
8. the chronology control, with what it does and does not certify;
9. the definition count against the four-slot budget, with conditional slots marked fired or unused;
10. the axiom report, one line per named result.
