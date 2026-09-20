# Track B act 26 — the circle-gluing rigidity of the normalized space: the restricted Euclidean metric and the mandatory affine extension, the census of the relabelled Fourier circles, a gated classification of the surjective isometries or a kernel-certified isometry outside the family, and the prefix-constrained corollary: RESULT

Executed under the frozen control plane `preregistration.md` in this directory, blob
**`521b63ccde0056453f42035ba9d7970be66cf6f9`**, from `main` at **`e0be0ab6dca7b6661a008a9f5e1f3a29ea736003`** —
the certified merge commit of that control plane, the round's mandated execution base `B`, certified
by main-push run 35499317330 with all four jobs green and the control-plane base check in mode `B`
reporting twenty-one rows and no failure — which this execution verified by blob as its first act,
before any target was executed.

**Outcome vector:** `A26-0-EXTENDS` · `A26-1-SEVERAL` · `A26-2-UNDECIDED` · `A26-3-NOT-EXECUTED`

**The headline is row 4 of the freeze's outcome-vector table, verbatim.** `A26-0` landed by
`a26_0_affine_extension`, its three conjuncts separate; `A26-1` landed by `a26_1_circle_census`
stating the `SEVERAL` branch, with the count `A26-1-N` obtained by `a26_1_circle_count` and the
dimension `A26-1-DIM` undecided; `A26-2` undecided with the positive route run — its first step
closed by `rigid_motion_of_tuple_isometry`, its second step, the marked set, not obtained, the
obstruction named; `A26-3` not executed, the gate closing on `A26-2-UNDECIDED`. `A26-2-P` is
undecided and enters no label. Every verdict is of the exact frozen proposition at the exact
configuration, with the geometry bound by equation or by `featureVec`, every generator written by its
frozen formula and the three definitions carried with their frozen statements, and of nothing in its
neighbourhood. **No verdict was inferred from another beyond the consumptions the freeze places.**
**No map is read as a symmetry, an antiunitary map, a time reversal or a dynamics.** **No theorem is
attributed to the literature, none of its theorems is consumed, and Mazur–Ulam is invoked nowhere.**
**Every earlier act's historical verdicts stand unchanged**: acts 12 through 25's labels are consumed
as landed, and this round's labels are earned under this freeze about the normalized space and the
family alone.

> **THE CLAUSE, carried at this mention — the headline.**
> Act 26 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 1. The round's shape, restated

**This is a SEALING round** under `AGENTS.md` `§A.37`, executed under the manifest protocol. It
creates new seal state — a new Lean module with three budgeted definitions and new named results and
a new `R7-*` guard clause — and it lands **`E` → `L` → `P`, with `P` mandatory**.

| object | where it lives | state at this execution | state from `P` |
| --- | --- | --- | --- |
| the mandated execution base | the prospective declaration `_MANIFEST_PROSPECTIVE = {'CGR': 'e0be0ab6dca7b6661a008a9f5e1f3a29ea736003'}` in `verification/lean/edge_rigidity_probe.py` | **declared**; the validator classifies `CGR` as `EXECUTION` against it | **removed** by `P` |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': 'e0be0ab6dca7b6661a008a9f5e1f3a29ea736003', 'authorized': ('CGR',)}` | the thirty records of the seals tree `08b37f66c35dae909b8cd820ca5705f66f4015b6` at `B`, plus the one addition authorized by stem | unchanged |
| the round's manifest record | `verification/seals/CGR.json` | **absent** | **written by `P`**: `{"round": "CGR", "kind": "sealed", "base": "e0be0ab6dca7b6661a008a9f5e1f3a29ea736003", "sealed_head": E, "merge": L}` |

**`CGR.json` is absent at execution and is written by `P` and by nothing before `P`.** That is a
statement about this execution and stays true as one. **No legacy seal constant is written**: nothing
matching `_CGR_(BASE|SEALED_HEAD|MERGE)` exists at any commit of this branch, and `SI-3`'s standing
contract — zero legacy assignment statements in the guard file — holds at every head. **No existing
manifest record is altered**: the thirty records at `B` are read and never written, and the
chronology verdict is the validator's through one keyed call, `_si2_authority('CGR', tag='R7-CGR')`.
**No closed round's contract is edited**: the supersession table is empty, and every closed round's
guard reads its own record at every head of this branch.

**The base-blob verification is recorded.** `git cat-file -p e0be0ab6:verification/programmes/oi-qm/track-b/act-26-orbit-geometry-rigidity/preregistration.md | git hash-object --stdin`
returns `521b63ccde0056453f42035ba9d7970be66cf6f9`, the blob the freeze names and the blob the
`R7-CGR` clause pins; `git rev-parse e0be0ab6:…/preregistration.md` returns the same, and so does
`git hash-object` on the file in the working tree at every commit of this branch.

**The files this round writes** are the new module `verification/lean-mathlib/OIBridge/OrbitGeometryRigidity.lean`,
this result note, one import line in `verification/lean-mathlib/OIBridge.lean` (directly after act
25's module, line 214), one census entry in `verification/lean-manuscript-census.json`, the `R7-CGR`
clause with the two declarations in `verification/lean/edge_rigidity_probe.py`, and the frozen
post-round sentence appended to the `P0` row of `verification/ROADMAP.md` after act 25's. **No
manuscript file is written.**

## 2. The start state

**Every one of the thirty paths the freeze pins by blob was checked at `B` by `git rev-parse`,
and every one matches**; they are the `frozen-blob` lines of the freeze's machine-checkable block,
which the base check verified at `M` (run 35496392690, at the candidate merge of pull request #698)
and at `B` (run 35499317330). The four files this round writes onto carry their pinned blobs at `B`:
`verification/ROADMAP.md` at `ac77cd2c9c7f6570dbd4e4f9c7301e6a057d6980`,
`verification/lean/edge_rigidity_probe.py` at `6d989ad2b89bc4d3e4b6335e654035c8dfb84b8b`,
`verification/lean-mathlib/OIBridge.lean` at `e95216970107304f116fc3edb7655712c07b3bec` and
`verification/lean-manuscript-census.json` at `0b7bd780e22efa617ec7fb06b2c9ed23ed7b7bc1`. The seals
tree at `B` is `08b37f66c35dae909b8cd820ca5705f66f4015b6`, thirty records, twenty-four `sealed`
and six `base-only`, no `CGR.json`, the same tree as at `D`.

**No start-state discrepancy arose in any pinned blob.** `D = ba8a98af…` and `B` are distinct
commits, as the freeze reads them: the drafting-time facts are facts about `D`, the pins are read at
`B`, and every pinned blob is the same at both, the tree at `B` differing from the tree at `D` by
exactly the one added preregistration file (2027 lines, no other path). `B`'s parents are `D` and
`112f997fa2fbf7d6c6f4ed4db64af3c841749e4e`, the head of pull request #698.

**The anti-contamination invariant is honoured**, carried in the freeze's own wording:

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

Sibling lanes present at `B` are not inputs and none was read. The start-state table is the complete
list of what this round consumes.

## 3. The ordering obligation's records

The obligation, in the freeze's own wording, which binds this execution:

> **The ordering obligation, act 26.** The rungs are act 21's declarations at blob `860daac4…`, the
> equivalence is act 12's at blob `4bba2040…`, the invariant family and the geometry are act 24's
> at blob `ce9d1aa0…`, the family and the class description are act 25's at blob `954fbdda…`, and
> nothing else. The execution's module **states no rung and no equivalence, and declares exactly
> the budgeted definitions — at most three, each with its frozen statement — and nothing else**;
> the geometry is bound, in every theorem that names it, to act 24's equation or to `featureVec`;
> each generator of the family is written, in every theorem that names it, by act 25's formula; the
> transpose is written by act 25's relation; and the four-shape conclusion is written out in every
> classification statement. From the module commit to the certified head `E`, **no commit of the
> branch adds, removes or alters a declaration, restates a rung, alters the geometry's equation,
> alters a generator's formula, adds or removes a generator, or uses an equivalence outside the
> frozen quotient list**; the module commit carries no verdict of any target; the verdict commits of
> the executed targets follow it in the order `A26-0`, `A26-1`, `A26-2`, `A26-3`; and no theorem of
> a later target's section is present before that target's verdict commit.

**Eight records, each checkable by an auditor from the branch alone.** The execution branch is
`claude/act-26-execution`, rooted at `B`, and its first-parent chain from `B` is, in order:

| # | commit | content |
| --- | --- | --- |
| 1 | `2ad6788111dac06258f5cac3d84dfa28966715f6` | **stage A**: the two declarations set to `B`, in the guard file only |
| 2 | `93a96aef82ada94e62f88f94cd31b8548cac7d07` | **the module commit**: the three definitions, Section A's ten shared lemmas, plus the import line; no verdict, no coincidence lemma |
| 3 | `913d70cc1eb9979eb9210efe729bc056661f6699` | `A26-0`: `a26_0_affine_extension` and five supporting results |
| 4 | `7cc175bc04eeb3e99e6b36a6fa4ef4de112fb632` | `A26-1`: `a26_1_circle_census`, `a26_1_circle_count` and one hundred thirty-nine supporting results |
| 5 | `5282eda2327d945b4b5d7586a8bb260589ecfbdf` | `A26-2`: `rigid_motion_of_tuple_isometry`, the positive route's first step; no classification theorem, no witness |

followed by the packaging commit carrying this note, the `R7-CGR` clause, the `ROADMAP` sentence,
the census entry and the axiom table's remaining lines, and by whatever certification fixes as `E`.
**`A26-3` has no verdict commit**: the gate did not open it.

### 3.1 The declaration table (record 1)

| object | the merged declaration consumed, with its line range at its blob | this round's module |
| --- | --- | --- |
| `FibreGram` | `TwoSidedGauge.lean` `4bba2040c33424fafbc6d31c0d63b86dff33691a`, lines 95–97 | consumed unrestated |
| `GramPhaseEquiv` | the same, lines 102–103 | consumed unrestated; the only equivalence used in any verdict |
| `RealizableGram` | the same, lines 108–110 | consumed unrestated; "realizable" in every statement |
| `fibreGram_apply`, `sh1_necessity`, `sh1_sufficiency` | the same, lines 115–116, 168, 1070 | consumed through act 25's theorems |
| `AdmissibleDilationAt` | `DilationChoice.lean` `7e3a8222cedf530f3c109662e7174d72b6358063`, lines 134–136 | consumed unrestated; named in no statement of this round, no transpose shape being stated |
| `RelabelTransition` | `RepresentativeNaturality.lean` `4c1137f35600320b9273c857ec62271341b05cd0`, lines 167–168 | consumed unrestated; named in no statement of this round |
| `mixedTriple` | `OrbitGeometrySelector.lean` `ce9d1aa05dfdedfb5cac171cfe6379681942195f`, lines 79–80 | consumed unrestated; the body of `featureVec`; the geometry bound to its equation in every theorem that names `d` |
| `dist_eq_norm_toLp`, `geo1_separation_single`, `geo1_equiv_of_zero_single`, `mixedTriple_gauge` | the same, lines 439–443, 412, 497, 88 | consumed, in the shared lemmas |
| `ProperAt`, `PropagatesFrom` | `IntermediateCrossTimeStructure.lean` `cb14c43b0becfe1a379ae3615d5553723ede9163`, lines 167–171 and 186–193 | the prefix's standing hypotheses; named in no statement of this round, `A26-3` not being executed |
| `EvolvesTotally`, `PreservesAdmissible`, `L2` inline, `Reversible`, `L4d` inline | `OrbitLawRigidityTwisted.lean` `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8`, lines 96–100, 108–110, 123–128, and `LadderConds` 179–196 | the prefix's rungs; named in no statement of this round, `A26-3` not being executed |
| act 23's `H z` | `OrbitLawGaps.lean` `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1`, `hadamard_z_admissible` at line 116 | the lambda `Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)`, written out at every mention |
| act 25's `iso1_family_acts`, `iso2_classes_single`, `fourier_coord_uniform` | `OrbitGeometryIsometries.lean` `954fbddaa7511713a26c316b3b2e0f29497e81d2`, lines 636, 1081, 1159 | consumed; `iso2_classes_single` in both directions in the shared lemmas, `relabel2_relabel2` and `relabel2_gramPhaseEquiv` (lines 488, 290) in the count, `mixedTriple_relabel2` (line 72) nowhere in a statement |
| this round's module | — | **exactly the three budgeted definitions, each with its frozen statement** (below); no `abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque` at any commit; it imports `OIBridge.OrbitGeometryIsometries` |

**This round's module carries exactly the three budgeted definitions, each verbatim**, and no other
declaration of any kind at any commit; it imports `OIBridge.OrbitGeometryIsometries`; `R7-CGR`
checks both mechanically at every commit from the module commit to the certified object. The three,
as the module carries them:

```
def featureVec {V : Type} [Fintype V] [DecidableEq V] (G : V → Matrix V V ℂ) :
    EuclideanSpace ℂ ((V × V × V) × (V × V × V)) :=
  WithLp.toLp 2 (mixedTriple G)
```

```
def normalizedSet (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) :
    Set (EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) :=
  {x | ∃ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G ∧ featureVec G = x}
```

```
def IsSurjIsometryOn {E : Type} [MetricSpace E] (S : Set E) (f : E → E) : Prop :=
  (∀ x ∈ S, f x ∈ S) ∧ (∀ y ∈ S, ∃ x ∈ S, f x = y) ∧ ∀ x ∈ S, ∀ y ∈ S, dist (f x) (f y) = dist x y
```

**None of the three was omitted.** **No rung was restated, no equivalence was widened, no generator
was added or removed, no domain and no metric was substituted, no affinity was assumed and nothing
was imported.**

### 3.2 The stage-A commit (record 2)

**`2ad6788111dac06258f5cac3d84dfa28966715f6`.** `git show --stat` lists one file,
`verification/lean/edge_rigidity_probe.py`, +2/−2: `_MANIFEST_PROSPECTIVE = {'CGR': B}` and
`_MANIFEST_BASELINE = {'base': B, 'authorized': ('CGR',)}`, both outside the validator's
marker-bounded regions, and nothing else. The supersession table being empty, no closed round's
contract is touched. At this commit the guard printed **eighty-nine `R7-*` tags, all `PASS`**,
`R7-OGC` and `R7-OGS` classified `ARCHIVED`, with `CGR` declared.

### 3.3 The module commit (record 3)

**`93a96aef82ada94e62f88f94cd31b8548cac7d07`**, the first commit at which the module is present. It
carries the three definitions and the named results **`featureVec_ofLp`**, **`dist_featureVec`**, **`featureVec_gauge`**, **`gramPhaseEquiv_of_featureVec_eq`**, **`featureVec_mem_normalizedSet`**, **`relabelled_fourier_mem_normalizedSet`**, **`normalizedSet_eq_iUnion`**, **`featureVec_image_eq`**, **`bridge_of_tuple_isometry`**, **`tuple_isometry_of_bridge`** — the unfolding of the feature
embedding, act 24's distance as the ambient distance of feature vectors, equal feature vectors for
equivalent tuples and the converse on realizable tuples, membership of realizable tuples and of the
relabelled Fourier tuples in the normalized set with the union equality as act 25's description
restated, the image lemma, and the bridge between tuple-level and set-level surjective isometries in
both directions — each a shared lemma and none a verdict: no conjunct of any target is discharged or
refuted, no extension is stated, no coincidence or non-coincidence of any relabelled circle with the
Fourier circle is stated, no count and no dimension is stated, no isometry is classified, and no
transition family is named in the module at this commit or at any later one.

### 3.4 The verdict commits (record 4)

| target | commit | named results |
| --- | --- | --- |
| `A26-0` | `913d70cc1eb9979eb9210efe729bc056661f6699` | `inner_sub_eq_of_dist_eq`, `exists_linearIsometryEquiv_of_inner_eq`, `exists_affineIsometryEquiv_of_dist_eq`, `eqOn_affineSpan_of_agree`, `exists_affineIsometryEquiv_of_isSurjIsometryOn`, `a26_0_affine_extension` |
| `A26-1` | `7cc175bc04eeb3e99e6b36a6fa4ef4de112fb632` | `fourier_coord_002`, `relabelled_coord_002`, `a26_1_circle_census`, `circle_coincide_trans`, `stab_row_swap13`, `stab_col_swap13`, `stab_row_double`, `stab_col_double`, `perm_decomp`, `pred_row_swap13`, `pred_col_swap13`, `pred_row_double`, `pred_col_double`, `pred_one`, `pred_row`, `pred_col`, `pred_stab`, `a26_1_circle_count`, and the one hundred twenty-three generated coordinate and pair lemmas `core_const_0`–`core_const_18`, `core_val_0`–`core_val_31`, `nc_0`–`nc_71` |
| `A26-2` | `5282eda2327d945b4b5d7586a8bb260589ecfbdf` | `rigid_motion_of_tuple_isometry` |
| `A26-3` | **none** | **none** — the gate did not open it |

Each verdict theorem first appears at its own verdict commit and at no earlier commit; each verdict
commit carries its own target's results and nothing of a later target's; the order on the
first-parent chain is `A26-0`, `A26-1`, `A26-2`. **The gate opened `A26-2`'s positive route** in
its extension form on `A26-0-EXTENDS` and `A26-1-SEVERAL`, the negative route being available under
either census branch, and **closed `A26-3`** in its rigidity form on `A26-2-UNDECIDED`; `A26-3`
has the label `A26-3-NOT-EXECUTED` by the gate rule.

### 3.5 The immutability span (record 5)

`git diff 93a96aef82ada94e62f88f94cd31b8548cac7d07 <E> -- verification/lean-mathlib/OIBridge/OrbitGeometryRigidity.lean | grep -c -E '^[-+](def |abbrev |structure |class |instance |axiom |opaque )'`
**returns `0`**: no diff between the module commit and the certified head adds or removes a
definition of any kind; the three frozen `def` lines and their bodies are byte-identical at every
commit from the module commit on. Measured at each verdict commit and at the packaging commit — which
touches the module only to complete the axiom table, adding `#print axioms` lines and nothing else —
and re-run by `R7-CGR` on every head from the module commit to the certified object.

### 3.6 The quotient, geometry, family and metric record (record 6)

**The only equivalence used in any verdict is act 12's `GramPhaseEquiv`**, through
`gramPhaseEquiv_refl`, `gramPhaseEquiv_trans`, act 24's `mixedTriple_gauge`, and act 25's
`relabel2_gramPhaseEquiv`; act 17's `GramTrajEquiv` and act 21's `LawEquiv` are not used. **The
geometry is bound, in every theorem that names it, to
`d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)`** — as the hypothesis `hd`
in every shared lemma and in the rigid-motion step — and **`featureVec`'s body is
`WithLp.toLp 2 (mixedTriple G)`** at its one declaration. **The metric is the restricted ambient one
at every mention**: `dist` of `EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))`
restricted to `normalizedSet Γ₀`, equal to `d` on realizable tuples by `dist_featureVec`, and never a
path metric or an intrinsic one. **Every generator is written, in every theorem that names it, by its
frozen formula**: the independent relabellings as `fun i => (G (π i)).submatrix τ τ` with one
permutation on the fibre label and one on both matrix indices, at bound permutations and at the
exhibited ones; the conjugation and the transpose are named in no statement of this round, no
four-shape conclusion being stated. **No equivalence was introduced or widened, no generator was
added or removed, no domain was substituted for the normalized space, no affinity was assumed, and
nothing was imported**; no candidate equivalence and no fifth generator was noticed.

### 3.7 The attestation set — three questions, answered as measurements at five boundaries (record 7)

The three questions, in act 21's wording at its lines 1033–1043, as this freeze consumes them:

> **Q1 — INTENTIONAL.** Did the execution attempt or run any proof, search, decision procedure or
> numerical experiment intended to reveal which of the frozen candidate laws satisfies or fails any
> rung, whether any rung is implied by the earlier rungs, or whether a same-initial-orbit pair
> exists?
>
> **Q2 — INCIDENTAL.** Did any compiler response, elaboration result, typeclass resolution, accepted
> or rejected term, or build output reveal any of that unintentionally?
>
> **Q3 — UNAIDED REASONING.** Did the execution **reason its way** to any information bearing on
> which laws survive, on which rungs restrict, or on the discriminating pair, **without running
> anything**?

**A PARTIAL fact counts for all three. There is no threshold below which a fact about the candidates
does not count.** Each answer is a measurement about what the execution acquired **in that span**
bearing on any target **not yet closed at the span's end**; what the freeze itself places in front of
the execution is not a YES and is listed. A span ending at a target the gate did not open is answered
for the targets that remain. **Knowledge acquired before a span is not acquired in it**: what the executor
knew before this chain's first commit is disclosed once, below, and each span answers for what it newly
acquired. **A YES is disclosed and is not cured by its disclosure.**

#### The prior knowledge, disclosed once and before the spans

**Before this chain's first commit the executor held no knowledge of any target's outcome.** It held the
landed record — acts 12 through 25, every consumed theorem and note — the freeze itself with its routes
and its hand-read branch predictions, and the drafting-time library readings the freeze records
(Mazur–Ulam whole-space only; the pieces of the extension argument; the real instance path). No census,
no coincidence, no count, no dimension, no candidate isometry and no extension proof was computed or
attempted before the freeze or between the freeze and `B`. This disclosure lists what the freeze supplies
and is not a cure for anything. **The span answers below measure what was newly acquired in each span and
nothing else**; the prior knowledge is not re-counted at any span.

#### The span `B` → module commit

| question | answer for the span `B` → module commit |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: verified the frozen blob at `B` by `git rev-parse` and `git cat-file | git hash-object`; created the branch from `B`; wrote and committed the stage-A edit and ran the guard at that commit; wrote the three definitions from the freeze's statements; ran a type-check probe in the scratchpad and not in the tree, confirming the instance path `InnerProductSpace ℝ (EuclideanSpace ℂ ι)` and `FiniteDimensional ℝ`, the affine-isometry type, `affineSpan`, `vectorSpan` and `Module.finrank`, `exists_affineIndependent`, `LinearIsometry.extend`, the polarization identity, and that the three definitions and the distance bridge typecheck — and finding the affine-span agreement lemma under the name `AffineMap.eqOn_affineSpan`; wrote and built Section A — the unfolding, the distance bridge, the gauge and separation lemmas, the membership and union lemmas restating act 25's description, the image lemma and the bridge in both directions — and the import line; built with zero errors. Nothing was run bearing on any target's outcome: no coincidence, no extension, no count, no dimension and no candidate was tested or proved; the probe revealed instance-resolution facts and a lemma name, which the freeze's route already reads and which decide nothing about any target.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's proof route for every target — polarization, the affine basis, the linear isometry of the direction subspace, `LinearIsometry.extend`, the affine assembly and uniqueness on the hull; the permuted monomial data and the branch theorem by `decide` and the reparametrization; the rigid motion, the marked set, finiteness and enumeration, or an exhibited map; the reading of the rungs into `A26-2`'s hypotheses — each recorded there as the freeze's reading and not as a finding; the hand-read branch predictions; the consumption of `A26-0` and `A26-1` by `A26-2` and of `A26-2` by `A26-3`; act 25's result note at its pinned blob, which records the two steps not reached and that the Fourier circle's rotations preserve its own metric; the merged modules.

#### The span module commit → `A26-0`

| question | answer for the span module commit → `A26-0` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: ran two name probes in the scratchpad pinning the library identifiers the freeze's route reads — `Module.Basis.span`, `Module.Basis.constr`, `Module.Basis.ext`, `LinearMap.mk₂`, `LinearMap.ext_basis`, `LinearMap.isometryOfInner`, `LinearIsometry.extend`, `LinearIsometry.toLinearIsometryEquiv`, `AffineIsometryEquiv.constVAdd` and `.trans`, `AffineMap.eqOn_affineSpan`, `innerₛₗ_apply_apply`, the polarization and norm-square identities; drafted Section B in the scratchpad and iterated it to a clean check, one fix to the basis-vector coercion and one simplification of the extension application; spliced Section B into the module; built with zero errors and zero warnings, sixteen results on the three standard axioms; checked the immutability contract against the module commit; committed the `A26-0` verdict commit. The proof is the freeze's own route, executed; it is universal in `E`, `S` and `f` and reads no property of the normalized set beyond the predicate `IsSurjIsometryOn`. No computation bearing on `A26-1`, `A26-2` or `A26-3` was run — no census, no coincidence, no count, no dimension, no candidate isometry — and the probes revealed only library names and signatures.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `A26-0` target with its three conjuncts and its hypothesis rule, the six-step extension route as the freeze's reading, the library provenance naming `LinearIsometry.extend`, `exists_affineIndependent`, `eqOn_affineSpan` and the polarization identity, and the statement that Mazur–Ulam is present and is not the lemma.

#### The span `A26-0` → `A26-1`

| question | answer for the span `A26-0` → `A26-1` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **YES — DISCLOSED** |
| **Q3 — UNAIDED REASONING** | **YES — DISCLOSED** |

**What the execution did in this span**, bearing on any target not yet closed at its end: ran the census — `A26-1`'s own execution, in `A26-1`'s own span — first as an exact computation outside the kernel in the scratchpad (the closed form of act 23's matrix checked against the displayed one; the dephased-core data of the `576` pairs; an independent sampled-membership control with no mismatch; the witness coordinate evaluated; the stabilizer's generators, the coset representatives, the generator words and the reparametrizations; a core coordinate and a separating parameter for each of the seventy-two ordered pairs of representatives), then in the kernel: the branch theorem through the named coordinate, the composition lemma, the four generator lemmas, the coset decomposition by `decide`, the generated coordinate and pair lemmas, the stabilizer words and the count theorem, iterated to zero errors and zero warnings; spliced Section C; built, one hundred fifty-seven results on the three standard axioms; checked the immutability contract; committed the `A26-1` verdict commit. **Q2, YES — DISCLOSED**: the census computation exposed, beyond what `A26-1`'s labels record, that each coordinate of a relabelled Fourier tuple at a unit parameter is `S z^m / 64` with `m ∈ {−1, 0, 1}` — so each relabelled circle is a round circle of the ambient real structure, its centre and radius readable from the monomial data — and the ranks of the real and imaginary Fourier-mode coefficient families (five and nine), and this bears on `A26-2`, open at the span's end; none of it was used to decide anything in this span, and it is recorded in §19 as an observation. **Q3, YES — DISCLOSED**: while deciding how far to certify the dimension, the executor briefly considered, without running anything, whether a rotation of a single circle could be a surjective isometry of the normalized set outside the family, and noted that the circles' cosine vectors are not mutually orthogonal (real rank five across nine circles), so that such a map would not preserve distances between circles; no conclusion was drawn and nothing was tested, and `A26-2` was opened from the freeze's routes and not from this remark. `A26-1-DIM` was not certified: the spanning-family half of its route was not attempted in the kernel, and the value computed outside the kernel is an observation and certifies nothing.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `A26-1` target with its two branches and their label discipline, the census route — the permuted monomial data, the coordinatewise coincidence reading, the reparametrizations `z' = ζ z` and `z' = ζ star z`, the count from representatives and the dimension from a spanning and an affinely independent family — as the freeze's reading, the hand-read prediction `SEVERAL` at medium strength, and act 25's `fourier_coord_uniform`, `mixedTriple_relabel2`, `relabel2_relabel2` and `relabel2_gramPhaseEquiv`.

#### The span `A26-1` → `A26-2`

| question | answer for the span `A26-1` → `A26-2` |
| --- | --- |
| **Q1 — INTENTIONAL** | **YES — DISCLOSED** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the gate — `A26-0-EXTENDS` and `A26-1-SEVERAL` open the positive route in the extension form, the negative route being available under either branch with no named candidate — and ran `A26-2`: in the kernel, the positive route's first step, the rigid motion, from the bridge and `A26-0`'s instantiation; and, as `A26-2`'s own execution in `A26-2`'s own span, **an exact computation outside the kernel of the isometries of the union of the nine circles** in the scratchpad — the classes lying on two distinct circles; the metric automorphisms of that finite set; for each, the per-circle parameter maps consistent with its marked points, filtered by the exact frame Gram constraints; the family's action on the union from its generators — with an independent floating-point control of its central claim and a countercontrol. **Q1, YES — DISCLOSED**: that computation was intended to reveal, and did reveal, facts bearing on `A26-2`'s outcome — the target of this span — as the freeze permits for this target alone ("a witness, if found, is admissible under the label's conditions"); what it found is recorded in §6 as the obstruction named and in §19 as an observation, and it earned no label: no witness of the frozen form exists, and the four-shape conclusion was not proved. Nothing bearing on `A26-3` was run, revealed or reasoned about; `A26-3`'s gate closes on this span's label. The marked-set step of the positive route was not obtained; no theorem quantifying over an isometry of the normalized space beyond the rigid-motion step was stated; `A26-2-P` was not attempted, the freeze naming no route.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `A26-2` target, its three hypotheses and four-shape conclusion, the positive route — the rigid motion, the marked set of intersection points characterized without circles, finiteness, enumeration — and the negative route as the freeze's readings, the frozen statement that no complete route to the four-shape conclusion is in hand, the hand-read prediction `UNDECIDED` at medium strength with the sign read positive at low strength, and the frozen obstruction of `A26-2-P`; and, from the earlier spans, `A26-0`'s and `A26-1`'s labels as earned and the two disclosed items of the span `A26-0` → `A26-1`.

#### The span `A26-2` → `A26-3`

| question | answer for the span `A26-2` → `A26-3` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the gate: `A26-2` reached `A26-2-UNDECIDED`, so `A26-3` is closed and has no verdict commit; no target remained open at this span's end. Wrote the packaging — this note, the `R7-CGR` clause, the `ROADMAP` sentence, the census entry, and the axiom table's remaining `#print axioms` lines in the module — and ran the lint, the release gate and the guard; no theorem of `A26-3` was stated or attempted, and nothing was run, revealed or reasoned about any transition family.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's gate rule for `A26-3`, its `NOT-EXECUTED` sentence, and the route it would have taken — `PreservesAdmissible` into the first hypothesis, `Reversible`'s second conjunct into the second, the isometry proposition into the third, `A26-2` at each `t` — reported here as the freeze's route and not executed.

### 3.7.1 The history-integrity statement, and the execution defects disclosed

**No commit on this branch was amended, reset, rebased over, cherry-picked over or force-pushed
away. There are no superseded SHAs.** Before certification this execution absorbed no later `main`.

**No execution defect is recorded on this chain.** The module's text at the packaging commit differs
from its text at the `A26-2` verdict commit by the addition of `#print axioms` lines for the one
hundred twenty-three generated lemmas of `A26-1`, so that the axiom table prints every named result,
and by nothing else; no theorem, no statement and no proof is touched. Four items of the freeze's
reading that the execution found otherwise are recorded as discrepancies in §21 and are not repaired.

### 3.8 The gate record (record 8)

| target | the label of the target before it, as earned | the gate, in its two forms | the route opened |
| --- | --- | --- | --- |
| `A26-1` | `A26-0-EXTENDS`, by `a26_0_affine_extension` at `913d70cc1eb9` | **executed whatever `A26-0`'s label** | the census |
| `A26-2` | `A26-0-EXTENDS` and `A26-1-SEVERAL`, by `a26_1_circle_census` at `7cc175bc04ee` | **the extension form: opened** — the positive route run; the negative route available under either branch, with no named candidate | the positive route, to its first step; no witness of the frozen form |
| `A26-3` | `A26-2-UNDECIDED`, the positive route having been run, at `5282eda2327d` | **the rigidity form: closed**: `A26-3-NOT-EXECUTED` | — |

## 4. `A26-0` — the restricted metric and the mandatory affine extension

**Outcome reached: `A26-0-EXTENDS`.**

> Every distance-preserving map of a subset of a finite-dimensional real inner-product space into
> that space agrees on the subset with an affine isometry of the whole space, and any two affine
> maps agreeing with it on the subset agree on the subset's affine hull, at evidence level 2 with
> nothing assumed of the map beyond distance preservation; applied to the normalized space at the
> single-carrier configuration, read as a subset of act 24's Euclidean feature space with the
> restricted ambient metric, every surjective isometry of it is the restriction of a rigid motion
> of that space carrying the normalized space onto itself. **This is a statement about one
> extension and the exact metric frozen**: it does not say any isometry is in any family, and it
> adopts nothing.

`a26_0_affine_extension` carries the freeze's (i), (ii) and (iii) as **three separate conjuncts**
of one statement, **the hypothesis on the map being distance preservation on the subset and nothing
else**, and each is reported separately:

| conjunct | statement, as the kernel carries it | proved by |
| --- | --- | --- |
| (i) the extension | for every real inner-product space `E` with `[FiniteDimensional ℝ E]`, every `S : Set E` and every `f : E → E` with `∀ x ∈ S, ∀ y ∈ S, dist (f x) (f y) = dist x y`, there is `g : E ≃ᵃⁱ[ℝ] E` with `∀ x ∈ S, g x = f x` | `exists_affineIsometryEquiv_of_dist_eq`: if `S` is empty, the identity; else a base point `p ∈ S`, the translated set `(· − p) '' S` and the translated map `v ↦ f (v + p) − f p`, which preserves real inner products on the translated set by `inner_sub_eq_of_dist_eq` (the polarization identity `⟪x, y⟫ = (‖x‖² + ‖y‖² − ‖x − y‖²)/2` applied to three distances); then `exists_linearIsometryEquiv_of_inner_eq` — `exists_linearIndependent` draws a basis `b` of the span of the translated set from it, `Module.Basis.span` and `Module.Basis.constr` build the linear map sending each basis vector to its image, inner products are preserved on the span by `LinearMap.ext_basis` on the two bilinear forms `⟪L x, L y⟫` and `⟪x, y⟫` (`LinearMap.mk₂`), `LinearMap.isometryOfInner` and `LinearIsometry.extend` extend to a linear isometry of `E`, `LinearIsometry.toLinearIsometryEquiv` makes it an automorphism (equal finite ranks), and the agreement with the map on every point `u` of the translated set follows from `‖L u − φ u‖² = 0`, the cross term `⟪L u, φ u⟫ = ⟪u, u⟫` by `Module.Basis.ext` on the two functionals `⟪L ·, φ u⟫` and `⟪·, u⟫`; the rigid motion is `constVAdd (−p)`, then the linear automorphism, then `constVAdd (f p)` |
| (ii) uniqueness on the affine hull | under the same hypotheses, for all `g g' : E →ᵃ[ℝ] E` with `∀ x ∈ S, g x = f x` and `∀ x ∈ S, g' x = f x`, `∀ x ∈ affineSpan ℝ S, g x = g' x` | `eqOn_affineSpan_of_agree`: `AffineMap.eqOn_affineSpan`; **uniqueness is asserted on the affine hull and nowhere else** |
| (iii) the instantiation | at `Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))`, for every `f` with `IsSurjIsometryOn (normalizedSet Γ₀) f`, there is `g : E ≃ᵃⁱ[ℝ] E` with `∀ x ∈ normalizedSet Γ₀, g x = f x` and `g '' normalizedSet Γ₀ = normalizedSet Γ₀`, `E` the ambient space `EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))` with its real structure | `exists_affineIsometryEquiv_of_isSurjIsometryOn`: (i) at `S = normalizedSet Γ₀` with the predicate's third conjunct, and `g '' S = S` from its first two conjuncts through `Set.image_congr` |

**The real structure was taken by the instance path the freeze reads**, `PiLp.innerProductSpace`
over `InnerProductSpace ℝ ℂ`, with `FiniteDimensional ℝ E` by `WithLp.instModuleFinite`, and the
**same** `dist`; the explicit identification with `EuclideanSpace ℝ (ι × Fin 2)` was not needed and
is not used. **No affinity, linearity, continuity or compactness was assumed of any map anywhere**:
(i) and (ii) quantify over an arbitrary `f : E → E` with distance preservation on `S` as their only
hypothesis on it, and (iii) over an arbitrary `f` with `IsSurjIsometryOn`; no statement of this
round assumes any map affine, linear, continuous or induced by a map on dilations, and no set is
assumed compact. Mazur–Ulam is invoked nowhere; `LinearIsometry.extend` is used as the freeze's route
reads it, on a linear isometry of a subspace.

## 5. `A26-1` — the census of the relabelled Fourier circles

**Outcome reached: `A26-1-SEVERAL`.**

> Some independent relabelling carries act 23's Fourier circle to a different set of classes at
> the single-carrier configuration: for one exhibited pair of permutations and one exhibited unit
> parameter, the relabelled Fourier tuple is equivalent under act 12's phase action to no Fourier
> tuple at any unit parameter, the inequivalence read through a named coordinate of act 24's
> feature map, at evidence level 2; so the normalized space is a union of at least two distinct
> circles. **This is a statement about the exact configuration frozen** and about nothing in its
> neighbourhood.

`a26_1_circle_census` **states the `SEVERAL` proposition**: `∃ (π τ : Equiv.Perm (Fin 4)) (z : ℂ),
star z * z = 1 ∧ ∀ z' : ℂ, star z' * z' = 1 → ¬ GramPhaseEquiv (fun i => (F(z) (π i)).submatrix τ τ)
(F(z'))`, with `F(z)` act 23's lambda written out at every mention. **The exhibited pair is
`(1, Equiv.swap 0 1)`** — the identity on the fibre labels, the transposition of the first two matrix
indices — **the exhibited parameter is `z = 1`**, and **the named coordinate is
`((0, 0, 2), (0, 0, 2))`** of act 24's feature map: `fourier_coord_002` evaluates it to the constant
`1 / 64` on the Fourier tuple at every parameter, `relabelled_coord_002` evaluates it to `−1 / 64` on
the relabelled tuple, and an equivalence would carry, by act 24's `mixedTriple_gauge`, the one value
onto the other. The label is the branch the theorem states, and no census outcome was read from
anything but this theorem.

**`A26-1-N`, the count — outcome `OBTAINED`, the number recorded being nine.**

> **The frozen `A26-1-N` `OBTAINED` sentence.**
> The relabelled Fourier circles at the single-carrier configuration are exactly the exhibited
> representatives, pairwise distinct as sets of classes, every relabelled circle equal to one of
> them, at evidence level 2, their number being the number recorded; it enters no label.

`a26_1_circle_count` certifies the count **from both sides**, over the list `R` of nine pairs of
permutations `(a, b)` with `a, b ∈ {1, Equiv.swap 2 3, Equiv.swap 1 2}` — a coset representative of
the subgroup `P` in `Equiv.Perm (Fin 4)` for the rows and one for the columns:

| clause | statement | proved by |
| --- | --- | --- |
| the list | `R.length = 9 ∧ R.Nodup` | `rfl` and `decide` |
| the non-coincidences | for all `r ∈ R`, `r' ∈ R` with `r ≠ r'`: `∃ z, star z * z = 1 ∧ ∀ z', star z' * z' = 1 → ¬ GramPhaseEquiv ((r) F(z)) ((r') F(z'))` — the circle of `r` is not contained in the circle of `r'` | the seventy-two lemmas `nc_0`–`nc_71`, one per ordered pair, each through one core coordinate `((0, 0, i), (0, 0, j))` with `i, j ∈ {1, 2, 3}`: `core_const_0`–`core_const_18` evaluate the coordinate on the `r'` circle at a symbolic unit parameter to a constant `±1 / 64` (the `z'`-exponents of the six entries cancelling, `linear_combination` against `star z' * z' = 1`), `core_val_0`–`core_val_31` evaluate it on the `r` circle at the exhibited parameter `1` or `Complex.I` to `±1 / 64` or `±Complex.I / 64`, and the two values differ |
| the coincidences | for all `π τ : Equiv.Perm (Fin 4)`, `∃ r ∈ R` with both inclusions: `∀ z` unit `∃ z'` unit, `GramPhaseEquiv ((π, τ) F(z)) ((r) F(z'))`, and `∀ z'` unit `∃ z` unit, the same | `perm_decomp` (`decide`): every permutation is `a.trans p` with `a` a representative and `p ∈ P`, `P` the order-eight subgroup `{1, swap 1 3, (swap 0 1).trans (swap 2 3), …}`; `pred_stab`: every element of `P × P` carries the Fourier circle onto itself as a set of classes, both inclusions — from the four generator lemmas `stab_row_swap13`, `stab_col_swap13` (the relabelled tuple **equals** the Fourier tuple at `−z`), `stab_row_double`, `stab_col_double` (phase-equivalent to the Fourier tuple at `star z`, with the column phases `(1, star z, −1, −star z)` and `(1, 1, 1, 1)`), lifted to the words in the generators by `circle_coincide_trans` (act 25's `relabel2_relabel2` and `relabel2_gramPhaseEquiv` and act 12's transitivity); then act 25's composition law reads `(a.trans p, b.trans q) F(z)` as `(a, b)` applied to `(p, q) F(z)` |

The count is `9 = 576 / 64`, the stabilizer of the Fourier circle being `P × P`; it enters no label.

**`A26-1-DIM`, the dimension — outcome `UNDECIDED`, with the step named.**

> **The frozen `A26-1-DIM` `UNDECIDED` sentence.**
> The dimension of the real affine hull of the normalized space at the single-carrier
> configuration is undecided in this round, with the step named; any value stated is an
> observation and certifies nothing; it enters no label.

The step named: **the spanning-family half of the freeze's route was not certified** — a family of
`n` vectors with every difference of points of the normalized set, over all `576` relabellings and
all unit parameters, in its span; the affinely independent family was not certified either, the
lower bound alone earning nothing. The definition budget admits no declaration of a coordinate
vector, a monomial datum or a Fourier-mode coefficient family through which the spanning statement
could be written and checked over the `4096` coordinates, and the execution did not attempt it
inline. No theorem names a dimension; **the value computed outside the kernel is recorded in §19 as
an observation and certifies nothing.**

**No map is read as a symmetry, an antiunitary map, a time reversal or a dynamics.** The exhibited
pair is `fun i => (G (1 i)).submatrix (Equiv.swap 0 1) (Equiv.swap 0 1)` and nothing else; the
parameter `z` of the Fourier family is a parameter of a frozen tuple and not a time, a flow or a
generator.

## 6. `A26-2` — the classification of the surjective isometries at the single carrier

**Outcome reached: `A26-2-UNDECIDED`, the positive route having been run.**

> Whether every surjective isometry of the normalized space at the single-carrier configuration
> belongs to the finite family is undecided in this round, with the obstruction named
> specifically — the step of the route that did not close and what would settle it. Neither the
> rigidity label nor its negation is claimed; no isometry outside the family is exhibited, and
> the absence of a proof is not a counterexample.

**The gate opened the positive route in its extension form**, `A26-0-EXTENDS` and `A26-1-SEVERAL`
both earned, and the negative route was available under the `SEVERAL` branch with no named
candidate. **The positive route was run**, `A26-0`'s extension and `A26-1`'s census consumed, and the
steps reached are these:

| step | outcome | named results, or the obstruction |
| --- | --- | --- |
| 1 — the rigid motion | **closed** | `rigid_motion_of_tuple_isometry`: for every `φ` on tuples with the three hypotheses — realizability preserved, surjectivity on classes, isometry on realizable tuples with `d` bound to act 24's equation — there is `g : E ≃ᵃⁱ[ℝ] E` with `g (featureVec G) = featureVec (φ G)` on every realizable `G` and `g '' normalizedSet Γ₀ = normalizedSet Γ₀`: the bridge `bridge_of_tuple_isometry` composed with `A26-0`'s (iii) |
| 2 — the marked set | **not obtained** | the freeze's candidate — the points lying on two distinct circles, characterized inside the set by their distance profile — was examined and does not determine the rigid motion: the classes lying on two distinct circles are **six**, **two on each circle**, at the parameters `1` and `−1` of each circle's own parametrization (an exact computation outside the kernel, recorded in §19), and two points fix a circle's isometries only up to the reflection through them; the set does not affinely span the hull either, six points spanning at most five dimensions; no other marked set was found; **what would settle it** is a kernel proof that every rigid motion carrying the normalized set onto itself is determined by finite data the set itself marks, or a different route from the rigid motion to the four-shape conclusion |
| 3 — finiteness | **not reached** | conditional on step 2 |
| 4 — enumeration | **not reached** | conditional on step 3 |

**The label is earned by the step not reached and by nothing else**: no theorem
`a26_2_rigid_single` exists, no theorem `a26_2_not_rigid_single` exists, **no isometry outside the
family is exhibited in the kernel, and the absence of a proof is not a counterexample**. The
negative route found no witness of the frozen form: **the frozen `NOT-RIGID` label requires one
exhibited realizable class sent to a class inequivalent to its image under every member of the family**,
and the exact computation of §19 found that for every surjective isometry of the union of the nine
circles and every class, some member of the family agrees with that isometry on that class's
circle — so no class of the frozen form exists for any candidate, and none is recorded; what the
computation found about the isometries as a whole is an observation, stated once in §19, and earns
nothing. `rigid_motion_of_tuple_isometry` is a step of the route and earns no label.

**The three hypotheses are the whole of what the classification assumed** — realizability preserved,
surjectivity on classes, isometry on realizable tuples, as the freeze displays them — and **no
linearity, affinity, continuity or compactness was assumed**: the rigid-motion step assumes nothing
of `φ` beyond the three, and the extension it consumes assumes nothing of any map beyond distance
preservation. Descent was never a hypothesis. **No exhibited map exists, and so none is named by a
formula and none is called a symmetry, an antiunitary map, a time reversal or a dynamics.**

**`A26-2-P`, the product cell — outcome `UNDECIDED`**, not attempted, the realizable classes there
not being described:

> **The frozen `A26-2-P` `UNDECIDED` sentence.**
> Whether every surjective isometry of the normalized space at the product configuration belongs
> to the finite family is undecided in this round, the realizable classes there not being
> described and nothing being imported to describe them. Neither label is claimed.

`A26-2-P` enters no label.

> **THE CLAUSE, carried at this mention — the classification, where the family is or is not all of the isometries.**
> Act 26 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 7. `A26-3` — the prefix-constrained corollary at the single carrier

**Outcome reached: `A26-3-NOT-EXECUTED`**, by the gate.

> The corollary for transition families was not executed, the classification of the isometries
> not having reached its rigidity label; no sentence of this round reports anything about it.

The route the corollary would have taken is the freeze's and is reported here as the freeze's route
and not as anything executed: `PreservesAdmissible` read into the first hypothesis of `A26-2`,
`Reversible`'s second conjunct into the second, the isometry proposition into the third, and `A26-2`
applied at each `t`. No theorem `a26_3_prefix_isometry_single` exists, no statement of this round
names `ProperAt`, `PropagatesFrom`, `EvolvesTotally`, `PreservesAdmissible`, `Reversible` or
`LadderConds`, and no partial execution of the closed target is reported as anything.

## 8. The outcome vector, and what it is not

The headline is row 4 of the freeze's outcome-vector table, selected verbatim and reported in no
other wording, and it is stated once, at the head of this note. **No verdict was inferred from
another beyond the consumptions the freeze places.** Each of the four labels is earned by its own
target's theorems or by the gate and by nothing else: `A26-0`'s by `a26_0_affine_extension`,
`A26-1`'s by `a26_1_circle_census`, `A26-2`'s by the recorded non-attainment of step 2 of its
positive route with no witness of the frozen form, `A26-3`'s by the gate rule; the consumptions the
freeze places are `A26-0` and `A26-1` in `A26-2`'s positive route, which consumed them and did not
close, and `A26-2` in `A26-3`, which was not executed. The gate record is §3.8. No single-label
headline, no summary label and no combination label exists for this round.

## 9. The route-authorization matrix, as honoured

**The route-authorization matrix is honoured**: each construction was used for its own target and
for nothing else, no fact learned during a later target's work was assigned to an earlier target, and
no alternative was substituted for a named one.

| construction or route | used for | used for nothing else |
| --- | --- | --- |
| polarization on the subset, the basis drawn from it, the linear isometry of the span, `LinearIsometry.extend`, the affine assembly, uniqueness on the affine hull; the instantiation at `normalizedSet Γ₀` | `A26-0` | consumed by `A26-2`'s route as `A26-0`'s verdict |
| the coordinates of a relabelled Fourier tuple as permuted monomials; the non-coincidence of a relabelled circle with `C₀` through a named coordinate; the count through the stabilizer and the representatives | `A26-1` | consumed by `A26-2`'s route as `A26-1`'s verdict; the dimension's families not obtained |
| `A26-0`'s rigid motion and `A26-1`'s census consumed; the marked set; finiteness; enumeration; or an exhibited map with the three hypotheses and a separated class | `A26-2` | step 1 obtained, step 2 not; no witness of the frozen form |
| `L1`, `L3s` and isometry read into `A26-2`'s hypotheses; `A26-2` consumed | `A26-3` | not executed |
| the shared lemmas of the module commit, the bridge among them | consumed | answer no target by themselves |

**The execution order `A26-0` → `A26-1` → `A26-2` → `A26-3` was followed**, one verdict commit per
executed target, the gate read between each, no target executed out of order, and no closed target's
route attempted for information.

## 10. The scope boundary as honoured

**Nothing here derives, recognises or approaches quantum evolution**, and nothing here says that any
generator, the family, the normalized space, any circle or any isometry is, resembles, approximates or
points toward it, a quantum symmetry, an antiunitary map, a time reversal or unitarity; no continuity
in time, composition in time, semigroup law, generator or one-parameter structure is introduced, and
the parameter `z` of the Fourier family is a parameter of a frozen tuple and not a time, a flow or a
generator, the rotations and reflections of any circle being no dynamics.

**No theorem is attributed to the literature, none of its theorems is consumed, and Mazur–Ulam is
invoked nowhere; no domain and no metric is substituted.** The two strands of literature the freeze
names are cited by it as the provenance of the route and of the shape of the question; `A26-0` is this round's theorem,
proved here from the library's linear algebra, and `A26-2`'s label is earned by the step not reached
and not by any imported fact. Every statement of this round is for the normalized space with the
restricted ambient metric.

**Every earlier act's historical verdicts stand unchanged**, acts 12 through 25's: act 12's
classification, act 21's census, `SIOP-YES` and `L-WIDE`, act 22's three verdicts, act 23's four, act
24's twelve isometry verdicts and seven cells, and act 25's four labels with `ISO1-R`, `ISO2-P`,
`ISO3-L`, `ISO3-P` and `ISO4-P`, none closed by anything here; act 25's `ISO3-UNDECIDED` stands as
earned, this round settling nothing of it and recording its own `A26-2-UNDECIDED` at the same
configuration. **Act 16's cancellation cell and the threading question are untouched in either
direction.** **Act 18's `D`-axis is untouched.** **Act 10's anchor-axis reclassification is
untouched.** Act 14's four carriers are not read and no carrier is adopted as the physical one.

**No generator outside the frozen four was tested, no normalized space or geometry outside the frozen
one, no metric other than the restricted ambient one, no configuration outside the single carrier,
and no equivalence outside the frozen quotient list was used in any verdict.** No fifth generator, no
second normalized space, geometry or metric, no further equivalence, rung, configuration or control,
no description of the product configuration's classes and no strengthening of a merged theorem was
discovered or executed; what the anti-expansion rule collected is in §19.

## 11. The non-adoption clause, carried verbatim at each mention

**THE CLAUSE is carried three times in this note** — at the headline, at the classification, and
here — each carriage opening with its own naming line and carrying the complete frozen clause, from
"Act 26 classifies" to "approaches quantum evolution.". Where a frozen byte-fixed sentence carries
the clause's substance in its own wording — the status rule's sentences and the `P0` row's sentence —
no quotation is inserted inside the quotation, as the freeze directs. **No law is adopted, endorsed or
given physical status by surviving, and the family, the normalized space and every map named are
adopted as nothing**: not as a symmetry group, not as a selector, not as a principle, not as the
physical geometry.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 26 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 12. The frozen `P0` sentence for the case reached

**Case A** — row 4 with the cell as predicted — is the case reached, with **one variable clause
replaced** as the freeze's substitution table directs for `A26-1-DIM` `UNDECIDED`: the clause "their
number and the dimension of their affine hull recorded at kernel level" is replaced by "their number
recorded at kernel level and the dimension of their affine hull recorded undecided". Every other
clause is as written for Case A. It is appended, verbatim, to the `P0` row of
`verification/ROADMAP.md` after act 25's sentence in the same cell, and the row's label stays
**OPEN** and two-part:

> Act 26 tests, in one gated round with four separately frozen targets, whether every distance-preserving map of the normalized space at the single-carrier configuration, read as a subset of act 24's Euclidean feature space with the restricted ambient metric, extends to an affine isometry of that space, how the relabelled Fourier circles of act 25's description sit in the quotient and what real affine hull they span, whether every surjective isometry of that normalized space belongs to act 25's finite family or a kernel-certified isometry lies outside it, and whether every transition family satisfying the conditions before naturality and isometry acts on classes as a member of it. Every distance-preserving map of the normalized space extends to an affine isometry of the ambient space, uniquely on the affine hull, with nothing assumed of the map beyond distance preservation. Some relabelling carries the Fourier circle to a different set of classes, so the normalized space is a union of several distinct circles, their number recorded at kernel level and the dimension of their affine hull recorded undecided. Whether every surjective isometry of the normalized space at that configuration belongs to the family is recorded undecided, with the step named; no isometry outside the family is exhibited, and the absence of a proof is not a counterexample. The corollary for transition families was not executed. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no verdict is inferred from another beyond the consumptions the freeze places; no condition is adopted; the family and the normalized space are named objects of test and are not adopted as the physical ones; no map is read as a symmetry, an antiunitary map, a time reversal or a dynamics; nothing is asserted at the product configuration beyond its recorded undecided cell, and nothing at any other configuration; acts 12 through 25's own verdicts stand exactly as they state them; nothing here introduces continuity, composition in time or a generator; and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

## 13. What no outcome licenses, and the status rule as honoured

The freeze's twenty-two forbidden sentences are honoured in terms. No sentence of this round says that
any generator, the family, any isometry or any map is, resembles, approximates or points toward a
quantum symmetry, an antiunitary map, a time reversal, unitarity, a dynamics or quantum evolution (1);
none says the family is the physical symmetry group, the geometry the physical geometry, that the
isometries select or that the normalized space is a state space (2), the non-adoption clause
governing; no target's verdict is inferred from another's beyond the placed consumptions (3); no
positive label is claimed from the absence of a counterexample, from a route that failed to close, or
from anything but the named route (4); the family is not said to be complete because no other
isometry was found, `A26-2` being undecided (5); the census outcome is read from
`a26_1_circle_census` and from nothing else (6); the count nine is stated as the kernel certifies it,
and the dimension is stated as no finding, the value computed outside the kernel being recorded as an
observation (7); no negative label is read from `fourier_circle_metric` or from any parameter (8);
no earlier act's verdict, witness or obstruction is rewritten or reinterpreted, act 25's
`ISO3-UNDECIDED`, act 24's `b` and act 21's `L-FAMILY` obstruction standing as they state them (9);
the isometry group of no space is stated beyond the label earned, and nothing is stated of the product
configuration, the whole tuple space, the whole feature image or the Fourier circle alone (10); no
isometry is assumed linear or affine and Mazur–Ulam is invoked nowhere, the extension being `A26-0`'s
theorem (11); the metric is identified with no named geometry of any other theory and no statement is
made for a path metric (12); nothing is said about the threading, the cross-time representative, act
16's cell, act 14's carriers, act 18's `D`-axis, act 10's anchor axis, Track I, Source B or C, or the
substratum rounds (13); `P0` is not closed and neither is either of its parts (14); no merged statement
is strengthened, superseded or extended (15); no continuity, smoothness, generation, one-parameter
structure or composition in time is imported, and no rotation or reflection of a circle is called a
dynamics (16); OI and QM are not said to be inequivalent (17); the generator list is not said to be
exhaustive, the family is not called the only natural family, and no enlargement of it is proposed
(18); the headline is the vector and no single label (19); nothing is said about the realizable
classes at the product configuration beyond the recorded obstruction (20); no verdict about a
substituted domain is reported as a verdict of this round, the observation of §19 about the union of
the nine circles being an observation and earning nothing (21); and the module carries the three
definitions with their frozen statements and no other, none described as a convenience (22). Every
target is reported with its frozen sentence, and no outcome reached its wording by any other route.

## 14. The relation to acts 12, 13, 17, 18, 20, 21, 22, 23, 24 and 25

| act | what is consumed | at what strength |
| --- | --- | --- |
| act 7 | `AdmissibleDilationAt`, the readback convention, `D4b` negative, `D5` NOT CERTIFIED | merged; named in no statement of this round |
| act 12 | `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `fibreGram_apply`, `sh1_necessity`, `sh1_sufficiency`, `gramPhaseEquiv_cross_invariant` | merged; none re-proved; no merged statement enlarged |
| act 13 | its `P0` threading sentence | untouched; named as what this round does not touch |
| act 17 | `GramTrajEquiv` named in the frozen quotient list; `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, `gramPhaseEquiv_trans` | merged; `GramTrajEquiv` used in no verdict |
| act 18 | `ProperAt`, `PropagatesFrom` | merged; named in no statement of this round |
| act 20 | `RelabelTransition` | merged; named in no statement of this round |
| act 21 | the ladder as the declarations of its merged module, its single-carrier configuration, the frozen quotient list, the attestation set, THE CLAUSE with "Act 21" read as "Act 26" | merged; the ladder consumed unrestated and named in no statement, `A26-3` not being executed; act 21's verdicts untouched |
| act 22 | its three verdicts | untouched |
| act 23 | `hadamard_z_admissible` and the Fourier matrix `H z` as the lambda its merged statements carry | merged; consumed as landed through act 25's theorems |
| act 24 | `mixedTriple` and the frozen geometry equation; `dist_eq_norm_toLp`, the bridge to the `ℓ²` norm; `geo1_separation_single`, `geo1_equiv_of_zero_single`, `mixedTriple_gauge`; its twelve verdicts and its cells | merged; consumed as landed; its undecided cells not closed |
| act 25 | the family, its four generators, the transpose relation and the four-shape conclusion, consumed verbatim; `iso1_family_acts`, `relabel2_relabel2`, `relabel2_gramPhaseEquiv`, `iso2_classes_single` in both directions, `fourier_coord_uniform`, `fibreGram_unique`, `mixedTriple_relabel2`; its four labels and its cells; its §7 table naming the two steps not reached | merged; consumed as landed; `ISO3-UNDECIDED` standing as earned, this round recording its own undecided label at the same configuration and revising nothing |

**No merged label is revised.** **A merged statement is not enlarged by being consumed.** The
direct-branch statement is carried unchanged: `D4a` positive on the direct branch; `T1` **necessary,
not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what fraction of OI
lies in the direct sector**; `D5` NOT CERTIFIED.

## 15. The definition budget

**Three slots were budgeted, and exactly three definitions were introduced, each with its frozen
statement**: `featureVec`, `normalizedSet` and `IsSurjIsometryOn`, displayed in §3.1 as the module
carries them; **none was omitted**. The module carries no other top-level `def`, and no `abbrev`,
`structure`, `class`, `instance`, `axiom` or `opaque`, at any commit; the four generators, the
transpose relation, the geometry, the Fourier matrix, the circles, the list of representatives, the
stabilizer and the permutations are bound variables or written-out expressions in the statements that
need them, the invariant family is act 24's `mixedTriple` consumed, and every rung is act 21's
declaration, named in no statement. **One hundred fifty-eight named results.**

## 16. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants**, with `B = e0be0ab6dca7b6661a008a9f5e1f3a29ea736003`, certified through the validator's
prospective path by the one keyed call `_si2_authority('CGR', tag='R7-CGR')`. The question is asked
of the real `pull_request.head.sha` in pull-request continuous integration and of `HEAD` otherwise,
**never** of the synthetic merge commit; an unresolvable head **fails closed** with no fallback; the
check excludes pre-freeze side history by requiring every commit in `git rev-list H ^B` to be itself
a descendant of `B`; and the guard recovers whatever history it needs and fails if recovery fails.

**The validator's classification of `CGR`**: `EXECUTION` at every head of the execution, printed by
the `R7-CGR` clause from the packaging commit on and read at `E` from the continuous-integration log
of the certification of record; `LANDED-PENDING-PIN` at `L`, permitted there and failing every
descendant as seal pending; `ARCHIVED` from `P`, which writes `verification/seals/CGR.json` with its
three fields and removes the `CGR` entry from the prospective declaration, and touches nothing else.

**The supersession table is empty and is honoured as empty**: no contract of any closed round was
edited, at any commit of this branch; at the stage-A commit and at every later head every closed
round's guard classifies its own record and passes.

**`SI-3`'s standing zero-legacy-statement contract holds at every head**: `_SI2_LEGACY_RE` finds zero
assignment statements in the guard file at `B` and at every commit of this branch, and no name
matching `_CGR_(BASE|SEALED_HEAD|MERGE)` exists anywhere.

### The ten preconditions, each at its scope, as the base check reported them at `M` and at `B`

The freeze's machine-checkable block carries thirty `frozen-blob` lines and twenty-one rows; the base
check reported `OK (mode M, 21 row(s), no failure)` at the candidate merge of pull request #698 on run
35496392690 and `OK (mode B, 21 row(s), no failure)` at `B` on run 35499317330.

| # | scope | precondition | result |
| --- | --- | --- | --- |
| 1 | `D` | the names were free when chosen | **PASS** — rows `d1-tag-free`, `d1-stem-free`, `d1-bare-free`, `d1-module-free`, `d1-dir-free`, `d1-act-free`, `d1-target-free`, `d1-theorem-prefix-free`: measured at `D`, recorded, `D` an ancestor of `B` |
| 2 | `D` | the seals tree at `D` is the pinned one | **PASS** — row `d2-seals-tree`, `08b37f66c35dae909b8cd820ca5705f66f4015b6`, thirty records |
| 3 | `D` | the guard at `D` is green and carries no legacy constant | **PASS** — eighty-nine tags on run 35492863856; zero legacy statements |
| 4 | `D → B` | `D` is an ancestor of `B` | **PASS** — row `db4-ancestor` |
| 5 | `D → B` | the blobs this round consumes are unchanged | **PASS** — thirty `frozen-blob` lines, each matched at `M` and at `B` |
| 6 | `B` | no act 26 execution object exists | **PASS** — rows `b6-guard-clean`, `b6-no-record`, `b6-no-module`, `b6-dir-control-plane-only` |
| 7 | `B` | no round is executing at `B` | **PASS** — row `b7-no-prospective`, `_MANIFEST_PROSPECTIVE = {}` at `B` |
| 8 | `B` | acts 24 and 25 are sealed at `B` | **PASS** — rows `b8-ogs-sealed`, `b8-ogc-sealed`, `b8-ogs-guard` and `b8-ogc-guard` |
| 9 | `B` | act 25's module is wired | **PASS** — row `b9-import-ogc` |
| 10 | `B` | this control plane is in the tree at its path | **PASS** — row `b10-self-present`, and the blob verified by `git hash-object` as the first act |

**No sibling lane's merge is a precondition of this round**, and none was waited for.

**The claim is scoped to the repository record.**

## 17. The axiom table — one line per named result

| named result | axioms |
| --- | --- |
| `featureVec_ofLp` | `[propext, Classical.choice, Quot.sound]` |
| `dist_featureVec` | `[propext, Classical.choice, Quot.sound]` |
| `featureVec_gauge` | `[propext, Classical.choice, Quot.sound]` |
| `gramPhaseEquiv_of_featureVec_eq` | `[propext, Classical.choice, Quot.sound]` |
| `featureVec_mem_normalizedSet` | `[propext, Classical.choice, Quot.sound]` |
| `relabelled_fourier_mem_normalizedSet` | `[propext, Classical.choice, Quot.sound]` |
| `normalizedSet_eq_iUnion` | `[propext, Classical.choice, Quot.sound]` |
| `featureVec_image_eq` | `[propext, Classical.choice, Quot.sound]` |
| `bridge_of_tuple_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `tuple_isometry_of_bridge` | `[propext, Classical.choice, Quot.sound]` |
| `inner_sub_eq_of_dist_eq` | `[propext, Classical.choice, Quot.sound]` |
| `exists_linearIsometryEquiv_of_inner_eq` | `[propext, Classical.choice, Quot.sound]` |
| `exists_affineIsometryEquiv_of_dist_eq` | `[propext, Classical.choice, Quot.sound]` |
| `eqOn_affineSpan_of_agree` | `[propext, Classical.choice, Quot.sound]` |
| `exists_affineIsometryEquiv_of_isSurjIsometryOn` | `[propext, Classical.choice, Quot.sound]` |
| `a26_0_affine_extension` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_coord_002` | `[propext, Classical.choice, Quot.sound]` |
| `relabelled_coord_002` | `[propext, Classical.choice, Quot.sound]` |
| `a26_1_circle_census` | `[propext, Classical.choice, Quot.sound]` |
| `circle_coincide_trans` | `[propext, Classical.choice, Quot.sound]` |
| `stab_row_swap13` | `[propext, Classical.choice, Quot.sound]` |
| `stab_col_swap13` | `[propext, Classical.choice, Quot.sound]` |
| `stab_row_double` | `[propext, Classical.choice, Quot.sound]` |
| `stab_col_double` | `[propext, Classical.choice, Quot.sound]` |
| `perm_decomp` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_0` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_1` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_2` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_3` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_4` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_5` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_6` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_7` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_8` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_9` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_10` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_11` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_12` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_13` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_14` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_15` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_16` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_17` | `[propext, Classical.choice, Quot.sound]` |
| `core_const_18` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_0` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_1` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_2` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_3` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_4` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_5` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_6` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_7` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_8` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_9` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_10` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_11` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_12` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_13` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_14` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_15` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_16` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_17` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_18` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_19` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_20` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_21` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_22` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_23` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_24` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_25` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_26` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_27` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_28` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_29` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_30` | `[propext, Classical.choice, Quot.sound]` |
| `core_val_31` | `[propext, Classical.choice, Quot.sound]` |
| `nc_0` | `[propext, Classical.choice, Quot.sound]` |
| `nc_1` | `[propext, Classical.choice, Quot.sound]` |
| `nc_2` | `[propext, Classical.choice, Quot.sound]` |
| `nc_3` | `[propext, Classical.choice, Quot.sound]` |
| `nc_4` | `[propext, Classical.choice, Quot.sound]` |
| `nc_5` | `[propext, Classical.choice, Quot.sound]` |
| `nc_6` | `[propext, Classical.choice, Quot.sound]` |
| `nc_7` | `[propext, Classical.choice, Quot.sound]` |
| `nc_8` | `[propext, Classical.choice, Quot.sound]` |
| `nc_9` | `[propext, Classical.choice, Quot.sound]` |
| `nc_10` | `[propext, Classical.choice, Quot.sound]` |
| `nc_11` | `[propext, Classical.choice, Quot.sound]` |
| `nc_12` | `[propext, Classical.choice, Quot.sound]` |
| `nc_13` | `[propext, Classical.choice, Quot.sound]` |
| `nc_14` | `[propext, Classical.choice, Quot.sound]` |
| `nc_15` | `[propext, Classical.choice, Quot.sound]` |
| `nc_16` | `[propext, Classical.choice, Quot.sound]` |
| `nc_17` | `[propext, Classical.choice, Quot.sound]` |
| `nc_18` | `[propext, Classical.choice, Quot.sound]` |
| `nc_19` | `[propext, Classical.choice, Quot.sound]` |
| `nc_20` | `[propext, Classical.choice, Quot.sound]` |
| `nc_21` | `[propext, Classical.choice, Quot.sound]` |
| `nc_22` | `[propext, Classical.choice, Quot.sound]` |
| `nc_23` | `[propext, Classical.choice, Quot.sound]` |
| `nc_24` | `[propext, Classical.choice, Quot.sound]` |
| `nc_25` | `[propext, Classical.choice, Quot.sound]` |
| `nc_26` | `[propext, Classical.choice, Quot.sound]` |
| `nc_27` | `[propext, Classical.choice, Quot.sound]` |
| `nc_28` | `[propext, Classical.choice, Quot.sound]` |
| `nc_29` | `[propext, Classical.choice, Quot.sound]` |
| `nc_30` | `[propext, Classical.choice, Quot.sound]` |
| `nc_31` | `[propext, Classical.choice, Quot.sound]` |
| `nc_32` | `[propext, Classical.choice, Quot.sound]` |
| `nc_33` | `[propext, Classical.choice, Quot.sound]` |
| `nc_34` | `[propext, Classical.choice, Quot.sound]` |
| `nc_35` | `[propext, Classical.choice, Quot.sound]` |
| `nc_36` | `[propext, Classical.choice, Quot.sound]` |
| `nc_37` | `[propext, Classical.choice, Quot.sound]` |
| `nc_38` | `[propext, Classical.choice, Quot.sound]` |
| `nc_39` | `[propext, Classical.choice, Quot.sound]` |
| `nc_40` | `[propext, Classical.choice, Quot.sound]` |
| `nc_41` | `[propext, Classical.choice, Quot.sound]` |
| `nc_42` | `[propext, Classical.choice, Quot.sound]` |
| `nc_43` | `[propext, Classical.choice, Quot.sound]` |
| `nc_44` | `[propext, Classical.choice, Quot.sound]` |
| `nc_45` | `[propext, Classical.choice, Quot.sound]` |
| `nc_46` | `[propext, Classical.choice, Quot.sound]` |
| `nc_47` | `[propext, Classical.choice, Quot.sound]` |
| `nc_48` | `[propext, Classical.choice, Quot.sound]` |
| `nc_49` | `[propext, Classical.choice, Quot.sound]` |
| `nc_50` | `[propext, Classical.choice, Quot.sound]` |
| `nc_51` | `[propext, Classical.choice, Quot.sound]` |
| `nc_52` | `[propext, Classical.choice, Quot.sound]` |
| `nc_53` | `[propext, Classical.choice, Quot.sound]` |
| `nc_54` | `[propext, Classical.choice, Quot.sound]` |
| `nc_55` | `[propext, Classical.choice, Quot.sound]` |
| `nc_56` | `[propext, Classical.choice, Quot.sound]` |
| `nc_57` | `[propext, Classical.choice, Quot.sound]` |
| `nc_58` | `[propext, Classical.choice, Quot.sound]` |
| `nc_59` | `[propext, Classical.choice, Quot.sound]` |
| `nc_60` | `[propext, Classical.choice, Quot.sound]` |
| `nc_61` | `[propext, Classical.choice, Quot.sound]` |
| `nc_62` | `[propext, Classical.choice, Quot.sound]` |
| `nc_63` | `[propext, Classical.choice, Quot.sound]` |
| `nc_64` | `[propext, Classical.choice, Quot.sound]` |
| `nc_65` | `[propext, Classical.choice, Quot.sound]` |
| `nc_66` | `[propext, Classical.choice, Quot.sound]` |
| `nc_67` | `[propext, Classical.choice, Quot.sound]` |
| `nc_68` | `[propext, Classical.choice, Quot.sound]` |
| `nc_69` | `[propext, Classical.choice, Quot.sound]` |
| `nc_70` | `[propext, Classical.choice, Quot.sound]` |
| `nc_71` | `[propext, Classical.choice, Quot.sound]` |
| `pred_row_swap13` | `[propext, Classical.choice, Quot.sound]` |
| `pred_col_swap13` | `[propext, Classical.choice, Quot.sound]` |
| `pred_row_double` | `[propext, Classical.choice, Quot.sound]` |
| `pred_col_double` | `[propext, Classical.choice, Quot.sound]` |
| `pred_one` | `[propext, Classical.choice, Quot.sound]` |
| `pred_row` | `[propext, Classical.choice, Quot.sound]` |
| `pred_col` | `[propext, Classical.choice, Quot.sound]` |
| `pred_stab` | `[propext, Classical.choice, Quot.sound]` |
| `a26_1_circle_count` | `[propext, Classical.choice, Quot.sound]` |
| `rigid_motion_of_tuple_isometry` | `[propext, Classical.choice, Quot.sound]` |

No `sorry`, no `native_decide`, no added axiom; `lake build OIBridge.OrbitGeometryRigidity` completes
with zero errors and zero warnings at every verdict commit and at the packaging commit. `decide` is
used over `Equiv.Perm (Fin 4)` and lists of permutations, as the freeze permits.

## 18. The predictions, reported against their outcomes

| target | prediction | outcome | reported as |
| --- | --- | --- | --- |
| `A26-0` | `A26-0-EXTENDS`, medium | `A26-0-EXTENDS` | **as predicted** |
| `A26-1` | `A26-1-SEVERAL`, medium | `A26-1-SEVERAL` | **as predicted** |
| `A26-1-N` | obtained, low, no value predicted | `OBTAINED`, nine | **as predicted**; enters no label |
| `A26-1-DIM` | obtained, low, no value predicted | `UNDECIDED`: the spanning family not certified | **not as predicted**; enters no label |
| `A26-2` | `A26-2-UNDECIDED` in the several-circles branch, medium for the label; the sign read positive at low strength | `A26-2-UNDECIDED`, the positive route run, step 1 closed, step 2 not obtained; the sign neither confirmed nor refuted in the kernel — the observation of §19 bears on it and certifies nothing | **as predicted** for the label; the sign untested in the kernel |
| `A26-2-P` | `UNDECIDED`, high | `A26-2-P-UNDECIDED` | **as predicted**; enters no label |
| `A26-3` | `A26-3-NOT-EXECUTED`, medium, following `A26-2` | `A26-3-NOT-EXECUTED` | **as predicted** |

## 19. The observations for a later round, stated once and narrowly

**No observation for the product configuration is recorded**: `A26-2` did not reach its positive
label, so what a positive `A26-2` would have supplied to a later round that freezes the product
configuration's description is not supplied, and nothing about the product configuration is asserted
beyond the recorded undecided cell.

**What the execution found outside the kernel, recorded as observations that certify nothing.** Each
item below is the output of an exact computation in the execution's scratchpad — Gaussian-integer and
rational arithmetic over the feature coordinates, with the controls named — and is not a finding of
this round, not a label, not a value the kernel certifies, and not a step of any route; failure rule
1 and forbidden sentence 7 govern its status, and it is stated here once so that a later freeze can
take it up or discard it.

1. **The coordinates.** Every coordinate of `Ψ ((π, τ) F(z))` at a unit parameter is `S z^m / 64`
   with `m ∈ {−1, 0, 1}`, the three exponents of `z` and of `star z` never both exceeding one in a
   coordinate; so each relabelled circle is, in the ambient real structure, a round circle with a
   centre, a cosine vector and a sine vector of integer entries over `64`, all nine of one radius.
2. **The affine hull.** The real coefficient families of the nine circles' modes have rank five
   (the real part: the centres' differences and the cosine vectors) and rank nine (the imaginary
   part: the sine vectors), two large primes agreeing; **the value fourteen for the dimension of the
   real affine hull is an observation and certifies nothing**, `A26-1-DIM` being undecided.
3. **The marked set.** The classes lying on two distinct circles are six, two on each circle, at the
   parameters `1` and `−1` of each circle; no class lies on a second circle at a parameter off the
   fourth roots of unity (a sampled control found none), and the metric automorphism group of the
   six points has order seventy-two and is the family's image on them.
4. **The isometries of the union.** Enumerating, for each metric automorphism of the six points, the
   per-circle parameter maps consistent with its marked points and filtering them by the exact Gram
   constraints of the frames, the isometries of the union of the nine circles number 36864, against
   2304 for the action of act 25's family on the union; the reflection of any single circle through
   its two marked points, the identity on the other eight, preserves every distance of the union (an
   independent floating-point control over three hundred random pairs agrees to `2 × 10⁻¹⁴`, and a
   quarter-turn of one circle alone, the countercontrol, changes distances by up to `0.80`) and is
   the action of no member of the family. **This bears on the sign of `A26-2`'s proposition and is
   not a verdict**: no map is exhibited in the kernel, no theorem states the isometry hypothesis for
   any such map, and the frozen negative label is not earned by it.
5. **Why the frozen negative form has no witness here.** Every per-circle map of every isometry of
   the union — thirty-six at each circle — is realised by some member of the family; so for every
   candidate and every class some member agrees with the candidate on that class's circle, and no
   single class is sent off every member's reach. A negative statement about this configuration, if
   a later freeze asks it, is of the form "for every member of the family and each of its four
   shapes, some class separates the exhibited map from it" — the class depending on the member —
   and not of the form this freeze fixed; what would settle it in the kernel is the isometry
   hypothesis for the single-circle reflection, a coordinate-sum identity over act 24's feature
   space read through the Fourier-mode structure of item 1, together with the per-member
   separations. **This round proposes nothing about the family, names no map as anything, and
   asks no further question.**

The anti-expansion rule collected nothing else: no fifth generator, no second normalized space or
geometry, no further equivalence, rung or configuration, no description of the product
configuration's classes, no strengthening of a merged theorem and no universal implication for a cell
recorded undecided in advance was noticed.

## 20. The provenance as honoured

The equivalence is act 12's at blob `4bba2040c33424fafbc6d31c0d63b86dff33691a`, consumed unrestated;
the rungs are act 21's declarations at blob `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8`, restated
nowhere and named in no statement; the invariant family and the geometry are act 24's at blob
`ce9d1aa05dfdedfb5cac171cfe6379681942195f`, consumed and never redefined, `featureVec` binding the one
and the equation the other; the family and the class description are act 25's at blob
`954fbddaa7511713a26c316b3b2e0f29497e81d2`, consumed unrestated; the Fourier matrix is act 23's lambda
at blob `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1`; the quotient list, the single-carrier
configuration and the non-adoption clause are act 21's unchanged, the clause with "Act 26" in its
first sentence as the freeze directs; the three definitions, the metric, the extension theorem, the
census and its count, the rigid-motion step and the gate are this freeze's, bound by statement, by
formula and by equation; the routes are the freeze's readings, with the two strands of literature the
freeze names as their provenance and as the provenance of no theorem. The freeze is not
edited.

## 21. The discrepancies — recorded and not repaired

**Four items are recorded. None is repaired, and the frozen document is not edited.** Each is a
detail of the freeze's reading that the execution found otherwise; the labels are earned by what the
kernel proves and by nothing stated in the reading, and no label turns on any of them.

**DF1 — the marked set of the positive route's second step.** The freeze's reading names the
intersection points of distinct circles as a finite set preserved by every rigid motion of the
normalized set and affinely spanning its hull. The intersection points are six, two on each circle,
and neither determine a circle's isometry nor span the hull. Failure rule 2 governs: the step is
recorded as not obtained with this obstruction, `A26-2` takes its `UNDECIDED` label, no affinity is
assumed to bridge the step, and the reading is not repaired.

**DF2 — the order of the monomial coordinates, written "of order at most three".** The freeze reads
each coordinate on the unit circle as `S z^(A − B) / 64` with `A − B ∈ [−3, 3]`; the kernel's
`fourier_coord_uniform` carries the exponents and not their difference, and the execution's
computation found `A − B ∈ {−1, 0, 1}` at every coordinate (§19, item 1). The freeze's bound is a
bound and not a value, nothing turns on it, and the wording is not repaired.

**DF3 — the form of the negative label.** The freeze fixes `A26-2-NOT-RIGID`'s witness as one
exhibited realizable class inequivalent to its image under every member of the family. The
execution's computation (§19, item 5) found that no class of that form exists for any surjective
isometry of the union of the nine circles, so that the frozen form cannot be earned at this
configuration whatever the proposition's truth; the label discipline is not changed, `A26-2` takes
`UNDECIDED`, and what a later freeze might ask is stated once in §19 as an observation.

**DF4 — the name of the affine-span agreement lemma.** The freeze's library provenance names
`eqOn_affineSpan`; the library carries it as `AffineMap.eqOn_affineSpan`. The lemma is the same and
the naming is not repaired.

**No start-state discrepancy arose**, in any of the thirty pinned blobs, in any of the four files
written onto, or in any of the ten preconditions: **every one matches** and **all ten pass**.
**No candidate discovered during execution was executed.** **No configuration was chosen after an
outcome was known.** **No alternative witness was substituted for a named one.** **No target was
executed out of order, and no verdict commit carries a later target's result.** No closed round's
contract failed on any head of this branch, so no amendment is called for.

## 22. The provenance of this note

Every frozen sentence in this note — the `A26-0-EXTENDS`, `A26-1-SEVERAL`, `A26-2-UNDECIDED` and
`A26-3-NOT-EXECUTED` sentences, the `A26-1-N`, `A26-1-DIM` and `A26-2-P` carriages, the outcome-vector
row, the `P0` sentence with its one substitution, the ordering obligation, the anti-contamination
invariant and the three carriages of THE CLAUSE — was extracted by line range from the frozen
preregistration blob `521b63cc…` at `B` and not retyped, and the `R7-CGR` clause pins each by the same
extraction.
