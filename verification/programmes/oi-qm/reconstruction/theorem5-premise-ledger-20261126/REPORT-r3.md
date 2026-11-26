# T5-LEDGER-1: the premise ledger of SM Theorem 5 (unit A; #1049, #1217). Report, revision r3

**Revision r3.** Applies corrections D1 and D2 of the delta review of r2 (PR #1595 comment
7190237418), as the owner directed (#1169 comment 7190274734). Optional nits D3 and D4 are not
applied, and nothing else differs from REPORT-r2.md, which is kept unchanged.

**WIP / UNVERIFIED. Model-written research record, paper-only. Nothing here is adopted, proposed
for the manuscripts or authorized beyond the unit's scope.**

**Revision r2.**
- This revision applies findings F1–F13 of the independent review of r1. The review was of
  REPORT.md at `8f1ee17d`, posted verbatim on PR #1595.
- REPORT.md (r1) is kept unchanged and is superseded. CHANGES-r2.md maps each change to its
  finding.
- r2 is pending a focused delta review.

**Method and labels.**
- Every new step is labelled [A] (exact hand algebra here, unreviewed) or [W] (reasoning here,
  unreviewed). Other labels are as in PLAN.md §1.
- No computation, enumeration or Lean build was run. No manuscript, ledger, census or registry was
  edited. No premise was adopted, weakened or changed.
- Names introduced for conditions a step needs are classification labels, not premise proposals:
  SMD; the readings r1 and r2; Φ-kin and Φ-dyn; R-res.

- **Plan:** PLAN.md in this directory, commit `c6cb9170b38b99067ed3dea4f8fcd188a4d68179`, committed
  alone before any report.
- **Authorization and Goal link:** as in PLAN.md (owner decision quoted in #1169 comment
  7189139613; account amaybaum; comment created 2026-11-26T10:16:17Z; decision stated as received
  2026-11-26T10:16Z). Goal link: #1049 and #1217.
- **Pinned main commit [P]:** `353a066f18766837fed8c7f58507e09ff549b1a4`. Lines are cited as in
  PLAN.md §0, and all quoted lines were re-read at [P].
- **Evidence layer of every result:** mathematical derivation on paper. The lane 1 and lane 2
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
   - **P1** (SM:342, first sentence) is a derived condition when U(6) acts on the real phase space
     through the real lift's positive-frequency complex structure J_F (Lemma 1).
     - P1 fails through the site-local J_0 (Lemma 1′).
     - By [L2] Proposition 2, no site-local complex structure that is tamed, or cubic-equivariant,
       commutes with the update.
     - P1 holds trivially on the doubled complexification of the phase space, which is not an
       action on SM:312's real field.
   - **P2** ("the unbroken subgroup of a state with condensate Σ is its unitary stabilizer") splits
     into five steps.
     - P2a holds given H-PF.
     - P2e is derived on the linear branch with b = 0.
     - P2b, P2c and P2d each need a condition on the state:
       - P2b needs stationarity under the same scalar linear map, which gives J-Hermiticity. This
         is built into R-kin-st, so R-kin-st is a state condition and not only a symmetry reading
         (Counterexample 10).
       - P2c needs the two-point condensate clause, under the on-site reading of SM:374
         (Counterexample 9).
       - P2d needs SMD: the state's symmetry is fixed by its second moment. This is new.
         Proposition A gives a state that meets every stated premise and every lane 2 condition
         and still defeats the step. It is constructed on T, with abs(μ) < 1 or V_rest, and
         L ≥ 7.
     - P2c and P2d fail under every ambient-symmetry reading. P2b is proved only under R-kin-st,
       because it needs stationarity.
3. **No extremal state on T realizes the conclusion (Proposition B, new).** On T, with abs(μ) < 1
   or V_rest, no state that is ergodic for the update and translations, or extremal with O
   included, has a U(6)-stabilizer containing U(3)×U(2)×U(1) with distinct block values.
4. **Q2 (R-kin versus R-dyn).**
   - On the class PLAN.md §3 fixes, R-kin implies R-dyn at the observer level (Proposition D),
     given SM:312's offset-free linear update. Under the R-dyn reading, R-dyn has no content at the
     Z/q level.
   - Control CC7 therefore fails in PLAN.md §8's sense. Per PLAN.md §5, Q2 is reported as vacuous
     for the stated class, and no §6 verdict sentence is printed (§4).
   - In plain terms, on the stated branch the full dynamical symmetry follows from the kinetic
     symmetry, so the stated class cannot discriminate between the readings.
   - Outside the stated class (an offset reaching the lift, or a component-local nonlinear term at
     observer level), the kinetic symmetry does not secure the residual-symmetry step P2e. This is
     supplementary (§4.3).
5. **Q3.**
   - H-PF is independent of the stated premises. The witness is the complexified real field.
   - The two-point clause is independent of the stated premises under reading r1 of SM:374 (witness:
     Counterexample 9). Under reading r2, SM:374 states it.
   - Neither is derived.
6. **Correctness bands unchanged.** This is consistency-axis work (§A.23).

## 1. Setting and notation

**Carrier and update** (branch premises, PLAN.md §3(iii)).
- The observer-level real field is φ(n, t) ∈ R^6 (SM:312), on carrier T = (Z/L)^d or Z = Z^d.
- At M = μI_6 the real lift is F = F_s ⊗ I_6, with F_s(u, v) = (v, A_s v − u) and
  A_s = (μ/d) Σ_j (T_j + T_j⁻¹).
- abs(αμ) < 1/d is equivalent to abs(μ) < 1. μ = 1 is the massless point (SM:322, SM:328).

**Complex structure and unitary action.**
- For abs(μ) < 1 on T: J_s = D_s(−D_s²)^(−1/2), with D_s = F_s − A_s/2. Write
  s_L = (1 − A_s²/4)^(1/2), so that (−D_s²)^(−1/2) = s_L⁻¹. J_F = J_s ⊗ I_6 is unique ([L2]
  Theorem 1).
- At μ = 1, J_F exists on V_rest (T), or as a closed operator (Z; bounded on K under H-top) ([L2]
  Propositions 3 and 6). It does not exist on the null sector V_0 (T).
- For w = X + iY ∈ U(6): R(w) = I ⊗ X + J_s ⊗ Y.

**Field and moments.**
- The J-linear field is Φ_n(x) = ℓ_n(x) − iℓ_n(J_F x).
- C is the second moment and C_− = (C − JCJᵀ)/2. The on-site condensate is Σ_n = E[Φ_n Φ_n†].

**Layers.** M is the mathematical stabilizer statement; Φ is the physical reading.

**Readings.**
- R-coup, R-kin, R-kin-st and R-dyn are as in PLAN.md §2 Q2. R-kin-st includes stationarity of the
  state under the map whose kinetic symmetry is taken, so it is partly a state condition. The
  readings are not nested: CE10 meets R-dyn but not R-kin-st.
- **R-res:** Stab_{U(6)}(Σ) lies in the symmetry group of the full dynamics. This is weaker than
  R-dyn.
- **r1 / r2 of SM:374.** In r1, "copy-mixing" refers to H-link's m copies (SM:362) and is vacuous
  at m = 1, and "scalar on each of these isotypic blocks" is read on-site, as SM:136 states the
  condensate clause. In r2, "scalar on each isotypic block" applies to the full two-point function,
  which is TPC.
- **Φ-kin / Φ-dyn** of "unbroken subgroup" (SM:342). Φ-kin takes the stabilizer within the kinetic
  symmetry group of P1. Φ-dyn takes the residual symmetry group of the full dynamics.

## 2. Q1: the premise ledger

Classes S, Dv and U are as in PLAN.md §2. Items marked † were found while tracing.

"Not stated" below means not stated in the §4 primary scope, which was read in full (§12), and not
stated in any record hit of the supplementary sweep that was read. The sweep is described in §12.

| Id | Item | Layer | Class | Location / derivation | Carries |
| --- | --- | --- | --- | --- | --- |
| H1 | H-link, m = 1 | M, Φ | S | SM:340; SM:360–364 | — |
| H2 | H-cust kinetic clause | Φ (not consumed by M) | S | SM:340; SM:374 | — |
| H2a | H2 supplied at M = μI_6 | Φ | Dv | Proposition 4b, SM:334–336 ([P] proof), with its hypotheses | those hypotheses |
| H3 | Σ O-equivariant (on-site) | M, Φ | S | SM:340; SM:136; SM:374 | — |
| H4a† | φ is the J_F-linear field Φ (H-PF) | Φ | U (not stated; independent of the stated premises, §5) | SM:312 (real field); SM:222 ("a real/complex wave operator is an observer-level lift whose derivation must be stated separately"); SM:362 (abstract ⊗ℂ); SM:505 ("equipped after-the-fact"); SM:809 (real-to-complex step open) | — |
| H4b† | The law ⟨·⟩ and its invariance (L-SDS) | Φ | U (not stated) | Not stated at SM:340. SM:136: "a hypothesis on the solution". SM:290: "the stationary law and Gaussian limit of the realized scalar dynamics" is open. SM:298: "Whether one realized map supports both the structural chain and the required stationary law remains open". The state is not the selected measure's image (Proposition C) | — |
| H5 | Distinct block values | M, Φ | S | SM:340. Incompatible with the selected-measure image (Proposition C) | — |
| H6-M | Complex structure and Hermitian form on the carrier, with O unitary | M | S | SM:362 together with U(6) in SM:340 | — |
| H6-Φ | The same, acting on the real phase space and commuting with the update | Φ | Dv | J_F: [L2] Theorems 1 and 1Z. Not site-local if tamed, or if cubic-equivariant ([L2] Proposition 2; Lemma 1′) | LIN, LIFT (S: SM:312–316; SM:232 records the bridge as unproved); abs(μ) < 1, or at μ = 1 V_rest / K: **H-ZM / H-top (unit C)** |
| P1 | Kinetic term invariant under the custodial unitary action (SM:342) | Φ | Dv with U(6) via J_F (Lemma 1). Trivially Dv on the doubled complexification (u, v) ⊗ ℂ, with w acting as I ⊗ w; this is not an action on SM:312's real phase space. Not supplied by H6-M as an action on the real phase space | Lemma 1 | as H6-Φ |
| P2a† | Stab(state) ⊆ Stab(Σ_n) | Φ | Dv given H4a | §2.3 | H-PF |
| P2b† | C J-Hermitian (C_− = 0) | Φ | U as stated; Dv given L-SDS | Proposition 7 ([L2], re-derived in CC3). CE10 defeats it without L-SDS | L-SDS |
| P2c† | Stab(C) = Stab(Σ_n) | Φ | U under r1; Dv under r2 | TPC with CC3. CE9 defeats it under r1 | TPC |
| P2d† | Stab(state) = Stab(C) | Φ | U; Dv given SMD | Proposition A defeats it on T (abs(μ) < 1 or V_rest; L ≥ 7) with every stated premise and L-SDS, TPC and H-PF held | SMD |
| P2e† | The stabilizer is a symmetry group of the full dynamics (Φ-dyn; vacuous under Φ-kin) | Φ | Dv | Proposition D | LIN, b = 0 (S: SM:312) |
| P3 | 6 = T_1 + E + A_1, irreducible and pairwise inequivalent over ℂ | M | Dv | [K] `theorem_7`; `finrank_commutant` = 3 over ℚ (`OIBridge.lean`:448); base change to ℂ [A] | — |
| P4 | Schur: Σ = aP_T1 + bP_E + cP_A1 with real a, b, c | M | Dv | [A] | — |
| P5 | a, b, c distinct give U(3)×U(2)×U(1) | M | Dv | [A]; coincidence enlarges it (CC5) | H5 |
| L-HPF | as H4a | Φ | U | §5 | — |
| L-SDS | as H4b | Φ | U | as H4b | — |
| L-TPC | full two-point clause | Φ | S under r2; U under r1 | SM:374; §5 | — |
| SMD† | U(6)-stabilizer of the state equals that of its second moment (e.g. a centred Gaussian state) | Φ | U (not stated; SM:290 records the Gaussian limit as open) | Proposition A; on T not replaceable by extremality (Proposition B) | — |
| L-NZM | non-zero-mode condensate at μ = 1 | Φ | U | [L2] Proposition 11; **depends on H-ZM (unit C)** | H-ZM |

### 2.1 Lemma 1 (P1 with J_F) [A]

At M = μI_6, abs(μ) < 1 on T: for every w ∈ U(6), R(w) commutes with F and J_F and preserves ω
and E, and w ↦ R(w) is a homomorphism.

*Proof.*
- R(w)R(w′) = I⊗(XX′ − YY′) + J_s⊗(XY′ + YX′) = R(ww′).
- F_s commutes with J_s.
- With Ω = Ω_s ⊗ I: R(w)ᵀΩR(w) = Ω⊗(XᵀX + YᵀY) + ΩJ_s⊗(XᵀY − YᵀX), using J_sᵀΩ_sJ_s = Ω_s and
  J_sᵀΩ_s = −Ω_sJ_s. Unitarity w†w = I gives XᵀX + YᵀY = I and XᵀY − YᵀX = 0.
- E(x, y) = ω(Dx, y), and D = D_s ⊗ I commutes with R(w).
- The same holds on V_rest at μ = 1 (T), and on the domain of J_F on Z.
∎

**Lemma 1′ [A].** With J_0(u, v) = (−v, u):
- J_0F_s(u, v) = (u − A_s v, v) and F_sJ_0(u, v) = (u, A_s u + v);
- they agree for all (u, v) only if A_s = 0.

**Scope of the site-local statement.**
- Lemma 1′ treats J_0 only.
- [L2] Proposition 2 shows that site-local complex structures commuting with F are exactly
  diag(P, P) ⊗ 1, with P² = −1 on R^6. These are not tamed and not cubic-equivariant.
- So no site-local, tamed, F-commuting structure exists, and no site-local, cubic-equivariant,
  F-commuting structure exists, for α ≠ 0.

### 2.2 Layer M [A]

P3, P4 and P5, with H1, H3, H5 and H6-M, give Theorem 5's statement for any Hermitian
O-equivariant Σ on V_link ⊗ ℂ.

**CC4.** In O(6), a real block-scalar Σ with distinct values has stabilizer O(3)×O(2)×O(1), of
dimension 4 against 14.

### 2.3 P2a [A]

- Φ_n(R(w)x) = wΦ_n(x), because ℓ_n(R(w)x) = Xℓ_n(x) + Yℓ_n(J_F x) and
  ℓ_n(J_F R(w)x) = Xℓ_n(J_F x) − Yℓ_n(x).
- Hence Stab(state) ⊆ Stab(C) ⊆ Stab(Σ_n).
- For φ = u, R(w) mixes u with the v-dependent J_F x, and the inclusion has no content.

### 2.4 Proposition A (SMD is needed; new) [A]

**Carrier and range.** T, with abs(μ) < 1, or states on V_rest. L ≥ 7, so that a k_0 exists whose
coordinates have pairwise distinct absolute values, nonzero and not π (as for Counterexample 9).
Z is not claimed.

**Construction.**
- C_0 = Σ_b κ_b G⁻¹ ⊗ P_b, with κ_b pairwise distinct.
- W = Σ_{g∈O} g(Π_{k_0}G⁻¹ ⊗ Q)g⁻¹, Counterexample 9's ε-term (CC1).
- ρ is the equal mixture of the centred Gaussians with covariances C_0 ± εW, where
  0 < ε < min κ_b.

**ρ meets every stated premise, together with L-SDS, TPC (r2) and H-PF.**
- Each component is positive, F-stationary, translation-invariant and cubic-invariant.
- The second moment of ρ is exactly C_0.
- Σ_n = 2γ Σ_b κ_b P_b, with distinct values.
- φ = Φ.

**Its stabilizer.**
- A symmetry R(w) of ρ preserves C_0, so w ∈ U(3)×U(2)×U(1) (CC3).
- R(w) also preserves κ_4(ℓ(X)) = 3ε²(ℓWℓᵀ)², from m_4 = 3σ⁴ + 3a².
- R[ℓ] is an integral domain, so R(w)WR(w)ᵀ = ±W.
- On the k_0 subspace only g = id contributes, and w_φ = e^{iφP_T1} gives
  w_φQw_φ† = e^{iφ}|t⟩⟨e| + e^{−iφ}|e⟩⟨t|. This equals ±Q only if e^{iφ} = ±1.
- So the identity component of Stab(ρ) omits the T_1 phase circle, and
  Stab(ρ) ⊊ Stab(C_0) = Stab(Σ_n). (w_π swaps the two components and lies in Stab(ρ).)

The dynamics in the witness is the fully U(6)-symmetric linear lift, so P2d fails under every
reading.
∎

### 2.5 Proposition B (extremal states on T; new) [A]

**Carrier and range.** T, abs(μ) < 1, or laws supported on V_rest.

**Statement.** Let G be the abelian group generated by F and the translations, and let K be its
closure. Suppose ρ is G-ergodic, or extremal among laws invariant under G and O. If the identity
component of Stab_{U(6)}(ρ) contains U(3)×U(2)×U(1), then the T_1 and E blocks of Σ_n vanish, so
the block values are not distinct. The statement runs in this one direction only.

*Proof.*
- **Character spaces.**
  - F and the translations commute with J_F and act unitarily.
  - Decompose the J_F-complex space V into the joint character spaces
    E_χ = {x : F x = χ(F)x, T_j x = χ(T_j)x}.
  - Since A = A_s ⊗ I_6 and the translations act on the spatial factor, E_χ = S_χ ⊗ ℂ^6. Each E_χ
    is invariant under every R(w), and K acts on E_χ by the scalar χ.
- **Ergodic support.**
  - K is a compact abelian group of isometries. A G-ergodic law is K-invariant and concentrated
    on one K-orbit, because orbits of a compact group form a standard partition.
  - It is then the invariant law on that orbit. So supp ρ = Kx ⊆ ∏_χ S¹x_χ.
- **Line condition.**
  - R(w) commutes with K, so R(w)(Kx) = K(R(w)x). Preserving the support forces R(w)x ∈ Kx, i.e.
    R(w)x_χ ∈ S¹x_χ for every χ.
  - For w ∈ SU(3), in the T_1 block, this defines a continuous character of SU(3), which is trivial.
    So x_χ ∈ S_χ ⊗ (E ⊕ A_1).
  - The same argument with SU(2) on E gives x_χ ∈ S_χ ⊗ A_1.
  - Hence the T_1 and E components vanish ρ-almost surely.
- **The case including O.**
  - O normalizes G and is finite, so an extremal (G, O)-invariant law is supported on finitely
    many disjoint K-orbits, the O-images of one orbit.
  - R(w) commutes with K, so a symmetry R(w) permutes this finite set of orbits.
  - The identity component acts continuously on a finite set and therefore trivially. It contains
    SU(3) and SU(2), so each of these fixes every orbit, and the line condition applies as above.
∎

**Consequence.** On T, P2's conclusion with distinct values holds only for a non-extremal state.
So a pure-phase requirement cannot exclude Proposition A without excluding the conclusion itself.
On Z the question is open (§9, O3).

### 2.6 Proposition C (the selected-measure state is custodially scalar; elaborating) [A]

- Under Proposition 4b's hypotheses, the counting measure, the observer σ-algebra and hence the
  observer-level law are invariant under the signed permutations B_6 (SM:336).
- B_6 acts by real matrices commuting with J_F, and its six-dimensional representation is
  absolutely irreducible.
- So Σ_n = c·I_6, and H5 fails.
- The condensate state is therefore not the selected measure's observer image. Its selection lies
  outside the stated premises (SM:136, SM:493).

### 2.7 Proposition D (R-kin implies R-dyn on the stated class; borderline) [A]

**On the class of PLAN.md §3.**
- The observer-level update is SM:312–314's linear map with no offset. At M = μI_6, abs(μ) < 1, it
  is F.
- By Lemma 1, every R(w) is a symmetry of the full observer-level dynamics.
- So R-kin, through J_F, implies R-dyn at the observer level, and P2e holds.
- The result depends on SM:312's offset-free linear form, which is a stated branch premise.
- Under the R-dyn reading, SM:493's "substratum dynamics is locally U(6) invariant" has no content
  at the Z/q level, where no U(6) acts ([L1] §2.7). It may instead refer to the A6 covariance of
  Sub:102. The record `q3-a6-offsets-20261108/ASSESSMENT.md` finds no stated class for "site-wise
  U(6)".

**Outside §3(iii)** (supplementary; §4.3):
- **Offset reaching the lift (b_A1 ≠ 0).**
  - Off resonance (abs(μ) < 1), the fixed point x* = (I − F)⁻¹β exists, and τ_{x*}R(w)τ_{−x*} is a
    symmetry of x ↦ Fx + β. This is lane 1's class (b).
  - At resonance (μ = 1) on T, β lies in V_0, where J_F does not exist ([L2] Proposition 3). No
    stationary law exists ([L2] Proposition 4(b)).
  - For the internal action of the abstract ℂ^6 used in [L1-Q4] (H6-M), the w fixing e_A1 form a
    U(5). That loses 11 generators, including the A_1 phase. This count is [L1-Q4]'s and is
    conditional on it.
  - For R(w) through J_F the count is not defined on V_0.
- **Component-local nonlinearity.** Take F_λ(u, v) = (v, A v − u + λN(v)), with N acting
  component-wise as an odd cubic. This is an illustrative surrogate of SM:130's and SM:338's
  "component-local" nonlinearity, not the framework's derived dynamics.
  - F_λ meets R-kin.
  - For x = (u, 0): J_F x = (−A s_L⁻¹u/2, −s_L⁻¹u), and F_λ(R(i)x) − R(i)F_λ(x) = (0, −λN(s_L⁻¹u)).
  - This is nonzero for every u ≠ 0. So the global phase, which lies in U(3)×U(2)×U(1), is not a
    symmetry, and both R-dyn and R-res fail.

## 3. Controls

| Control | Result | Status |
| --- | --- | --- |
| CC1 | Counterexample 9 re-derived [A] within its range: positivity; F-stationarity; J-Hermiticity; translation and cubic invariance; vanishing on-site part of the ε-term (Schur); w_φ not a stabilizer. It defeats P2c under r1, meets §3 under r1 and violates r2. The Z case needs the bump-support condition of PRESERVATION.md §2 | green |
| CC2 | Counterexample 10 re-derived [A]: S = 2κ′(c′ − c)e^{−iθ}/s²; F′CF′ᵀ = C; the block computation forces Y = 0, giving O(n). It defeats P2b and meets §3 | green |
| CC3 | (a) Proposition 7 re-derived [A]: S(x, y) = E[Φ(x)Φ(y)] picks up e^{i(θ_j+θ_k)} ≠ 1, so C_− = 0 on V_rest. (b) With TPC and C_− = 0, compression at a ψ with distinct c_b gives Stab(C) = U(3)×U(2)×U(1). For a centred Gaussian state (SMD), the state stabilizer is the same | green |
| CC4 | H6-M and H6-Φ carried; dimension 4 against 14 | green |
| CC5 | H5 carried | green |
| CC6 | P3 is Dv at [K] | green |
| CC7 | Within the class (i)–(iii) of PLAN.md §3, no dynamics meets R-kin and not R-dyn at the observer level (Proposition D). Under the R-dyn reading there is no U(6) content at the Z/q level. The plan's examples (threshold-type nonlinearity, offset) violate §3(iii) | **failed in PLAN.md §8's sense.** Per PLAN.md §5 Q2 is reported vacuous. Writer's reading: the §8 halt applies to the Q2 verdict, which is not printed. Q1 and Q3 do not rest on CC7 and are reported |
| CC8 | Table below | green |
| CC9 | All quoted lines re-read at [P] | green |

**CC8 witness checks.** ✓ meets; ✗ fails. "q" means the kinetic and dynamical clauses of
Proposition 4b are met, while the state is not the selected-measure image; by Proposition C, no
state meeting H5 is.

| Witness | (i) SM:340 | (ii) SM:362; SM:374 r1 / r2; SM:334–338; SM:136 | (iii) SM:232, SM:312–316 | R-kin | R-kin-st | R-dyn (obs.) |
| --- | --- | --- | --- | --- | --- | --- |
| CE9 (T or Z, abs(μ) < 1 or V_rest) | ✓ | ✓; ✓ / ✗; q; ✓ | ✓ | ✓ | ✓ | ✓ |
| CE10 | ✓ | ✓; ✓ / ✓ (real-form TPC); q; ✓ | ✓ | ✓ | ✗ | ✓ |
| Proposition A (T, abs(μ) < 1 or V_rest, L ≥ 7) | ✓ | ✓; ✓ / ✓; q; ✓ | ✓ | ✓ | ✓ | ✓ |
| Complexified real field (Q3) | ✓ | ✓; ✓ / ✓; q; ✓ | ✓ | ✓ | ✓ | ✓ |
| F_λ | ✓ | ✓; —; q; ✓ | ✗ (nonlinear) | ✓ | ✓ (state stationary under F) | ✗ |
| Resonant offset | ✓ | ✓; —; q; ✓ | ✗ (b ≠ 0) | ✓ | no stationary state | ✗ (conditional on [L1-Q4]) |

## 4. Q2

### 4.1 Table

| Id | Q2 entry |
| --- | --- |
| H1, H3, H5, H6-M, P3–P5 | none |
| H2, H2a | H2 is the source of R-kin. H2a entails B_6-symmetry of the substratum rule only |
| H6-Φ | R-kin's object |
| P1 | R-kin (Lemma 1) |
| P2a | none |
| P2b | proved under R-kin-st, which includes the state condition L-SDS. Counterexample under R-kin and R-dyn (CE10) |
| P2c | fails under every reading under r1; none under r2 |
| P2d | fails under every reading on T (Proposition A; abs(μ) < 1 or V_rest; L ≥ 7); none given SMD |
| P2e | R-kin with SM:312's offset-free linearity (Proposition D); vacuous under Φ-kin |

### 4.2 Decision rule

CC7 failed: within the stated class, R-kin and R-dyn coincide at the observer level. Per PLAN.md
§5, Q2 is reported as vacuous for that class, and no verdict sentence of PLAN.md §6 is printed.

What the table shows on the stated class:
- No item is proved only under R-dyn.
- The items not proved under R-kin are P2b, P2c (under r1) and P2d. Their missing content is a
  state condition (L-SDS, TPC, SMD), and R-dyn supplies none of these.

### 4.3 Supplementary: the class extended beyond §3(iii) (outside the decision rule)

- With an offset or a component-local nonlinear term at observer level, P2e under Φ-dyn has a
  counterexample under R-kin and under R-kin-st (F_λ, illustrative). It holds under R-res, and so
  under R-dyn.
- At resonance with b_A1 ≠ 0, R-res fails for the A_1 phase, conditional on [L1-Q4]'s action, and
  no stationary state exists on T.
- Whether the observer-level interactions of SM:338 and SM:493 meet R-res is H-PF-int, which is
  open.

## 5. Q3

**TPC.**
- Under r1: independent of the stated premises. Witness: Counterexample 9 (CC1, CC8).
- Under r2: SM:374 states it, so it follows trivially. It is not derived.

**H-PF.** Independent of the stated premises. Witness: the centred Gaussian with covariance C_0,
with φ := u ⊗ 1. It meets §3 (CC8), and φ is not J_F-linear.

Sources examined. In the §4 primary scope, read in full, the following were examined and none
states or derives H-PF:
- SM:222 (the complex lift's derivation "must be stated separately");
- SM:362 (abstract ⊗ℂ);
- SM:505 ("equipped after-the-fact");
- SM:565 ("a real scalar bijection");
- SM:809 (real-to-complex step open);
- Sub:288 (S has "no complex structure");
- SM:22, SM:509 and Main §3 (QM kinematics, with no explicit formal map to J_F);
- the kernel statements (`A6Instantiation`: "`AddAut (Fin 6 → ℂ)`" types the carrier and does not
  introduce the inner product, unitarity, Σ or the stabilizer).

The supplementary sweep (§12) found one record that classifies the complex structure and the
condensate as non-native inputs: A1-11 `FORWARD-ALGEBRA.md`, rows "Complex Hilbert/unitary lift and
positive-frequency `J`" and "Equivariant `Σ` and distinct `a,b,c`". It found none that derives them.

The negative results of this section are independence results by witness against the fixed premise
set of §3. They do not depend on the extent of the search.

## 6. Readings and restatements

**Layer M restatements, consistent with the ledger:**
- Sub:163, Sub:189, Sub:193;
- SM:474, SM:575;
- ch05:120 and its identical mirror at FULL:1435–1439. Every substantive line of ch05 appears
  verbatim in FULL.

**Layer Φ readings:**
- SM:114: "the surviving global stabilizer" carried to local gauge invariance.
- ch05:102: "the unitary symmetry of the pre-condensate kinetic term is reduced by the state to the
  stabilizer" (Φ-kin).
- ch05:140: the stabilizer "acts at each site".
- SM:130: "custodial U(6) of the real lift … broken by the threshold only down to this
  signed-permutation group". On §3's class the threshold acts at the Z/q level.
- SM:136: "the framework's own gauge mechanism is spontaneous breaking of a dynamical symmetry by
  that condensate" (Φ-dyn).
- SM:493: "locally U(6) invariant … removed spontaneously … Higgs mechanism". Under the R-dyn
  reading this has no content at the Z/q level; it may refer to A6 covariance.
- SM:428: the stabilizer is "a literal algebraic structure on the lattice, existing before any
  trace-out is performed". At the bijection level, the complex structure this needs (H6-M) is
  supplied only after the fact: SM:505 equips the bijection-level carrier "after-the-fact with the
  complex inner-product structure V_K = ℂ^6". It is not native: Sub:288 says S has "no complex
  structure", and SM:565 calls the fundamental object "a real scalar bijection". Theorem 5's Σ is
  moreover an observer-level state datum, "a hypothesis on the solution" (SM:136), and not the image
  of the selected measure (Proposition C). SM:428's reading therefore needs both the added complex
  structure and a lattice-level Σ.

**SM:344.** "Exact conditional on H-link + H-cust" holds for layer M. For layer Φ, SM:342's P2
sentence also needs:
- H-PF;
- L-SDS;
- TPC under r1;
- SMD, which on T is required by Proposition A (abs(μ) < 1 or V_rest; L ≥ 7).

## 7. Consequences (PLAN.md §6)

**For #1049.**
- On the branch as SM:312 states it (linear, no offset), P2e follows from R-kin (Proposition D).
- Under Φ-dyn, the dependence on b = 0 is carried by that branch premise, whose underlying bridge
  SM:232 records as unproved. It returns exactly when an offset reaches the observer-level update
  (lane 1's SM:232 condition).
- When it returns:
  - off resonance, the static shift restores the action about x* (class (b));
  - at resonance on T, with stationarity required, no condensate state exists ([L2] Proposition
    4(b));
  - at resonance without stationarity, the loss of the A_1 phase holds for [L1-Q4]'s action on the
    abstract ℂ^6 and is conditional on it.
- Under Φ-kin, P2e is vacuous and no dependence on b arises.
- Q4b and O5 are not decided. Lane 1's conditions Q4c, H-b and SM:232 are carried.

**For #1217.**
- Layer M needs only H-link's abstract ⊗ℂ.
- Layer Φ rests on several premises:
  - H-PF (independent of the stated premises);
  - L-SDS (not stated);
  - TPC (stated under r2, independent under r1);
  - SMD (not stated; on T required by Proposition A and not replaceable by extremality);
  - at μ = 1, H-ZM or H-top and L-NZM (unit C).
- None is derived from stated premises.

## 8. Productivity verdict (PLAN.md §7)

**The test is met through G4, pending review.** Proposition A gives a state on T (abs(μ) < 1 or
V_rest; L ≥ 7) that meets every stated premise and lane 2's conditions and defeats P2d. This goes
beyond reproducing Counterexamples 9 and 10.

- **G1 is withdrawn.** Proposition D is the fact that makes CC7 fail, so PLAN.md §5 reports it as
  vacuous.
- G2 holds only through items that also fail under R-dyn.
- G3 is not met.

**Pressure test (Proposition A, unfavourable).** Proposition A was tested against a pure-phase
requirement. Proposition B shows that on T such a requirement excludes the conclusion itself.

**Classification (§A.31):**

| Class | Findings |
| --- | --- |
| NEW | Proposition A (SMD); Proposition B; the split of P2 into P2a–P2e |
| POSITIVE | Lemma 1 |
| ELABORATING | Proposition C; the r1/r2 variance; Q3 independence of H-PF and of TPC under r1; the SM:428 reading |
| BORDERLINE | Proposition D |
| CONFIRMING | CC1–CC3; the A1-11 record's classification of the complex structure and condensate as non-native inputs |

## 9. Open nodes

- **O1 (unit C).** H-ZM / H-top at μ = 1, for H6-Φ, P1 and L-NZM. Not pursued here.
- **O2.** Whether any premise states L-SDS or SMD. None does in the §4 primary scope, which was read
  in full, or in the sweep hits read (§12). SM:290 and SM:298 record the stationary law and the
  Gaussian limit as open.
- **O3.** On Z: whether spatial clustering plus stationarity under the linear F implies SMD. This
  is a literature route on Gaussianity of invariant states of free lattice dynamics, not checked.
  Propositions A and B are not claimed on Z.
- **O4.** R-res for the observer-level interactions (H-PF-int).
- **O5.** The owner reading of SM:374 (r1 or r2) and of "unbroken subgroup" (Φ-kin or Φ-dyn).

## 10. Findings for routing (listed, not edited)

1. **SM:342 and SM:344.** P2 holds as the inclusion given H-PF. Equality needs L-SDS, TPC (r1) and
   SMD; the last is shown on T, abs(μ) < 1 or V_rest, L ≥ 7. "Exact conditional on H-link + H-cust"
   holds for the statement only. Route: #1217.
2. **Lane 2 REPORT-r2 §4.7 and §6 item 3.** The stabilizer conclusion holds for the two-point
   function. For the state it also needs SMD (Proposition A, on T as above). A mutable record citing
   it (PRESERVATION.md) would carry this. Route: #1217.
3. **SM:136 and SM:493** state a spontaneous breaking of a dynamical symmetry (Φ-dyn). Theorem 5's
   proof uses no U(6) symmetry of the substratum dynamics. Under the R-dyn reading, SM:493's "locally
   U(6) invariant" has no content at the Z/q level, and it may refer to A6 covariance. SM:493's
   "(Theorem 5, revised)" is revision-history voice (§A.33). Route: #1029.
4. **Section pointers.** SM:613 "(§4.3)" and SM:130 "(Theorem 5, §4.6)": Theorem 5 is at SM:340, in
   §4.4. Route: #1029.
5. **SM:136 / SM:340 against SM:374.** The condensate clause is on-site at SM:136 and SM:340 and
   admits the two-point reading r2 at SM:374. Route: #1217.
6. **SM:428** places the stabilizer "on the lattice … before any trace-out". At the bijection level
   the complex structure is added after the fact (SM:505) and is not native (Sub:288; SM:565).
   Theorem 5's Σ is an observer-level state datum (SM:136; Proposition C). The reading therefore
   needs both the added complex structure and a lattice-level Σ. Route: #1217.
7. **PLAN.md of this unit (CC7).** The plan named examples for CC7 (threshold, offset) that lie
   outside its own §3(iii), so CC7 could not be met within §3. Recorded for the planning of
   successor units.
8. **PLAN.md of this unit (§6).** The verdict rule has no branch for items that fail under every
   reading. Had CC7 been green, the rule would have printed "kinetic symmetry does not suffice"
   from P2b–P2d, which fail equally under R-dyn. Recorded for the planning of successor units.

## 11. Off-`main` references (§A.42 item 8)

| Reference | Classification |
| --- | --- |
| commit `c6cb9170` (PLAN.md) | support on `main` once merged, for the preregistration order. The merge must keep `c6cb9170` reachable (no squash) |
| commit `8f1ee17d` (r1) | provenance (superseded text); on `main` once merged without squash |
| PR #1595 and its review comment | provenance: evidence of review; no result uses it |
| #1169 comments 7189139613, 7189143747 | provenance (authority record; synthesis) |
| lane 1 and lane 2 records, `A5-Q4-STAGE2D.md`, PRESERVATION.md, A1-11 `FORWARD-ALGEBRA.md`, `q3-a6-offsets-20261108/ASSESSMENT.md` | support on `main` at [P] (lane pins are ancestors) |
| kernel modules (`LinkDecomposition`, `OIBridge`, `A6Instantiation`, `BackgroundIndependence`) | support on `main`; statements read, not built |

Support off `main`: none.

## 12. Verification status and remediation (§A.46 item 4)

**This table authorizes no work.**

| Claim | Status | Missing | Issue | What would resolve it |
| --- | --- | --- | --- | --- |
| Q1 classifications (S/Dv/U) | unreviewed. U items rest on the reading described below | independent review | #1217, #1049 | recorded review |
| Lemma 1, 1′; §2.2–2.3 | unreviewed | independent review | #1217 | review |
| Proposition A, on T only (abs(μ) < 1 or V_rest; L ≥ 7) | unreviewed; Z not claimed | review; exact finite control on a small torus (authorization needed); the Z case (O3) | #1217 | review; authorized control; a Z argument |
| Proposition B (one direction) | unreviewed | review | #1217 | review |
| Propositions C, D; §4.3 | unreviewed; F_λ illustrative; resonant count conditional on [L1-Q4] | review | #1049, #1217 | review |
| Q3 independence results (H-PF; TPC under r1) | unreviewed; by witness | review | #1217 | review |
| CC1–CC3 re-derivations | unreviewed; inherit [L2]'s model reviews | independent non-model verification | #1217 | as lane 2 |
| Search (PLAN.md §4) | see below | the hits of the six filtered terms not read individually | #1217 | a recorded full reading of those hits |

**Search actually performed.**
- **Primary scope, read in full:**
  - SM:10–34, SM:110–140, SM:216–620 and SM:805–815. Of SM:811, only the parts bearing on SM:809's
    step were used; the energy question is unit C's.
  - Sub:80–110 and Sub:140–200.
  - Main:736–750.
  - ch05 (whole), checked line by line against FULL.
  - The statements of the four kernel modules.
- **Supplementary sweep over `papers/*.md`, `book/*.md` and `verification/`.** All twelve PLAN.md §4
  terms were swept at [P]. "Condensate", "Σ", "⟨φφ", "⊗ℂ / \otimes\mathbb C" and "stationary" were
  swept in r3.
- **Every hit read in context (six terms):**
  - "two-point";
  - "positive-frequency";
  - "U(6)";
  - "unbroken";
  - "⟨φφ" (one manuscript hit, SM:340; four record hits);
  - "⊗ℂ" (manuscript hits SM:32, SM:362, SM:531, Sub:280, ch05:106 and FULL:1421; ten record
    files).
- **Hits read only through a filter (six terms):**
  - **"Complex structure", "H-cust", "custodial"** (122 files under `verification/`): hits
    co-occurring with "deriv", "stationar", "Gaussian", "two-point", "supplied", "sourc" or
    "follows".
  - **"Condensate"** (72 files under `verification/`): hits co-occurring with the same words or
    "native". Manuscript hits (19 files) were not read individually outside the primary scope.
  - **"Σ"** (364 files under `verification/`; the symbol is mostly the summation sign): only hits
    on lines that also name the condensate were read, through the condensate filter. Manuscript
    hits (30 files) were not read individually outside the primary scope.
  - **"Stationary"** (161 files under `verification/`; 8 manuscript files):
    - Record hits co-occurring with "condensate", "Σ", "Theorem 5", "complex structure",
      "two-point" or "H-cust" were read; three lines, none bearing on the condensate state.
    - Manuscript hits co-occurring with "condensate", "Gaussian", "realized", "two-point" or "Σ"
      were read. These are SM:290, SM:292, SM:298, SM:803, SM:811 (unit C's) and SM:1225, which
      bear on the scalar stationary law or the gauge measure; GR:56 and GR:859 (horizon regimes);
      and ch18:52 with its FULL:4785 mirror (Born status).
- **Result of the r3 sweep.**
  - No hit states or derives H-PF, L-SDS, TPC or SMD.
  - Three foundations audits treat the condensate as a supplied input: A1-11 `FORWARD-ALGEBRA.md`
    ("NON-NATIVE INPUT"), `a1-finiteness-classes-20261117/CLASSIFICATION.md` ("PHYSICAL SOURCE
    GAP"; "lacks native H-link and condensate") and `a1-09-dependency-census/CENSUS.md` ("supplied
    condensate stabilizer").
  - SM:1225 lists "Open stationary-law and measure-map obligations", and SM:803 calls the
    stationary-law and Gaussian-limit step a "proposal".
  - No classification changes.

## 13. Node log

- **Pass 1.** Seed classification. Layer M.
- **Pass 2.** Split of P2; CC1–CC3; Proposition A.
- **Pass 3.** Proposition B.
- **Pass 4.** CC7; Proposition D; offset and F_λ; Proposition C.
- **Pass 5.** Q3 and restatements. No NEW finding.
- **Pass 6.** §A.34 re-check. No NEW finding. The checks:
  - CC3's equality, both inclusions;
  - P5's "iff distinct";
  - Proposition B, one direction only.
- **Pass 7 (r2; sweep completed in r3).**
  - Completed reading of the primary scope, and the supplementary sweep as described in §12.
  - Repairs of Proposition B, the F_λ algebra and the resonant count.
  - The reading added SM:222, SM:290, SM:298, SM:428 and SM:565, and the A1-11 and Q3-assessment
    records. The r3 sweep added SM:803, SM:1225 and the three foundations audits named in §12.
  - All are supporting or elaborating, and none changes a classification. No NEW finding.

**Stopping rule.**
- The first branch of PLAN.md §8 holds for the primary scope and for the six sweep terms whose
  every hit was read: "two-point", "positive-frequency", "U(6)", "unbroken", "⟨φφ" and "⊗ℂ".
- It does not hold for the six terms read through a filter: "complex structure", "H-cust",
  "custodial", "condensate", "Σ" and "stationary".
- The alternative branch holds: passes 5, 6 and 7 are three consecutive passes with no NEW finding.
- Every ledger item is classified, and each Q3 target has an outcome.
