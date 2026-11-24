Final bounded review of DESIGN-v5.5 (ledger and terminology verification tool)

Verdict: ACCEPT WITH REQUIRED CORRECTIONS

Reviewer: the independent, non-author session that wrote review-v5.2 to review-v5.4.

Limits:
- read-only;
- no repository, git or GitHub write;
- no workflow run and no host call;
- Stage 1 worktree not touched;
- new files only under `D/review-v5.5/`.

The scripts are mine. They import P's frozen `edits_check.py` only after checking its blob hash. I did not read or run `work-v55/`. Date 2026-11-23.

Goal link (sec. A.47): A1-EXIT (#1169). This review decides whether DESIGN-v5.5 closes review-v5.4's V1-V5, the addendum's C1-C4 and the residual-trust list under the owner's decisions R-D1 to R-D5. It adopts nothing and authorizes nothing.

Inputs (sha256, verified; all match the coordinator's values)

- DESIGN-v5.5.md 74db584a5bdb861519f9703e3b5d102ba07a60dfd0e8f89ea183bd89a80b52a4
- CHANGES-v5.5.md 815e8a03e998bf4f0a8909669d50b895c96a2808ae5ab2c09c4c32d15325a1ed
- review-v5.4/review-v5.4.md bc0921e37a1d941f3845b200dd90e744dcf0fdd635f8cac7fb2b6ca9d67af854
- review-v5.4/review-v5.4-addendum.md 8559e4336e293a5b879a5154c928fcad209be8e1a1aa37d15ddab459b1059ef3

The stopping rule, as the owner approved it: a finding blocks only if it is demonstrated or supported by a reproducible counterexample, and it violates an existing requirement or an agreed pass condition. Every finding below is classified under that rule.

Summary

Every scoped item is resolved in substance. My own parity rerun against v5.5's rule confirms the writer's demonstration:

- no valid, unambiguous operation of the frozen plan is rejected;
- the only refusals P does not make are chained edits.

One finding blocks under the stopping rule, and it has a bounded fix:

- F2: the offline replay cannot reproduce an op-C result's delegated host-run outcomes, because the committed snapshot does not hold them.

One further correction is required but does not block:

- F1: control S11-58k leaves edit 2's `old` text unspecified, and with an `old` absent at `H`, P refuses the case.

Neither needs a redesign, hence ACCEPT WITH REQUIRED CORRECTIONS.

***

Findings by scope item

R-D1 / V1 / C4: parity and the refusals stricter than P

My implementation of sec. 6.1 as written covers:

- uniqueness at `H`;
- application in list order with P's non-overlapping `str.count` selection;
- the segment model, under which an occurrence must lie inside one original-`H` segment;
- splices built from the mapping, with the final text rebuilt from disjoint splices at `H`.

I compared it with P's own `variant()` and P's application (`rv55_parity.py`). The random cases are 30,000, generated with a different seed and generator from the writer's, over three alphabets, one with non-ASCII characters, 1-4 edits each, and 50% of edits with a second variant.

| Outcome | Count |
|---|---|
| Both apply, with identical final text | 2860 |
| Both refuse | 26921 |
| v5.5 accepts where P refuses | **0** |
| Text differs | **0** |
| Extra refusals | 219, all chained |

- **A1:** applied, with identical text.
- **Crafted cases:**
  - overlap (`"aa"` in `"xaaay"`): selected at offset 1, as P selects;
  - adjacent independent edits, Unicode offsets, and a second variant selected after an earlier edit removed `old`: all identical to P;
  - chained (an `old` created by an earlier edit, and one across an image boundary): refused as chained, while P applies them;
  - an occurrence spanning the point of an earlier deletion: refused as chained, while P applies it.

The three stricter kinds are documented, each with the reason the input is invalid or ambiguous:

- (i) a splice for the unselected variant;
- (ii) a splice covering two edits, which is malformed under the ledger schema;
- (iii) chained edits, which disjoint splices cannot express.

P's per-edit items 5 and 6 are recorded in every case, and the design makes no claim of complete equivalence. This meets R-D1.

Findings:

- **F1. Not blocking, but a required precision.** The counterexample is my instantiation of the control (`rv55_controls.py`), so it does not meet the stopping rule.
  - S11-58k's case is: edit 1 `ab q` → `xy` at `"ab qc"`; edit 2 "selects its second variant `yc`". Its stated expectation is "ERROR (chained); P applies".
  - The case does not specify edit 2's `old`. `yc` does not occur at `H`, so P applies the list only if edit 2's `old` occurs exactly once at `H` and no longer occurs after edit 1.
  - With an `old` absent at `H` (I used `zz`), P refuses at its first-loop uniqueness check, and the tool refuses at uniqueness, not as chained. The stated expectation then does not hold, and a control's predicate must equal its expectation (Stage 1 B6, sec. 10.4).
  - Specify edit 2 completely. Verified example:
    - edit 2 = `{old: "qc", new: "Q", old_step2: "yc", new_step2: "Q"}`;
    - at `H` = `"ab qc"`, `old` is unique;
    - after edit 1 only `yc` matches, spanning the image boundary;
    - P applies it (result `"xQ"`), and v5.5 refuses it as chained.
- **N1. Not blocking.** Sec. 6.1's (iii) says the occurrence "lies wholly or partly inside an image". An occurrence that spans the insertion point of an empty image (a deletion) lies inside no image, yet the binding rule correctly refuses it, because it crosses two original segments. Crafted counterexample: "occurrence spanning a deletion". The rule is right, so this is wording only. State it as "or spans the point where an earlier edit's image, possibly empty, was inserted".
- S11-58i and S11-58j behave as stated: overlap selected at offset 1; chained refused while P applies.

R-D2 / V4: withdrawal integrity

Resolved:

- Admission reads the edit status and hidden state of every owner comment.
- Edited forms, form text in an edit history, hidden comments and unreadable status all refuse.
- The append-only, owner-approved freeze ledger and the committed snapshots keep every observed withdrawal and supersession binding after deletion, hiding or editing (TR31, TR32).
- A conflicting or unverifiable ledger refuses (TR36).
- A designation must be verifiable now, so a ledger entry never designates.

Findings:

- **N2. Not blocking under the rule (no reproducible counterexample, because it depends on host behaviour I could not exercise).** A withdrawal posted and deleted before any admission observed it, on a host that exposes no deletion events, reactivates nothing that was ever observed, but `F` would be admitted. The design states this as a residual and names who can delete comments. Whether that residual is acceptable is an owner decision (below).
- **N3. Not blocking.** Sec. 6.3 says every freeze-ledger change "lands through the authority-change procedure, with an `oi-authority/1 approve` comment", and also that every acceptance landing "appends the events its admission observed". The text should say whether an acceptance append also needs its own approval comment. I recommend that it does, since that is the stricter choice.

R-D3 / V2, V3: execution identity

Resolved:

- `head_sha` must be on `main`'s first-parent chain of the attested repository and contain `A`, the tool and the pinned workflow, so the predicate is satisfiable.
- The workflow content and every `engine_pins` blob are read at `head_sha` through the host API by both the tool and the consumer, with no further file allowed under `tools/ledger_coverage/`.
- The evaluated commits are explicit, recorded inputs, compared with the landing record (TR28-TR30).
- The runner's faithful execution is a stated residual.

No findings.

R-D4 / V5, C1, C2: authority record, forms and changes

Resolved:

- `tools/ledger_coverage/authority.json`, schema `oi-tool-authority/2`.
- Numeric id 7273571 decides; the login is informational only.
- Exact versioned key=value forms; a malformed form, an unknown version, a wrong key order or a trailing space refuses (TR38, TR39).
- The first line is the bytes up to the first LF, with one trailing CR removed (TR37).
- Every change to `A` needs, before the merge:
  - an independent review naming both blobs;
  - an owner approval comment, `oi-authority/1 approve from=... to=...`, verified like a designation;
  - for an owner-id change, approval from both ids.
- The merge by the owner's account is provenance only.
- The first `A` (`from=none`) is stated as circular: a residual.

Finding:

- **N4. Not blocking.** The approval form names blob hashes only, not which record (`A` or the freeze ledger) it approves. Collisions are infeasible, so this is not a defect. Naming the record kind would make each approval self-describing (optional O1).

R-D5 / C3: durable evidence

Resolved:

- `result.json.gz` with fixed gzip parameters, where the sha256 of the uncompressed bytes decides;
- the full admission snapshot and its sha256;
- the reproducibility recipe;
- ledger appends;
- CI metadata as provenance only;
- the offline `replay --snapshot` mode (TR45).

Finding:

- **F2. Blocking (bounded).** The counterexample is in the design text and can be checked by reading it:
  - For op C, the result includes the delegated classes.
  - The host-run classes `pdf` and `ci` are decided from host run and job records and an uploaded artifact's sha256, which the tool reads from the host API inside the job (sec. 7.2).
  - The native classes rerun checkers in clones, including PDF builds, whose offline determinism is not established.
  - The admission snapshot's field list (sec. 6.3) holds admission data only, not this delegated evidence.
  - Yet sec. 5 requires `replay --snapshot` to recompute the result "from git objects and the committed snapshot alone", byte for byte.

  For an op-C result that cannot hold, which violates R-D5 (replay independent of temporary CI artifacts). The fix is to add the delegated evidence to the committed snapshot: for each class, the host records read, the artifact and result-file sha256s, and the checker outputs the tool produced. Replay must then take those from the snapshot, as it takes admission, and say so. Add a TR45 case for an op-C result.

Residual-trust list

The list is complete for the scope. It now names:

- the host API and its attestations;
- the runner;
- access control on `main`;
- who can delete, hide or edit comments, and the undetected-deletion residual;
- the first `A`;
- the owner's account;
- the authenticity of the snapshot at acceptance time.

I found no unstated assumption.

Consequential edits (writer's point 5)

The diff hunks for TR4, TR11, TR17 and TR19 change only:

- TR4: `A.owner` to `A.owner.id`;
- TR11 and TR19: the admission-point references renumbered by V4, from point 4 to point 3;
- TR17: the near-form example rewritten in the C2 syntax.

The acceptance-section repair moves the X11 clause out of the durable-evidence paragraph into its own bullet, without changing its meaning. The other hunks are the scoped items: sec. 0.2, 14, 15 item 0a, and the S13 list, now including S11-58a-k and TR1-TR46. Nothing else changed.

***

Required corrections

1. **F1 (not blocking):** specify S11-58k's edit 2 completely so that P applies the list, for example with the corrected example above.
2. **F2 (blocking):** include the delegated evidence in the committed snapshot and replay op-C results from it, and extend TR45 to an op-C result.

Optional

- O1. Name the approved record kind in the approval form, for example `oi-authority/1 approve record=authority from=... to=...`.
- O2. N1's wording for chained edits.
- O3. N3: say whether acceptance-time ledger appends need their own approval comment (stricter: yes).

Not verified

- No host call was made. The host semantics are assumed by the design and stated as residuals or specified fail-closed: edit history with content, hidden state, deletion events, comment counts, merged-by id, fork status, and the run record's `head_sha` and file contents.
- No v5.5 implementation exists. The controls were checked against the rules, not run, except the parity rules, which I implemented myself.
- Deterministic gzip output was not measured; the uncompressed sha256 decides.
- The owner decisions reached me through the coordinator, without comment ids.

Owner decisions needed

1. Accept the residual of a withdrawal deleted before any admission observed it, on a host without deletion events (N2), or require another safeguard. For example, a withdrawal could count only once it is recorded in the freeze ledger.
2. Confirm the three refusals stricter than P: (i) the unselected variant, (ii) two edits in one splice, (iii) chained edits. Each is now documented and justified, and the measurement shows no valid, unambiguous operation rejected.
3. Confirm the freeze ledger as constructed (`oi-freeze-ledger/1`, append-only, owner-approved) and N3's approval question.
4. Final authorization of the writer's choices, which match the owner's provisional preferences:
   - the `authority.json` path;
   - the versioned forms;
   - authority changes by review plus a verified approval comment;
   - the numeric id deciding, with the login informational.

Files (D/review-v5.5/; MANIFEST.sha256 covers them)

- `rv55_parity.py` and `out55-parity.txt`: my implementation of the v5.5 rule against P, with random, crafted and A1 cases.
- `rv55_controls.py` and `out55-controls.txt`: S11-58i, j, k and the corrected k.
- `data/`: P's `edits_check.py`, `edits.json` and `ledger.json`.
- `diff-v54-v55.txt`.
