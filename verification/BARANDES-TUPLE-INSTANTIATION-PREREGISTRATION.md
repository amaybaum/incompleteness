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

    PPer Γ  ∧  p0 nonneg  ∧  ∑ j, p0 j = 1
        ⟹   BarandesTuple (V, ℕ, {0}, Γ_B, p, A)

with `Γ_B(t, 0) = (Γ t)ᵀ`, `p` CONSTRUCTED from `Γ_B` and `p0`, and `𝒜` the full commutative
algebra of maps `V × ℕ → ℝ`

**stated over the visible class rather than over the realization layer.** Arc B's
`C_OI(V) = PPer(V)` makes `PPer` the exact OI visible class, so proving it there is both stronger
and cleaner; that a merged `RootedRealization` instantiates the tuple then follows by composing with
the merged `rootedMap_mem_PPer`, and is recorded as a corollary rather than as the theorem.

**Layer 1 is independent of layer 2 altogether.** No result in this layer mentions
unistochasticity, and none is conditioned on the branch test's outcome.

### The interface is Source C v2's actual process, not a simplification

**The interface is typed from Source C v2 §3 directly**, at these coordinates on act 5's
authoritative surface convention — the PDF of arXiv:2309.03085v2:

| # | Axiom | Source C v2 |
|---|---|---|
| **X1a** | `C` finite, of size `N` | p. 8; the tuple `(C, T, T₀, Γ, p, A)` at eq (24), p. 8 |
| **X1b** | `T` is the set of target times and **includes the initial time `0`** | p. 8: "`T` denotes the system's set of target times, **including a time 0** that will be called the system's initial time" |
| **X1c** | `T₀ ⊂ T` is the set of conditioning times and **includes that same `0`** | p. 8: "`T₀ … is taken to be a subset `T₀ ⊂ T` … **`T₀` will be assumed to include the initial time 0**" |
| **X2** | `Γ : C² × T × T₀ → [0,1]`, with `Γ_ij(t ← t₀) ≡ p(i,t \| j,t₀)` for all `i,j ∈ C`, `t ∈ T`, `t₀ ∈ T₀` | eq (25), p. 8; eq (27), p. 9 |
| **X3** | normalization `Σ_i Γ_ij(t ← t₀) = 1`, for all `j`, `t`, `t₀ ∈ T₀` | eq (28), p. 9 |
| **X4** | trivialization `Γ_ij(t₀ ← t₀) ≡ δ_ij`, for all `t₀ ∈ T₀` | eq (29), p. 9 |
| **X5** | `p : C × T → [0,1]` | eqs (30)–(31), p. 9 |
| **X6** | initial normalization `Σ_j p_j(0) = 1` | eq (32), p. 10 |
| **X7** | marginalization `p_i(t) = Σ_j Γ_ij(t ← 0) p_j(0)` | eq (33), p. 10 |
| **X8** | all-time normalization `Σ_i p_i(t) = 1` for all `t` | eq (34), p. 10 |
| **X9** | divisibility over conditioning times: `Γ_ij(t ← t₀) = Σ_k Γ_ik(t ← t′) Γ_kj(t′ ← t₀)`, for all `t ∈ T` and **all `t₀, t′ ∈ T₀`** | eq (35), p. 10 |
| **X10** | `𝒜` is a **commutative algebra whose elements are maps** `A : C × T → ℝ`, under pointwise function arithmetic — **and is taken maximal**, containing every well-defined map of that form | eq (40), p. 12: "`A` denotes a **commutative algebra of maps of the form** `A : C × T → ℝ`, under the usual rules of function arithmetic"; eq (41); and p. 12: "will always be taken to be **maximal**, in the sense of containing every well-defined map of the form (40)" |

**The conditioning argument stays in the interface.** `Γ` is a map carrying `t₀ ∈ T₀`; instantiating
it at `T₀ = {0}` by `Γ_B(t, 0) := (Γ t)ᵀ` is a *declaration*, and the argument does not disappear
from the type. Proving `TI1` against a `Γ` that had lost it would be proving it for a weaker tuple
than Source C defines.

**X9 is a required axiom, and its restriction to `T₀` is the source's own.** Source C p. 10 writes
"The transition map `Γ` **will be assumed to satisfy** the following divisibility condition … for all
`i, j ∈ C`, `t ∈ T`, `t₀, t′ ∈ T₀`", and p. 11 adds that when `t′` is a target but not a conditioning
time the values "will not be well-defined, and the divisibility condition will not hold. The process
described here is therefore **indivisible for generic target times**." So X9 is an axiom *and*
consistent with act 1's `BD3`: it constrains only conditioning times and is no general divisibility
requirement.

### The declarations

| Component | Declaration |
|---|---|
| `C` | `V`, the visible carrier |
| `T` | `ℕ` |
| `T₀` | `{0}` |
| `Γ_B(t, 0)` | `(Γ t)ᵀ` for the `PPer` family — equivalently `(rootedMap R t)ᵀ`; the transposed orientation act 2 settled, and the one X3's sum over the first index requires |
| `p` | **constructed from a parameterized initial `p0`** — see below |
| `𝒜` | the **full commutative algebra of maps `V × ℕ → ℝ`** under pointwise arithmetic, taken maximal and canonical |

**`p` is parameterized at time 0 only, and constructed thereafter.** X5–X8 are not satisfied by an
arbitrary normalized static vector: eq (33) *fixes* every later-time value. So the round
parameterizes an arbitrary non-negative `p0` with `Σ_j p0 j = 1`, defines

    p i t  :=  ∑ j, (Γ t)ᵀ i j * p0 j

and proves X7 **by construction** and X8 **as a consequence** of X3 and X6 — which is how Source C
itself derives (34), from (28) and (32). **`p` remains declared rather than OI-supplied**, per Q8;
what changes is that only `p0` is free. Any statement of the form "our datum determines `p0`" is
forbidden.

**`𝒜` is the algebra, not one random variable, and it lives over `V × ℕ`.** Source C p. 12 says
"`A` denotes a **commutative algebra of maps of the form** `A : C × T → ℝ`" — so the tuple component
is the algebra whose *elements* are such maps, under pointwise function arithmetic, and the text then
takes it **maximal**, "containing every well-defined map of the form (40)". Two errors are therefore
forbidden: typing the component as a single map `C × T → ℝ`, and typing it over `V` alone. The
curried element form `V → ℕ → ℝ` is acceptable; `V → ℝ` is **not**. This is a type-level requirement
rather than a matter of wording. `𝒜` is taken canonically, not derived and not argued minimal; the
word "minimal" is not used of it.

### Every axiom individually

**Each of X1a–X10 is proved as its own named result**, with no aggregate "the tuple axioms hold".
Act 2's `rootedMap_zero`, `rootedMap_isRowStochastic` and the transpose lemmas are **consumed, not
re-proved**; what is new is the interface and the instantiation.

### The vacuity theorem, stated separately

This layer's treatment of X9 does **two** things, and they are separate named results.

**First, it discharges X9.** At `T₀ = {0}` the only admissible `t₀` and `t′` are both `0`, so the
condition reads `Γ_B(t,0) = Σ_k Γ_B(t,0)_{ik} Γ_B(0,0)_{kj}`, and X4's trivialization collapses the
right-hand side. X9 is therefore **proved**, not skipped — it is one of the ten axioms `TI1`
requires.

**Second, a separate named theorem states that discharging it says nothing about `PDivisible`.**
Our `PDivisible` quantifies over **all** intermediate times; X9 quantifies over conditioning times
in a singleton. **That theorem must not derive all-time `PDivisible`**, and no outcome of this layer
is evidence for or against it in either direction — it neither establishes divisibility nor refutes
it. Source C's own p. 11 remark, that the process "is therefore indivisible for generic target
times", is the source-side counterpart and is cited, not extended.

Keeping these two apart is the point: X9 being *discharged* is a fact about the interface at a
singleton `T₀`, and reading it as a divisibility finding about OI would be exactly the mistake the
second theorem exists to block.

### Layer-1 outcomes

**`TI1` — tuple instantiation proved.** Every axiom of the frozen interface is kernel-proved, in the
shape above, under the declarations above. Any side condition the theorem's statement carries —
`Nonempty V` or similar — is **named in the statement** and recorded; it does not change the label.

**`TI2` — a named tuple axiom is incompatible, with counterexample.** A lawful member of the class
is **exhibited** violating a **named** axiom X1a–X10. The burden is against the **fully typed frozen
interface under the frozen declarations** — with `p` constructed from `p0` and `A` on `V × ℕ` — and
**not** against a weaker reading: a `PPer` family paired with an arbitrarily chosen bad `p` is not a
counterexample, because `p` is not free at times after 0. This is a refutation and carries a
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
and are **consumed, not re-proved**. This lemma is what makes a `UB2` witness checkable by a **failed
row- or column-stochasticity check** rather than by reasoning about all unitaries — and **for the
planned witness below, specifically by a row-sum computation on `Aᵀ`**, since `Aᵀ` is
column-stochastic and it is its row sums that fail.

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

with `Γ 0 = 1` and period `2`. Its transpose is

    Aᵀ  =  [[1, 1], [0, 0]]

whose **columns** each sum to `1` — so `Aᵀ` **is** column-stochastic — and whose **rows** sum to `2`
and `0`, so it fails **row** stochasticity. The refutation therefore runs through the **row half** of
`IsUnistochastic M → IsRowStochastic M ∧ IsColStochastic M`, applied to `Aᵀ`, and **not** the column
half.

**The orientation is frozen here because it is easy to get backwards.** Transposing a row-stochastic
matrix makes it column-stochastic, so the failure that survives transposition into Source A's
orientation is the row one. An execution attempting to refute via column-stochasticity of `Aᵀ` would
be proving the wrong obligation, and would fail.

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

**Definition budget.** The module introduces **at most seven** top-level definitions, and these are
the seven:

1. `BarandesTuple` — the interface (a structure carrying X1a–X10);
2. its axiom predicate, if the structure does not carry the axioms as fields;
3. the constructed `p` from `Γ_B` and `p0` — inline in the instantiation if that keeps the count;
4. `IsUnistochastic`;
5. `DirectBranch`;
6. `OffDirectBranch`;
7. the `T₀ = {0}` divisibility condition the separate vacuity theorem is about.

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
5. **`p0` is parameterized, never supplied**, and `p` at later times is **constructed** per X7, not
declared. No claim that our datum determines `p0`.
6. **`A` is the full function algebra, taken canonically.** Not derived, not argued minimal, and the
   word "minimal" is not used of any construction.
7. **Source coordinates**, where cited, follow act 1's frozen table and act 5's authoritative
   surface — the PDF of arXiv:2302.10778v3 for Source A — and are never mixed across sources.
8. **Direct unistochasticity and dilatability stay distinct**, in both directions, per the control
   above.
9. **No representation shortcut**, per the rule above: `QfbData.born`, `overlap_row_sum`,
   `overlap_col_sum`, `QStar` and representation existence are all disqualified from discharging
   `UB1`, and `IsUnistochastic` is defined from scratch rather than through any of them.
10. **Each interface axiom is a separately named result** — X1a through X10 above; no aggregate
    satisfaction claim, and the interface is typed from Source C v2 rather than summarized, so that
    `TI1` is not proved for a weaker tuple than the source defines. **Layer 1 mentions
    unistochasticity nowhere** and is conditioned on no layer-2 outcome.
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

**`TI1` is likely, but less trivially than the earlier draft assumed.** X2–X4 are what `PPer`
already carries after transposition, and X9 collapses by X4 at a singleton `T₀`. What the earlier
draft missed, and what this freeze now requires, is that X5–X8 are a *law* rather than a
declaration: eq (33) fixes `p` at every later time, and X8 must be derived rather than assumed. The
live path away from `TI1` is therefore an axiom the earlier component-level ledger did not examine —
act 4's M1 one level down, and the reason the interface is typed from the source rather than
summarized. Whether such an axiom would be *refuted* (`TI2`) or merely *unsettled* (`TI3`) cannot be
predicted, and is not.

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

1. the frozen interface X1a–X10, with each axiom named, cited to Source C v2, and its proof status
   individually;
2. the instantiation theorem and the declarations it runs under, with `p0` shown parameterized and
   `p` shown constructed per X7, and `A` on `V × ℕ`;
3. the layer-1 label `TI1`–`TI3`, with `TI2`'s named axiom and exhibited counterexample if reached,
   or `TI3`'s named obstruction;
4. the unistochasticity predicate and the universal statement, in the transposed orientation;
5. the layer-2 label `UB1`–`UB3`, with any counterexample exhibited as a lawful realization and a
   concrete matrix;
6. the **pair** `(TIx, UBy)`, reported as a pair and not collapsed;
7. the recorded predictions and whether each held;
8. X9 discharged at `T₀ = {0}` by trivialization, and — separately — that discharging it bears on
   `PDivisible` in neither direction;
9. the definition count, and the `#print axioms` line for every named result;
10. what remains open and what would settle it — including, under `UB2`, that the dilated branch is
    now the load-bearing obligation;
11. explicitly: that direct unistochasticity and dilatability are different propositions and neither
    was inferred from the other; that no outcome says Source A is inapplicable; that `CU1a`, `MP4`
    and `SA2` are unrevised; that no candidate-selection principle has been adopted; that nothing
    here claims OI forces quantum structure; and that nothing here is a sourcing claim.
