# Verifier round V3-13 — retirement: RESULT (halted)

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #744. **The round halted under
the specification's `S12`**: the execution head `E` failed checkpoint `C8` for a cause inside the
round's own paths, so no `E` was designated, and the withdrawal commit `W` restores every execution
path to its state at `F`. This note is part of `W`. The reconciliation and the verdict on the
receipt commit are recorded in the receipt, `verification/receipts/V3-13.json`, and on the pull
request.

- **`D`** — `f9a9acaa44e4982d7814200c46bf1da222b4cbfc`, the head of `main` after `V3-12`'s landing,
  certified by push run 36149801375.
- **`F`** — `d6fa4c6371f56575b6a55c61029a2d073a158478`, whose only parent is `D` and which adds the
  preregistration alone, blob `11e4302066bad73eb770f60f5ed13ee488c5e530`.
- **Shape** — non-sealing, halted with execution commits.

| target | outcome | predicted |
|---|---|---|
| `V313-0` | `F-DESIGNATED` | the same, strong |
| `V313-1` | not reached: `C1` and `C2` held, and the retained guard code was not preserved (`C8`) | `GUARD-RETIRED`, strong |
| `V313-2` | not reached: `C3` held; withdrawn with the round | `AUTHORITY-SWAPPED`, strong |
| `V313-3` | not reached: `C4` and `C5` held; withdrawn with the round | `VERIFIER-SETTLED`, strong |
| `V313-4` | failed at the candidate head: `C8` | `RETIRED-GREEN`, strong |
| `V313-5` | not reached: no `E` designated | `E-DESIGNATED`, strong |
| `V313-6` | measured on the halted receipt commit, and recorded in the receipt | `RECEIPT-HOLDS`, strong |

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

| stage | commit | what it did |
|---|---|---|
| 1 | `cc90082cfbe9dbfe6f84c30d154f189e336d0d75` | added `retire.py`, `messages.json`, `headers.json` and `controls.py` to the record directory |
| 2 | `0811754da89dd5e3674ec913c0c89a24462a88fd` | the guard, written by `retire.py` |
| 3 | `f1dabfb32d60c753b5916470873ab6239cbb21e8` | `legacy-records` in; `V2`, the control-plane tools and the diagnostics job out; `v3-self-test` and `v3-corpus` in; the depth-1 probes checkout |
| 4 | `d658231fdc54593d4d0aafdffed9705ea1d1071d` | the verifier, its corpus and the specification |
| 5 | `dc9f08a076e09c137ac0a61191a02bed3bb839c4` | `AGENTS.md` and `verification/README.md` |
| result | `d4143df7a68af8f29f0137e811bc4f4b289fefa4` | the result note as it stood at the candidate head |

Every one of the nineteen stage files had its frozen blob, and the local checkpoints held:

- **`C1`:** the four record-directory files had their frozen blobs; `controls.py --self-test`
  passed.
- **`C2`:** `retire.py`, run at the stage 1 commit under CPython 3.11.15, printed
  `1616 predicates retired, 1610 as the census classes them and 6 by the amendment; 2486 retained`,
  `structural rows: 15 removed with the emptied checks, 85 kept`, `91 checks remain` and
  `retained predicates missing: 0`. The guard had its frozen blob
  `d1c6bf660958f870b9e9c8e3d07fe6935ba5f824` and compiled. `controls.py history` reported 213 history
  sites at `D` and 0 at stage 2; `controls.py pc4s` and `controls.py vacuity` gave their frozen
  outcomes.
- **`C3`–`C5`:** the stage 3, 4 and 5 files had their frozen blobs; the manifest was `V3-12`'s;
  `legacy_records_check.py` passed at stage 3; `controls.py callers` reported 0 at stages 3 and 4;
  the V3 self-test passed and the corpus reported 135 vectors at stage 3 and 140 at stage 4.
- **`C6`, `C7`, `C9`** held at every stage commit and at the candidate head.

The census classification and its amendment held as measured: 1,616 predicates were retired and
2,486 retained, each by its text hash. What failed is the preservation of the code the round
retained.

***

## `C8` at the candidate head

The candidate head `d4143df7a68af8f29f0137e811bc4f4b289fefa4` was held and the workflow
dispatched on it. Run 36168400287 is a `workflow_dispatch` run whose `head_sha` is that commit:

| job | conclusion |
|---|---|
| `Lean kernel check` | success |
| `Mathlib bridge` | success: the release gate passes 21 of 21, `legacy-records` reporting 303 records in 75 closed namespaces all intact, `v3-self-test` OK, `v3-corpus` 140 vectors and `v3-receipts` holding on three receipts |
| `Numerical probes` | failure: the guard stops after `R1` to `R3` with `TypeError: list indices must be integers or slices, not NoneType` at `rank`, line 229; `Foundations probes` is skipped |

**The cause is in the frozen transformation.** Its step for compound statements left empty counts
a `continue`, `break` or `pass` as removed code, and so deletes an `if` whose body is only such a
statement even where the transformation removed nothing from it, inside the functions and loops the
round retains. Comparing the guard at `D` with the guard at stage 2, five statements were deleted
that way:

| retained statement (line at `D`) | deleted `if` (line at `D`) |
|---|---|
| module-level `for n in (5, 6):` (174) | `if induced_by(n, perm, E) is not None:` (180) |
| `def rank(M):` (226) | `if piv is None: continue` (232) |
| `def grow(clique, cand):` (300) | `if len(clique) + len(cand) - i <= best: break` (304) |
| `def _ogs_def_ok(text):` (25297) | `if not l.strip(): break` (25309) |
| `def _cgr_token(s, i):` (26766) | `if depth == 0: break` (26777) |

None of the five is a predicate, so no text-hash control saw them, and the frozen guard blob
carried them; the guard is run in CI only, as the preregistration's first hazard states.

By the status rule, a `C8` failure the round's paths cause halts the round. The freeze is not
repaired: `retire.py` and the frozen blobs stand as recorded, and no second execution head is built
in this round.

***

## The withdrawal

`W` is the single-parent child of the candidate head. It restores every path the governed-path
block at `F` governs by an `execution` entry to its state at `F`: the guard, the release gate, the
workflow, the verifier, its corpus and the specification, `AGENTS.md` and `verification/README.md`
take their blobs at `F`; `tools/certificate_verifier.py`, `tools/control_plane_base_check.py`,
`tools/control_plane_lint.py`, `verification/certificates/conformance/` and
`g12-reject-execution-changes-legacy-seal-namespace.json` are present again with their blobs at
`F`; `verification/infrastructure/legacy-records.json`, `tools/legacy_records_check.py` and the six
vectors stage 4 added are absent. The record directory keeps what the round wrote there:
the preregistration, `retire.py`, `messages.json`, `headers.json`, `controls.py` and this note.

The candidate head is listed in the receipt's `candidates` with what was measured on it, and
nowhere else.

The scripts that applied the stages, rehearsed the round and built the withdrawal, none of which is
landed:

| script | SHA-256 |
|---|---|
| `exec313.py` (applied the five stages, reading every blob back from the preregistration at `F`) | `7782d082c7ae546f7d9e0c581c6d2654e3611e88b76ca6ab9dbab48969c9d84b` |
| `sim313.py` (the drafting-time rehearsal) | `e47c2678f84d7a5dfcd8265f01dc5dcf203e793b8f7791fab8264e1a47c6a2bd` |
| `readme_control.py` (the `R7-A6P` and `R7-A6I` scanners, extracted from the guard) | `257129b0e9c973fc630faa458956056cd248a3b05b3a04975417f79562f62093` |
| `wd313.py` (built `W` and checked the withdrawal invariant, the record directory and the legacy records) | `6288b2c2a872d26aa8be8a0c359ef2dade8e1a184a9fe5d94b561d511cc095c1` |

***

## Discrepancies

One, against the freeze: `C8` failed at the candidate head, because the frozen transformation
deleted five retained statements. The round halted and the discrepancy is recorded here, not
repaired.
