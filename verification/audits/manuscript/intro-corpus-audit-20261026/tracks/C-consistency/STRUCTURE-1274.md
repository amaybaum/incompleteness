# Structure :1274 — classification (coordinator draft, awaiting independent review)

Base: main a5168789.

## Claim (papers/Structure.md:1274, tail)
"[Main]'s reverse-direction lemma (every P-indivisible process on a finite configuration
space admits a deterministic dilation) is consistent with the same correspondence (the lemma
carries its own proof in [Main §3.2])."

## What the cited source proves
- Main.md:270 Lemma (Reverse direction, scoped): a single one-step doubly stochastic matrix is
  the one-step marginal of a bijection with uniform hidden prior (exact iff rational). Its own
  scope sentence: "The scope is the matrix, not the process ... is not claimed by this lemma".
- Main.md:512/514 finite-horizon process dilation (+ response-table extension): every stochastic
  process on finite C_V, on a finite horizon K, has an exact bijective realization from
  P0 ⊗ mu_H (structured, non-uniform prior). No P-indivisibility hypothesis: universal.
- Main.md:634 Remark (consolidation): the exact all-time form is false — a fixed finite
  bijection has finite order L, so its multi-time law is L-periodic; a nonperiodic target has no
  exact all-time realization by one fixed finite substratum.

## Classification
Instance of the already-identified class fixed at Substratum :136 by #951 (process-level
realization attributed to the scoped one-step §3.2 lemma). Not a new scientific issue in the
framework: Main's own statements are correct; :1274 is a stale/overstated restatement.
Two aggravations relative to the Substratum :136 instance:
1. No horizon qualifier. Read as an all-time process statement it is refuted by Main :634.
2. The "P-indivisible" restriction is spurious (the finite-horizon theorem is universal,
   Markov chains included — cf. Main :427, Explainer :381); harmless as a subset claim but it
   suggests the dilation is specific to the indivisible class.
Wrong citation: §3.2 → §3.4.

## Sibling site found by grep (not in Track C's report)
papers/Substratum.md:110 — "[Main §3.2] ... reverse-direction lemma (stochastic process →
bijection)". Same class: the §3.2 lemma maps a matrix, not a process.
Corpus grep (papers/*.md, book/*.md) for reverse-lemma phrasings: no other overstated site;
book Lemma B.2.2 (appendix-b :42, FULL :5809) mirrors the scoped Main :270 correctly;
ch01 :179 / FULL :523 and Explainer :381 state the process form with "on any finite horizon".

## Proposed replacement text (for a separate PR after review)
Structure :1274 tail →
"[Main]'s finite-horizon process-dilation theorem (on each finite horizon, every stochastic
process on a finite configuration space, P-divisible or not, is the visible marginal of a
deterministic bijection with a hidden prior independent of the visible initial state; no single
finite bijection realizes a nonperiodic target exactly for all times) is consistent with the same
correspondence (proof in [Main §3.4])."
Substratum :110 →
"- [Main §3.2] Forward Stinespring dilation (bijection → CPTP channel) and reverse-direction
lemma (one-step doubly stochastic matrix → uniform-prior bijection); [Main §3.4] finite-horizon
process dilation (stochastic process → bijection, per horizon)"
Regenerate Structure.tex/.pdf, Substratum.tex/.pdf via sh ./build.sh Structure Substratum.
Status class: paper proof (Main §3.4) for the restated content; no Lean identifier claimed.

## Track C S-3 (:1180/:1190/:1256) — classification
SC-3 propagation class (recurrence-scale P-indivisibility credited to C4 alone: "from C4 plus a
fixed finite reversible representative"). True as a sufficiency statement, but C4 is not needed:
any non-deterministic visible step gives the non-permutation rooted map (Main §2.3, merged SC-3).
Not SC-16: these sites claim recurrence-scale, not accessible-window, indivisibility.

## After independent review (REVIEW.md: CONFIRMED, same class, not a new scientific issue)
- Replacement for :1274 to say "a finite deterministic bijection (depending on the horizon K)", since "on
  each finite horizon" leaves open whether one bijection serves all horizons.
- Root cause missed above: the remarks after the scoped lemma call it "the correspondence at the
  stochastic-process level … both directions" — Main:274 and appendix-b:46 = FULL:5813. With a uniform
  prior the converse holds only for doubly stochastic matrices, and only for one step. These remarks are
  corrected in the same unit as :1274 and Substratum :110.
