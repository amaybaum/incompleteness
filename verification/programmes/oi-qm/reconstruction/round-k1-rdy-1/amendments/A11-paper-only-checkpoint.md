# A11. Paper-only execution: a checkpoint before `E`

**Governs:** base §9 (lines 248–270), by adding the row below. It changes no gate, token or control.

**Row added to §9:**

| Invariant | Checkpoint |
|---|---|
| Paper-only execution (OD-4) | Before `E` is designated, the reviewer checks `delta(F, E)`: (1) every path it changes is `result.md`, `gate-table.json` (A9), or a derivation file with the suffix `.md` that `result.md` names explicitly, each in the round's record directory; (2) each such file has mode `100644`, and none carries a script, a program, a notebook or a workflow, or adds or names an execution path; (3) the execution log, kept in `result.md`, records that no computation was performed. Any violation blocks the designation of `E` pending a separate owner decision |

**Scope.** This is a reviewer checkpoint under `AGENTS.md` §A.41, added for this round. It is not a predicate of
`tools/v3_verifier.py`: under architecture `S7` the verifier checks only that every path `delta(F, E)` changes is
authorized by the governed-path set at `F`, and the entry `record AM` on the record directory admits any file within it.
The execution log's statement that no computation was performed is a declaration by the executor; by itself it is not
independent proof that no computation occurred.

**Source.** amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6656166518
(2026-11-05T10:54:11Z):

> **R3 — Add the checkpoint at E.** Approve the additional procedural checkpoint rather than weakening §12. Before E: Verify that changes from F to E are restricted to `result.md`, `gate-table.json` and explicitly named derivation `.md` files. Verify that none introduces executable content or an execution path. Require the execution log to record that no computation was performed. Any violation blocks the E transition pending a separate owner decision. Describe this accurately as a new checkpoint, not an existing verifier guarantee. A log declaration alone must not be presented as independent proof that no computation occurred.
