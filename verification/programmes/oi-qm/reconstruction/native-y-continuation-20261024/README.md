# Native-Y research checkpoints

WIP research, 24 October 2026. This branch preserves the native-Y continuation
and scoped independent review. It does not adopt a physical premise, change an
acceptance criterion, certify a native round, or authorize a merge.

Base: `de6fe29324ade8a0826c18f7829786086dd590da`.
Workstream branch: `draft/native-y-research-checkpoints-20261024`.
Related research: [#885](https://github.com/amaybaum/incompleteness/pull/885),
whose branch remains under a separate writer and is not modified here.

## Findings and next task

Latest construction: [outward_v6/CORRECTION-REPORT.md](outward_v6/CORRECTION-REPORT.md).
One added initial source (u,0,u), using only the existing apparatus seed,
produces the clean native code (0,0,y) at q7,R+7. The full nonlinear source
calculation and geometry are checked; independent review is being finalized.
This is a clean readout of the original qY operand for the current native
family. The arbitrary qY diagnostic guarantees D=p only, and q2.A-only reuse
still fails. A reusable late input socket and the subsequent Y reset are open.

Read [the combined report](parallel_v3/COMBINED-REPORT.md), then
[the independent review](parallel_v3/review/REPORT.md). The reports preserve
their original scientific scope and historical preparation statements.

* An actual nearby native x sidecar is available in the previous slice next
  to the current q2 operand; persistence and a usable junction are unproved.
* A conditional five-tick native A extractor exists. Its direct late splice
  fails a readiness condition, with a controlled counterexample.
* A standalone native reset/herald candidate has a checked tagged terminal
  law. The strict common raw carrier requirement fails for that candidate.
* The third outward step gives `(u,x*u,u)` and supplies no new raw-Y socket.

Next: embed this clean output into a subsequent native measurement/reset
using its actual two-slice neighborhood, then prove the complete record and
outgoing-carrier law including failures. Do not reload q7 into a separately
clean apparatus. Delayed private access, supplied initial readiness, and the
147-bit extension for the seven old public records remain explicit resources.

## Reproduce this checkpoint

From this directory, with Python 3.12, its standard library, and a C++17 compiler (`g++`):

```sh
python3 replay.py
```

The driver verifies the payload manifest and all 18 earlier independently reviewed
input hashes and the five locally retained inputs of the new review, compiles Python source, then runs 20 checker groups normally and
with `-O`, comparing both with recorded deterministic output. It runs in a
temporary copy because the symbolic checker regenerates a JSON result.
Expected: 20 passing groups and `PASS: checkpoint replay` with exit status 0.
These checks establish only the scopes stated in the reports, not Lean
certification, a universal compiler theorem, or a full transport audit.

## Continuing checkpoints

The owner requested continuous saving of findings to a draft repository branch.
During active work, publish each meaningful finding, negative result, completed
review, and session handoff promptly to this branch with forward commits.
Run applicable bounded checks first; label incomplete or failing work
`WIP / UNVERIFIED` and state exactly what remains unchecked. Keep this
workstream's guiding draft PR aligned with its current head and next task.
Preserve reviewed commits. Do not amend, force-push, delete the branch, merge,
dispatch workflows, or designate F/E as part of checkpointing. This policy
does not schedule unattended background work.

## Provenance and omissions

The historical v3 combined report describes a separate portable handoff ZIP;
its `--baseline` command, dependency archives, and PDF are not the layout of
this repository checkpoint. This tree contains the v2 interface sources and
v3 research sources/inputs needed for the 20-group replay above. The earlier
ten-checker v1 bundle is not rerun by this driver. Copied inherited core code
and source geometry are retained where the current checks need them.

The standalone PDF, archive containers, rendering scripts, caches, executables,
temporary search logs, and orchestration notes are omitted. Deterministic
checker outputs are retained as regression expectations; historical provenance
files describe the original calculations, including their then-read-only
repository status. The user's later checkpoint instruction authorizes this
publication. No historical result is strengthened by publication.

Repository-wide full-history, Lean and release gates are left to ordinary PR
CI. No special workflow dispatch or exact-head attestation is claimed.
