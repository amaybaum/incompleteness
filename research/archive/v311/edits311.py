#!/usr/bin/env python3
"""Scratch: V3-11's frozen edits as (path, stage, old, new) replacements, each old occurring exactly
once in the file at D. Never landed. Imported by render311.py and sim311.py; run alone it applies
every edit to D's files under ./out/ and prints the predicted blobs."""
import os
import subprocess
import sys

REPO = '/home/user/incompleteness'
V = 'tools/v3_verifier.py'
G = 'tools/release_gate.py'
W = '.github/workflows/verify.yml'
AG = 'AGENTS.md'
AR = 'verification/infrastructure/v3/architecture.md'
RM = 'verification/README.md'

EDITS = [
    # ---- stage 1: the verifier's --receipts mode
    (V, 1, '''"""v3_verifier.py -- the V3 shadow verifier (round V3-2).

SHADOW ONLY. This tool implements the protocol-3 specification
(verification/infrastructure/v3/architecture.md) and reports. It decides nothing: no verdict it
prints changes any exit status, nothing required invokes it, and V1 and V2 remain the only
mechanisms that accept or reject a build, a pull request or a round. It has no authoritative mode.
''', '''"""v3_verifier.py -- the V3 verifier (round V3-2; the V3 verdict from round V3-11).

This tool implements the protocol-3 specification (verification/infrastructure/v3/architecture.md).
Its --receipts mode is the V3 verdict the release gate runs: it verifies every receipt in a
commit's tree from the commit that last wrote it and exits 1 on any receipt that does not hold. The
projection over the V2 attestation rows, and the shadow report that prints it, gate nothing. V1 and
V2 keep running beside it; they do not decide whether a native round is protocol-valid.
'''),
    (V, 1, '''    --reachable <C> <Q>            a diagnostic, never a verdict: whether Q is an ancestor of C
''', '''    --reachable <C> <Q>            a diagnostic, never a verdict: whether Q is an ancestor of C
    --receipts <C>                 every receipt in C's tree, verified from the commit reachable
                                   from C that last wrote it; exit 1 on any that does not hold
'''),
    (V, 1, '''    except Undecidable as u:
        return 'undecidable', u.code
''', '''    except Undecidable as u:
        return 'undecidable', u.code


RECEIPT_DIR = b'verification/receipts/'
RECEIPT_PATH = re.compile(rb'verification/receipts/[A-Z0-9]+(-[A-Z0-9]+)*\\.json')


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
'''),
    (V, 1, '''         '--reachable <C> <Q> | --project <subject> | --mode shadow --subject <commit>')
''', '''         '--reachable <C> <Q> | --receipts <C> | --project <subject> | '
         '--mode shadow --subject <commit>')
'''),
    (V, 1, '''            print('REACHABLE %s' % (code if code else state))
            return 0
''', '''            print('REACHABLE %s' % (code if code else state))
            return 0
        if argv[:1] == ['--receipts'] and len(argv) == 2:
            c = check_oid(argv[1])
            ok, lines = receipts(Repo(cwd), c)
            print('\\n'.join(lines))
            return 0 if ok else 1
'''),
    (V, 1, '''            print('v3_verifier shadow report -- SHADOW ONLY: this report gates nothing; V1 and V2 '
                  'remain authoritative')
''', '''            print('v3_verifier shadow report -- DIAGNOSTIC: this report gates nothing; the V3 '
                  'verdict is --receipts, run by the release gate')
'''),
    # ---- stage 2: the release gate and the workflow
    (G, 2, '''                       nothing; this step is where V2 can reject a build.
''', '''                       nothing; this step is where V2 can reject a build.
  v3-receipts          the V3 verdict, from round V3-11: every receipt in the
                       tree, verified by tools/v3_verifier.py --receipts from
                       the commit that last wrote it. A receipt is data no other
                       check reads, so this step is where a native round whose
                       receipt does not hold can reject a build. V1 and V2 keep
                       running beside it and can still fail the gate; they do
                       not decide whether a native round is protocol-valid.
'''),
    (G, 2, '''        label = sys.argv[sys.argv.index('--label') + 1]
    checks = [
''', '''        label = sys.argv[sys.argv.index('--label') + 1]
    # the commit under check, located here because tools/v3_verifier.py reads no ref: the gate
    # names the commit, and a failed lookup leaves an empty argument, which the verifier refuses
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                          text=True).stdout.strip()
    checks = [
'''),
    (G, 2, '''                      [sys.executable, "tools/certificate_verifier.py", "--mode", "authoritative"]),
''', '''                      [sys.executable, "tools/certificate_verifier.py", "--mode", "authoritative"]),
        # v3-receipts: the V3 verdict (round V3-11). Every receipt under verification/receipts/,
        # verified from the commit that last wrote it; a receipt that does not hold, or a
        # repository too shallow to decide, fails the gate. It needs full history, so the
        # workflow's Mathlib bridge job checks out with fetch-depth: 0.
        ("v3-receipts",
                      [sys.executable, "tools/v3_verifier.py", "--receipts", head]),
'''),
    (W, 2, '''  # able to obscure the state of the zero-import core gate above.
  bridge:
    name: Mathlib bridge
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

''', '''  # able to obscure the state of the zero-import core gate above. fetch-depth: 0 is load-bearing
  # for the release gate's v3-receipts step, which verifies each receipt from the commit that last
  # wrote it and fails on a shallow repository (round V3-11).
  bridge:
    name: Mathlib bridge
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

'''),
    (W, 2, '''  # V3-2: the V3 shadow verifier, SHADOW ONLY. Not a required check, not invoked by the release
  # gate, and no other job depends on it; V1 and V2 remain authoritative. Self-test and corpus go
  # red only on a defect of the shadow itself; the shadow report always exits 0. fetch-depth: 0
  # gives the corpus's repository vectors and the projection the history they read.
  v3-shadow-verifier:
    name: V3 shadow verifier
''', '''  # V3-2: the V3 verifier's diagnostics. Not a required check, and no other job depends on it: the
  # V3 verdict is the release gate's v3-receipts step, which the required Mathlib bridge check runs
  # (round V3-11). Self-test and corpus go red only on a defect of the verifier itself; the shadow
  # report, the projection over the V2 attestation rows, always exits 0. fetch-depth: 0 gives the
  # corpus's repository vectors and the projection the history they read.
  v3-shadow-verifier:
    name: V3 verifier diagnostics
'''),
    # ---- stage 3: the rule, the specification's preamble and the README
    (AG, 3, '''shape explicitly as no guard, no pin, `E` → `L`, so its meaning is unchanged. A
preregistration is not amended to track later vocabulary, and none needs to be.
''', '''shape explicitly as no guard, no pin, `E` → `L`, so its meaning is unchanged. A
preregistration is not amended to track later vocabulary, and none needs to be.

From `V3-11`'s landing this rule is the compatibility lifecycle, not the default. It governs the
rounds begun before that landing, which keep the protocol under which they landed, and a later round
only when the owner designates its preregistration a §A.37 compatibility round. Every other round
runs under §A.39.
'''),
    (AG, 3, '''## §A.39 Provisional native V3 rounds

§A.37 remains the default lifecycle for every round, and it governs the round that adopted this
rule, `V3-9`. A round whose preregistration the owner authorizes as a **provisional V3 pilot** runs
instead under the native lifecycle of `verification/infrastructure/v3/architecture.md`, which is
operative for such rounds and no others:
''', '''## §A.39 Native V3 rounds

From `V3-11`'s landing every new round runs under the native lifecycle of
`verification/infrastructure/v3/architecture.md`, unless the owner designates its preregistration a
§A.37 compatibility round. `V3-9`, which adopted this section, ran under §A.37; `V3-10` and `V3-11`
ran under it as provisional pilots. Each round keeps the protocol under which it landed:
'''),
    (AG, 3, '''`F` is designated, the pilot's branch is held at exactly `F` and the workflow is dispatched on it
''', '''`F` is designated, the round's branch is held at exactly `F` and the workflow is dispatched on it
'''),
    (AG, 3, '''**A halted pilot.** A pilot that halts after `F` instead of reaching a designated `E` follows the
''', '''**A halted round.** A round that halts after `F` instead of reaching a designated `E` follows the
'''),
    (AG, 3, '''A provisional pilot carries no guard clause, seal manifest record, round certificate or
`control-plane-preconditions` block: its receipt, `verification/receipts/<round>.json`, is its
protocol record. It leaves `V1` and `V2` authority unchanged. The guard and the release gate run on
its pull request as on any other, and they remain the repository's authoritative checks until a
later round makes V3 the default.
''', '''**Authority.** A native round is protocol-valid exactly when `tools/v3_verifier.py --verify-round Q`
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
'''),
    (AR, 3, '''The specification is operative only for a round the owner authorizes as a provisional
V3 pilot under `AGENTS.md` §A.39. Every other round is governed by `AGENTS.md` §A.37 until a later
round makes V3 the default, and no `V1` or `V2` state is changed or migrated by it.
''', '''The specification is operative for every round begun after round `V3-11`'s landing that the
owner does not designate a compatibility round under `AGENTS.md` §A.37, and for the provisional
pilots `V3-10` and `V3-11` under `AGENTS.md` §A.39. A round begun earlier keeps the protocol under
which it landed, and no `V1` or `V2` state is changed or migrated by the specification.
'''),
    (RM, 3, '''`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
''', '''`tools/v3_verifier.py` is the V3 verifier, installed by round `V3-2` as a shadow
'''),
    (RM, 3, '''is an ancestor of a given commit, as a diagnostic that no verdict reads. It gates nothing: it has
no authoritative mode, no verdict it prints changes an exit status, the release gate does not
invoke it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1` and `V2`
remain authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an
''', '''is an ancestor of a given commit, as a diagnostic that no verdict reads. Its `--receipts` mode is
the V3 verdict: the release gate's `v3-receipts` step runs it at the commit under check and fails
on any receipt in `receipts/` that does not hold from the commit that last wrote it
(`infrastructure/round-v3-11-authority-cutover/`). Its projection over the `V2` attestation rows
gates nothing, and its workflow job, `V3 verifier diagnostics`, is not a required check. `V1` and
`V2` keep running and can still fail the release gate; they do not decide whether a native round is
protocol-valid. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an
'''),
    (RM, 3, '''builder, not a verifier (`infrastructure/round-v3-9-operationalization/`). A round the owner
authorizes as a provisional V3 pilot under `AGENTS.md` §A.39 runs in one pull request, its receipt
`receipts/<round>.json` is its protocol record, and `tools/v3_verifier.py --verify-round` must hold
on its receipt commit before the pull request lands.
''', '''builder, not a verifier (`infrastructure/round-v3-9-operationalization/`). A native round under
`AGENTS.md` §A.39 runs in one pull request, its receipt `receipts/<round>.json` is its protocol
record, and `tools/v3_verifier.py --verify-round` must hold on its receipt commit before the pull
request lands.
'''),
]

STAGES = {1: [V], 2: [G, W], 3: [AG, AR, RM]}


def apply(texts, stage=None):
    """texts: {path: str} at D; returns the texts after every edit (of one stage, if given)."""
    out = dict(texts)
    for path, st, old, new in EDITS:
        if stage is not None and st != stage:
            continue
        assert out[path].count(old) == 1, (path, old[:60])
        out[path] = out[path].replace(old, new)
    return out


def blob(s):
    return subprocess.run(['git', 'hash-object', '--stdin'], cwd=REPO, input=s.encode(),
                          capture_output=True, check=True).stdout.decode().strip()


if __name__ == '__main__':
    D = sys.argv[1]
    here = os.path.dirname(os.path.abspath(__file__))
    paths = sorted({e[0] for e in EDITS})
    at_d = {p: subprocess.run(['git', 'show', '%s:%s' % (D, p)], cwd=REPO, capture_output=True,
                              check=True).stdout.decode() for p in paths}
    new = apply(at_d)
    for p in paths:
        full = os.path.join(here, 'out', p)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, 'w', encoding='utf-8').write(new[p])
        print('%-50s %s -> %s' % (p, blob(at_d[p])[:8], blob(new[p])))
