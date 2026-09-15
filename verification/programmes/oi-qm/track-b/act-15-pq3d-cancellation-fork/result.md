# Track B act 15 — the `PQ3` (d) cancellation fork: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`6428e0acab070ccfd2a84d13c6f55616526206ba`, merged into `main` as
`e4501bfff4e80533a5440c67d032f1ad401bdbe1` (PR #634) — the freeze's mandated execution base.

## The round's shape, restated

**This is a SEALING round** under `AGENTS.md` `§A.37`. It creates new seal and pin state and lands
**`E` → `L` → `P`, with `P` mandatory**. The seal constants it fills are `_TCF_BASE`, set by this
execution to the mandated base, and `_TCF_SEALED_HEAD` and `_TCF_MERGE`, which are **present and
unset at execution** and are set by the pin commit `P` after the landing merge `L`. **No existing
seal constant is altered**: `_CTI_BASE`, `_CTI_SEALED_HEAD`, `_CTI_MERGE`, `_PQT_BASE`,
`_PQT_SEALED_HEAD` and `_PQT_MERGE` are read and never written, and the execution's diff against
`verification/lean/edge_rigidity_probe.py` **adds** the `R7-TCF` clause and changes nothing else in
the file.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `e4501bfff4e80533a5440c67d032f1ad401bdbe1` (merge of PR #634) |
| This round's frozen control plane | `preregistration.md`, blob `6428e0acab070ccfd2a84d13c6f55616526206ba` |
| `AGENTS.md` (`§A.37`, the round lifecycle) | blob `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| Act 14's control plane | `../act-14-threading-observability/preregistration.md`, blob `1b16008470bb1e2456c57aad58421a5941a55e0c` |
| Act 14's result (`PQ0`–`PQ4`, the fork left UNDECIDED) | `../act-14-threading-observability/result.md`, blob `d4815d56b1cea2ed42540a7d6262c3c4201ac9b7` |
| Act 13's control plane | `../act-13-cross-time-invariants/preregistration.md`, blob `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1` |
| Act 13's result (`CT1`–`CT4`, `CL1`) | `../act-13-cross-time-invariants/result.md`, blob `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| Act 12's result (`LG1`, `RO1`, `TG2`, `TG3`, `SH1`) | `../act-12-two-sided-gauge/result.md`, blob `467d8be147b6ebd91f2eed12404566af74ac779f` |
| Act 11's result (`GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`) | `../act-11-coherent-lift-gauge/result.md`, blob `7b24353ad626de6f930e41242334cb09945ae303` |
| Act 7's governing preregistration (`D3`, `D4b`, the readback amendment) | `../act-07-dilation-choice/preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| Substratum Lemma 24.1b control plane (named, consumed by nothing) | `../../../substratum/lemma-24-1b-framework-data/preregistration.md`, blob `f614b666ad9098f866969c4c524e47f504e5d71c` |
| Act 14's module | `verification/lean-mathlib/OIBridge/ThreadingObservability.lean`, blob `91508205b33d9419fbffec5ad44035fad35de5f1` |
| Act 13's module | `verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean`, blob `47eb21e22845f0319926227c80d0d7f2f033880b` |
| Act 12's module | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| Act 11's module | `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`, blob `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| Act 7 layer 2's module | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 10's module (`one_admissible_at_every_anchor`) | `verification/lean-mathlib/OIBridge/AnchorRobustness.lean`, blob `b74202bc160918b32ca1b333da532a141ea8015d` |
| The live queue, `P0` row as act 14 left it | `verification/ROADMAP.md`, blob `4f9af3d3e8a2d5d66ff063c94a388d2c7c04f218` |
| The chronology guard | `verification/lean/edge_rigidity_probe.py`, blob `dc30d365a06cb3a118d3bdb100c18b9b8c0d799e` |
| The module index | `verification/lean-mathlib/OIBridge.lean`, blob `179d57a9245b117f0db76fc9dec5362dc7a8fe2b` |
| This round's module | `verification/lean-mathlib/OIBridge/CancellationFork.lean` (created here) |

**Every blob the freeze pins is present at the mandated base with the SHA the freeze records —
all eighteen, the fourteen read-only rows and the three rows for files this round writes onto, plus
`AGENTS.md`. No start-state discrepancy.** The verification was this round's first act, before any
target was executed, and the preregistration blob was confirmed by
`git cat-file -p B:…/preregistration.md | git hash-object --stdin` against the SHA the `R7-TCF`
clause pins.

**The anti-contamination invariant is honoured.** Sibling rounds merged into `main` between this
freeze and its base are present at `B` and are **not** inputs: this round consumed only what the
freeze's start-state table names. One sibling artifact was read and is recorded here for
completeness: the `R7-PC4S` guard clause of the concurrent physical-realization round was read **as
a structural template for the shape of a sealing round's guard clause**, on the owner's direction,
and **no result, label, number or finding of that round is consumed, cited or compared**. No target
of this round rests on it, and nothing about that round is asserted here.

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Outcome, in one line

**`CF0` is settled negative — the record is silent — and `CF1`, `CF2`, `CF3` (a) and (b), `CF4` (a)
and (b) and `CF5` all landed at evidence level 2. `CF5` reached LINE 1 of its four-outcome
hierarchy: `PQ3-d⁺`, an exhibited cancelling triple.** This is the freeze's **Case B**.

**The freeze's central prediction did not hold, and that is reported as what it is.** The freeze
rated a second UNDECIDED the single most likely outcome, at **medium** strength, and rated line 1 —
`PQ3-d⁺` — **not predicted**, at **low**. The round reached line 1. The reversal is recorded here
in terms: **the preregistered `CF5` prediction of UNDECIDED is falsified by this round's own
exhibition**, the freeze is left exactly as written, and the outcome is earned by a triple with all
three conjuncts proved in the kernel and never by a search.

**The answer is relative to `𝒪₂`, under act 7's readback convention with `D4b` negative, and it
travels to no other carrier.** No carrier is adopted as the physical one, `P0` stays **OPEN** and
two-part, and nothing here names, endorses or excludes a selection principle.

## Predictions against outcomes

| target | preregistered sign | strength | landed | against prediction |
| --- | --- | --- | --- | --- |
| `CF0` | negative — the record is silent | high | **negative, silent** | as predicted |
| `CF1` | positive | high | **positive**, level 2 | as predicted |
| `CF2` | positive | high | **positive**, level 2 | as predicted |
| `CF3` (a) | positive | high | **positive**, level 2 | as predicted |
| `CF3` (b) | positive | medium | **positive**, level 2 | as predicted; the frozen UNDECIDED allowance for (b) was **not** used |
| `CF4` (a) | positive | high | **positive**, level 2 | as predicted |
| `CF4` (b) | positive | high | **positive**, level 2 | as predicted |
| `CF5` | **UNDECIDED** | medium | **line 1, `PQ3-d⁺`**, level 2 | **REVERSED** — the predicted outcome did not occur |
| `CF5` → line 1 | not predicted | low | **reached** | landed **above** its rating |
| `CF5` → line 2 (`S`) | not predicted | low | not reached, and **not claimed** | — |
| `CF5` → line 3 (`N`) | not predicted | low | not reached, and **not claimed** | — |

**Lines 2 and 3 were not reached and are not claimed.** Neither `S` nor `N` is proved by this round;
both are **refuted** by it, which is a different thing and is recorded as such below.

## `CF0` — is the universal ingredient in the merged record? NO: the record is SILENT

**Evidence type: prose and record audit, type P.** `CF0` carries **no evidence level**, no Lean was
written for it, and it is **not** part of the axiom table. It is settled by the freeze's own evidence
rule — a verbatim quotation with a coordinate, or the recorded statement that the passage sought does
not exist on the named and bounded search — and by nothing else.

### The search, as the freeze bounds it, executed and recorded in full

**The file set**, enumerated at the mandated base `e4501bf`: **215 files** — 171 `*.lean` files under
`verification/lean-mathlib/` and `verification/lean/`, 43 `preregistration.md` and `result.md` files
under `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`. The set was taken from
`git ls-tree -r --name-only e4501bf`, so the un-tracked `.lake` package tree is outside it by
construction.

**The question asked of each hit**, in the freeze's words: does this declaration state, for **every**
lift, **every** `W ∈ 𝒢_L` and **every** strong family, a conclusion about `readback a₀` of the
modulus square of `W (U_t K_t K_sᴴ U_sᴴ) Wᴴ` — or a statement from which such a conclusion follows by
consuming merged results alone, with the consumption exhibited?

**The result recorded for each frozen term:**

| term | hits | files | bearing declarations | recorded answer |
| --- | --- | --- | --- | --- |
| `ThreadingRelated` | 17 | 4 | 4 | **does not supply it.** All four are act 14's `PQ1` (b), `PQ1` (c), `PQ2` (c) and `PQ3` (c) — **existential** exhibitions on one lift each, not universal statements |
| `LeftFibreGroup` | 63 | 10 | 7 | **does not supply it.** The two universal ones are act 14's `pq1a_constant_left_redundant_visible` and `pq3a_pair_redundant_visible`, whose conclusion is about `readback a₀ (‖(W U_t K_t) p q‖²)` — the **per-time lift**, one level below the relative object. The other five are existential exhibitions (`ct4`, `cl1`, `pq1b`, `pq1c`, `pq3c`) |
| `readback` | 466 | 42 | 28 | **does not supply it.** The 28 declarations whose statement mentions `readback` are adjudicated one by one below; none concerns a `𝒢_L` conjugation of a general relative object |
| `RelativeCandidate` | 2 | 1 | 0 | **not relevant to the question.** Both hits are in this round's own freeze, naming the conditional budget slot act 14 left unused. No merged declaration carries the name |
| `CrossGram` | 149 | 7 | 3 | **does not supply it.** `ct3a`, `ct3c` and `ct4` are existential exhibitions about the cross-Gram's separating power, not universal statements about a conjugated readback |
| `conj` | 4009 | 151 | 0 | **does not supply it.** 268 declarations carry the token in their name; the overwhelming majority are `conjTranspose`, `conjChannel` and `starRingEnd` mechanics in other programmes. The one in this fork's vocabulary is act 13's `ct2a_relative_conj`, which states the **matrix** identity `U'_t U'_sᴴ = W (U_t U_sᴴ) Wᴴ` and stops there — its statement contains no `readback` |
| `cancel` | 397 | 90 | 0 | **does not supply it.** 14 declarations carry the token in their name, 11 of them ring-cancellation lemmas in other files. The one in this fork's vocabulary is act 14's `pq3b_no_cancellation_on_anchoredChannel`, a statement about the **anchored-channel carrier `𝒪₁`**, which act 14's own status rule 5 says travels to no other carrier |
| `GL2` | 162 | 14 | 2 | **does not supply it.** `gl2_strong_gauge_moves_relative_candidate` and `ct3a` are **existential** on one exhibited lift |
| `GL3` | 68 | 14 | 0 | **does not supply it.** `gl3_constant_gauge_preserves_relative` is universal but about a **constant right factor**, and its conclusion is an identity of matrices with no `𝒢_L` and no readback in it |
| `CT2` | 74 | 10 | 0 | **does not supply it.** `ct2a_relative_conj` gives the conjugation **identity**; `ct2a_crossGram_iff_constLeft` and `ct2b_fibreCrossGram_iff` are about which datum determines the lift, not about a readback |
| `CT3` | 127 | 10 | 2 | **does not supply it.** `ct3a` and `ct3c` are existential; `ct3g_fibreCrossGram_strong_right` is universal but about the fibre cross-Gram, not a readback |
| `CT4` | 94 | 8 | 1 | **does not supply it.** `ct4_constant_left_obstruction` is an **existential** exhibition on one lift over `Fin 2 × Fin 2` |
| `CL1` | 65 | 8 | 1 | **does not supply it.** `cl1_constant_left_moves_relative_candidate` is **existential**: it says a constant left move **can** change the relative candidate, and says nothing about every constant left move |
| `PQ3` | 120 | 5 | 2 | **does not supply it.** `pq3a_pair_redundant_visible` is universal but concludes about the **per-time** lift's readback; `pq3c_pair_physical_relative_candidate` is an existential exhibition |

**The twenty-eight `readback`-bearing declarations, adjudicated.** Four are definitions or bridges
(`readback`, `Readback`, `readback_of_admissible`, `pq0a_readback_is_diagonal_action`) — *not
relevant to the question*. Four are act 7's structural controls on the readback
(`readback_isColStochastic`, `readback_relabel`, `readback_permMatrix_apply`,
`rb3_forced_on_modulusSquared_unitary`) and one is `rb3_is_anchorwise` — each *does not supply it*,
and `readback_relabel` (`R-3`) in particular is a statement about relabelling the ancilla **type**
along a bijection carrying the anchor, which is not a `𝒢_L` conjugation and which the freeze's
hazard 18 names by name. Three are act 10's anchor-invariance witnesses (`ab2_iff_…`,
`not_ab2_witnessA`, `not_ab2_witnessB`) — *not relevant*. Three belong to other programmes
(`causal_readback_verdict`, `core_history_readback`, `core_pIndivisible_two`) — *not relevant*.
Two are the universal per-time statements `pq1a_constant_left_redundant_visible` and
`pq3a_pair_redundant_visible` — *does not supply it*, quoted and diagnosed below. The remaining
eleven are **existential** exhibitions on one lift each (`gl2_…`, `ct3a`, `ct3c`, `ct4`, `cl1`,
`pq1b`, `pq1c`, `pq2a`, `pq2c`, `pq3c`, `rb3_of_admissible`) — *does not supply it*, each being an
existence statement where a universal is required.

**The nearest miss, quoted verbatim with its coordinate**, from
`verification/lean-mathlib/OIBridge/ThreadingObservability.lean`, `pq3a_pair_redundant_visible`:

> `CoherentLift a₀ Γ (fun t => W * U t * K t) ∧ ∀ t, readback a₀ (Matrix.of fun p q => ‖(W * U t * K t) p q‖ ^ 2) = readback a₀ (Matrix.of fun p q => ‖U t p q‖ ^ 2)`

**This is universal over exactly the triples this round is about** — every coherent lift, every
`W ∈ 𝒢_L`, every strong family — and its conclusion is about the readback of the **per-time lift**
`W U_t K_t`, not about the readback of the **relative object** `W (U_t K_t K_sᴴ U_sᴴ) Wᴴ`. The
relative object carries `Wᴴ` on the input side, which is exactly what the per-time statement never
has to face. **That is the gap, and nothing in the merged record closes it.**

### The finding, in the freeze's frozen wording — outcome `CF0`-silent

> On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
> `verification/lean/`, every `preregistration.md` and `result.md` under
> `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
> the merged record contains no universal theorem, quantified over the threading equivalence,
> about how a constant `𝒢_L` conjugation acts on the anchored readback of a general relative
> object. **The finding is that the record is silent on the point.** It is not a finding that such
> a theorem is false, not a finding that it is unprovable, and not a bound on what a later round
> could prove. Act 14's recording of the same absence is confirmed on this round's own search and
> is not enlarged.

**Reconstructive inference is forbidden as a finding, and none is offered.** No step of this section
has the form "the record must contain X, because otherwise Y would not have been written". **Where
the record is silent, the finding is that it is silent** — not that the thing sought is false, and
not that it is true. In particular, `CF5`'s positive outcome below **is not retro-evidence about
`CF0`**: that no such universal theorem is in the record is a fact about the record at this base,
and the fact that one branch of the fork is now refuted is a separate fact about `𝒪₂`.

## `CF1` — the cancellation equation in normal form: POSITIVE

`cf1_composite_normal_form`, universally quantified, at evidence level 2. Outcome `CF1`-positive, in
the freeze's frozen wording:

> The composite's relative object is the constant left element's conjugation of
> `U_t K_t K_sᴴ U_sᴴ`, universally, at evidence level 2. This is an identity of matrices; it says
> nothing about the value of any readback and nothing about the fork.

Act 13's merged `ct2a_relative_conj` is the `K ≡ 1` case and is **consumed there, not re-proved
here**. The kernel statement carries the freeze's hypotheses — `LeftFibreGroup W` and
`StrongAnchorStabilizer a₀ (K t)` — and the module's docstring records in terms that **neither is
load-bearing**: the proof is associativity together with the conjugate transpose of a product, so the
identity holds for arbitrary matrices. That is recorded so that no reader takes the identity to
depend on the hypotheses, and it is entered in the discrepancies section below.

## `CF2` — time-dependence of the strong family is necessary: POSITIVE

`cf2_constant_strong_family_redundant`, at evidence level 2, stated as two conjuncts: the third
conjunct holds whenever `K` is constant in time, and hence no such triple is cancelling. Outcome
`CF2`-positive, in the freeze's frozen wording:

> No cancelling triple has a strong family constant in time, at evidence level 2, through act 11's
> merged `GL3` consumed as the universal statement it is. **This is a necessary condition on a
> hypothetical witness and is not evidence that one exists.** `GL3` is not extended and no
> converse is claimed: time-dependence is necessary for the strong part to move the relative
> candidate, and is not shown sufficient.

**The exhibited witness of `CF5` satisfies this condition and is not evidence for it**: `CF2` is a
universal statement and the witness is one triple. The witness's strong family is checked
time-dependent as a separate conjunct of `cf5_cancelling_triple_exists`, which is a fact about that
triple and not a converse to `GL3`.

## `CF3` — the cardinality scoping: BOTH CONJUNCTS

`cf3_cardinality_scoping`, at evidence level 2, the two conjuncts of one theorem. The frozen
medium-strength allowance for reporting `CF3` (b) UNDECIDED was **available and was not used**: the
column-stochasticity route cost one lemma, `relativeCandidate_eq_one_of_visible_subsingleton`, which
consumes act 11's merged `visible_marginal_eq_one_of_visible_subsingleton` applied to the relative
object, admissible for its own readback by act 7's definition of admissibility. Outcome `CF3`-both,
in the freeze's frozen wording:

> No cancelling triple exists with a single ancilla configuration or with a single visible
> outcome, at evidence level 2: `|A| ≥ 2` and `|V| ≥ 2` are necessary, each as a conjunct of one
> theorem. **These bound where a witness could live and are not evidence that one exists.**

**The exhibited witness lives at `|V| = 2`, `|A| = 3`, inside the region `CF3` leaves open.** That is
a consequence of `CF3` about the witness, not evidence that `CF3` implies a witness exists, and the
freeze's hazard 15 is honoured: `CF3` bounds where one could live and nothing more.

## `CF4` — the two non-triviality conjuncts: BOTH

`cf4_nontriviality_conjuncts`, at evidence level 2, the two conjuncts of one theorem. Outcome
`CF4`-both, in the freeze's frozen wording:

> In any cancelling triple the strong family moves the relative object itself at some time pair,
> and the constant left element moves the anchored readback of some relative object, so `W ≠ 1`;
> both at evidence level 2. Act 11's `GL2` and act 13's `CT4` with `CL1` are the merged
> existential statements that each is possible on one exhibited lift; **neither is enlarged, and
> neither of these necessary conditions is evidence that a cancelling triple exists.**

`CF4` (b) runs through act 13's merged `ct2a_relative_conj`, which rewrites the left part's relative
object as the conjugation; the rest is the contrapositive of an equality of matrices.

## `CF5` — THE FORK: LINE 1, `PQ3-d⁺`

`cf5_cancelling_triple_exists`, at evidence level 2. **The highest line of the four-outcome hierarchy
the kernel actually carries is line 1**, and it is reported at that line and no other.

### The triple

On `V = Fin 2`, `A = Fin 3`, anchor `a₀ = 0`, with two effective times. Nothing below is a top-level
definition; each object is a bound variable pinned by an equation in the statement that needs it.

| object | value | why it is admissible |
| --- | --- | --- |
| `W` | `P(swap((0,0),(0,1)))` | `LeftFibreGroup W`: its support lies inside the visible fibre `0`, so it is unitary and vanishes off the visible diagonal. `W ≠ 1` is a conjunct, certified at the entry `((0,0),(0,0))` |
| `U_0` | `𝟙` | admissible for its own readback at the anchor |
| `U_t`, `t ≠ 0` | `P(swap((0,0),(1,1)))` | admissible for its own readback at the anchor, so `U` is a coherent lift of the frozen visible family `Γ_t = readback a₀ (‖U_t‖²)` |
| `K_0` | `𝟙` | strong |
| `K_t`, `t ≠ 0` | `P(swap((0,1),(1,2)) · swap((0,2),(1,1)))` | `StrongAnchorStabilizer a₀ (K t)`: its support misses both anchored columns `(0,0)` and `(1,0)`, so it fixes every anchored column pointwise. `K` is time-dependent, certified as a conjunct |

The composite `U'_t = W U_t K_t` is a coherent lift of the **same** visible family — act 12's merged
`left_preserves_admissible` on top of act 7's merged `admissible_mul_of_fixes_anchor` — and is
`≈_T`-related to `U`, both conjuncts of the theorem.

### The three conjuncts

**`C` holds at EVERY time pair.** At `(0,0)` and at equal nonzero times both relative objects are
`𝟙`. At `(1,0)` and `(0,1)` the conjugation by `W` undoes in the anchored readback exactly what the
strong threading does: the anchored columns land in the visible fibre `1` on both sides, at both
visible indices. This is proved as `∀ t s`, not at sampled pairs, by reducing each relative object to
a single permutation matrix and reading its anchored column off act 7's merged
`readback_permMatrix_apply`.

**`¬L` is certified at the time pair `(1,0)` and the entry `(0,0)`:** `𝒪₂(W U_·)(1,0)_{0,0} = 1`
while `𝒪₂(U)(1,0)_{0,0} = 0`. `W` carries the anchored basis vector of fibre `0` to `(0,1)`, which
`U_1` leaves inside fibre `0`, while `U_1` carries the anchored basis vector itself into fibre `1`.

**`¬R` is certified at the time pair `(0,1)` and the entry `(0,0)`:** `𝒪₂(U_· K_·)(0,1)_{0,0} = 1`
while `𝒪₂(U)(0,1)_{0,0} = 0`. Both entry values are proved, and the two inequalities are then
separate conjuncts derived from them.

**The two halves do different work at different time pairs, and that is the content of the
cancellation.** `¬L` is visible at `(1,0)` and `¬R` at `(0,1)`; at every pair the composite agrees
with `U`. Neither half is redundant on its own, and the composite is.

### The outcome, in the freeze's frozen wording — outcome line 1, `PQ3-d⁺`

> A cancelling triple is exhibited: relative to the relative-candidate carrier, and under act 7's
> readback convention with `D4b` negative, the pair of a constant in-fibre left move and a
> time-dependent strong right gauge can be redundancy while neither part is. The triple's three
> conjuncts are proved in the kernel at evidence level 2, with the lift's coherence discharged
> from merged results and the two inequalities certified at named time pairs and named entries.
> **This is a statement about `𝒪₂` and travels to no other carrier**; act 14's `PQ3` (b) settles
> the analogous question negatively on `𝒪₁` and the two do not conflict, `𝒪₁` and `𝒪₂` being computed
> from different operations on the lift with no implication proved between them in either
> direction. **No carrier is adopted as the physical one**, `P0` stays OPEN and two-part, and
> nothing here names, endorses or excludes a selection principle.

## The seam: `N`, `S`, and what line 1 does to act 14's `PQ3-d⁻` row

**`N`** — no cancelling triple exists: for every triple, `C → (L ∨ R)`. This is the exact negation of
`PQ3-d⁺` and is the reading act 14's row carries before the dash and its propagation sentence
carries throughout.

**`S`** — for every triple, `C → (L ∧ R)`. This is the reading act 14's row carries after the dash,
taken pointwise over triples.

**`S` implies `N`, by propositional logic alone.** **`N` does not imply `S`**: as schemas,
`C → (L ∨ R)` does not entail `C → (L ∧ R)`. So `S` is strictly the stronger, and the two are kept
apart at every use in this round.

**What this round establishes is `¬N`, and `¬S` follows from it.** The exhibited triple has `C` and
neither `L` nor `R`, so `N` is false on the relative-candidate carrier —
`cf5_not_no_cancelling_on_relativeCandidate` states exactly that and is proved from the exhibition in
three lines. Since `S` implies `N`, `¬N` gives `¬S`. **That direction is reported as following, not
as separately proved**, and it is the weaker of the two directions the kernel could have been asked
for: what is proved is that `N` is false, and `¬S` is its immediate consequence.

**Act 14's row stands exactly as act 14 wrote it.** This round does not repair, correct, reinterpret,
normalize or supersede it, and no sentence here says what act 14 "meant". The fact that its row
carries two readings while its propagation sentence carries only the weaker is entered in the
discrepancies section below **and nowhere else**.

## What these outcomes do NOT license

1. **The fork is not reported unresolvable, undecidable or hard.** It is resolved, at line 1, by an
   exhibited triple.
2. **Nothing here is a finding against act 14's settled results.** `PQ0`, `PQ1` (a)–(d), `PQ2`,
   `PQ3` (a)–(c) and `PQ4` stand exactly as act 14 states them, and none is revised. `PQ3` (d) was
   recorded UNDECIDED by act 14 with its obstruction named, and answering it is not a correction of
   anything act 14 settled.
3. **"No cancelling triple exists" is not asserted, on any strength.** It is **refuted**. `CF2`,
   `CF3` and `CF4` remain what the freeze says they are — necessary conditions on a witness — and
   their conjunction is not a further, stronger sentence.
4. **No search is presented as evidence.** The exhibition is a proved triple; the exploratory search
   that located it is provenance and not evidence, and no target rests on it.
5. **No sentence of `S`'s form is asserted, and no sentence of `N`'s form is asserted.** Both are
   refuted, not proved. Act 14's `PQ3-d⁻` label is never used bare in this round: every use names
   `N` or `S` alongside it.
6. **Act 14's `PQ3-d⁻` row is not corrected, repaired, reinterpreted, normalized or superseded.** The
   two readings are **recorded** as a discrepancy and act 14's merged text stands as written. No
   artifact of this round edits act 14.
7. **The record's silence at `CF0` shows nothing about the truth of the theorem sought.** Silence is
   not a truth value, and `CF5`'s outcome is not retro-evidence about what the record contains.
8. **No outcome of this round is carried to act 13's `CT3` (d), and no ingredient of `CT3` (d) is
   carried here.**

   > **THE CLAUSE, carried at this mention — the list of what no outcome of this round licenses.**
   > `CT3` (d) is act 13's fork and `PQ3` (d) is act 14's. `CT3` (d) asks whether the full column
   > cross-Gram separates every strong-right threading — a question about one datum's separating
   > power. `PQ3` (d) asks whether a constant in-fibre left move and a time-dependent strong right
   > gauge can cancel on the relative-candidate carrier — a question about cancellation between two
   > parts of one relation. **Neither instantiates, constrains, nor supplies evidence for the other,
   > and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever
   > this round returns, and no outcome of this round moves it in either direction.

9. **No carrier-free verdict is written.** Act 14's status rule 3 binds this round too: the threading
   freedom is neither called gauge nor called physical without naming a carrier.
10. **No carrier is adopted as the physical one, and none is asserted not to be.**
11. **`P0` is not closed, and neither of its two parts is.**
12. **No selection principle, connection or gauge fixing is named, endorsed, excluded, asserted or
    denied**, in either direction.
13. **Nothing here says OI and QM are inequivalent.** Two lifts differing is not two theories
    differing, and the established finite observable-law correspondence is untouched. Every `𝒪₂`
    statement is a statement under act 7's own readback convention, with `D4b` negative.
14. **No verdict is transferred between carriers.** `PQ3` (b) settles the composite-versus-left
    question on `𝒪₁`; that is not evidence for or against anything on `𝒪₂`, and this round's answer
    on `𝒪₂` is not evidence for or against anything on `𝒪₁`.
15. **Nothing is said about Track I, or about Source B or Source C**, on any axis.
16. **Nothing is imported from the substratum Lemma 24.1 rounds.** A shared word is not a bridge.

## The status rule, as honoured

Each target is reported with the sentence the freeze fixed for the outcome reached, quoted verbatim
above and nowhere paraphrased: `CF0`-silent, `CF1`-positive, `CF2`-positive, `CF3`-both, `CF4`-both,
and `CF5` line 1. **No outcome chose its own wording**, and no sentence was invented where the freeze
supplies one.

**`CF5` is reported at the highest line the kernel actually carries, and never a higher one.** Line 1
is earned by an exhibited triple with all three conjuncts proved at evidence level 2, the lift's
coherence discharged from merged results, and the two inequalities certified at named time pairs and
named entries — which is exactly what the hierarchy's line 1 requires. Lines 2 and 3 are **not**
reported: neither `S` nor `N` is proved here, and the freeze's specific defect — reporting a settling
outcome at a strength the kernel does not carry — is guarded against in the other direction too, by
reporting `¬S` as following from `¬N` rather than as separately established.

## The relation to acts 11, 12, 13 and 14 — every merged label consumed, none revised

`GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `CT1`, `CT2`, `CT3`, `CT4`,
`CL1`, `PQ0`, `PQ1`, `PQ2`, `PQ3` (a)–(c) and `PQ4` are consumed at their own strengths and **none is
revised**. Specifically:

- **`GL3` is consumed as the universal statement it is**, and no converse is added. `CF2` says
  time-dependence is necessary; act 11's own note refuses "every time-dependent gauge moves every
  relative candidate" in terms, and this round does not write it.
- **`GL2`, `CT4` and `CL1` are consumed at their own existential strengths.** None is cited as though
  it quantified over lifts, which is exactly the gap `N` and `S` would each have needed filled.
- **`ct2a_relative_conj` is consumed for the `K ≡ 1` conjugation identity** and is not re-proved.
- **Act 14's `PQ3` (b) is untouched** and is not carried from `𝒪₁` to `𝒪₂` in either direction.
- **Act 7's `D4b` is negative and the readback is the repository's own convention**, carried at every
  `𝒪₂` use in this round rather than once in a footnote.
- **Act 13's `CT3` (d) stands UNDECIDED and is untouched.**

  > **THE CLAUSE, carried at this mention — the relation to acts 11, 12, 13 and 14.**
  > `CT3` (d) is act 13's fork and `PQ3` (d) is act 14's. `CT3` (d) asks whether the full column
  > cross-Gram separates every strong-right threading — a question about one datum's separating
  > power. `PQ3` (d) asks whether a constant in-fibre left move and a time-dependent strong right
  > gauge can cancel on the relative-candidate carrier — a question about cancellation between two
  > parts of one relation. **Neither instantiates, constrains, nor supplies evidence for the other,
  > and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever
  > this round returns, and no outcome of this round moves it in either direction.

**One resemblance is recorded so that it is not mistaken for a bridge**, exactly as the freeze
records it: both forks have a branch whose ingredient is "a universal theorem about a conjugation
that does not move an anchored readback". The two theorems quantify over different things, and
neither would establish the other. Recording the resemblance is not transferring it, and no target of
this round is stated over act 13's objects.

## The frozen post-round sentence for the `P0` row — Case B, the row's label unchanged

The `P0` row stays **OPEN** and two-part. The sentence appended to `verification/ROADMAP.md` is the
freeze's Case B, produced by the substitutions Case B names and carried verbatim:

> `P0` remains open and two-part, and act 14's answer relative to each frozen carrier of observables
> stands exactly as act 14 states it. The cancellation fork `PQ3` (d) — whether a constant in-fibre
> left move and a time-dependent strong right gauge can cancel on the relative-candidate carrier, so
> that the pair is redundancy relative to that carrier while neither part is — is answered
> `PQ3-d⁺`: relative to the relative-candidate carrier, under act 7's readback convention with `D4b`
> negative, the two parts can cancel, so the pair can be redundancy relative to that carrier while
> neither part is. What this round adds is the
> shape of any resolution and not a resolution: the composite's relative object is the constant left
> element's conjugation of `U_t K_t K_sᴴ U_sᴴ`; a cancelling triple's strong family cannot be
> constant in time; none exists with a single ancilla configuration or with a single visible
> outcome; and in any such triple the strong family moves the relative object itself while the
> constant left element moves the anchored readback of some relative object, so the constant left
> element is not the identity. Act 13's `CT3` (d)
> stays UNDECIDED and is untouched; neither fork answers the other. **No carrier is adopted as the
> physical one**, `P0`'s other part — what selects or constrains the Gram/orbit trajectory across
> time — is untouched, and nothing here names, endorses or excludes a selection principle.

**No case closes `P0`**, and this case reports neither of its two parts closed.

## Discrepancies

**Five items are recorded. None is repaired, and the freeze is not edited.** The preregistration is
immutable once merged; each item below is recorded here and nowhere else in the round's artifacts
except where a reader would otherwise be misled.

1. **Act 14's `PQ3-d⁻` row carries two non-equivalent readings, and its propagation sentence carries
   only the weaker.** The row, at `act-14-threading-observability/preregistration.md` line 417, reads
   "no such triple exists — relative to `𝒪₂` the pair is redundancy only when both parts are"; the
   clause before the dash is `N` and the clause after it is `S`, and `S` is strictly the stronger.
   The same file's propagation wording, at lines 563–566, carries only "the two parts cannot cancel",
   which is `N`. **This is recorded as a discrepancy of this round's reading against act 14's label.
   It is not repaired, not corrected, not reinterpreted and not normalized.** Act 14's merged text
   stands exactly as act 14 wrote it. No target of this round is carried by the discrepancy, and no
   prediction changed sign or strength because of it. What this round did instead is refuse the
   undifferentiated label: `N` and `S` are named individually at every use, and the outcome is
   reported as `¬N`, with `¬S` following.

2. **The freeze's Case B retains a clause that reads against the outcome reached.** Case B is
   composed from Case A by naming the clauses that change — the replaced clause, the search clause,
   and the sentence beginning "A second UNDECIDED" — and it says every other clause stands. One of
   the clauses it retains is "What this round adds is the shape of any resolution and not a
   resolution", which belongs to the UNDECIDED case. **This round did reach a resolution**, so that
   clause reads against its own outcome. **It is carried verbatim as the freeze's own frozen wording
   and is recorded here rather than edited**, and the `ROADMAP` records the same point in its own
   prose immediately after the block quote so that no reader of the queue is misled. What the round
   adds is the resolution **together with** the four items the clause lists.

3. **`CF1`'s frozen hypotheses are not load-bearing.** The freeze states `CF1` for every `W` with
   `LeftFibreGroup W` and every strong family `K`, and says it is proved "from the unitarity of `W`
   … and nothing else". The kernel proof uses **neither**: the identity is associativity together
   with the conjugate transpose of a product, and holds for arbitrary matrices. The statement carries
   the freeze's hypotheses so that the theorem is the one the freeze names, and the module's
   docstring records in terms that they are not used, so that no reader takes the identity to depend
   on them. **Nothing is claimed beyond the frozen statement.**

4. **The `ROADMAP` append is a full section in acts 11–14's established shape.** The freeze's written
   -files table says `verification/ROADMAP.md` is "written only by appending the frozen post-round
   sentence for the case reached; the row's label unchanged". The execution appends a section
   carrying the frozen Case B sentence **verbatim** in a block quote, together with the per-target
   summary, the not-licensed paragraph and the two document links, and appends one clause to the `P0`
   row cell — the shape acts 11, 12, 13 and 14 each used. **The row's label is unchanged (`OPEN`),
   nothing in the `ROADMAP` is rewritten, and the frozen sentence is carried without alteration.**

5. **One sibling artifact was read for structure only.** The `R7-PC4S` guard clause of the concurrent
   physical-realization round, which is not merged at this base, was read on the owner's direction as
   a worked example of a sealing round's guard clause in strong-ancestry-versus-archive mode. **No
   result, label, number, prediction or finding of that round is consumed, cited or compared**, no
   target of this round rests on it, and nothing about that round is asserted here. This is recorded
   because the freeze's anti-contamination invariant governs what a round consumes, and the honest
   record is that a structural template was read while no research content was.

**No other discrepancy.** Every blob the freeze pins is present at the mandated base with the SHA the
freeze records. The definition budget was not exceeded. No hazard's named failure occurred.

## The chronology control

**`R7-TCF` certifies the strong property**, reusing act 10's mechanism by name through acts 12's,
13's and 14's copies, with the archive-mode scaffolding of PR #599 carried and its pins **unset at
execution**:

- the preregistration blob is pinned **by content** to `6428e0acab070ccfd2a84d13c6f55616526206ba`,
  with a drift control that fails the guard if one byte is appended to it;
- the real execution head `H` is resolved from `pull_request.head.sha` in a pull-request run —
  **never** the synthetic merge commit — failing closed with no fallback;
- `_TCF_BASE = 'e4501bfff4e80533a5440c67d032f1ad401bdbe1'` must be an ancestor of `H`; **and**
- **every commit in `git rev-list H ^B` must be a descendant of `B`**, which excludes pre-freeze side
  history rather than merely certifying the final head;
- history recovery is performed by the guard itself for `B`, for `H` **and for every enumerated
  commit**, and a failed recovery **fails** the check rather than skipping it;
- **`_TCF_SEALED_HEAD` and `_TCF_MERGE` are unset at execution.** They are set in the pin commit `P`
  after the landing merge `L`, because pinning them in the execution would make the execution's own
  head depend on where it landed. That is a statement about this execution and stays true as one.
  With them set, the guard runs in **archive mode**: the same strong check re-run against the sealed
  head, the pinned merge required to carry it as its second parent, and both required reachable from
  the current target, fail-closed.

**Act 13's and act 14's seals are untouched.** `_CTI_BASE`, `_CTI_SEALED_HEAD`, `_CTI_MERGE`,
`_PQT_BASE`, `_PQT_SEALED_HEAD` and `_PQT_MERGE` carry exactly the values those rounds set, and the
guard checks them equal to those values with mutation controls, since an archive seal belongs to the
round that set it.

**The preconditions checked at `B`**, with the freeze's own commands:

| # | precondition | checked |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | `git rev-list --parents -n 1 B` shows two parents, `0ef0741` and `3fab917`; the preregistration blob hashes to `6428e0acab070ccfd2a84d13c6f55616526206ba` |
| 2 | Act 14's execution is merged **and sealed** | `_PQT_SEALED_HEAD = '5008a47bf7e67edc502120f9269c4a4661ef7342'` and `_PQT_MERGE = 'c50dd22457bfd4812761cb56e7ca1a559af33c5e'`, both non-`None` at `B` |
| 3 | Act 14's module and result are in the tree | both `git cat-file -e` checks succeed at `B` |
| 4 | Act 13's execution is merged **and sealed** | `_CTI_SEALED_HEAD = '9ea94f9ca52f12e8cd4215be7e039d1f86d81fc7'` and `_CTI_MERGE = '292848b3c908d33ac432a5360effe0c259e3ce16'`, both non-`None` at `B` |
| 5 | No act 15 execution object precedes the freeze | the only path under this round's directory at `B` is `preregistration.md`, and `OIBridge/CancellationFork.lean` does not exist at `B` |

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** **The claim is scoped to the repository record.** **Before certification this
execution absorbed no later `main`**: no merge from `main`, no rebase, no amend, no force-push, and
the head carries exactly one parent, the mandated base.

## Definition budget: **ONE of the frozen two slots fires**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 | `RelativeCandidate` — `readback a₀ (‖U_t U_sᴴ‖²)`, the `𝒪₂` value at one time pair | **fired** — needed, because every target states an equality or an inequality of `𝒪₂` values over all time pairs |
| 2 (conditional) | a cancelling-triple predicate | **unused** — `CF2`, `CF3`, `CF4` and `CF5` are stated readably with the three conjuncts written inline, so the conditional did not fire |

**No third definition was introduced** and **no amendment was needed**. **No lift, gauge element,
witness, matrix, triple, entry value or pair is a top-level definition** — each is a bound variable
pinned by an equation in the statement that needs it, as acts 10, 11, 12, 13 and 14 did. Acts 7's,
10's, 11's, 12's, 13's and 14's definitions are **reused, not redefined**. The module contains
exactly one `def`.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked. Ten named results, **no unproved declaration, no added
kernel assumption, no kernel-bypassing decision procedure**, every one printing only
`[propext, Classical.choice, Quot.sound]`. `decide` is used over finite index types and is
kernel-checked; `native_decide` appears nowhere, and neither does `sorry`.

| Result | Axioms |
| --- | --- |
| `relativeCandidate_apply` | `[propext, Classical.choice, Quot.sound]` |
| `relativeCandidate_congr` | `[propext, Classical.choice, Quot.sound]` |
| `cf1_composite_normal_form` | `[propext, Classical.choice, Quot.sound]` |
| `cf2_constant_strong_family_redundant` | `[propext, Classical.choice, Quot.sound]` |
| `relativeCandidate_eq_one_of_visible_subsingleton` | `[propext, Classical.choice, Quot.sound]` |
| `cf3_cardinality_scoping` | `[propext, Classical.choice, Quot.sound]` |
| `cf4_nontriviality_conjuncts` | `[propext, Classical.choice, Quot.sound]` |
| `relativeCandidate_of_permMatrix` | `[propext, Classical.choice, Quot.sound]` |
| `cf5_cancelling_triple_exists` | `[propext, Classical.choice, Quot.sound]` |
| `cf5_not_no_cancelling_on_relativeCandidate` | `[propext, Classical.choice, Quot.sound]` |

**`CF0` is type P and carries no evidence level**, so it is **not** part of the axiom table. It is
settled by the frozen evidence rule and by nothing else.

## What this round does not do

It does not: adopt a carrier as the physical one; name, endorse or exclude a selection principle;
assert or deny that a connection or gauge fixing exists or suffices; propose a datum sufficient for
the relative candidate; introduce a measurement model, regularity, homogeneity, generated evolution
or source-level coherence condition; change `CoherentLift`'s `ℕ`-indexing; revise `GL1s`, `GL1w`,
`GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1`, `PQ0`,
`PQ1`, `PQ2`, `PQ3` (a)–(c), `PQ4` or any merged label; answer act 13's fork `CT3` (d) or move it in
either direction; repair, correct, reinterpret, normalize or supersede act 14's `PQ3-d⁻` row, which
is recorded as carrying two readings and is left exactly as act 14 wrote it; report a proof of `N` in
`S`'s words, or `S` on the strength of `N` — neither is proved and both are refuted; change `D3`,
`D4b`, `D5`, the direct-branch statement or the readback convention; alter any existing archive seal
constant; consume or compare anything from the substratum Lemma 24.1 rounds; compare Source A with B
or C; edit any manuscript; close `P0` or either of its parts; or say anything about Track I.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.
