# F-SLICE-HZM: preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it.

- **Evidence layer of every new result:** mathematical derivation on paper, labelled [A] and [W]
  in the report, with source reading at the pin [P]. The records of lane 2 [L2], unit A [A-rec]
  and unit C [C3] are model-reviewed paper derivations, used as named conditional inputs.
- **No computation was run by the writer, and no Lean was built.** The delta review of r2 ran a
  numerical cross-check of Proposition P; it is numerical evidence only and is not part of the
  record.

## 1. The record preserved

**Authoritative report:** `REPORT-r5.md` (revision r5, commit
`4ab5de248cd7a3498c3bdac68cc97e218a34f4ec`, the head of `research/f-slice-hzm-20261126` before
this file).

**Superseded versions,** kept unchanged:
- `REPORT.md` (r1, commit `5073afda47acfc4fb246fa508156393cd3da8894`);
- `REPORT-r2.md` (r2, commit `82b8ff3f17c8c947a7dc218ded9220ff235fdac8`);
- `REPORT-r3.md` (r3, commit `89c496b98130ff821baf60a1268bc5ae0572c61f`);
- `REPORT-r4.md` (r4, commit `21ba94c3ac19139885b7de4891e7234c7d4c84d1`).

**Change maps.** `CHANGES-r2.md` to `CHANGES-r5.md` map each change to its review finding. r4 and
r5 change text only. r4 adds the N-1 qualifier to the R2 condition, the uncentred-reading case to
R3, and the rotation-group assumption to ρ_T; r5 corrects the O_h example in §3.4. No derivation,
witness, classification or outcome changes after r3.

**Plan.** `PLAN.md` (commit `7e85350126158ae7c2f95bf6312cf8f735f18a01`, committed alone before r1)
fixes the questions, the classes, the decision rule, the controls and the stopping conditions. It
is recorded, not frozen, and is not superseded. It states that the writer read the input records
before writing it and began considering the question while reading, and that no derivation was
recorded before its commit. Report §1 records how the plan's premise list is read.

**Status in the header.** The header of `REPORT-r5.md` records the report's status before
acceptance ("WIP / UNVERIFIED"), and its outcome is stated by reading. Review, and the status the
owner set for the readings, are recorded here.

**Accountable Issues:** #1217 and #1049 (programme #1169). Guiding pull request: #1611.

**Owner decisions.** Each is a #1169 comment posted from the account `amaybaum`, quoting the
owner:
- **Comment 7199704501** (created 2026-11-26T17:49:03Z; decision received 2026-11-26T17:49Z):
  activation of work package WP-2, scientific research, by the owner's decision "Proceed as
  suggested".
- **Comment 7200549806** (created 2026-11-26T18:30:55Z; decision received 2026-11-26T18:30Z),
  item 4, authorizes the investigation: "Authorize all three ranked scientific investigations —
  SMD sourcing, uniform norm control and F-slice — at paper-only level, with independent review and
  bounded stopping conditions."
- **Comment 7202075726** (created 2026-11-26T19:53:55Z; decision received 2026-11-26T19:52Z):
  - item 3: "Preserve #1612, #1614 and #1611 at their reviewed landing heads, subject to their
    remaining verification and landing requirements. Preservation only; no premise adoption or
    manuscript integration.";
  - item 4: "For F-slice, retain N-1 as a candidate extension reading and N-2, N-8 and N-9 as
    additional candidate premises, not established consequences. Preserve R2 conditionally and
    retain the alternative R3 obstructions. Do not claim R1 or remove H-ZM.";
  - and: "All existing correctness, independent review, staging, freeze, trial and landing gates
    remain in force."

**Independent non-author reviews.** These are model reviews by reviewer agents, each recorded on
PR #1611 as reviewer text posted verbatim: evidence of review, not independent mathematical
verification.
- **Comment 7201020516, review of r1 at `5073afda`: REVISE,** findings 1–8. It found §3.1, §3.2,
  Proposition P, Lemma L and ρ_W correct, and found that §4.2's label exclusion rested on an
  unstated reading of φ on the static labels and that step (c) is consumed through the state's
  stabilizer.
- **Comment 7201250359, delta review of r2 at `82b8ff3f`: REVISE (minor),** findings 1–8, of which
  r3 applies 1–7 (finding 8 is a register remark with no change). It found ρ_S, both directions of
  §4.2, R_ext, the momentum choice in Proposition P and the Lemma L additions correct. Its
  numerical cross-check of Proposition P is numerical evidence only.
- **Comment 7201639742, delta review of r3 at `89c496b9`: ACCEPT WITH NITS,** nits 1–4. It checked
  witness ρ_T and the implication by hand, correct given that O is the rotation group.
- **Comment 7201689426, delta review of r4 at `21ba94c3`: ACCEPT WITH NITS,** one nit, on the O_h
  example in §3.4.
- **Comment 7201724532, delta review of r5 at `4ab5de24`: ACCEPT.**
- **One reviewer wrote several reviews.** The delta reviews of r3, r4 and r5 each refer to that
  agent's own preceding review ("against my r2 review", "my r3 review", "my r4 review"), so the
  reviews of r2 to r5 come from one reviewer agent. The records do not state whether that agent
  also wrote the review of r1.

## 2. Substantive result and its precise scope

**Scope.** Carrier T = (Z/L)^d at the massless point (αμ = 1/d), for SM Theorem 5's consumers only,
on the linear lift. Every result is conditional on LIN, LIFT, b_A1 = 0, an F-stationary law with
finite second moments, and lane 2's Theorem 1, and inherits the open SM:232 bridge. Carrier Z
(H-top), the nonlinear lift (H-PF-int) and the other consumers of H-ZM or of the static labels
(the SM:811 energy, SM:344) are not addressed. Nothing concerns the Z/q level. H-PF, L-SDS, TPC and
SMD remain carried and unsourced.

**Results [A].**
- **§3.1–§3.2, what the F-slice supplies.** The centring x ↦ x − x*(t) is the spectral projection
  P_rest on the stationary support. The "J on every label sector" is the single J_F on V_rest, the
  J of lane 2's Proposition 5. J, and Σ under the centred reading, read the state only through
  P_rest∗ρ, so unit C's disintegration step (c) is not consumed for them. The second-moment split
  uses only second-moment stationarity.
- **Proposition P.** Without the requirement LI that J commute with the deviation dynamics, a
  staggered label sector (L even, a ≠ 0) admits a one-parameter family of tamed pairs (J_t, J_{−t})
  intertwined by F and the translations, besides (J_F, J_F); momenta k = (π, 0, 0) in d = 3 for
  every even L, and k = (2π/L, 0) in d = 2 for even L ≥ 4.
- **§3.4, the stabilizer reads the joint law.** Stab(ρ) ⊆ Stab(P_rest∗ρ) ⊆ Stab(C_rest). P2a's
  inclusion holds without step (c); P2d consumes step (c). Witness ρ_S: the two stabilizers can
  differ. Witness ρ_T (μ = 1, L ≥ 7, generic k_0 as in unit A's Proposition A, O the cubic
  rotation group of order 24): SMD read on the full ρ is strictly stronger than SMD on P_rest∗ρ.
- **Lemma L.** Any continuous action of U(6) on the static labels commuting with the translations
  is trivial on SU(6); the internal action on the link index cannot extend to the static labels.
- **§4.2.** Given Lemma L, real-linearity and H-PF on V_rest, covariance of φ on the labels is
  equivalent to the centred reading φ = Φ_n ∘ P_rest, each direction proved. A non-covariant
  real-linear extension (H-PF_u) is also admissible and defeats P2a (witness ρ_W, §6).

**The four readings (report §8, §10).**
- **N-1:** the custodial action of SM:342 read as the extension R_ext, acting trivially on the
  static labels on SU(6). Under the internal reading P1 is OB (Lemma L).
- **N-2:** LI, the label-independent J.
- **N-8:** the centred reading of φ on the stationary support.
- **N-9:** SMD read on the full ρ.

**Current status of the readings, as the owner set it (comment 7202075726, item 4).**
- N-1 is a candidate extension reading, not the uniquely established reading.
- N-2, N-8 and N-9 are additional candidate premises: not adopted and not derived.
- The preserved outcome is therefore **R2**: a conditional route for Theorem 5's consumers on T at
  the massless point that does not use H-ZM's claim that the static modes are unobservable. It
  holds under N-1's extension reading and the candidate premises N-2, N-8 and N-9, with every
  condition of the scope above. Under those premises the affected consumers become S given the
  premise (H6-Φ for N-2; P2a and L-NZM for N-8; P2d for N-9). The report names R2 "route under a
  further premise", with stopping condition 3.
- **The R3 obstructions are retained:** P1 is OB if only the internal reading of the custodial
  action is admitted (Lemma L), and P2a is OB if the uncentred reading is the only admitted reading
  of φ (ρ_W).
- **R1 is not claimed, and H-ZM is not removed.**

This status is one the owner set. It adopts no premise (§A.29, §A.50 item 6): N-1 remains a
candidate reading and N-2, N-8 and N-9 remain candidate premises. No witness separating H-ZM from
the F-slice premises is claimed: N-8 imposes H-ZM's content restricted to φ. Lane 2's statement
"Exclusion requires the named hypothesis H-ZM" stays true as stated.

**Productivity (report §9):** gem, borderline. NEW (borderline): Proposition P. POSITIVE: §3.1–§3.2.
ELABORATING: Lemma L, §4.2, §3.4 with ρ_S and ρ_T, and ρ_W. CONFIRMING: C+2. Report §7 records
that several controls have low power on §4.2's step, and that no control decides whether the label
exclusion is derived or assumed.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Each result is a paper derivation checked only by the model reviews of §1. The remediation plan
below authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| §3.1–§3.2 (centring is P_rest; one J; J and Σ do not consume step (c)) | report §3.1–§3.2 | partially verified: hand derivation, model-reviewed | independent non-model review | #1217 | a recorded independent review |
| Proposition P | report §3.3 | partially verified, as above; the delta review of r2 added a numerical cross-check, numerical evidence only | independent review; an exact finite control on a small even torus | #1217 | a recorded review; an exact control run under authorization |
| §3.4, ρ_S | report §3.4 | partially verified, as above | independent review | #1217 | a recorded independent review |
| §3.4, ρ_T and the implication | report §3.4 | partially verified, given that O is the rotation group | independent review | #1217 | a recorded independent review |
| Lemma L | report §4.1 | partially verified, as above | independent review | #1217 | a recorded independent review |
| §4.2, both directions; witness ρ_W | report §4.2, §6 | partially verified, as above | independent review | #1217 | a recorded independent review |
| Outcome R2 | report §8; §2 here | conditional: on N-1's extension reading and the candidate premises N-2, N-8 and N-9, and on the conditions of §2; status set by the owner; R3 obstructions retained; R1 not claimed | a derivation of N-1, N-2, N-8 or N-9 from stated premises, or an owner decision adopting or rejecting each (§A.29, §A.50 item 6) | #1217, #1049 | a written derivation, a counterexample, or an owner decision on each premise |
| Inherited conditions LIN, LIFT, the SM:232 bridge, L-SDS, lane 2's Theorem 1; carried TPC, SMD, H-PF (N-5) | report §2, §10 | open or posited as stated in report §2; lane 2's Theorem 1 model-reviewed | verification of lane 2's Theorem 1; sourcing of the carried premises | #1217; #1049 for LIN | the remediation of the lane 2, unit A and unit C records; an owner decision on any premise |
| Open nodes N-3, N-4, N-6 | report §10 | open | derivation or trace | #1217 | a written derivation or trace |
| W-1 search for a stated centring of Σ | report §1 | keyword-based, not exhaustive | an exhaustive search | #1217 | a recorded exhaustive search |
| Preregistration order (`PLAN.md` before r1) | `PLAN.md` | evidence is commit order only: `7e853501` at 18:37:53Z precedes `5073afda` at 18:50:45Z (2026-11-26) | none available from commit order alone | #1217, #1049 | none; the limitation stands as stated |

## 4. Off-`main` references (§A.42 item 8)

Each reference is classified by reading the claim it is attached to, using the three classes:
provenance, support on `main`, and support off `main` (gap).

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7199704501, 7200549806 (owner decisions) | `PLAN.md`, report header; §1 here | provenance: authority records quoted with author and time; no result uses them |
| #1169 comment 7202075726, item 3 | §1 here | provenance: authority record quoted with author and time |
| #1169 comment 7202075726, item 4 | §1, §2, §3 here | support off `main` (gap): the status of N-1, N-2, N-8 and N-9 and of the outcome in §2 rests on it. The gap is closed by the landing condition of §5, through the quotation of its content in full in this record with author and time (§A.42 item 7). No scientific result uses it |
| #1169 comment 7191949320 (successor assessment) | `PLAN.md`, report §12 | provenance: question source |
| #1169 comment 7190274734, item 4 (the owner's successor question for unit C) | §6 here | provenance: question source, also quoted on `main` in unit C's `PRESERVATION.md` §6 |
| PR #1611 comments 7201020516, 7201250359, 7201639742, 7201689426, 7201724532 (reviews) | report header; §1 here | provenance: evidence of review; no result uses them |
| the numerical cross-check script of the delta review of r2, held in the reviewer's scratch space | §1 here | provenance: no result uses it |
| commit `7e853501` (`PLAN.md`) | report header; §1, §3 here | support off `main` (gap), closed by the landing condition of §5: it holds the plan and the evidence of its order |
| commit `5073afda` (r1) | report header; §3 here, preregistration-order row | support off `main` (gap), closed by the landing condition of §5: the order claim uses its commit time. For identifying the r1 text it is provenance |
| commits `82b8ff3f` (r2), `89c496b9` (r3), `21ba94c3` (r4) | report header; §1 here | provenance: cited to identify the earlier texts |
| commit `4ab5de24` (r5) | §1 here | support off `main` (gap), closed by the landing condition of §5: the authoritative report |
| the commit adding this file | — | support off `main` (gap), closed by the landing condition of §5: this record's own content |
| pin `a8d4ab96` and the SM line citations | report header, throughout | support on `main`: `a8d4ab96` is an ancestor of `main` at `84e927b9`. `papers/SM.md` differs between them only at line 14, which the report does not cite; `papers/Main.md` (lines 360, 544, 686, 718, 732) and `papers/Substratum.md` (lines 60, 201) also differ, by one-line replacements that leave line numbers unchanged and concern none of the passages the report reads. The other files that W-1 searched and that differ are `papers/Computation.md`, `papers/Methodology.md`, `papers/Structure.md`, `book/The-Incompleteness-of-Observation-FULL.md`, `book/ch02-substratum.md`, `book/ch04-methodology.md` and `book/ch14-quantum-computing.md`. No changed line in any of these files, or in SM, Main or Substratum, contains a W-1 term or a W-1 pairing of "condensate" with a centring term; the changed SM:14 mentions the condensate-stabilizer construction on both sides of the change, with no such term. So no change bears on W-1 |
| lane 2 (`complex-carrier-20261126`), unit A (`theorem5-premise-ledger-20261126`) and unit C (`hzm-energy-sourcing-20261126`) records | throughout | support on `main`: at the pin and unchanged at `84e927b9`; model-reviewed inputs, carried as named conditions (lane 2's Theorem 1 among them) |
| #1217, #1049, #1169 | headers | provenance: accountability and routing |

**Support off `main` (gaps), and how they close.** Each gap below is closed when the merge commit
of §5 lands with the commit reachable from `main`. None is closed before that, and keeping the
branch does not close it.
- `7e853501`: `PLAN.md` and the preregistration order.
- `5073afda`: its commit time, for the preregistration-order row.
- `4ab5de24`: the authoritative report.
- #1169 comment 7202075726, item 4: closed through its quotation in this file (§A.42 item 7).
- The commit that adds this file: this record, including that quotation.

## 5. Landing condition

The record is preserved only through a **merge commit, not a squash**. The merge keeps these
commits reachable from `main`:
- `7e853501`, `5073afda`, `82b8ff3f`, `89c496b9`, `21ba94c3` and `4ab5de24`;
- the commit that adds this file, which follows the reviewed head `4ab5de24` and adds only this
  file.

That `PLAN.md`'s commit precedes every report commit is part of the record's provenance.

The owner decision of 2026-11-26T19:52Z, item 3 ("Preserve #1612, #1614 and #1611 at their
reviewed landing heads, subject to their remaining verification and landing requirements"), is the
owner's approval of this merge (§A.50 item 1), subject to the review of this file and green CI. The
same decision keeps every existing gate in force.

## 6. Preservation rationale

The unit answers rank 3 of the successor assessment, the successor question the owner named for
unit C ("F-slice: Can it eliminate the need for H-ZM in Theorem 5?", #1169 comment 7190274734,
item 4): whether unit C's F-slice supplies the inputs that Theorem 5's Σ and H-PF consume. It uses
a plan committed before the report, and its outcome is stated by reading with every condition.

It establishes:
- **that the F-slice's J is lane 2's Proposition 5's J**, and that J and Σ do not consume unit C's
  step (c);
- **that a slice-dependent J is possible unless LI is imposed** (Proposition P);
- **that the internal action has no translation-commuting U(6) extension to the static labels**,
  because any such action is trivial on SU(6) (Lemma L);
- **that Theorem 5's null-sector treatment on T reduces to four named readings**, one of which,
  SMD on ρ, is strictly stronger on the F-slice than on the H-ZM route (ρ_T);
- **the R3 obstructions** under the internal and uncentred readings.

Under the owner's status of §2 it preserves R2 as a conditional route under named candidate
premises, not a removal of H-ZM. It is substantive and nonredundant with lane 2 and units A and C,
it is independently reviewed by the model reviews of §1, and its open gaps carry the remediation
plans of §3. Its findings for routing (report §11) are listed there and edit no other record.

## 7. Standing of this record

Preservation establishes no claim (§A.46 item 1). The model reviews are evidence of review, not
independent mathematical verification, and landing the record does not change any result's
evidence layer. No premise is adopted, H-ZM is not changed, and nothing is proposed for the
manuscripts.
