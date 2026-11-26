# OI-QM-APPROX-1: uniform norm control in the converse under approximate composition

Plan, recorded before any derivation and not frozen. Status of every question at this commit:
**open**.

- **Accountable home:** #1216 (OI-QM-APPROX-1); programme #1169. The question is open node O2-a of
  unit 3 (`../unit3/REPORT-r3.md` §10, line 601) and assumption-watch marker W4 (§9 there).
- **Authorization.** Owner decision at #1169 comment 7200549806 (posted from the account
  `amaybaum` 2026-11-26T18:30:55Z, quoting the owner's decision received 2026-11-26T18:30Z),
  item 4: "Authorize all three ranked scientific investigations — SMD sourcing, uniform norm
  control and F-slice — at paper-only level, with independent review and bounded stopping
  conditions." Standing work package WP-2, record #1169 comment 7199704501. The question is rank 2
  of the successor assessment, #1169 comment 7191949320: "Identify an operationally justified
  bound on the norm in the converse, then check whether the same assumptions admit the large-norm
  countercontrol."
- **Writer:** an agent of the coordinating session, designated writer of this investigation; it
  writes nothing to GitHub. Independent non-author review follows the report; no acceptance is
  claimed here.
- **Pinned source.** `main` = `a8d4ab969e274dc6ba25cbc6021da909d5aec814`. Unit 3's record
  (`../unit3/`) and unit 2's record (`../unit2/`) are on `main` at that commit.
- **Goal link (§A.47).** Serves #1216 (Foundational). The investigation decides whether the
  converse of the finite-precision characterization under M_C (unit 2's Lemma 7 and Theorem 8;
  unit 3's Lemma 7η and Theorem 8η) admits a norm bound on the available families that is derived
  from the hypotheses of the converse, or from a named operational property, and is uniform over
  class(η) at fixed η; or whether those hypotheses admit a large-norm theory for which the converse
  fails. It does not decide whether OI supplies the structure rules or the δ-conditions (unit 2
  O5), and does not bear on the kinematics (W3).

## 1. Fixed setting (inherited, unchanged)

Everything below is used exactly as fixed in `../unit2/PLAN.md` and `../unit3/PLAN.md`: the
carrier A (|A| = d), the levels and the system, the complex matrix kinematics taken as given, the
history class (adaptive protocols of horizon exactly K, outcome bound m, input densities, exact
classical control), TV, the metrics M_H and M_C (with the quantifier order of M_C: correspondences
c, c′ fixed before the supremum over protocols and inputs), the norms ‖·‖ and ‖·‖_{1→1}, the
δ-forms, the η-model class(η) and the padding-defect floor τ_min. The interface is that of the
converse under M_C: hypotheses m ≥ 2, K ≥ 2, M_C(T, Q) < ε at the level (or on Λ), T in class(η);
conclusion: correspondences c, c′ with ‖F − c(F)‖ and ‖c′(J) − J‖ at most κ(ε, η, …) → 0.

The quantity to be bounded is the norm of available families, in particular g = sup_E ‖c′(M_E)‖
of `../unit3/REPORT-r3.md` §5. Under M_H the converse is disproved in every η-class (unit 2
Theorem 5; unit 3 control C1); this investigation is about M_C only, and no M_H statement is used
as evidence for an M_C statement.

## 2. Questions

| ID | Question | Status |
| --- | --- | --- |
| U1 | Does M_C(T, Q) < ε with m, K ≥ 2 (with or without the η-rules) imply an explicit bound on the norms of available families, in a norm fixed in advance (the trace-norm induced family norm) or in a stated operational substitute? | open |
| U2 | If only a partial or relative bound is obtained: what single quantity, if any, does the converse reduce to? Each direction of any claimed equivalence is a separate question (§A.34). | open |
| U3 | Is there an operational property, stated without reference to the quantum instrument set and not chosen because it reproduces QM (§A.29), from which the missing quantity follows? Any such property is recorded as a candidate premise, not adopted (§A.50 item 6). | open |
| CC-L | Do the same assumptions admit the large-norm countercontrol: a theory T in class(η), m, K ≥ 2, M_C(T, Q) < ε, τ_min > 0, whose available families have norm of order 1/τ_min (or unbounded as ε → 0) and for which the conclusion of Lemma 7 fails for every pair of correspondences? | open |

## 3. Decision rule (fixed now)

U1 ends in exactly one of:
- **N1, bound.** An explicit bound on sup ‖F‖ (available F, at most m outcomes), proved from the
  hypotheses of the converse and the η-rules alone, uniform over class(η) at fixed small η. It
  must make hypothesis (Hg) of Lemma 7η hold for small (ε, η), so the converse holds with
  κ → 0. Status: proved (paper derivation).
- **N2, relative bound.** An explicit bound proved in a norm other than the fixed one, or proved
  up to one named residual quantity that the hypotheses do not bound. The residual is named, and
  both directions of its relation to the converse are stated separately.
- **N3, broken.** CC-L is realized. Status: disproved, for the stated class only.
- **N4, obstruction.** Neither; the step where every attempted bound fails and what would close
  it are stated.

CC-L ends in: realized (N3); excluded for a named subclass, with proof; or open.

A bound whose assumptions admit CC-L is void. A result that needs a premise outside §1 is
recorded and the investigation ends there (§A.29; §A.50 item 6).

## 4. Controls and countercontrols (fixed now)

- **C0 (exact QM).** At T = Q, with c = c′ = id, every bound must hold (norms 1), and any
  reduction must be consistent with unit 2's Lemma 7 (‖c′(J) − J‖ ≤ 184ε). Where τ_min = 0, it
  must be consistent with unit 3's Corollary 7c.
- **C1 (negative results).** No statement may contradict unit 2's Theorem 5 (M_H), Proposition 11
  (M_C at m = 1 or K = 1) or Proposition 9 (level set), which hold in every η-class (unit 3 §1.3).
  In particular no bound may drop m ≥ 2 or K ≥ 2.
- **CC-s (rescaled QM, T_s of unit 3 `PRESERVATION.md` §7).** It lies in class(η) with τ_min = s.
  Any claim about theories with τ_min > 0 must be checked against it: whether T_s satisfies the
  hypotheses M_C < ε, and whether a claimed bound holds for it.
- **CC-L (large-norm countercontrol).** As in §2. Candidates are tested against the hypotheses
  exactly as stated; a candidate that violates M_C < ε is recorded as excluded, with the
  violating protocol.

## 5. Stopping conditions

Stop when the decision rule resolves for U1 and CC-L has a status; or after a bounded effort (one
writer session) with the remaining gap stated precisely; or if the result would need a new
premise, which is recorded and not adopted. Any branch favourable to the framework is
pressure-tested before acceptance (§A.31).

## 6. What would count as each outcome

- **Bound (N1):** a theorem of the form sup ‖F‖ ≤ B(ε, η, d, m, K) with B bounded as (ε, η) → 0.
- **Relative bound (N2):** e.g. a bound in a norm defined by the theory's own protocols, or
  sup ‖F‖ ≤ C·R with R a named quantity, together with whether R is necessary.
- **Countercontrol (N3):** an explicit theory meeting every hypothesis, with the failing
  conclusion exhibited.
- **Obstruction (N4):** the failing estimate and the branch it leaves unexcluded.

## 7. Inputs and labels

- [U2]: `../unit2/REPORT-r3.md` (Lemma 7 steps A–D, N1–N5, Theorems 5 and 8, Propositions 9 and
  11); [U3]: `../unit3/REPORT-r3.md` and `PRESERVATION.md` (η-model, τ_min, Lemma P, Lemma 7η,
  (Hg), Corollary 7c, T_s). Both are reviewed paper derivations, not independently verified
  (§A.46 items 7 and 8); a result here that uses an unchanged step is stated relative to it.
- [L]: standard mathematics, recalled. [A]: this investigation's own arguments, unreviewed.
- Small local numerical controls are permitted; their code and output are recorded here.
- Provenance only: the owner decisions and the successor assessment cited above. No content off
  `main` is used as support (§A.42 item 8).

## 8. Boundaries

Paper-only. No manuscript change, no premise adopted, no frozen record edited, no GitHub write,
no push.
