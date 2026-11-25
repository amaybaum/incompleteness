# Revision r3 of PR #1566 and gate v2: owner decisions, review findings and changes

Delta review of r2 (PR #1566 head 2c8c80a2, gate v2 9fcd3f79). Owner decisions (amaybaum,
2026-11-25), verbatim: "Q1 | Restore the §A.49 rule 1 refusal to §A.51 item 5." "Q2 | Unexpected
appended content must trigger broader containment. Narrow containment only for mechanically
recognizable, bounded footer-related differences." "Q3 | A multi-process plan is one write sequence.
Add a persistent plan-level latch that cannot be bypassed by restarting a process. Default to
single-process execution." "Q4 | A permitted transport difference counts as successful validation
under the adopted allowlist, with the discrepancy recorded. Preserve exact-match requirements for
previously validated mechanisms until explicitly revalidated." "Fix G1 and G2 as well." "For Q2,
distinguish recognizing a footer-shaped discrepancy for containment purposes from accepting a
discrepancy as harmless. Acceptance must still require the exact approved allowlist rule." "Proceed
with one bounded r3 and independent delta review. Keep the existing validated gate operational until
its replacement is approved." With the simplicity objective: "One write gate, one verification
procedure, one containment mechanism."

Local revision only: no GitHub write, network write, commit or push. `gate.py`, `mock.py`,
`test_gate.py` and `countercontrol.py` are unchanged; `gate.py` stays in use. "AGENTS.md" below is
the PR's amended copy.

| Item | Change |
|---|---|
| Q1 (F1) | §A.51 item 5's first sentence lists "a §A.49 rule 1 refusal" again among the package stops. The gate already writes the global marker on a pre-check refusal. |
| Q2 (F2) | Rule 3's third condition: the stored text after the sent content must consist only of newlines and exact copies of the attribution footer; "Any other appended text stops every automated text write. This shape decides only how far the stop extends; a difference is accepted only as rule 2 provides". Code: `transport_rules.footer_shaped_tail` replaces `tail_confined`; it is used only by `_containment_scope`, and acceptance still goes through `classify` and the exact rule. Tests `q9` (link, forged owner line, spaces after the footer, look-alike footer, `[bot]` in a body and in a title: global; doubled, one-newline and removed footers: operation-level and still rejected), `q4`, `q5`. C3 mutant `narrow_on_any_appended_text` (r2's condition) fails 6 tests. |
| Q3 (F4) | Rule 3: a sequence is one run of a plan, in one writer process unless the plan's record names several; its end is recorded persistently for the plan, checked by every process of the plan before each request; restarting does not continue it; only an owner decision clears it. Code: `Gate2` requires `plan_id`; every halt and refusal writes `HALT-PLAN.<plan_id>` in the same halt directory, through the same functions, as the other markers (see consolidation 1). Tests `q10` (the same plan refused in a restarted gate and in a separate process after `.notified` exists; a new plan writes), `q11`. C3 mutants `no_sequence_latch` (5 failures) and `memory_only_latch` (2, among them `q10`). |
| Q4 | Rule 2: "The allowlist applies to an operation validated under it and to the write that validates an operation (§A.51 item 2); an operation validated by an exact match before the allowlist was adopted is held to an exact match until it is validated again under the allowlist." §A.51 item 2: validated when the write "passed §A.49's read-back: an exact match, or a difference that rule 2's allowlist permits, recorded as that rule requires". Code: registry field `"allowlist": True`; `_allowlist_applies` admits a permitted difference only on a single-write (validation) write or an operation so marked; otherwise the difference is a mismatch. Test `q12`; C3 mutant `allowlist_on_exact_validated_ops` fails it. |
| G1 | One comparison for every operation (`_expected_state`): unsent title and body, labels and state against the pre-write read, changed only as the operation intends; for a created Issue or pull request, no labels and open; a comment carries neither. Rule 3's second condition says what "expected" means. Test `q13` (labels emptied on a body edit with a footer-shaped body difference, the reviewer's probe; labels on a create; state on a body edit and a label change; title on a pull-request edit; labels on a close): all global. C3 mutant `labels_state_only_on_their_ops` (r2's checks) fails `q13`. |
| G2 | A `.notified` companion that already exists for the failed operation makes the halt global (condition 4 in `_containment_scope`, the simpler of the two fixes the review offered); an operation marker that already exists, or cannot be written, when the halt is written also makes it global (`escalated_from`). PROTOCOL-v2 §5: the companion is removed with its marker. Test `q14`; C3 mutant `ignore_stale_companion` fails it. |
| F3 | Rule 3's lead-in: "decided mechanically from the write, its read-back and the local halt record; a mismatch the writer cannot see there does not count". |
| F5 | §A.49 adoption line cites "#1169 comments 7165155374 and 7166845267" in place of "the owner's decision of 2026-11-25 on #1566". |
| G3 (not requested; one line) | The halt store is read again immediately before the write request, so a halt recorded during the pre-write read stops the request (test `q15`). No lock: PROTOCOL-v2 §5 states that writers are single-threaded. |
| Adoption lines | §A.51's line now reads "items 2 and 5 amended [date of merge] ...". The placeholders (F6) remain for the merge checklist. |
| Nits | `CHANGES-r2.md` is a frozen record of r2 and is not edited; README's r1 and r2 paragraphs keep their own counts, and an r3 paragraph is added. PROTOCOL-v2 §5 states that the global stop on pre-write refusals and push failures is intended. |

## Consolidations (simplicity objective)

Each answers: (1) what failure it prevents; (2) why an existing mechanism cannot prevent it;
(3) whether a simpler solution gives equivalent protection.

1. **One halt store.** r2 had two containment mechanisms: an in-memory latch (`_SEQUENCE_STOP`, the
   instance field `_stopped`, `_check_sequence`, `_latch`) and the marker files. r3 has one store,
   the halt directory, read by one function (`_check_clear`) and written by one (`_halt`, through
   `_latch` and `_write_marker`). The plan latch Q3 requires is a file in that store, not a third
   mechanism. `_HALTED` remains as the store's in-process copy. (1) A restarted or second process of
   a plan continuing after a halt (Q3), and, through the copy, a process continuing when a marker
   cannot be written. (2) The r2 in-memory latch dies with its process, and the r2 markers hold a
   plan only until `.notified` exists. (3) Dropping the in-memory copy would be simpler, but a
   marker write can fail (full or read-only disk), and r2's in-process latch refuses every further
   write of the process whatever the plan id; removing it would weaken that safeguard, so it stays,
   as the write-failure fallback of the same store.
2. **One comparison for every operation.** r2 compared unsent title and body on PATCH and DELETE
   writes, labels only on label operations and state only on `issue.close`, in three branches.
   r3 has one function, `_expected_state`, for every operation. (1) G1: a label or state change on
   a body edit or a create went unseen or was contained to the operation. (2) The r2 branches were
   per operation type; extending each would duplicate the same check. (3) This is the simpler form.
3. **One footer-shape predicate.** `footer_shaped_tail` replaces `tail_confined`; there is still
   exactly one predicate deciding the extent of a stop, and it is separate from `classify`.
   (1) Q2: appended non-footer text confined to the operation. (2) `tail_confined` accepted any
   appended text. (3) A stricter predicate in place of the old one adds no mechanism.
4. **One marker writer.** Plan, operation and global markers are created by one helper
   (`_write_marker`: exclusive create, fsync, outcome returned), so the escalation of G2 is decided
   in one place.

## Deliberately not simplified

- **gate2 still builds on gate.py by subclassing.** Merging them would change `gate.py`, which must
  stay the operational, validated mechanism until the replacement is approved.
- **`canonical_footer_body` exists in both `gate.py` and `transport_rules.py`.** `gate.py` is frozen;
  test `g15` checks that the two agree.
- **Evidence both in files and embedded in the marker.** The embedded copy is what survives a failed
  evidence-file write (test `q8`); removing either weakens a reviewed safeguard.
- **No process-claim file to enforce single-process plans.** (1) It would refuse a second process
  that uses a plan id by mistake. (2) The plan latch already stops every process of a plan after a
  halt, which is the failure Q3 names. (3) Stating the default (one process per plan, `run_plan`)
  and passing the same id to each process of a multi-process plan gives the required protection
  without another file that only an owner could clear after a crash.
- **G4 (a v1 gate or another module copy in the same process).** Not changed: `gate.py` is frozen.
  The plan latch now stops another copy of `gate2` that uses the same plan id; PROTOCOL-v2 §5 states
  that a v1 gate checks only `HALT`.

## Behaviour notes

- A `classify` result of `exact` for texts whose bytes differ (impossible with the registry's
  `classify`, possible only under mutation) is treated as rejected. The C3 mutant that accepts
  rejected differences therefore passes them off as permitted by the one listed rule, and fails 23
  tests.
- Halt evidence keys for unsent fields are `unsent-<field>.expected` and `unsent-<field>.stored`,
  JSON-encoded, for `title`, `body`, `labels` and `state`.
- Discrepancy records carry `plan_id`.

## Results

`test_gate2.py` 56 tests pass; `test_gate.py` 18 pass; `countercontrol2.py` C1-C3 pass (C2:
6/6/4/11/4/3 failures; C3: 23/2/14/5/2/28/15/6/1/1/1); `countercontrol.py` passes with output equal
to `results-countercontrol.json`. Recorded in `results-tests2.txt` and
`results-countercontrol2.json`.
