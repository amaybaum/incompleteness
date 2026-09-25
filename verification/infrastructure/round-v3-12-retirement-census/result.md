# Verifier round V3-12 — retirement census: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #743. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/V3-12.json`, and on the pull request.

- **`D`** — `81150851f84c8aa1df71dc69013a6ca6f6d71b51`, the head of `main` after `V3-11`'s landing,
  certified by push run 36125130929 with all six jobs green.
- **`F`** — `4b506738d80125d5083032ede21088a13e28aca4`, whose only parent is `D` and which adds the
  preregistration alone, blob `2fe79e4b1ac42222bd2da50f619507cad7f65cea`.
- **Shape** — non-sealing and record-only: no execution path, guard clause, seal, manifest record
  or `V2` certificate.

| target | outcome at `E` | predicted |
|---|---|---|
| `V312-0` | `F-DESIGNATED` | the same, strong |
| `V312-1` | `TOOL-LANDED` | the same, strong |
| `V312-2` | `CENSUS-REPRODUCED` | the same, strong |

`V312-3` to `V312-5` are measured at or after `E` and recorded in the receipt and on the pull
request.

***

## `V312-0` — `F`: F-DESIGNATED

The branch was held at `F` and the workflow dispatched on it. Run 36135049153 is a
`workflow_dispatch` run whose `head_sha` is `F`, and all six of its jobs are green: the guard
reports 105 PASS and 0 FAIL, with its top-level verdict map identical to `D`'s; the release gate
passes 20 of 20, `V2` authoritative OK with 0 failures and `v3-receipts` holding on two receipts.
That run is `F`'s `check-run` attestation, recorded on the pull request in comment 5833158342. The
owner then designated `F` in comment 5833297294, which is `F`'s `owner-designation` attestation.

***

## The execution

Each stage commit took its expected values from the preregistration as it stands at `F` and
refused on any mismatch. Each commit has exactly one parent.

| stage | commit | path | blob |
|---|---|---|---|
| 1 | `69ced7cebf88af8201b538cabfa3782d7192f117` | `census.py` | `54beb708bb52825ff60c476d49f4c71d3a3be609` |
| 2 | `ca72dd83c12d0290df6c5fc1dc6b13df19ae0289` | `census.json` | `a39ddc49eaa7a9527e052e30e40a8f2cdd5712c8` |
| 2 | | `legacy-records.json` | `9e48bd31797e1673f03807e699a10ae4a0b960c7` |

The paths are in the record directory. This note, whose only parent is the stage 2 commit, is `E`.

***

## `V312-1` — the tool: TOOL-LANDED

- **`C1`:** `census.py` has blob `54beb708bb52825ff60c476d49f4c71d3a3be609` and SHA-256
  `77ba82e4996e115da206269e1d60faa36d9e43b65d9aa2a85506a2c1607eee38`, the frozen content.
- **`C2`:** `census.py --self-test` prints `SELF-TEST  28 predicates, all as expected`.

***

## `V312-2` — the census: CENSUS-REPRODUCED

- **`C3`:** `python3 census.py . 81150851f84c8aa1df71dc69013a6ca6f6d71b51
  verification/infrastructure/round-v3-12-retirement-census/`, run at the stage 1 commit under
  CPython 3.11.15, wrote `census.json` with blob `a39ddc49eaa7a9527e052e30e40a8f2cdd5712c8` and
  `legacy-records.json` with blob `9e48bd31797e1673f03807e699a10ae4a0b960c7`, the predicted blobs.
  A second run into a scratch directory gave the same bytes.
- **`C4`:** `census.json` reports 4,202 predicates over 105 checks — 2,492 `retain`, 1,268
  `redundant`, 291 `retire-history`, 49 `retire-machinery`, 2 `retire-whole` and 100
  `structural` — with 50 checks retained whole, 41 split and 14 emptied, 4,199 accumulator writes
  and 199 agreeing V2 pins. `legacy-records.json` holds 303 records in 75 closed namespaces.

***

## Scope and unchanged state up to `E`

`git diff --no-renames --name-status D E`:

| status | path |
|---|---|
| `A` | `verification/infrastructure/round-v3-12-retirement-census/census.json` |
| `A` | `verification/infrastructure/round-v3-12-retirement-census/census.py` |
| `A` | `verification/infrastructure/round-v3-12-retirement-census/legacy-records.json` |
| `A` | `verification/infrastructure/round-v3-12-retirement-census/preregistration.md` |
| `A` | `verification/infrastructure/round-v3-12-retirement-census/result.md` |

Every path is an addition under the record directory. At `E` the preregistration keeps its `F`
blob, and every file outside the record directory keeps its `D` blob.

The scripts that applied the stages, rehearsed the round and ran the tool's mutants, none of which
is landed:

| script | SHA-256 |
|---|---|
| `exec312.py` (applies the two stages, reading every value back from the preregistration at `F`) | `ebe75ad726bb8dc3c80f2ea069fe1ef92638ac68c7b31a206804decde0c17ca6` |
| `sim312.py` (the drafting-time rehearsal) | `e3faf7935c9c78a4b4311d3d92b4a602b99d15bb953301a632a1b5a5e8d57f0e` |
| `mutants312.py` (the fourteen mutants of `census.py`, all rejected by its self-test) | `7ff5b4c894e1c0b97cebc9434d15148284a539131636c088500e0e55224f3fad` |

***

## Discrepancies

None against the freeze.
