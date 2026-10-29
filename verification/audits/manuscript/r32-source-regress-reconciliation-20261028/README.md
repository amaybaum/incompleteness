# R32 source reconciliation: deeper-substratum regress

Base: `20ca05fe9e7e460de29e08f7a21029042fa45b12` (held PR #982).
This is a separate source-correction checkpoint for #946 and Introduction #918;
it does not move that reviewed head or authorize a merge.

## Concrete defect

Book Chapter 3's concluding turtles paragraph claimed a proof that below a
certain depth the word "below" stops referring, despite its preceding paragraphs
retaining an open complete observable/gauge classification. The preceding
paragraph also called the gauge boundary a proof of where deduction ends.
Neither assertion follows from the restricted ancillary invariance.

## Correction and scope

The two assertions now state the declared premises, conditional mathematical
results and open physical reconstruction obligations. The positive redundancy
claim is confined to Theorem 24(iii)'s independently prepared normalized decoupled
ancilla at the fixed channel interface. No global gauge, regress-termination or
new physical theorem is asserted. Chapter 3 and FULL are mirrored exactly.

The old "below a certain depth" claim has zero remaining occurrences in maintained
paper/book Markdown and regenerated book TeX. Legitimate discussions of declared
premises and the open regress question are preserved. No canonical paper theorem,
Lean source, ledger classification or historical review record is changed.

## Publication evidence

`sh ./build.sh --book` succeeded: 547 pages, no missing glyphs. The source stamp,
MD/TeX/PDF SHA256 values and ordered mirroring of all 28 book content files are
recorded in `publication-check.json`. Corrected pages 99–100 were rendered and
visually inspected. Full normal PR CI and independent acceptance remain separate
gates; no native F/E action or merge is authorized.
