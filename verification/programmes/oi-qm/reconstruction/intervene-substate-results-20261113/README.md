# Option-(c) carried results: preservation note

This note covers the twelve files listed below and no other file. Each is a byte-identical copy
from draft PR #1274 (branch `research/optc-1230-1232-20261113`, head
`fef9485712fe0b2c72416bfc900654ff64e7453d`), at the path it has there. They are preserved because a
record on `main` uses `NEW-RESULTS.md` as support (§A.42 items 2 and 8). Preservation establishes no
claim of these files (§A.46 item 1) and changes no scientific status.

Authority: owner decision of 2026-11-20 (`amaybaum`, #1169 comment 7030839727): "Narrow preservation
PR(s), not merges of the original drafts, for #1273, #1231 and #1232, plus #1274 where it is
needed." Accountable Issue: #1169.

## Files

| File | Blob at `fef94857` | SHA-256 | Bytes |
| --- | --- | --- | --- |
| `NEW-RESULTS.md` | `b0e930ab5792eb8173e74e3feb18b9262b651109` | `e26cef1cf8d99bdc39ffe3de3a6d663ed8c54af69de2afc98c935e839e4ba943` | 50066 |
| `CHANGES.md` | `220c189b0426316f8ce23c2a25e439a0d7d5714a` | `dcd0e1470b34f68195ffe50ef2f5610b4fdbba36154423c92ae963dd1dfb77b1` | 23763 |
| `DEPENDENCIES.md` | `6c127b0af1823f8f73614728755d79e05a64a65b` | `5213023f49a1b06ad71090b6cb4b2685c56e3e81edac531c82d4238ea16ca25a` | 15016 |
| `PROVENANCE.md` | `3277a372eb680c89c2594dae4ee196d93bb876a8` | `e6bb9b65d63991cca8f0a66531354f2668458a242d632039f73efef30baa78a4` | 8194 |
| `review/REVIEW-r1.md` | `67e455ecd42764afcc759fb0dd510fbe0bc6a4d1` | `63c0d35ac0b4427c931597462e798c910bfeada1518cce467e6e9bc57a72b18f` | 23695 |
| `review/RESPONSE-r1.md` | `7be0bbdc0cdee58e621d2ee29e3a715ef19f8bf1` | `31aa17185bb0ff44adc6bc3cd7ed06f43742b292e14c0b692bb66a50788e95dc` | 8596 |
| `review/CONFIRM-r2.md` | `223af48d9b9d728ecef4a4bab7fbe28b5e72c2e1` | `c15958b49d72c9b006df181dc6b914597e3efca471b00e2ebf9637aaecd61287` | 9753 |
| `review/NOTES-STATUS.md` | `e70ec088e7c5f839f9b795751e44f2b2e496a759` | `cec82a1029ddf3450460c25365031cc68e5a8c3de88366883e5290366b999dd1` | 13158 |
| `review/CONFIRM-CORR322.md` | `9375d5e6994d120018c5be50436015a0469c9d7f` | `fa3e09eb665b623a15466dac0946be99a707439789643102dadd29adb40d7f24` | 10244 |
| `review/RESPONSE-CORR322.md` | `248f32ef9712a3c50bd74ff8e549c7f0a4e430b6` | `238a70a72936b2689a0674359523dee986a8c253b143d1b1122c60bd3867893f` | 16512 |
| `review/DELTA-REVIEW-1274.md` | `82c6971dfa6227c98d10518d724717a0b71be4bd` | `a01bd419fd05a15be66de9ba9253af2e1fa8ebc133f9bc1c9b804f811df06ab2` | 21025 |
| `review/CONFIRM-DELTA-1274.md` | `e94049af6f8a12d461105462bf65ba22815019cb` | `ac5d6e7ea02eacdeff1782e36bd50f4bd6da0b22601effd83e6c9e39fff35508` | 6110 |

`git hash-object` on each file reproduces its blob.

## The citation on `main` that uses these files

`selection-discriminator-20261113/support/synthesis/SYNTHESIS-r3.md` (SR3), line 40 and §8 line 729,
cites `intervene-substate-results-20261113/NEW-RESULTS.md` at `d015131d`, blob `1859e8c5`, as support
off `main` for MM-3e (E2), the MM-3 §A.31 check (G1), MM-4b (L4), MM-6 (S7), MM-7 (N3), MM-8 (N4),
MM-9 (SLL), T1 and T6. SR3:730 cites `DEPENDENCIES.md` (blob `6c127b0a`) as provenance; that blob is
the one landed here.

The landed `NEW-RESULTS.md` is the head blob, not `1859e8c5`; one copy is landed, so `main` carries no
second version of the record. The two differ only in §3.1 (G1), by the forward corrections Δ30 and
Δ31 that `CHANGES.md` records (owner decisions #1274 comment 6865575359 and #1169 comment
6872005186). Lines 1–301 are identical. Lines 302–312 are the added scope paragraph. Lines 322–326
of `1859e8c5` are replaced by lines 333–340. Every other line n of `1859e8c5` is line n + 11 here
for 302 ≤ n ≤ 321 and line n + 14 for n ≥ 327. With that offset, every SR3 use outside G1, in
MM-3e, MM-4, MM-6, MM-7, MM-8, MM-9 and SR3 §6 (SR3's OC:64–67, :123–125, :333–392, :427–465,
:479–516, :532–535 and :584–595), resolves on `main` to unchanged text and is support on `main` at
this path.

SR3:267–269 uses G1 (OC:263–331) for the statement that "on non-spanning frames a nonnegative frame
matrix does not separate classical from non-classical transformations". The landed lines 302–312
and 333–340 restrict that non-separation to the octahedral and Husimi frames, and give a
non-spanning frame, the tetrahedral frame with an added point of probability zero, on which every
frame representative of the Hadamard has the entry −1/2, so the test separates there
(`review/NOTES-STATUS.md`; `review/DELTA-REVIEW-1274.md`). SR3:267–269 is therefore not support on
`main` as SR3 states it; its scoped form, that the E_f classical class is frame-relative without
spanning and that an E_f verdict must state whether its frame spans, is. SR3:634's use of
OC:323–326 (G1 relates to (SP) by analogy only) is lines 337–340 here. SR3 itself is not edited:
`selection-discriminator-20261113/ARTIFACTS.sha256` and `RETENTION.json` pin its bytes.

## Review and status

- `review/REVIEW-r1.md` (independent review at `1ef60d92`, ACCEPT WITH CHANGES), `review/RESPONSE-r1.md`
  and `review/CONFIRM-r2.md` (ACCEPT at `4b40dcdc`) cover the package as it stood at `d015131d`.
  ChatGPT review 5895564670 on #1274 (posted under `amaybaum`, 2026-11-13T17:44:35Z) at `d015131d`:
  "ACCEPT as a scoped research-evidence package, with separate integration gates."
- The correction of §3.1: `review/CONFIRM-CORR322.md` (REVISE at `040d929e`), `review/RESPONSE-CORR322.md`,
  `review/NOTES-STATUS.md` (the hand checks), `review/DELTA-REVIEW-1274.md` (non-author, ACCEPT WITH
  CHANGES at `bb80e420`) and `review/CONFIRM-DELTA-1274.md` (ACCEPT at `d1c25281`, where
  `NEW-RESULTS.md` and `CHANGES.md` take their landed blobs). ChatGPT review 5901837851 on #1274
  (posted under `amaybaum`, 2026-11-14T05:14:43Z) at `fef94857`: "ACCEPT as the complete bounded
  correction-delta package"; it replaces REVISE 5900794367 at `0b68c9e1` for that review's blocker.
- All reviews are model reviews: evidence of review, not independent mathematical verification.
  The carried results keep their support labels ([A], [X], [L]) and are paper-level research
  records, not established (§A.46 items 1 and 7).
- `DEPENDENCIES.md` traces every off-`main` reference of `NEW-RESULTS.md` against `main` at
  `c3b5f37a`. Rows A1 and A2 cite APPROX-UNIT1 r4a at `e41cf6137be165add39c7e557e97d3dddf110239`
  (#1221), which is an ancestor of `main` through the #1221 merge `ef62afb4`. The file on `main`,
  `verification/programmes/oi-qm/approximation/unit1/APPROX-UNIT1.md`, is r4b (blob `40f69592`,
  not r4a's `2cbaab43`); the two ranges the rows cite, r4a:471–483 (C1–C3) and r4a:365–375 (§4.2,
  NX-1 and the E_f classical class), are byte-identical there at lines 474–486 and 368–378. Rows A1
  and A2 are therefore support on `main` at those lines, with that difference stated. The content
  is a paper argument with exact generic checks, not kernel-checked, so `NEW-RESULTS.md` keeps
  (T5a), (T5b) and (T5d) as named hypotheses and its T5(c) conditional, as written. The gaps that
  remain are D2 (L3, for N2's necessity), D3 (L2 with class (a)3) and E2 (Bell-scope Theorem N);
  each is carried as a stated condition, and none is asserted as proved. Remediation stays with
  #1169 (D2, D3) and #868 (E2); this note authorizes no work.

## Not landed

`STATUS.md`, `review/CONFIRM-STATUS.md`, `review/CONFIRM-STATUS-r2.md` and `review/RESPONSE-STATUS.md`
remain on #1274's branch. No record on `main` uses them; this note gives the standing of the files
landed here. `STATUS.md` has a landing-basis section that review 5901837851 asks to be brought into
line with the adopted §A.46 at integration, and it is not copied without that change and its review.
References to these four files inside the landed review files are provenance. `CHANGES.md`:52
(row Δ30) cites `review/CONFIRM-STATUS.md` finding 1, with `review/NOTES-STATUS.md`, for the
non-spanning frame on which the test separates (the tetrahedral frame plus a point of probability
zero; Hadamard entry −1/2). That content is support on `main` through the landed
`review/NOTES-STATUS.md`:82–122, which checks finding 1 independently, and
`review/DELTA-REVIEW-1274.md`; `review/CONFIRM-STATUS.md` itself is provenance for where the finding
was first raised.
