# NOTES-QB5A-r4: working log for the G3 QB5(a) preregistration, revision 4

## 1. Pins and commit state

**Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.

**Branch.** `research/g3-offset-873-20261113`.

- r3 is committed at `4a157f19`.
- The committed r3 is byte-identical to the writer's r3. The check was
  `git show 4a157f19:<path> | cmp` against the writer's copy.
- The edit check `CONFIRM-QB5A-PREREG-r3.md` was read from the copy the coordinator supplied. The
  coordinator reports that it is committed unchanged beside r3.

**Commit state, as observed when this file was written.**

- r4, NOTES-QB5A-r4 and RESPONSE-QB5A-r3 are not committed.
- The writer does not commit, push or post.

## 2. Authority and request

- Authorization and owner guidance are as in r3: #873 c.6872004336 and c.6872277416.
- The coordinator's request for r4 is a session message, not an owner record. It asks for:
  - CF3-1 and CF3-2, applied verbatim;
  - no change beyond them, apart from the title and the history;
  - the Q-6b/Q-6c labels and the absence of a K-GR346·s4 row left as they are;
  - the OQ answers kept marked as pending.

## 3. Sources read

- `CONFIRM-QB5A-PREREG-r3.md`, in full.
- The writer's r3, to locate each replacement point.
- No corpus passage was opened. No inventory passage was classified.

## 4. Decisions

| # | Decision | Reason |
|---|---|---|
| D-27 | The CF3 replacement text is applied by scripted exact-string replacement, each asserted to match once | The review's text lands unaltered, and nothing else is touched |
| D-28 | The Group P paragraph is re-wrapped after the replacement, with its words unchanged | The file's line width is kept |
| D-29 | The commit carrying the edit check is not named in r4's history | Its ID was not given to the writer. RESPONSE-QB5A-r3 §3 notes this for the coordinator |

## 5. Commands run

All were read-only, apart from writing the three new files.

- `cat` of the edit check.
- `git show 4a157f19:<path> | cmp` against the writer's r3.
- `sed -n` and `grep -n` on r3 and r4.
- A Python script applying exact-string replacements to a copy of r3. It computes nothing on OI rules.
- `diff` of r3 against r4: 7 hunks.
- `grep` for the barred path strings: no hits.

## 6. Off-`main` references (§A.42 item 8)

The references of NOTES-QB5A-r3 §6 carry over. The following are added.

| Reference | Claim it is attached to | Class |
|---|---|---|
| `qb5a/G3-QB5A-PREREG-r3.md` at `4a157f19` (branch) | the base of r4 | support off `main`; lands with #1275 |
| `qb5a/CONFIRM-QB5A-PREREG-r3.md` (branch) | CF3-1 and CF3-2, and their replacement texts | support off `main`; lands with #1275 |

## 7. Marker resolution in r4, in place

**Authority.**

- The owner's answers to OQ-1 to OQ-7 are recorded at #873 c.6872827835 (`amaybaum`, 2026-11-14T06:05:54Z),
  with the OQ-2 and OQ-7 qualifications and the owner's confirmation.
- The writer read the comment first-hand with the GitHub MCP tool (`issue_read`, `get_comments` on #873).
- The coordinator's request for this edit is a session message. It asks for one marker-resolution edit to
  r4, in place, so that the freeze can designate an r4 commit.

**Base.** `G3-QB5A-PREREG-r4.md` at `2afc1c33`. It is byte-identical to the writer's copy before the edit
(checked by `git show 2afc1c33:<path> | cmp`). After the edit the file has 1332 lines.

**Lines changed.** "old" is r4 at `2afc1c33`; "new" is r4 after the edit. Nothing else changed.

| Old | New | Change |
|---|---|---|
| 36–38 | 36–39 | Revision history: the answers are recorded at c.6872827835 and cited at each point of use; §15 keeps the alternatives as a record only |
| 88 | 89–90 | §0 summary: OQ-1 to OQ-5 and OQ-7 answered at c.6872827835 |
| 195 | 197 | §2.2, running-vacuum bullet: marker → "(owner decision OQ-1, #873 c.6872827835)" |
| 227 | 229 | §3, "Sorting at Stage 3": marker → OQ-3 citation |
| 615 | 617 | §5.4, grounding status: marker → OQ-7 citation |
| 658 | 660 | §6.3, `Com`: marker → OQ-7 citation |
| 732–733 | 734–735 | §7.2, closure: marker → OQ-2 citation, re-wrapped |
| 772–775 | 774–777 | §8.2, QB7(a) sensitivity line: marker → OQ-1 citation, re-wrapped |
| 837–838 | 839–840 | §8.5 (ii): marker → OQ-2 citation |
| 842–843 | 844–845 | §8.5 (v): marker → OQ-3 citation, re-wrapped |
| 983 | 985 | §10.3, X11: marker → OQ-7 citation; the fallback is marked "not adopted" |
| 1184–1185 | 1186–1188 | §14.1, freeze bullet: the OQ-5 citation; the owner designates F on #873 after independent acceptance; the owner's confirmation requires r4 to have CF3-1 and CF3-2 applied and independently confirmed first |
| 1215–1266 | 1218–1315 | §15, rewritten |

**What the §15 rewrite contains.**

- Every question is recorded as answered.
- Each decision is quoted verbatim from c.6872827835, and so is the owner's confirmation sentence.
- The OQ-2 and OQ-7 qualifications are quoted, each with a "where the text meets it" list.
- The OQ-5 confirmation is quoted.
- Each alternative is kept, marked "not adopted; record only".
- The applied texts are kept as they were.

**Not changed.**

- r4:1182 (new :1184): "An owner answer to a pending OQ is applied by the alternative text of §15." It is
  now vacuous, because no OQ is pending and no alternative is adopted. It was left as it stands, under the
  instruction to change nothing else.
- r4:257 (new :259) contains "pending" only inside a quoted corpus phrase. It is not a marker.

**Checks.**

- `grep` for "pending owner decision": none remains.
- `grep` for the barred path strings: no hits.

**Qualifications checked against the existing text.** No rewrite was made to close a gap.

- **OQ-2: met.**
  - Δ1–Δ8 are predicates on §5 attributes (§7.2).
  - Δ9.k are enumerated and translated at Q-1b, by two independent readers, and committed before any row
    is classified (X-19). That is before any grounding test.
  - An unresolved or unclassifiable reason goes to the deviation procedure and never changes the frozen rule
    (Q-1b; §14.2; I-BLIND item 1).
  - The negatives are relative to the frozen list (§7.2).
  - **Possible gap, noted.** The decision says "mechanically defined predicates". Δ9.k predicates, once
    committed, are applied mechanically. Writing them at Q-1b is a translation by two independent readers,
    reconciled once, with any disagreement sent to deviations. Whether that writing step counts as
    "mechanically defined" is for the owner or the reviewer to judge.
- **OQ-7: met.**
  - As and As|cond are commitments on both sides under the same tests (§5.3; §5.4; `Com`).
  - Verdicts resting only on them are labelled (§6.3).
  - Ps, D|cond and In stay distinct values, and per-row statuses are kept (§5.3).
  - A plain claim is As, never Ns.
  - **Minor, noted.** The decision's sentence "This is not independent physical verification of the
    assertion" is quoted in §15. The rule text itself conveys it only through the "rests on unqualified
    assertion" label.
- **Other decisions, checked for completeness.**
  - **OQ-1: possible gap.** The decision asks that sensitivity be reported "whenever their treatment
    changes the verdict". §8.2's sensitivity line flips only the A3 cells of the running-vacuum rows
    (to non-committal). It does not flip their role or definiens cells.
  - **OQ-3: met.** It is met by §3 and §8.5 (v), and in general by §8.3 item 3. §8.5 (v) states the
    mirror rule for a metric-defined W0 quantity.
  - **OQ-4: met.** The search methodology and omissions are recorded in NOTES-QB5A-r2 §5, as updated by
    NOTES-QB5A-r3 D-25.
  - **OQ-5.** The decision's wording names "the complete r2 rule". The confirmation supersedes this with the
    r4 requirement. Both are quoted.

## 8. CF4 edits in r4, in place

**Authority.** The edits apply `qb5a/CONFIRM-QB5A-PREREG-r4.md` (ACCEPT WITH CHANGES, a check of r4 at
`3607d5f9`), CF4-1 to CF4-5, using its replacement text verbatim. The coordinator's request is a session
message.

**Base.** `G3-QB5A-PREREG-r4.md` at `3607d5f9`. It is byte-identical to the writer's copy before the edit
(`git show 3607d5f9:<path> | cmp`). After the edit the file has 1351 lines.

**Lines changed.** "old" is r4 at `3607d5f9`; "new" is r4 after the edit. Nothing else changed. OQ-2 needed
no change.

| Old | New | CF4 item | Change |
|---|---|---|---|
| 37 | 37 | CF4-5 | the owner-record time is written "2026-11-14T06:05:54Z" |
| 197 | 197 | CF4-1 (2) | §2.2: "§8.2 carries the QB7(a) sensitivity." |
| (after 678) | 679–680 | CF4-2 (1) | §6.3: label bullet "The label reports a textual commitment of the corpus. It is not independent physical verification …" |
| 774–777 | 776–788 | CF4-1 (1) | §8.2: the QB7(a) sensitivity, three recomputations (i)–(iii) over RV, with labels; (ii) is a counterfactual, never the rendered verdict |
| 848–849 | 859–861 | CF4-5 | §8.5 (v): the OQ-3 mirror rule, stated generally, citing §8.3 item 3 |
| 1073 | 1085 | CF4-1 (4) | Q-7 row: "the QB7(a) sensitivity" |
| 1160 | 1172 | CF4-1 (3) | X-10 cell: the three computations are recorded, with the label wherever one differs; the reviewer recomputes them (X-21) |
| 1184–1185 | 1196–1197 | CF4-3 | §14.1: the stale procedural line is replaced by "The owner's answers to OQ-1 to OQ-7 are applied as §15 records … A change to an applied answer before F is a new revision, reviewed under this section." |
| 1186–1188 | 1198–1204 | CF4-4 | §14.1: the freeze bullet names the acceptance chain (REVIEW-QB5A-PREREG-r2, CONFIRM-QB5A-PREREG-r3, and the r4 check returning ACCEPT FOR FREEZE); F is that head, by its full SHA |
| 1218 | 1234 | CF4-5 | §15 intro: the owner-record time is written "2026-11-14T06:05:54Z" |
| 1231 | 1247–1248 | CF4-1 (5) | §15 OQ-1, text applied: the sensitivity is reported in both directions and with the rows removed |
| (after 1330) | 1348–1349 | CF4-2 (2) | §16: "A verdict resting on As or As|cond rows reports what the corpus asserts. It is not independent physical verification of the assertion (OQ-7)." |

**Not changed.**

- The OQ-1 alternative in §15 still says "Delete §8.2's sensitivity line". That alternative is a record only
  and is not adopted, so it was left as it stands.

**Checks.**

- Each replacement was asserted to match exactly once.
- `diff` against `3607d5f9` gives 11 hunks, matching the table above.
- `grep` for the barred path strings: no hits.
- No passage was classified, and no outcome is stated or predicted.
