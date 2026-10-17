# Operational incident: scratch files deleted by an agent that had not created them

- **Date:** 2026-10-17, UTC, during the independent review of PR #854 (R11).
- **Who:** the R11 review subagent of this session.
- **What:** while removing its own logs with a `find … -newer … -delete` pattern, it also deleted five files in the session
  scratchpad that it had not created:
  - `dockerd.log`, `dockerd2.log` (earlier docker-daemon attempts)
  - `lake-cache.log`, `lake-build.log` (earlier Lean/lake build attempts)
  - `pull.log` (an earlier git pull)
- **Recoverable:** no. No process held them open.
- **Impact:** none found. No file on `main` cites any of the five, no preregistration, manifest or archive names them, and
  none was evidence or a pinned input. They were incidental operational logs.
- **Detection:** the agent reported it itself in its final report.

## Root cause

A cleanup step selected files by modification time across a shared directory rather than by the exact paths the agent
had created.

## Corrective rule (owner, 2026-10-17)

Agents do not delete, move or clean up any file or directory they did not create, without explicit authorization.
They remove only their own scratch work, by exact path. The rule was sent to every running agent of this session the
same day and is part of every agent brief issued since.

## Related rules

AGENTS §A.26 (provenance integrity): an unaccounted file is quarantined, never deleted. This incident concerns the
converse case, the deletion of accounted working files, and the corrective rule above closes it.
