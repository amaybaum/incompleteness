# OI-QM-APPROX-1, unit 2 (G3-D14): preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it. Evidence
layer of every result: this unit's mathematical derivation on paper [A]. No computation was run.

## 1. The record preserved

- **Authoritative report:** `REPORT-r3.md` (revision r3, commit
  `b10379335d8c36207f10cff476991a8daaa3210e`). It supersedes `REPORT.md` (commit
  `99e8e49843aa9a649f8a7c81928dd4ad4602c993`) and `REPORT-r2.md` (commit
  `f257597b086d69cf98e6383d59ad72166f61c1e1`), which are kept unchanged. `CHANGES-r2.md` and
  `CHANGES-r3.md` map the revisions. `PLAN.md` (commit `d2fd361ebd2aff7f5d9ade027c55f3cf1f5c133d`)
  fixes the questions, the metrics M_H and M_C, the horizon (exactly K), the δ-forms, the
  productivity test and the stopping rule before any bound, and is not superseded.
- **Citation correction.** `REPORT-r2.md` and `CHANGES-r2.md` cite the first review as a comment on
  #1169; it is PR #1584 comment 7184945033 (`CHANGES-r3.md`). `CHANGES-r3.md` lists only the
  substantive changes; the final review found `REPORT-r3.md` editorially reflowed throughout, with
  no other change to any statement, hypothesis, constant or status.
- **Accountable Issue:** #1216 (programme #1169). Guiding pull request: #1584.
- **Owner decisions** (each a #1169 comment posted from the account `amaybaum`, quoting the owner):
  - comment 7186638587 (created 2026-11-26T08:28:33Z; owner decision time stated as
    2026-11-26T08:28:18Z), item 7, #1216: "Approve all five nits and confirm the mathematical
    content missing from the recorded decision". Symbols of that item were lost in storage; the
    bound "288ε, ε ≤ 1/64" survives, and the values m = 1 and K = 1 are those recorded in
    `REPORT-r3.md` and the final review. The stored item also asks to restore "the stated
    normalization" without showing which normalization it means; the final review notes this, and
    it is not identified here.
  - comment 7187418279 (created 2026-11-26T09:05:58Z; owner decision received 2026-11-26T09:05Z),
    item 3, Lane 3: "If that verdict is ACCEPT or ACCEPT WITH NITS, and explicitly confirms
    Proposition 11's proofs and the corrected bounds, authorize acceptance and preservation of r3."
    The condition is met by PR #1584 comment 7186807685 (below).
- **Independent non-author reviews** (model reviews by a Claude reviewer agent; evidence of review,
  not independent mathematical verification):
  - PR #1584 comment 7184945033, review of r1 at `99e8e498`: REVISE (minor).
  - PR #1584 comment 7185177023, focused delta review of r2 at `f257597b`: ACCEPT WITH NITS.
  - PR #1584 comment 7186807685, focused delta review of r3 at `b1037933` with the owner's required
    confirmations (#1169 comment 7186783427, created 2026-11-26T08:35:39Z): ACCEPT WITH NITS. It
    confirms the strict hypothesis, the Lemma 7 padding argument, both negative cases of
    Proposition 11, the corrected bound of Corollary 10 and the preservation of both preregistered
    metrics and the horizon. Comment 7186790779 is an earlier version of the same review (same
    verdict and findings, SHA-256 prefix `335f9797` against `97e3664c`), without the owner's
    confirmations section.
  - Each delta review was given that reviewer's previous reviews of this record.

## 2. Substantive result and its precise scope

All results hold inside the given complex matrix kinematics of Main:572, with the six structure
rules exact, at fixed (d, m, K); none bears on the derivation of that kinematics. Every conclusion
names its metric, M_H or M_C as fixed in `PLAN.md` §2, at horizon exactly K.

- **Q0 (§1).** No δ-form refers to the quantum instrument set. Proposition 1: the δ-forms for
  every δ > 0 do not imply the exact conditions (T_alg).
- **Direction 1 (Theorem 4; Theorems 2–3).** C_δ[max(m, 2), Λ₁(n, m)] with δ(N(m+1)+1) < 1
  implies M_H ≤ M_C ≤ ½((1+ε₁)^K − 1).
- **Direction 2 under M_H (Theorem 5, Lemma 6): disproved.** T_dec has M_H = 0 at every level and
  for every (m, K), while I_δ fails for every δ < 1/2 at every level n with N = d·n ≥ 2.
- **Direction 2 under M_C, m ≥ 2 and K ≥ 2 (Lemma 7, Theorem 8).** Under the strict hypothesis
  M_C(T, Q) < ε ≤ 1/48: ‖F − c(F)‖ ≤ 160ε for every available F with at most m outcomes and
  ‖c′(J) − J‖ ≤ 184ε for every quantum instrument J with at most m outcomes, κ = 184ε; on a level
  set Λ containing every level the δ-forms reference, C_{δ(ε)}[m, Λ] holds with
  δ(ε) = 184(N_Λ+1)ε.
- **Proposition 11.** M_C(T_dec, Q) = 0 at K = 1 (every m) and at m = 1 (every K), while
  C_δ[m, Λ] fails for every δ < 1/2 whenever Λ contains a level n with d·n ≥ 2 and the level 2n:
  Direction 2 under M_C is disproved at m = 1 and at K = 1.
- **Proposition 9.** A metric M_C that omits a level L ≥ 2 does not bound U_δ at L.
- **Corollary 10 (M_C, m ≥ 2, K ≥ 2, all levels and the system).** C_δ[m] for every δ > 0, M_C = 0,
  and "available sets lie in the quantum instruments with closure equal to them" are equivalent.
  (b) ⇒ (a) is applied instance by instance with ε ≤ min(1/48, δ/(184(N_i+1))); for instances of
  V, U, C and L, N_i = 1 and ε ≤ min(1/48, δ/368). At m = 1 or K = 1, (b) implies neither (a) nor
  (c).

## 3. Verification status and remediation (§A.46 items 4 and 8)

Every result is [A], checked by the model reviews of §1. In #1169 comment 7185038641 the owner's
assessment table lists Theorems 4 and 5 as "Independently verified"; §A.46 item 8 classes a model's
acceptance as evidence of review, not independent mathematical verification, and the status below
follows item 8. The remediation plan below authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| Q0 and Proposition 1 | §1 | partially verified: hand derivation, model-reviewed | independent non-model review; Lindemann–Weierstrass checked by the first review by recall only | #1216 | a recorded independent review |
| Direction 1 (Theorems 2–4, §3.4) | §2–§3 | partially verified | independent review; N2 (Choi bound, used in Theorem 2) checked by the first review by recall only; O1 (optimal soundness constant), O2 (approximate structure rules) open | #1216 | a recorded independent review; a derivation for O1 or O2 |
| M_H converse (Theorem 5, Lemma 6) | §4.1 | partially verified | independent review | #1216 | a recorded independent review |
| M_C converse (Lemma 7, Theorem 8, Proposition 9) | §4.2, §4.4 | partially verified; constants confirmed by the final review | independent review; N3 (used in the I-clause of Theorem 8) checked by the first review by recall only; O4 (level-uniform converse), O9 (optimal constant) open | #1216 | a recorded independent review; a derivation for O4 or O9 |
| Proposition 11 | §4.3 | partially verified; both cases confirmed by the final review | independent review | #1216 | a recorded independent review |
| Corollary 10 and the "Outside m ≥ 2, K ≥ 2" paragraph | §5 | partially verified; final-review finding 1 recorded, not applied: the m = 1 argument for (a) ⇒ (b) does not write the system case, for which the review gives a one-sentence argument through L_δ; no status is affected | independent review; that sentence | #1216 | a recorded independent review, or a revision adding the system case |
| Preregistration order (PLAN.md before the report) | `PLAN.md`, §5 below | evidence is commit order only: `d2fd361e` at 06:39:34Z, `99e8e498` at 06:46:33Z; the report was committed by the coordinating session (first-review observation 8) | none available from commit order alone | #1216 | none; the limitation stands as stated |
| Open nodes O7 (other preparations); O5, O6 outside this unit; O8 (#945) | §8 | open | derivation or refutation | #1216; #1169, #1211 for O5; #945 for O8 | a written derivation or counterexample |

## 4. Off-`main` references (§A.42 item 8)

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7184425769, 7185038641, 7186638587, 7186783427, 7187418279 (owner decisions) | `PLAN.md`, report headers; §1, §3 here | provenance: authority records quoted with author and time; no result uses them |
| PR #1584 comments 7184945033, 7185177023 (reviews of r1 and r2) | report header, report §6 | provenance: evidence of review. The Lemma 7 padding route and the Proposition 11 construction originate in the first review (credit, report §6); the proofs used are written in `REPORT-r3.md` §4.2–§4.3 |
| PR #1584 comments 7186790779, 7186807685 (review of r3) | §1 here | provenance: evidence of review; no result uses them |
| commits `99e8e498` (REPORT.md) and `f257597b` (REPORT-r2.md), superseded | report headers | provenance: cited only to identify the earlier texts |
| commits `d2fd361e` (PLAN.md), `b1037933` (REPORT-r3.md, CHANGES-r3.md) and the commit adding this file | report headers; §1 here | support on `main` once the merge of §5 lands: the record's own content; not before |
| commit `b6c6b80b`, Main line citations, OB/ Lean citations | report header, report §1–§6 | support on `main`: `b6c6b80b` is an ancestor of `main` at `13f5c66a`; `papers/Main.md` differs between them only at lines 692, 716, 720 and 724, and every Main citation is at lines 572–610; `verification/lean-mathlib/` is unchanged |
| #1222, #1227, #1229, the F945-R note | `PLAN.md` §7, report §6 | provenance: named as not used |
| #945, #1211, #1216, #1169 | report §7–§8 | provenance: routing and accountability |

Support off `main`: none. Unit 1 r4b
(`verification/programmes/oi-qm/approximation/unit1/APPROX-UNIT1.md`) is on `main` and unchanged
since `b6c6b80b`; it is used for the labels D13, D14 and the motivation of M_C only.

## 5. Landing condition

The record is preserved only through a merge commit that keeps `d2fd361e`, `99e8e498`, `f257597b`,
`b1037933` and the commit adding this file reachable from `main`; `PLAN.md`'s commit before any
report commit is part of the record's provenance. Per the owner decision of 2026-11-26T09:05Z,
preservation includes integration with current `main` and exact-head CI. Merging needs the owner's
separate approval (§A.50 item 1).

## 6. Preservation rationale

Row D14 of unit 1's dependency matrix is recorded there as "open (not stated anywhere read)"
(`PLAN.md`). The report gives, at fixed (d, m, K) and under two preregistered metrics, an explicit
bound for Direction 1 (Theorem 4), a theory-level counterexample to Direction 2 under M_H (Theorem
5), a converse under M_C for m, K ≥ 2 with explicit constants and a necessary level-set condition
(Lemma 7, Theorem 8, Proposition 9), counterexamples at m = 1 and K = 1 (Proposition 11), and the
identification of what the δ-relaxation characterizes under M_C: the closure of the available sets,
not the sets (Proposition 1, Corollary 10). Its §7 classifies Theorems 4 and 5, Proposition 11,
Proposition 1 and Corollary 10 as NEW.
