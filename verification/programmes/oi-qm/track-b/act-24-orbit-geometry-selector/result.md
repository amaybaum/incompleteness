# Track B act 24 — the orbit-geometry selector audit: the mixed-triple invariants, the metric they induce, its controls, the twelve families against it, and the rigidity cells, at act 12's and act 21's configurations: RESULT

Executed under the frozen control plane `preregistration.md` in this directory, blob
**`3b61d6c90fe3f05bbf5e791f74d7106e9be2f94a`**, from `main` at **`d0fcdbc03c4b828d630f677253cf0914f451b63d`** —
the certified merge commit of that control plane, the round's mandated execution base `B`, certified
by main-push run 35458160449 with all four jobs green and the control-plane base check in mode `B`
reporting twenty-five rows and no failure — which this execution verified by blob as its first act,
before any target was executed.

**Outcome vector:** `GEO1-METRIC` · `GEO2-CONTROLS-PASS` · `GEO3-DISCRIMINATES` · `GEO4-UNDECIDED`

**The headline is row 2 of the freeze's outcome-vector table, verbatim.** `GEO0` silent; `GEO1`
landed by `geo1_triple_metric`; `GEO2` landed by `geo2_relabel_isometry`, `geo2_twoSided_trivial`
and `geo2_product_tensor`; `GEO3` landed via `ΦCTRL` and `Φ_SC`, with every family of the twelve
recorded; `GEO4` undecided on `b`, with `a0` holding, `a1` and `a3` `NOT-IMPLIES`, `b₀` `NOT-RIGID`,
`a2` and `a4` undecided. Every verdict is of the exact frozen proposition at the exact configuration,
with the geometry and every family bound by equation, and of nothing in its neighbourhood. **No
verdict was inferred from another beyond the consumptions the freeze places.** **No independence of
conditions is asserted and no characterization of the isometries is made.** **No theorem is
attributed to the literature and no completeness is asserted past the base-star hypothesis.**
**Every earlier act's historical verdicts stand unchanged**: acts 12 through 23's labels are consumed
as landed, and this round's labels are earned under this freeze about the geometry alone.

> **THE CLAUSE, carried at this mention — the headline.**
> Act 24 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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
| the mandated execution base | the prospective declaration `_MANIFEST_PROSPECTIVE = {'OGS': 'd0fcdbc03c4b828d630f677253cf0914f451b63d'}` in `verification/lean/edge_rigidity_probe.py` | **declared**; the validator classifies `OGS` as `EXECUTION` against it | **removed** by `P` |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': 'd0fcdbc03c4b828d630f677253cf0914f451b63d', 'authorized': ('OGS',)}` | the twenty-eight records of the seals tree `9f762b8d0b5656950e5030c4eb9ca6514362cce0` at `B`, plus the one addition authorized by stem | unchanged |
| the round's manifest record | `verification/seals/OGS.json` | **absent** | **written by `P`**: `{"round": "OGS", "kind": "sealed", "base": "d0fcdbc03c4b828d630f677253cf0914f451b63d", "sealed_head": E, "merge": L}` |

**`OGS.json` is absent at execution and is written by `P` and by nothing before `P`.** That is a
statement about this execution and stays true as one. **No legacy seal constant is written**: nothing
matching `_OGS_(BASE|SEALED_HEAD|MERGE)` exists at any commit of this branch, and `SI-3`'s standing
contract — zero legacy assignment statements in the guard file — holds at every head. **No existing
manifest record is altered**: the twenty-eight records at `B` are read and never written, and the
chronology verdict is the validator's through one keyed call, `_si2_authority('OGS', tag='R7-OGS')`.
**No closed round's contract is edited**: the supersession table is empty, and every closed round's
guard reads its own record at every head of this branch.

**The base-blob verification is recorded.** `git cat-file -p d0fcdbc0:verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/preregistration.md | git hash-object --stdin`
returns `3b61d6c90fe3f05bbf5e791f74d7106e9be2f94a`, the blob the freeze names and the blob the
`R7-OGS` clause pins; `git rev-parse d0fcdbc0:…/preregistration.md` returns the same.

**The files this round writes** are the new module `verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean`,
this result note, one import line in `verification/lean-mathlib/OIBridge.lean` (directly after act
23's module, line 213), one census entry in `verification/lean-manuscript-census.json`, the `R7-OGS`
clause with the two declarations in `verification/lean/edge_rigidity_probe.py`, and the frozen
post-round sentence appended to the `P0` row of `verification/ROADMAP.md` after act 23's. **No
manuscript file is written.**

## 2. The start state

**Every one of the twenty-three paths the freeze pins by blob was checked at `B` by `git rev-parse`,
and every one matches**; they are the `frozen-blob` lines of the freeze's machine-checkable block,
which the base check verified at `M` (run 35457437686, at the candidate merge of pull request #689)
and at `B` (run 35458160449). The four files this round writes onto carry their pinned blobs at `B`:
`verification/ROADMAP.md` at `d03aa6602d8536ab8aab29dd09ea7602de4d7e78`,
`verification/lean/edge_rigidity_probe.py` at `f7a87a38cf04e19be90a96d48d6852e1dccea058`,
`verification/lean-mathlib/OIBridge.lean` at `87a71880518adc9b31672b807323d24270eedfe9` and
`verification/lean-manuscript-census.json` at `3ade6a83dab02e91c3e7837a4f4b3a77cef48352`. The seals
tree at `B` is `9f762b8d0b5656950e5030c4eb9ca6514362cce0`, twenty-eight records, twenty-two `sealed`
and six `base-only`, no `OGS.json`, the same tree as at `D`.

**No start-state discrepancy arose in any pinned blob.** `D = 9907d3ac…` and `B` are distinct
commits, as the freeze reads them: the drafting-time facts are facts about `D`, the pins are read at
`B`, and every pinned blob is the same at both, the tree at `B` differing from the tree at `D` by
exactly the one added preregistration file (1990 lines, no other path). `B`'s parents are `D` and
`98b567578098ff3bf6e3576d94302c7d3a2157b1`, the head of pull request #689.

**The anti-contamination invariant is honoured**, carried in the freeze's own wording:

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

Sibling lanes present at `B` are not inputs and none was read. The start-state table is the complete
list of what this round consumes.

## 3. The ordering obligation's records

The obligation, in the freeze's own wording, which binds this execution:

> **The ordering obligation, act 24.** The rungs are act 21's declarations at blob `860daac4…`, the
> equivalence is act 12's at blob `4bba2040…`, and nothing else. The execution's module **states no
> rung, no equivalence, and exactly one top-level definition, `mixedTriple`, with the body this
> freeze displays**; the geometry is bound, in every theorem that names it, to the equation this
> freeze displays, and every family is bound, in every theorem that names it, to the equation its
> merged verdict carries — `Φ_conj` to the entrywise `star`. From the first commit that adds the
> module to the certified head `E`, **no commit of the branch adds a second definition, alters the
> one definition's body, restates a rung, alters the geometry's equation, or uses an equivalence
> outside the frozen quotient list**; the module commit carries no verdict of any target; the
> verdict commits of the executed targets follow it in the order `GEO1`, `GEO2`, `GEO3`, `GEO4`;
> and no theorem block in one family's subsection of `GEO3` names another family.

**Eight records, each checkable by an auditor from the branch alone.** The execution branch is
`claude/act-24-execution`, rooted at `B`, and its first-parent chain from `B` is, in order:

| # | commit | content |
| --- | --- | --- |
| 1 | `34e70f2ce033a9d92cea05f5a0713ae18f608d18` | **stage A**: the two declarations set to `B`, in the guard file only |
| 2 | `11c0383a056718ca019f99568aaa95fb16d14c61` | **the module commit**: Section A, the one definition and the fourteen shared lemmas, plus the import line; no verdict |
| 3 | `774aea83af37da4003f85425d00b3e114235a42d` | `GEO1`: `geo1_triple_metric` and its twelve supporting results |
| 4 | `5e85dfd3bb86a0fd188c1c35ca01f17a4947ba90` | `GEO2`: `geo2_relabel_isometry`, `geo2_twoSided_trivial`, `geo2_product_tensor`, `geo2_controls` and two supporting results |
| 5 | `37099179aebeea32773eb70a85f670f6108a6601` | `GEO3`: the twelve family theorems and four supporting results |
| 6 | `babe01cfb3c7016392896731afa9b47c4d2556b7` | `GEO4`: `geo4_a0_isometry_injective`, `geo4_a1_l5_not_implies_geo`, `geo4_a3_geo_not_implies_l5`, `geo4_b0_not_relabel_rigid` and nine supporting results |

followed by the packaging commit carrying this note, the `R7-OGS` clause, the `ROADMAP` sentence and
the census entry, and by whatever certification fixes as `E`.

### 3.1 The declaration table (record 1)

| object | the merged declaration consumed, with its line range at its blob | this round's module |
| --- | --- | --- |
| `GramPhaseEquiv` | `TwoSidedGauge.lean` `4bba2040c33424fafbc6d31c0d63b86dff33691a`, lines 102–103 | consumed unrestated |
| `RealizableGram` | the same, lines 108–110 | consumed unrestated |
| `FibreGram`, `fibreGram_apply`, `gramPhaseEquiv_cross_invariant`, `sh1_necessity`, `sh1_sufficiency` | the same, lines 115–116 and 168–171 and Section H | consumed unrestated |
| `RelabelTransition` | `RepresentativeNaturality.lean` `4c1137f35600320b9273c857ec62271341b05cd0`, lines 167–168 | consumed unrestated |
| `ProperAt`, `PropagatesFrom` | `IntermediateCrossTimeStructure.lean` `cb14c43b0becfe1a379ae3615d5553723ede9163`, lines 167–174 and 186–194 | the first two conjuncts of the prefix, written out |
| `EvolvesTotally` | `OrbitLawRigidityTwisted.lean` `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8`, lines 96–100 | the third conjunct of the prefix, written out |
| `PreservesAdmissible` | the same, lines 108–110 | the fourth conjunct, written out |
| `L2`, inline | the fifth conjunct of `LadderConds`, lines 179–196 | written out |
| `Reversible` | the same, lines 123–128 | the sixth conjunct, written out |
| `L4d`, inline | the seventh conjunct of `LadderConds` | written out |
| `L4n`, inline | the eighth conjunct of `LadderConds` | named in no statement of this round |
| `FactorizesOnProduct` | the same, lines 143–157 | `L5`, written out at `e = Equiv.refl` |
| `ΦI`, `ΦP`, `ΦC`, `ΦT` | `phiI_ladder` 548, `phiP_ladder` 577, `phiC_census` 746, `phiT_l2_restricts` 842, at the same blob | each pinned to its merged equation in its own `GEO3` subsection |
| `ΦPP`, `ΦCTRL` | `phiPP_ladder` 1166, `phiCTRL_census` 1282, at the same blob | likewise |
| `Φ_swap` | `phiSwap_l5_restricts`, `OrbitLawNaturalityFactorization.lean` `d41b157a3f38d4ebedbe11ad9682a8693836a383`, line 179 | likewise; consumed for cell `a3` |
| `Φ_MD`, `Φ_PC`, `Φ_HS`, `Φ_SC` | `phiMD_l1_restricts` 285, `phiPC_l3i_restricts` 447, `phiHS_l3s_restricts` 606, `phiSC_corner` 850, `OrbitLawGaps.lean` `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1` | likewise; `phiSC_corner` consumed for cell `a1` |
| `Φ_conj` | this freeze, lines 821–824: `fun _ G => fun i => Matrix.of fun j k => star (G i j k)` | pinned to that equation in its `GEO3` subsection and in cell `b₀` |
| `mixedTriple` | **this round's one definition**, the freeze's lines 568–571 | `def mixedTriple (G : V → Matrix V V ℂ) : (V × V × V) × (V × V × V) → ℂ := fun p => G p.1.1 p.2.1 p.2.2.1 * G p.1.2.1 p.2.2.1 p.2.2.2 * G p.1.2.2 p.2.2.2 p.2.1` |

**This round's module carries exactly one declaration of its own**: the line `def mixedTriple` with
the body the freeze displays, and no `abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque`
at any commit; it imports `OIBridge.OrbitLawGaps`, `OIBridge.OrbitLawRigidityTwisted` and
`OIBridge.OrbitLawNaturalityFactorization`; `R7-OGS` checks all of this mechanically at every commit
from the module commit to the certified object. **No rung was restated, no equivalence was widened,
and neither the invariant family nor the geometry was adjusted.**

### 3.2 The stage-A commit (record 2)

**`34e70f2ce033a9d92cea05f5a0713ae18f608d18`.** `git show --stat` lists one file,
`verification/lean/edge_rigidity_probe.py`, +2/−2: `_MANIFEST_PROSPECTIVE = {'OGS': B}` and
`_MANIFEST_BASELINE = {'base': B, 'authorized': ('OGS',)}`, both outside the validator's
marker-bounded regions, and nothing else. The supersession table being empty, no closed round's
contract is touched. At this commit the guard printed **eighty-seven `R7-*` tags, all `PASS`**,
`R7-OLT`, `R7-OLN` and `R7-OLG` classified `ARCHIVED`, with `OGS` declared.

### 3.3 The module commit (record 3)

**`11c0383a056718ca019f99568aaa95fb16d14c61`**, the first commit at which the module is present. It
carries the one definition and the named results **`mixedTriple_gauge`**, **`mixedTriple_cross`**, **`mixedTriple_star`**, **`coord_le_dist`**, **`zseq_dist`**, **`hadamard_i_cross_all`**, **`hadamard_one_cross_all`**, **`fibreGram_z_cross02`**, **`norm_one_of_star_mul`**, **`entry_bound_aux`**, **`fourier_entry_norm`**, **`fourier_entry_diff`**, **`fourier_coord_diff`**, **`fourier_feature_norm`** — the invariance
of every coordinate under the phase action, the cross-invariant coordinate and its value, the
conjugation of the feature map, the coordinate bound, the sequence's two distance identities, the
sixteen cross-invariants of `Gᵢ` and of `G₁`, the `(0,2)` invariant of the Fourier family, the
entry bound at unit parameters with the coordinate bound it gives, and the feature norm `1` — each a
shared lemma and none a verdict: no conjunct of any target is discharged or refuted, and no family is
named in the module at this commit.

### 3.4 The four verdict commits (record 4)

| target | commit | named results | families named, in that section only |
| --- | --- | --- | --- |
| `GEO1` | `774aea83af37da4003f85425d00b3e114235a42d` | `geo1_separation_star`, `realizable_entry_ne_zero`, `geo1_separation_single`, `geo1_separation_product`, `dist_eq_norm_toLp`, `geo1_metric_props`, `geo1_class_invariant`, `geo1_zero_of_equiv`, `features_eq_of_dist_zero`, `geo1_equiv_of_zero_single`, `geo1_equiv_of_zero_product`, `geo1_triple_metric`, `mixedTriple_continuous` | none |
| `GEO2` | `5e85dfd3bb86a0fd188c1c35ca01f17a4947ba90` | `mixedTriple_relabel`, `geo2_relabel_isometry`, `geo2_twoSided_trivial`, `mixedTriple_product`, `geo2_product_tensor`, `geo2_controls` | none |
| `GEO3` | `37099179aebeea32773eb70a85f670f6108a6601` | `fourier_dist_le`, `realizable_prod_of_adm`, `coord_cross_product`, `one_le_norm_I_sub_one`, `geo3_phiI_isometry`, `geo3_phiP_isometry`, `geo3_phiC_not_isometry`, `geo3_phiT_isometry`, `geo3_phiPP_isometry`, `geo3_phiSwap_isometry`, `geo3_phiConj_isometry`, `geo3_phiPC_not_isometry`, `geo3_phiMD_not_isometry`, `geo3_phiCTRL_not_isometry`, `geo3_phiSC_not_isometry`, `geo3_phiHS_not_isometry` | each of the twelve in its own subsection |
| `GEO4` | `babe01cfb3c7016392896731afa9b47c4d2556b7` | `conj_eq_transpose`, `realizable_conj`, `conj_conj`, `conj_gramPhaseEquiv`, `conj_cross`, `relabel_product_cross`, `conj_fibreGram_one`, `conj_fibreGram_negOne`, `conj_product`, `geo4_a0_isometry_injective`, `geo4_a1_l5_not_implies_geo`, `geo4_a3_geo_not_implies_l5`, `geo4_b0_not_relabel_rigid` | `Φ_SC` in cell `a1`, `Φ_swap` in cell `a3`, `Φ_conj` in cell `b₀` |

Each verdict theorem first appears at its own verdict commit and at no earlier commit; each verdict
commit carries its own target's results and nothing of a later target's; the order on the
first-parent chain is `GEO1`, `GEO2`, `GEO3`, `GEO4`. **The gate opened each target**: `GEO2` on
`GEO1-METRIC`, `GEO3` on `GEO2-CONTROLS-PASS`, `GEO4` on `GEO3-DISCRIMINATES`; no target has a
`NOT-EXECUTED` label.

### 3.5 The immutability span (record 5)

`git diff 11c0383a056718ca019f99568aaa95fb16d14c61 <E> -- verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean | grep -c -E '^[-+](def |abbrev |structure |class |instance |axiom |opaque )'`
**returns `0`**: no diff between the module commit and the certified head adds or removes a
definition of any kind, and no change touches the definition's block — the line `def mixedTriple`
and its body are byte-identical at every commit from the module commit on. Measured at the `GEO4`
commit and again at the packaging commit, whose only changes to the module are one docstring (§3.7.1)
and nothing inside any statement or proof, and re-run by `R7-OGS` on every head from the module
commit to the certified object.

### 3.6 The quotient and geometry record (record 6)

**The only equivalence used in any verdict is act 12's `GramPhaseEquiv`**, through
`gramPhaseEquiv_cross_invariant`, `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`,
`gramPhaseEquiv_trans`, act 23's `gramPhaseEquiv_fst_of_product`, and this round's
`mixedTriple_gauge`, `geo1_separation_star` and `conj_gramPhaseEquiv`, which are statements about it;
act 17's `GramTrajEquiv` enters only through act 18's `ProperAt` and `PropagatesFrom` as consumed in
cell `b₀`, and act 21's `LawEquiv` is not used. **The definition's body is the displayed one at every
commit, and the geometry is bound, in every theorem that names it, to
`d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)`** — as a hypothesis `hd`
in every shared lemma and control, and as the equation `d = (fun G H => …) →` in every verdict
theorem. **No equivalence was introduced or widened during execution**, no candidate equivalence was
noticed, and **neither the invariant family nor the geometry was adjusted** at any point.

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
the execution is not a YES and is listed.

#### The span `B` → module commit

| question | answer for the span `B` → module commit |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: verified the frozen blob at `B` by `git hash-object` and every other pinned blob by `git rev-parse`; wrote and committed the stage-A edits and ran the guard at that commit; read act 21's, act 22's and act 23's merged modules at their pinned blobs — the ladder declarations, `witness_supply`, `hadamard_entries`, `product_realizable`, `product_cross`, `relabel_product`, `relabel_one`, `ol1a_descent`, `phiCTRL_census`, `phiSwap_l5_restricts`, act 23's seven shared lemmas and its four verdicts — and act 12's `fibreGram_apply`, `gramPhaseEquiv_cross_invariant` and `sh1_sufficiency`, to reuse their proof shape; wrote the one definition and the fourteen shared lemmas of Section A and built them, the builds revealing compile errors in the entry-bound case analysis (a `star`-form hypothesis had to be restated for `linear_combination`) and in a sum bound (`Finset.single_le_sum` needing its function named) and then that the lemmas compile, and nothing else. Two compiler probes of the post-`simp` goal shape for two entries of the Fourier family were run in a scratch file, in service of the freeze-listed shared lemma `fourier_entry_diff` and of nothing else. No proof, search or experiment about any family's isometry status, any control, any conjunct of `GEO1` or any cell was attempted or run, no build output revealed any, and the execution reasoned to no fact bearing on any target beyond what the freeze and the pinned blobs state.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's proof route for every target — the based gauge fixing, the three controls, the twelve family analyses with the two perturbation pairs and the shift argument, the seven cells and `Φ_conj`'s analysis, each recorded there as the freeze's reading and not as a finding; the values of every separating quantity; the witness supply, items 8–10 included; the consumption of `GEO3`'s `Φ_SC` and `Φ_swap` verdicts by cells `a1` and `a3`; acts 12's, 18's, 21's, 22's and 23's result notes at their pinned blobs, which record every consumed fact; the merged modules. Reading those is reading the freeze.

#### The span module commit → `GEO1`

| question | answer for the span module commit → `GEO1` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the freeze's `GEO1` target; wrote and built the thirteen named results of Section B — the based gauge fixing, the full-support fact from act 12's sufficiency, the Euclidean-norm identity, the metric properties, class invariance, the two directions of the zero-distance equivalence and their instantiation at the two frozen configurations, the assembled `geo1_triple_metric`, and the continuity half of `GEO1-T`; the builds revealed two elaboration details (an instantiated rewrite where a bare `rw` picked the wrong occurrence, and a `field_simp` replaced by `eq_div_iff`) and nothing about any later target. The compactness half of `GEO1-T` was not attempted, as recorded in §5. No control, no family's isometry status and no cell was proved or reasoned to.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `GEO1` target with its conjuncts (i)–(vi-b), the base-star hypothesis and its discharge at `|A| = 1` through act 12's `sh1_sufficiency` and `fibreGram_apply`, and the observation sub-question `GEO1-T`.

#### The span `GEO1` → `GEO2`

| question | answer for the span `GEO1` → `GEO2` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the freeze's `GEO2` target; wrote and built the six named results of Section C — the coordinate permutation under a relabelling and the relabelling isometry through `Equiv.sum_comp`, the two-sided triviality through act 13's `fibreGram_left_mul`, `fibreGram_mul_weak_apply` and `weak_anchor_coeff_norm_one` and `GEO1` (vi-b), the tensor identity, its consequence through the index bijection and `Finset.sum_mul_sum`, and the assembled `geo2_controls`; the builds revealed an `omit` clause needed on one section variable, a `beta_reduce` needed before a rewrite after `subst`, and unused binder names, and nothing about any family or cell. One linter-only `omit` attribute was added to `GEO1`'s `mixedTriple_continuous` in this commit, changing no statement and no proof, disclosed in §3.7.1. No family's isometry status and no cell was proved or reasoned to.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `GEO2` target with its three controls, the tensor identity and its consequence, and the freeze's statement that the relabelling isometries of `GEO3` are instances of control (a).

#### The span `GEO2` → `GEO3`

| question | answer for the span `GEO2` → `GEO3` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the freeze's `GEO3` target and the twelve family analyses; wrote and built the four helpers and the twelve family theorems of Section D, one per subsection — the two perturbation pairs at `N = 32768` and the shift argument at `n = 300` against `n = 1`, the merge pairs through `GEO1` (vi-a), the relabellings through `GEO2` (a), the conjugation through `mixedTriple_star`; the builds revealed the name `pow_le_pow_left₀`, a cardinality normalization, `split_ifs` discharging the branch conditions from context, two `i · i = −1` residuals closed by `linear_combination`, and a beta-redex in the `Φ_HS` distance bound, and nothing about any cell. Whether `ΦCTRL` and `Φ_SC` are isometries is `GEO3`'s own question and not a later target's; cells `a1` and `a3` consume `GEO3`'s verdicts by the freeze's placement. No cell's universal statement was proved or reasoned to, and `Φ_conj`'s prefix, `L5` and relabelling conjuncts — cell `b₀`'s — were not touched.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `GEO3` target, its label rule, the twelve family rows with their merged equations and predicted verdicts, the three perturbation arguments as the freeze's reading, the witness supply items 8–10, the module commit's entry and coordinate bounds, feature norm, sequence identities and cross-invariant tables, and act 23's `gramPhaseEquiv_fst_of_product`, `hadamard_z_admissible`, `fibreGram_z_entries` and `zseq_facts`.

#### The span `GEO3` → `GEO4`

| question | answer for the span `GEO3` → `GEO4` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the freeze's `GEO4` target, its implication matrix and `Φ_conj`'s recorded analysis; wrote and built the nine conjugation lemmas and the four cell theorems of Section E in the route order the freeze fixes — `a0` from `GEO1`, then the witness cells `a1` (`phiSC_corner` and `GEO3`), `a3` (`phiSwap_l5_restricts` and `GEO3`) and `b₀` (`Φ_conj`'s prefix, `L5` and isometry conjuncts discharged in the theorem, the relabelling clause refuted through the module commit's cross-invariant tables) — and only then attempted the universal statements `a2`, `a4` and `b`, none of which was obtained, their obstructions recorded in §8; the builds revealed the scoped `ComplexOrder` instance that `PosSemidef.transpose` needs, single-carrier fixedness restated pointwise, the descent lemma's explicit `Γ` argument, and two numeral refutations needing `norm_num` after `simp`, and nothing else. No target remained open after this span, so no later target could be revealed.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `GEO4` target, its seven cells with their routes, the route order (witness cells before any universal attempt), `Φ_conj`'s analysis conjunct by conjunct as the freeze's reading, the sixteen cross-invariants of `Gᵢ` and the sixteen of `G₁` from the module commit, act 22's `phiSwap_l5_restricts` and act 23's `phiSC_corner` at their pinned lines, and act 21's `ol1a_descent`.

### 3.7.1 The history-integrity statement, and the execution defects disclosed

**No commit on this branch was amended, reset, rebased over, cherry-picked over or force-pushed
away. There are no superseded SHAs.** Before certification this execution absorbed no later `main`.

**No execution defect is recorded; two hygiene items are disclosed.** First, the `GEO2` verdict
commit carries, besides `GEO2`'s six results, one linter-only `omit [Fintype V] [DecidableEq V] in`
attribute added to `GEO1`'s `mixedTriple_continuous`, silencing an unused-section-variable warning;
the statement and the proof are unchanged, and the result was and remains `GEO1`'s. Second, the
`GEO3` commit's docstring of `geo3_phiMD_not_isometry` named `Φ_PC` in `Φ_MD`'s subsection; the
packaging commit rewrites that docstring to describe the collapse in its own terms, the statement and
the proof being byte-identical, so that the subsection isolation the freeze's contract (c) requires
holds at the certified head, where `R7-OGS` checks it. One item of the freeze's reading that the
kernel computes differently is recorded as a discrepancy in §22 and is not repaired.

### 3.8 The gate record (record 8)

| target | the label of the target before it, as earned | the gate |
| --- | --- | --- |
| `GEO2` | `GEO1-METRIC`, by `geo1_triple_metric` at `774aea83af37` | **opened** |
| `GEO3` | `GEO2-CONTROLS-PASS`, by `geo2_controls` at `5e85dfd3bb86` | **opened** |
| `GEO4` | `GEO3-DISCRIMINATES`, by `geo3_phiCTRL_not_isometry` and `geo3_phiSC_not_isometry` at `37099179aebe` | **opened** |

## 4. `GEO0` — the bounded search, recorded in full

**Outcome reached: `GEO0`-silent.**

> On the search this freeze bounds — act 12's, act 18's, act 21's, act 22's and act 23's control
> planes, amendments, result notes and modules, and `verification/ROADMAP.md`, against the frozen
> term list — the merged record carries one phase-invariant quantity read at one fibre pair, act
> 12's cross-invariant, and one geometry built from it, act 18's pseudometric, proved there not to
> separate act 12's classes, and decides neither whether a finite family of such quantities
> separates them, nor whether a distance written from the Gram data does, nor whether any
> transition family of the record is an isometry of any such distance, nor whether such isometry
> follows from or implies any rung of act 21's ladder. **The finding is that the record is silent
> on the point.** It is not a finding that any such statement is false, not a finding that one is
> unprovable, and not a bound on what a later round could prove.

**`GEO0` is a type-P target and carries no evidence level.** No Lean was written for it, and this
round's own theorems are not treated as retro-evidence about it.

**The file set at `B`**, as the freeze bounds it: act 12's `result.md` and `TwoSidedGauge.lean`;
act 18's `result.md` and `IntermediateCrossTimeStructure.lean`; act 21's `preregistration.md`,
`amendments/amendment-1.md`, `result.md` and `OrbitLawRigidityTwisted.lean`; act 22's
`preregistration.md`, `result.md` and `OrbitLawNaturalityFactorization.lean`; act 23's
`preregistration.md`, `result.md` and `OrbitLawGaps.lean`; and `verification/ROADMAP.md`. **The
question asked of each hit**: does this passage state that a finite family of phase-invariant
products of Gram entries separates act 12's classes, or that a distance on Gram tuples written from
the Gram data does, or that any transition family of the record is or is not an isometry of any such
distance, or that isometry of any such distance follows from or implies any rung of act 21's ladder?
This round's own control plane is inside the set by construction and its hits are recorded as not
relevant to the question; the counts below are of the fifteen files named, the control plane
excluded, each term counted as a case-insensitive substring.

| term | hits (act 12 result / module; act 18 result / module; act 21 prereg / amendment / result / module; act 22 prereg / result / module; act 23 prereg / result / module; ROADMAP) | recorded answer |
| --- | --- | --- |
| `metric` | 1 / 1 / 10 / 9 / 2 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 7 | **Does not supply it.** Act 18's result (lines 98, 403–412) and module (lines 104, 706–716) carry `LC2`'s named Gram pseudometric, one quantity read at one fibre pair, proved a pseudometric on orbit classes and **proved not to separate**: the countercontrol at its line 753 shares the invariant while being inequivalent; act 12's result (line 208) and module (line 51) say the round introduces no regularity; act 21's control plane (line 699) records act 18's pseudometric as named and not canonical and (line 1227) that no metric on the index is used; the `ROADMAP`'s hits are other rounds' (a curvature/metric convergence condition of the hydrodynamic lane, and `symmetric`). No statement that any family of invariants or any distance separates act 12's classes, and none about isometries. |
| `pseudometric` | 0 / 0 / 8 / 9 / 1 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 | **Does not supply it.** The same hits as `metric`: act 18's `LC2` pseudometric, proved not to separate, and act 21's mention of it. |
| `distance` | 0 / 0 / 1 / 2 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 | **Does not supply it.** Act 18's result (line 412) and module (lines 707, 712): the distance between two classes under `LC2`'s pseudometric, in the sentence recording that the bound `ε_t = 0` lies below it; no distance written from the Gram data is said to separate anything. |
| `isometr` | 3 / 8 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 2 | **Not relevant to the question.** Every hit is act 12's Gram-isometry lemma `exists_unitary_of_gram_eq` (result lines 106–111; module lines 35, 629–714, 748; `ROADMAP` lines 205, 260): two families of vectors with equal Gram matrices are related by a unitary, `Mathlib`'s `LinearIsometry.extend` doing the extension. A statement about vector families and one unitary; nothing about an isometry of any distance on the orbit space by any transition family. |
| `geometr` | 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 2 | **Not relevant to the question.** The `ROADMAP`'s two hits are other lanes' (`geometric`, `geometry` in the hydrodynamic and substratum rows). |
| `invariant` | 5 / 8 / 15 / 15 / 27 / 2 / 13 / 26 / 22 / 12 / 14 / 17 / 12 / 17 / 9 | **Does not supply it.** Act 12's cross-invariant `G^{(0)}_{10} · G^{(1)}_{01}`, `gramPhaseEquiv_cross_invariant`, read at one fibre pair in every later act's separation; act 18's `∼_D`-invariance of `LC2`'s pseudometric; act 21's, 22's and 23's separations through that one invariant at named pairs. **One invariant read at one pair**, never a finite family, never a completeness statement. |
| `cycle` | 1 / 1 / 1 / 0 / 6 / 0 / 0 / 0 / 3 / 0 / 0 / 3 / 0 / 0 / 2 | **Not relevant to the question.** Every hit is `cocycle` (act 12's vacuous cocycle condition) or `lifecycle` (`§A.37`'s vocabulary); no closed walk of matrix indices is named anywhere. |
| `triple` | 0 / 0 / 2 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 22 | **Not relevant to the question.** Act 18's result (lines 862–863) names its own triple of seal pins; the `ROADMAP`'s hits are acts 15's and 16's cancelling triples of threading moves. No product of three Gram entries is named anywhere. |
| `Bargmann` | 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 | **Absent.** |
| `Hadamard` | 10 / 13 / 9 / 10 / 11 / 0 / 7 / 7 / 8 / 3 / 2 / 9 / 12 / 10 / 2 | **Does not supply it.** Act 12's Hadamard dilations `H₁`, `Hᵢ` and act 23's family `H(z)`, the objects every separation is read on; no equivalence classification of them and no completeness or isometry statement about them. |
| `complete` | 0 / 0 / 1 / 0 / 3 / 0 / 7 / 1 / 7 / 3 / 0 / 6 / 3 / 0 / 12 | **Does not supply it.** `the record is complete`, `complete list`, a lattice completion in act 21's declarations, and the `ROADMAP`'s substratum rows (`completeness of 𝒢_sub`); no completeness of any invariant family is stated. |
| `separat` | 8 / 1 / 17 / 12 / 31 / 0 / 16 / 10 / 29 / 10 / 5 / 48 / 32 / 15 / 44 | **Does not supply it.** Every hit is a separation of two named classes through act 12's cross-invariant at one named pair, or act 18's statement that `LC2`'s pseudometric does not separate; none is a statement that a family separates all classes. |
| `Wigner` | 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 | **Absent.** |
| `conjugat` | 1 / 1 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 12 | **Not relevant to the question.** Act 12's result (line 103) and module (line 240): the right weak action conjugates the Gram data by the anchored phases; the `ROADMAP`'s hits are the substratum lane's hidden conjugation (`P1` rows) and act 13's constant-left conjugation. No entrywise conjugation of fibre-Gram tuples is named as a transition family anywhere. |
| `antiunitar` | 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 | **Absent.** |
| `rigid` | 0 / 0 / 4 / 0 / 97 / 8 / 29 / 36 / 26 / 9 / 3 / 26 / 9 / 3 / 4 | **Does not supply it.** Act 21's `L-WIDE` rigidity verdict about the ladder's surviving class, act 22's and act 23's rung verdicts, and act 18's readback sandwich; none concerns an isometry of any distance, and none implies or is implied by one. |

**A search that finds a decision is a finding, and a search that does not is equally a finding.**
The second is what happened, and the finding is that the record is silent. Act 12's cross-invariant
and act 18's pseudometric are recorded as found and as what they are: one invariant read at one
pair, and one geometry built from it, proved not to separate, which decides none of the four
questions. Reconstructive inference is refused as a finding here.

## 5. `GEO1` — completeness of the mixed triples, and the metric they induce

**Outcome reached: `GEO1-METRIC`.**

> The mixed-triple feature map — every product of three Gram entries around a closed three-step
> walk of matrix indices, with a fibre label per step — is invariant under act 12's phase action at
> every finite carrier, and separates act 12's classes on every pair of tuples with Hermitian fibres, equal diagonals
> and no vanishing entry on one base star, hence on the realizable tuples at both frozen
> configurations, where no entry vanishes; and the Euclidean distance of feature vectors is a
> metric on classes: nonnegative, symmetric, subadditive, constant on each class in both
> arguments, and zero exactly on the pairs `GramPhaseEquiv` relates on the realizable tuples, each
> direction of the last proved separately, at evidence level 2. **This is a statement about the
> exact family and the exact quantity frozen under these names**: it does not say the family is
> minimal, canonical or physical, does not say the induced metric is canonical or the right
> geometry to impose, says nothing about tuples with a vanishing entry, and adopts nothing.

`geo1_triple_metric` carries the conjuncts (i)–(vi-b) of the freeze as separate conjuncts of one
statement, quantifying over every finite carrier `W` with `[Fintype W] [DecidableEq W]` where the
freeze says "every finite carrier", with `Ψ = mixedTriple` and `d` bound by the displayed equation.
Each conjunct, reported separately:

| conjunct | statement | proved by |
| --- | --- | --- |
| (i) invariance | `GramPhaseEquiv G H → mixedTriple G = mixedTriple H`, every finite carrier | `mixedTriple_gauge`: at every coordinate the three phases cancel in pairs, `star (c j) · c j = 1` |
| (ii) separation at a base star | Hermitian fibres, equal diagonals, `∀ j, G j₀ j₀ j ≠ 0`, and `Ψ G = Ψ H` give `GramPhaseEquiv G H` | `geo1_separation_star`: the phases `c j := H j₀ j₀ j / G j₀ j₀ j`, of modulus `1` by the coordinate `((j₀,j₀,j₀),(j₀,j,j₀))` and the diagonal, and every entry `H i j k = star (c j) · G i j k · c k` by the coordinate `((j₀,i,j₀),(j₀,j,k))` and one division — one star and one triangle per entry, no graph argument |
| (iii) at the two configurations | for realizable `G H` at the single-carrier and at the product configuration, `Ψ G = Ψ H → GramPhaseEquiv G H` | `geo1_separation_single`, `geo1_separation_product`: (ii) at `j₀ = 0`, the Hermitian hypothesis from `RealizableGram`'s positive-semidefinite conjunct, the equal diagonals from its fourth conjunct (both equal the visible family), and the support from `realizable_entry_ne_zero` — at `|A| = 1` every realizable tuple has the form `star (U (i,x) (j,0)) · U (i,x) (k,0)` by `sh1_sufficiency` and `fibreGram_apply`, with `‖U (i,x) (j,0)‖ ^ 2 = Γ i j ≠ 0`, so no entry vanishes |
| (iv) the metric properties | `0 ≤ d G H`, `d G G = 0`, `d G H = d H G`, `d G K ≤ d G H + d H K`, every finite carrier | `geo1_metric_props`, through `dist_eq_norm_toLp`: `d G H` is the norm of `Ψ G − Ψ H` in `EuclideanSpace ℂ`, so the four are those of a norm |
| (v) class invariance | `GramPhaseEquiv G G' → GramPhaseEquiv H H' → d G H = d G' H'` | `geo1_class_invariant`, from (i) |
| (vi-a) zero implies equivalent | at each frozen configuration, realizable `G H` with `d G H = 0` are `GramPhaseEquiv` | `geo1_equiv_of_zero_single`, `geo1_equiv_of_zero_product`: `features_eq_of_dist_zero` (a Euclidean norm vanishes only on the zero vector) then (iii) |
| (vi-b) equivalent implies zero | `GramPhaseEquiv G H → d G H = 0`, every finite carrier | `geo1_zero_of_equiv`, from (i) |

**The two directions of the zero-distance equivalence are proved separately**, (vi-a) and (vi-b),
each with its own witness in the statement, and the equivalence is displayed nowhere as a single
biconditional. **The support hypothesis is the base star `∀ j, G j₀ j₀ j ≠ 0` and nothing more**,
discharged at the frozen configurations from act 12's merged results and assumed nowhere else.
**Nothing is asserted about tuples with a vanishing entry on the base star, at any carrier, or at
`|A| > 1`.**

**`GEO1-T`, the observation sub-question — outcome `GEO1-T-UNDECIDED`.** The continuity half is
proved, `mixedTriple_continuous`: `Ψ` is continuous on `V → Matrix V V ℂ` as a finite product of
coordinate projections, so `d` is continuous. The compactness half — that the set of realizable
tuples at each frozen configuration is closed and bounded, so that the class space with `d` is
compact and `d` induces the quotient topology — was not attempted: closedness of the rank-at-most-`|A|`
condition and of the realizable set was not available in a usable form, and the freeze places the
attempt only after (i)–(vi-b) closed. **`GEO1-T` enters no label**, and whether `d` induces the
quotient topology on the realizable classes is not claimed.

## 6. `GEO2` — the three controls

**Outcome reached: `GEO2-CONTROLS-PASS`.**

> Every carrier relabelling is an exact isometry of the geometry, act 12's two-sided gauge acts
> trivially on it, and the feature map carries the product embedding to the tensor product of the
> factors' feature vectors, so that the distance between two products with a common second factor
> is the factors' distance scaled exactly by the common factor's feature norm, at evidence level 2.
> **This is a statement about three named constructions of the record and the exact quantity
> frozen**; it says nothing about constructions not on the list and does not say the geometry is
> preserved by anything else.

| control | theorem | proved by |
| --- | --- | --- |
| (a) relabellings | `geo2_relabel_isometry`: `d (RelabelTransition σ G) (RelabelTransition σ H) = d G H`, every finite carrier and every `σ` | `mixedTriple_relabel` — the feature map of a relabelled tuple is the feature map read at permuted coordinates — and `Equiv.sum_comp` along the bijection `(σ × σ × σ) × (σ × σ × σ)` of the index set |
| (b) the two-sided gauge | `geo2_twoSided_trivial`: `d (FibreGram a₀ (L * U * K)) (FibreGram a₀ U) = 0` for `L` in the left fibre group and `K` a weak anchored stabilizer | act 13's `fibreGram_left_mul` (the left factor leaves every fibre-Gram tuple unchanged) and `fibreGram_mul_weak_apply` with `weak_anchor_coeff_norm_one` (the right weak factor conjugates the tuple by the anchored phases, a `GramPhaseEquiv`), then `GEO1` (vi-b) |
| (c) the tensor identity | `mixedTriple_product`: `Ψ (X ⊠ Y) (((a₁,b₁),(a₂,b₂),(a₃,b₃)), ((j₁,k₁),(j₂,k₂),(j₃,k₃))) = Ψ X ((a₁,a₂,a₃),(j₁,j₂,j₃)) · Ψ Y ((b₁,b₂,b₃),(k₁,k₂,k₃))` | an entrywise identity of monomials, `ring` |
| (c) its consequence | `geo2_product_tensor`: `d (X ⊠ Y) (X' ⊠ Y) = d X X' · Real.sqrt (∑ q, ‖Ψ Y q‖ ^ 2)`, with `d` on each carrier bound to the displayed equation on that carrier | the index bijection between product-carrier coordinates and pairs of factor coordinates, `Fintype.sum_equiv`, the identity, and `Finset.sum_mul_sum` for the one product of sums, then `Real.sqrt_mul` |

`geo2_controls` assembles the four as one statement. **The identity and its consequence are reported
apart**: the identity is exact and homogeneous of degree three in each factor; the consequence is
what the perturbation arguments of `GEO3` consume, with the feature norm of `G(H₁)` and of `G(Hᵢ)`
equal to `1` by the module commit's `fourier_feature_norm` at `z = 1` and `z = i`.

## 7. `GEO3` — the twelve families against the geometry

**Outcome reached: `GEO3-DISCRIMINATES`, via `ΦCTRL` and `Φ_SC`.**

> The geometry discriminates within the structurally admissible class: an exhibited transition
> family satisfying every condition of act 21's ladder before naturality, named for this target in
> advance, is not an isometry of it on realizable tuples, at evidence level 2, with the pair and
> the separating quantity named; and every family of the frozen list is recorded with its own
> verdict. **This is a statement about the exact families and the exact quantity frozen**: it does
> not say isometry is the right condition to impose, does not say any family is excluded from
> anything by it, and does not adopt the geometry as a selector.

**The label was earned by `ΦCTRL` and `Φ_SC`, and by no family outside the prefix.** Both are proved
not isometries; both satisfy the prefix through `L4d` by acts 21's and 23's merged verdicts, consumed
and not re-proved. The other ten verdicts are census entries and earn the label of nothing. Each
theorem is named `geo3_<family>_isometry` or `geo3_<family>_not_isometry` for the outcome reached,
sits in its own subsection of the module's `GEO3` section, names no other family, and pins `Γ₀`,
`H₁`, `Hᵢ`, `Γ`, the family and `d` by equations.

### 7.1 The twelve-row census

| family | theorem | label | configuration | the pair and the separating quantity, or the route |
| --- | --- | --- | --- | --- |
| `ΦI` | `geo3_phiI_isometry` | **ISOMETRY** | the single-carrier configuration | `d G H = d G H` by `rfl` |
| `ΦP` | `geo3_phiP_isometry` | **ISOMETRY** | the single-carrier configuration | `GEO2` (a) at `σ = (2 3)` |
| `ΦC` | `geo3_phiC_not_isometry` | **NOT-ISOMETRY** | the single-carrier configuration | the pair `G(H₁)`, `G(Hᵢ)`, both realizable by `sh1_necessity`, both sent to `G(H₁)`: the images are at distance `0` while the inputs differ at the coordinate `((1,0,1),(1,1,0))`, values `1/64` and `i/64` — the diagonal `¼` times act 12's cross-invariant at the fibre pair `(0,1)`, `1/16` and `i/16` (`hadamard_entries`'s `c1`, `c2`) |
| `ΦT` | `geo3_phiT_isometry` | **ISOMETRY** | the single-carrier configuration | at each `t` the map is the identity or `σ`, by the case on `Even t`, each `GEO2` (a) |
| `ΦPP` | `geo3_phiPP_isometry` | **ISOMETRY** | the product configuration | `GEO2` (a) at `σ × σ` |
| `ΦCTRL` | `geo3_phiCTRL_not_isometry` | **NOT-ISOMETRY** | the product configuration | the perturbation pair at `t = 0`, `N = 32768`: `G(H₁) ⊠ G(Hᵢ)` fires and is sent to `G(H₁) ⊠ σG(Hᵢ)`; `F(zs N) ⊠ G(Hᵢ)` does not fire (the marginal lemma against the realizable second factor's diagonal `¼`, then `zs N / 16 = 1/16` against `zs N ≠ 1`) and is fixed; `d G H = d (G(H₁)) (F(zs N)) ≤ 3 ‖zs N − 1‖ < 1/4096` by `GEO2` (c), the feature norm `1` of `G(Hᵢ)` and the entry bound; the images differ at the cross-invariant coordinate of the product pair `((0,0),(0,2))`, values `i/4096` and `1/4096`, by `‖i − 1‖/4096 ≥ 1/4096` |
| `Φ_swap` | `geo3_phiSwap_isometry` | **ISOMETRY** | the product configuration | `GEO2` (a) at the exchange of the two factors |
| `Φ_MD` | `geo3_phiMD_not_isometry` | **NOT-ISOMETRY** | the product configuration | the pair `G(Hᵢ) ⊠ G(H₁)`, `G(H₁) ⊠ G(H₁)` at `t = 0`, both realizable by `product_realizable`, both sent to `G(H₁) ⊠ G(H₁)`: the images are at distance `0` while the inputs are inequivalent by act 23's `gap_separations` at `((0,0),(1,0))` and therefore at positive distance by `GEO1` (vi-a) |
| `Φ_PC` | `geo3_phiPC_not_isometry` | **NOT-ISOMETRY** | the product configuration | the same pair at `t = 0`, both sent to `G(H₁) ⊠ G(H₁)`; the separating quantity is `GEO1` (vi-a) on `gap_separations`' inequivalence at `((0,0),(1,0))` |
| `Φ_HS` | `geo3_phiHS_not_isometry` | **NOT-ISOMETRY** | the product configuration | the shift argument: for `n ≥ 1`, `Φ_HS t (F n) = F (n + 1)`, the branch index unique by `zseq_facts`'s injectivity and the marginal lemma, so an isometry would give `d (F n) (F (n + 1)) = d (F 1) (F 2)` for every `n ≥ 1` by induction; at `n = 300`, `d (F 300) (F 301) ≤ 3 ‖zs 301 − zs 300‖ < 1/15000` by `GEO2` (c), the feature norm and the entry bound, while `d (F 1) (F 2) ≥ ‖zs 2 − zs 1‖/4096 > 1/8192` at the cross-invariant coordinate of the product pair `((0,0),(1,0))`, whose value on `F n` is `zs n / 4096` |
| `Φ_SC` | `geo3_phiSC_not_isometry` | **NOT-ISOMETRY** | the product configuration | the perturbation pair at `t = 0`, `N = 32768`: `G(Hᵢ) ⊠ G(H₁)` fires on the first disjunct and is sent to `σG(Hᵢ) ⊠ G(H₁)`; `F(i · zs N) ⊠ G(H₁)` fires on neither disjunct (the marginal lemma, then `i · zs N / 16 = i/16` against `zs N ≠ 1`, `hadamard_entries`'s `c2` and `r1` reading the two disjuncts) and is fixed; `d G H = d (G(Hᵢ)) (F(i · zs N)) ≤ 3 ‖zs N − 1‖ < 1/4096`; the images differ at the cross-invariant coordinate of the product pair `((0,0),(2,0))`, values `i/4096` and `1/4096`, the first factor's invariant at `(0,2)` being `z`-free (`fibreGram_z_cross02`) |
| `Φ_conj` | `geo3_phiConj_isometry` | **ISOMETRY** | the product configuration | `mixedTriple_star`: the feature map of the conjugate is the conjugate of the feature map, and `norm_star` at every coordinate |

Six isometries and six non-isometries, as the family tables predict. Each family's frozen sentence,
carried with its naming line:

> **The frozen `Φ`-ISOMETRY sentence, carried for `ΦI`.**
> The transition family named `Φ` is an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2. **This is a statement about
> the exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

> **The frozen `Φ`-ISOMETRY sentence, carried for `ΦP`.**
> The transition family named `Φ` is an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2. **This is a statement about
> the exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

> **The frozen `Φ`-NOT-ISOMETRY sentence, carried for `ΦC`.**
> The transition family named `Φ` is not an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2, with the pair and the
> separating quantity named. **This settles that family against that proposition and nothing in its
> neighbourhood**, and it is not a statement that families of its shape fail in general.

> **The frozen `Φ`-ISOMETRY sentence, carried for `ΦT`.**
> The transition family named `Φ` is an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2. **This is a statement about
> the exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

> **The frozen `Φ`-ISOMETRY sentence, carried for `ΦPP`.**
> The transition family named `Φ` is an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2. **This is a statement about
> the exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

> **The frozen `Φ`-NOT-ISOMETRY sentence, carried for `ΦCTRL`.**
> The transition family named `Φ` is not an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2, with the pair and the
> separating quantity named. **This settles that family against that proposition and nothing in its
> neighbourhood**, and it is not a statement that families of its shape fail in general.

> **The frozen `Φ`-ISOMETRY sentence, carried for `Φ_swap`.**
> The transition family named `Φ` is an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2. **This is a statement about
> the exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

> **The frozen `Φ`-NOT-ISOMETRY sentence, carried for `Φ_MD`.**
> The transition family named `Φ` is not an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2, with the pair and the
> separating quantity named. **This settles that family against that proposition and nothing in its
> neighbourhood**, and it is not a statement that families of its shape fail in general.

> **The frozen `Φ`-NOT-ISOMETRY sentence, carried for `Φ_PC`.**
> The transition family named `Φ` is not an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2, with the pair and the
> separating quantity named. **This settles that family against that proposition and nothing in its
> neighbourhood**, and it is not a statement that families of its shape fail in general.

> **The frozen `Φ`-NOT-ISOMETRY sentence, carried for `Φ_HS`.**
> The transition family named `Φ` is not an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2, with the pair and the
> separating quantity named. **This settles that family against that proposition and nothing in its
> neighbourhood**, and it is not a statement that families of its shape fail in general.

> **The frozen `Φ`-NOT-ISOMETRY sentence, carried for `Φ_SC`.**
> The transition family named `Φ` is not an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2, with the pair and the
> separating quantity named. **This settles that family against that proposition and nothing in its
> neighbourhood**, and it is not a statement that families of its shape fail in general.

> **The frozen `Φ`-ISOMETRY sentence, carried for `Φ_conj`.**
> The transition family named `Φ` is an isometry of the geometry on realizable tuples at the
> configuration its merged verdict is stated at, at evidence level 2. **This is a statement about
> the exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

**What the discrimination verdicts do and do not depend on**, in the freeze's two-part wording and
no stronger: Merge witnesses are metric-independent once separation is proved. Sequence-discontinuity
witnesses are invariant across metrics inducing the quotient topology. `ΦC`, `Φ_PC` and `Φ_MD` send
two classes at positive distance to one class; `ΦCTRL`, `Φ_SC` and `Φ_HS` send inputs whose distance
goes below any bound to images whose distance stays above one. **The isometry verdicts of `GEO3` are
verdicts about the frozen `d`**, and `GEO1-T`, undecided, enters no label.

**No family's verdict is inferred from another's**: the relabellings' isometries are instances of
`GEO2` (a) and are still stated and proved one by one; `Φ_MD`'s and `Φ_PC`'s pairs are recomputed
inside their own theorems. `ΦX` of act 21 is excluded as a law on trajectories and not a transition
family, as the freeze records, and its exclusion is not a verdict.

> **THE CLAUSE, carried at this mention — the census, where a family is or is not an isometry.**
> Act 24 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 8. `GEO4` — the rigidity attempt and the implication cells

**Outcome reached: `GEO4-UNDECIDED`.**

> Whether the conditions of act 21's ladder before naturality, factorization and isometry of the
> geometry force a law to act on realizable classes as a carrier relabelling or as one composed with
> entrywise conjugation is undecided in this round, with the obstruction named specifically — the
> step of the universal attempt that did not close and what would settle it. Neither the rigidity
> label nor its negation is claimed; the absence of a proof is not a counterexample.

**The label is earned by `b` alone.** The universal statement `geo4_b_rigid` was attempted after the
three witness cells had closed and was not obtained; the obstruction is named below. No family on the
frozen list satisfies `b`'s hypotheses and fails its conclusion, and no `NOT-RIGID` label exists for
`b`. The seven cells, each a separate proposition, none inferred from another, each stated with the
prefix written out as the first seven conjuncts of `LadderConds`, `L5` as `FactorizesOnProduct
(Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ`, and
isometry as the displayed proposition with `d` bound by equation:

| cell | assumed | tested | label | theorem | route |
| --- | --- | --- | --- | --- | --- |
| `a0` | isometry | injectivity on realizable classes | **holds** | `geo4_a0_isometry_injective` | universal: equivalent images are at distance `0` by `GEO1` (vi-b), so the inputs are at distance `0` by isometry, hence equivalent by `GEO1` (vi-a) |
| `a1` | the prefix, `L5` | isometry | **NOT-IMPLIES** | `geo4_a1_l5_not_implies_geo` | `Φ_SC`: its prefix and `L5` conjuncts consumed from act 23's `phiSC_corner`, its non-isometry from `GEO3`'s `geo3_phiSC_not_isometry`, the family entering both by its pinned equation and `rfl` |
| `a2` | the prefix, `L4n` | isometry | **UNDECIDED** | — | universal attempt, not obtained; obstruction below |
| `a3` | the prefix, isometry | `L5` | **NOT-IMPLIES** | `geo4_a3_geo_not_implies_l5` | `Φ_swap`: its prefix conjuncts and its `L5` failure consumed from act 22's `phiSwap_l5_restricts`, its isometry from `GEO3`'s `geo3_phiSwap_isometry` |
| `a4` | the prefix, isometry | `L4n` | **UNDECIDED** | — | universal attempt, not obtained; obstruction below |
| `b₀` | the prefix, `L5`, isometry | one `σ` with `Φ t G ∼ RelabelTransition σ G` on realizable `G` | **NOT-RIGID** | `geo4_b0_not_relabel_rigid` | `Φ_conj`, every conjunct discharged in the theorem; the separating invariant below |
| `b` | the prefix, `L5`, isometry | one `σ` with `Φ t G ∼ σ G`, or one `σ` with `Φ t G ∼ σ (star G)`, on realizable `G` | **UNDECIDED** | — | universal attempt, not obtained; obstruction below |

The cells' frozen sentences, each carried with its naming line:

> **The frozen cell sentence, carried for `a0`.**
> Isometry of the geometry on realizable tuples implies injectivity on realizable classes, at
> evidence level 2, by separation; the converse is not asked.

> **The frozen cell sentence, carried for `a1`.**
> At the frozen product configuration, the conditions before naturality together with
> factorization do not imply isometry of the geometry: an exhibited family, named for this cell in
> advance, satisfies every one of them and is not an isometry, at evidence level 2. No independence
> of isometry and factorization is asserted.

> **The frozen cell sentence, carried for `a3`.**
> At the frozen product configuration, the conditions before naturality together with isometry of
> the geometry do not imply factorization: an exhibited family, named for this cell in advance,
> satisfies every one of them and does not factorize, at evidence level 2. No independence of
> isometry and factorization is asserted.

> **The frozen cell sentence, carried for `b₀`.**
> At the frozen product configuration, the conditions before naturality, factorization and isometry
> of the geometry do not force a law to act on realizable classes as a carrier relabelling: an
> exhibited family, named for this cell in advance, satisfies every one of them and sends one named
> realizable class to a class no relabelling reaches, at evidence level 2, with the separating
> invariant named. **This is a statement about the relabelling conclusion alone**; nothing here
> calls the witness antiunitary, a symmetry, or a candidate for anything.

> **The frozen `UNDECIDED` cell sentence, carried for `a2`.**
> The cell is undecided in this round, with the obstruction named specifically — which conjunct of
> the named witness did not close and at which step, or which step of the universal attempt did
> not close. Neither label is claimed; the absence of an exhibited counterexample is not a proof of
> the implication, and the absence of a proof is not a counterexample.

> **The frozen `UNDECIDED` cell sentence, carried for `a4`.**
> The cell is undecided in this round, with the obstruction named specifically — which conjunct of
> the named witness did not close and at which step, or which step of the universal attempt did
> not close. Neither label is claimed; the absence of an exhibited counterexample is not a proof of
> the implication, and the absence of a proof is not a counterexample.

### 8.1 `Φ_conj`'s conjuncts, each reported separately

`geo4_b0_not_relabel_rigid` instantiates the universal at `Φ_conj`, pinned to
`fun _ G => fun i => Matrix.of fun j k => star (G i j k)`, and discharges every hypothesis inside the
theorem:

| conjunct | discharged by |
| --- | --- |
| `ProperAt` | the constant solutions at `G(H₁) ⊠ G(H₁)` and at `F(−1) ⊠ G(H₁)`, both real tuples fixed exactly by the conjugation (`conj_fibreGram_one`, `conj_fibreGram_negOne`: their fibres are symmetric, so the conjugate, which is the fibrewise transpose of a Hermitian tuple by `conj_eq_transpose`, is the tuple itself; `conj_product` for the products), both realizable (`hadamard_z_admissible` at `z = −1`, `product_realizable`), inequivalent through the product cross-invariant at `((0,0),(1,0))`, values `1/256` and `−1/256`; the non-solution the constant trajectory at `G(Hᵢ) ⊠ G(H₁)`, whose image at time `0` is its conjugate, inequivalent to it at `((0,0),(1,0))`, values `i/256` and `−i/256` (`conj_cross`) |
| `PropagatesFrom` | clause (i) from descent through act 21's `ol1a_descent`; clause (ii) at `t = 1`, the two constant solutions above |
| `L0` `EvolvesTotally` | the iterates `t ↦ C^[t] G₀`, realizable at every `t` by `L1` |
| `L1` `PreservesAdmissible` | `realizable_conj`: the conjugate of a realizable tuple is realizable — its fibres are the transposes of positive semidefinite matrices (`Matrix.PosSemidef.transpose`), of the same rank (`Matrix.rank_transpose`), summing to the transpose of the identity, with the same diagonal, which is real by `RealizableGram`'s fourth conjunct |
| `L2` | `Φ₀ = C`, by construction |
| `L3i` and `L3s` | `conj_conj`: the conjugation is an involution on tuples, so injectivity on classes follows from descent applied twice and surjectivity from the preimage `C G'` |
| `L4d` | `conj_gramPhaseEquiv`: `H = c ⋆ G` gives `star H = (star c) ⋆ (star G)` with `‖star (c j)‖ = 1` |
| `L5` `FactorizesOnProduct` | `Φ₁ = Φ₂ =` the single-carrier conjugation, fixed before the inputs; `star (X ⊠ Y) = star X ⊠ star Y` entrywise (`conj_product`), the displayed equivalence `gramPhaseEquiv_refl`; the cardinality `1 = 1 · 1` and the visible family's product form by computation |
| isometry | `GEO3`'s `geo3_phiConj_isometry`, consumed |
| the relabelling clause refuted | at `t = 0`, for every `σ : Equiv.Perm (Fin 4 × Fin 4)`: the cross-invariant of `RelabelTransition σ (G(Hᵢ) ⊠ G(H₁))` at `((0,0),(1,0))` is a product of a cross-invariant of `G(Hᵢ)` and one of `G(H₁)` at the relabelled indices (`relabel_product_cross`), the first in `{1/16, i/16}` at every ordered pair of indices and the second `1/16` at every ordered pair (`hadamard_i_cross_all`, `hadamard_one_cross_all`), so the value lies in `{1/256, i/256}`; the cross-invariant of the conjugate at the same pair is `star ((i/16)(1/16)) = −i/256` (`conj_cross`); `gramPhaseEquiv_cross_invariant` then refutes `Φ_conj 0 (G(Hᵢ) ⊠ G(H₁)) ∼ σ (G(Hᵢ) ⊠ G(H₁))` |

**The separating class is `[G(Hᵢ) ⊠ G(H₁)]` and the separating invariant is act 12's cross-invariant
at the product pair `((0,0),(1,0))`, `−i/256` against the set `{1/256, i/256}`.** `Φ_conj`'s `L4n`
status is neither tested nor reported; its conjuncts are discharged for cell `b₀`'s hypotheses and
for `GEO3`'s isometry test, and it is named as the entrywise `star` and as nothing else.

### 8.2 The universal attempts, and the obstructions named

Each was attempted after `a0`, `a1`, `a3` and `b₀` had closed, in the route order the freeze fixes,
and none was obtained.

- **`a2`, the prefix with `L4n` implies isometry.** The step that did not close is the first: from
  the existence, at each `t`, of a lift `Ψ` on dilations satisfying the lifting obligation, the
  admissibility obligation and act 20's `TwistedNatural`, to any constraint on the feature distances
  of the images. `TwistedNatural`'s two closure conjuncts constrain how `Ψ` intertwines the left and
  weak-right actions on dilations, and nothing in the declaration relates `Ψ`'s action on fibre-Gram
  tuples to the coordinates of `Ψ`. What would settle it is a theorem that a twisted-natural lift
  acts on realizable fibre-Gram tuples by a carrier relabelling composed with a two-sided gauge
  move — which would give isometry by `GEO2` (a) and (b) — or a family on the frozen list satisfying
  the prefix and `L4n` and failing isometry, of which the list has none: the two non-isometries in
  the prefix, `ΦCTRL` and `Φ_SC`, both fail `L4n` by acts 22's and 23's verdicts. Neither label is
  claimed.
- **`a4`, the prefix with isometry implies `L4n`.** The step that did not close is the construction
  of a dilation-level map `Ψ`, fixed before the inputs, from an isometry of the class-level geometry:
  the isometry hypothesis constrains `Φ t` only through distances of realizable tuples and supplies
  no map on dilations and no candidate for `αL`, `αR`. What would settle it is a lifting theorem from
  isometries of the feature geometry on realizable tuples to twisted-natural maps on dilations, or a
  family on the frozen list that is an isometry, satisfies the prefix, and fails `L4n`, of which the
  list has none: every isometry of the list that is tested against `L4n` satisfies it, and `Φ_conj`'s
  `L4n` status is not tested. Neither label is claimed.
- **`b`, the prefix with `L5` and isometry forces a relabelling or a relabelling composed with the
  conjugation.** The step that did not close is the passage from an isometry of the geometry on the
  realizable tuples to a single permutation `σ` of the carrier `Fin 4 × Fin 4`: the hypotheses
  constrain `Φ t` through act 12's classes and the feature distances, and no argument in the record
  produces a permutation of the carrier from an isometry of the feature geometry restricted to the
  realizable set, the isometries of that geometry not being characterized here and their
  characterization being out of this round's scope by its own freeze. What would settle it is a
  classification of the isometries of the feature geometry on the realizable classes at the product
  configuration, which is a question for a later round with its own freeze. Neither the rigidity
  label nor its negation is claimed; the absence of a proof is not a counterexample.

**No independence of conditions is asserted and no characterization of the isometries is made.**
`a1` and `a3` are two facts about two named families at one configuration; `a0` is separation; `b₀`
is one family sending one class off every relabelling's reach; no square of independences is
reported, and nothing is said about the isometry group of the orbit space beyond the twelve verdicts
and the `b` cell's undecided outcome.

## 9. The outcome vector, and what it is not

The headline is row 2 of the freeze's outcome-vector table, selected verbatim and reported in no
other wording, and it is stated once, at the head of this note. **No verdict was inferred from
another beyond the consumptions the freeze places.** Each of the four labels is earned by its own
target's theorems and by nothing else: `GEO1`'s by `geo1_triple_metric`, `GEO2`'s by
`geo2_relabel_isometry`, `geo2_twoSided_trivial` and `geo2_product_tensor`, `GEO3`'s by
`geo3_phiCTRL_not_isometry` and `geo3_phiSC_not_isometry`, `GEO4`'s by the recorded non-attainment of
`geo4_b_rigid`; the consumptions the freeze places are `GEO1` (vi-a) and (vi-b) in `a0` and in the
merge pairs, `GEO2` (c) in the perturbation and shift arguments, and `GEO3`'s `Φ_SC` and `Φ_swap`
verdicts in cells `a1` and `a3`. The gate record is §3.8. No single-label headline, no summary label
and no combination label exists for this round.

## 10. The route-authorization matrix, as honoured

**The route-authorization matrix is honoured**: each construction was used for its own target and
cells and for nothing else, no witness was reassigned to another target or cell, and no alternative
was substituted for a named one.

| construction or route | used for | used for nothing else |
| --- | --- | --- |
| the loop invariance, the based-triangle gauge fixing, the full-support fact, the Euclidean norm facts | `GEO1` | consumed by later targets as `GEO1`'s verdict, not re-proved there |
| the index permutation, the two-sided gauge laws, the tensor identity | `GEO2` | consumed by `GEO3` and `GEO4` as `GEO2`'s verdict |
| the twelve families, the two perturbation pairs, the shift argument | `GEO3` | `ΦCTRL`'s and `Φ_SC`'s non-isometries earn the label; the other ten are census entries |
| `Φ_SC` | cell `a1` | its prefix and `L5` are act 23's, consumed; it answers no other cell |
| `Φ_swap` | cell `a3` | its prefix and `L5` failure are act 22's, consumed; it answers no other cell |
| `Φ_conj` | cell `b₀` and its `GEO3` row | its `L4n` status is not a verdict; it answers no other cell |
| the universal routes | `a0`, `a2`, `a4`, `b` | `a0` obtained; `a2`, `a4`, `b` undecided |
| the shared lemmas of the module commit | consumed | answer no target by themselves |

**The execution order `GEO1` → `GEO2` → `GEO3` → `GEO4` was followed**, one verdict commit per
target, the gate read between each, and no target was executed out of order; the universal attempts
of `GEO4` were made only after the three witness cells had closed.

## 11. The scope boundary as honoured

**Nothing here derives, recognises or approaches quantum evolution**, and nothing here says that any
family, the invariant family or the geometry is, resembles, approximates or points toward it; no
continuity in time, composition in time, semigroup law, generator or one-parameter structure is
introduced — `mixedTriple_continuous` is continuity of a polynomial map on a finite-dimensional space
and says nothing about time — and the parameter `z` of the Fourier family and the index `N` are a
parameter of a frozen witness supply and a fixed index, not a time, a flow or a limit.

**No theorem is attributed to the literature and no completeness is asserted past the base-star
hypothesis.** The Bargmann-invariant, frame-equivalence and complex-Hadamard literature is cited by
the freeze as the provenance of the route; no theorem of it is consumed, the tuple statement (ii) is
this round's and is proved here, and nothing is said about tuples with a vanishing entry.

**Every earlier act's historical verdicts stand unchanged**, acts 12 through 23's: act 12's
classification, act 18's `LC2` pseudometric verdicts, act 21's census, `SIOP-YES` and `L-WIDE`, act
22's three verdicts and act 23's four. **Act 16's cancellation cell and the threading question are
untouched in either direction.** **Act 18's `D`-axis is untouched.** **Act 10's anchor-axis
reclassification is untouched.** Act 14's four carriers are not read and no carrier is adopted as
the physical one.

**No family outside the frozen twelve was tested, no invariant family or geometry outside the frozen
one, no control outside the frozen three, no configuration outside the frozen two, no decomposition
other than `e = Equiv.refl`, and no equivalence outside the frozen quotient list was used in any
verdict.** No thirteenth family, no second invariant family or geometry, no further equivalence,
rung, configuration or control, no completeness statement for tuples with zero entries, no
strengthening of a merged theorem and no universal implication for a cell whose witness had closed
was discovered, and none was executed.

## 12. The non-adoption clause, carried verbatim at each mention

**THE CLAUSE is carried three times in this note** — at the headline, at the census, and here — each
carriage opening with its own naming line and carrying the complete frozen clause, from "Act 24
classifies" to "approaches quantum evolution.". Where a frozen byte-fixed sentence carries the clause's
substance in its own wording — the status rule's sentences and the `P0` row's sentence — no quotation
is inserted inside the quotation, as the freeze directs. **No law is adopted, endorsed or given
physical status by surviving, and the invariant family and the geometry are adopted as nothing**:
not as a selector, not as a principle, not as the physical geometry.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 24 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 13. The frozen `P0` sentence for the case reached

**Case A** — `GEO0` silent, row 2 with the cells as predicted — is the case reached, and its sentence
is the frozen sentence with every clause as written for Case A, none of the variable clauses
replaced. It is appended, verbatim, to the `P0` row of `verification/ROADMAP.md` after act 23's
sentence in the same cell, and the row's label stays **OPEN** and two-part:

> Act 24 tests, in one gated round with four separately frozen targets, whether a finite family of phase invariants written from the Gram data alone — every product of three Gram entries around a closed three-step walk of matrix indices, with a fibre label per step — separates act 12's classes on the realizable tuples, whether the record's legitimate constructions preserve the distance it induces, whether that distance tells the record's structurally admissible laws apart, and whether, together with every condition of act 21's ladder before naturality and with factorization, isometry of it forces a law to act on classes as a carrier relabelling, at act 12's and act 21's frozen configurations, with a closed list of twelve named laws frozen with it. The family separates the classes on the realizable tuples at both configurations, where no entry vanishes, and the Euclidean distance of feature vectors is a metric on classes: nonnegative, symmetric, subadditive, constant on each class in both arguments, and zero exactly on act 12's equivalent pairs. Every carrier relabelling is an exact isometry of it, act 12's two-sided gauge acts trivially on it, and the product embedding with a common second factor scales it exactly by the common factor's feature norm. The geometry discriminates within the structurally admissible class: a law satisfying every condition before naturality and factorizing, and a law satisfying every condition before naturality and conditioning one factor on the other, each named for that target in advance, are not isometries of it, while every relabelling law of the record is one. Whether every law satisfying the conditions before naturality, factorization and isometry acts on classes as a carrier relabelling or as one composed with entrywise conjugation is recorded undecided, with the obstruction named; the entrywise conjugation, named in advance, satisfies every condition before naturality, factorizes, is an isometry, and sends one admissible class to a class no relabelling reaches, so the relabelling conclusion alone is not forced; isometry implies injectivity on classes; and the conditions before naturality with factorization do not force isometry, nor with isometry force factorization. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no verdict is inferred from another; no condition is adopted; the invariant family and its geometry are named objects of test and are not adopted as the physical ones; nothing is asserted about tuples with a vanishing entry; acts 12 through 23's own verdicts stand exactly as they state them; nothing here introduces continuity, composition in time or a generator; and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

## 14. What no outcome licenses, and the status rule as honoured

The freeze's twenty forbidden sentences are honoured in terms. No sentence of this round says that a
family, the invariant family or the geometry is, resembles or points toward quantum evolution,
unitarity or a quantum symmetry, and `Φ_conj` is named as the entrywise conjugation and as nothing
else (1); none says a surviving law is the physical one or that the geometry is the physical
geometry or selects (2), the non-adoption clause governing; no independence of conditions and no
square is reported (3); no target's verdict is inferred from another's beyond the placed consumptions
(4); no positive label is claimed from the absence of a counterexample or from anything but the named
route (5); no witness is said to settle a cell other than its own (6); no earlier act's verdict or
witness is rewritten or reinterpreted (7); no non-isometry is read as a physical or programme
exclusion (8); the isometries are not characterized (9); the geometry is identified with no named
geometry of any other theory (10); no theorem is attributed to the literature and no completeness is
claimed past the base star (11); nothing is said about the threading, the cross-time representative,
act 16's cell, act 14's carriers, act 18's `D`-axis, act 10's anchor axis, Track I, Source B or C, or
the substratum rounds (12); `P0` is not closed (13); no merged statement is strengthened, superseded
or extended (14); no continuity, smoothness, generation, one-parameter structure or composition in
time is imported, and `N` is not a limit (15); OI and QM are not said to be inequivalent (16); no
list is said to be exhaustive (17); the headline is the vector and no single label (18); `Φ_conj` is
not said to be admissible as a law or to survive the ladder, and its `L4n` status is not reported
(19); and the metric-dependence of the discrimination verdicts is stated with the freeze's two
qualifications and no stronger (20). Every target is reported with its frozen sentence, and no
outcome reached its wording by any other route.

## 15. The relation to acts 12, 13, 17, 18, 20, 21, 22 and 23

| act | what is consumed | at what strength |
| --- | --- | --- |
| act 7 | `AdmissibleDilationAt`, the readback convention, `D4b` negative, `D5` NOT CERTIFIED | merged; none re-proved |
| act 12 | `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `fibreGram_apply`, `gramPhaseEquiv_cross_invariant`, `sh1_necessity`, `sh1_sufficiency`, `fibreGram_posSemidef`, the Hadamard objects through `witness_supply`; the cross-invariant recorded by `GEO0` as one invariant at one pair | merged; none re-proved; no merged statement enlarged |
| act 13 | `WeakAnchorStabilizer`, `fibreGram_left_mul`, `fibreGram_mul_weak_apply`, `weak_anchor_coeff_norm_one` | merged; consumed in control (b) |
| act 17 | `GramTrajEquiv` through act 18's definitions; `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, `gramPhaseEquiv_trans` | merged; none re-proved |
| act 18 | `ProperAt`, `PropagatesFrom`; the `LC2` pseudometric recorded by `GEO0` as the geometry this round's is measured against, not reused | merged; none re-proved |
| act 20 | `RelabelTransition`, `TwistedNatural` | merged; consumed as declarations; `L4n` named in no statement of this round |
| act 21 | `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, `FactorizesOnProduct`, `LadderConds`'s conjuncts, `witness_supply`, `hadamard_entries`, `product_realizable`, `product_cross`, `relabel_product`, `relabel_one`, `ol1a_descent`, and `phiI_ladder`, `phiP_ladder`, `phiC_census`, `phiT_l2_restricts`, `phiPP_ladder`, `phiCTRL_census` as the families' merged equations | merged; the ladder consumed unrestated; act 21's verdicts untouched |
| act 22 | `phiSwap_l5_restricts` (the prefix and the `L5` failure of `Φ_swap`, consumed in cell `a3`), the family's merged equation | merged; consumed as landed |
| act 23 | `gramPhaseEquiv_fst_of_product`, `hadamard_z_admissible`, `fibreGram_z_entries`, `zseq_facts`, `gap_separations`, `phiSC_corner` (the prefix and `L5` of `Φ_SC`, consumed in cell `a1`), the four families' merged equations | merged; consumed as landed |

**No merged label is revised.** **A merged statement is not enlarged by being consumed.** The
direct-branch statement is carried unchanged: `D4a` positive on the direct branch; `T1` **necessary,
not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what fraction of OI
lies in the direct sector**; `D5` NOT CERTIFIED.

## 16. The definition budget

**One slot was budgeted, and one definition was introduced.** The module carries exactly one
top-level definition, whose body is the freeze's, verbatim:

```
def mixedTriple (G : V → Matrix V V ℂ) : (V × V × V) × (V × V × V) → ℂ :=
  fun p => G p.1.1 p.2.1 p.2.2.1 * G p.1.2.1 p.2.2.1 p.2.2.2 * G p.1.2.2 p.2.2.2 p.2.1
```

and no `abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque`; the geometry, the isometry
proposition, every rung as act 21's declaration consumed, the twelve families, the Fourier family,
the sequence and its rotation, the product tuples, the Hadamard objects and the permutations are
bound variables pinned by equations in the statements that need them, and the prefix through `L4d`
is written out as the first seven conjuncts of `LadderConds` in every statement that needs it.
**Sixty-two named results.**

## 17. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants**, with `B = d0fcdbc03c4b828d630f677253cf0914f451b63d`, certified through the validator's
prospective path by the one keyed call `_si2_authority('OGS', tag='R7-OGS')`. The question is asked
of the real `pull_request.head.sha` in pull-request continuous integration and of `HEAD` otherwise,
**never** of the synthetic merge commit; an unresolvable head **fails closed** with no fallback; the
check excludes pre-freeze side history by requiring every commit in `git rev-list H ^B` to be itself
a descendant of `B`; and the guard recovers whatever history it needs and fails if recovery fails.

**The validator's classification of `OGS`**: `EXECUTION` at every head of the execution, printed by
the `R7-OGS` clause from the packaging commit on and read at `E` from the continuous-integration log
of the certification of record; `LANDED-PENDING-PIN` at `L`, permitted there and failing every
descendant as seal pending; `ARCHIVED` from `P`, which writes `verification/seals/OGS.json` with its
three fields and removes the `OGS` entry from the prospective declaration, and touches nothing else.

**The supersession table is empty and is honoured as empty**: no contract of any closed round was
edited, at any commit of this branch; at the stage-A commit and at every later head every closed
round's guard classifies its own record and passes.

**`SI-3`'s standing zero-legacy-statement contract holds at every head**: `_SI2_LEGACY_RE` finds zero
assignment statements in the guard file at `B` and at every commit of this branch, and no name
matching `_OGS_(BASE|SEALED_HEAD|MERGE)` exists anywhere.

### The ten preconditions, each at its scope, as the base check reported them at `M` and at `B`

The freeze's machine-checkable block carries twenty-three `frozen-blob` lines and twenty-five rows;
the base check reported `OK (mode M, 25 row(s), no failure)` at the candidate merge of pull request
#689 on run 35457437686 and `OK (mode B, 25 row(s), no failure)` at `B` on run 35458160449.

| # | scope | precondition | result |
| --- | --- | --- | --- |
| 1 | `D` | the names were free when chosen | **PASS** — rows `d1-tag-free`, `d1-stem-free`, `d1-bare-free`, `d1-module-free`, `d1-dir-free`, `d1-act-free`, `d1-def-free`: measured at `D`, recorded, `D` an ancestor of `B` |
| 2 | `D` | the seals tree at `D` is the pinned one | **PASS** — row `d2-seals-tree`, `9f762b8d0b5656950e5030c4eb9ca6514362cce0`, twenty-eight records |
| 3 | `D` | the guard at `D` is green and carries no legacy constant | **PASS** — eighty-seven tags on run 35451692651; zero legacy statements |
| 4 | `D → B` | `D` is an ancestor of `B` | **PASS** — row `db4-ancestor` |
| 5 | `D → B` | the blobs this round consumes are unchanged | **PASS** — twenty-three `frozen-blob` lines, each matched at `M` and at `B` |
| 6 | `B` | no act 24 execution object exists | **PASS** — rows `b6-guard-clean`, `b6-no-record`, `b6-no-module`, `b6-no-def`, `b6-dir-control-plane-only` |
| 7 | `B` | no round is executing at `B` | **PASS** — row `b7-no-prospective`, `_MANIFEST_PROSPECTIVE = {}` at `B` |
| 8 | `B` | acts 21, 22 and 23 are sealed at `B` | **PASS** — rows `b8-olt-sealed`, `b8-oln-sealed`, `b8-olg-sealed`, `b8-olt-guard`, `b8-oln-guard` and `b8-olg-guard` |
| 9 | `B` | acts 21's, 22's and 23's modules are wired | **PASS** — rows `b9-import-olt`, `b9-import-oln` and `b9-import-olg` |
| 10 | `B` | this control plane is in the tree at its path | **PASS** — row `b10-self-present`, and the blob verified by `git hash-object` as the first act |

**No sibling lane's merge is a precondition of this round**, and none was waited for.

**The claim is scoped to the repository record.**

## 18. The axiom table — one line per named result

| named result | axioms |
| --- | --- |
| `mixedTriple_gauge` | `[propext, Classical.choice, Quot.sound]` |
| `mixedTriple_cross` | `[propext, Classical.choice, Quot.sound]` |
| `mixedTriple_star` | `[propext, Classical.choice, Quot.sound]` |
| `coord_le_dist` | `[propext, Classical.choice, Quot.sound]` |
| `zseq_dist` | `[propext, Classical.choice, Quot.sound]` |
| `hadamard_i_cross_all` | `[propext, Classical.choice, Quot.sound]` |
| `hadamard_one_cross_all` | `[propext, Classical.choice, Quot.sound]` |
| `fibreGram_z_cross02` | `[propext, Classical.choice, Quot.sound]` |
| `norm_one_of_star_mul` | `[propext, Classical.choice, Quot.sound]` |
| `entry_bound_aux` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_entry_norm` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_entry_diff` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_coord_diff` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_feature_norm` | `[propext, Classical.choice, Quot.sound]` |
| `geo1_separation_star` | `[propext, Classical.choice, Quot.sound]` |
| `realizable_entry_ne_zero` | `[propext, Classical.choice, Quot.sound]` |
| `geo1_separation_single` | `[propext, Classical.choice, Quot.sound]` |
| `geo1_separation_product` | `[propext, Classical.choice, Quot.sound]` |
| `dist_eq_norm_toLp` | `[propext, Classical.choice, Quot.sound]` |
| `geo1_metric_props` | `[propext, Classical.choice, Quot.sound]` |
| `geo1_class_invariant` | `[propext, Classical.choice, Quot.sound]` |
| `geo1_zero_of_equiv` | `[propext, Classical.choice, Quot.sound]` |
| `features_eq_of_dist_zero` | `[propext, Classical.choice, Quot.sound]` |
| `geo1_equiv_of_zero_single` | `[propext, Classical.choice, Quot.sound]` |
| `geo1_equiv_of_zero_product` | `[propext, Classical.choice, Quot.sound]` |
| `geo1_triple_metric` | `[propext, Classical.choice, Quot.sound]` |
| `mixedTriple_continuous` | `[propext, Classical.choice, Quot.sound]` |
| `mixedTriple_relabel` | `[propext, Classical.choice, Quot.sound]` |
| `geo2_relabel_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo2_twoSided_trivial` | `[propext, Classical.choice, Quot.sound]` |
| `mixedTriple_product` | `[propext, Classical.choice, Quot.sound]` |
| `geo2_product_tensor` | `[propext, Classical.choice, Quot.sound]` |
| `geo2_controls` | `[propext, Classical.choice, Quot.sound]` |
| `fourier_dist_le` | `[propext, Classical.choice, Quot.sound]` |
| `realizable_prod_of_adm` | `[propext, Classical.choice, Quot.sound]` |
| `coord_cross_product` | `[propext, Classical.choice, Quot.sound]` |
| `one_le_norm_I_sub_one` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiI_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiP_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiC_not_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiT_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiPP_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiSwap_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiConj_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiPC_not_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiMD_not_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiCTRL_not_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiSC_not_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `geo3_phiHS_not_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `conj_eq_transpose` | `[propext, Classical.choice, Quot.sound]` |
| `realizable_conj` | `[propext, Classical.choice, Quot.sound]` |
| `conj_conj` | `[propext, Classical.choice, Quot.sound]` |
| `conj_gramPhaseEquiv` | `[propext, Classical.choice, Quot.sound]` |
| `conj_cross` | `[propext, Classical.choice, Quot.sound]` |
| `relabel_product_cross` | `[propext, Classical.choice, Quot.sound]` |
| `conj_fibreGram_one` | `[propext, Classical.choice, Quot.sound]` |
| `conj_fibreGram_negOne` | `[propext, Classical.choice, Quot.sound]` |
| `conj_product` | `[propext, Classical.choice, Quot.sound]` |
| `geo4_a0_isometry_injective` | `[propext, Classical.choice, Quot.sound]` |
| `geo4_a1_l5_not_implies_geo` | `[propext, Classical.choice, Quot.sound]` |
| `geo4_a3_geo_not_implies_l5` | `[propext, Classical.choice, Quot.sound]` |
| `geo4_b0_not_relabel_rigid` | `[propext, Classical.choice, Quot.sound]` |

No `sorry`, no `native_decide`, no added axiom; `lake build OIBridge.OrbitGeometrySelector` completes
with zero warnings.

## 19. The predictions, reported against their outcomes

| target | prediction | outcome | reported as |
| --- | --- | --- | --- |
| `GEO0` | negative, high | `GEO0`-silent | **as predicted** |
| `GEO1` | `GEO1-METRIC`, high | `GEO1-METRIC` | **as predicted** |
| `GEO1-T` | `HOLDS`, medium, an observation entering no label | `GEO1-T-UNDECIDED`: continuity proved, compactness not attempted | **not as predicted**; enters no label |
| `GEO2` | `GEO2-CONTROLS-PASS`, high | `GEO2-CONTROLS-PASS` | **as predicted** |
| `GEO3` | `GEO3-DISCRIMINATES` via `ΦCTRL` and `Φ_SC`, medium, with the census as the family tables predict | `GEO3-DISCRIMINATES` via both, the twelve verdicts as the tables predict | **as predicted** |
| `GEO4` | `GEO4-UNDECIDED`; `a0` holds, `a1` and `a3` `NOT-IMPLIES`, `a2` and `a4` `UNDECIDED`, `b₀` `NOT-RIGID`; medium for the cells, high for `b` | the same, cell for cell | **as predicted** |

## 20. The observation for the classification round, stated once and narrowly

If a later round freezes the classification act 21 named as the obstruction to `L-FAMILY`: a
classification of the isometries of this geometry at the product configuration must **exclude**
`ΦCTRL`, `Φ_SC`, `Φ_MD`, `Φ_PC` and `Φ_HS`, each proved not an isometry, modulo the frozen law
equivalence, and must **account for** `ΦPP`, `Φ_swap` and `Φ_conj`, each proved an isometry; at the
single-carrier configuration it must exclude `ΦC` and account for `ΦI`, `ΦP` and `ΦT`. **These results
place no inclusion requirement on the separate single-carrier classification at `Γ ≡ ¼`, `|A| = 1`
beyond that accounting, and no requirement that any parameter set contain any group or any family.**
It is an observation for that round and not a finding of this one. The anti-expansion rule collected
no further observation: no thirteenth family, no second invariant family or geometry, no further
equivalence, rung, configuration or control, and no completeness statement for tuples with zero
entries was noticed.

## 21. The provenance as honoured

The rungs of the prefix and `L5` were consumed as act 21's declarations at blob
`860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` and restated nowhere; the equivalence is act 12's at
blob `4bba2040c33424fafbc6d31c0d63b86dff33691a`; the quotient list, the two configurations and the
non-adoption clause are act 21's unchanged, the clause with "Act 24" in its first sentence as the
freeze directs; the witness supply is act 21's and act 23's extended by the three frozen items 8–10,
each proved in the module commit; the eleven families of the record are consumed at their merged
equations and `Φ_conj` is this freeze's; the invariant family and the geometry are this round's
objects of test. The freeze is not edited.

## 22. The discrepancies — recorded and not repaired

**One item is recorded. It is not repaired, and the frozen document is not edited.** It is an index
of the freeze's reading that the kernel reads differently; the labels are earned by what the kernel
proves and by nothing stated in the reading.

**DF1 — the product pair written "`((0,1),(0,0))`".** The freeze's `Φ_HS` argument names "the
cross-invariant coordinate of the product pair `((0,1),(0,0))`", and `Φ_conj`'s analysis names the
same pair for the `ProperAt` separation and for the `b₀` refutation. Read literally as `(i₀, i₁)`
with `i₀ = (0,1)` and `i₁ = (0,0)`, that coordinate on `F(z) ⊠ G(H₁)` carries `G(H₁)`'s invariant at
`(1,0)` and `F(z)`'s at `(0,0)`, and is `z`-free. The pair the values the freeze states belong to is
`i₀ = (0,0)`, `i₁ = (1,0)` — act 21's `product_separations` pair, at which the value on `F(z) ⊠ G(H₁)`
is `z/256` times the diagonal — and that is the pair the kernel proofs read (`geo3_phiHS_not_isometry`,
`geo4_b0_not_relabel_rigid`); the freeze's stated values `1/256`, `−1/256`, `i/256`, `−i/256` and
`zs n/4096` hold there. The `ΦCTRL` pair `((0,0),(0,2))` and the `Φ_SC` pair `((0,0),(2,0))` are
used exactly as frozen. The wording is read as a transposition of the pair and is not repaired.

**No start-state discrepancy arose**, in any of the twenty-three pinned blobs, in any of the four
files written onto, or in any of the ten preconditions: **every one matches** and **all ten pass**.
**No candidate discovered during execution was executed.** **No configuration was chosen after an
outcome was known.** **No alternative witness was substituted for a named one.** **No target was
executed out of order, and no verdict commit carries a later target's result.**

## 23. The provenance of this note

Every frozen sentence in this note — the `GEO0`-silent sentence, the `GEO1-METRIC`,
`GEO2-CONTROLS-PASS`, `GEO3-DISCRIMINATES` and `GEO4-UNDECIDED` sentences, the six `Φ`-ISOMETRY and
six `Φ`-NOT-ISOMETRY carriages, the six cell carriages, the outcome-vector row, the `P0` sentence,
the ordering obligation, the anti-contamination invariant and the three carriages of THE CLAUSE — was
extracted by line range from the frozen preregistration blob `3b61d6c9…` at `B` and not retyped,
and the `R7-OGS` clause pins each by the same extraction.
