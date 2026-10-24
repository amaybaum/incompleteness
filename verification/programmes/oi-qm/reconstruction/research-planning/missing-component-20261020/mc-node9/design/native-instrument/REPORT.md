# A bounded native instrument under the report18 rule: report

> **Research record.** It reports the investigation preregistered in `PREREG.md`
> (sha256 `e92724ca…`). That it was written before any construction code rests on the timestamp recorded in
> `PREREG.sha256`: the preregistration was first committed together with the code. Every number below is printed by
> `instrument_checks.py` (saved output `instrument_checks.out`), except values marked as from the independent review
> (`review/REVIEW.md`) and two that the coordinator computed by
> hand from the definitions:
> - the entropy deficits: per read, Σ over the three fresh components c ≠ a of 1 − h₂((1 + a·c)/2);
> - the acceptance flag's degree: per component, "4-bit value < 10" is ¬b₃ ∨ (¬b₂ ∧ ¬b₁), of degree 3, and four
>   components give degree 12. That is the degree of this threshold sampler only: any exact sampler needs degree
>   at least 2, and lower-degree flags suffice (`review/REVIEW.md`).
>
> The coordinator wrote this report from the checker output and from the investigating session's summary.

## 1. The instrument

The rule is the unchanged report18 update U′ = H(SU) ⊕ U_old, with H(a, b, d) = (b, d, a ⊕ bd).

1. **Prepared distributions.**
   - For w ∈ {±X, ±Y, ±Z, ±R} (R = (4/5, 3/5, 0)), P_w is a hidden register of four bits λ_c, one per menu axis c.
     The bits are independent, with P(λ_c = 1) = (1 + c·w)/2.
   - Each bit is drawn by heralded rejection: four fair bits per component, accepted iff their value is below 10.
     At most two attempts are made.
   - One attempt accepts with (10/16)⁴ = 625/4096. That is the same for every w, so the herald carries no
     information about the preparation.
   - The preparation places 5 copies of each component, which adds 16 copy equalities, all independent of the
     setting.
   - **Why rejection is needed.** The R read needs non-dyadic probabilities, such as 9/10 and 1/10. Under uniform
     counting, a readiness event that is an affine subspace has a power-of-two count, so it cannot give them. The
     earlier constructions (reports 15–19) used only such events. Exact R values therefore need a rejection herald,
     or a supplied non-dyadic resource. More precisely, the accepted count's odd part must be divisible by 5 for each
     component, or by 25 for a single joint herald (`review/REVIEW.md`).
2. **Herald and clock records.**
   - The preparation herald is accept or fail, over at most two attempts.
   - The read reports at the record receiver at tick 2.
   - The re-preparation herald follows.
   - Ticks are update counts; there is no physical clock.
3. **Side-register access.**
   - The accessible record is exactly the preparation herald, the record receiver's triple at tick 2 and the
     re-preparation herald.
   - Every other register is inaccessible, by stipulation. That stipulation is part of the interface.
4. **Read and outgoing state.**
   - The read with setting a carries λ_a to the record receiver by first light. It arrives in field B at tick 2,
     so o = λ_a.
   - Re-preparation writes λ′_c = λ_a ⊕ 1 ⊕ r_c, with fresh r_c ~ Bern((1 + a·c)/2).
   - That map is linear because antipodal Born values are complementary.
   - Natively, three field-A sources XOR at each outgoing receiver.
5. **Readiness.**
   - 95 pins per record device and 93 per outgoing device: 467 across 5 devices.
   - The count is not minimal: by parity, odd-distance current-slice pins do not affect the tick-2 record.

## 2. Results (exact; all controls green)

**Controls**

| Control | Result |
|---|---|
| C-RANK | (1, w) has rank 4, and the four relations span its null space |
| C-QM (positive) | the exact quantum record laws satisfy every identity, single and two reads. It computes them from the Bloch formula the instrument is built from, not from density matrices as preregistered; the review's density-matrix computation agrees |
| C-AFF (scope) | an affine but non-Born law passes the identities, so the identities do not test Born values |
| C-ND (negative) | a non-disturbing instrument fails the sequential identities on 6 of 16 setting pairs; largest witness TV 2684038546875/2⁴⁷ ≈ 0.019 |
| C-HER (negative) | a herald whose acceptance depends on w fails the single-read identities; witness TV up to 9068125/2²⁶ ≈ 0.135 |
| C-NAT | releasing one even-distance readiness pin changes an accessible register |

The first C-NAT attempt released an odd-distance pin, and the record did not change, because by parity that pin
cannot affect the tick-2 record. The checker keeps that attempt as an observation and uses an even-distance pin
for the control.

**Questions**

| Question | Result |
|---|---|
| Q1: identities, single read | exactly 0 at every atom of the complete record, for X, Y, Z and R |
| Q2: identities, two sequential reads | exactly 0 for all 16 ordered setting pairs |
| Q3: Born values | the single-read and complete single- and two-read laws equal the quantum laws exactly |
| Q4: closure | given the herald and the outcome, the outgoing law is exactly P_{s·a}, jointly over all components |
| Q5: native realization | the record and outgoing registers of the single read equal the register-level map in 1024 runs, 512 input assignments × 2 dense full-torus backgrounds; receivers are silent before tick 2 |

**Q6: widening access**

| Access added | Result |
|---|---|
| (a) the unread hidden components | the identities fail; witness TV 95155025/2³⁰ ≈ 0.0886 for every setting |
| (b) the fresh re-preparation bits | the identities still hold, but closure given the record fails for every setting: the conditional law of the outgoing state given the record differs from P_{s·a} |
| (c) the record site, read natively at later ticks (readiness extended) | for this layout, with copy rows 8 apart in the order X, Y, Z, R: from window D = 8 every setting's record depends on unread components. The identities first fail at D = 8 for X and Z and at D = 10 for Y. For R the λ_Z dependence is invisible to this menu's identities. With the rows in the order Z, X, R, Y, the R read fails (TV ≈ 0.298) and Z is the invisible case (`review/REVIEW.md`) |

The R case in (c) is a dependence the identities do not flag, not a protection.

## 3. Findings

1. **Exact, but supplied.** The instrument meets the identities, the Born values and closure exactly at the register
   level; under the fixed rule, the single read's transport and re-preparation registers at tick 2 are native. The
   native dynamics only transports and XORs. The following are supplied:
   - the product preparation law;
   - three fresh biased bits per read, with entropy deficits of 0.531, 0.278, 0 and 0.809 bits for X, Y, Z and R;
   - an ideal herald;
   - the tick;
   - the access stipulation.

   This is a classical hidden-register model fitted to the finite menu and run on the lattice. It is not a
   derivation of quantum statistics.
2. **New: non-dyadic Born values need a non-subspace event.** Exact R-menu probabilities cannot come from affine
   readiness events under uniform counting. The threshold sampler here has a joint acceptance flag of degree 12 in
   its fair bits; any exact sampler needs degree at least 2, and lower-degree flags suffice, for example
   1 ⊕ x₀x₁ ⊕ x₂x₃ per component (`review/REVIEW.md`). No flag was built natively here. The composition builder (`design/composition/`) supplies conjunctions
   of any degree under the same rule. Whether that gives a native acceptance flag, and at what readiness cost, is
   untested.
3. **Access decides the identities and closure in the examples tested.** For this instrument and layout, they hold
   or fail according to which registers are accessible. Native
   records stay clean only through geometry and a bounded horizon: reading the record site 8 ticks later exposes
   unread components. A finite menu's identities can miss a real dependence, as the R case in Q6(c) shows.
4. **Not constructed:** native reuse (routing the outgoing registers into a second device), native preparation of
   the readiness, a clock, and any reason the dynamics would select Born values.

## 4. Relation to the checklist (`CONDITIONS.md`)

- **Entry 2 (freshness):** fresh biased bits are supplied, and exposing them breaks closure given the record
  (Q6(b)).
- **Entry 3 (preparation):** the instrument names its rejection resource and its readiness, and both are paid for.
- **Entry 4 (heralding):** the herald's acceptance is equal for every station, and C-HER shows what a station-
  dependent herald does.

No requirement, obstruction or sufficient method in the checklist changes. Finding 3 restates its access
condition with an exact example.
