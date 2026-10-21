# Node 8 step 1, revision r1: changed output lines

This file compares `p8s1.r1.run1.out` (from `p8s1_r1.py`, amendment A-3) with `p8s1.run1.out` (from `p8s1.py` at
`390e252f`). The output has 372 lines against 365. `diff` reports the changed hunks listed below. Every other line is
byte-identical, including all access classes, digests, transformation counts, preparable-set and pure-set counts,
mutant verdicts, convex-closure lines, SHARED-ALT and the eight section 6.10 summary lines.

**Outcome comparison.** The comparison parses the budget m=3 line of each class in both files and takes four values
from it: the Pur-E pass count, the number of states, the Pur-E fail count, and the Pur-U verdict word.

| class | 390e252f | r1 |
|---|---|---|
| R1a, R1b | 2 of 63, fails 61; Pur-U fails | same |
| KSWAP, CLC4 | 2 of 63, fails 61; Pur-U holds | same |
| CL | 2 of 9, fails 7; Pur-U holds | same |
| R2a1, R2b1, R2a2, R2b2 | 4 of 93585, fails 93581; Pur-U fails | same |

No Pur-E or Pur-U outcome changed, and no check changed from pass to fail.

## Changed lines, by cause

**Input digest (no outcome).** Line 4: the AMENDMENTS sha256 is `f0ab4db2…dcc04`, not `6856df0d…5ebec`, because A-3
was appended.

**F3, C2 not checked (text only).**
- Line 143: the K-C1C4 check message ends "(C1, C3, C4 measured; C2 not checked)". It no longer ends "(C2 by the
  structural reading: every step is a bijection)".
- Lines 147–150 and 152: the K-PR6 K-C1C4 lines add "C2 not checked". Line 152 reads "passes C1, C3 and C4" and no
  longer reads "passes K-C1C4". The value (False) is unchanged.
- Lines 155–164: each passing class reads "C1, C3 and C4 pass, C2 not checked" and no longer reads "passes". The
  candidate list states that independence from all of C1–C4 is not established for its members. The K-C1C4-classes
  message is reworded the same way. The candidate set, the failing set (R1b), the witnesses and the protocols are
  unchanged.

**F1, new positive controls (added lines 216–222; gating).** These lines are K-PURPOS: two fixture lines through the
one-bit generator (`onebit_grid_text`), with counts 2 of 63 and 3 of 63, so the mixed state P(h=1) = 1/2 is counted.
They are followed by the K-PURPOS check, the K-PURPOS-SPK fixture line (7 of 7, the mixed A-state with 24
purifications) and its check. Line 238 (originally 231) appends both checks to the I-6 gate list. The check total rises
from 22 to 24.

**F1 and F2, generated verdict text (no outcome change).**
- Lines 255, 269, 283 and 297 (R1a, R1b, KSWAP, CLC4; originally 248, 262, 276, 290). The Pur-E clause names the
  states with at least one purification, counted from the purification table, and no longer names "the pure states".
  The Pur-U clause gives, for each state with two or more purifications, "connected pairs c of t". It names the
  connecting map, or the unconnected pairs of purifications, followed by "no collected reversible transformation of B
  (n maps) connects these pairs". R1a and R1b: 0 of 2 for delta_0 and for delta_1. KSWAP and CLC4: 2 of 2, by
  'perm[id] ; perm[(0,)->(1,) (1,)->(0,)]'. The clause states that states with one purification are vacuous for Pur-U
  (0 such states) and that the 61 states without a purification are Pur-E failures, not Pur-U cases.
- Lines 321–322, 331–332, 341–342 and 351–352 (the four R2 classes; originally 314–315, 324–325, 334–335, 344–345).
  The composites line says that the composite lemma's argument is printed with the budget m=3 line. It no longer says
  "validated on the one-bit composites". The m=3 line counts Pur-E from the purification table of the lemma's 16
  products of point masses and prints the lemma's argument. The Pur-U clause reports "connected pairs 2 of 12" for
  each of the four point-mass states: (1,0) <-> (0,1) are connected by 'perm[id]', and the other 10 ordered pairs are
  named as unconnected. The hard-coded text "(the hidden cells are never written by any op or phi)" is removed.
- Line 245 (originally 238): the K-CL message reads "(one instance of the composite lemma used for the R2
  composites)", not "(validates the lemma ...)".

**F9, gating (text only).**
- Line 369 (originally 362): the A1-SCOPE message states that each line is scanned before printing.
- Lines 371–372: the check count is 24 PASS. The final line reads "P8S1  HOLDS (certifies the controls only; ...)".

## Sensitivity of K-PURPOS

A scratch run evaluates the positive-control condition with the Pur-E count replaced by the rule of `390e252f`
(k = size of the single-system pure set). The condition fails: the line reports "holds for 2 of 63". Under the
repaired rule it passes: "holds for 3 of 63". In the run itself, the static check A1-PRINT caught one draft print that
carried purification text outside `pur_line`. The draft was reworded before the recorded runs.

## Replay

`python3 -I -B p8s1_r1.py` was run twice from `probe/`. Both outputs are byte-identical, sha256
`82dbd118fb8521bcb944bc8638c80b14654d30a50d5f00145d112cfcb2910734`, Python 3.13.16, about 35 s per run. The original
run is reproduced byte for byte from a checkout of `390e252f` with `python3 -I -B p8s1.py`.
