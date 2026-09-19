# Track B act 23 — the gaps of act 21's ladder, bundled: `L1`, `L3i`, `L3s` and the fourth corner of `L4n`/`L5`, at act 21's product configuration: RESULT

Executed under the frozen control plane `preregistration.md` in this directory, blob
**`93c06674792fa3565f6f94e5e954e484dca33cf2`**, from `main` at **`64214bfb0ae41b9f0a4fb11159089fff32d4dd85`** —
the certified merge commit of that control plane, the round's mandated execution base `B`, certified
by main-push run 35445878205 with all four jobs green and the control-plane base check in mode `B`
reporting twenty rows and no failure — which this execution verified by blob as its first act,
before any target was executed.

**Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n`

**The headline is row 1 of the freeze's outcome-vector table, verbatim.** `G0` silent; `G1` landed
via `Φ_MD`; `G2` landed via `Φ_PC`; `G3` landed via `Φ_HS`; `G4` landed via `Φ_SC`, with its
corollary. Every verdict is of the exact frozen declaration at the exact frozen configuration, for
the ordered decomposition `e = Equiv.refl`, and of nothing in its neighbourhood. **No verdict was
inferred from another.** **No independence of rungs is asserted**: four named laws occupy four
targets, and each target's label is earned by its own witness and by nothing else. **No surviving
law is said to interact, couple or fail to compose in any other sense.** **Act 21's and act 22's
historical verdicts stand unchanged**: `L1-UNDECIDED`, `L3i-UNDECIDED` and `L3s-UNDECIDED` were the
correct verdicts under act 21's freeze, act 22's `L4n-RESTRICTS`, `L5-RESTRICTS` and
`PREFIX-NOT-IMPLIES-L5` stand exactly as act 22 states them, and this round's labels are earned
under this freeze.

> **THE CLAUSE, carried at this mention — the headline.**
> Act 23 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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
| the mandated execution base | the prospective declaration `_MANIFEST_PROSPECTIVE = {'OLG': '64214bfb0ae41b9f0a4fb11159089fff32d4dd85'}` in `verification/lean/edge_rigidity_probe.py` | **declared**; the validator classifies `OLG` as `EXECUTION` against it | **removed** by `P` |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': '64214bfb0ae41b9f0a4fb11159089fff32d4dd85', 'authorized': ('OLG',)}` | the twenty-seven records of the seals tree `981a23a164b091ae0093facf81f7bd5ccf12e004` at `B`, plus the one addition authorized by stem | unchanged |
| the round's manifest record | `verification/seals/OLG.json` | **absent** | **written by `P`**: `{"round": "OLG", "kind": "sealed", "base": "64214bfb0ae41b9f0a4fb11159089fff32d4dd85", "sealed_head": E, "merge": L}` |

**`OLG.json` is absent at execution and is written by `P` and by nothing before `P`.** That is a
statement about this execution and stays true as one. **No legacy seal constant is written**: nothing
matching `_OLG_(BASE|SEALED_HEAD|MERGE)` exists at any commit of this branch, and `SI-3`'s standing
contract — zero legacy assignment statements in the guard file — holds at every head. **No existing
manifest record is altered**: the twenty-seven records at `B` are read and never written, and the
chronology verdict is the validator's through one keyed call, `_si2_authority('OLG', tag='R7-OLG')`.
**No closed round's contract is edited**: the supersession table is empty, and every closed round's
guard reads its own record at every head of this branch.

**The base-blob verification is recorded.** `git cat-file -p 64214bfb:verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/preregistration.md | git hash-object --stdin`
returns `93c06674792fa3565f6f94e5e954e484dca33cf2`, the blob the freeze names and the blob the
`R7-OLG` clause pins; `git rev-parse 64214bfb:…/preregistration.md` returns the same.

**The files this round writes** are the new module `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean`,
this result note, one import line in `verification/lean-mathlib/OIBridge.lean` (directly after act
22's module, line 211), one census entry in `verification/lean-manuscript-census.json`, the `R7-OLG`
clause with the two declarations in `verification/lean/edge_rigidity_probe.py`, and the frozen
post-round sentence appended to the `P0` row of `verification/ROADMAP.md` after act 22's. **No
manuscript file is written.**

## 2. The start state

**Every one of the nineteen paths the freeze pins by blob was checked at `B` by `git rev-parse`, and
every one matches**; the first thirteen are also the `frozen-blob` lines of the freeze's
machine-checkable block, which the base check verified at `M` (run 35445184572, at the candidate
merge of pull request #686) and at `B` (run 35445878205). The four files this round writes onto carry
their pinned blobs at `B`: `verification/ROADMAP.md` at `1379654dd278502ce0b588c6b0dac94b9314f2e7`,
`verification/lean/edge_rigidity_probe.py` at `36bb18b1ca7430f6dec6bc9877e4b51a1c0fef52`,
`verification/lean-mathlib/OIBridge.lean` at `30a4d439a3ac17e408ea9298292d8070078a8e69` and
`verification/lean-manuscript-census.json` at `0c258131533c2754cf8bd1b1d851f9dee6cd9fdf`. The seals
tree at `B` is `981a23a164b091ae0093facf81f7bd5ccf12e004`, twenty-seven records, twenty-one `sealed`
and six `base-only`, no `OLG.json`.

**No start-state discrepancy arose in any pinned blob.** `D = 59c1b7ef…` and `B` are distinct
commits, as the freeze reads them: the drafting-time facts are facts about `D`, the pins are read at
`B`, and every pinned blob is the same at both, the tree at `B` differing from the tree at `D` by
exactly the one added preregistration file (1654 lines, no other path).

**The anti-contamination invariant is honoured**, carried in the freeze's own wording:

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

Sibling lanes present at `B` are not inputs and none was read. The start-state table is the complete
list of what this round consumes.

## 3. The ordering obligation's records

The obligation, in the freeze's own wording, which binds this execution:

> **The ordering obligation, act 23.** The rungs are act 21's declarations at blob `860daac4…` and
> nothing else. The execution's module **states no rung, no equivalence and no top-level definition
> of any kind**; every rung it discharges or refutes is act 21's declaration applied to a family
> pinned by equation. From the first commit that adds the module to the certified head `E`, **no
> commit of the branch adds a definition, restates a rung, or uses an equivalence outside the
> frozen quotient list**; the module commit carries no verdict of any target; the four verdict
> commits follow it in the order `G1`, `G2`, `G3`, `G4`; and each witness is pinned, in every theorem
> that names it, to the equation this freeze gives it and to nothing else — `Φ_MD` to its two-time
> statement, `Φ_PC` to the collapse onto `G₁ ⊠ G₁`, `Φ_HS` to the shift along `F_n`, `Φ_SC` to
> `RelabelTransition (Equiv.prodCongr σ 1)` on the self-controlled set.
>

**Seven records, each checkable by an auditor from the branch alone.** The execution branch is
`claude/act-23-execution`, rooted at `B`, and its first-parent chain from `B` is, in order:

| # | commit | content |
| --- | --- | --- |
| 1 | `7984fcd96f5874897827dae80dbc55a81e6b470d` | **stage A**: the two declarations set to `B`, in the guard file only |
| 2 | `bdee3ece8f4af1d4ba663ceb81907d89075f00b1` | **the module commit**: Section A, the seven shared lemmas, plus the import line; no verdict |
| 3 | `98d937b0b39c51722b75e24a63f7965dfe078ff5` | `G1`: `phiMD_l1_restricts` |
| 4 | `997d2b215d3e7cbe02dc332abda81168646aaab1` | `G2`: `phiPC_l3i_restricts` |
| 5 | `b8c4b7841a3aad81ef7f143aa830e882d09a5634` | `G3`: `phiHS_l3s_restricts` |
| 6 | `96cb6e6f56908fe3fc9c1621dcbfefb9445f618c` | `G4`: `phiSC_corner` and `l5_not_implies_l4n` |

followed by the packaging commit carrying this note, the axiom table appended to the module, the
`R7-OLG` clause, the `ROADMAP` sentence and the census entry, and by whatever certification fixes as
`E`.

### 3.1 The declaration table (record 1)

| rung | the act 21 declaration consumed, at blob `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` | this round's module |
| --- | --- | --- |
| `L1` | `PreservesAdmissible`, lines 108–116, the fourth conjunct of `LadderConds` | no declaration of its own |
| `L3i` | the first conjunct of `Reversible`, lines 123–134 (the conjunct at lines 129–131) | no declaration of its own |
| `L3s` | the second conjunct of `Reversible`, lines 123–134 (the conjunct at lines 132–134) | no declaration of its own |
| `L4n` | the eighth conjunct of `LadderConds`, inline, lines 190–195: `∀ t, ∃ Ψ αL αR, (lifting) ∧ (admissibility) ∧ TwistedNatural a₀ αL αR Ψ` | no declaration of its own |
| `L5` | `FactorizesOnProduct`, lines 143–157, the ninth conjunct of `LadderConds` | no declaration of its own |
| each target's prefix | the corresponding leading conjuncts of `LadderConds`, lines 179–196, written out in every statement that needs them | no declaration of its own |

**This round's module carries no declaration of its own**: no `def`, `abbrev`, `structure`, `class`,
`instance`, `axiom` or `opaque` at any commit, and it imports `OIBridge.OrbitLawRigidityTwisted` and
`OIBridge.OrbitLawNaturalityFactorization`; `R7-OLG` checks all of this mechanically at every commit
from the module commit to the certified object. **No rung was restated and no equivalence was
widened.**

### 3.2 The stage-A commit (record 2)

**`7984fcd96f5874897827dae80dbc55a81e6b470d`.** `git show --stat` lists one file,
`verification/lean/edge_rigidity_probe.py`, +2/−3: `_MANIFEST_PROSPECTIVE = {'OLG': B}` and
`_MANIFEST_BASELINE = {'base': B, 'authorized': ('OLG',)}`, both outside the validator's
marker-bounded regions, and nothing else. The supersession table being empty, no closed round's
contract is touched. At this commit the guard printed **eighty-six `R7-*` tags, all `PASS`**,
`R7-OLT` and `R7-OLN` classified `ARCHIVED`, with `OLG` declared.

### 3.3 The module commit (record 3)

**`bdee3ece8f4af1d4ba663ceb81907d89075f00b1`**, the first commit at which the module is present. The
named results it carries are **`gramPhaseEquiv_fst_of_product`**, **`product_gramPhaseEquiv_fst`**,
**`zero_not_realizable`**, **`hadamard_z_admissible`**, **`fibreGram_z_entries`**, **`zseq_facts`**
and **`gap_separations`** — the product-marginal lemma in both directions, the non-realizability of
the zero tuple, supply item 7's admissibility and cross-invariant at every unit parameter with its
Pythagorean sequence, and the entries and separations the verdicts read — each a shared lemma and
none a verdict: no conjunct of any rung is discharged or refuted for any of the four witnesses, and
no witness is named in the module at this commit.

### 3.4 The four verdict commits (record 4)

| target | commit | named results | witness named in that section only |
| --- | --- | --- | --- |
| `G1` | `98d937b0b39c51722b75e24a63f7965dfe078ff5` | `phiMD_l1_restricts` | `Φ_MD` |
| `G2` | `997d2b215d3e7cbe02dc332abda81168646aaab1` | `phiPC_l3i_restricts` | `Φ_PC` |
| `G3` | `b8c4b7841a3aad81ef7f143aa830e882d09a5634` | `phiHS_l3s_restricts` | `Φ_HS` |
| `G4` | `96cb6e6f56908fe3fc9c1621dcbfefb9445f618c` | `phiSC_corner`, `l5_not_implies_l4n` | `Φ_SC` |

Each verdict theorem first appears at its own verdict commit and at no earlier commit; each verdict
commit carries its own target's results and nothing of a later target's; the order on the
first-parent chain is `G1`, `G2`, `G3`, `G4`.

### 3.5 The immutability span (record 5)

`git diff bdee3ece8f4af1d4ba663ceb81907d89075f00b1 <E> -- verification/lean-mathlib/OIBridge/OrbitLawGaps.lean | grep -c -E '^\+(def |abbrev |structure |class |instance |axiom |opaque )'`
**returns `0`**: no diff between the module commit and the certified head introduces a definition.
Measured at the `G4` commit and again at the packaging commit, whose only change to the module is
the axiom table of twelve `#print axioms` lines, and re-run by `R7-OLG` on every head from the module
commit to the certified object.

### 3.6 The quotient record (record 6)

**The only equivalence used in any verdict is act 12's `GramPhaseEquiv`**, through
`gramPhaseEquiv_cross_invariant`, `relabel_gramPhaseEquiv`, `gramPhaseEquiv_of_relabel`, act 17's
`gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and `gramPhaseEquiv_trans`, and this round's two
product-marginal lemmas, which are statements about it; act 17's `GramTrajEquiv` enters only through
act 18's `ProperAt` and `PropagatesFrom` as consumed, and act 21's `LawEquiv` is not used. **No
equivalence was introduced or widened during execution**, and no candidate equivalence was noticed.

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

**What the execution did in this span**, bearing on any target not yet closed at its end: verified the frozen blob at `B` and every other pinned blob; wrote and committed the stage-A edits and ran the guard at that commit; read act 21's merged module at its pinned blob — the ladder declarations, `witness_supply`, `hadamard_entries`, `product_separations`, `product_realizable`, `product_cross`, `relabel_product`, `ol1a_descent`, `phiPP_ladder` and `phiCTRL_census` — and act 22's merged module, to reuse their proof shape; wrote the seven lemmas of Section A and built them, the builds revealing compile errors in the unitarity computation and in the sequence's arithmetic and then that the lemmas compile, and nothing else. No proof, search or experiment about any witness's rung status was attempted or run, no build output revealed any, and the execution reasoned to no fact bearing on any target beyond what the freeze and the pinned blobs state. One value of the freeze's reading, `Gᵢ 0 0 3 · G₁ 0 0 0 = −i/16` in `Φ_SC`'s refutation, was known before execution to differ from act 21's merged `hadamard_entries` (`Gᵢ 0 0 3 = 1/4`, so `1/16`); it was noticed while the control plane was drafted, is a discrepancy of the reading recorded in §22 and not a fact about any rung's status, since the refutation needs only that the entry is nonzero.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's proof route for every target — `Φ_MD`'s, `Φ_PC`'s, `Φ_HS`'s and `Φ_SC`'s analyses, each recorded there as the freeze's reading and not as a finding; the countercontrol table; the witness supply, item 7 included; act 21's and act 22's result notes at their pinned blobs, which record every consumed fact; act 21's merged module, whose `phiPP_ladder` and `phiCTRL_census` are the templates for every prefix and for the `L4n` refutation; act 22's merged module. Reading those is reading the freeze.

#### The span module commit → `G1`

| question | answer for the span module commit → `G1` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the freeze's `Φ_MD` section and `G1` target; wrote and built `phiMD_l1_restricts`; inside that theorem block computed the separation `[G(H₁) ⊠ G(H₁)] ≠ [G(H₁) ⊠ G(Hᵢ)]` at `((0,0),(0,1))`, which the freeze's `Φ_MD` analysis states for the two constant solutions and which `G2`'s, `G3`'s and `G4`'s analyses also state; each later verdict recomputes it inside its own block and consumes nothing from `G1`'s. The builds revealed one elaboration detail (the time-zero branch closing by `if_pos` rather than by `rfl`) and nothing about any later target. No conjunct of any later target's witness was proved, and none was reasoned to.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `Φ_MD` section, `G1` target and countercontrol row; the separation between the two constant solutions, stated in the freeze's analyses of all four witnesses.

#### The span `G1` → `G2`

| question | answer for the span `G1` → `G2` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the freeze's `Φ_PC` section and `G2` target; wrote and built `phiPC_l3i_restricts`, whose prefix proofs follow `phiCTRL_census`'s template for a time-homogeneous conditional transition. The build was clean at the first attempt and revealed nothing. No conjunct of `Φ_HS`'s or `Φ_SC`'s ladder statement was proved, and none was reasoned to.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `Φ_PC` section, `G2` target and countercontrol row; the statement that its prefix analysis is as for `Φ_MD`'s time-`0` map.

#### The span `G2` → `G3`

| question | answer for the span `G2` → `G3` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the freeze's `Φ_HS` section and `G3` target; wrote and built `phiHS_l3s_restricts`, the injectivity proof by the case split on membership in the family the freeze describes; the build revealed one sign in a `linear_combination` coefficient and nothing about `G4`. Whether `Φ_HS` is injective on classes is `G3`'s own prefix conjunct and not a later target's. No conjunct of `Φ_SC`'s ladder statement was proved, and none was reasoned to.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `Φ_HS` section, `G3` target and countercontrol row; supply item 7 and the module commit's `hadamard_z_admissible`, `fibreGram_z_entries` and `zseq_facts`.

#### The span `G3` → `G4`

| question | answer for the span `G3` → `G4` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**What the execution did in this span**, bearing on any target not yet closed at its end: read the freeze's `Φ_SC` section and `G4` target; wrote and built `phiSC_corner` and `l5_not_implies_l4n`, the `L4n` refutation by transcription of `phiCTRL_census`'s with the roles of the factors exchanged; the build revealed one misdirected use of the class-invariance lemma and nothing else. The one docstring line that began with the word `class` was rewrapped before the commit so that the freeze's line-start definition check reads no false hit; this concerns the mechanical check and no target. No target remained open after this span, so no later target could be revealed.

**The freeze-supplied facts that were in front of the execution in this span**, listed so that the
owner can weigh them: the freeze's `Φ_SC` section, `G4` target and countercontrol row, including the product-marginal lemma's use, the factor maps, the closure of the self-controlled set under the relabelling and the exchanged-roles refutation; act 21's merged `phiCTRL_census` and act 21's `h1move` in `witness_supply`.

### 3.7.1 The history-integrity statement, and the execution defects disclosed

**No commit on this branch was amended, reset, rebased over, cherry-picked over or force-pushed
away. There are no superseded SHAs.** Before certification this execution absorbed no later `main`.

**No execution defect is recorded.** Three items are recorded as discrepancies of the freeze's
reading in §22, and none is repaired.

## 4. `G0` — the bounded search, recorded in full

**Outcome reached: `G0`-silent.**

> On the search this freeze bounds — act 21's control plane, amendment and result note, act 22's
> control plane and result note, act 21's and act 22's modules, act 20's result note and module,
> and `verification/ROADMAP.md`, against the frozen term list — the merged record decides neither
> the rung status of `L1`, of `L3i` nor of `L3s` under act 21's labels at the product
> configuration, and does not decide whether the prefix through `L4d` with `L5` implies `L4n`
> there. **The finding is that the record is silent on the point.** It is not a finding that any
> such statement is false, not a finding that one is unprovable, and not a bound on what a later
> round could prove.

**`G0` is a type-P target and carries no evidence level.** No Lean was written for it, and this
round's own theorems are not treated as retro-evidence about it.

**The file set at `B`**, as the freeze bounds it: act 21's `preregistration.md`,
`amendments/amendment-1.md` and `result.md`; act 22's `preregistration.md` and `result.md`;
`OrbitLawRigidityTwisted.lean`; `OrbitLawNaturalityFactorization.lean`; act 20's `result.md` and
`RepresentativeNaturality.lean`; and `verification/ROADMAP.md`. **The question asked of each hit**:
does this passage decide `L1`'s, `L3i`'s or `L3s`'s rung status under act 21's labels at the product
configuration, or decide whether the prefix through `L4d` with `L5` implies `L4n` there? This round's
own control plane is inside the set by construction and its hits are recorded as not relevant to the
question; the counts below are of the ten files named, the control plane excluded. The five rung
names are counted as whole tokens; the other terms as substrings.

| term | hits (act 21 prereg / amendment / result; act 22 prereg / result; act 21 module; act 22 module; act 20 result / module; ROADMAP) | recorded answer |
| --- | --- | --- |
| `L1` | 19 / 0 / 23 / 12 / 9 / 8 / 3 / 0 / 0 / 0 | **Does not supply it.** Act 21's freeze states the rung and predicts `L1-FREE` at medium with UNDECIDED allowed; act 21's result reports `L1-UNDECIDED` (its §`L1`, line 412) with the obstruction named — the implication from `L0` alone not claimed, `l1_free_on_shared_class` proving `L0 + L2 + L4d → L1` at a time-homogeneous configuration, and no `L1` violator in its frozen list; act 22's control plane and note name `L1` only as untouched; the modules carry the declaration and that lemma. |
| `L3i` | 18 / 0 / 17 / 9 / 4 / 7 / 4 / 0 / 0 / 0 | **Does not supply it.** Act 21's result reports `L3i-UNDECIDED` (line 455): `ΦC` fails `L3i` but is not `L-PROP`; act 22 names `L3i` only as untouched. |
| `L3s` | 16 / 0 / 15 / 9 / 4 / 6 / 4 / 0 / 0 / 0 | **Does not supply it.** Act 21's result reports `L3s-UNDECIDED` (line 455) for the same reason; act 22 names `L3s` only as untouched. |
| `L4n` | 53 / 1 / 49 / 78 / 39 / 11 / 19 / 3 / 0 / 0 | **Does not supply it.** Act 21's `L4n-UNDECIDED` and act 22's `L4n-RESTRICTS` via `ΦCTRL` are verdicts about `L4n`'s own status; neither decides whether the prefix with `L5` implies `L4n`. Act 20's result says in terms that it adjudicates no rung of any ladder. |
| `L5` | 62 / 0 / 50 / 80 / 44 / 18 / 15 / 0 / 0 / 0 | **Does not supply it.** Act 21's `L5-UNDECIDED`, act 22's `L5-RESTRICTS` via `Φ_swap` and act 22's `PREFIX-NOT-IMPLIES-L5` concern `L5`'s status and the implication from the prefix through `L4n` **to** `L5`; the converse direction, from `L5` with the prefix through `L4d` to `L4n`, is decided nowhere. |
| `PreservesAdmissible` | 1 / 0 / 3 / 5 / 3 / 7 / 4 / 0 / 0 / 0 | **Does not supply it.** The declaration, its use in `LadderConds`, act 21's `l1_free_on_shared_class` at a time-homogeneous configuration, and the prefix statements of acts 21 and 22; no rung-status label for `L1` beyond `L1-UNDECIDED`. |
| `Reversible` | 1 / 0 / 3 / 5 / 2 / 5 / 4 / 0 / 0 / 0 | **Does not supply it.** The declaration and its use in the prefix statements; no label for either conjunct beyond `L3i-UNDECIDED` and `L3s-UNDECIDED`. |
| `injectiv` | 5 / 0 / 1 / 0 / 0 / 3 / 0 / 1 / 3 / 2 | **Not relevant to the question.** Act 21's freeze and result state `L3i`'s wording and `ΦC`'s failure of it (not `L-PROP`); act 20's hits are the injectivity of the permutation `σ` in `RelabelLift`'s off-fibre vanishing; the `ROADMAP`'s hits are other rounds'. |
| `surjectiv` | 3 / 0 / 1 / 0 / 0 / 3 / 0 / 0 / 0 / 0 | **Not relevant to the question.** Act 21's freeze and result state `L3s`'s wording and `ΦC`'s failure of it (not `L-PROP`); act 21's module carries the declaration. |
| `RESTRICTS` | 13 / 0 / 24 / 21 / 14 / 0 / 3 / 0 / 0 / 0 | **Does not supply it.** The label's definition and its earned instances — act 21's `L0` and `L2`, act 22's `L4n` and `L5`; none for `L1`, `L3i` or `L3s`. |
| `FREE` | 19 / 0 / 4 / 8 / 5 / 0 / 0 / 0 / 0 / 0 | **Does not supply it.** The label's definition and act 21's `L1` discussion; no `FREE` label is stated or reached for `L1`, `L3i` or `L3s` anywhere, and act 22 attempted none. |
| `UNDECIDED` | 39 / 0 / 33 / 25 / 8 / 0 / 1 / 7 / 0 / 14 | **Does not supply it.** Act 21's `L1`, `L3i` and `L3s` are recorded UNDECIDED, the absence of a decision; act 20's and the `ROADMAP`'s hits are other rounds' labels. |
| `corner` | 0 / 0 / 0 / 6 / 4 / 0 / 0 / 0 / 0 / 0 | **Does not supply it.** Act 22's control plane (lines 598, 719, 951, 1011, 1048, 1339) and result (lines 373, 407) say in terms that the fourth corner is **outside** act 22, unexecuted and unnamed; no witness and no implication is decided. |
| `implies` | 1 / 0 / 0 / 4 / 6 / 0 / 2 / 2 / 3 / 6 | **Not relevant to the question.** Act 21's freeze on forbidden resemblance sentences; act 22's `PREFIX-NOT-IMPLIES-L5` (the other direction); act 20's `RNT1` chain among naturality notions; the `ROADMAP`'s hits are other rounds'. |
| `implication` | 4 / 0 / 10 / 26 / 8 / 2 / 1 / 8 / 6 / 4 | **Does not supply it.** Act 21's `UNDECIDED` sentences and `l1_free_on_shared_class`; act 22's non-implication from the prefix through `L4n` to `L5`, one-directionally, with the fourth corner named as outside; act 20's `RNT1` chain; the `ROADMAP`'s hits are other rounds'. |

**A search that finds a decision is a finding, and a search that does not is equally a finding.**
The second is what happened, and the finding is that the record is silent. Reconstructive inference
is refused as a finding here.

## 5. `G1` — the `L1` rung status, via `Φ_MD`

**Outcome reached: `L1-RESTRICTS`, via `Φ_MD`.**

> **The frozen `Li-RESTRICTS` sentence, carried for `L1`.**
> An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
> `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
> a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
> statement about the exact condition frozen under the label `Li`, at the configuration named, and
> it does **not** endorse the condition, does **not** say the programme requires it, and does
> **not** say it is the right condition to impose.

`phiMD_l1_restricts` pins `Γ₀`, `H₁`, `Hᵢ`, `Γ` and `Φ_MD` by equations — `Φ_MD`'s two-time statement
exactly as the freeze gives it: at `t = 0` the class `[G(Hᵢ) ⊠ G(H₁)]` is sent onto `G(H₁) ⊠ G(H₁)`
and every other tuple is fixed; at every `t ≥ 1` that class is sent to the zero tuple and every other
tuple is fixed — and carries the prefix conjuncts and the failure as conjuncts.

### 5.1 `Φ_MD` satisfies the prefix of `L1`

> **The frozen `Φ`-SURVIVES-PREFIX sentence, carried for `Φ_MD`.**
> The transition family named `Φ` in this round's frozen list satisfies every conjunct of the
> prefix before `Li` of the ladder act 21 fixes, at the configuration this freeze names for it,
> at evidence level 2, with each conjunct discharged separately. **This is a statement about the
> exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

Each conjunct, discharged separately:

| conjunct | discharged by |
| --- | --- |
| `ProperAt` | the constant solutions at `G(H₁) ⊠ G(H₁)` and at `G(H₁) ⊠ G(Hᵢ)`, neither in the fired class (`gap_separations`, at `((0,0),(1,0))`), inequivalent through the product cross-invariant at `((0,0),(0,1))`, `1/256` against `i/256`; the non-solution the constant trajectory at `G(Hᵢ) ⊠ G(H₁)`, whose image at time `0` is `G(H₁) ⊠ G(H₁)`, inequivalent to it at `((0,0),(1,0))`; realizability by `product_realizable` and `sh1_necessity` |
| `PropagatesFrom` | clause (i) from descent through act 21's `ol1a_descent`; clause (ii) at `t = 1`, the two constant solutions above |
| `L0` `EvolvesTotally` | on the fired class the trajectory `G₀, G(H₁) ⊠ G(H₁), G(H₁) ⊠ G(H₁), …`, realizable at every `t`; elsewhere the constant trajectory, every later `Φ_MD t` fixing it |

Descent, `Φ_MD t G ∼ Φ_MD t G'` from `G ∼ G'`, is proved inside the theorem as the step
`PropagatesFrom` clause (i) rests on; it is `L4d`, not part of `L1`'s prefix, and earns no label.

### 5.2 `Φ_MD` fails `L1`

> **The frozen `Φ`-FAILS sentence, carried for `Φ_MD` at `L1`.**
> The transition family named `Φ` fails the rung named, at the configuration this freeze names, at
> evidence level 2, with the failing conjunct and the separating class named. **This settles that
> family against that rung and nothing in its neighbourhood**, and it is not a statement that
> families of its shape fail in general.

`¬ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ_MD`, with the instance carried as conjuncts of the
statement: `G(Hᵢ) ⊠ G(H₁)` is realizable at `Γ 1`; `Φ_MD 1 (G(Hᵢ) ⊠ G(H₁))` is the zero tuple; and the
zero tuple's fibres sum to `0` and not to `1` on the non-trivial index type `Fin 4 × Fin 4`
(`zero_not_realizable`). **The failing conjunct is `∑ i, G i = 1` of `RealizableGram` at the
transition index `t = 1`; the separating class is `[G(Hᵢ) ⊠ G(H₁)]`.** Configuration: the frozen
product configuration, `|A₁| = |A₂| = 1`.

**Both together earn the label.** `L1-FREE` was not attempted and is not reportable from anything
here. `Φ_MD` fails `L2` and `L3i` too; neither is a verdict, and neither is reported as one.

**Why the label is earned here and was not earned in act 21.** A rung's label is earned by the witness
its countercontrol names, and act 21's `L1` row named none. This freeze named `Φ_MD` for `L1`
prospectively, before any execution object existed; the label is this round's, and **Act 21's
historical verdict `L1-UNDECIDED` stands as act 21's verdict**, unchanged.

> **THE CLAUSE, carried at this mention — the census, where a law survives the prefix or fails a rung.**
> Act 23 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 6. `G2` — the `L3i` rung status, via `Φ_PC`

**Outcome reached: `L3i-RESTRICTS`, via `Φ_PC`.**

> **The frozen `Li-RESTRICTS` sentence, carried for `L3i`.**
> An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
> `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
> a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
> statement about the exact condition frozen under the label `Li`, at the configuration named, and
> it does **not** endorse the condition, does **not** say the programme requires it, and does
> **not** say it is the right condition to impose.

`phiPC_l3i_restricts` pins `Γ₀`, `H₁`, `Hᵢ`, `Γ` and `Φ_PC` by equations — the collapse of
`[G(Hᵢ) ⊠ G(H₁)]` onto `G(H₁) ⊠ G(H₁)` at every `t`, every other tuple fixed — and carries the prefix
conjuncts and the failure as conjuncts.

### 6.1 `Φ_PC` satisfies the prefix of `L3i`

> **The frozen `Φ`-SURVIVES-PREFIX sentence, carried for `Φ_PC`.**
> The transition family named `Φ` in this round's frozen list satisfies every conjunct of the
> prefix before `Li` of the ladder act 21 fixes, at the configuration this freeze names for it,
> at evidence level 2, with each conjunct discharged separately. **This is a statement about the
> exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

| conjunct | discharged by |
| --- | --- |
| `ProperAt` | as for `Φ_MD`: the constant solutions at `G(H₁) ⊠ G(H₁)` and `G(H₁) ⊠ G(Hᵢ)`, the non-solution the constant trajectory at `G(Hᵢ) ⊠ G(H₁)` |
| `PropagatesFrom` | clause (i) through `ol1a_descent`; clause (ii) at `t = 1` |
| `L0` `EvolvesTotally` | the iterates `t ↦ (Φ_PC 0)^[t] G₀`, realizable at every `t` |
| `L1` `PreservesAdmissible` | the image of a realizable tuple is `G(H₁) ⊠ G(H₁)` (realizable by `product_realizable`) or the tuple itself |
| `L2` | `Φ₀ = Φ_PC 0`, by construction |

### 6.2 `Φ_PC` fails `L3i`

> **The frozen `Φ`-FAILS sentence, carried for `Φ_PC` at `L3i`.**
> The transition family named `Φ` fails the rung named, at the configuration this freeze names, at
> evidence level 2, with the failing conjunct and the separating class named. **This settles that
> family against that rung and nothing in its neighbourhood**, and it is not a statement that
> families of its shape fail in general.

At every `t`: `G(Hᵢ) ⊠ G(H₁)` and `G(H₁) ⊠ G(H₁)` are realizable, their images are the same tuple
`G(H₁) ⊠ G(H₁)`, and they are inequivalent, so the first conjunct of `Reversible`, stated in its own
words, fails. **The failing conjunct is injectivity on classes, the first conjunct of `Reversible`;
the separating classes are `[G(Hᵢ) ⊠ G(H₁)]` and `[G(H₁) ⊠ G(H₁)]`, separated by the product
cross-invariant at `((0,0),(1,0))`, values `i/256` and `1/256`.** The second conjunct of `Reversible`
is not read: `Φ_PC` fails `L3s` too, and that is not a verdict and is not reported as one.

**Both together earn the label.** `L3i-FREE` was not attempted and is not reportable from anything
here. **Act 21's historical verdict `L3i-UNDECIDED` stands as act 21's verdict**, unchanged: its
named countercontrol `ΦC` was not an `L-PROP` law, and `Φ_PC` is.

## 7. `G3` — the `L3s` rung status, via `Φ_HS`

**Outcome reached: `L3s-RESTRICTS`, via `Φ_HS`.**

> **The frozen `Li-RESTRICTS` sentence, carried for `L3s`.**
> An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
> `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
> a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
> statement about the exact condition frozen under the label `Li`, at the configuration named, and
> it does **not** endorse the condition, does **not** say the programme requires it, and does
> **not** say it is the right condition to impose.

`phiHS_l3s_restricts` pins `Γ₀`, `H₁`, `Hᵢ`, the family `H(·)`, the sequence `z_·`, the tuples `F_n`,
`Γ` and `Φ_HS` by equations — the shift `F_n ↦ F_{n+1}` along supply item 7 for `n ≥ 1`, the index
written with `Nat.find` and unique because the classes `[F_n]` are pairwise distinct, every other
tuple fixed — and carries the prefix conjuncts, `L3i` included, and the failure as conjuncts.

**The family's admissibility and the distinctness of its classes are the module commit's lemmas**:
`hadamard_z_admissible` (`H(z)` is an admissible dilation of `Γ₀ ≡ ¼` at the anchor `0` for every
`z` with `star z * z = 1`), `fibreGram_z_entries` (diagonal entry `¼`, cross-invariant `z/16` at the
fibre pair `(0,1)`, read in the verdict at `(1,0)` by commutativity) and `zseq_facts` (`z_n` unit,
`z_1 = i`, `n ↦ z_n` injective, `z_n ≠ 1`); the verdict combines them through `product_realizable`,
`sh1_necessity` and act 21's `product_cross` at `((1,0),(0,0))`, values `z_n/256` against `1/256`.
**No finiteness of the class space was assumed or claimed**: what the family exhibits is infinitely
many distinct admissible classes at the frozen configuration, and no more.

### 7.1 `Φ_HS` satisfies the prefix of `L3s`, `L3i` included

> **The frozen `Φ`-SURVIVES-PREFIX sentence, carried for `Φ_HS`.**
> The transition family named `Φ` in this round's frozen list satisfies every conjunct of the
> prefix before `Li` of the ladder act 21 fixes, at the configuration this freeze names for it,
> at evidence level 2, with each conjunct discharged separately. **This is a statement about the
> exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

| conjunct | discharged by |
| --- | --- |
| `ProperAt` | the constant solutions at `G(H₁) ⊠ G(H₁)` and `G(H₁) ⊠ G(Hᵢ)`, neither in the family (their invariant at `((1,0),(0,0))` is `1/256` and `z_n ≠ 1`), inequivalent at `((0,0),(0,1))`; the non-solution the constant trajectory at `F_1`, whose image `F_2` is inequivalent to it (`z_2 ≠ z_1`) |
| `PropagatesFrom` | clause (i) through `ol1a_descent`; clause (ii) at `t = 1` |
| `L0` `EvolvesTotally` | the iterates `t ↦ (Φ_HS 0)^[t] G₀`, realizable at every `t` |
| `L1` `PreservesAdmissible` | the image is some `F_{n+1}`, realizable, or the tuple itself |
| `L2` | `Φ₀ = Φ_HS 0`, by construction |
| `L3i` | the case split on membership in the family: both in the family, `F_{n+1} ∼ F_{m+1}` forces `n = m` and `G ∼ F_n ∼ G'`; exactly one in the family, the other's image would be in the family, a contradiction; neither, the images are `G` and `G'` |

### 7.2 `Φ_HS` fails `L3s`

> **The frozen `Φ`-FAILS sentence, carried for `Φ_HS` at `L3s`.**
> The transition family named `Φ` fails the rung named, at the configuration this freeze names, at
> evidence level 2, with the failing conjunct and the separating class named. **This settles that
> family against that rung and nothing in its neighbourhood**, and it is not a statement that
> families of its shape fail in general.

At every `t`: `F_1 = G(Hᵢ) ⊠ G(H₁)` is realizable, and no realizable `G` has `Φ_HS t G ∼ F_1` — an
image in the family is some `F_{n+1}` with `n ≥ 1`, distinct from `F_1`; an image outside the
family is `G` itself, outside the family — so the second conjunct of `Reversible`, stated in its own
words, fails. **The failing conjunct is surjectivity onto classes, the second conjunct of
`Reversible`; the separating class is `[F_1] = [G(Hᵢ) ⊠ G(H₁)]`, the one the shift never reaches.**

**Both together earn the label**, `L3i` included in the prefix: a shift that is not injective on
classes would earn nothing for `L3s`, and this one is injective by its own conjunct. `L3s-FREE` was
not attempted and is not reportable from anything here. **Act 21's historical verdict
`L3s-UNDECIDED` stands as act 21's verdict**, unchanged. **`L3s` is not inferred from `L3i`, and
`L3i` is not inferred from `L3s`**: `G2`'s and `G3`'s witnesses are separate, and no finiteness
argument was available or used.

## 8. `G4` — the corner, via `Φ_SC`

**Outcome reached: `L5-NOT-IMPLIES-L4n`, via `Φ_SC`.**

> At the frozen product configuration, the conjunction of the standing `L-PROP` hypotheses with
> `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d` and with `L5` as act 21 froze it does not imply `L4n` at
> act 20's certified strength: an exhibited transition family satisfies every conjunct of that
> prefix, factorizes into fixed local maps for the ordered decomposition named, and admits no
> twisted-natural lift, at evidence level 2. **This is a statement about the exact declarations at
> the exact configuration**: it does not say that `L4n` and `L5` are independent, does not report a
> square of independences, does not say that any law interacts or fails to compose in any sense,
> and does not say that either condition is or is not the right condition to impose.

`phiSC_corner` pins `Γ₀`, `H₁`, `Hᵢ`, `Γ` and `Φ_SC` by equations — `RelabelTransition
(Equiv.prodCongr σ 1)`, `σ = (2 3)` on the first factor, on the classes with a product representative
`G(Hᵢ) ⊠ G₂` or `(RelabelTransition σ G(Hᵢ)) ⊠ G₂` with `G₂` realizable, every other tuple fixed —
and carries the first seven conjuncts of `LadderConds`, `FactorizesOnProduct` and the `L4n` failure
as conjuncts. `l5_not_implies_l4n` instantiates the universal at `Φ_SC`.

### 8.1 `Φ_SC` satisfies the prefix through `L4d`

> **The frozen `Φ`-SURVIVES-PREFIX sentence, carried for `Φ_SC`.**
> The transition family named `Φ` in this round's frozen list satisfies every conjunct of the
> prefix before `Li` of the ladder act 21 fixes, at the configuration this freeze names for it,
> at evidence level 2, with each conjunct discharged separately. **This is a statement about the
> exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

| conjunct | discharged by |
| --- | --- |
| `ProperAt` | the constant solutions at `G(H₁) ⊠ G(H₁)` and `G(H₁) ⊠ G(Hᵢ)`, neither fired — by the product-marginal lemma `gramPhaseEquiv_fst_of_product` against act 12's `[G(H₁)] ≠ [G(Hᵢ)]` (`hadamard_slices_not_twoSided`, through `witness_supply`) and act 21's `[G(H₁)] ≠ [σ G(Hᵢ)]` (`h1move` in `witness_supply`) — and inequivalent at `((0,0),(0,1))`; the non-solution the constant trajectory at `G(Hᵢ) ⊠ G(H₁)`, fired to `(σ G(Hᵢ)) ⊠ G(H₁)`, inequivalent to it at `((0,0),(2,0))`, values `1/256` and `i/256` (`gap_separations`) |
| `PropagatesFrom` | clause (i) through `ol1a_descent`; clause (ii) at `t = 1` |
| `L0` `EvolvesTotally` | the iterates `t ↦ (Φ_SC 0)^[t] G₀`, realizable at every `t` by `realizable_relabel` (`Γ ≡ 1/16` invariant under `σ × 1`) |
| `L1` `PreservesAdmissible` | `realizable_relabel` on the fired branch; the identity elsewhere |
| `L2` | `Φ₀ = Φ_SC 0`, by construction |
| `L3i` and `L3s` | `Φ_SC t ∘ Φ_SC t = id` exactly: `σ` is an involution (`relabel_relabel_symm` with `(σ × 1).symm = σ × 1`), and the fired set is closed under the relabelling (`relabel_product` and `relabel_one` carry `G(Hᵢ) ⊠ G₂` to `(σ G(Hᵢ)) ⊠ G₂` and back), so injectivity and surjectivity follow as `phiCTRL_census` proves them for `ΦCTRL` |
| `L4d` | `relabel_gramPhaseEquiv`, the branch condition being a property of the class |

### 8.2 `Φ_SC` satisfies `L5`, with its factor maps named

`FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ_SC`
holds with **the factor maps `Φ₁ t G₁ := RelabelTransition σ G₁` when `G₁ ∼ G(Hᵢ)` or
`G₁ ∼ RelabelTransition σ G(Hᵢ)`, and `G₁` otherwise, and `Φ₂ t G₂ := G₂`**, both fixed before the
inputs as the declaration's quantifier order requires. For realizable `G₁`, `G₂`: on the fired branch
`Φ_SC t (G₁ ⊠ G₂) = RelabelTransition (σ × 1) (G₁ ⊠ G₂) = (RelabelTransition σ G₁) ⊠ G₂` **exactly**,
by `relabel_product` and `relabel_one`, and the displayed equivalence is `gramPhaseEquiv_refl`; on the
other branch both sides are `G₁ ⊠ G₂`. That the branch of `Φ_SC` on `G₁ ⊠ G₂` is decided by the first
factor is the product-marginal lemma in both directions (`product_gramPhaseEquiv_fst` for the fired
branch, `gramPhaseEquiv_fst_of_product` against the realizable second factor's diagonal entry `¼`
for the other).

### 8.3 `Φ_SC` fails `L4n`

> **The frozen `Φ`-FAILS sentence, carried for `Φ_SC` at `L4n`.**
> The transition family named `Φ` fails the rung named, at the configuration this freeze names, at
> evidence level 2, with the failing conjunct and the separating class named. **This settles that
> family against that rung and nothing in its neighbourhood**, and it is not a statement that
> families of its shape fail in general.

At every `t`, no `Ψ αL αR` satisfies the lifting obligation, the admissibility obligation and
`TwistedNatural`, by `phiCTRL_census`'s refutation with the roles of the factors exchanged. Take the
weak anchored gauge `K = diagonal c` with `c (3,0) = −1` and `c j = 1` otherwise, so that `σ × 1`
carries `(2,0)` to `(3,0)`; the second closure conjunct makes `αR K` a weak anchored stabilizer with
phases `c'`. Reading the lifting equation at `U K` and at `U` at the entry `((0,0),(0,0),(2,0))`: on
the fired branch, with `U` a dilation of `G(Hᵢ) ⊠ G(H₁)`, `Φ_SC` relabels the gauged input, so one
side carries `c (3,0) = −1` against the entry `G(Hᵢ)^{(0)}_{03} · G(H₁)^{(0)}_{00} = 1/16`,
nonzero, and the other carries `star (c' (0,0)) · c' (2,0)` against the same entry, giving
`star (c' (0,0)) · c' (2,0) = −1`; on the identity branch, with `U` a dilation of `G(H₁) ⊠ G(H₁)`,
one side carries `c (2,0) = 1` against `G(H₁)^{(0)}_{02} · G(H₁)^{(0)}_{00} = 1/16`, nonzero, and
the other the same `star (c' (0,0)) · c' (2,0)`, giving `1`. **The induced map is fixed before the
input and cannot see the branch.** **The failing conjunct is the right closure and right
intertwining conjuncts of `TwistedNatural`, read together with the lifting obligation; the
separating classes are `[G(Hᵢ) ⊠ G(H₁)]` and `[G(H₁) ⊠ G(H₁)]`.**

### 8.4 The corner

**The prefix conjuncts, `L5` and the `L4n` failure together earn the label.** `l5_not_implies_l4n`
refutes the universal — every transition family on `Fin 4 × Fin 4` satisfying the first seven
conjuncts of act 21's `LadderConds` and `FactorizesOnProduct` for `e = Equiv.refl` satisfies the inline
`L4n` — by instantiation at `Φ_SC` through `phiSC_corner`, the witness entering by `phiSC_corner`'s
pinned equation and `rfl`, so that the equation is carried once, in `phiSC_corner`'s statement, and
the corollary's section names no other witness. **This is a statement about the exact
declarations at the exact configuration, for the ordered decomposition `e`, and about nothing in
their neighbourhood.** **No independence of rungs is asserted**: `ΦCTRL` fails both `L4n` and `L5`,
`Φ_swap` satisfies `L4n` and fails `L5`, `ΦPP` satisfies both, and `Φ_SC` satisfies `L5` and fails
`L4n`; four corners at one configuration are four facts about four named laws, and no square of
independences is reported. `L5-IMPLIES-L4n` was not attempted and is not reportable from anything
here.

## 9. The outcome vector, and what it is not

The headline is row 1 of the freeze's outcome-vector table, selected verbatim and reported in no
other wording, and it is stated once, at the head of this note. **No verdict was inferred from
another.** Each of the four labels is earned by its own target's theorem and by nothing else: `G1`'s
by `phiMD_l1_restricts`, `G2`'s by `phiPC_l3i_restricts`, `G3`'s by `phiHS_l3s_restricts`, `G4`'s by
`phiSC_corner` with `l5_not_implies_l4n`. No single-label headline, no summary label and no
combination label exists for this round.

## 10. The witness-authorization matrix, as honoured

**The witness-authorization matrix is honoured**: each witness was tested for its own target and
for nothing else, no witness was reassigned to another target, and no alternative witness was
substituted for a named one.

| witness | tested for | tested for nothing else |
| --- | --- | --- |
| `Φ_MD` | `G1`, `L1` | its failures of `L2` and `L3i` are not verdicts |
| `Φ_PC` | `G2`, `L3i` | its failure of `L3s` is not a verdict |
| `Φ_HS` | `G3`, `L3s` | its satisfaction of `L3i` is a prefix conjunct of `G3` and not a verdict about `L3i` |
| `Φ_SC` | `G4`, the corner | its satisfaction of `L1`, `L3i` and `L3s` is its prefix and not a verdict about any of them |
| `ΦCTRL`, `Φ_swap`, `ΦPP` | — | context only: the other three corners, consumed from acts 21 and 22, not re-proved, not tested, witnesses of nothing here |

The shared lemmas of the module commit are not witnesses and answer no target by themselves.
**The execution order `G1` → `G2` → `G3` → `G4` was followed**, one verdict commit per target, and
no target was executed out of order; no universal proof was attempted for any target.

## 11. The scope boundary as honoured

**No statement of this round distinguishes two lifts that `≈_O` identifies.** Every object every
verdict is stated in is a fibre-Gram tuple or its class; no lift is compared with another lift.

**Nothing here derives, recognises or approaches quantum evolution**, and nothing here says that any
surviving or failing law is, resembles, approximates or points toward it, or that the evolution is
continuous, smooth, generated or one-parameter; in particular the parameter `z` of the Fourier family
is a parameter of a frozen witness supply and not a time, a flow or a generator. `CoherentLift` is
`ℕ`-indexed and this round does not change that.

**Act 21's and act 22's verdicts are untouched in either direction**, and so are act 21's `SIOP-YES`,
its `L-WIDE` and its per-rung verdicts, and act 22's three verdicts. **Act 16's cancellation cell and
the threading question are untouched in either direction.** **Act 18's `D`-axis is untouched.**
**Act 10's anchor-axis reclassification is untouched.** Act 14's four carriers are not read and no
carrier is adopted as the physical one.

**No law outside the frozen four was tested, no rung outside `L1`, `L3i`, `L3s` and, for the corner,
`L4n` against the prefix with `L5` was tested, no configuration outside the frozen product
configuration was used, no decomposition other than `e = Equiv.refl` was used, and no equivalence
outside the frozen quotient list was used in any verdict.** No fifth candidate, no further
equivalence, no further rung, no further configuration and no universal implication for a target
whose witness had closed was discovered, and none was executed.

## 12. The non-adoption clause, carried verbatim at each mention

**THE CLAUSE is carried three times in this note** — at the headline, at the census, and here — each
carriage opening with its own naming line and carrying the complete frozen clause, from "Act 23
classifies" to "approaches quantum evolution.". Where a frozen byte-fixed sentence carries the clause's
substance in its own wording — the status rule's sentences and the `P0` row's sentence — no quotation
is inserted inside the quotation, as the freeze directs. **No law is adopted, endorsed or given
physical status by surviving.**

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 23 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 13. The frozen `P0` sentence for the case reached

**Case A** — `G0` silent, `L1-RESTRICTS`, `L3i-RESTRICTS`, `L3s-RESTRICTS` and `L5-NOT-IMPLIES-L4n` —
is the case reached, and its sentence is the frozen sentence with every clause as written for Case A,
none of the four variable clauses replaced. It is appended, verbatim, to the `P0` row of
`verification/ROADMAP.md` after act 22's sentence in the same cell, and the row's label stays
**OPEN** and two-part:

> Act 23 tests, in one bundled round with four separately frozen targets, the three rungs act 21 left undecided and act 22 did not touch, and the corner of the naturality/factorization square act 22 left outside, at act 21's product configuration and against act 21's unchanged ladder, with a closed list of four named laws frozen with it, one per target. Preservation of admissibility on the whole orbit space has content on the class: a time-inhomogeneous law, named for that rung in advance, satisfies the standing hypotheses and totality and sends an unreached admissible class to a non-admissible tuple. Injectivity on classes has content on the class: a partial collapse, named for that rung in advance, satisfies every earlier condition and merges two admissible classes. Surjectivity onto classes has content on the class and is not forced by injectivity: a shift along an infinite family of admissible classes, named for that rung in advance, satisfies every earlier condition including injectivity and misses one admissible class. Factorization over independent systems together with every condition before naturality does not force representative-level gauge-naturality: a class-conditional relabelling of one factor, named for that corner in advance, satisfies every condition before naturality, factorizes into fixed local maps for the ordered decomposition, and admits no twisted-natural lift. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no verdict is inferred from another; no independence of conditions is asserted; no surviving law is said to interact or to fail to compose in any other sense; act 21's and act 22's own verdicts stand exactly as they state them; and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

## 14. What no outcome licenses, and the status rule as honoured

The freeze's seventeen forbidden sentences are honoured in terms. No sentence of this round says that
a law is, resembles or points toward quantum evolution, or that the shift is a Hilbert-space map (1);
none says a surviving law is the physical one (2), the non-adoption clause governing; none reports an
independence of `L4n` and `L5` or a square of independences (3); no target's verdict is inferred from
another's, in either direction (4); no `FREE` label and no implied corner is claimed from absence (5);
no witness is said to settle a target other than its own (6); act 21's and act 22's verdicts and
witnesses are not rewritten or reinterpreted (7); `Φ_MD`'s failure of `L1` is not read as a physical
statement about any evolution (8); nothing is said about `Ω_t`'s cardinality beyond the distinct
classes `Φ_HS` exhibits (9); `OL1` is not read as preserving the admissible orbit space (10); nothing
is said about the threading, the cross-time representative, act 16's cell, act 14's carriers, act
18's `D`-axis, act 10's anchor axis, Track I, Source B or C, or the substratum rounds (11); `P0` is not
closed (12); no merged statement is enlarged, the Fourier family at an arbitrary parameter being this
round's supply item (13); no continuity, smoothness, generation or one-parameter structure is imported
(14); OI and QM are not said to be inequivalent (15); neither list is said to be exhaustive (16); and
the headline is the vector and no single label (17). Every target is reported with its frozen
sentence, and no outcome reached its wording by any other route.

## 15. The relation to acts 12, 13, 17, 18, 20, 21 and 22

| act | what is consumed | at what strength |
| --- | --- | --- |
| act 7 | `AdmissibleDilationAt`, the readback convention, `D4b` negative, `D5` NOT CERTIFIED | merged; none re-proved |
| act 12 | `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `fibreGram_apply`, `gramPhaseEquiv_cross_invariant`, `sh1_necessity`, `star_mul_self_eq_norm_sq`, `hadamard_slices_not_twoSided` through `witness_supply`; the Fourier family `H(z)` read at an arbitrary unit parameter as this round's supply item 7 | merged; none re-proved; no merged statement enlarged |
| act 13 | `WeakAnchorStabilizer`, `weak_preserves_admissible`, `fibreGram_mul_weak_apply` | merged; none re-proved |
| act 17 | `GramTrajEquiv` through act 18's definitions; `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, `gramPhaseEquiv_trans` | merged; none re-proved |
| act 18 | `ProperAt`, `PropagatesFrom` | merged; none re-proved |
| act 20 | `RelabelTransition`, `TwistedNatural` | merged; consumed as declarations; no lift of this round is built from act 20's |
| act 21 | `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, `FactorizesOnProduct`, `LadderConds`'s conjuncts, `witness_supply`, `hadamard_entries`, `product_realizable`, `product_cross`, `relabel_product`, `relabel_one`, `realizable_relabel`, `relabel_gramPhaseEquiv`, `relabel_relabel_symm`, `gramPhaseEquiv_of_relabel`, `ol1a_descent`, `phiPP_ladder` and `phiCTRL_census` as templates | merged; the ladder consumed unrestated; `OL1` read at its exact strength; act 21's verdicts untouched |
| act 22 | its three verdicts and its module, imported | merged; consumed as landed; nothing of it re-proved or used in any verdict of this round |

**No merged label is revised.** **A merged statement is not enlarged by being consumed.** The
direct-branch statement is carried unchanged: `D4a` positive on the direct branch; `T1` **necessary,
not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what fraction of OI
lies in the direct sector**; `D5` NOT CERTIFIED.

## 16. The definition budget

**Zero slots were budgeted, and zero definitions were introduced.** The module carries no `def`,
`abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque`; the four witnesses, the Fourier family
and its sequence, the product tuples, the Hadamard objects, the permutations and the visible families
are bound variables pinned by equations in the statements that need them, and each target's prefix is
written out as the corresponding conjuncts of `LadderConds` in every statement that needs it.
**Twelve named results.**

## 17. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants**, with `B = 64214bfb0ae41b9f0a4fb11159089fff32d4dd85`, certified through the validator's
prospective path by the one keyed call `_si2_authority('OLG', tag='R7-OLG')`. The question is asked
of the real `pull_request.head.sha` in pull-request continuous integration and of `HEAD` otherwise,
**never** of the synthetic merge commit; an unresolvable head **fails closed** with no fallback; the
check excludes pre-freeze side history by requiring every commit in `git rev-list H ^B` to be itself
a descendant of `B`; and the guard recovers whatever history it needs and fails if recovery fails.

**The validator's classification of `OLG`**: `EXECUTION` at every head of the execution, printed by
the `R7-OLG` clause from the packaging commit on and read at `E` from the continuous-integration log
of the certification of record; `LANDED-PENDING-PIN` at `L`, permitted there and failing every
descendant as seal pending; `ARCHIVED` from `P`, which writes `verification/seals/OLG.json` with its
three fields and removes the `OLG` entry from the prospective declaration, and touches nothing else.

**The supersession table is empty and is honoured as empty**: no contract of any closed round was
edited, at any commit of this branch; at the stage-A commit and at every later head every closed
round's guard classifies its own record and passes.

**`SI-3`'s standing zero-legacy-statement contract holds at every head**: `_SI2_LEGACY_RE` finds zero
assignment statements in the guard file at `B` and at every commit of this branch, and no name
matching `_OLG_(BASE|SEALED_HEAD|MERGE)` exists anywhere.

### The ten preconditions, each at its scope, as the base check reported them at `M` and at `B`

The freeze's machine-checkable block carries thirteen `frozen-blob` lines and twenty rows; the base
check reported `OK (mode M, 20 row(s), no failure)` at the candidate merge of pull request #686 on run
35445184572 and `OK (mode B, 20 row(s), no failure)` at `B` on run 35445878205.

| # | scope | precondition | result |
| --- | --- | --- | --- |
| 1 | `D` | the names were free when chosen | **PASS** — rows `d1-tag-free`, `d1-stem-free`, `d1-bare-free`, `d1-module-free`, `d1-dir-free`, `d1-act-free`: measured at `D`, recorded, `D` an ancestor of `B` |
| 2 | `D` | the seals tree at `D` is the pinned one | **PASS** — row `d2-seals-tree`, `981a23a164b091ae0093facf81f7bd5ccf12e004`, twenty-seven records |
| 3 | `D` | the guard at `D` is green and carries no legacy constant | **PASS** — eighty-six tags on run 35441377788; zero legacy statements |
| 4 | `D → B` | `D` is an ancestor of `B` | **PASS** — row `db4-ancestor` |
| 5 | `D → B` | the blobs this round consumes are unchanged | **PASS** — thirteen `frozen-blob` lines, each matched at `M` and at `B` |
| 6 | `B` | no act 23 execution object exists | **PASS** — rows `b6-guard-clean`, `b6-no-record`, `b6-no-module`, `b6-dir-control-plane-only` |
| 7 | `B` | no round is executing at `B` | **PASS** — row `b7-no-prospective`, `_MANIFEST_PROSPECTIVE = {}` at `B` |
| 8 | `B` | acts 21 and 22 are sealed at `B` | **PASS** — rows `b8-olt-sealed`, `b8-oln-sealed`, `b8-olt-guard` and `b8-oln-guard` |
| 9 | `B` | acts 21's and 22's modules are wired | **PASS** — rows `b9-import-olt` and `b9-import-oln` |
| 10 | `B` | this control plane is in the tree at its path | **PASS** — row `b10-self-present`, and the blob verified by `git hash-object` as the first act |

**No sibling lane's merge is a precondition of this round**, and none was waited for.

**The claim is scoped to the repository record.**

## 18. The axiom table — one line per named result

| named result | axioms |
| --- | --- |
| `gramPhaseEquiv_fst_of_product` | `[propext, Classical.choice, Quot.sound]` |
| `product_gramPhaseEquiv_fst` | `[propext, Classical.choice, Quot.sound]` |
| `zero_not_realizable` | `[propext, Classical.choice, Quot.sound]` |
| `hadamard_z_admissible` | `[propext, Classical.choice, Quot.sound]` |
| `fibreGram_z_entries` | `[propext, Classical.choice, Quot.sound]` |
| `zseq_facts` | `[propext, Classical.choice, Quot.sound]` |
| `gap_separations` | `[propext, Classical.choice, Quot.sound]` |
| `phiMD_l1_restricts` | `[propext, Classical.choice, Quot.sound]` |
| `phiPC_l3i_restricts` | `[propext, Classical.choice, Quot.sound]` |
| `phiHS_l3s_restricts` | `[propext, Classical.choice, Quot.sound]` |
| `phiSC_corner` | `[propext, Classical.choice, Quot.sound]` |
| `l5_not_implies_l4n` | `[propext, Classical.choice, Quot.sound]` |

No `sorry`, no `native_decide`, no added axiom; `lake build OIBridge.OrbitLawGaps` completes with zero
warnings.

## 19. The predictions, reported against their outcomes

| target | prediction | outcome | reported as |
| --- | --- | --- | --- |
| `G0` | negative, high | `G0`-silent | **as predicted** |
| `G1` | `L1-RESTRICTS` via `Φ_MD`, high | `L1-RESTRICTS` via `Φ_MD` | **as predicted** |
| `G2` | `L3i-RESTRICTS` via `Φ_PC`, high | `L3i-RESTRICTS` via `Φ_PC` | **as predicted** |
| `G3` | `L3s-RESTRICTS` via `Φ_HS`, medium | `L3s-RESTRICTS` via `Φ_HS` | **as predicted** |
| `G4` | `L5-NOT-IMPLIES-L4n` via `Φ_SC`, medium–high | `L5-NOT-IMPLIES-L4n` via `Φ_SC` | **as predicted** |

## 20. The observation for the classification round, stated once and narrowly

If a later round freezes the classification act 21 named as the obstruction to `L-FAMILY`: a
full-ladder classification at the product configuration must **exclude** `Φ_MD`, `Φ_PC`, `Φ_HS` and
`Φ_SC`, each of which fails a rung, and a classification of each one's prefix at that configuration
must **account for** it, modulo the frozen law equivalence. **These product-configuration results
place no inclusion requirement on the separate single-carrier classification at `Γ ≡ ¼`, `|A| = 1`,
and no requirement that any parameter set contain any group or any family.** It is an observation
for that round and not a finding of this one.

## 21. The provenance as honoured

The rungs `L1`, `L3i`, `L3s`, `L4n` and `L5`, and each prefix, were consumed as act 21's declarations
at blob `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` and restated nowhere; the quotient list, the
configuration, the witness supply and the non-adoption clause are act 21's unchanged, the supply
extended by the one frozen item 7 and the clause with "Act 23" in its first sentence as the freeze
directs; `ΦCTRL`, `Φ_swap` and `ΦPP` are acts 21's and 22's, consumed as context; `Φ_MD`, `Φ_PC`,
`Φ_HS` and `Φ_SC` are this freeze's, each pinned by equation in every theorem that names it. The
freeze is not edited.

## 22. The discrepancies — recorded and not repaired

**Three items are recorded. None is repaired, and the frozen document is not edited.** Each is a value
or index of the freeze's reading that the kernel computes differently; the label in each case is
earned by what the kernel proves and by nothing stated in the reading.

**DF1 — the index of `L1`'s failure.** The freeze's `Φ_MD` analysis and its countercontrol row place
the failure "at `t = 1`", and its closing sentence names the failing conjunct "at `t + 1 = 1`". The
kernel's instance is the transition index `t = 1`: the realizable tuple `G(Hᵢ) ⊠ G(H₁)` at `Γ 1` has
the zero tuple as its image `Φ_MD 1 (G(Hᵢ) ⊠ G(H₁))`, which fails `RealizableGram` at `Γ (1 + 1)`;
`Γ` being constant, the slice index is immaterial to the verdict. The wording "`t + 1 = 1`" is read
as a slip for the transition index and is not repaired.

**DF2 — the entry `Gᵢ 0 0 3 · G₁ 0 0 0`.** The freeze's `Φ_SC` analysis gives this entry the value
`−i/16`. Act 21's merged `hadamard_entries` gives `G(Hᵢ)^{(0)}_{03} = ¼` (its `e3`), so the entry is
`1/16`. The refutation needs only that the entry is nonzero, and the kernel proof reads `e3` and
`d1`; the value is recorded and not repaired. This item was noticed while the control plane was
drafted, before execution, and is disclosed in §3.7.

**DF3 — the separation `[G(H₁)] ≠ [σ G(Hᵢ)]`.** The freeze's `Φ_SC` analysis states it as "the
cross-invariant at the fibre pair `(0,2)`, values `1/16` and `−1/16`". Act 21's merged
`hadamard_entries` gives the invariant of `σ G(Hᵢ)` at `(0,2)` as `i/16` (its `r2`), and the
separation itself is act 21's merged `h1move` in `witness_supply`, which the kernel proof consumes;
the separation of the non-solution's image from the fired class is read on the product carrier at
`((0,0),(2,0))`, values `1/256` and `i/256` (`gap_separations`). The values are recorded and not
repaired.

**No start-state discrepancy arose**, in any of the nineteen pinned blobs, in any of the five files
written onto, or in any of the ten preconditions: **every one matches** and **all ten pass**. **No
candidate discovered during execution was executed.** **No configuration was chosen after an outcome
was known.** **No alternative witness was substituted for a named one.** **No target was executed
out of order, and no verdict commit carries a later target's result.**

## 23. The provenance of this note

Every frozen sentence in this note — the `G0`-silent sentence, the three `Li-RESTRICTS` carriages,
the four `Φ`-SURVIVES-PREFIX and four `Φ`-FAILS carriages, the `L5-NOT-IMPLIES-L4n` sentence, the
outcome-vector row, the `P0` sentence, the ordering obligation, the anti-contamination invariant and
the three carriages of THE CLAUSE — was extracted by line range from the frozen preregistration blob
`93c06674…` at `B` and not retyped, and the `R7-OLG` clause pins each by the same extraction.
