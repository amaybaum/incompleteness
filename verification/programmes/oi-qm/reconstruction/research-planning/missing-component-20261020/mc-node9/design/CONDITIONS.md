# Conditions for a native construction: research checklist

> **DRAFT — research checklist.** It collects the constraints that the owner-check reports have established or
> proposed for a native OI construction of quantum behaviour. Each entry gives its requirement, exact scope,
> supporting reports, status and what a successor construction must demonstrate.
>
> Each entry keeps three kinds of statement apart:
> - **operational requirements**, which any construction must meet;
> - **obstructions proved for specified rule classes**;
> - **sufficient construction methods**, which the current candidates use.
>
> A sufficient method is not a requirement. None of the three is an OI premise, and for every entry it is open
> whether OI implies the condition or the condition is an additional assumption.
>
> Status is one of:
> - **proved** — a proof is on record;
> - **independently reviewed** — the coordinator has replayed the proof's checker and run independent checks;
> - **proposed** — a stated requirement or observation not yet proved or reviewed.

The reports are in `owner-checks/`.

## 1. Logic: bounded-degree conjugacy limits computation

- **Requirement (from a proved obstruction).** Suppose a rule must write a function of algebraic degree d into a
  single raw register, under the restrictions below. Then it must not be conjugate to a linear rule by a pointwise
  bijection G with deg(G)·deg(G⁻¹) < d.
- **Exact scope.**
  - **The basic fact.** If F = G⁻¹ L G with L linear, deg G = g and deg G⁻¹ = g′, then every raw output bit of F^t
    has degree at most g·g′ at every tick.
  - **What it limits.** Functions written into a single raw register at a predetermined deadline, assuming:
    - prepared resources that do not depend on the input;
    - affine input encoding;
    - affine readout.
  - **The repaired rule.** For the repaired three-field rule, and every member of its 16-predicate family, the bound
    is 2. Exact zero detection of J ≥ 3 freely varying bits is then impossible. With randomized resources that do not
    depend on the input, some input errs with probability at least 1/8.
  - **What the bound does not exclude:**
    - restricted input domains;
    - distributed records read by an explicit decoder, which then performs the computation and must be counted;
    - nonlinear input encodings;
    - rules with no conjugacy of the stated degree.
- **Supporting reports.**
  - report17: the obstruction for the repaired rule (F1–F4).
  - report18: a rule beyond the previous degree-2 bound. A two-stage AND attains degree 3, and output degree reaches
    10 with 10 free variables.
  - report20: the composition builder (`design/composition/`) writes raw ANDₙ for every n ≥ 2 under the report18
    rule, with affine readiness resources. It was independently reviewed for n = 2–13.
- **Status.**
  - The obstruction for the repaired rule is proved and independently reviewed.
  - The general g·g′ bound is proved by polynomial composition; the owner reviewed it in report18.
  - For the report18 rule, ANDₙ of degree n for every n excludes any conjugacy to linear dynamics with forward and
    inverse degrees bounded uniformly in lattice size and time. This is proved and independently reviewed (report20).
    It does not exclude size-dependent degree bounds or representations outside the stated conjugacy class.
- **A successor must demonstrate** the degree its detector functions need. Either its rule reaches that degree under
  the stated encoding, readout and resource restrictions, or it must name the decoder or encoding that supplies the
  missing degree.

## 2. Freshness: conditional on the complete accessible record

- **Requirement (operational).** The source resource must have the law that the downstream record law requires,
  conditional on the complete accessible record. That record covers preparation, waiting and stopping, including
  every detector, clock and side record. The source must also be independent of the marks the downstream test uses.
  The current candidates' resource contract is uniform independent source symbols. An alternative construction could
  use different resources, provided it reproduces the required complete-record law.
- **Exact scope.**
  - **A sufficient method (not the only possible proof):** reserved initial coordinates that meet three conditions:
    - for each start w, they are fair and independent of everything else;
    - the event W = w and every record before the start depend only on the other coordinates;
    - given those other coordinates, the source word is a bijective function of the reserved coordinates.
  - **Linearity is not needed for that method.**
    - For linear waves, the frontier argument and rank calculations supply the bijection (report15, report16).
    - For a rule U′ = H(SU) ⊕ U_old with H a bijection, local permutivity along the unique extreme path supplies it
      (report18).
  - **Leaving reserved bits unchanged is not enough.** A copy into a visible register leaves a bit fair but no longer
    fresh (report17).
  - **Same-tick heralds.** Freshness given past records does not imply independence from a same-tick herald.
    Selecting on the current detector bit biases the marks (report15, joint-readiness handoff).
- **Supporting reports.**
  - report15: fixed-start freshness, which also holds on random backgrounds.
  - report16: the stopping-time law, with ideal readiness flags and a waiting cap.
  - report17: the prepared-prior lemma and the copy countercontrol.
  - report18: the permutive-frontier lemma and a non-bijective countercontrol.
- **Status.** The method is proved and independently reviewed for the stated constructions and records.
- **A successor must demonstrate** the required source law conditional on its complete accessible record, by this
  method or another. If it uses this method, it must show two things on each branch:
  - every record its native readiness flag, clock and detector produce depends only on unreserved coordinates;
  - the output map stays bijective in the reserved ones.

  Any record that reveals a reserved coordinate breaks this proof.

## 3. Preparation: resources, waiting and workspace

- **Requirement (operational).** Ready events, and any detector used to recognize them, must be paid for in an
  explicit resource budget.
- **Exact scope.**
  - **Entropy.** For an event E of codimension J, readiness with probability at least 1 − δ at a predetermined tick
    requires an initial entropy deficit of at least (1 − δ)J − h₂(δ) − δ·log₂(1 − 2^−J). This is a bound on
    information resources; reading it as heat needs thermodynamic assumptions that have not been supplied.
  - **Waiting.** Waiting can select ready runs, but under uniform counting success by deadline B has probability at
    most (B + 1)·2^−J.
    - The Kac return mean is not the mean first-hit time from a uniform start.
    - In the three-field rule some states never become ready, so the unconditional mean first-hit time is infinite.
  - **Detector accounting (proposed).**
    - A detector's initialization, the information it retains, and any restoration needed for reuse must be stated
      and counted. A one-shot detector need not implement a reset.
    - In report18 the gate evaluates 3 inputs on a 99-bit readiness event: 93 fixed bits in the receiver region and 6
      at the source port, with the three payload coordinates free.
- **Supporting reports.**
  - report16: the entropy bound, the deadline bound, and first hit against return (S3, S4).
  - report18: finding 4, workspace accounting.
- **Status.** The entropy and deadline bounds are proved and independently reviewed. The detector accounting is
  proposed.
- **A successor must demonstrate:**
  - its initial resource state and that state's entropy deficit;
  - its detector's initialization, retained information and any restoration for reuse;
  - the joint law of readiness, waiting time, failures and the subsequent source symbols.

## 4. Heralding: herald records must respect preparation equivalence

- **Requirement (operational).** Operationally equivalent preparation mixtures must produce identical laws for the
  complete herald record: attempts, failures, timestamps and reads. For an approximate claim, their distance must fit
  the stated error budget.
- **Exact scope.**
  - **Equal per-station success rates.** If attempts are conditionally independent Bernoulli trials with those rates,
    equal rates give equal attempt-count laws.
    - Equal marginal rates alone do not suffice, because correlations between attempts can differ.
    - Equal rates also say nothing about the rest of the record. With equal heralds, the fourth record identity
      still fails through the timestamps and reads (report13; time-blind TV 0.00064).
  - **Persistent stations (sufficient methods are not universal).** A success rate affine in the station's state does
    not suffice when a run keeps one station across repeated attempts. The waiting law is then a nonlinear function
    of the rate.
    - Exact example: take success rate p = 1/2 + x/10, where x is the station's X Bloch component.
    - The X-mixture ½X⁺ + ½X⁻ gives P(fail, then succeed) = 6/25. The Z-mixture ½Z⁺ + ½Z⁻ gives 1/4.
    - Both have first-attempt success probability 1/2. The second attempt exposes their different second moments of
      p, a gap of 1/100.
    - Redrawing the station independently at every attempt is one sufficient repair for this example. It is not a
      universal requirement.
  - **Failures established for the station laws tested:**
    - report12: the attempt count leaks the preparation at finite n;
    - report13: the fourth record identity fails;
    - report14: the exact clock gives a witness for every frame.
- **Supporting reports.**
  - report12: finding 2, the attempt-count leak.
  - report13: the four record identities and their completeness.
  - report14: the all-frame witness.
- **Status.**
  - The failures for the tested station laws are proved and independently reviewed.
  - The persistent-station example is exact arithmetic, and the owner checked it.
  - The requirement as stated is proposed: it is the operational definition the four identities test.
- **A successor must demonstrate**, under its actual attempt and mixing protocol, that the complete herald-record law
  as a function of the station satisfies every linear relation the station states satisfy. On the current menu
  those are the four record identities. Otherwise it must bound the violation within its error budget.

## Boundary

- **Two claims kept apart.**
  - C-SPH-1 established a bounded result under supplied resources, including a continuum reservoir and a
    real-valued clock.
  - Equivalence with native preparation is open.
- **The four-identity test.** The native constructions recorded in report15 to report18 define no station-indexed
  quantum preparations, so they have not reached the four-identity test.
- **Separate obligations.** Angular-law selection, composites and Yang–Mills dynamics each remain separate open
  obligations.
