# Track B act 22 — does the standing prefix through `L4n` force `L5`? The factor-swap relabelling against unchanged factorization, and `ΦCTRL` named for `L4n`: RESULT

Executed under the frozen control plane `preregistration.md` in this directory, blob
**`cc83ddb9ecbc2c8e884d160d1d3ffeba2575baea`**, from `main` at **`ccd5704fd157348903cbdea746d24cf5d5498b78`** —
the certified merge commit of that control plane, the round's mandated execution base `B`, certified
by main-push run 35436608551 with all four jobs green and the control-plane base check in mode `B`
reporting sixteen rows and no failure — which this execution verified by blob as its first act,
before any target was executed.

**Outcome reached: `L4n-RESTRICTS`, `L5-RESTRICTS` and `PREFIX-NOT-IMPLIES-L5`, over act 21's unchanged ladder at act 21's frozen product configuration.** `OF0` silent; `OF1` landed via `ΦCTRL`; `OF2` landed in both parts via `Φ_swap`; `OF3` consumed; `OF4` landed. Every verdict is of the exact frozen declaration at the exact frozen configuration, for the ordered decomposition `e = Equiv.refl`, and of nothing in its neighbourhood.

**What the swap separates, stated once and one-directionally.** `Φ_swap` preserves product form and exchanges the factors; what it fails is factorization into **fixed local maps for the ordered decomposition `e`**, and what is established is that the prefix through `L4n` does not imply that `L5`. **No independence of rungs is asserted**: three named laws occupy three corners, and the fourth corner is outside this round. **No surviving law is said to interact, couple or fail to compose in any other sense.** **Act 21's historical verdicts stand unchanged**: `L4n-UNDECIDED` and `L5-UNDECIDED` were the correct verdicts under act 21's freeze, and this round's labels are earned under this freeze.

## 1. The round's shape, restated

**This is a SEALING round** under `AGENTS.md` `§A.37`, executed under the manifest protocol. It
creates new seal state — a new Lean module with new named results and a new `R7-*` guard clause —
and it lands **`E` → `L` → `P`, with `P` mandatory**.

| object | where it lives | state at this execution | state from `P` |
| --- | --- | --- | --- |
| the mandated execution base | the prospective declaration `_MANIFEST_PROSPECTIVE = {'OLN': 'ccd5704fd157348903cbdea746d24cf5d5498b78'}` in `verification/lean/edge_rigidity_probe.py` | **declared**; the validator classifies `OLN` as `EXECUTION` against it | **removed** by `P` |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': 'ccd5704fd157348903cbdea746d24cf5d5498b78', 'authorized': ('OLN',)}` | the twenty-six records of the seals tree `90d5a4ae59c931216d52a8ce9456ae906366085e` at `B`, plus the one addition authorized by stem | unchanged |
| the round's manifest record | `verification/seals/OLN.json` | **absent** | **written by `P`**: `{"round": "OLN", "kind": "sealed", "base": "ccd5704fd157348903cbdea746d24cf5d5498b78", "sealed_head": E, "merge": L}` |

**`OLN.json` is absent at execution and is written by `P` and by nothing before `P`.** That is a
statement about this execution and stays true as one. **No legacy seal constant is written**: nothing
matching `_OLN_(BASE|SEALED_HEAD|MERGE)` exists at any commit of this branch, and `SI-3`'s standing
contract — zero legacy assignment statements in the guard file — holds at every head. **No existing
manifest record is altered**: the twenty-six records at `B` are read and never written, and the
chronology verdict is the validator's through one keyed call, `_si2_authority('OLN', tag='R7-OLN')`.

**The base-blob verification is recorded.** `git cat-file -p ccd5704f:verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md | git hash-object --stdin`
returns `cc83ddb9ecbc2c8e884d160d1d3ffeba2575baea`, the blob the freeze names and the blob the
`R7-OLN` clause pins; `git rev-parse ccd5704f:…/preregistration.md` returns the same.

**The files this round writes** are the new module `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean`,
this result note, one import line in `verification/lean-mathlib/OIBridge.lean` (directly after act
21's module, line 211), one census entry in `verification/lean-manuscript-census.json`, the `R7-OLN`
clause with the two declarations and the supersession table's one edit in
`verification/lean/edge_rigidity_probe.py`, and the frozen post-round sentence appended to the `P0`
row of `verification/ROADMAP.md` after act 21's. **No manuscript file is written.**

## 2. The start state

**Every one of the fifteen paths the freeze pins by blob was checked at `B` by `git rev-parse`, and
every one matches**; the first nine are also the `frozen-blob` lines of the freeze's
machine-checkable block, which the base check verified at `M` (run 35436171509) and at `B` (run
35436608551). The four files this round writes onto carry their pinned blobs at `B`:
`verification/ROADMAP.md` at `cc08d5df3d390c34578a97e655ceb8ef0f8077c9`,
`verification/lean/edge_rigidity_probe.py` at `57fa9f040f1c628007f3188a6ecbe691a2a735fb`,
`verification/lean-mathlib/OIBridge.lean` at `7eb77dd0c0385ecb43fe572f004d1a275cba8321` and
`verification/lean-manuscript-census.json` at `2c86fbce9aac3060c146061c0ff643fc7ca37030`. The seals
tree at `B` is `90d5a4ae59c931216d52a8ce9456ae906366085e`, twenty-six records, twenty `sealed` and six
`base-only`, no `OLN.json`.

**No start-state discrepancy arose in any pinned blob.** `D = d08b932d…` and `B` are distinct commits,
as the freeze reads them: the drafting-time facts are facts about `D`, the pins are read at `B`, and
every pinned blob is the same at both, the tree at `B` differing from the tree at `D` by exactly the
one added preregistration file.

**The anti-contamination invariant is honoured**, carried in the freeze's own wording:

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

Sibling lanes present at `B` are not inputs and none was read. The start-state table is the complete
list of what this round consumes.

## 3. The ordering obligation's records

The obligation, in the freeze's own wording, which binds this execution:

> **The ordering obligation, act 22.** The rungs are act 21's declarations at blob `860daac4…` and
> nothing else. The execution's module **states no rung, no equivalence and no top-level definition
> of any kind**; every rung it discharges or refutes is act 21's declaration applied to a family
> pinned by equation. From the first commit that adds the module to the certified head `E`, **no
> commit of the branch adds a definition, restates a rung, or uses an equivalence outside the
> frozen quotient list**, and the candidate `Φ_swap` is pinned in every theorem that names it to
> `fun _ G => RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4)) G` and to nothing else.

**Five records, each checkable by an auditor from the branch alone.** The execution branch is
`claude/act-22-execution`, rooted at `B`, and its first-parent chain from `B` is, in order:

| # | commit | content |
| --- | --- | --- |
| 1 | `8150ae35c8679b599110944330b07f7afeae7b32` | **stage A**: the two declarations set to `B` and the supersession table's one edit in `R7-OLT`, in the guard file only |
| 2 | `a2f0d98a027871272d7d58951d3121abe6bcf8fa` | **the module commit**: Section A, the two lemmas `relabel_prodComm` and `gramPhaseEquiv_diag`, plus the import line; no verdict |
| 3 | `8063293a8415a9a3da249578b1a5c9c2310f1f7e` | `OF1`: `phiCTRL_l4n_restricts` |
| 4 | `e721387fcbb21cab1b86bd6a197b890a2991c5cc` | `OF2`: `phiSwap_l5_restricts` |
| 5 | `0bf3b048ade194c378407bb7d3d20eb837cc5e61` | `OF4`: `prefix_not_implies_l5` and the axiom table |

followed by the packaging commit carrying this note, the `R7-OLN` clause, the `ROADMAP` sentence and
the census entry, and by whatever certification fixes as `E`.

### 3.1 The declaration table (record 1)

| rung | the act 21 declaration consumed, at blob `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` | this round's module |
| --- | --- | --- |
| `L4n` | the eighth conjunct of `LadderConds`, inline, lines 190–195: `∀ t, ∃ Ψ αL αR, (lifting) ∧ (admissibility) ∧ TwistedNatural a₀ αL αR Ψ` | no declaration of its own |
| `L5` | `FactorizesOnProduct`, lines 143–157, the ninth conjunct of `LadderConds` | no declaration of its own |
| the prefix through `L4n` | the first eight conjuncts of `LadderConds`, lines 179–196, written out in every statement that needs them | no declaration of its own |

**This round's module carries no declaration of its own**: no `def`, `abbrev`, `structure`, `class`,
`instance`, `axiom` or `opaque` at any commit, and it imports `OIBridge.OrbitLawRigidityTwisted`;
`R7-OLN` checks both mechanically at every commit from the module commit to the certified object.
**No rung was restated and no equivalence was widened.**

### 3.2 The stage-A commit (record 2)

**`8150ae35c8679b599110944330b07f7afeae7b32`.** `git show --stat` lists one file,
`verification/lean/edge_rigidity_probe.py`, +5/−6: `_MANIFEST_PROSPECTIVE = {'OLN': B}`,
`_MANIFEST_BASELINE = {'base': B, 'authorized': ('OLN',)}`, and in `R7-OLT`'s `_olt_declarations`
the two statements `if not (_MANIFEST_BASELINE == {'base': _OLT_B, 'authorized': ('OLT',)}): return False`
removed and the declared branch made `return (_MANIFEST_BASELINE == {'base': _OLT_B, 'authorized': ('OLT',)} and _MANIFEST_PROSPECTIVE['OLT'] == _OLT_B)`,
exactly as the supersession table states; nothing else.

### 3.3 The module commit (record 3)

**`a2f0d98a027871272d7d58951d3121abe6bcf8fa`**, the first commit at which the module is present. The
named results that entered first are **`relabel_prodComm`** and **`gramPhaseEquiv_diag`**, the two
lemmas the freeze's proof route names — the exchange identity and diagonal preservation — and
nothing else: no verdict, no conjunct of any rung for any family. They entered together in one
commit, which is recorded in §21.

### 3.4 The immutability span (record 4)

`git diff a2f0d98a027871272d7d58951d3121abe6bcf8fa <E> -- verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean | grep -c -E '^\+(def |abbrev |structure |class |instance |axiom |opaque )'`
**returns `0`**: no diff between the module commit and the certified head introduces a definition.
Measured at the `OF4` commit, after which no commit of this branch touches the module, and re-run by
`R7-OLN` on every head from the module commit to the certified object.

### 3.5 The quotient record (record 5)

**The only equivalence used in any verdict is act 12's `GramPhaseEquiv`**, through
`gramPhaseEquiv_cross_invariant`, `gramPhaseEquiv_diag`, `relabel_gramPhaseEquiv` and
`gramPhaseEquiv_of_relabel`; act 17's `GramTrajEquiv` enters only through act 18's `ProperAt` and
`PropagatesFrom` as consumed, and act 21's `LawEquiv` is not used. **No equivalence was introduced
or widened during execution**, and no candidate equivalence was noticed.

## 4. The attestation set — three questions, answered as measurements for the span `B` → module commit

The three questions, in act 21's wording as this freeze consumes them:

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

| question | answer for the span `B` → `a2f0d98a…` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**A PARTIAL fact counts for all three. There is no threshold below which a fact about the candidates
does not count.** What the execution did between `B` and the module commit: verified the frozen blob
at `B`; wrote and committed the stage-A edits; read act 21's merged module at its pinned blob, in
particular the proofs of `phiPP_ladder` and `phiCTRL_census`, to reuse their proof shape; wrote the
two lemmas of Section A and built them once, the build revealing that they compile and nothing else.
No proof, search or experiment about any candidate's rung status was attempted or run before the
module commit, no build output revealed any, and the execution reasoned to no fact bearing on the
candidates beyond what the freeze and the pinned blobs already state.

**The freeze-supplied facts that were in front of the execution**, listed so that the owner can weigh
them: the freeze's proof route for every target — the exchange identity, the diagonal cancellation,
the two instances, the cross equations at `((0,0),(1,0))` and the closing step; the freeze's drafting
check with its seven recorded outcomes; act 21's result note at its pinned blob, which records
`ΦCTRL`'s failure of `L4n` in full and names the settlement this round executes; act 21's merged
module, whose `phiCTRL_census` carries every conjunct `OF1` consumes and whose `phiPP_ladder` is the
template for `OF2`'s prefix; and act 20's merged lift and exact law at arbitrary `σ`. Reading those is
reading the freeze.

### 4.1 The history-integrity statement, and the execution defects disclosed

**No commit on this branch was amended, reset, rebased over, cherry-picked over or force-pushed
away. There are no superseded SHAs.** Before certification this execution absorbed no later `main`.

**No execution defect is recorded.** Two remarks are recorded as discrepancies in §21, and neither
is repaired.

## 5. `OF0` — the bounded search, recorded in full

**Outcome reached: `OF0`-silent.**

> On the search this freeze bounds — act 21's control plane, amendment and result note, act 21's
> module, act 20's result note and module, and `verification/ROADMAP.md`, against the frozen term
> list — the merged record decides neither the rung status of `L4n` nor that of `L5` under act
> 21's labels, and does not decide whether the prefix through `L4n` implies `L5` at the product
> configuration. **The finding is that the record is silent on the point.** It is not a finding
> that any such statement is false, not a finding that one is unprovable, and not a bound on what
> a later round could prove.

**`OF0` is a type-P target and carries no evidence level.** No Lean was written for it, and this
round's own theorems are not treated as retro-evidence about it.

**The file set at `B`**, as the freeze bounds it: act 21's `preregistration.md`,
`amendments/amendment-1.md` and `result.md`; `OrbitLawRigidityTwisted.lean`; act 20's `result.md`
and `RepresentativeNaturality.lean`; and `verification/ROADMAP.md`. **The question asked of each
hit**: does this passage decide `L4n`'s or `L5`'s rung status under act 21's labels, or decide
whether the prefix through `L4n` implies `L5` at the product configuration?

| term | hits (act 21 prereg / amendment / result / module; act 20 result / module; ROADMAP) | recorded answer |
| --- | --- | --- |
| `L4n` | 53 / 1 / 49 / 11 / 3 / 0 / 0 | **Does not supply it.** Act 21's freeze states the rung and predicts nothing for it; act 21's result reports `L4n-UNDECIDED` with the obstruction named and `ΦCTRL`'s failure recorded as an observation carrying no label; act 20's result says in terms that it adjudicates no rung of any ladder. |
| `L5` | 77 / 0 / 52 / 18 / 0 / 0 / 0 | **Does not supply it.** Act 21's result reports `L5-UNDECIDED` because its named violator fails `L4n`, and names the settlement — a law with a twisted-natural lift that fails factorization by another mechanism, or a universal implication proof — without deciding either. |
| `FactorizesOnProduct` | 1 / 0 / 5 / 8 / 0 / 0 / 0 | **Does not supply it.** The declaration, its satisfaction by `ΦI` (trivial instance), `ΦPP` (with content) and its failure by `ΦCTRL`; nothing about its status as a rung or about the implication. |
| `TwistedNatural` | 15 / 0 / 6 / 6 / 8 / 8 / 0 | **Does not supply it.** Act 20's notion and its exact law for one lift; act 21's `L4n` inline; no rung status and no implication. |
| `RESTRICTS` | 13 / 0 / 24 / 0 / 0 / 0 / 0 | **Does not supply it.** The label's definition and act 21's two earned instances, `L0` and `L2`; `L4n` and `L5` carry no such label there. |
| `FREE` | 19 / 0 / 4 / 0 / 0 / 0 / 0 | **Does not supply it.** The label's definition and act 21's `L1` discussion; no `L4n-FREE` and no `L5-FREE` is stated or reached anywhere. |
| `UNDECIDED` | 39 / 0 / 33 / 0 / 7 / 0 / 14 | **Does not supply it.** Act 21's five `UNDECIDED` rungs, `L4n` and `L5` among them, are the absence of a decision; act 20's and the `ROADMAP`'s hits are other rounds' labels. |
| `factoriz` | 6 / 0 / 19 / 9 / 0 / 0 / 0 | **Does not supply it.** `L5`'s wording, the `L5` test, the product-embedding construction and `ΦCTRL`'s two-instance refutation; nothing about whether the prefix forces factorization. |
| `implies` | 1 / 0 / 0 / 0 / 2 / 3 / 6 | **Not relevant to the question.** Act 21's freeze on `L1`; act 20's implication chain among its three notions (`RNT1`); the `ROADMAP`'s hits are other rounds'. |
| `implication` | 4 / 0 / 10 / 2 / 8 / 6 / 4 | **Does not supply it.** Act 21's `UNDECIDED` sentences, which say that the absence of an implication proof is not reported as content, and its `L1` implication `l1_free_on_shared_class`, which is about `L1`; act 20's `RNT1` chain among naturality notions; the `ROADMAP`'s hits are other rounds'. |

**A search that finds a decision is a finding, and a search that does not is equally a finding.**
The second is what happened, and the finding is that the record is silent. Reconstructive inference
is refused as a finding here.

## 6. `OF1` — the `L4n` rung status, via `ΦCTRL`

**Outcome reached: `L4n-RESTRICTS`, via `ΦCTRL`.**

> **The frozen `Li-RESTRICTS` sentence, carried for `L4n`.**
> An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
> `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
> a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
> statement about the exact condition frozen under the label `Li`, at the configuration named, and
> it does **not** endorse the condition, does **not** say the programme requires it, and does
> **not** say it is the right condition to impose.

`phiCTRL_l4n_restricts`, **obtained from act 21's merged `phiCTRL_census` by projection and nothing
else**: the eight conjuncts the label requires — `ProperAt`, `PropagatesFrom`, `EvolvesTotally`,
`PreservesAdmissible`, `L2`, `Reversible`, descent, and at every `t` the non-existence of a lift
satisfying the lifting obligation, the admissibility obligation and `TwistedNatural` — are the first
eight conjuncts of the merged theorem's conclusion, restated by consumption; the ninth, the failure
of `L5`, is not consumed here. No rung is restated and nothing is re-proved. **The failing conjunct
is the right closure and right intertwining conjuncts of `TwistedNatural`, read together with the
lifting obligation**, and **the separating classes are `[G(H₁) ⊠ G(Hᵢ)]` and `[G(Hᵢ) ⊠ G(Hᵢ)]`**,
exactly as act 21's §7 records: the induced right map is fixed before the input and cannot see which
branch the input is in. Configuration: the frozen product configuration, `|A₁| = |A₂| = 1`.

**Why the label is earned here and was not earned in act 21.** A rung's label is earned by the witness
its countercontrol names, and act 21's `L4n` row named none, so act 21 recorded the failure as an
observation under the witness rule. This freeze named `ΦCTRL` for `L4n` prospectively, before any
execution object existed; the label is this round's, and **act 21's historical verdict
`L4n-UNDECIDED` stands as act 21's verdict**, unchanged.

> **THE CLAUSE, carried at this mention — the census, where a law survives the prefix or fails a rung.**
> Act 22 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 7. `OF2` — the `L5` rung status, via `Φ_swap`, in two parts

**Outcome reached: `OF2` landed in both parts, and `L5-RESTRICTS`, via `Φ_swap`.** One theorem,
`phiSwap_l5_restricts`, pins `Γ₀`, `H₁`, `Hᵢ`, `Γ` and
`Φ_swap = fun _ G => RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4)) G` by equations, as
`phiCTRL_census` pins its family, and carries both parts as conjuncts.

**The exchange identity is proved**, as its own lemma before any verdict: `relabel_prodComm`,
`RelabelTransition (Equiv.prodComm V V) (X ⊠ Y) = Y ⊠ X`, entrywise and exactly — act 21's
`relabel_product` is stated for `Equiv.prodCongr σ₁ σ₂` only and was not used at the exchange.

### 7.1 Part (a) — `Φ_swap` satisfies the prefix through `L4n`

> **The frozen `Φ`-SURVIVES-PREFIX sentence, carried for `Φ_swap`.**
> The transition family named `Φ` in this round's frozen list satisfies every conjunct of the
> prefix through `L4n` of the ladder act 21 fixes, at the configuration this freeze names for it,
> at evidence level 2, with each conjunct discharged separately. **This is a statement about the
> exact family frozen under that label**, and it does **not** endorse it, does **not** say it
> obtains, and does **not** adopt it as the physical law of evolution.

Each conjunct, discharged separately:

| conjunct | discharged by |
| --- | --- |
| `ProperAt` | the constant solution at `G(H₁) ⊠ G(H₁)` (fixed exactly by the exchange), the solution `t ↦ Φ_swap^[t] (G(H₁) ⊠ G(Hᵢ))`, and the constant at `G(H₁) ⊠ G(Hᵢ)` as the non-solution; the two solutions inequivalent at `t = 0` through the cross-invariant at `((0,0),(0,1))`; the non-solution because `[G(H₁) ⊠ G(Hᵢ)] ≠ [G(Hᵢ) ⊠ G(H₁)]` at `((0,0),(1,0))`; realizability by `product_realizable` and `sh1_necessity` |
| `PropagatesFrom` | clause (i) from descent through act 21's `ol1a_descent`; clause (ii) at `t = 1`, the two solutions above at `[G(H₁) ⊠ G(H₁)]` and `[G(Hᵢ) ⊠ G(H₁)]`, inequivalent at `((0,0),(1,0))` |
| `L0` `EvolvesTotally` | the iterate `t ↦ Φ_swap^[t] G₀`, realizable at every `t` by `realizable_relabel` (`Γ ≡ 1/16` invariant under the exchange) |
| `L1` `PreservesAdmissible` | `realizable_relabel` |
| `L2` | `Φ₀ = RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4))`, by construction |
| `L3i` | `gramPhaseEquiv_of_relabel` |
| `L3s` | the preimage `RelabelTransition (prodComm)⁻¹ G'`, realizable by `realizable_relabel`, with `relabel_symm_relabel` |
| `L4d` | `relabel_gramPhaseEquiv` |
| `L4n` | act 20's merged `RelabelLift (prodComm)`, `RelabelInducedLeft`, `RelabelInducedRight`, with `rnt2_lifting_property`, `rnt2_admissible` (`Γ` constant) and `rnt3_law_exact`, at `σ = Equiv.prodComm (Fin 4) (Fin 4)` |

### 7.2 Part (b) — `Φ_swap` fails `L5` as act 21 froze it

> **The frozen `Φ`-FAILS sentence, carried for `Φ_swap` at `L5`.**
> The transition family named `Φ` fails the rung named, at the configuration this freeze names, at
> evidence level 2, with the failing conjunct and the separating class named. **This settles that
> family against that rung and nothing in its neighbourhood**, and it is not a statement that
> families of its shape fail in general.

`¬ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ_swap`,
by the frozen route. The factor maps `Φ₁`, `Φ₂` are fixed before the inputs, so the universal is
read at two instances, `G₁ = G(H₁)` and `G₂ ∈ {G(H₁), G(Hᵢ)}`; with `X = Φ₁ 0 G(H₁)`,
`Y = Φ₂ 0 G(H₁)`, `Y' = Φ₂ 0 G(Hᵢ)`, the two displayed equivalences are
`G(H₁) ⊠ G(H₁) ∼_D X ⊠ Y` and `G(Hᵢ) ⊠ G(H₁) ∼_D X ⊠ Y'`, the second's left side being `Φ_swap` of
`G(H₁) ⊠ G(Hᵢ)` by the exchange identity. **The diagonal equations** at the product index
`((0,0),(0,0))`, through `gramPhaseEquiv_diag`, give `X 0 0 0 · Y 0 0 0 = ¼ · ¼ = X 0 0 0 · Y' 0 0 0`,
so `X 0 0 0 ≠ 0` and, cancelling it, `Y 0 0 0 = Y' 0 0 0`. **The cross-invariant equations** at the
product fibre pair `((0,0),(1,0))`, through act 12's `gramPhaseEquiv_cross_invariant` and act 21's
`product_cross`, give `(X 0 1 0 · X 1 0 1) · (Y 0 0 0)² = (1/16) · (¼ · ¼)` and
`(X 0 1 0 · X 1 0 1) · (Y' 0 0 0)² = (i/16) · (¼ · ¼)`, by `hadamard_entries`; with `Y 0 0 0 = Y' 0 0 0`
the two left sides coincide, so `1/256 = i/256`, which `norm_num [Complex.ext_iff]` refutes — the
closing step of `phiCTRL_census`. **The failing conjunct is the existence of fixed factor maps
`Φ₁`, `Φ₂` for the ordered decomposition `e`; the separating classes are `[G(H₁) ⊠ G(H₁)]` and
`[G(Hᵢ) ⊠ G(H₁)]`, the images of the two instances, and the separating invariant is act 12's
cross-invariant at `((0,0),(1,0))`, values `1/256` and `i/256`.**

**No property of the factor maps beyond the two displayed equivalences was used.** The declaration
requires no realizability, normalization or admissibility of `Φ₁ t G₁` or `Φ₂ t G₂`, none was
assumed, and the nonzero factor cancelled is a diagonal entry read from the equivalence.

### 7.3 The rung

> **The frozen `Li-RESTRICTS` sentence, carried for `L5`.**
> An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
> `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
> a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
> statement about the exact condition frozen under the label `Li`, at the configuration named, and
> it does **not** endorse the condition, does **not** say the programme requires it, and does
> **not** say it is the right condition to impose.

**Both parts together earn the label**: part (a) is the requirement that the witness satisfy every
earlier rung, part (b) the failure. What fails is factorization into **fixed local maps for the
ordered decomposition `e`**: the transition preserves product form — it sends a product class to a
product class — and exchanges the factors, and nothing here says it interacts, couples or fails to
compose in any other sense. `L5-FREE` was not attempted and is not reportable from anything here.

## 8. `OF3` — the positive control, consumed

**`phiPP_ladder`, consumed**: act 21's product permutation `Φ_{σ×σ}`, `σ = (2 3)` on each factor,
satisfies `LadderConds` in full at the same configuration, `L5` included with content — the
factorization `Φ₁ = Φ₂ = Φ_σ` an equality of tuples before any equivalence. So a law of the prefix
**can** satisfy `L5` with content at this configuration, and `OF2` (b) is a fact about `Φ_swap` and
not about the condition being empty. No Lean was written for `OF3`.

## 9. `OF4` — the non-implication

**Outcome reached: `PREFIX-NOT-IMPLIES-L5`.**

> At the frozen product configuration, the conjunction of the standing `L-PROP` hypotheses with
> `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d` and `L4n` at act 20's certified strength does not imply
> `L5` as act 21 froze it: an exhibited transition family satisfies every conjunct of that prefix
> and fails factorization into fixed local maps for the ordered decomposition named, at evidence
> level 2. **This is a statement about the exact declarations at the exact configuration**: it
> does not say that any surviving law interacts, couples or fails to compose in any other sense,
> does not say that `L5` fails at any other configuration or decomposition, and does not say that
> `L5` is or is not the right condition to impose.

`prefix_not_implies_l5`: the universal — every transition family on `Fin 4 × Fin 4` satisfying the
first eight conjuncts of act 21's `LadderConds` satisfies `FactorizesOnProduct` for
`e = Equiv.refl` — refuted by instantiation at `Φ_swap` through `phiSwap_l5_restricts`. **This is
a statement about the exact declarations at the exact configuration, for the ordered decomposition
`e`, and about nothing in their neighbourhood.** **No independence of rungs is asserted**: `ΦCTRL`
fails both rungs, `Φ_swap` satisfies `L4n` and fails `L5`, `ΦPP` satisfies both, and the fourth corner
— a law failing `L4n` and satisfying `L5` — is outside this round, unexecuted and unnamed.

> **THE CLAUSE, carried at this mention — the headline.**
> Act 22 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 10. The scope boundary as honoured

**No statement of this round distinguishes two lifts that `≈_O` identifies.** Every object every
verdict is stated in is a fibre-Gram tuple or its class; no lift is compared with another lift.

**Nothing here derives, recognises or approaches quantum evolution**, and nothing here says that any
surviving or failing law is, resembles, approximates or points toward it, or that the evolution is
continuous, smooth, generated or one-parameter. `CoherentLift` is `ℕ`-indexed and this round does
not change that.

**`L1`, `L3i` and `L3s` are untouched in either direction**, and so are act 21's `SIOP-YES`, its
`L-WIDE` and its per-rung verdicts. **Act 16's cancellation cell and the threading question are
untouched in either direction.** **Act 18's `D`-axis is untouched.** **Act 10's anchor-axis
reclassification is untouched.** Act 14's four carriers are not read and no carrier is adopted as the
physical one.

**No law outside the frozen three was tested, no rung outside `L4n` and `L5` was tested, no
configuration outside the frozen product configuration was used, no decomposition other than
`e = Equiv.refl` was used, and no equivalence outside the frozen three was used in any verdict.**
No fourth candidate, no further equivalence, no further rung, no further configuration and no
fourth-corner witness was discovered, and none was executed.

## 11. The non-adoption clause, carried verbatim at each mention

**THE CLAUSE is carried three times in this note** — at the census, at the headline, and here — each
carriage opening with its own naming line and carrying the complete frozen clause, from "Act 22
classifies" to "approaches quantum evolution.". Where a frozen byte-fixed sentence carries the clause's
substance in its own wording — the status rule's sentences and the `P0` row's sentence — no quotation
is inserted inside the quotation, as the freeze directs. **No law is adopted, endorsed or given
physical status by surviving.**

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 22 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## 12. The frozen `P0` sentence for the case reached

**Case A** — `OF0` silent, `L4n-RESTRICTS`, `L5-RESTRICTS` and `PREFIX-NOT-IMPLIES-L5` — is the case
reached, and its sentence is the frozen sentence with every clause as written for Case A. It is
appended, verbatim, to the `P0` row of `verification/ROADMAP.md` after act 21's sentence in the same
cell, and the row's label stays **OPEN** and two-part:

> Act 22 tests two of the rungs act 21 left undecided, at act 21's product configuration and against act 21's unchanged ladder, with a closed list of three named laws frozen with it. Representative-level gauge-naturality at act 20's certified strength has content on the class: act 21's controlled relabelling, named for that rung in advance, satisfies every earlier condition and admits no twisted-natural lift. Factorization over independent systems has content on the class and is not forced by the conditions before it: the relabelling that exchanges the two factors satisfies every condition through gauge-naturality and does not factorize into fixed local maps for the ordered decomposition, so the standing prefix through naturality does not imply factorization at that configuration. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no independence of conditions is asserted, no surviving law is said to interact or to fail to compose in any other sense, act 21's own verdicts stand exactly as act 21 states them, and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

## 13. What no outcome licenses, and the status rule as honoured

The freeze's sixteen forbidden sentences are honoured in terms. No sentence of this round says that a
law is, resembles or points toward quantum evolution, or that the swap is an entangling gate (1); none
says a surviving law is the physical one (2), the non-adoption clause governing; none reports an
independence of `L4n` and `L5` or a square of independences (3); none reads the failure of `L5` as
interaction, coupling or non-composition in any other sense (4); no `FREE` label is claimed from
absence (5); no inclusion requirement is placed on any classification (6); act 21's historical
verdicts are not rewritten (7); no invariant of a factor map is read from realizability (8);
`relabel_product` is not applied at the exchange (9); `OL1` is not read as preserving the admissible
orbit space (10); nothing is said about `L1`, `L3i`, `L3s`, the threading, act 16's cell, act 14's
carriers, act 18's `D`-axis, act 10's anchor axis, Track I, Source B or C, or the substratum rounds
(11); `P0` is not closed (12); no merged statement is enlarged (13); no continuity is imported (14);
OI and QM are not said to be inequivalent (15); neither list is said to be exhaustive (16). Every
target is reported with its frozen sentence, and no outcome reached its wording by any other route.

## 14. The relation to acts 12, 17, 18, 20 and 21

| act | what is consumed | at what strength |
| --- | --- | --- |
| act 7 | `AdmissibleDilationAt`, the readback convention, `D4b` negative, `D5` NOT CERTIFIED | merged; none re-proved |
| act 12 | `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `gramPhaseEquiv_cross_invariant`, `sh1_necessity`, `star_mul_self_eq_norm_sq` | merged; none re-proved |
| act 17 | `GramTrajEquiv` through act 18's definitions; `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, `gramPhaseEquiv_trans` | merged; none re-proved |
| act 18 | `ProperAt`, `PropagatesFrom` | merged; none re-proved |
| act 20 | `RelabelTransition`, `RelabelLift`, `RelabelInducedLeft`, `RelabelInducedRight`, `TwistedNatural`, `rnt2_lifting_property`, `rnt2_admissible`, `rnt3_law_exact` | merged; the lift and exact law consumed at `σ = Equiv.prodComm (Fin 4) (Fin 4)`, an instance of their arbitrary-`σ` statements |
| act 21 | `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, `FactorizesOnProduct`, `LadderConds`'s conjuncts, `witness_supply`, `hadamard_entries`, `product_realizable`, `product_cross`, `realizable_relabel`, `relabel_gramPhaseEquiv`, `relabel_symm_relabel`, `gramPhaseEquiv_of_relabel`, `ol1a_descent`, `phiPP_ladder`, `phiCTRL_census` | merged; the ladder consumed unrestated; `OL1` read at its exact strength — descent gives maps on the ambient tuple quotient and uniqueness of continuation, and preservation of the admissible orbit space is `L1`; act 21's verdicts untouched |

**No merged label is revised.** **A merged statement is not enlarged by being consumed.** The
direct-branch statement is carried unchanged: `D4a` positive on the direct branch; `T1` **necessary,
not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what fraction of OI
lies in the direct sector**; `D5` NOT CERTIFIED.

## 15. The definition budget

**Zero slots were budgeted, and zero definitions were introduced.** The module carries no `def`,
`abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque`; `Φ_swap`, `ΦCTRL`, the product tuples,
the Hadamard objects, the permutations and the visible families are bound variables pinned by
equations in the statements that need them, and the prefix through `L4n` is written out as the first
eight conjuncts of `LadderConds` in every statement that needs it. **Five named results.**

## 16. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants**, with `B = ccd5704fd157348903cbdea746d24cf5d5498b78`, certified through the validator's
prospective path by the one keyed call `_si2_authority('OLN', tag='R7-OLN')`. The question is asked
of the real `pull_request.head.sha` in pull-request continuous integration and of `HEAD` otherwise,
**never** of the synthetic merge commit; an unresolvable head **fails closed** with no fallback; the
check excludes pre-freeze side history by requiring every commit in `git rev-list H ^B` to be itself
a descendant of `B`; and the guard recovers whatever history it needs and fails if recovery fails.

**The validator's classification of `OLN`**: `EXECUTION` at every head of the execution, printed by
the `R7-OLN` clause from the packaging commit on and read at `E` from the continuous-integration log
of the certification of record; `LANDED-PENDING-PIN` at `L`, permitted there and failing every
descendant as seal pending; `ARCHIVED` from `P`, which writes `verification/seals/OLN.json` with its
three fields and removes the `OLN` entry from the prospective declaration, and touches nothing else.

**The supersession table's one edit was made at exactly the place the table names, and reported as
a measurement.** In `R7-OLT`'s `_olt_declarations`, the baseline equality
`_MANIFEST_BASELINE == {'base': _OLT_B, 'authorized': ('OLT',)}` is required in the **declared** branch
only, and the recorded branch and the docstring are unchanged. **Nothing else in `R7-OLT` was
touched**, no negative case, mutation control or tag map was touched, and the freeze recorded the
negative control at the drafting snapshot: without the disposition exactly `R7-OLT` goes red on a
simulated act 22 head, its authority and ordering conjuncts both passing, and with it the simulated
execution head and the simulated landing-plus-pin state run green. At the stage-A commit the guard
printed **eighty-five `R7-*` tags, all `PASS`**, `R7-OLT` classified `ARCHIVED` under the disposition
with `OLN` declared.

**`SI-3`'s standing zero-legacy-statement contract holds at every head**: `_SI2_LEGACY_RE` finds zero
assignment statements in the guard file at `B` and at every commit of this branch, and no name
matching `_OLN_(BASE|SEALED_HEAD|MERGE)` exists anywhere.

### The ten preconditions, each at its scope, as the base check reported them at `M` and at `B`

The freeze's machine-checkable block carries nine `frozen-blob` lines and sixteen rows; the base check
reported `OK (mode M, 16 row(s), no failure)` at the candidate merge `28ed5c98…` on run 35436171509
and `OK (mode B, 16 row(s), no failure)` at `B` on run 35436608551.

| # | scope | precondition | result |
| --- | --- | --- | --- |
| 1 | `D` | the names were free when chosen | **PASS** — rows `d1-tag-free`, `d1-stem-free`, `d1-bare-free`, `d1-module-free`, `d1-dir-free`: measured at `D`, recorded, `D` an ancestor of `B` |
| 2 | `D` | the seals tree at `D` is the pinned one | **PASS** — row `d2-seals-tree`, `90d5a4ae59c931216d52a8ce9456ae906366085e` |
| 3 | `D` | the guard at `D` is green and carries no legacy constant | **PASS** — eighty-five tags on run 35433619877; zero legacy statements |
| 4 | `D → B` | `D` is an ancestor of `B` | **PASS** — row `db4-ancestor` |
| 5 | `D → B` | the blobs this round consumes are unchanged | **PASS** — nine `frozen-blob` lines, each matched at `M` and at `B` |
| 6 | `B` | no act 22 execution object exists | **PASS** — rows `b6-guard-clean`, `b6-no-record`, `b6-no-module`, `b6-dir-control-plane-only` |
| 7 | `B` | no round is executing at `B` | **PASS** — row `b7-no-prospective`, `_MANIFEST_PROSPECTIVE = {}` at `B` |
| 8 | `B` | act 21 is sealed at `B` | **PASS** — rows `b8-olt-sealed` and `b8-olt-guard` |
| 9 | `B` | act 21's module is wired | **PASS** — row `b9-import` |
| 10 | `B` | this control plane is in the tree at its path | **PASS** — row `b10-self-present`, and the blob verified by `git hash-object` as the first act |

**No sibling lane's merge is a precondition of this round**, and none was waited for.

**The claim is scoped to the repository record.**

## 17. The axiom table — one line per named result

| named result | axioms |
| --- | --- |
| `relabel_prodComm` | `[propext, Classical.choice, Quot.sound]` |
| `gramPhaseEquiv_diag` | `[propext, Classical.choice, Quot.sound]` |
| `phiCTRL_l4n_restricts` | `[propext, Classical.choice, Quot.sound]` |
| `phiSwap_l5_restricts` | `[propext, Classical.choice, Quot.sound]` |
| `prefix_not_implies_l5` | `[propext, Classical.choice, Quot.sound]` |

No `sorry`, no `native_decide`, no added axiom; `lake build OIBridge.OrbitLawNaturalityFactorization`
completes with zero warnings.

## 18. The predictions, reported against their outcomes

| target | prediction | outcome | reported as |
| --- | --- | --- | --- |
| `OF0` | negative, high | `OF0`-silent | **as predicted** |
| `OF1` | `L4n-RESTRICTS` via `ΦCTRL`, high | `L4n-RESTRICTS` via `ΦCTRL` | **as predicted** |
| `OF2` (a) | positive, high | landed | **as predicted** |
| `OF2` (b) | positive, high | landed | **as predicted** |
| `L5` | `L5-RESTRICTS` via `Φ_swap`, high conditional on `OF2` | `L5-RESTRICTS` via `Φ_swap` | **as predicted** |
| `OF3` | consumed | consumed | — |
| `OF4` | positive, high conditional on `OF2` | `PREFIX-NOT-IMPLIES-L5` | **as predicted** |

## 19. The observation for the classification round, stated once and narrowly

If a later round freezes the classification act 21 named as the obstruction to `L-FAMILY`: a
full-ladder classification at the product configuration must **exclude** `Φ_swap`, which fails `L5`,
and a classification of the prefix through `L4n` at that configuration must **account for** it,
modulo the frozen law equivalence. **This product-configuration result places no inclusion requirement
on the separate single-carrier classification at `Γ ≡ ¼`, `|A| = 1`, and no requirement that any
parameter set contain any group.** It is an observation for that round and not a finding of this one.

## 20. The provenance as honoured

The rungs `L4n` and `L5`, and the prefix, were consumed as act 21's declarations at blob
`860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` and restated nowhere; the quotient list, the configuration,
the witness supply and the non-adoption clause are act 21's unchanged, the clause with "Act 22" in
its first sentence as the freeze directs; `ΦCTRL` and `ΦPP` are act 21's, consumed at merged
strength; `Φ_swap` is this freeze's, pinned by equation to
`fun _ G => RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4)) G` in every theorem that names it.
The freeze is not edited.

## 21. The discrepancies — recorded and not repaired

**Two items are recorded. None is repaired, and the frozen document is not edited.**

**DF1 — the module commit carried two first results.** The freeze's record 3 asks for "the named
result that entered first"; `relabel_prodComm` and `gramPhaseEquiv_diag` entered together at
`a2f0d98a…`, both non-verdict lemmas of the frozen route. Recorded as the two results that entered
first; the commit is not split.

**DF2 — the drafting check's fourth outcome was computed over a wider index family than the frozen
sentence states.** The freeze records the product cross product "at `i₀ = (0,m)`, `i₁ = (1,m)`, for
every `m`"; the check as run evaluated the phase-invariant product `P i j k · P i' k j` over every
`i = (0,i₂)`, `i' = (1,i₂')`, `j = (1,j₂)`, `k = (0,j₂)`, which contains the stated family at
`i₂ = i₂' = j₂ = m`, and found one value on each product tuple over the whole family. The frozen
sentence is true of the sub-family the kernel proof uses; the wider measurement is recorded here and
is evidence for nothing.

**No start-state discrepancy arose**, in any of the fifteen pinned blobs or in any of the ten
preconditions: **every one matches** and **all ten pass**. **No candidate discovered during execution
was executed.** **No configuration was chosen after an outcome was known.** **No alternative witness
was substituted for a named one.**

## 22. The provenance of this note

Every frozen sentence in this note — the `OF0`-silent sentence, the two `Li-RESTRICTS` carriages, the
`Φ`-SURVIVES-PREFIX and `Φ`-FAILS carriages, the `PREFIX-NOT-IMPLIES-L5` sentence, the `P0` sentence,
the ordering obligation, the anti-contamination invariant and the three carriages of THE CLAUSE — was
extracted by line range from the frozen preregistration blob `cc83ddb9…` at `B` and not retyped, and
the `R7-OLN` clause pins each by the same extraction.
