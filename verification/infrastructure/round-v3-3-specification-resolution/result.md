# Verifier round V3-3 — V3 specification resolution: RESULT

Executed on #729 from the certified execution base and from nothing else, under `AGENTS.md` §A.37:
the control plane #728, then this execution pull request, which also carries the landing.

- **`D`** — `347113a234ef5eea6986b663ea0971687591b33b`.
- **`B`** — `70f714d4067f4f3f78c0dd8e0834bb868ad2b6d0`, the merge of #728. Its parents are `D`
  and the reviewed control-plane head `5e246493877c871fb29a7df96b0b519da394e83b`, and its tree is
  that head's. Push run 35972419116 was green on all six jobs, the control-plane base check in mode `B`
  with 13 rows and 2 frozen blobs.
- **Preregistration** — blob `ad0a89f3c25a8a6e270dcf62cbc12ed2001b5110` at `B` and at `E`.
- **Shape** — non-sealing, `E` → `L`, no `P`: no guard clause, manifest record, round certificate or
  attestation (reading `R5`).
- **Status** — every target reached its passing outcome. For `V33-6` the repository-wide conditions
  (the guard, the release gate, `V2`) are established by the exact-head run on `E`, which the `E`
  certification record on #729 identifies; they were not run locally.

| target | outcome | predicted |
|---|---|---|
| `V33-0` | `BASE-HOLDS` | `BASE-HOLDS`, strong |
| `V33-1` | `SPECIFICATION-SETTLED`; blob `3326bf30` | `SPECIFICATION-SETTLED`; blob `3326bf30`, strong |
| `V33-2` | `CORPUS-CONFORMING`; digest `187c8301` | `CORPUS-CONFORMING`; digest `187c8301`, strong |
| `V33-3` | `DEPARTURES-DEMONSTRATED`; digest `605f9328` | `DEPARTURES-DEMONSTRATED`; digest `605f9328`, strong |
| `V33-4` | `SETTLEMENTS-SATISFIABLE` | `SETTLEMENTS-SATISFIABLE`, strong |
| `V33-5` | `ALTERNATIVES-EXCLUDED` | `ALTERNATIVES-EXCLUDED`, strong |
| `V33-6` | `SHADOW-UNCHANGED` | `SHADOW-UNCHANGED`, strong |
| `V33-7` | `SCOPE-HELD` | `SCOPE-HELD`, strong |

`SETTLEMENTS-SATISFIABLE` and `ALTERNATIVES-EXCLUDED` are consistency findings about the settlements
and their vectors, made with code by the author of the settlements; they are not evidence that the
settlements are right (hazard `H1`).

The shadow verifier `tools/v3_verifier.py` is unchanged and gates nothing. `V1` and `V2` remain
authoritative. V3 is not operative.

***

## `V33-0` — the base: BASE-HOLDS

The execution branch was created at exactly `B`, after `B`'s push run was green. At `B` the
preregistration's blob is the frozen `ad0a89f3`, `verification/infrastructure/v3/architecture.md`'s
is `6c80e584021f973c529625b1da89469e7b136dfe` and `tools/v3_verifier.py`'s is
`2c34d4d7f1adadc4bdecbad94ff8eadb7b30f974`, the two frozen blobs. The control-plane base check in
mode `B` holds at `B`: 13 rows and 2 frozen blobs, no failure. No execution object existed at `B`.

***

## `V33-1` — the normative text: SPECIFICATION-SETTLED

Stage 1, commit `ffa46b453f0dd02e22cd541bdc4dd145808be0d7`, whose only parent is `B`. The sixteen
edits `A1`–`A16` were read back from the preregistration as it stands at `B` and applied in order to
`architecture.md`'s blob at `B`. The result is blob `3326bf309d6392e4e5d69a9e7ab6d812dba035af`, the
predicted one, and it is the file's blob at `E` (`C6`). The commit changes no other file.

***

## `V33-2` — the corpus: CORPUS-CONFORMING

Stage 2, commit `bfb4d90b9a53de2060d6179b1fd330113addf1c7`, whose only parent is `ffa46b45`. At `E`,
`verification/infrastructure/v3/conformance/` is the set at `B` less
`g6-admit-record-class-by-broader-entry`, plus the ten frozen additions: 93 vectors. The additions'
digest, SHA-256 of the ten files concatenated in path order, is
`187c8301b1fb32b19089d14a8ad3c96462d841bf619fe24081a2d752a635d15b`, the predicted one, so each
addition has its drafting-time bytes and matches its frozen row.

`C1`: `tools/v3_verifier.py --corpus` runs the 93 vectors as an exact set, every one as expected,
exit 0.

***

## `V33-3` — the departures: DEPARTURES-DEMONSTRATED

`verification/infrastructure/v3/conformance-pending/` holds exactly the eleven frozen pending
vectors. Their digest is `605f9328fa4751fb766362a743e043883249784c4899fe088038f01baa5d96bc`, the
predicted one.

`C2`: the unchanged shadow runs the directory with exit 1, and every vector runs not as expected,
with the shadow verdict the pending table records: `FAILS s10:` for
`k4-admit-superseded-receipt-unreadable`, `HOLDS` for the other ten. No pending vector is met by the
unchanged shadow.

***

## `V33-4` — satisfiability: SETTLEMENTS-SATISFIABLE

`C3`: the settlement patch, a scratch copy of the shadow changed only where the settlements depart
from its readings and never tracked, regenerated at `E` from the shadow's unchanged source with
SHA-256 `481cf746fa74ba94bb7238f016921f5a98a7d415416c679745f3eb4545ab0bd3`, runs `conformance/` (93)
and `conformance-pending/` (11), every vector as expected, exit 0 on both.

`C4`: for each of the eleven pending vectors, the settlement patch with that vector's own rule taken
out runs that vector not as expected, and every pending vector not decided by the same rule as
expected.

| pending vector | rule taken out |
|---|---|
| `g6-reject-execution-entry-within-record-directory` | `G6` record class |
| `g6-reject-halted-landing-publishes-unnamed-seal-record` | `G6` record paths in the halted landing |
| `g6-reject-halted-record-commit-writes-unnamed-seal-record` | `G6` record paths in the record commit |
| `g6-reject-record-class-by-broader-entry` | `G6` record class |
| `g6-reject-record-entry-outside-own-record` | `G6` record class |
| `g6-reject-record-file-entry-in-non-sealing-round` | `G6` record class at `F` |
| `g7-reject-superseded-receipt-commit-changes-preregistration` | `K4` seal records from the final receipt |
| `k2-reject-governed-block-only-in-amendment` | `K2` blocks in the preregistration only |
| `k2-reject-round-block-only-in-amendment` | `K2` blocks in the preregistration only |
| `k4-admit-superseded-receipt-unreadable` | `K4` seal records from the final receipt |
| `k4-reject-superseded-receipt-authorizes-own-extra-path` | `K4` seal records from the final receipt |

***

## `V33-5` — the alternatives: ALTERNATIVES-EXCLUDED

`C5`: each of the eighteen rejected alternatives the settlement tables name with a distinguishing
vector, other than `V3-2`'s own readings, which `C2` exercises, was implemented in a scratch copy.
Seventeen are copies of the unchanged shadow; `G6` (b) is a copy of the settlement patch. Each copy
runs its distinguishing vector not as expected while the copy it was made from runs it as expected.
No control was void.

The scratch scripts, none of which is landed:

| script | SHA-256 |
|---|---|
| `settle.py` (builds the settlement patch) | `0f18c88d939e7c504bf14d7a5df48d789033f9cdcf98c293d682541f2f06e430` |
| `alternatives.py` (`C4`, `C5`, drafting-time paths) | `dcc551a8e8cbbc6791a61f52a11a6c44acdb1edd7e0cf4494048b848709265b4` |
| `alternatives_e.py` (the same, reading the repository's directories) | `9d38696f2c64bb8a24447db2e127f4f860f1fe99188b8a3b668c58ba07a53d66` |
| `frozen_edits.py` (`C6`) | `18f8ff6e2e976ef3449d710bb174a06135d9f309435e93de32f4c517acbbb327` |
| `gen_v33.py` (builds the vectors) | `a5a6e9391da4a9f7615c17305b0cd6c6b7ed3ea5b014215cc69c6feaa1820793` |
| `helpers.py` (`V3-2`'s recipe helpers) | `146e10c4f5a3e093c4091ca9561fd878f00b0450f481b1e7b202d1157c8c118b` |

`alternatives_e.py` differs from `alternatives.py` only in the two lines that locate the conforming
and pending vectors; its output at `E` is identical to the drafting-time output of
`alternatives.py`.

***

## The seven items at `E`

The shadow is unchanged, so its conformance at `E` is its conformance at `D`, as measured by `C1`
and `C2`.

| item | settlement | same as `V3-2`'s reading | shadow at `E` conforms |
|---|---|---|---|
| `K1` | (a), with precisions | yes | yes, but for `K2`'s location |
| `K2` | (b), a rule about `F` only | no | no |
| `K3` | (a), non-strict | yes | yes |
| `K4` | (f) | no | no |
| `G5` | (a), authorization not required | yes | yes |
| `G6` | (c) | no | no |
| `G7` | (a) | yes | yes, but through `K4` |

`G8` to `G12` remain as recorded in the preregistration and are not settled.

***

## `V33-6` — non-authority: SHADOW-UNCHANGED

At `E`, `tools/v3_verifier.py`, `.github/workflows/verify.yml`, `tools/release_gate.py`,
`tools/certificate_verifier.py`, `verification/lean/edge_rigidity_probe.py` and `AGENTS.md` have
their `B` blobs, and the shadow's self-test passes. No act of `V3-2`'s promotion boundary is
present: no `verification/receipts/` directory exists, the shadow has no authoritative mode, and no
required check was touched.

The guard's verdict (105 PASS, 0 FAIL, with `D`'s verdict map), `V2` authoritative OK and the
release gate's 19 of 19 steps at `E` are taken from the exact-head run on `E`, not run locally.

***

## `V33-7` — scope: SCOPE-HELD

`git diff --no-renames --name-status B E`:

| status | path |
|---|---|
| `M` | `verification/infrastructure/v3/architecture.md` |
| `A` | the ten added vectors of `verification/infrastructure/v3/conformance/` |
| `D` | `verification/infrastructure/v3/conformance/g6-admit-record-class-by-broader-entry.json` |
| `A` | the eleven vectors of `verification/infrastructure/v3/conformance-pending/` |
| `A` | `verification/infrastructure/round-v3-3-specification-resolution/result.md` |

This is exactly the mutation budget. Nothing on the budget's never-written list changes. With rename
detection on, Git reports the deletion and the added
`conformance-pending/g6-reject-record-class-by-broader-entry.json` as one rename, because the two
files are similar; the change is one deletion and one addition, and scope is accounted with rename
detection off.

***

## Discrepancies

None against the freeze. Two execution details are recorded:

- **The first `C3` invocation.** The settlement patch lives in scratch, and run with `--corpus` and
  no directory it resolves the corpus relative to its own location, so the first invocation reported
  `CORPUS absent`. Run again naming the repository's `conformance/` directory, it ran the 93 vectors
  as expected.
- **Rename display.** As stated under `V33-7`, Git's rename heuristic can show the `G6` deletion and
  addition as a rename; the no-renames diff is the scope of record.

***

## Chronology

The execution's commits after `B` are three: the normative text (`ffa46b45`), the vectors
(`bfb4d90b`), and this note, which is `E`. Each has exactly one parent, the first `B`. None changes
the preregistration, and the branch absorbed no later `main`. Nothing has been merged.
