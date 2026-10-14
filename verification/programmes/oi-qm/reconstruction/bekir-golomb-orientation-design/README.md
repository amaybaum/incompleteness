# Orientation diagnostic of the Bekir–Golomb formal premise

This package proves that the repository proposition
`OIBridge.ScopeTransfer.BGIntegerClassification` is false as stated. It does
not refute the published Bekir–Golomb classification or the physical
two-branch conclusion. It is design evidence, not a certified native round.

The baseline is `dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`.

## Exact finding

Take the source `(0,1,4,10,12,17)` and reflect the second printed ruler:
`(0,1,8,11,13,17)` becomes `(0,4,6,9,16,17)`. The pair satisfies every
hypothesis of the formal premise, including strict order, unique positive
differences, equal difference sets, and exclusion of translation and
reflection congruence. No pair of relabelings satisfies its positive
exceptional conclusion. The reversed exceptional conclusion does hold.

`OrientationDesign.lean` proves the hypotheses, impossibility, refutation and
both positive controls. A proposed positive correspondence forces three
linear relations on the source labels. A kernel decision over all 720
source permutations (`source_difference_cases`) shows that every surviving
configuration has one of three difference patterns; that exactly three
permutations survive is checked by `exact_check.py`, not by the kernel. In
each pattern, two forced gaps cannot originate at one target mark, checked
over all 216 target triples.
This proves impossibility for every pair of relabelings. It uses
`decide +kernel`, without `native_decide`, `Lean.ofReduceBool` or `sorry`.

`exact_check.py` compares complete gap fingerprints of all 720 × 720
permutation pairs. `independent_check.py` instead uses unique directed gaps
to force the target labeling for each source labeling. They share no
arithmetic implementation or generated correspondence table. Both read
`r1`, `r2` and `mu` from `HomometricSix.lean` with the same pattern and both
reflect a ruler assuming its first mark is 0, so an error in those
definitions or in that parse would affect both checks alike. Each rejects a
translation, a reflection-congruent pair and a corrupted correspondence. Both report three
positive and zero negative matches for the original pair, and zero positive
and three negative matches for the singly reflected pair. They agree for all
eight reflection/order variants.

`quoted_family_check.py` independently expands the recorded primary-source
factorizations using exact integer coefficient vectors. It checks all 15 gap
identities as identities in both parameters for the quoted family, either
ruler order, and independent reflections. The same count is empty for a
corrupted correspondence, a translated family and a reflection-congruent
family. These are family controls, not a
proof that the family exhausts the general exceptional class.

## Conditional repair

`SignedRepairDesign.lean` is the candidate companion module. It places the
orientation choice outside the universal gap quantifiers. It transfers both
orientations to real spectra and excludes the reversed exceptional physical
branch by conjugating the source eigenbasis and applying the existing
six-mode obstruction. The exclusion uses the actual hypotheses: unitarity,
nonzero overlaps, distinct gaps on both sides and equality of all probability
families. The general signed classification remains an explicit hypothesis.

The manuscript and registry statements of this result are in
`papers/GR.md` §3.3 and `verification/coverage/LEDGER.json`. BG-1's frozen
records are unchanged.

## Compilation and reproduction

The seven diagnostic reports and three conditional-repair reports passed in
[Actions run 38534906783](https://github.com/amaybaum/incompleteness/actions/runs/38534906783)
at `c3a3fe9ec00b64802dda5878c5ffcd9f69584e13`, using the repository's pinned
Lean/Mathlib project. `axiom-reports.txt` records the actual reports. Every
axiom lies in `{propext, Classical.choice, Quot.sound}`. All 303 legacy records
and 46 existing native receipts passed the preservation checks. The
workflow also runs `quoted_family_check.py`, which has no Lean component.

From the repository root, run the three Python files with `python3 -I -B`.
After building `OIBridge.TurnpikeScopeTransfer` and `OIBridge.PiccardBridge`,
run each design Lean file with `lake env lean` from
`verification/lean-mathlib`, using its repository-relative path. The workflow
spells out those commands, checks the count and contents of every report,
compares each Python output with its committed JSON, and verifies
`SHA256SUMS`.

The next classification obligation is the complete source-to-proposition
comparison, including every normalization and exceptional case, followed by
a general proof if pursuing kernel closure. Neither accepting this diagnostic
nor compiling its consumers establishes that obligation.
