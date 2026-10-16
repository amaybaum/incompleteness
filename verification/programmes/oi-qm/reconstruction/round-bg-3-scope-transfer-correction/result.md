# Reconstruction round BG-3 — the scope-transfer module after the premise refutation: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #849.

- **`D`**: `e3ad5d7a71910ce5413ef6dacd25bf5a63d5a1e0`, the head of `main` after #826. It is certified by push run
  38800143579.
- **`F`**: `777ddf8dcada759b5f3bcab26a4ff3833ba720bf`.
  - It is reached from `D` by five single-parent commits, each changing only the preregistration. At `F` the
    preregistration's blob is `0eed851b670d3c913c37ae022a864fa920a0ffc0`.
  - Its exact-head `workflow_dispatch` run is 38854027737, attempt 1, on the round branch held at `F`. It concluded
    `success` with all 37 jobs succeeded, and it is `F`'s `check-run` attestation. It attests the control plane only.
  - The owner approved `F` at this SHA in the working session on 2026-10-16 and instructed that the designation be
    recorded at it. The record is comment 6208713192 on #849, posted after the check run concluded and before stage 1.
- **Shape**: non-sealing, in three stages, pushed together.
  - Stage 1, `c5c3abb9166260ebdacedfd62d366c0e26f21ece`: `controls.py` (blob `52b52095`) and `edit-ledger.json` (blob `1e82e5a6`).
  - Stage 2, `409acead450c8a390111d4233b414b473db16ae8`: `TurnpikeScopeTransfer.lean` (blob `6c2e3e33`) and `ROADMAP.md` (blob `3209f8b0`).
  - Stage 3: this note, candidate `E`.

**Cells and how they are read.** Q-RED, Q-PRES and Q-DOC are read from the tree at `E` by `controls.py`. Q-KER is read
from the saved tail of `E`'s exact-head Mathlib bridge log. The round outcome `BG-3-READ` also requires
`controls.py check E --freeze F`, the exact-head run at `E` green on every job (`C3`), `C-FRESH`, `C-ORDER` and `C-DES`
at `E`. This note is part of `E`, so it does not record them; they are recorded in the candidate-`E` attestation on
#849.

**Measured at stage 2, before this note.**
- `controls.py check 409acead450c8a390111d4233b414b473db16ae8 --freeze F`: C1, C2, L0, L, P, R, S and G pass. The two governed files are the edit ledger
  applied to `D`, byte for byte; no statement of the module changes; `real_to_integer_surrogate` is the one new
  declaration; and no excluded phrase occurs in the module.
- `controls.py --self-test` at stage 1: every case passes.
- `legacy_records_check.py` at stages 1 and 2: 303 records intact.

**`C-FRESH`.** The round branch's `verify.yml` runs before `E`'s are:
- the pull-request runs 38808971016 (`7c221e98`), 38818676319 (`f33b2fa2`) and 38850767708 (`777ddf8d`), which test
  synthetic merges in the pull request's own cache scope, which a run on the branch cannot restore;
- `F`'s check run 38854027737, at a commit whose OIBridge sources are `D`'s. Its build cache restored on an exact
  primary-key hit (`oibridge-Linux-324962b2…-68dd7c1c…`) and saved none ("Cache hit occurred on the primary key …, not
  saving cache").

So no run on the branch has saved a build cache, and `E`'s exact-head run restores `main`'s. No run is dispatched
between `F`'s check run and the push of the three stages.

The non-inference rule, as frozen:

> Non-inference rule: this round proves no classification, adopts no sign-aware classification, and discharges no
> hypothesis; `real_to_integer_surrogate` restates a reduction the adopted proof already carried, and assumes no
> classification. The round does not show the published classification false, nor a physical reconstruction theorem;
> it does not change the status of the two-branch theorem, which `papers/GR.md` §3.3 states conditional on H-BG, nor
> of any ledger, census or manuscript site; and it does not retire the design package. It leaves
> `CongruentReconstruction.lean`'s docstrings as they are; their correction is a separate round.

**Premises this round does not source:** the published classification and its comparison with any formal premise; the
sign-aware classification; the exclusion of the reversed correspondence in the adopted library.

The earned reading is printed by `controls.py verdict` over `E`'s bridge log exactly when all four cells are positive.
It is recorded, with the tokens, in the candidate-`E` attestation.

No manuscript, census entry, probe, workflow, `CongruentReconstruction.lean`, BG-2 record or file of the design package
changes. Correctness bands are unchanged (consistency axis).
