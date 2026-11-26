# F-SLICE-HZM: does the centred label-sector J supply what Theorem 5's Σ and H-PF consume? Report, r2

**WIP / UNVERIFIED. Model-written research record, paper-only. Nothing here is adopted, proposed
for the manuscripts or authorized beyond the unit scope. No premise is adopted, weakened or
changed, and H-ZM is not changed.**

**Revision r2** applies findings 1–8 of the independent review of r1. The review is posted verbatim
on PR #1611, comment 7201020516 (posted from the account amaybaum, created 2026-11-26T18:56:36Z),
with verdict REVISE. r1 is `REPORT.md` at `5073afda47acfc4fb246fa508156393cd3da8894`, kept
unchanged; `CHANGES-r2.md` maps each finding to its change. r2 is pending a focused delta review.

- **Plan:** `PLAN.md` in this directory, commit `7e85350126158ae7c2f95bf6312cf8f735f18a01`,
  committed alone before r1. §1 records how the plan's premise list is read.
- **Accountable Issues:** #1217 and #1049; programme #1169. Work package, authorization and Goal
  link: as in PLAN.md (WP-2, #1169 comment 7199704501; #1169 comment 7200549806, item 4).
- **Pinned main commit [P]:** `a8d4ab969e274dc6ba25cbc6021da909d5aec814`. `papers/` at [P] equals
  `papers/` at `353a066f18766837fed8c7f58507e09ff549b1a4`, the pin of units A and C.
- **Labels.**
  - [A] exact hand algebra here;
  - [W] reasoning here;
  - [P] text quoted at [P];
  - [L2], [A-rec], [C3]: a result of lane 2
    (`verification/programmes/oi-qm/reconstruction/complex-carrier-20261126/REPORT-r2.md`), of unit
    A (`verification/programmes/oi-qm/reconstruction/theorem5-premise-ledger-20261126/REPORT-r3.md`)
    or of unit C (`verification/programmes/substratum/hzm-energy-sourcing-20261126/REPORT-r3.md`).
    Each is a model-reviewed paper derivation, not an independently verified theorem, used as a
    named conditional input (§A.46 item 7).
- **Evidence layer of every new result:** mathematical derivation on paper. No computation was run
  and no Lean was built.
- **Premise status words:**
  - proved: on paper, here or in a cited record;
  - conditional: holds under named premises;
  - posited: a stated posit of the framework;
  - open: neither proved nor posited.

## 0. Summary

| Item | Result |
| --- | --- |
| What the F-slice supplies (Q-J) | The label-sector family collapses to one linear map. The centring x ↦ x − x*(t) equals the spectral projection P_rest on the stationary support, and the "J on every label sector" is the single J_F on V_rest, independent of the label. This is the J of lane 2's Proposition 5. J and Σ read the state only through P_rest∗ρ, so unit C's disintegration step (c) is not consumed for them. The state's stabilizer reads the joint law of labels and fluctuations, so step (c) is consumed there (§3.2, §3.4). [A] |
| Slice-dependent J (Proposition P) | C3 (d) takes J commuting with the deviation dynamics y ↦ Fy (LI). If J is required only on the label sector, the two slices of a staggered pair can carry different structures intertwined by F and the translations. The tamed structures then contain a one-parameter family (J_t, J_{−t}). This holds in d = 3 for every even L, with k = (π, 0, 0) (§3.3). [A] |
| Lemma L | Any continuous action of U(6) on the static labels that commutes with the lattice translations (equivalently with F) is trivial on SU(6). The internal action on the link index cannot extend to the static labels (§4.1). [A] |
| Label exclusion (a reading) | Covariance of φ on the labels is a requirement on how φ extends to the support. Given Lemma L, real-linearity and H-PF on V_rest, it is equivalent to φ = Φ_n ∘ P_rest, the centred reading (N-8). Under that reading the condensate is Σ_c, the object of the H-ZM route. A non-covariant real-linear extension is also admissible and defeats P2a (ρ_W, §6) (§4.2). [A] |
| Consumers (Q-cons) | Layer M items: NC. H6-Φ, P1, P2a, P2b, P2c, P2e and L-NZM: S under the readings below. P2d: S under SMD read on the full ρ, which is strictly stronger than the SMD of the H-ZM route (§5). The internal reading of P1 is OB (Lemma L). The uncentred reading of Σ is OB for P2a (ρ_W). |
| Outcome (PLAN §4) | **R1, route around H-ZM**, on carrier T at the massless point. It holds under four reading dependences: the extension reading of the custodial action (N-1), LI (N-2), the centred reading of φ on the support (N-8), and SMD read on ρ (N-9). It is conditional on LIN, LIFT, b_A1 = 0, a stationary law with finite second moments, and lane 2's Theorem 1. Every control is green; three are low-power for §4.2 (§7). Under the reviewer's alternative classification, which takes N-8 as a premise rather than a reading, the outcome is R2 (§8). |
| What R1 means | On T, Theorem 5's inputs do not use H-ZM's claim that the static modes are unobservable. The static labels stay as observable classical data, consistent with Main's specified partitions. What the route requires instead is that the field φ, not every observable, be blind to the labels (N-8). No premise is removed: H-PF, L-SDS, TPC and SMD remain carried, and SMD is needed in a stronger form. Lane 2's sentence "Exclusion requires the named hypothesis H-ZM" stays true as stated. |

## 1. Execution

- **Read in full:**
  - C3 §5.3, §7.2 and §11;
  - L2 §1–§6;
  - unit A §1–§7 and §9;
  - lane 2 PRESERVATION.md §2;
  - SM:340–344, 360–364 and 374, with SM:136, 222, 230, 232, 240, 290, 292, 298 and 312–316 for
    the lift trace.
- **Reading of PLAN §4.** Class S is defined there by the premises "Proposition 5's route already
  carries other than H-ZM", listed as LIN, LIFT, b = 0, stationarity and Theorem 1. That list omits
  H-PF, L-SDS, TPC and SMD, which unit A's ledger carries for Theorem 5 on the H-ZM route as well.
  This report treats them as carried. Where a consumer needs one of them in a stronger form on the
  F-slice than on the H-ZM route, the class states it (SMD read on ρ, §5).
- **Widening W-1: search for a stated centring or exclusion.** It looked for a stated centring of
  the condensate, or a stated exclusion of the static background from it, over `papers/*.md` and
  `book/*.md` at [P].
  - Terms: "connected", "centred", "centered", "fluctuation", "where the inverse exists", "zero
    mode", "zero-mode", "uniform background", "background value" and "subtract".
  - A regular expression pairing "condensate" with "connected", "centred", "centered", "fluctuat",
    "subtract" or "zero.mode" within 200 characters.
  - Every SM and Substratum hit was read in context, and none states a centring or exclusion for
    Theorem 5's Σ.
  - SM:292's "on a sector where the inverse exists" restricts the proposed scalar Gaussian's
    covariance. That is a different object with proposal status, not a premise of Theorem 5.
  - The search is not exhaustive. Within it, N-8 is not stated.
- **Passes:** four depth-first passes in r1 (§9), and one in r2 applying the review. Stopping
  condition 1 applies.

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
| 12 | J commutes with the deviation dynamics (LI) | [C3] (d), by construction | part of C3's definition: H6-Φ read on V_rest (§3.3) |
| 13 | [C3] step (c), disintegration over the labels | [C3] (c) [W] | not consumed for J or Σ (§3.2). Consumed through the state's stabilizer in P2a and P2d (§3.4) |

Nothing in links 1–13 concerns the Z/q level or the bijection-level carrier of SM:505. Every
result below inherits links 1–8 as conditions.

## 3. Q-J: what the F-slice supplies

Notation is as in [L2] §1 and [C3] §5.3:
- V = V_0 ⊕ V_π ⊕ V_rest, with V_π present for even L;
- L_0 is the static subspace, spanned by (𝟙, 𝟙) ⊗ c and (s, −s) ⊗ a, with c, a ∈ R^6 and
  s_n = (−1)^{abs(n)};
- P_0, P_π and P_rest are the spectral projections of A ⊗ I_2 onto a = 2, a = −2 and (−2, 2).

### 3.1 The centring is the spectral projection [A]

- **Commutation.** P_0, P_π and P_rest are functions of A ⊗ I_2. F = [[0, I], [−I, A]] has entries
  that are polynomials in A, so all three commute with F.
- **The centring.** On the support L_0 ⊕ V_rest (link 9), write x = l + y with
  l = (P_0 + P_π)x ∈ L_0 and y = P_rest x. On L_0, F acts as +1 on the c-block and −1 on the
  a-block. So l(t) = c(1, 1) + (−1)^t a(1, −1), which is x*(t) of [C3] (d). The deviation
  x − x*(t) = P_rest x is a fixed linear map, independent of t and of the label.
- **Moments from stationarity alone.** Let D = F|_{L_0} = diag(I, −I) on (c, a). Stationarity
  gives:
  - E[y] = F E[y], hence E[y] = 0, since F has no eigenvalue 1 on V_rest;
  - E[a] = −E[a], hence E[a] = 0; E[c] is unrestricted;
  - X = E[l yᵀ] satisfies X = D X Fᵀ. On the c-block X_c(Fᵀ − I) = 0, and on the a-block
    X_a(Fᵀ + I) = 0. F has neither eigenvalue +1 nor −1 on V_rest, so X = 0;
  - the c–a block Y of E[l lᵀ] satisfies Y = −Y, so it vanishes.

  The second moment is therefore the direct sum E[c cᵀ] ⊕ E[a aᵀ] ⊕ C_rest, with C_rest the second
  moment of P_rest x. Only second-moment stationarity is used.

### 3.2 The label-sector J is one J [A]

[C3] (d) places, on the slice through x*(t), the structure x*(t) + y ↦ x*(t) + J_F y. By §3.1 this
is the linear map 𝒥 = id_{L_0} ⊕ J_F on L_0 ⊕ V_rest. Hence:
- The J on every label sector is the same operator, J_F on V_rest. It equals the J of lane 2's
  Proposition 5, since the coisotropic reduction {w = 0}/L_0 is identified with V_rest by the same
  P_rest.
- 𝒥² = id ⊕ (−1) ≠ −1. No complex structure on L_0 ⊕ V_rest that preserves it is tamed: for
  l ∈ L_0, l lies in the radical of ω restricted to L_0 ⊕ V_rest, so ω(Jl, l) = 0 whenever
  Jl ∈ L_0 ⊕ V_rest. The F-slice supplies a complex structure on the fibre V_rest, not on the
  stationary support.
- J, and Σ under the centred reading of §4.2, read the state only through P_rest∗ρ, which is
  F-invariant on V_rest with finite second moments. For them the disintegration of [C3] (c) is not
  consumed. The state's stabilizer, which P2a and P2d read, is not a function of P_rest∗ρ alone
  (§3.4).

### 3.3 Proposition P: a slice-dependent J is possible [A]

Let L be even and a ≠ 0, so that the label sector consists of two slices
S_± = c(1, 1) ± a(1, −1) + V_rest. F maps S_+ to S_−, and so does each unit translation T_j, since
T_j s = −s. Both slices have tangent space V_rest.

**Proposition P.** Consider pairs (J_+, J_−) of complex structures on V_rest such that:
- each is tamed by ω;
- F J_± = J_∓ F;
- T_j J_± = J_∓ T_j for every j.

The solution set contains, besides (J_F, J_F), a one-parameter family (J_t, J_{−t}), t ∈ R, with
J_t ≠ J_F for t ≠ 0. The only pair with J_+ = J_− is (J_F, J_F).

*Choice of momentum.* In d = 3, take k = (π, 0, 0), available for every even L including L = 2:
a(k) = (2/3)(−1 + 1 + 1) = 2/3. In d = 2, take k = (2π/L, 0) for even L ≥ 4. In either case
a(k) ∉ {−2, 0, 2}.

*Proof.*
- **Reduction.** The conditions hold iff J_+ commutes with the slice-preserving group 𝒢_+ and
  J_− = F J_+ F⁻¹. 𝒢_+ is generated by F², the products T_i T_j^{±1}, and T_j⁻¹F.
  - From F J_+ = J_− F and F J_− = J_+ F, J_+ commutes with F².
  - From T_j J_+ = J_− T_j, J_+ commutes with T_j⁻¹F.
  - The converse is direct.

  The group generated by F and the T_j is abelian, so F preserves each joint eigenspace of 𝒢_+.
- **Two eigenspaces.** Take k as above. Since a(k + π) = −a(k), k + π also lies in V_rest. Let P
  be the F-eigenspace for e^{iθ} at momentum k (θ = θ_k), and N the F-eigenspace for
  e^{−i(π−θ)} = −e^{iθ} at momentum k + π, each ≅ C^6.
- **Same character on 𝒢_+.** F² gives e^{2iθ} on both. T_iT_j^{±1} gives e^{i(k_i ± k_j)} on both,
  since the π's cancel modulo 2π. T_j⁻¹F gives e^{−ik_j}e^{iθ} on P and (−e^{−ik_j})(−e^{iθ}) on
  N. So E = P ⊕ N lies in one joint eigenspace E_χ. Moreover χ ≠ χ̄, because e^{2iθ} is not real
  (a(k) ≠ 0, so θ ≠ π/2).
- **The Krein form.** Let h(z, z′) = 2iω(z, z̄′), hermitian on E_χ.
  - h > 0 on P and h < 0 on N, by [L2] Theorem 1's Krein sign applied at k and, conjugated, at
    k + π.
  - P ⊥_h N, because ω(z, z̄′) carries the translation character e^{ik}e^{−i(k+π)} = −1.
  - h is nondegenerate on E_χ, which ω pairs only with E_χ̄. Write E_χ = E ⊕ E^{⊥h}.
- **The family.** In h-orthonormal bases of P and N, set
  S_t = [[cosh t, sinh t], [−sinh t, −cosh t]] ⊗ I_6 on E. On E^{⊥h}, set S = +1 on the
  F-positive part and −1 on the F-negative part.
  - S² = 1, and hS is positive definite: on E it is [[cosh t, sinh t], [sinh t, cosh t]] ⊗ I_6,
    and on E^{⊥h} it is J_F's taming.
  - Define J_t = iS on E_χ, its conjugate on E_χ̄, and J_F on every other joint eigenspace.
  - For x = z + z̄, ω(J_t x, x) = Re h(Sz, z) > 0. So J_t is a tamed complex structure commuting
    with 𝒢_+, and J_t ≠ J_F for t ≠ 0.
  - This is the mechanism of the indefinite-B family of [L2] §2.3.
- **The partner.** F preserves E and h, acts on E as e^{iθ} diag(1, −1), and commutes with S on
  E^{⊥h}. So F J_t F⁻¹ = J_{−t}.
- **The diagonal case.** If J_+ = J_−, then J_+ commutes with F, and [L2] Theorem 1 on V_rest gives
  J_F.
∎

The solution set is larger than this family: other momenta, and rotations within blocks, give
further members.

**Reading.**
- In deviation coordinates the family is a period-two J(t) = J_{(−1)^t t}.
- [C3] (d) asks for a "commuting J" with the deviation dynamics y ↦ Fy. That is H6-Φ read on V_rest
  (link 12, LI), and it excludes the family. H-ZM supplies the same condition automatically,
  because the quotient identifies S_+ with S_−.
- What Proposition P adds is that the label sector alone does not force it. LI is the F-slice's
  form of F-commutation, and R1 depends on it.
- For L odd, or for a = 0, the sector is one F-invariant slice, and Theorem 1 gives J_F with no
  further condition.
- Whether any stated premise selects LI over the family is open (N-2).

### 3.4 The stabilizer reads the joint law [A]

Under the extension R_ext = id on V_null ⊕ R(w) on V_rest (§4.2), Stab(ρ) is the stabilizer of the
joint law of (l, y). It is contained in Stab(P_rest∗ρ), and the inclusion can be strict.

**Witness ρ_S.** Take L ≥ 7 even, so that [A-rec] Proposition A applies on V_rest. Let ν_± be the
centred Gaussians on V_rest with covariances C_0 ± εW, the two components of Proposition A. Let e
be a unit vector of the A_1 block, which is fixed by O. Set a = 0 and

    ρ_S = ½ (δ_{c = e} ⊗ ν_+) + ½ (δ_{c = −e} ⊗ ν_−).

Properties:
- ρ_S is F-stationary, because F fixes c and each ν_± is F-invariant.
- It is translation-invariant and cubic-invariant, and it is supported on L_0 ⊕ V_rest.
- P_rest∗ρ_S is Proposition A's mixture. Its stabilizer contains w_π = e^{iπ P_{T1}}, which swaps
  ν_+ and ν_− ([A-rec] §2.4).
- R_ext(w_π) maps the component (e, ν_+) to (e, ν_−), which is not a component of ρ_S. So
  w_π ∉ Stab(ρ_S), and Stab(ρ_S) ⊊ Stab(P_rest∗ρ_S).

Consequences:
- **P2a.** The inclusion Stab(ρ) ⊆ Stab(Σ_c) still holds, since
  Stab(ρ) ⊆ Stab(P_rest∗ρ) ⊆ Stab(Σ_c).
- **P2d.** The equality Stab(ρ) = Stab(C) reads the label disintegration, so [C3] step (c) is
  consumed there. SMD read on ρ is strictly stronger than SMD read on P_rest∗ρ, which is what the
  H-ZM route needs.
- **Unbroken group.** For the same ρ, the F-slice can give a smaller unbroken group than the H-ZM
  route.
- **Sufficient condition.** If the labels are independent of y, then Stab(ρ) = Stab(P_rest∗ρ) under
  this R_ext.

## 4. The static labels and the custodial action

### 4.1 Lemma L [A]

Let ρ: U(6) → GL(L_0) be a continuous homomorphism commuting with the translations restricted to
L_0. On (c, a), T_j|_{L_0} = diag(I, −I), which equals F|_{L_0}. Then ρ is trivial on SU(6). In
particular, no such ρ restricts on SO(6) ⊂ U(6) to the internal action c ↦ Xc, a ↦ Xa.

*Proof.*
1. ρ commutes with diag(I, −I), so it preserves the c-block and the a-block, each ≅ R^6.
2. SU(6) is compact, so its continuous representation on each block is completely reducible.
3. The complexification of each block is a 6-dimensional complex representation that is
   self-conjugate.
4. The irreducible representations of SU(6) of dimension at most 6 are 1, 6 and 6̄, with 6 ≇ 6̄.
   - A self-conjugate representation containing 6 also contains 6̄, which needs dimension 12.
   - So the complexification is a sum of trivial representations, and each block is trivial for
     SU(6).
5. SO(6) ⊂ SU(6), and its internal action is not trivial.
∎

**Consequences.**
- On the F-slice, the custodial U(6) acts on the static link labels at most through
  det: U(6) → U(1).
- This sharpens [L2] Proposition 3 and its remark that the U(6) "is not a group acting on the
  six-link carrier at k = 0" ([L2] REPORT-r2.md line 275). That statement concerns the symplectic
  commutant on V_0; Lemma L concerns any translation-commuting continuous action on the stationary
  labels.

**The excluded action.** An action that does not commute with the translations can act internally
on the labels: with z = c + ia, z ↦ wz preserves E, and ω restricted to L_0 ⊕ V_rest. But T_j and
F|_{L_0} act on z as complex conjugation, so it mixes the k = 0 and k = π sectors. It is therefore
neither an internal symmetry of the link index nor a symmetry of F, and it lies outside the
readings admitted in §5.

### 4.2 The label exclusion is the covariant reading [A]

**What P2a uses.** P2a ([A-rec] §2.3) uses Φ_n(R(w)x) = wΦ_n(x), which unit A derives from H-PF on
a space where J_F exists. On the F-slice the support is L_0 ⊕ V_rest. On L_0 there is no J_F, so
Φ_n is undefined there, and H-PF does not say how φ extends. Covariance of φ on the labels is
therefore a requirement on the extension, not a premise the ledger already carries.

**Equivalence.** Let R_ext be any extension of R(w) on V_rest by a continuous, translation-commuting
action on L_0 (Lemma L). Let φ be real-linear in x, with φ = Φ_n on V_rest (H-PF on V_rest). Then:
- **(⇒)** If φ is R_ext-covariant on the support, then for l ∈ L_0 and w ∈ SU(6),
  φ(l) = φ(R_ext(w) l) = wφ(l). SU(6) fixes no nonzero vector of C^6, so φ(l) = 0, and
  φ = Φ_n ∘ P_rest.
- **(⇐)** If φ = Φ_n ∘ P_rest, then φ is R_ext-covariant, since P_rest commutes with R_ext and Φ_n
  is covariant on V_rest.

So covariance on the support is equivalent, given Lemma L, to the centred reading
φ = Φ_n ∘ P_rest (N-8). Under it,

    Σ = Σ_c := E[Φ_n(P_rest x) Φ_n(P_rest x)†],

the condensate of the H-ZM route, computed from P_rest∗ρ.

**Another extension is admissible.** The extension φ = ℓ_n(l) + Φ_n(P_rest x) (H-PF_u) is
real-linear and agrees with H-PF on V_rest, but it is not covariant. It defeats P2a (§6). Neither
H-PF nor any stated premise found (§1, W-1) selects between the two extensions. Whether the centred
reading counts as a reading of Σ = ⟨φφ†⟩ that Theorem 5's text admits, or as a further premise
X = "φ = Φ_n ∘ P_rest", is recorded in §8.

**The extension R_ext exists.** It is unique on SU(6). R_ext = id on V_null ⊕ R(w) on V_rest
commutes with F and the translations and preserves ω and E:
- V_null is ω-orthogonal to V_rest;
- L_0 = ker D lies in the radical of E, where D = F − A/2 vanishes on L_0: D(1, 1) = 0 at a = 2,
  and D(1, −1) = 0 at a = −2.

## 5. Q-cons: the consumers in Theorem 5

The consumers are the rows of [A-rec] §2 that carry Proposition 5's output, together with the
layer M rows. The rows that carry it are H6-Φ, P1 and L-NZM, and through them P2a–P2e.

The proof steps are SM:342 [P]:
- P1: "Under H-cust the pre-condensate observer-level kinetic term is invariant under the custodial
  unitary action on the physical link carrier";
- P2: "The unbroken subgroup of a state with condensate $\Sigma$ is its unitary stabilizer";
- P3–P5: the Schur and stabilizer steps.

| Consumer | What it reads | F-slice class | Reading, and reason |
| --- | --- | --- | --- |
| H1, H3, H5, H6-M, P3, P4, P5 (layer M) | nothing ([A-rec] §2.2: abstract ⊗ℂ of SM:362) | NC | — |
| H2, H2a (kinetic clause) | nothing (Proposition 4b, any μ) | NC | — |
| H6-Φ | a complex structure commuting with the update, tamed, on the space the state lives on | S | J_F on the fibre V_rest, commuting with the deviation dynamics (§3.2, with LI, N-2). The reading "a complex structure on the whole stationary support" is OB (§3.2), as it is for every route at μ = 1 on T ([L2] Proposition 3) |
| P1 | a custodial unitary action, leaving the kinetic term invariant, on the physical link carrier | S | Extension reading (N-1): R_ext of §4.2. The internal reading, in which U(6) acts on the static link labels by the same internal action as on every other mode, is OB (Lemma L) |
| P2a, with H-PF | φ(R(w)x) = wφ(x) on the support; Stab(state) ⊆ Stab(Σ) | S | Centred reading (N-8): φ = Φ_n ∘ P_rest. The inclusion holds through Stab(ρ) ⊆ Stab(P_rest∗ρ) ⊆ Stab(Σ_c) (§3.4). The uncentred reading H-PF_u is OB (§6) |
| P2b (C_− = 0) | J-Hermiticity of the state's moment | S | On Σ_c: [L2] Proposition 7 on V_rest with L-SDS, as on the H-ZM route |
| P2c (TPC) | the two-point clause | S | On C_rest, as on V_rest ([A-rec] CE9's range includes V_rest). The state condition is carried, not supplied |
| P2d (SMD) | the state's stabilizer equals its second moment's | S, under SMD read on ρ (N-9) | Stab(ρ) reads the joint law of (l, y) (§3.4). SMD read on the full ρ is strictly stronger than the SMD on P_rest∗ρ that the H-ZM route needs. Equivalently: SMD on P_rest∗ρ together with independence of the labels from y. SMD itself is the rank-1 investigation's question |
| P2e | the stabilizer is a symmetry of the full dynamics | S | R_ext commutes with F on all of V, so [A-rec] Proposition D extends |
| L-NZM | a non-zero-mode condensate at μ = 1 | S | Centred reading (N-8): Σ = Σ_c is supported on V_rest. The macroscopic zero-mode reading of [L2] Proposition 11 cannot enter a covariant Σ, consistent with that proposition's "leaves U(6) unbroken" |

Under the readings N-1, N-2, N-8 and N-9, every consumer is NC or S. P1 is OB under the internal
reading, and P2a is OB under the uncentred reading.

## 6. The uncentred reading: witness ρ_W [A]

Let L ≥ 4, μ = 1 and b = 0. Let ρ_W be the product of two laws:
- **on the labels:** a = 0, and c a centred Gaussian on R^6 with covariance Σ_b σ_b² P_b, the σ_b
  pairwise distinct;
- **on V_rest:** the centred Gaussian with covariance κ G⁻¹ ⊗ I_6, κ > 0, where G⁻¹ is the inverse
  J-metric ([A-rec] §2.4).

ρ_W is F-stationary: F is the identity on c, and G⁻¹ ⊗ I_6 is F-invariant. It is
translation-invariant, and cubic-invariant because Σ_b σ_b² P_b commutes with the link
representation. It has finite second moments and is supported on L_0 ⊕ V_rest.

- **Centred (covariant) reading.** Σ_c = 2γκ I_6 (the form of [L2] Proposition 8). The block values
  coincide, so H5 fails and Theorem 5 does not apply. This is not a defect.
- **Uncentred reading** (H-PF_u: φ = ℓ_n(l) + Φ_n(P_rest x), the labels entering as a real part).
  - By §3.1 the cross moments vanish, so Σ_u = Σ_b (2γκ + σ_b²) P_b.
  - Its block values are distinct, and its matrix stabilizer is U(3)×U(2)×U(1).
  - But R_ext(w) preserves ρ_W for every w. Under any translation-commuting extension SU(6) acts
    trivially on the labels (Lemma L), so SU(6) ⊆ Stab(ρ_W) ⊄ U(3)×U(2)×U(1).
  - P2a fails. The distinct block values come entirely from the static labels, as in [L2]
    Proposition 11.

So the uncentred reading is OB for P2a. A Theorem 5 conclusion drawn from it would be the
witness → theorem error that the claim/evidence rules guard against.

## 7. Controls

| Id | Result | Status |
| --- | --- | --- |
| C+1 | At abs(μ) < 1 there is no null sector: L_0 = 0, P_rest = I, R_ext = R(w), and §4.2 reduces to H-PF. Every consumer takes [A-rec]'s class without H-ZM: H6-Φ, P1 and P2e Dv via J_F; P2a Dv given H-PF; P2b–P2d carry L-SDS, TPC and SMD | green |
| C+2 | Under H-ZM the reduced space is {w = 0}/L_0 ≅ V_rest by P_rest, φ = Φ_n([x]) = Φ_n(P_rest x), and Σ is supported off the null sector. Every consumer that [A-rec] marks as carrying H-ZM is supplied, which reproduces [L2] Proposition 5 | green |
| C−1 | The uncentred reading was tested against P2a with ρ_W (§6) and classified OB, not S | green |
| C−2 | Rejected as H6-Φ: 𝒥 = id ⊕ J_F (𝒥² ≠ −1); any J preserving L_0 ⊕ V_rest (untamed, §3.2); the site-local J_0 and site-local structures ([A-rec] Lemma 1′, [L2] Proposition 2). The pair family J_t (§3.3) is tamed and F-intertwining but violates LI; it is recorded, not accepted as C3's J | green |
| C−3 | With b_A1 ≠ 0 at μ = 1 no stationary law exists ([L2] Proposition 4(b)), so the F-slice is empty and supplies nothing | green |
| C−4 | The SM quotes (SM:136, 222, 232, 240, 290, 292, 298, 312, 316, 340, 342, 344, 362) and the record quotes (L2 line 275 and its summary row; A-rec rows H6-Φ and L-NZM and §2.3; C3 §5.3 (d)) were re-extracted at [P] by fixed-string match | green |
| C−5 (added in r2) | A real-linear extension of Φ_n to the support that is not R_ext-covariant must not be classified S for P2a. H-PF_u is such an extension, and it is classified OB (§6) | green |

**Power.** C+1, C+2 and C−3 cannot fail on §4.2's step:
- at C+1, L_0 = 0;
- at C+2, the quotient already gives Φ_n ∘ P_rest;
- C−3 re-cites [L2] Proposition 4(b) rather than testing the method.

No control decides whether the label exclusion is derived or assumed. The review settled that it is
a reading (§4.2), and R1 is conditioned on it (N-8). C−1 and C−5 are the non-vacuous
countercontrols for P2a.

## 8. Outcome against the decision rule (PLAN §4)

Under the most favourable admitted readings every consumer is NC or S (§5), and every control is
green. The rule prints:

**R1, route around H-ZM.** For Theorem 5's consumers on carrier T at the massless point, H-ZM can be
replaced by the F-slice under four reading dependences:
- **N-1:** the extension reading of the custodial action in SM:342;
- **N-2:** LI, the F-slice form of F-commutation;
- **N-8:** the centred reading of φ on the support;
- **N-9:** SMD read on the full ρ.

It is conditional on LIN, LIFT, b_A1 = 0, a stationary law with finite second moments, and lane 2's
Theorem 1.

**Alternative classification (from the review).** If the centred reading N-8 is taken as a premise
X = "φ = Φ_n ∘ P_rest" rather than as a reading of Σ = ⟨φφ†⟩ that Theorem 5's text admits, then
P2a and L-NZM are S|X, the outcome is R2, and stopping condition 3 applies. Which of the two is
right is a question about what Theorem 5's text admits. SM:340 does not say whether Σ is computed
from the full observer-level field or from a field blind to the static background (§1, W-1). The
choice is the owner's (N-8).

**Directional statements (§A.34):**
- **H-ZM route ⇒ F-slice inputs, for J and Σ.** Under H-ZM, every input of §5 is supplied with the
  same J and, under the centred reading, the same Σ (C+2). This does not give the same stabilizer.
  On the F-slice the state's stabilizer reads the joint law of (l, y), and it can be strictly
  smaller (§3.4).
- **The F-slice route does not use H-ZM.** It requires only that the field φ, not every observable,
  be blind to the labels (N-8). The labels stay registered and conserved, as Main's specified
  partitions require ([C3] §4.1). No witness separating H-ZM from the F-slice premises is claimed:
  N-8 imposes H-ZM's content restricted to φ.

**Scope:**
- carrier T only; carrier Z (H-top) is not addressed;
- Theorem 5 only. Other consumers of H-ZM or of the static labels are not traced: the SM:811
  energy, and the charged matter action and amplitude-scale gauge of SM:344;
- the linear lift only; H-PF-int is not addressed;
- no premise is removed from Theorem 5. H-PF, L-SDS, TPC and SMD remain carried and unsourced, and
  SMD is needed on ρ. LIN, LIFT and the SM:232 bridge remain conditions;
- under the internal reading of P1, or the uncentred reading of φ, the F-slice is OB.

Nothing is proposed for the manuscripts. Narrowing [A-rec]'s row H6-Φ ("at μ = 1 V_rest / K: H-ZM /
H-top (unit C)") or its row L-NZM ("depends on H-ZM (unit C)") on T would change records outside
this unit, and so would changing lane 2's PRESERVATION statement of what Theorem 5's use of J needs.
These are listed for routing only (§11).

## 9. Passes, classification and productivity

- **Pass 1 (Q-lift; Q-J).** §2, §3.1 and §3.2. ELABORATING. J and Σ do not consume step (c).
- **Pass 2 (skepticism on the uniqueness in C3 (d)).** Proposition P.
- **Pass 3 (consumers; P1 and P2a on the labels).** Lemma L, §4.2 and witness ρ_W.
- **Pass 4 (skepticism on the favourable R1).** It examined three things:
  - the non-translation-commuting action z ↦ wz (§4.1);
  - the internal reading of P1;
  - whether §4.2 used a premise.

  No NEW finding came of it, and r1 recorded only N-1.
- **Pass 5 (r2, applying the review).**
  - §4.2 is a reading, equivalent given Lemma L to the covariant reading (N-8).
  - The stabilizer reads the joint law (§3.4, ρ_S), so P2d needs SMD on ρ (N-9).
  - The directional statement is restated.

  ELABORATING.

Stopping condition 1 holds: the rule resolved with all controls green, under the readings named in
§8.

**Productivity (PLAN §7): gem, borderline.** The unit yields facts strictly stronger than C3's O3:
- the F-slice's J is Proposition 5's J;
- a slice-dependent J is possible unless LI is imposed (Proposition P);
- Lemma L excludes an internal action on the static labels;
- Theorem 5's null-sector treatment on T reduces to four named readings, one of which (N-9) is
  stronger on the F-slice than on the H-ZM route.

These facts constrain how H-ZM may be replaced. The equivalence of §4.2 locates exactly what the
replacement requires of φ.

| Class | Findings |
| --- | --- |
| NEW (borderline) | Proposition P (a slice-dependent J is possible); §3.4 (the stabilizer reads the joint law; SMD on ρ is strictly stronger) |
| POSITIVE | §3.1–§3.2: the centring is P_rest; there is one J; J and Σ do not consume step (c); the moment split needs no disintegration |
| ELABORATING | Lemma L; §4.2 (the label exclusion is equivalent, given Lemma L, to the covariant reading); witness ρ_W |
| CONFIRMING | C+2 (Proposition 5 reproduced) |

Correctness bands unchanged: consistency-axis work (§A.23).

## 10. Open nodes

- **N-1 (owner reading).** Must "the custodial unitary action on the physical link carrier"
  (SM:342) act on the static link labels by the internal action? If so, the F-slice is OB by
  Lemma L and only the H-ZM route remains. Or does it admit a translation-commuting extension that
  acts trivially on the labels on SU(6), which gives R1? Related to [A-rec] O5.
- **N-2.** Does any stated premise select the label-independent J (LI) over the period-two pair
  family of Proposition P on staggered label sectors (L even, a ≠ 0)? Not searched beyond the
  inputs.
- **N-3.** Carrier Z. The F-slice adds nothing there, and H-top stands ([L2] Proposition 6).
- **N-4.** Other consumers of H-ZM, or of the retained static labels, outside Theorem 5 are not
  traced: the SM:811 energy shells, the SM:344 reduction, and the amplitude-scale gauge of [C3] O1.
- **N-5.** Inherited and carried:
  - LIN, LIFT and the SM:232 bridge;
  - L-SDS (SM:290, SM:298);
  - lane 2's Theorem 1 (model-reviewed);
  - TPC, SMD and H-PF itself, all unsourced ([A-rec] §5, §9 O2).
- **N-6.** The nonlinear lift (H-PF-int). The F-slice relies on the linear F throughout.
- **N-7.** Independent review of r2, as the authorization requires before any use. In particular:
  §3.4, §4.2's equivalence, and the momentum choice in Proposition P.
- **N-8 (owner reading; added in r2).** Is the condensate's field φ the centred one,
  φ = Φ_n ∘ P_rest, on the stationary support? Equivalently, given Lemma L, is φ R_ext-covariant on
  the labels? If this is a reading Theorem 5 admits, the outcome is R1. If it is a premise, the
  outcome is R2 (§8). No stated premise found selects it (§1, W-1).
- **N-9 (added in r2).** SMD read on the full ρ, including the joint law of labels and
  fluctuations. Alternatively, SMD on P_rest∗ρ together with independence of the labels from y.
  Both are stronger than the SMD of the H-ZM route (§3.4). This is for the rank-1 investigation's
  attention, not investigated here.

## 11. Findings for routing (listed, not edited)

1. **[A-rec] rows H6-Φ and L-NZM.** On T at μ = 1, the F-slice supplies these inputs without H-ZM,
   under the readings N-1, N-2 and N-8. P2d then needs SMD read on ρ (N-9) (§5, §8). Route: #1217.
2. **[C3] §5.3 (d), "the unique tamed commuting J on every label sector".** Unique under LI, which
   is how C3 builds it. Without LI, the pair level admits the family of Proposition P. A mutable
   record citing C3, such as its PRESERVATION.md, could carry this. Route: #1217.
3. **[C3] §5.3 pressure test, "step (c) is [W]".** J and Σ do not consume step (c). The state's
   stabilizer does, in P2a and P2d (§3.2, §3.4). Route: #1217.
4. **[L2] Proposition 5 and PRESERVATION §2** ("exclusion needs the named hypothesis H-ZM"). True as
   stated. Theorem 5's use of J on T does not need the exclusion, under the readings of §8. Route:
   #1217.

## 12. References not on `main` (§A.42 item 8)

| Reference | Classification |
| --- | --- |
| #1169 comments 7199704501, 7200549806, 7191949320 | provenance: work package, authorization and question source; no result uses them |
| PR #1611 comment 7201020516 (review of r1) | provenance: evidence of review; no result uses it |
| commits `7e853501` (PLAN.md), `5073afda` (r1) and the commit adding r2 | support on `main` once merged without squash, for the preregistration order and the r1 text; not before |
| C3, L2 and A-rec records, and lane 2 PRESERVATION.md | support on `main` at [P] |

Support off `main`: none.

## 13. Verification status and remediation (§A.46 item 4)

**This table authorizes no work.**

| Claim | Status | Missing | Issue | What would resolve it |
| --- | --- | --- | --- | --- |
| §3.1–§3.2 | reviewed once (r1 review: correct), as a model review | independent non-model verification | #1217 | recorded review |
| Proposition P | reviewed once (correct), as a model review; the momentum choice was added in r2 | delta review; an exact finite control on a small even torus (needs authorization) | #1217 | review; authorized control |
| §3.4 and ρ_S | new in r2, unreviewed | review | #1217 | review |
| Lemma L | reviewed once (correct); complete reducibility and the dimension-12 step added in r2 | delta review | #1217 | review |
| §4.2 (the label exclusion equivalent, given Lemma L, to the covariant reading) | the mechanics were reviewed (correct); restated in r2 as an equivalence | delta review | #1217 | review |
| Witness ρ_W | reviewed once (correct) | — | #1217 | — |
| R1 outcome | conditional on four reading dependences: N-1, N-2 (LI), N-8 and N-9 (SMD on ρ), and on N-5. Under the alternative classification of N-8 the outcome is R2 | owner readings N-1 and N-8; delta review | #1217, #1049 | owner decisions on N-1 and N-8; review |
| W-1 search | keyword-based, not exhaustive | an exhaustive search for a stated centring of Σ | #1217 | a recorded exhaustive search |
