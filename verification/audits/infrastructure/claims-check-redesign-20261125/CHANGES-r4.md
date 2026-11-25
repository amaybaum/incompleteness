# Changes in revision r4 (Issue #1565, PR #1567)

This note maps the r3 independent review (PR #1567 comment 7170477503, verdict REVISE) and the
owner's decision (`amaybaum`, 2026-11-25T18:50:53Z; #1169 comment 7171541574) to `DESIGN-r4.md`
and `work/proto.r4.py`. Every earlier file in this directory is unchanged, byte for byte.

## Plain statement

- The checker flags defined patterns and enforces the structure of review records. Independent
  scientific review is responsible for detecting reworded claims outside those patterns.
- The record holes of review findings 2 and 3 are closed for the review's probes. Each of the
  review's four record probes that gave exit 0 under r3 gives exit 3 under r4: the three on
  H-slope sentences through correction 1, the `W-KDEG` probe through correction 3.
- Correction 2 checks evidence that the record writer chooses, and a wider span can meet it. On
  sentences without a hypothesis token, misleading-qualifier records remain the reviewer's judgment
  (`DESIGN-r4.md` §5).
- No vocabulary was added. The word lists now follow `DESIGN-r3.md` §3.2: inflections match, and
  bare generic heads are removed or replaced by the rule's own multi-word phrase.
- Silent PASS does not increase on any batch. All 195 preserved controls are unchanged (0 MISS,
  0 FPFAIL). Batch W, per rule: 17 → 16 of 30. Batch W, any rule firing: 16 → 15.
- Review load at main `4c3ad079`: 256 → 234 active findings. 36 of them contain a hypothesis
  token, and with the licence list empty they can be resolved only by rewording or an adopted
  licence.
- Batch W is not held out for r4. One focused independent review is required before adoption.

## Review findings

| Finding | Disposition | Where |
|---|---|---|
| 1 Criterion 6 fails at first run (paraphrase class) | Not repaired, as the owner directs. The argument-only widening and the `isotropic`/`quadratic`/`metric` additions add vocabulary and are not adopted. The class is stated as the responsibility of independent scientific review. W-P-09 is caught by the inflection fix of finding 4, not by new vocabulary. | `DESIGN-r4.md` §0, §1, §3 |
| 2 `unrelated` records clear H-qualified claims | Corrected. (a) An `unrelated` record is refused when the sentence contains `H-…`. (b) `mention`, `supposition` and `question` evidence must contain the rule's own match (code C: arguments and cues; code A: cues, the present arguments and the anaphor; code P: the strong cue). The three probes give exit 3 because correction 1 refuses them. Correction 2 checks evidence the writer chooses and can be met by a wider span; misleading-qualifier records on sentences without a hypothesis token remain reviewer judgment. | §1 items 1–2, §5; `results-r4/exitcodes.txt` |
| 3 Duplicate `W-KDEG` id | Corrected. The second rule is renamed `W-KDEG-ANSWER` (family `W-KDEG`, the same templates). `W-KDEG` keeps its meaning. Record checks use the rule that raised the finding. Rule ids are asserted unique. The probe gives exit 3. | §1 item 3 |
| 4 Lexicon breaks its own criterion | Corrected, adding no term. Inflections: `couplings`, `horizons`, plural forms of `thermal ratio/spectrum/character`, of the `quantum …` heads, and of `quadratic symbol`, `propagation geometry` and `projected memory`; `single values`, `conditions for`, `led to`. Bare heads: `symmetr…` and `substratum` replaced by `substratum symmetry`; bare `horizon` removed from `W-GR-THERM-KIN`. | §1 item 4 |
| 5 M1 cannot fail; injection mostly re-tests sentence-local controls | M1 is dropped from criterion 2. M2 is restated as a segmentation check. Injection is restated as a check on segmentation and the anaphora window, not as independent evidence. | §2 |
| 6 Narrowing criterion stated after measurement | Stated: the r3 dial was chosen after measurement. r4's edits applied the criterion before r4's first run, which cannot be checked from the files. | §2 |
| 7 `--main` defaults to HEAD | Corrected in one line: the default is `origin/main`. | §1 item 5 |
| 8 `negated` reviewer-judgment residual | Added to the reviewer guidance. | §5 |
| 9 `W-GR-EPSKAPPA` literal-only | Not changed. It is not among the authorized corrections. W-P-18 and W-P-19 still pass. | §1 |
| 10 Spurious "exit 0" line in r3's self-test output | `results-r4/self-test.txt` holds only the program's output. The r3 file is unchanged. | — |
| §5 Candidate manuscript finding (ch05:13, FULL:1328) | Still flagged under r4 (`W-BM-EUCLID`, C). Not adjudicated here. | §4 |

## Owner items

| Item | Disposition |
|---|---|
| "Authorize all four proposed corrections and the documentation changes." | Corrections 1–4 in §1. Documentation: §0, §2, §5, and the `--main` line. |
| "Do not expand the vocabulary beyond the stated corrections." | No term added. The only changes to the lists are the inflections and the bare-head qualifications of correction 4. |
| "Explicitly acknowledge that independent scientific review remains responsible for detecting reworded claims outside the checker's defined patterns." | `DESIGN-r4.md` §0, this note's plain statement, and the `work/proto.r4.py` docstring. |
| "Complete one focused independent review before presenting the design for adoption." | Not yet done. It is the next step (`DESIGN-r4.md` §7). |

## What changed in the measurements

- **Controls (195).** Identical outcomes under r3 and r4.
- **Batch W.** Only W-P-09 changes (PASS → REVIEW).
- **Records and exit codes.** 73 controls, all as expected under r4. One r3 expectation is reversed
  by correction 2: a `question` record whose evidence lacks the cue. Four controls re-exercise the
  r3 record checks that correction 1 would otherwise mask on H-token sentences. One control records
  a residual that the corrections as stated leave open: an H-token only in a code-A finding's
  window.
- **Tree M.** 23 bare-head findings fall away, and one `couplings` finding is added
  (`papers/SM.md:527`).
- **Injection.** Earlier controls: 0 PASS under both. Batch W: 116,494 → 109,679 PASS. Three W items
  gain a few PASS through host-paragraph findings removed by correction 4.

## Files added in r4

`DESIGN-r4.md`, `CHANGES-r4.md`, `work/proto.r4.py`, `work/run_r4.py`, and `results-r4/`:
`self-test.txt`, `controls-W.txt`, `compare.txt`, `exitcodes.txt`, `m2.txt`, `injection-r4.txt`,
`injection-r3.txt`, `treeM-scan.txt`, `treeM-scan-summary-r4.json` and
`treeM-hypothesis-token.txt`.
