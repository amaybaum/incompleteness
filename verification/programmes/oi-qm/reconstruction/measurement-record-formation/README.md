# MR-1 — status

MR-1's preregistration in this directory is frozen by owner designation (amaybaum,
2026-10-31T21:14:51Z: "I hereby designate exact commit `1a236f332e8ea12b7fdb125bf8c5098ccd71d36c`
as the MR-1 preregistration freeze.";
[#1023 comment 6549225579](https://github.com/amaybaum/incompleteness/pull/1023#issuecomment-6549225579)),
and its amendments and stage-1 log are append-only (`amendments/MR-star.md:3–5`,
`amendments/KS-substitution.md:3–4`). None of them is edited. This note states the standing of
the stage-1 token and qualifies two of their premises and one set of their negative claims.

**G★ item 2.** `preregistration.md:99` names G★ ("G★ named"), and `:638–639` provides that "a
map `Θ` from `𝔐★` into the carrier meeting G★ items 1–5 is reported as a separate finding for
owner disposition"; no MR-1 token uses G★ as its criterion. G★ is defined in F2-1's frozen A★
(`verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md:140`).
Item 2 states that no diagonal unitary commuting with the readout projectors conjugates `G_Θ`
into either class, and that this "is necessary for `R`". The necessity fails for the
ones-fixing class:

- `D†·rot·D` lies in `onesClass` for `D = diag(1, i)`: kernel theorem
  `OIBridge.PC1Controls.gauged_rot_mem_onesClass`
  (`verification/lean-mathlib/OIBridge/PC1Controls.lean:132`);
- every architecture containing `rot` has `R`: kernel theorem
  `OIBridge.PC1Controls.falsifier_available_of_mem` (`PC1Controls.lean:324`).

Both are built on `main`; the argument is finding PC-F1,
`verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/preregistration.md:87–100`.
PC-F1 states that the necessity holds for item 2's clause without a gauge and for the
nonnegative half of its gauge clause (`:99`), and keeps the ones-fixing gauge condition as an
L2 requirement that every generated class with `P` meets (`:96–98`). Item 2 as written
therefore asks more than `R` needs, and the necessity of its gauged ones-fixing condition for
`R` is not a valid premise. The full F2-1 status is in
`verification/programmes/substratum/recursive-substates/README.md`. MR-1's citations of G★
item 3 (`preregistration.md:105–106`; `amendments/MR-star.md:124`, `:668`) are unaffected.

**The stage-1 token `GAP` is provisional.** It stands only if a controls-only stage 2, under its
own owner gate, returns every reference result of §M.4–§M.8; otherwise it is `VOID` under 0(i)
(`amendments/MR-star.md:876–878`; `amendments/stage1-log.json:745`). No stage 2 has been
authorized or run.

**Proposition B2.** B2 (`preregistration.md:307–311`) is proved on paper from #912's conditional
theorem (`../composition-access-20261024/REPORT.md`). The review record of that package is
author-posted and names no reviewer (`../composition-access-20261024/SCOPE.md`), so the proof B2
rests on is not independently reviewed on `main`. B2 asks that the controller's randomness be
independent of `U` given the public history; #912's theorem covers a controller whose randomness
is independent of the whole residual boundary. Whether B2's weaker condition suffices is open
(#1088 comment 6636314963).

**Negative claims are limited to the sources read.** MR★'s correction C.1-1
(`amendments/MR-star.md:1527–1532`) restricts C-3's "is stated anywhere" and C-13's "exists in the
corpus" to the sources read (§S.8), since no corpus-wide search was recorded. The same restriction
applies to C-3's "No principle in the corpus supplies one" (`amendments/MR-star.md:1353`), which
C.1-1 does not name.

**N5 / LA-EQUAL proof standing.** Two read-only, model-authored reviews of the LA-EQUAL proof are
consolidated in [LA-EQUAL-REVIEW.md](LA-EQUAL-REVIEW.md). Under the stated hypotheses, the tail
independence and `EMPTY` have a conditional argument. The full `LA-EQUAL` equality is not
established: it also needs the setting-independence of the pre-cut history, which requires a
hypothesis outside H-prior's displayed form (the pre-cut port-5 bank law) and the parent unit's
forward-kernel proof, which is not independently reviewed on `main`. None of the five hypotheses is
derived for native OI, and H-rule is the native-Y model rule, not the corpus's selected linear rule.
The frozen N5 text is unchanged and is not a premise of an established claim (AGENTS.md §A.46
item 7). The proof gap belongs to #1007 and its consequence for MR-1 to #866.
