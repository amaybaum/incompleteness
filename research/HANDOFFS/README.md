# Handoffs between research threads (protocol)

A handoff carries one result from the thread that established it to a thread that can use it, without changing
the receiving thread's assumptions silently.

1. **Source.** The result must be committed on the source thread's branch with its evidence (commit id, path,
   status label, scripts and outputs, replay).
2. **Write-up.** The coordinator writes `HO-<n>-<source>-to-<target>.md` here (on `research/overview`): the
   statement, its status label (CERTIFIED / CONDITIONAL on named items / CONJECTURE / FAILED), the exact evidence
   pointers (branch, commit, path, sha256), what the receiving thread may assume (stated as the exact proposition)
   and what it may not (scope limits, open conditions). Version 1. A later change is a new version
   (`HO-<n>-v2-…`), never an edit in place.
3. **Receipt.** The receiving thread copies the handoff into `research/<target>/inbox/` on its own branch with a
   commit whose message names the handoff and version, and records in its `LOG.md` whether and how it relies on
   it. Until that commit exists, the thread does not rely on the result.
4. **Index.** The table below lists every handoff with its state.

| id | from | to | result | version | received (commit) |
|---|---|---|---|---|---|
| — | — | — | (none yet) | — | — |
