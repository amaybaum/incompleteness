# Necessary conditions for a native construction: research checklist

> **DRAFT — research checklist.** It collects the constraints that the owner-check reports have established or
> proposed for a native OI construction of quantum behaviour. Each entry states its requirement, exact scope,
> supporting reports, status and what a successor construction must demonstrate. Status is one of:
>
> - **proved** — a proof is on record;
> - **independently reviewed** — the coordinator has replayed the proof's checker and run independent checks;
> - **proposed** — a stated requirement or observation not yet proved or reviewed.
>
> None of these is an OI premise. Whether OI implies a condition, or the condition is an additional assumption, is
> open for every entry.

The reports are in `owner-checks/`.

## 1. Logic: bounded-degree conjugacy limits computation

- **Requirement.** A rule that must compute functions of algebraic degree d must not be conjugate to a linear rule by
  a pointwise bijection G with deg(G)·deg(G⁻¹) < d.
- **Exact scope.**
  - The basic fact: if F = G⁻¹ L G with L linear, deg G = g and deg G⁻¹ = g′, then every raw output bit of F^t has
    degree at most g·g′ at every tick.
  - That limits functions written into a single raw register at a predetermined deadline. It assumes input-independent
    prepared resources, affine input encoding and affine readout.
  - For the repaired three-field rule, and every member of its 16-predicate family, the bound is 2. Exact zero
    detection of J ≥ 3 freely varying bits is then impossible, and with input-independent randomized resources some
    input errs with probability at least 1/8.
  - The bound does not exclude any of the following:
    - restricted input domains;
    - distributed records read by an explicit decoder, which then performs the computation and must be counted;
    - nonlinear input encodings;
    - rules outside the class.
- **Supporting reports.** report17 (obstruction for the repaired rule; F1–F4); report18 (a rule outside the class:
  degree 3 attained by a two-stage AND, and finite evidence of degree growing to 10 with 10 variables).
- **Status.**
  - The obstruction for the repaired rule is proved and independently reviewed.
  - The general g·g′ bound is proved by polynomial composition, and the owner reviewed it in report18.
  - That the report18 rule has no bounded-degree conjugacy is proposed, on finite evidence only.
- **A successor must demonstrate** the degree its detector functions need. It must either show that its rule
  reaches that degree under the stated encoding, readout and resource restrictions, or state the decoder or
  encoding that supplies the missing degree.

## 2. Freshness: conditional on the complete accessible record

- **Requirement.** Source symbols must be uniform and independent conditional on the complete accessible preparation,
  waiting and stopping record, including every detector, clock and side record. They must also be independent of the
  marks the downstream test uses.
- **Exact scope.**
  - A sufficient mechanism is a set of reserved initial coordinates satisfying three conditions:
    - for each start w, they are fair and independent of everything else;
    - the event W = w and every record before the start depend only on the other coordinates;
    - given those other coordinates, the source word is a bijective function of the reserved coordinates.
  - Linearity is not necessary.
    - For linear waves, the frontier argument and rank calculations supply the bijection (report15, report16).
    - For a rule U′ = H(SU) ⊕ U_old with H a bijection, local permutivity along the unique extreme path supplies it
      (report18).
  - Leaving reserved bits unchanged is not enough. A copy into a visible register leaves a bit fair but no longer
    fresh (report17).
  - Freshness given past records does not imply independence from a same-tick herald. Selecting on the current
    detector bit biases the marks (report15, joint-readiness handoff).
- **Supporting reports.**
  - report15: fixed-start freshness, which also holds on random backgrounds.
  - report16: the stopping-time law, ideal readiness flags and a waiting cap.
  - report17: the prepared-prior lemma and the copy countercontrol.
  - report18: the permutive-frontier lemma and a non-bijective countercontrol.
- **Status.** Proved and independently reviewed for the stated constructions and records.
- **A successor must demonstrate** that every record its native readiness flag, clock and detector produce depends
  only on unreserved coordinates on each branch, and that the output map stays bijective in the reserved ones. Any
  record that reveals a reserved coordinate breaks the proof.

## 3. Preparation: resources, waiting and workspace

- **Requirement.** Ready events must be paid for in the resource budget.
- **Exact scope.**
  - **Entropy.** For an event E of codimension J, readiness with probability at least 1 − δ at a predetermined tick
    requires an initial entropy deficit of at least (1 − δ)J − h₂(δ) − δ·log₂(1 − 2^−J). This bound concerns
    information resources; reading it as heat needs thermodynamic assumptions that have not been supplied.
  - **Waiting.** Waiting can select ready runs, but under uniform counting success by deadline B has probability at
    most (B + 1)·2^−J.
    - The Kac return mean is not the mean first-hit time from a uniform start.
    - In the three-field rule some states never become ready, so the unconditional mean first-hit time is infinite.
  - **Workspace (proposed).**
    - A native detector carries its own clean-workspace and reset requirement, which belongs in the same budget.
    - In report18 the gate evaluates 3 inputs on a 99-bit readiness event.
    - Detection is worth building only if its total clean resources cost less than preparing the event directly.
- **Supporting reports.** report16 (entropy bound, deadline bound, first hit against return; S3, S4); report18
  (finding 4, workspace).
- **Status.** The entropy and deadline bounds are proved and independently reviewed. The workspace accounting is
  proposed.
- **A successor must demonstrate** its initial resource state, the state's entropy deficit, and the detector's
  workspace and reset cost. It must also give the joint law of readiness, waiting time, failures and the subsequent
  source symbols.

## 4. Heralding: herald records must respect preparation equivalence

- **Requirement.** Operationally equivalent preparation mixtures must produce identical laws for the complete herald
  record: attempts, failures, timestamps and reads. For an approximate claim, their distance must fit the stated
  error budget.
- **Exact scope.**
  - **Equal per-attempt success rates at every station** make the attempt-count record the same for every
    preparation. That is sufficient for that marginal, but not for the full record: with equal heralds the fourth
    record identity still fails through the timestamps and reads (report13; time-blind TV 0.00064).
  - **A success rate affine in the station's state** does not cause the attempt-count marginal to violate
    equivalence, provided the station is redrawn independently at every attempt.
  - **It is not sufficient when a run keeps one station across repeated attempts.** The waiting law is then a
    nonlinear function of the rate. Exact example: take success rate 1/2 + x/10 for Bloch component x. The
    mixtures ½Z⁺ + ½Z⁻ and ½X⁺ + ½X⁻ give P(fail, then succeed) = 6/25 and 1/4 respectively. This example is the
    coordinator's and is not separately reviewed.
  - **Failures established:**
    - report12: the attempt count leaks the preparation at finite n;
    - report13: the fourth record identity fails;
    - report14: the exact clock gives a witness for every frame.

    These hold for the station laws tested.
- **Supporting reports.** report12 (finding 2, attempt-count leak), report13 (four record identities and completeness),
  report14 (all-frame witness).
- **Status.**
  - The failures for the tested station laws are proved and independently reviewed.
  - The requirement as stated is proposed: it is the operational definition the four identities test.
- **A successor must demonstrate** that the complete herald-record law, as a function of the station, satisfies every
  linear relation the station states satisfy: the four record identities on the current menu. Alternatively it must
  bound the violation within its error budget, under its actual attempt and mixing protocol.

## Boundary

- **Two claims kept apart.**
  - C-SPH-1 established a bounded result under supplied resources, including a continuum reservoir and a
    real-valued clock.
  - Equivalence with native preparation is open.
- **The four-identity test.** The native constructions, recorded in report15 to report18, define no station-indexed
  quantum preparations, so they have not reached the four-identity test.
- **Separate obligations.** Angular-law selection, composites and Yang–Mills dynamics are each separate open
  obligations.
