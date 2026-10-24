# Native-Y research checkpoints

WIP research, 24 October 2026. This branch preserves the native-Y continuation
and scoped independent review. It does not adopt a physical premise, change an
acceptance criterion, certify a native round, or authorize a merge.

Base: `de6fe29324ade8a0826c18f7829786086dd590da`.
Workstream branch: `draft/native-y-research-checkpoints-20261024`.
Related research: [#885](https://github.com/amaybaum/incompleteness/pull/885),
whose branch remains under a separate writer and is not modified here.

## Findings and next task

Latest construction: [reset_v8/REPORT.md](reset_v8/REPORT.md).
Two initial sources W=111 and G=011/101 depending on the existing seed u
route the native Y value to q8=(0,y,0) at R+8 while preserving clean q7.
The coupled-source calculation is [independently accepted](reset_v8/review/REPORT.md).
The arbitrary late-q7 input socket fails throughout the tested family.
The calibrated 5:3:2 reset and extended joint public-record law remain open.

Start with [CURRENT-HANDOFF.md](CURRENT-HANDOFF.md) for the current result and
resume task. Read [the historical combined report](parallel_v3/COMBINED-REPORT.md), then
[the independent review](parallel_v3/review/REPORT.md). The reports preserve
their original scientific scope and historical preparation statements.

Historical v3 findings:

* An actual nearby native x sidecar is available in the previous slice next
  to the current q2 operand; persistence and a usable junction are unproved.
* A conditional five-tick native A extractor exists. Its direct late splice
  fails a readiness condition, with a controlled counterexample.
* A standalone native reset/herald candidate has a checked tagged terminal
  law. The strict common raw carrier requirement fails for that candidate.
* The third outward step gives `(u,x*u,u)` and supplies no new raw-Y socket.

Next: embed this clean output into a subsequent native measurement/reset
using its actual two-slice neighborhood, then prove the complete record and
outgoing-carrier law including failures. Do not reload q8 into a separately
clean apparatus. Delayed private access, supplied initial readiness, and the
prior 147-bit extension through R+7 remain explicit resources; that prior accounting
does not certify W-modified public histories through R+8.

## Reproduce this checkpoint

From this directory, with Python 3.12, its standard library, and a C++17 compiler (`g++`):

```sh
python3 replay.py
```

The driver verifies the payload manifest and retained input hashes bound by
the independent reviews, compiles Python source, then runs 25 checker groups normally and
with `-O`, comparing both with recorded deterministic output. It runs in a
temporary copy because the symbolic checker regenerates a JSON result.
Expected: 25 passing groups and `PASS: checkpoint replay` with exit status 0.
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
v3–v8 research sources/inputs needed for the 25-group replay above. The earlier
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

## Parallel continuation and actual reset boundary

[CURRENT-HANDOFF.md](CURRENT-HANDOFF.md) now includes the actual q7 interface
and both the earlier [one-source obstruction](reset_v7/REPORT.md) and the
[new two-source clean route](reset_v8/REPORT.md).
The [shared equivalence obligations](EQUIVALENCE-OBLIGATIONS.md) link the separate
states/dynamics (#911) and composition/access (#912) research PRs.
Run `python3 replay.py --latest` for the new reset_v8 author/reviewer controls;
`python3 replay.py` retains the full checkpoint replay.

The continuation replayed the two new groups in the packaged layout. The prior
23 groups retain unchanged sources and previously passing evidence; a fresh
full-suite run is not claimed. See CHECKPOINT-CHECKS.json for that distinction.
