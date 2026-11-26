# OI-QM-APPROX-1, uniform norm control in the converse: preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it.

- **Evidence layer of every result:** mathematical derivation on paper, labelled [A] in the
  report, using the reviewed paper derivations of units 2 and 3 ([U2], [U3]) for unchanged steps,
  named where used, and unit 3's item D1 ([D1], partially verified) for the definition of T_s and
  τ_min = s only.
- **No computation was run, and no Lean was built.**

## 1. The record preserved

**Authoritative report:** `REPORT-r4.md` (revision r4, commit
`05f65082257f5b649a21a23c290a0a3275ea4991`, the head of `research/uniform-norm-control-20261126`
before this file).

**Superseded versions,** kept unchanged:
- `REPORT.md` (r1, commit `1a6252f41ce71a029239a82f9bea667d056f8335`);
- `REPORT-r2.md` (r2, commit `1f49e6beda01526faf6b1a32204fdd225abfecb1`);
- `REPORT-r3.md` (r3, commit `626628da47c75f045de32762ebb8e8443912959a`).

**Change maps.** `CHANGES-r2.md`, `CHANGES-r3.md` and `CHANGES-r4.md` map each change to its review
finding. r3 and r4 change text only: no result, proof or status changes after r2.

**Plan.** `PLAN.md` (commit `de3447139fa13ce8ba1c84baa66d6302c03fa48f`) fixes the questions U1–U3
and CC-L, the decision rule N1–N4, the controls and the stopping conditions. It is not superseded.

**Provenance qualification of the plan.** The header of `REPORT-r2.md`, kept in r3 and r4, states
(in answer to observation 10 of the first review): before the plan was committed, the writer read
the inputs and explored the question informally in the session, including the idea behind Theorem
G (using the coverage partner of the identity as a gauge); none of this was written down before
`PLAN.md` was committed, and the written derivation followed it. The plan therefore does not
certify that the derivation started afterwards, only that the decision rule was recorded before the
report. The first review records the same limitation: the report followed the plan by four
minutes, and the plan's N2 example anticipates Theorem G; it judged the risk limited because the
rule N1–N4 is outcome-neutral.

**Status in the header.** The label line of `REPORT-r4.md` calls the report's own arguments
"unreviewed". Review is recorded here.

**Accountable Issue:** #1216 (programme #1169). Guiding pull request: #1614.

**Owner decisions.** Each is a #1169 comment posted from the account `amaybaum`, quoting the
owner:
- **Comment 7199704501** (created 2026-11-26T17:49:03Z; decision received 2026-11-26T17:49Z):
  activation of work package WP-2, scientific research, by the owner's decision "Proceed as
  suggested".
- **Comment 7200549806** (created 2026-11-26T18:30:55Z; decision received 2026-11-26T18:30Z),
  item 4, authorizes the investigation: "Authorize all three ranked scientific investigations —
  SMD sourcing, uniform norm control and F-slice — at paper-only level, with independent review and
  bounded stopping conditions."
- **Comment 7202075726** (created 2026-11-26T19:53:55Z; decision received 2026-11-26T19:52Z),
  item 3: "Preserve #1612, #1614 and #1611 at their reviewed landing heads, subject to their
  remaining verification and landing requirements. Preservation only; no premise adoption or
  manuscript integration." The same decision states: "All existing correctness, independent
  review, staging, freeze, trial and landing gates remain in force."

**Independent non-author reviews.** These are model reviews by a reviewer agent, each recorded on
PR #1614 as reviewer text posted verbatim: evidence of review, not independent mathematical
verification.
- **Comment 7201587290, review of the plan and r1 at `1a6252f4`: ACCEPT WITH NITS,** findings 1–9
  and observation 10. It checked every result by hand, found no mathematical error, and found the
  findings to concern how strongly some results are worded.
- **Comment 7201674246, delta review of r2 at `1f49e6be`: ACCEPT WITH NITS,** two nits. It
  confirmed findings 1–10 applied and checked by hand the arguments new in r2: CC-p, the two
  Neumann bounds of Prop S and the finiteness of g.
- **Comment 7201697931, delta review of r3 at `626628da`: ACCEPT WITH NITS,** one propagation
  finding: the narrowed CC-p claim survived in the CC-p heading and its §8 bullet.
- **Comment 7201722517, delta review of r4 at `05f65082`: ACCEPT.** It confirmed the propagation
  fix, with no result, proof, constant or status changed.
- **All four reviews are by one reviewer agent.** The delta reviews refer to that agent's own
  earlier reviews ("against my review of r1", "as I proposed", "my r3 propagation finding"). All
  review evidence for this record therefore comes from a single model reviewer.

## 2. Substantive result and its precise scope

Every result holds for a theory T at a level (or on the system) under the converse's hypotheses
m ≥ 2, K ≥ 2 and M_C(T, Q) < ε with ε < 1/16, with correspondences c, c′ whose soundness and
coverage terms are at most ε. Nothing is stated across levels, and nothing uses M_H. Every result
is [A].

**Gauged norm control.**
- **Lemmas R and I:** the coverage partner Φ := c′(id) of the identity is invertible, and its
  (K−1)-fold dual carries the test effects onto the projectors within 4ε.
- **Theorem G:** ‖Φ^{-1}∘F‖ ≤ C_G = 8(1+2ε)/(1−16ε) for every available family F with at most m
  outcomes. It uses no structure rule, no padding, no τ_min and no hypothesis on g. It is a bound
  in the gauge of the chosen correspondence's coverage partner of the identity, which is not
  unique; it is not norm control in the trace norm.
- **Corollary G1:** g ≤ sup_F ‖F‖ ≤ C_G‖c′(id)‖ and ‖c′(id)‖ ≤ sup_F ‖F‖, each direction separate;
  g is finite for every admissible pair whenever ε < 1/16. Over a class of theories, with a chosen
  c′ for each, two separate statements hold: if ‖c′(id)‖ ≤ ν over the class, every available
  family has norm at most C_Gν; if the available families are bounded by B over the class, then
  ‖c′(id)‖ ≤ B.

**Reduction of the converse.**
- **Lemma 7G:** Lemma 7 in the gauge of Φ, with c̃(F) = c(Φ)^{K−2}∘c(F), a quantum instrument.
- **Theorem U, each direction separate:** (U-a) for an admissible pair, with φ := ‖c′(id) − id‖,
  Lemma 7's map bounds hold for the pair (c̃, c′) with constants (1+φ)κ + φ, and Theorem 8 follows
  through unit 2's proof; (U-b) Lemma 7's coverage bound with constant κ gives φ(c′) ≤ κ. No bound
  on ‖F − c(F)‖ for the original c is claimed, and c̃ is not claimed to have soundness term at most
  ε.
- **τ_min ≤ φ(c′)** for every admissible c′.
- Norm control is necessary for the converse (Theorem U). Whether it is sufficient in class(η) at
  small η is open (UN-1).

**The system under rule (a) (Prop S):** with η_a < 1, ‖Φ^{-1}‖ ≤ C_G/(1 − η_a) and Φ^{-1} lies
within δ_S of the quantum channel c̃(I′); two one-directional perturbation bounds, each with its
own smallness condition, neither supplied by the hypotheses. At levels no bound on ‖Φ^{-1}‖ is
obtained.

**Countercontrols.**
- **Prop X1:** gauge-conjugate theories S∘Q∘S^{-1} with tr∘S = tr and M_C < ε have all norms at
  most 32(1+2ε)/(1−16ε).
- **Prop X2:** T_− = −Q (and T_ω = ωQ, ω^K = 1, ω ≠ 1) has M_C = 0 at every m, norms 1, and
  Lemma 7's conclusion fails; it lies in class(η) only for η_a, η_c, η_d, η_e ≥ 2. It is not CC-L.
- **CC-s:** T_s satisfies M_C < ε only if ((1+s)^K − 1)/2 < ε, hence only if s < 2ε/K; it is not a
  CC-L candidate.
- **CC-p:** with S^{-1} the depolarizing channel C_p, F1 holds exactly, the coverage term is at
  least p/4, and norms reach (1 + p(N−2)/N)/(1−p). F1 alone does not bound the norms; whether the
  soundness term alone does is not tested. It is a countercontrol for Prop X1, not for Theorem G.
- **Necessary conditions for CC-L:** for every admissible c′, φ(c′) not small, ‖c′(id)‖ ≥ g/C_G
  and φ(c′) ≥ τ_min.

**Outcome against the decision rule (`PLAN.md` §3), over the green controls C0 and C1:**
- **U1: N2, a relative bound.** Uniform in the gauged norm (Theorem G); in the trace norm only up
  to the factor ‖c′(id)‖ (Corollary G1). No bound on that factor, uniform over class(η) at fixed
  small η, is obtained.
- **U2:** the single residual is φ = ‖c′(id) − id‖, related to the converse in both directions
  (Theorem U); ‖c′(id)‖ is the part of φ that unit 3's marker W4 isolates.
- **U3: open.** The idle step at each level (§6 of the report) is recorded as a candidate premise
  whose sufficiency is open. It is not adopted (§A.29, §A.50 item 6), and this record adopts
  nothing.
- **CC-L: open,** with gauge conjugates and T_s excluded and the necessary conditions proved.
- The stop is by bounded effort, with the gap stated as node UN-1.

**Productivity (report §8).** NEW: Theorem G, Lemma 7G and Theorem U (under M_C the converse needs
no padding in the gauge of c′(id), and its whole residual is φ); Prop X2. ELABORATING: Prop X1,
CC-s and CC-p. BORDERLINE: §6.

**Routing note: unit 3's g = ∞ branch.** Corollary G1 shows that g is finite for every admissible
pair whenever ε < 1/16, m ≥ 2 and K ≥ 2. So the branch g = ∞ that unit 3 leaves open
(`../unit3/REPORT-r3.md` §5.2, "may be infinite"; §5.3, "excludes neither g = ∞") does not occur in
that range; the branch that remains is a finite g above unit 3's threshold (1/8 − 6ε)/ω′. This is
listed for routing only. Unit 3's record is not edited; recording it against unit 3's O2-a is a
matter for a mutable record of unit 3 or for #1216.

## 3. Verification status and remediation (§A.46 items 4 and 8)

The report carries no table of this kind; this one is built from its results (§0, §2–§6) and its
open nodes UN-1 to UN-5 (§7). Each result is a paper derivation checked only by the model reviews
of §1. The remediation plan below authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| Lemmas R and I, Theorem G | report §2 | partially verified: hand derivation, model-reviewed | independent non-model review | #1216 | a recorded independent review |
| Corollary G1, including the finiteness of g and the two directions of uniformity | report §2 | partially verified, as above; the finiteness of g was added in r2 and checked by the delta review of r2 | independent review | #1216 | a recorded independent review |
| Lemma 7G; Theorem U (U-a) and (U-b); τ_min ≤ φ | report §2–§3 | partially verified, as above | independent review | #1216 | a recorded independent review |
| Theorem 8 under (U-a) | report §3 | partially verified; relies on unit 2's proof of Theorem 8 [U2], a reviewed paper derivation, not independently verified | independent review of this step and verification of [U2]'s Theorem 8 | #1216 | a recorded review; verification of [U2] |
| Prop S and its two Neumann bounds | report §4 | partially verified; the bounds were added in r2 and checked by the delta review of r2; their smallness conditions are not supplied by the hypotheses | independent review | #1216 | a recorded independent review |
| Prop X1, Prop X2, CC-p, necessary conditions for CC-L | report §5 | partially verified: model-reviewed | independent review | #1216 | a recorded independent review |
| CC-s | report §5 | partially verified; uses T_s from unit 3's item D1, itself partially verified (definition and τ_min = s only) | independent review; verification of D1 | #1216 | a recorded review |
| C0 comparison with unit 2's constants | report §9 | asymptotic only (at ε = 1/48, κ_cov = 216ε exceeds 184ε) | none; the limitation stands as stated | #1216 | — |
| Second route of §6 (measure-and-prepare estimate) | report §6 | a sketch, not claimed | a written proof, if pursued | #1216 | a written derivation |
| UN-1: whether M_C < ε in class(η) at small η implies φ_min → 0, or a bound on ‖c′(id)‖ (unit 3's O2-a in reduced form) | report §7 | open | a proof or a counterexample | #1216 | a written derivation or an explicit theory |
| UN-2: whether an idle step at each level implies φ_min = O(ε + η_id) | report §6–§7 | open; candidate premise, not adopted | a proof or a counterexample; an owner decision on the premise | #1216 | a written derivation, a counterexample, or an owner decision (§A.29, §A.50 item 6) |
| UN-3: CC-L, a theory with small η, M_C < ε and φ(c′) bounded away from 0 for every admissible c′ | report §5, §7 | open; gauge conjugates and T_s excluded, Prop X2 only at η ≥ 2 | a realization or an exclusion | #1216 | an explicit theory or a proof of exclusion |
| UN-4: Theorem G at levels with a gauge chosen independently of c′ | report §7 | open | a proof or a counterexample | #1216 | a written derivation |
| UN-5: optimal constants in Theorem G and Lemma 7G | report §7 | open; not needed for any status | none for any status | #1216 | — |
| Preregistration order (`PLAN.md` before the report) | `PLAN.md`; §1 here | evidence is commit order only: `de344713` at 19:06:18Z precedes `1a6252f4` at 19:10:33Z (2026-11-26); with the provenance qualification of §1, the plan does not certify that the derivation started afterwards | none available from commit order alone | #1216 | none; the limitation stands as stated |

## 4. Off-`main` references (§A.42 item 8)

Each reference is classified by reading the claim it is attached to, using the three classes:
provenance, support on `main`, and support off `main` (gap).

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7199704501, 7200549806, 7202075726 (owner decisions) | `PLAN.md`, report §10; §1 here | provenance: authority records quoted with author and time; no result uses them |
| #1169 comment 7191949320 (successor assessment) | `PLAN.md`, report §10 | provenance: question source |
| PR #1614 comments 7201587290, 7201674246, 7201697931, 7201722517 (reviews) | report headers; §1 here | provenance: evidence of review; no result uses them. The provenance qualification of §1 rests on the report's own header, not on the review |
| commit `de344713` (`PLAN.md`) | report headers; §1, §3 here | support off `main` (gap), closed by the landing condition of §5: it holds the plan and the evidence of its order |
| commit `1a6252f4` (r1) | report headers; §3 here, preregistration-order row | support off `main` (gap), closed by the landing condition of §5: the order claim uses its commit time. For identifying the r1 text it is provenance |
| commits `1f49e6be` (r2) and `626628da` (r3) | report headers; §1 here | provenance: cited to identify the r2 and r3 texts; r2's header, which carries the provenance qualification, is repeated unchanged in r4 |
| commit `05f65082` (r4) | §1 here | support off `main` (gap), closed by the landing condition of §5: the authoritative report |
| the commit adding this file | — | support off `main` (gap), closed by the landing condition of §5: this record's own content |
| pin `a8d4ab96` | report headers | support on `main`: an ancestor of `main` at `84e927b9` |
| unit 2 (`../unit2/REPORT-r3.md`), unit 3 (`../unit3/REPORT-r3.md`, `../unit3/PRESERVATION.md`, item D1) | throughout | support on `main`: at the pin and unchanged at `84e927b9`; reviewed paper derivations (D1 partially verified), used for unchanged steps named where used and carried as conditions of the steps that use them |
| #1216, #1169 | headers | provenance: accountability |

**Support off `main` (gaps), and how they close.** Each gap below is closed when the merge commit
of §5 lands with the commit reachable from `main`. None is closed before that, and keeping the
branch does not close it.
- `de344713`: `PLAN.md` and the preregistration order.
- `1a6252f4`: its commit time, for the preregistration-order row.
- `05f65082`: the authoritative report.
- The commit that adds this file: this record.

## 5. Landing condition

The record is preserved only through a **merge commit, not a squash**. The merge keeps these
commits reachable from `main`:
- `de344713`, `1a6252f4`, `1f49e6be`, `626628da` and `05f65082`;
- the commit that adds this file, which follows the reviewed head `05f65082` and adds only this
  file.

That `PLAN.md`'s commit precedes every report commit is part of the record's provenance.

The owner decision of 2026-11-26T19:52Z, item 3, makes preservation subject to the record's
remaining verification and landing requirements, and keeps every existing gate in force. Merging
needs the owner's approval (§A.50 item 1).

## 6. Preservation rationale

The investigation answers rank 2 of the successor assessment and unit 3's open node O2-a in part:
whether the converse under M_C admits a norm bound derived from its hypotheses, and whether those
hypotheses admit the large-norm countercontrol. It uses a plan committed before the report, with
the provenance qualification of §1, its verdicts are printed over green controls, and its negative
statements are scoped.

It establishes:
- **a uniform norm bound in the gauge of c′(id)** (Theorem G), needing no padding, no τ_min and no
  hypothesis on g;
- **the reduction of the converse to the single number φ = ‖c′(id) − id‖**, each direction proved
  separately (Theorem U), which locates unit 3's padding obstruction (W4) in that route rather than
  in the converse;
- **that g is finite whenever ε < 1/16** (Corollary G1), which removes unit 3's g = ∞ branch
  (routing only);
- **that M_C < ε at m, K ≥ 2 does not by itself give the converse, even with bounded norms**
  (Prop X2, at η ≥ 2 only);
- **the exclusion of two candidate countercontrol classes** and necessary conditions for CC-L.

It is substantive and nonredundant with units 2 and 3, it is independently reviewed, and its open
gaps carry the remediation plans of §3.

## 7. Standing of this record

Preservation establishes no claim (§A.46 item 1). The model reviews are evidence of review, not
independent mathematical verification, and landing the record does not change any result's
evidence layer. The idle step remains a candidate premise, not adopted, and nothing is proposed
for the manuscripts.
