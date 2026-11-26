# COMPLEX-CARRIER-1, lane 2: preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it. Evidence
layer of every result: mathematical derivation on paper. No computation was run.

## 1. The record preserved

- **Authoritative report:** `REPORT-r2.md` (revision r2, commit
  `e814d5417616e798ff98115795e9cf46d9fdbb40`). It supersedes `REPORT.md` (r1, commit
  `77881879bc1b4df9156fe537e5ee9bd261345cf1`), which is kept unchanged; `CHANGES-r2.md` maps each
  r1 to r2 change to its review finding. `PLAN.md` (commit
  `143f359928698125f854b86e756ba827dc518064`) fixes the questions, productivity test and stopping
  rule before the work and is not superseded.
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
    passages that r2 leaves unchanged. It was written by the reviewer agent that wrote the r1
    review, resumed, so all review evidence for this record comes from a single model reviewer.

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
  block-scalar for an F-stationary, cubic-invariant state. Counterexample 9 holds on T for
  abs(αμ) < 1/d or on V_rest, and on Z for abs(αμ) < 1/d; αμ = 1/d on Z is not claimed. The Z case
  also needs a condition the report does not state (delta-review nit 1): the support of the bump
  Π_{k_0} must be small enough that its 24 rotated copies around g k_0, and their negatives, do not
  overlap. Counterexample 10: block-dependent dressing. Proposition 11: a zero-mode condensate at
  α = 1/d does not produce U(6) → U(3)×U(2)×U(1); on Z its relation to K is not examined.
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
| "H-ZM not supplied on `main`" (Proposition 5) | §3.1 | the corpus search for zero-mode premises was keyword-based over papers/ at `b6c6b80b`, not exhaustive (r1 review limitation) | an exhaustive search of the corpus for a premise making uniform static shifts unobservable | #1217 | a recorded exhaustive search, or a premise found or ruled out |
| Carrier Z domain and topology (Proposition 6) | §3.2 | partially verified | independent review | #1217 | a recorded independent review |
| Σ results (Propositions 7, 8, 11; Counterexamples 9, 10) | §4 | partially verified; delta-review nits recorded, not applied. Nit 1: without the support condition of §2, the lower bound min κ_b − ε on each subspace and the step "on the k_0 subspace it equals Σ_b κ_b P_b + εQ" can fail in the Z case of Counterexample 9. Nit 2: "on T" should read "on V_rest" in the §4 isomorphism sentence; only the direction "C_− = 0 implies S_n = 0" is used, so no result changes | independent review; the support condition for the Z case of Counterexample 9; controls X4, X5, C2 | #1217 | review; a revision stating the support condition; X4, X5, C2 run under authorization |
| Preregistration order (PLAN.md before the report) | §5 below | established only from commit timestamps: `143f3599` at 06:29:10Z, `77881879` at 06:47:51Z (r1 review limitation) | none available from commit order alone | #1217 | none; the limitation stands as stated |
| Named hypotheses H-ZM, H-top, H-PF, H-PF-int; open nodes O1–O8 | §5, §8 | open; not adopted; O1–O8 not audited by the reviews | derivation or refutation of each | #1217; #1049 for LIN | a written derivation, a counterexample, or an owner decision on a premise |

Controls X1–X6 and C1–C2 (§9 of the report) are listed and have not been run.

## 4. Off-`main` references (§A.42 item 8)

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7184425769, 7186638587, 7187418279 (owner decisions) | report header; §1 here | provenance: authority records quoted with author and time; no result uses them |
| PR #1585 comments 7184957447, 7187069631 (reviews of r1 and r2) | report header; §1 here | provenance: evidence of review; no result uses them |
| commit `77881879` (r1, superseded) | report header | provenance: cited only to identify the r1 text |
| commits `143f3599` (PLAN.md), `e814d541` (REPORT-r2.md, CHANGES-r2.md) and the commit adding this file | report header; §1 here | support on `main` once the merge of §5 lands: the record's own content; not before |
| commit `b6c6b80b` [P] and the SM line citations | report header, throughout | support on `main`: `b6c6b80b` is an ancestor of `main` at `13f5c66a`. `papers/SM.md` differs between them only at lines 1394 and 1472, which the report does not cite. `papers/Main.md` (lines 692, 716, 720, 724) and `papers/Substratum.md` (line 463) also differ; no changed hunk concerns zero modes, shift symmetry or uniform shifts, so Proposition 5's search of papers/ at [P] is unaffected |
| U1: #1211 unit 1, BRIDGE-UNIT1.md r5 at `820519cf` (not on `main`) | report header, §2–§4 | provenance: every statement used is re-derived in the report |
| checks script at `820519cf` for C1, C2 | report §9 | provenance: controls listed, not run; no result rests on them |
| #1049 (Q-β; LIN row) | report §3.1, §4.6, §5 | provenance: LIN is a named conditional input, not supported by #1049 |
| NQ-1059 | report §5, §8 | provenance: named as not started |
| #1217, #1211, #1169 | report header | provenance: accountability |

Support off `main`: none. POSIT-MIN D1(b), D1(c)
(`verification/audits/foundations/posit-min-20261120/`) and C5 audit candidate 2
(`verification/audits/foundations/c5-discovery-audit.md`) are on `main`; LIN remains a named
conditional input and O7 an open node.

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
