# Focused confirmation of Q-868-H unit 1 r3

**Model-written (Claude Code subagent, 2026-11-13). Not human verification (§A.46 item 7).** This is read-only: no
push, comment, edit or dispatch was made, and no probe was run. The reviewer is the author of the r2 review and not of
r3.

- **Head:** `research/q868h-868-20261113` at `c9d14e1135a23b73f61f62be33ffdca5b642fe67` (fetched by name). Its parent is
  `44f7c328`, whose parent is `82f592db`.
- **Files and hashes:**

  | file | sha256 | blob |
  | --- | --- | --- |
  | `Q868H-UNIT1.md` (r3) | `40e36e3c…6015` | `e4d91694` |
  | `DISPOSITIONS-r3.md` | `e29fb502…f5e9` | `7ccbdeb8` |
  | `r2/Q868H-UNIT1.md` | `1e128f28…79e6` (unchanged from r2) | `4d96a563` |
  | `review/REVIEW-Q868H-UNIT1-r2.md` | `651612e8…268e` | `144cc7db` |

- **Owner record read:** #868 c.6853568040 (`amaybaum`, 2026-11-13T12:55:08Z), with `gh api`.

## Verdict: CONFIRMED (ACCEPT)

RC1–RC5 are applied, and O1, O2, O3 and O7 are applied correctly. The r2→r3 diff contains nothing else. No new
overclaim was found. The nits below are optional and do not block.

## (1) RC1–RC5

| item | r3 text | status |
| --- | --- | --- |
| RC1 | §0 QC paragraph: my new text, verbatim, reflowed together with O2 | applied |
| RC2 | §0 "E-iso, WL, H-PREP and (iv) via P3"; §5.2 heading "…H-PREP, (iv) via P3; NNB for the Y read" | applied |
| RC3 | §0 "FAIL** (with NNB carried)"; §11 Q3 "with NNB carried (including under premise I)" | applied |
| RC4 | §0 "No native class-level witness exists … since each contains SWAP/2 (§7)"; §7 "No native class-level witness exists" | applied |
| RC5 | header: "The authorization says \"No computation\"", then the owner decision "r3; ratify the probes" with author, date and comment id, scoped to the two §10 probes, with "The same record authorizes no other computation" | applied, modified to reflect the owner's ratification |

For RC5:
- The #1210/#1211 citations are gone, and there is no owner question 4 (grep: zero hits for "question 4" and
  "Generic checks").
- The quoted words match c.6853568040, including "Not authorized: any other computation".
- Restricting the ratification to the two §10 probes is the narrower reading of "the unit's … probe scripts", and it
  is safe.

## (2) O1, O2, O3, O7

- **O1.** "−1/2 or −1/4 per branch, and at most −1/4 for mixtures" is correct. The Bell-basis minimum is `−(1 + v)/4`,
  and the two paths give `v = ±u`.
- **O2.** "as a product-test table only", plus "row sum `pp = 1` with certainty, where QM gives 0 (QC-4)" and
  "`τ_Y` takes their table to SWAP/2 (QC-3)", is correct for both Φ⁺-table preparations:
  - E3 has `pp = 1` at the coupling, and the coupling does not change `pp`;
  - E4 with `τ_Y` has `pp = 1`;
  - `τ_Y` sets `pp = 0`, which gives `⟨YY⟩ = +1`.
- **O3.** "carried here as a posit; the settings enter through P3's external controller" appears in §0 and §2.4. It
  matches AP1:421 and Main:406-407.
- **O7** (new hand argument, §6.0) holds. Every native read on A (raw parity-cell, ancilla, mediator, multi-record) is
  wing-local by E-iso and WL, so it leaves B's slots unchanged. B's first read therefore records `f_b^B(s)`, a function
  of B's slots of the pre-read configuration. The A-event is a function of `s` and A's meter, ancilla and mediator
  unknowns. The herald is therefore `E[1_α · (1, v_B(s))]`, a nonnegative combination of cube-vertex heralds,
  whatever correlation A's unknowns have with `s`. It uses no premise beyond (V)'s list, and mediators are local by
  WL. One wording point: "reweights the law of `s`" is exact only when the A-unknowns are marginalized, which is what
  the conclusion uses.

## (3) The r2→r3 diff is limited to the listed changes

`git diff --no-index r2/Q868H-UNIT1.md Q868H-UNIT1.md` shows these hunks and nothing else:
- the revision header;
- RC5;
- O3 at two sites;
- RC2 at two sites;
- RC1, O2 and O1 in the §0 QC paragraph;
- RC4 at two sites;
- O7;
- RC3 at two sites.

The reflowed lines of the §0 (V) and (C) paragraphs keep their wording unchanged apart from the O3 and RC2 insertions.

## (4) Byte identity of the committed review

`cmp` of `review/REVIEW-Q868H-UNIT1-r2.md` against my `REVIEW-r2.md` reports them identical (sha256 `651612e8…268e`).

## (5) OBJECTS.md additions

- **Accurate:**
  - the r2 row moved to `r2/` (blob and sha256 unchanged);
  - the new rows for r3, DISPOSITIONS-r3 and the review (every blob and sha256 recomputed and matching);
  - the owner-decision line, whose words match c.6853568040.
- **ASSESS gap:** ASSESS-868 r3a and REVIEW-868-r3 are now in `assess-868-r3a/` and match `d97c4b6b…` and
  `2a5014a5…`. OBJECTS correctly records the gap as closed on the branch and open on `main` until landing.

## (6) Overclaim check

- No verdict or scope is strengthened.
- QC FAIL now carries NNB, and (C) carries (iv).
- The native-witness negative is now stated at class level.
- The added text has no history, register, secret or local-path hits under SC-42. Its capitals are identifiers and
  status tokens only.
- Two SC-42 hits elsewhere in OBJECTS come from `44f7c328`, not from this commit: "earlier revisions" at :89 and
  "SOME FAIL" at :113, a quoted probe output. Neither is in the unit text.

## Optional nits (non-blocking)

- **a.** The RC5 header puts the owner's sentence in quotes ending at "as covered." The original continues ", and r3
  records that decision." Either drop the period inside the quote or quote the whole sentence. Adding the time,
  12:55:08Z, would also meet §A.42 item 7.
- **b.** DISPOSITIONS-r3 is inaccurate in three places:
  - it names `r2-r3.diff`, which is not committed;
  - it names the review as `REVIEW-r2.md`, which is committed as `review/REVIEW-Q868H-UNIT1-r2.md`;
  - it says `OBJECTS.md` was "not touched", but the same commit changes it.
- **c.** The OBJECTS r3 row says "applies RC1–RC5"; it also applies O1, O2, O3 and O7.
- **d.** r3 still cites ASSESS as `reassess/868/ASSESS-868.md`. It could also name `assess-868-r3a/ASSESS-868.md`, which
  is now on the branch.
- **e.** O4 (an unpreserved second run of the r2 probe) is left open, as DISPOSITIONS-r3 records.
