# Reconstruction round KINF-SEED-1 — the sharp seed of the ball from a sharp stage test: PREREGISTRATION (draft for owner review)

**Status: research draft, not a control plane.** Written by the research thread `research/equivalence` (node E8) and
held on that branch under `research/equivalence/preregistration-drafts/` for owner review. No round is opened, no pull
request exists, nothing under `verification/` is written, no `D` is designated and no `F` exists. If the owner opens
the round, this text is copied into the record directory below on a pull request from the designated `D`; every
measurement marked *(at L)* is re-taken at `D`; `controls.py` is generated; the predicted execution tree is built and
dispatched; and this file may change in any of those steps before `F` (`G9`). Every measurement here was taken at
L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`, the head of `main` known to this thread.

```v3-round
round KINF-SEED-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-kinf-seed-1-stage-sharp-test/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-kinf-seed-1-stage-sharp-test/
record AM verification/receipts/KINF-SEED-1.json
execution A verification/lean-mathlib/OIBridge/StageSeed.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory would hold this preregistration, the round's frozen `controls.py` and the result note. **No
manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe, no landed kernel module and no other
round's record change under any outcome.**

## The objects

- **`D`** — to be designated by the owner (the head of `main` when the round opens). Drafting measurements: L.
- **`F`** — the commit carrying the frozen control plane, designated by the owner; `delta(D, F)` is the control plane.
- **`E`** — the certified execution head; **`Λ`**, **`Q`** — the reconciliation and the receipt commit (§A.39).

## What the round is

K∞-Seed (ROADMAP :1023–1024) asks for `SharpSeed (eball d) r` (OrbitGeneration.lean:65), an effect on the ball with
the value one at a state and the value zero at a state; K1's selector consumes it as `hP1` (K1Bridge.lean:128). The
round asks one question:

- **Q-SEED.** Is K∞-Seed implied by SC∞ (`SCInf`, StageCompletion.lean:78), a completion chart (`CompletionChart`,
  CompletionAction.lean:144), one stage effect with the value one at one stage preparation and zero at another, and
  any affine identification of the chart body with `eball C.d` — and, with TRB-1's identification
  (`chartBody_eq_eball`, TransitiveBody.lean:651) or KTRANS-DENSE-1's (`chartBody_eq_eball_of_dense`,
  DenseOrbit.lean:209), does the seed exist?

The earned reading of a positive cell is only this: inside K1's hypothesis list the seed is not an independent seam;
it is carried to the ball by the chart and the ball identification from one finite-stage fact, a *sharp stage test*.

## The kernel declarations the round would add (frozen surface, module `OIBridge/StageSeed.lean`)

Import: `OIBridge.DenseOrbit` only. Namespace `OIBridge.StageSeed`; `open Set KInfFoundations OrbitGeneration
OrbitNormalization StageCompletion CompletionAction TransitiveBody DenseOrbit`. Three theorems, no definition, three
`#print axioms` lines:

```lean
theorem sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D) (hSC : SCInf D)
    {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}
    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)
    (A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)) (hA : A '' chartBody C = eball C.d) :
    SharpSeed (eball C.d) (effTr A (effR C.L C.p0 (coord D ⟨i, e⟩)))
theorem exists_sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D)
    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}
    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)
    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}
    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :
    ∃ r, SharpSeed (eball C.d) r
theorem exists_sharpSeed_eball_of_stage_dense {D : DirectedStages} (C : CompletionChart D)
    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}
    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)
    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}
    (hG : PreservesBody (chartBody C) G) (hT : DenseBoundaryOrbit (chartBody C) G) :
    ∃ r, SharpSeed (eball C.d) r
```

The proofs compose landed theorems only: CMP-1's `sharpSeed_completion` (StageCompletion.lean:224), OG-1's
`sharpSeed_restrict` (OrbitNormalization.lean:427) and `sharpSeed_tr` (:242), and the two chart identifications.
**Census family** (inserted after KT4-PREM-1's position in the file, i.e. at the end of `families`): name "the sharp
seed of the ball from a sharp stage test: under SC∞ a stage effect certain at one stage preparation and zero at another
is a sharp seed of eball along the completion chart and any affine identification of the chart body with the ball
(round KINF-SEED-1, reconstruction)", `modules: ["StageSeed"]`, `status: "kernel-only"`, `manuscript: []`.
**Import line**: `import OIBridge.StageSeed` directly after `import OIBridge.RelcSelectC5` (the last line at L).

**Design-run rule.** Compilation failures may cause proof repairs; no repair may strengthen or weaken a frozen
statement. A statement mismatch found by a control returns the round to design.

## The decision rule (frozen; implemented by `controls.py verdict`)

The **effective statement** of a theorem is defined as in KTRANS-DENSE-1 (its binder groups, own binders and
conclusion, whitespace-normalized).

| Cell | Outcome | Rule |
|---|---|---|
| Q-SEED | `KINF-SEED-PROVED` | all of: the module's three theorems have exactly the frozen effective statements above; every identifier they name resolves (in the module's namespace context) to the landed declaration it resolves to at `D` (S2); the exact-head run at `E` builds the module with each of the three `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`; and the landed controls of S3 read at `D` have their frozen statements |
| Q-SEED | `KINF-SEED-NOT-ESTABLISHED` | otherwise |

The round's outcome is `KINF-SEED-1-READ` when the cell is assigned by its rule. The token printed is generated by
`controls.py verdict E` from the measurements at `E`; no token is written by hand.

## The non-inference rule (frozen)

> This round does not show that OI, StageCompletion or the observer architecture supplies a sharp stage test, a
> completion chart, SC∞, finite rank, boundary transitivity, a dense boundary orbit or any identification of the chart
> body with the ball; adopts no premise; and makes no manuscript claim. The sharp stage test — one stage effect with the
> value one at one stage preparation and zero at another — is a premise about a finite stage and is not sourced here.
> Every hypothesis of the three theorems is a hypothesis.

**Premise this round does NOT source:** the sharp stage test (`h1`, `h0`), SC∞ (`hSC`), the chart, and K∞-Trans in
either form (`hT`); the round relocates K∞-Seed onto them and proves nothing about their availability.

## The ROADMAP wording the round would license (HP-1, row K∞-Seed; not applied by the round)

At L, ROADMAP :1023–1024 reads: "**K∞-Seed** — a sharp seed, `SharpSeed`; on the completion it follows from SC∞ and a
stage effect with values one and zero at two stage preparations (`sharpSeed_completion`)." Under `KINF-SEED-PROVED` the
sentence may be extended — by the owner, or by a later round that governs `verification/ROADMAP.md` — with: "It is
carried to the ball along the completion chart and the ball's identification (`sharpSeed_eball_of_stage`), so its
remaining content is the stage-level sharp test." Under `KINF-SEED-NOT-ESTABLISHED` nothing is licensed. The status of
K∞-Seed stays OPEN under either outcome.

## The controls (in `controls.py`)

- **S1 surface.** The module's preamble (import, namespaces, `open` lines), its three theorems in order with their
  frozen signatures, and exactly three `#print axioms` lines. Mutations, each of which must fail with its code: `hSC`
  dropped; `h0` dropped (the seed becomes certain-only); `eball C.d` replaced by `chartBody C` in the conclusion of the
  first theorem; `hT` replaced by `True`; a fourth `#print axioms` line; a second import.
- **S2 resolution.** `SharpSeed`, `SCInf`, `CompletionChart`, `chartBody`, `eball`, `effTr`, `effR`, `coord`,
  `PreservesBody`, `BoundaryTransitive`, `DenseBoundaryOrbit` resolve to the landed declarations (OrbitGeneration.lean:65,
  StageCompletion.lean:78, CompletionAction.lean:144/:166, TransitiveBody.lean:518, OrbitNormalization.lean:159/:400,
  OrbitGeneration.lean:69/:79, DenseOrbit.lean:53). Mutation: a local `eball` shadowing the landed one.
- **S3 landed controls (read at `D`, not re-proved).** SC∞ is load-bearing: `not_scInf_bad : ¬ SCInf badD`
  (StageCompletion.lean:350) — a stage value that does not transfer to the completion. The zero value is load-bearing:
  `not_sharpSeed_unsharp : ¬ SharpSeed ball3 unsharpSeed` (OrbitGeneration.lean:652). Positive control:
  `bitTower_scInf` (StageCompletion.lean:401) and `bitTower_sharpSeed` (:413), the conjunct of `cmp1_core` (:425). A
  landed statement that differs at `D` fails S3 and only S3.
- **S4 phrases.** The module header and the result note contain none of: "OI supplies", "OI provides", "derived from
  OI", "sourced from OI", "K∞-Seed is discharged", "K∞-Seed is derived", "no longer needed", "premise adopted",
  "design module", "not for merge" (case-insensitive, whitespace-normalized). Mutation: "K∞-Seed is discharged." in the
  header.
- **V verdicts.** The cell yields one token by its rule; at a commit carrying the result note, the note contains exactly
  the computed token. Controls: a broken signature reads `KINF-SEED-NOT-ESTABLISHED`; a landed control differing at `D`
  reads `KINF-SEED-NOT-ESTABLISHED`; the note-token reader finds exactly the stated token.
- **I, C** as KTRANS-DENSE-1: `OIBridge.lean` is `D`'s with the one import line; the census is `D`'s with the one
  family, in `D`'s two-space JSON layout. **R, G**: the record directory holds exactly `preregistration.md`,
  `controls.py`, `result.md`; `delta(D, E)` is exactly the record paths and the three execution paths.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F`; `delta(D, F)` is the control plane only |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| every frozen theorem elaborates and is kernel-checked within the three axioms | `C3`: the dispatch run at exactly `E`, run to completion; its Mathlib bridge build and the three `#print axioms` lines |
| the module is registered and no manuscript changes | `C4`: the release gate at `E` — `lean-manuscript`, `claims`, `duplicate`, `voice`, `mirror`, `staleness` all PASS |
| the statements are the frozen ones and resolve to the landed objects | `C5`: `controls.py check E --freeze F` (S1, S2) |
| the landed controls have their frozen statements at `D` | `C5` (S3) |
| the change stays inside the governed paths | `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the result note carries exactly the computed token and no forbidden phrase | `C5` (V, S4) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q` prints `VERDICT  HOLDS`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design evidence and the predicted outputs

| run | commit | workflow run | measured |
|---|---|---|---|
| 1 | `0578b13d` (`dev-equivalence/kinf-seams`, module `EqvSeams`) | 38083220991 | Mathlib bridge build failed at one declaration of §C (`sum_mul_ehom`); §A's three theorems elaborated |
| 2 | `f5367a7a` (same branch; proof repair of `sum_mul_ehom` only) | 38083519826 | `Build completed successfully (3645 jobs)`; the three §A prints `[propext, Classical.choice, Quot.sound]`; gate `lean-axioms` OK (5875, no sorry); gate failed at `lean-manuscript` (unregistered modules) and at `claims`, `duplicate` (the branch carried the research archive) |

**Predicted outputs, generated from those measurements by the rule above:** the three frozen statements are §A of
`EqvSeams` as built in run 2, unchanged; read by the Q-SEED rule, run 2's measurements give `KINF-SEED-PROVED` for
the statement surface, and the landed controls of S3 are present at L with the frozen statements. The rules, not this
reading, are what a frozen file would fix. **Not yet measured:** the predicted execution tree (module `StageSeed`
alone, the census family, the import line, `controls.py`) at the designated `D`, which must be built and dispatched
before `F`; at L its release gate is expected to pass every step, since the census family registers the module and the
tree carries no research directory (the comparable L-based design branch of this thread, run 38090116254 for draft
S3, failed only at `lean-manuscript`, the step a family discharges).

## Stages

1. **C1** adds `controls.py` (frozen blob) to the record directory.
2. **S1** adds the module, the import line and the census family in one commit; `controls.py check S1 --freeze F`
   passes; the exact-head run at S1 is green on every job.
3. **Repairs**, if any, change theorem proofs only, each passing `controls.py check`; a failure a proof-only repair
   cannot fix halts the round.
4. **S2** adds `result.md`; this is candidate `E`; `controls.py check E --freeze F` passes; the exact-head run at `E`
   is green on every job.

## Outcomes

- **`KINF-SEED-1-READ`** — `controls.py check E --freeze F` prints `controls: OK`, `controls.py verdict E` prints one
  token for Q-SEED, and the exact-head run at `E` is green on every job. The result note states the cell in its row's
  words, the earned reading and the non-inference rule.
- **`KINF-SEED-1-HALTED`** — anything else, under the specification's `S12`; the result note names the failing check
  or job.

No outcome sources a sharp stage test, adopts a premise or edits the ROADMAP or a manuscript. Correctness bands are
unchanged by either outcome: the round is consistency-axis work.
