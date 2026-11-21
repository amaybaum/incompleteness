# Amendment A2 to the comparison preregistration: integration of `43122ff6`

**Status.** WIP / UNVERIFIED, written before any after-state exists. It records how two concurrent
revisions of this record were joined. One is `33b68ff0` and `09673477`, which revise `PREREG.md` in
place in answer to both review rounds (c.7059099956, c.7059220314). The other is `43122ff6`, which
answers round 1 by amendment A1 (`amendments/A1-replay.md`, blob `505d0329`), a compiled list
`edits/S2.json` (blob `3d242ed2`) and its own `verdict.py` (blob `ef9b7970`). The two were joined by the
merge commit `1bb6c2cc`, under the owner's writer designation (#1169 c.7059632884, c.7059633249).
`1bb6c2cc` records ancestry only: its tree equals `09673477`'s, so it adopts nothing itself. What is
adopted enters in the commits after it, as stated row by row below. `43122ff6` was reviewed in
#1483 c.7059580868 (ACCEPT-WITH-NITS for preparation); that review's findings are dispositioned in the
second table.

**Rule.** Where `43122ff6` and the revised `PREREG.md` differ, the more complete fix for each finding
is kept, and each superseded item is named below. `PREREG.md` as revised, with this amendment,
governs. A1 and `edits/S2.json` are removed from the tree and remain in its history at `43122ff6`.
Nothing of them is adopted silently.

| `43122ff6` item | Disposition | Reason |
|---|---|---|
| Replayed state R: every compiled edit applied to the pin, and H compared with R line by line; no hand citation can make J | **kept as a J precondition** (PREREG §3, completeness), with per-item citations | A J needs its region replayed from the cited edits to equal the same region of R, with every landed edit that touches the region cited. Without this, a reviewed change that H reverts on a line keeping another reviewed change was J (review c.7059976436, finding 2); it is now U (T21b). Citations are kept so that a J names its edits, J9 can check the row a cited edit lists, and C7 and C8 can perturb a cited item |
| Replay-missing items: a reviewed change absent from H is U | **adopted**, PREREG §3 and T21 | The comparison with the baseline cannot see a reviewed change that H lacks or reverts, because its line then equals the baseline. The landed edits are those of every unit whose merge is an ancestor of H, plus DEL |
| `replace`, with old strings matched with whitespace runs as `\s+` | **superseded** by exact strings | The exact strings replay every unit to its merge byte for byte (C6 (c)), so no tolerance is needed, and an exact match admits fewer accidental matches |
| `replace-each` for multi-site records (S2-C A1-1) | **superseded** by composition into each parent edit, checked against the 15 sites the record states | A composed edit replays at each site in one step, and the site count is a compile-time check |
| `resolve`: a resolved catch-up line applied to the line of similarity ≥ 0.5 | **superseded** by `S2-C:C4-resolved`, with the exact old line of the merge's first parent and the resolved line of RESULT §9.1 | A similarity threshold could pick the wrong line. Of the three lines §9.1 quotes, only M:224 was resolved by hand (RESULT §9); M:736 and Sub:92 replay from their splices |
| `edits/S2.json`, 168 edits, amendments as separate entries, replay not run | **superseded** by `inputs/edits-s2.json`, 139 composed edits | Its replay against the merges was not run. The 139-edit list reproduces each unit's merge byte for byte (C6 (c)); the count differs because amendments are composed into their parent edits and two of S2-C's three resolved lines are not edits (they replay from their splices) |
| FULL scope: a chapter edit applies to FULL only inside that chapter's FULL span | **superseded** by explicit `files` | An edit applies to FULL only when its record names the FULL mirror (`mirror`, `full_mirror`, a FULL site, or a `-FULL` entry), which is at least as narrow, and C6 (c) shows the result is the merge |
| J9 table (F: "finite" count kept, no open term lost; O: carries an open term; J: loses none) | **kept, with the revised J9** | The same conditions, plus the row must be the entry's own and listed on a covering edit, and no J10 term gained |
| Relocation out of Main is R | **kept** | Unchanged in both |
| R resolution: a URL on any PR or Issue, `reviewer` ≠ `author` | **superseded** by a URL on the result PR, `reviewer` ≠ `classify.json`'s `classifier`, and `proof` for a J10 item | Narrower, and it carries the owner's requirement that a generality claim clear only with a proof |
| `check-edits` recompiles each unit from its allowlist at a pinned commit; DEL at H | **kept, extended** as C6 (a)–(d) | Adds the structural checks, the replay against the merges, and, for DEL, the deletion commit as ancestor of H and its replay from its first parent |
| C6-DEL fails at the pin, so the pin self-run is VOID | **superseded**: (d) is not applicable only when H is the pin, and fails at every other head without a deletion list | The pin self-run tests the tools. At any real H the deletion list is required |
| C7 by appending " [perturbed]" | **superseded** by changing a number token outside the cited new strings (or appending " 0"), as round 2 proposed | Tests the value path the comparison is for |
| Fresh output: `--out` absent or empty, `out_was_fresh` recorded and required | **kept** as the refusal of a non-empty `DIR` | Same guarantee; a refused run writes nothing |
| `verdict.json` records the input digests | **kept** | Also the frozen digests |
| Ledger `rows.json` at `7f28886f`, by digest, read from Git objects; a reconciled ledger only by a further amendment | **kept** | Identical |
| Widened flag | **kept, extended** | Also J10 hits; no category exempt |
| Self-test cases G1–G7, S1/S1b, M1, Markdown parsers on fixed samples | G1–G7 **kept** (T12); M1 **adopted** (T21); S1/S1b **superseded** with the FULL-span rule; parser samples **superseded** by C6 (a) and (c) on the real records | Parsing is checked on the records it will read, against their merges |
| Commands `compile --units`, `check-edits --edits --units --commit` | **superseded** by `compile-s2`, `compile-del --commit` and `check-edits` | No edit list is passed by hand |

**Review of `43122ff6` (c.7059580868).**

| Finding | Disposition | Where |
|---|---|---|
| 1. Run the S2 replay against `7f28886f` before the deletion | **adopted in substance** | C6 (c) replays the five units from the pin through each merge, `7f28886f` the last, and reproduces every manuscript file byte for byte. No comparison against a Step-2 head is run |
| 2. `resolve` is loose | **superseded** | `resolve` is not used; `S2-C:C4-resolved` is exact (table above) |
| 3. `verdict` classifies over VOID controls | **adopted** | With any control failed, `verdict` classifies nothing and writes VOID with no item classes. The labelled preparation mode (`collect --prep`, allowed only at the pin) gives the pin self-run without a pinned commit |
| 4. Record the deletion list's digest at the designated head | **adopted** | `controls.json` records the SHA-256 of the landed `edits.json` blob; `verdict` checks it in C6 (d) |

With the completeness precondition, each check of `43122ff6` that bears on a finding is kept, or is
replaced by one at least as strict on the same case.
