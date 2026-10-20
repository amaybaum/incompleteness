# Node 7 amendments

Amendments to the frozen preregistration (`PREREG.md`, sha256
`99834efa540bbf0d2f6cd84bc819daa71b7d612864775285785e033739ebd3bc`, committed at `73a27ba1`). `PREREG.md` is not
edited. Each entry gives its date, its reason, and whether any result was known when it was written. No entry changes a
decision clause in a candidate's favour.

**State of knowledge when A-1 to A-7 were written (2026-10-20).** No probe of step 2 had been run, and no clause
outcome had been computed for any candidate. The preregistration's own notes already anticipate some outcomes. Drafting
reasoning about the H-Bell functionals had suggested the shape of the HB-3α result. That is stated where it applies.

***

**A-1. K-8: the carrier size of the Tsirelson-near point (a bug in a stated detail).** Written before any probe ran.
- PREREG §4.3 and the K-8 row place the PR/anti-PR point v = 12/17 "at n = 34". That box has entries
  (1 ± 12/17)/4 = 29/68 and 5/68, so in 𝒜_CHSH it needs n = 68. In 𝒜_CHSH every λ value carries one deterministic
  response pair, and the PR box itself is the mixture of two such pairs.
- In the long-edge gate class the same box is reached at n = 34: the shared bit λ supplies the halving, and the
  anti-PR weight is k/n = 5/34.
- K-8's claim ("𝒜_CHSH(100) and the gate class each contain a TLM-certified quantum point within ε/4 of the Tsirelson
  correlation") is unchanged and is tested as stated, at n = 68 and n = 34 respectively.
- No decision clause changes.

**A-2. K-10: the n = 4 part is not run.** Written before any probe ran.
- K-10's exhaustive check runs locally at n ≤ 3. The n = 4 check needs a CI dispatch, which needs owner approval and was
  not requested.
- Under the no-reduction clause, K-10 is "incomplete beyond n_done = 3" until that run.
- Every clause that the reduction could decide is reported with the dependence stated. In this execution no clause is
  decided through the reduction: every member of 𝒜_CHSH that a clause uses is exhibited explicitly as a list of
  deterministic response pairs and checked directly.
- I-6's gate is applied as follows. Verdicts are printed, labelled "provisional on K-10 (n = 4, CI)". If the n = 4 run
  fails, every verdict is void until reviewed.

**A-3. HB-3α: how the ensemble weight enters the hop-metric functional.** Written before the HB-3α computation ran.
Drafting reasoning had already suggested that the condition fails for every w > 0.
- PREREG names "ensemble weighting" as the interpretive choice. It does not say how the weight w enters a functional
  whose metric (the hop metric of the support graph) does not depend on edge weights. Two readings are evaluated:
  - option 1: the support graph's hop metric, with uniform measures on its balls (independent of w for w > 0);
  - option 2: the support graph's hop metric, with the ensemble average of the per-graph ball measures,
    m_x = (1 − w) m_x^{reference} + w m_x^{glued}.
- HB-3α receives a verdict only if both options give the same admitted set. Otherwise it is Parked with the option
  named as the gap. This adds a Park condition, so it cannot favour the candidate.

**A-4. L3-C: which record statistics.** Written before the L3-C computation ran.
- PREREG fixes that records are read at the readout phase of the clock. It does not fix whether the record law is:
  - (α) the first pass from the initial-configuration slice; or
  - (β) the stationary readout-phase statistics over the selected orbits.
- Both are evaluated. L3-C receives a verdict only if both give the same verdict, and is otherwise Parked.

**A-5. PC-4b in the POM scenario.** Written before the PC-4 computation ran.
- For DR, Th(R) under the family's own accessible set needs a choice the preregistration does not make: whether a
  readout may write to a pointer it has written before (DR uses fresh pointers and fresh disturbance bits).
- Under PREREG's rule the POM part of PC-4b is Parked with that choice named. The CHSH part is decided on LE, whose
  readouts need no such choice.
- Under §6 precedence a Parked part prevents a decision only if the decision depends on it. A failure in the CHSH part
  decides Failure whatever the POM part gives.

**A-6. PC-3b, the (b1) grid search.** Written before any probe ran.
- For PC-3b, which is K-P, a box is admitted only through the inner set: an exhibited exact quantum realization or,
  for zero marginals, an exactly certified TLM inequality. So no admitted box violates TLM.
- The (b1) search over the full correlator grid for n ≤ 100 (about 2·10⁹ points) is therefore replaced, for PC-3b
  only, by that written argument plus an exhaustive bounded instance at n ≤ 12.
- This substitutes an argument for an enumeration on a result that holds by construction. It is flagged here because
  it touches a positive control's (b) clause. It does not enter any classification: §6 classifies on the family stage,
  (a) and (a-POM).

**A-7. Productivity, the first clause.** Written before any probe ran.
- The first clause ("a principle passes (Emergence or Reproduction with outcome (a))") is met by PC-3b only if PC-3b
  passes. PC-3b is the quantum set itself, which passes by construction (it is K-P).
- Both readings are reported. The literal reading is met by PC-3b. On the substantive reading, that pass carries no
  information, and the verdict rests on the second clause.
- This can only lower a gem claim.

***

**State of knowledge when A-8 and A-9 were written (2026-10-20).** After the first debug runs of `p7.py`. A-9 was
written after the control gate had suppressed every verdict, so no candidate verdict was known. A-8 was written after
the candidate verdicts of the second debug run were known.

**A-8. HB-3α: a probe check that was too strict (a bug in the test, not in a decision clause).**
- The probe asserted that the reference curvature on the lattice edge (A, A+e1) is exactly 0 at L = 6 and 8. With
  mesoscopic radius δ = 2 it is 4/25 and 2/25 there, because on a small torus the coordinate function is not
  1-Lipschitz across the wrap. It is exactly 0 for L ≥ 10 (computed), and on ℤ³ (z₁ is 1-Lipschitz, so W1 ≥ 1, which
  is the translation cost).
- The check now requires the reference value to be ≥ 0 at every L and exactly 0 at L ≥ 10. L = 10 and 12 were added
  as further instances, and L = 4 is reported as a flow instance only, since the closed form needs 3L/2 ≥ 4δ + 1.
- HB-3α's decision rests on the long-edge pair: κ(A, B) ≤ −5/4 for every δ ≥ 1 and every w > 0, while the reference
  value tends to 0. That is unaffected. The candidate fails with either version of the check, so the change cannot
  favour it.

**A-9. The perfect-correlation certifier (a bug in the test).**
- The first version flagged a box whenever three CHSH-oriented signed correlators equalled 1 and the fourth did not.
  That wrongly excluded the local box E = (1, 1, 1, 1). K-7 failed, and I-6 suppressed every verdict, as designed.
- The certifier now applies the argument as §2 states it: if three correlators are ±1, the fourth must equal their
  product.
- No verdict had been printed before the fix.
