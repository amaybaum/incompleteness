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

Prepared locally, with no GitHub write, network write or commit. `gate.py`, `mock.py`, `mock2.py`,
`transport_rules.py`, `test_gate.py` and `countercontrol.py` are unchanged; `gate.py` stays in use.

| Item | Change | Tests |
|---|---|---|
| Refusal | `gate2.lt_bang_violations(text, field)` returns one explanation when the text contains the two-character sequence: it names the field, every position (0-based character offset, 1-based line and column), says that GitHub has stored such text with the exclamation mark removed, that the text is not sent and not altered, and asks the writer to reword it. `Gate2._write` adds it to the existing pre-check of every text field the write would send (every body and title, of every operation: `comment.create`, `issue.edit_body`, `issue.create`, `pr.create`, `pr.edit`), after the field set is checked and before the pre-write read, so no request is made. The text is never changed; no substitution or escaping. | `lt1` (every body and title of every text operation: refused, reason names field and offset, zero writes, zero reads, zero git runs, the caller's dict and the evidence text unchanged); `lt2` (at the start, at the end, just before the footer, two in code spans, in a fenced block, two adjacent, in a title at start and end; line and column on a later line); `lt4` (refused before reaching a transport that removes the exclamation mark) |
| Positive control | Separated or look-alike characters are not refused: `< !`, `<` newline `!`, `!<`, `x<y!`, `&lt;!`, `<?xml`, `a < b!`, `<` with U+FF01, U+FF1C with `!`, `(?<=x)` with a separate `!`. | `lt3` (each sent once in title and body, stored exactly, no marker) |
| Latching | Handled as every other pre-check refusal in gate v2 (`_halt`): it latches the plan (`HALT-PLAN.<plan_id>` and the in-process store) and writes the global marker `HALT`; only a recorded owner decision clears them. | `lt5` (same gate, a new gate of the plan and a later sequence refuse the reworded text with zero requests; after the owner clears the markers by hand, the reworded text is sent and stored exactly) |
| Read-back | Unchanged. | C4 below |

**Choice on latching.** The refusal latches, as gate v2 treats every pre-check refusal (§A.49 rule 1
checks, the `oi-` form, send forms): a refusal is a failed pre-check, and §A.51 item 5 stops the
package's automated operations on a failed preflight. This does not conflict with the owner
decision: the text is still refused before any request, explained, and left for the writer to
reword, and the latch adds a stop, never a write. It differs from the comment poster, which refuses
this text without writing a halt marker; a uniform rule in gate v2 keeps one containment mechanism,
and the owner may choose the non-latching form instead.

**Countercontrol C4** (`countercontrol2.py`): with no refusal, 4 tests fail (`lt1`, `lt2`, `lt4`,
`lt5`); with titles not checked, 3 (`lt1`, `lt2`, `lt4`); with the text substituted and sent, 4
(`lt1`, `lt2`, `lt4`, `lt5`); the positive control `lt3` passes under each. Under the gate without
the refusal and a transport that removes the exclamation mark, each of the seven text fields is
written once and the exact read-back halts globally, with the stored text equal to the sent text
less the exclamation mark. The C3 latch mutants now also fail `lt1`, `lt2`, `lt4` and `lt5`
(no sequence latch: 10; memory-only latch: 7; every halt confined to its operation: 33); C1, C2 and
the other C3 entries are unchanged apart from the test count.

## Results

`test_gate2.py` 64 tests pass (the 59 earlier tests unchanged); `test_gate.py` 18 pass;
`countercontrol2.py` C1-C4 pass; `countercontrol.py` passes with output equal to
`results-countercontrol.json`. Recorded in `results-tests2.txt` and `results-countercontrol2.json`.
A focused independent check is required before the validation write.
