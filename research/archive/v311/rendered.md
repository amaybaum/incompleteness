# Verifier round V3-11 — authority cutover: PREREGISTRATION

**Status: control plane of a provisional V3 pilot.** This round runs under `AGENTS.md` §A.39 as it
stands at `D`: one pull request from `D`, the control plane drafted on it, execution after the owner
designates `F`, and the round's protocol record a receipt checked by `tools/v3_verifier.py
--verify-round`. The owner's designation of `F` is the authorization §A.39 requires.

> **The receipt becomes the V3 verdict for new rounds.** The execution gives the verifier a
> `--receipts` mode, runs it from the release gate that the required `Mathlib bridge` check already
> runs, and rewrites §A.39 as the default lifecycle with §A.37 as the compatibility lifecycle. It
> changes no mathematics, no guard, no certificate, no seal and no ruleset.

## The declarations

```v3-round
round V3-11
kind non-sealing
record-directory verification/infrastructure/round-v3-11-authority-cutover/
```

```v3-governed-paths
record AM verification/infrastructure/round-v3-11-authority-cutover/
record AM verification/receipts/V3-11.json
execution M tools/v3_verifier.py
execution M tools/release_gate.py
execution M .github/workflows/verify.yml
execution M AGENTS.md
execution M verification/infrastructure/v3/architecture.md
execution M verification/README.md
```

The record directory holds this preregistration and the result note. The receipt path is
`verification/receipts/V3-11.json`. The six execution paths may only be modified. Nothing else may
change.

## The objects

The symbols are the specification's (`verification/infrastructure/v3/architecture.md`, Objects):

- `D` = `76a2c4dd82f0bf0dc8113256bf76bc02171e1337`, the head of `main` after `V3-10`'s landing,
  certified by push run 36109549145 with all six jobs green. The pull request begins here. Every
  measurement in this file was taken at `D`.
- `F` — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- `E` — the certified execution head, which the owner designates.
- `Λ` — the last reconciliation, a merge whose first parent `LB` is `main` when it is built and
  whose second parent is `E` (or a superseded receipt commit); it is built with `--no-ff` if
  `main` is still `D`.
- `Q` — the final receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/V3-11.json`.

## What the cutover means, frozen

These four statements are what the execution installs, and the frozen texts below say them:

1. **The V3 verdict.** A native round is protocol-valid exactly when `--verify-round Q` prints
   `VERDICT  HOLDS` on its receipt commit. The release gate's `v3-receipts` step runs
   `tools/v3_verifier.py --receipts` at the commit under check. That mode verifies every receipt in
   the tree from its receipt commit, the commit reachable from the checked commit that last wrote
   the receipt, and exits 1 on any receipt that does not hold. The required `Mathlib bridge` check
   runs the gate, so a receipt that does not hold fails a required check.
2. **Host attestations.** The owner's designations and the check runs stay recorded in the receipt
   and outside the verifier's semantics: no predicate reads them.
3. **V1 and V2 during the transition.** The guard and the round-certificate verifier keep running,
   and a failure of either still fails the release gate: they remain compatibility and
   repository-integrity gates until a later round decides which of their checks survive. They do not
   decide whether a native round is protocol-valid.
4. **The lifecycles.** From this round's landing §A.39 governs every new round, and §A.37 governs
   the rounds begun before that landing and any later round the owner designates a §A.37
   compatibility round. Each round keeps the protocol under which it landed.

The standalone workflow job keeps running the verifier's self-test, corpus and projection, and is
renamed `V3 verifier diagnostics`: it is not a required check, and it is not where the V3 verdict
is decided. Its job id, `v3-shadow-verifier`, is unchanged.

## Measurements at `D`

- **Name freedom.** `v3-11`, `round-v3-11`, `V311-`, `receipts/V3-11`, `v3-receipts`,
  `--receipts` and `V3 verifier diagnostics` occur nowhere in the tree at `D`; `authority-cutover`
  occurs only inside `SI-2`'s directory name, `round-si-2-authority-cutover`.
  `verification/receipts/` holds one file, `V3-10.json`, and `verification/v3-seals/` does not
  exist.
- **The authority surfaces.** The words `SHADOW ONLY` occur in the workflow's V3 job comment, in
  `tools/v3_verifier.py`'s docstring and in its shadow report banner. The preamble of
  `architecture.md`, §A.39 and `verification/README.md` restrict V3 to provisional pilots. The
  release gate's only protocol verdict is the `V2` step `certificate-verifier --mode authoritative`.
  The `Mathlib bridge` job checks out with the default shallow clone; the `Numerical probes`,
  `Control-plane base check`, `Certificate verifier` and V3 jobs check out with `fetch-depth: 0`.
- **What pins those surfaces.** The guard reads the workflow for the `Certificate verifier` job in
  shadow mode and for `repertoire_lie`, reads the release gate for the `certificate-verifier`
  authoritative step and the `lean-manuscript` step, and reads `AGENTS.md` for the phrases its
  `R7-MSP`, `R7-SI2` and `R7-SI3` blocks require, all of them in §A.35 and §A.37. It reads nothing
  of §A.39, of the V3 job, of `tools/v3_verifier.py` or of `architecture.md`. The corpus's command-
  line vectors test only argument refusal.
- **Full history in the gate.** At `D` with full history, `tools/certificate_verifier.py --mode
  authoritative` prints `authoritative OK (0 failure(s))`: it fetches the history it needs from a
  shallow checkout and reads the same with a full one. `tools/control_plane_lint.py` passes; with
  full history it also lints the pull request's own additions (`origin/main...HEAD`), which is how
  it was built to run. No other gate step invokes git.
- **Rehearsal.** The whole lifecycle was run at `D` in a scratch worktree, with placeholder
  attestation records, by the script whose SHA-256 the result note records: `F`, the three stage
  commits with every control below, the result note, a `--no-ff` reconciliation onto `D`, and a
  receipt commit built by `tools/v3_receipt.py`. Every predicted blob was produced, every control
  was as predicted, `--verify-round` printed `VERDICT  HOLDS` on the receipt commit, and the gate's
  `v3-receipts` step, run alone at a synthetic merge of that commit into `D`, passed on two
  receipts.

## The execution, FROZEN

The execution is four commits after `F`, each with one parent: one commit per stage, then the
result note, which is `E`. Each stage applies its edits below, in order, to the files as they stand
at its parent: in each edit the first text occurs exactly once in the file and is replaced by the
second. Nothing else in any file changes.

| stage | path | blob at `D` | predicted blob |
|---|---|---|---|
| 1 | `tools/v3_verifier.py` | `ccfbe813` | `b63add13bd519df3ec1d6a33323c2aac8eca611e` |
| 2 | `tools/release_gate.py` | `ca851bef` | `346192312603df4edf705e1d65c38e998af5afa3` |
| 2 | `.github/workflows/verify.yml` | `d14d1938` | `fb2072b6cd8e323399d5748fd303d90c399a2cd6` |
| 3 | `AGENTS.md` | `864494c1` | `59896fa5738ae117bf6726a19c05156a78a17c0e` |
| 3 | `verification/infrastructure/v3/architecture.md` | `f699471b` | `ac9c3ec4aeb4294bda3efc671ac8e626f0bcc88f` |
| 3 | `verification/README.md` | `e8a5c383` | `e1bbd08aa68c50812fd56cd78f48b9fea2121202` |

### Edit 1 — stage 1, `tools/v3_verifier.py`

The text at the parent:

```text
"""v3_verifier.py -- the V3 shadow verifier (round V3-2).

SHADOW ONLY. This tool implements the protocol-3 specification
(verification/infrastructure/v3/architecture.md) and reports. It decides nothing: no verdict it
prints changes any exit status, nothing required invokes it, and V1 and V2 remain the only
mechanisms that accept or reject a build, a pull request or a round. It has no authoritative mode.
```

Its replacement:

```text
"""v3_verifier.py -- the V3 verifier (round V3-2; the V3 verdict from round V3-11).

This tool implements the protocol-3 specification (verification/infrastructure/v3/architecture.md).
Its --receipts mode is the V3 verdict the release gate runs: it verifies every receipt in a
commit's tree from the commit that last wrote it and exits 1 on any receipt that does not hold. The
projection over the V2 attestation rows, and the shadow report that prints it, gate nothing. V1 and
V2 keep running beside it; they do not decide whether a native round is protocol-valid.
```

### Edit 2 — stage 1, `tools/v3_verifier.py`

The text at the parent:

```text
    --reachable <C> <Q>            a diagnostic, never a verdict: whether Q is an ancestor of C
```

Its replacement:

```text
    --reachable <C> <Q>            a diagnostic, never a verdict: whether Q is an ancestor of C
    --receipts <C>                 every receipt in C's tree, verified from the commit reachable
                                   from C that last wrote it; exit 1 on any that does not hold
```

### Edit 3 — stage 1, `tools/v3_verifier.py`

The text at the parent:

```text
    except Undecidable as u:
        return 'undecidable', u.code
```

Its replacement:

```text
    except Undecidable as u:
        return 'undecidable', u.code


RECEIPT_DIR = b'verification/receipts/'
RECEIPT_PATH = re.compile(rb'verification/receipts/[A-Z0-9]+(-[A-Z0-9]+)*\.json')


def receipts(repo, c):
    """(all hold, lines): every receipt in C's tree, each verified from its receipt commit, the
    commit reachable from C that last wrote it. A path under verification/receipts/ that is not a
    receipt path fails, and so does a receipt whose receipt commit does not hold. UNDECIDABLE, a
    shallow repository included, is never promoted to HOLDS."""
    try:
        repo.need(c)
        paths = sorted(p for p in repo.entries(c) if p.startswith(RECEIPT_DIR))
    except Undecidable as u:
        return False, ['RECEIPTS  UNDECIDABLE  %s' % u.code]
    lines, ok = [], True
    for p in paths:
        name = p.decode('utf-8', 'replace')
        if not RECEIPT_PATH.fullmatch(p):
            lines.append('RECEIPT  %s  FAILS  s10:receipt-path' % name)
            ok = False
            continue
        out = repo.run(['rev-list', '-n', '1', c, '--', name])
        q = out.decode().strip() if out else ''
        if not q:
            lines.append('RECEIPT  %s  UNDECIDABLE  undecidable:receipt-commit' % name)
            ok = False
            continue
        verdict, codes, _att = verify_round(repo, q)
        lines.append('RECEIPT  %s  Q %s  %s%s' % (name, q, verdict,
                                                   '  ' + ', '.join(codes) if codes else ''))
        ok = ok and verdict == 'HOLDS'
    lines.append('RECEIPTS  %d receipt(s), %s' % (len(paths), 'all hold' if ok else 'NOT ALL HOLD'))
    return ok, lines
```

### Edit 4 — stage 1, `tools/v3_verifier.py`

The text at the parent:

```text
         '--reachable <C> <Q> | --project <subject> | --mode shadow --subject <commit>')
```

Its replacement:

```text
         '--reachable <C> <Q> | --receipts <C> | --project <subject> | '
         '--mode shadow --subject <commit>')
```

### Edit 5 — stage 1, `tools/v3_verifier.py`

The text at the parent:

```text
            print('REACHABLE %s' % (code if code else state))
            return 0
```

Its replacement:

```text
            print('REACHABLE %s' % (code if code else state))
            return 0
        if argv[:1] == ['--receipts'] and len(argv) == 2:
            c = check_oid(argv[1])
            ok, lines = receipts(Repo(cwd), c)
            print('\n'.join(lines))
            return 0 if ok else 1
```

### Edit 6 — stage 1, `tools/v3_verifier.py`

The text at the parent:

```text
            print('v3_verifier shadow report -- SHADOW ONLY: this report gates nothing; V1 and V2 '
                  'remain authoritative')
```

Its replacement:

```text
            print('v3_verifier shadow report -- DIAGNOSTIC: this report gates nothing; the V3 '
                  'verdict is --receipts, run by the release gate')
```

### Edit 7 — stage 2, `tools/release_gate.py`

The text at the parent:

```text
                       nothing; this step is where V2 can reject a build.
```

Its replacement:

```text
                       nothing; this step is where V2 can reject a build.
  v3-receipts          the V3 verdict, from round V3-11: every receipt in the
                       tree, verified by tools/v3_verifier.py --receipts from
                       the commit that last wrote it. A receipt is data no other
                       check reads, so this step is where a native round whose
                       receipt does not hold can reject a build. V1 and V2 keep
                       running beside it and can still fail the gate; they do
                       not decide whether a native round is protocol-valid.
```

### Edit 8 — stage 2, `tools/release_gate.py`

The text at the parent:

```text
        label = sys.argv[sys.argv.index('--label') + 1]
    checks = [
```

Its replacement:

```text
        label = sys.argv[sys.argv.index('--label') + 1]
    # the commit under check, located here because tools/v3_verifier.py reads no ref: the gate
    # names the commit, and a failed lookup leaves an empty argument, which the verifier refuses
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                          text=True).stdout.strip()
    checks = [
```

### Edit 9 — stage 2, `tools/release_gate.py`

The text at the parent:

```text
                      [sys.executable, "tools/certificate_verifier.py", "--mode", "authoritative"]),
```

Its replacement:

```text
                      [sys.executable, "tools/certificate_verifier.py", "--mode", "authoritative"]),
        # v3-receipts: the V3 verdict (round V3-11). Every receipt under verification/receipts/,
        # verified from the commit that last wrote it; a receipt that does not hold, or a
        # repository too shallow to decide, fails the gate. It needs full history, so the
        # workflow's Mathlib bridge job checks out with fetch-depth: 0.
        ("v3-receipts",
                      [sys.executable, "tools/v3_verifier.py", "--receipts", head]),
```

### Edit 10 — stage 2, `.github/workflows/verify.yml`

The text at the parent:

```text
  # able to obscure the state of the zero-import core gate above.
  bridge:
    name: Mathlib bridge
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

```

Its replacement:

```text
  # able to obscure the state of the zero-import core gate above. fetch-depth: 0 is load-bearing
  # for the release gate's v3-receipts step, which verifies each receipt from the commit that last
  # wrote it and fails on a shallow repository (round V3-11).
  bridge:
    name: Mathlib bridge
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

```

### Edit 11 — stage 2, `.github/workflows/verify.yml`

The text at the parent:

```text
  # V3-2: the V3 shadow verifier, SHADOW ONLY. Not a required check, not invoked by the release
  # gate, and no other job depends on it; V1 and V2 remain authoritative. Self-test and corpus go
  # red only on a defect of the shadow itself; the shadow report always exits 0. fetch-depth: 0
  # gives the corpus's repository vectors and the projection the history they read.
  v3-shadow-verifier:
    name: V3 shadow verifier
```

Its replacement:

```text
  # V3-2: the V3 verifier's diagnostics. Not a required check, and no other job depends on it: the
  # V3 verdict is the release gate's v3-receipts step, which the required Mathlib bridge check runs
  # (round V3-11). Self-test and corpus go red only on a defect of the verifier itself; the shadow
  # report, the projection over the V2 attestation rows, always exits 0. fetch-depth: 0 gives the
  # corpus's repository vectors and the projection the history they read.
  v3-shadow-verifier:
    name: V3 verifier diagnostics
```

### Edit 12 — stage 3, `AGENTS.md`

The text at the parent:

```text
shape explicitly as no guard, no pin, `E` → `L`, so its meaning is unchanged. A
preregistration is not amended to track later vocabulary, and none needs to be.
```

Its replacement:

```text
shape explicitly as no guard, no pin, `E` → `L`, so its meaning is unchanged. A
preregistration is not amended to track later vocabulary, and none needs to be.

From `V3-11`'s landing this rule is the compatibility lifecycle, not the default. It governs the
rounds begun before that landing, which keep the protocol under which they landed, and a later round
only when the owner designates its preregistration a §A.37 compatibility round. Every other round
runs under §A.39.
```

### Edit 13 — stage 3, `AGENTS.md`

The text at the parent:

```text
## §A.39 Provisional native V3 rounds

§A.37 remains the default lifecycle for every round, and it governs the round that adopted this
rule, `V3-9`. A round whose preregistration the owner authorizes as a **provisional V3 pilot** runs
instead under the native lifecycle of `verification/infrastructure/v3/architecture.md`, which is
operative for such rounds and no others:
```

Its replacement:

```text
## §A.39 Native V3 rounds

From `V3-11`'s landing every new round runs under the native lifecycle of
`verification/infrastructure/v3/architecture.md`, unless the owner designates its preregistration a
§A.37 compatibility round. `V3-9`, which adopted this section, ran under §A.37; `V3-10` and `V3-11`
ran under it as provisional pilots. Each round keeps the protocol under which it landed:
```

### Edit 14 — stage 3, `AGENTS.md`

The text at the parent:

```text
`F` is designated, the pilot's branch is held at exactly `F` and the workflow is dispatched on it
```

Its replacement:

```text
`F` is designated, the round's branch is held at exactly `F` and the workflow is dispatched on it
```

### Edit 15 — stage 3, `AGENTS.md`

The text at the parent:

```text
**A halted pilot.** A pilot that halts after `F` instead of reaching a designated `E` follows the
```

Its replacement:

```text
**A halted round.** A round that halts after `F` instead of reaching a designated `E` follows the
```

### Edit 16 — stage 3, `AGENTS.md`

The text at the parent:

```text
A provisional pilot carries no guard clause, seal manifest record, round certificate or
`control-plane-preconditions` block: its receipt, `verification/receipts/<round>.json`, is its
protocol record. It leaves `V1` and `V2` authority unchanged. The guard and the release gate run on
its pull request as on any other, and they remain the repository's authoritative checks until a
later round makes V3 the default.
```

Its replacement:

```text
**Authority.** A native round is protocol-valid exactly when `tools/v3_verifier.py --verify-round Q`
prints `VERDICT  HOLDS` on its receipt commit `Q`. The release gate's `v3-receipts` step runs
`tools/v3_verifier.py --receipts` at the commit under check: it verifies every receipt in the tree
from the commit that last wrote it and fails on any that does not hold, so the required
`Mathlib bridge` check carries the V3 verdict. The host attestations a receipt records, the owner's
designations and the check runs, are outside the verifier's semantics: no predicate reads them.

A native round carries no guard clause, seal manifest record, round certificate or
`control-plane-preconditions` block: its receipt, `verification/receipts/<round>.json`, is its
protocol record. The guard (`V1`) and the round-certificate verifier (`V2`) keep running on its pull
request as on any other, and a failure of either still fails the release gate: until a later round
decides which of their checks survive, they are compatibility and repository-integrity gates. They
do not decide whether a native round is protocol-valid.
```

### Edit 17 — stage 3, `verification/infrastructure/v3/architecture.md`

The text at the parent:

```text
The specification is operative only for a round the owner authorizes as a provisional
V3 pilot under `AGENTS.md` §A.39. Every other round is governed by `AGENTS.md` §A.37 until a later
round makes V3 the default, and no `V1` or `V2` state is changed or migrated by it.
```

Its replacement:

```text
The specification is operative for every round begun after round `V3-11`'s landing that the
owner does not designate a compatibility round under `AGENTS.md` §A.37, and for the provisional
pilots `V3-10` and `V3-11` under `AGENTS.md` §A.39. A round begun earlier keeps the protocol under
which it landed, and no `V1` or `V2` state is changed or migrated by the specification.
```

### Edit 18 — stage 3, `verification/README.md`

The text at the parent:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
```

Its replacement:

```text
`tools/v3_verifier.py` is the V3 verifier, installed by round `V3-2` as a shadow
```

### Edit 19 — stage 3, `verification/README.md`

The text at the parent:

```text
is an ancestor of a given commit, as a diagnostic that no verdict reads. It gates nothing: it has
no authoritative mode, no verdict it prints changes an exit status, the release gate does not
invoke it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1` and `V2`
remain authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an
```

Its replacement:

```text
is an ancestor of a given commit, as a diagnostic that no verdict reads. Its `--receipts` mode is
the V3 verdict: the release gate's `v3-receipts` step runs it at the commit under check and fails
on any receipt in `receipts/` that does not hold from the commit that last wrote it
(`infrastructure/round-v3-11-authority-cutover/`). Its projection over the `V2` attestation rows
gates nothing, and its workflow job, `V3 verifier diagnostics`, is not a required check. `V1` and
`V2` keep running and can still fail the release gate; they do not decide whether a native round is
protocol-valid. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an
```

### Edit 20 — stage 3, `verification/README.md`

The text at the parent:

```text
builder, not a verifier (`infrastructure/round-v3-9-operationalization/`). A round the owner
authorizes as a provisional V3 pilot under `AGENTS.md` §A.39 runs in one pull request, its receipt
`receipts/<round>.json` is its protocol record, and `tools/v3_verifier.py --verify-round` must hold
on its receipt commit before the pull request lands.
```

Its replacement:

```text
builder, not a verifier (`infrastructure/round-v3-9-operationalization/`). A native round under
`AGENTS.md` §A.39 runs in one pull request, its receipt `receipts/<round>.json` is its protocol
record, and `tools/v3_verifier.py --verify-round` must hold on its receipt commit before the pull
request lands.
```

## The controls, FROZEN

Each stage commit is followed by its checkpoint, run at that commit. A negative control runs on a
child of a stage commit that is built for the control and never pushed.

- **`C1`** (stage 1): `tools/v3_verifier.py --self-test` passes and `--corpus` prints
  `CORPUS  135 vector(s), exact and as expected`.
- **`C2`** (stage 1): `--receipts <stage 1>` exits 0 and prints exactly two lines:
  `RECEIPT  verification/receipts/V3-10.json  Q 4a6e67e4cb097ae49d4e2d9f303b29c3b66ea952  HOLDS`
  and `RECEIPTS  1 receipt(s), all hold`.
- **`C3`** (stage 1): `--receipts 92683262a67190d7468a31a0c2f1dfdbc391778e`, a commit whose tree has
  no receipt, exits 0 and prints `RECEIPTS  0 receipt(s), all hold`.
- **`C4`** (stage 1): `--receipts HEAD` exits 2 and prints
  `v3_verifier: refused (input:not-an-object-id)`.
- **`C5`** (stage 1, negative): on a child that rewrites `V3-10.json` with its execution delta
  digest zeroed, `--receipts` names that child as the receipt commit, reports it `FAILS`, ends
  `NOT ALL HOLD` and exits 1.
- **`C6`** (stage 1, negative): on a child that adds `verification/receipts/notes.txt`, `--receipts`
  reports that path `FAILS  s10:receipt-path` and exits 1.
- **`C7`** (stage 1, negative): in a depth-1 clone, `--receipts` prints
  `RECEIPTS  UNDECIDABLE  undecidable:shallow-repository` and exits 1.
- **`C8`** (stage 1, mutation): each of three scratch copies of the verifier with one line of the
  mode wrong — the verdict ignored, a non-receipt path accepted, the exit status dropped — exits 0
  on `C5`'s or `C6`'s commit, so `C5` and `C6` catch it.
- **`C9`** (stage 2): the release gate's `v3-receipts` step, run alone at the stage 2 commit, passes
  on `RECEIPTS  1 receipt(s), all hold`; `tools/ci_gate_presence_test.py` passes; the guard's
  conditions on the workflow and the gate named above hold on the new files; the `Mathlib bridge`
  job checks out with `fetch-depth: 0`; the diagnostics job carries its new name and the old one is
  gone.
- **`C10`** (stage 2, negative): with the stage 2 files on `C5`'s child, the gate's `v3-receipts`
  step fails.
- **`C11`** (stage 3): `voice`, `claims`, `duplicate`, `artifact-placement` and `control-plane-lint`
  pass.
- **`C12`** (stage 3): the guard's own tests of `AGENTS.md` for `R7-SI2` and `R7-SI3`, taken from
  the guard file and run on the new `AGENTS.md`, hold, and the `R7-MSP` phrases are present.
- **`C13`** (stage 3): `AGENTS.md` has one `## §A.39 ` heading, and neither `provisional V3 pilot`
  nor `Provisional native` remains in it.

## The lifecycle, in the order §A.39 fixes

1. **`F`.** The branch is held at the candidate `F` and the workflow is dispatched on it. The run
   whose `head_sha` is `F`, every job green, is `F`'s `check-run` attestation. The owner reviews
   this file and designates `F` in a comment on the pull request, which is `F`'s
   `owner-designation` attestation. No commit after `F` changes this file.
2. **Execution to `E`.** The four execution commits are pushed together. The branch is held at `E`
   and the workflow is dispatched on it; the run whose `head_sha` is `E`, every job green, is `E`'s
   `check-run` attestation, and the owner's designation of `E` its `owner-designation`.
3. **Reconciliation.** `Λ` is built with first parent the current tip of `main` and second parent
   `E`.
4. **`Q`.** `tools/v3_receipt.py --status complete` builds the receipt from `D`, `F`, `E`, `Λ` and
   the four attestation records, with no candidates and no resolved paths; `Q` adds it at
   `verification/receipts/V3-11.json`.
5. **Verification.** `tools/v3_verifier.py --verify-round Q` must print `VERDICT  HOLDS`, and the
   pull-request run on `Q` must be green, its release gate's `v3-receipts` step passing on two
   receipts, before the pull request lands. Both are recorded on the pull request.
6. **Landing.** The pull request lands through ordinary review and merge, and the push run on the
   landed `main` must be green with the same step passing on two receipts.

If `main` moves after `Q`, a further reconciliation onto the new tip, with second parent `Q`, and a
new receipt commit on it replace `Λ` and `Q` (`K3`, `K4`); the superseded receipt stays in history.

## Targets

| target | passing outcome | stop outcome |
|---|---|---|
| `V311-0` | `F-DESIGNATED` — the dispatched run on exactly `F` is green on every job, and the owner designates `F` | `F-NOT-DESIGNATED` |
| `V311-1` | `RECEIPTS-MODE-INSTALLED` — stage 1 produces the predicted blob and `C1`–`C8` are as predicted | `RECEIPTS-MODE-WRONG` |
| `V311-2` | `GATE-WIRED` — stage 2 produces the predicted blobs and `C9`–`C10` are as predicted | `GATE-WIRING-WRONG` |
| `V311-3` | `RULE-CUT-OVER` — stage 3 produces the predicted blobs and `C11`–`C13` are as predicted | `RULE-WRONG` |
| `V311-4` | `E-DESIGNATED` — the dispatched run on exactly `E` is green on every job: the release gate passes every step, `v3-receipts` on `RECEIPTS  1 receipt(s), all hold` and `V2` authoritative OK; the guard 105 PASS and 0 FAIL with `D`'s verdict map; the diagnostics job's self-test and 135-vector corpus; and the owner designates `E` | `E-NOT-DESIGNATED` |
| `V311-5` | `RECEIPT-HOLDS` — `Q` carries the receipt `tools/v3_receipt.py` builds, `--verify-round Q` prints `VERDICT  HOLDS`, and the pull-request run on `Q` is green with `v3-receipts` passing on `RECEIPTS  2 receipt(s), all hold` | `RECEIPT-FAILS` |
| `V311-6` | `CONTROL-FAILS` — the same receipt with its execution delta digest zeroed, committed on `Λ` in a scratch clone, prints `VERDICT  FAILS` and fails the gate's `v3-receipts` step | `CONTROL-VOID` |
| `V311-7` | `SCOPE-HELD` — `delta(D, Q)` is exactly the governed set; no guard, certificate, seal, manifest record, corpus vector, paper, book or Lean file changes | `SCOPE-BROKEN` |

A stop outcome after `F` halts the round under §A.39's halt path: `W` or the record commit, a
reconciliation, a halted receipt carrying `F`'s attestations alone, and `--verify-round` holding on
it. A stop before `F` is designated closes the pull request unmerged.

## Predictions

Every target is predicted to reach its passing outcome, strongly: the lifecycle and every control
were rehearsed at `D`, and the edits touch no file the guard's verdicts read except for the
conditions `C9` and `C12` re-check.

## Hazards

- **`H1` — the gate depends on history.** A shallow checkout of the `Mathlib bridge` job would make
  `v3-receipts` print `UNDECIDABLE` and fail every build; stage 2 therefore gives that job full
  history in the same commit that adds the step.
- **`H2` — the receipt commit is located, not recorded.** A receipt cannot name its own commit, so
  `--receipts` takes the last commit reachable from the checked commit that wrote the receipt. A
  later round that rewrites another round's receipt makes that commit the receipt commit, which then
  fails `--verify-round`: the governed-path rules already forbid such a write, and the gate fails
  closed on it (`C5`).
- **`H3` — the controls test the wiring, not the specification.** They show that a receipt that
  holds passes the gate and one that does not fails it; they are not evidence that the
  specification is right.

## What the round does not do or license

1. It retires nothing. The guard, the round-certificate verifier, the control-plane machinery and
   §A.37 remain installed; which of their checks survive is the next round's census.
2. It writes no `V2` certificate, guard clause, seal or manifest record; its receipt is its
   protocol record.
3. It changes no ruleset: the `Mathlib bridge` check was required before this round and carries the
   V3 verdict after it.
4. It licenses no sentence that `V1` or `V2` has no authority: while installed, either can still
   fail the release gate.

## Readings, recorded rather than resolved

- **`R1` — the veto's location.** The V3 verdict is a release-gate step, as the `V2` verdict became
  one in round `CV-1`, so the repository's one required gate carries it and no ruleset change is
  needed. The owner chose this location over a required standalone job.
- **`R2` — the verifier reads no ref.** The gate locates the commit under check with
  `git rev-parse HEAD` and passes its object id; `--receipts` refuses anything else (`S1`).
- **`R3` — exit status.** `--verify-round` still prints its verdict and exits 0 whatever the
  verdict; `--receipts` is the mode whose exit status carries it.
- **`R4` — bootstrap.** At `F` the gate has no `v3-receipts` step. From stage 2 it checks
  `V3-10`'s receipt, and at `Q` it checks this round's own receipt before this round can land.
- **`R5` — non-sealing.** The round owns no seal state.
