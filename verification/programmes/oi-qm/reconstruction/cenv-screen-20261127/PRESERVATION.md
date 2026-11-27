# C-ENV screen: preservation record

Mutable record under §A.46 items 4 and 8. It cites the plan and the report and does not change them. It documents the owner's conditional approval of preservation (#1169 comment 7213109404, as corrected by comment 7213183135) and the conditions that approval sets.

- **Evidence layers.**
  - The report is a mathematical derivation on paper with source reading. Every argument in it is labelled P-here: Theorem 1, Corollary 1.2, Lemmas 3.1–3.3 and 8.1, Nodes 2, 9 and 10, controls K1–K7, and D1.
  - No computation was run and no Lean was built.
  - The standard results it uses (Pontryagin duality, integral closure of UFDs, units of Laurent rings, entropy facts for ℤ^d shifts) are cited, not reproved.
- **Inputs.** Records on `main`, cited at `69786da24`, an ancestor of `main`, with every cited file unchanged through `4e2f034a`:
  - NR-1;
  - `papers/Main.md` (posit ledger; :296), `papers/SM.md` §4, `papers/Substratum.md`:56 and :407;
  - MECH-1 `DESIGN.md`;
  - FSLICE-PS-1.

  Phase 1's r1 and r3 at `95d7c225` are now on `main` through the merge `4e2f034a` (§4).

## 1. The record preserved

**Authoritative report:** `REPORT.md` (revision r2) at `888e13c8` on `research/cenv-screen-20261127`. Revision r1 of the same file is at `02726c54`. Both texts were written by the unit's writer and committed verbatim by the coordinating session.

**Plan.** `PLAN.md` was committed alone at `50f51227` (2026-11-27T07:30:23Z), before any derivation. Report r1 followed at `02726c54` (07:36:18Z) and r2 at `888e13c8` (07:44:24Z). PLAN.md is unchanged at both report commits. It fixes the following:
- the questions S1 and S2;
- the class 𝒜_L;
- the justification criterion J1–J5;
- the readability criterion;
- the outcome-neutral decision rule;
- controls K1–K7;
- the registered tuple (q, α, d) = (2, 1, 3);
- the stopping bounds and the Goal link (#914).

Its pre-plan disclosure records that the writer conjectured the eigenline obstruction before the plan, without deriving it.

Its §10 said "No push and no GitHub write is made by this unit". The branch was published, and PR #1627 opened, by the coordinating session under the owner's publication rule (§A.43).

**Writers.**
- PLAN.md and both report revisions: a Claude subagent designated by the coordinating session as the unit's writer.
- Commits `02726c54` and `888e13c8`, and this file: the Claude coordinating session, working under its takeover under §A.52 (#1169 comment 7212372089).

**Accountable Issues:** #1169, with #914. Guiding pull request: #1627.

**Owner decisions.** Each is a #1169 comment posted from the account `amaybaum` by the coordinating session, quoting the owner (amaybaum):
- **Comment 7212372089** (created 2026-11-27T07:20:10Z), from the approved list: "Authorize the bounded paper-only C-ENV screen as the first Phase 2 investigation. Determine whether the proposed invariant background is independently physically justified and whether it permits an initially readable encoding at one registered parameter tuple." "Stop the C-ENV investigation if either requirement fails. Do not initiate T-ENV computation without further authorization." "… SMD and C-NL remain suspended under their existing holds."
- **Comment 7213109404** (created 2026-11-27T08:04:27Z). The owner replied "Approved" to a text that includes: "Preserve the C-ENV screen after independent review of its preservation record." "Include non-stationary backgrounds as a P2-MIN candidate requiring independent physical justification." "Proceed with bounded paper-only P2-MIN, excluding SMD and C-NL." Its recorded scope line understated that text; the correction at #1169 comment 7213183135 states that the C-ENV merge is authorized, conditional on the independent review of this record and the final landing checks.
- **Preservation decision: approved, conditional on the independent review of this record and the final landing checks.**
  - Comment 7213109404, as corrected by comment 7213183135, approves preservation conditional on an independent review of this preservation record. That review is #1627 comment 7213223364 (ACCEPT WITH NITS on fc55e93f), whose findings are applied in the commit that follows it.
  - This file does not itself authorize a merge (§A.50 item 1).

**Independent non-author reviews.** These are model reviews by reviewer agents started with fresh contexts, recorded on PR #1627 as verbatim reviewer text. They are evidence of review, not independent mathematical verification.
- **Comment 7212726809, review of r1 at `02726c54`: REVISE,** text only.
  - It checked by hand Node 1 (F̂, ω and λ), Node 2, Lemmas 3.1 and 3.3, Corollary 3.4, Propositions 4.1–4.2, Corollary 1.2, the coset reduction, controls K3–K6, the (L3) reading, D1 R3 and the decision rule, and found them correct.
  - It made one major finding (confine every negative to stationary backgrounds), one moderate, two minor and five nits. All nine are applied in r2.
- **Comment 7212792912, delta review of r2 at `888e13c8`: ACCEPT.**
  - It found all nine findings resolved and the verdicts unchanged, and checked the new Node 2, Node 9 and Node 10 mathematics by hand.
  - It gave two non-blocking notes, not applied in the report:
    - (i) Node 4's sublattice bullet lost its explanatory sentence ("They would change the ring to a sublattice group ring with a larger free module").
    - (ii) "Maximal isotropic" in Node 2 means maximal among isotropic submodules. In that sense it is equivalent to M = M^{⊥λ}. This record adopts that reading.
- **Comment 7213223364, review of this preservation record at `fc55e93f`: ACCEPT WITH NITS.** This is the review comment 7213109404 requires. Findings 1–5 are wording fixes, applied in the commit that follows it.

## 2. Substantive result and its precise scope

**Question.** Is C-ENV's proposed invariant background independently physically justified, and does it permit an initially readable encoding at the registered tuple?

**Results, with their exact limitations.**
- **Verdicts.** S1 is FAIL (F1), S2 is NOT REACHED, and C-ENV is STOP. They are generated by PLAN §6 for the class 𝒜_L: Haar laws of closed subgroups (or cosets) that are invariant under every lattice translation, invariant under the native rule F (stationary), and Lagrangian (reading (L3)).
- **Theorem 1 (P-here).** The scope is prime q, α ∈ F_q^× and full translation invariance.
  - (a) No closed translation- and F-invariant Lagrangian subgroup exists, for any d ≥ 1.
  - (b) None of half entropy density exists for d ≥ 2, or for d = 1 with α² ≠ 1.
  - (c) For d ≥ 2, every closed translation- and F-invariant subgroup is the whole phase space or has entropy density 0.

  Corollary 1.2 extends (a)–(c) to invariance under any power F^k for d ≥ 2. The core step: a stationary half-rank subgroup needs a root of t² − Xt + 1 in the Laurent ring. Such a root would be a unit, so X would have at most two monomials. But X has 2d monomials.
- **Supporting results.**
  - Lemma 8.1: readability over a coset law holds iff g ∉ H.
  - Node 9: non-atomic, readable, zero-entropy invariant subgroups exist, for example Δ = 1 + x₁.
  - Node 10: non-stationary translation-invariant Lagrangian subgroups exist, for example L = {u = 0} and its F-orbit.
  - D1 R3: entropy density is conserved by the native rule and is not lowered in weak limits.
- **Scope of STOP.** STOP rests on the plan's reading of "invariant background" as F- and translation-invariant ((L2), J1). The non-stationary translation-invariant Lagrangian class was **not tested**. The owner's decision at #1169 comment 7213109404 treats non-stationary backgrounds as a P2-MIN candidate requiring independent physical justification. This record preserves that class as an open candidate, not as a result.
- **Not covered:**
  - composite q;
  - backgrounds invariant only under a proper sublattice of translations;
  - non-algebraic invariant laws of intermediate entropy (whether ergodic ones exist at the tuple is open);
  - asymptotic randomization for the native rule (open);
  - any T-ENV quantity.

**Nonredundancy.**
- NR-1 treats the selected rule under the maximal-entropy Haar prior only.
- Phase 1 r3 proposed (E2L) and settled only the vacuum variant.
- No record on `main` decides whether a stationary Lagrangian or intermediate-entropy algebraic background exists for the native rule.
- Theorem 1 and Corollary 1.2 decide it negatively, in the stated scope. D1 records the consequence for the minimal missing principle: within the corpus at D, a stationary low-entropy background is neither generated by the native dynamics nor selected by the ledger's measure principle, and so would have to be posited.

**What the record does not show.**
- That every C-ENV variant fails: the non-stationary class is untested.
- That the root choice of D1 item 3 is the positive-frequency choice of the complex-structure gap. That is an open question (AW-CENV-1), and no identification is made.
- No premise is adopted (§7).

## 3. Verification status and remediation (§A.46 items 4 and 8)

The remediation plans authorize no work (§A.45 rule 3). "Model-reviewed" means checked by hand in the reviews of §1. That is evidence of review, not independent mathematical verification.

| Claim | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| Theorem 1(a)–(c), Corollary 1.2 | report Nodes 2–4 | partially verified: P-here, model-reviewed (7212726809, 7212792912) | independent non-model review | #1169, #914 | a recorded independent check; optionally a Lean statement of the unit/monomial-count step (Proposition 4.1) |
| Node 2 (duality, ⇐ direction, J-map reading of (L3)) | report Node 2 | partially verified: P-here, model-reviewed | as above | #1169 | as above |
| Lemma 3.3 (rank 2 ⇒ entropy density 0) | report Node 3 | partially verified: P-here, model-reviewed | as above | #1169 | as above |
| Lemma 8.1 (readability dichotomy) | report Node 8 | partially verified: P-here, model-reviewed | as above | #1169 | as above |
| Controls K1–K7 | report §3 | pass, P-here, model-reviewed. K1a, K1b and K2 are close to built-in; K5 is vacuous for the monomial step; K6 is the non-trivial control | none beyond the above | #1169 | as above |
| Node 9 remark (zero-entropy readable example) | report Node 9 | partially verified: P-here, model-reviewed in the delta review | as above | #1169 | as above |
| Node 10 (non-stationary Lagrangian class exists) | report Node 10 | partially verified: P-here, model-reviewed in the delta review. The class itself is **untested** | testing the class needs independent physical justification first (owner, 7213109404) | #914, #1169 | P2-MIN under its own authorization |
| Verdicts S1 FAIL (F1), S2 NOT REACHED, C-ENV STOP | report §0 | generated by PLAN §6 for 𝒜_L; model-reviewed | inherits Theorem 1 | #1169 | as Theorem 1 |
| D1 R3 (entropy density conserved; weak limits do not lower it) | report §4 | P-here from cited standard facts; model-reviewed | citation check | #1169 | a recorded check |
| D1 asymptotic randomization for the native rule | report §4 | open | a proof of the Pivato–Yassawi hypotheses for the second-order rule | #914 | a separately authorized unit |
| D1 ergodic intermediate-entropy invariant laws at the tuple | report §4 | open | a construction or an exclusion | #914 | P2-MIN or a separately authorized unit |
| D1 item 1 (no stationary Lagrangian background) | report §4 | inherits Theorem 1, in its scope | as Theorem 1 | #1169 | as Theorem 1 |
| D1 item 2 (invariant low entropy must be posited) | report §4 | P-here synthesis within the corpus at D | review; it is limited to the corpus and to principles proposed in the unit | #914 | P2-MIN |
| D1 item 3 (root requirement; resemblance to positive frequency) | report §4, AW-CENV-1 | root requirement: inherits Proposition 4.1. Resemblance: open, no formal map | a formal map or a refutation | #914 | P2-MIN or complex-structure work |
| D1 item 4 (options (a)–(d)) | report §4 | premise choices, untested. Option (d) is the owner's P2-MIN candidate | each needs its own §A.29 assessment | #914, #1169 | P2-MIN and owner decisions |
| Preregistration order | `PLAN.md` | commit order: `50f51227` at 07:30:23Z precedes `02726c54` at 07:36:18Z (2026-11-27) | none available from commit order alone | #1169 | none; the limitation stands |
| This file | here | model-reviewed (#1627 comment 7213223364, ACCEPT WITH NITS; findings applied) | confirmation that the findings are applied | #1169 | a recorded confirmation |

## 4. Off-`main` references (§A.42 item 8)

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7212372089, 7213109404, 7213183135 | plan and report headers; §1 here | provenance: authority records quoted with author and time |
| PR #1627 comments 7212726809, 7212792912, 7213223364 | report status line; §1 and §3 here | provenance: evidence of review |
| Phase 1 r3 `REPORT-r3.md` at `95d7c225` (§3.0 CS labels, §3.1 (E2L) wording and T-ENV nomination, P1-33) | PLAN §2; report §0, §4 and §6 | reclassified from provenance off `main` to **provenance whose content is on `main`**. `95d7c225` is reachable from `main` through the merge `4e2f034a` (#1625). The C-ENV claims use only the restated definition and the quoted sentences. **Differences in the landed `REPORT-r3.md`**, from in-place corrections at `e56149db`, `6877032e` and `3e5f8ac0): the quoted passages are unchanged. These are the (E2L) wording, the T-ENV nomination ("closed, translation-invariant and rule-invariant Lagrangian subgroup"), the CS labels and P1-33's Pivato–Yassawi sentence. P1-33 now adds NR-1 Proposition 5.1's exception for nonzero nilpotent α, which does not arise at prime q with α ≠ 0. The sentence after (E2L) now cites `composition-access-20261024/REPORT.md` for the conditional-freshness requirement, in place of #885. The C-ENV records do not quote that sentence |
| Phase 1 r1 `REPORT.md` at `95d7c225` (§3.1) | report K1a; §0 "initial-condition posit of past-hypothesis type" | reclassified as for r3. The file is byte-identical on `main` |
| #1625 comment 7210194622 | PLAN header | provenance |
| #885 (acceptance rule) | J4's list of deliverables | provenance. Only its name is used. `main` now locates the conditional-freshness requirement in `composition-access-20261024/REPORT.md` |
| NR-1, Main, SM, Substratum, MECH-1 (`verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md`), FSLICE-PS-1 | report §6 | support on `main`: cited at `69786da24`, an ancestor of `main`, with the files unchanged through `4e2f034a` |
| Branch commits `50f51227`, `02726c54`, `888e13c8`, and the commits adding and completing this file (through the landing head) | §1 and §3 here | support off `main` (gap), closed by the merge commit of §5. `50f51227` and `02726c54` carry the preregistration order. `888e13c8` carries the authoritative report |
| Standard results (Pontryagin duality; Kitchens–Schmidt; Schmidt 1995; Walters; Haah 2013; Pivato–Yassawi 2002) | report §6 | external literature, cited by name. Pivato–Yassawi's applicability is stated as open |

Once §5's merge lands, every reference is classified and no gap remains.

## 5. Landing condition

The record is preserved only through a **merge commit, not a squash**. The merge keeps reachable from `main`:
- `50f51227` (the plan) before `02726c54` (report r1);
- `888e13c8` (report r2, authoritative);
- the commits adding and completing this file, through the landing head.

The merge needs:
- the independent review of this record that #1169 comment 7213109404 requires (#1627 comment 7213223364), with its findings applied and confirmed;
- the final landing checks. The owner's approval is comment 7213109404, as corrected by comment 7213183135, conditional on that review.

This file gives neither.

## 6. Preservation rationale

The record answers the owner-authorized first Phase 2 question. It has a plan committed before derivation, an outcome-neutral decision rule, controls able to fail, and two review rounds ending in ACCEPT. Its result is substantive and nonredundant (§2):
- It closes C-ENV's stationary Lagrangian route for the native rule, in the stated scope.
- It shows that stationary algebraic backgrounds at d ≥ 2 have either maximal or zero entropy density.
- It records, within the corpus at D, that a stationary low-entropy background is neither generated by the native dynamics nor selected by the ledger's measure principle, and so would have to be posited.

These findings narrow the search for a physical mechanism, the owner's highest scientific priority, and identify the non-stationary class that the owner has routed to P2-MIN as a candidate requiring independent physical justification (#1169 comment 7213109404; Goal link #914).

The reviews are recorded in §1, the §A.42 item 8 tracing is complete subject to §5's merge (§4), the accountable Issues are #1169 and #914, and each open gap carries a remediation plan (§3).

## 7. Standing of this record

- Preservation establishes no claim (§A.46 item 1). The model reviews are evidence of review, not independent mathematical verification. Landing the record does not change any result's evidence layer.
- **No premise is adopted.** In particular, none of the following is adopted:
  - the justification routes R1–R4;
  - a low-entropy far-field principle of past-hypothesis type;
  - an added root-supplying structure;
  - a non-stationary Lagrangian initial law.

  Each remains a candidate to be judged under §A.29.
- No T-ENV work is authorized or begun. SMD and C-NL were not touched. Nothing is proposed for the manuscripts.

## 8. Owner question recorded in the report

The report put to the owner whether the non-stationary translation-invariant Lagrangian class falls under the stop instruction. #1169 comment 7213109404 addresses it for planning by routing the class to P2-MIN: non-stationary backgrounds are included as a P2-MIN candidate requiring independent physical justification. This record does not reopen C-ENV and does not test that class.
