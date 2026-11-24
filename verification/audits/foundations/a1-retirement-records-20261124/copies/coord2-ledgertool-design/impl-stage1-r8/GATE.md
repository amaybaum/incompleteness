# Gate (step 0): B-2 and N-5 against adopted design v5.5.9

Design: `DESIGN-v5.5.9.md`, sha256 cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9 (verified).
Review: `review-stage1-r7/review.md`, sha256 0e4034339138326302c79e7cdfd377a90e23af0688eddb04f6507d292936b33b (verified).
Subject: 1611c9e81a3c736b084dd9eaef5a02a6e627cdf3, worktree clean. Determination made before any file of the subject
was changed.

## Item 1: B-2 (control only)

Design text, sec. 6.3, "The freeze ledger", "Reconciliation":

> 1481  - a ledger or snapshot event that conflicts with the thread refuses, as does a missing ledger or
> 1482    one that cannot be verified.

and the refusal's point and exit (admission):

> 1488 **Admission.** The tool performs the following inside a host CI job. Any step that fails or cannot
> 1489 be completed refuses admission with ERROR `CONFIG_UNREVIEWED`:

Control requirement, sec. 10.4: "A control's predicate must test its whole stated expectation" (TR36, line 2319:
"the freeze ledger missing, unverifiable, or conflicting with the thread | ERROR").

The engine at 1611c9e8 already implements this (review r7 sec. 1: engine refuses at point `ledger`, exit 65; only
mutant R7-06 admits). The change adds a control for behaviour the design states verbatim and changes no engine code.

**Determination: control gap (defect of the control suite against the design). No normative change. Proceed.**

## Item 2: N-5 (engine)

### What the design says an event is, and where it is recorded

> 1447 once existed. So withdrawals and supersessions, once observed, are made durable on `main`:
> 1449 - **The ledger.** It is a record `oi-freeze-ledger/1` at `A.freeze_ledger_path` on `main`. It is an
> 1450   append-only list of observed events per plan and round. Each event is a designation, withdrawal
> 1451   or supersession, with its commit ids, comment id, author numeric id, creation time, edit status
> 1452   as read, first line, and body sha256.

> 1454 ... Every acceptance
> 1455   landing (sec. 5) also appends the events its admission observed.

Sec. 5, "Durable evidence": one landing commits both records of the same observation:

> 814   - **The admission snapshot** of sec. 6.3, and its sha256.
> 817   - **The events the admission observed,** appended to the freeze ledger only with the append's own
> 818     owner approval comment (sec. 6.3, N3).

and the snapshot itself records the same comments and the snapshots already committed:

> 1548 - for every comment of admission point 3: id, author numeric id, creation time, the blob sha256 of
> 1549   the version of `A` in force at its creation, edit status, hidden state, full first line and body
> 1550   sha256;
> 1551 - the freeze-ledger blob, and the committed snapshots it was reconciled with;

So the design itself puts one observed comment into the ledger and into every later snapshot: duplicate records of
one comment are the designed normal case, not an anomaly. Each record is an observation of one comment, identified by
its comment id, whose id, author and creation time the host attests as immutable (line 1575: "a comment's immutable
id, numeric author id, creation time"; line 1467: "the comment is matched by its immutable id, author numeric id,
creation time and edit status").

### How the design processes it

> 1513 5. **Deterministic state.** The forms for this plan and round, together with the bound events of the
> 1514    freeze ledger and committed snapshots, are processed in order of creation time, then comment id.
> 1517    - a withdrawal of `F` makes it withdrawn;

> 1365   completed; the admission its snapshot records stands, and the events it appended bind under
> 1366   reconciliation. ...  A withdrawal, and the
> 1367   revoking half of a supersession, bind from their creation.

A withdrawal is one comment with one creation; "makes it withdrawn" is the effect of that one withdrawal. Nothing in
v5.5.9 says that a withdrawal recorded in two places is two withdrawals. The ordering key "creation time, then comment
id" (1514) totally orders events only if a comment id is one event.

### The N-5 sequence under the design

F designated; W (owner comment) withdraws F; F2 designated (owner comment, present); F2 admitted and landed, so W is
in the ledger and in the committed snapshot; W's comment deleted. Under 1476-1478 W binds ("a withdrawal ... in the
ledger or in a committed snapshot binds, even if its comment is now deleted"); under 1516-1517 F is withdrawn and F2
designated; 1521: "The run's `F` is admitted only if, at the end, it is the one designated commit of the round." F2
is that commit; none of the listed refusals (1522-1525) applies to one withdrawal of a designated commit. **The design
prescribes that F2 is admitted.** The engine at 1611c9e8 refuses ("a withdraw names a revoked commit") because it
processes W once per record. This is an implementation defect against 1513-1517 and 1521.

The engine already holds the one-comment-one-event reading between the thread and the records: a recorded event
whose comment is present is not processed again (`seen` in `admit`, point 5). The fix extends the same rule to the
records among themselves; it adds no new concept.

### Two records of one comment that differ

- Comment present: if two records of one comment differ in kind, commits, author, creation time or first line, at
  least one of them differs from the comment itself, so 1481 ("a ledger or snapshot event that conflicts with the
  thread refuses") already prescribes the refusal (the engine at 1611c9e8 compares only author and first line with
  the thread; the duplicate check covers the remaining observed fields through the other record).
- Comment deleted: two records of one immutably attested comment that differ cannot both be its observation; the
  event's content cannot be established. The design's refusals: 1524-1525 "any other conflict", and 1488-1489 "Any
  step that fails or cannot be completed refuses admission". Neither silently merging nor choosing one record is
  prescribed; refusing is the reading these lines give.

Fields compared: the observed fields of 1450-1452 that the engine's records carry: `kind`, `commit`, `by`,
`created_at`, `author_id`, `first_line`, and `body_sha256` where both records carry it (the engine's own snapshot
events do not carry a body sha256; comparing a missing value with a present one is outside this item, cf. N-6).
Engine-derived fields of a snapshot event (`owner_comment`, `designates`, `processed`, `bound`) are not observations
and are not compared. The check runs over the recorded events of this plan and round (the set the engine already
filters), before point 5.

**Determination: implementation defect against v5.5.9 (1450-1455, 814-818, 1365-1367, 1513-1517, 1521); the
conflicting-duplicate refusal is prescribed by 1481 (comment present) and 1488-1489 / 1524-1525 (comment deleted).
No normative change. Proceed.**

Not acted on: N-6 (missing event keys), N-7 (snapshots of other rounds), the narrowness of the thread-conflict
comparison to author and first line, and anything else.
