# Verifier round V3-13 — retirement: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #744. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/V3-13.json`, and on the pull request.

- **`D`** — `f9a9acaa44e4982d7814200c46bf1da222b4cbfc`, the head of `main` after `V3-12`'s landing,
  certified by push run 36149801375.
- **`F`** — `d6fa4c6371f56575b6a55c61029a2d073a158478`, whose only parent is `D` and which adds the
  preregistration alone, blob `11e4302066bad73eb770f60f5ed13ee488c5e530`.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or `V2` certificate.

| target | outcome at `E` | predicted |
|---|---|---|
| `V313-0` | `F-DESIGNATED` | the same, strong |
| `V313-1` | `GUARD-RETIRED` | the same, strong |
| `V313-2` | `AUTHORITY-SWAPPED` | the same, strong |
| `V313-3` | `VERIFIER-SETTLED` | the same, strong |

`V313-4` to `V313-6` are measured at or after `E` and recorded in the receipt and on the pull
request.

***

## `V313-0` — `F`: F-DESIGNATED

The branch was held at `F` and the workflow dispatched on it. Run 36164944152 is a
`workflow_dispatch` run whose `head_sha` is `F`, and all six of its jobs are green: the guard
reports 105 PASS and 0 FAIL, with its verdict map identical to `D`'s, tag for tag and in order; the
release gate passes, `V2` authoritative OK with 0 failures and `v3-receipts` holding on three
receipts. That run is `F`'s `check-run` attestation, recorded on the pull request in comment
5836680118. The owner then designated `F` in comment 5836716920, which is `F`'s
`owner-designation` attestation.

***

## The execution

Each stage commit took its expected blobs from the preregistration as it stands at `F` and refused
on any mismatch. Each commit has exactly one parent.

| stage | commit | what it does |
|---|---|---|
| 1 | `cc90082cfbe9dbfe6f84c30d154f189e336d0d75` | adds `retire.py`, `messages.json`, `headers.json` and `controls.py` to the record directory |
| 2 | `0811754da89dd5e3674ec913c0c89a24462a88fd` | the guard, written by `retire.py` |
| 3 | `f1dabfb32d60c753b5916470873ab6239cbb21e8` | `legacy-records` in; `V2`, the control-plane tools and the diagnostics job out; `v3-self-test` and `v3-corpus` in; the depth-1 probes checkout |
| 4 | `d658231fdc54593d4d0aafdffed9705ea1d1071d` | the verifier, its corpus and the specification |
| 5 | `dc9f08a076e09c137ac0a61191a02bed3bb839c4` | `AGENTS.md` and `verification/README.md` |

Every one of the nineteen stage files has its frozen blob. This note, whose only parent is the
stage 5 commit, is `E`.

***

## `V313-1` — the guard: GUARD-RETIRED

- **`C1`:** the four record-directory files have their frozen blobs; `controls.py --self-test`
  prints `controls: self-test OK`.
- **`C2`:** `retire.py`, run at the stage 1 commit under CPython 3.11.15, printed
  `1616 predicates retired, 1610 as the census classes them and 6 by the amendment; 2486 retained`,
  `structural rows: 15 removed with the emptied checks, 85 kept`, `91 checks remain` with the 14
  emptied checks named, and `retained predicates missing: 0`. The guard has blob
  `d1c6bf660958f870b9e9c8e3d07fe6935ba5f824`, 14,792 lines, and compiles.
- **The history control:** `controls.py history` reports 56 files run by the probes job, all 56
  named, with 213 history sites at `D` and 0 at stage 2.
- **The amendment's controls**, at their frozen outcomes:
  - `controls.py pc4s . D`: the four `R7-PC4S` rows hold; 35 files read, 34 of them legacy
    records (every record under `verification/seals/`) and `verification/migration-manifest.json`
    as a lookup; one directory listed, `verification/seals`, a closed namespace; a one-byte change
    to `verification/seals/PC4.json` makes line 17854 fail.
  - `controls.py vacuity . <stage 2> D`: in the 1,610 transformation the strings `N15` and `N14`
    seek occur 0 times outside their definitions, and both hold on the guard, with those strings
    removed outside them, and on their definitions alone; the three countercontrols fail. At `D`
    the strings occurred outside the definitions 10 times and once, and the same evaluations hold,
    as the preregistration records.

## `V313-2` — the authority: AUTHORITY-SWAPPED

- **`C3`:** the four stage 3 files have their frozen blobs, and the manifest's blob at stage 3,
  `9e48bd31797e1673f03807e699a10ae4a0b960c7`, is `V3-12`'s. `legacy_records_check.py` reports
  `303 record(s) in 75 closed namespace(s), all intact` at stage 3 and `manifest-absent` at stage 2.
  The same commit deletes `tools/certificate_verifier.py`, `tools/control_plane_base_check.py`,
  `tools/control_plane_lint.py` and the 90 files of `verification/certificates/conformance/`.
  `controls.py callers` reports 0 at stage 3; the V3 self-test passes and the corpus reports
  `135 vector(s), exact and as expected`.

## `V313-3` — the verifier: VERIFIER-SETTLED

- **`C4`:** the eight stage 4 files have their frozen blobs; the V3 self-test passes; the corpus
  reports `140 vector(s), exact and as expected`; `controls.py callers` reports 0, with
  `ATTESTATION_DIR`, `AXES`, `SETTLED`, `_axis`, `_strong`, `_v3only` and `project` removed.
- **`C5`:** the two stage 5 files have their frozen blobs.

***

## Checks up to `E`

- **`C6`:** `--receipts` holds on three receipts at each of the five stage commits;
  `legacy_records_check.py` passes at stages 3, 4 and 5.
- **`C7`:** `git diff --no-renames --name-status D <stage 5>` lists 114 paths — 13 added, 7
  modified, 94 deleted — each governed by the block at `F` with its change authorized, and none a
  record of the legacy-records manifest. This note adds one more path under the record directory.
- **`C9`:** `verification/README.md` keeps every string literal of the stage 2 guard it carried at
  `D`, the anchor "`.github/workflows/verify.yml` runs" among them, and the slices `R7-A6P` and
  `R7-A6I` scan carry no over-reading by those checks' own scanner functions;
  `.github/workflows/verify.yml` keeps `repertoire_lie` and has no `lake build OIBridge.` or
  `lake env lean OIBridge/` line; `AGENTS.md` keeps the §A.35 heading and "updates the registry in
  the same commit"; `tools/release_gate.py` keeps `"lean-manuscript"`.
- At stage 5, `duplicate_check`, `claims_check`, `artifact_placement_check`,
  `baseline_label_check`, `ci_gate_presence_test` and `voice_scope_test` pass.

`C8`, the dispatch run at `E`, and `C10`, the receipt commit, follow this note.

The scripts that applied the stages, rehearsed the round and checked the README slices, none of
which is landed:

| script | SHA-256 |
|---|---|
| `exec313.py` (applies the five stages, reading every blob back from the preregistration at `F`) | `7782d082c7ae546f7d9e0c581c6d2654e3611e88b76ca6ab9dbab48969c9d84b` |
| `sim313.py` (the drafting-time rehearsal, 85 of 85 as predicted) | `e47c2678f84d7a5dfcd8265f01dc5dcf203e793b8f7791fab8264e1a47c6a2bd` |
| `readme_control.py` (the `R7-A6P` and `R7-A6I` scanners, extracted from the guard) | `257129b0e9c973fc630faa458956056cd248a3b05b3a04975417f79562f62093` |

***

## Discrepancies

None against the freeze.
