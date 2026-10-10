"""Scratch: V3-13's edits to AGENTS.md. Never landed as is."""
import os
_S = os.path.dirname(os.path.abspath(__file__))
AGENTS = 'AGENTS.md'
_A = open('/home/user/incompleteness/AGENTS.md', encoding='utf-8').read()
_A37_OLD = _A[_A.index('## §A.37 Round lifecycle: control plane, then execution and landing\n'):
              _A.index('---\n\n## §A.39 Native V3 rounds\n')]
_A37_NEW = open(os.path.join(_S, 'a37_new.md'), encoding='utf-8').read() + '\n'

AGENTS_EDITS = [
# ---- the review rule for frozen control planes, restated for native rounds
("""- Frozen control-plane blob after head movement. When a control-plane
  preregistration is frozen by exact commit SHA and blob SHA, the blob identity is
  authoritative. If the PR head changes after freeze approval, re-read the frozen
  file at the new head and verify its blob SHA. If the approved blob is unchanged,
  the freeze remains valid; record the new head and the unchanged blob without
  requiring a full repeat review. If the blob changes at all, the freeze approval
  lapses and a fresh exact-head/blob freeze review is required before merge or
  execution. A branch sync, merge-from-base, or unrelated commit therefore does not
  invalidate a freeze merely by moving the head; it invalidates it only if it
  changes the frozen blob. This exception applies to the freeze itself, not to
  ordinary final exact-head review of execution/result PRs.
""",
"""- Freeze and head movement. A round's freeze is the exact commit `F` the owner
  designates, and the verifier rejects any change to its control-plane files after
  `F` (§A.39). A head that moves after `E` moves by reconciliation: review what
  the reconciliation brings in, and check that the landing adds exactly the
  execution's own changes, each conflict resolved by merits (§A.39).
"""),
# ---- the lessons register points at the rules that hold
("""  otherwise. Hence §A.37's diagnostic rule — check the exact-head certification before calling a
  red badge a research failure, and never cure it by merging main into a sealed execution.
""",
"""  otherwise. Hence §A.39's exact-head rule — a pull-request run tests a synthetic merge, so check
  the exact-head run before calling a red badge a research failure, and never cure it by merging
  main into a certified execution.
"""),
("""  twenty minutes earlier. Hence §A.37's resolve-by-merits rule and its check that a landing adds
  exactly the execution's own diff.
""",
"""  twenty minutes earlier. Hence §A.39's resolve-by-merits rule and its check that a landing adds
  exactly the execution's own diff.
"""),
("""  corrected by append-only amendment. Hence §A.37's `D` / `B` / `M` vocabulary subsection and
  the control-plane lint.
""",
"""  corrected by append-only amendment. Hence the `D` / `B` / `M` vocabulary §A.37 records; a
  native round has no mandated base, its execution anchored at the designated commit `F`.
"""),
# ---- the local-check rule, in the short-form working rules
("""- **§A.28 Repo minimalism.** The repo is public and permanent; the burden of proof is on adding,
  not omitting. Before committing a file: it must be needed by a reader of the manuscripts or the
  code, be maintained, and not leak process. Process artifacts are cheap to add and expensive to
  retire.
""",
"""- **§A.28 Repo minimalism.** The repo is public and permanent; the burden of proof is on adding,
  not omitting. Before committing a file: it must be needed by a reader of the manuscripts or the
  code, be maintained, and not leak process. Process artifacts are cheap to add and expensive to
  retire.
- **§A.40 Where verification runs.** Cheap deterministic checks run locally before a push: a
  tool's self-test, the V3 verifier's self-test and corpus, `legacy_records_check.py`, a round's
  own scripts, compilation and static checks of changed Python. The Lean kernel, the Mathlib
  bridge, the release gate and the full probe suite run in CI. The exact-head host runs, dispatched
  on exactly `F` and `E`, are the source of certification (§A.39); a local run is evidence for the
  executor and is never recorded as a `check-run` attestation.
"""),
# ---- §A.37 becomes a record
(_A37_OLD, _A37_NEW),
# ---- §A.39: the one lifecycle, reconciliation rules, the two immutabilities
("""From `V3-11`'s landing every new round runs under the native lifecycle of
`verification/infrastructure/v3/architecture.md`, unless the owner designates its preregistration a
§A.37 compatibility round. `V3-9`, which adopted this section, ran under §A.37; `V3-10` and `V3-11`
ran under it as provisional pilots. Each round keeps the protocol under which it landed:
""",
"""From `V3-11`'s landing every new round runs under the native lifecycle of
`verification/infrastructure/v3/architecture.md`. `V3-9`, which adopted this section, ran under
§A.37; `V3-10` and `V3-11` ran under it as provisional pilots. Each round keeps the protocol under
which it landed:
"""),
("""3. **Reconciliation, if needed.** Later history enters the round only through reconciliation
   merges after `E`: first parent a later base on whose first-parent chain `D` lies, second parent
   `E` or the previous receipt commit. The last reconciliation is `Λ`.
""",
"""3. **Reconciliation, if needed.** Later history enters the round only through reconciliation
   merges after `E`: first parent a later base on whose first-parent chain `D` lies, second parent
   `E` or the previous receipt commit. The last reconciliation is `Λ`. Conflicts are resolved in the
   reconciliation, never in `E`, and **by merits, not by side**: each row or block is taken from
   the branch that owns it, the round's own from `E` and every row a later round has moved from
   the base. A clean automatic merge is not evidence of a correct one where both sides touched the
   same files; compare the landing with the execution's own diff and account for every difference.
"""),
("""before it is designated. A pull-request run tests a synthetic merge, not `F` or `E`, and is not
recorded as their attestation. These are host attestations, which the receipt records and no
predicate of `tools/v3_verifier.py` reads.
""",
"""before it is designated. A pull-request run tests a synthetic merge, not `F` or `E`, and is not
recorded as their attestation. These are host attestations, which the receipt records and no
predicate of `tools/v3_verifier.py` reads. So a red pull-request badge on a round held at `F` or `E`
is diagnosed against the exact-head run first; it is never cured by merging main into the round
before `E`.
"""),
("""A native round carries no guard clause, seal manifest record, round certificate or
`control-plane-preconditions` block: its receipt, `verification/receipts/<round>.json`, is its
protocol record. The guard (`V1`) and the round-certificate verifier (`V2`) keep running on its pull
request as on any other, and a failure of either still fails the release gate: until a later round
decides which of their checks survive, they are compatibility and repository-integrity gates. They
do not decide whether a native round is protocol-valid.
""",
"""A native round carries no guard clause, seal manifest record, round certificate or
`control-plane-preconditions` block: its receipt, `verification/receipts/<round>.json`, is its
protocol record. The guard (`V1`) keeps running on its pull request as on any other and still
fails the release gate on a failed check, but it checks content — kernel modules, manuscripts and
notes — and never a round's chronology; it does not decide whether a native round is
protocol-valid.

**Two immutabilities, kept apart.** They protect different populations by different mechanisms, and
neither stands in for the other:

- **Native rounds' records** — each round's record directory and seal record — are kept by
  `tools/v3_verifier.py --receipts` (the specification's `G13`): once a round's receipt holds, its
  record directory and seal record at every later commit must be exactly those at its receipt
  commit. A correction is made by a new native round in its own record.
- **The records of the rounds landed before V3** are kept by the release gate's `legacy-records`
  step, `tools/legacy_records_check.py`: every record listed in
  `verification/infrastructure/legacy-records.json` keeps its blob, and no file is added under a
  closed namespace. The manifest changes only as the governed work of a native round whose receipt
  holds and whose governed paths name the manifest: a migration, a repair or a change to the
  population is a native round, and a commit that changes a record and the manifest together
  fails.
"""),
]
