# Reconstruction round BG-2 — does the cited Bekir–Golomb premise hold as the kernel states it?: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #826.

- **`D`**: `3519213a47c2c63f7ece3f55a81acffc2a96a3af`, the head of `main` after #846. It is certified by push run
  38694888962.
- **`F`**: `c9f1a34dd6fb3a537a522d1bb38c26ba6f00ed4f`.
  - It is reached from `D` by six single-parent commits, each changing only the preregistration. At `F` the
    preregistration's blob is `0c72480270c31e4f784d087ace00eebe8eea2f0f`.
  - Its exact-head `workflow_dispatch` run is 38740709601, attempt 1. It concluded `success` with all 36 jobs
    succeeded, and it is `F`'s `check-run` attestation. It attests the control plane only.
  - The owner designated `F` on 2026-10-15, with the three execution blobs frozen and execution authorized through
    this stage. The designation was first given in session. Its host records came after stages 1 and 2:
    - comment 6198856734 states the designation and accepts the two stages as a recorded exception;
    - comment 6199095822 records the owner's personal confirmation of both.

    See *Execution chronology*.
- **Shape**: non-sealing, in three stages.
  - Stage 1, `0f37e5473b07a82a0ae306320b8d22722a267d95`: `controls.py`, blob `caf0dfe0`.
  - Stage 2, `cbe4f0bfa80a9c1914090f0330843ba18e6f47bc`: the module (blob `9f7ef150`), the probe (blob `905ea465`), the
    workflow shard, the import line and the census family.
  - Stage 3: this note, which supersedes the stage-3 note at `95e3246ac37b0df401f63eab02162c910979ef03`.

**Cells:** `BG-2-PREMISE-REFUTED`, `BG-2-CONTROLS-PROVED`, `BG-2-ORIENTATION-EXACT`.

**Q-REF: BG-2-PREMISE-REFUTED.**
- The module states the eight frozen declarations, in order and with their frozen signatures (S1). Its landed objects
  resolve at `D`'s blobs and lines (S2).
- `not_BGIntegerClassification : ¬ BGIntegerClassification` names the premise. Its proof applies the hypothesis at
  `6 r1 r2refl` to `hyps_r1_r2refl` and closes with `not_muForm_r1_r2refl` (S3).
- `not_muForm_r1_r2refl` takes eight of the conclusion's gap identities, which give three linear relations on
  `r1 ∘ eS`.
  - `source_difference_cases` reduces those relations to three difference patterns, by `decide +kernel` over
    `Equiv.Perm (Fin 6)`.
  - `reflected_difference_obstruction` shows that `r2refl` realizes none of them, by `decide +kernel` over the 216
    target triples.
- The exact-head run at stage 2 builds the module, and its three prints lie within
  `[propext, Classical.choice, Quot.sound]` (table below).

**Q-CTRL: BG-2-CONTROLS-PROVED.**
- `muForm_r1_r2` realizes `mu` at the printed pair `(r1, r2)` in the orientation the premise's conclusion fixes. Its
  witness is `⟨Equiv.refl _, Equiv.refl _, _⟩`, from `mu_gap`.
- `revMuForm_r1_r2refl` realizes `mu` at the instance `(r1, r2refl)` in the reversed orientation. Its witness is
  `⟨Equiv.refl _, Fin.revPerm, _⟩`.
- Both are among the frozen declarations (S1, S2), and both prints lie within the three axioms.

**Q-EXACT: BG-2-ORIENTATION-EXACT.**
- The probe at `E` is the frozen blob `905ea465`, run by `controls.py` with `python3 -I`. It prints `PASS` for
  O0–O5, K1 and K2, `checks: 8, failures: 0` and `VERDICT PREMISE-ORIENTATION-EXACT`.
- O2 and O3 give 3/0 at `---`, `-RR`, `S--` and `SRR`, and 0/3 at the four variants with one reflection. The forced-`eT`
  algorithm reproduces every count.
- O4 finds 146 eligible members of the box `p1 ≤ 7`, `p2 ≤ 29`. The signed form holds at `(X,Y)`, `(Y,X)` and
  `(RX,RY)`, and never at `(X,RY)` or `(RX,Y)`.
- O5 works at span ≤ 40.
  - It finds 760, 8406, 51394 and 75352 Golomb rulers at 3, 4, 5 and 7 marks, with no nontrivial homometric pair.
  - At six marks it finds 132914 rulers and 248 ordered pairs: 124 signed, 124 reversed, 0 neither and 0 both.
- K1 (`mu 0 2 ↔ mu 0 3`) gives no solution by either algorithm. K2 rejects `(r1, 17 − r1 ∘ rev)` and `(r1, r1 + 3)`.

The three cells are read by separate rules, and none reads another's outcome. All three are positive. The round
outcome `BG-2-READ` also requires three checks at `E`:
- `controls.py check E --freeze F`;
- the three frozen blobs at `E` (`C2`);
- the exact-head run at `E`, green on every job.

This note is part of `E`, so it does not record them. They are recorded in the candidate-`E` attestation.

The earned reading:

> `BGIntegerClassification` as stated at TurnpikeScopeTransfer.lean:542 is false: the six-mark integer rulers
> (0,1,4,10,12,17), (0,4,6,9,16,17) satisfy its hypotheses, no relabelings realize mu in the orientation its conclusion
> fixes, and the pair realizes mu reversed. `spectral_classification_of_BG` and `twoBranch_of_BGClassification` remain
> implications with refutable `hBG`.

The non-inference rule, as frozen:

> Non-inference rule: this round does not show that the 2007 classification, its exceptional family or the two-branch theorem of GR is
> false, nor that a reversed exceptional correspondence is realizable by unitary eigenbases; it refutes one formal
> statement at one instance and formalizes no classification, slice or corrected premise. The sites its outcome bears
> on — GR.md:178 and :182, LEDGER.json:2602 and :3110, ROADMAP.md:72 and :1141, PROGRAMME.md:605, the census family
> "Hamiltonian reconstruction" (lean-manuscript-census.json:144) and the scope blocks at edge_rigidity_probe.py:14676–14680,
> bohr_frequency_probe.py:10082–10085 and gap_correspondence_probe.py:953–956 — already state at `D` the unsigned premise
> refuted and reconstruction conditional on H-BG, the ledger, ROADMAP, PROGRAMME and census sites citing the design
> package landed with #842; none of them changes here. The probe is not a kernel proof.

**Premises this round does not source:**
- the 2007 classification and its scope;
- the correct form of the exceptional clause;
- the exclusion of the reversed correspondence;
- the integer-to-real passage for any corrected premise.

## Evidence at stage 2

- **Exact-head run.** Run 38752296936 is a `workflow_dispatch`, attempt 1, with `head_sha` exactly stage 2
  (`cbe4f0bf`). It concluded `success`. The API reports `total_count` 37 jobs, and all 37 are listed and succeeded.
  Pull-request run 38752298075, a synthetic merge with `main`, also succeeded. It is not an attestation.
- **Mathlib bridge, job 116481534373.**
  - The module was built fresh: `Built OIBridge.TurnpikePremiseOrientation (5.8s)`, then
    `Build completed successfully (3652 jobs)`.
  - The module raised no warning. The log has no `sorryAx`, no `Lean.ofReduceBool` and no build error line.
  - 5.8 s is lake's build time for the whole module, not the elaboration time of any one declaration.
  - The axiom reports:

    | declaration | axioms |
    | --- | --- |
    | `hyps_r1_r2refl` | `propext, Classical.choice, Quot.sound` |
    | `source_difference_cases` | `propext, Classical.choice, Quot.sound` |
    | `reflected_difference_obstruction` | `propext` |
    | `not_muForm_r1_r2refl` | `propext, Classical.choice, Quot.sound` |
    | `not_BGIntegerClassification` | `propext, Classical.choice, Quot.sound` |
    | `muForm_r1_r2` | `propext, Quot.sound` |
    | `revMuForm_r1_r2refl` | `propext, Classical.choice, Quot.sound` |

  - The release gate passed every step:
    - `lean-axioms`: 5988 named results, which is 5981 at `F` plus the round's 7, with no `sorry`;
    - `lean-manuscript`: OK;
    - `legacy-records`: 303 records in 75 closed namespaces, intact;
    - `v3-corpus`: 140 vectors;
    - `v3-receipts`: 46 receipts, all hold.
- **Shard `probes_bg2`, job 116481534630.** The probe printed the values in Q-EXACT, `checks: 8, failures: 0` and
  `VERDICT PREMISE-ORIENTATION-EXACT`. `controls.py --self-test` was OK, and every frozen mutation was rejected.
- **Other required jobs.** The Lean kernel check (job 116481534563) and the probe aggregate (job 116490507665)
  succeeded.
- **The frozen controls over the run.**
  - `controls.py check cbe4f0bf --freeze c9f1a34d` passed C1, S1, S2, S3, S4 and G. G found 7 paths; BG-1's directory
    and the legacy manifest are untouched.
  - `controls.py verdict cbe4f0bf --freeze c9f1a34d --axioms <job 116481534373's log>` read all seven reports. It
    printed the three tokens above and the earned reading.

## Execution chronology (executor's record)

- **14:01:53 UTC.** The candidate-`F` exact-head attestation was posted: comment 6193930438 on #826. It is not a
  designation.
- **Between 14:18:40 and 14:30:17 UTC.** The owner designated `F` and authorized execution through stage 3, in the
  owner's working session with the executor. No designation of `F` was on the host at that time.
- **14:30:17 and 14:30:35 UTC.** Stages 1 and 2 were committed.
- **About 14:31 UTC.** Stages 1 and 2 were pushed to `draft/bg-2`.
- **14:32:21 UTC.** The stage-2 exact-head run was dispatched.
- **18:03:44 UTC.** The designation of `F` and the exception were posted on #826, in comment 6198856734.
- **About 18:04 UTC.** The first stage-3 commit, `95e3246a`, was pushed as candidate `E`, and its exact-head run
  38782670851 was dispatched.
- **About 18:14 UTC.** The owner personally confirmed the designation and the exception, in comment 6199095822.
- **After that.** This note superseded the one at `95e3246a`, whose provenance sentence overstated the authorship of
  comment 6198856734.

§A.39 and the specification's `S2` require the owner's designation of `F` before execution begins. Stages 1 and 2
preceded any host record of that designation. Stage 1's commit message says it was made "under the owner's F
designation". That refers to the in-session designation; no host record existed then. No commit has been rewritten.

**The recorded exception.**
- **The designation and the exception.** Comment 6198856734 states both. It was posted at 18:03:44 UTC, after stages
  1 and 2 were executed.
- **Who wrote what.** A reviewer whose analysis the owner relayed into the session drafted the comment's text. The
  executor posted it verbatim at the owner's request. Comment 6199081087 corrects the comment's own provenance line on
  this point.
- **The owner's confirmation.** The owner personally confirmed the designation and the exception at about 18:14 UTC.
  The executor recorded the confirmation at the owner's request, in comment 6199095822, quoting the owner's words.
- **What the exception accepts.** Stages 1 and 2 are retained as a recorded exception to §A.39's requirement that
  designation precede execution.
- The exception does not change the chronology above, and it does not establish that the requirement was satisfied.
- The V3 verifier reads no attestation (`G8`, `S5`). So a later `VERDICT HOLDS` on this round's receipt carries no
  evidence about the order of the designation and the execution.
- Every later round keeps the requirement in full.

## Execution notes

- **Blob identity.** The three frozen blobs are present at stage 1 (`controls.py`) and at stage 2 (all three), checked
  with `git rev-parse`. Stage 2's tree differs from the tested predicted tree `7608a838` only in the preregistration,
  which is the version at `F`.
- **The self-test at stage 1.** `controls.py --self-test` reads the module, which stage 2 adds, so it cannot run at
  stage 1. The preregistration requires it at `E` (`C2`). At stage 2 it is OK locally.
- **Legacy records.** `tools/legacy_records_check.py` reports 303 records in 75 closed namespaces, intact, at stage 1
  and at stage 2.
- **Execution status.**
  - *Mathematical execution:* no deviation from the frozen proof, probe or control design, and no proof repair.
  - *Governance execution:* a recorded exception to the designation-before-execution chronology, expressly
    acknowledged by the owner (*Execution chronology*). It is not strict compliance with §A.39.

**Scope.** BG-2 certifies the refutation of the premise as the kernel states it, and its controls. It changes no
landed module, manuscript, ROADMAP or BG-1 record. Three pieces of work are separate and governed on their own:
- correcting `TurnpikeScopeTransfer.lean`;
- the signed repair;
- replacing the design-package citations.
