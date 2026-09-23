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
`padData_rooted`, `ancBorn`, `ancPow`, `padData_bornPow`, `sum_ancPow`, and their one-step
ingredients `padData_born` and `sum_ancBorn` (`OperationalSourcing.lean`);
`IsRowStochastic`, `PDivisible`, `PIndivisibleWithin` (`CausalReadback.lean`); the orientation bridge
of `TransposeBridge.lean`.

**This round introduces exactly eight definitions, each fixed here in the form it will take**: the
four immediately below, `Admissible` in the subsection after them, `NamedRuleInadmissible` with
target C1, and the two competing propositions frozen with target C4.

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

**The negative of C1's named-rule admissibility subtarget is frozen too, and `CU3` requires it.**
All three statements above are positive, so their failing to close proves nothing about the
criterion — exactly the proof-search-versus-negation gap that C2's "not established" status exists
to respect. Criterion failure is therefore its own frozen target, covering the **first two**
statements: `candidateOf_isRowStochastic` has no frozen negative, and its non-closure is `CU4`.

```lean
/-- CRITERION FAILURE.  Some representation meeting C1's hypotheses carries a named rule that the
frozen `Admissible` does not admit. -/
def NamedRuleInadmissible : Prop :=
  ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (_ : Nonempty V) (Q : QfbData V),
    Q.IsLaw ∧ Q.PositiveRootMass ∧ (∀ k, ∃ b, Q.read b = k)
    ∧ (¬ Admissible Q (initWeight Q) ∨ ¬ Admissible Q (uniformWeight Q))

theorem named_rule_inadmissible : NamedRuleInadmissible    -- the CU3 side
```

`CU3` is claimed **only** when that theorem is proved. C1 failing to close without it is `CU4`, and
so is any non-closure of `candidateOf_isRowStochastic`, whose negative is not frozen at all.

**C2 — the decisive question: must the two rules agree?** Exhibit a lawful representation on which
they differ:

```lean
theorem candidate_rules_disagree :
    ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (Q : QfbData V) (n : ℕ),
      Q.IsLaw ∧ Q.PositiveRootMass
      ∧ candidateOf Q (initWeight Q) n ≠ candidateOf Q (uniformWeight Q) n
```

Only the existential is frozen, so C2 either **closes** or is **not established**; failing to find
its witness is never reported as agreement of the named rules, and it is what separates `CU1a` from
`CU1b`.

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
is the real theorem: the ancilla marginalizes away, so the uniform rule is padding-invariant despite
`padData` multiplying every fibre by `Anc`.

**The merged route it consumes, named exactly, since the statement is at general `n`.** The
factorization used is `padData_bornPow`, which gives
`(padData Q Anc W w).bornPow t (b, x) (b', x') = Q.bornPow t b b' * ancPow W t x x'` at **every**
horizon, and the normalization used is `sum_ancPow`, which gives `∑ x', ancPow W t x x' = 1` at
every step. The one-step `padData_born` and `sum_ancBorn` are the ingredients those two are proved
from, not the theorems C3 applies: `sum_ancBorn` is a row-sum statement about `ancBorn` alone and
does not reach general `n`.

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
theorem admissible_nonUnique : AdmissibleNonUnique      -- the CU1a / CU1b side
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

If `NamedRuleInadmissible` is proved, that is `CU3`, and neither C4 theorem is claimed. Note the
scope carefully: what is shown in that case is that *this* criterion fails on a named rule, and the
round has no means to say more, since Control 4 forbids reshaping `Admissible` after freeze and
nothing here quantifies over alternative criteria.

## Admissible outcomes

Because C4 quantifies over **arbitrary** admissible weights while C2 asks about the two **named**
rules, non-uniqueness has two genuinely different strengths, and they are separated here. The
enumeration below is exhaustive over the possible states of C1, C2 and C4, and its cases are
mutually exclusive.

**CU1a — the named rules are underdetermined.** C1 and C2 close: two independently admissible
extraction rules differ on one lawful representation, with the representation held fixed. C4 closes
on the non-unique side as well, and necessarily so: C1 makes both named rules admissible, so the C2
witness instantiates `AdmissibleNonUnique` directly. A candidate-selection principle is then
required *before* "OI forces this interference discrepancy" is a well-defined family-level question.

**CU1b — the admissibility interface is underdetermined, the named pair unresolved.** C1 closes and
`AdmissibleNonUnique` closes on **some** admissible pair, while C2 is **not established** on
`initWeight` and `uniformWeight`. This is a real possibility rather than a bookkeeping case: the C2
and C4 targets were deliberately separated so that the general existential can close on a pair the
named rules do not witness.

It is strictly weaker than `CU1a` and carries a strictly weaker licence. What is shown is that the
frozen admissibility conditions do not force a unique candidate; whether the two *natural* rules
differ stays open, and is reported as open unless separately proved.

**CU2 — the internal candidate is unique at this interface.** `AdmissibleAgree` closes. C2's witness
then does not exist as a **consequence of that theorem** — C1 makes both named rules admissible, so
agreement forces their candidates to coincide — rather than because a search for it failed.

What that buys is stated at its own scope, since this round forbids identifying `candidateOf` with
any external object. Uniqueness is of **our** `candidateOf` at **this** interface. It makes the
*this-side* discrepancy a well-defined function of the representation, so a next round may study
that discrepancy — or may instead discharge the mapping obligation, proving that our representation
instantiates the external construction. **`CU2` does not make the external interference question
well-posed**, and the mapping is a separate obligation that no theorem in this round addresses.
§3.6's accessible-window countermodel remains the first obstacle for the this-side discrepancy
round.

**CU3 — the frozen admissibility criterion does not admit both named rules.** `NamedRuleInadmissible`
is **proved**: some representation meeting C1's hypotheses carries a named rule the frozen
`Admissible` does not admit, so the two rules are not being compared as instances of one common
specification and C4 is not asked.

`CU3` is reached only that way. C1 merely failing to close is `CU4`, never `CU3`: the C1 statements
are positive, so their non-closure is a fact about the search and not about the criterion, and the
round claims criterion failure only where it has proved it.

The scope of this outcome is **exactly** that, and the wording is frozen because the overclaim is
easy to reach for. `CU3` establishes that *this* criterion, at *this* interface, does not do the job
asked of it. It does **not** establish that no neutral criterion exists, nor that every neutral
strengthening fails: the round does not formalize "neutral", quantifies over no space of candidate
criteria, and is forbidden by Control 4 from reshaping `Admissible` to try others. The general
question of whether some admissibility criterion admits both rules is therefore **left open** by
`CU3` and must be reported as open. Reaching it would need a target that quantifies over criteria,
and no such target is frozen here.

**CU4 — unresolved.** Either C1 does not close and `NamedRuleInadmissible` is not proved either, or
C1 closes and neither C4 side closes. In the second case C2 is not established either, since a C2
witness together with C1 would prove `AdmissibleNonUnique`. Recorded as open, with what is missing.
A failed search is never reported as a uniqueness result, and never as a criterion-failure result.

**The five cases are exhaustive.** If `NamedRuleInadmissible` is proved, the outcome is `CU3`.
Otherwise, if C1 does not close, the outcome is `CU4`. If C1 closes, exactly one of three things is
true of C4 — `AdmissibleNonUnique` proved, `AdmissibleAgree` proved, or neither — giving
`CU1a`/`CU1b` (split by whether C2 closes), `CU2`, and `CU4` respectively. No further split is
needed on C2: it cannot close under `CU2` or `CU4`, for the reasons given in each.

**Every decisive outcome is earned by a proof, and none by a failed search.** `CU1a` needs C2;
`CU1b` needs `AdmissibleNonUnique`; `CU2` needs `AdmissibleAgree`; `CU3` needs
`NamedRuleInadmissible`. `CU4` is not a decisive outcome: it is the one label that records
unresolved non-closure, and it records exactly that.

**C2 has no frozen complement, and this is deliberate.** C4 freezes both sides because its outcome
label turns on which one is true, so `CU2` must be earned by proof. C2 freezes only the existential,
so **failure to close C2 is reported as "not established", never as agreement of the named rules**.
Distinguishing `CU1a` from `CU1b` therefore requires proving C2, not failing to refute it. A
named-rule agreement theorem could be frozen to make C2 two-sided as well; none is frozen in this
round, and no claim that the named rules agree is available without one.

## How a CU1a, CU1b or CU3 result must be described

This constraint is frozen because it is the easiest thing in the round to get wrong. **The three
outcomes carry different licences, in strictly decreasing strength, and they are stated separately
so that the weaker two cannot borrow the strongest one's sentence.**

### If the outcome is `CU1a`

`CU1a` proves that the two **named** rules — each a natural extraction from the representation —
differ on one fixed lawful representation, so the bridge demonstrably fails to pick between them.

**Permitted:** *the merged OI → `QfbData` bridge does not select the candidate at this interface*,
together with a statement of what a candidate-selection principle would have to do, given as a
**requirement** and not proposed as a condition.

### If the outcome is `CU1b`

`CU1b` proves that **some** admissible pair differs, on weights that need not be natural extraction
rules, and leaves the named pair unresolved.

**Permitted:** *the frozen admissibility conditions do not force a unique candidate*, with the
question of whether `initWeight` and `uniformWeight` differ reported as **open**.

**Not permitted under `CU1b`:** the `CU1a` sentence about the bridge; a candidate-selection
principle stated as required; any suggestion that the two natural rules have been shown to differ.
`CU1b` is a result about the admissibility interface, not about the named rules — and not a result
that the named rules agree either, since C2 has no frozen complement.

### If the outcome is `CU3`

`CU3` proves only that the frozen `Admissible` fails to admit both named rules, and leaves open
whether some other criterion admits both. None of the statements above follows from it.

**Permitted:** *the frozen admissibility criterion does not compare the two named rules*, with the
question of whether the bridge selects a candidate under some other admissibility criterion
reported as **open**.

**Not permitted under `CU3`:** that the merged bridge does not select the candidate; that the
admissibility conditions fail to force a unique candidate; that a candidate-selection principle is
required; any requirement statement of the `CU1a` kind. `CU3` is a result about a criterion, not
about the bridge and not about uniqueness under that criterion.

### Under any outcome

**Not permitted:** *Barandes's framework requires an additional physical principle.*

Act 1 established that the external diagnostic discussion uses a **particular** candidate, whereas
our `PDivisible` quantifies existentially over all stochastic candidates. That external construction
may well supply the selection canonically — from the relative unitary of its own dilation. If it
does, the eventual task is to show that **our** representation instantiates **his** construction,
not to add a principle to his framework. Nothing in this round licenses a claim about what his
construction does or does not fix; act 1's determinations are the only citation for that, and this
round does not extend them.

## Prediction recorded before proving

**`CU1a` is predicted, at roughly two-to-one against `CU2`, with `CU1b` the fallback if the named
pair proves harder to separate than the general existential, and `CU3` unlikely.**

The ground is that `initWeight` reads `Q.init` and `uniformWeight` reads only the fibre's
cardinality, and nothing in `IsLaw` or `PositiveRootMass` ties those together: a lawful `Q` may
place unequal initial weight on basis points of one fibre whose `bornPow` rows differ. That is a
reason to expect a witness, not a construction of one, and C2 is a witness target that either closes
or does not.

Note that the ground concerns the **named** rules specifically, which is why the prediction is
recorded on `CU1a` rather than on the `CU1` family: `CU1b` needs only some admissible pair, so it is
strictly easier to reach and a prediction covering both would be weaker than the ground supports.

**`CU3` is recorded as unlikely, and the reason is stated so the prediction can be scored.** The
neutrality argued for `Admissible` above is a *reading* of its three clauses rather than a theorem,
which is why the outcome exists at all. But `PositiveRootMass` gives `0 < rootMass k`, and
`rootMass k` is the sum of `init` over the fibre, so every fibre is nonempty — which is exactly what
`uniformWeight` needs to normalize, and positivity of the same quantity is what `initWeight` needs.
Nonnegativity then comes from `IsLaw`'s `∀ b, 0 ≤ init b` on one side and from `1 / card` on the
other. So both named rules look admissible under hypotheses the targets already carry, and
`NamedRuleInadmissible` looks unprovable.

That is a reading of the merged statements, **not** a proof, and it is recorded here rather than
acted on: the target stays frozen, because an outcome should be reachable and earned even when it is
not expected. If C1 nonetheless fails to close and no counterexample is proved, the outcome is
`CU4`.

**No prediction is recorded on C3**, which is expected to close as stated; if it does not, the
scoping pass's Finding 2 was wrong and that is reported as such.

## Mandatory controls

1. **No claim about any Barandes predicate or construction**, beyond citing act 1's determinations.
   `BD3`, `BR3` and `RT1` are neither reopened, softened nor re-derived.
2. **No primary source is consulted.**
3. **The scoping pass is not cited as settled.** Its Findings 2 and 3 are provisional by its own
   terms; C3 is where Finding 2 becomes a theorem, and Finding 3 is not used as a premise anywhere.
4. **Nothing merged is restated, and nothing frozen is reshaped.** All **eight** definitions this
   round introduces are frozen above in the form given — `FibreWeight`, `candidateOf`,
   `initWeight`, `uniformWeight`, `Admissible`, `NamedRuleInadmissible`, and the two C4
   propositions `AdmissibleNonUnique` and `AdmissibleAgree`. The outcome-bearing propositions are
   frozen no less than the constructions: the point of stating them is that none may be reshaped
   after the targets resolve. If a target is unprovable against them, the outcome is `CU4` and the
   definitions stand.
5. **Kernel discipline.** No `sorry`, no custom `axiom`, no `native_decide`; a `#print axioms` line
   on every named result, printing only `[propext, Classical.choice, Quot.sound]`.
6. **§3.6 is not reopened**, and no claim is made about whether OI forces indivisibility.
7. **Arc D's quarantine is used, not undermined.** C3 consumes `padData_rooted`, `padData_bornPow`
   and `sum_ancPow`, the general-horizon statements, rather than their one-step ingredients;
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
3. the outcome label — one of `CU1a`, `CU1b`, `CU2`, `CU3`, `CU4` — the prediction, and whether it
   held;
4. if `CU1a`: that the merged bridge does not select the candidate at this interface, and what a
   candidate-selection principle would have to do, stated as a **requirement** and not proposed as
   a condition, with no claim about the external framework;
4b. if `CU1b`: **only** that the frozen admissibility conditions do not force a unique candidate,
   with the named pair reported as **open** — not as agreeing. No bridge statement and no
   requirement statement is permitted from `CU1b`;
4c. if `CU3`: **only** that the frozen admissibility criterion does not compare the two named
   rules, with whether the bridge selects a candidate under some other criterion reported as
   **open**. No requirement statement and no claim about the bridge is permitted from `CU3`;
5. if `CU2`: that **our** `candidateOf` is unique at **this** interface, and that this makes the
   *this-side* discrepancy well defined — **not** that the external interference question is
   well-posed, which needs the mapping obligation discharged separately; then what a next round
   must prove, whether that is the this-side discrepancy round with §3.6 named as its first
   obstacle, or the mapping itself;
6. whether C3 confirmed or refuted the scoping pass's Finding 2;
7. what remains open;
8. explicitly, that nothing here claims OI forces quantum structure, nothing identifies a this-side
   object with an external one, and nothing is a sourcing claim.
