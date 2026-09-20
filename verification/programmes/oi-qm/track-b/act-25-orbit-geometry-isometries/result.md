# Track B act 25 — the orbit-geometry isometries: the normalized realizable quotient, the finite family that acts on it, the internal description of its classes at the single carrier, a gated classification of its surjective isometries, and the prefix-constrained corollary: RESULT

Executed under the frozen control plane `preregistration.md` in this directory, blob
**`f4892f64e1667244fc262a01fb46b27f9b1ba1ba`**, from `main` at **`dd3bd2e726e0fb3bccd96df9c46a532119a9ee97`** —
the certified merge commit of that control plane, the round's mandated execution base `B`, certified
by main-push run 35470951442 with all four jobs green and the control-plane base check in mode `B`
reporting twenty-one rows and no failure — which this execution verified by blob as its first act,
before any target was executed.

**Outcome vector:** `ISO1-FAMILY-ACTS` · `ISO2-CLASSIFIED` · `ISO3-UNDECIDED` · `ISO4-NOT-EXECUTED`

**The headline is row 4 of the freeze's outcome-vector table, verbatim.** `ISO0` silent; `ISO1`
landed by `iso1_family_acts` with its two instantiations, its sixteenth conjunct `iso1_word_normal_form`
kernel-checking that every word in the generators reduces to one of the four shapes; `ISO2` landed by `iso2_classes_single`,
both directions; `ISO3` undecided with the route run — step 1 closed by `fourier_circle_metric`,
steps 3 and 2 not obtained, the obstructions named; `ISO4` not executed, the gate closing on
`ISO3-UNDECIDED`. `ISO1-R`, `ISO3-L`, `ISO2-P` and `ISO3-P` are undecided and `ISO4-P` is not
executed, each entering no label. Every verdict is of the exact frozen proposition at the exact
configuration, with the geometry bound by equation and every generator written by its frozen
formula, and of nothing in its neighbourhood. **No verdict was inferred from another beyond the
consumptions the freeze places.** **No generator is read as a symmetry, an antiunitary map or a
time reversal.** **No theorem is attributed to the literature, no classification is imported and no
weaker domain is substituted.** **Every earlier act's historical verdicts stand unchanged**: acts 12
through 24's labels are consumed as landed, and this round's labels are earned under this freeze
about the family and the normalized space alone.

> **THE CLAUSE, carried at this mention — the headline.**
> Act 25 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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
creates new seal state — a new Lean module with new named results and a new `R7-*` guard clause —
and it lands **`E` → `L` → `P`, with `P` mandatory**.

| object | where it lives | state at this execution | state from `P` |
| --- | --- | --- | --- |
| the mandated execution base | the prospective declaration `_MANIFEST_PROSPECTIVE = {'OGC': 'dd3bd2e726e0fb3bccd96df9c46a532119a9ee97'}` in `verification/lean/edge_rigidity_probe.py` | **declared**; the validator classifies `OGC` as `EXECUTION` against it | **removed** by `P` |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': 'dd3bd2e726e0fb3bccd96df9c46a532119a9ee97', 'authorized': ('OGC',)}` | the twenty-nine records of the seals tree `ffb92daab9ea2f3d64c47b9c73e4b9c3466b763f` at `B`, plus the one addition authorized by stem | unchanged |
| the round's manifest record | `verification/seals/OGC.json` | **absent** | **written by `P`**: `{"round": "OGC", "kind": "sealed", "base": "dd3bd2e726e0fb3bccd96df9c46a532119a9ee97", "sealed_head": E, "merge": L}` |

**`OGC.json` is absent at execution and is written by `P` and by nothing before `P`.** That is a
statement about this execution and stays true as one. **No legacy seal constant is written**: nothing
matching `_OGC_(BASE|SEALED_HEAD|MERGE)` exists at any commit of this branch, and `SI-3`'s standing
contract — zero legacy assignment statements in the guard file — holds at every head. **No existing
manifest record is altered**: the twenty-nine records at `B` are read and never written, and the
chronology verdict is the validator's through one keyed call, `_si2_authority('OGC', tag='R7-OGC')`.
**No closed round's contract is edited**: the supersession table is empty, and every closed round's
guard reads its own record at every head of this branch.

**The base-blob verification is recorded.** `git cat-file -p dd3bd2e7:verification/programmes/oi-qm/track-b/act-25-orbit-geometry-isometries/preregistration.md | git hash-object --stdin`
returns `f4892f64e1667244fc262a01fb46b27f9b1ba1ba`, the blob the freeze names and the blob the
`R7-OGC` clause pins; `git rev-parse dd3bd2e7:…/preregistration.md` returns the same, and so does
`git hash-object` on the file in the working tree at every commit of this branch.

**The files this round writes** are the new module `verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean`,
this result note, one import line in `verification/lean-mathlib/OIBridge.lean` (directly after act
24's module, line 213), one census entry in `verification/lean-manuscript-census.json`, the `R7-OGC`
clause with the two declarations in `verification/lean/edge_rigidity_probe.py`, and the frozen
post-round sentence appended to the `P0` row of `verification/ROADMAP.md` after act 24's. **No
manuscript file is written.**

## 2. The start state

**Every one of the twenty-six paths the freeze pins by blob was checked at `B` by `git rev-parse`,
and every one matches**; they are the `frozen-blob` lines of the freeze's machine-checkable block,
which the base check verified at `M` (run 35470058510, at the candidate merge of pull request #691)
and at `B` (run 35470951442). The three further paths of the start-state table — `AGENTS.md`,
`tools/control_plane_base_check.py` and `tools/control_plane_lint.py` — carry their pinned blobs at
`B` as well. The four files this round writes onto carry their pinned blobs at `B`:
`verification/ROADMAP.md` at `fb5a9df14952d24217d677677c6562c4eac562ed`,
`verification/lean/edge_rigidity_probe.py` at `bdd76b23985638d6f6715561c8975480b2e53584`,
`verification/lean-mathlib/OIBridge.lean` at `165f4bf3caf7cb6c5120476969415b5545150bd1` and
`verification/lean-manuscript-census.json` at `02225c2573515aae60a5f73ba0510f8f438a0b53`. The seals
tree at `B` is `ffb92daab9ea2f3d64c47b9c73e4b9c3466b763f`, twenty-nine records, twenty-three `sealed`
and six `base-only`, no `OGC.json`, the same tree as at `D`.

**No start-state discrepancy arose in any pinned blob.** `D = 17272da2…` and `B` are distinct
commits, as the freeze reads them: the drafting-time facts are facts about `D`, the pins are read at
`B`, and every pinned blob is the same at both, the tree at `B` differing from the tree at `D` by
exactly the one added preregistration file (2088 lines, no other path). `B`'s parents are `D` and
`a6cb0c41acbe790b2f566faa56c9149f3d5e107e`, the head of pull request #691.

**The anti-contamination invariant is honoured**, carried in the freeze's own wording:

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

Sibling lanes present at `B` are not inputs and none was read. The start-state table is the complete
list of what this round consumes.

## 3. The ordering obligation's records

The obligation, in the freeze's own wording, which binds this execution:

> **The ordering obligation, act 25.** The rungs are act 21's declarations at blob `860daac4…`, the
> equivalence is act 12's at blob `4bba2040…`, the invariant family and the geometry are act 24's
> at blob `ce9d1aa0…`, and nothing else. The execution's module **states no rung, no equivalence
> and no definition of any kind**; the geometry is bound, in every theorem that names it, to act
> 24's equation; each generator of the family is written, in every theorem that names it, by its
> frozen formula; the transpose is written by its frozen relation; and the four-shape conclusion is
> written out in every classification statement. From the first commit that adds the module to the
> certified head `E`, **no commit of the branch adds a definition, restates a rung, alters the
> geometry's equation, alters a generator's formula, adds or removes a generator, or uses an
> equivalence outside the frozen quotient list**; the module commit carries no verdict of any
> target; the verdict commits of the executed targets follow it in the order `ISO1`, `ISO2`,
> `ISO3`, `ISO4`; and no theorem of a later target's section is present before that target's
> verdict commit.

**Eight records, each checkable by an auditor from the branch alone.** The execution branch is
`claude/act-25-execution-2`, rooted at `B`, and its first-parent chain from `B` is, in order:

| # | commit | content |
| --- | --- | --- |
| 1 | `edbc1e15b887566e6776376e6d776563f0ad593e` | **stage A**: the two declarations set to `B`, in the guard file only |
| 2 | `d431e86e914ee3ac2a1dc7831a805fea2e5acb1f` | **the module commit**: Section A, the eight shared lemmas, plus the import line; no definition, no verdict |
| 3 | `c9d7683b301522106a6d3d08974dab3cbe58772c` | `ISO1`: `iso1_family_acts`, `iso1_word_normal_form`, `iso1_single_carrier`, `iso1_product_carrier` and twelve supporting results |
| 4 | `c4ab120bb9a2dd312272012d0661b03e3ce54a3a` | `ISO2`: `iso2_classes_single` and seven supporting results |
| 5 | `13fbbd4ba07181033439dcd291965da2b0b29c55` | `ISO3`: `fourier_circle_metric` and three supporting results, the route's step 1; no classification theorem |

followed by the packaging commit carrying this note, the `R7-OGC` clause, the `ROADMAP` sentence and
the census entry, and by whatever certification fixes as `E`. **`ISO4` has no verdict commit**: the
gate did not open it.

### 3.1 The declaration table (record 1)

| object | the merged declaration consumed, with its line range at its blob | this round's module |
| --- | --- | --- |
| `FibreGram` | `TwoSidedGauge.lean` `4bba2040c33424fafbc6d31c0d63b86dff33691a`, lines 95–97 | consumed unrestated |
| `GramPhaseEquiv` | the same, lines 102–103 | consumed unrestated; the only equivalence used in any verdict |
| `RealizableGram` | the same, lines 108–110 | consumed unrestated; "realizable" in every statement |
| `fibreGram_apply`, `sh1_necessity`, `gramPhaseEquiv_cross_invariant`, `sh1_sufficiency` | the same, lines 115–116, 168–171, 870–871, 1070 | consumed |
| `AdmissibleDilationAt` | `DilationChoice.lean` `7e3a8222cedf530f3c109662e7174d72b6358063`, lines 134–136 | consumed unrestated; the hypothesis under which every transpose is taken |
| `RelabelTransition` | `RepresentativeNaturality.lean` `4c1137f35600320b9273c857ec62271341b05cd0`, lines 167–168 | consumed unrestated; its body `fun i => (G (σ i)).submatrix σ σ` is the `(π, τ)` formula at `π = τ = σ`, the diagonal case; named in no statement of this round |
| `mixedTriple` | `OrbitGeometrySelector.lean` `ce9d1aa05dfdedfb5cac171cfe6379681942195f`, lines 79–80 | consumed unrestated; the geometry bound to its equation in every theorem that names `d` |
| `mixedTriple_star`, `realizable_conj`, `conj_conj` | the same, lines 114, 1523, 1534 | consumed, in (iv), (xi) and (x) |
| `conj_gramPhaseEquiv` | the same, line 1541 | the descent of `C`, consumed by the freeze's placement; used in no proof of this round |
| `ProperAt`, `PropagatesFrom` | `IntermediateCrossTimeStructure.lean` `cb14c43b0becfe1a379ae3615d5553723ede9163`, lines 167–171 and 186–193 | the prefix's standing hypotheses; named in no statement of this round, `ISO4` not being executed |
| `EvolvesTotally`, `PreservesAdmissible`, `L2` inline, `Reversible`, `L4d` inline | `OrbitLawRigidityTwisted.lean` `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8`, lines 96–100, 108–110, 123–128, and `LadderConds` 179–196 | the prefix's rungs; named in no statement of this round, `ISO4` not being executed |
| act 23's `H z` | `OrbitLawGaps.lean` `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1`, `hadamard_z_admissible` at line 116 | the lambda `Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)`, written out at every mention |
| this round's module | — | **no definition**: no line beginning with `def `, `abbrev `, `structure `, `class `, `instance `, `axiom ` or `opaque ` at any commit; it imports `OIBridge.OrbitGeometrySelector` |

**This round's module carries no declaration of its own**: no `def`, `abbrev`, `structure`, `class`,
`instance`, `axiom` or `opaque` at any commit; it imports `OIBridge.OrbitGeometrySelector`; `R7-OGC`
checks both mechanically at every commit from the module commit to the certified object. **No rung
was restated, no equivalence was widened, no generator was added or removed, no domain was
substituted and nothing was imported.**

### 3.2 The stage-A commit (record 2)

**`edbc1e15b887566e6776376e6d776563f0ad593e`.** `git show --stat` lists one file,
`verification/lean/edge_rigidity_probe.py`, +2/−2: `_MANIFEST_PROSPECTIVE = {'OGC': B}` and
`_MANIFEST_BASELINE = {'base': B, 'authorized': ('OGC',)}`, both outside the validator's
marker-bounded regions, and nothing else. The supersession table being empty, no closed round's
contract is touched. At this commit the guard printed **eighty-eight `R7-*` tags, all `PASS`**,
`R7-OLT`, `R7-OLN`, `R7-OLG` and `R7-OGS` classified `ARCHIVED`, with `OGC` declared.

### 3.3 The module commit (record 3)

**`d431e86e914ee3ac2a1dc7831a805fea2e5acb1f`**, the first commit at which the module is present. It
carries the named results **`mixedTriple_relabel2`**, **`fibreGram_unique`**, **`mixedTriple_transpose`**, **`rows_phase`**, **`transpose_admissible`**, **`antipodal`**, **`dephase`**, **`fourier_entry_monomial`** — the coordinate identity of an independent relabelling,
the fibre-Gram entry at a one-element ancilla, the coordinate identity of the dilation transpose,
the row-phase lemma, the admissibility of the transpose, the unit-modulus identity with its
antipodal consequence, the dephasing of a single-carrier dilation, and the entries of the Fourier
tuple as monomials — each a shared lemma and none a verdict: no conjunct of any target is
discharged or refuted, no realizable class is described, no isometry is classified, and no
transition family is named in the module at this commit or at any later one.

### 3.4 The verdict commits (record 4)

| target | commit | named results |
| --- | --- | --- |
| `ISO1` | `c9d7683b301522106a6d3d08974dab3cbe58772c` | `relabel2_realizable`, `relabel2_gramPhaseEquiv`, `relabel2_isometry`, `conj_isometry`, `transpose_single_valued`, `transpose_unitary`, `transpose_descends`, `transpose_isometry`, `relabel2_dilation`, `conj_dilation`, `conj_relabel2`, `relabel2_relabel2`, `iso1_word_normal_form`, `iso1_family_acts`, `iso1_single_carrier`, `iso1_product_carrier` |
| `ISO2` | `c4ab120bb9a2dd312272012d0661b03e3ce54a3a` | `row_forms`, `core_row_norm`, `perm_of_rows`, `rows_injective`, `core_nonreal`, `core_real`, `classify_dephased`, `iso2_classes_single` |
| `ISO3` | `13fbbd4ba07181033439dcd291965da2b0b29c55` | `fourier_entry_uniform`, `fourier_coord_uniform`, `fourier_coord_diff_norm`, `fourier_circle_metric` |
| `ISO4` | **none** | **none** — the gate did not open it |

Each verdict theorem first appears at its own verdict commit and at no earlier commit; each verdict
commit carries its own target's results and nothing of a later target's; the order on the
first-parent chain is `ISO1`, `ISO2`, `ISO3`. **The gate opened `ISO2`** on `ISO1-FAMILY-ACTS`,
**opened `ISO3`'s route** on `ISO2-CLASSIFIED`, and **closed `ISO4`** on `ISO3-UNDECIDED`; `ISO4`
has the label `ISO4-NOT-EXECUTED` by the gate rule.

### 3.5 The immutability span (record 5)

`git diff d431e86e914ee3ac2a1dc7831a805fea2e5acb1f <E> -- verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean | grep -c -E '^[-+](def |abbrev |structure |class |instance |axiom |opaque )'`
**returns `0`**: no diff between the module commit and the certified head adds or removes a
definition of any kind, there being none at any commit. Measured at the `ISO3` commit and again at
the packaging commit, which does not touch the module, and on the first attempt's chain at its own commits, and re-run by `R7-OGC` on every head from
the module commit to the certified object.

### 3.6 The quotient, geometry and family record (record 6)

**The only equivalence used in any verdict is act 12's `GramPhaseEquiv`**, through
`gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, and this round's `relabel2_gramPhaseEquiv`,
`transpose_single_valued` and `transpose_descends`, which are statements about it; act 17's `GramTrajEquiv` and act 21's `LawEquiv` are not used. **The geometry is bound, in
every theorem that names it, to
`d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)`** — as a hypothesis `hd`
in every shared lemma and control, and as the equation `d = (fun G H => …) →` in every verdict
theorem. **Every generator is written, in every theorem that names it, by its frozen formula**: the
independent relabellings as `fun i => (G (π i)).submatrix τ τ` with one permutation on the fibre
label and one on both matrix indices, the conjugation as `fun i => Matrix.of fun j k => star (G i j k)`,
the transpose through admissible dilations `U` as `FibreGram a₀ Uᵀ` under `AdmissibleDilationAt Γ a₀ U`
and `FibreGram a₀ U = G`, with `GramPhaseEquiv` on the result — never as a transpose of the tuple's
fibres, and never through one chosen dilation. **No equivalence was introduced or widened, no
generator was added or removed, no domain was substituted for the realizable quotient, and nothing
was imported**; no candidate equivalence and no fifth generator was noticed.

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
acquired.

#### The prior attempt's knowledge, disclosed once and before the spans

**Before this chain's first commit the executor already knew every target's outcome.** The first execution attempt (§3.7.2) had run the kernel proofs of every target: `ISO2` reaches `ISO2-CLASSIFIED` by the frozen route at `f239305c3b5b`, `ISO3`'s route closes step 1 and not steps 3 and 2 at `bbf87156d71e`, and `ISO4` is closed by the gate. That knowledge is **prior knowledge**: it was acquired before this chain existed, by proofs run in the first attempt, and it bore on every target this chain had still to execute. It is disclosed here, once, as what it is — the outcome of every target, known in advance — and it did not change any route: this chain replays the first attempt's `ISO2` and `ISO3` commits with their content unchanged, and its `ISO1` commit adds the theorem the attempt lacked. **The span answers below measure what was newly acquired in each span and nothing else**; the prior knowledge is not re-counted at any span, and this disclosure does not cure it.

#### The span `B` → module commit

| question | answer for the span `B` → module commit |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: verified the frozen blob at `B` by `git rev-parse` and `git cat-file | git hash-object`; created the branch from `B`; wrote and committed the stage-A edit, byte-identical to the first attempt's, and ran the guard at that commit; replayed the first attempt's module commit by cherry-pick with its content unchanged — Section A, the eight shared lemmas, the import line. Nothing was built or run in this span beyond the guard, and nothing bearing on any target was newly acquired in it: the outcomes known at its start are the prior knowledge disclosed above, acquired before this chain existed.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's proof route for every target — the coordinate identities of the three generators, the row-phase argument, the transpose's admissibility and descent, the six relations, the dephasing with its phases, the antipodal identity, the shape of the case analysis, the monomial coordinates of the Fourier tuple and the three steps of the classification route — each recorded there as the freeze's reading and not as a finding; the consumption of `ISO2` by `ISO3` and of `ISO3` by `ISO4`; acts 12's, 21's, 23's and 24's result notes at their pinned blobs, which record every consumed fact; the merged modules. Beyond the freeze, the prior knowledge disclosed above.

#### The span module commit → `ISO1`

| question | answer for the span module commit → `ISO1` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: staged the first attempt's Section B without committing it; wrote and built `iso1_word_normal_form` — the four-shape normal form for every word in the generators, by induction on the word from the six relations, descent and realizability preservation — and added it as the sixteenth conjunct of `iso1_family_acts`; built with zero errors and zero warnings; committed the sixteen results of Section B as one `ISO1` verdict commit. The builds revealed elaboration details only (`simp` rewriting a transposed submatrix before a rewrite lemma could match, so the rewrite is done first; the number of patterns `ext` consumes after `convert`; the toolchain path) and nothing about any later target; the word theorem's proof reasons about `ISO1`'s own object only. `ISO1-R`'s finite check was not carried out, as recorded in §5. Nothing bearing on `ISO2`, `ISO3` or `ISO4` was newly acquired in this span.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `ISO1` target with its conjuncts (i)–(xi), the route of each, the six relations as the normal form's relations, the accounting act 24 asked for as a control, and the observation sub-question `ISO1-R` with its three outcomes; the first attempt's `ISO1` commit, whose fifteen results are replayed unchanged; and the prior knowledge disclosed above.

#### The span `ISO1` → `ISO2`

| question | answer for the span `ISO1` → `ISO2` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: replayed the first attempt's `ISO2` commit by cherry-pick with its content unchanged — the eight named results of Section C, the two directions of `iso2_classes_single` as separate conjuncts — built it (zero errors, zero warnings, thirty-two results) and committed it as the `ISO2` verdict commit. `ISO2-P` was not attempted, the freeze naming no route. The build re-established a result already known from the first attempt and revealed nothing new; nothing bearing on `ISO3` or `ISO4` was newly acquired in this span.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `ISO2` target with its two directions, the five steps of the class-description route as the freeze's reading, and the frozen obstruction of `ISO2-P`; the first attempt's `ISO2` commit, replayed unchanged; and the prior knowledge disclosed above.

#### The span `ISO2` → `ISO3`

| question | answer for the span `ISO2` → `ISO3` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: replayed the first attempt's `ISO3` commit by cherry-pick with its content unchanged — the four named results of Section D that close step 1 of the route — built it (zero errors, the one linter warning of §3.7.1, thirty-six results) and committed it as the `ISO3` verdict commit. Steps 3 and 2 of the route were not re-attempted; no theorem quantifying over an isometry of the normalized space was stated; no candidate isometry outside the family was found or sought; `ISO3-P` was not attempted. The build re-established a result already known from the first attempt and revealed nothing new; nothing bearing on `ISO4` was newly acquired in this span.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `ISO3` target, its three hypotheses and four-shape conclusion, the three steps of the route in the order 1, 3, 2 as the freeze's reading, the frozen statement that no complete route to the four-shape conclusion is in hand, and the frozen obstructions of `ISO3-L` and `ISO3-P`; the first attempt's `ISO3` commit, replayed unchanged; and the prior knowledge disclosed above.

#### The span `ISO3` → `ISO4`

| question | answer for the span `ISO3` → `ISO4` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the gate: `ISO3` reached `ISO3-UNDECIDED`, so `ISO4` is closed and has no verdict commit; no target remained open at this span's end. Wrote the packaging — this note, the `R7-OGC` clause, the `ROADMAP` sentence and the census entry — and ran the lint, the release gate and the guard; the module is untouched in this span. No theorem of `ISO4` was stated or attempted, `ISO4-P` was not attempted, and nothing was run, revealed or reasoned about any transition family.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's gate rule for `ISO4`, its `NOT-EXECUTED` sentence, the route it would have taken — `PreservesAdmissible` into the first hypothesis, `Reversible`'s second conjunct into the second, the isometry proposition into the third, `ISO3` at each `t` — reported here as the freeze's route and not executed, and the frozen `ISO4-P` sentence.

### 3.7.1 The history-integrity statement, and the execution defects disclosed

**No commit on this branch was amended, reset, rebased over, cherry-picked over or force-pushed
away. There are no superseded SHAs.** Before certification this execution absorbed no later `main`.

**No execution defect is recorded on this chain; one hygiene item is disclosed.** The hypothesis `hw : star w * w = 1`
of `fourier_coord_diff_norm` is stated and not used by its proof, the identity holding for unit `z`
alone, and the build reports it as an unreferenced binder name; the statement is kept as it was
built at the `ISO3` verdict commit and is not edited. The module's text at the packaging commit is
byte-identical to its text at the `ISO3` verdict commit; no verdict commit touches an earlier
target's results. Three items of the freeze's reading that the kernel represents
differently are recorded as discrepancies in §22 and are not repaired.

### 3.7.2 The first execution attempt, ruled unlanded

**A first execution attempt preceded this chain and was ruled unlanded.** It ran on the branch
`claude/act-25-execution`, rooted at the same `B`, with the first-parent chain stage A
`24ff53cccd44b7a92c8f1604b7d9295ff26303e9`, module commit `5bca42f0df2f38a299baf8019a2e98765263449c`, `ISO1` `d4b7738aafeb3ad06b4ab3bb86c1000f59bef204`, `ISO2` `f239305c3b5bf013fd8868da8f9c0672c90434ed`, `ISO3`
`bbf87156d71e8ed2dcd96850d33c4aa8dde63d03` and packaging `e09e296e94b923915361c9ec8b86b7963cd7ecf2`, and was opened as pull request #692 at that head, whose
exact-head continuous integration was fully green. The owner withdrew its certification on review: its
`ISO1` verdict commit kernel-checked the six generator relations and no theorem that every word in the
generators reduces to one of the four shapes, while the frozen `ISO1-FAMILY-ACTS` sentence asserts that
reduction at evidence level 2; `ISO2` and `ISO3` having been gated on that label, the defect was upstream
of the whole chain. **No landing merge and no pin of that attempt was pushed**: a landing merge and a pin
were constructed locally, never pushed, and are used for nothing. The attempt's branch and pull request
stand as they are, unmerged and unrewritten, as evidence; nothing of that chain is part of this round's
certified history. This chain replays the frozen chronology from `B`: its stage-A and module-commit
trees are byte-identical to the attempt's, its `ISO1` verdict commit carries the sixteen results of
Section B including the missing theorem, and its `ISO2` and `ISO3` verdict commits replay the attempt's
with their content unchanged. What the attempt revealed is disclosed once, before the span
attestations of §3.7, as prior knowledge.

### 3.8 The gate record (record 8)

| target | the label of the target before it, as earned | the gate | the key hazard's rule |
| --- | --- | --- | --- |
| `ISO2` | `ISO1-FAMILY-ACTS`, by `iso1_family_acts` at `c9d7683b3015` | **opened** | — |
| `ISO3` | `ISO2-CLASSIFIED`, by `iso2_classes_single` at `c4ab120bb9a2` | **opened**: the route was run | **not applied** — `ISO2` classified internally, so the route was run |
| `ISO4` | `ISO3-UNDECIDED`, the route having been run, at `13fbbd4ba071` | **closed**: `ISO4-NOT-EXECUTED` | — |

## 4. `ISO0` — the bounded search, recorded in full

**Outcome reached: `ISO0`-silent.**

> On the search this freeze bounds — act 12's, act 21's, act 23's and act 24's control planes,
> amendments, result notes and modules, and `verification/ROADMAP.md`, against the frozen term
> list — the merged record carries twelve isometry verdicts about named transition families, one
> witness sending a class off every carrier relabelling's reach, and one recorded non-attainment
> naming the classification of the isometries as what would settle it, and decides neither what
> the realizable classes at either frozen configuration are, nor whether any map other than a
> carrier relabelling or the entrywise conjugation is an isometry of the geometry, nor whether
> every isometry of it is of any named form, nor whether any condition of act 21's ladder with
> isometry forces membership in any named family. **The finding is that the record is silent on
> the point.** It is not a finding that any such statement is false, not a finding that one is
> unprovable, and not a bound on what a later round could prove.

**`ISO0` is a type-P target and carries no evidence level.** No Lean was written for it, and this
round's own theorems are not treated as retro-evidence about it.

**The file set at `B`**, as the freeze bounds it: act 12's `result.md` and `TwoSidedGauge.lean`;
act 21's `preregistration.md`, `amendments/amendment-1.md`, `result.md` and
`OrbitLawRigidityTwisted.lean`; act 23's `preregistration.md`, `result.md` and `OrbitLawGaps.lean`;
act 24's `preregistration.md`, `result.md` and `OrbitGeometrySelector.lean`; and
`verification/ROADMAP.md`. **The question asked of each hit**: does this passage classify the
realizable tuples at either frozen configuration modulo act 12's equivalence, or state that a map
other than a carrier relabelling or the entrywise conjugation is an isometry of act 24's geometry,
or state that every isometry of it is of any named form, or state that any condition of act 21's
ladder with isometry forces a law to act on classes as a member of any named family? This round's
own control plane is inside the set by construction and its hits are recorded as not relevant to the
question; the counts below are of the thirteen files named, each read at its pinned blob at `B`, the
control plane excluded, each term counted as a case-insensitive substring.

| term | hits (act 12 result / module; act 21 prereg / amendment / result / module; act 23 prereg / result / module; act 24 prereg / result / module; ROADMAP) | recorded answer |
| --- | --- | --- |
| `isometr` | 3 / 8 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 138 / 177 / 66 / 10 | **Does not supply it.** Act 12's hits (result lines 106–111; module lines 35, 629–714, 748) and the `ROADMAP`'s at lines 205 and 260 are the Gram-isometry lemma `exists_unitary_of_gram_eq`, a statement about vector families with equal Gram matrices and one unitary, not about any map of the orbit space. Act 24's hits are its twelve isometry verdicts about twelve named transition families, its cell `a0` (an isometry is injective on classes), its cell `b` recorded undecided with the classification of the isometries named as what would settle it, and its observation for this round; the `ROADMAP`'s hit at line 63 is act 24's `P0` sentence restating them. No statement that any map other than a carrier relabelling or the entrywise conjugation is an isometry of the geometry, none that every isometry of it is of any named form, and none that any condition of act 21's ladder with isometry forces membership in any family. |
| `classif` | 7 / 5 / 49 / 0 / 30 / 2 / 18 / 14 / 1 / 19 / 16 / 1 / 18 | **Does not supply it.** Act 12's classification is of the per-slice quotient by the two-sided action — the realizable tuples are the fibre-Gram data of admissible dilations, in both directions (`SH1`), and the classes are the orbits of the phase action (`TG2`) — and describes no class as a relabelled Fourier class; act 20's is of one lift against three notions; every other hit is `§A.37`'s lifecycle vocabulary ("the validator classifies"), THE CLAUSE's first sentence, act 24's provenance line naming the complex-Hadamard literature and consuming nothing, or act 24's `b` obstruction naming the classification of the isometries as what is not in hand. |
| `Hadamard` | 10 / 13 / 11 / 0 / 7 / 7 / 9 / 12 / 10 / 22 / 18 / 16 / 2 | **Does not supply it.** Act 12's Hadamard dilations `H₁`, `Hᵢ`, act 21's `hadamard_entries`, act 23's family `H(z)` with its admissibility, and act 24's entry, coordinate and feature-norm bounds on it — the objects every separation is read on; act 24's control plane names the Haagerup classification as provenance and consumes nothing of it. No description of the realizable classes modulo act 12's equivalence anywhere. |
| `Fourier` | 0 / 0 / 0 / 0 / 0 / 0 / 9 / 4 / 3 / 8 / 16 / 31 / 0 | **Does not supply it.** Act 23's Fourier family `H(z)` at a unit parameter, its Pythagorean sequence and its admissibility; act 24's bounds on it and its `Φ_HS` shift argument along it. No statement that every realizable class at either configuration is the class of a relabelled Fourier tuple. |
| `dephas` | 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 | **Absent.** |
| `transpos` | 2 / 37 / 2 / 0 / 0 / 12 / 0 / 0 / 4 / 3 / 10 / 15 / 1 | **Not relevant to the question.** Act 12's hits are `conjTranspose` lemma names and the anchor-swapping transpositions of its test dilations; act 21's and act 23's are `conjTranspose` lemma names and the column transposition `σ = (2 3)` of `ΦP`; act 24's are `conj_eq_transpose` (the conjugate of a Hermitian tuple is its fibrewise transpose) and `Matrix.PosSemidef.transpose` inside `realizable_conj`. No transpose of a dilation is named as a map on classes anywhere. |
| `conjugat` | 1 / 1 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 24 / 23 / 26 / 14 | **Does not supply it.** Act 12's right weak action conjugates the Gram data by the anchored phases; the `ROADMAP`'s hits are the substratum lane's hidden conjugation and act 13's constant-left conjugation; act 24's are `Φ_conj`, the entrywise conjugation, proved an isometry at the product configuration and the witness of its cell `b₀`. The entrywise conjugation is one of the two maps the question excepts, and act 24's verdict about it decides nothing about any other map. |
| `antiunitar` | 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 8 / 2 / 0 / 0 | **Not relevant to the question.** Every hit is act 24's forbidden-sentence list, its term list, or its statement that nothing calls its witness antiunitary. |
| `Wigner` | 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 6 / 1 / 0 / 0 | **Not relevant to the question.** Every hit is act 24's provenance section, its forbidden-sentence list or its term list. |
| `rigid` | 0 / 0 / 97 / 8 / 29 / 36 / 26 / 9 / 3 / 61 / 28 / 9 / 4 | **Does not supply it.** Act 21's `L-WIDE` verdict about the ladder's surviving class, act 23's rung verdicts, and act 24's rigidity cells — `b₀` `NOT-RIGID` for the carrier relabellings alone, `b` undecided; none concerns the classification of the isometries, and act 24's `b` names that classification as absent. |
| `relabel` | 0 / 1 / 37 / 0 / 25 / 169 / 61 / 32 / 71 / 75 / 54 / 65 / 15 | **Does not supply it.** Act 20's `RelabelTransition`, act 21's relabelling laws and product relabellings, act 23's, and act 24's relabelling isometry — the carrier relabelling `(σ, σ)`, one of the two maps the question excepts. No independent relabelling of fibres and of matrix indices is named anywhere, and no statement that the relabellings exhaust anything. |
| `permut` | 0 / 0 / 12 / 0 / 3 / 4 / 5 / 2 / 0 / 5 / 6 / 2 / 0 | **Does not supply it.** Act 21's carrier permutations `σ = (2 3)` and `σ × σ`, act 23's and act 24's — each a carrier relabelling. No permutation of the rows of a dilation independent of its columns is named anywhere. |
| `affine` | 0 / 0 / 0 / 0 / 1 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 | **Not relevant to the question.** The one hit is act 21's own record search, naming `TwoByTwoNoGo`'s affine rigidity of another programme. |
| `linear` | 2 / 23 / 0 / 0 / 0 / 2 / 0 / 1 / 7 / 0 / 3 / 11 / 6 | **Not relevant to the question.** Act 12's `LinearIsometry.extend` inside the Gram-isometry lemma, the tactic name `linear_combination` in every module, and the `ROADMAP`'s hydrodynamic and substratum lanes. No statement that any isometry of any orbit geometry is linear or affine, and none assuming it. |
| `compact` | 0 / 0 / 0 / 0 / 1 / 0 / 0 / 0 / 0 / 2 / 4 / 1 / 0 | **Not relevant to the question.** Act 24's `GEO1-T`, recorded undecided with the compactness half not attempted, and act 21's compact-semigroup remark of another programme. No compactness of any orbit space is asserted or used. |

**A search that finds a decision is a finding, and a search that does not is equally a finding.**
The second is what happened, and the finding is that the record is silent. Act 24's twelve isometry
verdicts, its `b₀` witness and its `b` obstruction are recorded as found and as what they are:
verdicts about twelve named maps, one class sent off every carrier relabelling's reach by the
entrywise conjugation, and a recorded non-attainment naming the classification of the isometries
as what would settle it — which decide none of the four questions. Reconstructive inference is
refused as a finding here.

## 5. `ISO1` — the normalized space and the family that acts on it

**Outcome reached: `ISO1-FAMILY-ACTS`.**

> The finite family generated by the independent relabellings of fibres and of matrix indices,
> the entrywise conjugation and the dilation transpose acts on the realizable classes at both
> frozen configurations: each generator sends realizable tuples to realizable tuples, sends
> equivalent tuples to equivalent tuples, and preserves act 24's distance on realizable tuples;
> the transpose, defined through any admissible dilation of the tuple, is defined for every
> realizable tuple and is the same class whichever dilation is taken; and every word in the
> generators is, on realizable classes, one of four shapes — a relabelling, a relabelling
> composed with conjugation, a relabelling composed with the transpose, or a relabelling composed
> with both — at evidence level 2. **This is a statement about four named maps and the exact
> quantity frozen**: it does not say the family is all of the isometries, does not say any
> generator is a symmetry, an antiunitary map or a time reversal, and adopts nothing.

`iso1_family_acts` carries the conjuncts (i)–(x) of the freeze as fifteen separate conjuncts of one
statement, and the normal form for every word as a sixteenth, quantifying over every finite carrier `W` with `[Fintype W] [DecidableEq W]`, every ancilla
`A` with `Fintype.card A = 1` where the freeze says so, and every constant symmetric `Γ` with no
vanishing entry where a conjunct needs it, with `d` bound by the displayed equation; (xi) is the two
instantiations. Each conjunct, reported separately:

| conjunct | proved by |
| --- | --- |
| (i) realizability of `(π, τ)` | `relabel2_realizable`: positive semidefiniteness and rank invariant under `submatrix τ τ`, the relabelled fibres summing to the relabelled identity by `Equiv.sum_comp`, the diagonal the constant; stated at every carrier `W`, every ancilla `A` and every constant `Γ` |
| (ii) descent of `(π, τ)` | `relabel2_gramPhaseEquiv`: the phases `c ∘ τ` |
| (iii) isometry of `(π, τ)` | `relabel2_isometry`: `mixedTriple_relabel2` and the sum reindexed along `(π.prodCongr (π.prodCongr π)).prodCongr (τ.prodCongr (τ.prodCongr τ))` by `Equiv.sum_comp`, with `d` bound to the displayed equation |
| (iv) isometry of `C` | `conj_isometry`: act 24's `mixedTriple_star` at every coordinate and `norm_star`, at every carrier; realizability and descent of `C` consumed from act 24's `realizable_conj` and `conj_gramPhaseEquiv` in the instantiations |
| (v) admissibility of `Uᵀ` | `transpose_admissible`: `Uᵀ` unitary by `transpose_unitary`; the anchored moduli exchanged by the one-element sum and the symmetry of `Γ` |
| (vi) totality of `T` | act 12's `sh1_sufficiency`, consumed as the sixth conjunct |
| (vii) single-valuedness of `T` on classes | `transpose_single_valued`: at full support the rows of two dilations of one tuple differ by unit phases (`rows_phase`, from the coordinates `(j, j)` and `(j₀, k)` through `fibreGram_unique`), so the transposed fibre-Gram tuples are related by those phases |
| (viii) descent of `T` | `transpose_descends`: `U * Matrix.diagonal (fun p => c p.1)` is an admissible dilation of the phase-equivalent tuple, and its transpose has the fibre-Gram tuple of `Uᵀ` exactly, so the relation holds with `gramPhaseEquiv_refl` |
| (ix) isometry of `T` | `transpose_isometry`: `mixedTriple_transpose` — a coordinate of `FibreGram a₀ Uᵀ` is the conjugate of a coordinate of `FibreGram a₀ U` at `((p.2.2.1, p.2.2.2, p.2.1), p.1)` — then `norm_star` and the sum reindexed along that bijection |
| (x) `T ∘ (π, τ) = (τ, π) ∘ T` | conjunct 10: `relabel2_dilation` — the submatrix `U.submatrix (Prod.map π id) (Prod.map τ id)` is admissible, its fibre-Gram tuple is the `(π, τ)`-relabelling and its transpose's is the `(τ, π)`-relabelling of `FibreGram a₀ Uᵀ` — then `transpose_single_valued` against any admissible `U''` of the relabelled tuple; on classes, the transpose written through every dilation |
| (x) `T ∘ C = C ∘ T` | conjunct 11: `conj_dilation` — `U.map star` is admissible, its fibre-Gram tuple is the conjugate and its transpose's is the conjugate of `FibreGram a₀ Uᵀ` — then `transpose_single_valued` |
| (x) `T ∘ T = id` | conjunct 12: `transpose_admissible` on `Uᵀ`, `transpose_single_valued` against any admissible `U''` of `FibreGram a₀ Uᵀ`, and `Matrix.transpose_transpose` |
| (x) `C ∘ C = id` | conjunct 13: act 24's `conj_conj`, consumed |
| (x) `C ∘ (π, τ) = (π, τ) ∘ C` | conjunct 14: `conj_relabel2`, an exact equality of tuples |
| (x) `(π, τ) ∘ (π', τ') = (π.trans π', τ.trans τ')` | conjunct 15: `relabel2_relabel2`, an exact equality of tuples |
| (x′) every word reduces to one of the four shapes | conjunct 16, `iso1_word_normal_form`: for a word `w : List ((Equiv.Perm W × Equiv.Perm W) ⊕ (Unit ⊕ Unit))` — a relabelling token `(π, τ)`, the conjugation token, the transpose token — and a chain `c : ℕ → (W → Matrix W W ℂ)` with `c 0 = G`, `c w.length = H` and each step realizing its token by its frozen formula (`c (n + 1) = fun i => (c n (π i)).submatrix τ τ`; `c (n + 1) = fun i => Matrix.of fun j k => star (c n i j k)`; `∃ U, AdmissibleDilationAt Γ a₀ U ∧ FibreGram a₀ U = c n ∧ GramPhaseEquiv (c (n + 1)) (FibreGram a₀ Uᵀ)`), for realizable `G`: `∃ π τ`, `H` is `GramPhaseEquiv` to `(π, τ) G`, or to `C ((π, τ) G)`, or, for every admissible dilation `U` of `G`, to `(π, τ) (FibreGram a₀ Uᵀ)`, or to `C ((π, τ) (FibreGram a₀ Uᵀ))` — the freeze's four-shape conclusion with `H` in the place of `φ G`. Proved by induction on the word: the empty word is the shape `(1, 1)` by `gramPhaseEquiv_refl`; a word `g :: w'` reaches `H` through `c 1 = g G`, realizable by (i), by `realizable_conj` or by `sh1_necessity` on the dilation `transpose_descends` supplies, so the induction hypothesis gives `H` a shape over `c 1`, and one further generator on the left of a shape is again a shape — by `relabel2_relabel2`, `conj_relabel2`, `conj_conj`, `relabel2_dilation`, `conj_dilation`, `transpose_descends`, `transpose_single_valued`, `relabel2_gramPhaseEquiv` and `conj_gramPhaseEquiv` — with `gramPhaseEquiv_trans` joining the steps. No definition is introduced: the word type, the chain and the step relation are written inline |
| (xi) the instantiations | `iso1_single_carrier` at `V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ₀ ≡ ¼`, and `iso1_product_carrier` at `V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0, 0)`, `Γ = Γ₀ ⊗ Γ₀ ≡ 1/16`: every hypothesis of every conjunct discharged (the constant, symmetric, non-vanishing `Γ`, the one-element ancilla), with the transpose's realizability through `sh1_necessity` and the conjugation's through `realizable_conj` |

**The transpose's totality, single-valuedness and descent are reported apart from its isometry**:
(vi) is act 12's theorem consumed; (vii) and (viii) are this round's `transpose_single_valued` and
`transpose_descends`, each a statement about the relation written through every admissible
dilation; (ix) is `transpose_isometry`, a statement about dilations that needs neither. **The six
relations are reported**, each on classes with the transpose relation written out through the
dilations, three as exact equalities of tuples and three through `transpose_single_valued`.

**Every word in the generators reduces to one of the four shapes, kernel-checked by
`iso1_word_normal_form`**: the sentence's clause "every word in the generators is, on realizable classes,
one of four shapes" is the sixteenth conjunct of `iso1_family_acts` and not an inference from the six
relations. The theorem quantifies over every finite list of generator tokens and every chain realizing
it, at every finite carrier with a one-element ancilla and a constant non-vanishing visible family; the
four shapes are the freeze's displayed conclusion; and the transpose shapes are read through every
admissible dilation of the start, as the frozen conclusion reads them. It assumes nothing of the chain
beyond the step relation, and the induction uses the six relations, descent and realizability
preservation and nothing else.

**The accounting act 24 asked for, reported as a control and earning no label.** `RelabelTransition σ`
is, by its merged body, the `(π, τ)` formula at `π = τ = σ`, so `ΦI` is `(1, 1)`, `ΦP`'s map and
`ΦT`'s maps are `(σ, σ)` and `(1, 1)` at `σ = Equiv.swap 2 3`, and at the product configuration
`ΦPP` is `(σ × σ, σ × σ)`, `Φ_swap` is `(prodComm, prodComm)` and `Φ_conj` is `C`; each is a named
element of the family by inspection of its merged equation, and no non-isometry of act 24's list is
a candidate for membership, none satisfying the isometry hypothesis. No theorem of this round states
this accounting, and it earns nothing.

**`ISO1-R`, the observation sub-question — outcome `ISO1-R-UNDECIDED`.**

> **The frozen `ISO1-R-UNDECIDED` sentence.**
> Whether the dilation transpose is generated by the relabellings and the conjugation on the
> realizable classes is undecided in this round, with the step named; it enters no label.

The step named: the finite check the freeze names — one exhibited realizable tuple, `(swap 0 1, 1) F(z)`
or another, against the `1152` images `(π, τ) C ^ e G`, each inequivalence read through a named
invariant, or the universal agreement of one `(π, τ, e)` with `T` on every realizable class — was
not carried out in the kernel; the hand reading's observation that `T` fixes every Fourier class
(`H z` being symmetric) was not stated as a theorem either. **`ISO1-R` enters no label**, and the
family is frozen with all four generators either way.

**No generator is read as a symmetry, an antiunitary map or a time reversal.** The relabellings are
`fun i => (G (π i)).submatrix τ τ`, the conjugation is the entrywise `star`, the transpose is the
matrix transpose of the dilation, and each is named by its formula and as nothing else.

## 6. `ISO2` — the internal description of the realizable classes at the single carrier

**Outcome reached: `ISO2-CLASSIFIED`.**

> At the single-carrier configuration every realizable tuple is equivalent, under act 12's phase
> action, to an independent relabelling of act 23's Fourier tuple at a unit parameter, and every
> such tuple is realizable, each direction proved separately at evidence level 2 from act 12's
> merged sufficiency theorem, act 23's merged admissibility and elementary algebra, with nothing
> imported. **This is a statement about the exact configuration frozen**: it says nothing at the
> product configuration, nothing at any other visible family, nothing at `|A| > 1`, and does not
> say the Fourier tuple is canonical or physical.

`iso2_classes_single` carries the two directions as **separate conjuncts** under `§A.34`, at
`Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))`, `A = Fin 1`, `a₀ = 0`, with `H z` written as act 23's
lambda at every mention: (a) every realizable `G` is `GramPhaseEquiv` to
`fun i => (FibreGram (0 : Fin 1) (H z) (π i)).submatrix τ τ` for some `π τ : Equiv.Perm (Fin 4)` and
some `z` with `star z * z = 1`; (b) every such tuple is realizable. **The two directions are reported
apart**, each with its own witness in the statement, and the equality of the two sets of classes is
displayed nowhere as a single biconditional. The case analysis, each case named with the step that
closed it:

| step or case | closed by |
| --- | --- |
| the dilation | act 12's `sh1_sufficiency`, consumed: `U` admissible at `Γ₀`, anchor `0`, with `FibreGram 0 U = G` |
| the dephasing | `dephase`: with `r i = 2 * U (i, 0) (0, 0)`, `c j = 4 * star (U (0, 0) (0, 0)) * U (0, 0) (j, 0)` and `K i j = 2 * star (r i) * star (c j) * U (i, 0) (j, 0)`, the entries of `K` have unit modulus, its first row and first column are `1`, its rows are pairwise orthogonal, `‖c j‖ = ‖r i‖ = 1`, and `FibreGram 0 U i j k = star (c j) * (star (K i j) * K i k / 4) * c k` — the moduli from `AdmissibleDilationAt`, the orthogonality from the unitarity of `U` read at the anchored slots |
| the antipodal lemma | `antipodal`: for unit-modulus `a b c` with `1 + a + b + c = 0`, from the conjugated sum `ab + bc + ca + abc = 0` and `(a + b)(b + c)(c + a) = (a + b + c)(ab + bc + ca) − abc = 0`, one of `a + b`, `b + c`, `c + a` vanishes and the remaining number is `−1`; `row_forms`: every row `(1, a, b, c)` of `K` with `i ≠ 0` is `(1, x, −1, −x)`, `(1, −1, x, −x)` or `(1, x, −x, −1)` for one unit `x` |
| Case B — every entry real | `core_real`: each row is one of the four rows of the core matrix at `z = 1`, the row types are injective (`rows_injective`: two distinct rows are orthogonal while a core row has squared norm `4`, `core_row_norm`), and the injective row-type map is a permutation `π` (`perm_of_rows`, through `Equiv.ofBijective` and `Finite.injective_iff_bijective`) |
| Case A — a non-real entry | `classify_dephased`: a non-real entry `K i j` has `i ≠ 0`, `j ≠ 0`; row `i` has one of the three forms with `x ∉ {1, −1}`; the row swap `Equiv.swap 1 i` and a column permutation `τ₀ ∈ {1, Equiv.swap 1 2, Equiv.swap 2 3}` fixing `0` bring it to position `1` in the form `(1, x, −1, −x)`; then `core_nonreal`: every other row `(1, y, −1, −y)`, `(1, −1, y, −y)` or `(1, y, −y, −1)` is forced by its orthogonality with row `1` — `2 + 2 y star x = 0` gives `y = −x`; `(1 − star x)(1 − y) = 0` gives `y = 1`; `(1 + y)(1 + star x) = 0` gives `y = −1` — to `(1, −x, −1, x)` or `(1, −1, 1, −1)`, the row types are injective and the injective row-type map is a permutation `π`; the inverse row swap and `τ₀.symm` are absorbed into `(π, τ)` |
| the assembly of (a) | `iso2_classes_single` (a): `FibreGram 0 U` is act 12's action by the phases `c` on the tuple `star (K i j) * K i k / 4`, which is `(π, τ) F(z)` entrywise by `fibreGram_unique` and `Matrix.of_apply`; `gramPhaseEquiv_symm` gives the direction stated |
| the converse (b) | `iso2_classes_single` (b): act 23's `hadamard_z_admissible`, act 12's `sh1_necessity`, and `ISO1` (i) `relabel2_realizable` at the constant `Γ₀` |

**Every step was derived from the pinned blobs and nothing was imported**: the route reaches
outside act 12's merged sufficiency theorem, act 23's merged admissibility, act 12's necessity
theorem and elementary algebra at no step, and no classification of complex Hadamard matrices, of
any order, is consumed or cited as a step. **This is a statement about the exact configuration
frozen**, and nothing is asserted at the product configuration, at any other visible family, at
`|A| > 1` or at any other `Γ`.

**`ISO2-P`, the product cell — outcome `ISO2-P-UNDECIDED`**, with the frozen obstruction:

> **The frozen `ISO2-P` `UNDECIDED` sentence.**
> What the realizable classes at the product configuration are is undecided in this round: the
> freeze names no route, the realizable tuples there being the fibre-Gram data of `16 × 16`
> unitaries with entries of modulus `¼` modulo phases on rows and on columns, and nothing is
> imported to describe them. Neither a description nor its impossibility is claimed.

The cell was not attempted, the freeze naming no route; no description of the `16 × 16` case was
imported and none is asserted. **`ISO2-P` enters no label.**

## 7. `ISO3` — the classification of the surjective isometries at the single carrier

**Outcome reached: `ISO3-UNDECIDED`, the route having been run.**

> Whether every surjective isometry of the normalized space at the single-carrier configuration
> belongs to the finite family is undecided in this round, with the obstruction named
> specifically — the step of the route that did not close and what would settle it. Neither the
> rigidity label nor its negation is claimed; no isometry outside the family is exhibited, and
> the absence of a proof is not a counterexample.

**The route was run in the frozen order 1, 3, 2, with `ISO2`'s description consumed**, and the
steps reached are these:

| step | outcome | named results, or the obstruction |
| --- | --- | --- |
| 1 — the intrinsic metric of the Fourier circle | **closed** | `fourier_entry_uniform`: for each index triple one sign `s ∈ {1, −1}` and one pair of exponents `a, b ∈ {0, 1}` serve every unit `z`, the entry being `s * z ^ a * (star z) ^ b / 4`; `fourier_coord_uniform`: every coordinate of `Ψ (F(z))` is `S * z ^ A * (star z) ^ B / 64` with `S`, `A`, `B` fixed independently of `z`; `fourier_coord_diff_norm`: `‖S z^A (star z)^B/64 − S w^A (star w)^B/64‖ = ‖S/64 − S (star z * w)^A (star (star z * w))^B/64‖` at unit `z`, `w`, the factor `z^A (star z)^B` having norm one; `fourier_circle_metric`: `d (F z) (F w) = d (F 1) (F (star z * w))` for unit `z`, `w`, with `d` bound to the displayed equation — a statement about the Fourier circle and about nothing else, classifying no isometry |
| 3 — the optional lemma `ISO3-L` | **not obtained** | the classical extension theorem — a distance-preserving map of a subset of a real inner-product space into itself extends to an affine isometry of the affine hull — is not available in the kernel's library in a form applicable to the image of the realizable tuples in `((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → ℂ` read as a real inner-product space, and was not proved here; what would settle it is a kernel proof of that extension theorem for subsets of a finite-dimensional real inner-product space, applied to the normalized space |
| 2 — the special classes and the finiteness argument | **not obtained** | no argument was derived from the circle's intrinsic metric of step 1 and the cross distances `d ((π, τ) F(z)) ((π', τ') F(w))` to the four-shape conclusion: neither that the classes with an exceptional distance profile are exactly the intersection points of distinct circles, nor that an isometry preserving each circle and that finite set agrees on classes with a member of the family, was derived, and no theorem quantifying over an isometry of the normalized space was stated; what would settle it is a kernel proof that every map with the three hypotheses permutes the finite union of relabelled Fourier circles circle by circle and is on each circle a member of the family, or the affine extension of step 3 followed by a finite-dimensional argument on the affine hull |

**The label is earned by the step not reached and by nothing else**: no theorem
`iso3_isometries_single` exists, no theorem `iso3_not_rigid_single` exists, **no isometry outside
the family is exhibited, and the absence of a proof is not a counterexample**. No candidate
isometry outside the family was found or sought, so no witness is recorded with a span, and no
partial result on any substituted domain — the Fourier circle alone, a finite set of classes, the
dephased matrices without the passage through act 12's theorem, the whole tuple space or the whole
feature image — is reported as a verdict of this round; `fourier_circle_metric` is a step of the
route and earns no label.

**The three hypotheses are the whole of what the classification would have assumed** —
realizability preserved, surjectivity on classes, isometry on realizable tuples, as the freeze
displays them — and **no linearity, affinity, continuity or compactness was assumed** anywhere: no
statement of this round quantifies over an isometry of the normalized space at all, and the four
results of Section D assume nothing of any map. Descent was never a hypothesis. Act 24's `GEO1-T`
stays undecided and was not reopened.

**`ISO3-L`, the optional lemma — outcome `ISO3-L-UNDECIDED`**, with the step named in the table:

> **The frozen `ISO3-L` `UNDECIDED` sentence.**
> Whether every map satisfying the three hypotheses extends to an affine isometry of the real
> affine span of the normalized space is undecided in this round, with the step named; it enters
> no label, and linearity is assumed of no isometry anywhere in this round.

**`ISO3-P`, the product cell — outcome `ISO3-P-UNDECIDED`**, not attempted, the realizable classes
there not being described:

> **The frozen `ISO3-P` `UNDECIDED` sentence.**
> Whether every surjective isometry of the normalized space at the product configuration belongs
> to the finite family is undecided in this round, the realizable classes there not being
> described and nothing being imported to describe them. Neither label is claimed.

Neither `ISO3-L` nor `ISO3-P` enters any label.

> **THE CLAUSE, carried at this mention — the classification, where the family is or is not all of the isometries.**
> Act 25 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 8. `ISO4` — the prefix-constrained corollary at the single carrier

**Outcome reached: `ISO4-NOT-EXECUTED`**, by the gate.

> The corollary for transition families was not executed, the classification of the isometries
> not having reached its rigidity label; no sentence of this round reports anything about it.

The route the corollary would have taken is the freeze's and is reported here as the freeze's route
and not as anything executed: `PreservesAdmissible` read into the first hypothesis of `ISO3`,
`Reversible`'s second conjunct into the second, the isometry proposition into the third, and `ISO3`
applied at each `t`. No theorem `iso4_prefix_isometry_single` exists, no statement of this round
names `ProperAt`, `PropagatesFrom`, `EvolvesTotally`, `PreservesAdmissible`, `Reversible`,
`LadderConds` or `FactorizesOnProduct`, and no partial execution of the closed target is reported as
anything.

**`ISO4-P`, the product cell — outcome `ISO4-P-NOT-EXECUTED`:**

> **The frozen `ISO4-P` `NOT-EXECUTED` sentence.**
> The corollary at the product configuration, with factorization among its hypotheses, was not
> executed, the isometries there not being classified; no sentence of this round reports anything
> about it.

## 9. The outcome vector, and what it is not

The headline is row 4 of the freeze's outcome-vector table, selected verbatim and reported in no
other wording, and it is stated once, at the head of this note. **No verdict was inferred from
another beyond the consumptions the freeze places.** Each of the four labels is earned by its own
target's theorems or by the gate and by nothing else: `ISO1`'s by `iso1_family_acts`, `ISO2`'s by
`iso2_classes_single`, `ISO3`'s by the recorded non-attainment of steps 3 and 2 of its route,
`ISO4`'s by the gate rule; the consumptions the freeze places are `ISO2`'s description in `ISO3`'s
route, which consumed it and did not close, and `ISO3` in `ISO4`, which was not executed. The gate
record is §3.8. No single-label headline, no summary label and no combination label exists for this
round.

## 10. The route-authorization matrix, as honoured

**The route-authorization matrix is honoured**: each construction was used for its own target and
for nothing else, no fact learned during a later target's work was assigned to an earlier target, and
no alternative was substituted for a named one.

| construction or route | used for | used for nothing else |
| --- | --- | --- |
| the coordinate permutations of the three generators, the reindexing of the sum, the row-phase lemma, the transpose's admissibility and descent, the six relations | `ISO1` | consumed by `ISO2` (b) as `ISO1` (i), not re-proved there |
| the dephasing through `sh1_sufficiency`, the unit-modulus identity, the finite case analysis over the placement of the antipodal pairs, the converse through `hadamard_z_admissible`, `sh1_necessity` and `ISO1`'s relabelling fact | `ISO2` | consumed by `ISO3`'s route as `ISO2`'s verdict |
| `ISO2`'s description consumed; the intrinsic metric of the Fourier circle; the cross distances; the special points; the optional extension lemma | `ISO3` | step 1 obtained, steps 3 and 2 not; no witness found |
| `L1`, `L3s` and isometry read into `ISO3`'s hypotheses; `ISO3` consumed | `ISO4` | not executed |
| the shared lemmas of the module commit | consumed | answer no target by themselves |

**The execution order `ISO1` → `ISO2` → `ISO3` → `ISO4` was followed**, one verdict commit per
executed target, the gate read between each, no target executed out of order, and no closed target's
route attempted for information.

## 11. The scope boundary as honoured

**Nothing here derives, recognises or approaches quantum evolution**, and nothing here says that any
generator, the family, the normalized space or any isometry is, resembles, approximates or points
toward it, a quantum symmetry, an antiunitary map, a time reversal or unitarity; no continuity in
time, composition in time, semigroup law, generator or one-parameter structure is introduced, and the
parameter `z` of the Fourier family is a parameter of a frozen tuple and not a time, a flow or a
generator, the rotations of the Fourier circle being no dynamics.

**No theorem is attributed to the literature, none of its theorems is consumed, no classification is
imported and no weaker domain is substituted.** The complex-Hadamard, Euclidean-isometry and
Wigner-type literature is cited by the freeze as the provenance of the route; `ISO2`'s description is
this round's and is proved here from act 12's merged theorem, and `ISO3`'s label is earned by the
step not reached and not by any imported fact.

**Every earlier act's historical verdicts stand unchanged**, acts 12 through 24's: act 12's
classification, act 21's census, `SIOP-YES` and `L-WIDE`, act 22's three verdicts, act 23's four, and
act 24's twelve isometry verdicts and seven cells, `b`, `a2` and `a4` undecided as act 24 records
them and not closed by anything here. **Act 16's cancellation cell and the threading question are
untouched in either direction.** **Act 18's `D`-axis is untouched.** **Act 10's anchor-axis
reclassification is untouched.** Act 14's four carriers are not read and no carrier is adopted as
the physical one.

**No generator outside the frozen four was tested, no normalized space or geometry outside the frozen
one, no configuration outside the frozen two, no decomposition other than `e = Equiv.refl`, and no
equivalence outside the frozen quotient list was used in any verdict.** No fifth generator, no second
normalized space or geometry, no further equivalence, rung, configuration or control, no description
of the product configuration's classes, no strengthening of a merged theorem and no universal
implication for a cell recorded undecided in advance was discovered, and none was executed.

## 12. The non-adoption clause, carried verbatim at each mention

**THE CLAUSE is carried three times in this note** — at the headline, at the classification, and
here — each carriage opening with its own naming line and carrying the complete frozen clause, from
"Act 25 classifies" to "approaches quantum evolution.". Where a frozen byte-fixed sentence carries
the clause's substance in its own wording — the status rule's sentences and the `P0` row's sentence —
no quotation is inserted inside the quotation, as the freeze directs. **No law is adopted, endorsed or
given physical status by surviving, and the family and the normalized space are adopted as nothing**:
not as a symmetry group, not as a selector, not as a principle, not as the physical geometry.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 25 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 13. The frozen `P0` sentence for the case reached

**Case A** — `ISO0` silent, row 4 with the cells as predicted — is the case reached, and its sentence
is the frozen sentence with every clause as written for Case A, none of the variable clauses
replaced. It is appended, verbatim, to the `P0` row of `verification/ROADMAP.md` after act 24's
sentence in the same cell, and the row's label stays **OPEN** and two-part:

> Act 25 tests, in one gated round with four separately frozen targets, whether the finite family generated by the independent relabellings of fibres and of matrix indices, the entrywise conjugation and the dilation transpose acts on the realizable classes of act 24's geometry at act 12's and act 21's frozen configurations, whether every realizable class at the single-carrier configuration is the class of a relabelled Fourier tuple at a unit parameter, derived from act 12's sufficiency theorem alone, whether every surjective isometry of that normalized space belongs to the family, and whether every transition family satisfying the conditions before naturality and isometry acts on classes as a member of it. The family acts: each generator preserves realizability, descends to classes and is an isometry, and every word in the generators reduces to one of four shapes. Every realizable class at the single-carrier configuration is the class of a relabelled Fourier tuple at a unit parameter, and every such tuple is realizable, each direction proved separately and nothing imported. Whether every surjective isometry of the normalized space at that configuration belongs to the family is recorded undecided, with the step named; no isometry outside the family is exhibited, and the absence of a proof is not a counterexample. The corollary for transition families was not executed. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no verdict is inferred from another beyond the consumptions the freeze places; no condition is adopted; the family and the normalized space are named objects of test and are not adopted as the physical ones; no generator is read as a symmetry, an antiunitary map or a time reversal; nothing is asserted at the product configuration beyond its recorded undecided cells, and nothing at any other configuration; acts 12 through 24's own verdicts stand exactly as they state them; nothing here introduces continuity, composition in time or a generator; and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

## 14. What no outcome licenses, and the status rule as honoured

The freeze's twenty forbidden sentences are honoured in terms. No sentence of this round says that
any generator, the family or any isometry is, resembles, approximates or points toward a quantum
symmetry, an antiunitary map, a time reversal, unitarity or quantum evolution, the conjugation being
the entrywise `star` and the transpose the matrix transpose of the dilation (1); none says the family
is the physical symmetry group, the geometry the physical geometry, or that the isometries select
(2), the non-adoption clause governing; `ISO2`'s theorem is attributed to no literature and no
literature's classification is used as a step (3); no target's verdict is inferred from another's
beyond the placed consumptions (4); no positive label is claimed from the absence of a counterexample,
from a route that failed to close, or from anything but the named route (5); the family is not said
to be complete because no other isometry was found, `ISO3` being undecided (6); no earlier act's
verdict, witness or obstruction is rewritten or reinterpreted, act 24's `b`, `b₀` and act 21's
`L-FAMILY` obstruction standing as they state them (7); `ISO1-R`'s outcome is a fact about one
relation and one family and is not read as a programme statement (8); the isometry group of no space
is stated, the normalized space at the single carrier included, beyond the label earned (9); the
geometry is identified with no named geometry of any other theory (10); no isometry is assumed
linear or affine and Mazur–Ulam is invoked nowhere, `ISO3-L` being undecided (11); nothing is said
about the threading, the cross-time representative, act 16's cell, act 14's carriers, act 18's
`D`-axis, act 10's anchor axis, Track I, Source B or C, or the substratum rounds (12); `P0` is not
closed and neither is either of its parts (13); no merged statement is strengthened, superseded or
extended, `ISO2`'s description being a theorem about act 12's realizable set that enlarges no merged
statement (14); no continuity, smoothness, generation, one-parameter structure or composition in
time is imported (15); OI and QM are not said to be inequivalent (16); the generator list is not said
to be exhaustive and the family is not called the only natural family (17); the headline is the
vector and no single label (18); nothing is said about the realizable classes at the product
configuration beyond the recorded obstruction (19); and no verdict about a substituted domain is
reported as a verdict of this round, `fourier_circle_metric` being a step of a route and earning
nothing (20). Every target is reported with its frozen sentence, and no outcome reached its wording
by any other route.

## 15. The relation to acts 7, 12, 13, 17, 18, 20, 21, 22, 23 and 24

| act | what is consumed | at what strength |
| --- | --- | --- |
| act 7 | `AdmissibleDilationAt`, the readback convention, `D4b` negative, `D5` NOT CERTIFIED | merged; none re-proved |
| act 12 | `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `fibreGram_apply`, `sh1_necessity`, `sh1_sufficiency`, `gramPhaseEquiv_cross_invariant`; its classification recorded by `ISO0` as the fibre-Gram characterization of the realizable tuples and not a description of the classes | merged; none re-proved; no merged statement enlarged |
| act 13 | its `P0` threading sentence | untouched; named as what this round does not touch |
| act 17 | `GramTrajEquiv` named in the frozen quotient list; `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, `gramPhaseEquiv_trans` | merged; `GramTrajEquiv` used in no verdict |
| act 18 | `ProperAt`, `PropagatesFrom` | merged; named in no statement of this round |
| act 20 | `RelabelTransition` | merged; the diagonal case of the independent relabellings; named in no statement of this round |
| act 21 | the ladder as the declarations of its merged module, its two configurations, the frozen quotient list, the attestation set, THE CLAUSE with "Act 21" read as "Act 25"; `realizable_relabel`, `relabel_gramPhaseEquiv`, `relabel_one`, `product_realizable`, `hadamard_entries`, `ol1a_descent` | merged; the ladder consumed unrestated and named in no statement, `ISO4` not being executed; act 21's verdicts untouched |
| act 22 | its three verdicts | untouched |
| act 23 | `hadamard_z_admissible` and the Fourier matrix `H z` as the lambda its merged statements carry; `fibreGram_z_entries`, `zseq_facts` | merged; consumed as landed; the sequence not used |
| act 24 | `mixedTriple` and the frozen geometry equation; `geo1_triple_metric` with its conjuncts, `geo1_separation_single`, `geo1_equiv_of_zero_single`, `geo1_zero_of_equiv`, `realizable_entry_ne_zero`, `mixedTriple_relabel`, `geo2_relabel_isometry`, `mixedTriple_star`, `conj_eq_transpose`, `realizable_conj`, `conj_conj`, `conj_gramPhaseEquiv`, `geo3_phiConj_isometry`, `geo4_a0_isometry_injective`; its twelve verdicts, its `b₀` witness and its `b` obstruction recorded by `ISO0`; its observation for this round | merged; consumed as landed; `mixedTriple_star`, `realizable_conj` and `conj_conj` used in the kernel, the rest consumed as the freeze places them — the normalized space's definition and the descent of `C` — and used in no proof; its undecided cells not closed |

**No merged label is revised.** **A merged statement is not enlarged by being consumed.** The
direct-branch statement is carried unchanged: `D4a` positive on the direct branch; `T1` **necessary,
not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what fraction of OI
lies in the direct sector**; `D5` NOT CERTIFIED.

## 16. The definition budget

**Zero slots were budgeted, and no definition was introduced.** The module carries no top-level
`def`, `abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque` at any commit; the normalized
space, the four generators, the transpose relation, the geometry, the Fourier matrix, the dephasing
phases and the permutations are bound variables or written-out expressions in the statements that
need them, the invariant family is act 24's `mixedTriple` consumed, and every rung is act 21's
declaration, named in no statement. **Thirty-six named results.**

## 17. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants**, with `B = dd3bd2e726e0fb3bccd96df9c46a532119a9ee97`, certified through the validator's
prospective path by the one keyed call `_si2_authority('OGC', tag='R7-OGC')`. The question is asked
of the real `pull_request.head.sha` in pull-request continuous integration and of `HEAD` otherwise,
**never** of the synthetic merge commit; an unresolvable head **fails closed** with no fallback; the
check excludes pre-freeze side history by requiring every commit in `git rev-list H ^B` to be itself
a descendant of `B`; and the guard recovers whatever history it needs and fails if recovery fails.

**The validator's classification of `OGC`**: `EXECUTION` at every head of the execution, printed by
the `R7-OGC` clause from the packaging commit on and read at `E` from the continuous-integration log
of the certification of record; `LANDED-PENDING-PIN` at `L`, permitted there and failing every
descendant as seal pending; `ARCHIVED` from `P`, which writes `verification/seals/OGC.json` with its
three fields and removes the `OGC` entry from the prospective declaration, and touches nothing else.

**The supersession table is empty and is honoured as empty**: no contract of any closed round was
edited, at any commit of this branch; at the stage-A commit and at every later head every closed
round's guard classifies its own record and passes.

**`SI-3`'s standing zero-legacy-statement contract holds at every head**: `_SI2_LEGACY_RE` finds zero
assignment statements in the guard file at `B` and at every commit of this branch, and no name
matching `_OGC_(BASE|SEALED_HEAD|MERGE)` exists anywhere.

### The ten preconditions, each at its scope, as the base check reported them at `M` and at `B`

The freeze's machine-checkable block carries twenty-six `frozen-blob` lines and twenty-one rows;
the base check reported `OK (mode M, 21 row(s), no failure)` at the candidate merge of pull request
#691 on run 35470058510 and `OK (mode B, 21 row(s), no failure)` at `B` on run 35470951442.

| # | scope | precondition | result |
| --- | --- | --- | --- |
| 1 | `D` | the names were free when chosen | **PASS** — rows `d1-tag-free`, `d1-stem-free`, `d1-bare-free`, `d1-module-free`, `d1-dir-free`, `d1-act-free`, `d1-target-free`, `d1-theorem-prefix-free`: measured at `D`, recorded, `D` an ancestor of `B` |
| 2 | `D` | the seals tree at `D` is the pinned one | **PASS** — row `d2-seals-tree`, `ffb92daab9ea2f3d64c47b9c73e4b9c3466b763f`, twenty-nine records |
| 3 | `D` | the guard at `D` is green and carries no legacy constant | **PASS** — eighty-eight tags on run 35467053564; zero legacy statements |
| 4 | `D → B` | `D` is an ancestor of `B` | **PASS** — row `db4-ancestor` |
| 5 | `D → B` | the blobs this round consumes are unchanged | **PASS** — twenty-six `frozen-blob` lines, each matched at `M` and at `B` |
| 6 | `B` | no act 25 execution object exists | **PASS** — rows `b6-guard-clean`, `b6-no-record`, `b6-no-module`, `b6-dir-control-plane-only` |
| 7 | `B` | no round is executing at `B` | **PASS** — row `b7-no-prospective`, `_MANIFEST_PROSPECTIVE = {}` at `B` |
| 8 | `B` | acts 23 and 24 are sealed at `B` | **PASS** — rows `b8-olg-sealed`, `b8-ogs-sealed`, `b8-olg-guard` and `b8-ogs-guard` |
| 9 | `B` | act 24's module is wired | **PASS** — row `b9-import-ogs` |
| 10 | `B` | this control plane is in the tree at its path | **PASS** — row `b10-self-present`, and the blob verified by `git hash-object` as the first act |

**No sibling lane's merge is a precondition of this round**, and none was waited for.

**The claim is scoped to the repository record.**

## 18. The axiom table — one line per named result

| named result | axioms |
| --- | --- |
| `mixedTriple_relabel2` | `[propext, Classical.choice, Quot.sound]` |
| `fibreGram_unique` | `[propext, Classical.choice, Quot.sound]` |
| `mixedTriple_transpose` | `[propext, Classical.choice, Quot.sound]` |
| `rows_phase` | `[propext, Classical.choice, Quot.sound]` |
| `transpose_admissible` | `[propext, Classical.choice, Quot.sound]` |
| `antipodal` | `[propext, Classical.choice, Quot.sound]` |
| `dephase` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_entry_monomial` | `[propext, Classical.choice, Quot.sound]` |
| `relabel2_realizable` | `[propext, Classical.choice, Quot.sound]` |
| `relabel2_gramPhaseEquiv` | `[propext, Classical.choice, Quot.sound]` |
| `relabel2_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `conj_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `transpose_single_valued` | `[propext, Classical.choice, Quot.sound]` |
| `transpose_unitary` | `[propext, Classical.choice, Quot.sound]` |
| `transpose_descends` | `[propext, Classical.choice, Quot.sound]` |
| `transpose_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `relabel2_dilation` | `[propext, Classical.choice, Quot.sound]` |
| `conj_dilation` | `[propext, Classical.choice, Quot.sound]` |
| `conj_relabel2` | `[propext, Classical.choice, Quot.sound]` |
| `relabel2_relabel2` | `[propext, Classical.choice, Quot.sound]` |
| `iso1_word_normal_form` | `[propext, Classical.choice, Quot.sound]` |
| `iso1_family_acts` | `[propext, Classical.choice, Quot.sound]` |
| `iso1_single_carrier` | `[propext, Classical.choice, Quot.sound]` |
| `iso1_product_carrier` | `[propext, Classical.choice, Quot.sound]` |
| `row_forms` | `[propext, Classical.choice, Quot.sound]` |
| `core_row_norm` | `[propext, Classical.choice, Quot.sound]` |
| `perm_of_rows` | `[propext, Classical.choice, Quot.sound]` |
| `rows_injective` | `[propext, Classical.choice, Quot.sound]` |
| `core_nonreal` | `[propext, Classical.choice, Quot.sound]` |
| `core_real` | `[propext, Classical.choice, Quot.sound]` |
| `classify_dephased` | `[propext, Classical.choice, Quot.sound]` |
| `iso2_classes_single` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_entry_uniform` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_coord_uniform` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_coord_diff_norm` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_circle_metric` | `[propext, Classical.choice, Quot.sound]` |

No `sorry`, no `native_decide`, no added axiom; `lake build OIBridge.OrbitGeometryIsometries` completes
with zero errors and one linter warning, the unreferenced binder name of §3.7.1; the `ISO1` verdict commit builds
with zero errors and zero warnings.

## 19. The predictions, reported against their outcomes

| target | prediction | outcome | reported as |
| --- | --- | --- | --- |
| `ISO0` | negative, high | `ISO0`-silent | **as predicted** |
| `ISO1` | `ISO1-FAMILY-ACTS`, high | `ISO1-FAMILY-ACTS` | **as predicted** |
| `ISO1-R` | `T-NEW`, low, an observation entering no label | `ISO1-R-UNDECIDED`: the finite check not carried out | **not as predicted**; enters no label |
| `ISO2` | `ISO2-CLASSIFIED`, medium | `ISO2-CLASSIFIED` | **as predicted** |
| `ISO2-P` | `UNDECIDED`, high | `ISO2-P-UNDECIDED` | **as predicted**; enters no label |
| `ISO3` | `ISO3-UNDECIDED`, medium for the label; the sign read positive at low strength | `ISO3-UNDECIDED`, the route run, step 1 closed, steps 3 and 2 not obtained; the sign neither confirmed nor refuted | **as predicted** for the label; the sign untested |
| `ISO3-L` | `HOLDS`, medium, entering no label | `ISO3-L-UNDECIDED` | **not as predicted**; enters no label |
| `ISO3-P` | `UNDECIDED`, high | `ISO3-P-UNDECIDED` | **as predicted**; enters no label |
| `ISO4` | `ISO4-NOT-EXECUTED`, medium, following `ISO3` | `ISO4-NOT-EXECUTED` | **as predicted** |
| `ISO4-P` | `NOT-EXECUTED` in advance | `ISO4-P-NOT-EXECUTED` | **as predicted**; enters no label |

## 20. The observation for a later round, stated once and narrowly

**No observation for the product configuration is recorded**: `ISO3` did not reach its positive
label, so what a positive `ISO3` would have supplied to a later round that freezes the product
configuration's description is not supplied, and nothing about the product configuration is asserted
beyond the recorded undecided cells. The anti-expansion rule collected no observation: no fifth
generator, no second normalized space or geometry, no further equivalence, rung or configuration, no
description of the product configuration's classes, no strengthening of a merged theorem, and no
universal implication for a cell recorded undecided in advance was noticed. What a later round on
the single-carrier classification would need is stated in §7's table as the two steps not reached,
and is an observation about the route and not a finding of this one.

## 21. The provenance as honoured

The equivalence is act 12's at blob `4bba2040c33424fafbc6d31c0d63b86dff33691a`, consumed unrestated;
the rungs are act 21's declarations at blob `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8`, restated
nowhere and named in no statement; the invariant family and the geometry are act 24's at blob
`ce9d1aa05dfdedfb5cac171cfe6379681942195f`, consumed and never redefined; the Fourier matrix is act
23's lambda at blob `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1`; the quotient list, the two
configurations and the non-adoption clause are act 21's unchanged, the clause with "Act 25" in its
first sentence as the freeze directs; the family, its normal form and the normalized space are this
freeze's, bound by formula and by equation; the classification route is the freeze's reading, with
the complex-Hadamard, Euclidean-isometry and Wigner-type literature as its provenance and as the
provenance of no theorem. The freeze is not edited.

## 22. The discrepancies — recorded and not repaired

**Three items are recorded. None is repaired, and the frozen document is not edited.** Each is a
detail of the freeze's reading that the kernel represents differently; the labels are earned by
what the kernel proves and by nothing stated in the reading, and no value, no step and no outcome
turns on any of them.

**DF1 — the composition of two relabellings, written "`(π ∘ π', τ ∘ τ')`".** The freeze's sixth
relation reads `(π, τ) ∘ (π', τ') = (π ∘ π', τ ∘ τ')`. Applying `(π', τ')` first and then `(π, τ)`
gives, entrywise, `G (π' (π i)) (τ' (τ j)) (τ' (τ k))`, whose fibre permutation is `π' ∘ π`, that is
`π.trans π'` in the kernel's notation; `relabel2_relabel2` proves the relation with
`(π.trans π', τ.trans τ')`, and `iso1_family_acts`'s fifteenth conjunct states it that way. The
freeze's `∘` is read as the composition in the order the relation's left side applies the two
relabellings, and the wording is not repaired.

**DF2 — the exponent of the Fourier coordinates, written "`± z ^ k / 64` for an integer `k` with
`−3 ≤ k ≤ 3`".** The kernel states each coordinate of `Ψ (F(z))` as `S * z ^ A * (star z) ^ B / 64`
with natural exponents `A`, `B` on `z` and on `star z`, each the sum of three exponents in `{0, 1}`
(`fourier_coord_uniform`, which carries the exponents and not their bound), which at `star z * z = 1`
is `S z ^ (A − B) / 64` with `A − B ∈ [−3, 3]`; the integer exponent is never
formed, and the intrinsic-metric identity is proved through the factorization
`z ^ A (star z) ^ B · (1 − (star z · w) ^ A (star (star z · w)) ^ B)` instead. The value is the same
and the representation is not repaired.

**DF3 — the dephasing phases, written "`r i := 2 * star (u i 0)`" and "`c j := 2 * star (u 0 j) * (2 * u 0 0)`".**
The kernel's `dephase` names `r i = 2 * U (i, 0) (0, 0)` and `c j = 4 * star (U (0, 0) (0, 0)) * U (0, 0) (j, 0)`
— the conjugates of the freeze's two phase vectors — and writes the dephased matrix as
`K i j = 2 * star (r i) * star (c j) * U (i, 0) (j, 0)`, which is the freeze's `K i j = 2 * r i * u i j * c j`
entry for entry; the phase action carrying `FibreGram 0 U` to the tuple of `K / 2` is by the kernel's
`c`, the conjugate of the freeze's. The matrix, the moduli and the equivalence are the same, and the
naming is not repaired.

**No start-state discrepancy arose**, in any of the twenty-six pinned blobs, in any of the four
files written onto, or in any of the ten preconditions: **every one matches** and **all ten pass**.
**No candidate discovered during execution was executed.** **No configuration was chosen after an
outcome was known.** **No alternative witness was substituted for a named one.** **No target was
executed out of order, and no verdict commit carries a later target's result.** No closed round's
contract failed on any head of this branch, so no amendment is called for.

## 23. The provenance of this note

Every frozen sentence in this note — the `ISO0`-silent sentence, the `ISO1-FAMILY-ACTS`,
`ISO2-CLASSIFIED`, `ISO3-UNDECIDED` and `ISO4-NOT-EXECUTED` sentences, the `ISO1-R`, `ISO3-L`,
`ISO2-P`, `ISO3-P` and `ISO4-P` carriages, the outcome-vector row, the `P0` sentence, the ordering
obligation, the anti-contamination invariant and the three carriages of THE CLAUSE — was extracted by
line range from the frozen preregistration blob `f4892f64…` at `B` and not retyped, and the
`R7-OGC` clause pins each by the same extraction.
