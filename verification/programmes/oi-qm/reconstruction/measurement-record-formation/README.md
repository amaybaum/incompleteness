# MR-1 — status of a cited premise

MR-1's records in this directory are frozen (the preregistration by owner designation,
[#1023 comment 6549225579](https://github.com/amaybaum/incompleteness/pull/1023#issuecomment-6549225579))
and are not edited. This note qualifies one premise they cite.

**G★ item 2.** `preregistration.md:99` names G★ ("G★ named"), and `:638–639` reports "a map `Θ`
from `𝔐★` into the carrier meeting G★ items 1–5" as a separate finding. G★ is defined in F2-1's
frozen A★
(`verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md:140`).
The ones-fixing half of its item 2, the statement that no diagonal unitary commuting with the
readout projectors conjugates `G_Θ` into a ones-fixing class and that this "is necessary for
`R`", is refuted on `main`:

- `D†·rot·D` lies in `onesClass` for `D = diag(1, i)`: kernel theorem
  `OIBridge.PC1Controls.gauged_rot_mem_onesClass`
  (`verification/lean-mathlib/OIBridge/PC1Controls.lean:132`), built on `main`;
- any class containing `rot` has `R`, so the gauged ones-fixing condition is not necessary for
  `R`: finding PC-F1,
  `verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/preregistration.md:87–100`.

The nonnegative half of item 2, and its clause without a gauge, stand. G★ items 1–5 as written
therefore ask more than `R` needs, and the refuted half is not a valid premise for any claim.
The full F2-1 status is in
`verification/programmes/substratum/recursive-substates/README.md`. MR-1's G★ item 3 citations
(`amendments/MR-star.md:124`, `:668`) are unaffected.
