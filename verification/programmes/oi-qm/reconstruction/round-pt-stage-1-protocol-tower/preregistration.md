# Reconstruction round PT-STAGE-1 — the protocol tower: finite OI protocols as directed stages with SC∞ and finite rank: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`. It is built from `research/archive/{oistage,rank}/RESULT.md` and `research/archive/sa/SA-LEDGER.md` on
`origin/research/archive` (`4dc0321c`), and from `research/equivalence/NOTES-E2.md`, `NOTES-E7.md` (§1, row
Kinf-Stage) and `research/archive/eq/{A,E}/RESULT.md` on `origin/research/equivalence` (`424aa33b`). No design module,
probe or `controls.py` exists for it yet (no `.lean` file at `D`, at `main` `501331f5` or on either research branch
mentions `protocolTower`); the statement surface below is proposed and is fixed only by design runs before `F`.
Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round PT-STAGE-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-pt-stage-1-protocol-tower/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-pt-stage-1-protocol-tower/
record AM verification/receipts/PT-STAGE-1.json
execution A verification/lean-mathlib/OIBridge/ProtocolTower.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

D: dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4. Delta(D, F) is this preregistration and any amendments in the round's
`amendments/` directory; **no manuscript, built artifact, `verification/ROADMAP.md`, landed kernel module or other
round's record changes under any outcome.**

Owner decisions recorded (PR #827, comment 6254706688, on the brief of comment 6254586082): encoding E1, stage `n`
holding protocols of length at most `n + 1`; the visible-readout controls listed under Q-TOWER; no elementary-scope
cell; every positive token states what its credited hypothesis contributes and carries a countercontrol wherever a
countermodel exists.

## What the round is

K∞-Stage (ROADMAP.md:1023–1026 at `main` `501331f5`; :1022–1025 at `D`) is "stage consistency, the elementary scope
and finite rank: `SCInf`, `BinaryVisible` and `FiniteRank`. … A predicate for the full elementary-visible scope is not
yet formalized." These are CMP-1's hypotheses (StageCompletion.lean: `SCInf` :78, `BinaryVisible` :244, `FiniteRank`
:299), "proved for no OI construction"; the `DirectedStages` values at `D` are `badD` (:342), `bitTower` (:393) and
`midD` (CompletionAction.lean:404). **Findings** (none kernel at `D`):
- **PT** (oistage §1.1, §2; written, exact T0–T5 on Ω = Z₄ × Z₂): finite Ω, `φ : Equiv.Perm Ω`, readout `π : Ω → V`,
  a weight μ (canonical `unif`, CanonicalMeasure.lean:106), a menu of permutations; stage n: protocols over
  {obs, idle} ∪ A (obs records π(ω), then applies φ), records of positive weight, effects (protocol, record set),
  conditional counting. Forward maps are label inclusions, so the laws and SC∞ hold by `rfl`. No trace or ℂ enters
  (classical protocols).
- **`BinaryVisible` is satisfied degenerately** (SA-LEDGER, BinaryVisible row; exact P2 (a), (a2)). The structure
  (StageCompletion.lean:244–249) requires only `p(v0) + p(v1) = 1` at every stage and naturality. The zero/unit pair
  of the empty protocol meets it at every stage of every protocol tower. The readout content lies outside the
  structure.
- **Not in this round.** CT (§1.2), the lattice form: SC∞ by `card_fibre` (RegionTower.lean:398) and the cone
  `iterate_dependsOnlyOn_ball` (:283), with the action-interleaved cone lemma and `extPerm` transitivity missing. OPACT
  data (§5, F-S1; exact A1–A5): prefix-closed effects make `AffineRespect` (CompletionAction.lean:58) free, by label
  maps, and bijective actions give inverse data; without prefix closure it fails (A3).
- **NG1** (oistage §6; written, exact P1): for finite Ω every posterior is (μ∘σ⁻¹)·1_C normalized, so finitely many
  preparation vectors: the completed body is a polytope with finite automorphism group, and no drive exists. **NG2**
  (§7; written, re-read in SA §3; exact L1–L2): passive reads, `FiniteRank` and a time step with an inverse datum on the
  body leave a point or no d+2 extreme points in general position, excluding strictly convex bodies of dimension ≥ 2.
- **FiniteRank, open in general.** R0 (rank §1; written, exact on six instances): under SC∞, dim aff{prepVec x} =
  rank[p(e | x)] − 1, both infinite together. Finite Ω: rank ≤ |Ω| (written, SA §2.3); SA P3 (exact): an infinite
  carrier with SC∞, `BinaryVisible`, no `FiniteRank`. Leap rule on ℤ, readout v₀, uniform measure (rank §0, §4): passive
  nonlinear 1, 4, 6, 11, 21, 50, 89, 154 (n ≤ 8; ℚ to n = 4, two-prime F_p lower bounds beyond: affine dimension ≥ 153,
  unboundedness not proved); majority 1, 4, 8, 16, 32, 64, 120 (n ≤ 7, same fields); linear 1 at every horizon (written;
  exact to n = 8); with flip and swap, ranks 1, 3, 3 (linear), 1, 4, 7 (nonlinear) at L = 1, 2, 3 (F_p lower bounds).

The round asks, for finite carriers only:
- **Q-TOWER (kernel).** Is `protocolTower` a `DirectedStages` with inclusion maps and `SCInf` by `rfl` (as
  `bitTower_scInf` StageCompletion.lean:401), with a nonempty body when the weight is normalized? Is its
  `BinaryVisible` witness the `[obs]` readout pair, present at stage 0 under E1? When the readout attains both Boolean
  values on the weight's support, is each visible effect strictly between 0 and 1 at the empty preparation of every
  stage? Is a finite `Substratum`'s tower an instance?
- **Q-RANK (kernel).** Has the body `FiniteRank` with direction of dimension ≤ `Fintype.card Ω`?

## The proposed statement surface

Module `OIBridge/ProtocolTower.lean`, importing `OIBridge.CompletionAction`, `OIBridge.CanonicalMeasure`,
`OIBridge.SubstratumInterfaceAudit`. Proposals, not built; `D⋯` abbreviates `protocolTower φ π acts μ hμ0`:

```lean
inductive Step (A : Type) where | obs | idle | act (a : A)
variable {Ω V A : Type} [Fintype Ω] [DecidableEq Ω] [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]
  (φ : Equiv.Perm Ω) (π : Ω → V) (acts : A → Equiv.Perm Ω) (μ : Ω → ℝ) (hμ0 : ∀ ω, 0 ≤ μ ω)
def leaves : List (Step A) → Ω → Ω                                   -- the configuration a protocol leaves
def record : (w : List (Step A)) → Ω → (Fin (obsCount w) → V)        -- the readouts its obs steps write
noncomputable def table (e : Σ w, Finset (Fin (obsCount w) → V)) (x : Σ w, Fin (obsCount w) → V) : ℝ
  -- μ{ω : record x.1 ω = x.2 ∧ record e.1 (leaves x.1 ω) ∈ e.2} / weight x, weight x := μ{ω : record x.1 ω = x.2}
noncomputable def stage (n : ℕ) : FiniteStage   -- E1: lengths ≤ n + 1; preparations of positive weight; p := table
noncomputable def protocolTower : DirectedStages                      -- ι := ℕ; maps: inclusions on values
theorem protocolTower_scInf : SCInf D⋯ := fun _ _ _ _ _ => rfl
theorem protocolTower_body_nonempty (hμ1 : ∑ ω, μ ω = 1) : (body D⋯).Nonempty
theorem protocolTower_body_empty_zero : body (protocolTower φ π acts 0 (fun _ => le_rfl)) = ∅   -- countercontrol
-- the visible readout, V := Bool
def readoutEffect (i : ℕ) (b : Bool) : (stage i).E                    -- ⟨[obs], {r | r 0 = b}⟩
def emptyPrep (i : ℕ) (h : 0 < ∑ ω, μ ω) : (stage i).P                -- ⟨[], ()⟩
noncomputable def protocolTower_binaryVisible (π : Ω → Bool) : BinaryVisible D⋯
    -- v0 i := readoutEffect i false, v1 i := readoutEffect i true
theorem protocolTower_binaryVisible_v0 (i) : (protocolTower_binaryVisible π).v0 i = readoutEffect i false := rfl
theorem protocolTower_binaryVisible_v1 (i) : (protocolTower_binaryVisible π).v1 i = readoutEffect i true := rfl
theorem protocolTower_readout_nondegenerate (hπ : ∀ b : Bool, ∃ ω, 0 < μ ω ∧ π ω = b) (i : ℕ) (b : Bool) :
    0 < (stage i).p (readoutEffect i b) (emptyPrep i _) ∧ (stage i).p (readoutEffect i b) (emptyPrep i _) < 1
noncomputable def degenerateVisible : BinaryVisible D⋯                 -- countercontrol: v0 i := ⟨[], ∅⟩, v1 i := ⟨[], univ⟩
theorem degenerateVisible_values (i : ℕ) (x : (stage i).P) :            -- countercontrol
    (stage i).p (degenerateVisible.v0 i) x = 0 ∧ (stage i).p (degenerateVisible.v1 i) x = 1
theorem readout_certain_of_const (b₀ : Bool) (h : ∀ ω, 0 < μ ω → π ω = b₀) (hw : 0 < ∑ ω, μ ω) (i : ℕ) :  -- countercontrol
    (stage i).p (readoutEffect i b₀) (emptyPrep i hw) = 1
-- finite rank
noncomputable def response : (Ω → ℝ) →ₗ[ℝ] CSpace D⋯                -- with `posterior : Prep D⋯ → Ω → ℝ`
theorem prepVec_eq_response (x : Prep D⋯) : prepVec D⋯ x = response … (posterior … x)
theorem protocolTower_finiteRank : FiniteRank (body D⋯)
theorem protocolTower_rank_le : Module.finrank ℝ (affineSpan ℝ (body D⋯)).direction ≤ Fintype.card Ω
theorem protocolTower_chart (hμ1 : ∑ ω, μ ω = 1) : Nonempty (CompletionChart D⋯)   -- by `exists_completionChart`
noncomputable def growingTower : DirectedStages                        -- countercontrol (see the credit table)
theorem growingTower_scInf : SCInf growingTower
noncomputable def growingTower_binaryVisible : BinaryVisible growingTower
theorem growingTower_sharp : ∃ x0 x1 : (growingTower.stage 0).P,
    (growingTower.stage 0).p (growingTower_binaryVisible.v0 0) x0 = 1 ∧
      (growingTower.stage 0).p (growingTower_binaryVisible.v1 0) x1 = 1
theorem not_finiteRank_growingTower : ¬ FiniteRank (body growingTower)
-- the substratum instance
noncomputable def substratumTower (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V]
    (Vs : Finset 𝒮.ι) (acts : A → Equiv.Perm 𝒮.Conf) : DirectedStages   -- 𝒮.φ, restriction to Vs, unif
```

Landed objects cited, each at the same line at `D` and at `main` `501331f5` (the files' blobs are identical at both):
`FiniteStage` KInfFoundations.lean:63; StageCompletion.lean `StageMap` :53, `DirectedStages` :63, `SCInf` :78, `val`
:98, `prepVec` :135, `body` :141, `body_subset` :171, `BinaryVisible` :244, `perfectlyDistinguishable_visible` :274,
`FiniteRank` :299, `badD` :342, `not_scInf_bad` :350, `bitTower` :393, `bitTower_scInf` :401; CompletionAction.lean
`AffineRespect` :58, `CompletionChart` :144, `exists_completionChart` :154, `midD` :404; `unif`
CanonicalMeasure.lean:106; `Substratum` SubstratumInterfaceAudit.lean:60, `Conf` :78, `φ` :81; RegionTower.lean
`iterate_dependsOnlyOn_ball` :283, `card_fibre` :398; `not_boundaryTransitive_of_nonextreme_boundary`
TransitiveBody.lean:301; `stochastic_interface_gap` StochasticInterface.lean:182; `trajProb` PassiveQuotient.lean:339.
Rank proof route: `body_subset`, `response`.

The elementary-scope predicate is not part of this round. It is to be the subject of a separate round with its own
controls, for which `ElemScope` (SA-LEDGER §4 P-D) is the preferred starting candidate; it is not adopted here as a
premise.

## The decision rules

| Cell | Token | Rule |
|---|---|---|
| Q-TOWER | `PT-STAGE-TOWER-PROVED` | the Q-TOWER declarations are exactly the frozen ones (S1) and resolve to the landed objects (S2); `protocolTower_scInf`'s proof is the frozen `rfl` term; `protocolTower_binaryVisible_v0` and `_v1` hold by `rfl`, so the witness is the `[obs]` readout pair; `protocolTower_readout_nondegenerate` takes `hπ`; the Q-TOWER countercontrols elaborate with their frozen statements (S3); the exact-head run at `E` builds the module with every frozen `#print axioms` line within `[propext, Classical.choice, Quot.sound]` |
| Q-TOWER | `PT-STAGE-TOWER-NOT-ESTABLISHED` | otherwise |
| Q-RANK | `PT-STAGE-RANK-PROVED` | S1, S2, the build and the prints for the Q-RANK declarations; `protocolTower_finiteRank`'s proof names `prepVec_eq_response` and `body_subset`; the Q-RANK countercontrols elaborate with their frozen statements (S3) |
| Q-RANK | `PT-STAGE-RANK-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. `PT-STAGE-1-READ` when both cells are assigned; the tokens are printed by
`controls.py verdict E` from the measurements at `E`.

## What each positive token credits

| Token | credited hypothesis | what it contributes | countercontrol (the conclusion fails without it) |
|---|---|---|---|
| `PT-STAGE-TOWER-PROVED` | a horizon-independent table read through label inclusions | SC∞ by definitional equality | `not_scInf_bad` (landed): identity label maps with a stage-dependent table violate SC∞ |
| | a normalized weight, `hμ1` | the empty protocol is a preparation of weight 1, so the body is nonempty | `protocolTower_body_empty_zero`: with the zero weight no record has positive weight and the body is empty |
| | E1 with the readout `π : Ω → Bool` | the `[obs]` readout pair at every stage, stage 0 included | `degenerateVisible` with `degenerateVisible_values`: the zero/unit pair of the empty protocol also satisfies `BinaryVisible`, at the values 0 and 1 only. The S3 pin requires the token's witness to be the readout pair, so the degenerate pair cannot earn it |
| | `hπ`: the readout attains both Boolean values on the weight's support | each visible effect strictly between 0 and 1 at the empty preparation | `readout_certain_of_const`: when the readout takes one value `b₀` on the support, the visible effect for `b₀` is certain at the empty preparation of every stage |
| `PT-STAGE-RANK-PROVED` | finiteness of Ω | every preparation vector is the response of a vector in ℝ^Ω, which bounds the rank by `Fintype.card Ω` | `growingTower`: a directed stage system with SC∞ and a `BinaryVisible` pair that is sharp at stage 0, whose body has no finite rank. Its protocol-tower form on Ω = ℤ is SA P3 (exact, not kernel) |

Not credited by any token:
- **The chart.** `protocolTower_chart` is the landed `exists_completionChart` applied to the two credited results.
- **The substratum instance.** `substratumTower` applies the generic construction to a finite `Substratum`'s own data
  (`𝒮.φ`, the restriction to `Vs`, `unif`). Its properties are those of the generic theorems at those data; it fixes
  that the construction accepts the framework's substratum, and adds no hypothesis.
- **A sharp visible pair.** `protocolTower_readout_nondegenerate` gives no preparation on which a visible effect is
  certain. The hypotheses of `perfectlyDistinguishable_visible` hold on some protocol towers and not on others
  (SA-LEDGER, BinaryVisible row), and the round claims neither.
- **The encoding.** E1 is a definition. Under lengths at most `n`, stage 0 carries the empty protocol alone, and
  `BinaryVisible` could be met there only by the zero/unit pair of the empty protocol, as in `degenerateVisible`.

## The earned reading and the non-inference rule

> Earned reading (only when both cells are positive): for finite substratum protocol data the protocol tower is a
> field-neutral DirectedStages with inclusion maps and SC∞ by definitional equality, with a nonempty body when the
> weight is normalized. Its BinaryVisible witness is the readout of one observation, present from stage 0. When the
> readout attains both values on the weight's support, each visible effect lies strictly between 0 and 1 at the empty
> preparation of every stage. The body has finite rank at most the number of configurations, hence a chart. A finite
> Substratum's tower is an instance. The result establishes directed stages, SC∞ and finite-rank infrastructure. It
> does not establish K∞-Geom, K∞-Trans, K∞-Drive or physical reconstruction.

> Non-inference rule: the tower gives stages and a chart, not a ball. On finite carriers the completed body is a
> polytope (NG1, written with exact instances, not a kernel theorem here), so in chart dimension ≥ 2 no body-preserving
> family is boundary transitive (`not_boundaryTransitive_of_nonextreme_boundary` TransitiveBody.lean:301 with NG1,
> written, SA §3.2) and no drive exists; NG2 (written) excludes strictly convex bodies of dimension ≥ 2 for passive
> towers with FiniteRank and a reversible step. A positive outcome sources neither K∞-Geom, K∞-Trans nor K∞-Drive and
> is evidence for none. SC∞ here is projective consistency of one global law, with no elementary or quantum content.
> Bare `BinaryVisible` holds for the degenerate pair; the readout content is the nondegeneracy result under `hπ`, and
> it is not a sharp pair. Infinite-carrier finite rank (CT, R0, the leap ranks) is not addressed. No scope predicate is
> defined or met. NG1 and NG2 concern passive classical towers; record-writing observation and a step irreversible on
> the body (SA §3.2) lie outside them and are not decided.

**Premises this round does not source:** finite rank of any infinite-carrier completion; the CT lemmas; K∞-Act
(prefix-closed effects, `AffineRespect`, `Undoes`, inverse data); a sharp stage test (NOTES-E2 §1); K∞-Drive, K∞-Trans,
K∞-V4, K∞-Copy, K∞-Geom; an elementary-scope predicate; the choice of μ (`stochastic_interface_gap`
StochasticInterface.lean:182).

## The ROADMAP wording the round would license

Not applied by the round. With Q-TOWER and Q-RANK positive, K∞-Stage (ROADMAP.md:1023–1026 at `main`) may gain: "On
finite carriers the protocol tower has `SCInf` by definitional equality, a visible readout pair that is nondegenerate
when the readout attains both values, and a completion of finite rank (`protocolTower_scInf`,
`protocolTower_readout_nondegenerate`, `protocolTower_finiteRank`); infinite-carrier finite rank and the elementary
scope are not supplied." The owner scopes ROADMAP.md:1022 at `main` ("All are unsourced"; :1021 at `D`). K∞ and
K∞-Stage remain OPEN under every outcome.

## The controls (in `controls.py`)

- **S1 surface**: preamble, frozen declarations and signatures in order, frozen prints. Mutations failing with their
  codes:
  - positivity dropped;
  - an `n`-dependent table;
  - a non-inclusion map;
  - stage `n` restricted to lengths at most `n`;
  - `hπ` dropped from `protocolTower_readout_nondegenerate`;
  - the rank bound changed;
  - a countercontrol removed;
  - an extra print.
- **S2 resolution**: every landed object above resolves to its declaration at `D`.
- **S3 load-bearing**:
  - `protocolTower_scInf`'s proof is `fun _ _ _ _ _ => rfl`; a `simp` proof fails S3 alone.
  - `protocolTower_binaryVisible_v0` and `_v1` are proved by `rfl`. A witness whose fields are `degenerateVisible`'s,
    or any pair other than `readoutEffect i false` and `readoutEffect i true`, fails S3.
  - `protocolTower_finiteRank`'s proof names `prepVec_eq_response` and `body_subset`.
  - Each countercontrol's statement is the negation, or the degenerate value pattern, of its credited conclusion, as
    frozen. `not_scInf_bad` (StageCompletion.lean:350) resolves unchanged.
  - The module text has no `ℂ`, `Complex`, `Matrix` or `trace`.
- **S4 phrases** (header, result note): "K∞-Stage is discharged", "sources K∞-Geom", "sources K∞-Trans", "the
  completion is a ball", "OI supplies finite rank", "scope is sourced", "kernel proof of NG", "design module", "sharp
  visible pair is supplied".
- **V, G**:
  - one token per cell; the earned reading exactly when both are positive;
  - `D..E` inside the governed paths;
  - one import line after `import OIBridge.EqvK2MaxCone` (OIBridge.lean:268, the last import at `D`);
  - one census family (§A.35) with `modules: ["ProtocolTower"]`, `status: "kernel-only"` and `manuscript: []`.

## Retained evidence (AGENTS §A.42)

Each file is a complete expected result: build success, the release gate's steps and verdict, each governed module's
`#print axioms` reports, and the failure markers. Each names the commit it holds at, the recipe that regenerates it
(`verification/audits/evidence-retention/reproduce.py` at `main`), and its provenance: the run, the job, and the
digest of the log text it was read from. No raw log is committed.

| file (in the record directory, outside `amendments/`) | what | when |
| --- | --- | --- |
| `evidence/design-predicted-tree.json` | the predicted-tree run of design work item 3 | pinned by sha256 in this file before `F`; committed at that hash by the first execution commit |
| `evidence/F-run.json` | `F`'s exact-head `check-run` | by the first execution commit |
| `evidence/E-run.json` | `E`'s exact-head `check-run` | by an evidence-retention commit landed on `main` through its own pull request, before the reconciliation |

The predicted-tree run is dispatched on a disposable branch, at a commit `main` does not reach. Before `F` the owner
decides whether that commit is retained under `verification/audits/evidence-retention/objects/`, as for BG-3's
design-tree runs, so that the expected result reproduces from `main`.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py` blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms | `C3`: the dispatch run at exactly `E`, every job `success`; the Mathlib bridge build and the frozen prints |
| SC∞ by `rfl`; the visible witness is the readout pair; the rank proof factors through `response`; each credited hypothesis has its countercontrol; field-neutral content | `C5`: S3 in `controls.py check E --freeze F` |
| the module is registered; no manuscript changes; the change stays in the governed paths | `C4`: the release gate at `E` passing every step; `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |
| the design evidence the freeze relies on is retained at its pinned hash | `C8`: sha256 of `evidence/design-predicted-tree.json` at the first execution commit equals this file's pin |
| `F`'s exact-head run is retained | `C9`: `evidence/F-run.json` present at the first execution commit and naming `F` as its commit |
| `E`'s exact-head run reaches `main` before the reconciliation | `C10`: the reconciliation's first parent contains `evidence/E-run.json`, added by a commit that is not a round commit; the receipt's candidate entry for `E` names its digest |

## Design work required before F

1. Build the design module from `D` (build green, prints within the three axioms, gate red only at
   `lean-manuscript`). Nothing mentioning `protocolTower` exists on any branch. Fix `Fintype` for bounded words and
   records, general μ or `unif`, and `weight` via `trajProb` (PassiveQuotient.lean:339) or not.
2. Build the countercontrols. `growingTower` (stage `n` the classical stage on `n + 2` points with the point
   indicators, the indicator of point 0 and its complement as effects, inclusion maps) carries the most risk: its
   `¬ FiniteRank` needs infinitely many affinely independent preparation vectors. If it cannot be built, the owner
   decides before `F` whether the rank token is narrowed. It is not kept without its countercontrol.
3. Build and dispatch the predicted execution tree; `controls.py`, its self-test and the family text. None exists.
   Extract the run's expected result as `evidence/design-predicted-tree.json` and enter its sha256 in this file.
4. Outside the default surface, and only by owner decision before `F`: R0 in kernel form (one witness per direction,
   §A.34); label duals (a K∞-Act round); CT; an exact layer replaying SA P3 or oistage P1 (adding a probe and the
   workflow to the paths).
5. Reconciliation is expected to meet two later rows on `main`: the import `OIBridge.TurnpikePremiseOrientation` at
   OIBridge.lean:269 and BG-2's census family, both written after `D` at the places this round also writes. Each is
   taken from `main` and each of this round's rows from `E` (§A.39 step 3).

## Stages and outcomes

C1 adds `controls.py` with `evidence/design-predicted-tree.json` and `evidence/F-run.json`; S1 the module, import line
and census family; later commits repair proofs only; S2 the result note, candidate `E`. **`PT-STAGE-1-READ`**:
`controls.py check E --freeze F` OK, one token per cell, the exact-head run at `E` green on every job.
**`PT-STAGE-1-HALTED`**: anything else (`S12`). No outcome sources K∞-Geom, K∞-Trans, K∞-Drive, physical
reconstruction or finite rank beyond finite carriers, or edits the ROADMAP or a manuscript; correctness bands unchanged
(consistency axis).
