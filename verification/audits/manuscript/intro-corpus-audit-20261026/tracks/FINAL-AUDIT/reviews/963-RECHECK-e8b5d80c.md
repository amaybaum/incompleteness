## SC-17 re-review at `e8b5d80c`

**Verdict: REVISE, for one phrase at :974.** `git ls-remote` shows the head is `e8b5d80ce2ca58d57727a21898e9ad6a5fc56ea1`, one commit on `183c1a74`. It touches only the Explainer `.md`/`.tex`/`.pdf` and the README.

### (a) The three items
- **:771 is closed.** It now says "conditional on H-slope with the horizon and frame conditions" and "fixed by the same thermal matching, under the same conditions, whatever σ is [GR §5]". Both match GR's abstract (:12, :24, :28) and GR §5.
- **:773 is closed.** The new text reads: "…come from different arguments applied to the same dynamics without modification, and each of the seven checks could have failed. They are consistency checks, with one free geometric parameter (ε) and σ undetermined, not proof." It matches GR §4 and is in neutral register. "Without modification" is accurate: the same rule feeds both sides.
- **:974 is closed in substance.** The framing in which observed GR selects the dynamics is gone, and the conditions are named as inputs of the lemma. One phrase remains; see (b).

### (b) "not consequences of observed QM or GR" at :974
It passes §A.32, but it is a no-go stated more strongly than SM §4.1 supports, the same defect as R2 earlier:
- SM shows these conditions are assumed, not that they cannot follow from observation.
- The nearest-neighbour range is "an assumption beyond bounded coupling degree".
- Whether centre independence descends to a zero observer-level self-weight is "open".
- Linearity rests on the observer-level amplitude-scale-gauge premise.

So SM supports "not derived", not "not consequences".

**Exact replacement at :974.**
- Current: "these conditions are inputs of the lemma, not consequences of observed QM or GR [SM §4.1]"
- Replace with: "these conditions are inputs of the lemma and are not derived from observed QM or GR [SM §4.1]"

### (c) The gap equation and the 1/4 in other SC-17-edited lines
I checked every line SC-17 has edited.
- **:974, "If ℏ has the specific value c³ε²/(4Gσ), the gap equation pins ε = 2√σ l_p".** This is fine. Given the stated premise, it is the algebraic inversion that GR §4 calls "algebraically equivalent", so no H-slope condition is needed.
- **:769, item "(3) the gap equation for ℏ".** It appears in the list of checks with no conditions. It names a check rather than stating a value, and the conditions appear at :477 and two lines below at :771. **Optional:** append "(conditional on H-slope with the horizon and frame conditions)".
- **No other edited line states the 1/4 or the gap equation.**

### (d) Stamps, regeneration and the scan
- **Stamp.** The `source-sha256` in `Explainer.tex` (`31b36bee…`) equals the hash of `Explainer.md`.
- **Regeneration.** I re-ran pandoc, and the output is byte-identical to the committed `.tex`.
- **PDF.** It has 71 pages and contains the new :974 text.
- **Added-lines scan.** It is clean: no self-assessment, reader-instruction or history phrases and no caps emphasis.
- **Release gate.** Every step passes except lean-axioms, which fails locally as expected.
- **Worktree.** My temporary worktree is removed; no gc or prune was run.

Once the :974 phrase is replaced and the Explainer regenerated, I would ACCEPT.
