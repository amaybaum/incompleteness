# COMPLEX-CARRIER-1, lane 2: preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it. Evidence
layer of every result: mathematical derivation on paper. No computation was run.

## 1. The record preserved

- **Authoritative report:** `REPORT-r2.md` (revision r2, commit
  `e814d5417616e798ff98115795e9cf46d9fdbb40`). It supersedes `REPORT.md` (r1, commit
  `77881879bc1b4df9156fe537e5ee9bd261345cf1`), which is kept unchanged; `CHANGES-r2.md` maps each
  r1 to r2 change to its review finding. `PLAN.md` (commit `143f359928698125f854b86e756ba827dc518064`)
  fixes the questions, productivity test and stopping rule before the work and is not superseded.
  The header of `REPORT-r2.md` records its status before the delta review; review and acceptance
  are recorded here.
- **Accountable Issue:** #1217 (parent #1211, programme #1169). Guiding pull request: #1585.
- **Owner decisions** (each a #1169 comment posted from the account `amaybaum`, quoting the owner):
  - comment 7186638587 (created 2026-11-26T08:28:33Z; owner decision time stated as
    2026-11-26T08:28:18Z), item 7, #1217: "Approve findings 1–10, including the corrected
    counterexample, definite-B restriction, dimensional limitations and range condition. Do not
    generalize the conclusions beyond their proved domain."
  - comment 7187418279 (created 2026-11-26T09:05:58Z; owner decision received 2026-11-26T09:05Z),
    item 3, Lane 2: "Accept r2 following the independent ACCEPT WITH NITS verdict. Authorize
    preservation under §A.46 item 8." and "Preserve all reviewed mathematical restrictions and scope
    narrowings. Do not promote the conditional sourcing of complex structure into an unconditional
    derivation from the fundamental substratum." and "Leave the two optional nits unapplied."
- **Independent non-author reviews** (model reviews by a Claude reviewer agent; evidence of review,
  not independent mathematical verification):
  - PR #1585 comment 7184957447, review of r1 at `77881879`: REVISE (minor), findings 1–10.
  - PR #1585 comment 7187069631, focused delta review of r2 at `e814d541`: ACCEPT WITH NITS. It
    confirms findings 1–10 fixed and the writer's three narrowings sound; it did not recheck r1
    passages that r2 leaves unchanged.

## 2. Substantive result and its precise scope

All results are conditional on LIN (linearity of the lift) and LIFT (existence of the real lift),
neither established here, and concern the observer-level real lift only. Nothing is claimed for the
fundamental Z/q level or for the bijection-level carrier of SM:505.

- **(i) Canonicity, carrier T (Theorem 1).** A complex structure commuting with F and tamed by ω
  exists iff E is positive definite, and is then unique, J_F = D(−D²)^(−1/2). Under a change of
  symplectic form ω_B (§2.3), uniqueness holds when B is definite on each frequency eigenspace;
  for B indefinite within a degenerate eigenspace the tamed commuting structures form a family S_t.
  Every conserved symplectic form with positive definite matched energy selects J_F.
- **(i) Carrier Z (Theorem 1Z).** A bounded such J exists iff abs(αμ) < 1/d; a closed densely
  defined one iff abs(αμ) ≤ 1/d; uniqueness is up to restriction of J_F.
- **Locality (Proposition 2).** Site-locality, F-commutation and cubic-equivariant taming never
  hold together; the pair F-commutation plus taming holds for abs(αμ) ≤ 1/d on Z, and on T for
  abs(αμ) < 1/d or restricted to V_rest. The decay rates of J_F are at derivation-sketch level.
- **(ii) Null modes at α = 1/d.** On T, J fails on the null sector (Proposition 3); with b = 0
  stationary states lie in w = 0, and with b_A1 ≠ 0 no stationary law exists (Proposition 4);
  exclusion needs the named hypothesis H-ZM, not supplied on `main` and not adopted
  (Proposition 5). On Z (Proposition 6): no normalizable null modes; J_F closed and unbounded on
  l²; finitely supported vectors form a core for d ≥ 3, and lie in D(J_F) for d = 1, 2 only under
  zero-mode constraints; the energy completion performs the H-ZM quotient for d = 1, 2 only; J_F is
  bounded on K, which is not l², and that choice is named H-top.
- **(iii) Σ.** Proposition 7: F-stationary moments are J-Hermitian on V_rest (T) and between
  spectral subspaces of A for compact sub-intervals of (−2, 2) (Z). Proposition 8: on-site Σ is real
  block-scalar under cubic invariance. Counterexample 9 holds on T for abs(αμ) < 1/d or on V_rest,
  and on Z for abs(αμ) < 1/d; αμ = 1/d on Z is not claimed. Counterexample 10: block-dependent
  dressing. Proposition 11: a zero-mode condensate at α = 1/d does not produce
  U(6) → U(3)×U(2)×U(1); on Z its relation to K is not examined.
- **T-only results:** §2.6, the b-remark of §4.1 and Proposition 4.
- **Conclusion (§6).** J is sourced by the real lift conditional on LIN and LIFT. Its use in SM
  Theorem 5 needs the named bridge premise H-PF (not adopted), stationarity under the same
  custodially scalar linear map, H-cust's condensate clause on the full two-point function, and a
  non-zero-mode condensate at α = 1/d. The interacting case is the named open hypothesis H-PF-int.
  The complex structure is sourced conditionally on these named hypotheses; it is not derived from
  the fundamental substratum. Audit classification: C, Layer 0, emergent.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Every result is a paper derivation checked by the model reviews of §1. The remediation plan below
authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| Canonicity on T (Lemma 0, Theorem 1, §2.3) | §1–§2.3 | partially verified: hand derivation, model-reviewed | independent non-model review; exact control X1 | #1217 | a recorded independent review, or X1 run under authorization with green controls |
| Canonicity on Z (Theorem 1Z) | §2.4 | partially verified, as above | independent non-model review | #1217 | a recorded independent review |
| Locality (Proposition 2) | §2.5 | partially verified; decay rates (O5) a sketch, not checked by the reviews | independent review; controls X6 and C1; a written decay proof | #1217 | review; X6 and C1 run under authorization; a written derivation for O5 |
| Null sector (Propositions 3–5, §2.6) | §2.6, §3.1 | partially verified | independent review; controls X2, X3, C2 | #1217 | review; X2, X3, C2 run under authorization |
| Carrier Z domain and topology (Proposition 6) | §3.2 | partially verified | independent review | #1217 | a recorded independent review |
| Σ results (Propositions 7, 8, 11; Counterexamples 9, 10) | §4 | partially verified; delta-review nits 1 (support of the bump on Z in Counterexample 9) and 2 (V_rest in the §4 isomorphism sentence) recorded, not applied; neither changes a result | independent review; controls X4, X5, C2 | #1217 | review; X4, X5, C2 run under authorization |
| Named hypotheses H-ZM, H-top, H-PF, H-PF-int; open nodes O1–O8 | §5, §8 | open; not adopted; O1–O8 not audited by the reviews | derivation or refutation of each | #1217; #1049 for LIN | a written derivation, a counterexample, or an owner decision on a premise |

Controls X1–X6 and C1–C2 (§9 of the report) are listed and have not been run.

## 4. Off-`main` references (§A.42 item 8)

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7184425769, 7186638587 (owner decisions) | header | provenance: authority records quoted with author and time; no result uses them |
| PR #1585 comment 7184957447 (review of r1) | header | provenance; evidence of review |
| commit `77881879` (r1) | header | on this record's branch; reachable from `main` only through a merge commit (§5) |
| commit `b6c6b80b` [P] and the SM line citations | header, throughout | support on `main`: `b6c6b80b` is an ancestor of `main` at `13f5c66a`; `papers/SM.md` differs between them only at lines 1394 and 1472, which the report does not cite |
| U1: #1211 unit 1, BRIDGE-UNIT1.md r5 at `820519cf` (not on `main`) | header, §2–§4 | provenance: every statement used is re-derived in the report |
| checks script at `820519cf` for C1, C2 | §9 | provenance: controls listed, not run; no result rests on them |
| C5 audit candidate 2, cited in U1 | §8 O7 | provenance: open node, not addressed |
| #1049 (Q-β; LIN row) and POSIT-MIN D1(b), D1(c) | §3.1, §4.6, §5 | provenance: LIN is a named conditional input, not supported by these |
| NQ-1059 | §5, §8 | provenance: named as not started |
| #1217, #1211, #1169 | header | provenance: accountability |

Support off `main`: none.

## 5. Landing condition

The record is preserved only through a merge commit that keeps `143f3599`, `77881879`, `e814d541`
and the commit adding this file reachable from `main`; the order of PLAN.md's commit before the
report commits is part of the record's provenance. Per the owner decision of 2026-11-26T09:05Z,
preservation includes integration with current `main` and exact-head CI. Merging needs the owner's
separate approval (§A.50 item 1).

## 6. Preservation rationale

The report settles question (i) on T and Z by proof with the necessary conditions identified
(F-commutation and taming; cubic commutation and compatibility as consequences), settles (ii) on
both carriers, proves (iii) in a stated class and disproves it beyond that class by two
counterexamples. Its §7 classifies as NEW the locality trilemma (Proposition 2), the need for
H-cust's condensate clause on the full two-point function (Counterexample 9), the dressing
dependence (Counterexample 10), the role of b_A1 = 0 at the normalized branch (Proposition 4),
Proposition 5 with H-ZM, Proposition 6 with the topology choice on Z (H-top), and Proposition 11.
It names H-PF as the premise on which the use of J in SM Theorem 5 depends.
