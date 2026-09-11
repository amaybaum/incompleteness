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
| **1 — tuple instantiation** | Does the OI visible class `PPer` instantiate the external stochastic-process tuple interface? | `TI1` / `TI2` / `TI3` |
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

Define the external stochastic-process tuple interface and **prove** the instantiation theorem, in
the shape

    PPer Γ  ∧  p normalized   ⟹   BarandesTuple (V, ℕ, {0}, Γᵀ, p, V → ℝ)

**stated over the visible class rather than over the realization layer.** Arc B's
`C_OI(V) = PPer(V)` makes `PPer` the exact OI visible class, so proving it there is both stronger
and cleaner; that a merged `RootedRealization` instantiates the tuple then follows by composing with
the merged `rootedMap_mem_PPer`, and is recorded as a corollary rather than as the theorem.

**Layer 1 is independent of layer 2 altogether.** No result in this layer mentions
unistochasticity, and none is conditioned on the branch test's outcome.

The declarations are exactly these:

| Component | Declaration |
|---|---|
| `C` | `V`, the visible carrier |
| `T` | `ℕ` |
| `T₀` | `{0}` |
| `Γ(t ← 0)` | `(Γ t)ᵀ` for the `PPer` family — equivalently `(rootedMap R t)ᵀ` at the realization layer; the transposed orientation act 2 settled |
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
tuple axioms hold". The separately frozen subresults are:

1. **finite carrier** — `C = V` is a `Fintype`;
2. **column-stochasticity after transpose** — `IsColStochastic ((Γ t)ᵀ)`, which is Source A's and
   Source C's normalization orientation; act 2's `isRowStochastic_iff_isColStochastic_transpose` is
   consumed, not re-proved;
3. **identity / trivialization at zero** — `(Γ 0)ᵀ = 1`;
4. **the normalized standalone `p`** — non-negative and summing to one, as declared;
5. **the full observable algebra** — `V → ℝ` taken canonically as `A`;
6. **the singleton-`T₀` conditioning condition** — `T₀ = {0}` as the conditioning-time set.

Act 2's `rootedMap_zero` and `rootedMap_isRowStochastic`, and the transpose lemmas, are **consumed,
not re-proved**; what is new is the interface and the instantiation.

If stating the interface surfaces an axiom act 1's Q8 did not examine, that axiom is proved or its
status recorded — Q8's ledger is inherited as a ledger of *components*, and this layer extends it to
the *interface's axioms*, which is a different question.

### The vacuity theorem, stated separately

**A separate named theorem states that the Source-C divisibility condition restricted to
`T₀ = {0}` is vacuous** — a condition quantified over conditioning times in a singleton says nothing
about our all-time `PDivisible`, which quantifies over all intermediate times.

**That theorem must not derive all-time `PDivisible`**, and no outcome of this layer is evidence for
or against it in either direction. The vacuity is recorded precisely because it is easy to mistake
for a finding, and in both directions at once: it neither establishes divisibility nor refutes it.

### Layer-1 outcomes

**`TI1` — tuple instantiation proved.** Every axiom of the frozen interface is kernel-proved, in the
shape above, under the declarations above. Any side condition the theorem's statement carries —
`Nonempty V` or similar — is **named in the statement** and recorded; it does not change the label.

**`TI2` — a named tuple axiom is incompatible, with counterexample.** A lawful member of the class
is **exhibited** violating a **named** axiom of the interface. This is a refutation and carries a
refutation's burden.

**`TI3` — unresolved.** Neither proved nor refuted, with the axiom and the obstruction named.

**Failure to prove `TI1` is not `TI2`.** `TI2` requires an exhibited lawful counterexample; absent
one the answer is `TI3`. This is act 5's A1 discipline one layer down, and the grid is deliberately
**parallel to layer 2's** so the same rule reads the same way in both.

## Layer 2 — the Source-A branch test

### The branch-test target — three exact ingredients

**1. `IsUnistochastic`, defined independently of any existing representation object.** Existence of
a complex unitary whose entrywise norm-squares equal the visible matrix, per Source A (30), p. 11:

    IsUnistochastic M  ≡  ∃ U : Matrix V V ℂ, U ∈ unitaryGroup ∧ ∀ i j, M i j = ‖U i j‖²

It is defined from scratch — **not** in terms of `QfbData`, `QStar`, `born`, `overlap`, or anything
else in the representation corpus. Defining it through any of those would build the shortcut this
round exists to forbid straight into the predicate.

**2. The structural lemma.** Unistochasticity forces stochasticity in *both* directions:

    IsUnistochastic M  →  IsRowStochastic M ∧ IsColStochastic M

This is Source A's own observation at p. 11 — "every unistochastic transition matrix is doubly
stochastic" — proved here rather than cited. `IsColStochastic` and the transpose lemmas are act 2's
and are **consumed, not re-proved**. This lemma is what makes a `UB2` witness checkable by a
column-sum computation rather than by reasoning about all unitaries.

**3. The direct-branch proposition, in the exact external orientation**, and its genuine
counterexample complement:

    DirectBranch   ≡  ∀ Γ, PPer Γ → ∀ t, IsUnistochastic ((Γ t)ᵀ)

    OffDirectBranch ≡  ∃ Γ, PPer Γ ∧ ∃ t, ¬ IsUnistochastic ((Γ t)ᵀ)

These are stated over `PPer` — Arc B's exact OI visible class — so the branch test is about the
class, not about one realization. The second is the **genuine** complement: an exhibited witness,
not the mere absence of a proof of the first.

### Layer-2 outcomes

**`UB1` — proved.** `DirectBranch` holds: every OI / `PPer` visible family is directly
unistochastic, kernel-proved.

**`UB2` — refuted.** `OffDirectBranch` is proved: a **lawful OI / `PPer` family** is exhibited that
is not directly unistochastic. The witness must be lawful — a genuine `PPer` family, and where the
realization layer is wanted, a genuine `RootedRealization` with a normalized non-negative prior,
obtainable through the merged `pper_has_responseRealization`.

**`UB3` — unresolved.** Neither proved nor refuted, with what is missing named.

### The planned `UB2` route, recorded as motivation and not as a result

If `UB2` is reached, the intended witness is on `Fin 2`: a `PPer` family whose slice at some `t > 0`
is the row-stochastic

    A  =  [[1, 0], [1, 0]]

with `Γ 0 = 1` and period `2`. Its transpose has a zero row, so it is not column-stochastic, and the
structural lemma then denies unistochasticity.

**This is recorded here as the planned route, not as an executed result.** It is written into the
freeze so the execution cannot quietly substitute a weaker or differently-shaped witness, and it is
**not** a preregistered conclusion: the round must still prove `PPer` membership and the negation,
and if it cannot, the answer is `UB3`.

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

## No representation shortcut

**`QfbData.born`, `overlap_row_sum`, `overlap_col_sum`, `QStar`, or the existence of any
Hilbert/unitary representation may not discharge `UB1`** — not unless a **merged theorem** identifies
**the exact matrix under test, at every time**, with the corresponding unitary modulus-square matrix.
Arc D's `RD1` is why: representational presence is a proved disqualified ground.

The corpus already proves unitary-derived Born matrices have the expected row normalization, and
that the overlap construction is doubly stochastic. **Neither fact identifies those matrices with the
rooted family**, and that gap is the whole of the trap:

- **`overlap_row_sum` / `overlap_col_sum`** (`CoherentLift.lean`) prove `B_{ia} = |V_{ia}|²` doubly
  stochastic — genuinely a modulus-square of a unitary, but of the **coherent-lift transport matrix
  on the shell**, not of `(Γ t)ᵀ`. No merged theorem equates the two.
- **`QfbData.born`** is `‖Q.U b' b‖²` — a modulus-square of a unitary on the **basis carrier
  `Bas`**, not on `V`. The passage from basis to visible carrier runs through the fibre structure,
  and act 3's `CU1a` proved that passage does not determine a unique visible candidate.
- **`QStar`** is an all-time fixed-basis Born **representability** predicate; Arc C's `RC1` places it
  in **proper overlap** with `C_OI`, so it is neither necessary nor sufficient here, and in any case
  representability is existence of *some* representation, which is exactly what `RD1` disqualifies.

Any `UB1` must be proved **about `(Γ t)ᵀ` itself**, through the `IsUnistochastic` predicate defined
from scratch above.

## What this round produces

**Kernel results, in one new Lean module.** Act 1's evidence level 2 — kernel-checked — for every
named result, with `#print axioms` printing only `[propext, Classical.choice, Quot.sound]`, and no
`sorry`, `axiom` or `native_decide`.

**Definition budget.** The module introduces **at most six** top-level definitions, and these are
the six:

1. `BarandesTuple` — the interface (a structure);
2. its axiom predicate, if the structure does not already carry the axioms as fields;
3. `IsUnistochastic`;
4. `DirectBranch`;
5. `OffDirectBranch`;
6. the `T₀ = {0}` divisibility condition whose vacuity the separate theorem states.

`IsColStochastic` and the transpose lemmas are act 2's and are imported, not redefined. **Witnesses
are built inside the proofs that need them**, per act 3's lesson — no top-level witness definitions.
The count is pinned in the result note and guarded.

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
9. **No representation shortcut**, per the rule above: `QfbData.born`, `overlap_row_sum`,
   `overlap_col_sum`, `QStar` and representation existence are all disqualified from discharging
   `UB1`, and `IsUnistochastic` is defined from scratch rather than through any of them.
10. **Each interface axiom is a separately named result** — the six frozen subresults above; no
    aggregate satisfaction claim. **Layer 1 mentions unistochasticity nowhere** and is conditioned on
    no layer-2 outcome.
11. **The `T₀ = {0}` divisibility vacuity is recorded**, and no outcome is read as evidence about
    `PDivisible`.
12. **`UB2` and `TI2` each require an exhibited lawful counterexample**; failure to prove `UB1`
    gives `UB3`, and failure to prove `TI1` gives `TI3`.
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
are exactly what `PPer` already carries, with `T₀` and `p` declarable per Q8's ledger. The live path
away from `TI1` is that stating the interface surfaces an axiom Q8 did not examine; act 4's M1 is
the standing reminder that an interface's axioms are not its components. Whether such an axiom would
be *refuted* (`TI2`) or merely *unsettled* (`TI3`) cannot be predicted, and is not.

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
3. the layer-1 label `TI1`–`TI3`, with `TI2`'s named axiom and exhibited counterexample if reached,
   or `TI3`'s named obstruction;
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
