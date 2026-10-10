# Verifier round V3-12 — retirement of the legacy protocol machinery: PREREGISTRATION

**Status: draft control plane, not designated.** This file is a draft on a local branch from `D`. It
carries the retirement census, the proposed disposition of every surface, the dependencies between
the proposed removals and the predicted authority model after the round. The execution texts and
predicted blobs are frozen only after the owner decides the questions listed under *Decisions before
`F`*; until then this file is not a candidate `F`.

> **A mechanism may reject a build only because it protects a property of the repository.** V3-11
> made the receipt the protocol authority for new rounds. This round measures every surviving pre-V3
> authority surface, keeps each check that protects the current tree or the immutable record of a
> landed round, and retires each check whose only content is the superseded chronology of control
> planes, mandated bases, landings, pins and seals.

## The declarations

The governed paths below are provisional: they are the paths the recommended dispositions touch,
and they are fixed at `F` after the decisions.

```v3-round
round V3-12
kind non-sealing
record-directory verification/infrastructure/round-v3-12-retirement/
```

```v3-governed-paths
record AM verification/infrastructure/round-v3-12-retirement/
record AM verification/receipts/V3-12.json
execution M verification/lean/edge_rigidity_probe.py
execution M tools/release_gate.py
execution M .github/workflows/verify.yml
execution D tools/certificate_verifier.py
execution D tools/control_plane_lint.py
execution D tools/control_plane_base_check.py
execution A tools/legacy_records_check.py
execution A verification/infrastructure/legacy-records.json
execution M tools/v3_verifier.py
execution M AGENTS.md
execution M verification/README.md
execution M verification/ROADMAP.md
execution M verification/infrastructure/v3/architecture.md
```

`verification/seals/`, `verification/certificates/`, `verification/receipts/V3-10.json`,
`verification/receipts/V3-11.json` and every landed round's records are not governed and are not
written: the specification forbids a native round to write seal state (`G12`), and landed records
are immutable.

## The objects

- `D` = `81150851f84c8aa1df71dc69013a6ca6f6d71b51`, the head of `main` after `V3-11`'s landing,
  certified by push run 36125130929 with all six jobs green. Every measurement in this file was
  taken at `D`.
- `F`, `E`, `Λ` and `Q` as in `verification/infrastructure/v3/architecture.md`.

## How the census was measured

Every measurement was read-only at `D`. The per-predicate census of the guard is in `census.json`
beside this file, one row per predicate with its line at `D`, the SHA-256 of its source text and
its class, and for each retired predicate its reason.

- **The guard's predicates.** A predicate is any statement that can change a top-level check's
  verdict: an update of the check's accumulator, an entry written into its `_checks` table, or an
  append to its `_bad` list. They were extracted from the guard's syntax tree, 3,488 of them over
  the 105 top-level checks. For each predicate the extraction follows, through the syntax tree, the
  helper functions it calls and the module-level values it reads back to their assignments, and
  records what those actually execute.
- **The retirement test.** A predicate is **history-dependent** when it or anything it reaches
  executes a `git` subprocess, reads the host environment, reads protocol seal state (the
  prospective declaration, the declared baseline, a seal-validator verdict) or opens
  `verification/seals/`. A history-dependent predicate re-derives facts about the commits of a
  landed round (its base, its execution chain, its landing, its pin) or about the seal machinery
  itself. Those facts are immutable once landed, and they are recorded in the round's own notes and
  in its round certificate. The predicate can fail only if history is rewritten, an object is
  missing or a checkout is shallow, so it protects no property of the tree.
- **The two other surveys.** `tools/certificate_verifier.py` was read family by family, and every
  failure path was classified; the workflow, the release gate, the control-plane tools, the seal
  readers and the maintained documentation were surveyed surface by surface. Both surveys are in
  `census.json`.

## The census

### The guard, `verification/lean/edge_rigidity_probe.py`

| class | predicates | what they read |
|---|---|---|
| retain — substantive integrity | 2,099 | the Lean modules, the manuscripts, the live notes and registries, the workflow's wiring of substantive probes, or an exact computation |
| retain — historical compatibility | 1,043 | only the records of a landed round in the tree: its preregistration, result, amendments and census, their frozen blobs and their readings |
| retire | 342 | history-dependent (251), or the machinery of the retired seal and certificate installation and the seven overrides below (91) |
| structural | 4 | the `_bad` bookkeeping line of a table-form check |

- **66 checks are retained whole**, among them `R1`–`R9`, `R7` and every kernel-module and
  manuscript-propagation guard from `R7-FWD` to `R7-DILCH`, and `R7-A11P`. No predicate of theirs
  reads history.
- **2 checks retire whole:** `R7-VIS` and `R7-ARCH`, synthetic regressions of the archive-mode
  visibility and ancestry rules of §A.37.
- **37 checks are split.** Their retained predicates stay, and their retired predicates go.

| retired predicate family | predicates | checks | what it re-derives |
|---|---|---|---|
| the seal and certificate machinery of `SI-1`, `SI-2`, `SI-3`, `GR-1`, `GR-2`, `CV-1` | 210 | 6 | the seal validator, its synthetic repositories and negative suites, the base-tree pins, the guard's own placement budgets, the V2 store, corpus and wiring |
| `_ordering_pred` | 56 | 7 | the order of a landed execution's first-parent commits and the module text at each |
| `_execution_ancestry` | 28 | 28 | the seal validator's verdict on the round's manifest record: execution ancestry from `B` and landing reachability |
| `_integrity_ok` | 13 | 11 | the manifest record set against the declared baseline |
| inline chronology values | 12 | 9 | the recoverability and pass of a round's chain walk |
| `_declarations` | 7 | 7 | the prospective declaration and the recorded seal state |
| `_locating` | 6 | 6 | blobs at the mandated base and the parents of `B` and `D` |
| `_chron_ok`, `_authority`, `_base_ancestry`, `_git` | 8 | 3 | the chronology walks and seal authority of `PFR`, `PRA` and `RBR` |
| archive-mode synthetic regressions | 2 | 2 | `R7-VIS`, `R7-ARCH` |

Seven retirements are overrides of the mechanical rule, each recorded in `census.json`: five
`R7-GR1` predicates and one placement predicate that test the guard's own code against `GR-1`'s
frozen texts, and one `R7-CV1` predicate that couples `CV-1`'s note to the V2 gate step being
wired.

Two consequences follow for the execution:

- **Dead code.** Retiring the 342 predicates leaves 130 guard functions, 2,084 lines, reachable only
  from retired predicates, and module-level machinery that computes their inputs. The execution
  removes both, and nothing a retained predicate reaches.
- **Messages.** The messages of 36 of the 39 affected checks describe chronology, pins, seals or
  the manifest. A retained message may not state a property its check no longer tests (§A.30), so
  each of those messages loses exactly the clauses of its retired predicates.

### The round-certificate verifier, `tools/certificate_verifier.py` (V2)

It holds 52 certificates (51 translated, 1 bootstrap), 36 attestation rows, 157 evidence pins
(33 of them seal records), 42 control-plane pins, 15 dependency edges, 0 relocation records,
0 live-policy clauses and an 89-vector conformance corpus. It never reads `verification/receipts/`.

| family | what it checks | class |
|---|---|---|
| `VIS` | the §A.37 visibility union: host event, payload, `origin/<base>`, a network fetch when shallow | retire |
| `BASE` | each control-plane blob entered first-parent history as the recorded merge | retire |
| `TOPO-E`, `TOPO-L` | the sealed head and the unique landing, re-derived over the visibility union | retire |
| `LEG-PART` | the V1/V2 ownership partition | retire |
| `POLICY` | round-owned live-tree predicates (none exist) | retire |
| `TOPO-EXIST`, `TOPO-TREE`, `BASEONLY` | the recorded commits exist, the recorded tree is the sealed head's, the base is an ancestor | rebind: facts about immutable objects, subsumed by pinning the records that name them |
| `STORE`, `SCH-CERT`, `SCH-ROW`, `PROV`, `ROW-CERT`, `DEP`, `RELOC`, `LEG-PREREG` | the records are present, well formed and mutually consistent | retain — historical, as record integrity |
| `EVID` | the 157 evidence blobs are unchanged in the tree | retain — historical |
| `CORPUS` | the implementation reproduces its 89 vectors | rebind: meaningful only while the implementation survives |

The measured gap: V2 does not pin the 36 attestation rows, the 16 content-only certificates, the
current `CV1.json` or the seal record `PRA.json`. Their only protection is the topology
re-derivation (`ROW-CERT`, `TOPO-*`, `BASEONLY`). Retiring that re-derivation without a replacement
pin would leave them unprotected.

### The release gate, `tools/release_gate.py` (20 steps)

| step | class |
|---|---|
| `toolchain`, `staleness`, `baseline-label`, `voice`, `voice-scope`, `ci-gate-presence`, `artifact-placement`, `manifest-drift`, `claims`, `duplicate`, `mirror`, `citation`, `architecture`, `dependency-label`, `coverage`, `lean-axioms`, `lean-manuscript` | retain — substantive |
| `v3-receipts` | retain — substantive: the protocol validity of native rounds |
| `certificate-verifier` | split: its record-integrity content is kept (see the proposal), its chronology retires |
| `control-plane-lint` | retire: it lints §A.37 control planes; for a native preregistration it can only produce false failures |

### The workflow, `.github/workflows/verify.yml`

| job or step | class |
|---|---|
| `Lean kernel check` | retain — substantive |
| `Mathlib bridge`: build and release gate | retain — substantive |
| `Numerical probes`: 43 probes and 12 foundations probes | retain — substantive |
| `Numerical probes`: the guard | split, as above |
| `Control-plane base check` job | retire: §A.37 `D`/`B`/`M` preconditions only |
| `Certificate verifier` job (shadow) | retire: it duplicates the gate step and gates nothing |
| `V3 verifier diagnostics`: self-test, corpus | rebind: the correctness of the verifier that decides protocol validity |
| `V3 verifier diagnostics`: `Report (shadow)` | retire: it compares V3 with V2's attestation rows |

### The control-plane machinery and §A.37

- `tools/control_plane_base_check.py`: retire. It selects preregistrations and amendments that carry
  a `control-plane-preconditions` block and changed against the first parent; 24 historical files
  carry one. For a native round it does nothing, except fail if the round edits one of those 24
  files or quotes a literal block.
- `tools/control_plane_lint.py`: retire. It lints the 24 block files and every control-plane file
  in the pull request's diff; prose such as ``B = `<sha>` `` in a native preregistration fails it.
- `AGENTS.md` §A.37: the compatibility lifecycle. Its text describing the guard's ancestry, archive
  mode, `L`/`P` and seal gating becomes a description of past practice once the chronology
  predicates retire. 26 of its phrases are pinned by `R7-SI2` and `R7-SI3` predicates that this
  census retires.

### Seal records and other legacy records

- `verification/seals/` holds 34 records (28 `sealed`, 6 `base-only`). Its readers are the guard's
  seal machinery (retired here), V2's evidence pins (33 of 34), and the V3 verifier's `G12`
  exclusion, which forbids any native round to write there. They stay read-only data.
- `verification/certificates/` holds the 52 certificates, 36 attestation rows, `live-policy.json`,
  `legacy-v1-owned.json` and the 89-vector corpus. They stay read-only data; the V3 verifier's
  projection reads the attestation rows as a diagnostic.

### The maintained documentation

62 groups of statements were found: 21 to rewrite, 16 to reframe as description of past practice,
25 to keep. 16 of them are false or misleading at `D` already, among them:

- `AGENTS.md` 77–87, the review rule that lets a frozen control plane's head absorb its base by
  merging, which a native round cannot do (`G9`);
- `AGENTS.md` 653–667, which calls every round two pull requests and says §A.37 governs rounds
  begun after it was written;
- `verification/README.md` 2519–2584, which says the retired legacy seal constants are read and the
  old machinery runs as a shadow, and counts 22 seal records where there are 34;
- `verification/README.md` 2641, which says CI is three jobs run on changes under `verification/`;
  there are six, with no path filter. Its opening words, "`.github/workflows/verify.yml` runs", are
  the end anchor of two retained guard extractions (`R7-A6P`, `R7-A6I`) and must stay.
- `verification/infrastructure/v3/architecture.md` 382–385, which says `verification/seals/` holds
  protocol 2's seal state; it is the guard's manifest, and V2 only pins it.

Of the 166 historical round records, 106 mention §A.37, seals or certificates. None of the 166 is
edited, being records.

## Proposed dispositions

| surface | disposition |
|---|---|
| 3,142 retained guard predicates | unchanged |
| 342 retired guard predicates | removed, with the code only they reach and the message clauses that describe them |
| `R7-VIS`, `R7-ARCH` | removed |
| `tools/certificate_verifier.py`, the `certificate-verifier` gate step, the `Certificate verifier` job | removed; the record-integrity property V2 protects is carried by `legacy-records` (below), which pins more than V2 did |
| `legacy-records` (new gate step, `tools/legacy_records_check.py`, `verification/infrastructure/legacy-records.json`) | added: every file under `verification/certificates/` and `verification/seals/`, every V2 evidence and control-plane path, and every file of a landed pre-V3 round directory, byte-identical to its blob at `D` |
| `tools/control_plane_lint.py`, the `control-plane-lint` gate step | removed |
| `tools/control_plane_base_check.py`, the `Control-plane base check` job | removed |
| `V3 verifier diagnostics` | `Report (shadow)` removed; self-test and corpus moved into the release gate as `v3-verifier`; the job removed |
| `tools/v3_verifier.py` | docstring only: V2 no longer runs; no verdict, mode or code path changes |
| `AGENTS.md` | §A.37 condensed to a record of the lifecycle under which the pre-V3 rounds landed; §A.39 states the authority model below; the review rule 77–87 and the placement rule 623–627 restated for native rounds; a new section on local checks and CI |
| `verification/README.md`, `ROADMAP.md`, `architecture.md` | the 21 rewrites and 16 historical framings of the documentation survey, and the corrections of what is already false |
| `verification/seals/`, `verification/certificates/`, receipts, landed records | not written |

## Dependencies between the removals

1. **Record integrity is never unprotected.** `legacy-records` is installed in the same stage as,
   or an earlier stage than, the removal of `certificate-verifier`, and it covers the attestation
   rows, the content-only certificates, `CV1.json` and `PRA.json`, which V2 does not pin.
2. **§A.37's pinned phrases.** The `R7-SI2` and `R7-SI3` predicates pinning 26 phrases of §A.37
   retire in the same stage as, or an earlier stage than, any edit to those phrases.
3. **V2's wiring and store.** The `R7-CV1` predicates that pin the shadow job, the gate step, the V2
   store counts and the V2 corpus retire in the same stage as, or an earlier stage than, the removal
   of any of those.
4. **Gate before tool.** The `control-plane-lint` and `certificate-verifier` steps leave the gate in
   the same commit as, or before, their tools are deleted; `ci-gate-presence` holds throughout.
5. **Job before tool.** The `Control-plane base check` job leaves the workflow with, or before, the
   deletion of `tools/control_plane_base_check.py`.
6. **The README anchor.** "`.github/workflows/verify.yml` runs" stays, and every rewrite inside the
   span `R7-A6P` and `R7-A6I` extract passes their retained forbidden-phrase scans.
7. **Dead code after predicates.** Guard code is removed only when no retained predicate reaches it.
8. **The receipts.** `tools/v3_verifier.py` keeps every code path; `V3-10`'s and `V3-11`'s receipts
   hold from their receipt commits at every stage commit and at `Q`.
9. **The seal records.** Nothing under `verification/seals/` is written (`G12`).
10. **The verdict map.** The guard's top-level verdicts at `E` are `D`'s minus `R7-VIS` and
    `R7-ARCH`, all `PASS`.

## The predicted authority model after V3-12

After this round, these are the mechanisms that can reject a build, and the property each one
protects:

| mechanism | property protected |
|---|---|
| `Lean kernel check` | the zero-import core's proofs are accepted by the Lean kernel |
| `Mathlib bridge`: build | every OIBridge module compiles, so every cited kernel theorem is proved |
| gate `toolchain` | the build entry point exists and the shared glyph header is unique |
| gate `staleness` | every generated `.tex`/`.pdf` matches its source |
| gate `baseline-label` | handover documents name a current baseline |
| gate `voice`, `voice-scope` | manuscript prose carries no revision narration, and the checker scans exactly the manuscript |
| gate `ci-gate-presence` | CI runs the real release gate |
| gate `artifact-placement`, `manifest-drift` | the `verification/` root holds only accounted files, and the migration manifest agrees with its source mapping |
| gate `claims` | no withdrawn result is asserted |
| gate `duplicate` | no paragraph or heading is repeated within a file |
| gate `mirror` | every chapter line is in the consolidated book |
| gate `citation` | every citation resolves, with no duplicate bibliography entry |
| gate `architecture` | the lattice code's invariants hold |
| gate `dependency-label` | no result is labelled derived while it depends on a named condition |
| gate `coverage` | every canonical statement has ledger coverage, and no level claims more than its checkers deliver |
| gate `lean-axioms` | no kernel result depends on `sorryAx`, read from the kernel's axiom report |
| gate `lean-manuscript` | every kernel identifier the manuscripts cite exists and is current |
| gate `legacy-records` | the records of the rounds landed before V3 are byte-identical to their frozen state |
| gate `v3-verifier` | the verifier that decides protocol validity reproduces its conformance corpus exactly |
| gate `v3-receipts` | every native round is protocol-valid: its receipt holds from its receipt commit |
| `Numerical probes`: 55 probes | the exact and numerical claims they compute |
| `Numerical probes`: the guard's 3,142 retained predicates | kernel modules carry no `sorry`, axiom or `native_decide`, print the axioms of exactly their results and state their theorems as frozen; manuscripts state each claim at its evidence and carry no forbidden over-reading; landed rounds' records keep their frozen blobs and readings; `R1`–`R9` compute exactly |

Nothing that can reject a build re-derives the chronology of a control plane, a mandated base, an
execution chain, a landing, a pin or a seal, and nothing reads the host event or a remote ref.
`V1`'s retained predicates and V2's record-integrity content protect the properties above and
decide nothing about a round's protocol validity, which is the receipt's alone.

## Decisions before `F`

1. **V2's form.** Recommended: replace `tools/certificate_verifier.py` with `legacy-records`, a
   byte pin of every legacy record, which protects strictly more than V2's evidence pins and carries
   no chronology. The alternative keeps V2 and cuts it in place: remove `VIS`, `BASE`, `TOPO-E`,
   `TOPO-L`, `LEG-PART` and `POLICY`, add pins for the rows and certificates V2 leaves unpinned, and
   remove the corresponding vectors from its 89-vector corpus.
2. **§A.37's form.** Recommended: condense §A.37 to a record of how the pre-V3 rounds landed, and
   withdraw the owner's option to designate a new §A.37 compatibility round, since no mechanism
   would remain to check one. The alternative keeps §A.37's text and the option, with the lifecycle
   unverified.
3. **The V3 verifier's own checks.** Recommended: move its self-test and corpus into the release
   gate as `v3-verifier`, so the authority's correctness is on the required path, and remove the
   diagnostics job. The alternative keeps the job non-required.
4. **The shape of the execution.** The guard edit removes 342 predicates, the code only they reach
   and 36 message clauses. Recommended: freeze it as the deterministic transformation that produces
   it, the script's SHA-256 and the predicted guard blob, with the retired predicates listed in
   `census.json` by line and text hash; every other file's edits are frozen as texts. The
   alternative splits the execution into a separate round after this census lands.

## What is frozen at `F` and not before

- the governed paths, decided by the answers above;
- the stages, their order satisfying the dependencies, their exact texts and predicted blobs;
- the controls of each stage, among them: the guard's retained predicates all pass and each retired
  predicate's absence is checked by text hash; a mutation of each retained class still fails its
  check; `legacy-records` fails on a one-byte change to an attestation row, a content-only
  certificate, `CV1.json`, `PRA.json` and a V2 evidence file; `v3-receipts` holds on `V3-10` and
  `V3-11` at every stage; the release gate and the workflow parse and `ci-gate-presence` holds;
- the targets, predictions and readings.

## What this round does not do or license

1. It changes no mathematics, no manuscript claim, no Lean file and no ruleset.
2. It writes no seal record, certificate, attestation row, receipt of another round or landed
   record.
3. It licenses no sentence that a retired check was wrong: each was true of its round, and its facts
   remain recorded in that round's notes and certificate.
