# MR-1 — status of a cited premise

MR-1's preregistration in this directory is frozen by owner designation (amaybaum,
2026-10-31T21:14:51Z: "I hereby designate exact commit `1a236f332e8ea12b7fdb125bf8c5098ccd71d36c`
as the MR-1 preregistration freeze.";
[#1023 comment 6549225579](https://github.com/amaybaum/incompleteness/pull/1023#issuecomment-6549225579)),
and its amendments and stage-1 log are append-only (`amendments/MR-star.md:3–4`,
`amendments/KS-substitution.md:3–4`). None of them is edited. This note qualifies one premise
they cite.

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
