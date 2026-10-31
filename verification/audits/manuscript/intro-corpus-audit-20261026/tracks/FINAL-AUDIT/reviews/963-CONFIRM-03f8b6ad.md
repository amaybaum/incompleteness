## SC-17 delta confirmation at `03f8b6ad`

**Verdict: ACCEPT.** `git ls-remote` shows the head is `03f8b6ad9de5e55bd503a99f7a2621567c2d4489`, one commit on `e8b5d80c`. It changes only the Explainer `.md`/`.tex`/`.pdf` and the README row.

**What changed** (I read the diff from `183c1a74`, through `e8b5d80c`, to `03f8b6ad`):
- **:974** now has my exact replacement: "…these conditions are inputs of the lemma and are not derived from observed QM or GR [SM §4.1]". That matches the scope of SM §4.1, where the nearest-neighbour range is assumed, centre-independence descent is open, and linearity rests on an observer-level premise.
- **:769** now reads "(3) the gap equation for ℏ (conditional on H-slope with the horizon and frame conditions)". The wording matches :771 and GR's statement of those conditions, and the punctuation of the list is intact.
- **:771 and :773** are unchanged since I confirmed them at `e8b5d80c`.

**Stamp and regeneration.**
- The `source-sha256` in `Explainer.tex` (`7344ff76…`) equals the hash of `Explainer.md`.
- I re-ran pandoc, and the output is byte-identical to the committed `.tex`.
- The PDF has 71 pages and contains both new phrases.

**Scan.** I ran it over every Markdown line SC-17 added (`0d917665..03f8b6ad`) and it is clean. There are no self-assessment, reader-instruction or history phrases. There is no caps emphasis. None of the retired phrases remains, including "not consequences", "no single condition", "selected by the QM" and "information-screening".

**Gate.** The release gate passes every step except lean-axioms, which fails locally as expected.

My temporary worktree is removed; no gc or prune was run.
