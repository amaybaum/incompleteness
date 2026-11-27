# OI-QM-APPROX-1, UN-1: the identity partner in the converse under M_C — report, revision r2

Revision r2 applies the independent review of r1 (`REPORT.md`, commit
`d4d9846146f73f3ed80cb4f0846646a2d08aeb08`), posted on PR #1622 with verdict REVISE (minor) and no
mathematical error found. r1 and `PLAN.md` are unchanged. The change map is `CHANGES-r2.md`.

This is the writer's report under `PLAN.md` (commit `b2adbd64bae000d42a7a03887aa4410e3b0f7006`).
That plan fixes the questions, the decision rule, the controls and the stopping conditions, which
are not restated here. Pinned source: `main` = `13c05b4fe666c2e128eed1213874be9b8208982d`.

Labels:
- [A]: this unit's paper argument, unreviewed.
- [UNC]: `../uniform-norm-control-20261126/REPORT-r4.md`.
- [U3]: `../unit3/REPORT-r3.md`.
- [U2]: `../unit2/REPORT-r3.md`.
- [L]: standard mathematics.

[UNC], [U3] and [U2] are reviewed paper derivations, not independently verified. Each result
below that uses them is conditional on the named step.

No computation was run. Nothing here is adopted, promoted or proposed for the manuscripts. The
no-push and no-GitHub-write boundary of `PLAN.md` §7 applies to the writer. Publication of the
record by the coordinating session is outside it.

## 0. Results

| ID | Result | Premises | Status |
| --- | --- | --- | --- |
| Theorem D (dichotomy) | For every admissible c′ at a level (or the system), with ν := ‖c′(P)‖: if 6ε + ω′C_Gν ≤ 1/8, then φ(c′) ≤ 184ε + 16ω′C_Gν. Hence either ν ≥ ν_+ := (1/8 − 6ε)/(ω′C_G), or φ(c′) ≤ φ_− := (184ε + 16ω′C_G)/(1 − 16ω′C_G), the latter when 16ω′C_G < 1 | m, K ≥ 2, M_C < ε, T in class(η); [U3] Lemma 7η; [UNC] Corollary G1 | proved [A], conditional on [U3] Lemma 7η and [UNC] G1 |
| Corollary D1 | Bounded norm suffices in class(η): along any family with ‖c′(P)‖ ≤ ν fixed, φ(c′) → 0 as (ε, η) → 0 | same | proved [A], same conditions |
| Prop I (idle step) | τ_min ≤ ι ≤ φ_min, where ι is the distance from the identity of the nearest available single-outcome family. On the small branch of Theorem D, an idle step within φ_− exists. The six rules alone do not give one at levels (unit 2's T^{(L)}) | as stated | proved [A] (the last clause relative to [U2] Proposition 9) |
| Obstruction | The large branch ν ≥ ν_+ (ν_+ → ∞ as η → 0 at fixed K) is not excluded. A D3 theory must lie on it for every admissible c′ | — | open |

**Outcome against the decision rule (`PLAN.md` §3).**
- **Q-A/Q-B: D2, controlled on a reduced scope; the remainder obstructed.**
  - *Scope controlled:* τ_min = 0 at the level (the padding rules in closure, in particular
    η = 0). There φ ≤ 184ε for every admissible pair. This is proved in unit 3 (Corollary 7c) and
    the predecessor (Theorem U (U-b)); the scope and its proof are inherited, not new to this unit.
  - *Remainder obstructed:* in class(η) where τ_min > 0, no φ_bound is obtained for every
    admissible c′. Theorem D excludes every admissible c′ whose identity partner has norm below
    ν_+, because each such c′ has φ ≤ φ_− → 0. So a counterexample (D3) needs
    ‖c′(P)‖ ≥ ν_+ ≈ 1/(8(3K − 4)τ_min C_G) for **every** admissible c′. No such theory was found;
    this large branch is the obstruction.
- **The predecessor's sufficiency question is closed positively (Corollary D1).** In class(η) at
  small η, a bounded identity-partner norm forces φ → 0. The bounded-norm counterexample Prop X2
  [UNC] has no analogue inside class(η) at small η.
- **Q-C: open.** Two sub-results stand:
  - on the small branch of Theorem D, the identity partner is itself an idle step within φ_−
    (Prop I (ii));
  - the six exact rules alone do not supply one at levels (Prop I (iii)).

  Whether the converse's hypotheses supply an idle step in general (on the large branch) is
  open. The idle step
  stays a **candidate premise**, not adopted (§A.29, §A.50 item 6). Its sufficiency (UN-2) is open.
- **Q-D.** The structure rules enter only through τ_min: rules (b) and (e) at a level, and (a), or
  (e), (d1) and (f), on the system ([U3] §3). The obstruction scales as 1/τ_min.

The stop is by bounded effort, with the gap stated (§6).

***

## 1. Theorem D

Fix a level n (or the system), m ≥ 2, K ≥ 2, T in class(η), and an admissible pair (c, c′) with
both terms at most ε. Let τ_min be T's padding-defect floor there,
ω_j := (1+τ_min)^j − 1 and ω′ := 2ω_{K−1} + ω_{K−2} ([U3] §5). Let ν := ‖c′(P)‖_{1→1} and
g := sup_E ‖c′(M_E)‖.

**Theorem D [A].** If 6ε + ω′C_Gν ≤ 1/8, then ‖c′(J) − J‖ ≤ 184ε + 16ω′C_Gν for every quantum
instrument J with at most m outcomes. In particular φ(c′) ≤ 184ε + 16ω′C_Gν.

*Proof.*
1. Since 6ε ≤ 1/8, ε ≤ 1/48 < 1/16. Corollary G1 [UNC] gives g ≤ C_Gν < ∞.
2. Then μ := 6ε + ω′g ≤ 6ε + ω′C_Gν ≤ 1/8, so the second case of hypothesis (Hg) of [U3]
   Lemma 7η holds. (When ω′ = 0, the first case holds and Corollary 7c [U3] gives the stronger
   bound 184ε.)
3. Lemma 7η [U3] gives ‖c′(J) − J‖ ≤ 88ε + 16μ ≤ 88ε + 96ε + 16ω′C_Gν.
4. Take J = P for φ. □

**The dichotomy.** For an admissible c′, either ν ≥ ν_+ := (1/8 − 6ε)/(ω′C_G), or Theorem D
applies.
- In the second case, ν = ‖Φ‖ ≤ 1 + φ, so φ ≤ 184ε + 16ω′C_G(1 + φ).
- When 16ω′C_G < 1, this gives φ ≤ φ_− := (184ε + 16ω′C_G)/(1 − 16ω′C_G).
- As (ε, η) → 0 at fixed (d, n, m, K): τ_min ≤ τ(n) → 0 ([U3] §3), so ω′ → 0, φ_− → 0 and
  ν_+ → ∞.

**Corollary D1 [A].** Let a family of pairs (T, c′) in class(η) satisfy ‖c′(P)‖ ≤ ν for a fixed ν,
and let (ε, η) → 0. Then φ(c′) → 0, and by Theorem U (U-a) [UNC] the converse holds for (c̃, c′)
with constants → 0. This answers the sufficiency part of the predecessor's UN-1 positively inside
class(η). The predecessor's Prop X2 (T_− = −Q, φ = 2) lies outside class(η) at small η
(τ_min = 2), consistent with control C1.

*Pressure test (favourable branch, §A.31).*
1. *The quantifier order in Lemma 7η.* Lemma 7η is stated for fixed (c, c′) with terms at most ε
   satisfying (Hg). Here g is read from the same c′, through G1, so no hypothesis is shared across
   correspondences.
2. *The constants.* At ω′ = 0 the bound is 184ε, which is unit 2's Lemma 7 bound (C0).
3. *Is the step new?* Unit 3 left the branches g = ∞ and g ≥ (1/8 − 6ε)/ω′ open. G1 removes the
   first, and expresses the second as a property of one family, c′(P). Theorem D is that
   combination. It adds no estimate of its own to Lemma 7η and G1. Its content is that the
   residual of the converse in class(η) is the single large-norm branch of φ.
4. *C1.* For T_−, ω′ is large (τ_min = 2), so ν_+ < 1 and Theorem D says nothing. T_− is
   therefore not contradicted.

## 2. Prop I: the idle step

Let ι := inf ‖D′ − id‖_{1→1} over available single-outcome families D′ at the level.

**Prop I [A].**
- (i) τ_min ≤ ι ≤ φ_min. The identity is a channel, and Φ = c′(P) is an available single-outcome
  family.
- (ii) If some admissible c′ lies on the small branch of Theorem D, then ι ≤ φ_− → 0. An idle step
  is then derived, with η_id = φ_−.
- (iii) The six exact rules, without M_C at the level, do not give an idle step at levels. Unit 2's
  T^{(L)} [U2, Proposition 9] is a `FiniteOperationalTheory`. Every available level-L map returns
  0 on ρ ⊗ |0⟩⟨1|, so every available single-outcome D′ at L has ‖D′ − id‖ ≥ 1. Moreover
  M_C(T^{(L)}, Q) ≥ 1/184 at L, so (iii) does not contradict (ii).

*Proof.* (i) follows from the definitions. (ii) follows from (i) and Theorem D. (iii): for
X = ρ ⊗ |0⟩⟨1| (‖X‖₁ = 1), ‖(D′ − id)X‖₁ = ‖X‖₁ = 1 ([U2] Proposition 9's computation).

For the bound on M_C: the Lüders readout at L has Kraus operators 1_A ⊗ |k⟩⟨k|, which are of the
admitted form, so it is available, and its coarse-graining is an available dephasing channel.
Hence τ_min = 0 at L. If M_C(T^{(L)}, Q) < ε ≤ 1/48 at L, then Corollary 7c [U3] gives
φ(c′) ≤ 184ε for an admissible c′. But φ(c′) ≥ 1 by the computation above, so ε ≥ 1/184. Since
1/184 < 1/48, M_C(T^{(L)}, Q) ≥ 1/184 at L. □

**Status of Q-C.**
- On the system, the idle step is rule (a), which class(η) supplies (η_id = η_a).
- At levels, it is not derivable from the rules alone (iii). It is derived from M_C on the small
  branch (ii). It is open on the large branch. Q-C therefore prints **open**.

So the idle step is not established as a consequence of the existing structure, and it remains a
candidate premise, not adopted.

Its sufficiency (UN-2: idle step ⇒ φ_min small) is still open. With an idle step I′,
[UNC] Prop S's argument bounds ‖Φ^{-1}‖, a lower bound on Φ, but not ‖Φ‖. Replacing c′(P) by I′
is not shown to keep the coverage term at most ε.

## 3. The large branch (CC-L / D3)

A D3 theory needs ‖c′(P)‖ ≥ ν_+ for every admissible c′. Theorem U (U-a) and G1 [UNC] then imply
the following of it:
- the available families are, in the gauge of Φ, within κ_snd of Φ∘(quantum instruments);
- some available family has norm of order ν_+;
- τ_min ≤ ι ≤ φ_min.

Candidates checked, each against every hypothesis:
- **Gauge conjugates S∘Q∘S^{-1}** (tr∘S = tr): all norms are at most 32(1+2ε)/(1−16ε) ([UNC]
  Prop X1), below ν_+ for small η. Excluded.
- **Rescaled QM T_s** (unit 3's D1, partially verified): M_C < ε only for s < 2ε/K ([UNC] CC-s).
  Its norms are then about 1, so it is on the small branch. Excluded.
- **T_S with S^{-1} = C_p:** for p > 4ε it fails the coverage term, which is at least p/4
  ([UNC] CC-p), so M_C < ε fails. For p ≤ 4ε it is a gauge conjugate (tr∘C_p^{-1} = tr), so Prop
  X1 bounds its norms by 32(1+2ε)/(1−16ε), below ν_+ for small η. The two cases together cover
  every p. Excluded.
- **T_− and T_ω:** they lie outside class(η) at small η. Excluded by scope.

No candidate on the large branch was found.

**What blocks a proof.** Two further routes were tried. Each excludes only a window of ν.
- **Through Lemma 7η (Theorem D).** The window is [≈1, ν_+), with ν_+ ∝ 1/τ_min.
- **Through tail effects at K = 2 (sketch, not claimed).** Lemma 7G's coverage half writes
  G_E ≈ Φ∘M_E in the gauge. With Lemma R it gives Φ†(EΓ_ΦE) ≈ E for every projector E, where
  Γ_Φ = Φ†(I), with error 4ε + κ_cov‖Φ‖‖Γ_Φ‖. On rank-one E this forces Φ ≈ ±id when the error is
  small. Since ‖Γ_Φ‖ ≤ ‖Φ‖, the error is quadratic in ‖Φ‖ with coefficient O(ε), so the route
  excludes only ‖Φ‖ ∈ (≈1, ≈ε^{-1/2}). Its window does not depend on η. Its constants are not
  written out, so it is recorded as a sketch.

In both routes the information that M_C gives about un-gauged quantities is multiplied by
un-gauged sizes. This is marker W5 of [UNC]. No route found here excludes the large branch.

## 4. Controls (`PLAN.md` §4)

| Control | Check | Status |
| --- | --- | --- |
| C0 | At T = Q, c = c′ = id: τ_min = 0, ω′ = 0, φ = 0 ≤ 184ε. The idle step is the identity | green |
| C1 | Theorem D says nothing for T_− (ν_+ < 1), and Prop I (iii) uses unit 2's Proposition 9 without contradicting it. No statement drops m, K ≥ 2 or crosses levels | green |
| CC-p | Theorem D uses both terms of M_C (through G1 and Lemma 7η), not F1 alone. T_S with S^{-1} = C_p fails coverage and is not a counterexample | green |
| D3 candidates | four candidate families checked, all excluded (§3) | checked |

The verdicts are printed over green controls.

## 5. Classification (§A.31)

- **Theorem D and Corollary D1: ELABORATING.** They combine [U3] Lemma 7η with [UNC] G1. Their
  content is that, inside class(η) at small η, the converse's residual is the large-norm branch of
  the identity partner alone, and that bounded norm suffices.
- **Prop I: ELABORATING.** The idle step is not derivable from the rules alone at levels. It is
  derivable on the small branch.
- **§3 sketch: BORDERLINE.**

The decision rule (PLAN §3) prints D2 for Q-A/Q-B (inherited scope, remainder obstructed) and
open for Q-C. No NEW finding is claimed.

## 6. Open nodes

| ID | Node | Status |
| --- | --- | --- |
| UN1-a | Exclude the large branch ‖c′(P)‖ ≥ ν_+ for some admissible c′, or construct a D3 theory on it | open |
| UN1-b | Does an idle step at a level (with M_C < ε) hold on the large branch? | open; candidate premise, not adopted |
| UN1-c | UN-2: does an idle step imply φ_min small? | open |
| UN1-d | Write out the constants of the K = 2 tail-effect route (§3), which would give an η-independent window | open; sketch only |

## 7. Verification status and remediation (§A.46 item 4)

No result here is independently verified. The plans below authorize no work (§A.45 rule 3).

| Claim | Where | Evidence level | Missing verification | Accountable Issue | What would resolve it |
| --- | --- | --- | --- | --- | --- |
| Theorem D, Corollary D1 | §1 | paper derivation [A], conditional on [U3] Lemma 7η and [UNC] G1, both reviewed but not independently verified | independent review of this report; independent verification of Lemma 7η and G1 | #1216 | a recorded independent review; a verification of the inherited steps |
| Prop I (i), (ii) | §2 | paper derivation [A] | independent review | #1216 | a recorded independent review |
| Prop I (iii) | §2 | paper derivation [A] relative to [U2] Proposition 9, and, for the bound M_C(T^{(L)}, Q) ≥ 1/184, to [U3] Corollary 7c and [UNC] Theorem U (U-b); all three are reviewed but not independently verified | independent review; independent verification of [U2] Proposition 9, [U3] Corollary 7c and [UNC] (U-b) | #1216 | a recorded independent review; a verification of the inherited steps |
| Exclusions of §3 | §3 | applications of [UNC] Prop X1, CC-s and CC-p, and of scope | as for those results | #1216 | as recorded in the predecessor's preservation record |
| K = 2 tail-effect route | §3 | sketch, not claimed | a written derivation | #1216 | UN1-d |
| The large branch (UN1-a) | §3, §6 | open | a proof or a counterexample | #1216 | a written derivation or construction |
| Plan before derivation | `PLAN.md` | commit order only; the earlier informal exploration is disclosed in the plan | none available from commit order | #1216 | the limitation stands as stated |

## 8. Off-`main` references (§A.42 item 8)

| Reference | Where | Classification |
| --- | --- | --- |
| #1169 comment 7208939261 (owner decision), #1169 comment 7199704501 (WP-2) | `PLAN.md` | provenance: authority, quoted with author and time; no result uses them |
| #1216, #1169 | `PLAN.md`; §7 | provenance: accountability |
| `../uniform-norm-control-20261126/REPORT-r4.md` (G1, Theorem U, Lemmas R and 7G, Props S and X1, X2, CC-s and CC-p) | §0–§4 | support on `main` at the pin (landed through #1614) |
| `../uniform-norm-control-20261126/PRESERVATION.md` (verification status and scope of the predecessor's results used here) | §0–§4, §7 | support on `main` at the pin |
| `../unit3/REPORT-r3.md` (Lemma 7η, (Hg), Corollary 7c, τ_min, τ(n), ω′) | §1, §2 | support on `main` at the pin |
| `../unit2/REPORT-r3.md` (Proposition 9, Lemma 7) | §2, §4 | support on `main` at the pin |
| PR #1622 review of r1 | header | provenance: findings applied in r2; no result uses its content |
| PR #1614 | header lineage | provenance: no result uses its discussion |
| commit `b2adbd64` (this unit's plan) | header | support for the plan-order row of §7 once it is on `main`; not before |

Support off `main`: none, apart from this unit's own commits until they land.
