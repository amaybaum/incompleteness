# Track B act 3 — candidate selection and uniqueness: preregistration

Base: `main` at `0c5e7798a46af0490734bc4f6a15862966407744` (post-PR #563, the scoping pass merged).

Presupposes act 1 (`BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md`, PR #560), act 2
(`BARANDES-TRANSPOSE-BRIDGE-RESULT.md`, PR #562), and the scoping pass
`BARANDES-REPRESENTATION-FREEDOM-SCOPING.md`, **merged by PR #563 and used only as scoping
motivation, not as a proved premise**. Its Findings 2 and 3 are provisional by its own terms; this
round may not cite them as settled, and C3 is where Finding 2 becomes a theorem. Ordering is carried
in **ancestry, not prose**: every commit of this branch descends from the merge that brought the
scoping pass to `main`.

A **proof round** over this programme's own objects. It consumes no primary source.

Status: **draft; nothing here is frozen until the reviewer approves an exact commit and blob, and no
execution begins before the freeze is merged.**

## Why this round, and why not the one it replaces

The question Track B is heading toward is whether OI forces the interference discrepancy of
arXiv:2302.10778v3 §3.5 to be nonzero. Reaching it requires a chain:

    OI stochastic family  →  representation  →  candidate intermediate  →  discrepancy

Arc D round 1 settled that the **first** arrow does not determine operator content: padding by an
arbitrary finite ancilla unitary preserves the represented family exactly. The scoping pass found
reason to think the **second** arrow may not determine the candidate either — and that if so, the
missing ingredient sits earlier than any interference round would look.

A previous draft asked whether the discrepancy is invariant under representation freedom. It is
withdrawn before freeze because the scoping pass found that padding — the only parameterized
same-family freedom the corpus proves — appears inert at the candidate level for both natural
extraction rules. That round's `RU1` could therefore have failed for want of a construction rather
than for want of truth, and a null of that shape is uninterpretable.

**This round asks the prior question instead, and it is designed so that every outcome is
reachable.** It does not merely observe that two extraction rules exist; it asks whether they
**must agree**.

## What is fixed before proving

Merged and used, not redefined: `QfbData`, `IsLaw`, `PositiveRootMass`, `born`, `bornPow`,
`rootMass`, `jointMass`, `rooted`, `QStar` (`QuantumRepresentation.lean`); `padData`,
`padData_rooted`, `padData_born`, `ancPow`, `sum_ancBorn` (`OperationalSourcing.lean`);
`IsRowStochastic`, `PDivisible`, `PIndivisibleWithin` (`CausalReadback.lean`); the orientation bridge
of `TransposeBridge.lean`.

**This round introduces exactly seven definitions, each fixed here in the form it will take**: the
four immediately below, `Admissible` in the subsection after them, and the two competing
propositions frozen with target C4.

```lean
/-- Weight assigned to each basis point of the visible fibre over `k`, from which a visible
candidate propagator is marginalized. -/
def FibreWeight (Q : QfbData V) : Type := V → Q.Bas → ℝ

/-- The visible candidate propagator induced by a representation and a fibre weighting: push
`bornPow n` down to the visible carrier by weighting each source fibre and summing each target
fibre. -/
noncomputable def candidateOf (Q : QfbData V) (μ : FibreWeight Q) (n : ℕ) : Matrix V V ℝ :=
  fun k j => ∑ b ∈ univ.filter (fun b => Q.read b = k),
               ∑ b' ∈ univ.filter (fun b' => Q.read b' = j), μ k b * Q.bornPow n b b'

/-- The init-weighted rule: weight the fibre by the normalized initial law. -/
noncomputable def initWeight (Q : QfbData V) : FibreWeight Q :=
  fun k b => if Q.read b = k then Q.init b / Q.rootMass k else 0

/-- The uniform-on-fibre rule: weight every basis point over `k` equally. -/
noncomputable def uniformWeight (Q : QfbData V) : FibreWeight Q :=
  fun k b => if Q.read b = k
    then 1 / (univ.filter (fun c => Q.read c = k)).card else 0
```

Control 4 forbids reshaping any of these after seeing what proves.

**Admissibility, stated before the targets rather than after.** A `FibreWeight` is *admissible* when
it is supported on the fibre it names, nonnegative, and normalized there:

```lean
def Admissible (Q : QfbData V) (μ : FibreWeight Q) : Prop :=
  (∀ k b, Q.read b ≠ k → μ k b = 0) ∧ (∀ k b, 0 ≤ μ k b) ∧ (∀ k, ∑ b, μ k b = 1)
```

These three conditions are **not** claimed to be logically necessary for the output to be
row-stochastic. That would be false: a signed weight on a fibre whose visible rows happen to
coincide still marginalizes to a stochastic row. What the three say together is that `μ` **is a
probability distribution on the source fibre** — support, nonnegativity, normalization, one clause
each — which is what "weight the fibre and marginalize" means. Relative to that reading each clause
is forced; absolutely, they are sufficient for C1, which is what the round needs of them.

Support and normalization alone do **not** suffice, and the gap is not cosmetic. Write
`R_b (j) = ∑_{b' ∈ fibre j} bornPow n b b'` for the visible row of a basis point. Then
`candidateOf Q μ n k j = ∑_{b ∈ fibre k} μ k b * R_b (j)`, so the row *sums* come out at one from
support and normalization by themselves — `∑_j ∑_{b} μ k b * R_b (j) = ∑_{b ∈ fibre k} μ k b = 1` —
while each *entry* is only an **affine**, not convex, combination of the fibre's visible rows. A
signed weight `(2, -1)` on two basis points of one fibre whose visible rows differ produces a row
such as `[2, -1]`: normalized, and negative. `candidateOf_isRowStochastic` is false without the
sign condition.

Nonnegativity is neutral in exactly the sense the other two conditions are: **none of the three
mentions `init`, `U`, or the fibre's cardinality**, so none privileges `initWeight` or
`uniformWeight`. Whether that neutrality survives contact with the proofs is target C4.

## The four targets

**C1 — both rules are admissible, and admissible rules give candidates.**

```lean
theorem initWeight_admissible (Q : QfbData V) (hQ : Q.IsLaw) (hP : Q.PositiveRootMass) :
    Admissible Q (initWeight Q)

theorem uniformWeight_admissible (Q : QfbData V) [Nonempty V] (h : ∀ k, ∃ b, Q.read b = k) :
    Admissible Q (uniformWeight Q)

theorem candidateOf_isRowStochastic (Q : QfbData V) (hQ : Q.IsLaw) (μ : FibreWeight Q)
    (hμ : Admissible Q μ) (n : ℕ) : IsRowStochastic (candidateOf Q μ n)
```

Without C1 the later targets compare objects that are not candidates.

**C2 — the decisive question: must the two rules agree?** Exhibit a lawful representation on which
they differ:

```lean
theorem candidate_rules_disagree :
    ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (Q : QfbData V) (n : ℕ),
      Q.IsLaw ∧ Q.PositiveRootMass
      ∧ candidateOf Q (initWeight Q) n ≠ candidateOf Q (uniformWeight Q) n
```

This is the target that makes underdetermination a theorem rather than an observation, and it holds
the **representation fixed**: no appeal to representation freedom is made or needed.

A witness needs a `Q` whose visible fibre has at least two basis points carrying different `init`
weight and different `bornPow` rows, **and a visible carrier with at least two points**. The second
requirement is not a matter of convenience: on `V = Fin 1` the single entry of `candidateOf Q μ n`
*is* the row sum, hence `1` for every admissible `μ` whatever `Bas` is, so the two rules cannot
differ there. The first plausible shape is `V = Fin 2` with one fibre of size two.

**C3 — the subsidiary padding theorems, at exact scope.** The mechanism the scoping pass uncovered,
proved rather than asserted:

```lean
theorem candidateOf_initWeight_eq_rooted (Q : QfbData V) (hQ : Q.IsLaw) (hP : Q.PositiveRootMass)
    (n : ℕ) (k j : V) : candidateOf Q (initWeight Q) n k j = Q.rooted n k j

theorem candidateOf_uniformWeight_padData_eq (Q : QfbData V) (Anc : Type) [Fintype Anc]
    [DecidableEq Anc] [Nonempty Anc] (W : Matrix Anc Anc ℂ) (hW : W ∈ Matrix.unitaryGroup Anc ℂ)
    (w : Anc → ℝ) (n : ℕ) (k j : V) :
    candidateOf (padData Q Anc W w) (uniformWeight _) n k j
      = candidateOf Q (uniformWeight Q) n k j
```

The first is essentially definitional and is stated so that the second is seen not to be. The second
is the real theorem: the ancilla marginalizes away by `sum_ancBorn`, so the uniform rule is padding-
invariant despite `padData` multiplying every fibre by `Anc`.

**C4 — do the admissibility conditions force uniqueness?** **Both competing propositions are frozen
here, exactly.** Which one is true is not predicted; which one the round proves is not left to be
chosen after C2 resolves.

```lean
/-- NON-UNIQUENESS.  Some lawful representation carries two admissible weights whose induced
visible candidates differ at some elapsed time. -/
def AdmissibleNonUnique : Prop :=
  ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (Q : QfbData V) (μ ν : FibreWeight Q) (n : ℕ),
    Q.IsLaw ∧ Q.PositiveRootMass ∧ Admissible Q μ ∧ Admissible Q ν
    ∧ candidateOf Q μ n ≠ candidateOf Q ν n

/-- UNIVERSAL AGREEMENT.  On every lawful representation, any two admissible weights induce the
same visible candidate at every elapsed time. -/
def AdmissibleAgree : Prop :=
  ∀ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (Q : QfbData V) (μ ν : FibreWeight Q) (n : ℕ),
    Q.IsLaw → Q.PositiveRootMass → Admissible Q μ → Admissible Q ν →
    candidateOf Q μ n = candidateOf Q ν n
```

These are exact negations of one another over the stated domain, so exactly one is true, and the
round's task is to prove whichever it is:

```lean
theorem admissible_nonUnique : AdmissibleNonUnique      -- the CU1 side
theorem admissible_agree : AdmissibleAgree              -- the CU2 side
```

The execution contract on these two, stated conditionally so that it does not collide with `CU4`:
**if C4 closes, exactly one of those two theorem statements appears in the executed module, and the
frozen text above is what it must say; under `CU4`, neither appears.** Both appearing is impossible
and neither is reshaped in either case. `CU2` therefore requires a proof of `AdmissibleAgree` as
sharp as C2's existential witness; it is never reached by failing to find a counterexample, and a
failed search for a witness is `CU4`, not `CU2`.

`AdmissibleNonUnique` is deliberately stated over **arbitrary** admissible weights rather than over
`initWeight` and `uniformWeight` specifically. C2 is the concrete instance at the two named rules;
C4 is the general question, and the two can come apart in one direction only: C2 could fail on the
named pair while C4 succeeds on some other admissible pair. The reverse cannot happen, because C1
makes both named rules admissible and a C2 witness therefore instantiates C4's existential
directly.

If C1 fails against `Admissible` **as frozen above** for one of the two named rules, that is `CU3`,
and neither C4 theorem is claimed. Note the scope carefully: what fails in that case is *this*
criterion, and the round has no means to say more, since Control 4 forbids reshaping `Admissible`
after freeze and nothing here quantifies over alternative criteria.

## Admissible outcomes

**CU1 — underdetermined at the candidate layer.** C1 and C2 close: two independently admissible
extraction rules differ on one lawful representation, with the representation held fixed. A
candidate-selection principle is then required *before* "OI forces this interference discrepancy"
is a well-defined family-level question.

**CU2 — unique at the tested interface.** C2's witness does not exist because the frozen
admissibility conditions force the rules to coincide, and that coincidence is **proved**, not merely
unwitnessed. The interference question becomes well-posed and the next round asks whether OI forces
a nonzero discrepancy, with §3.6's accessible-window countermodel as its first obstacle.

**CU3 — the frozen admissibility criterion does not admit both named rules.** C1 fails against
`Admissible` as frozen, for `initWeight` or for `uniformWeight`, so the two rules are not being
compared as instances of one common specification and C4 is not asked.

The scope of this outcome is **exactly** that, and the wording is frozen because the overclaim is
easy to reach for. `CU3` establishes that *this* criterion, at *this* interface, does not do the job
asked of it. It does **not** establish that no neutral criterion exists, nor that every neutral
strengthening fails: the round does not formalize "neutral", quantifies over no space of candidate
criteria, and is forbidden by Control 4 from reshaping `Admissible` to try others. The general
question of whether some admissibility criterion admits both rules is therefore **left open** by
`CU3` and must be reported as open. Reaching it would need a target that quantifies over criteria,
and no such target is frozen here.

**CU4 — unresolved.** Neither non-uniqueness nor uniqueness closes. Recorded as open, with what is
missing. A failed search is never reported as a uniqueness result.

## How a CU1 or CU3 result must be described

This constraint is frozen because it is the easiest thing in the round to get wrong.

**Permitted:** *the merged OI → `QfbData` bridge does not select the candidate.*

**Not permitted:** *Barandes's framework requires an additional physical principle.*

Act 1 established that the external diagnostic discussion uses a **particular** candidate, whereas
our `PDivisible` quantifies existentially over all stochastic candidates. That external construction
may well supply the selection canonically — from the relative unitary of its own dilation. If it
does, the eventual task is to show that **our** representation instantiates **his** construction,
not to add a principle to his framework. Nothing in this round licenses a claim about what his
construction does or does not fix; act 1's determinations are the only citation for that, and this
round does not extend them.

## Prediction recorded before proving

**`CU1` is predicted, at roughly two-to-one against `CU2`, with `CU3` materially live.**

The ground is that `initWeight` reads `Q.init` and `uniformWeight` reads only the fibre's
cardinality, and nothing in `IsLaw` or `PositiveRootMass` ties those together: a lawful `Q` may
place unequal initial weight on basis points of one fibre whose `bornPow` rows differ. That is a
reason to expect a witness, not a construction of one, and C2 is a witness target that either closes
or does not.

`CU3` is live because the neutrality argued for `Admissible` above is a *reading* of its three
clauses, not a theorem: C1 is where the frozen criterion has to actually admit both named rules, and
it can fail there. If it does, the scope constraint stated with `CU3` applies without softening.

**No prediction is recorded on C3**, which is expected to close as stated; if it does not, the
scoping pass's Finding 2 was wrong and that is reported as such.

## Mandatory controls

1. **No claim about any Barandes predicate or construction**, beyond citing act 1's determinations.
   `BD3`, `BR3` and `RT1` are neither reopened, softened nor re-derived.
2. **No primary source is consulted.**
3. **The scoping pass is not cited as settled.** Its Findings 2 and 3 are provisional by its own
   terms; C3 is where Finding 2 becomes a theorem, and Finding 3 is not used as a premise anywhere.
4. **Nothing merged is restated, and nothing frozen is reshaped.** All **seven** definitions this
   round introduces are frozen above in the form given — `FibreWeight`, `candidateOf`,
   `initWeight`, `uniformWeight`, `Admissible`, and the two C4 propositions `AdmissibleNonUnique`
   and `AdmissibleAgree`. The last two are frozen no less than the first five: the point of stating
   both is that neither may be reshaped after C2 resolves. If a target is unprovable against them,
   the outcome is `CU3` or `CU4` and the definitions stand.
5. **Kernel discipline.** No `sorry`, no custom `axiom`, no `native_decide`; a `#print axioms` line
   on every named result, printing only `[propext, Classical.choice, Quot.sound]`.
6. **§3.6 is not reopened**, and no claim is made about whether OI forces indivisibility.
7. **Arc D's quarantine is used, not undermined.** C3 consumes `padData_rooted` and `sum_ancBorn`;
   it does not re-prove them, and representational presence grounds nothing.
8. **No manuscript edit**, whatever is found.
9. **No sourcing inference.** A statement about weightings and marginals sources nothing.
10. **Track separation** both ways, per Amendment 2. **No fifth condition.** No deferred Arc D
    resource adjudicated.

## Non-doings

Do not: claim OI forces or fails to force quantum structure; attribute a gap to the external
framework; identify `candidateOf` with any external object; reopen §3.6, `BD3`, `BR3` or `RT1`;
consult a primary source; attempt to construct a non-padding representation freedom; begin the
tuple-instantiation lemma, Arc D round 2, or Arc E; edit manuscripts.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any Lean is written. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen, committed before the work they affect.
- **Two PRs, in order.** Control-plane PR carrying **this file alone**, reviewed, frozen and merged
  before any execution; then exactly one execution/result PR from the resulting `main`. The scoping
  note is already merged separately, as history without freeze semantics, so that a non-adjudicative
  record and an immutable proof contract never share a control-plane event.
- Final exact-head review after module, guard, result note and registry updates are complete.
- No merge without an explicit owner direction after exact-head review.

## Allowed final report

1. each of the four targets, with its outcome and the named results carrying it;
2. the axiom line for every named result, and the count;
3. the outcome label `CU1`–`CU4`, the prediction, and whether it held;
4. if `CU1` or `CU3`: what a candidate-selection principle would have to do, stated as a
   **requirement** and not proposed as a condition, and phrased per the constraint above — the
   merged bridge does not select the candidate, with no claim about the external framework; and if
   `CU3`, that what failed is the frozen criterion at this interface, with the existence of some
   criterion admitting both rules reported as **open**;
5. if `CU2`: what the next round must prove, with §3.6 named as its first obstacle;
6. whether C3 confirmed or refuted the scoping pass's Finding 2;
7. what remains open;
8. explicitly, that nothing here claims OI forces quantum structure, nothing identifies a this-side
   object with an external one, and nothing is a sourcing claim.
