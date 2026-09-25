# Verifier round V3-13 — retirement: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39: one pull
request from `D`, the control plane drafted on it, execution after the owner designates `F`, and
the round's protocol record a receipt on which `tools/v3_verifier.py --verify-round` must print
`VERDICT  HOLDS`.

> **V3-13 retires the checks that re-derive the chronology of the rounds landed before V3.** It
> removes 1,616 guard predicates — the 1,610 `V3-12`'s census retires and six this freeze's
> amendment to the census adds — and the 14 checks the census empties, the `V2` certificate verifier, the control-plane base check and lint, and the V3 verifier's projection over
> the `V2` rows. It installs `legacy-records` in the same commit that removes `V2`, adds `G13` to the
> V3 verifier so a native round's records stay as its receipt commit left them, and makes §A.37 a
> record. Legacy immutability and native-round immutability are kept by two mechanisms, over two
> populations, and neither stands in for the other.

## The declarations

```v3-round
round V3-13
kind non-sealing
record-directory verification/infrastructure/round-v3-13-retirement/
```

```v3-governed-paths
record AM verification/infrastructure/round-v3-13-retirement/
record AM verification/receipts/V3-13.json
execution M .github/workflows/verify.yml
execution M AGENTS.md
execution D tools/certificate_verifier.py
execution D tools/control_plane_base_check.py
execution D tools/control_plane_lint.py
execution A tools/legacy_records_check.py
execution M tools/release_gate.py
execution M tools/v3_verifier.py
execution M verification/README.md
execution D verification/certificates/conformance/
execution A verification/infrastructure/legacy-records.json
execution M verification/infrastructure/v3/architecture.md
execution AD verification/infrastructure/v3/conformance/
execution M verification/lean/edge_rigidity_probe.py
```

The record directory holds this preregistration, the guard transformation `retire.py` with its two
inputs `messages.json` and `headers.json`, the retirement controls `controls.py`, and the
result note. The receipt path is `verification/receipts/V3-13.json`. Every other path the round
changes is an execution path listed above; nothing in the legacy-records population is among them.

## The objects

The symbols are the specification's (`verification/infrastructure/v3/architecture.md`, Objects):

- `D` = `f9a9acaa44e4982d7814200c46bf1da222b4cbfc`, the head of `main` after `V3-12`'s landing,
  certified by push run 36149801375 with all six jobs green, the release gate passing with
  `v3-receipts` holding on three receipts, and the guard 105 PASS and 0 FAIL. The pull request
  begins here. Every measurement in this file was taken at `D`.
- `F` — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- `E` — the certified execution head, which the owner designates.
- `Λ` — the last reconciliation, a merge whose first parent is `main` when it is built and whose
  second parent is `E` (or a superseded receipt commit); it is built with `--no-ff` if `main` is
  still `D`.
- `Q` — the final receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/V3-13.json`.

## The owner's decisions

`V3-12`'s preregistration left six questions to this freeze. The owner answered them:

1. **`G12` and `verification/seals/`.** `verification/seals/` leaves `G12`. `G12` governs only a
   native round's own seal record, `verification/v3-seals/<round>.json`; the old tree is legacy
   state, protected by `legacy-records` alone as a closed namespace. The specification's wording that
   called it protocol 2's seal state is corrected. This changes the verifier and removes a duplicate
   authority.
2. **Changes to `legacy-records.json`.** A change to the manifest is admitted only as the governed
   work of a native round whose receipt holds. A commit that changes a record and the manifest
   together fails, however consistent its bytes: a migration, a repair or a change to the population
   is protocol-governed work.
3. **Native records after landing.** `--receipts` gains the check (`G13`): once a native round's
   receipt holds, its record directory and seal record must be exactly those at its receipt commit.
   A correction is made by a new native round, never by rewriting the old one.
4. **The five never-executed legacy rounds.** None is re-preregistered. Their directories are
   closed historical records; a question one of them froze is taken up, if ever, by a new native
   round that cites the old freeze as provenance.
5. **The probes checkout.** With the history-dependent predicates retired, the `Numerical probes`
   job uses the ordinary depth-1 checkout, and this round carries a control showing that no retained
   probe or guard path needs repository history.
6. **The verifier's projection.** It is retired. A caller census is frozen below, showing that no
   caller remains once the wiring changes of stage 3 are in; stage 4 then removes the projection code.

### Two immutabilities, not one mechanism

| | legacy immutability | native-round immutability |
|---|---|---|
| population | the records of the rounds landed before V3: 303 records in 75 closed namespaces, listed in `verification/infrastructure/legacy-records.json` | each native round's record directory and seal record, named by its receipt |
| mechanism | release-gate step `legacy-records`, `tools/legacy_records_check.py` | release-gate step `v3-receipts`, `tools/v3_verifier.py --receipts` (`G13`) |
| what it checks | every listed record keeps its blob and mode; no file is added under a closed namespace; the manifest's blob is the initial one or the certified execution head's blob of a held native round whose governed paths name it | for every receipt in the tree whose receipt commit holds: the record directory at the commit under check equals the one at the receipt commit, path for path, mode and blob; the seal record keeps the blob the receipt names |
| how it changes | only by a native round that governs the manifest | never; a later native round records a correction in its own record |

Neither mechanism reads the other's population. `G12` no longer names `verification/seals/`, so no
V3 rule reads legacy state, and `legacy_records_check.py` lists no native record directory.

## What this round adopts from `V3-12`

`V3-12`'s preregistration set eleven constraints on this round. Each is adopted:

| constraint | how it is met |
|---|---|
| 1. base | `D` is `V3-12`'s certified landing; the manifest installed at stage 3 is byte-identical to `V3-12`'s, blob `9e48bd31797e1673f03807e699a10ae4a0b960c7` |
| 2. no unguarded records | stage 3 installs `legacy-records` (manifest, checker, gate step) and removes `V2` (gate step, job, tool, conformance corpus) in one commit; `R7-CV1` leaves at stage 2 |
| 3. the guard edit | adopted with the amendment below: stage 2 removes the census's 1,610 retired predicates and the amendment's six, each identified by check, line at `D` and text hash; the other 2,486 keep their text hashes; the map at `E` is `D`'s without the 14 emptied checks, all `PASS` |
| 4. retained anchors | no edited file loses a string a retained predicate requires of it; `verification/README.md` keeps "`.github/workflows/verify.yml` runs" (checkpoint `C9`) |
| 5. §A.37's pinned phrases | `R7-SI2` and `R7-SI3` leave at stage 2; §A.37 is edited at stage 5 |
| 6. steps and jobs before tools | every removed step and job leaves at stage 3 with its tool; `ci-gate-presence` holds at every stage |
| 7. the V3 checks | `v3-self-test` and `v3-corpus` enter the gate at stage 3, which removes the diagnostics job |
| 8. the receipts | `V3-10`'s, `V3-11`'s and `V3-12`'s receipts hold at every stage commit and at `Q` |
| 9. the records | nothing in the population is written; the one removal under a closed namespace is `verification/certificates/conformance/`, which is not in it |
| 10. §A.37 as history | §A.37 becomes a record with no provision for a new round; §A.39 governs every new round; a repair or migration of legacy state is a native round |
| 11. local checks | `AGENTS.md` gains §A.40, which states the division of verification work |

## The retirement

### The guard

`retire.py` transforms the guard `verification/lean/edge_rigidity_probe.py` at `D` (blob
`2eab600fb8cd078b3dd0f3867a6e7420cfc2b79f`, 35,098 lines) deterministically, deleting source line
ranges so that every retained line is byte-identical to its line at `D`. It runs as

```
python3 retire.py <guard> <V3-12 census.json> <output> messages.json headers.json
```

under CPython 3.11, whose `ast.unparse` the census's text hashes come from. In order:

1. every predicate the census classes `redundant`, `retire-history`, `retire-machinery` or
   `retire-whole` — 1,268, 291, 49 and 2, together 1,610 — and the six of the amendment below are
   removed, 1,616 in all, each located by its line at `D` and the first sixteen hexadecimal digits of
   the SHA-256 of its unparsed text, which must match; an amendment row must also be a `retain` row
   of the census with that hash;
2. the 14 checks the census empties are removed whole, their `check` calls and bookkeeping with
   them: `R7-ABR`, `R7-ARCH`, `R7-BRIDGE`, `R7-CV1`, `R7-DILCH`, `R7-DILMAP`, `R7-GR1`, `R7-GR2`,
   `R7-RBR`, `R7-SI1`, `R7-SI2`, `R7-SI3`, `R7-SRCA`, `R7-VIS`;
3. dead code goes to a fixpoint: compound statements left empty; module-level functions, assignments
   and in-place mutations nothing live reaches, by reaching definitions; counter increments that
   counted only removed predicates; and loops left binding only such names;
4. comments whose code is gone go with it: a comment block or comment-only paragraph all of whose
   code is removed, the headers of the 14 emptied checks, the nineteen orphaned descriptions of the
   base and seal constants round `SI-3` removed, and six drift-control comment lines;
5. the messages of the 41 split checks are replaced by the texts in `messages.json`, and 20 comment
   paragraphs by those in `headers.json`: the headers of 19 retained checks that described retired
   controls, and the header of the emptied `R7-BRIDGE` section, whose two file readers other checks
   use. Each new message and header is the old one with every clause removed that no retained
   predicate tests, joined grammatically, and no clause added; the `R7-BRIDGE` header names only
   what remains.

`retire.py` prints its controls: 1,616 predicates retired, 1,610 as the census classes them and 6
by the amendment, and 2,486 retained; of the census's 100 `structural` rows, 15 removed with the
emptied checks and 85 kept; every retained predicate's unparsed text present at least as many times
as at `D` (0 missing); 91 checks remain, and the 14 emptied checks are gone. The output has 14,792
lines and blob `d1c6bf660958f870b9e9c8e3d07fe6935ba5f824`; a second run gives the same bytes.
`retire.py --census-only` applies the census without the amendment, the 1,610 transformation
against which the vacuity control measures.

`check` still appends each tag to `CHECK_TAGS`, which after stage 2 nothing reads. It is a line
inside a retained function, `retire.py` does not edit function bodies, and it stays.

### The amendment to `V3-12`'s census

By the owner's direction this freeze reclassifies six predicates the census classes `retain`, and
retires them with the census's 1,610. The census and its record are not edited: the amendment is
this table, and `retire.py` carries it as `AMENDMENT`, refusing a row that is not a `retain` row of
the census with its hash.

| check | line at `D` | text hash | predicate | reclassified as |
|---|---|---|---|---|
| `R7-PC4S` | 17854 | `1459be91d4a5bcbb` | `ok_pc4s &= _pc4s_round1_seal()` | legacy seal read |
| `R7-PC4S` | 17999 | `cfaf77fc616d9bc3` | its mutation on `_base` | legacy seal read |
| `R7-PC4S` | 18000 | `2e5e128c60b1684a` | its mutation on `_sealed` | legacy seal read |
| `R7-PC4S` | 18001 | `3a685893e4885af0` | its mutation on `_merge` | legacy seal read |
| `R7-OLT` | 24113 | `27f4b1d56c51ac71` | `ok_olt &= _olt_supersessions()` (`N15`) | self-satisfying |
| `R7-OLN` | 24549 | `2175b51bb131cb5f` | `ok_oln &= _oln_supersession()` (`N14`) | self-satisfying |

**Legacy seal read.** The four `R7-PC4S` rows compare round `PC4`'s seal record with the values
round 1 set, through the guard's record reader. The census's resolver could not resolve that
reader's path and retained them as unresolved, its hazard 2; its thirteen adjudications class the
same comparison for `R7-HYE` `redundant`. They protect no fact that `legacy-records` does not: the
seal records are records of the closed namespace `verification/seals`. Keeping them would leave
seal-reading machinery in a guard that, after this round, reads none.

**Self-satisfying.** `N15` and `N14` look in the guard's own source for strings of `SI-3`'s
supersession table: two object ids, `_seal_field('SI3', 'sealed_head')`, `_SI3_MANIFESTED`,
`_SI3_MANDATED_BASE`, and `R7-OLT`'s declared-branch baseline equality. After the 1,610
transformation each string occurs only in the predicate's own literal, so neither can fail on any
change to the rest of the guard. `N14` keeps one negative conjunct, the absence of a statement that
reads `_MANIFEST_BASELINE`, a name the transformed guard no longer defines.

**The controls**, in `controls.py`, run at the stage 1 commit:

- `controls.py pc4s <repository> <D>` evaluates the four `R7-PC4S` rows with exactly the guard
  definitions they reach, executed from the guard at `D` over `D`'s tree with every file read and
  directory listing recorded and no child process allowed. Frozen outcome: all four hold; 35 files
  read, 34 of them records of the legacy-records manifest (every record under
  `verification/seals/`) and the 35th `verification/migration-manifest.json`, read as a lookup;
  one directory listed, `verification/seals`, a closed namespace; and a one-byte change to
  `verification/seals/PC4.json` makes the unmutated predicate fail.
- `controls.py vacuity <repository> <commit> <D>` builds the 1,610 transformation of the guard at
  `D` and evaluates `N15` and `N14`, taken from it, on its text, on its text with every occurrence
  of their strings outside their own definitions removed, and on their own definitions alone.
  Frozen outcome: the strings occur 0 times outside the definitions and all six evaluations hold;
  the countercontrols fail as they must — each predicate on a text without its strings, and `N14`
  on the guard with the statement it forbids appended.

The same evaluations on the guard at `D`, which the control reports without requiring them, also
hold: the strings then occurred outside the definitions, 10 times for `N15` and once for `N14`,
but removing them changes neither verdict. The two predicates were self-satisfying at `D` as well;
the transformation removes the occurrences that made it look otherwise.

**The count.** 1,616 retired and 2,486 retained. No `structural` row moves: the six predicates'
checks keep their other predicates, so their accumulators and bookkeeping stay. What goes with the
six is dead code, removed by the same fixpoint and counted as statements, not predicates: the
record reader, schema and accessor with their constants, and the two source reads.

### `V2` and `legacy-records`

Stage 3 is one commit. It adds the manifest at `verification/infrastructure/legacy-records.json`,
byte-identical to `V3-12`'s; the checker `tools/legacy_records_check.py`; and the gate step
`legacy-records`. It removes the gate step `certificate-verifier`, the workflow job
`Certificate verifier`, `tools/certificate_verifier.py` and `V2`'s conformance corpus
`verification/certificates/conformance/` (90 files, none in the population, all under the closed
namespace `verification/certificates`, which is why the corpus and the check must change together).
The certificates, attestations, `live-policy.json` and `legacy-v1-owned.json` stay, as records.

`legacy_records_check.py <commit>` runs its self-test, then reads git objects at the commit and
nothing else. Its self-test covers: an intact tree; a live file changed; a record mutated, deleted
or given another mode; a file added under a closed namespace; a record and the manifest changed
together by an ordinary commit; a native round governing the manifest whose receipt holds
(admitted); the same round without the manifest in its governed paths, and with a receipt that does
not hold (both refused); and two malformed manifests.

### The control-plane tools

Stage 3 also removes the gate step `control-plane-lint`, the workflow job `Control-plane base
check`, `tools/control_plane_lint.py` and `tools/control_plane_base_check.py`. A native round
carries no `control-plane-preconditions` block; its freeze is `F`, which the verifier re-derives.

### The V3 verifier

Stage 3 adds the gate steps `v3-self-test` and `v3-corpus` and removes the workflow job
`V3 verifier diagnostics`, whose last step was the one caller of the projection. Stage 4 then
edits `tools/v3_verifier.py`:

- **`G12` restated.** `foreign()` no longer lists `verification/seals/`; the specification's `G12`
  says the same, and that `legacy-records` keeps the records of the rounds before V3.
- **`G13` added.** `--receipts` checks, for each receipt whose receipt commit holds, that the round's
  record directory at the commit under check equals the one at its receipt commit, path for path,
  mode and blob, and that the seal record keeps the blob the receipt names; a failure is
  `g13:record-directory-changed` or `g13:seal-record-changed`. `--verify-round` is unchanged: whether
  a round holds is still decided from `Q`.
- **The projection removed**: `--project`, `--mode shadow`, the projection functions, the
  `SETTLED` table and `ATTESTATION_DIR`.

The conformance corpus replaces `g12-reject-execution-changes-legacy-seal-namespace` with
`g12-admit-execution-changes-legacy-seal-namespace` and adds five `G13` vectors, each a landed
sealing round checked by `--receipts` after a later commit: records unchanged (holds); a record file
modified, added or deleted, and the seal record changed (each fails, family `g13`). The corpus
becomes 140 vectors. The runner gains a `receipts` step for repository vectors.

**The caller census, frozen.** `controls.py callers <repository> <commit> <D>` lists the names
`tools/v3_verifier.py` defines at `D` and not at the commit, and every file outside the round
records that refers to one through the verifier's module or runs the verifier with `--project` or
`--mode`:

| commit | names removed | callers |
|---|---|---|
| `D` | none | 1: `.github/workflows/verify.yml:310`, the diagnostics job's shadow report |
| stage 3 | none | 0 |
| stage 4 | `ATTESTATION_DIR`, `AXES`, `SETTLED`, `_axis`, `_strong`, `_v3only`, `project` | 0 |

`tools/v3_receipt.py` and `tools/legacy_records_check.py`, the verifier's two importers, use none of
the seven names.

### The workflow

After stage 3 the workflow has three jobs: `Lean kernel check`, `Mathlib bridge` with the release
gate, and `Numerical probes`, which checks out at depth 1. The bridge job keeps `fetch-depth: 0`:
`v3-receipts` and `legacy-records` read history.

**The history control, frozen.** `controls.py history <repository> <commit>` scans every Python
file the probes job runs at the commit, with each repository module it imports from its own
directory, for a subprocess or git import, a call of `os.system`, `os.popen` or a subprocess
function, an environment read, and a string constant that is a git subcommand, `git`, a path
through `.git` or a ref under `refs/`:

| commit | files | history sites |
|---|---|---|
| `D` | 56 (56 named) | 213, all in the guard |
| stage 2 and every later stage | 56 (56 named) | 0 |

The count at `D` is the countercontrol: the scan finds the sites the retirement removes.

### The release gate

After stage 3 it runs 21 steps: `toolchain`, `baseline-label`, `staleness`, `voice`,
`voice-scope`, `ci-gate-presence`, `artifact-placement`, `manifest-drift`, `claims`, `duplicate`,
`mirror`, `citation`, `architecture`, `dependency-label`, `coverage`, `lean-axioms`,
`lean-manuscript`, `legacy-records`, `v3-self-test`, `v3-corpus` and `v3-receipts`.

### The documents

Stage 5 edits `AGENTS.md` and `verification/README.md`; stage 4 edits the specification.

- `AGENTS.md`: §A.37 becomes a record of how the rounds before V3 ran and the vocabulary their
  records use, pointing to the section's full text at `D`, with no provision for a new round;
  §A.39 drops the compatibility designation, carries the resolve-by-merits and exact-head rules for
  reconciliation, and states the two immutabilities; §A.40 states where verification runs; the
  review rule for frozen control-plane blobs is restated for a native freeze; the lessons register
  points at the rules that now hold.
- `verification/README.md`: the `SI-1`, `SI-2`, `SI-3` and `CV-1` paragraphs are put in their own
  time where they described the retired machinery in the present; the workflow sentence names three
  jobs; the V3 verifier paragraph drops the projection and names `G13`; one paragraph describes this
  round.
- `verification/infrastructure/v3/architecture.md`: the preamble drops the compatibility
  designation and names this round's settlements; `G12` is restated; `G13` is added under `S10`, with
  a row in the traceability table.

## The authority model after `V3-13`

| mechanism | property protected |
|---|---|
| `Lean kernel check` | the zero-import core's proofs are accepted by the Lean kernel |
| `Mathlib bridge`: build | every OIBridge module compiles |
| gate `toolchain` … `lean-manuscript` | as at `D` (`V3-12`'s table) |
| gate `legacy-records` | every legacy record keeps its blob, nothing is added to a closed namespace, and the manifest changes only through a held native round |
| gate `v3-self-test`, `v3-corpus` | regression evidence for the verifier's implementation |
| gate `v3-receipts` | every native round is protocol-valid from its receipt commit, and its records are unchanged since (`G13`) |
| `Numerical probes` | the companion probes, and the guard's 2,486 retained predicates in 91 checks, reading no history |

**What nothing checks**, recorded so that it is decided: the existence and ancestry of the commits
the legacy records name, which rest on the repository's history and its branch protection; and the
host attestations a receipt records, which no predicate reads (§A.39). `V3-12`'s second item, native
records after landing, is `G13`.

## The execution

Five stage commits and the result note, each with one parent, from `F`:

1. **Stage 1** adds to the record directory:

| path | blob |
|---|---|
| `verification/infrastructure/round-v3-13-retirement/retire.py` | `1e549b70d131629d45092fdd807c6d61a6fab0d6` |
| `verification/infrastructure/round-v3-13-retirement/messages.json` | `96e82a37fe24342a2022829ae78fbf1cd9f0e888` |
| `verification/infrastructure/round-v3-13-retirement/headers.json` | `8c727cad183a54048064013b3805013d35ed9fc1` |
| `verification/infrastructure/round-v3-13-retirement/controls.py` | `0870fdecc54e5a8545b2ab1e72c108c8a4adaa51` |

2. **Stage 2** writes the guard with `retire.py`, run at the stage 1 commit from the repository
   root as `python3 verification/infrastructure/round-v3-13-retirement/retire.py
   verification/lean/edge_rigidity_probe.py
   verification/infrastructure/round-v3-12-retirement-census/census.json
   verification/lean/edge_rigidity_probe.py
   verification/infrastructure/round-v3-13-retirement/messages.json
   verification/infrastructure/round-v3-13-retirement/headers.json`:

| path | blob |
|---|---|
| `verification/lean/edge_rigidity_probe.py` | `d1c6bf660958f870b9e9c8e3d07fe6935ba5f824` |

3. **Stage 3** swaps the authority, deleting `tools/certificate_verifier.py`,
   `tools/control_plane_base_check.py`, `tools/control_plane_lint.py` and
   `verification/certificates/conformance/`, and writing:

| path | blob |
|---|---|
| `verification/infrastructure/legacy-records.json` | `9e48bd31797e1673f03807e699a10ae4a0b960c7` |
| `tools/legacy_records_check.py` | `0d8f5f49b762954aaa075e543e2be53ec54529c7` |
| `tools/release_gate.py` | `a279ff334d0196c5212be8a6f403d73326008d2d` |
| `.github/workflows/verify.yml` | `7196339b8a31ba2f31098d631a75d69995e48e8a` |

4. **Stage 4** edits the verifier, its corpus and the specification, deleting
   `verification/infrastructure/v3/conformance/g12-reject-execution-changes-legacy-seal-namespace.json`
   and writing:

| path | blob |
|---|---|
| `tools/v3_verifier.py` | `ad47527d1f52bc95f5037637ae7fdd0a294d9513` |
| `verification/infrastructure/v3/architecture.md` | `08d768669cd4c3cf1113e2f78ec2d141cf074661` |
| `verification/infrastructure/v3/conformance/g12-admit-execution-changes-legacy-seal-namespace.json` | `f0207794af2eaf6f2c43a7ecd932589aaab51d44` |
| `verification/infrastructure/v3/conformance/g13-admit-records-unchanged-after-later-commit.json` | `3c8f396a5fe0db70519328cf31082225f0143e19` |
| `verification/infrastructure/v3/conformance/g13-reject-record-file-added-after-landing.json` | `6a4a28fc793abe165b8c629465951643ad070231` |
| `verification/infrastructure/v3/conformance/g13-reject-record-file-deleted-after-landing.json` | `311c119ee0c85345e7afcd1068617005d9f67ed6` |
| `verification/infrastructure/v3/conformance/g13-reject-record-file-modified-after-landing.json` | `a474cb4792ab6ac72bea532f74bfcdf6efd615a9` |
| `verification/infrastructure/v3/conformance/g13-reject-seal-record-changed-after-landing.json` | `7e55b7f3176b3707098e97e35b9204be12f996b4` |

5. **Stage 5** edits the documents:

| path | blob |
|---|---|
| `AGENTS.md` | `4560d2db156fa40acba81acb76c440556f5a44fb` |
| `verification/README.md` | `75f767b6ce7dbff72121ba4fb26a449d95880557` |

6. **The result note** `result.md`, whose commit is `E`.

## Targets

| target | question | outcome if it holds | predicted |
|---|---|---|---|
| `V313-0` | is `F` attested and designated? | `F-DESIGNATED` | holds, strong |
| `V313-1` | does stage 2 remove exactly the census's retirements and the amendment's six, and keep the rest? | `GUARD-RETIRED` | holds, strong |
| `V313-2` | does stage 3 swap `V2` for `legacy-records` in one commit with no record written? | `AUTHORITY-SWAPPED` | holds, strong |
| `V313-3` | does stage 4 restate `G12`, add `G13` and remove the projection with no caller left? | `VERIFIER-SETTLED` | holds, strong |
| `V313-4` | does every gate pass at `E`, with the guard's map `D`'s without the 14 emptied checks? | `RETIRED-GREEN` | holds, strong |
| `V313-5` | is `E` attested and designated? | `E-DESIGNATED` | holds, strong |
| `V313-6` | does `--verify-round Q` hold? | `RECEIPT-HOLDS` | holds, strong |

The checkpoints:

- **`C1`** (stage 1): the four files have their frozen blobs; `controls.py --self-test` passes.
- **`C2`** (stage 2): `retire.py` exits 0 printing `1616 predicates retired, 1610 as the census
  classes them and 6 by the amendment; 2486 retained`, `retained predicates missing: 0` and
  `91 checks remain`; the guard has its frozen blob and compiles; `controls.py history` reports 0
  sites at stage 2 and 213 at `D`; `controls.py pc4s` and `controls.py vacuity` give their frozen
  outcomes.
- **`C3`** (stage 3): the four files have their frozen blobs, the manifest byte-identical to
  `V3-12`'s; `legacy_records_check.py` passes at stage 3 and fails at stage 2 (the manifest
  absent); `controls.py callers` reports 0; the V3 self-test and corpus pass.
- **`C4`** (stage 4): the eight files have their frozen blobs; the V3 self-test passes; the corpus
  reports 140 vectors as expected; `controls.py callers` reports 0 with the seven names removed.
- **`C5`** (stage 5): the two files have their frozen blobs.
- **`C6`** (every stage commit and `Q`): `--receipts` holds on `V3-10`'s, `V3-11`'s and `V3-12`'s
  receipts; from stage 3, `legacy_records_check.py` passes.
- **`C7`** (`E`): `git diff --no-renames --name-status D E` lists only governed paths, each change
  authorized, and no path of the legacy-records population.
- **`C8`** (`E`): the dispatch run at `E` has its three jobs green; the guard reports 91 PASS and 0
  FAIL with its verdict map equal to `D`'s without the 14 emptied checks; the release gate passes
  21 of 21, `legacy-records` intact and `v3-receipts` holding on three receipts.
- **`C9`** (`E`): the files this round edits still carry what the retained predicates require of
  them: `verification/README.md` every string literal of the stage 2 guard that it carries at `D`,
  the anchor "`.github/workflows/verify.yml` runs" among them, and no over-reading in the slices
  `R7-A6P` and `R7-A6I` scan, by those checks' own scanner functions; `.github/workflows/verify.yml`
  `repertoire_lie` and no `lake build OIBridge.` or `lake env lean OIBridge/` line; `AGENTS.md` the
  §A.35 heading and "updates the registry in the same commit"; `tools/release_gate.py`
  `"lean-manuscript"`.
- **`C10`** (`Q`): `tools/v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`; `--receipts Q`
  holds on four receipts; `legacy_records_check.py Q` passes.

**The status rule.** Each target's outcome is its checkpoints' verdict. If `C1` to `C5` fails, the
stage is not the one frozen here: the round halts under the specification's `S12` and records the
discrepancy; the freeze is not repaired. A failure of `C8` that the round's paths cannot cause is
diagnosed and recorded before `E` is brought for designation; one they cause halts the round.

## Hazards

1. **The guard is not run locally.** `retire.py`'s controls are static: text hashes, dead-code
   reachability and a history scan. That the 91 retained checks still pass is measured only by the
   dispatch run at `E` (`C8`). A retained predicate that depended on a side effect of a removed
   statement the analysis does not model would fail there.
2. **The Python version.** `retire.py` locates predicates by `ast.unparse` text hashes; it runs
   under 3.11, as the census did.
3. **The shallow checkout.** The history control scans the probes job's own files and the modules
   they import from their directories; a probe that reached history some other way would fail
   closed in CI at `E`, not pass silently.
4. **The G13 check and later rounds.** From this round's landing, a round that changes another
   native round's record directory fails the gate. None does at `D`.

## What this round does not do or license

1. It changes no mathematics, no manuscript, no Lean file and no record of another round.
2. It retires no check of content beyond the census and the amendment: the 2,486 predicates they
   retain keep their text, and the new messages and headers say less than the old ones, never
   more.
3. It licenses no sentence that a retired check was wrong. Each was true of its round, and its facts
   remain recorded in that round's notes, seal record and certificate.
4. It re-preregisters none of the five legacy rounds that were frozen and never executed.
