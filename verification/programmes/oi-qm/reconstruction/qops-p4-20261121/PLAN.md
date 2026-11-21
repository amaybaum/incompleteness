# QOPS-P4 plan: the smallest candidate that is natively both non-MIO and non-DIO

**Standing. Plan, committed before the analysis it governs.** Round 4 of the research tracks
([#1169 c.7067281228](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7067281228)),
native-mechanisms track. Design and paper research only. Not authorized:
- running a preregistered computation;
- implementation;
- merges;
- manuscript edits;
- counting an imported quantum operation as native;
- adopting any premise automatically.

- **Goal link (§A.47).** Serves #1169 (`QM ⊆ OI + E`), O1, with O3 kept in the same model. It
  decides which of READOUT-ALG's open instruments and sites could supply a non-DIO element, a
  non-MIO element, or both, natively, and what the smallest additional premise is in each case. It
  does not decide whether any premise holds.
- **Base.** Stacked on #1518 at `46240053`, which was reviewed and CONFIRMED WITH NITS, with its
  nits applied. #1518 stays as reviewed. Accountable Issue: #1490.
- **Inputs.**
  - READOUT-ALG (#1513 at `4554dd63`, `RA`). It is provisional and under review. Its finding is
    treated as a question, under the owner's provisional-readout constraint (#1169
    c.7066770882).
  - OPRES (#1511 `7669e511`): Lemma C and Theorem C.
  - From #1518: Q-ind, narrowed; P6 ("at least one; one suffices"); H-F1 and its ties; and
    T-WP's productivity, NON-GEM as a computation.
- **Rules applied.**
  - The three readout levels are kept apart: effects, instruments with their updates, and
    operationally accessible algebras.
  - The layer rule: ontic or Born-form; typing, soundness or operational. Each result is stated
    at the layer where it is proved.
  - (N)/(I) labels, and Established / Assumed / Missing.

## Questions

1. **Q1.** For each of RA's items left Open for O1-D (items 1, 4, 11, 12 and 22) and each
   full-algebra site (items 24 and 25), does it supply non-DIO natively, non-MIO natively, or
   neither? What is the smallest additional premise that would make it supply each? This is the
   opposite direction to RA §3.1, which names premises sufficient for DIO.
2. **Q2.** Over all candidates, including #1518's H-F1 and its ties, what is the smallest one that
   supplies **both** non-MIO and non-DIO with no imported quantum operation counted as native? If
   no candidate is native, which needs the smallest premise, and at which level and layer?

## Productivity test (fixed now)

**GEM** iff both hold:
- (i) at least one Q1 classification is strictly stronger than RA's own for that item. That
  means it is decided at the instrument level from a premise weaker than RA §3.1's, or decided
  without a premise;
- (ii) Q2's answer names a ranked minimal premise set, with at least one premise not named in RA
  §3.1 or #1518.

**NON-GEM** if every classification restates RA or #1518.

**INCONCLUSIVE** if the decisive instrument-level question cannot be settled on paper. The
missing input is then named.

## Method and limits

- Paper proofs and readings only.
- No computation, and no new preregistration unless a decisive computation is found. If one is
  found, it is preregistered and not run.
- The record goes under `verification/programmes/oi-qm/reconstruction/qops-p4-20261121/`.
