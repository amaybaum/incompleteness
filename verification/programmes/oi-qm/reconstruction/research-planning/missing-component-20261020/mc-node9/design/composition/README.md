# Composition lemma under the report18 rule (coordinator-authored, unreviewed)

> **WIP / UNVERIFIED — research record.** The coordinator's session produced this investigation, at the owner's
> instruction, as the composition-lemma target named in report19. Owner-session handoffs are reviewed
> independently, and this one is not reviewed yet. It adopts no premise.

- `PREREG.md`: the decision rule and the held-out sizes (n = 9, 12). Both were fixed before the builder existed.
- `REPORT.md`: the builder, the branches tried and the verdict.
  - Section A, the builder, was hashed before any held-out run; `REPORT-sectionA.sha256` holds that hash.
- `composition_checks.py`: the checker. Its helper modules sit beside it.
  - Its saved output is `composition_checks.out`.
  - Replayed normally and with `-O`, byte-identical; about 1 minute.
- `check3d_78.out`: full 3-D dynamics at n = 7 and 8 (`check3d.py 7 8`; 554 s and 954 s).

**Verdict, as the checker generates it:**
- At every discovery size (n = 2–8) and both held-out sizes (n = 9, 12), the builder gives exact ANDₙ with degree n.
  This holds on the exact register machine and on the 3-D first-light sweep.
- Full 3-D dynamics on dense full-torus backgrounds confirm it for n = 2–8.
- The preregistered full-torus criterion is not met at the held-out sizes. At T = 169 and 241 those runs are beyond
  bounded compute.
