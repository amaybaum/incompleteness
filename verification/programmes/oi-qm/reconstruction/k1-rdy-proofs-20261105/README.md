# K1-RDY lemma proofs (#1031, option 1b)

**Status: written proofs, not independently reviewed. WIP / UNVERIFIED.** This directory decides no gate, token,
readiness result or owner question, and changes no statement of the K1-RDY text. It authorizes nothing.

## Purpose

The K1-RDY preregistration accepted on 2026-11-02 (313 lines, recorded sha256 `a93f3f33f0c5a6e8…`) uses four results
whose earlier arguments are held only in Issue comments, off `main`. The owner's ruling #1031 comment 6651204512
(amaybaum, 2026-11-05T06:15:48Z, "Off-`main` proofs: Option 1b") asks for self-contained paper proofs of them, an
independent review, and landing on `main` through a separately approved, narrowly scoped pull request before the new
round's base `D`. `LEMMAS.md` holds the proofs:

| Result | Statement in the text | Outcome in `LEMMAS.md` |
|---|---|---|
| P1 invariant-measure lemma | named at lines 244–245; content at lines 72–76; no accepted statement | statement assembled from its uses (§1.1), proved (§1.2) |
| Blindness lemma | lines 97–100 | proved as stated (§2) |
| L-O(i) | lines 102–106 | proved as stated (§3) |
| L-O(ii) | lines 102–103, 107–110 | proved as stated (§4) |

No counterexample or gap was found, and no correction is proposed. `LEMMAS.md` §5 lists the points the reviewer should
check: the assembled P1 statement, three marked readings, and the uses that lie outside the four results.

## Sources

- The text: body lines 5–317 of #1031 comment 6567522034, held byte for byte as `PREREG-RECOVERED.md` on PR #1114's
  branch at `e18b36e3`. "Line N" in `LEMMAS.md` refers to it. The statements proved are quoted from it verbatim, so the
  proofs are readable without it. It is not copied here.
- Earlier arguments, provenance only: proposal K1-RDY r3 (#914 comment 6564008455) and its review (#914 comment
  6564018307); the text's review (#1031 comment 6567537517); the draft proofs in #1114 comment 6650931698, §3.
  `LEMMAS.md` §0.1 gives the line ranges and recorded digest prefixes.

## Limits

- Hand derivations only. No enumeration, model computation, Lean run or workflow dispatch was used; enumeration before
  `F` is not authorized (#1031 comment 6651204512).
- Until an independent review of these proofs is recorded on `main`, no result here is established (`AGENTS.md`
  §A.46 items 1 and 7), and K1-RDY's uses of the four results remain dependent on that review.
- The line locators point to a text that is not on `main`. They resolve once lines 1–313 of the text are on `main`.
- Not covered: §5.3's class rule (Q4), the cycle decomposition of `φ` at the instance, P3's explicit image (line 89),
  TA (c4), and the gates that precede G4.
