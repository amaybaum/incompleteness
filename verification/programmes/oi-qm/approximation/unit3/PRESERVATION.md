# OI-QM-APPROX-1, unit 3 (O2): preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it. Evidence
layer of every result: this unit's mathematical derivation on paper [A], checked by model reviews
only. No computation was run and no Lean was built.

## 1. The record preserved

**Authoritative report: `REPORT-r3.md`**, revision r3, at the commit that adds it on
`research/i1216-approx-composition-20261126`. It applies the required correction N1 of the delta
review (the first case of (Hg) in Lemma 7η is proved by Corollary 7c's argument for each (F, ρ)).
It is otherwise identical to `REPORT-r2.md`, apart from its title and its one-line revision note.

**Superseded, kept unchanged:**
- `REPORT.md` (r1), commit `9d5b5dc15e2e218ffe4ea43e10d624083f87c438`;
- `REPORT-r2.md` (r2) and `CHANGES-r2.md`, commit `6e20b6cbb32a68f733e54b47bccdc3b6f1740516`.

`CHANGES-r2.md` maps r1 to r2. The revision note of `REPORT-r3.md` maps r2 to r3.

**Not superseded:** `PLAN.md`, commit `92969d74ba364af5fecff1524ca9e4809e700dbf`. It fixes the
following before any result:
- the η-model;
- the questions;
- the decision rule;
- the controls C0, C1 and CC;
- the baseline S and the productivity test;
- the stopping rule;
- the Goal link.

**Accountable Issue:** #1216 (OI-QM-APPROX-1); programme #1169. Guiding pull request: #1596.
Pinned source: `main` = `353a066f18766837fed8c7f58507e09ff549b1a4`.

**Owner decisions** (each a #1169 comment posted from the account `amaybaum`, quoting the owner):
- **Comment 7189139613** (created 2026-11-26T10:16:17Z; owner decision received
  2026-11-26T10:16Z), item 2, lane 2: "Approximate composition (#1216) — Determine whether the
  stability results survive approximate preparation, readout and feed-forward." Acceptance
  criterion: "Obtain an explicit stability bound, a counterexample or a precisely identified
  obstruction. Preserve the distinction between the history and correspondence metrics." Item 3:
  "Do not authorize computation or adopt additional premises through the new research units."
- **Comment 7190274734** (created 2026-11-26T11:06:26Z; owner decision received
  2026-11-26T11:06Z), item 1:
  - "Approve final acceptance and preservation of units A, B and C, at their independently
    reviewed revisions, under §A.46 item 8."
  - Row B: "B — Approximate composition (#1596) | Accepted | Apply the required correction. Leave
    the three optional nits unapplied."
  - "Where a correction changes a scientific statement, ensure that the authoritative preserved
    record states the corrected result unambiguously rather than leaving a misleading assertion
    in place."
  - "Complete the proposed accuracy checks, integration with main and exact-head CI. Return for
    separate merge approvals."

**Independent non-author reviews.** These are model reviews by a Claude reviewer agent that wrote
none of the reviewed work. They are evidence of review, not independent mathematical verification
(§A.46 item 8).
- **PR #1596 comment 7189898722**, review of r1 at `9d5b5dc1`: REVISE (minor), findings F1–F9.
  Applied in r2.
- **PR #1596 comment 7190026508**, focused delta review of r2 at `6e20b6cb`, by the same reviewer
  agent, resumed: ACCEPT WITH NITS.
  - It confirms F1–F8 resolved, and Corollary 7c and the τ_min form of Lemma 7η under adversarial
    checking.
  - It confirms that the converse is not described as disproved.
  - It confirms the gem verdict.
  - Nit N1 is applied in r3. Nits N2–N4 are optional and recorded in §7, not applied.
- No review covers r3 itself. r3 differs from the reviewed r2 only by the N1 paragraph in §5.2,
  its title and its revision note.

## 2. Substantive result and its precise scope

All results hold inside the given complex matrix kinematics of Main:572, at fixed (d, m, K), with
the δ-forms, the metrics M_H and M_C and the horizon (exactly K) of unit 2 unchanged. The six
structure rules hold only to accuracies η_r, as fixed in `PLAN.md` §2. No result bears on the
derivation of the kinematics.

- **Direction 1, both metrics (Theorems 3η and 4η).** Assume C_δ[max(m, 2), Λ₁(n, m)] with
  δ(N(m+1)+1) < 1, and the η-rules (e) at level 2, and (c) and (b) at level L = n·2^k. Then
  M_H ≤ M_C ≤ ½((1+ε₁)^K − 1), where:
  - ε₁ = max(ε_s, ε_c(η));
  - ε_s = δ(4N(m+1)+3) does not depend on η;
  - ε_c(η) = (1+β)^D − 1 + η_c(L)Σ_{j=0}^{D−2}(1+β)^j + η_b(L) + δ, with β = δ + 2d·η_e(2) and
    D = 3k + 1.

  System histories, which also assume the η-rules (d1) at r = 1 and (f), add
  (1 + ε_c|_{n=1})η_d(1) + η_f. The bound tends to 0 as (δ, η) → 0. Under
  M_H it is obtained only through M_H ≤ M_C. Whether an η_r can be removed under M_H is open.
- **Converse under M_C where the padding-defect floor is 0 (Corollary 7c; the verbatim case of
  Theorem 8η).** At a level with τ_min = 0, unit 2's Lemma 7 holds verbatim for every pair of
  correspondences with terms at most ε ≤ 1/48: ‖F − c(F)‖ ≤ 160ε and ‖c′(J) − J‖ ≤ 184ε. Where
  τ_min = 0 at every level of Λ, C_{184(N_Λ+1)ε}[m, Λ] holds. No hypothesis on the norm g of the
  test families is needed.
- **Converse under M_C in general (Lemma 7η, Theorem 8η).** For correspondences satisfying (Hg),
  κ = 88ε + 16(6ε + ω′(τ_min)g), and C_{(N_Λ+1)κ_Λ}[m, Λ] holds. The bound tends to 0 exactly
  when ω′g → 0. That is guaranteed under an a priori norm bound or a crude validity bound V_{δ0};
  when g depends on ε it is a condition of type B2. m, K ≥ 2 and the level-set condition remain
  necessary.
- **Obstruction (B4).** For bounds uniform over class(η) at a fixed η > 0, and for single
  theories with a positive padding-defect floor τ_min and for which ω′(τ_min)·g is not small, the padding's trace defect multiplies the
  output norms of the test families. No hypothesis of Lemma 7 bounds those norms a priori. The
  bootstrap leaves the branch g ≳ 1/(8(3K−4)τ_min) unexcluded.
- **The converse is not disproved.** The uniform converse remains open (O2-a). Every
  "disproved" in the report refers to Direction 2 under M_H (Theorem 5, transferred to every
  η-class by control C1).
- **Q3.** For theories satisfying the rules in closure, (a) ⇒ (b) and (b) ⇒ (a) of the analogue of
  Corollary 10 are each proved, as separate statements.
- **Controls.** C0 (η = 0 reproduces unit 2's bounds and hypotheses symbol by symbol), C1 and CC
  (T_triv) are green.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Every result is [A], checked only by the model reviews of §1. The results are reviewed paper
derivations, not independently verified theorems (owner decision at #1169 comment 7189139613,
item 3). The remediation plan below authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| Q0η: (M1)–(M3), Lemma E, C1, CC (T_triv) | report §1 | partially verified: hand derivation, reviewed by both reviews | independent non-model review; exact finite controls of T_triv's distances | #1216 | a recorded independent review; controls under an authorization that covers computation |
| Direction 1 (Theorems 3η and 4η, Lemma B) | report §3–§4 | partially verified | independent review; O2-b (necessity of the factor 2d), O2-c (M_H sub-question) and O2-e (lower bound) open | #1216 | a recorded independent review; a derivation for O2-b, O2-c or O2-e |
| Lemma 7η and Theorem 8η (conditional on (Hg)), Lemma P, Lemma V | report §5.2, §5.4 | partially verified | independent review | #1216 | a recorded independent review |
| Corollary 7c, the τ_min form of Lemma 7η, the verbatim case of Theorem 8η, the convergence clauses, §6 | report §5.2, §5.4, §6 | partially verified: reviewed by the delta review only; the N1 paragraph of r3 is unreviewed | independent review | #1216 | a recorded independent review |
| The obstruction of §5.3 (O2-a) | report §5.3 | open: obstruction to the argument, not a disproof | an a priori norm bound, or a counterexample with τ_min > 0 and g of order 1/τ_min | #1216 | a written derivation or counterexample |
| Inherited unit 2 inputs [U2] | report §8 | partially verified (unit 2's preservation record) | as recorded there | #1216 | as recorded there |
| Preregistration order (PLAN.md before the report) | `PLAN.md` | evidence is commit order only: `92969d74` at 10:33:20Z before `9d5b5dc1` at 10:43:31Z on 2026-11-26; both committed by the coordinating session | none available from commit order alone | #1216 | none; the limitation stands as stated |
| D1, the construction T_s (review-originated, not in the report) | §7 here | partially verified: derived in the delta review, checked by the writer | independent review | #1216 | a recorded independent review |

## 4. Off-`main` references (§A.42 item 8)

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7189139613, 7190274734 (owner decisions); 7189143747 (synthesis) | `PLAN.md`, report headers; §1 here | provenance: authority records quoted with author and time; no result uses them |
| PR #1596 comments 7189898722, 7190026508 (reviews) | report headers and §8; §1 and §7 here | provenance: evidence of review. The argument of Corollary 7c originates in finding F1 of 7189898722; its proof is written in `REPORT-r3.md` §5.2. D1 originates in 7190026508; its statement and the writer's check are written in §7 here |
| PR #1584 comments (unit 2 reviews) | report §8 | provenance: no claim uses their content |
| commits `9d5b5dc1` (REPORT.md) and `6e20b6cb` (REPORT-r2.md, CHANGES-r2.md), superseded | report headers; §1 here | provenance for every result: cited to identify the earlier texts. `9d5b5dc1` is also support, on `main` once the merge of §5 lands, for the preregistration-order row (§3), through its commit order |
| commits `92969d74` (PLAN.md), the commit adding `REPORT-r3.md` and the commit adding this file | report headers; §1 here | support on `main` once the merge of §5 lands: the record's own content; not before |
| commit `b1037933` (unit 2 REPORT-r3.md) and unit 2's PLAN.md and PRESERVATION.md | report §8 | support on `main`: ancestors of the pin `353a066f` |
| commit `353a066f`, Main line citations, OB/ Lean citations | report header, §1–§8 | support on `main`: the pin is `main`'s head at drafting |
| #1216, #1169, #945, #1211 | report §9–§10 | provenance: routing and accountability |

Support off `main`: none.

## 5. Landing condition

The record is preserved only through a merge commit, not a squash. The merge must keep reachable
from `main`:
- `92969d74`, `9d5b5dc1` and `6e20b6cb`;
- the commit adding `REPORT-r3.md`;
- the commit adding this file.

`PLAN.md`'s commit before any report commit is part of the record's provenance. Per the owner
decision of 2026-11-26T11:06Z, preservation includes integration with current `main`, accuracy
checks and exact-head CI. Merging needs the owner's separate approval (§A.50 item 1).

## 6. Preservation rationale

Unit 2 left open node O2 ("approximate structure rules") and marker W2: its stability results
used the six structure rules of Main:572 exactly. This record brings O2 to a status at fixed (d, m, K):
B1 for Direction 1; the converse verbatim where τ_min = 0; B4, with O2-a open, for bounds uniform
over class(η) at fixed η > 0. The preregistered metrics M_H and M_C are kept apart:
- **Direction 1** survives relaxation of every rule, with an explicit bound, and its soundness
  part does not depend on the rules.
- **The converse under M_C** survives verbatim wherever the paddings come arbitrarily close to
  trace preservation.
- **Otherwise the converse** meets a precisely identified obstruction: exact trace preservation
  of the padding supplies an a priori norm control that no hypothesis states (marker W4).
- The record classifies Lemma 7η and the obstruction as NEW. The result is substantive,
  nonredundant and scoped. It feeds the owner's successor question, "Can uniform norm control be
  derived from physically meaningful observer constraints?" (#1169 comment 7190274734, item 4).

## 7. Optional nits of the delta review, recorded and not applied

Per the owner decision of 2026-11-26T11:06Z ("Leave the three optional nits unapplied"):

- **N2.** §6 (b) ⇒ (a) uses only the padding rules in closure: (b) and (e) at each level, and (a)
  or (e), (d1) and (f) on the system. The hypothesis "all rules in closure" is correct but
  stronger than needed.
- **N3.** The label line of r2 and r3 drops "unreviewed" from [A]. The items new in r2 (τ_min,
  Corollary 7c, the convergence clauses) were reviewed only by the delta review, and the N1
  paragraph of r3 by none. §3 above records this.
- **N4 (D1).** Label [R]: a derivation originating in the delta review (PR #1596 comment
  7190026508), checked by the writer on paper. It is not part of the report.
  - *The construction.* For s > 0, let T_s be exact finite QM rescaled:
    - its available families at every level and on the system are exactly the (1+s)·J, for J a
      quantum instrument;
    - its available preparations are exactly the (1+s)·P, for P completely positive and trace
      preserving from the system into a level.
  - *T_s satisfies every η_r-rule with η_r ≤ s(1+s).* Every norm involved is 1:
    - (a), (d1) and (e) hold within s;
    - (b) holds exactly;
    - (c), (d2) and (f) hold within s(1+s), since the exact composite is (1+s)² times an
      instrument or a channel, and (1+s) times it is available.
  - *τ_min = s at every level and on the system.* Every available single-outcome family is
    (1+s)Φ with Φ a channel. For every channel D and density ρ,
    ‖(1+s)Φ − D‖_{1→1} ≥ |tr((1+s)Φ(ρ) − D(ρ))| = s, and D = Φ attains s.
  - *Consequences.*
    - For every η with each η_r ≥ s(1+s), class(η) contains a theory with τ_min > 0. So the scope
      of §5.3, "bounds uniform over class(η) at fixed η > 0", is not vacuous.
    - T_s is not a counterexample to Lemma 7. Its test families have norm about 1 + s, and V_s
      holds, so for s and ε small enough sufficient condition (ii) gives (Hg).
    - O2-a is unchanged.
