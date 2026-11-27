# OI-QM-APPROX-1, UN-1: the identity partner in the converse under M_C

This plan is recorded before the derivation and is not frozen. Every question is **open** at this
commit. The writer explored informally during the predecessor unit, and that exploration is written
up only as the sketch in `../uniform-norm-control-20261126/REPORT-r4.md` §6. No derivation for
this unit had been written down when this plan was committed.

- **Accountable home:** #1216 (OI-QM-APPROX-1); programme #1169. This unit follows the
  uniform-norm-control record (`../uniform-norm-control-20261126/`, landed through #1614), open
  nodes UN-1 and UN-2 of `REPORT-r4.md` §7.
- **Authorization.** Owner decision recorded at #1169 comment 7208939261 (posted from the account
  `amaybaum` at 2026-11-27T03:22:49Z), quoting the owner's reply "Proceed as suggested" to the
  proposal: "Approved: under WP-2, paper-only investigations UN-1 (#1216), F-slice premise sourcing
  (#1217), and SMD clustering (#1049/#1217), each with preregistration, bounded stopping conditions
  and independent review." Standing work package WP-2 (#1169 comment 7199704501).
- **Writer:** an agent of the coordinating session. It writes nothing to GitHub. An independent
  non-author review follows the report.
- **Pinned source:** `main` = `13c05b4fe666c2e128eed1213874be9b8208982d`.
- **Goal link (§A.47).** Serves #1216 (Foundational). The unit decides whether the hypotheses of
  the converse of the finite-precision characterization under M_C (m, K ≥ 2, M_C < ε, class(η) at
  small η) control the identity partner φ, which by Theorem U of the predecessor is the single
  residual of that converse. It also decides whether the candidate "idle step" property follows
  from the existing structure or would be a new premise. It does not decide whether OI supplies the
  structure rules or the δ-conditions.

## 1. Fixed setting and notation (inherited, unchanged)

The following are as fixed in `../unit2/PLAN.md`, `../unit3/PLAN.md` and
`../uniform-norm-control-20261126/` (PLAN.md and REPORT-r4.md):
- the carrier, the levels and the system, and the given kinematics;
- the history class (horizon exactly K, outcome bound m, input densities, exact classical
  control), TV, and M_C with its quantifier order;
- the norms; the η-model class(η), with its six rules (a)–(f) and τ_min;
- c, c′, Φ := c′(P), Ψ := c(Φ), c̃, A_E, C_ρ, C_G, κ_cov and κ_snd;
- φ(c′) := ‖Φ − id‖_{1→1}, and φ_min, the infimum of φ over admissible c′.

Lemmas R and I, Theorem G, Corollary G1, Lemma 7G, Theorem U, Prop S, Props X1 and X2, CC-s and
CC-p are used as stated there [UNC]. M_H is not used.

## 2. Questions

| ID | Question | Status |
| --- | --- | --- |
| Q-A | Under m, K ≥ 2, M_C < ε and T in class(η), is there an explicit φ_bound(ε, η, d, n, m, K) with φ_min ≤ φ_bound and φ_bound → 0 as (ε, η) → 0? Answer on the system and at levels separately | open |
| Q-B | If not, can the hypotheses be met with φ(c′) bounded away from 0 for every admissible c′, at arbitrarily small (ε, η)? (This is CC-L, or a bounded-norm analogue of it inside class(η)) | open |
| Q-C | Does an idle step at each level (an available single-outcome family within η_id of the identity, with η_id → 0 as η → 0) follow from the six η-rules and M_C < ε? Answer at levels and on the system separately | open |
| Q-D | Is the obstruction, if any, one of the hypotheses' scope (system versus levels; which rules enter)? | open |

Each direction of any equivalence is a separate question (§A.34).

## 3. Decision rule (fixed now, outcome-neutral)

Q-A and Q-B together end in exactly one of the following.
- **D1, controlled.** An explicit φ_bound → 0, proved, with every hypothesis and rule named. The
  predecessor's Theorem U then gives the converse with explicit constants on that scope.
- **D2, controlled on a reduced scope.** D1 holds on a stated subset (for example the system, or
  levels with a stated rule), and the rest is open or obstructed.
- **D3, broken.** An explicit theory in class(η), for arbitrarily small (ε, η), meeting every
  hypothesis, with φ(c′) ≥ c > 0 for every admissible c′. Status: disproved for that class only.
- **D4, obstruction.** Neither: the failing step and the unexcluded branch are stated.

Q-C ends in exactly one of the following:
- **derived** (proved from the η-rules and M_C < ε, with an explicit η_id);
- **not derivable** (a theory in class(η) meeting the hypotheses with no near-identity available at
  some level);
- **open**.

If a result needs a premise outside §1, it is recorded as a candidate premise, not adopted
(§A.29; §A.50 item 6), and the investigation stops there for that question.

## 4. Controls and countercontrols (fixed now)

- **C0 (exact QM).** At T = Q, c = c′ = id: φ = 0. Any φ_bound must be ≥ 0, and any idle-step
  derivation must return the identity.
- **C1 (scope).** No result may contradict unit 2's Theorem 5, Proposition 11 or Proposition 9,
  or the predecessor's Prop X2. In particular, any claimed φ_bound must fail for T_− = −Q, which
  lies outside class(η) at small η. A derivation that would also bound φ for T_− is void.
- **CC-p.** Any claim that law boundedness (F1) controls φ is tested against T_S with
  S^{-1} = C_p.
- **CC-L / D3 candidates.** A candidate is checked against every hypothesis as stated: each η-rule
  at its level, m, K ≥ 2, and both terms of M_C. A candidate that violates one is recorded as
  excluded, with the violated hypothesis.

## 5. Stopping conditions

Stop when:
- Q-A/Q-B and Q-C each reach a branch;
- or after a bounded effort (one writer session), with the gap stated precisely;
- or when a result needs a new premise, which is then recorded.

Favourable branches are pressure-tested before acceptance (§A.31).

## 6. Inputs and labels

- [UNC]: `../uniform-norm-control-20261126/REPORT-r4.md` and `PRESERVATION.md`, on `main`.
- [U2], [U3]: units 2 and 3, on `main`.

[UNC], [U2] and [U3] are reviewed paper derivations, not independently verified (§A.46 item 7).

- [L]: standard mathematics, recalled.
- [A]: this unit's own arguments, unreviewed.

No content off `main` is used as support (§A.42 item 8).

## 7. Boundaries

Paper-only. No premise adopted, no manuscript change, no frozen record edited, no push, no GitHub
write.
