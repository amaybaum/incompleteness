# QOPS-P3 plan: the next minimal native-mechanism test

**Standing. Plan, committed before the analysis it governs.** Design level only, under the owner's
portfolio decision
([#1169 c.7066630306](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066630306),
Group B, "Native mechanisms … find the next minimal mechanism test"). Paper research and
preregistration are authorized. No computation, implementation, CI dispatch, manuscript edit,
premise adoption or merge is authorized.

- **Goal link (§A.47).** Serves #1169 (`QM ⊆ OI + E`), on O1 and O3 together. It identifies the
  smallest hypothesis that would add one of three things to OI's native operations, and designs
  the test that would decide it:
  - a non-MIO element;
  - a non-DIO element;
  - a native ready-cell source.

  It does not decide whether any hypothesis holds.
- **Base.** Stacked on #1501 at `cd3672fa`, which was reviewed and CONFIRMED WITH NITS, with its
  last nit applied. #1501 stays as reviewed. Accountable Issue: #1490.
- **Inputs, at their reviewed standing.**
  - OPRES #1511 at `7669e511`: Theorem C, Proposition D and Remark D′, all (I).
  - The owner's restatement of O1 as two separate obligations, non-MIO and non-DIO
    (#1169 c.7066541026).
  - I3-SOURCE #1508 at `df520f3b`: S1 and S2, both (I).
  - QOPS-P2 #1501 at `cd3672fa`: P1–P5, J1 and amendment A01.
- **R-READ** (are native readouts in the configuration algebra?) is **unresolved**. READOUT-ALG
  (#1513) is checking it. Neither answer is assumed.

## Questions

1. **Q1.** How do O1's two obligations relate to O3's ready-cell link in one model? Does
   supplying one discharge another?
2. **Q2.** What is the smallest candidate mechanism, labelled as a hypothesis, that supplies a
   non-MIO element, a non-DIO element or a ready-cell source natively, with O1 and O3 kept in
   one model? "Smallest" is ordered by:
   - first, the number of elements outside OPRES's native class `𝒩`;
   - then, the support of those elements (one gate, one time, one site);
   - then, the RES cost in pinned cells.
3. **Q3.** What is the minimal decisive test for it? It must have controls, a countercontrol and a
   classical-simulator countercontrol, and be useful under either answer to R-READ.

## Productivity test (fixed now)

The unit is a **GEM** iff all three hold:
- (i) the hypothesis is strictly smaller than FLOW for all native gates and all `t` (QS H-QOPS-G)
  in Q2's order;
- (ii) the preregistered test has at least one outcome branch that no known theorem fixes in
  advance;
- (iii) its classical-simulator countercontrol is not vacuous: some preregistered outcome would
  make it fail.

It is a **NON-GEM** if (i) fails, or if every branch of the test is fixed by a known theorem.

It is **INCONCLUSIVE** if (ii) cannot be decided on paper because it depends on an unresolved
input (R-READ). The input is then named.

## Outcome categories for Q1–Q3

Each question is answered as ESTABLISHED (with its proof or construction), OPEN, or INCONCLUSIVE,
and the missing input is named. Every result carries an (N) or (I) label with its imports named,
and the record ends with Established / Assumed / Missing.

## Method and limits

- Paper proofs and readings only.
- The test goes into `PREREG.md` as rules, with no outcomes.
- The record goes under `verification/programmes/oi-qm/reconstruction/qops-p3-20261121/`.
- No run.
