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

**Status.** Nothing here is adopted. No GitHub write, network write, commit or push was made.
`gate.py`, `mock.py`, `test_gate.py` and `countercontrol.py` are unchanged, and `gate.py` stays the
operational mechanism until the owner approves a replacement. Adoption needs, in this order: an
independent non-author review of this directory's v2 files; the controlled validation write of §7
under its own owner grant; the owner's approval of the replacement and of the amended §A.49 text
in §8 (§A.50: amending a rule is the owner's).

**Revision r2** (owner decision, amaybaum, 2026-11-25: "Correct the containment policy and gate v2's
missing run-level stop.", with the clarification distinguishing run-level and operation-level
containment) revises §1, §4, §5, §8 and §9 after the independent review of PR #1566 comment
7166798215. `CHANGES-r2.md` maps each review finding to its change.

***

## 1. Policy

Every automated text write is read back. The stored text of each field the write sent is compared
byte for byte with the expected text, which is the text sent, fixed and hashed before the write.

| Outcome | Condition | Action |
|---|---|---|
| `exact` | stored equals the expected text byte for byte | accepted |
| `permitted <rule-id>` | stored differs, and exactly one rule of the owner-adopted allowlist that applies to that field permits the difference | accepted; a discrepancy record is written (§4) |
| `rejected` | any other difference; no rule, or more than one rule, permits it; a read-back that is not a string | the sequence ends at once, and every text write stops unless §5's conditions confine the halt to the operation; sent, stored and diff are kept as evidence |

Fields the write did not send (for example the body on a close or label change) must stay
byte-identical. No allowlist applies to them. Titles are compared exactly: the only rule applies to
bodies alone. Failed read-back, an unexpected status, an exception during the write (unknown
outcome), a missing created-object id, a failed pre-check, a missing grant or a failure to write a
discrepancy record end the sequence and write the global marker, as in `gate.py` (§5).

There is no normalization, trimming, case folding, Unicode normalization or similarity measure
anywhere in the comparison.

## 2. Architecture: integrity verification separated from transport-difference detection

- `gate2.py` verifies content integrity. It fixes the expected text, makes one write, reads back and
  compares bytes. When they differ it asks `transport_rules.classify(sent, stored, rules, field)`
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
  (run-level latch and two-level markers, §5), the write path (to add classification, the
  containment decision and records) and `push` (to put pushes under the same latch).
- `transport_rules.tail_confined(sent, stored)` decides rule 3's third condition: the sent content
  (the text sent less its trailing tail as `split_footer_tail` delimits it) is not empty and the
  stored text begins with it. It decides where a difference lies, never whether it is permitted.

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
`time`, `rule_id`, `rule_version`, `rule_description`, the complete `sent` and `stored` texts,
`sent_sha256`, `stored_sha256`, byte lengths, `unified_diff` (exact lines, with the diff(1) marker
for a missing final newline) and `char_opcodes`, a character-level edit script that reproduces the
stored text from the sent text exactly (test `p3` checks the reproduction). Records are written only
after every field and every check of the write has passed, so a write that halts on a later field
leaves no record (test `q4`). If a record cannot be written, the write is not accepted: the sequence
ends and the global marker is written, naming any record already written for that write.

The evidence directory must be durable (not RAM-backed scratch): records and halt evidence are
copied to the evidence branch under §A.26 and §A.42 before the session ends.

**Rejected difference.** The halt marker, `HALT` or `HALT.<operation>` as §5 decides (JSON: reason,
scope, mechanism, pid, time, and for each evidence text its file name, SHA-256 and the complete text),
with `halt-<scope>-<pid>-<seq>-<field>.sent.txt`, `.stored.txt` and `.diff.txt` beside it, each
created exclusively so that two halts in one process do not overwrite each other's evidence (test
`c6`). The texts are embedded in the marker, so an evidence file that cannot be written loses
nothing (test `q8`).

## 5. Containment: run level and operation level

Two levels, as the owner's clarification of 2026-11-25 distinguishes them and amended rule 3 (§8)
states them.

**Run level.** A sequence is the writes of one run of a writer process or of a plan. `Gate2` latches
on every `Halted` it raises and on every other exception during a write or push: from then on, that
instance and every other `Gate2` instance in the process refuse every write and push, before any
request, whatever the caller does with the exception (`_SEQUENCE_STOP`; nothing in the module clears
it). A loop that catches `Halted` per item, the shape of `edit.py`, makes no further write (test
`q3`, also with a new gate per item and with a `.notified` file appearing mid-loop); a pre-existing
marker that refuses one operation also ends the sequence (test `c3`). A plan that runs across
processes is held between processes by the markers below.

**Beyond the run.** The global marker `HALT`, the same file name `gate.py` uses, stops every
mechanism for every later process using the halt directory. `gate2` writes it for every failure
except one: a read-back mismatch for which every condition of rule 3 holds, decided mechanically
(`Gate2._containment_scope`):

1. the outcome is known: the request returned an expected status and, for a created object, its id
   (the decision is reached only past those checks);
2. read-back succeeded, with no unsent-field, label or state failure;
3. every rejected field difference is tail-confined (`transport_rules.tail_confined`); a
   classification that raised is not a rejected difference;
4. no other operation's marker is outstanding (any `HALT.<x>` file other than `.notified`
   companions), and no global marker.

Then, and only then, `HALT.<operation>` is written instead and blocks that operation alone. So an
unknown outcome (`TimeoutError`, test `q1`), a content change (`0.3` to `0.4`, test `q2`), a hard
break removed at the end of the content, a failed read-back, a pre-check refusal, a missing grant, a
push failure and an unknown operation are all global; a doubled, removed, altered or misplaced
footer, or text appended after the content, is operation-level (tests `q5`, `q6`, and every
negative control, whose expected scope is computed by an independent restatement of condition 3).

**Owner told before a later sequence writes.** While any `HALT.<operation>` lacks its companion
`HALT.<operation>.notified`, every later sequence refuses every write and push (test `c1b`). A person
creates the companion by hand once the evidence is kept and the owner has been told through a
channel other than an automated GitHub write; the gate never creates it. The operation stays
suspended until a recorded owner decision removes its marker.

Markers are checked first, before any request including a read; they are created with
`O_CREAT|O_EXCL` and fsync, never overwritten and never removed by the gate. Removal is by hand on a
recorded owner decision. Placing both gates' markers in one directory makes a `gate.py` halt stop
`gate2` as well.

**Known limits.** The check of a marker and the write that follows are not atomic across processes
(as in v1). Markers are local files: other hosts, containers and sessions are held only if they share
the halt directory, and otherwise by telling the owner. Within those limits, residual exposure under
operation-level containment is bounded to the tail-confined class: a shared layer that changes text
before the end of the content stops everything on its first such write.

**Relation to §A.49 rule 3 and §A.51 item 5.** `gate2` implements amended rule 3 (§8) and the
amended first sentences of §A.51 item 5: the package's operations stop on every failure the gate
treats as global, and continue in a later sequence only after an operation-level halt.

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
  `{"issue.edit_body": {"validated": False, "send_form": None}}` and a single-write grant for
  (`issue.edit_body`, 1548).
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

## 8. Proposed amended text of AGENTS.md §A.49 rules 2 and 3 and §A.51 item 5

Revision r2 of the amendment text on PR #1566, as it stands in the draft (rule 2, rule 3, §A.51
item 5). The adoption lines are dated and cite the owner's approval record at merge.

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
>    permitting transformation are kept as a record. A transformation enters, changes in or leaves
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
>    the error does not continue it. A sequence is the writes made by one run of a writer process or
>    of a plan. Every automated GitHub text write, for every agent and session, then stops as well,
>    unless every one of the following conditions holds, each decided mechanically from the write and
>    its read-back:
>    - the outcome of the write is known: the request completed with an expected status and, for a
>      created object, the response names its id;
>    - the read-back succeeded, and no field the write did not send, no label and no state differs
>      from what is expected;
>    - every rejected difference lies wholly in the trailing tail after the last character of the
>      sent content: the text sent, less the newlines and any attribution footer at its very end
>      (rule 2), is not empty and is stored unchanged as the start of the stored text;
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

§A.51 item 5:

> 5. **Stop.** An unknown outcome of a write, push or launch, a step outside the package's scope, a
>    failed preflight or push read-back (item 3), a failed check the package names as a stop, or
>    evidence that conflicts with the package's records stops the package's automated operations at
>    once. A §A.49 mismatch, a failed text read-back included, stops them in the same way, and every
>    automated text write as §A.49 rule 3 provides, unless that rule confines it to the failed
>    operation; then the sequence in which it occurred still ends at once and the failed operation is
>    suspended, and the package's other operations may continue in a later sequence through validated
>    mechanisms. The evidence is kept under §A.26 and the owner is told. Only a recorded owner
>    decision resumes a stopped package or a suspended operation.

## 9. Controls and results (mock transport only)

Run in this directory: `python3 -I -B test_gate2.py` and `python3 -I -B countercontrol2.py`.
Recorded outputs: `results-tests2.txt`, `results-countercontrol2.json`.

**`test_gate2.py`: 49 tests, all pass.** The unchanged v1 suite `test_gate.py` (18 tests) and v1
countercontrols pass in the same run (`results-tests2.txt`).

- Registry (`r1`–`r5`): closed frozen tuple with one rule; no footer formatting in `gate2.py`;
  malformed registries raise; a classification failure halts globally; two rules permitting the same
  difference are `rejected` and halt (tail-confined, so operation-level).
- Positive (`p1`–`p5`): as before: exact; footer appended; differing newlines before and after the
  footer; hard breaks and indentation kept alongside an appended footer; the footer quoted earlier in
  the content; the real #1558, #1062, #1245, #1556 and #1505 pairs permitted and #1565 and the #1548
  validations exact; records checked field by field; the five-body D1 replay accepted with four
  records.
- Negative (`test_neg_*`): the same cases as before, each rejected by `classify` and, through the
  gate: one write; a halt whose scope (global or operation) equals that of an independent
  restatement of rule 3's condition 3; sent, stored and diff kept, in files and in the marker, with
  matching digests; no record; the same gate and any other gate in the process refuse every
  mechanism; a later sequence refuses the operation; after an operation-level halt, a later sequence
  writes nothing until `.notified` exists and then writes another operation; after a global halt, a
  later sequence writes nothing through any mechanism even with every `.notified` present.
  `test_neg_content_changes_stop_globally` fixes the global scope for content changes in every
  footer variant.
- Containment (`c1`–`c6`): run-level latch after an operation-level halt, in the same gate and
  another gate of the process, also after notification, and a later sequence writing a comment, a
  label and a push but not the operation; notification required before a later sequence writes;
  global marker blocks all with zero transport calls and is not overwritten; an existing operation
  marker refuses its operation and ends the sequence; an unknown operation halts globally; a marker
  blocks a separate process; a second tail-confined halt with another operation's marker
  outstanding is global, with separate evidence files.
- Probes (`q1`–`q8`), from the review: `TimeoutError` on PATCH is global; `0.3` to `0.4` is global; a
  loop catching `Halted` makes zero further writes (gate reused or built per item; operation-level
  or global; `.notified` appearing mid-loop); no orphaned record when a later field fails (R8); rule
  3's conditions on a fixed table; an outstanding marker of another operation makes a tail-confined
  halt global; an internal exception during a write latches and is global; the marker embeds the
  texts when evidence files cannot be written.
- Ported `gate.py` guarantees (`g01`–`g17`): as before, with every failure global.

**`countercontrol2.py`: C1, C2 and C3 pass.**

- C1: `gate.py` halts on the real #1505 and #1558 pairs; `gate2` accepts each as
  `permitted footer-attribution-1` with one complete record. D1 replay: `gate.py` 1 write then a
  halt; `gate2` 5 writes and 4 records.
- C2, rule mutants; baseline 49 run, 0 failed: strip all whitespace: 5 tests fail; `.strip()` on
  the whole text: 5; ignore the footer text: 3; accept a doubled footer: 7; let spaces and tabs in
  the tail differ: 3; no two-newline separator check: 2. Each has negative controls among its
  failures.
- C3, gate mutants: accepting `rejected`: 20; skipping the discrepancy record: 1 (`p3`); a single
  global marker for every halt: 11; no run-level latch: 3 (`c1`, `c3`, `q3`); every halt confined to
  its operation (gate v2's containment before r2): 25, among them `q1`, `q2`, `q4`; narrowing without
  the tail condition: 13.

**Limits.** These controls show the gate's control flow and the rule's exact behaviour on stated
inputs, against a mock. They do not show the behaviour of the real GitHub path; §7 is the first
step for that. Test `c5` runs in a subprocess that imports unmutated modules, so in-process mutants
do not reach it.

## Files (new; the v1 files are unchanged)

| File | Content |
|---|---|
| `transport_rules.py` | Allowlist: `Rule`, `REGISTRY`, `classify`, send forms |
| `gate2.py` | Gate v2 prototype (imports `gate.py`) |
| `mock2.py` | Mock extensions (subclasses `mock.MockGitHub`) |
| `test_gate2.py` | Control suite (49 tests) |
| `countercontrol2.py` | C1–C3 |
| `results-tests2.txt`, `results-countercontrol2.json` | Recorded outputs |
| `PROTOCOL-v2.md` | This document |
| `CHANGES-r2.md` | Revision r2: each review finding and its change |
