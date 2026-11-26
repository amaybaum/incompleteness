# HZM-ENERGY-SOURCING, unit C (lane 3): preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it.

- **Evidence layers of the results:** source reading at the pin, reproducible by the commands of
  `REPORT-r3.md` §2, and mathematical derivation on paper, labelled [A] and [W] in the report.
- **No computation was run, and no Lean was built.**

## 1. The record preserved

**Authoritative report:** `REPORT-r3.md` (revision r3), as added in the commit that adds the
rebuilt r3 text. r3 is `REPORT-r2.md` with only these edits:
- the title;
- a revision note;
- the three wording corrections N1–N3 of the delta review of r2;
- the mention of Main:306–312 in D-1.

Every other line is byte-identical to `REPORT-r2.md`. The corrections are located as follows:
- **N1:** §3, Main:262 row, reason (2).
- **N2:** §1, W-1, which files GR:372 with the energy-offset near misses.
- **N3:** §1, D-8, which says "read the narrow-term hits it checked".

**An earlier, condensed text of `REPORT-r3.md`, at `d5b119f9`.** It condensed r2 well beyond
these edits. The accuracy check found this, and that text is superseded by the rebuilt r3.

**Superseded versions,** kept unchanged:
- `REPORT.md` (r1, commit `266fbc60ea94dcabbc1f65a405f2b8c9863a82b1`);
- `REPORT-r2.md` (r2, commit `04248fc9dbb9dcb2e4e865aec250bffbeb2fc67a`).

**Change maps.** `CHANGES-r2.md` maps each r1-to-r2 change to its review finding. r3's own
revision note lists its edits.

**Plan.** `PLAN.md` (commit `d4f97b5387fe448baeebe3ebd2caae41da89f259`) fixes the targets, search
protocol, decision rule, controls, productivity test and stopping rule before any search result.
It is not superseded.

**Correction N1 changes a scientific statement, and r3 states the corrected result.**
- r3 reads: "The restriction of σ_c (or τ_c) to the visible sites of a proper region is not a
  symmetry of F [A]".
- r2's broader wording, "A visible-internal version does not exist", is not the preserved result.

**Status in the header.** The header of `REPORT-r3.md` records the report's status before
acceptance. Review and acceptance are recorded here.

**Accountable Issues:** #1217 and #1049 (programme #1169). Guiding pull request: #1594.

**Owner decisions.** Each is a #1169 comment posted from the account `amaybaum`, quoting the
owner:
- **Comment 7189139613** (created 2026-11-26T10:16:17Z; decision received 2026-11-26T10:16Z),
  item 2, authorizes the unit. Its row reads "| 3 | Physical sourcing of H-ZM and SM:811 energy
  (#1217, #1049) | Determine whether existing premises already supply these conditions. |". Its
  criterion reads "Lane 3: Either derive the required conditions from existing premises or
  establish exactly what remains unsourced. Failure to find a source must not be presented as proof
  that none can exist." It also says "Do not authorize computation or adopt additional premises
  through the new research units."
- **Comment 7190274734** (created 2026-11-26T11:06:26Z; decision received 2026-11-26T11:06Z),
  item 1:
  - "Approve final acceptance and preservation of units A, B and C, at their independently
    reviewed revisions, under §A.46 item 8."
  - For unit C: "Accepted | Apply the three wording corrections."
  - "Where a correction changes a scientific statement, ensure that the authoritative preserved
    record states the corrected result unambiguously rather than leaving a misleading assertion in
    place."

**Independent non-author reviews.** These are model reviews by a Claude reviewer agent: evidence of
review, not independent mathematical verification.
- **PR #1594 comment 7190048646, review of r1 at `266fbc60`: REVISE,** findings 1–14. It
  re-derived U1–U3, F-stag, §5.2 and F-slice (a)–(d), reproduced every sweep count and re-extracted
  every quote.
- **PR #1594 comment 7190223659, focused delta review of r2 at `04248fc9`: ACCEPT WITH NITS,**
  nits N1–N3.
  - It confirms findings 1–14 resolved.
  - It reproduces widening W-1.
  - It ran its own screen of Main §3.1, §3.2 and §3.4, which returned only Main:306–312, not a
    candidate.
- **PR #1594 comment 7190487175, accuracy check at `d5b119f9`: REVISE,** on the accuracy of the
  record, not of the science.
  - It found the condensed r3 described inaccurately, and a fourth class in the off-`main` trace.
  - It confirmed N1–N3, the Main:306–312 mention and the scientific statements of this record as
    accurate.
- **All three reviews are by one reviewer agent, resumed.** All review evidence for this record
  therefore comes from a single model reviewer.

## 2. Substantive results and their precise scope

All results are at the pin `353a066f18766837fed8c7f58507e09ff549b1a4`. Every negative statement is
**within the searched scope** of `REPORT-r3.md` §1–§2. None states impossibility, and none is
evidence that no premise could supply the condition (owner criterion, §1).

**T1a, the constant static shift.**
- **At the substratum interface:** contradicted for the partitions Main specifies. These are site
  factorization (ledger (viii), Main:368), the visible sector as the sites of a region (Main:298)
  and readout regions (Main:376), with Main §1.4 indexing the visible process by their
  configurations (Main:84–89).
- **For the observer of SM §4.1:** contradicted conditional on the register transferring through
  the SM:232 bridge (open, O2); otherwise unsourced within the searched scope.
- **Partially sourced, conditional on open alternatives:** the shift-invariant interface 𝒜_C (a
  research record, not a stated interface), or a physical status for the translation clause of the
  amplitude-scale gauge ("proposed" at SM:96, status open at Substratum:272).
- **Individual invariant readouts:** the SM §6.5 link-difference map, E and its shells at α = 1/d,
  and the uniform counting measure. These are not the complete register.

**T1b.** Unsourced within the searched scope. It coincides with T1a for itinerary registers ([W];
kernel mechanism PassiveQuotient/ObservabilityQuotient), given that the shift normalizes F.

**T2a and T2b, the staggered static shift.**
- T2a has the same two-level form as T1a.
- Both are unsourced within the searched scope, even conditionally.
- The reason: τ_c⁻¹ ∘ F ∘ τ_c (x) = Fx − 2cv [A], so τ_c is not a symmetry of F. It is not an
  alphabet relabelling, and it is not in 𝒜_C.

**T1Z and T2Z (secondary).** Unsourced within the searched scope.

**Main:262** (symmetry-to-gauge criterion). It does not supply T1a or T2a. Reason (2) as
corrected: the restriction of σ_c (or τ_c) to the visible sites of a proper region is not a
symmetry of F [A].

**T3, linear lift: "defined".**
- The text defines E, the "total energy" (SM:292–296).
- The T3b positive-definiteness requirement fails on the full phase space at α = 1/d. By
  Proposition U1 [A], no conserved function with compact sublevel sets exists there, for any b.
- The requirement holds only on invariant constraint slices, which the text requires and does not
  specify.
- The selecting condition is named: which conserved labels the observer's records fix (Main ledger
  (iv)).

**T3, affine lift at resonance (b ≠ 0): "unspecified".**
- The text does not treat this case.
- By U2 [A], no conserved function meets the requirement.
- By U3 [A], Q′ = E_⊥ + Q′_0, with Q′_0 a function of the uniform variables. So the choice among
  Q′, E_⊥ and E_⊥ + f(Q′_0) is a choice of uniform-sector treatment.
- No stated premise within the searched scope selects one.

**F-stag [A].** At α = 1/d with L even, E_⊥ is only semidefinite, and its shells do not confine the
staggered null direction. Lane 1 REPORT-r2 line 297 holds for odd L, or with the staggered labels
fixed.

**D5 (#1049).** Lane 1's class-(c) placement does not depend on reading the energy as Q′. The E_⊥
branch rests on an unstated interface choice together with a staggered-label treatment.

**F-slice.** On T at α = 1/d with b = 0, under stationarity with finite second moments, an
alternative to the H-ZM quotient exists that yields a unique J on every label sector.
- It is conditional on lane 2's Theorem 1, a model-written record.
- Step (c) is [W].
- Whether it serves the consumers of lane 2's Proposition 5 (Theorem 5's Σ, H-PF) is open (O3).
- It does not show that H-ZM is unnecessary for Theorem 5.

**Productivity:** gem.
- U1 is modestly NEW.
- U3, F-stag and the conditioned F-slice are NEW.
- §4.1, §4.3 and §5.2 are ELABORATING.
- U2 is CONFIRMING.

The stopping rule applied is (c): a partial state.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Every result is a paper derivation or source reading, checked by the model reviews of §1. The
remediation plan below authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| T1a/T2a two-level verdict, T1b/T2b, T1Z/T2Z | REPORT-r3 §4–§6 | partially verified: source reading and hand algebra, model-reviewed | independent non-model review; the unswept remainders D-1 to D-8 | #1217 | a recorded independent review; a recorded sweep of the remainders |
| Register transfer to the SM §4.1 observer (O2) | §4.1, §11 | open | a derivation, from stated premises, of the register of the SM §4.1 observer | #1217 | a written derivation, or an owner decision on the interface premise |
| Main:262 row, reason (2) as corrected | §3 | partially verified; the r3 wording was confirmed by the accuracy check, not otherwise reviewed | independent review | #1217 | a recorded independent review |
| U1, U2, U3 | §7.2–§7.3 | partially verified: re-derived by the model review | independent non-model review; an exact finite control | #1049 | a recorded review, or an exact control run under authorization |
| F-stag | §7.4 | partially verified, as above | independent review | #1049 | a recorded independent review |
| F-slice (a)–(d) | §5.3 | partially verified; step (c) [W]; conditional on lane 2 Theorem 1; consumer question open (O3) | independent review; verification of lane 2 Theorem 1; a written answer to O3 | #1217 | a recorded review; verification of lane 2 Theorem 1; a derivation or counterexample for O3 |
| Sweep counts | §2 | reproduced by the model review with the stated commands | none beyond the remainders | #1217, #1049 | — |
| Unswept remainders D-1 to D-8 | §1 | not swept | see the list below the table | #1217, #1049 | a recorded sweep under the same decision rule; until then every verdict stays scoped |
| Preregistration order (PLAN.md before any result) | `PLAN.md` | evidence is commit order only: `d4f97b53` at 10:32:19Z precedes the first result commit `266fbc60` at 10:48:01Z (2026-11-26); `04248fc9` follows at 11:02:16Z | none available from commit order alone | #1217, #1049 | none; the limitation stands as stated |
| Open nodes O1–O6 | §11 | open; not adopted | derivation, refutation or owner decision | O1: proposed #1049 (§7); O2, O3, O4, O6: #1217; O5: #1217, #1049 | a written derivation, a counterexample or an owner decision |

**The unswept remainders D-1 to D-8:**
- **D-1:** the rest of Main §3.1, §3.2 and §3.4 word for word; SM:312–344 and SM:360–374; the
  remainder of Structure, GR, Introduction and Methodology.
- **D-2:** the Group N remainder in the verification records.
- **D-3:** \pi and quotient in papers and book, below snippet level.
- **D-4:** the Group B remainder in papers and book. W-1 covers gauge.
- **D-5:** the Lean high-volume hits.
- **D-6:** POSIT-MIN, Q3, Q4 and BRIDGE-UNIT1.
- **D-7:** the grep mode, recorded: fixed-string, not the planned `-E`.
- **D-8:** the 95 non-`.lean` files under the Lean directories, and the 147 files under papers/
  that are neither `.md`, `.tex` nor `.pdf`.

## 4. Off-`main` references (§A.42 item 8)

Each reference is classified by reading the claim it is attached to, using the three classes:
provenance, support on `main`, and support off `main` (gap).

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7189139613, 7190274734 (owner decisions) | `PLAN.md`, report headers; §1 here | provenance: authority records quoted with author and time; no result uses them |
| #1169 comment 7189143747 (synthesis) | `PLAN.md` §1 | provenance |
| #1049 comment 6624263637 (owner decisions Q1, Q2) | report §4.1, §12 | provenance: governance record, quoted. No scientific claim uses it: the substratum-interface contradiction rests on Main:84–89, Main:298, Main:368, Main:376 and SubstratumInterfaceAudit, on `main`. Q1 and Q2 are also quoted on `main` at A5-LINEAR-AFFINE:601 and :608, and Q2 at A5-Q4-STAGE2D:39–42 |
| PR #1594 comments 7190048646, 7190223659, 7190487175 (reviews) | report headers; §1 here | provenance: evidence of review; no result uses them |
| commit `04248fc9` (r2, superseded) | report headers; §3 here | provenance: cited to identify the r2 text. Its commit time in the §3 preregistration row is supplementary; the order claim rests on `d4f97b53` and `266fbc60` |
| commit `d5b119f9` (condensed r3, superseded) | §1 here | provenance: cited to identify the text the accuracy check reviewed |
| commit `d4f97b53` (PLAN.md) | report headers; §1, §3 here | support off `main` (gap), closed by the landing condition of §5: it holds the preregistration and the evidence of its order |
| commit `266fbc60` (r1) | §3 here, preregistration-order row | support off `main` (gap), closed by the landing condition of §5: the order claim uses its commit time. For identifying the r1 text it is provenance |
| the commit adding the rebuilt `REPORT-r3.md` | §1 here | support off `main` (gap), closed by the landing condition of §5: the authoritative report |
| the commit adding this file | — | support off `main` (gap), closed by the landing condition of §5: this record's own content |
| pin `353a066f` and every file:line citation | throughout | support on `main`: the pin is `main` at the time of writing |
| lane 1 and lane 2 records (`qbeta-trace-20261126`, `complex-carrier-20261126`) | throughout | support on `main`: they are at the pin and are used as pointers. Lane 2 Theorem 1 is used as a premise of F-slice (d) and carried as a condition of that result |
| #1217, #1049, #1169 | headers | provenance: accountability |

**Support off `main` (gaps), and how they close.** Each gap below is closed when the merge commit
of §5 lands with the commit reachable from `main`. None is closed before that, and keeping the
branch does not close it.
- `d4f97b53`: `PLAN.md` and the preregistration order.
- `266fbc60`: its commit time, for the preregistration-order row.
- The commit that adds the rebuilt `REPORT-r3.md`: the authoritative report.
- The commit that adds this file: this record.

## 5. Landing condition

The record is preserved only through a **merge commit, not a squash**. The merge keeps these
commits reachable from `main`:
- `d4f97b53`, `266fbc60`, `04248fc9` and `d5b119f9`;
- the commit that adds the rebuilt `REPORT-r3.md`;
- the commit that adds this file.

That `PLAN.md`'s commit precedes every report commit is part of the record's provenance.

Per the owner decision of 2026-11-26T11:06Z, preservation includes the accuracy checks,
integration with current `main` and exact-head CI. Merging needs the owner's separate approval
(§A.50 item 1).

## 6. Preservation rationale

The unit answers the owner's question for lane 3: whether existing premises supply H-ZM and the
SM:811 energy. It uses a preregistered protocol, its controls are all green, and every negative is
scoped to its searched scope.

It establishes:
- **the status of H-ZM for both static modes:**
  - at Main's specified partitions, contradicted;
  - for the SM §4.1 observer, contradicted only if the register transfers through the SM:232
    bridge (O2, open), and otherwise unsourced within the searched scope;
  - for the constant mode, conditionally sourced;
- **that SM:292's positive-definite shell cannot exist on the full phase space** at the normalized
  branch (U1);
- **that the choice among Q′, E_⊥ and E_⊥ + f(Q′_0) reduces to a uniform-sector treatment** (U3),
  which settles how #1049's D5 placement rests on the manuscript;
- **a correction of scope to lane 1's confinement statement** (F-stag);
- **a conditioned alternative to the H-ZM quotient** (F-slice). The owner named it as a successor
  question: "F-slice: Can it eliminate the need for H-ZM in Theorem 5?" (#1169 comment 7190274734,
  item 4).

It is substantive and nonredundant with lanes 1 and 2, it is independently reviewed, and its open
gaps carry the remediation plans of §3.

## 7. Proposed accountable Issue for O1 (a proposal for the owner)

O1 has two parts:
- the physical status of the amplitude-scale gauge's translation clause;
- the wording variance between SM:96 ("affine relabellings", translations included) and SM:811
  ("additive-automorphism group", which strictly excludes translations).

The variance is immaterial for SM:811's link-difference map. It is a manuscript-consistency defect
(§A.47 item 4).

This record **proposes #1049** as the accountable Issue, because the owner's decision Q2 on the
amplitude-scale gauge is recorded there. This is a proposal only: the owner may name another Issue
or open a new one. It authorizes no manuscript edit.
