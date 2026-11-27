# SMD-CL-1: preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it. It is a
draft prepared for the owner's consolidated preservation decision; it records no decision.

- **Evidence layers of the results:** mathematical derivation on paper, labelled [A] in the report,
  or reasoning, labelled [W] (the K1 routes of report §3). No computation was run and no Lean was
  built; the report's control CC-E is vacuous because no identity it uses needed computation.
- **Inputs used as model-reviewed results:** SMD-SRC-1 (`../smd-sourcing-20261126/`), unit A
  (`../theorem5-premise-ledger-20261126/`) and lane 2 (`../complex-carrier-20261126/`), named where
  used.

## 1. The record preserved

**Authoritative report:** `REPORT.md` at commit `b7e29ea7418f03fa32198f7d68df2f47c5f664ba`, the
head of `research/smd-clustering-20261127` before this file. The report was revised in place; its
earlier texts are in the branch history:
- `22347bb93cd89ea41541c77b921373282d15f0e1`: the report as first committed (r1);
- `74610711be9aa33081fd4b2d347ffcb5f4090095`: r2, review findings F1–F11 applied; no r1 result
  changes, and one derivation is added (S-2′, for F4);
- `aa7230170faf04796921b569babe6da2460ce91a`: r3, delta-review nits D1–D3 applied;
- `b7e29ea7`: the optional nit E1 applied (one line in S-2′).

**Plan.** `PLAN.md` (commit `98172765ce183501d3f9762906a0d1db7ed913ac`, committed alone before the
report) fixes the questions, the decision rule, the controls, the stopping conditions and the Goal
link. It is unchanged at `b7e29ea7`. Its chronology disclosure states that, before writing it, the
writer formed, without writing or checking them, three candidate directions later used (the
product form and symmetry of the selected measure, the conserved energy average, phase-locked plane
waves). The plan fixes the decision rule before the report; it does not certify that no part of a
route was conceived before it.

**Status in the header.** The report's header records its status before review ("Pending
independent non-author review"), and its §11 table records the r1 and r2 reviews only. All reviews
are recorded here.

**Accountable Issues:** #1049 and #1217 (programme #1169). Guiding pull request: #1623.

**Owner decisions.** Each is a #1169 comment posted from the account `amaybaum`, quoting the
owner:
- **Comment 7199704501** (created 2026-11-26T17:49:03Z): activation of work package WP-2,
  scientific research.
- **Comment 7208939261** (created 2026-11-27T03:22:49Z; decision received 2026-11-27), unit 3,
  authorizes the investigation: "SMD clustering (#1049 and #1217, follows #1612). Whether the
  required cumulant clustering can be sourced from the substratum dynamics, including the open K1
  and K0 on 0 < |μ| < 1." Rules: "paper-only; preregistered plan committed before any derivation;
  no premise adopted (AGENTS.md sections A.29 and A.50 item 6); independent non-author review;
  preservation only by a separate owner decision."
- **Comment 7209325168** (created 2026-11-27T03:51:22Z; owner, coordinating session, 2026-11-27),
  quoted in part: "This is an important negative result. It narrows the search for a genuine
  physical mechanism rather than merely replacing one assumption with another."; "SMD remains
  physically unsourced. Theorem P provides a conditional mathematical result, but the required
  state has not been derived from the substratum."; "The K0 route is ruled out within the stated
  scope."; "Clustering remains an additional condition, rather than a derived physical property.";
  "Prepare #1623 together with UN-1 and F-slice for a consolidated preservation decision."; "Do not
  initiate another SMD successor investigation yet."; "Preserve the negative results and their
  exact limitations. No new premise is adopted, and no merge is authorized yet."
- **Preservation decision: pending.** A consolidated owner decision for #1622, #1623 and #1624
  under §A.46 item 8 has not been recorded. This record does not authorize a merge (§A.50 item 1).

**Independent non-author reviews.** These are model reviews by reviewer agents, each recorded on
PR #1623 as reviewer text posted verbatim: evidence of review, not independent mathematical
verification.
- **Comment 7209241804, review of r1 at `22347bb9`: REVISE (minor),** findings F1–F11, two
  blocking (F1: the Q1 verdict named the wrong missing property; F2: Lemma N's scope and
  classification). It found no mathematical error and re-derived by hand ρ_Q item by item, Lemmas
  A and R, Corollary T (including its non-circularity), S-2, and the Stein re-derivation.
- **Comment 7209292122, delta review of r2 at `74610711`: ACCEPT WITH NITS,** D1–D3. It found
  F1–F11 fixed and S-2′'s mathematics correct, with S-2′ calling on (H) where (H′) applies (D1).
- **Comment 7209304818, confirmation of r3 at `aa723017`: ACCEPT, with one optional nit** (E1).
- **Confirmation of `b7e29ea7` (E1 applied):** to be recorded on #1623; not available when this
  file was written.
- The review texts do not state whether one reviewer agent wrote more than one of them; each was
  started with a fresh context.

## 2. Substantive result and its precise scope

The results concern the observer-level real linear offset-free lift F = F_s ⊗ I_6 of SM:314 at
M = μI_6, the fixed premise set of SMD-SRC-1, and the substratum as Main and SM specify it, at the
pin `13c05b4f`. Nothing is claimed for μ = 1, an offset b ≠ 0, the nonlinear case, or manuscript
wording.

**Negative results, with their exact limitations.**
- **Q1, selected counting measure: NOT SOURCED, conditional on (B) and (H)** (S-2).
  - (B): the observer-level configuration is the image of the infinite-volume substratum
    configuration under a measurable, translation-equivariant map Π. It is a reading of the
    coarse-graining bridge, which is unproved (SM:232).
  - (H): Proposition 4b's hypotheses, under which the observer image is invariant under the signed
    permutations B_6 (SM:130; unit A Proposition C). (H) is load-bearing for the assignment.
  - Under (B) and (H), the image is a single mixing phase (K3 when Π has finite range) with scalar
    Σ, so Theorem 5's condensate state is neither that image nor a translation-ergodic component of
    it. The missing property is distinct block values, not clustering. The NEW content beyond unit
    A's Proposition C is the extremality step.
- **Q1, energy-shell ensemble: NOT SOURCED, conditional on (H′)** (S-2′): Proposition 4b's
  hypotheses with the shell law in place of the counting measure. (B) is not used. Extremality of
  the shell law is not needed and not established.
- **Q1, prepared prior or record-selected orbit: REDUCED.** The basis is that Main and SM supply no
  derivation of its stationary law or clustering (SM:290, SM:298, SM:1225). Lemma N (finite t) and
  S-3 are consistent with this and do not establish it.
- **Q3, K0: OBSTRUCTION, by the witness ρ_Q,** for every d ≥ 1 and every 0 < abs(μ) < 1, under the
  fixed premise set (L-SDS, TPC (r2), O-equivariant Σ with distinct block values, H-PF, the kinetic
  clause, the linear offset-free branch): ρ_Q is translation-ergodic and F-stationary, and
  Stab(ρ_Q) = U(3)×U(2)×Z_4 ⊊ Stab(C) = U(3)×U(2)×U(1). It is a witness, not a classification:
  it is not O-invariant as a law (the fixed set does not require it), and an O-invariant K0 witness
  is not constructed (open node N3). It is consistent with SMD-SRC-1's Theorem P: ρ_Q violates K1
  and K2.

**Other results.**
- S-1 (what the selected measure supplies), S-3 (no Gaussianization at the substratum level),
  Lemma N (finite t; t → ∞ limits not shown).
- Lemma A (under ergodicity each covariance atom has rank ≤ 1; mixing excludes atoms; under K0
  with TPC only A_1 carries atoms), Lemma R (cumulants of F-stationary laws live on resonance
  sets), Corollary T (an independent proof of Theorem P for translation-invariant states).
- Q2, K1: OPEN, with the gap sharpened (report §3).
- Q4: [I-Stein] re-derived, with symmetric dependency neighbourhoods, modulo the textbook
  Stein-equation bounds; H-αCLT unchanged (no source read; no external access).

**Productivity:** met through G1, G2 and G3 of `PLAN.md` §4. NEW: ρ_Q; the extremality step of
S-2.

**What the record does not show.** SMD is not sourced, and Theorem P stays a conditional result:
the clustering it needs is not derived from the substratum, and remains a condition on the state.
No premise is adopted, and nothing is proposed for the manuscripts.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Each result is a paper derivation checked only by the model reviews of §1. The remediation plan
below authorizes no work (§A.45 rule 3).

| Claim | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| S-2 (Q1 NOT SOURCED, selected measure) | report §1.2 | partially verified: model-reviewed (r1); conditional on (B) and (H) | independent non-model review | #1217 | a recorded independent review |
| Conditional input (B) | report §1.2, §11 | a reading of the unproved coarse-graining bridge (SM:232); not adopted | a proof of the bridge in the form (B), or a bridge of another form | #1217 | a proof, or an owner decision on the reading |
| Conditional input (H) | report §1.2, §11 | Proposition 4b's hypotheses, as unit A carries them; not established here | as recorded in unit A | #1217 | as recorded in unit A |
| S-2′ (energy-shell ensemble) | report §1.2 | partially verified: model-reviewed (r2 delta review); conditional on (H′), not established here | independent non-model review; a check of Proposition 4b's hypotheses for the shell law | #1217 | a recorded review and check |
| Q1 REDUCED (prepared prior, record-selected orbit) | report §1.2 | rests on the absence of a derivation in Main and SM (SM:290, SM:298, SM:1225) | a derivation or refutation of a stationary clustering observer law with distinct values from such a datum | #1217 | either |
| ρ_Q (Q3, K0 obstruction) | report §2 | partially verified: model-reviewed, re-derived by hand in the r1 review | independent non-model review; optionally a non-model check of the relation-lattice computation | #1217 | a recorded independent review |
| O-invariant K0 witness (N3) | report §9, §11 | open | a construction with the cubic orbit's relation lattice, or a proof that none exists | #1217 | either |
| S-1, S-3, Lemma N (finite t) | report §1.2 | partially verified: model-reviewed | independent non-model review; the t → ∞ question is not addressed | #1217 | a recorded review; a separate result for limits |
| Lemmas A, R; Corollary T | report §2.5, §3 | partially verified: model-reviewed | independent non-model review | #1217 | a recorded review |
| K1 (Q2, N1) | report §3 | open | a proof, or a translation-mixing witness | #1217 | either |
| [I-Stein] re-derivation | report §4 | partially verified: model-reviewed; uses textbook Stein-equation bounds | independent non-model review | #1217 | a recorded review |
| H-αCLT (N5) | report §4 | stated hypothesis, no source read | a source check or a proof | #1217 | a pinned theorem or a proof |
| Preregistration order (`PLAN.md` before the report) | `PLAN.md` | evidence is commit order only: `98172765` at 03:30:19Z precedes `22347bb9` at 03:34:04Z (2026-11-27); with the chronology disclosure of §1 | none available from commit order alone | #1049, #1217 | none; the limitation stands as stated |

**Finding for routing (#1217), listed and not edited.** SMD-SRC-1's mutable status records
(`../smd-sourcing-20261126/REPORT.md` §14 and `../smd-sourcing-20261126/PRESERVATION.md` §3) list
Corollary P3′ as conditional on the recalled [I-Stein]. After review of report §4 here, they could
record P3′ as resting on this re-derivation and the textbook Stein-equation bounds. The owner
directed that no SMD successor investigation be opened; the findings go to the Phase 1
reassessment (#1625), and this note changes no record.

## 4. Off-`main` references (§A.42 item 8)

Each reference is classified by reading the claim it is attached to.

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7199704501, 7208939261, 7209325168 (owner decisions) | `PLAN.md`, report header; §1 here | provenance: authority records quoted with author and time; no result uses them |
| PR #1623 comments 7209241804, 7209292122, 7209304818 (reviews); the confirmation of `b7e29ea7` | report r2 header and §10; §1 here | provenance: evidence of review; no result uses them |
| PR #1612 ("landed via #1612") | `PLAN.md` | provenance: how SMD-SRC-1 reached `main`; the content used is on `main` |
| #1622, #1624, #1625 | §1, §3 here | provenance: the consolidated decision and the Phase 1 reassessment |
| commit `98172765` (`PLAN.md`) | report header; §1, §3 here | support off `main` (gap), closed by the landing condition of §5: the plan and the evidence of its order |
| commit `22347bb9` (r1) | §1, §3 here | support off `main` (gap), closed by §5: the preregistration-order row uses its commit time. For identifying the r1 text it is provenance |
| commits `74610711`, `aa723017` | §1 here | provenance: they identify the texts the delta and confirmation reviews read |
| commit `b7e29ea7` (`REPORT.md`) | §1 here | support off `main` (gap), closed by §5: the authoritative report |
| the commit adding this file | — | support off `main` (gap), closed by §5: this record's own content |
| pin `13c05b4f`, Main and SM line citations | report header, throughout | support on `main`: `13c05b4f` is an ancestor of `main` at `650c8053`, and `papers/Main.md` and `papers/SM.md` are unchanged between them |
| SMD-SRC-1, unit A and lane 2 records | throughout | support on `main`: unchanged between the pin and `650c8053`; used as model-reviewed inputs, named where used |
| Ross 2011, Theorem 3.5 "as recalled in [S]"; Rosiński and Żak; Dudnikova, Komech and Spohn (2003); textbook facts (Kronecker, Wiener's lemma, the ergodic theorem, Cramér's decomposition theorem, mixing of Bernoulli actions and their factors, the Stein-equation bounds) | report §2–§4 | external literature or textbook results: Ross only for comparison; Rosiński and Żak not used by this report's results; H-αCLT is a stated hypothesis, not a pinned source; the textbook facts are cited by name |
| #1049, #1217, #1169 | headers | provenance: accountability and routing |

**Support off `main` (gaps), and how they close.** Each is closed when the merge commit of §5 lands
with the commit reachable from `main`; none is closed before that, and keeping the branch does not
close it: `98172765` (the plan and its order), `22347bb9` (its commit time), `b7e29ea7` (the
authoritative report), and the commit adding this file. With these, the tracing is complete:
every reference is classified, and no gap remains once §5's merge lands.

## 5. Landing condition

The record is preserved only through a **merge commit, not a squash**, which keeps reachable from
`main`: `98172765`, `22347bb9`, `74610711`, `aa723017`, `b7e29ea7`, and the commit that adds this
file, which follows `b7e29ea7` and adds only this file. That `PLAN.md`'s commit precedes every
report commit is part of the record's provenance. The merge needs the owner's separate approval
(§A.50 item 1), which the pending consolidated decision may give; the owner's decision of
2026-11-27 states that "no merge is authorized yet".

## 6. Preservation rationale

The investigation answers the open question SMD-SRC-1 left: whether the clustering its Theorem P
needs can be sourced from the substratum, and whether K1 or K0 suffices. It used a plan committed
before the report, and its negative results are scoped:
- the specified substratum supplies no state meeting the fixed set, under (B) and (H) for the
  selected measure and under (H′) for the energy-shell ensemble, and the remaining sources rest on
  an open obligation of SM; so SMD stays physically unsourced and clustering stays a condition on
  the state;
- the K0 route is ruled out within the stated scope, by an explicit witness;
- the K1 gap is narrowed to singular resonant cumulants.

The record is substantive and nonredundant with SMD-SRC-1, unit A and lane 2: SMD-SRC-1 traded SMD
for clustering, and this record tests that trade against the substratum and against the weaker
notions. It narrows the search for a physical mechanism, which the owner set as the scientific
priority (#1169 comment 7209325168; Goal link #914, #1217). Its reviews are those of §1, its
§A.42 item 8 tracing is complete (§4), its accountable Issues are #1049 and #1217, and each open
gap carries a remediation plan (§3).

## 7. Standing of this record

Preservation establishes no claim (§A.46 item 1). The model reviews are evidence of review, not
independent mathematical verification, and landing the record does not change any result's
evidence layer. No premise is adopted, no SMD successor investigation is opened, and nothing is
proposed for the manuscripts.
