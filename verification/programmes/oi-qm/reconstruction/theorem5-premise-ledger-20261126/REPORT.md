# T5-LEDGER-1: the premise ledger of SM Theorem 5 (unit A; #1049, #1217). Report

**WIP / UNVERIFIED. Model-written research record, paper-only. Nothing here is adopted, proposed
for the manuscripts or authorized beyond the unit's scope.**
- Every new step is labelled [A] (exact hand algebra here, unreviewed) or [W] (reasoning here,
  unreviewed). Other labels are as in PLAN.md §1.
- No computation, enumeration or Lean build was run. No manuscript, ledger, census or registry was
  edited. No premise was adopted, weakened or changed.
- Names introduced below for conditions a step needs (SMD; the readings r1/r2, Φ-kin/Φ-dyn;
  R-res) are classification labels. They are not premise proposals.

- **Plan:** PLAN.md in this directory, commit `c6cb9170b38b99067ed3dea4f8fcd188a4d68179`, committed
  alone before this report. Questions, conventions, decision rule, controls, productivity test and
  stopping rule are those of PLAN.md.
- **Authorization and Goal link:** as in PLAN.md (owner decision quoted in #1169 comment
  7189139613; account amaybaum; comment created 2026-11-26T10:16:17Z; decision stated as received
  2026-11-26T10:16Z). Goal link: #1049 and #1217, as stated in PLAN.md.
- **Pinned main commit [P]:** `353a066f18766837fed8c7f58507e09ff549b1a4`. Line conventions as in
  PLAN.md §0. All quoted lines were re-read at [P] from git objects.
- **Evidence layer of every result below:** mathematical derivation on paper. The lane 1 and lane 2
  inputs are reviewed paper derivations, not independently verified theorems.

## 0. Summary

1. **Theorem 5's statement (layer M) is supported by stated premises and exact algebra.** The
   statement is the stabilizer in U(6) of an O-equivariant Σ with distinct block values. It uses:
   - H-link with m = 1 (S), whose ⊗ℂ supplies an abstract complex structure;
   - O-equivariance of Σ (S);
   - distinct values (S);
   - the decomposition 6 = T_1 + E + A_1 ([K]);
   - Schur's lemma and the stabilizer computation ([A]).
   No symmetry of any dynamics is used, and the kinetic clause of H-cust is not consumed.
2. **The proof's physical sentences (layer Φ) need more.**
   - **P1** (SM:342, first sentence) is a derived condition only when U(6) acts through the real
     lift's positive-frequency complex structure J_F (Lemma 1). Through any site-local complex
     structure it fails (Lemma 1′).
   - **P2** ("the unbroken subgroup of a state with condensate Σ is its unitary stabilizer") splits
     into five steps. One holds unconditionally (P2a needs H-PF; P2e is derived). The other three
     fail under every ambient-symmetry reading unless a state condition is added:
     - stationarity under the same scalar linear map, giving J-Hermiticity (Counterexample 10);
     - the two-point condensate clause, needed under the on-site reading of SM:374
       (Counterexample 9);
     - SMD: the state's symmetry is fixed by its second moment. This is new: Proposition A gives a
       state meeting every stated premise and every lane 2 condition that defeats the step.
3. **No ergodic state on T realizes the conclusion (Proposition B, new).** On the torus, no state
   that is ergodic, or extremal, under the update and translations has a U(6)-stabilizer
   containing U(3)×U(2)×U(1) with distinct block values. On T the conclusion can therefore be
   realized only by mixtures, and mixtures are exactly what Proposition A exploits.
4. **Q2 (R-kin versus R-dyn).**
   - On the class fixed by PLAN.md §3, R-kin implies R-dyn at the observer level (Proposition D),
     given SM:312's linear update (b = 0). R-dyn has no content at the substratum level.
   - So control CC7 finds no dynamics in the stated class that meets R-kin and not R-dyn. Per
     PLAN.md §5, Q2 is reported as **vacuous for the stated class**, and the §6 verdict sentences
     are not printed (§4).
   - In plain terms: on the stated branch the full dynamical symmetry is not an extra premise; it
     follows from the kinetic symmetry.
   - Outside the stated class (an offset reaching the lift, or a component-local nonlinear term at
     observer level), the kinetic symmetry does not secure the residual-symmetry step P2e.
     Supplementary analysis, §4.3.
5. **Q3.**
   - **H-PF is independent of the stated premises.** Witness: the complexified real field.
   - **The two-point clause** is independent of the stated premises under reading r1 of SM:374
     (witness: Counterexample 9). Under reading r2, SM:374 states it.
   - Neither is derived.
6. **Correctness bands unchanged.** This is consistency-axis work (§A.23).

## 1. Setting and notation

**Carrier and update.** These are the branch premises (PLAN.md §3(iii)).
- Observer-level real field φ(n, t) ∈ R^6 (SM:312) on carrier T = (Z/L)^d, or Z = Z^d (lane 2 §3).
  Results below are stated for T unless Z is named.
- At M = μI_6 the real lift is F = F_s ⊗ I_6 on pairs x = (u, v), with
  F_s(u, v) = (v, A_s v − u) and A_s = (μ/d) Σ_j (T_j + T_j⁻¹).
- In lane 2's notation αμ = μ/d, so abs(αμ) < 1/d iff abs(μ) < 1. μ = 1 is the massless point
  (SM:322, SM:328).

**Complex structure.** For abs(μ) < 1 on T, J_s = D_s(−D_s²)^(−1/2) with D_s = F_s − A_s/2. This
is the unique complex structure commuting with F_s and tamed by ω ([L2] Theorem 1). Then
J_F = J_s ⊗ I_6. At μ = 1 it exists on V_rest (T), or as a closed operator (Z; bounded on K under
H-top) ([L2] Propositions 3, 6).

**The internal unitary action.** For w = X + iY ∈ U(6), with X and Y real,
R(w) = I ⊗ X + J_s ⊗ Y.

**J-linear field.** Φ_n(x) = ℓ_n(x) − i ℓ_n(J_F x), where ℓ_n reads u_n.
- C is the phase-space second moment, and C_− = (C − J C Jᵀ)/2 its J-anti-invariant part.
- Σ_n = E[Φ_n Φ_n†] is the on-site condensate.

**Layers.** As in PLAN.md §2: **M**, the mathematical stabilizer statement; **Φ**, the physical
reading.

**Readings of an ambient symmetry.** As in PLAN.md §2 Q2: R-coup, R-kin, R-kin-st, R-dyn. One more
label is used:
- **R-res:** Stab_{U(6)}(Σ) is contained in the symmetry group of the full dynamics. This is
  weaker than R-dyn.

**Readings of steps found while tracing (PLAN.md §3):**
- **r1 / r2 of SM:374.** Reading r1: "does not introduce extra copy-mixing custodial structure"
  concerns mixing across H-link's m copies (SM:362), and is vacuous at m = 1; "scalar on each of
  these isotypic blocks" is read on-site, as SM:136 states the condensate clause. Reading r2:
  "scalar on each isotypic block" applies to the full two-point function, which is TPC.
- **Φ-kin / Φ-dyn of "unbroken subgroup" (SM:342).** Φ-kin: the stabilizer within the kinetic
  symmetry group set up in P1. Φ-dyn: the residual symmetry group of the full dynamics.

## 2. Q1: the premise ledger

Classes: S (stated assumption), Dv (derived condition), U (unsupported step), per PLAN.md §2. Items
marked † were found while tracing; they refine seed items P2 and H4.

| Id | Item | Layer | Class | Location / derivation | Carries |
| --- | --- | --- | --- | --- | --- |
| H1 | H-link, m = 1 | M, Φ | S | SM:340; SM:360–364 | — |
| H2 | H-cust kinetic clause | Φ (not consumed by M) | S | SM:340; SM:374 | — |
| H2a | H2 supplied at M = μI_6 | Φ | Dv | Proposition 4b, SM:334–336 ([P] proof). Hypotheses: identical independent component rule, counting measure, component-complete site observer; H-blind for extensions | the hypotheses listed |
| H3 | Σ O-equivariant (on-site) | M, Φ | S | SM:340; SM:136; SM:374 | — |
| H4a† | φ is the J_F-linear field Φ (H-PF) | Φ | U | Not stated: SM:312 makes φ a real field; SM:362 gives an abstract ⊗ℂ; SM:505 says "equipped after-the-fact"; SM:809 names the real-to-complex step as open. Independent of the stated premises (§5) | — |
| H4b† | The law ⟨·⟩: which state, invariant under what (L-SDS) | Φ | U | Not stated at SM:340. SM:136 calls Σ "a hypothesis on the solution". By Proposition C the state is not the selected measure's observer image | — |
| H5 | Distinct block values | M, Φ | S | SM:340. By Proposition C, incompatible with taking the state to be Proposition 4b's selected-measure image | — |
| H6-M | A complex structure and Hermitian form on the carrier, with O acting unitarily | M | S | H-link's V_link ⊗ ℂ (SM:362) | — |
| H6-Φ | The same, acting on the observer phase space and commuting with the update | Φ | Dv | J_F: existence and uniqueness [L2] Theorems 1, 1Z; no site-local alternative (Lemma 1′; [L2] Proposition 2) | LIN, LIFT (S: SM:312–316, with SM:232 recording the bridge as unproved); abs(μ) < 1, or at μ = 1 V_rest / K: **H-ZM / H-top (unit C)** |
| P1 | Kinetic term invariant under the custodial unitary action (SM:342) | Φ | Dv with U(6) via J_F; U via H6-M alone | Lemma 1 | as H6-Φ |
| P2a† | Stab(state) ⊆ Stab(Σ_n) | Φ | Dv given H4a | §2.3 | H-PF |
| P2b† | C J-Hermitian (C_− = 0), so that Stab(C) can contain non-orthogonal unitaries | Φ | U as stated; Dv given L-SDS | Proposition 7 ([L2]; re-derived, CC3). Counterexample 10 defeats it without L-SDS (CC2) | L-SDS |
| P2c† | Stab(C) = Stab(Σ_n) | Φ | U under r1; Dv under r2 | TPC with CC3's argument. Counterexample 9 defeats it under r1 (CC1) | TPC |
| P2d† | Stab(state) = Stab(C) | Φ | U; Dv given SMD | Proposition A defeats it with every stated premise and L-SDS, TPC and H-PF held | SMD |
| P2e† | The stabilizer is a symmetry group of the full dynamics (Φ-dyn); vacuous under Φ-kin | Φ | Dv | Proposition D (observer level, SM:312 linear, b = 0) | LIN, b = 0 (S: SM:312) |
| P3 | 6 = T_1 + E + A_1, multiplicity-free and irreducible over ℂ | M | Dv | [K] `theorem_7` (projector identities, ranks 3, 2, 1, over ℚ); `finrank_commutant` = 3 over ℚ (`OIBridge.lean`:448). Base change to ℂ gives a commutant of complex dimension 3, so three pairwise inequivalent absolutely irreducible blocks [A] | — |
| P4 | Schur: Σ = aP_T1 + bP_E + cP_A1 with real a, b, c | M | Dv | H3 + P3 + Hermiticity [A] | — |
| P5 | a, b, c distinct give Stab = U(3)×U(2)×U(1) | M | Dv | A unitary commuting with Σ preserves its eigenspaces, and conversely [A]. If two values coincide the stabilizer grows, e.g. U(5)×U(1) (CC5) | H5 |
| L-HPF | as H4a | Φ | U | §5 | — |
| L-SDS | as H4b, stationarity part | Φ | U | — | — |
| L-TPC | full two-point clause | Φ | S under r2; U under r1 | SM:374; §5 | — |
| SMD† | the state's U(6)-stabilizer is that of its second moment (e.g. a centred Gaussian state) | Φ | U | Proposition A; on T it cannot be replaced by extremality (Proposition B) | — |
| L-NZM | non-zero-mode condensate at μ = 1 | Φ | U | [L2] Proposition 11; **depends on H-ZM (unit C)** | H-ZM |

### 2.1 Lemma 1 (P1 with J_F) [A]

At M = μI_6, abs(μ) < 1 on T: for every w ∈ U(6), R(w) commutes with F and J_F, and preserves ω and
E. The map w ↦ R(w) is a group homomorphism.

*Proof.*
- **Homomorphism.** R(w)R(w′) = I⊗(XX′ − YY′) + J_s⊗(XY′ + YX′) = R(ww′), using J_s² = −1.
- **Commutation.** F_s commutes with J_s, so R(w) commutes with F = F_s ⊗ I.
- **ω is preserved.**
  - With Ω = Ω_s ⊗ I, R(w)ᵀΩR(w) = Ω⊗(XᵀX + YᵀY) + ΩJ_s⊗(XᵀY − YᵀX).
  - Here J_sᵀΩ_sJ_s = Ω_s and J_sᵀΩ_s = −Ω_sJ_s were used.
  - w†w = I gives XᵀX + YᵀY = I and XᵀY − YᵀX = 0.
- **E is preserved.** E(x, y) = ω(Dx, y) with D = D_s ⊗ I commuting with R(w), because J_s is a
  function of D_s.
- The same holds on V_rest at μ = 1 (T), and on the domain of J_F on Z ([L2] Theorem 1Z).
∎

**Lemma 1′ [A].** With the site-local J_0(u, v) = (−v, u), the phase R_0(i) = J_0 ⊗ I does not
commute with F for α ≠ 0.
- J_0F_s(u, v) = (u − A_s v, v) and F_sJ_0(u, v) = (u, A_s u + v).
- These agree for all (u, v) only if A_s = 0.
- So P1 holds through J_F and fails through a site-local complex structure; [L2] Proposition 2 is
  the general form.

### 2.2 Layer M [A]

P3, P4 and P5 together with H1, H3, H5 and H6-M give Theorem 5's statement for any Hermitian
O-equivariant Σ on V_link ⊗ ℂ. That includes a real symmetric Σ, such as E[uuᵀ]. Nothing about a
dynamics enters.

**Real-carrier control (CC4).** In O(6), a real block-scalar Σ with distinct values has stabilizer
O(3)×O(2)×O(1), of dimension 4 against 14. So H6-M is load-bearing.

### 2.3 P2a [A]

Φ_n(R(w)x) = wΦ_n(x):
- ℓ_n(R(w)x) = Xℓ_n(x) + Yℓ_n(J_F x);
- ℓ_n(J_F R(w)x) = Xℓ_n(J_F x) − Yℓ_n(x).

So R(w) maps the law's Σ_n to wΣ_n w†, and Stab(state) ⊆ Stab(C) ⊆ Stab(Σ_n).

For φ = u (H-PF failing), R(w) mixes u with the v-dependent J_F x. Then E[uuᵀ] is not covariant
under R(w), and the inclusion has no content.

### 2.4 Proposition A (SMD is needed; new) [A]

**Carrier T, abs(μ) < 1, or states on V_rest.** Let C_0 = Σ_b κ_b G⁻¹ ⊗ P_b with κ_b pairwise
distinct, and let W = Σ_{g∈O} g(Π_{k_0}G⁻¹ ⊗ Q)g⁻¹ be the ε-term of Counterexample 9 (CC1). The
state ρ is the equal mixture of the centred Gaussians with covariances C_0 + εW and C_0 − εW,
0 < ε < min κ_b.

**ρ meets every stated premise, together with L-SDS, TPC and H-PF:**
- each component is positive (CC1);
- each component is F-stationary, translation-invariant and cubic-invariant;
- the second moment is exactly C_0, so TPC holds in J-Hermitian form, and r2 of SM:374 is met;
- Σ_n = 2γ Σ_b κ_b P_b is O-equivariant with distinct values;
- φ = Φ.

**Its U(6)-stabilizer is strictly smaller than U(3)×U(2)×U(1).**
- A symmetry R(w) of ρ preserves C_0, so w ∈ U(3)×U(2)×U(1) (CC3).
- It also preserves the fourth cumulant of every linear functional. For a mixture of
  N(0, σ² + a) and N(0, σ² − a), m_4 = 3σ⁴ + 3a², so κ_4(ℓ(X)) = 3ε²(ℓWℓᵀ)².
- Hence q(ℓ)² = q′(ℓ)² for the quadratic forms of W and of R(w)WR(w)ᵀ. R[ℓ] is an integral
  domain, so (q − q′)(q + q′) = 0 gives q′ = ±q, and R(w)WR(w)ᵀ = ±W.
- For w_φ = e^{iφP_T1}: on the k_0 subspace, only g = id contributes (k_0 generic, as in CC1), so
  the J-complex internal block of W is Q.
- w_φ Q w_φ† = e^{iφ}|t⟩⟨e| + e^{−iφ}|e⟩⟨t|, which equals ±Q only if e^{iφ} = ±1.
- So the T_1 phase circle is not in the stabilizer's identity component. (w_π swaps the two
  components and does lie in the stabilizer.)

**Therefore Stab(ρ) ⊊ Stab(C_0) = Stab(Σ_n).** Step P2d fails with every stated premise held,
under every reading of §1. The dynamics is the fully U(6)-symmetric linear lift, so even R-dyn
holds.
∎

Z is not claimed.

### 2.5 Proposition B (extremal states on T; new) [A]

**Carrier T, abs(μ) < 1, or laws supported on V_rest.** Let ρ be ergodic for the group generated
by F and the translations, or extremal among the laws invariant under F, translations and O. Then
the identity component of Stab_{U(6)}(ρ) contains U(3)×U(2)×U(1) only if the T_1 and E blocks of
Σ_n vanish. In that case the block values are not distinct.

*Proof.*
- **Setup.** F is an isometry for the J_F metric. Write V = ⊕_j E_j, where E_j ≅ S_j ⊗ ℂ^6 are the
  complex spectral subspaces on which F acts as e^{iθ_j}, θ_j ∈ (0, π). U(6) acts as I ⊗ w on
  each.
- **Support.** An ergodic law of this equicontinuous action is Haar measure on an orbit closure,
  which lies in ∏_j S¹x_j. A symmetry maps the support to itself, so (I⊗w)x_j ∈ S¹x_j for every j.
- **SU(3) step.** For w ∈ SU(3), embedded in the T_1 block, (I⊗w)x_j = e^{iψ(w)}x_j defines a
  continuous character of SU(3), which is trivial. Then x_j ∈ S_j ⊗ (E ⊕ A_1), because SU(3) fixes
  no nonzero vector of ℂ³.
- **SU(2) step.** The same argument with SU(2) on E gives x_j ∈ S_j ⊗ A_1.
- **Hence** the T_1 and E components vanish ρ-almost surely.
- **The O-extremal case.** The support is a finite union of distinct such tori. A connected group
  of symmetries maps each torus to itself, because the tori form a finite, Hausdorff-discrete
  family. The same argument then applies.
∎

**Consequence.**
- On T, P2's conclusion with distinct values can hold only for a non-extremal (mixture) state.
- Requiring a "pure phase" therefore does not exclude Proposition A without also excluding the
  conclusion itself.
- On Z, spatial clustering is available, and a route from clustering plus stationarity to
  Gaussianity is open (§9, O3).

### 2.6 Proposition C (the selected-measure state is custodially scalar; elaborating) [A]

Under Proposition 4b's hypotheses (§3(ii)), the following are invariant under the hyperoctahedral
group B_6 of signed permutations of the components:
- the counting measure;
- the component-complete site observer's σ-algebra;
- hence the observer-level law (SM:336).

B_6 acts by real matrices commuting with J_F. Its six-dimensional representation is irreducible
over R with a one-dimensional commutant (SM:336), hence absolutely irreducible. So Σ_n = c·I_6, and
H5 fails.

The condensate state of Theorem 5 is therefore not the observer image of the selected measure. Its
selection lies outside the stated premises, in agreement with SM:136 ("a hypothesis on the
solution") and SM:493 ("removed spontaneously").

### 2.7 Proposition D (R-kin implies R-dyn on the stated class) [A]

On the class of PLAN.md §3, the observer-level update is the linear map of SM:312–314 with b = 0
(SM:312: "general second-order linear update"). At M = μI_6, abs(μ) < 1, this map is F itself.
By Lemma 1, every R(w) is a symmetry of the full observer-level dynamics. So R-kin, with U(6) taken
through J_F, implies R-dyn at the observer level, and P2e holds.

The same holds for any custodially scalar linear observer-level map, including the
memory-resummed response d(ω, k)I_6 of Proposition 4b, with U(6) taken through that map's own
complex structure. It does not hold across two different maps (Counterexample 10).

At the substratum level no U(6) acts on the Z/q alphabet ([L1] §2.7). SM:493's "substratum
dynamics is locally U(6) invariant" therefore has no content there, and the proof does not use it.

**Outside §3(iii)** (supplementary; §4.3):
- **Offset reaching the lift (b_A1 ≠ 0).**
  - Off resonance (abs(μ) < 1), the fixed point x* = (I − F)⁻¹β exists, and τ_{x*}R(w)τ_{−x*} is a
    symmetry of x ↦ Fx + β. This is lane 1's class (b); [L1] and owner Q2 read the shift as a
    relabelling.
  - At resonance on T (μ = 1), no stationary law exists ([L2] Proposition 4(b)). Without a
    stationarity requirement, the symmetries of x ↦ Fx + β that are linear about 0 are the w fixing
    e_A1: dimension 25, so 11 generators are lost, including the A_1 phase. This agrees with
    [L1-Q4].
- **Component-local nonlinearity.** Take F_λ(u, v) = (v, A v − u + λN(v)), with N acting
  component-wise as an odd cubic. This is an illustrative surrogate of SM:130's and SM:338's
  "component-local" nonlinearity; it is not the framework's derived dynamics.
  - F_λ is symplectic and meets R-kin.
  - For x = (u, 0) with N(u) ≠ 0, and s = (1 − A_s²/4)^(−1/2): F_λ(R(i)x) − R(i)F_λ(x) = (0, −λs³N(u)).
  - The global phase R(i) is not a symmetry, so R-dyn fails. Since the global phase lies in
    U(3)×U(2)×U(1), R-res fails too.

## 3. Controls

| Control | Result | Status |
| --- | --- | --- |
| CC1 | Counterexample 9 re-derived [A] in its stated range: (a) positivity on each image subspace (min κ_b − ε); (b) F-stationarity (G⁻¹ and Π_{k_0} commute with F; O commutes with F at M = μI); (c) J-Hermiticity; (d) translation and cubic invariance; (e) the ε-term's on-site part vanishes, since the O-average of an intertwiner T_1 → E is zero by Schur; (f) w_φ fails to stabilize C (§2.4). It defeats P2c under r1 and meets §3 under r1. It violates r2. The Z case also needs the bump-support condition (PRESERVATION.md §2) | green |
| CC2 | Counterexample 10 re-derived [A]. With Φ = u − i(v − cu)/s and C = κ′[[1, c′], [c′, 1]], which F′-stationarity checks (F′CF′ᵀ = C): S = E[Φ²] = 2κ′(c′ − c)e^{−iθ}/s². In a block C = C_1 ⊗ I_n with C_− ≠ 0: R(w)C_−R(w)ᵀ = C_−⊗(XXᵀ − YYᵀ) + J C_−⊗(YXᵀ + XYᵀ), while R(w)C_+R(w)ᵀ = C_+ ⊗ I. Linear independence of C_− and JC_− forces Y = 0. Stabilizer: O(n), and O(3)×O(2)×O(1) over the blocks. It defeats P2b. It meets §3, since bare F is custodially scalar and stationarity under F is not stated | green |
| CC3 | (a) Proposition 7 re-derived [A]: S(x, y) = E[Φ(x)Φ(y)] is F-invariant; on E_j × E_k it picks up e^{i(θ_j+θ_k)} ≠ 1, so S = 0, i.e. C_− = 0 on V_rest. (b) With TPC and C_− = 0: a w commuting with C commutes with the compression ⟨ψ|C|ψ⟩ = Σ_b c_b P_b, where ψ has distinct c_b (it exists off three proper real quadrics). So w ∈ U(3)×U(2)×U(1), and conversely. Second-moment stabilizer: exactly U(3)×U(2)×U(1). The state stabilizer is the same for a centred Gaussian (with SMD) | green |
| CC4 | H6-M and H6-Φ carried; real stabilizer has dimension 4 against 14 (§2.2) | green |
| CC5 | H5 carried; coincident values enlarge the stabilizer | green |
| CC6 | P3 classified Dv at [K] | green |
| CC7 | Within §3's class (i)–(iii), no dynamics meets R-kin and not R-dyn at the observer level (Proposition D), and R-dyn is not meaningful at the substratum level. The plan's named examples (threshold-type nonlinearity, offset) meet R-kin and not R-dyn, but violate SM:312's linear, b = 0 form, i.e. §3(iii) | negative within §3: per PLAN.md §5, Q2 is reported vacuous for the stated class (§4) |
| CC8 | Itemized checks below | green |
| CC9 | All quoted lines re-read at [P] | green |

**CC8 witness checks** (✓ meets, ✗ fails):

| Witness | (i) SM:340 | (ii) SM:362, SM:374 r1 / r2, SM:334–338, SM:136 | (iii) SM:232, SM:312–316 | R-kin | R-kin-st | R-dyn (obs.) |
| --- | --- | --- | --- | --- | --- | --- |
| CE9 | ✓ | ✓ / ✗ | ✓ | ✓ | ✓ | ✓ |
| CE10 | ✓ | ✓ / ✓ (real-form TPC) | ✓ | ✓ | ✗ (dressed map not scalar) | ✓ |
| Prop. A mixture | ✓ | ✓ / ✓ | ✓ | ✓ | ✓ | ✓ |
| Complexified real field (Q3) | ✓ | ✓ / ✓ | ✓ | ✓ | ✓ | ✓ |
| F_λ | ✓ | ✓ | ✗ (nonlinear) | ✓ | ✓ (state stationary under F) | ✗ |
| Resonant offset | ✓ | ✓ | ✗ (b ≠ 0) | ✓ | no stationary state | ✗ |

For every witness, the Proposition 4b clause of (ii) constrains the dynamics, measure and observer.
None of these states is the selected measure's image, and by Proposition C no state meeting H5 can
be.

## 4. Q2: ambient symmetry per item

### 4.1 Table

| Id | Q2 entry |
| --- | --- |
| H1, H3, H5, H6-M, P3, P4, P5 | none (no ambient symmetry used) |
| H2, H2a | H2 is the source of R-kin; H2a entails B_6-symmetry of the substratum rule and nothing about U(6) at rule level |
| H6-Φ | R-kin's object: J_F is defined by F |
| P1 | R-kin (it is R-kin, derived from H2 with J_F; Lemma 1) |
| P2a | none |
| P2b | proved under R-kin-st (CC3(a), U(6) through the stationary map's own J). Counterexample under R-kin and under R-dyn (CE10) |
| P2c | fails under every reading under r1 (CE9 meets R-kin-st and R-dyn); none under r2 |
| P2d | fails under every reading (Proposition A); none given SMD |
| P2e | R-kin, with SM:312 linearity (Proposition D); vacuous under Φ-kin |

### 4.2 Decision rule

CC7 is negative within the class PLAN.md §3 fixes. Per PLAN.md §5 ("Without one, the R-kin/R-dyn
distinction is vacuous for the class, and Q2 is reported as vacuous rather than decided"), the
verdict sentences of PLAN.md §6 are not printed.

The table states what holds on that class:
- R-dyn at the observer level follows from R-kin (Proposition D).
- No item is proved only under R-dyn.
- The items not proved under R-kin (P2b, P2c under r1, P2d) fail equally under R-dyn. Their
  missing content is a state condition (L-SDS, TPC, SMD), not an ambient symmetry.

### 4.3 Supplementary: the class extended beyond §3(iii) (outside the decision rule)

Extend the class by letting the observer-level dynamics carry an offset or a component-local
nonlinear term. Under Φ-dyn, P2e then:
- has a counterexample under R-kin and under R-kin-st (F_λ, an illustrative surrogate);
- holds under R-dyn, and already under the weaker R-res.

At resonance with b_A1 ≠ 0, R-res fails for the A_1 phase, but no stationary state exists on T.
Whether the observer-level interactions of SM:338 and SM:493 satisfy R-res is the interacting
question H-PF-int ([L2] §4.6), open.

## 5. Q3

- **TPC.**
  - Under r1: **independent of the stated premises.** Witness: Counterexample 9 (CC1, CC8). It
    meets SM:340, SM:136, SM:374 r1 and the branch, is F-stationary, translation- and
    cubic-invariant, and violates TPC.
  - Under r2: SM:374 states TPC, so it follows trivially. Nothing derives it.
- **H-PF.** **Independent of the stated premises.**
  - Witness: the centred Gaussian with covariance C_0 (§2.4), with φ taken as the complexified real
    field u ⊗ 1. Then Σ = E[uuᵀ] is O-equivariant and block-scalar with distinct values, and H-link
    and the branch hold. φ is not J_F-linear.
  - In the search scope (PLAN.md §4):
    - SM:362 gives an abstract ⊗ℂ;
    - SM:505 says "equipped after-the-fact";
    - SM:809 names the real-to-complex step as open;
    - Sub:288 says S carries no complex structure;
    - SM:509 and Main §3 give QM kinematics with no explicit formal map to J_F.
  - No source states or derives H-PF.
- **Neither target is derived from stated premises.** The negative findings are
  independence results, by witness. They are not "not found" outcomes.

## 6. Readings and restatements

- **Layer M restatements, consistent with the ledger:** Sub:163, Sub:189, Sub:193, SM:474, SM:575
  (Theorem 14 uses the stabilizer's abelian directions), and ch05:120 with its identical mirror at
  FULL:1435–1439 ("exact at those stated premises").
- **Layer Φ readings:**
  - SM:114: the "surviving global stabilizer" carried to local gauge invariance.
  - SM:130: "custodial U(6) of the real lift … broken by the threshold only down to this
    signed-permutation group". On §3's class the threshold acts at the substratum level, where no
    U(6) acts. At observer level it corresponds to §4.3's extended class.
  - SM:493: "The substratum dynamics is locally U(6) invariant … removed spontaneously … Higgs
    mechanism". This uses a spontaneous-breaking reading that Theorem 5's proof does not consume.
- **SM:344:** "exact conditional on H-link + H-cust" holds for layer M. For layer Φ, SM:342's P2
  sentence also needs H-PF, L-SDS, TPC (under r1) and SMD.

## 7. Consequences (PLAN.md §6)

**For #1049.**
- On the stated branch, Theorem 5's proof consumes no symmetry beyond R-kin plus SM:312's
  linearity (Proposition D). Lane 1's D3/D16 dependence on b = 0 under R-dyn is therefore not a
  dependence of the proof.
- That dependence arises only where the offset reaches the observer-level update. This is lane 1's
  SM:232 condition, which also leaves SM:312's linear form. There:
  - off resonance, the static shift restores the action about x* (class (b));
  - at resonance on T, with stationarity required, no condensate state exists ([L2] Proposition
    4(b));
  - at resonance without stationarity, the A_1 phase is lost, matching lane 1's (c) placement.
- Conditional on Q4c, H-b and SM:232, as in lane 1. The owner reading of Q4b is not decided.

**For #1217.**
- Layer M needs only H-link's abstract ⊗ℂ.
- Layer Φ rests on several premises, not one:
  - H-PF (independent of the stated premises);
  - L-SDS (not stated);
  - TPC (stated under r2, independent under r1);
  - SMD (found; not stated; on T not replaceable by extremality);
  - at μ = 1, H-ZM or H-top and L-NZM (unit C).
- None is derived from stated premises.

## 8. Productivity verdict (PLAN.md §7)

**The test is met, pending independent review:**
- **G1:** Proposition D proves that R-kin suffices on the stated branch for the step lane 1 left
  Q4b-dependent (P2e, the D3/D16 Σ-route step). It does so by deriving R-dyn from R-kin and
  SM:312's linearity.
- **G4:** Proposition A gives a state meeting every stated premise, and lane 2's conditions, that
  defeats P2d. It goes beyond the reproduction of Counterexamples 9 and 10.
- G2 is met only through items that also fail under R-dyn.
- G3 is not met.

**Pressure tests.**
- **G1 is favourable to the framework.** It holds only on the linear observer-level branch.
  - SM:338 and SM:493 place interactions at observer level, outside §3(iii). F_λ shows that a
    component-local term removes even the global phase.
  - G1 also depends on taking U(6) through J_F (Lemma 1′).
  - It is recorded with that scope.
- **Proposition A is unfavourable.** It was tested against a pure-phase requirement. Proposition B
  shows that on T such a requirement excludes the conclusion itself.

**Classification of findings (§A.31):**

| Class | Findings |
| --- | --- |
| NEW | Proposition A (SMD); Proposition B; the split of P2 into P2a–P2e with per-step conditions |
| POSITIVE | Proposition D; Lemma 1 |
| ELABORATING | Proposition C; the r1/r2 variance of SM:374 against SM:136; Q3 independence of H-PF and of TPC under r1 |
| CONFIRMING | CC1–CC3 |

## 9. Open nodes

- **O1 (unit C).** H-ZM / H-top at μ = 1 for H6-Φ, P1 and L-NZM. Not pursued here.
- **O2.** Whether any premise states L-SDS or SMD. Within scope, none does.
- **O3.** On Z: whether spatial clustering plus stationarity under the linear F implies SMD (a
  literature route on Gaussianity of invariant states of free lattice dynamics; not checked).
  Propositions A and B are not claimed on Z.
- **O4.** The interacting case: R-res for the observer-level interactions (H-PF-int).
- **O5.** The owner reading of SM:374 (r1 or r2) and of "unbroken subgroup" (Φ-kin or Φ-dyn).

## 10. Findings for routing (listed, not edited)

1. **SM:342 / SM:344.** P2 holds as the inclusion Stab(state) ⊆ Stab(Σ), given H-PF. Equality
   needs L-SDS, TPC (r1) and SMD. "Exact conditional on H-link + H-cust" is accurate for the
   statement only. Route: #1217.
2. **Lane 2 REPORT-r2 §4.7 / §6 item 3.** The stabilizer conclusion holds for the two-point
   function. For the state it also needs SMD. A mutable record citing it (PRESERVATION.md) would
   carry this. Route: #1217.
3. **SM:493.** Theorem 5's proof uses no U(6) symmetry of the substratum dynamics. Also,
   "(Theorem 5, revised)" is revision-history voice (§A.33). Route: #1029, beside lane 1's variance
   item.
4. **Section pointers.** SM:613 cites "(§4.3)" and SM:130 cites "(Theorem 5, §4.6)"; Theorem 5 is
   at SM:340 in §4.4. Route: #1029.
5. **SM:136 / SM:340 against SM:374.** The condensate clause is stated on-site at SM:136 and
   SM:340, and admits the two-point reading r2 at SM:374. Route: #1217.

## 11. Off-`main` references (§A.42 item 8)

| Reference | Classification |
| --- | --- |
| commit `c6cb9170` (PLAN.md) | support on `main` once merged: the preregistration order. Not before |
| PR #1595 | provenance |
| #1169 comments 7189139613, 7189143747 | provenance (authority record; synthesis) |
| lane 1 and lane 2 records, `A5-Q4-STAGE2D.md`, PRESERVATION.md | support on `main` at [P]. Their pin `b6c6b80b` is an ancestor; line carry-over per PLAN.md §0 |
| kernel modules (`LinkDecomposition`, `OIBridge`, `A6Instantiation`) | support on `main`; statements read, not built |

Support off `main`: none.

## 12. Verification status and remediation (§A.46 item 4)

This plan authorizes no work.

| Claim | Status | Missing | Issue | What would resolve it |
| --- | --- | --- | --- | --- |
| Lemma 1, 1′; §2.2–2.3 | hand derivation, unreviewed | independent review | #1217 | recorded review |
| Proposition A | unreviewed | review; exact finite control on a small torus (authorization needed) | #1217 | review; authorized control |
| Proposition B | unreviewed; the ergodic-measure step uses the standard structure of equicontinuous systems | review | #1217 | review |
| Propositions C, D; §4.3 | unreviewed; F_λ is illustrative | review | #1049, #1217 | review |
| CC1–CC3 re-derivations | unreviewed; inherit [L2]'s model reviews | independent non-model verification | #1217 | as lane 2 |
| Search (PLAN.md §4) | passages bearing on Theorem 5 read in full; others identified by their opening sentences | full reading of every passage | #1217 | recorded full reading |

## 13. Node log

- **Pass 1.** Seed classification. P3–P5 and layer M.
- **Pass 2.** Split of P2; CC1–CC3; Proposition A.
- **Pass 3.** Skepticism on Proposition A (extremality): Proposition B.
- **Pass 4.** CC7; Proposition D; offset and F_λ; Proposition C.
- **Pass 5.** Q3 sweep and restatements. No NEW finding.
- **Pass 6.** §A.34 re-check:
  - CC3's "iff" (both inclusions given);
  - P5's "iff distinct" (the stabilizer, and its enlargement on coincidence);
  - Proposition B is one-directional (necessity only).
  No NEW finding.

Every ledger item is classified, and each Q3 target has an outcome. The stopping rule is met.
