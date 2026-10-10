# Aborted launch: stage 5 (Q-EX-BRIDGE), first launch of threads D and C, 2026-10-10 16:40:27Z

**Cause (coordinator's error).** `PROTOCOL-STAGE5.md` (`9e01f098…`) names `pt/D/` and `pt/C/` as the working
directories. Both already exist: they are the stage-1 thread records (threads A–D of stage 1), covered by
`pt/stage1.manifest.sha256`. The launch messages instructed each thread to create its directory and to stop and
report if it already existed.

**What happened.** Thread D stopped at its first integrity step at 16:41:15Z, wrote nothing anywhere, and reported:
`pt/D/` exists (51 files, mtimes 04:34–05:50, all listed in `stage1.manifest.sha256`); its own check
`sha256sum -c --quiet stage1.manifest.sha256` passed at 16:41:38Z; it did not read any protocol, ledger, kernel or
manuscript file, nor `pt/C/`, `pt/audit/` or `pt/base/`. It noted that `pt/C/` also exists (stage-1 thread C) and
recommended fresh names such as `pt/D5/`.

**Coordinator's verification (16:42:34Z).** All six manifests verify (`inputs`, `stage1`, `inputs2`, `inputs3`,
`stage2`, `inputs4`); no file under `pt/C/` or `pt/D/` is newer than 16:40Z; the stage-1 records are intact.

**Disposition.** Append-only amendment `pt/PROTOCOL-STAGE5-AMENDMENT-1.md` renames the working directories to
`pt/D5/` and `pt/C5/`; `PROTOCOL-STAGE5.md` is unchanged. Thread D is relaunched with the amendment; thread C is
relaunched after its first instance reports (it was given the same stop instruction).

**Lesson for the launch checklist.** Before naming a working directory in a protocol, list `pt/` and check the name
against every manifest; the stage-4 launch used fresh single letters (`Y`, `Z`) by luck of the alphabet, not by a
check. The "eight protocol hashes" slip of stage 4 and this one have the same shape: a launch detail not verified
against the tree. Both were caught by the threads' own guards.

**Thread C, first instance (reported 16:44Z).** Stopped at check (1) without writing; verified all six manifests and `ns.manifest`; read only the directory-name lines of the protocol (116–128), the names and mtimes in `pt/C/`, and the C/ and D/ entries of the stage-1 manifest; recommended `pt/C5/`, `pt/D5/`. Both threads relaunched under amendment 1 (D5 16:43Z, C5 16:45Z).
