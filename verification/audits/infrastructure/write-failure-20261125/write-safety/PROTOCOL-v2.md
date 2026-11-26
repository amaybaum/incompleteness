# Write gate v2: bounded transport-difference policy (prototype, not adopted)

Local prototype under the owner decision of 2026-11-25 (amaybaum), quoted as relayed by the
coordinating session:

> "Proceed with the bounded transport-difference policy now. ... The solution should be general in
> architecture but conservative in what it accepts: * Exact match: accept normally. * Recognized
> transport-only difference: accept only if it matches an explicitly permitted transformation,
> initially limited to the exact attribution footer and its surrounding whitespace. * Any other
> difference: reject and immediately suspend the affected write mechanism. ... * Require
> independent review and controlled validation before adopting the revised mechanism. Do not
> introduce unrestricted whitespace normalization, fuzzy matching or automatic acceptance of newly
> observed transformations. Keep the existing validated mechanism operational until its
> replacement is approved."

and the two clarifications of the same day (amaybaum, 2026-11-25):

> "Protect meaningful Markdown whitespace. The permitted transformation must not remove whitespace
> that belongs to the intended content, including Markdown hard line breaks or indentation. Add
> negative controls for these boundary cases."

> "Keep the rule extensible but closed by default. Future transport transformations must require
> explicit approval, independent review and regression controls. Never learn new exceptions
> automatically."

**Status.** Nothing here is adopted. Revision r4 was committed on the evidence branch at
`88352d9a75be0ada24b3107ffdab09a512890d31` and revision r5 at
`0a1b5675af31d1885a5e108d6b143bea74ea4aa1`, and r5's non-stopping revision at
`456bdb25e7ea85aeaae6721207e38684df3f8413`. The owner accepted its grant rule, one grant for one
sent write (amaybaum, 2026-11-26T03:43:11Z, #1169 comment 7181966825): "A refusal before transmission must not consume the grant. Refused input: no request sent, grant remains available. Valid input: grant consumed when the write is attempted. Unexpected write discrepancy or uncertain transmission: grant remains consumed, and containment rules apply." `gate.py`, `mock.py`,
`test_gate.py` and `countercontrol.py` are unchanged,
and `gate.py` stays the operational mechanism until the owner approves a replacement. Adoption
needs, in this order: an independent non-author review of this directory's v2 files; the controlled
validation write of §7 under its own owner grant; the owner's approval of the replacement and of the
amended §A.49 text in §8 (§A.50: amending a rule is the owner's).

**Revision r2** (owner decision, amaybaum, 2026-11-25: "Correct the containment policy and gate v2's
missing run-level stop.", with the clarification distinguishing run-level and operation-level
containment) revises §1, §4, §5, §8 and §9 after the independent review of PR #1566 comment
7166798215. `CHANGES-r2.md` maps each review finding to its change.

**Revision r3** (owner decisions Q1 to Q4 of 2026-11-25, amaybaum, with "Fix G1 and G2 as well" and
the simplicity objective "One write gate, one verification procedure, one containment mechanism")
revises §1, §2, §4, §5, §7, §8 and §9 after the delta review of r2. `CHANGES-r3.md` maps each
decision and finding to its change and lists each consolidation.

**Revision r4** (owner decision, amaybaum, 2026-11-25T17:53:56Z, recorded at #1169 comment
7170157100: "1 — Plan identity | Fix and verify enforcement across restarts." "2 — Footer count |
Cap at one permitted footer copy. Additional copies trigger conservative containment.") revises §2,
§5, §7, §8 and §9 after the delta review of r3 (PR #1566 comment 7170013007). `CHANGES-r4.md` maps
each change.

**Revision r5** (owner decision, amaybaum, 2026-11-25T20:29:25Z, #1169 comment 7173759648: "Add the
same pre-write refusal to gate v2 before its validation write. Require targeted tests,
countercontrols and a focused independent check."), committed at
`0a1b5675af31d1885a5e108d6b143bea74ea4aa1`, adds one pre-check: any text field the write would send
(every body and title, of every operation) that contains a less-than sign immediately followed by
an exclamation mark is refused before any request (`gate2.lt_bang_violations`), because GitHub
stored comment 7172299731 with that exclamation mark removed. The reason names the field and each
position and asks the writer to reword; the text is never altered. Its non-stopping revision (owner
decision, amaybaum, 2026-11-25: "I authorize the non-stopping refusal for this specific pre-check,
provided the reviewer confirms compatibility with §A.51.") makes this one refusal raise
`gate2.Refused`, which is not `Halted`, after every other pre-check has passed: no marker, no plan
latch, no in-process latch, and a single-write grant taken by the refused attempt is given back, so
a reworded text can be sent. Every other pre-check and containment rule, and the exact read-back,
are unchanged. Tests `lt1`–`lt7`, countercontrol C4; `CHANGES-r5.md`.

***

## 1. Policy

Every automated text write is read back. The stored text of each field the write sent is compared
byte for byte with the expected text, which is the text sent, fixed and hashed before the write.

| Outcome | Condition | Action |
|---|---|---|
| `exact` | stored equals the expected text byte for byte | accepted |
| `permitted <rule-id>` | stored differs, exactly one rule of the owner-adopted allowlist that applies to that field permits the difference, and the operation is validated under the allowlist or this is its single-write validation write | accepted; a discrepancy record is written (§4) |
| `rejected` | any other difference; no rule, or more than one rule, permits it; a permitted difference on an operation validated by exact read-back only (registry entry without `"allowlist": True`), which stays exact until revalidated; a read-back that is not a string | the sequence ends at once, and every text write stops unless §5's conditions confine the halt to the operation; sent, stored and diff are kept as evidence |

Fields the write did not send (for example the body on a close or label change), the labels and
the state must read back as the write should leave them: as the read made before the write, changed
only as the operation intends (labels added or removed, the state closed), or, for a new Issue or
pull request, no labels and open. This one comparison runs for every operation. No allowlist applies
to it. Titles are compared exactly: the only rule applies to
bodies alone. Failed read-back, an unexpected status, an exception during the write (unknown
outcome), a missing created-object id, a failed pre-check, a missing grant or a failure to write a
discrepancy record end the sequence and write the global marker, as in `gate.py` (§5). The one
exception is r5's refusal of a less-than sign followed by an exclamation mark, which sends nothing
and does not end the sequence.

There is no normalization, trimming, case folding, Unicode normalization or similarity measure
anywhere in the comparison.

## 2. Architecture: integrity verification separated from transport-difference detection

- `gate2.py` verifies content integrity by one procedure for every operation. It fixes the expected
  text, makes one write, reads back, compares bytes and compares the unsent fields, labels and state
  (§1). When they differ it asks `transport_rules.classify(sent, stored, rules, field)`
  for a classification and acts on it. It contains no footer text and no knowledge of any
  transformation (test `r2` checks the source). Send forms are delegated to
  `transport_rules.send_form_violations`.
- `transport_rules.py` holds the allowlist. Each rule is a frozen `Rule` object with a stable `id`, a
  `version`, a `description`, the `fields` it may apply to, and a pure function
  `permits(sent, stored) -> bool` that decides by exact construction. `REGISTRY` is a frozen tuple
  written in source. `classify` validates the registry (a tuple of `Rule`s with unique ids) on every
  call and returns `("exact", None)`, `("permitted", rule_id)` or `("rejected", None)`; two rules
  that both permit a difference make it `rejected` (ambiguity).
- `gate2.Gate2` subclasses `gate.Gate` and imports its operations, pre-checks (§A.49 rules 1 and 4),
  refspec checks, push path, read-back paths and grants. It overrides only the halt mechanism
  (one halt store, §5), the write path (to add classification, the unified comparison, the
  containment decision and records) and `push` (to put pushes under the same store).
- `transport_rules.footer_shaped_tail(sent, stored)` decides rule 3's third condition: the sent
  content (the text sent less its trailing tail as `split_footer_tail` delimits it) is not empty,
  the stored text begins with it, and what follows is only newlines and at most one exact copy of
  `FOOTER_CORE`. It decides how far a stop extends, never whether a difference is accepted:
  acceptance needs `classify` and the exact rule.

## 3. The rule `footer-attribution-1` (version 1)

`FOOTER_CORE` is these exact bytes, with no newline at either end:

```
---
_Generated by [Claude Code](https://claude.ai/code)_
```

**Split.** For a text `x`, `split_footer_tail(x)` returns `(content, footer_count)`:

1. `t1` is `x` with trailing newline characters (U+000A only) removed.
2. If `t1` ends with `FOOTER_CORE`, let `before` be `t1` without it, `content` be `before` with
   trailing newlines (U+000A only) removed, and `sep` the newlines between them. The footer is
   recognised, giving `(content, 1)`, only when `sep` has at least two newlines, `content` is not
   empty, and `content` does not itself end with `FOOTER_CORE`.
3. Otherwise the result is `(t1, 0)`.

**Permit.** `permits(sent, stored)` is true iff both are strings,
`content(sent) == content(stored)` byte for byte, `footer_count(stored) == 1` and
`footer_count(sent) <= 1`. The rule applies to the field `body` only.

**What may differ, exactly:**
- the presence of `FOOTER_CORE` at the very end: absent or present in the sent text, present exactly
  once in the stored text;
- the number of newline characters (U+000A) between the last character of the content and
  `FOOTER_CORE`, provided each text carrying the footer has at least two there;
- the number of newline characters (U+000A) after the content (when the sent text has no footer) or
  after `FOOTER_CORE`, up to the end of the text.

**Everything else is content and must be byte-identical**, including: spaces and tabs anywhere,
also at the end of the last content line (two trailing spaces are a Markdown hard line break) and
as indentation (indented code, nested list items); a trailing backslash (a hard line break);
space-only lines; any non-ASCII space, carriage return, form feed, vertical tab or format
character; and any character after the footer other than a newline.

**Not permitted:** a footer removed, doubled, altered by one character, replaced by another
attribution, preceded by fewer than two newlines (with one, the last content line becomes a setext
heading), indented, followed by anything but newlines, or not at the very end; a footer added to an
empty body; any difference in a title or in a field not sent.

**Real cases.** Permitted: #1558, #1062, #1245, #1556 (footer appended to a body sent without it)
and #1505 (three newlines before the footer sent, two stored). Exact: #1565 and both #1548
validation writes.

**Known limit.** Newlines at the end of the content are not protected. In ordinary Markdown a run
of two or more newlines between blocks renders identically; inside a fenced code block left
unclosed at the end of a body, the number of trailing blank lines can be visible, and the same holds
for an unclosed HTML `<pre>`, `<textarea>` or comment and for a math block, where the footer can also
fall inside the block or be hidden. The rule does not parse Markdown, by design. The amended rule 2
states this limit (§8).

## 4. Records kept

**Permitted difference.** `discrepancy-<operation>-<target>-<field>-<pid>-<seq>.json` in the
evidence directory, created exclusively and fsynced, with: `operation`, `target`, `field`, `repo`,
`plan_id`, `time`, `rule_id`, `rule_version`, `rule_description`, the complete `sent` and `stored` texts,
`sent_sha256`, `stored_sha256`, byte lengths, `unified_diff` (exact lines, with the diff(1) marker
for a missing final newline) and `char_opcodes`, a character-level edit script that reproduces the
stored text from the sent text exactly (test `p3` checks the reproduction). Records are written only
after every field and every check of the write has passed, so a write that halts on a later field
leaves no record (test `q4`). If a record cannot be written, the write is not accepted: the sequence
ends and the global marker is written, naming any record already written for that write.

The evidence directory must be durable (not RAM-backed scratch): records and halt evidence are
copied to the evidence branch under §A.26 and §A.42 before the session ends.

**Rejected difference.** The plan latch `HALT-PLAN.<plan_id>` and the halt marker, `HALT` or
`HALT.<operation>` as §5 decides (JSON: reason,
scope, mechanism, pid, time, and for each evidence text its file name, SHA-256 and the complete text),
with `halt-<scope>-<pid>-<seq>-<field>.sent.txt`, `.stored.txt` and `.diff.txt` beside it, each
created exclusively so that two halts in one process do not overwrite each other's evidence (test
`c6`). The texts are embedded in the marker, so an evidence file that cannot be written loses
nothing (test `q8`).

## 5. Containment: one halt store, run level and operation level

Two levels, as the owner's clarification of 2026-11-25 distinguishes them and amended rule 3 (§8)
states them, kept in one halt store: the files of the halt directory, mirrored in the writer process
by `gate2._HALTED`. One function (`Gate2._check_clear`) reads the store, at the points stated below;
one function (`Gate2._halt`, with `_latch`) writes it.

**Run level: the plan latch.** A sequence is one run of a plan. The plan id is fixed in the plan's
record before the run and never generated per process: `gate2.record_plan(halt_dir, plan_id)` writes
the plan record `PLAN` in the halt store once, exclusively, and refuses while a record exists; the
gate never writes it. The plan's record is not deleted, replaced or rewritten while the plan is
active, and a plan whose sequence a halt has ended stays active until a recorded owner decision
resolves that halt. Every `Gate2` is
constructed with a `plan_id` (required; `[A-Za-z0-9][A-Za-z0-9._-]{0,99}`), which must equal the
recorded one: the gate takes the id from the record, and refuses, with no request made, when the
record is missing or unreadable or names another id, at construction and at every check of the
store, so neither a restarted process nor a running one can substitute an id (tests `q16`, `q17`,
also in a separate process). Every halt, and every refusal of a write or push, ends the sequence: it
is appended to `_HALTED`, which stops every `Gate2` in the process whatever the caller does with the
exception, and written to `HALT-PLAN.<plan_id>`, which stops every process that runs the same plan,
including a restarted one (test `q10`). Nothing in the module clears either; the latch file is removed
by hand only on a recorded owner decision. A loop that catches `Halted` per item, the shape of
`edit.py`, makes no further write (test `q3`, also with a new gate per item and with a `.notified`
file appearing mid-loop). Plans run in one process by default (`run_plan`); a plan whose record
names several processes passes the same `plan_id` to each. A later sequence is a new plan, whose
record can be written only after the previous plan's record has been removed by hand; it then meets
the markers below.

**Beyond the run.** The global marker `HALT`, the same file name `gate.py` uses, stops every
mechanism for every later process using the halt directory. `gate2` writes it for every failure
except one: a read-back mismatch for which every condition of rule 3 holds, decided mechanically
from the write, its read-back and the halt store (`Gate2._containment_scope`); a mismatch that the
store does not show is not counted:

1. the outcome is known: the request returned an expected status and, for a created object, its id
   (the decision is reached only past those checks);
2. read-back succeeded, and no unsent field, label or state differs from what the write should leave
   (§1), on every operation;
3. every rejected field difference lies in a footer-shaped tail
   (`transport_rules.footer_shaped_tail`): after the sent content, only newlines and at most one
   exact copy of the attribution footer; a classification that raised is not a rejected difference;
4. no other operation's marker is outstanding (any `HALT.<x>` file other than `.notified`
   companions), no global marker, and no `.notified` companion of this operation's marker left from
   an earlier incident (it would let later sequences start without the owner being told).

Then, and only then, `HALT.<operation>` is written instead and blocks that operation alone. If that
marker already exists when the halt is written (another process halted meanwhile) or cannot be
written, the halt is made global (`escalated_from` in the record). So an unknown outcome
(`TimeoutError`, test `q1`), a content change (`0.3` to `0.4`, test `q2`), a hard break removed at
the end of the content, any appended text other than newlines and one exact footer (an injected
link, a forged "Owner decision" line, spaces after the footer, a look-alike footer, `[bot]` after a
title: test `q9`), two or more footer copies (tests `q5`, `q9`, `q18`), a label or state change on
any write (test `q13`), a failed read-back, a pre-check refusal, a missing grant, a push failure and
an unknown operation are all global; a removed or misplaced exact footer, or newlines alone, is
operation-level (tests `q5`, `q9`, and every negative control, whose expected scope is computed by
an independent restatement of condition 3). Recognizing that shape is not acceptance: `classify`
still rejects each of those differences.

**Owner told before a later sequence writes.** While any `HALT.<operation>` lacks its companion
`HALT.<operation>.notified`, every later sequence refuses every write and push (test `c1b`). A person
creates the companion by hand once the evidence is kept and the owner has been told through a
channel other than an automated GitHub write; the gate never creates it. The operation stays
suspended until a recorded owner decision removes its marker; the companion is removed with it
(otherwise condition 4 makes the operation's next halt global, test `q14`).

The store is checked for a write at its start, again once the operation is known (before the
pre-write read) and again immediately before the write request, but not before the read-back
request; for a push at its start only, before any git command, not again before the remote-ref reads
or `git push`. Markers are created with `O_CREAT|O_EXCL` and fsync, never overwritten and never
removed by the gate. Removal is by hand on a recorded owner decision. Placing both gates' markers in
one directory makes a `gate.py` halt stop `gate2` as well.

**Strictness.** Pre-write refusals and push failures write the global marker, which is stricter than
rule 3 requires: they show a defect in the writer or its environment rather than in one operation's
transport, and the strictness is intended.

**Known limits.** Writers are single-threaded: the check of the store and the request that follows
are not atomic across processes or threads (as in v1), although the store is checked again
immediately before the write request (test `q15`). Markers are local files: other hosts, containers
and sessions are held only if they share the halt directory, and otherwise by telling the owner.
`gate.py` checks only `HALT`, so a v1 gate in the same process is not stopped by a plan latch or an
operation marker. Within those limits, residual exposure under operation-level containment is
bounded to footer-shaped tails: a shared layer that changes text before the end of the content, or
appends anything else, stops everything on its first such write.

**Relation to §A.49 rule 3 and §A.51 item 5.** `gate2` implements amended rule 3 (§8) and the
amended §A.51 item 5: the package's operations stop on every failure the gate treats as global,
including a §A.49 rule 1 refusal, and continue in a later sequence only after an operation-level
halt.

## 6. The allowlist is closed by default

- `REGISTRY` is a frozen tuple in source. Neither module offers an API that adds, changes or removes
  a rule, and nothing is learned from an observed difference: a newly observed transformation is a
  `rejected` outcome and a halt, every time.
- A rule is added, changed (a new version) or removed only by an explicit owner decision recorded
  with author and time, followed by an amendment of this protocol and of the allowlist named in
  §A.49 rule 2, with:
  - the exact construction of the rule and the characters it lets differ;
  - its own positive controls from real evidence, and negative controls and countercontrols showing
    that content, links, internal whitespace, Markdown structure and whitespace, and authorization
    records still reject;
  - mutation runs showing that looser variants of the rule fail those negative controls;
  - an independent non-author review, then a controlled validation write under its own grant.
- Rule ids are identifiers: never reused for a different rule; a changed rule takes a new version,
  and records name both.

## 7. Controlled validation write proposed for #1548

Proposed, not authorized: it needs its own owner grant (§A.51 item 2) and comes after the
independent review.

- Operation: REST Issue-body edit, `PATCH repos/amaybaum/incompleteness/issues/1548`, `body` field,
  through `gate2` with the `gh api` transport of `issue-1548/validation-2/run_gate.py`, registry
  `{"issue.edit_body": {"validated": False, "send_form": None}}`, a single-write grant for
  (`issue.edit_body`, 1548) and `plan_id="validation-1548-v2"`, recorded by `record_plan` in the
  plan record before the run. Under amended §A.51 item 2 an
  outcome of `permitted footer-attribution-1`, with its record, validates the operation under the
  allowlist; the registry then records `"allowlist": True` for it only on the owner's decision.
- Sent text: the body below, sent **without** the footer, no trailing newline, 685 bytes, SHA-256
  `7da70f20dea6aeaf0a062b51b5a652d505028dcfcf5bff289234311e1072efce`:

```
WRITE-PATH-TEST: reusable Issue for automated write-path testing (not research).

Designated by owner decision recorded at comment 7165319386. This body is the controlled validation write of the revised write gate (gate2) with the bounded transport-difference policy. It is sent without the attribution footer; the outcome must be an exact match, or a difference permitted by rule footer-attribution-1 alone, kept as a record with both texts, their digests, the diff and the rule.

The earlier validation bodies and the original body of this Issue are preserved on branch `evidence/write-failure-20261125`, under `verification/audits/infrastructure/write-failure-20261125/issue-1548/`.
```

- Expected stored text (prediction from the four D1 observations): the sent text followed by
  `"\n\n"` and `FOOTER_CORE`, no trailing newline, 743 bytes, SHA-256
  `7e35afeb7185222b053d77c566ada17c004c1ba9328c661f35de2a06f4a5a763`.
- Pass: the outcome is `exact` or `permitted footer-attribution-1`, the title is unchanged, and for
  `permitted` the discrepancy record exists with both complete texts, both digests, the diff and the
  rule id and version. Any other outcome ends the sequence, halts as §5 decides and ends
  validation; the evidence is kept under §A.26 and the owner is told. Either passing outcome is recorded as observed; the
  prediction of `permitted` is not a pass condition.
- Before the write, #1548's current body is saved (SHA-256 of
  `issue-1548/validation-2/stored-body.md`:
  `c5c14c60634dfe4d8c13a8f9fd4006a2940fd825592170a2dc0795d6f4758780` if unchanged).

## 8. Proposed amended text of AGENTS.md §A.49 rules 2 and 3 and §A.51 items 2 and 5

Revision r4 of the amendment text on PR #1566, as it stands in the draft (rule 2, rule 3, §A.51
items 2 and 5). The adoption lines are dated and cite the owner's approval record at merge.

> 2. **Exact read-back.** After every write, the stored text is read back and compared byte for
>    byte with an expected text fixed before the write: the text sent, for every body, title,
>    comment, review and review comment. The stored text is accepted only when it is byte-identical
>    to the expected text, or when it differs from it only by one transformation listed, by
>    identifier and version, in the transport-difference allowlist stated in this rule. Each listed
>    transformation states the fields it applies to and the exact characters it lets differ, and is
>    decided by exact construction. This text is authoritative: a registry in code that applies the
>    allowlist lists the same entries with the same effect, and where the two differ this text
>    governs. The allowlist has one entry, `footer-attribution-1` version 1: in the body of an
>    Issue, a pull request or a comment only, never in a title, a review or a review comment, the
>    attribution footer (the line `---` followed by the line
>    `_Generated by [Claude Code](https://claude.ai/code)_`) after content that is not empty, once
>    at the very end of the stored text and not repeated there, and absent from, or likewise at the
>    very end of, the text sent, with only the number of newlines before it (at least two) and after
>    it differing; spaces, tabs and every other character are compared exactly. The newlines at the
>    end of the content are not protected: where the content ends inside an unclosed block, such as
>    a fenced code block, an HTML `<pre>`, `<textarea>` or comment, or a math block, a change in
>    their number can be visible, and the footer can fall inside the block or be hidden. For every
>    accepted difference, the complete sent
>    and stored texts, their SHA-256 digests, the exact diff, and the identifier and version of the
>    permitting transformation are kept as a record. The allowlist applies to an operation validated
>    under it and to the write that validates an operation (§A.51 item 2); an operation validated by
>    an exact match before the allowlist was adopted is held to an exact match until it is validated
>    again under the allowlist. A transformation enters, changes in or leaves
>    the allowlist only by owner decision, with independent review and its own regression
>    controls; none is added because it has been observed. The text sent is chosen from the footer
>    handling observed for that operation. Observed with Claude Code on 2026-11-23: comments posted
>    through the REST API and pull requests opened through the GitHub connector were stored
>    unchanged when the text sent ended with one blank line, `---`, the footer line and no trailing
>    newline; a pull-request description edited through the connector had such a footer removed,
>    and was stored unchanged when sent without one. Observed on 2026-11-25: Issue bodies edited
>    through the REST API and sent without the footer were stored with it appended after one blank
>    line, and one sent with two blank lines before the footer was stored with one. These are
>    observations, not rules of the tooling. No normalization or fuzzy comparison is allowed. Any
>    other difference, or a read-back that fails or cannot be completed, is a mismatch.

> 3. **Stop on a mismatch.** A mismatch ends the sequence in which it occurs: no further GitHub write
>    or push is made in that sequence, whatever the writer does on the failure; catching or ignoring
>    the error does not continue it. A sequence is the writes made by one run of a plan (every
>    automated writer runs one), in one writer process unless the plan's record names several, and
>    then in all of them. The plan's identifier is fixed in the plan's record before the run and is
>    never generated per process. The plan's record is not deleted, replaced or rewritten while the
>    plan is active, and a plan whose sequence a halt has ended stays active until a recorded owner
>    decision resolves that halt. The end of a sequence is recorded persistently for its plan; every
>    process of the plan checks that record at the start of each write and push and again immediately
>    before the write request, restarting a process does not continue the sequence, and only a
>    recorded owner decision clears the record. Every automated GitHub text write, for every agent and
>    session, then stops as well, unless every one of the following conditions holds, each decided
>    mechanically from the write, its read-back and the local halt record; a mismatch the writer
>    cannot see there does not count:
>    - the outcome of the write is known: the request completed with an expected status and, for a
>      created object, the response names its id;
>    - the read-back succeeded, and no field the write did not send, no label and no state differs
>      from what the write should leave, judged against the read made before the write or, for a
>      created object, the values a new object has;
>    - every rejected difference lies wholly in a footer-shaped tail after the last character of the
>      sent content: the text sent, less the newlines and any attribution footer at its very end
>      (rule 2), is not empty and is stored unchanged as the start of the stored text, and what
>      follows it there consists only of newlines and at most one exact copy of the attribution
>      footer. Any other appended text stops every automated text write. This shape decides only how
>      far the stop extends; a difference is accepted only as rule 2 provides;
>    - no other operation has a mismatch outstanding, that is, one that no recorded owner decision
>      has yet resolved.
>
>    When all of them hold, only the failed operation is suspended, for every agent and session: its
>    tool (the client, such as `gh api`), its path (the API endpoint, such as
>    `PATCH /repos/{owner}/{repo}/issues/{number}`) and its kind of write (such as a body edit, as
>    distinct from closing an Issue through the same endpoint). Other operations may then continue, in
>    a later sequence, through validated mechanisms. Before any later sequence writes, the text sent
>    and the text stored are kept as evidence under §A.26 and the owner is told, through a channel
>    other than an automated GitHub write. Only a recorded owner decision resumes a suspended
>    operation, after it is corrected and validated (§A.51 item 2), or lifts a stop of every automated
>    text write; a later correction does not make a failed write a pass.

§A.51 item 2:

> 2. **Standing write grants.** An operation is validated when one write of it, made through the same
>    tool and path under the owner's grant for that one write, passed §A.49's read-back: an exact
>    match, or a difference that rule 2's allowlist permits, recorded as that rule requires. A
>    package may grant its writers standing use of validated operations on its targets, without a
>    grant for each write. An operation that is not validated needs a grant for each write. A
>    standing grant to edit comments extends only to comments that the package's designated writers
>    wrote under it; editing a comment written under another work package, or by the owner in person,
>    needs a separate authorization. Every write remains subject to §A.49.

§A.51 item 5:

> 5. **Stop.** An unknown outcome of a write, push or launch, a step outside the package's scope, a
>    failed preflight or push read-back (item 3), a §A.49 rule 1 refusal, a failed check the package
>    names as a stop, or evidence that conflicts with the package's records stops the package's
>    automated operations at once. A §A.49 mismatch, a failed text read-back included, stops them in
>    the same way, and every automated text write as §A.49 rule 3 provides, unless that rule confines
>    it to the failed operation; then the sequence in which it occurred still ends at once and the
>    failed operation is suspended, and the package's other operations may continue in a later
>    sequence through validated mechanisms. The evidence is kept under §A.26 and the owner is told.
>    Only a recorded owner decision resumes a stopped package or a suspended operation.

## 9. Controls and results (mock transport only)

Run in this directory: `python3 -I -B test_gate2.py` and `python3 -I -B countercontrol2.py`.
Recorded outputs: `results-tests2.txt`, `results-countercontrol2.json`.

**`test_gate2.py`: 66 tests, all pass.** The unchanged v1 suite `test_gate.py` (18 tests) and v1
countercontrols pass in the same run (`results-tests2.txt`).

- Registry (`r1`–`r5`): closed frozen tuple with one rule; no footer formatting in `gate2.py`;
  malformed registries raise; a classification failure halts globally; two rules permitting the same
  difference are `rejected` and halt (footer-shaped, so operation-level).
- Positive (`p1`–`p5`): exact; footer appended; differing newlines before and after the footer; hard
  breaks and indentation kept alongside an appended footer; the footer quoted earlier in the
  content; the real #1558, #1062, #1245, #1556 and #1505 pairs permitted and #1565 and the #1548
  validations exact; records checked field by field; the five-body D1 replay accepted with four
  records.
- Negative (`test_neg_*`): each case rejected by `classify` and, through the gate: one write; a halt
  whose scope (global or operation) equals that of an independent restatement of rule 3's
  condition 3; sent, stored and diff kept, in files and in the marker, with matching digests; no
  record; the same gate and any other gate in the process refuse every mechanism; a later sequence
  refuses the operation; after an operation-level halt, a later sequence writes nothing until
  `.notified` exists and then writes another operation; after a global halt, a later sequence writes
  nothing through any mechanism even with every `.notified` present.
- Containment (`c1`–`c6`): the sequence latch after an operation-level halt, in the same gate and
  another gate of the process, also after notification, and a later sequence writing a comment, a
  label and a push but not the operation; notification required before a later sequence writes;
  global marker blocks all with zero transport calls and is not overwritten; an existing operation
  marker refuses its operation and ends the sequence; an unknown operation halts globally; a marker
  blocks a separate process; a second footer-shaped halt with another operation's marker
  outstanding is global, with separate evidence files.
- Probes (`q1`–`q8`), from the review of r1: `TimeoutError` on PATCH is global; `0.3` to `0.4` is
  global; a loop catching `Halted` makes zero further writes; no orphaned record when a later field
  fails; rule 3's conditions on a fixed table; an outstanding marker of another operation makes a
  halt global; an internal exception latches and is global; the marker embeds the texts when
  evidence files cannot be written.
- Revision r3 (`q9`–`q15`): appended text other than newlines and exact footers (link, forged
  owner line, spaces, look-alike footer, `[bot]` in a body and a title) is global, footer-shaped
  differences are operation-level and still rejected (Q2); the plan latch refuses the same plan in a
  restarted gate and in a separate process after `.notified` exists, while a new plan writes (Q3);
  `plan_id` is required and checked; a permitted difference passes a single-write validation write
  and an operation validated under the allowlist, and halts an operation validated by exact
  read-back only (Q4); labels and state are compared on body edits, creates, pull-request edits,
  closes and label changes (G1); a stale `.notified` companion, or an operation marker appearing
  during the write, makes the halt global (G2); a global halt recorded during the pre-write read
  stops the write request (G3).
- Revision r4 (`q16`–`q18`): the plan record is never rewritten while it exists; a caller id that
  differs from it is refused at construction, in this process and in a separate one, a missing
  record is refused, and a record swapped during the run refuses the next request; after an
  operation-level halt and `.notified`, a restart with the same id or a substituted one writes
  nothing, in this process and in a separate one (item 1); one footer copy (or none) with newlines
  is operation-level, two copies, two joined copies and fifty copies are global, each still
  rejected (item 2). Tests that used a doubled footer as their operation-level case now use a
  removed footer.
- Ported `gate.py` guarantees (`g01`–`g17`): as before, with every failure global.
- Revision r5 (`lt1`–`lt7`): the less-than/exclamation sequence refused in every body and title of
  every text operation, at the start, at the end, before the footer, in code spans and a fenced
  block, with every position named, zero requests and nothing written to the halt store;
  separated characters and look-alikes sent and stored exactly; after a refusal the same gate, a
  new gate of the plan and a later sequence send the reworded text once, read back exactly; a
  refused text followed by another pre-check failure, or a text failing both, halts as before; a
  single-write grant survives a refusal and is then used once.

**`countercontrol2.py`: C1, C2, C3 and C4 pass.**

- C1: `gate.py` halts on the real #1505 and #1558 pairs; `gate2` accepts each as
  `permitted footer-attribution-1` with one complete record. D1 replay: `gate.py` 1 write then a
  halt; `gate2` 5 writes and 4 records.
- C2, rule mutants; baseline 66 run, 0 failed: strip all whitespace: 7 tests fail; `.strip()` on
  the whole text: 7; ignore the footer text: 5; accept a doubled footer: 5; let spaces and tabs in
  the tail differ: 5; no two-newline separator check: 4. Each has negative controls among its
  failures.
- C3, gate mutants: passing a rejected difference off as permitted: 25; skipping the discrepancy
  record: 2; a single global marker for every halt: 16; no sequence latch: 7 (among them `c1`,
  `q3`, `q10`); a latch in memory only, without the plan latch file: 4 (`q10`, `q15`, `q17`,
  `lt6`); every halt confined to its operation (before r2): 31; narrowing without the tail condition: 16; narrowing on
  any appended text (r2's condition): 7 (among them `q9`); labels and state compared only on their
  own operations (before G1): 1 (`q13`); a stale companion ignored (before G2): 1 (`q14`); the
  allowlist applied to operations validated by exact read-back only (before Q4): 1 (`q12`); the
  caller's plan id taken in place of the record's (before r4 item 1): 2 (`q16`, `q17`); any number
  of footer copies narrowing (r3's condition, before r4 item 2): 4 (among them `q18`).
- C4, mutants of the r5 refusal: no refusal: 6; titles not checked: 3 (`lt1`, `lt2`, `lt4`); the
  text substituted and sent: 6; the refusal latching like other pre-checks: 6 (among them `lt1`,
  `lt5`, `lt7`); the positive control `lt3` passes under each. With the gate as it is, for each of
  the seven text fields a refused text makes no request and leaves only the plan record, and a valid
  write then succeeds exactly on the same gate and on a new gate of the plan. Without the refusal,
  under a transport that removes the exclamation mark, each field is written once and the exact
  read-back halts globally on the change.

**Limits.** These controls show the gate's control flow and the rule's exact behaviour on stated
inputs, against a mock. They do not show the behaviour of the real GitHub path; §7 is the first
step for that. Test `c5` runs in a subprocess that imports unmutated modules, so in-process mutants
do not reach it; the same holds for the subprocess parts of `q10`, `q16` and `q17`. The in-process
parts of `q16` and `q17` fail under the plan-id mutant.

## Files (new; the v1 files are unchanged)

| File | Content |
|---|---|
| `transport_rules.py` | Allowlist: `Rule`, `REGISTRY`, `classify`, `footer_shaped_tail`, send forms |
| `gate2.py` | Gate v2 prototype (imports `gate.py`) |
| `mock2.py` | Mock extensions (subclasses `mock.MockGitHub`) |
| `test_gate2.py` | Control suite (66 tests) |
| `countercontrol2.py` | C1–C4 |
| `results-tests2.txt`, `results-countercontrol2.json` | Recorded outputs |
| `PROTOCOL-v2.md` | This document |
| `CHANGES-r2.md` | Revision r2: each review finding and its change |
| `CHANGES-r3.md` | Revision r3: each owner decision and finding, its change, and the consolidations |
| `CHANGES-r4.md` | Revision r4: each change, its reason and its tests |
| `CHANGES-r5.md` | Revision r5: the pre-write refusal, its non-stopping revision, its tests and countercontrols |
