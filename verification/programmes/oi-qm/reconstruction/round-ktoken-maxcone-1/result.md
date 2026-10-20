# Reconstruction round KTOKEN-MAXCONE-1 — the conditional pair-cone theorem for k tokens: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #829. This note is stage 3, candidate `E`. `E`
is not designated.

- **`D`**: `b96662e6be4f537502c772db369ea32a35b213a8`.
- **`F`**: `e12c1573dc1605baf6ed299f9fe11cdb31ef56ee`, a single-parent child of `D` that adds only the
  preregistration. At `F` the preregistration's blob is `ffbcab2918a4e1e7594f7ab4b827b70bb25b9f9f`.
  - Its exact-head `workflow_dispatch` run is 39163559807, attempt 1. It concluded `success`, every job succeeded,
    and it is `F`'s `check-run` attestation. It attests the control plane only: `F`'s tree holds none of the round's
    execution files.
  - The owner designated `F` in comment 6255241760 on #829, created 2026-10-18T21:16:05Z. The comment authorizes
    recording the designation and preparing the execution stages from exactly `F`. It does not authorize `E`'s
    execution, `Q`, merging, archive promotion or publication of pending expected-result evidence. At
    2026-10-18T21:33:30Z the owner edited one row of it, the release-gate count, from 23/23 to 22/22.
    `evidence/f-run/designation.json` holds the comment as first captured; `evidence/f-run/index.json` records the
    edit.
- **Shape**: non-sealing, in three stages, each a single-parent child of the one before.
  - Stage 1, `86eb9d49a919570d4179212f438bcb308c8ea176`: `controls.py` (blob `7c9672a1`), the two pinned evidence
    files and `evidence/f-run/`.
  - Stage 2, `7ce49dd18f86e5ddce9e54fba56469ea722ca537`: the module (blob `14bb9fc0`), the probe (blob `04580c51`),
    `checks/KTokenPairCheck.lean` (blob `354bd7ce`) and `checks/run_checks.py` (blob `dc6c77d1`); `verify.yml`
    (blob `72d698f3`) with the six frozen splices; the import line; the census family.
  - Stage 3: this note.

## The cells

The four cells and their rules are frozen in the preregistration (*The decision rules*):

| Cell | Positive token |
|---|---|
| Q-INCL | `KTOKEN-MAXCONE-INCLUSIONS-PROVED` |
| Q-EQ | `KTOKEN-MAXCONE-EQ-PROVED` |
| Q-PAIR | `KTOKEN-MAXCONE-PAIR-RECOVERED` |
| Q-EXACT | `KTOKEN-MAXCONE-K3-EXACT` |

The tokens are printed by `controls.py verdict E --freeze F --axioms <E's exact-head bridge log>`. Q-INCL, Q-EQ and
Q-PAIR read the 68 axiom reports of `OIBridge/KTokenMaxCone.lean`, the absence line and check A3's final line from
that log. Q-EXACT re-runs the probe blob at `E`. The round outcome `KTOKEN-MAXCONE-1-READ` also requires
`controls.py check E --freeze F`, the five frozen blobs at `E` (`C2`) and the exact-head run at `E` green on every
job.

This note is part of `E`, so it records none of these measurements and no cell token. They are recorded in `E`'s
retained expected result (§A.42 item 2) and in the receipt's candidate entry for `E`.

## What `E` carries

The module states, for every `k` and every `K ⊆ WK k`:
- `subset_QK_of_maxCone_drive`: `K ⊆ QK k` from hmax (`K ⊆ maxConeK (eball 3)`), hH2 (`cnotK i j` invariance for
  `i < j`) and hA (`actK j (rotLin t)` and `actK j cycEquiv` invariance for `(j : ℕ) ≠ 0`);
- `QK_subset_of_products_cone_drive`: `QK k ⊆ K` from hH1 (products of `eball 3` states), hadd, hsmul, hH2 and hA;
- `kCone_eq_QK_of_drive_maxCone`: `K = QK k` under all six hypotheses;
- `kCone_eq_QK_iff_drive_maxCone`: with hH1, hadd, hsmul and hmax fixed, `K = QK k` holds exactly when hH2 and hA
  hold. Its directional witnesses are `driveInvariantK_of_eq_QK` (`K = QK k` gives hH2 and hA) and
  `kCone_eq_QK_of_drive_maxCone` (hH2 and hA, with the four fixed hypotheses, give `K = QK k`). The equivalence is
  stated only relative to the four fixed hypotheses;
- `pairCone_eq_Q3_of_kToken`: at `k = 2`, through `pairCarrierEquiv`, the statement of
  `pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153–160). The module does not import `OIBridge.EqvK2MaxCone`.
  Check A3 compares the two statements and the recovery's used constants at the level of kernel terms; it is a
  meta-level check, not a Lean kernel proof.

These are statements of the frozen surface; whether `E` proves them within `[propext, Classical.choice, Quot.sound]`
is read from `E`'s exact-head run, as above.

The probe at `E` is the frozen blob `04580c51`: exact arithmetic over Q(i) at `k = 3`, with the countercontrols and
written family arguments listed in the preregistration (*The exact layer*). Finite witnesses are not universal
statements.

## Design evidence

The preregistration pins the expected results of two design runs, retained as `evidence/run1-39043849411.json` and
`evidence/run2.json`. Both runs built the module, probe and check-file blobs frozen at `F`. In each:
- every job succeeded (38 jobs);
- the build succeeded and the release gate passed 22 of 22 steps;
- the module's 68 `#print axioms` reports each lie within `[propext, Classical.choice, Quot.sound]`, with no
  `sorryAx`, `Lean.ofReduceBool` or `sorry` marker;
- the absence line is present and check A3's final line is `A3-CHECK-NONVACUOUS: 13 cases as expected`, with its
  eleven mutations failing;
- the probe printed `checks: 3196, failures: 0`, rejected its five mutations and printed `VERDICT KTOKEN-K3-EXACT`.

Run 2 also ran `controls.py --self-test`, at the earlier blob `8c8eb522`. The frozen `controls.py` blob `7c9672a1`
has been exercised by no design run and by no exact-head run. The design runs are evidence for the predicted tree,
not `check-run` attestations of `F` or `E`, and they stand in for no check the preregistration assigns to `E`.

## The non-inference rule, as frozen

> Non-inference rule: this round sources none of its hypotheses: not the products in K, the cone closure, the maxCone
> bound (product-test validity on an actual k-token cone), or the CNOT and rotation/cyclic invariance (the open
> compatibility premise A_miss with its gate part). The k-token carrier and Pauli dictionary are coordinate
> constructions carrying multi-token local tomography as a premise, not a field-neutral k-token dictionary from OI; the
> maxCone bound is not derived from IE₂, FCC or a composition principle. No Kn claim is made: state cones on qubit-power
> carriers say nothing about other sizes, the operational repertoire or drivability, and would combine with a descent
> from qubit-power carriers (KN-DESC-1, a draft) only through a map to operational carriers and a drivability source,
> neither supplied here. Invariance under every unitary is not shown. The probe is an exact computation and check A3 a
> meta-level check over kernel terms; neither is a Lean kernel proof, and finite witnesses are not universal statements.

**Premises this round does not source:**
- hH1, hadd, hsmul, hmax, hH2 and hA for any physical k-token cone;
- the k-token carrier (multi-token local tomography);
- the drive source, K∞-Trans and K∞-Geom;
- test validity; the sharp-test reduction `maxCone_bound_of_sharp_available` (EqvK2MaxCone.lean:194) is pair-level;
- IE₂ and FCC.

The earned reading is the preregistration's and applies only under `KTOKEN-MAXCONE-1-READ` with all four cells
positive.

## Execution notes

- **Blob identity.** The five frozen blobs are present at stage 2 (`controls.py` from stage 1), checked with
  `git rev-parse`. No frozen blob differs, and no proof, probe or control was repaired.
- **The tested tree.** Stage 2's tree differs from design run 2's tree (`6959ced4`) only in `controls.py`
  (`8c8eb522` there, the frozen `7c9672a1` here), in the preregistration, which is the version at `F`, and in the
  evidence files. `E` adds this note.
- **`F`'s run record.** `evidence/f-run/results.json` is read from a partial window of the bridge job's log
  (job 117781736738): original lines 33628–38627 of 38627. In that window the build succeeded, the release gate
  passed 22 of 22 steps, `OIBridge.lean`'s 19 axiom reports are complete and within the three axioms, and no failure
  marker appears. The axiom reports and failure markers of original lines 1–33627 were not read; `index.json`
  lists both as missing. For those lines the record carries only the release gate's own `lean-axioms` summary.
- **Pull-request run.** Run 39244307297 on stage 2 is a `pull_request` run of a synthetic merge with `main`. It
  succeeded. It is not an attestation.
- **Legacy records.** The round changes no file listed in `verification/infrastructure/legacy-records.json`.

**Scope.** The round adds one kernel module, one probe, one census family (`kernel-only`, `manuscript: []`), one
import line and one workflow shard with check A3's step. It changes no landed module, manuscript, built artifact,
`verification/ROADMAP.md` or other round's record. The ROADMAP K2 wording in the preregistration is licensed only
under `KTOKEN-MAXCONE-1-READ` with all four cells positive, and it is not applied by this round. K2 and Kₙ remain
open. Correctness bands are unchanged (consistency axis).
