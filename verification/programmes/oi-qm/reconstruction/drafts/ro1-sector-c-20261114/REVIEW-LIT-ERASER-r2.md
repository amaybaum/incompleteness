# REVIEW of LIT-ERASER-r2 (focused confirmation)

**Object.** `LIT-ERASER-r2.md` and `RESPONSE-LIT-ERASER-r1.md` at PR #1294 head
`bd8fc19d5a145d671d461b1c1cbbdf7e7accd93d`, compared with r1 at `e18126ee` and with
`REVIEW-LIT-ERASER-r1.md`.
**Authorization.** Issue #1169 comment 6891511297, item (2a). This review was read-only.
**Reviewer.** Claude (independent of the writer). **Date.** 2026-11-15.

## Verdict: ACCEPT WITH CHANGES

All eight r1 findings are resolved. One required change remains: the text added to C2 for finding 7
contradicts the note's own read status for Dürr 1998 (finding A). That text repeats an imprecision
that was already in r1's C5(a), which my r1 review missed. The fix is one phrase at each of two
sites. Once it is made, the note is ready for owner acceptance and needs no further review round.

## 1. Resolution of the r1 findings

| r1 # | Status in r2 |
|---|---|
| 1 | **Resolved.** §3 now says: equality for a pure marker; for mixed markers the inequality holds, in general strictly, and equality is still possible (the `(1, 1)` example, labelled as such). The `2 Tr(ρ²) − 1` curve is limited to Schwindt's half-wave-plate coupling. The change of "inside it" to "inside or on it" is correct |
| 2 | **Resolved.** C6 states that U4's whole-complement states are pure, so equality holds at every tick of U4's model. The mixed example is placed outside that model, and the note no longer suggests that QM-4 is wrong within it. PARTLY now rests on two grounds: (a) U4 cites the inequality where its argument needs the equality; (b) "exclude each other" has two readings. §3 is updated to match |
| 3 | **Resolved.** The source's continuation is quoted ("to gather information that has leaked from the system", which matches arXiv:1911.06282), and the operations-on-environment point is labelled the writer's inference |
| 4 | **Resolved.** C1, C2 and C4 are reworded; the verdicts are unchanged |
| 5 | **Resolved.** C10 is now self-contained. The page range 480–485 for *Nature Phys.* 8 is correct |
| 6 | **Resolved.** "arXiv carries v1 only" is added. The 7.7 ns figure is attributed to my report and marked NOT READ. Its status stays unresolved, which is correct |
| 7 | **Resolved in scope, with one wording defect.** The statement is now limited to Kim, Walborn and Ma. But the added sentence says Dürr's patterns were "taken with the marker unread"; see finding A |
| 8 | **Resolved.** Eichmann et al., *PRL* 70, 2359 (1993) is listed NOT READ; the citation is correct. Brune 1996 is listed NOT READ. Bertet et al., *Nature* 411, 166 (2001), doi:10.1038/35075517, is listed as abstract only. The note's summary of that abstract (a small cavity field acting as a beam splitter; visibility rising with mean photon number) agrees with my understanding of the paper. I could not open nature.com to confirm the abstract text, so I have not verified it at source. The C8 verdict is unchanged, which is correct |

## 2. The new C6 claim

The claim is correct. At `D = V = 1/√2`, `D² + V² = 1/2 + 1/2 = 1`, which is on the equality
boundary. So partial distinguishability and partial visibility coexist even in the pure case, and
"exclude each other" read as a statement about states is false.

Read as a statement about processes, it is true under equality. On `D² + V² = 1` with
`D, V ≥ 0`, any increase in one quantity forces a decrease in the other, so the two cannot both
increase.

The C6 wording draws exactly this distinction and no more. It is consistent with §3's "trade off"
wording, `V ≤ √(1 − D²)`.

## 3. Nothing else changed

- **Line diff r1 → r2:** the only changes are the title, the review line in the header, and the
  sites listed in the response table (§1.6, C1, C2, C3, C4, C6, C8, C10, and §3 in three places).
  I found no other change.
- **Other files:** r1 is unchanged. `REVIEW-LIT-ERASER-r1.md` on the branch is byte-identical to the
  review I wrote.
- **README:** the SHA-256 digests listed for `LIT-ERASER-r2.md` (`224c3d5b…`), `LIT-ERASER-r1.md`
  (`4d943f7b…`) and `REVIEW-LIT-ERASER-r1.md` (`afffc5be…`) match the files at `bd8fc19d`.
- **The response's "not changed" statement** (the Glan/Glen spelling, and the Dürr and SEW abstracts
  read at nature.com for r1) is accurate as a record. I still could not open nature.com, so those
  two abstracts remain unchecked by me.

## Finding A (required)

**The note states that Dürr 1998's patterns were taken with the marker unread, but its own record
says this was NOT READ.**

- C2 (new text) says: "Schwindt 1999's `V` and Dürr 1998's atom patterns are unconditional data
  taken with the marker unread, in non-delayed arrangements (C1, C5(a))".
- C1 and row 1.11 record: "for Dürr 1998, whether the marker was read in the fringe-free runs was
  NOT READ". Dürr's numbers are SECONDARY.
- C5(a) already listed Dürr under "`V` near zero measured with the marker unread", and that text
  was carried over from r1.

So for Dürr the note asserts a condition it records as unread.

**Fix:** in C2 and C5(a), qualify Dürr as "unconditional patterns (SECONDARY); whether the marker
was read NOT READ". Alternatively, keep only Schwindt (and Walborn Fig. 3 at coincidence level) as
the marker-unread cases.

## Ready for owner acceptance?

**Not yet; it will be after finding A is fixed.** That fix is a two-site wording correction that
brings the text into line with the note's own read-status record, and no further independent round
is needed for it. Everything else checked in r1 still holds in r2.

## Not checked

- The Bertet 2001, Dürr 1998 (*Nature*) and SEW 1991 abstracts at source (nature.com was
  unreachable).
- Any published journal version.
