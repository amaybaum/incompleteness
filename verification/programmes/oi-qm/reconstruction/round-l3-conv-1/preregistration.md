# Reconstruction round L3-CONV-1 — what the converse direction of Level III proves, relative to its target class: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`. It is built from skeleton S5 of `research/equivalence/NOTES-E7.md`, `NOTES-E9.md` §1–§6 and the LEDGER row
L3-conv on `origin/research/equivalence` (head `424aa33b`). One design module covers part of it,
`research/equivalence/lean/EqvLevel3.lean` (blob `dc89d735`); no probe or `controls.py` exists; the statement surface
below is proposed and is fixed only by design runs before `F`. Nothing is executed. Only the owner designates `F`
under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round L3-CONV-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-l3-conv-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-l3-conv-1/
record AM verification/receipts/L3-CONV-1.json
execution A verification/lean-mathlib/OIBridge/Level3Converse.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

D: dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4. Delta(D, F) is this preregistration and any amendments in the round's
`amendments/` directory; **no manuscript, built artifact, `verification/ROADMAP.md`, landed kernel module or other
round's record changes under any outcome.**

Owner decisions recorded (PR #825, comment 6254706488, on the brief of comment 6254585897): the region availability
carries no composite clause and the round claims system-level exactness only, not OI⁺; no exact layer is added; every
positive token states what its credited hypothesis contributes and carries a countercontrol wherever a countermodel
exists.

## What the round is

Level III is a uniqueness theorem (AGENTS §A.34). A member of `QuasilocalSystem ι Q`
(QuasilocalCharacterization.lean:168) has, per finite region Λ, an injective (:176) unital star homomorphism `st Λ`
(:173) from `Matrix (Conf Λ Q) (Conf Λ Q) ℂ` by definition. At `D` a continuous map agreeing with the stages is the
canonical map (`canon_unique` :359), and two Target A systems (`OISystem` :463) with one dynamics are intertwined by
`systemEquiv` (`systemEquiv_dyn` :497). `QuasilocalSystem` occurs in no other kernel module at `D` or at `main`
`501331f5`; no theorem concludes an OI_Q condition from membership. The round bounds that direction with three
questions, each read by its own rule:

- **Q-CONV-REG (kernel).** Does Kraus normalization transfer along an injective unital star homomorphism out of a
  region's matrix algebra, into any star `ℂ`-algebra, in each direction, with injectivity used only for the
  algebra-to-matrix direction and unitality for the matrix-to-algebra direction, and does each direction fail without
  its hypothesis? At a member, the transfer along `S.st Λ` is the instance.
- **Q-CONV-EXACT (kernel).** Is a member's region availability — the instruments of a region's Kraus families whose
  images under `S.st Λ` are normalized in `S.A` — exactly the region's finite endomorphic Kraus instruments, with
  soundness from the injective direction and fullness from the unital direction, and does each inclusion fail along a
  map lacking its hypothesis?
- **Q-NONCOMM (kernel).** When there is a site and two states per site, does every member contain `a, b` with
  `a * b ≠ b * a`, from injectivity of one single-site stage, and is every member commutative when every region has at
  most one configuration?

## The proposed statement surface

Module `OIBridge/Level3Converse.lean`, namespace `OIBridge.Level3Converse`, importing
`OIBridge.QuasilocalCharacterization` and `OIBridge.KrausSoundness`; context
`{ι Q} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]`, `{B : Type*} [Ring B] [StarRing B] [Algebra ℂ B]`,
`K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ`, `M := Matrix (Conf Λ Q) (Conf Λ Q) ℂ`. [built]: in `EqvLevel3`, statement
unchanged; everything else is unbuilt, and exact signatures are fixed by the design runs.

```lean
-- Q-CONV-REG
theorem kraus_of_normalized_along (φ : M →⋆ₐ[ℂ] B) (hφ : Function.Injective φ) (K) :
    (∑ k, star (φ (K k)) * φ (K k) = 1) → ∑ k, (K k)ᴴ * K k = 1
theorem normalized_along_of_kraus (φ : M →⋆ₐ[ℂ] B) (K) :
    (∑ k, (K k)ᴴ * K k = 1) → ∑ k, star (φ (K k)) * φ (K k) = 1
theorem kraus_iff_of_member (S : QuasilocalSystem ι Q) {n : ℕ} (Λ : Finset ι) (K) :           -- [built]
    (∑ k, star (S.st Λ (K k)) * S.st Λ (K k) = 1) ↔ ∑ k, (K k)ᴴ * K k = 1
noncomputable def trivialStage (Λ : Finset ι) : M →⋆ₐ[ℂ] (Fin 0 → ℂ)                         -- countercontrol
theorem not_kraus_of_normalized_trivial (Λ : Finset ι) : ∃ K : Fin 1 → M,
    (∑ k, star (trivialStage Λ (K k)) * trivialStage Λ (K k) = 1) ∧ ¬ ∑ k, (K k)ᴴ * K k = 1      -- countercontrol
theorem not_normalized_of_kraus_zero (Λ : Finset ι) : ∃ K : Fin 1 → M,
    (∑ k, (K k)ᴴ * K k = 1) ∧ ¬ ∑ k, star ((0 : M →⋆ₙₐ[ℂ] M) (K k)) * (0 : M →⋆ₙₐ[ℂ] M) (K k) = 1  -- countercontrol
-- Q-CONV-EXACT
def availAlong (φ : M →⋆ₙₐ[ℂ] B) (m : ℕ) (F : Fin m → M →ₗ[ℂ] M) : Prop :=
  ∃ (n : ℕ) (K : Fin (n + 1) → M) (out : Fin (n + 1) → Fin m),
    (∑ k, star (φ (K k)) * φ (K k) = 1) ∧ F = instrumentBranch K out
def regionAvail (S : QuasilocalSystem ι Q) (Λ : Finset ι) : ∀ m, (Fin m → M →ₗ[ℂ] M) → Prop :=
  availAlong (S.st Λ : M →⋆ₙₐ[ℂ] S.A)
theorem regionTheory_krausSound (S) (Λ) (m) (F) : regionAvail S Λ m F → IsFiniteEndomorphicKrausInstrument F
theorem regionTheory_full (S) (Λ) (n m) (K : Fin (n + 1) → M) (out : Fin (n + 1) → Fin m) :
    ∑ k, (K k)ᴴ * K k = 1 → regionAvail S Λ m (instrumentBranch K out)
theorem regionTheory_exactSystem (S : QuasilocalSystem ι Q) (Λ : Finset ι) :
    ∀ (m : ℕ) (F : Fin m → M →ₗ[ℂ] M), regionAvail S Λ m F ↔ IsFiniteEndomorphicKrausInstrument F
theorem regionAvail_indep (S S' : QuasilocalSystem ι Q) (Λ : Finset ι) : regionAvail S Λ = regionAvail S' Λ
theorem availAlong_trivial_not_sound (Λ : Finset ι) : ∃ F : Fin 1 → M →ₗ[ℂ] M,
    availAlong (trivialStage Λ : M →⋆ₙₐ[ℂ] (Fin 0 → ℂ)) 1 F ∧ ¬ IsFiniteEndomorphicKrausInstrument F  -- countercontrol
theorem availAlong_zero_not_full (Λ : Finset ι) : ∃ F : Fin 1 → M →ₗ[ℂ] M,
    IsFiniteEndomorphicKrausInstrument F ∧ ¬ availAlong (0 : M →⋆ₙₐ[ℂ] M) 1 F                      -- countercontrol
-- Q-NONCOMM
theorem exists_not_comm_along [Nontrivial Q] (i₀ : ι)
    (φ : Matrix (Conf {i₀} Q) (Conf {i₀} Q) ℂ →⋆ₐ[ℂ] B) (hφ : Function.Injective φ) : ∃ a b : B, a * b ≠ b * a
theorem not_comm_of_system [Nontrivial Q] (S : QuasilocalSystem ι Q) (i₀ : ι) :               -- [built]
    ∃ a b : S.A, a * b ≠ b * a
theorem trivialStage_comm (a b : Fin 0 → ℂ) : a * b = b * a                                    -- countercontrol
theorem system_comm_of_subsingleton_conf (S : QuasilocalSystem ι Q)
    (h : ∀ Λ : Finset ι, Subsingleton (Conf Λ Q)) (a b : S.A) : a * b = b * a                  -- countercontrol
theorem system_comm_of_subsingleton [Subsingleton Q] (S : QuasilocalSystem ι Q) (a b : S.A) : a * b = b * a
theorem system_comm_of_isEmpty [IsEmpty ι] (S : QuasilocalSystem ι Q) (a b : S.A) : a * b = b * a
```

§A.34 witnesses, one per direction of each displayed biconditional: `kraus_iff_of_member` from
`kraus_of_normalized_along` with `S.injective Λ` (→) and `normalized_along_of_kraus` (←);
`regionTheory_exactSystem` from `regionTheory_krausSound` (→), which names `kraus_of_normalized_along`, and
`regionTheory_full` (←), which names `normalized_along_of_kraus`. `regionAvail_indep` follows from
`regionTheory_exactSystem` at `S` and `S'`. `regionTheory_exactSystem` has the shape of
`ExactFiniteEndomorphicQuantumOps` (KrausSoundness.lean:134) with `regionAvail S Λ` in place of a theory's `avail`;
its two halves correspond to `KrausSound` (:128) and `HasFullFiniteEndomorphicInstruments`
(StinespringAssembly.lean:186), split as in `exact_iff_sound_and_full` (KrausSoundness.lean:141).

**The region availability is not a `FiniteOperationalTheory`** (OperationalAssembly.lean:594). That structure's
fields include composite availability (`availExt` :599, `prepAvail` :626, `readout_avail` :642) and
`prepAvail_discard` (:649), which constrains the system availability by the composite one. With no composite clause,
`prepAvail_discard`, `avail_id` and `avail_coarse` are not obligations of this round. Packaging `regionAvail` as a
`FiniteOperationalTheory` would bring back a composite clause, and with it the obligation to prove
`prepAvail_discard` for `regionAvail`.

Landed objects cited, under `verification/lean-mathlib/OIBridge/`, each at the same line at `D` and at `main`
`501331f5` (the files' blobs are identical at both): QuasilocalCharacterization.lean `QuasilocalSystem` :168, `st`
:173, `injective` :176, `dense` :180, `oiSystem` :187, `canonEquiv` :350, `canonEquiv_stage` :355, `canon_unique`
:359, `OISystem` :463, `LocalityPreserving` :475, `systemEquiv_dyn` :497, `phase_localityPreserving` :769,
`phaseQ_ne_heisQ` :792; QuasilocalAlgebra.lean `ReversibleDynamics` :956; RegionTower.lean `Conf` :86;
InstrumentCompletion.lean `qInstrument_of_kraus` :165, `kraus_of_finiteSupport` :178, `finiteSupport_iff_kraus` :195;
MonoidalCompletion.lean `instrumentBranch` :731; KrausSoundness.lean `instrumentBranch_trace` :91,
`IsFiniteEndomorphicKrausInstrument` :112, `KrausSound` :128, `ExactFiniteEndomorphicQuantumOps` :134,
`exact_iff_sound_and_full` :141; StinespringAssembly.lean `HasFullFiniteEndomorphicInstruments` :186;
OperationalAssembly.lean `FiniteOperationalTheory` :594, `availExt` :599, `prepAvail` :626, `readout_avail` :642,
`prepAvail_discard` :649; LevelOneSeam.lean `ExactAllFiniteEndomorphicQuantumOps` :186; AncillaClosure.lean
`ExactCompositeQuantumOps` :364; CarrierGeneralOIPlus.lean `OIPlus` :185, `oiPlus_of_qm` :198;
ImplementationLocality.lean `fullClass` :374, `fullClass_arch` :518, `genTheory` :852; SubstratumSource.lean
`genTheory_qm_of_quantumArchitecture` :136, `fullClass_quantumArchitecture` :151.

**Provenance, not evidence of record.** `EqvLevel3` was built once, at the head of `dev-equivalence/split-l3`:
run 38091534622 (job 114328799399), head 8c92343e3a7d21b41a97090271285e0bff591eef.
Its Build step succeeded and its Release gate step failed (the job's step list), at `lean-manuscript` alone according
to `NOTES-E9.md` §6. That run is provenance for the two built statements kept here. The freeze relies on no claim read
from its log: the design evidence of record is the predicted-tree run of design work item 5, retained as stated under
"Retained evidence" below. The kernel modules `Level3Converse` uses have one blob at `D` and at `main`, the toolchain
files are unchanged between them, and no name declared here occurs at either; nothing is built at `D`.

## The decision rules

| Cell | Token | Rule |
|---|---|---|
| Q-CONV-REG | `L3-CONV-TRANSFER-PROVED` | the REG declarations are exactly the frozen ones (S1) and resolve (S2); `kraus_of_normalized_along` takes the injectivity hypothesis and `normalized_along_of_kraus` takes none (S1); `kraus_iff_of_member` names its two witnesses, one per direction, and supplies `QuasilocalSystem.injective` to the forward one (S3); both REG countercontrols elaborate with their frozen statements (S3); the exact-head run at `E` builds the module with every frozen print within `[propext, Classical.choice, Quot.sound]` |
| Q-CONV-REG | `L3-CONV-TRANSFER-NOT-ESTABLISHED` | otherwise |
| Q-CONV-EXACT | `L3-CONV-REGION-EXACT-PROVED` | the same conditions for the EXACT declarations; `regionTheory_exactSystem` assembled from its two witnesses, which name `kraus_of_normalized_along` and `normalized_along_of_kraus` respectively; `regionAvail S Λ` is `availAlong` at `S.st Λ` by definition; both EXACT countercontrols elaborate; the module names none of the full-class objects and imports neither `CarrierGeneralOIPlus` nor `SubstratumSource` (S3) |
| Q-CONV-EXACT | `L3-CONV-REGION-EXACT-NOT-ESTABLISHED` | otherwise |
| Q-NONCOMM | `L3-CONV-NONCOMM-PROVED` | the same conditions for the NONCOMM declarations; `not_comm_of_system` names `exists_not_comm_along` and `QuasilocalSystem.injective`; the three NONCOMM countercontrols elaborate, and `system_comm_of_subsingleton_conf` names `QuasilocalSystem.dense` (S3) |
| Q-NONCOMM | `L3-CONV-NONCOMM-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. `L3-CONV-1-READ` when the three cells are assigned; tokens printed by
`controls.py verdict E` from the measurements at `E`.

## What each positive token credits

| Token | credited hypothesis | what it contributes | countercontrol (the conclusion fails without it) |
|---|---|---|---|
| `L3-CONV-TRANSFER-PROVED` | injectivity of `φ` (forward) | recovers `∑ Kᴴ K = 1` from its image | `not_kraus_of_normalized_trivial`: along the unital, non-injective `trivialStage` into the trivial algebra, `K = 0` has normalized image and is not normalized |
| | unitality of `φ` (backward) | carries `1` to `1` | `not_normalized_of_kraus_zero`: along the zero star homomorphism, which is multiplicative and star-preserving but not unital, `K = 1` is normalized and its image is not |
| `L3-CONV-REGION-EXACT-PROVED` | soundness: the forward transfer at `S.st Λ` | every available family is Kraus-representable | `availAlong_trivial_not_sound`: along `trivialStage` the zero family is available, and it is no Kraus instrument because it does not preserve the aggregate trace (`instrumentBranch_trace`) |
| | fullness: the backward transfer at `S.st Λ` | every normalized Kraus family is available | `availAlong_zero_not_full`: along the zero map the identity instrument is Kraus-representable and not available |
| `L3-CONV-NONCOMM-PROVED` | `[Nontrivial Q]` and a site `i₀` | a single-site matrix algebra with two configurations, which is noncommutative | `system_comm_of_subsingleton_conf`, with its two instances `system_comm_of_subsingleton` and `system_comm_of_isEmpty`: when every region has at most one configuration, every member is commutative (stages are scalars, and the stages are dense) |
| | injectivity of the stage | carries the noncommuting matrix pair into `S.A` | `trivialStage_comm`: the unital, non-injective `trivialStage` lands in a commutative algebra |

Not credited by any token:
- **Member-level statements as such.** `kraus_iff_of_member` also follows from the landed Q1 (`qInstrument_of_kraus`,
  `kraus_of_finiteSupport`) by transport along `canonEquiv` (`canonEquiv_stage`). The REG token credits the transfer
  along an arbitrary injective unital star homomorphism, which no landed theorem states.
- **A member-general finite-support characterization.** For a family inside one stage, the characterization is the
  forward transfer applied to a choice of preimages, and it carries no hypothesis beyond the transfer's. The round
  does not state it separately. Its landed form at the OI completion is `finiteSupport_iff_kraus`.
- **Member independence.** `regionAvail_indep` is a consequence of `regionTheory_exactSystem` and credits no
  hypothesis. It records that the region availability carries no information about the member.
- **Composite availability and OI⁺.** OI⁺ needs system and composite exactness (`oiPlus_of_qm` requires
  `ExactAllFiniteEndomorphicQuantumOps`, LevelOneSeam.lean:186). Composite exactness for the full implementation class
  is landed (`genTheory_qm_of_quantumArchitecture`, `fullClass_quantumArchitecture`), and it does not depend on the
  member. No declaration of this round claims either.
- **The dynamical converse.** The converse over all locality-preserving star automorphisms fails at `oiSystem` by the
  landed `phaseQ_ne_heisQ` with `phase_localityPreserving`. The round does not restate it.

## The earned reading and the non-inference rule

> Earned reading (only when all three cells are positive): Level III states uniqueness among quasilocal systems
> carrying the substratum's matrix-algebra stages. Relative to that class its converse direction holds region by
> region, and at the system level only. Kraus normalization transfers along any injective unital star homomorphism
> out of a region's matrix algebra: injectivity recovers the matrix normalization, and unitality carries it forward.
> Each direction fails without its hypothesis. A member's region availability is exactly the region's finite
> endomorphic Kraus instruments, independently of the member. When there is a site and two states per site, every
> member has a noncommutative algebra; when every region has at most one configuration, every member is commutative.

> Non-inference rule: this round derives no quantum kinematics, dynamics or OI_Q condition at Level III, from OI or
> from anything weaker than membership in `QuasilocalSystem`, whose definition contains the complex matrix stages. The
> transfer uses only that the stage maps are injective unital star homomorphisms. It holds for any star algebra
> receiving such stages and is not evidence for OI. Level III is not restated as a biconditional: each displayed
> biconditional is a per-region transfer or availability statement with one witness per direction. The round claims
> no OI⁺, no composite exactness and no availability beyond the finite-support instruments of one region
> (`q3_countermodel`, InstrumentAvailability.lean:335).

**Premises this round does not source:** the complex matrix stages (the class's definition; the K row); composite
availability of any kind; Target A's dynamics `Φ` (data); the repairing hypotheses of NOTES-E9 §2 and the transport
form of NOTES-E14 and NOTES-E17.

## The controls (in `controls.py`)

- **S1 surface**: preamble, declarations in frozen order and signature, one `#print axioms` per theorem. Mutations,
  each failing with its code:
  - `[Nontrivial Q]` dropped from `not_comm_of_system`;
  - `hφ` dropped from `kraus_of_normalized_along`;
  - an injectivity hypothesis added to `normalized_along_of_kraus`;
  - `kraus_iff_of_member`'s right side made `∑ k, K k * (K k)ᴴ = 1`;
  - the `↔` of `regionTheory_exactSystem` replaced by `→`;
  - `regionAvail_indep` removed;
  - a declaration mentioning `OIPlus` or `ExactCompositeQuantumOps` added;
  - an import of `OIBridge.CarrierGeneralOIPlus` added;
  - a countercontrol removed;
  - an extra print.
- **S2 resolution**: each landed identifier above resolves to its `file:line` at `D` (`OIPlus` in
  `OIHierarchyGeneral`, not CompletedOI.lean:418).
- **S3 load-bearing**:
  - (i) the §A.34 witnesses above. A biconditional whose direction does not name its witness fails S3 alone.
  - (ii) `kraus_iff_of_member` passes `S.injective Λ` to `kraus_of_normalized_along`. `regionTheory_krausSound` names
    `kraus_of_normalized_along`, and `regionTheory_full` names `normalized_along_of_kraus`.
  - (iii) `regionAvail` unfolds to `availAlong` at `S.st Λ`, so the EXACT countercontrols bear on the same
    predicate.
  - (iv) each countercontrol's statement is the negation of its credited conclusion at its named map, as frozen.
  - (v) `not_comm_of_system` names `exists_not_comm_along` and `QuasilocalSystem.injective`.
    `system_comm_of_subsingleton_conf` names `QuasilocalSystem.dense`.
  - (vi) negative pin: no declaration names `genTheory`, `fullClass`, `fullClass_arch`,
    `genTheory_qm_of_quantumArchitecture`, `fullClass_quantumArchitecture`, `oiPlus_of_qm`, `OIPlus` or
    `ExactCompositeQuantumOps`. The module's imports are exactly the two above.
  - (vii) `q3_countermodel` (InstrumentAvailability.lean:335): with infinitely many sites the all-sites phase map is
    the total of no finite-support available operation, and no rule reads the region availability as covering it.
- **S4 phrases** (module header, result note): "OI implies quantum mechanics", "OI_Q iff", "OI_Q ⟺", "Level III
  equivalence", "Level III iff", "the converse of Level III is proved", "derives the kinematics", "design module",
  "satisfies OI⁺", "OI⁺ at every region".
- **V, G**:
  - three tokens; the earned reading exactly when all three are positive;
  - the diff `git diff --no-renames --name-status D E` lies inside the governed paths;
  - one import line after `import OIBridge.EqvK2MaxCone` (OIBridge.lean:268 at `D`);
  - one census family (§A.35), "Level III's converse direction relative to its target class: Kraus normalization
    transfer along injective unital star homomorphisms, system-level exactness of each member's region availability,
    noncommutativity of every member (round L3-CONV-1, reconstruction)", with `modules: ["Level3Converse"]`,
    `status: "kernel-only"` and `manuscript: []`.

## Retained evidence (AGENTS §A.42)

Each file is a complete expected result: build success, the release gate's steps and verdict, each governed module's
`#print axioms` reports, and the failure markers. Each names the commit it holds at, the recipe that regenerates it
(`verification/audits/evidence-retention/reproduce.py` at `main`), and its provenance: the run, the job, and the
digest of the log text it was read from. No raw log is committed.

| file (in the record directory, outside `amendments/`) | what | when |
| --- | --- | --- |
| `evidence/design-predicted-tree.json` | the predicted-tree run of design work item 5 | pinned by sha256 in this file before `F`; committed at that hash by the first execution commit |
| `evidence/F-run.json` | `F`'s exact-head `check-run` | by the first execution commit |
| `evidence/E-run.json` | `E`'s exact-head `check-run` | by an evidence-retention commit landed on `main` through its own pull request, before the reconciliation |

The predicted-tree run is dispatched on a disposable branch, at a commit `main` does not reach. Before `F` the owner
decides whether that commit is retained under `verification/audits/evidence-retention/objects/`, as for BG-3's
design-tree runs, so that the expected result reproduces from `main`.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms | `C3`: the dispatch run at exactly `E`, every job `success`; the Build step and every print |
| the module is registered; no manuscript changes | `C4`: the release gate at `E` passing every step |
| each direction of each displayed biconditional has its own witness; each credited hypothesis has its countercontrol; no full-class object is named | `C5`: S3 in `controls.py check E --freeze F` |
| the change stays inside the governed paths | `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |
| the design evidence the freeze relies on is retained at its pinned hash | `C8`: sha256 of `evidence/design-predicted-tree.json` at the first execution commit equals this file's pin |
| `F`'s exact-head run is retained | `C9`: `evidence/F-run.json` present at the first execution commit and naming `F` as its commit |
| `E`'s exact-head run reaches `main` before the reconciliation | `C10`: the reconciliation's first parent contains `evidence/E-run.json`, added by a commit that is not a round commit; the receipt's candidate entry for `E` names its digest |

## Design work required before F

1. Port `EqvLevel3` (blob `dc89d735`) to `Level3Converse` at `D`. Keep `kraus_iff_of_member` and
   `not_comm_of_system` with their statements unchanged. Route `kraus_iff_of_member` through its two named
   directions (§A.34), and route `not_comm_of_system` through `exists_not_comm_along`. Do not carry
   `phase_not_oiInduced`, `NaiveConverseDyn` or `not_naiveConverseDyn`, which restate landed Target B. Owner's choice:
   remove the recorded warning.
2. Write and build the unbuilt declarations, fixing their order and exact signatures. Their cost is unchecked; the
   countercontrols `system_comm_of_subsingleton_conf` (closure of scalar stages) and `trivialStage` (a unital star
   homomorphism into the pointwise trivial algebra `Fin 0 → ℂ`) carry the most risk. If either cannot be built, the
   owner decides before `F` whether the corresponding token is narrowed. It is not kept without its countercontrol.
3. Fix the type-class context of `B` and the coercion from `→⋆ₐ` to `→⋆ₙₐ` used by `regionAvail`.
4. Generate `controls.py` (S1–S4, V, G; `--self-test` driving each mutation).
5. Build and dispatch the predicted execution tree at `D`, recording the Build step, every print and every gate
   step. Extract its expected result as `evidence/design-predicted-tree.json` and enter its sha256 in this file.
6. Reconciliation is expected to meet two later rows on `main`: the import `OIBridge.TurnpikePremiseOrientation` at
   OIBridge.lean:269 and BG-2's census family, both written after `D` at the places this round also writes. Each is
   taken from `main` and each of this round's rows from `E` (§A.39 step 3).

## Stages and outcomes

C1 `controls.py` with `evidence/design-predicted-tree.json` and `evidence/F-run.json`; S1 the module, import line
and family; proof repairs only; S2 the result note, the candidate `E`. **`L3-CONV-1-READ`**:
`controls.py check E --freeze F` OK, three tokens printed, the exact-head run at `E` green on every job.
**`L3-CONV-1-HALTED`**: anything else (`S12`). No outcome edits the ROADMAP or a manuscript or restates Level III as a
biconditional; the H-∞ obligation (ROADMAP row P1, :71 at `main` `501331f5`, :70 at `D`) stays OPEN; correctness
bands unchanged (consistency axis).
