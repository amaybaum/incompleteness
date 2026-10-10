# PT protocol — stage 5, amendment 1 (append-only; `PROTOCOL-STAGE5.md`, `9e01f098…`, is unchanged)

Adopted 2026-10-10 16:44Z by the coordinator, after the first launch of threads D and C stopped at their first
integrity step: the directories `pt/D/` and `pt/C/` that `PROTOCOL-STAGE5.md` names as working directories already
exist — they are the stage-1 thread records, covered by `pt/stage1.manifest.sha256` (51 and 28 files). Both threads
were instructed to stop if the directory existed; thread D did so and wrote nothing; the stage-1 manifest and the
other five manifests verify after the stop (16:42:34Z). The aborted launch is recorded at
`pt/audit/aborted-launches/stage5-launch1.md`.

**Amendment.** Wherever `PROTOCOL-STAGE5.md` says `pt/D/` read `pt/D5/`, and wherever it says `pt/C/` read `pt/C5/`:
the working directories of the stage-5 threads are `pt/D5/` (BRIDGE-DERIVE) and `pt/C5/` (BRIDGE-COUNTER). The
anomaly sweep of each thread excludes the sibling directory under its new name, `pt/audit/` and `pt/audit*-replay/`.
The stage-1 directories `pt/A/`–`pt/D/` are records: readable like the other stage-1 records, never written.
Nothing else in the protocol changes: question, outcomes, disguise test, dependency chain, candidates, assignments,
rules, deliverables.

This amendment carries its own sidecar `PROTOCOL-STAGE5-AMENDMENT-1.sha256` and is named in the relaunch message
with its hash; the threads verify both files at start and at end.
