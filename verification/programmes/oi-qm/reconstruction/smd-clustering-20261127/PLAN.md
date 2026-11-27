# SMD-CL-1: sourcing the clustering of Theorem P; K1 and K0 (#1049, #1217). Plan

**WIP / UNVERIFIED. Model-written research plan, paper-only. Nothing here is adopted, proposed for
the manuscripts or authorized beyond the investigation's scope. This file fixes the questions, the
decision rule, the controls and countercontrols, the stopping conditions and the Goal link. It is
committed alone, before the report, and contains no result. It is recorded, not frozen; it is not
a frozen preregistration under §A.39 or §A.50 item 5.**

**Chronology disclosure.** Before writing this file the writer had written SMD-SRC-1
(`../smd-sourcing-20261126/`, landed via #1612) and read, for this unit: the owner decision quoted
below; Main's Lemma 3, its measure Remark and status Remark (Main:54–60) and the posit ledger
(Main:736); SM:130, SM:226, SM:232, SM:290–296, SM:312–316. While reading, the writer formed,
without writing or checking them, candidate directions: that the selected (counting) measure is a
product measure whose observer image is symmetric; that linear dynamics conserves a spatially
averaged energy density; and that phase-locked plane waves might give a non-mixing ergodic
witness. Every outcome class below is admissible.

- **Accountable Issues:** #1049 and #1217; programme #1169. Predecessor record: SMD-SRC-1.
- **Authorization:** owner decision (account `amaybaum`, #1169 comment 7208939261, created
  2026-11-27T03:22:49Z; decision "Proceed as suggested", received 2026-11-27), unit 3: "SMD
  clustering (#1049 and #1217, follows #1612). Whether the required cumulant clustering can be
  sourced from the substratum dynamics, including the open K1 and K0 on 0 < |μ| < 1." Rules quoted
  there: "paper-only; preregistered plan committed before any derivation; no premise adopted
  (AGENTS.md sections A.29 and A.50 item 6); independent non-author review; preservation only by
  a separate owner decision." Operations under work package WP-2 (#1169 comment 7199704501).
- **Goal link (§A.47).** Serves #1049 and #1217 (tier Foundational). It decides (i) whether the
  clustering hypothesis that SMD-SRC-1 traded SMD for is supplied by the substratum dynamics and
  measure as Main and SM specify them, or remains a condition on the state; and (ii) whether
  stationarity with translation mixing (K1) or ergodicity (K0) forces SMD on 0 < abs(μ) < 1. It
  does not decide any manuscript wording, H-ZM, the coarse-graining bridge, or the adoption of any
  premise.
- **Pinned main commit [P]:** `13c05b4fe666c2e128eed1213874be9b8208982d`.
- **Writer:** the designated writer of this unit; branch `research/smd-clustering-20261127`. No
  push and no GitHub write by the writer.

## 0. Labels and fixed set

Labels as in SMD-SRC-1 PLAN.md §0 ([A], [W], [I], [U-A], [L2], [C]; statuses proved / conditional /
posited / open), plus [S]: a result of SMD-SRC-1's REPORT.md (reviewed paper derivation, partially
verified). The fixed set and the notions K0–K3, Kα, and SMD are as in SMD-SRC-1 (PLAN.md §1–§2;
REPORT.md §1.2, with uniformly bounded moments and the distance-indexed α of H-αCLT).

## 1. Questions

- **Q1 (sourcing).** Does the substratum, as Main and SM specify it — the finite bijective
  representative, the second-order linear update mod q (Main posits (vii), (xiii)), the selected
  counting measure (Lemma 3; posit (iv)), and the stated observer-level branch with its labelled
  conditional inputs (the coarse-graining bridge of SM:232, Proposition 4b's hypotheses) — supply an
  observer-level state that is F-stationary, K2- or K3-clustering with uniformly bounded moments, and
  meets the fixed set (in particular distinct block values)?
- **Q2 (K1).** On Z^d, 0 < abs(μ) < 1: does L-SDS with K1 and the fixed set force SMD? Positive
  result, obstruction, or a sharpened gap.
- **Q3 (K0).** The same with K0.
- **Q4 (imports).** Check [I-Stein] and H-αCLT against their sources where possible. No external
  access is used (§A.50 item 4); where a source cannot be read, a self-contained re-derivation
  counts as the check, and otherwise the import stays as labelled.

## 2. Decision rule (fixed before any result)

**Q1.**
- **SOURCED** iff a derivation from Main/SM premises, with only labelled conditional inputs already
  in the corpus, yields an observer-level law meeting L-SDS, K2 or K3 and the fixed set.
- **NOT SOURCED (obstruction)** iff it is shown that the specified measure and dynamics cannot
  yield such a law, under stated conditional inputs.
- **REDUCED** iff the requirement is shown to rest on a named input not supplied by Main/SM (for
  example a preparation datum), without a derivation either way.
- **OPEN** otherwise. Outcomes may combine (different readings of the measure), each with scope.

**Q2, Q3** (per notion, on 0 < abs(μ) < 1), exactly as SMD-SRC-1 PLAN.md §3: POSITIVE iff a proof;
OBSTRUCTION iff a witness meeting L-SDS, the notion and every premise of the fixed set with
Stab(ρ) ⊊ Stab(C), with an itemized witness check; OPEN otherwise, with the gap.

**Q4.** Per import: re-derived / checked against source / unchanged (stated).

Verdict sentences are generated from these assignments and printed only over green controls. No
outcome is preferred.

## 3. Controls and countercontrols

- **CC-W (witness check).** Every witness carries an itemized table against L-SDS, every premise of
  the fixed set, each clustering notion and SMD; a missing line voids it.
- **CC-R (resonance or locking is load-bearing).** For any non-Gaussian stationary witness, show the
  line at which F-stationarity would fail if the phase relation it uses were broken.
- **CC-M (consistency with SMD-SRC-1).** A K0 or K1 witness must violate K2 (else it contradicts
  Theorem P [S]); a positive result for K1 or K0 must not apply to SMD-SRC-1's ρ_K (non-ergodic)
  or to ρ_D at μ = 0.
- **CC-T (positive control).** Any new structural lemma on cumulants must reproduce Theorem P's
  conclusion on the class where Theorem P holds.
- **CC-S (sourcing countercontrol).** An obstruction to Q1 must identify what the specified measure
  does supply (so that "not sourced" is not a relabelling of a trivially absent property), and must
  state which conditional input it uses.
- **CC-E (exact computation).** Any identity certified by computation uses exact arithmetic,
  with code and output recorded here; floating point illustrates only.
- **CC-P (pin).** Quoted lines are re-read at [P].

**Skepticism (§A.31).** A result favourable to the framework (SOURCED, or POSITIVE for K1/K0) is
pressure-tested against CC-M and against the selected measure's symmetry before acceptance.

## 4. Productivity test (§A.31)

The unit is a gem iff it yields at least one of: (G1) a Q1 outcome other than OPEN, with its
conditional inputs named; (G2) POSITIVE or OBSTRUCTION for K1 or K0; (G3) an import re-derived or
checked. Non-gems: restating SMD-SRC-1's open nodes; relabelling.

## 5. Stopping conditions

Stop when the first holds: every question is assigned under §2 with controls run; a bounded effort
of the order of SMD-SRC-1 is exhausted (the remaining gap stated); a result would need a premise
outside the fixed set and the stated conditional inputs (recorded; adoption is the owner's, §A.29,
§A.50 item 6). Halt (no verdict) on a failed control, a provenance anomaly (§A.26), or a positive
and an obstruction for the same notion and range.

## 6. Exclusions and review

No manuscript, ledger, census or registry edit; no edit of earlier records; no premise adopted,
weakened or changed; no frozen procedure, trial, dispatch or Lean build; no push and no GitHub
write. The report is reviewed by an independent non-author reviewer at an exact commit (controls,
claim/evidence boundary, §A.34 directions, verdict generation, §A.42 item 8 tracing). A model
review is evidence of review, not independent mathematical verification (§A.46).

Deliverables: this PLAN.md as its own commit; then REPORT.md with the assignments and generated
verdict, labelled premises, scopes, controls, open nodes, §A.42 item 8 tracing and a §A.46 item 4
table.
