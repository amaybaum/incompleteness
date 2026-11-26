# HZM-ENERGY-SOURCING, unit C (lane 3): preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it.

Evidence layers of the results:
- source reading at the pin, reproducible by the commands of `REPORT-r3.md` §2;
- mathematical derivation on paper, labelled [A] and [W] in the report.

No computation was run, and no Lean was built.

## 1. The record preserved

- **Authoritative report:** `REPORT-r3.md` (revision r3), committed with this record.
- **Superseded versions,** kept unchanged:
  - `REPORT.md` (r1, commit `266fbc60ea94dcabbc1f65a405f2b8c9863a82b1`);
  - `REPORT-r2.md` (r2, commit `04248fc9dbb9dcb2e4e865aec250bffbeb2fc67a`).
- **Change maps:**
  - `CHANGES-r2.md` maps each r1-to-r2 change to its review finding.
  - r3 applies only the three wording corrections N1–N3 of the delta review and the optional D-1
    mention of Main:306–312. Its header records this.
- **Plan:** `PLAN.md` (commit `d4f97b5387fe448baeebe3ebd2caae41da89f259`) fixes the targets, search
  protocol, decision rule, controls, productivity test and stopping rule before any search result.
  It is not superseded.
- **Correction N1 changes a scientific statement**, and r3 states the corrected result. Reason (2)
  of the Main:262 row reads, in r3: "The restriction of σ_c (or τ_c) to the visible sites of a
  proper region is not a symmetry of F [A]". r2's broader wording, "A visible-internal version does
  not exist", is not the preserved result.
- **Header status.** The header of `REPORT-r3.md` records its status before acceptance. Review and
  acceptance are recorded here.
- **Accountable Issues:** #1217 and #1049 (programme #1169). Guiding pull request: #1594.
- **Owner decisions** (each a #1169 comment posted from the account `amaybaum`, quoting the owner):
  - **Comment 7189139613** (created 2026-11-26T10:16:17Z; decision received 2026-11-26T10:16Z),
    item 2. It authorizes the unit with the row "| 3 | Physical sourcing of H-ZM and SM:811 energy
    (#1217, #1049) | Determine whether existing premises already supply these conditions. |" and
    the criterion "Lane 3: Either derive the required conditions from existing premises or
    establish exactly what remains unsourced. Failure to find a source must not be presented as
    proof that none can exist." It also says "Do not authorize computation or adopt additional
    premises through the new research units."
  - **Comment 7190274734** (created 2026-11-26T11:06:26Z; decision received 2026-11-26T11:06Z),
    item 1. It says "Approve final acceptance and preservation of units A, B and C, at their
    independently reviewed revisions, under §A.46 item 8." For unit C: "Accepted | Apply the three
    wording corrections." And: "Where a correction changes a scientific statement, ensure that the
    authoritative preserved record states the corrected result unambiguously rather than leaving a
    misleading assertion in place."
- **Independent non-author reviews.** These are model reviews by a Claude reviewer agent. They are
  evidence of review, not independent mathematical verification.
  - **PR #1594 comment 7190048646,** review of r1 at `266fbc60`: **REVISE**, findings 1–14. It
    re-derived U1–U3, F-stag, §5.2 and F-slice (a)–(d), reproduced every sweep count, and
    re-extracted every quote.
  - **PR #1594 comment 7190223659,** focused delta review of r2 at `04248fc9`: **ACCEPT WITH
    NITS**, nits N1–N3. It confirms findings 1–14 resolved and reproduces widening W-1. It ran its
    own screen of Main §3.1, §3.2 and §3.4 with a different vocabulary; that screen returned only
    Main:306–312, which is not a candidate. The delta review was written by the reviewer agent that
    wrote the r1 review, resumed. All review evidence for this record therefore comes from a single
    model reviewer, and r3's three corrections were not separately reviewed.

## 2. Substantive results and their precise scope

All results are at the pin `353a066f18766837fed8c7f58507e09ff549b1a4`. Every negative statement
is **within the searched scope** of `REPORT-r3.md` §1–§2. None states impossibility, and none is
evidence that no premise could supply the condition (owner criterion, §1).

- **T1a, the constant static shift.**
  - **At the substratum interface:** contradicted for the partitions Main specifies. These are site
    factorization (ledger (viii), Main:368), the visible sector as the sites of a region (Main:298)
    and readout regions (Main:376), with Main §1.4 indexing the visible process by their
    configurations (Main:84–89).
  - **For the observer of SM §4.1:** contradicted conditional on the register transferring through
    the SM:232 bridge (open, O2); otherwise unsourced within the searched scope.
  - **Partially sourced, conditional on open alternatives:** the shift-invariant interface 𝒜_C (a
    research record, not a stated interface), or a physical status for the amplitude-scale gauge's
    translation clause. That clause is "proposed" at SM:96, with status open at Substratum:272.
  - **Individual invariant readouts,** which are not the complete register: the SM §6.5
    link-difference map, E and its shells at α = 1/d, and the uniform counting measure.
- **T1b.** Unsourced within the searched scope. It coincides with T1a for itinerary registers
  ([W], kernel mechanism PassiveQuotient/ObservabilityQuotient), given that the shift normalizes F.
- **T2a, T2b, the staggered static shift.**
  - T2a has the same two-level form as T1a.
  - Unsourced within the searched scope, even conditionally. τ_c⁻¹ ∘ F ∘ τ_c = F − 2cv [A], so τ_c
    is not a symmetry of F. It is not an alphabet relabelling and not in 𝒜_C.
- **T1Z, T2Z (secondary).** Unsourced within the searched scope.
- **Main:262** (symmetry-to-gauge criterion). It does not supply T1a or T2a. Reason (2) as
  corrected: the restriction of σ_c (or τ_c) to the visible sites of a proper region is not a
  symmetry of F [A].
- **T3, linear lift: "defined".**
  - The text defines E, the "total energy" (SM:292–296).
  - The T3b positive-definiteness requirement fails on the full phase space at α = 1/d. By
    Proposition U1 [A], no conserved function with compact sublevel sets exists there, for any b.
  - The requirement holds only on invariant constraint slices, which the text requires and does not
    specify.
  - The selecting condition is named: which conserved labels the observer's records fix (Main
    ledger (iv)).
- **T3, affine lift at resonance, b ≠ 0: "unspecified".**
  - The text does not treat this case.
  - By U2 [A], no conserved function meets the requirement.
  - By U3 [A], Q′ = E_⊥ + Q′_0 with Q′_0 a function of the uniform variables. So the choice among
    Q′, E_⊥ and E_⊥ + f(Q′_0) is a choice of uniform-sector treatment.
  - No stated premise within the searched scope selects one.
- **F-stag [A].** At α = 1/d with L even, E_⊥ is only semidefinite on the staggered null direction.
  Lane 1 REPORT-r2 line 297 holds for odd L, or with the staggered labels fixed.
- **D5 (#1049).** Lane 1's class-(c) placement does not depend on reading the energy as Q′. The E_⊥
  branch rests on an unstated interface choice together with a staggered-label treatment.
- **F-slice.** On T at α = 1/d with b = 0, under stationarity with finite second moments, an
  alternative to the H-ZM quotient exists that yields a unique J on every label sector.
  - It is conditional on lane 2's Theorem 1, a model-written record.
  - Step (c) is [W].
  - Whether it serves the consumers of lane 2's Proposition 5 (Theorem 5's Σ, H-PF) is open (O3).
  - It does not show that H-ZM is unnecessary for Theorem 5.
- **Productivity:** gem. U1 is modestly NEW; U3, F-stag and the conditioned F-slice are NEW;
  §4.1, §4.3 and §5.2 are ELABORATING; U2 is CONFIRMING. The stopping rule applied is (c): a
  partial state.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Every result is a paper derivation or source reading checked by the model reviews of §1. The
remediation plan below authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| T1a/T2a two-level verdict, T1b/T2b, T1Z/T2Z | REPORT-r3 §4–§6 | partially verified: source reading and hand algebra, model-reviewed | independent non-model review; the unswept remainders D-1 to D-8 | #1217 | a recorded independent review; a recorded sweep of the remainders |
| Register transfer to the SM §4.1 observer (O2) | §4.1, §11 | open | a derivation, from stated premises, of the register of the SM §4.1 observer | #1217 | a written derivation, or an owner decision on the interface premise |
| Main:262 row, reason (2) as corrected | §3 | partially verified; the r3 wording was not separately reviewed | independent review | #1217 | a recorded independent review |
| U1, U2, U3 | §7.2–§7.3 | partially verified: re-derived by the model review | independent non-model review; an exact finite control | #1049 | a recorded review, or an exact control run under authorization |
| F-stag | §7.4 | partially verified, as above | independent review | #1049 | a recorded independent review |
| F-slice (a)–(d) | §5.3 | partially verified; step (c) [W]; conditional on lane 2 Theorem 1; consumer question open (O3) | independent review; verification of lane 2 Theorem 1; a written answer to O3 | #1217 | a recorded review; verification of lane 2 Theorem 1; a derivation or counterexample for O3 |
| Sweep counts | §2 | reproduced by the model review with the stated commands | none beyond the remainders | #1217, #1049 | — |
| Unswept remainders D-1 to D-8 | §1 | not swept | **D-1:** the rest of Main §3.1, §3.2 and §3.4 word for word, SM:312–344, SM:360–374, and the remainder of Structure, GR, Introduction and Methodology. **D-2:** the Group N remainder in verification records. **D-3:** \pi and quotient below snippet level in papers and book. **D-4:** the Group B remainder in papers and book (W-1 covers gauge). **D-5:** the Lean high-volume hits. **D-6:** POSIT-MIN, Q3, Q4, BRIDGE-UNIT1. **D-7:** the grep mode recorded (fixed-string, not the planned `-E`). **D-8:** the 95 non-`.lean` files under the Lean directories and the 147 non-`.md`, non-`.tex`, non-`.pdf` files under papers/ | #1217, #1049 | a recorded sweep under the same decision rule; until then every verdict stays scoped |
| Preregistration order (PLAN.md before any result) | `PLAN.md` | evidence is commit order only: `d4f97b53` at 10:32:19Z, `266fbc60` at 10:48:01Z, `04248fc9` at 11:02:16Z (2026-11-26) | none available from commit order alone | #1217, #1049 | none; the limitation stands as stated |
| Open nodes O1–O6 | §11 | open; not adopted | derivation, refutation or owner decision | O1: proposed #1049 (§7); O2, O3, O6: #1217; O4: #1217; O5: #1217, #1049 | a written derivation, a counterexample or an owner decision |

## 4. Off-`main` references (§A.42 item 8)

Each reference is classified by reading the claim it is attached to.

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7189139613, 7190274734 (owner decisions) | `PLAN.md`, report headers; §1 here | provenance: authority records quoted with author and time; no result uses them |
| #1169 comment 7189143747 (synthesis) | `PLAN.md` §1 | provenance |
| #1049 comment 6624263637 (owner decisions Q1, Q2) | report §4.1, §12 | provenance: governance record, quoted. No scientific claim uses it: the substratum-interface contradiction rests on Main:84–89, Main:298, Main:368, Main:376 and SubstratumInterfaceAudit on `main`. Q1 and Q2 are also quoted on `main` at A5-LINEAR-AFFINE:601 and :608, and Q2 at A5-Q4-STAGE2D:39–42 |
| PR #1594 comments 7190048646, 7190223659 (reviews) | report headers; §1 here | provenance: evidence of review; no result uses them |
| commits `266fbc60` (r1) and `04248fc9` (r2), superseded | report headers | provenance for every result: cited only to identify the earlier texts. `266fbc60` is also support on `main` for the preregistration-order row (§3), through its commit time, once the merge of §5 lands; not before |
| commit `d4f97b53` (PLAN.md), the commit adding `REPORT-r3.md`, and the commit adding this file | report headers; §1 here | support on `main` once the merge of §5 lands: the record's own content; not before |
| pin `353a066f` and every file:line citation | throughout | support on `main`: the pin is `main` at the time of writing |
| lane 1 and lane 2 records (`qbeta-trace-20261126`, `complex-carrier-20261126`) | throughout | support on `main`: on `main` at the pin and used as pointers. Lane 2 Theorem 1 is used as a premise of F-slice (d) and carried as a condition of that result |
| #1217, #1049, #1169, #1211 | headers | provenance: accountability |

Support off `main`: none.

## 5. Landing condition

The record is preserved only through a **merge commit, not a squash**. The merge keeps the
following reachable from `main`:
- `d4f97b53`, `266fbc60` and `04248fc9`;
- the commit adding `REPORT-r3.md`;
- the commit adding this file.

That `PLAN.md`'s commit precedes every report commit is part of the record's provenance. Per the
owner decision of 2026-11-26T11:06Z, preservation includes the accuracy checks, integration with
current `main` and exact-head CI. Merging needs the owner's separate approval (§A.50 item 1).

## 6. Preservation rationale

The unit answers the owner's question for lane 3: whether existing premises supply H-ZM and the
SM:811 energy. It does so with a preregistered protocol, controls that are all green, and every
negative scoped to its searched scope.

It establishes:
- the two-level status of H-ZM for both static modes: contradicted at Main's specified partitions,
  and only conditionally sourced for the constant mode;
- that SM:292's positive-definite shell cannot exist on the full phase space at the normalized
  branch (U1);
- that the choice among Q′, E_⊥ and E_⊥ + f(Q′_0) reduces to a uniform-sector treatment (U3), which
  decides how #1049's D5 placement rests on the manuscript;
- a correction of scope to lane 1's confinement statement (F-stag);
- a conditioned alternative to the H-ZM quotient (F-slice). The owner has named it as a successor
  question: "F-slice: Can it eliminate the need for H-ZM in Theorem 5?" (#1169 comment 7190274734,
  item 4).

It is substantive, nonredundant with lanes 1 and 2, and independently reviewed. Its open gaps carry
the remediation plans of §3.

## 7. Proposed accountable Issue for O1 (a proposal for the owner)

O1 has two parts:
- the physical status of the amplitude-scale gauge's translation clause;
- the wording variance between SM:96 ("affine relabellings", translations included) and SM:811
  ("additive-automorphism group", which strictly excludes translations).

The variance is immaterial for SM:811's link-difference map. It is a manuscript-consistency defect
(§A.47 item 4). This record **proposes #1049** as its accountable Issue, because the owner's
decision Q2 on the amplitude-scale gauge is recorded there. This is a proposal only: the owner may
name another Issue or open a new one. It authorizes no manuscript edit.
