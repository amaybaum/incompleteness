# Reconstruction round KINF-1 — the field-neutral foundations of the pre-quantum completion: RESULT (halted)

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #773. **The round halted under
the specification's `S12`**, on a freeze failure in the frozen definitions (Hazard 5 of the
preregistration): two frozen predicates do not mean what the preregistration says they mean, and a
definition frozen whole cannot be repaired inside the round. No `E` was designated, and the
withdrawal commit `W` restores every execution path to its state at `F`. This note is part of `W`.
The reconciliation and the verdict on the receipt commit are recorded in the receipt,
`verification/receipts/KINF-1.json`, and on the pull request.

- **`D`** — `98f5f08bad2d02aba00b9cfce51538c5e890cc18`, the head of `main` after round NB-1's landing,
  certified by push run 36754815367.
- **`F`** — `0f6092505e3071f4f903042d2bb20f67f659aaaf`, whose only parent is `D` and which adds the
  preregistration alone, blob `5630f1f595679673784b1d433dbf59e33d9b0140`. Its exact-head
  `workflow_dispatch` run 36772881017 concluded `success` with all 31 jobs succeeded and none
  cancelled (release gate 21 of 21, `lean-axioms` 5288 named results and no sorry, twenty receipts
  holding, the 303 legacy records intact); that run is `F`'s `check-run` attestation. The owner
  designated `F` in pull-request comment 5919730077, `F`'s `owner-designation` attestation.
- **Shape** — non-sealing, halted with one execution commit.

**Outcome:** none of the two frozen labels. `KINF-1-FOUNDATIONS-PROVED` was not measured, since no
`E` exists; `KINF-1-UNDECIDED` does not apply, since the halt is a freeze failure and not an
unobtained verdict. The preregistered prediction, `KINF-1-FOUNDATIONS-PROVED` at strength *very
high*, is recorded as **not tested**: the round did not reach the measurement.

***

## The freeze failure

The preregistration describes the family `avail` as *the round's stand-in for the effects the
completion makes available*, and `fullEffects Ω` as *every affine functional that is an effect on
`Ω`*. Under that reading the constant functional `1` belongs to `fullEffects Ω`, and to any physical
effect family, since the unit effect is an effect on every body. The two frozen predicates then
read as follows, on any body `Ω` with at least two states:

- `SupportingEffectComplete Ω avail` — *every frontier point of `Ω` is certain for some available
  effect* — **holds for every `Ω`** as soon as the unit is available, since the unit is certain
  everywhere. The condition selects nothing.
- `SingletonFaces Ω avail` — *every available effect is certain on at most one state* — **fails for
  every `Ω`** as soon as the unit is available, since the unit's certain face is all of `Ω`. The
  condition excludes everything.

Consequently `KInf1 Ω (fullEffects Ω)` is trivially true, `strictConvex_of_supporting_singleton`
with `avail = fullEffects Ω` is vacuous on every body with two states, and the preregistration's
statement that the 3-ball control shows *singleton faces hold* is not a statement about the frozen
predicate: the probe checks that one rank-one effect has a singleton certain face, which is true,
while `SingletonFaces Ω (fullEffects Ω)` is false for the Bloch ball as for every other body. The
torus and Stiefel instances fail the frozen `SingletonFaces` for the same trivial reason before the
flat faces they were chosen to exhibit are reached.

The frozen definitions elaborate, and every frozen theorem is true as stated: Lemma C is a correct
theorem about a family `avail` that excludes the unit. The failure is semantic. The vocabulary
the round exists to fix does not carry the meaning the preregistration assigns it, and the
definitions `SupportingEffectComplete`, `SingletonFaces` and `KInf1` are frozen whole under
Hazard 5, so the round cannot correct them and reach a valid `E`. The status rule's freeze-failure
clause applies: the round halts under `S12`, and the correction is a new round.

**What is unaffected.** `FiniteStage` and its lemmas, `IsEffectOn`, `certainFace`, `fullEffects`
as a set, `PerfectlyDistinguishable`, `CentrallySymmetric`, `ElementaryDrivability`, `CopyNatural`,
Lemma D (`card_le_two_of_centrallySymmetric`, `…_full`), Lemma B
(`eq_closedBall_of_frontier_subset_sphere`), `exposedPoints` and the finite-preparation bound,
Theorem F2 (`classical_exposed_ncard_le`) and `qubit_certain_face` do not mention (SEC) or (SF)
and carry the meaning the preregistration gives them. The design runs recorded in the
preregistration remain evidence that these elaborate and are kernel-checked within the three
axioms; none of that is a result of this round.

**The repair, for the successor round.** Distinguish proper effects from the unit: an effect `e`
is proper on `Ω` when some `y ∈ Ω` has `e y < 1`. Supporting-effect completeness then requires a
proper available effect certain at each frontier point, and singleton faces constrain the certain
faces of proper available effects only. Under those definitions the unit may remain available, the
3-ball satisfies (SF) with the full effects, the torus and Stiefel orbitopes fail it at their flat
faces and not at the unit, and Lemma C's proof goes through unchanged, since the effect it obtains
from (SEC) is proper. The successor round freezes those definitions and re-derives the affected
statements; it is a new native round with its own preregistration.

***

## The execution

| commit | content | run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `0f609250` | the preregistration, blob `5630f1f5` | 36772881017 | `success`, all 31 jobs |
| `c6081c10` | stage 1: `controls.py` (`3086fafb`), the probe (`3c1adfe7`), the workflow shard (`d66dc30d`) | {{S1_RUN}} | {{S1_CONCLUSION}} |
| `W` | this note; the probe removed and the workflow restored to `D`'s blob `df249b7c`, so every execution path is at its state at `F`; `controls.py` stays, being a record path | — | — |

Checkpoint `C1` held: the preregistration's blob at `F` is `5630f1f5`. `controls.py --self-test`
printed `controls: self-test OK` at the stage 1 commit. Stage 2 was not created: the failure was
found in owner review after stage 1 was dispatched and before any Lean text entered the round. The
stage 1 run was left to finish and is recorded above; the commit is listed in the receipt as a
candidate and nowhere else.

## What stays open

- Everything the preregistration named as open: field-neutral drivability (K∞-R), sharp supporting
  effects beyond the matrix level (K∞-1), singleton faces (SF) and copy naturality; none is
  discharged by anything here.
- The corrected vocabulary, and the lemmas about it, await the successor round.
