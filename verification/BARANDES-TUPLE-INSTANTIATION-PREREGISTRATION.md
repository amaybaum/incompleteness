# Track B act 6 — tuple instantiation and the Source-A branch test: preregistration

Base: `main` at `e6880f2c6562ead502b1234ee767c0e654aa67d7` (post-PR #569, act 5 closed at `SA2`).

Presupposes act 1 (`BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md`, PR #560), act 2
(`BARANDES-TRANSPOSE-BRIDGE-RESULT.md`, PR #562), the scoping pass
(`BARANDES-REPRESENTATION-FREEDOM-SCOPING.md`, PR #563), act 3
(`BARANDES-CANDIDATE-SELECTION-RESULT.md`, PR #565), act 4
(`BARANDES-DILATION-MAPPING-RESULT.md`, PR #567) and act 5
(`BARANDES-SOURCE-A-CANDIDATE-RESULT.md`, PR #569).

**This is a kernel round. Lean is written.** Acts 4 and 5 were source-to-formal audits and forbade
it; this one requires it, and the controls below are those of a kernel round rather than an audit.

Status: **draft; nothing here is frozen until the reviewer approves an exact commit and blob, and no
execution begins before the freeze is merged.**

## Two layers, two label families, deliberately not merged into one headline

The round answers **two logically independent questions** that have become adjacent, and reports a
**pair** of outcomes, one from each family. Forcing a single label would hide exactly the
combination that is most informative.

| Layer | Question | Labels |
|---|---|---|
| **1 — tuple instantiation** | Does a merged `RootedRealization` instantiate the external stochastic-process tuple interface? | `TI1` / `TI2` / `TI3` |
| **2 — Source-A branch test** | Is every visible OI transition matrix unistochastic, in the transposed orientation Source A's eq (39) requires? | `UB1` / `UB2` / `UB3` |

**The labels are orthogonal.** All nine pairs are coherent and none is excluded a priori. In
particular `(TI1, UB2)` — our processes instantiate the tuple, but not every visible OI process lies
on Source A's direct unistochastic branch — is a fully coherent result, and would make §3.4's
dilation the next load-bearing obligation.

## Why this round is on the critical path

Act 3 (`CU1a`) proved our bridge does not select the candidate. Act 4 (`MP4`) found Source C's
construction forms no intermediate candidate at all. Act 5 (`SA2`) found Source A's construction
does form one, load-bearing for its interference formula, but computes it from a **unitary lift**
that the visible stochastic family does not fix — established **on the direct unistochastic branch
that eq (39) assumes**.

Act 5 deferred to this round the containment question, and it has a sharp first sub-question: **which
branch does OI actually land on?** Until that is settled we do not know which theorem to freeze next.
Layer 1 supplies the interface that makes the question statable in the kernel; layer 2 answers it.

## Layer 1 — tuple instantiation

### The instantiation target

Define the external stochastic-process tuple interface and **prove** that a merged
`RootedRealization V H` instantiates it, under exactly these declarations:

| Component | Declaration |
|---|---|
| `C` | `V`, the visible carrier |
| `T` | `ℕ` |
| `T₀` | `{0}` |
| `Γ(t ← 0)` | `(rootedMap R t)ᵀ` — the transposed orientation act 2 settled |
| `p` | **an arbitrary normalized declaration**, explicitly parameterized |
| `A` | the **full (maximal) function algebra on `V`**, taken canonically |

**`p` is parameterized, not supplied.** Act 1's Q8 established our datum does not carry it. The
instantiation theorem therefore quantifies over an arbitrary `p` satisfying non-negativity and
normalization, and the round **does not** pretend OI supplied one. Any statement of the form "our
datum determines `p`" is forbidden.

**`A` is taken canonically as the full function algebra on `V`**, not derived and not argued
minimal. The word "minimal" is not used of it.

### Every axiom individually

**Each axiom of the frozen interface is proved as its own named result**, with no aggregate "the
tuple axioms hold". At minimum this covers non-negativity, normalization in the transposed
orientation, and trivialization at `0`. Act 2's `rootedMap_zero` and `rootedMap_isRowStochastic` are
**consumed, not re-proved**; what is new is the interface and the instantiation.

If stating the interface surfaces an axiom act 1's Q8 did not examine, that axiom is proved or its
status recorded — Q8's ledger is inherited as a ledger of *components*, and this layer extends it to
the *interface's axioms*, which is a different question.

### The vacuity record

**Any divisibility requirement restricted to `T₀ = {0}` is vacuous**, and the round records this
explicitly: a condition quantified over conditioning times in a singleton `{0}` says nothing about
our all-time `PDivisible`, which quantifies over all intermediate times. **No outcome of this layer
is evidence for or against `PDivisible`**, and the result note says so in terms. This is recorded
because the vacuity is easy to mistake for a finding in either direction.

### Layer-1 outcomes

**`TI1` — instantiated.** Every axiom of the frozen interface is kernel-proved for a merged
`RootedRealization` under the declarations above, with **no added hypothesis** beyond them and the
ambient finiteness/decidability already carried by the merged structures.

**`TI2` — instantiated under a named added hypothesis.** As `TI1`, but some axiom needs a hypothesis
not in the list above — `Nonempty V`, a positivity side condition, or similar. The hypothesis is
**named**, and whether it is *necessary* is recorded as proved or open, never asserted.

**`TI3` — not instantiated.** Reported with a **mandatory sub-status**, and the two are never
conflated:

- ***refuted*** — a lawful `RootedRealization` is exhibited violating a named axiom;
- ***unresolved*** — the round did not settle it, with the axiom and the obstruction named.

Act 5's A1 discipline applies here one layer down: **failure to prove is not refutation**, and an
unresolved axiom is never reported as a finding about OI.

## Layer 2 — the Source-A branch test

### The branch-test target

Formalize the exact property Source A's eq (39) presupposes, **in the transposed orientation**: that
each visible `Γ(t ← 0) = (rootedMap R t)ᵀ` is **unistochastic** — that is, there exists a unitary
whose entrywise modulus-squares are its entries, per Source A (30), p. 11.

Then settle, for the OI class:

> **Universal direct unistochasticity.** For every lawful `RootedRealization R` and every `t`,
> `(rootedMap R t)ᵀ` is unistochastic.

### Layer-2 outcomes

**`UB1` — proved.** Universal direct unistochasticity holds for the OI class, kernel-proved.

**`UB2` — refuted.** A **lawful OI counterexample** is exhibited: a `RootedRealization` and a time
whose visible transition matrix is **not** unistochastic. The witness must be lawful — a genuine
`RootedRealization` with a normalized non-negative prior — either constructed directly or obtained
through the merged `pper_has_responseRealization`, which realizes any `PPer` family.

**`UB3` — unresolved.** Neither proved nor refuted, with what is missing named.

**Failure to prove `UB1` is not `UB2`.** `UB2` requires an exhibited lawful counterexample;
absent one, the answer is `UB3`. This is the same discipline act 5 froze at A1 and act 4 at `MP3`,
and it is the single most likely way this layer could be misreported.

## The control this round exists to protect: direct unistochasticity ≠ dilatability

These are **different propositions** and the round keeps them apart in both directions.

- **`UB2` does not mean Source A is inapplicable.** Source A's §3.4, p. 10 dilates a non-unitary
  `Θ(t ← 0)` to a unitary one on a larger carrier. A visible matrix that is not unistochastic may
  still be embedded that way. `UB2` therefore places OI on **act 5's unadjudicated dilated branch**
  and makes the dilation the next load-bearing obligation — it does **not** show the correspondence
  fails, and no sentence to that effect is permitted on any outcome.
- **Dilatability never proves unistochasticity.** The existence of a dilation of `Γ` is not evidence
  that `Γ` itself is unistochastic, and must never be used as such. The two carriers differ, and the
  dilated object is a different matrix.

**This round does not adjudicate dilatability at all.** It is a branch test. Whether the dilation
choice moves the induced candidate is act 5's open non-unistochastic branch and belongs to a later
round with its own freeze.

## The representation-inference rule, and the two concrete temptations

**Do not infer visible unistochasticity from the existence of some `QfbData` or Hilbert
representation** — not unless a **merged theorem** already identifies that representation's
fixed-basis modulus-square with **the same `Γ`**, for the **full class under study**. Arc D's `RD1`
is why: representational presence is a proved disqualified ground.

Two merged objects make this tempting, and neither licenses the inference:

- **`overlap_row_sum` / `overlap_col_sum`** (`CoherentLift.lean`) prove `B_{ia} = |V_{ia}|²` doubly
  stochastic — genuinely a modulus-square of a unitary, but of the **coherent-lift transport matrix
  on the shell**, not of `(rootedMap R t)ᵀ`. No merged theorem equates the two.
- **`QfbData.born`** is `‖Q.U b' b‖²` — a modulus-square of a unitary on the **basis carrier
  `Bas`**, not on `V`. The passage from basis to visible carrier runs through the fibre structure,
  and act 3's `CU1a` proved that passage does not determine a unique visible candidate.

Either would, if used, produce a `UB1` that is not earned. Any `UB1` must be proved **about
`(rootedMap R t)ᵀ` itself**.

## What this round produces

**Kernel results, in one new Lean module.** Act 1's evidence level 2 — kernel-checked — for every
named result, with `#print axioms` printing only `[propext, Classical.choice, Quot.sound]`, and no
`sorry`, `axiom` or `native_decide`.

**Definition budget.** The module introduces **at most six** top-level definitions: the tuple
interface (structure), its axiom predicate, the instantiation datum, a unistochasticity predicate,
the universal statement, and its negative. Witnesses are built **inside** the proofs that need them,
per act 3's lesson. The count is pinned in the result note and guarded.

## Mandatory controls

1. **Kernel discipline.** No `sorry`, `axiom`, `native_decide`; `#print axioms` for every named
   result; the new module registered in `verification/lean-manuscript-census.json`.
2. **Merged results are consumed, never re-proved.** `rootedMap_zero`, `rootedMap_isRowStochastic`,
   `rootedMap_mem_PPer`, `pper_has_responseRealization`, `RT1` and act 3's definitions are used as
   merged and not reshaped.
3. **Act 1's determinations are cited, never extended.** `BD3`, `BR3` and Q8 are neither reopened,
   softened nor re-derived.
4. **`CU1a`, `MP4` and `SA2` are cited, never revised.** No outcome here revises any of them, and
   acts 4 and 5 are not reopened.
5. **`p` is parameterized, never supplied.** No claim that our datum determines it.
6. **`A` is the full function algebra, taken canonically.** Not derived, not argued minimal, and the
   word "minimal" is not used of any construction.
7. **Source coordinates**, where cited, follow act 1's frozen table and act 5's authoritative
   surface — the PDF of arXiv:2302.10778v3 for Source A — and are never mixed across sources.
8. **Direct unistochasticity and dilatability stay distinct**, in both directions, per the control
   above.
9. **No representation-existence inference**, per the rule above.
10. **Each interface axiom is a separately named result**; no aggregate satisfaction claim.
11. **The `T₀ = {0}` divisibility vacuity is recorded**, and no outcome is read as evidence about
    `PDivisible`.
12. **`UB2` requires an exhibited lawful counterexample**; failure to prove `UB1` gives `UB3`.
13. **No manuscript edit**, whatever is found.
14. **No sourcing inference.** Track separation both ways, per Amendment 2. **No fifth condition.**
    No deferred Arc D resource adjudicated, and §3.6 is not reopened.

## Non-doings

Do not: choose a unitary lift or adopt any candidate-selection principle; adjudicate the
gauge-versus-empirical tension act 5 recorded open; prove or claim anything about interference;
decide `F1` versus `F2`; adjudicate dilatability or the dilated branch; reopen acts 4 or 5; claim
Source A is inapplicable on any outcome; infer unistochasticity from representation existence; claim
our datum supplies `p`; read the `T₀ = {0}` vacuity as evidence about `PDivisible`; use "minimal" of
any construction; begin the BD3 follow-up, Arc D round 2 or Arc E; edit manuscripts.

## Prediction recorded before executing

**`TI1` is likely**, on merged grounds rather than on any reading of a source: the axioms the
interface will require — non-negativity, normalization after transposition, trivialization at `0` —
are exactly what `rootedMap_isRowStochastic` and `rootedMap_zero` already give, with `T₀` and `p`
declarable per Q8's ledger. The live path to `TI2` is that stating the interface surfaces a side
condition Q8 did not examine, `Nonempty V` being the obvious candidate; act 4's M1 is the standing
reminder that an interface's axioms are not its components.

**`UB2` is materially likely, and this is the round's substantive prediction.** The ground is
merged and definitional, not a reading of Source A's construction: Arc B's `PPer` — the exact OI
visible class — requires `Γ 0 = 1`, **row** stochasticity at every time, and periodicity, and
carries **no column-sum condition**; while Source A states at p. 11 that every unistochastic matrix
is doubly stochastic. A lawful OI family that fails double stochasticity at some time would
therefore refute `UB1`. Whether one exists is exactly what the round must exhibit, and
`pper_has_responseRealization` supplies a merged route from any `PPer` family to a lawful
realization.

**The prediction is recorded at that strength and no higher.** It is not a finding: `UB2` is earned
only by an exhibited lawful counterexample, and if none is produced the answer is `UB3`.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen, committed before the work they affect.
- **Two PRs, in order.** Control-plane PR carrying **this file alone**, reviewed, frozen and merged
  before any execution; then exactly one execution/result PR from the resulting `main`.
- Final exact-head review after the Lean module, result note and registry updates are complete.
- No merge without an explicit owner direction after exact-head review.

## Allowed final report

1. the frozen interface, with each axiom named and its proof status individually;
2. the instantiation theorem and the declarations it runs under, with `p` shown parameterized;
3. the layer-1 label `TI1`–`TI3`, with `TI3`'s sub-status *refuted* or *unresolved* if reached;
4. the unistochasticity predicate and the universal statement, in the transposed orientation;
5. the layer-2 label `UB1`–`UB3`, with any counterexample exhibited as a lawful realization and a
   concrete matrix;
6. the **pair** `(TIx, UBy)`, reported as a pair and not collapsed;
7. the recorded predictions and whether each held;
8. the `T₀ = {0}` divisibility vacuity, and that no outcome bears on `PDivisible`;
9. the definition count, and the `#print axioms` line for every named result;
10. what remains open and what would settle it — including, under `UB2`, that the dilated branch is
    now the load-bearing obligation;
11. explicitly: that direct unistochasticity and dilatability are different propositions and neither
    was inferred from the other; that no outcome says Source A is inapplicable; that `CU1a`, `MP4`
    and `SA2` are unrevised; that no candidate-selection principle has been adopted; that nothing
    here claims OI forces quantum structure; and that nothing here is a sourcing claim.
