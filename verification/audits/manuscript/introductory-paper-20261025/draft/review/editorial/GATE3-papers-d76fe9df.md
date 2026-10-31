## Gate 3 check: papers/Introduction.md at `d76fe9df` (r29)

**Verdict: ACCEPT.** Both edits read well, G1 is acceptable as it stands, and the layout is clean at 22 pages. One optional wording point remains (item 1).

Read-only: no edits, commits, pushes or comments, and the worktree used for the rebuild has been removed. Line numbers refer to `papers/Introduction.md` at `d76fe9df`.

### The two edits
- **#2 (L140):** the paragraph now ends "…belong to starts that never happen, as in the different-deck example [Main §2.3]." The rule-not-sample point is made once, in the opening sentence, and the back-reference to the example is kept. Clean.
- **#3 (L152):** the case-2 explanation now reads "The failure of chaining is a property of the world's rule, its dynamics with its hidden preparation, rather than of any accessible record: it constrains how such a world can be described, not what accessible data will show [Main §2.3, Scope]." It is accurate, says "accessible" where it should, and drops the restated result.
  1. *Optional:* "accessible record" now ends two consecutive sentences ("…neither appears in any accessible record. The failure of chaining … rather than of any accessible record: …"). One way to drop the echo: "The failure of chaining is a property of the world's rule, its dynamics with its hidden preparation: it constrains how such a world can be described, not what accessible data will show [Main §2.3, Scope]."

### G1 (L130)
I accept the reason for keeping it. Next to the merged contrast sentence it reads as the positive statement of what the contrast implies, and it adds the reason the contrast lacks: a difference could come from the setup rather than the dynamics.

2. *Optional:* if a tighter form is wanted that keeps it positive and stand-alone, this joins it to the contrast without restating the condition: "Only then is a forecast from a start a forecast of what the rule does; if the setup changed with the start, a difference between two forecasts could come from the setup rather than from the dynamics."

### Layout
- `sh ./build.sh Introduction` gives 22 pages; p22 holds 23 lines of references, down from 28 at r28.
- The `.tex` is identical to the committed file.
- A direct compile has 0 overfull boxes, 0 underfull boxes and 0 missing characters.
- Theorem 2 still breaks after (b), as accepted at r23.
- Page tops show no new widows. The (i)–(v) list, the italics and the displays are intact.
