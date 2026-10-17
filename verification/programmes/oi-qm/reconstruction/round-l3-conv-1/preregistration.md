# Reconstruction round L3-CONV-1 — what the converse direction of Level III proves, relative to its target class: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`. It is built from skeleton S5 of `research/equivalence/NOTES-E7.md`, `NOTES-E9.md` §1–§6 and the LEDGER row
L3-conv on `origin/research/equivalence` (head `424aa33b`). One design module covers part of it,
`research/equivalence/lean/EqvLevel3.lean` (blob `dc89d735`, design run 38091534622 on `dev-equivalence/split-l3` at
`8c92343e`, based on L = `9f9f8257`); no probe or `controls.py` exists; the statement surface below is proposed and
is fixed only by design runs before `F`. Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an
instruction to proceed is not a designation.

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

## What the round is

Level III is a uniqueness theorem (AGENTS §A.34). A member of `QuasilocalSystem ι Q`
(QuasilocalCharacterization.lean:168) has, per finite region Λ, an injective unital star homomorphism `st Λ` from
`Matrix (Conf Λ Q) (Conf Λ Q) ℂ` by definition. At `D` a continuous map agreeing with the stages is the canonical map
(`canon_unique` :359), and two Target A systems (`OISystem` :463) with one dynamics are intertwined by `systemEquiv`
(`systemEquiv_dyn` :497). `QuasilocalSystem` occurs in no other kernel module at `D`; no theorem concludes an OI_Q
condition from membership. The round bounds that direction with two questions, each read by its own rule:

- **Q-CONV (kernel; two cells).** For every member `S` and finite region Λ: (REG) does Kraus normalization transfer
  along `S.st Λ` in each direction, and are the member's finite-support instruments exactly the images of the region's
  Kraus families, the landed Q1 (`finiteSupport_iff_kraus`, InstrumentCompletion.lean:195, OI completion only) at
  every member? (OIPLUS) does the region theory they define satisfy OI⁺ at every Λ, through `oiPlus_of_qm`?
- **Q-NAIVE (kernel).** Is `NaiveConverseDyn ι Q` (below; `LocalityPreserving` QuasilocalCharacterization.lean:475, `ReversibleDynamics`
  QuasilocalAlgebra.lean:956) false when there is a site and two states per site, and does every member then
  contain `a, b` with `a * b ≠ b * a`?

## The proposed statement surface

Module `OIBridge/Level3Converse.lean`, namespace `OIBridge.Level3Converse`, importing
`OIBridge.QuasilocalCharacterization`, `OIBridge.CarrierGeneralOIPlus`, `OIBridge.SubstratumSource`; context
`{ι Q} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]`, `K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ`.
[built]: in `EqvLevel3`, statement unchanged; everything else is unbuilt.

```lean
theorem phase_not_oiInduced [Nontrivial Q] (i₀ : ι) (Φ : ReversibleDynamics ι Q) :             -- [built]
    ¬ ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
        phaseEquiv i₀ (stage Λ X) = stage (hat Φ Λ) (transported Φ Λ X)
def NaiveConverseDyn (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q] :   -- [built]
    Prop := ∀ (S : QuasilocalSystem ι Q) (α : S.A ≃⋆ₐ[ℂ] S.A), LocalityPreserving S α →
      ∃ Φ : ReversibleDynamics ι Q, ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
        α (S.st Λ X) = S.st (hat Φ Λ) (transported Φ Λ X)
theorem not_naiveConverseDyn [Nontrivial Q] (i₀ : ι) : ¬ NaiveConverseDyn ι Q                 -- [built]
theorem not_comm_of_system [Nontrivial Q] (S : QuasilocalSystem ι Q) (i₀ : ι) :               -- [built]
    ∃ a b : S.A, a * b ≠ b * a
theorem kraus_iff_of_member (S : QuasilocalSystem ι Q) {n : ℕ} (Λ : Finset ι) (K) :           -- [built]
    (∑ k, star (S.st Λ (K k)) * S.st Λ (K k) = 1) ↔ ∑ k, (K k)ᴴ * K k = 1
def MemberFiniteSupport (S) (β : Fin n → S.A) : Prop := ∃ Λ : Finset ι, ∀ k, β k ∈ Set.range (S.st Λ)
theorem finiteSupport_iff_kraus_of_member (S) (β : Fin n → S.A) :
    ((∑ k, star (β k) * β k = 1) ∧ MemberFiniteSupport S β)
      ↔ ∃ Λ K, (∀ k, β k = S.st Λ (K k)) ∧ ∑ k, (K k)ᴴ * K k = 1
noncomputable def regionTheory (S) (Λ) : FiniteOperationalTheory (Conf Λ Q) :=
  { genTheory fullClass fullClass_arch (Conf Λ Q) with avail := regionAvail S Λ, avail_id := _, avail_coarse := _ }
theorem regionTheory_exactSystem (S) (Λ) : ExactFiniteEndomorphicQuantumOps (regionTheory S Λ)
theorem regionTheory_oiPlus (S : QuasilocalSystem ι Q) : ∀ Λ : Finset ι, OIPlus (regionTheory S Λ)
theorem regionAvail_indep (S S' : QuasilocalSystem ι Q) (Λ : Finset ι) : regionAvail S Λ = regionAvail S' Λ
```

§A.34 witnesses: `kraus_iff_of_member` from `kraus_of_member_normalized` (→) and `member_normalized_of_kraus` (←);
`finiteSupport_iff_kraus_of_member` from `kraus_of_finiteSupport_member` (→) and `finiteSupport_of_kraus_member` (←),
the landed `kraus_of_finiteSupport` (InstrumentCompletion.lean:178) and `qInstrument_of_kraus` (:165) with `S.st`
for `stage`; `regionTheory_exactSystem` by `exact_iff_sound_and_full` from `regionTheory_krausSound` (`KrausSound`)
and `regionTheory_full` (`HasFullFiniteEndomorphicInstruments`). `regionAvail S Λ O F`: `F` is the family
`o ↦ ∑_{out k = o} conjChannel (K k)` for some `K : Fin (n + 1) → …`, `out` with `S.st Λ (K k)` normalized in `S.A`.
Controls: `targetA_conclusion (T : OISystem ι Q)`, the conclusion of `NaiveConverseDyn` for `T.α`; countercontrol
`stage_comm_of_subsingleton [Subsingleton Q]`: `S.st Λ X * S.st Λ Y = S.st Λ Y * S.st Λ X`.

Landed objects at `D`, under `verification/lean-mathlib/OIBridge/`: QuasilocalCharacterization.lean `st` :173,
`injective` :176, `oiSystem` :187, `oi_localityPreserving` :479, `continuous_phaseQ` :704, `phaseEquiv` :756,
`phaseEquiv_apply` :766, `phase_localityPreserving` :769, `phaseQ_ne_heisQ` :792; QuasilocalAlgebra.lean `exists_ofM`
:481, `stage` :684, `stage_apply` :696, `hat` :1040, `transported` :1109, `continuous_heisQ` :1271, `heisQ_stage`
:1274; RegionTower.lean `Conf` :86; OperationalAssembly.lean `FiniteOperationalTheory` :594; MonoidalCompletion.lean
`conjChannel` :360; KrausSoundness.lean `KrausSound` :128, `ExactFiniteEndomorphicQuantumOps` :134,
`exact_iff_sound_and_full` :141; StinespringAssembly.lean `HasFullFiniteEndomorphicInstruments` :186;
CarrierGeneralOIPlus.lean `OIPlus` :185 (`OIHierarchyGeneral`, not CompletedOI.lean:418), `oiPlus_of_qm` :198;
ImplementationLocality.lean
`fullClass` :374, `fullClass_arch` :518, `genTheory` :852; SubstratumSource.lean `genTheory_qm_of_quantumArchitecture`
:136, `fullClass_quantumArchitecture` :151.

**Design evidence.** Run 38091534622, job 114328799399: Build step success, Release gate step failure (the job's
step list). NOTES-E9 §6 records `Build completed successfully (3646 jobs)`, the four prints each `[propext,
Classical.choice, Quot.sound]`, one warning (an unused simp argument in `not_comm_of_system`) and `lean-manuscript` as
the only failing gate step. The modules `EqvLevel3` uses have one blob at L and `D`, the toolchain files are
unchanged, and no name declared here occurs at `D`; nothing is built at `D`.

## The decision rules

| Cell | Token | Rule |
|---|---|---|
| Q-CONV-REG | `L3-CONV-TRANSFER-PROVED` | the REG declarations are exactly the frozen ones (S1) and resolve (S2); each displayed biconditional names its two frozen witnesses, one per direction, and the forward transfer names `QuasilocalSystem.injective` (S3); the exact-head run at `E` builds the module with every frozen print within `[propext, Classical.choice, Quot.sound]` |
| Q-CONV-REG | `L3-CONV-TRANSFER-NOT-ESTABLISHED` | otherwise |
| Q-CONV-OIPLUS | `L3-CONV-REGION-OIPLUS-PROVED` | the same conditions for the OIPLUS declarations; `regionTheory_exactSystem` assembled from its two witnesses; `regionTheory_oiPlus` names `oiPlus_of_qm` and `genTheory_qm_of_quantumArchitecture` (S3) |
| Q-CONV-OIPLUS | `L3-CONV-REGION-OIPLUS-NOT-ESTABLISHED` | otherwise |
| Q-NAIVE | `L3-CONV-NAIVE-REFUTED` | the same conditions for the Q-NAIVE declarations and both controls; `not_naiveConverseDyn` names `oiSystem`, `phase_localityPreserving` and `phase_not_oiInduced`, which names `phaseQ_ne_heisQ` (S3) |
| Q-NAIVE | `L3-CONV-NAIVE-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. `L3-CONV-1-READ` when the three cells are assigned; tokens printed by
`controls.py verdict E` from the measurements at `E`.

## The earned reading and the non-inference rule

> Earned reading (only when all three cells are positive): Level III states uniqueness among quasilocal systems
> carrying the substratum's matrix-algebra stages. Relative to that class its converse direction holds region by
> region: Kraus normalization transfers along every member's stage maps in each direction, the member's
> finite-support instruments on a region are the images of its Kraus families, and the region theory they define,
> with composite availability from the full implementation class, satisfies OI⁺, its availability independent of the
> member. When there is a site and two states per site, the converse over all locality-preserving star automorphisms
> is false and every member has a noncommutative algebra.

> Non-inference rule: this round derives no quantum kinematics, dynamics or OI_Q condition at Level III, from OI or
> from anything weaker than membership in `QuasilocalSystem`, whose definition contains the complex matrix stages. The
> transfer holds because the stage maps are injective unital star homomorphisms; it holds for any C*-algebra receiving
> such stages and is not evidence for OI. Level III is not restated as a biconditional: each displayed biconditional is
> a per-region transfer statement with one witness per direction. The region theory's composite clause comes from the
> interface, not the member, and the theory covers finite-support instruments only (`q3_countermodel`). The
> refutation concerns `NaiveConverseDyn` as stated, not converses under added hypotheses, which stay outside the round.

**Premises this round does not source:** the complex matrix stages (the class's definition; the K row); the region
theory's composite availability; Target A's dynamics `Φ` (data); the repairing hypotheses of NOTES-E9 §2 and the
transport form of NOTES-E14 and NOTES-E17.

## The controls (in `controls.py`)

- **S1 surface**: preamble, declarations in frozen order and signature, one `#print axioms` per theorem. Mutations,
  each failing with its code: `[Nontrivial Q]` dropped from `not_comm_of_system`; `LocalityPreserving S α` dropped
  from `NaiveConverseDyn`; `kraus_iff_of_member`'s right side made `∑ k, K k * (K k)ᴴ = 1`; `∀ Λ` in
  `regionTheory_oiPlus` replaced by `∅`; `regionAvail_indep` removed; an extra print.
- **S2 resolution**: each landed identifier above resolves to its `file:line` at `D` (`OIPlus` in `OIHierarchyGeneral`).
- **S3 load-bearing**: (i) the §A.34 witnesses above; a forward component not naming its witness fails S3 alone.
  (ii) `kraus_of_member_normalized` names `QuasilocalSystem.injective`; `member_normalized_of_kraus` does not. (iii)
  the refutation uses the landed Target B witness. (iv) `targetA_conclusion` with `oi_localityPreserving`: the
  predicate's conclusion holds for every Target A automorphism. (v) `stage_comm_of_subsingleton`: `[Nontrivial Q]`
  is load-bearing. (vi) `q3_countermodel` (InstrumentAvailability.lean:335): with infinitely many sites the all-sites
  phase map is the total of no finite-support available operation, and no rule reads the region theory as covering it.
- **S4 phrases** (module header, result note): "OI implies quantum mechanics", "OI_Q iff", "OI_Q ⟺", "Level III
  equivalence", "Level III iff", "the converse of Level III is proved", "derives the kinematics", "design module".
- **V, G**: three tokens; the earned reading exactly when all three are positive. The diff
  `git diff --no-renames --name-status D E` lies inside the governed paths; one import line after
  `import OIBridge.EqvK2MaxCone` (OIBridge.lean:268); one census family (§A.35), "Level III's converse direction
  relative to its target class: per-region Kraus transfer, region theories satisfying OI⁺, the dynamical converse
  refuted (round L3-CONV-1, reconstruction)", `modules: ["Level3Converse"]`, `status: "kernel-only"`, `manuscript: []`.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms | `C3`: the dispatch run at exactly `E`, every job `success`; the Build step and every print |
| each direction of each displayed biconditional has its own witness | `C5`: S3 in `controls.py check E --freeze F` |
| the module is registered; no manuscript changes | `C4`: the release gate at `E` passing every step |
| the change stays inside the governed paths | `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design work required before F

1. Port `EqvLevel3` (blob `dc89d735`) to `Level3Converse` at `D`, its five built statements unchanged, splitting
   `kraus_iff_of_member` into two named directions (§A.34); owner's choice: remove the recorded warning.
2. Write and build the unbuilt declarations, fixing the order and exact signatures of those given in prose; the
   region theory's cost is unchecked (NOTES-E7 S5; NOTES-E9 §5).
3. Owner decision on the region theory's composite clause: (a) inherited from `genTheory fullClass`, as proposed;
   (b) derived from the member's larger regions, not designed: regions give ancilla carriers of size `|Q|^m`, while
   `ExactCompositeQuantumOps` (AncillaClosure.lean:364) quantifies over every `Fin (k + 1)`; (c) none, the OIPLUS
   cell reduced to system-level exactness. The OIPLUS rule and the earned reading follow the choice.
4. If Mathlib at the pin has a trivial C*-algebra, add a semantic countercontrol for injectivity. Generate
   `controls.py` (S1–S4, V, G; `--self-test` driving each mutation).
5. Owner choice: an exact layer from `experiments/e9_level3.py` (blob `0db67028`; 7/7, `VERDICT
   LEVEL3-CONVERSE-BOUNDED`, replay identical: a real sign automorphism, the classical lattice, graded locality,
   non-uniform sites) would add a probe path, the workflow and an exact-layer section. This draft excludes it.
6. Build and dispatch the predicted execution tree at `D`, recording the Build step, every print and every gate step.

## Stages and outcomes

C1 `controls.py`; S1 the module, import line and family; proof repairs only; S2 the result note, the candidate `E`.
**`L3-CONV-1-READ`**: `controls.py check E --freeze F` OK, three tokens printed, the exact-head run at `E` green on
every job. **`L3-CONV-1-HALTED`**: anything else (`S12`). No outcome edits the ROADMAP or a manuscript or restates
Level III as a biconditional; the H-∞ obligation (ROADMAP row P1, :70) stays OPEN; correctness bands unchanged
(consistency axis).
