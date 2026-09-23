# Substratum — A6 background independence, round 1: definition and closure — RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3`, merged into `main` as
`8792801beeeccbf0673db137cae83e6663d21fba` (PR #593) — the freeze's mandated execution base.

**This is a definition round, not a proof round**, and the outcome below is read accordingly:
A6 now has candidate predicates on the least interface and a determination by quotation of which
manuscript coordinate asserts which; it has **no adopted predicate**, and nothing here says A6
holds of anything physical. `A6-inv`, `A6-cov`, `A6-glob` and `A6-sd` are four objects on three
interfaces and must not be silently identified; any sentence using "A6" without a suffix, other than
in a quotation or in "the `ROADMAP` row A6", is a defect.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `8792801beeeccbf0673db137cae83e6663d21fba` (merge of PR #593) |
| This round's frozen control plane | `preregistration.md`, blob `afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3` |
| The `Substratum` structure, `A1`–`A5`, `A3Family`, `waveSubstratum` and its five theorems; no A6 predicate | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` — matches the freeze |
| The A1–A6 list and §3 of the reconstruction | `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d` — matches the freeze |
| §3.1 and §4.4–§4.6 | `papers/SM.md`, blob `bad76808e6ab708732edcb3c6294236aa052cf34` — matches the freeze |
| The coupling graph as fixed one-step dependency | `papers/Main.md`, blob `deedef7a0053c6fa7054cad6bc1f9e5ee6580517` — matches the freeze |
| The queue row (`P1`, A6, `GAP`) and its section | `verification/ROADMAP.md`, blob `27c29ee54a9216b4d20e4f8e29822974f1855cf0` at the base — see the discrepancy note below |
| This round's module | `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean` |

**One discrepancy against the freeze's start-state table, recorded and not repaired.** The freeze
pins `verification/ROADMAP.md` at blob `3965d9305452cbfa37104366031655f07fb897aa`; at the mandated
base the file is blob `27c29ee54a9216b4d20e4f8e29822974f1855cf0`. The difference is the act 12
propagation that landed between the freeze's `main` and this round's base — the `P0` row and a new
act 12 section — and the row `P1 — A6, GAP` together with the whole section "P1 — A6, and what is
and is not already represented" is byte-identical in both blobs. The line coordinates the freeze
cites into the `ROADMAP` (`ROADMAP.md:227–229`, `:231–235`) refer to the pinned blob; the same text
sits at lines 283–285 and 287–291 of the base's blob. Nothing this round consumes from the
`ROADMAP` moved. The preregistration is immutable and is not edited for this.

## Outcome, in one line

**Every kernel target landed positively at evidence level 2, as predicted, and both type-P
determinations returned their predicted labels: `D1` is (a) at the definition with (b) as its
stated consequence, UNDECIDED at the three use-sites, and (d) at `SM.md:100`; `D2-iii` is:
statable, degenerate, not the axiom, gap unchanged at manuscript level.** No target moved from its
predicted strength, no target fell to UNDECIDED, and no falsifier of `D1` occurred. **No reading is
adopted.**

## `D1` — which reading each manuscript coordinate asserts

**`D1` — evidence type P**: a prose determination by quotation with coordinates against the blobs
in the start-state table, made from the quotations the freeze records and no others. It is not a
kernel result and does not appear in the axiom table.

**Outcome: (a) at the definition, with (b) as its stated consequence; UNDECIDED at the use-sites;
(d) at `SM.md:100`.** By coordinate:

1. **`Substratum.md:102` — (a), with (b) as its stated consequence.** The definition reads:

   > (A6) **Background independence.** The dynamics is invariant under spatially-varying
   > internal-index transformations that preserve the cubic-symmetric coupling matrix pointwise. The
   > promotion of the resulting global commutant symmetry to local gauge invariance is then a
   > derivation step ([SM §3.1]) — not part of the assumption itself.

   The first sentence is `A6Inv` word for word: "the dynamics" is the fixed rule `F`; "invariant"
   is `F (g · c) = g · (F c)`; "spatially-varying internal-index transformations" are
   `g : ι → AddAut V`; "preserve the cubic-symmetric coupling matrix pointwise" is
   `PreservesPointwise g M`. So the coordinate asserts **(a)** at `Substratum.md:102`. The second
   sentence names "the resulting global commutant symmetry" — `A6Glob`, reading **(b)** — as what
   the assumption yields, and places the promotion to local gauge invariance outside the
   assumption: "a derivation step … not part of the assumption itself". The definition is the
   authoritative coordinate and its label stands on its own sentence.

2. **`Substratum.md:104` — UNDECIDED.** The overlap remark reads: "A4 (center independence) and A6
   (background independence) overlap in physical content (A6 promotes the symmetry that A4
   constrains)". The obstruction is the verb: "A6 promotes" attributes the promotion to A6, which is
   compatible with shorthand for the derivation the definition names — A6 being the premise *from
   which* the promotion is derived, together with further premises — and equally compatible with a
   genuinely covariant reading **(c)** in which the promotion is what A6 itself supplies. The
   sentence excludes neither, so the text does not fix a reading here.

3. **`Substratum.md:162` — UNDECIDED.** Stage 2, step (d) closes: "Background independence (A6)
   then promotes the remaining global $SU(3) \times SU(2) \times U(1)$ to local gauge invariance
   ([SM §3.1])." The same obstruction: "promotes" with A6 as its subject. The citation of
   `[SM §3.1]` is the citation the definition attaches to the derivation step, which is consistent
   with the shorthand reading, but the sentence as written does not exclude **(c)**, so the label is
   UNDECIDED.

4. **`SM.md:110` — UNDECIDED.** "Background independence is then the premise promoting the
   surviving global stabilizer to the local gauge reading developed below." The word "premise" is
   the shorthand reading's word — A6 as a premise of a derivation — and "promoting" is the covariant
   reading's verb; the sentence carries both and fixes neither. The coordinate also scopes the
   promotion to "the H-link + H-cust single-copy branch" (a "conditional carrier reading"), which
   bears on what is promoted and not on which reading of A6 does the promoting.

5. **`SM.md:100` — (d).** "If space is the coupling graph, background independence requires the
   graph to evolve with the state: s(t+1) = φ_{s(t)}(s(t)), where each φ_s is a bijection but
   G_{φ_s} varies with s." This is `A6-sd`: a configuration-indexed family of rules with bijectivity
   automatic (`SM.md:102`), constrained at `SM.md:104` and built explicitly at `SM.md:108`. It is a
   structural property of a rule family, not an invariance under any group, and it is a separate
   object under a shared name.

6. **`Substratum.md:220` fixes nothing**: "A6 (background independence) is standard for gauge
   theories." **`Substratum.md:144`, `:188` and `:192` consume A1–A6 by name** as inputs of Stage 2,
   Lemma 23.0 and Theorem 23 and fix nothing.

**The use-sites are reported UNDECIDED, not as a contradiction with the definition**, exactly as
the freeze's prediction put it: both the shorthand reading and **(c)** are compatible with the
sentences as written. **No falsifier fired**: no use-site's quoted text excludes the shorthand
reading — so no coordinate is reported **(c)** and the outcome does not become SPLIT on that
ground — and none excludes **(c)** — so none is reported **(a)**. The transformation law at
`SM.md:112` and the sentence "The wave equation is invariant. This is local gauge invariance" at
`SM.md:114` are the *derived* object — the content `A6Cov` formalizes — presented as the output of
the derivation step, and they are not among the coordinates the freeze lists for `D1`; they are
recorded here as what the derivation produces, not as a coordinate asserting a reading of A6.

**A point where the freeze's outcome menu is ambiguous, recorded and not resolved here.** The menu
defines SPLIT as "different coordinates assert different readings, each listed with its
coordinate", and taken literally (a) at `Substratum.md:102` beside (d) at `SM.md:100` satisfies it.
The freeze's own prediction phrase does not use the label for that pair, calls `SM.md:100` "a
separate object" under a shared name, and reserves SPLIT for a use-site excluding the shorthand
reading; this note follows the prediction phrase and reports by coordinate. Whether the shared name
across `A6-sd` and the gauge readings should be labelled SPLIT is the freeze's to say in an
append-only amendment, not this note's.

**What `D1` does not decide:** which reading the programme *adopts*. That is an owner decision,
made after `D1`, `D3` and `D4` are reported together, and it is named below as **open and not
this round's**.

## `D2` — the manuscripts' wave rule against `A6-inv` on the least interface

`waveSubstratum d L q α` has alphabet `V = ZMod q` and no internal index: the case `K` a singleton,
where `AddAut (ZMod q)` is the unit group acting by multiplication, the site coupling is
`mulLeft α`, and every `g` preserves it pointwise. `A6-inv` is therefore **statable** on
`waveSubstratum` — read on `(waveSubstratum d L q α).R.F` with no new definition — in a
**degenerate** form.

- **`D2-i` — level 2, positive, as predicted.** `d2i_wave_witness` pins the frozen witness by
  equations inside the statement: `d = 1`, `L = 3`, `q = 3`, `α = 1`; `g 0 = 1`, `g 1 = 2`,
  `g 2 = 1` as unit multiplications on `ZMod 3` (`∀ v, g (fun _ => 1) v = 2 * v`, the identity at
  the other two sites); `c` the indicator of site `1` with value `1`
  (`c i = if i 0 = 1 then 1 else 0`); every `g` preserves `mulLeft 1` pointwise; and
  `F (g · c) 0 = 2` and `g 0 (F c 0) = 1`. `d2i_wave_not_a6inv` concludes
  `¬ A6Inv (waveSubstratum 1 3 3 1).R.F (mulLeft 1)`. The frozen witness was used unchanged.
- **`D2-ii` — level 2, positive, as predicted.** `d2ii_wave_a6glob`:
  `A6Glob (waveSubstratum d L q α).R.F (mulLeft α)` for every `d L q α`. The one risk the freeze
  named — the step from an additive automorphism of `ZMod q` to a `ZMod q`-linear one — did not
  arise: the commutation of `g` with `α` is the hypothesis of `A6Glob` itself, so a constant `g`
  passes through `α · Σ` by additivity alone. (The additive-to-linear step was proved anyway, as
  `addAut_zmod_smul`, where `D4-b`'s symmetric-point instance needs it.)
- **`D2-iii` — evidence type P, as predicted, in the freeze's words: statable, degenerate, not
  the axiom, gap unchanged at manuscript level.** **The degenerate form is not the manuscripts'
  A6.** With `K` a singleton the transformation group is the alphabet's unit group acting by
  rescaling, which is the amplitude-scale freedom the manuscripts assign to A5 —
  `Substratum.md:100`: "amplitude-scale gauge invariance — that the field-value scale is
  unphysical" — not the internal-index freedom of A6, which needs `K = 6`. Accordingly `D2-i` and
  `D2-ii` are reported as facts about the degenerate form, labelled so, and the wave substratum's
  A6 status at manuscript level remains a gap after `D2`, exactly as the interface audit's rule
  requires: a predicate found stronger, weaker or differently scoped than the axiom is recorded as
  a gap, not adjusted. No manuscript coordinate assigns site-dependent alphabet rescaling to A6
  rather than to A5, so the falsifier did not fire.

**So the answer to "vacuous or unstatable" is: neither.** Statable; degenerate; false in the
degenerate form at `q = 3`; true in its global specialization; and not the axiom.

## `D3` — `A6-inv` and `A6-cov` are provably distinct on a small carrier

- **`D3-a` — level 2, positive, as predicted.** `a6cov_all`: `∀ N M, A6Cov N M`. The two-line
  computation: `linkF N (gaugeLink g M) (g · c) i = Σ_j g i (M i j ((g j)⁻¹ (g j (c j))))
  = g i (Σ_j M i j (c j))`. **Bounded reading, as frozen:** **`A6-cov` restricts no link-coupled
  rule; its content is the interface, not a constraint.** This is a statement about the frozen
  `A6Cov` on link-coupled rules over a finite alphabet; it is not "local gauge invariance is
  trivial" and not a statement about `SM.md:114`'s derivation on the complex lift, which is outside
  the interface.
- **`D3-b` — level 2, positive, as predicted.** `d3b_witness` pins the frozen carrier by equations
  inside the statement: `ι = Fin 2` with `N 0 = {1}`, `N 1 = {0}`; `V = Fin 2 → ZMod 2`;
  `M i j = id`, which every `g` preserves pointwise; `g 0 = id`, `g 1` the component swap
  (`∀ v, g 1 v = fun k => v (k + 1)`); `c 1 = (1, 0)`; then `linkF N M (g · c) 0 = (0, 1)` and
  `g 0 (linkF N M c 0) = (1, 0)`. `d3b_not_a6inv` concludes `¬ A6Inv (linkF N (fun _ _ => id)) id`
  on that carrier.

**Bounded reading of `D3`, as frozen.** **The distinction is one-directional.** On link-coupled rules
`A6-cov` always holds and `A6-inv` sometimes fails, so `A6-inv` is the strictly stronger condition
there, and **no rule satisfies `A6-inv` and fails `A6-cov`**. "Provably distinct" means exactly:
there is a carrier on which one holds and the other fails, in the one direction available. That
`A6-inv` and `A6-cov` live on different interfaces — **`A6-cov` is not a predicate of a
`Substratum`**, it is a predicate of a neighbourhood function and a link coupling — is the first
reason they must not be identified; `D3` is the second.

## `D4` — single-edge rigidity of `A6-inv` on the constant-coupling rule

- **`D4-a` — level 2, positive, as predicted.** `d4a_single_edge`: if `F (g · c) = g · (F c)` for
  the rule `linkF N (fun _ _ => M₀)` and a given `g`, and `j ∈ N i`, then
  `∀ v, g i (M₀ v) = M₀ (g j v)`. Proof shape as frozen: evaluate at the indicator of `j` with value
  `v`; the sum over `N i` has one nonzero term. The indicator-sum formalization, the only cost the
  freeze named, is `Finset.sum_eq_single_of_mem` with `Pi.single`.
- **`D4-b` — level 2, positive, as predicted.** `d4b_edge_rigidity`: with `M₀` injective and `g`
  preserving `M₀` pointwise, `g i = g j` on every edge; `d4b_not_a6inv_of_nonconstant`: a
  nonconstant `g` in the pointwise stabilizer, with one edge between sites where it differs,
  refutes `A6-inv` for the constant-coupling rule. `a6glob_constLink`: `A6-glob` holds for every
  constant-coupling rule. `d4b_symmetric_point` states the symmetric point abstractly — an
  injective `M₀` whose pointwise stabilizer is all of `AddAut V`: `A6-inv` fails whenever
  `AddAut V` has two elements and `N` has an edge between distinct sites, while `A6-glob` holds —
  and `d4b_mu_id` instantiates it at the manuscripts' `M = μ I_6`: on `V = K → ZMod q`, with the
  coupling pinned by `M₀ v = μ • v` for a unit `μ`, injectivity is the unit and the pointwise
  stabilizer is everything by `addAut_zmod_smul` (every additive automorphism of `K → ZMod q` is
  `ZMod q`-linear). `addAut_nontrivial_of_ne_neg` supplies the two elements from any `v ≠ -v`. The
  "edge" is between distinct sites, `i ≠ j`, which is what "sites where it differs" requires; a
  self-loop would force nothing.

**Bounded reading of `D4`, as frozen. Single-edge by design.** It needs no connectivity. Its
connected-carrier corollary — on a connected `N` with injective `M₀`, `A6-inv` holds iff every
pointwise-stabilizing `g` is constant, i.e. iff `A6-inv` adds nothing to `A6-glob` — is recorded
here as analysis, **not** as a target, because "connected" is a definition this round does not
spend, and no connectivity definition is spent. **What `D4` says about the manuscripts:** under
reading (a), the manuscripts' own `K`-component rule at `M = μ I_6` violates A6 for every
nonconstant `G(n)`; under (b) it satisfies A6; under (c) A6 is an identity on it. `D4` does not
choose among these.

## The relations among the readings, at the strength reached

| relation | result | strength |
| --- | --- | --- |
| `A6-inv ⟹ A6-glob`, by specialization, always | `a6glob_of_a6inv` | level 2 |
| the phase-space form is a corollary of the `F`-form, not a reading | `leap_siteAct` | level 2 |
| `A6-cov` is an identity on link-coupled rules | `a6cov_all` | level 2 |
| `A6-inv` fails on a link-coupled rule; the distinction is one-directional | `d3b_not_a6inv` with `a6cov_all` | level 2 |
| `A6-inv` is rigid on the constant-coupling rule: single-edge, then `g i = g j` | `d4a_single_edge`, `d4b_edge_rigidity` | level 2 |
| at the symmetric point `A6-inv` fails and `A6-glob` holds | `d4b_symmetric_point`, `d4b_mu_id`, `a6glob_constLink` | level 2 |
| on `waveSubstratum` the degenerate `A6-inv` fails and `A6-glob` holds | `d2i_wave_not_a6inv`, `d2ii_wave_a6glob` | level 2, degenerate form |

## What these outcomes do NOT license

- **Nothing here says A6 holds of the physical substratum**, or fails of it. Every kernel target is
  about a frozen reading on a frozen carrier; `D1` is about text.
- **Nothing here touches the Standard-Model gauge-group derivation.** Theorems 5 and 7 of `SM`,
  H-link, H-cust, the `(3,2,1)` decomposition, the condensate stabilizer and the reduction to
  `SU(3) × SU(2) × U(1)` are neither consumed nor judged. `D3-a`'s "identity" is a statement about
  the frozen `A6Cov` on link-coupled rules over a finite alphabet, not about the promotion to local
  gauge invariance on the complex lift, which is outside the interface.
- **Nothing here is about Track B, `P0`, the fibre-Gram classification, or hydrodynamics.** The
  substratum programme and the OI→QM programme share the repository and nothing else in this round.
- **No reading is "the" A6.** After this round A6 has candidate predicates and a determination of
  which coordinate asserts which; it has no adopted predicate, and the `ROADMAP` row's label
  changes only by an owner decision recorded in an execution PR's propagation, not by this note.
  **The owner decision these outcomes set up — which reading to adopt — is named as open and not
  this round's.**
- **`A6-sd` is not formalized**, and nothing is said about H-Bell, preparation-indexed adjacency,
  or the state-dependent Einstein construction.
- **No manuscript is edited by this round.** No textual conflict was preregistered and none is
  reported: the definition asserts `A6-inv`, and the use-sites are UNDECIDED between shorthand for
  its derivation and a covariant reading. What `D1` reports at the use-sites is reported, not
  repaired; whether and how to sharpen the wording is an owner call for a propagation round.
- **Nothing here decides whether A4 and A6 overlap** (`Substratum.md:104`) or whether A6 is
  independent of A1–A5.

## The points where the manuscripts' intended reading was found unsettled, listed and not resolved

1. **The definition/use-site split.** `Substratum.md:102` asserts `A6-inv` with `A6-glob` as its
   consequence and places the promotion outside the assumption; `Substratum.md:104`, `:162` and
   `SM.md:110` say A6 "promotes" and are UNDECIDED between shorthand for that derivation and a
   covariant reading. Reported, not repaired.
2. **The `μ I_6`-versus-block-scalar denotation of "the cubic-symmetric coupling matrix".** Whether
   `Substratum.md:102`'s phrase denotes the scalar `M = μ I_6` of `SM.md:422`, whose pointwise
   stabilizer is everything, or the block-scalar `O`-equivariant object whose stabilizer is
   `U(3) × U(2) × U(1)`, is not decided here: `M` is a parameter of every reading, so both are
   instances, and no instance was chosen to resolve it.
3. **The shared name between `A6-sd` and the gauge readings.** `SM.md:100` calls a state-dependent
   coupling graph background independence; `Substratum.md:102` calls an invariance under
   internal-index transformations background independence. A coupling that depends on the state
   and a coupling that transforms under a gauge group are different objects, and `Main.md:392`'s
   preparation-indexed adjacency is the former. Named, and not identified.

## The chronology control

**`R7-A6D` certifies the strong property**, reusing act 10's mechanism by name through act 12's
copy:

- the preregistration blob is pinned **by content** to `afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3`;
- the real execution head `H` is resolved from `pull_request.head.sha` in a PR run — **never** the
  synthetic merge commit — failing closed with no fallback;
- `B = 8792801beeeccbf0673db137cae83e6663d21fba` must be an ancestor of `H`; **and**
- **every commit in `git rev-list H ^B` must be a descendant of `B`**, which excludes pre-freeze side
  history rather than merely certifying the final head;
- history recovery is performed by the guard itself for `B`, for `H` **and for every enumerated
  commit**, and a failed recovery **fails** the check rather than skipping it.

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** The claim is scoped to the repository record. The single permitted exception to the
"no execution object before the freeze" clause — the analysis inside the control-plane blob itself:
the quotations, the three witnesses with their equations, the expected relations — was the only
A6-specific material in the tree before this round, and every witness used here is one of those
three, unchanged.

## Definition budget: **SEVEN of the nine frozen slots fire**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 | `siteAct` | **fired** |
| 2 | `PreservesPointwise` | **fired** |
| 3 | `A6Inv` | **fired** |
| 4 | `A6Glob` | **fired** |
| 5 | `linkF` | **fired** |
| 6 | `gaugeLink` | **fired** |
| 7 | `A6Cov` | **fired** |
| 8 (conditional) | a `Rule`/`Substratum` packaging of `linkF` | **unused** |
| 9 (conditional) | a constant-coupling abbreviation | **unused** |

Slot 8 did not fire: every target is stated on `linkF` directly or on a bare `F`, and `D2` reads the
predicates on `(waveSubstratum d L q α).R.F` with no new definition, so no `Rule` or `Substratum`
packaging was needed. Slot 9 did not fire: `D4` is stated readably as `linkF N (fun _ _ => M₀)`.
**No tenth definition was introduced**: no predicate for `A6-sd`, no connectivity predicate, and no
phase-space form of any reading as a separate definition — the phase-space form is the theorem
`leap_siteAct` about `siteAct` and `leapEquiv`. And no witness, carrier, transformation,
configuration or coupling is a top-level definition: each is a bound variable pinned by an equation
in the statement that needs it. `Substratum`, `Rule`, `leapEquiv` and `waveSubstratum` are consumed
unmodified, and no field is added to `Substratum`.

**One notational point, recorded.** In the pinned Mathlib, `AddAut V` carries an additive group
structure, so the freeze's `(g j)⁻¹` is written in `gaugeLink` as the inverse equivalence
`(g j).symm` — the same object — so that no convention about the group structure on `AddAut V` is
used; the identity transformation is written `AddEquiv.refl` for the same reason.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked. Sixteen named results, **no `sorry`, no `axiom`, no
`native_decide`**, each with its own `#print axioms` line and none printing anything outside
`[propext, Classical.choice, Quot.sound]`; four print a strict subset of the three, which is
recorded as printed. **No type-P item is in this table**: `D1` and `D2-iii` are prose
determinations and are listed nowhere below.

| Result | Axioms |
| --- | --- |
| `a6glob_of_a6inv` | `[Quot.sound]` |
| `leap_siteAct` | `[propext, Classical.choice, Quot.sound]` |
| `a6cov_all` | `[propext, Quot.sound]` |
| `d3b_witness` | `[propext, Classical.choice, Quot.sound]` |
| `d3b_not_a6inv` | `[propext, Classical.choice, Quot.sound]` |
| `d4a_single_edge` | `[propext, Classical.choice, Quot.sound]` |
| `d4b_edge_rigidity` | `[propext, Classical.choice, Quot.sound]` |
| `d4b_not_a6inv_of_nonconstant` | `[propext, Classical.choice, Quot.sound]` |
| `a6glob_constLink` | `[propext, Classical.choice, Quot.sound]` |
| `d4b_symmetric_point` | `[propext, Classical.choice, Quot.sound]` |
| `addAut_nontrivial_of_ne_neg` | `[propext, Quot.sound]` |
| `addAut_zmod_smul` | `[propext, Quot.sound]` |
| `d4b_mu_id` | `[propext, Classical.choice, Quot.sound]` |
| `d2i_wave_witness` | `[propext, Classical.choice, Quot.sound]` |
| `d2i_wave_not_a6inv` | `[propext, Classical.choice, Quot.sound]` |
| `d2ii_wave_a6glob` | `[propext, Classical.choice, Quot.sound]` |

## What this round does not do

- **It adopts no reading**, and calls no reading "the" A6.
- **It proves or refutes A6 for nothing physical.** No sentence here begins "the substratum
  satisfies A6" or "A6 is refuted", and neither is a possible outcome of this round.
- **It formalizes neither `A6-sd`, `𝒢_sub`, the complex lift, the cubic-group action on `K`, nor
  any connectivity notion.** No lift to `ℂ`, no unitary group, no condensate `Σ`, no new field on
  `Substratum`.
- **It touches neither the Standard-Model derivation chain nor H-link, H-cust or H-Bell**, says
  nothing about Track B, `P0` or hydrodynamics, and does not decide the A4/A6 overlap.
- **It edits no manuscript.** `papers/` and `book/` are untouched; the three unsettled points above
  are listed for an owner call, not repaired.
- **It changes no merged label.** **The `ROADMAP` row `P1 — A6` keeps its `GAP` label**, its two
  attached qualifications about A3 and A4, and its section; the propagation appends a paragraph
  and links, and the label changes only by owner decision. The manuscript-axiom audit's finding
  about the bare operational carrier is untouched.
- **It revises nothing merged.** `Substratum`, `A1`–`A5`, `A4Exact`, `A3Family`, the four
  `Substratum` theorems, `waveF`, `waveRule`, `waveSubstratum`, `nbrs`, `dir`, the five
  `waveSubstratum_A*` theorems, `Rule` and `leapEquiv` are cited and consumed unmodified; the
  interface audit's Q1 verdict table and its A6 row, and the manuscript-axiom audit's gap verdict
  for A6 on the operational carrier and its scope repair, stand as they are.
