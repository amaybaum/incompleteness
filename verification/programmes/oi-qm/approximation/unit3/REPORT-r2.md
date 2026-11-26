# OI-QM-APPROX-1, unit 3 (O2): approximate structure rules — report, revision r2

Revision r2 of the writer's report. It applies findings F1–F8 of the independent review of r1. That
review is on PR #1596, comment 7189898722: posted from the account `amaybaum` at
2026-11-26T10:50:04Z, carrying the reviewer text verbatim, with verdict REVISE (minor). r1
(`REPORT.md`, commit `9d5b5dc1`) is kept unchanged. The change map is `CHANGES-r2.md`.

F1 strengthens a result in a direction favourable to the framework. Its argument was re-derived
here before adoption (§A.22, §A.31). It is recorded as [A], and its origin in the review is stated
in §8. The productivity verdict is provisional until a delta review of this revision.

The following are fixed in `PLAN.md` (commit `92969d74ba364af5fecff1524ca9e4809e700dbf`) and are
not restated:
- the η-model;
- the questions;
- the decision rule;
- the controls;
- the baseline S and the productivity test;
- the stopping rule;
- the Goal link.

Pinned source: `main` = `353a066f18766837fed8c7f58507e09ff549b1a4`. "OB/" =
`verification/lean-mathlib/OIBridge/`.

Labels:
- [A]: this unit's own paper argument.
- [U2]: unit 2's argument (`../unit2/REPORT-r3.md`, commit `b1037933`), a reviewed paper
  derivation that has not been independently verified. It is used only where the step is
  unchanged.
- [K], [P], [L]: as in `PLAN.md` §9.

No computation was run. Nothing here is adopted, promoted or proposed for the manuscripts.

## 0. Results

| ID | Metric | Branch | Result | Where |
| --- | --- | --- | --- | --- |
| Q0η | none | passed | (M1)–(M3) hold. C1 is green. CC (T_triv) is verified, with one precision: its M_H ≥ 1/2 holds on carriers of dimension at least 2. | §1 |
| Q1-C | M_C | B1 | Theorem 4η: an explicit ε(δ, η, d, n, m, K) → 0. Soundness does not depend on η. Coverage gains terms in η_e(2), η_c(L) and η_b(L), and, for system histories, in η_d(1) and η_f. Neither η_a nor rule (d2) enters. | §4 |
| Q1-H | M_H | B1 | The same bound, through M_H ≤ M_C. Whether any η_r can be removed under M_H: open. | §4.4 |
| Q2-L7 | M_C | B4 for a bound uniform over class(η) at fixed η > 0 | At a level whose padding-defect floor τ_min is 0, unit 2's Lemma 7 holds verbatim (Corollary 7c). In general, Lemma 7η gives κ = 88ε + 16μ with μ = 6ε + ω′(τ_min)g, for correspondences satisfying (Hg). It tends to 0 when ω′g → 0. | §5.2 |
| Q2-T8 | M_C | B4 for a bound uniform over class(η) at fixed η > 0 | Theorem 8η: C_{(N_Λ+1)κ_Λ}[m, Λ] under (Hg) at each level of Λ. Unit 2's Theorem 8 holds verbatim where τ_min = 0 at every level of Λ. (Hg) follows from a crude validity bound V_{δ0}. m, K ≥ 2 and the level-set condition remain necessary (C1). | §5.4 |
| Q2-H | M_H | disproved (C1) | Theorem 5 holds in every η-class. | §1.4 |
| Q3 | M_C | proved, both directions separately | For theories satisfying the rules in closure, (a) ⇒ (b) and (b) ⇒ (a) are each proved. | §6 |

Productivity verdict (`PLAN.md` §7): **gem**, provisional until the delta review. The grounds:
- **G3:** the obstruction of §5.3, which concerns bounds uniform over class(η) at fixed η > 0, and
  single theories with a positive padding-defect floor.
- **G1:** Lemma 7η and Corollary 7c, whose proofs need the bootstrap and the limit argument of
  §5.2, which go beyond S.

Q1 alone is the baseline S, which makes it record-only. The independent reviewer decides (§12).

***

## 1. Node 0

### 1.1 Model properties

- **(M1).** ‖·‖ is a norm on families with a fixed outcome set, so "some available Y has
  ‖Y − X‖ ≤ 0" holds exactly when X is available. For rule (e) at η_e = 0, localLuders_n is
  available. It is spectator-independent (`mapSpectatorIndependent_iff_localLuders`, the lemma
  behind `readout_is_localLuders`, OB/OperationalAssembly.lean:658 [K]), so it can serve as the
  kernel's `readout` field. Conversely, `readout_is_localLuders` gives readout n = localLuders.
  Hence class(0) = `FiniteOperationalTheory`.
- **(M2).** Each η-form is monotone in its η_r.
- **(M3).** Each exact object X of `PLAN.md` §2 is built from available objects and kinematic
  maps: id, coarse_f, bind, uniformAttach, Φ ∘ P, localLuders, discardWith. None refers to
  `IsFiniteEndomorphicKrausInstrument`.

### 1.2 Rule (e′) to rule (e_η): the conversion constant

**Lemma E [A].** If an n-outcome family R at level n satisfies (e′) with η′, then
‖R − localLuders_n‖ ≤ min(d, n)·η′. Conversely, (e_η) gives (e′) with η′ = η_e.

*Proof.*
1. Let Δ_k = R_k − localLuders_k, and let u, v be unit vectors in ℂ^A ⊗ ℂ^n.
2. Take Schmidt decompositions u = Σ_{p ≤ r} α_p a_p ⊗ b_p and v = Σ_q β_q a′_q ⊗ b′_q, with
   r ≤ min(d, n).
3. Then |u⟩⟨v| = Σ_{p,q} α_p β_q |a_p⟩⟨a′_q| ⊗ |b_p⟩⟨b′_q|, a sum of products of trace-norm-1
   factors.
4. So Σ_k ‖Δ_k(|u⟩⟨v|)‖₁ ≤ η′ (Σ_p α_p)(Σ_q β_q) ≤ η′ r, by Cauchy–Schwarz (Σ α_p ≤ √r).
5. Sum over a singular value decomposition of a general matrix.
6. The converse holds because ‖X ⊗ Y‖₁ = ‖X‖₁‖Y‖₁. □

### 1.3 C1: unit 2's counterexamples lie in every η-class

T_alg, T_dec and T^{(L)} are `FiniteOperationalTheory` instances [U2]. By (M1) and (M2) they lie
in class(η) for every η ≥ 0. Their stated failures concern the δ-forms and the metrics, which the
η-model leaves unchanged. So the following hold in every η-class:
- Proposition 1;
- Theorem 5;
- Proposition 11;
- Proposition 9.

**C1: green**, relative to [U2].

### 1.4 Q2-H

By C1, Direction 2 under M_H is disproved in every η-class, by Theorem 5 [U2].

### 1.5 CC: verification of T_triv

T_triv is defined in `PLAN.md` §5.3: the available families are the F_a = p_a Φ_a, with (p_a) a
probability vector and each Φ_a completely positive and trace preserving; the available
preparations are the completely positive, trace-preserving maps from the system into a level.

**Rules (a), (b), (c), (d) and (f) hold exactly:**
- (a): id has p = 1 and Φ = id.
- (b): Σ_{f(j)=a′} p_j Φ_j = q_{a′} Ψ_{a′}, where q_{a′} = Σ_{f(j)=a′} p_j and Ψ_{a′} is the
  corresponding mixture of channels (any channel when q_{a′} = 0).
- (c): bind(F, G)_{(a,b)} = p_a q^{(a)}_b (Ψ^{(a)}_b ∘ Φ_a).
- (d): uniformAttach(r), and Φ ∘ P with Φ a channel, are completely positive and trace
  preserving.
- (f): ptr ∘ p_a Φ_a ∘ P = p_a (ptr ∘ Φ_a ∘ P).

**Rule (e).**
- R_n with every branch (1/n)·id is available. Both R_n and localLuders_n have norm 1 (N1 [U2]),
  so (e_η) holds with η_e(n) ≤ 2. At n = 1, R_1 = id = localLuders_1, so η_e(1) = 0.
- Exact (e) fails at every n ≥ 2. Let F_a = p_a Φ_a have n outcomes, take k with p_k ≤ 1/n, and
  take X = ρ ⊗ |k⟩⟨k|. Then Σ_a ‖F_a(X) − δ_{ak}X‖₁ ≥ (1 − p_k) + Σ_{a≠k} p_a = 2(1 − p_k)
  ≥ 2(1 − 1/n).
- Hence η_e(n) ∈ [2(1 − 1/n), 2] for T_triv.

**The five conditions hold exactly (δ = 0):**
- V: every branch is positive, and the traces sum to the input trace.
- L, I and C: transport, withSpectator and uniform attach-run-discard each preserve the form
  p_a·(channel).
- U: conj U is a channel.

**M_H ≥ 1/2.**
1. Every T_triv protocol has a law independent of the input density: by induction,
   P(o⃗) = Π_t p^{(t)}_{o_t}.
2. On a carrier of dimension at least 2, take orthonormal e_0 and e_1. The quantum protocol
   (Lüders {|e_0⟩⟨e_0|, 1 − |e_0⟩⟨e_0|}, then identity channels) gives point-mass laws on
   different sequences for the inputs e_0 and e_1, at TV distance 1.
3. So every T_triv protocol is at distance at least 1/2 from one of these laws.
4. Hence M_H ≥ 1/2, and so M_C ≥ 1/2, for m = 2 and every K, on the system when d ≥ 2 and at
   every level with N ≥ 2. `PLAN.md` §5.3 said "on the system and at every level"; the condition
   on the carrier dimension is needed there.

**CC: verified.** The bound check is in §4.3.

***

## 2. Node 1: census of exact-rule uses in unit 2

| Unit 2 step | Rule | Level | Property taken |
| --- | --- | --- | --- |
| Theorem 2 (soundness), level and system | none | — | only V_δ, I_δ and L_δ |
| Theorem 3, binary readout of each qubit | (e) | 2 | the native level-2 readout equals localLuders; then I_δ into L |
| Theorem 3, composing 3k + 1 layers | (c) | L = n·2^k | the composite is available (3k binds) |
| Theorem 3, coarse-graining to J's outcomes | (b) | L | the coarse-grained family is available |
| Theorem 3, system case (`avail_of_availExt_one`, OB/LevelOneSeam.lean:107 [K]) | (d1) with r = 1, and (f) | 1, system | transport of an available level-1 family is available |
| Theorem 4 | none directly | — | through Theorems 2 and 3 |
| Lemma 7, padding D_T | (e), (b) at level n; (a) on the system | n, system | **exact trace preservation of the padding**, used in step A (applied to G_E) and in step C |
| Lemma 7, steps B and D | none | — | the padding there is the soundness partner of c′(P), a quantum channel |
| Theorem 8 | none directly | — | through Lemma 7 |

Every Direction 1 use takes an availability statement and then uses the map only through norm
estimates. The Lemma 7 use takes exact trace preservation, which a perturbation does not keep by
the triangle inequality alone, because the trace defect multiplies the norm of the map applied
*before* the padding. Unit 2 has no estimate of that norm in Direction 2.

***

## 3. Auxiliary lemmas [A]

- **B (bind difference).** ‖bind(F, G) − bind(F′, G′)‖ ≤ max_a ‖G(a)‖·‖F − F′‖ +
  max_a ‖G(a) − G′(a)‖·‖F′‖.
  - *Proof.* Write G(a)_b F_a − G′(a)_b F′_a = G(a)_b(F_a − F′_a) + (G(a)_b − G′(a)_b)F′_a.
    Sum the trace norms over (a, b), using Σ_b ‖H_b(Y)‖₁ ≤ ‖H‖‖Y‖₁. □
- **P (padding defect).** Let D be completely positive and trace preserving, and D′ a map with
  ‖D′ − D‖_{1→1} ≤ τ. Then for every matrix Y and every j ≥ 0,
  |tr D′^j(Y) − tr Y| ≤ ω_j ‖Y‖₁, with ω_j := (1+τ)^j − 1.
  - *Proof.* |tr D′(Z) − tr Z| = |tr((D′ − D)Z)| ≤ τ‖Z‖₁, and ‖D′^i Y‖₁ ≤ (1+τ)^i ‖Y‖₁.
    Telescope over the j steps. □
- **Paddings in class(η).**
  - At level n ≥ 2: coarse-graining is non-expansive, so some available single-outcome D′ lies
    within τ(n) := η_e(n) + η_b(n) of the dephasing channel coarse(localLuders_n), which is
    completely positive and trace preserving.
  - At level 1: R_1 itself serves, with τ(1) := η_e(1).
  - On the system: τ_sys := min(η_a, η_e(1) + (1 + η_e(1))η_d(1) + η_f). The second entry is the
    route of §4.1 applied to R_1.
- **Padding-defect floor.** At a level (or the system), τ_min(T) is the infimum of ‖D′ − D‖_{1→1}
  over available single-outcome families D′ and completely positive, trace-preserving maps D. It
  is a property of the theory. In class(η), τ_min ≤ τ(n), τ(1) or τ_sys respectively. The padding
  rules **hold in closure** at a level when τ_min = 0 there. This holds in particular when (b)
  and (e) at level n (respectively (a), or (e), (d1) and (f), on the system) hold for every
  positive value of their parameters.
- **V (norm from crude validity).** If V_{δ0} holds for a family G with at most m outcomes at a
  level, then ‖G‖ ≤ 2(1 + (2m+1)δ0).
  - *Proof.* For a density σ, let Y_b = G_b(σ) and let P_b ≥ 0 with ‖Y_b − P_b‖₁ ≤ δ0. Then
    ‖Y_b‖₁ ≤ tr P_b + δ0, and Σ_b tr P_b ≤ Re Σ_b tr Y_b + mδ0 ≤ 1 + δ0 + mδ0. For a general
    input, split it into four positive parts (N5 [U2]). □

***

## 4. Direction 1 (Q1)

Fix a level n, with N = d·n, k = ⌈log₂(m N²)⌉, L = n·2^k and D = 3k + 1. Let

β := δ + 2d·η_e(2).

### 4.1 Coverage

**Theorem 3η (coverage) [A].** Assume:
- U_δ at level L;
- I_δ for the two-outcome family R_2 of rule (e_η) at level 2, from level 2 into level L;
- C_δ for families with at most m outcomes into level n;
- the η-rules (e) at level 2, and (c) and (b) at level L.

Then every quantum instrument J at level n with at most m outcomes has an available G with the
same outcome set and

‖G − J‖ ≤ ε_c(η) := (1+β)^D − 1 + η_c(L)·Σ_{j=0}^{D−2} (1+β)^j + η_b(L) + δ.

*Proof.* The construction is unit 2's [U2]: Stinespring unitary, seed, final readouts, then C_δ.
Only the error count changes.

1. *Readout piece.*
   - R_2 is available with ‖R_2 − localLuders_2‖ ≤ η_e(2).
   - I_δ gives an available family at level L within δ of withSpectator(R_2).
   - By N3 [U2], with input dimension 2d, ‖withSpectator(R_2) − withSpectator(localLuders_2)‖
     ≤ 2d·η_e(2).
   - So the piece lies within β of the exact readout layer, which has norm 1.
2. *Unitary, flip and identity pieces.* These come from U_δ: within δ ≤ β of exact layers of
   norm 1.
3. *Composition.*
   - Let H_1 be the first piece. Let H_t be an available family within η_c of bind(H_{t−1}, L_t),
     where L_t(o) is the t-th layer's piece chosen by the earlier outcomes.
   - Let E_t be the exact composite, a quantum instrument of norm 1.
   - Lemma B gives err_t := ‖H_t − E_t‖ ≤ (1+β)err_{t−1} + β + η_c, with err_1 ≤ β.
   - By induction, err_D ≤ (1+β)^D − 1 + η_c Σ_{j=0}^{D−2}(1+β)^j.
4. *Coarse-graining.* Some available K lies within η_b of coarse(H_D). Coarse-graining is
   non-expansive, so ‖K − coarse(E_D)‖ ≤ err_D + η_b.
5. *Discard.* Uniform attachment followed by partial trace has norm 1, and applied to
   coarse(E_D) it gives exactly J [U2]. C_δ adds δ. □

**System instruments.** Apply Theorem 3η at level 1 to transport(J). This gives an available G at
level 1 with ‖G‖ ≤ 1 + ε_c|_{n=1}. Then:
- (d1) gives an available P_1 within η_d(1) of uniformAttach(1);
- (f) gives an available system family within η_f of discardWith(P_1, G);
- ‖discardWith(P_1, G) − discardWith(uniformAttach(1), G)‖ ≤ ‖G‖·η_d(1);
- discardWith(uniformAttach(1), G) = transport(G) (`discardWith_uniform_one_eq_transport`,
  OB/LevelOneSeam.lean:98 [K]), and transport is an isometry.

Hence

ε_c^{sys}(η) := ε_c|_{n=1} + (1 + ε_c|_{n=1})·η_d(1) + η_f.

### 4.2 History laws

**Theorem 4η (Direction 1, metrics M_C and M_H) [A].** At fixed (d, m, K) and level n, assume:
- C_δ[max(m, 2), Λ₁(n, m)] with δ(N(m+1) + 1) < 1;
- the η-rules of Theorem 3η.

Let ε₁ = max(ε_s, ε_c(η)), with ε_s = δ(4N(m+1) + 3) as in Theorem 2 [U2], which does not depend
on η. Then

M_H(T, Q) ≤ M_C(T, Q) ≤ ½((1+ε₁)^K − 1).

For system histories, use ε_s^{sys} and ε_c^{sys}(η), with the additional rules (d1) at r = 1
and (f).

*Proof.* Unit 2's proof applies unchanged [U2]:
- soundness by Theorem 2 and N4 with e = s = ε_s;
- coverage by Theorem 3η and N4 with e = ε_c(η) and s = ε_s. By Theorem 2 the coverage partner
  has norm at most 1 + ε_s. □

**Contribution of each rule** (the other parameters at 0), with D − 1 = 3k:

| Rule | Enters? | Level read | Form |
| --- | --- | --- | --- |
| (e) | yes | 2 only | inside β, as 2d·η_e(2), amplified by (1+β)^D |
| (c) | yes | L | η_c Σ_{j=0}^{3k−1}(1+β)^j ≤ 3k η_c (1+β)^{3k−1} |
| (d) | system histories only | 1 (d1, r = 1) | (1 + ε_c|_{n=1}) η_d(1) |
| (f) | system histories only | system | η_f |
| (b) | yes | L | η_b(L), additive |
| (a) | no | — | — |

Rule (d2) does not enter. The readout parameter is read only at level 2, not at n or at L.

### 4.3 Controls for Direction 1

- **C0.** At η = 0:
  - β = δ;
  - ε_c(0) = (1+δ)^{3k+1} − 1 + δ;
  - ε_c^{sys}(0) = ε_c|_{n=1}, which is unit 2's statement that "Theorem 3 at level 1 gives the
    same bound";
  - ε_s and ε_s^{sys} are unchanged;
  - at η = 0, R_2 is the native readout, so Theorem 3η's hypothesis on I_δ is unit 2's
    hypothesis "I_δ for the two-outcome readout from level 2 into level L";
  - Theorem 4η's hypotheses are C_δ[max(m, 2), Λ₁(n, m)] and δ(N(m+1) + 1) < 1, exactly unit
    2's.

  **Green.**
- **CC.** At δ = 0, with T_triv's η_e(2) ≥ 1 and every other η_r = 0: β ≥ 2d ≥ 2 and D ≥ 4, so
  ε_c ≥ (1+β)^D − 1 ≥ 80. Hence ε₁ ≥ 80, and ½((1+ε₁)^K − 1) ≥ 40 ≥ 1/2. **Green.** As
  `PLAN.md` states, this tests only that η_e is not dropped.

### 4.4 Q1-H

M_H ≤ M_C [U2] gives Theorem 4η's bound under M_H, so the status is B1. The sub-question, whether
some η_r can be removed under M_H, is **open**. Every coverage route found here passes through an
available family with J's outcome set and horizon, and the only rules producing such a family
from the δ-forms are those of Theorem 3η. This is a description of the routes found, not a proof
that none other exists.

### 4.5 Pressure test (favourable branch)

1. *Hidden exact inputs.*
   - The conditional flips and the identities are binds with U_δ pieces.
   - The seed identity is exact for the exact layers, and the approximate layers enter only
     through err_D.
   - The census (§2) lists every rule use. None is missed: Theorem 3's text was checked line by
     line.
2. *Uniformity.* Each η_r is used at finitely many instances, at the levels listed. Lemma B needs
   the pieces' norms, which are at most 1 + β.
3. *The dimension factor 2d* comes from N3. It is an upper bound; whether it is necessary is open
   (O2-b). Under the relaxation (e′), Lemma E adds min(d, 2) ≤ 2.
4. *Scope.* Theorem 4η transfers precision within the given kinematics. It does not show that
   any mechanism supplies the δ-forms or the η-rules (O5).

***

## 5. Direction 2 (Q2)

Fix a level n (or the system), with m ≥ 2, K ≥ 2 and T in class(η). Let τ_min be T's
padding-defect floor at that level (§3), with ω_j = (1+τ_min)^j − 1. Set

ω′ := 2ω_{K−1} + ω_{K−2}.

M_C(T, Q) < ε gives correspondences c, c′ whose soundness and coverage terms are at most ε. For a
chosen c′, let g := sup_E ‖c′(M_E)‖ over projectors E, where M_E = {E, 1 − E}. g belongs to the
chosen correspondence, not to T, and may be infinite.

### 5.1 Steps B and D do not depend on η

Unit 2's step B pads the quantum side with P and the T side with c′(P), compared through the
quantum soundness partner c(c′(P)) [U2]. No T-side trace preservation is used. Hence
‖Γ′_E − E‖ ≤ 2ε, where Γ′_E is the effect of c(G_E) and G_E = c′(M_E).

Step D likewise uses no D_T. So for every quantum instrument J and G = c′(J),
‖J − c(G)‖ ≤ 24ε [U2].

### 5.2 Lemma 7η

**Hypothesis (Hg)** on the correspondence: either ω′ = 0 and ε ≤ 1/48; or g < ∞ and
μ := 6ε + ω′g ≤ 1/8.

**Lemma 7η [A].** Let c, c′ be correspondences with terms at most ε that satisfy (Hg), and let
μ := 6ε + ω′g (μ := 6ε when ω′ = 0). Then:
- ‖F − c(F)‖ ≤ 64ε + 16μ for every available F with at most m outcomes;
- ‖c′(J) − J‖ ≤ κ := 88ε + 16μ for every quantum instrument J with at most m outcomes.

*Proof.* The supremum in M_C runs over all protocols for fixed c and c′, so each protocol below
may use its own padding. Let D′ be any available single-outcome family, with
‖D′ − D‖_{1→1} ≤ τ for some completely positive, trace-preserving D, and write ω_j(τ) for
(1+τ)^j − 1.

A′. *Step A, for G_E.*
- The T-protocol (G_E, D′^{K−1}) and its partner (c(G_E), c(D′)^{K−1}) are within ε in TV. The
  partner's padding is a quantum channel, so its law is tr c(G_E)_b(σ).
- Lemma P gives |tr D′^{K−1}(G_E)_b σ − tr (G_E)_b σ| ≤ ω_{K−1}(τ)‖(G_E)_b σ‖₁. Summed over b
  this is at most ω_{K−1}(τ)‖G_E‖.
- So |tr((Γ_E − Γ′_E)σ)| ≤ 2ε + ω_{K−1}(τ)‖G_E‖.
- The left side and ‖G_E‖ do not depend on D′, and τ can be taken arbitrarily close to τ_min.
  Since ω is continuous, |tr((Γ_E − Γ′_E)σ)| ≤ 2ε + ω_{K−1}‖G_E‖.
- N5 (factor 2) gives ‖Γ_E − Γ′_E‖ ≤ 4ε + 2ω_{K−1}g. With §5.1, ‖Γ_E − E‖ ≤ γ := 6ε + 2ω_{K−1}g.

C′. *Step C.*
- Fix a density ρ, an available F and projectors E_a. Let Y_a = (F_a − c(F)_a)ρ,
  D_ρ = Σ_a ‖Y_a‖₁ and S = Σ_a ‖F_a ρ‖₁ ≤ 1 + D_ρ.
- The protocol "F, then G_{E_a}, then D′^{K−2}" and its partner give
  Σ_a |tr D′^{K−2}(G_{E_a})_1 F_a ρ − tr(Γ′_{E_a} c(F)_a ρ)| ≤ 2ε.
- Lemma P with ‖(G_{E_a})_1 F_a ρ‖₁ ≤ g‖F_a ρ‖₁ replaces the first term by tr(Γ_{E_a} F_a ρ), at
  a cost of at most ω_{K−2}(τ) g S. The same limit in τ applies.
- Then Σ_a |tr(E_a Y_a)| ≤ (2ε + ω_{K−2} g S) + γ S + 2ε = 4ε + μS ≤ 4ε + μ(1 + D_ρ).
- Choosing each E_a to attain N5 (factor 4) gives D_ρ ≤ 16ε + 4μ + 4μD_ρ. With 4μ ≤ 1/2,
  D_ρ ≤ 32ε + 8μ. The four-part split gives ‖F − c(F)‖ ≤ 64ε + 16μ.

D′. *Step D.* By §5.1 and C′ applied to G = c′(J),
‖c′(J) − J‖ ≤ 24ε + 64ε + 16μ = 88ε + 16μ. □

**Corollary 7c (padding rules in closure) [A].** If τ_min = 0 at the level, then for every pair
of correspondences with terms at most ε ≤ 1/48: ‖F − c(F)‖ ≤ 160ε and ‖c′(J) − J‖ ≤ 184ε. No
hypothesis on g is needed. This is unit 2's Lemma 7 verbatim.

*Proof.* The norms that multiply ω(τ) in steps A′ and C′ are finite for each fixed pair (F, ρ):
- ‖G_E‖ for the test families G_{E_a} actually used, which are finitely many linear maps on a
  finite-dimensional space, because the projectors E_a depend only on Y_a;
- S, which is at most ‖F‖.

The left sides do not depend on the padding, and τ can be taken arbitrarily close to 0. So the
padding terms vanish:
- step A′ gives ‖Γ_E − E‖ ≤ 6ε;
- step C′ gives Σ_a |tr(E_a Y_a)| ≤ 10ε + 6εD_ρ, which is unit 2's inequality, so
  D_ρ ≤ 40ε/(1 − 24ε) ≤ 80ε;
- step D′ is unchanged. □

**A posteriori norm.** Applying C′ to F = G_E gives g ≤ 1 + 64ε + 16μ. When ω′ < 1/16, this
gives g ≤ (1 + 160ε)/(1 − 16ω′). This improves a finite g; it does not establish one.

**Sufficient conditions for (Hg).** Conditions (i) and (ii) make (Hg) hold for every
correspondence c′ with terms at most ε.
- (i) An a priori bound ν on the norms of the available two-outcome families at the level, with
  ω′ν ≤ 1/8 − 6ε.
- (ii) V_{δ0} at the level for the two-outcome families, with 2(1 + 5δ0)ω′ ≤ 1/8 − 6ε (Lemma V).
- (iii) τ_min = 0 at the level. Then no hypothesis on g is needed (Corollary 7c).

**Convergence.**
- κ = 88ε + 16(6ε + ω′g) tends to 0 as (ε, η) → 0 exactly when ω′g → 0.
- Under (Hg) alone, the lemma gives only κ ≤ 88ε + 2.
- Under (i) with a fixed ν, or (ii) with a fixed δ0: ω′ ≤ ω′(τ(n)) → 0 as η_e(n) + η_b(n) → 0,
  so κ → 0 (branch B1 on that hypothesis).
- If the correspondence, and hence g = g_ε, depends on ε, convergence needs ω′g_ε → 0 jointly.
  That is a condition of type B2.
- Under (iii), κ = 184ε.

### 5.3 The obstruction (B4), and its scope

**Scope.**
- The obstruction concerns bounds on Lemma 7 and Theorem 8 that are uniform over class(η) at a
  fixed η > 0. Such a bound must cover every theory in that class, including any with
  τ_min > 0.
- For a single theory it applies only where the theory's own padding defect has a positive floor
  τ_min(T) at a level, and ω′(τ_min)·g is not small for the available correspondences.
- Where τ_min = 0, Corollary 7c removes it.

**Step.** Lemma 7, step A for the test families G_E, and step C's padding.

**What fails.**
- With exact padding, the T-side law of a horizon-K protocol is linear in the effects of its
  first steps and does not depend on the size of their outputs.
- With a padding-defect floor τ_min > 0, every padding has trace defect at least τ_min. The law
  then differs from that value by up to ω_j times the trace norm of the output of the family
  before the padding.
- The hypotheses of Lemma 7 (M_C < ε, m, K ≥ 2, class(η)) give no a priori bound on that norm.
  No δ-form, in particular V, is assumed in Direction 2.

**The gap in the bootstrap.**
- The self-consistent inequality g ≤ 1 + 64ε + 16(6ε + ω′g) is derived only on the branch where
  μ(g) ≤ 1/8, that is g ≤ (1/8 − 6ε)/ω′.
- It excludes neither g = ∞ nor g > (1/8 − 6ε)/ω′. Since ω′ ≈ (3K − 4)τ_min, the latter is about
  1/(8(3K − 4)τ_min) for small τ_min and ε, and 1/(16τ_min) at K = 2.

**What would close it:**
- an a priori norm bound on available families with at most two outcomes, derived from M_C and
  the η-rules;
- or a theory in class(η), with m, K ≥ 2, M_C < ε and τ_min > 0, whose test families have norm of
  order 1/τ_min and for which the conclusion of Lemma 7 fails as (ε, η) → 0. That would be
  branch B3.

Neither is obtained here. This is an obstruction to the argument, not a disproof of the statement
(`PLAN.md` §4). The obstruction is exactly W2's third clause: the exact trace preservation of the
coarse-grained readout.

### 5.4 Theorem 8η

**Theorem 8η [A].** Let m ≥ 2, K ≥ 2 and T in class(η). Assume M_C(T, Q) < ε, and let c, c′ be
correspondences with terms at most ε that satisfy (Hg) at every level of a set Λ containing each
level the δ-forms reference. Let κ_Λ = max over Λ of 88ε + 16μ(level), and let N_Λ be as in
Theorem 8. Then, for families with at most m outcomes, T satisfies:
- V_{κ_Λ} and U_{κ_Λ};
- I_{(N_Λ+1)κ_Λ};
- C_{2κ_Λ} and L_{2κ_Λ}.

Hence C_{(N_Λ+1)κ_Λ}[m, Λ] holds. If τ_min = 0 at every level of Λ, then κ_Λ = 184ε and
δ(ε) = 184(N_Λ+1)ε, as in unit 2's Theorem 8, with no hypothesis on g.

*Proof.* Unit 2's proof [U2], with Lemma 7η or Corollary 7c in place of Lemma 7. Theorem 8 uses
the structure rules only through Lemma 7 (§2). □

For a finite Λ, (N_Λ+1)κ_Λ tends to 0 under the convergence condition of §5.2 at each level of Λ.
m ≥ 2, K ≥ 2 and the level-set condition remain necessary in every η-class, by Proposition 11
and Proposition 9 (C1). They are sufficient under (Hg), and where τ_min = 0.

### 5.5 Controls for Direction 2

- **C0.** At η = 0:
  - τ_min = 0 and ω′ = 0, and (Hg) reads ε ≤ 1/48;
  - μ = 6ε;
  - 64ε + 16μ = 160ε, and κ = 88ε + 96ε = 184ε;
  - Theorem 8η gives V_{184ε}, U_{184ε}, I_{184(N_Λ+1)ε}, C_{368ε} and L_{368ε}, with
    δ(ε) = 184(N_Λ+1)ε.

  These are unit 2's expressions and hypotheses. **Green.**
- **C1.** No Q2 verdict here drops m, K ≥ 2 or the level set. **Green.**

### 5.6 Pressure test

**Of Corollary 7c (favourable).** Four points were checked:
1. *The quantifier order.* The correspondences are fixed before the supremum over protocols
   (unit 2 `PLAN.md` §2), so a padding chosen for each protocol is admissible. The partner's
   padding c(D′) is a quantum channel whatever D′ is.
2. *What the projectors depend on.* The projectors E_a depend on Y_a, not on the padding.
3. *Finiteness.* The norms ‖G_{E_a}‖ and S are finite for fixed (F, ρ). The bound on D_ρ, and
   hence on ‖F − c(F)‖, does not depend on them.
4. *Lemma P.* It allows the trace-preserving reference map D to vary with D′.

No step fails.

**Of §5.3 (unfavourable to the stability claim).**
- *Is the obstruction an artifact of the proof?* Possibly. Other test families might have
  controlled norm. The families whose norms the η-rules control directly (R_n, D′ and their binds
  and coarse-grainings) give effects 1 ⊗ P_k only, not arbitrary projectors. Families giving
  arbitrary projectors need unitary families, whose norms are not controlled without V. So the
  obstruction is stated for the argument only.
- Corollary 7c shows that the obstruction is absent whenever the paddings come arbitrarily close
  to trace preservation.

***

## 6. Q3 (secondary): the analogue of Corollary 10

Say T satisfies the rules **in closure** if every η_r-rule holds for every η_r > 0 at every level.
Let m ≥ 2, K ≥ 2, and let Λ be all levels and the system.

- **(a) ⇒ (b) [A].** If T satisfies the rules in closure and C_δ[max(m, 2)] for every δ > 0, then
  M_C(T, Q) = 0 at every level and on the system. Theorem 4η applies at each level, and its bound
  tends to 0 as δ and every η_r tend to 0.
- **(b) ⇒ (a) [A].** If T satisfies the rules in closure and M_C(T, Q) = 0 at every level and on
  the system, then C_δ[m] holds for every δ > 0.
  - The rules in closure give τ_min = 0 at every level and on the system (§3).
  - Theorem 8η then holds in its verbatim form (κ = 184ε), and Corollary 10's instance-by-instance
    argument [U2] applies unchanged, with ε ≤ min(1/48, δ/(184(N_i+1))).

The two directions are separate statements with separate proofs (§A.34).

***

## 7. Controls: summary

| Control | Status |
| --- | --- |
| C0 (η = 0 reproduction) | green: Theorems 3η and 4η (§4.3), Lemma 7η, Corollary 7c and Theorem 8η (§5.5) |
| C1 (transfer of unit 2's counterexamples) | green (§1.3), relative to [U2] |
| CC (T_triv) | verified (§1.5); bound check green (§4.3) |

All verdicts above are printed over green controls.

## 8. Inputs and labels

| Input | Label | Use |
| --- | --- | --- |
| `FiniteOperationalTheory` and its fields (OB/OperationalAssembly.lean:594); `readout_is_localLuders` (:658) | [K] | Model; (M1) |
| `avail_of_availExt_one` (OB/LevelOneSeam.lean:107); `discardWith_uniform_one_eq_transport` (OB/LevelOneSeam.lean:98) | [K] | System coverage (§4.1) |
| `IsFiniteEndomorphicKrausInstrument` (OB/KrausSoundness.lean:112) | [K] definition | (M3) |
| Main:572 | [P] | The six rules, the five conditions, the given kinematics |
| Unit 2: Theorems 2–5 and 8, Lemma 7, Propositions 1, 9 and 11, Corollary 10, N1–N5, the proofs of steps B and D, and the definition of M_C (quantifier order) | [U2] | Unchanged steps, C0, C1, Corollary 7c |
| Lemmas E, B, P and V; the padding-defect floor; Theorems 3η and 4η; Lemma 7η; Corollary 7c; Theorem 8η; §5.3; §6 | [A] | This unit's results |
| Schmidt and singular value decompositions, Cauchy–Schwarz | [L] | Lemma E |
| Independent review of r1, PR #1596 comment 7189898722 | review record | Provenance for r2. The argument of Corollary 7c (quantifier order, finite norms for fixed F and ρ, a padding chosen for each protocol) originates in its finding F1. The proof written here, and its extension to the floor τ_min in Lemma 7η, are this unit's own. |
| Owner decisions (#1169 comment 7189139613); synthesis (#1169 comment 7189143747); PR #1584 reviews | provenance | No claim uses their content |

§A.42 item 8: every [U2] input is on `main` (commit `b1037933`, an ancestor of the pin). No
support lies off `main`.

## 9. Productivity verdict and classification

**Verdict: gem**, provisional until the delta review (`PLAN.md` §7):
- **G3:** the obstruction of §5.3, identified precisely: its step, the failing estimate, the
  bootstrap's excluded branch and what would close it. Its scope is bounds uniform over class(η)
  at fixed η > 0, and theories with a positive padding-defect floor.
- **G1:** Lemma 7η, Corollary 7c and Theorem 8η. Their proofs need the bootstrap and the limit
  argument of §5.2, which go beyond S, because unit 2 has no estimate of the norms involved.
- **Q1 (Theorem 4η):** the writer's assessment is that this is S, which is record-only. Its
  coefficients come from N3 and from Lemma B's recursion. The reviewer decides.

**Classification (§A.31):**
- §5.3 and Lemma 7η: **NEW**. In the converse under M_C, the exact trace preservation of the
  padding supplies an a priori norm control that no hypothesis states. It is needed only when the
  padding defect has a positive floor.
- Corollary 7c: **ELABORATING**. Its argument originates in the review (§8).
- Theorem 4η: **CONFIRMING**. Direction 1 is norm-continuous in the structure rules, and soundness
  does not depend on η.
- Lemma E and the CC verification: **ELABORATING**.
- §6: **ELABORATING**.

**Assumption-watch marker W4 (norm control).** Any argument that compares horizon-K laws through
steps that are only approximately trace preserving needs an a priori bound on the trace norm of
the outputs that precede those steps, or a padding whose defect can be made small after those
outputs are fixed. This applies to every approximate-operational statement in #1216 that pads or
composes with approximately trace-preserving steps.

## 10. Open nodes

| ID | Node | Status |
| --- | --- | --- |
| O2-a | Lemma 7η and Theorem 8η uniform over class(η) at fixed η > 0, or for a theory with τ_min > 0: an a priori norm bound, or a counterexample (§5.3) | open |
| O2-b | Whether the factor 2d on η_e(2) in Theorem 4η is necessary | open |
| O2-c | Q1-H sub-question: whether an η_r can be removed under M_H | open |
| O2-d | Q3, (b) ⇒ (a) | closed for theories satisfying the rules in closure (§6) |
| O2-e | A lower bound on the η-dependence of Theorem 4η at small η (G4) | open; CC gives one only at η_e ≥ 1 |

The open nodes of unit 2 other than O2 are unchanged.

## 11. Stopping rule

Each question has reached a status:
- Q1-C and Q1-H: B1.
- Q2-L7 and Q2-T8: B4 for bounds uniform over class(η) at fixed η > 0. They are proved verbatim
  where τ_min = 0, and with conditional bounds under (Hg).
- Q2-H: disproved, by C1.

The stop is by status (`PLAN.md` §8).

## 12. Points for the delta review

1. Corollary 7c and the τ_min form of Lemma 7η: the quantifier order of M_C, and the limit in τ
   in steps A′ and C′.
2. §5.2, convergence: the B1 and B2 cases.
3. §5.3: the scope and the constant 1/(8(3K − 4)τ_min).
4. §6, (b) ⇒ (a): that the rules in closure give τ_min = 0 at every level and on the system.
5. Whether Q1 is the baseline S (record-only), and whether Lemma 7η and Corollary 7c go beyond S.
