# F-SLICE-HZM: does the centred label-sector J supply what Theorem 5's Σ and H-PF consume? Report

**WIP / UNVERIFIED. Model-written research record, paper-only, pending independent review. Nothing here is adopted, proposed for the manuscripts or authorized beyond the unit scope. No premise is adopted, weakened or changed, and H-ZM is not changed.**

- **Plan:** `PLAN.md` in this directory, commit `7e85350126158ae7c2f95bf6312cf8f735f18a01`, committed alone before this report. No deviation from its decision rule, controls or stopping conditions; the one widening is named in §1.
- **Accountable Issues:** #1217 and #1049; programme #1169. Work package, authorization and Goal link: as in PLAN.md (WP-2, #1169 comment 7199704501; #1169 comment 7200549806, item 4).
- **Pinned main commit [P]:** `a8d4ab969e274dc6ba25cbc6021da909d5aec814`. `papers/` at [P] equals `papers/` at `353a066f18766837fed8c7f58507e09ff549b1a4`, the pin of units A and C.
- **Labels.** [A] exact hand algebra here; [W] reasoning here; [P] text quoted at [P]; [L2], [A-rec], [C3]: a result of lane 2 (`verification/programmes/oi-qm/reconstruction/complex-carrier-20261126/REPORT-r2.md`), of unit A (`verification/programmes/oi-qm/reconstruction/theorem5-premise-ledger-20261126/REPORT-r3.md`) or of unit C (`verification/programmes/substratum/hzm-energy-sourcing-20261126/REPORT-r3.md`), each a model-reviewed paper derivation, not an independently verified theorem, used as a named conditional input (§A.46 item 7).
- **Evidence layer of every new result:** mathematical derivation on paper. No computation was run and no Lean was built.
- **Premise status words:** proved (on paper, here or in a cited record), conditional (holds under named premises), posited (a stated posit of the framework), open (neither proved nor posited).

## 0. Summary

| Item | Result |
| --- | --- |
| What the F-slice supplies (Q-J) | The label-sector family collapses to one linear map: the centring x ↦ x − x*(t) equals the spectral projection P_rest on the stationary support, and the "J on every label sector" is the single J_F on V_rest, label-independent. This is the J of lane 2's Proposition 5. Unit C's disintegration step (c), its one [W] step, is not consumed by any Theorem 5 input (§3). [A] |
| Hidden assumption in C3 (d) | Uniqueness holds because C3 takes J time-independent in deviation coordinates (J commutes with the deviation dynamics F). If J is only required on the label sector, so that the two slices of a staggered pair may carry different structures intertwined by F and the translations, the tamed structures form a one-parameter family (J_t, J_{−t}) for every even L (§3.3). [A] |
| Lemma L | Any continuous action of U(6) on the static labels that commutes with the lattice translations (equivalently with F) is trivial on SU(6). The internal action on the link index cannot extend to the static labels (§4.1). [A] |
| Label exclusion | Given H-PF on V_rest and the U(6)-covariance of φ that P2a already consumes, Lemma L forces φ to vanish on the static labels: φ = Φ_n ∘ P_rest. The condensate is then the V_rest second moment Σ_c, the object of the H-ZM route (§4.2). [A] |
| Consumers (Q-cons) | Layer M items: NC. H6-Φ, P1, P2a, P2b–P2e and L-NZM: S under the extension reading of the custodial action (§5). The internal reading of P1 is OB (Lemma L). The uncentred reading of Σ is OB for P2a (witness ρ_W, §6). |
| Outcome (PLAN §4) | **R1, route around H-ZM**, on carrier T at the massless point, under the extension reading of SM:342's custodial action, conditional on LIN, LIFT, b_A1 = 0, a stationary law with finite second moments, and lane 2's Theorem 1. Every control is green (§7). |
| What R1 means | For Theorem 5's inputs on T, H-ZM's claim that the static modes are unobservable is not needed. The static labels stay as observable classical data, consistent with Main's specified partitions, and the covariance that P2a already uses keeps them out of the condensate. No premise is removed: H-PF, TPC, SMD and L-SDS remain carried, and lane 2's sentence "Exclusion requires the named hypothesis H-ZM" stays true as stated, since the F-slice does not exclude the null sector. |

## 1. Execution

- Read in full: C3 §5.3, §7.2 and §11; L2 §1–§4 and §5–§6; unit A §1–§7 and §9; lane 2 PRESERVATION.md §2; SM:340–344, 360–364 and 374, with SM:136, 222, 230, 232, 240, 290, 292, 298 and 312–316 for the lift trace.
- **Widening W-1.** A search for a stated centring of the condensate or a stated exclusion of the static background from it, over `papers/*.md` and `book/*.md` at [P]: "connected", "centred", "centered", "fluctuation", "where the inverse exists", "zero mode", "zero-mode", "uniform background", "background value", "subtract", and a regular expression pairing "condensate" with "connected", "centred", "centered", "fluctuat", "subtract" or "zero.mode" within 200 characters. Each SM and Substratum hit was read in context. None states a centring or exclusion for Theorem 5's Σ. SM:292's "on a sector where the inverse exists" restricts the proposed scalar Gaussian's covariance, a different object with proposal status; it is not a premise of Theorem 5. This search is not exhaustive and §4.2 does not rest on it.
- Passes: four depth-first passes over the consumers (§9). Stopping condition 1 applies.

## 2. Q-lift: the real-lift dependency

Each link from the substratum to the F-slice output, with its status.

| # | Link | Source | Status |
| --- | --- | --- | --- |
| 1 | The substratum-to-observer map: "**But the map $\varphi\to L_{\rm obs}\to\Delta_g$ is not proved anywhere in this framework.**" | SM:232 [P] | open |
| 2 | The real lift exists as the observer-level description (LIFT): "a real/complex wave operator is an observer-level lift whose derivation must be stated separately" | SM:222 [P]; L2 §5 | open |
| 3 | The observer-level update F(u, v) = (v, A v − u) ⊗ I_6, "stated on the observer-level branch of Corollary 1b", and "not identified with the fundamental bijection (finite under A1) without the coarse-graining bridge of §4.1" | SM:312–316 [P] | conditional on 1 and 2 |
| 4 | Linearity (LIN): "Linearity (A5) is a further restriction imposed on the selected lattice model" | SM:240 [P]; Main ledger (vii) | posited |
| 5 | M = μI_6 at μ = 1 (αμ = 1/d), the massless symmetric point | SM:230, SM:322, SM:334 | the normalization is observer-level (SM:232): conditional on 1 |
| 6 | Carrier T = (Z/L)^d | A1 via SM:222 | posited (A1) |
| 7 | b_A1 = 0 | offset-free form of SM:312; necessary for any stationary law at μ = 1 on T ([L2] Proposition 4(b)) | conditional on 3 and 4 |
| 8 | An F-stationary law ρ with finite second moments (L-SDS). "the stationary law and Gaussian limit of the realized scalar dynamics" are open; "Whether one realized map supports both the structural chain and the required stationary law remains open" | SM:290, SM:298 [P]; [A-rec] H4b | open (not stated) |
| 9 | Support on L_0 ⊕ V_rest (w = 0 almost surely) | [L2] Proposition 4(a); [C3] (a) | proved, conditional on 3–8 |
| 10 | P_rest is F-equivariant and the second moment splits (§3.1) | here [A] | proved, conditional on 3–9 |
| 11 | J_F on V_rest, unique among tamed F-commuting structures | [L2] Theorem 1, with E positive definite on V_rest ([C3] (d) [A]) | proved, conditional on 3, 4 |
| 12 | Time-independence of J in deviation coordinates (LI) | [C3] (d), by construction | part of C3's definition; exposed in §3.3 |
| 13 | [C3] step (c), disintegration over the labels | [C3] (c) [W] | not consumed (§3.2) |

Nothing in links 1–13 concerns the Z/q level or the bijection-level carrier of SM:505. Every result below inherits links 1–8 as conditions.

## 3. Q-J: what the F-slice supplies

Notation as in [L2] §1 and [C3] §5.3: V = V_0 ⊕ V_π ⊕ V_rest, with V_π present for even L; L_0 the static subspace, spanned by (𝟙, 𝟙) ⊗ c and (s, −s) ⊗ a, with c, a ∈ R^6 and s_n = (−1)^{abs(n)}. P_0, P_π and P_rest are the spectral projections of A ⊗ I_2 onto a = 2, a = −2 and (−2, 2).

### 3.1 The centring is the spectral projection [A]

- P_0, P_π and P_rest are functions of A ⊗ I_2, and F = [[0, I], [−I, A]] has entries that are polynomials in A, so all three commute with F.
- On the support L_0 ⊕ V_rest (link 9), write x = l + y with l = (P_0 + P_π)x ∈ L_0 and y = P_rest x. On L_0, F acts as +1 on the c-block and −1 on the a-block. So l(t) = c(1, 1) + (−1)^t a(1, −1) = x*(t) of [C3] (d), and the deviation is x − x*(t) = P_rest x, a fixed linear map independent of t and of the label.
- **Moments from stationarity alone.** Let D = F|_{L_0} = diag(I, −I) on (c, a). Stationarity gives
  - E[y] = F E[y], hence E[y] = 0, since F has no eigenvalue 1 on V_rest;
  - E[a] = −E[a], hence E[a] = 0; E[c] is unrestricted;
  - X = E[l yᵀ] satisfies X = D X Fᵀ. On the c-block X_c(Fᵀ − I) = 0 and on the a-block X_a(Fᵀ + I) = 0. F has neither eigenvalue +1 nor −1 on V_rest, so X = 0;
  - the c–a block of E[l lᵀ] satisfies Y = −Y, so it vanishes.

  So the second moment is the direct sum E[c cᵀ] ⊕ E[a aᵀ] ⊕ C_rest, with C_rest the second moment of P_rest x. No disintegration is used.

### 3.2 The label-sector J is one J [A]

[C3] (d) places, on the slice through x*(t), the structure x*(t) + y ↦ x*(t) + J_F y. By §3.1 this is the linear map 𝒥 = id_{L_0} ⊕ J_F on L_0 ⊕ V_rest. Hence:
- the J on every label sector is the same operator, J_F on V_rest, and it equals the J of lane 2's Proposition 5, since the coisotropic reduction {w = 0}/L_0 is identified with V_rest by the same P_rest;
- 𝒥² = id ⊕ (−1) ≠ −1. No complex structure on L_0 ⊕ V_rest that preserves it is tamed: for l ∈ L_0, l lies in the radical of ω restricted to L_0 ⊕ V_rest, so ω(Jl, l) = 0 whenever Jl ∈ L_0 ⊕ V_rest. The F-slice supplies a complex structure on the fibre V_rest, not on the stationary support;
- every Theorem 5 input traced in §5 reads the state only through the law P_rest∗ρ, which is F-invariant on V_rest with finite second moments. The disintegration of [C3] (c) is therefore not consumed.

### 3.3 Hidden assumption: uniqueness needs a label-independent J [A]

Let L be even and a ≠ 0, so the label sector consists of two slices S_± = c(1, 1) ± a(1, −1) + V_rest. F maps S_+ to S_−, and so does each unit translation T_j, since T_j s = −s. Both slices have tangent space V_rest.

**Proposition P (pair-level non-uniqueness).** Consider pairs (J_+, J_−) of complex structures on V_rest, tamed by ω, with F J_± = J_∓ F and T_j J_± = J_∓ T_j for every j. Besides (J_F, J_F) there is a one-parameter family (J_t, J_{−t}), t ∈ R, with J_t ≠ J_F for t ≠ 0. A pair with J_+ = J_− is (J_F, J_F).

*Proof.*
- The conditions hold iff J_+ commutes with the slice-preserving group 𝒢_+, generated by F², the products T_i T_j^{±1} and T_j⁻¹F, and J_− = F J_+ F⁻¹. (From F J_+ = J_− F and F J_− = J_+ F, J_+ commutes with F²; from T_j J_+ = J_− T_j, J_+ commutes with T_j⁻¹F. The converse is direct.) The group generated by F and the T_j is abelian, so F preserves each joint eigenspace of 𝒢_+.
- Pick k with a(k) ∉ {−2, 0, 2}; for even L ≥ 4, k = (2π/L, 0, …, 0) qualifies. Then k + π also lies in V_rest, since a(k + π) = −a(k). Let P be the F-eigenspace for e^{iθ} at momentum k (θ = θ_k), and N the F-eigenspace for e^{−i(π−θ)} = −e^{iθ} at momentum k + π, each ≅ C^6.
- On 𝒢_+ the two have the same character: F² gives e^{2iθ} on both; T_iT_j^{±1} gives e^{i(k_i ± k_j)} on both, since the π's cancel modulo 2π; T_j⁻¹F gives e^{−ik_j}e^{iθ} on P and (−e^{−ik_j})(−e^{iθ}) on N. So E = P ⊕ N lies in one joint eigenspace E_χ, and χ ≠ χ̄ because e^{2iθ} is not real (θ ≠ π/2).
- With h(z, z′) = 2iω(z, z̄′), hermitian on E_χ: h > 0 on P and h < 0 on N ([L2] Theorem 1's Krein sign, applied at k and, conjugated, at k + π), and P ⊥_h N, because ω(z, z̄′) carries the translation character e^{ik}e^{−i(k+π)} = −1. h is nondegenerate on E_χ, which ω pairs only with E_χ̄. Write E_χ = E ⊕ E^{⊥h}.
- In h-orthonormal bases of P and N, set S_t = [[cosh t, sinh t], [−sinh t, −cosh t]] ⊗ I_6 on E, and S = +1 on the F-positive and −1 on the F-negative part of E^{⊥h}. Then S² = 1, and hS is positive definite: on E it is [[cosh t, sinh t], [sinh t, cosh t]] ⊗ I_6, and on E^{⊥h} it is J_F's taming. Define J_t = iS on E_χ, its conjugate on E_χ̄, and J_F on every other joint eigenspace. For x = z + z̄, ω(J_t x, x) = Re h(Sz, z) > 0, so J_t is a tamed complex structure commuting with 𝒢_+, and J_t ≠ J_F for t ≠ 0. This is the mechanism of the indefinite-B family of [L2] §2.3.
- F preserves E and h, acts on E as e^{iθ} diag(1, −1) and commutes with S on E^{⊥h}, so F J_t F⁻¹ = J_{−t}.
- If J_+ = J_−, then J_+ commutes with F, and [L2] Theorem 1 on V_rest gives J_F.
∎

**Reading.** In deviation coordinates the family is a period-two J(t) = J_{(−1)^t t}. [C3] (d) excludes it by requiring a single J commuting with the deviation dynamics y ↦ Fy (link 12, LI). LI is the F-slice's form of the requirement that J commute with the update on the reduced space, which Proposition 5's route carries, and which H-ZM supplies automatically because the quotient identifies S_+ with S_−. For L odd, or a = 0, the sector is one F-invariant slice and Theorem 1 gives J_F with no further condition. Whether any stated premise selects LI over the family is open (N-2). The classes of §5 are for C3's construction, which includes LI.

## 4. The static labels and the custodial action

### 4.1 Lemma L [A]

Let ρ: U(6) → GL(L_0) be a continuous homomorphism commuting with the translations restricted to L_0 (T_j|_{L_0} = diag(I, −I) on (c, a), which equals F|_{L_0}). Then ρ is trivial on SU(6). In particular, no such ρ restricts on SO(6) ⊂ U(6) to the internal action c ↦ Xc, a ↦ Xa.

*Proof.* ρ preserves the c-block and the a-block, each ≅ R^6. A real representation of SU(6) of dimension 6 complexifies to a self-conjugate complex representation of dimension 6. The nontrivial irreducible representations of SU(6) of dimension at most 6 are the fundamental 6 and its dual 6̄, and 6 ≇ 6̄. So each block is trivial for SU(6). SO(6) ⊂ SU(6), and its internal action is not trivial. ∎

So, on the F-slice, the custodial U(6) acts on the static link labels at most through det: U(6) → U(1). This sharpens [L2] Proposition 3 and its remark that the U(6) "is not a group acting on the six-link carrier at k = 0" ([L2] REPORT-r2.md line 275): there the statement concerns the symplectic commutant on V_0, and here any translation-commuting continuous action on the stationary labels.

An action that does not commute with the translations can act internally on the labels: with z = c + ia, z ↦ wz preserves E and ω restricted to L_0 ⊕ V_rest. It mixes the k = 0 and k = π sectors, since T_j acts on z as complex conjugation, so it is neither an internal symmetry of the link index nor a symmetry of F. It is outside the readings admitted in §5.

### 4.2 The label exclusion follows from covariance [A]

The step P2a ([A-rec] §2.3) uses the covariance φ(R(w)x) = wφ(x) for x in the support of the state; Stab(state) ⊆ Stab(Σ) follows from it. On the F-slice the support is L_0 ⊕ V_rest. Let the custodial action there be any extension R_ext of R(w) on V_rest by a continuous, translation-commuting action on L_0 (Lemma L), and let φ be real-linear in x, with φ = Φ_n on V_rest (H-PF on V_rest). For l ∈ L_0 and w ∈ SU(6), covariance gives φ(l) = φ(R_ext(w) l) = wφ(l). SU(6) fixes no nonzero vector of C^6, so φ(l) = 0. Hence

    φ = Φ_n ∘ P_rest,   Σ = Σ_c := E[Φ_n(P_rest x) Φ_n(P_rest x)†],

which is the condensate of the H-ZM route, computed from P_rest∗ρ. The extension is unique on SU(6) and exists: R_ext = id on V_null ⊕ R(w) on V_rest commutes with F and the translations and preserves ω and E, because V_null is ω-orthogonal to V_rest and L_0 = ker D lies in the radical of E (D = F − A/2 vanishes on L_0: D(1, 1) = 0 at a = 2 and D(1, −1) = 0 at a = −2).

No premise beyond those Proposition 5's route carries is used: H-PF and P2a's covariance are carried by Theorem 5's ledger ([A-rec] P2a, H4a), and the translation-commuting action is the admitted reading of P1 (§5). The label exclusion, which a reader might take as a new bridge clause, is derived.

## 5. Q-cons: the consumers in Theorem 5

The consumers are the ledger rows of [A-rec] §2 that carry Proposition 5's output (H6-Φ, P1, L-NZM, and through them P2a–P2e), together with the layer M rows. The proof steps are SM:342 [P]: "Under H-cust the pre-condensate observer-level kinetic term is invariant under the custodial unitary action on the physical link carrier" (P1); "The unbroken subgroup of a state with condensate $\Sigma$ is its unitary stabilizer" (P2); and the Schur and stabilizer steps (P3–P5).

| Consumer | What it reads from the reduced space | F-slice class | Reading, and reason |
| --- | --- | --- | --- |
| H1, H3, H5, H6-M, P3, P4, P5 (layer M) | nothing ([A-rec] §2.2: abstract ⊗ℂ of SM:362) | NC | — |
| H2, H2a (kinetic clause) | nothing (Proposition 4b, any μ) | NC | — |
| H6-Φ | a complex structure commuting with the update, tamed, on the space the state lives on | S | J_F on the fibre V_rest commuting with the deviation dynamics (§3.2, with LI). The reading "a complex structure on the whole stationary support" is OB (§3.2), as it is for every route at μ = 1 on T ([L2] Proposition 3) |
| P1 | a custodial unitary action that leaves the kinetic term invariant, on the physical link carrier | S | extension reading: R_ext of §4.2. The internal reading, in which U(6) acts on the static link labels by the same internal action as on every other mode, is OB (Lemma L) |
| P2a, with H-PF | φ(R(w)x) = wφ(x) on the support; Stab(state) ⊆ Stab(Σ) | S | §4.2: covariance and Lemma L give φ = Φ_n ∘ P_rest, so the inclusion holds as on V_rest. The uncentred reading (labels inside φ, not covariant) is OB (§6) |
| P2b (C_− = 0) | J-Hermiticity of the state's moment | S | on Σ_c, [L2] Proposition 7 on V_rest with L-SDS, as on the H-ZM route |
| P2c (TPC) | the two-point clause | S | on C_rest, as on V_rest ([A-rec] CE9 range includes V_rest); the state condition is carried, not supplied |
| P2d (SMD) | the state's stabilizer equals its second moment's | S | on P_rest∗ρ, as on V_rest ([A-rec] Proposition A range includes V_rest); SMD is carried and is the rank-1 investigation's question |
| P2e | the stabilizer is a symmetry of the full dynamics | S | R_ext commutes with F on all of V, so [A-rec] Proposition D extends |
| L-NZM | a non-zero-mode condensate at μ = 1 | S | §4.2: Σ = Σ_c is supported on V_rest. The macroscopic zero-mode reading of [L2] Proposition 11 cannot enter a covariant Σ, consistent with that proposition's "leaves U(6) unbroken" |

Under the most favourable admitted reading every consumer is NC or S. Under the internal reading of P1, P1 is OB on the F-slice.

## 6. The uncentred reading: witness ρ_W [A]

Let L ≥ 4, μ = 1, b = 0. Let ρ_W be the product of:
- on the labels: a = 0, and c a centred Gaussian on R^6 with covariance Σ_b σ_b² P_b, σ_b pairwise distinct;
- on V_rest: the centred Gaussian with covariance κ G⁻¹ ⊗ I_6, κ > 0, G⁻¹ the inverse J-metric ([A-rec] §2.4).

It is F-stationary (F is the identity on c; G⁻¹ ⊗ I_6 is F-invariant), translation-invariant, cubic-invariant (Σ_b σ_b² P_b commutes with the link representation), has finite second moments and is supported on L_0 ⊕ V_rest.
- **Centred (covariant) reading.** Σ_c = 2γκ I_6 ([L2] Proposition 8 form). The block values coincide, so H5 fails and Theorem 5 does not apply. No defect.
- **Uncentred reading** (H-PF_u: φ = ℓ_n(l) + Φ_n(P_rest x), labels entering as a real part). By §3.1 the cross moments vanish, so Σ_u = Σ_b (2γκ + σ_b²) P_b. Its block values are distinct and its matrix stabilizer is U(3)×U(2)×U(1). But R_ext(w) preserves ρ_W for every w, and under any translation-commuting extension SU(6) acts trivially on the labels (Lemma L), so SU(6) ⊆ Stab(ρ_W) ⊄ U(3)×U(2)×U(1). P2a fails. The distinct values come entirely from the static labels, as in [L2] Proposition 11.

So the uncentred reading is OB for P2a, and a Theorem 5 conclusion drawn from it would be the witness → theorem error the claim/evidence rules guard against.

## 7. Controls

| Id | Result | Status |
| --- | --- | --- |
| C+1 | At abs(μ) < 1 there is no null sector: L_0 = 0, P_rest = I, R_ext = R(w), and §4.2 reduces to H-PF. Every consumer takes [A-rec]'s class without H-ZM (H6-Φ, P1 and P2e Dv via J_F; P2a Dv given H-PF; P2b–P2d carry L-SDS, TPC, SMD) | green |
| C+2 | Under H-ZM the reduced space is {w = 0}/L_0 ≅ V_rest by P_rest, φ = Φ_n([x]) = Φ_n(P_rest x), and Σ is supported off the null sector: every consumer [A-rec] marks as carrying H-ZM is supplied. This reproduces [L2] Proposition 5 | green |
| C−1 | The uncentred reading was tested against P2a with ρ_W (§6) and classified OB, not S | green |
| C−2 | Rejected as H6-Φ: 𝒥 = id ⊕ J_F (𝒥² ≠ −1); any J preserving L_0 ⊕ V_rest (untamed, §3.2); the site-local J_0 and site-local structures ([A-rec] Lemma 1′, [L2] Proposition 2). The pair family J_t (§3.3) is tamed and F-intertwining but violates LI, and is recorded, not accepted as C3's J | green |
| C−3 | With b_A1 ≠ 0 at μ = 1 no stationary law exists ([L2] Proposition 4(b)); the F-slice is empty and supplies nothing | green |
| C−4 | The SM quotes (SM:136, 222, 232, 240, 290, 292, 298, 312, 316, 340, 342, 344, 362) and the record quotes (L2 line 275 and its summary row; A-rec rows H6-Φ and L-NZM and §2.3; C3 §5.3 (d)) were re-extracted at [P] by fixed-string match | green |

## 8. Outcome against the decision rule (PLAN §4)

Every consumer is NC or S under the most favourable admitted reading (§5), and every control is green. The rule prints:

**R1, route around H-ZM.** For Theorem 5's consumers on carrier T at the massless point, H-ZM can be replaced by the F-slice, under the extension reading of the custodial action in SM:342 and the LI form of F-commutation, conditional on LIN, LIFT, b_A1 = 0, a stationary law with finite second moments, and lane 2's Theorem 1.

Directional statements (§A.34):
- **H-ZM route ⇒ F-slice inputs.** Under H-ZM every input of §5 is supplied with the same J and the same Σ (C+2).
- **F-slice ⇏ H-ZM.** The F-slice supplies these inputs while the static labels remain registered and conserved, as Main's specified partitions require ([C3] §4.1). Unobservability is not used.

Scope:
- carrier T only; carrier Z (H-top) is not addressed;
- Theorem 5 only; other consumers of H-ZM or of the static labels (the SM:811 energy, the charged matter action and amplitude-scale gauge of SM:344) are not traced;
- the linear lift only (H-PF-int is not addressed);
- no premise is removed from Theorem 5: H-PF, L-SDS, TPC and SMD remain carried and unsourced, and LIN, LIFT and the SM:232 bridge remain conditions;
- under the internal reading of P1 the F-slice is OB, and only the H-ZM route remains for that reading. That reading choice is the owner's (N-1).

Nothing is proposed for the manuscripts. Narrowing [A-rec]'s rows H6-Φ ("at μ = 1 V_rest / K: H-ZM / H-top (unit C)") and L-NZM ("depends on H-ZM (unit C)") on T, or lane 2's PRESERVATION statement of what Theorem 5's use of J needs, would be a change to records outside this unit and is listed for routing only (§11).

## 9. Passes, classification and productivity

- **Pass 1** (Q-lift; Q-J): §2, §3.1, §3.2. ELABORATING, with step (c) found not consumed (POSITIVE).
- **Pass 2** (skepticism on the favourable uniqueness in C3 (d)): Proposition P. NEW.
- **Pass 3** (consumers; P1 and P2a on the labels): Lemma L (ELABORATING [L2] Proposition 3), the label exclusion of §4.2 (NEW), witness ρ_W (ELABORATING [L2] Proposition 11).
- **Pass 4** (skepticism on the favourable R1): the non-translation-commuting action z ↦ wz (§4.1), the internal reading of P1, and whether §4.2 smuggles a premise (it uses only H-PF on V_rest, P2a's covariance and the translation-commuting reading). No NEW finding; the reading dependence is recorded as N-1.

Stopping condition 1 holds: the rule resolved with all controls green.

**Productivity (PLAN §7): gem.** The unit yields facts strictly stronger than C3's O3: the F-slice's J is Proposition 5's J; its uniqueness rests on LI (Proposition P); and Theorem 5's need for the null-sector treatment on T reduces, through Lemma L, to the covariance P2a already uses, except under the internal reading of P1. This constrains how H-ZM may be replaced and exposes a hidden assumption in C3 (d).

| Class | Findings |
| --- | --- |
| NEW | Proposition P (pair-level non-uniqueness; LI exposed); §4.2 (label exclusion derived from covariance and Lemma L) |
| POSITIVE | §3.1–§3.2 (centring is P_rest; one J; step (c) not consumed; moment split without disintegration) |
| ELABORATING | Lemma L; witness ρ_W |
| CONFIRMING | C+2 (Proposition 5 reproduced) |

Correctness bands unchanged: consistency-axis work (§A.23).

## 10. Open nodes

- **N-1 (owner reading).** Whether "the custodial unitary action on the physical link carrier" (SM:342) must act on the static link labels by the internal action (F-slice OB by Lemma L; only the H-ZM route remains) or admits a translation-commuting extension acting trivially on them on SU(6) (R1). Related to [A-rec] O5.
- **N-2.** Whether any stated premise selects the label-independent J (LI) over the period-two pair family of Proposition P on staggered label sectors (L even, a ≠ 0). Not searched beyond the inputs.
- **N-3.** Carrier Z: the F-slice adds nothing; H-top stands ([L2] Proposition 6).
- **N-4.** Other consumers of H-ZM or of the retained static labels outside Theorem 5 (SM:811 energy shells, the SM:344 reduction, the amplitude-scale gauge of [C3] O1) are not traced.
- **N-5.** Inherited and carried: LIN, LIFT and the SM:232 bridge; L-SDS (SM:290, SM:298); lane 2's Theorem 1 (model-reviewed); TPC, SMD and H-PF itself, unsourced ([A-rec] §5, §9 O2).
- **N-6.** The nonlinear lift (H-PF-int): the F-slice relies on the linear F throughout.
- **N-7.** Independent review of Proposition P, Lemma L's application, §4.2 and ρ_W, required by the authorization before any use.

## 11. Findings for routing (listed, not edited)

1. [A-rec] rows H6-Φ and L-NZM: on T at μ = 1, the F-slice supplies these inputs without H-ZM under the extension reading (§5, §8). Route: #1217.
2. [C3] §5.3 (d) "the unique tamed commuting J on every label sector": unique under LI; the pair level admits the family of Proposition P. A mutable record citing C3 (its PRESERVATION.md) could carry this. Route: #1217.
3. [C3] §5.3 pressure test, "step (c) is [W]": no Theorem 5 input consumes step (c) (§3.2). Route: #1217.
4. [L2] Proposition 5 and PRESERVATION §2 ("exclusion needs the named hypothesis H-ZM"): true as stated; Theorem 5's use of J on T does not need the exclusion under the extension reading. Route: #1217.

## 12. References not on `main` (§A.42 item 8)

| Reference | Classification |
| --- | --- |
| #1169 comments 7199704501, 7200549806, 7191949320 | provenance: work package, authorization and question source; no result uses them |
| commit `7e853501` (PLAN.md) and the commit adding this report | support on `main` once merged without squash, for the preregistration order; not before |
| C3, L2, A-rec records and lane 2 PRESERVATION.md | support on `main` at [P] |

Support off `main`: none.

## 13. Verification status and remediation (§A.46 item 4)

**This table authorizes no work.**

| Claim | Status | Missing | Issue | What would resolve it |
| --- | --- | --- | --- | --- |
| §3.1–§3.2 | unreviewed hand algebra | independent review | #1217 | recorded review |
| Proposition P | unreviewed | independent review; an exact finite control on a small even torus (needs authorization) | #1217 | review; authorized control |
| Lemma L and §4.2 | unreviewed; Lemma L uses standard representation theory of SU(6) | independent review | #1217 | review |
| Witness ρ_W | unreviewed | independent review | #1217 | review |
| R1 outcome | conditional on the readings of §5 and on N-5 | owner reading N-1; review | #1217, #1049 | owner decision on N-1; review |
| W-1 search | keyword-based, not exhaustive | not needed for §4.2, which is derived | #1217 | — |
