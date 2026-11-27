# OI-QM-APPROX-1, UN-1: the identity partner in the converse: preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it.

- **Evidence layer of every result:** mathematical derivation on paper, labelled [A] in the
  report. The derivations use the reviewed paper derivations of the predecessor ([UNC]) and of
  units 2 and 3 ([U2], [U3]) for steps named where used. Each result that uses them is conditional
  on the named step.
- **No computation was run, and no Lean was built.**

## 1. The record preserved

**Authoritative report:** `REPORT-r2.md` (revision r2), as it stands at commit
`4ccf254869ed22a03bdc6f3108f22f403ce18687`.
- r2 was added at commit `4e84b2f2a4c97674020969fd7962773187aed384`, the head that the
  delta review accepted.
- `4ccf2548` changes only one row of r2's §7, the remediation row for Prop I (iii). It applies the
  optional nit of that review: the row now names all three inherited steps, [U2] Proposition 9,
  [U3] Corollary 7c and [UNC] Theorem U (U-b), in its evidence-level, missing-verification and
  "What would resolve it" columns. No result, proof, outcome or other line changes. The
  preservation review, #1622 comment 7209435768, confirmed the changed row.

**Superseded version,** kept unchanged: `REPORT.md` (r1, commit
`d4d9846146f73f3ed80cb4f0846646a2d08aeb08`).

**Change map.** `CHANGES-r2.md` maps each r1-to-r2 change to its review finding. No proof changes
between r1 and r2. r2 changes two printed outcomes: Q-A/Q-B prints D2 (r1 printed D4), and Q-C
prints "open". It adds the bound M_C(T^{(L)}, Q) ≥ 1/184 to Prop I (iii) and completes the T_S
exclusion.

**Plan.** `PLAN.md` (commit `b2adbd64bae000d42a7a03887aa4410e3b0f7006`) fixes the questions Q-A to
Q-D, the decision rule D1–D4 and the outcomes of Q-C, the controls and the stopping conditions. It
is recorded, not frozen, and is not superseded. It discloses that the writer explored the question
informally during the predecessor unit, written up only as the sketch in the predecessor's §6, and
that no derivation for this unit had been written down when it was committed.

**Status in the header.** The label line of `REPORT-r2.md` calls the report's own arguments
"unreviewed". Review is recorded here.

**Accountable Issue:** #1216 (OI-QM-APPROX-1; programme #1169). Guiding pull request: #1622. The
record follows the uniform-norm-control record (`../uniform-norm-control-20261126/`, landed through
#1614) and takes up its open nodes UN-1 and UN-2.

**Owner decisions.** Each is a #1169 comment posted from the account `amaybaum`, quoting the
owner:
- **Comment 7199704501** (created 2026-11-26T17:49:03Z; decision received 2026-11-26T17:49Z):
  activation of work package WP-2, scientific research, by the owner's decision "Proceed as
  suggested".
- **Comment 7208939261** (created 2026-11-27T03:22:49Z; decision received 2026-11-27,
  coordinating session) authorizes the unit. The owner's reply "Proceed as suggested" approves the
  proposal: "Approved: under WP-2, paper-only investigations UN-1 (#1216), F-slice premise sourcing
  (#1217), and SMD clustering (#1049/#1217), each with preregistration, bounded stopping conditions
  and independent review."
- **Comment 7209325168** (created 2026-11-27T03:51:22Z; owner in the coordinating session,
  2026-11-27) directs the preparation: "Prepare #1623 together with UN-1 and F-slice for a
  consolidated preservation decision." and "Preserve the negative results and their exact
  limitations. No new premise is adopted, and no merge is authorized yet."
- **Preservation decision:** pending: consolidated preservation decision for #1622, #1623 and
  #1624.

**Independent non-author reviews.** These are model reviews by a reviewer agent, each recorded on
PR #1622 as reviewer text posted verbatim: evidence of review, not independent mathematical
verification.
- **Comment 7209032832, review of the plan at `b2adbd64` and r1 at `d4d98461`: REVISE (minor),**
  findings 1–5. It found no mathematical error, and checked by hand Theorem D, the dichotomy,
  Corollary D1 and Prop I (i)–(iii) with their constants. Findings 1 and 2 concerned the outcomes
  the preregistered rule prints (D2, not D4, for Q-A/Q-B; "open" for Q-C). Findings 3–5 asked for
  the proof of the M_C bound in Prop I (iii), the completion of the T_S exclusion with a support
  row, and a statement of the writer's no-push boundary.
- **Comment 7209077894, delta review of r2 at `4e84b2f2`: ACCEPT WITH NITS,** one optional nit. It
  confirmed findings 1–5 applied, with nothing else changed in substance, and checked by hand the
  new argument for M_C(T^{(L)}, Q) ≥ 1/184. The nit is applied at `4ccf2548`.
- **Both report reviews are by one reviewer agent.** The delta review is written "against my review
  of r1". Comment 7209435768 separately reviews the preservation record at `bf59a2e9`.

## 2. Substantive result and its precise scope

**Scope.** At a level n, or on the system, of a theory T in class(η), under the converse's
hypotheses m ≥ 2, K ≥ 2 and M_C(T, Q) < ε, for admissible pairs (c, c′) with both terms at most ε.
Nothing is stated across levels, and M_H is not used. φ(c′) := ‖c′(P) − id‖_{1→1} is the residual
of the converse identified by the predecessor's Theorem U. Every result is [A].

**Positive results.**
- **Theorem D (conditional on [U3] Lemma 7η and [UNC] Corollary G1).** With ν := ‖c′(P)‖ and
  ω′ := 2ω_{K−1} + ω_{K−2}, ω_j := (1+τ_min)^j − 1: if 6ε + ω′C_Gν ≤ 1/8, then
  ‖c′(J) − J‖ ≤ 184ε + 16ω′C_Gν for every quantum instrument J with at most m outcomes, and in
  particular φ(c′) ≤ 184ε + 16ω′C_Gν.
- **The dichotomy.** For each admissible c′, either ν ≥ ν_+ := (1/8 − 6ε)/(ω′C_G), or, when
  16ω′C_G < 1, φ(c′) ≤ φ_− := (184ε + 16ω′C_G)/(1 − 16ω′C_G). As (ε, η) → 0 at fixed (d, n, m, K),
  φ_− → 0 and ν_+ → ∞, using τ_min ≤ τ(n) → 0 from [U3] §3.
- **Corollary D1 (same conditions).** Along any family of pairs (T, c′) in class(η) with
  ‖c′(P)‖ ≤ ν for a fixed ν, φ(c′) → 0 as (ε, η) → 0; by [UNC] Theorem U (U-a), the converse then
  holds for the pair (c̃, c′) with constants tending to 0. This answers positively, inside class(η),
  the sufficiency part of the predecessor's UN-1: bounded identity-partner norm forces φ → 0. The
  predecessor's Prop X2 lies outside class(η) at small η and is not contradicted.
- **Prop I (i), (ii).** τ_min ≤ ι ≤ φ_min, where ι is the distance from the identity of the
  nearest available single-outcome family. If some admissible c′ lies on the small branch of
  Theorem D, an idle step within φ_− exists.
- **Report §5 classifies Theorem D, Corollary D1 and Prop I as ELABORATING.** Theorem D and
  Corollary D1 combine [U3] Lemma 7η with [UNC] Corollary G1 and add no estimate of their own. Prop I
  locates the idle-step question within the existing rules and shows that the rules alone do not
  supply it at levels. The §3 sketch is BORDERLINE. No NEW finding is claimed.

**Negative results, with their exact limitations.**
- **Prop I (iii): the six exact rules alone do not give an idle step at levels.** The witness is
  unit 2's T^{(L)} ([U2] Proposition 9): every available single-outcome map at level L annihilates
  ρ ⊗ |0⟩⟨1|, so ‖D′ − id‖ ≥ 1 for each of them. Limitations:
  - it concerns the rules without M_C at the level. T^{(L)} has M_C(T^{(L)}, Q) ≥ 1/184 at L, so it
    does not meet the converse's hypothesis M_C < ε for ε < 1/184, and it does not show that the
    rules together with M_C < ε fail to give an idle step;
  - the bound M_C(T^{(L)}, Q) ≥ 1/184 rests on [U3] Corollary 7c and [UNC] Theorem U (U-b), and the
    witness on [U2] Proposition 9, all reviewed and not independently verified;
  - it is a statement about levels. On the system, rule (a) of class(η) supplies an idle step
    (η_id = η_a).
- **The exclusions of D3 candidates (report §3).** Four named families are excluded:
  - gauge conjugates S∘Q∘S^{-1} with tr∘S = tr, by [UNC] Prop X1;
  - rescaled QM T_s, by [UNC] CC-s, which uses unit 3's item D1 (partially verified);
  - T_S with S^{-1} = C_p, for every p: by the coverage term ([UNC] CC-p) for p > 4ε, and by Prop
    X1 for p ≤ 4ε;
  - T_− and T_ω, by scope: they lie outside class(η) at small η.

  The norm-based exclusions are for small η, where ν_+ exceeds the reported bounds. The rescaled
  QM comparison uses the small-branch condition 16ω′C_G < 1. The exclusions inherit the status of
  the predecessor's results and concern only the named families.
- **What remains unexcluded is the large branch.** In class(η) where τ_min > 0, no φ_bound is
  obtained for every admissible c′. A D3 theory would need ‖c′(P)‖ ≥ ν_+ ≈ 1/(8(3K − 4)τ_min C_G)
  for every admissible c′. No such theory was found, and none was shown impossible: failure to
  exclude the branch is not a disproof, and failure to find a D3 theory is not evidence that none
  exists. The two routes tried each exclude only a window of ν: [≈1, ν_+) through Lemma 7η, and,
  in a sketch that is not claimed, (≈1, ≈ε^{-1/2}) through tail effects at K = 2.

**Outcome against the decision rule (`PLAN.md` §3), over the green controls C0, C1 and CC-p.**
- **Q-A/Q-B: D2, controlled on a reduced scope.** The scope is τ_min = 0 at the level (the padding
  rules in closure, in particular η = 0), where φ ≤ 184ε for every admissible pair. This scope and
  its proof are inherited from unit 3 (Corollary 7c) and the predecessor (Theorem U (U-b)), not new
  to this unit. The remainder, τ_min > 0, is obstructed by the large branch.
- **Q-C: open.** On the small branch the identity partner is itself an idle step (Prop I (ii)); the
  rules alone do not supply one at levels (Prop I (iii)); on the large branch it is open.
- **Q-D.** The structure rules enter only through τ_min, and the obstruction scales as 1/τ_min.
- The stop is by bounded effort, with the gap stated as open node UN1-a.

**No premise is adopted.** The idle step remains a candidate premise, not adopted (§A.29, §A.50
item 6), and its sufficiency (UN-2) is open. Nothing is proposed for the manuscripts.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Each result is a paper derivation checked only by the model reviews of §1. The remediation plan
below authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| Theorem D, the dichotomy, Corollary D1 | report §1 | partially verified: hand derivation, model-reviewed; conditional on [U3] Lemma 7η and [UNC] Corollary G1, [U3] §3 for τ_min ≤ τ(n) → 0 in the limit, and [UNC] Theorem U (U-a) for D1's converse conclusion | independent non-model review; independent verification of the inherited inputs | #1216 | a recorded independent review; a verification of the inherited steps |
| Prop I (i), (ii) | report §2 | partially verified, as above | independent review | #1216 | a recorded independent review |
| Prop I (iii), with M_C(T^{(L)}, Q) ≥ 1/184 | report §2 | partially verified, as above; relative to [U2] Proposition 9, [U3] Corollary 7c and [UNC] Theorem U (U-b), reviewed and not independently verified | independent review; independent verification of the three inherited steps | #1216 | a recorded independent review; a verification of the inherited steps |
| Exclusions of the four D3 candidate families at small η | report §3 | partially verified: applications of [UNC] Prop X1, CC-s and CC-p, and of scope; ν_+ exceeds the reported bounds and the small-branch comparison uses 16ω′C_G < 1; CC-s rests on unit 3's item D1, partially verified | as for those results, recorded in the predecessor's `PRESERVATION.md` §3 | #1216 | as recorded there |
| K = 2 tail-effect route (UN1-d) | report §3, §6 | a sketch, not claimed; constants not written out | a written derivation | #1216 | a written derivation with its constants |
| The large branch (UN1-a) | report §3, §6 | open | a proof that excludes it for some admissible c′, or a D3 theory on it | #1216 | a written derivation or an explicit construction |
| Idle step on the large branch (UN1-b) | report §2, §6 | open; candidate premise, not adopted | a proof or a counterexample; an owner decision on the premise | #1216 | a written derivation, a counterexample, or an owner decision (§A.29, §A.50 item 6) |
| UN-2 (UN1-c): idle step implies φ_min small | report §2, §6 | open | a proof or a counterexample | #1216 | a written derivation or an explicit theory |
| §7 row for Prop I (iii) as changed at `4ccf2548` | report §7 | applies the delta review's optional nit; confirmed in #1622 comment 7209435768 | the independent mathematical verification listed for Prop I (iii) above | #1216 | verification of the inherited steps |
| Preregistration order (`PLAN.md` before the report) | `PLAN.md`; §1 here | evidence is commit order only: `b2adbd64` at 03:24:03Z precedes `d4d98461` at 03:26:58Z (2026-11-27); the plan discloses earlier informal exploration | none available from commit order alone | #1216 | none; the limitation stands as stated |

## 4. Off-`main` references (§A.42 item 8)

Each reference is classified by reading the claim it is attached to, using the three classes:
provenance, support on `main`, and support off `main` (gap). The tracing covers every reference
in `PLAN.md`, `REPORT.md`, `REPORT-r2.md`, `CHANGES-r2.md` and this file, and is complete.

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7199704501, 7208939261, 7209325168 (owner decisions) | `PLAN.md`; §1 here | provenance: authority records quoted with author and time; no result uses them |
| PR #1622 comments 7209032832, 7209077894, 7209435768 (reviews) | report header, §8; §1 here | provenance: evidence of review; no result uses them |
| PR #1614 | report header | provenance: lineage; no result uses its discussion |
| commit `b2adbd64` (`PLAN.md`) | report header; §1, §3 here | support off `main` (gap), closed by the landing condition of §5: it holds the plan and the evidence of its order |
| commit `d4d98461` (r1) | report header; §3 here, preregistration-order row | support off `main` (gap), closed by the landing condition of §5: the order claim uses its commit time. For identifying the r1 text it is provenance |
| commit `4e84b2f2` (r2 as reviewed) | §1 here | provenance: cited to identify the text the delta review accepted |
| commit `4ccf2548` (r2 with the nit applied) | §1 here | support off `main` (gap), closed by the landing condition of §5: the authoritative report |
| the commits adding and completing this file | — | support off `main` (gap), closed by the landing condition of §5: this record's own content |
| pin `13c05b4f` | report header, `PLAN.md` | support on `main`: an ancestor of `main` at `650c8053` |
| `../uniform-norm-control-20261126/REPORT-r4.md` and `PRESERVATION.md` | throughout | support on `main`: at the pin (landed through #1614) and unchanged at `650c8053`; reviewed paper derivations, carried as conditions of the steps that use them |
| `../unit3/REPORT-r3.md` (Lemma 7η, (Hg), Corollary 7c, τ_min, τ(n), ω′) and unit 3's item D1 | report §1–§3 | support on `main`: at the pin and unchanged at `650c8053`; reviewed paper derivations (D1 partially verified) |
| `../unit2/REPORT-r3.md` (Proposition 9, Lemma 7) | report §2, §4 | support on `main`: at the pin and unchanged at `650c8053`; reviewed paper derivations |
| `../unit2/PLAN.md`, `../unit3/PLAN.md` | `PLAN.md` | support on `main`: inherited setting, unchanged at `650c8053` |
| #1216, #1169 | headers | provenance: accountability |
| #1049, #1217, #1623, #1624 | `PLAN.md`; §1 and §5 here | provenance: programme links and the consolidated preservation decision |

**Support off `main` (gaps), and how they close.** Each gap below is closed when the merge commit
of §5 lands with the commit reachable from `main`. None is closed before that, and keeping the
branch does not close it.
- `b2adbd64`: `PLAN.md` and the preregistration order.
- `d4d98461`: its commit time, for the preregistration-order row.
- `4ccf2548`: the authoritative report.
- The commits adding and completing this file: this record.

## 5. Landing condition

The record is preserved only through a **merge commit, not a squash**. The merge keeps these
commits reachable from `main`:
- `b2adbd64`, `d4d98461`, `4e84b2f2` and `4ccf2548`;
- the commits adding and completing this file, through the reviewed landing head.

That `PLAN.md`'s commit precedes every report commit is part of the record's provenance.

The owner's direction of 2026-11-27 (comment 7209325168) prepares the record for a consolidated
preservation decision with #1623 and #1624 and states that no merge is authorized yet. Preservation
and merging need that decision and the owner's approval of the merge (§A.50 item 1), together with
the review of this file and green CI.

## 6. Preservation rationale

The unit answers the predecessor's open node UN-1 in part, and its question on the idle step:
whether the converse's own hypotheses control the identity partner φ in class(η) at small η, and
whether the idle step follows from the existing structure. It uses a plan committed before the report, with the
disclosure of §1, its verdicts are printed over green controls, and its negative statements are
scoped as §2 states.

It establishes, conditionally on the inherited steps named in §2:
- **that inside class(η) at small η, a bounded identity-partner norm forces φ → 0** (Corollary D1),
  which closes positively the sufficiency question the predecessor left open there;
- **that the converse's residual in class(η) reduces to one branch**, the large-norm branch of the
  identity partner, ‖c′(P)‖ ≥ ν_+ with ν_+ ∝ 1/τ_min (Theorem D);
- **that the idle step is not a consequence of the six rules alone at levels** (Prop I (iii), with
  the limitations of §2), while it follows from M_C on the small branch (Prop I (ii));
- **the exclusion of four named D3 candidate families at small η**, where ν_+ exceeds the recorded
  norm bounds and the small-branch comparison applies, and the precise statement of the
  unexcluded large branch, open as UN1-a.

These are the negative results and their exact limitations that the owner's direction of
2026-11-27 asks to be preserved. The record is substantive and nonredundant with the predecessor
and units 2 and 3: it uses their results and adds the combination, the dichotomy, the positive
answer to the sufficiency question in class(η) and the status of the idle step. It is
independently reviewed by the model reviews of §1, its §A.42 item 8 tracing is complete, and its
open gaps carry the remediation plans of §3.

## 7. Standing of this record

Preservation establishes no claim (§A.46 item 1). The model reviews are evidence of review, not
independent mathematical verification, and landing the record does not change any result's
evidence layer. No premise is adopted: the idle step remains a candidate premise. Nothing is
proposed for the manuscripts.
