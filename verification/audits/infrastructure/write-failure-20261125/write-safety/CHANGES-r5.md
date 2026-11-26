# Revision r5 of gate v2: pre-write refusal of a less-than sign followed by an exclamation mark

On 2026-11-25 GitHub stored comment 7172299731 with one character removed: the exclamation mark of
a less-than sign immediately followed by an exclamation mark, inside a code span (evidence:
`comment-7172299731/` on the evidence branch). Owner decisions (amaybaum, 2026-11-25T19:31:10Z),
verbatim: "Reject any intended text containing the problematic sequence before sending a write
request." "Return a clear explanation of why the text was rejected." "Require explicit rewording by
the writer rather than automatic substitution." "Add positive and negative controls and obtain a
focused independent review." "Do not weaken the exact read-back requirement." And
(amaybaum, 2026-11-25T20:29:25Z, #1169 comment 7173759648): "Add the same pre-write refusal to gate
v2 before its validation write. Require targeted tests, countercontrols and a focused independent
check."

r5 was prepared locally, with no GitHub write or network write, and committed on the evidence
branch at `0a1b5675af31d1885a5e108d6b143bea74ea4aa1`. Its non-stopping revision, below, was
prepared locally in the same way and committed at `456bdb25e7ea85aeaae6721207e38684df3f8413`.
`gate.py`, `mock.py`, `mock2.py`,
`transport_rules.py`, `test_gate.py` and `countercontrol.py` are unchanged; `gate.py` stays in use.

## Non-stopping revision

Owner decision (amaybaum, 2026-11-25), verbatim: "I authorize the non-stopping refusal for this
specific pre-check, provided the reviewer confirms compatibility with §A.51. Include a
countercontrol demonstrating that no prohibited request is sent and that subsequent valid
operations remain possible. Do not change the behavior of other pre-checks or containment rules."

As committed at `0a1b5675`, the refusal latched like every other pre-check refusal (plan latch and
global marker). It now refuses the operation without stopping the sequence, as the comment poster
does: the poster and gate v2 behave alike for this refusal. The authorization is conditional on the
reviewer confirming compatibility with AGENTS.md §A.51 (item 5 stops a package on a failed
preflight); that confirmation is outstanding.

| Item | Change | Tests |
|---|---|---|
| Refusal | `gate2.lt_bang_violations(text, field)` returns one explanation when the text contains the two-character sequence: it names the field, every position (0-based character offset, 1-based line and column), says that GitHub has stored such text with the exclamation mark removed, that the text is not sent and not altered, and asks the writer to reword it. It covers every text field the write would send (every body and title, of every operation: `comment.create`, `issue.edit_body`, `issue.create`, `pr.create`, `pr.edit`). The text is never changed; no substitution or escaping. | `lt1` (every body and title of every text operation: refused, reason names field and offset, zero writes, reads and git runs, the caller's dict unchanged); `lt2` (at the start, at the end, just before the footer, two in code spans, in a fenced block, two adjacent, in a title at start and end; line and column on a later line); `lt4` (refused before reaching a transport that removes the exclamation mark) |
| Non-stopping outcome | `Gate2._write` checks the sequence in a second loop, after every other pre-check of every field has passed and before the pre-write read. On a hit, `Gate2._refuse` logs `("refused", op, target, field)` and raises `gate2.Refused` (attributes `op`, `target`, `field`, `reason`; not a subclass of `Halted`), and `_guarded` re-raises it untouched. No `_halt`, no `HALT`, no `HALT-PLAN.<plan_id>`, no in-process latch, no evidence file. | `lt1` (the same gate then sends a valid text exactly); `lt5` (after a refusal the same gate, a new gate of the same plan and a later sequence each send the reworded text once, read back exactly; zero requests for each refused attempt; only the plan record in the halt store) |
| Other pre-checks unchanged | Every other pre-check still halts as before and takes precedence: a text that fails another pre-check and also contains the sequence halts on the other check. | `lt6` (a refused text followed by a carriage-return failure halts globally, latches the plan and stops every mechanism; texts with a carriage return, a zero-width character or the `oi-` form plus the sequence halt) |
| Grant | A single-write grant taken by the refused attempt is given back, since nothing was sent; the reworded text is then the grant's one write. The owner accepted this rule (amaybaum, 2026-11-26T03:43:11Z, #1169 comment 7181966825): "A refusal before transmission must not consume the grant. Refused input: no request sent, grant remains available. Valid input: grant consumed when the write is attempted. Unexpected write discrepancy or uncertain transmission: grant remains consumed, and containment rules apply." | `lt7` (refused, reworded write succeeds, a further write halts as before) |
| Positive control | Separated or look-alike characters are not refused: `< !`, `<` newline `!`, `!<`, `x<y!`, `&lt;!`, `<?xml`, `a < b!`, `<` with U+FF01, U+FF1C with `!`, `(?<=x)` with a separate `!`. | `lt3` (each sent once in title and body, stored exactly, no marker) |
| Read-back | Unchanged. | C4 below |

`gate.main` (the CLI shape re-exported by `gate2`) maps only `Halted` to its exit code; a
`Refused` propagates to the caller as an exception.

**Countercontrol C4** (`countercontrol2.py`). Mutants, each failing the suite with its named tests
among the failures, the positive control `lt3` passing under each: no refusal, 6 failures (`lt1`,
`lt2`, `lt4`, `lt5` required); titles not checked, 3 (`lt1`, `lt2`, `lt4`); the text substituted
and sent, 6 (`lt1`, `lt2`, `lt4`, `lt5` required); the refusal latching as committed at `0a1b5675`,
6 (`lt1`, `lt5`, `lt7` required). With the gate as it is, for each of the seven text fields, a
refused text makes no request (no write, no read, no sent text containing the sequence) and leaves
only the plan record, and a valid write then succeeds exactly on the same gate and on a new gate of
the same plan. Under the gate without the refusal and a transport that removes the exclamation
mark, each field is written once and the exact read-back halts globally, the stored text equal to
the sent text less the exclamation mark. C1, C2 and C3 are unchanged apart from the test count and
the C3 latch counts (no sequence latch 7, memory-only latch 4, every halt confined to its operation
31), each required test still among the failures.

## Known limits (left as they are)

- Label names: sent in the `labels.add` payload and the `labels.remove` path, they get neither this
  refusal nor `precheck_text`, and `labels.add` can create a label; the exact label read-back is
  the backstop.
- Control characters other than format characters (category Cc, for example NUL) between the two
  characters pass both pre-checks; the exact read-back is the backstop.
- Grant ordering: the checks are not reordered; the sequence is checked after the single-write
  grant is taken, and a refusal gives the grant back (`lt7`).

## Results

`test_gate2.py` 66 tests pass (the 59 earlier tests unchanged); `test_gate.py` 18 pass;
`countercontrol2.py` C1-C4 pass; `countercontrol.py` passes with output equal to
`results-countercontrol.json`. Recorded in `results-tests2.txt` and `results-countercontrol2.json`.
The reviewer's confirmation of compatibility with §A.51 is required before the validation write.
