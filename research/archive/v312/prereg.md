# Verifier round V3-12 — retirement census: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39: one pull
request from `D`, the control plane drafted on it, execution after the owner designates `F`, and
the round's protocol record a receipt on which `tools/v3_verifier.py --verify-round` must print
`VERDICT  HOLDS`.

> **V3-12 establishes facts and retires no authority.** It lands, as its own record, a census of
> the pre-V3 protocol machinery measured at `D`. The census classifies every predicate of the
> guard and tests each one it would keep against a byte pin of the legacy records. It also fixes
> the complete population of that pin, the disposition of every other surface, the constraints a
> retirement must respect and the authority model a retirement would leave. Every mechanism that
> can reject a build at `D` still runs and gates after this round lands. The retirement is round
> `V3-13`, whose drafting snapshot is this round's certified landing.

## The declarations

```v3-round
round V3-12
kind non-sealing
record-directory verification/infrastructure/round-v3-12-retirement-census/
```

```v3-governed-paths
record AM verification/infrastructure/round-v3-12-retirement-census/
record AM verification/receipts/V3-12.json
```

The record directory holds this preregistration, the census tool `census.py`, its two outputs
`census.json` and `legacy-records.json`, and the result note. The receipt path is
`verification/receipts/V3-12.json`. No execution path is governed: nothing outside the record
directory and the receipt changes.

## The objects

The symbols are the specification's (`verification/infrastructure/v3/architecture.md`, Objects):

- `D` = `81150851f84c8aa1df71dc69013a6ca6f6d71b51`, the head of `main` after `V3-11`'s landing,
  certified by push run 36125130929 with all six jobs green, the release gate 20 of 20 with
  `v3-receipts` holding on two receipts, and the guard 105 PASS and 0 FAIL. The pull request
  begins here. Every measurement in this file was taken at `D`.
- `F` — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- `E` — the certified execution head, which the owner designates.
- `Λ` — the last reconciliation, a merge whose first parent is `main` when it is built and whose
  second parent is `E` (or a superseded receipt commit); it is built with `--no-ff` if `main` is
  still `D`.
- `Q` — the final receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/V3-12.json`.

`V3-9`'s preregistration sketched `V3-12` as the round that retires the old stack. The owner has
split that work: `V3-12` is the census, `V3-13` the retirement. Nothing here binds `V3-13`. Its
preregistration adopts or amends what this census records, and records any disagreement with it
there.

## The census tool

`census.py` is frozen by its content: blob `54beb708bb52825ff60c476d49f4c71d3a3be609`, SHA-256
`77ba82e4996e115da206269e1d60faa36d9e43b65d9aa2a85506a2c1607eee38`, 52,495 bytes. It runs as
`census.py <repository> <commit> <output directory>` and reads git objects at the named commit and
nothing else, so a commit gives the same bytes on any checkout. The census was measured with
CPython 3.11.15; the predicate texts it hashes come from `ast.unparse`, whose output can differ
between Python minor versions, so a replay uses 3.11. `census.py --self-test` runs its
synthetic-guard test.

### What a predicate is

A predicate is a module-level statement of the guard `verification/lean/edge_rigidity_probe.py`
that can change a top-level check's verdict: an assignment or augmented assignment to the check's
accumulator, or an entry written into or appended to a check table (`_<x>_checks`, `_<x>_bad`)
from which the accumulator is computed. They are found by name across the whole module, not in
the span between two `check` calls. Statements inside function bodies are not predicates; they are
reached as helpers.

### The rules

Applied in this order, the first match deciding:

| class | rule |
|---|---|
| `structural` | bookkeeping: an accumulator's initialization, or the line that lists a check table's failed entries |
| `retire-whole` | the predicates of `R7-VIS` and `R7-ARCH`, synthetic regressions of archive-mode chronology |
| `retire-history` | the predicate executes history: a git subprocess, a host-environment read, a read of the prospective seal declaration or baseline, or a filesystem read of `verification/seals/` |
| `redundant` | every file the predicate reads resolves statically, it reads at least one, and each lies in the legacy-records population; or it is one of the thirteen adjudicated predicates below |
| `retire-machinery` | a predicate of `R7-SI1`, `R7-SI2`, `R7-SI3`, `R7-GR1`, `R7-GR2` or `R7-CV1`, whose subject is the retired machinery: the seal validator, the guard's own code text, the V2 store and its wiring |
| `retain` | everything else: it reads a file outside the population, reads no file, or has a read site that does not resolve statically |

**What the predicate executes and reads** includes everything it reaches: the helper functions it
names, called or passed as values, transitively, each name resolved through Python's scopes; the
module-level values it loads, through every definition that can reach it (walking back to the
nearest top-level definition, so both arms of a branch or a `try` count) and every in-place
mutation after the earliest of them; and the control-flow headers (`if` and `while` tests, `for`
iterables, `with` items) that decide whether it, or any of those definitions and mutations, runs.
A predicate's own accumulator or table is not an input of it.

**Reads are resolved statically.** A read site is a call of `open`, a directory listing or an
existence test, or one of the guard's path primitives (`_bb_read`, `_bb_blob`, `_a11p_root`, and
`_artifact`, which maps a name through `verification/migration-manifest.json`). A helper that
passes its own parameter to a read site is resolved at each call, with the argument evaluated
there; a parameter whose default is a reader is a reader. Paths evaluate over string constants,
module constants, concatenation, f-strings, `os.path` joins and literal loop iterables. A name
bound locally never resolves to a module value of the same name. A read site that does not
resolve: a child process; executed text; a function passed as a value whose reads depend on its
own parameters, unless it is passed to a reader parameter; and a call of a name the calling
function rebinds. Reading the migration manifest to locate an artifact is a lookup, not a
protected read.

**Why redundancy retires a predicate.** A redundant predicate's verdict is a function of bytes
that legacy-records pins and of the guard's own code. It held at `D`. While legacy-records holds,
the predicate cannot change its verdict, so it protects nothing that legacy-records does not.

### The adjudications

The resolver leaves thirteen read sites open whose files were read by hand; each reads legacy
records only.

| check | predicates | what they read |
|---|---|---|
| `R7-HYE` | the seal comparison and its two mutation controls | the seal records of `HYA`, `HYB` and `HYE` through the record reader, and `HYE`'s preregistration |
| `R7-NLV`, `R7-SI1` | one drift control each | the pinned record, through a reader that appends one byte to it |
| `R7-SI2` | four drift controls | the same, for its three frozen blobs and its census |
| `R7-SI3` | four drift controls | the same, for its preregistration and amendment |

### The controls in the tool

1. **Completeness.** The module holds 4,199 assignments whose target is a check's accumulator or
   check table; every one precedes its check's call and every one is a predicate. With 3 appends,
   the predicates number 4,202.
2. **V2 agreement.** Every one of the 199 blobs the V2 certificates pin (157 evidence and 42
   control-plane entries, over 151 paths) equals the population's blob for that path.
3. **Adjudications.** Each adjudication names exactly one predicate; an unused one fails the run.
4. **Self-test.** A synthetic guard of 28 predicates covers every rule and each dataflow path above,
   among them a record pin through an injectable reader and its drift control, git inside a helper
   and inside an enclosing test, tables filled from records, from a live file and from git, values
   assigned in both arms of a `try`, a function called through a loop variable, a variable named
   like a nested function, a reader rebound inside a helper, a child process, and an accumulator
   written above an unrelated check.

Run while drafting and not landed: fourteen mutants of the tool, each disabling one mechanism
(in-place mutations, enclosing tests, table appends, reader parameters, literal iterables,
whole-module search, history, unresolved reads, the host environment, child processes, reaching
definitions, functions passed as values, scoped name resolution, rebound callables), are each
rejected by the self-test. Repeated runs at `D` gave identical bytes. Every resolved path exists at
`D` except the glob pattern `verification/lean-mathlib/OIBridge/*.lean` and
`verification/certificates/relocations`, whose absence V2 checks.

## The census at `D`

### The guard

| class | predicates |
|---|---|
| `retain` | 2,492 |
| `redundant` | 1,268 |
| `retire-history` | 291 |
| `retire-machinery` | 49 |
| `retire-whole` | 2 |
| `structural` | 100 |
| **total** | **4,202** |

A retirement would remove 1,610 predicates: 1,268 redundant, 291 history-dependent, 49 of the
retired machinery and 2 synthetic regressions.

- **50 checks are retained whole:** `R1`–`R9`, `R7-FWD`, `R7-OIN`, `R7-CAA`, `R7-INV`,
  `R7-MIN`, `R7-MSP`, `R7-CTN`, `R7-OINN`, `R7-PTR`, `R7-RB0`, `R7-RB1`, `R7-MAX`, `R7-LIFT`,
  `R7-SUB`, `R7-SCAL`, `R7-INST`, `R7-MIG`, `R7-FLOW`, `R7-PHASE`, `R7-PROP`, `R7-Q3`, `R7-Q3P`,
  `R7-EXEC`, `R7-LSRC`, `R7-SRCP`, `R7-C5D`, `R7-PCL`, `R7-CCS`, `R7-SMC`, `R7-RPF`, `R7-PFE`,
  `R7-DCA`, `R7-DIB`, `R7-FSS`, `R7-QSTAR`, `R7-AUDA`, `R7-CT2`, `R7-CT3`, `R7-CT3B`, `R7-CT3C`
  and `R7-CT3D`.
- **14 checks lose every predicate:** `R7-VIS` and `R7-ARCH`; `R7-SI1`, `R7-SI2`, `R7-SI3`,
  `R7-GR1`, `R7-GR2` and `R7-CV1`, the infrastructure rounds; and `R7-BRIDGE`, `R7-DILMAP`,
  `R7-SRCA`, `R7-DILCH`, `R7-RBR` and `R7-ABR`, whose every predicate is a shape contract on a
  frozen note or a pin of one, or a chronology walk.
- **41 checks are split.** After a retirement the guard would carry 91 checks.

What the 2,492 retained predicates read, a predicate counted once for each area it reads: Lean
kernel modules 1,572; live verification notes 781 (`verification/README.md` 161,
`verification/ROADMAP.md` 86, the programme indexes and live audits); the papers and the book 236;
companion probes 53; the workflow 10; `tools/claims_check.py` and
`tools/lean_manuscript_census.py` 3 each; `AGENTS.md` 2 and `tools/release_gate.py` 1, all
`R7-MSP`; the guard's own text 3. 2,393 read a file outside the population; 33 read no file and
compute exactly; 66 have a read site that does not resolve and are retained on that ground.

The 291 history-dependent predicates execute git (283), the host environment (202), the seal
declaration or baseline (155) or a filesystem read of `verification/seals/` (12), most more than
one.

**Against the first draft of this census.** The first draft classed 3,488 predicates as 2,099
substantive, 1,043 historical, 342 retired and 4 structural. Of its 1,043 historical predicates,
1,039 are redundant here, and 4 are retained because they read the live hydrodynamics
`PROGRAMME.md`. Of its 2,099 substantive predicates, 1,830 are retained, 182 are redundant (shape
contracts on frozen result notes), 79 are accumulator initializations and 8 execute history
through an enclosing test or a mutated table the draft did not follow. The draft's span-bounded
extraction missed 714 predicates, among them 551 of `R7`'s kernel-module checks and the eight
checks (`R7-DILL2`, `R7-AUDA`, `R7-AUDB`, `R7-CT2`, `R7-CT3`, `R7-CT3B`, `R7-CT3C`, `R7-CT3D`)
that accumulate far from their call: 658 retained, 39 redundant, 3 history-dependent and 14
structural. Of the draft's 342 retired predicates, 280 are history-dependent here, 49 are of the
retired machinery, 2 are synthetic regressions, 8 are redundant and 3 are bookkeeping; its seven
hand overrides need no override under the rules above, four being history-dependent and three
redundant.

### The legacy-records population

`legacy-records.json` holds `closed_namespaces`, a sorted list of directories, and `records`, a
sorted map from path to blob:

- **75 closed namespaces:** `verification/certificates/` (90 records), `verification/seals/` (34),
  and the 73 legacy round directories (174). A legacy round directory holds a
  `preregistration.md` without a `v3-round` block opener line; `V3-10`'s and `V3-11`'s directories
  hold one and are native, as is this round's. No round directory lies inside another.
- **5 individual pins:** the V2 evidence outside those namespaces,
  `verification/audits/foundations/a6-covariance-propagation-audit.md`,
  `act11-scope-propagation-audit.md`, `act11-scope-propagation-open-frontier-amendment.md` and
  `act12-scope-propagation-audit.md` in the same directory, and
  `verification/audits/operational/stochastic-observer-interface-audit.md`.
- **303 records** in all, each a regular file.
- **Not records:** `verification/certificates/conformance/`, the V2 implementation's 90-file
  conformance corpus, which tests the implementation and goes with it.

The population pins what V2 left unpinned: the 36 attestation rows, the 16 content-only
certificates, `CV1.json`, the seal record `PRA.json`, `legacy-v1-owned.json` and
`live-policy.json`.

**Legacy rounds never executed.** Five legacy directories hold a merged control plane and no
execution: `oi-qm/h-bell/round-hb-1-obligation-shape`, `oi-qm/reconstruction/
round-bg-1-integer-classification`, `physical-realization/round-c4-3-preparation-scope`,
`substratum/lemma-24-1b-framework-data` and `substratum/lemma-24-1c-spanning-class-decision`, all
under `verification/programmes/`. The population closes them with the rest. With §A.37 a record
of past practice, continuing any of them is a new native round with its own record directory,
whose preregistration may cite the legacy freeze.

### The other surfaces

**The round-certificate verifier `tools/certificate_verifier.py` (V2)**, 20 check families:

| families | what they check | disposition |
|---|---|---|
| `VIS`, `BASE`, `TOPO-E`, `TOPO-L`, `LEG-PART`, `POLICY` | the §A.37 visibility union, control-plane merges, sealed heads and landings, the V1/V2 partition, round-owned live policy (none exists) | retire: chronology and ownership |
| `TOPO-EXIST`, `TOPO-TREE`, `BASEONLY` | recorded commits exist, a recorded tree is the sealed head's, a base is an ancestor | retire: facts about immutable objects, false only if history is rewritten or missing |
| `STORE`, `SCH-CERT`, `SCH-ROW`, `PROV`, `ROW-CERT`, `DEP`, `RELOC`, `LEG-PREREG` | the records present, well formed and consistent | redundant: functions of bytes legacy-records pins |
| `EVID` | 157 evidence entries, over 151 paths, unchanged | redundant: legacy-records pins those 151 paths and 152 more records |
| `CORPUS` | the implementation reproduces its 89 vectors | retire with the implementation |

**The release gate, `tools/release_gate.py`**, 20 steps at `D`:

| steps | disposition |
|---|---|
| `toolchain`, `staleness`, `baseline-label`, `voice`, `voice-scope`, `ci-gate-presence`, `artifact-placement`, `manifest-drift`, `claims`, `duplicate`, `mirror`, `citation`, `architecture`, `dependency-label`, `coverage`, `lean-axioms`, `lean-manuscript` | retain |
| `v3-receipts` | retain: the native-round protocol verdict |
| `certificate-verifier` | retire, replaced by `legacy-records` |
| `control-plane-lint` | retire: it lints §A.37 control planes, and on a native preregistration it can only fail falsely |

**The workflow, `.github/workflows/verify.yml`**, six jobs at `D`:

| job | disposition |
|---|---|
| `Lean kernel check`, `Mathlib bridge`, `Numerical probes` (required) | retain; the guard inside `Numerical probes` keeps its retained predicates |
| `Control-plane base check` | retire: §A.37 `D`/`B`/`M` preconditions only |
| `Certificate verifier` | retire: shadow V2 run, gating nothing |
| `V3 verifier diagnostics` | retire: its self-test and corpus move into the release gate; its projection compares V3 with V2's attestation rows |

**Tools.** `tools/certificate_verifier.py`, `tools/control_plane_lint.py` and
`tools/control_plane_base_check.py` retire with their steps and jobs. The 24 historical files that
carry a `control-plane-preconditions` block are records and stay as they are.

**§A.37 and its callers.** §A.37 is the lifecycle of the rounds begun before `V3-11`'s landing.
Its text describing the guard's ancestry checks, archive mode, `L` and `P`, and seal gating
describes mechanisms a retirement removes. `R7-SI2` and `R7-SI3` pin 26 of its phrases; both lose
every predicate.

**Seal state.** `verification/seals/` holds 34 records (28 `sealed`, 6 `base-only`), the guard's
seal manifest. Its readers at `D` are the guard's seal machinery, V2's evidence pins (33 of 34) and
the V3 verifier's authorization rule. `V3`'s `G12` defines a round's own seal record path,
`verification/v3-seals/<round>.json`. `verification/seals/` is legacy state, which legacy-records
keeps immutable. At `D` the specification's `G12` section and the verifier's authorization rule
also list `verification/seals/` among the paths no V3 round may change, calling it the seal state
of protocol 2. V2 pins it but does not own it.

**The maintained documentation.** 62 groups of statements concern the machinery: 21 to rewrite, 16
to reframe as a record of past practice, 25 to keep. 16 are false or misleading at `D`, among them
`AGENTS.md` 77–87, a review rule for frozen control planes that a native round cannot use;
`AGENTS.md` 653–667, which calls every round two pull requests; `verification/README.md`
2519–2584, which counts 22 seal records where there are 34 and calls the retired legacy seal
constants read; `verification/README.md` 2641, which says CI is three jobs; and
`verification/infrastructure/v3/architecture.md` 382–385.

## The proposed authority model after `V3-13`

These are the mechanisms that would reject a build, and what each protects:

| mechanism | property protected |
|---|---|
| `Lean kernel check` | the zero-import core's proofs are accepted by the Lean kernel |
| `Mathlib bridge`: build | every OIBridge module compiles, so every cited kernel theorem is proved |
| gate `toolchain` | the build entry point exists and the shared glyph header is unique |
| gate `staleness` | every generated `.tex`/`.pdf` matches its source |
| gate `baseline-label` | no document names a superseded baseline |
| gate `voice`, `voice-scope` | manuscript prose carries no revision narration, and the checker scans exactly the manuscript |
| gate `ci-gate-presence` | CI runs the real release gate |
| gate `artifact-placement`, `manifest-drift` | the `verification/` root holds only accounted files, and the migration manifest agrees with its source mapping |
| gate `claims` | no withdrawn result is asserted |
| gate `duplicate` | no paragraph is repeated within a file |
| gate `mirror` | every chapter line is in the consolidated book |
| gate `citation` | every probe citation resolves |
| gate `architecture` | the lattice code's invariants hold |
| gate `dependency-label` | no result is labelled derived while it depends on a named condition |
| gate `coverage` | every canonical statement has ledger coverage, and no level claims more than its checkers deliver |
| gate `lean-axioms` | no kernel result depends on `sorryAx` |
| gate `lean-manuscript` | every kernel identifier the manuscripts cite exists and is current |
| gate `legacy-records` | every legacy record keeps its blob, and nothing is added to a closed namespace |
| gate `v3-self-test`, `v3-corpus` | the verifier that decides protocol validity passes its self-test and reproduces its conformance corpus exactly: regression evidence for the implementation |
| gate `v3-receipts` | every native round is protocol-valid: its receipt holds from its receipt commit |
| `Numerical probes`: companion probes | the exact and numerical claims they compute |
| `Numerical probes`: the guard's 2,492 retained predicates in 91 checks | kernel modules carry no `sorry`, axiom or `native_decide` and state their theorems as frozen; manuscripts and live notes state each claim at its evidence and carry no forbidden over-reading; `R1`–`R6`, `R8` and `R9` compute exactly |

`v3-self-test` and `v3-corpus` are separate steps from `v3-receipts`: the first two are regression
evidence about the verifier's implementation; the third is the protocol verdict on native rounds.

Nothing that could reject a build would re-derive the chronology of a control plane, a mandated
base, an execution chain, a landing, a pin or a seal, and nothing would read the host event or a
remote ref.

**What nothing would check.** Recorded here so that it is decided rather than inherited:

1. the existence and ancestry of the commits the legacy records name, which rest on the
   repository's history and its branch protection;
2. the immutability after landing of a native round's record directory (`V3-10`, `V3-11`, this
   round's): `--receipts` verifies each receipt from the commit that last wrote it and reads no
   later change to the record directory;
3. the host attestations a receipt records, which by §A.39 no predicate reads.

## Constraints on `V3-13`

These follow from the census. `V3-13`'s preregistration adopts them or records why not.

1. **Base.** `V3-13`'s `D` is this round's certified landing. At that commit `census.py` produces
   `legacy-records.json` byte-identical to this round's, since the population reads only legacy
   directories and this round's directory is native.
2. **No unguarded records.** One commit installs `legacy-records` (the manifest, byte-identical to
   this round's, its checker and its gate step) and removes V2 (its gate step, its job, the tool
   and the conformance corpus). No commit has neither. `R7-CV1`, which pins V2's wiring, is removed
   in that commit or earlier.
3. **The guard edit.** It removes exactly the 1,610 predicates this census retires, identified by
   check, line at `D` and text hash, with the bookkeeping that serves only them and the code only
   they reach. The 2,492 retained predicates keep their text hashes. The guard's verdict map
   afterwards is `D`'s without the 14 emptied checks, all `PASS`.
4. **Retained anchors.** An edit to `verification/README.md`, `verification/ROADMAP.md`,
   `.github/workflows/verify.yml`, `AGENTS.md`, `tools/release_gate.py` or the guard keeps every
   retained predicate that reads that file passing: 161, 86, 10, 2, 1 and 3 predicates. Among them,
   `R7-A6P` and `R7-A6I` extract `verification/README.md` up to the words
   "`.github/workflows/verify.yml` runs", which stay.
5. **§A.37's pinned phrases.** `R7-SI2` and `R7-SI3` are removed in the commit that edits §A.37 or
   earlier.
6. **Steps and jobs before tools.** Each gate step and workflow job leaves in the commit that
   deletes its tool or earlier, and `ci-gate-presence` holds at every commit.
7. **The V3 checks.** `v3-self-test` and `v3-corpus` enter the gate in the commit that removes the
   diagnostics job or earlier, so no commit runs them nowhere.
8. **The receipts.** `tools/v3_verifier.py`'s verdicts do not change: `V3-10`'s, `V3-11`'s and this
   round's receipts hold at every stage commit and at `Q`.
9. **The records.** Nothing in the population is written. The one removal under a closed namespace
   is the conformance corpus, which is not in it.
10. **§A.37 as history.** §A.37 becomes a record of how the pre-V3 rounds landed and the
    vocabulary needed to read their records, with no provision for designating a new §A.37 round;
    §A.39 governs every new round, and a repair or migration of legacy state is itself a native
    round.
11. **Local checks.** `AGENTS.md` states the division of verification work: cheap deterministic
    checks run locally, the Lean, Mathlib, release-gate and full-probe runs run in CI, and the exact
    host runs are the source of certification.

## Questions for `V3-13`'s freeze

1. **`G12` and `verification/seals/`.** Whether the specification's `G12` section and the
   verifier keep `verification/seals/` among the paths no native round may change, as a second
   guard beside legacy-records, or drop it so legacy-records alone governs legacy state. Either way
   its description as protocol 2's seal state is corrected; dropping it changes the verifier.
2. **Changes to the manifest.** Whether a change to `legacy-records.json` must be the governed
   execution of a native round whose receipt holds, or any commit that changes a record and the
   manifest together passes.
3. **Native records after landing.** Whether a check is added for item 2 of *What nothing would
   check*, in `--receipts` or beside it.
4. **The never-executed legacy rounds.** Whether any of the five is re-preregistered as a native
   round.
5. **The probes checkout.** The `Numerical probes` job checks out full history only for the guard's
   git reads; with those retired it could use the default depth.
6. **The verifier's projection.** Whether `tools/v3_verifier.py` keeps its projection mode, which
   reads V2's attestation rows and would then have no caller, so that the file stays unchanged.

## The execution

Two stage commits and the result note, each with one parent:

1. **Stage 1** adds `census.py` to the record directory, blob
   `54beb708bb52825ff60c476d49f4c71d3a3be609`.
2. **Stage 2** adds the output of `python3 census.py . 81150851f84c8aa1df71dc69013a6ca6f6d71b51
   verification/infrastructure/round-v3-12-retirement-census/`, run at the stage 1 commit:
   `census.json`, blob `a39ddc49eaa7a9527e052e30e40a8f2cdd5712c8`, and `legacy-records.json`, blob
   `9e48bd31797e1673f03807e699a10ae4a0b960c7`.
3. **The result note** `result.md`, whose commit is `E`.

## Targets

| target | question | outcome if it holds | predicted |
|---|---|---|---|
| `V312-0` | is `F` attested and designated? | `F-DESIGNATED` | holds, strong |
| `V312-1` | does stage 1 land the frozen tool, and does its self-test pass? | `TOOL-LANDED` | holds, strong |
| `V312-2` | does the tool at `D` reproduce the predicted outputs? | `CENSUS-REPRODUCED` | holds, strong |
| `V312-3` | is nothing outside the record directory changed, and does every gate still pass? | `NOTHING-RETIRED` | holds, strong |
| `V312-4` | is `E` attested and designated? | `E-DESIGNATED` | holds, strong |
| `V312-5` | does `--verify-round Q` hold? | `RECEIPT-HOLDS` | holds, strong |

The checkpoints:

- **`C1`** (stage 1): `census.py` has the frozen blob and SHA-256.
- **`C2`** (stage 1): `census.py --self-test` prints `SELF-TEST  28 predicates, all as expected`.
- **`C3`** (stage 2): the stage 2 files have the predicted blobs, and a second run at `D` into a
  scratch directory gives the same bytes.
- **`C4`** (stage 2): `census.json` reports 4,202 predicates, the class totals and check
  dispositions above, 4,199 accumulator writes and 199 agreeing V2 pins; `legacy-records.json`
  holds 303 records in 75 closed namespaces.
- **`C5`** (`E`): `git diff --no-renames --name-status D E` lists only paths under the record
  directory, each an addition.
- **`C6`** (`E`): the dispatch run at `E` has all six jobs green, the guard reports 105 PASS and 0
  FAIL with its verdict map identical to `D`'s, and the release gate passes 20 of 20 with
  `v3-receipts` holding on two receipts.
- **`C7`** (`Q`): `tools/v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`, and
  `--receipts Q` holds on three receipts.

**The status rule.** Each target's outcome is its checkpoints' verdict. If `C1`, `C2` or `C3`
fails, the census is not the one frozen here: the round halts under the specification's `S12` and
records the discrepancy; the frozen census is not repaired. A failure of `C6` that the round's
paths cannot cause is diagnosed and recorded before `E` is brought for designation.

## Hazards

1. **The Python version.** Predicate text hashes come from `ast.unparse`; a replay under a
   different minor version can change them. The census names 3.11.
2. **Static resolution.** The census does not run the guard: it reads the guard's syntax. A read the
   resolver cannot resolve keeps its predicate, so an unresolved read errs toward retention; the
   thirteen adjudications are the only exceptions, each read by hand.
3. **A snapshot.** The census describes the guard's blob at `D`,
   `2eab600fb8cd078b3dd0f3867a6e7420cfc2b79f`. A later change to the guard is outside it, and
   constraint 1 makes `V3-13` start from this round's landing.

## What this round does not do or license

1. It changes no mathematics, no manuscript, no Lean file, no guard, no gate, no workflow, no
   ruleset and no record of another round.
2. It retires nothing: every mechanism that can reject a build at `D` still does at its landing.
3. It licenses no sentence that a retired check was wrong. Each was true of its round, and its
   facts remain recorded in that round's notes and certificate.
