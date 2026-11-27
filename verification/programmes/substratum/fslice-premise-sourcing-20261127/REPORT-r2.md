# FSLICE-PS-1: can N-2, N-8 and N-9 be sourced from native OI dynamics? Report, r2

**WIP / UNVERIFIED. Model-written research record, paper-only, pending a delta review. No premise
is adopted, weakened or changed (§A.29, §A.50 item 6). Nothing is proposed for the manuscripts.**

**Revision r2.** This revision applies findings 1–11 of the independent review of r1. The review is
PR #1624 comment 7209242260 (posted from the account amaybaum, created 2026-11-27T03:45:08Z; verdict
REVISE, minor to moderate, with no class changes). r1 is `REPORT.md` at
`b3500e3194e4db04372c6ed2bf9b4ab4962c3dc8` and is kept unchanged. `CHANGES-r2.md` maps each finding
to its change.

**Revision r3** edits this file in place. It applies the nits D1–D4 of the delta review of r2, which
accepted r2 with nits, as the coordinator directed:
- D1: ρ_T′ specified (R9.6);
- D2: the χ-orbit condition in R2.2(a), and its consequence in O-1a;
- D3: wording in §2.2 step 3;
- D4: the §4.3 even-L entry.

Nothing else changes.

- **Plan:** `PLAN.md` in this directory, commit `158f4155c9b80f220bb6543b11e04497c3ec0328`,
  committed alone before r1. The rule is applied per carrier (§0, §4.3). That is a refinement of
  PLAN §4, which has no carrier axis, and is labelled where it is used.
- **Accountable Issue:** #1217; programme #1169. Work package, authorization and Goal link: as in
  PLAN.md (WP-2; #1169 comment 7208939261, author amaybaum, created 2026-11-27T03:22:49Z).
- **Pinned main commit [P]:** `13c05b4fe666c2e128eed1213874be9b8208982d`.
- **Labels:**
  - [A] exact hand algebra here;
  - [W] reasoning here;
  - [P] text quoted at [P];
  - [FS], [L2], [A-rec], [C3], [SMD-SRC]: results of the input records of PLAN §1. These are
    model-reviewed paper derivations, used as named conditional inputs (§A.46 item 7).
- **Status words:** proved, conditional, posited, open (PLAN §8).
- **Evidence layer:** mathematical derivation on paper. No computation was run, and no Lean was
  built.

## 0. Summary

| Question | Class (PLAN §4) | Decisive argument |
| --- | --- | --- |
| Q2: N-2, label-independent J (LI) | **R**: reduces to H-PF with its positive-frequency clause, referred to the update F on V_rest, which is H-PF's stated domain. **I** if the clause is dropped, which weakens H-PF and is not a reading of it (O-1a) | H-PF names J_F = D(−D²)^(−1/2) of the update F ([L2] §2.1, §5, §6). On V_rest J_F is one operator, independent of the label. Any J that is a function of the slice-preserving group is untamed (§2.2). Without the clause, Proposition P's family meets every remaining premise |
| Q8: N-8, centred reading φ = Φ_n ∘ P_rest | **R**: equivalent, given φ = Φ_n on V_rest and real-linearity, to H-PF's positive-frequency clause extended to the stationary support. That extension is not in H-PF as stated (O-1b). **I** under the formula-only reading (ρ_W) | Lemma PF [A], both directions (§3.2) |
| Q9: N-9, SMD on the full law | Rule applied per carrier, refinement labelled:<br>• **Even L ≥ 2:** I under both readings of the state (ρ_P, all even L), unless the state is also required to be R_π-invariant (R9.6).<br>• **Odd L ≥ 7:** I without the label-sector reading (ρ_T); R (to SMD on the fluctuation law) under it.<br>• **Odd L < 7:** O without the label-sector reading (no witness); R under it | ρ_T (L ≥ 7, any parity) and ρ_P (every even L ≥ 2, [A]) meet every stated and carried premise, N-2, N-8 and SMD on P_rest∗ρ, and violate N-9 (§4) |

**Routes closed or conditional for N-9 (§4):**
- Main's measure selection gives a custodially scalar state, on which Theorem 5 is vacuous.
- Extremality makes the labels deterministic, but by [A-rec] Proposition B no extremal state on T
  realizes Theorem 5's conclusion.
- Joint Gaussianity would give N-9 [A], but it is open and stronger than SMD.
- R_π-invariance, together with the label-sector reading, would give N-9 on even L [A], but it is
  not stated.

**Outcome against the rule.**
- No N_k is class D: none is derived from native OI dynamics.
- At least one N_k remains an independent premise. N-9 is class I under every admitted reading on
  carriers with even L, for states not required to be R_π-invariant. On odd L ≥ 7 it is class I
  without the label-sector reading.
- On odd L the rule falls to its third branch: each class is reported with the readings that decide
  it.
- Under the readings O-1a and O-1b, N-2 and N-8 are not additional to the carried bridge premise
  H-PF. H-PF itself stays open.
- **One route needs a premise outside the stated set.** Route R2.2(b) derives LI from naturality
  under the whole linear commutant of F, which is not stated. Under stopping condition 3 it is
  recorded as a new premise, NAT-C, and not adopted.

All controls are green (§5).

**What it would change.** If the readings O-1a and O-1b were both accepted, the candidate-premise
set of F-slice R2 would shrink from {N-2, N-8, N-9} to {N-9}. N-1 and H-PF would remain. This is a
finding for the owner; no status is changed.

## 1. Setting and carried conditions

The setting is that of [FS]:
- the carrier is T = (Z/L)^d with d = 3, at αμ = 1/d, M = μI_6, b_A1 = 0;
- V = V_0 ⊕ V_π ⊕ V_rest, with V_π present for even L;
- the stationary support is L_0 ⊕ V_rest;
- P_rest is the spectral projection onto V_rest, and J_F is defined on V_rest;
- Φ_n(y) = ℓ_n(y) − iℓ_n(J_F y);
- R_ext = id on V_null ⊕ R(w) on V_rest. This is N-1's extension reading, a candidate reading
  under the owner's ruling.

**Carried conditions C*:** LIN, LIFT, b_A1 = 0, L-SDS, lane 2's Theorem 1, H-link, H-cust, H5,
H-PF, TPC, and SMD on P_rest∗ρ. Their status words:
- LIN is posited (A5).
- LIFT and the SM:232 bridge are open.
- Lane 2's Theorem 1 is proved on paper, conditional on LIN and LIFT.
- H-link, H-cust's condensate clause, H5, H-PF, L-SDS, TPC and SMD are open: they are not stated as
  results in the papers ([A-rec] §2, §5).

The state is "a hypothesis on the solution rather than a consequence of the dynamics" (SM:136 [P]).

**The owner's ruling** framing the question: N-2, N-8 and N-9 are "additional candidate premises,
not established consequences" (#1169 comment 7202075726, item 4, quoted on `main` in [FS]
PRESERVATION.md §1).

## 2. Q2: N-2, label independence

### 2.1 Routes from the stated structure

**R2.1, the native structure.** [FS] Proposition P gives a one-parameter family (J_t, J_{−t}) of
tamed complex structures on the two slices of a staggered label sector. The family is intertwined by
F and the translations. Neither the stated premises nor taming exclude it (countercontrol N-a).

**R2.2, naturality under symmetries of F.** Two parts.

**(a) The stated symmetry types do not force LI [A, W].** The stated symmetry types are F, the
translations, the cubic group O and the custodial action.
- F and the translations: Proposition P's family is intertwined by them.
- The custodial action: the slice-dependent actions R_±(w) = I⊗X + J_±⊗Y form a group action on the
  support that commutes with F and the translations, since F J_± = J_∓ F.
- O: on a carrier where O acts freely on the orbit of a chosen momentum k (generic k_0 with L ≥ 7),
  and the O-orbit of χ is disjoint from the O-orbit of χ̄, S_t can be transported along the orbit
  to an O-equivariant family [W].
- The staggered shift τ_c is not a symmetry of F: τ_c⁻¹Fτ_c x = Fx − 2cv ([C3] §5.2).
- The constant shift σ_c is a symmetry, but it only relates c-sectors. Each of those is a single
  F-invariant slice, on which J is already J_F.

**(b) The whole linear commutant forces LI [A].** Let R_π = −id on V_π and id on V_0 ⊕ V_rest. It:
- commutes with F, the translations, O and R_ext;
- preserves ω and E, because V_π is ω- and E-orthogonal to the other spectral blocks;
- maps S_+ to S_− while fixing V_rest pointwise.

So naturality of J under R_π gives J_− = R_π J_+ R_π⁻¹ = J_+, which is LI. R_π = 1 − 2P_π is an
element of the linear commutant of F. It is not a point, translation or internal symmetry, and it is
nonlocal. No stated premise requires J to be natural under the whole linear commutant of F. ([L2]
Theorem 1 derives commutation for J_F on V_rest; it does not require it of a structure on the label
sectors.) This route is therefore not class D. Under stopping condition 3 its requirement is
recorded as a new premise:

> **NAT-C:** the complex structure on the stationary support is natural under the linear commutant
> of F (or at least under R_π).

NAT-C is not adopted.

**R2.3, the custodial covariance.** P2a's covariance Φ^J(R(w)x) = wΦ^J(x), with
R(w) = I⊗X + K⊗Y, forces K = J [A]. Comparing both sides gives ℓ_n(Kx) = ℓ_n(Jx) and
ℓ_n(JKx) = −ℓ_n(x) for every n. P2a is a step Theorem 5 needs (countercontrol N-d), so it supports
no class D or R.

**Class D:** none.

### 2.2 Reduction to H-PF [A]

H-PF is "SM's φ is the J-linear positive-frequency field Φ of the real lift" ([L2] §5). [L2]
identifies that J as "the positive-frequency J_F = D(−D²)^(−1/2)" (§6 item 1): +i on the
eigenvectors of F with eigenvalue e^{iθ}, θ ∈ (0, π), and −i on their conjugates (§2.1).

1. **J_F does not depend on the label.** On the F-slice the deviation dynamics on V_rest is F for
   every label ([FS] §3.1). So D = (F − F⁻¹)/2 on V_rest, and J_F with it, is one operator for every
   label.
2. **The family is not J_F.** On E = P ⊕ N ([FS] §3.3), J_t = iS_t with S_t ≠ diag(1, −1) for
   t ≠ 0. So J_t ≠ J_F, and J_F is the unique F-positive-frequency structure.
3. **No slice-preserving dynamics gives a tamed structure.** Let J be any structure that is a
   function of the slice-preserving group 𝒢_+: an element of the algebra that 𝒢_+ generates,
   with J² = −1. Then J acts as a scalar ±i on each joint eigenspace E_χ. E_χ contains P, where
   h(z, z) = 2iω(z, z̄) > 0, and N, where h < 0 ([L2] Theorem 1's Krein sign). Since
   ω(Jx, x) = Re h(Sz, z) for x = z + z̄, the scalar fails taming on P or on N. So no
   positive-frequency structure of any slice-preserving dynamics (F², T_j⁻¹F, or any other element
   of 𝒢_+) is tamed. Every tamed positive-frequency reading refers to F and gives J_F.
4. **The carrier's complex structure.** H-PF identifies the carrier's complex structure (H6-M) with
   the J of φ on phase space: that is the meaning of "J-linear". So the J of H6-Φ is J_F, and LI
   holds. P2a's covariance is not used.

**Direction (§A.34):** H-PF, with its clause referred to F on V_rest, implies N-2. The converse is
not claimed.

**If the clause is dropped,** so that φ is merely "J-linear for a tamed J commuting with the
dynamics on each slice", Proposition P's family meets every remaining premise, and N-2 is class I.
That is a weakening of H-PF, not a reading of it.

**Class of Q2:** R (H-PF, positive-frequency clause on V_rest); I without the clause.

## 3. Q8: N-8, the centred reading

### 3.1 Routes from the stated structure

- **R8.1, the native interface.** At Main's specified partitions the observer registers site
  values, which contain the labels ([C3] §4.1). Theorem 5's φ is not the registered real field. It
  is fixed only by the bridge H-PF, which "does not say how φ extends" to the labels ([FS] §4.2).
  Class D: none.
- **R8.2, the amplitude-scale gauge** (SM:96; Substratum:270–272, "Status (open)" [P]). If its
  translation clause were physical, a physical φ would be invariant under x ↦ x + c(1, 1)𝟙, so it
  would vanish on the constant labels [A]. The warrant is open, and SM:811 names the
  additive-automorphism group, which excludes translations ([C3] O1). The route supplies nothing
  for the staggered labels, since τ_c is neither a relabelling nor a symmetry of F ([C3] §5.2). It
  is conditional and partial.

### 3.2 Lemma PF and the equivalence [A]

**Lemma PF.** Let φ be real-linear on L_0 ⊕ V_rest, with φ = Φ_n on V_rest.

- **(⇒)** If, along every trajectory x(t) = F^t x of the support, t ↦ φ(x(t)) has Bohr spectrum in
  the open arc {e^{iθ} : θ ∈ (0, π)}, then φ vanishes on L_0, and φ = Φ_n ∘ P_rest.
- **(⇐)** If φ = Φ_n ∘ P_rest, then along every trajectory φ(x(t)) = Φ_n(F^t y) = 2ℓ_n(F^tΠ_+y) has
  Bohr spectrum in that arc.

*Proof of (⇒).* The support contains the trajectories with y = 0, namely
l(t) = c(1, 1)𝟙 + (−1)^t a(1, −1)s. Along them φ(l(t)) = φ_c + (−1)^t φ_a, whose spectrum lies in
{1, −1}. So φ_c = φ_a = 0.

*Proof of (⇐).* Π_+ is the Riesz projection of F onto the eigenvalues e^{iθ}, θ ∈ (0, π). For real
y, y = y_+ + ȳ_+ and J_F y = iy_+ − iȳ_+, so Φ_n(y) = 2ℓ_n(y_+), and F^tΠ_+ has only those
eigenvalues. Π_+ annihilates V_null, whose spectrum is {±1}.
∎

The arc condition is stated in the convention of [L2] §2.1. The mirror arc would be inconsistent
with φ = Φ_n on V_rest unless Φ_n = 0, so it is not included.

So, given real-linearity and φ = Φ_n on V_rest: **N-8 holds if and only if H-PF's
positive-frequency clause holds along the trajectories of the stationary support.** Each direction
is proved above (§A.34).

**Why the trajectory reading is offered.** The positive-frequency part of a real field is defined
spectrally on all of phase space: 2ℓ_n ∘ Π_+ equals Φ_n ∘ P_rest on V. This makes the trajectory
form the natural extension of H-PF's clause to the labels. It is an extension, not a restatement:
[FS] §4.2 records that H-PF does not fix φ on L_0.

### 3.3 The formula reading (countercontrol N-b)

- **H-PF_u.** The formula ℓ_n(x) − iℓ_n(Jx), with J defined on V_rest only, extends most simply as
  ℓ_n(l) + Φ_n(y), which is H-PF_u ([FS] §6). Its label term c + (−1)^t s_n a has frequencies 0 and
  π [A], so H-PF_u fails the extended clause.
- **The 𝒥 extension.** The extension through 𝒥 = id ⊕ J_F gives (1 − i)ℓ_n(l) + Φ_n(y), which
  fails in the same way [A].
- **The formula-only reading.** If H-PF is read as the formula on V_rest with no clause on L_0,
  H-PF_u is admissible. Witness ρ_W ([FS] §6) then meets every stated and carried premise and
  violates N-8, which is class I.

**Class of Q8:** R (equivalent to the clause extended to the support, O-1b); I under the
formula-only reading.

## 4. Q9: N-9, SMD on the full law

### 4.1 Routes

- **R9.1, measure selection** (Main:60 [P]: "selection among orbits is fixed by maximal entropy
  compatible with the observer's records"). Under Proposition 4b's hypotheses the selected measure's
  observer image has scalar Σ_n ([A-rec] Proposition C, model-reviewed per [A-rec]
  PRESERVATION.md). So H5 fails, and Theorem 5 is vacuous on that state. The route does not source
  N-9.
- **R9.2, the records fix the labels: the label-sector reading** [A].
  - **The labels are registrable.** One visible site's itinerary determines the labels
    asymptotically:
    - c = lim_T (1/T) Σ_{t<T} u_n(t);
    - a = lim_T (1/T) Σ_{t<T} (−1)^t s_n u_n(t).

    This holds because neither F nor −F has eigenvalue 1 on V_rest. It is consistent with Main:44,
    since a single visible site suffices.
  - **The reading.** Read Theorem 5's state as a label sector (c, {±a}) fixed by the records.
    Conditioning on F-invariant functions preserves F-invariance.
  - **Sectors with a = 0.** These include every sector on odd L. The labels are deterministic, so
    under R_ext Stab(ρ) = Stab(P_rest∗ρ) and Stab(C) = Stab(C_rest). N-9 is then equivalent to SMD
    on the sector's fluctuation law: class R.
  - **Sectors with a ≠ 0.** The slice (the sign of a) remains random within the sector, and ρ_P
    (§4.2) shows the residual dependence. Conditioning on the slice as well gives a law invariant
    under F² but not F, which fails L-SDS as stated.
- **R9.3, extremality** (countercontrol N-e) [A].
  - An ergodic ρ for the group generated by F and the translations has c and {±a} almost surely
    constant, because they are invariant functions.
  - P_rest∗ρ is ergodic too, being a factor.
  - By [A-rec] Proposition B, the identity component of Stab(P_rest∗ρ) contains U(3)×U(2)×U(1) only
    if the T_1 and E blocks of Σ_c vanish. Since Stab(ρ) ⊆ Stab(P_rest∗ρ), no extremal state
    realizes the conclusion with distinct block values.
  - This is conditional on Proposition B (model-reviewed per [A-rec] PRESERVATION.md).
- **R9.4, joint Gaussianity** [A].
  - A jointly Gaussian stationary ρ has vanishing label–fluctuation cross moments ([FS] §3.1), so
    its labels are independent of y, and N-9 follows with SMD.
  - Joint Gaussianity is open: SM:290 [P] records "the stationary law and Gaussian limit of the
    realized scalar dynamics" as open. It is stronger than SMD.
  - [SMD-SRC]'s Gaussianity theorem holds on Z with 0 < abs(μ) < 1, where there are no labels.
  - This is a conditional source only.
- **R9.5, label–fluctuation independence.** It is sufficient ([FS] §3.4), and open.
- **R9.6, invariance under the label reflections** [A].
  - R_π (−id on V_π, §2.1) maps (a, y) to (−a, y), and R_0 (−id on V_0, which commutes with F) maps
    (c, y) to (−c, y). Invariance of the state under either is not stated, so this route is not
    class D.
  - **R_π with the label-sector reading.** Write a staggered sector as ½δ_{+a} ⊗ ν_+ +
    ½δ_{−a} ⊗ ν_−. R_π-invariance gives ν_+ = ν_−, so y is independent of the sign of a, and N-9
    reduces to SMD on the fluctuation law (class R) on every sector on even L. Under it, ρ_P's class
    I would become class R. ρ_P is not R_π-invariant, because R_π exchanges ν|_S and ν|_{S^c}
    between the two labels.
  - **R_0.** ρ_T, with a = 0, is R_π-invariant but not R_0-invariant. R_0-invariance does not
    rescue N-9. The variant ρ_T′ (L ≥ 7) uses the set S = {q > m} of ρ_T. With a = 0 and e ∈ A_1, it gives
    weight ¼ to each of (c = e, 2ν|_S), (c = −e, 2ν|_S), (c = 2e, 2ν|_{S^c}) and (c = −2e, 2ν|_{S^c}). It
    is R_0-invariant, F-stationary, translation-invariant and cubic-invariant. It has P_rest∗ρ_T′ = ν and still excludes the T_1
    phase from its stabilizer, by the ray argument of [FS] §3.4.

### 4.2 Witnesses (countercontrol N-c)

**ρ_T** ([FS] §3.4, model-reviewed for even L): constant labels c = ±e (e ∈ A_1), a = 0, with
conditionals 2ν|_S and 2ν|_{S^c}. The extension to odd L ≥ 7 is new here [A]:
- on odd L there is no V_π, so a = 0 automatically;
- [A-rec] Proposition A supplies a generic k_0 for every L ≥ 7, for example 2π(1, 2, 3)/7 on L = 7;
- F has neither eigenvalue +1 nor −1 on V_rest.

**ρ_P** [A]: a single label sector with a ≠ 0, for every even L ≥ 2.
- **Data.** c = 0, a ∈ {±e′} with e′ ∈ A_1, and ν = N(0, C_0), with C_0 = Σ_b κ_b G⁻¹ ⊗ P_b and the
  κ_b distinct.
- **The quadratic form.** Pick any k_0 ∉ {0, π}. On even L, π − k_0 is a lattice momentum, and
  a(k_0) ∉ {±2} holds automatically, since a = ±2 only at 0 and π. Let z_k(y) ∈ C^6 be the
  F-positive Fourier component of y at k, in the natural O-equivariant normalisation, and set

      q_2(y) = Re Σ_{h∈O} z_{hk_0}(y)ᵀ z_{π−hk_0}(y),

  a bilinear (not sesquilinear) pairing. It has three properties:
  - **F-odd:** θ_{π−k} = π − θ_k, so the F-phases multiply to −1.
  - **T_j-odd:** the translation characters multiply to e^{ik_j}e^{i(π−k_j)} = −1.
  - **O-invariant:** since hπ ≡ π and zᵀz′ is invariant under the real link representation.

  q_2 is real, nonzero and indefinite.
- **The law.** Let S = {q_2 > 0}. Then FS = T_jS = S^c up to a null set, hS = S, ν(S) = ½ and S = −S.
  Define

      ρ_P = ½ δ_{a=e′} ⊗ 2ν|_S + ½ δ_{a=−e′} ⊗ 2ν|_{S^c}.

  F, the translations and O map the component (e′, ν|_S) to (−e′, ν|_{S^c}), so ρ_P is stationary
  and invariant. P_rest∗ρ_P = ν, so SMD holds on the fluctuation law. The cross moments vanish
  because S = −S, and C = e′e′ᵀ ⊕ C_0.
- **The stabilizer test.** Take φ = 2π/3 and w_φ = e^{iφP_T1}.
  - w_φ ∈ SU(6), since det w_φ = e^{3iφ} = 1. So by [FS] Lemma L it acts trivially on the labels
    under every translation-commuting extension. It lies in Stab(C) = Stab(C_0), and
    e^{2iφ} ≠ 1.
  - R(w_φ) acts on z_k as w_φ, so q_2′ = q_2 ∘ R(w_φ)⁻¹ multiplies the T_1 part of the pairing by
    e^{−2iφ}.
- **Test points, valid for every k_0 ∉ {0, π}.**
  - Let y_0 have positive-frequency components only at k_0 and π − k_0, in the T_1 block, with
    z_{k_0}ᵀz_{π−k_0} = e^{iψ}.
  - A term h of q_2 is nonzero on y_0 only if hk_0 ∈ {k_0, π − k_0}.
  - Every such term equals z_{k_0}ᵀz_{π−k_0}, because the pairing is symmetric. This covers
    2k_0 ≡ π as well, where the term is zᵀz.
  - So q_2(y_0) = N cos ψ and q_2′(y_0) = N cos(ψ − 2φ), with N ≥ 1.
  - Choose cos ψ > 0 > cos(ψ − 2φ). A neighbourhood of y_0 of positive ν-measure then lies in
    S ∖ R(w_φ)S.
  - For y_1 with E-block components and zᵀz′ = 1, q_2(y_1) = q_2′(y_1) = N > 0, so a neighbourhood
    lies in S ∩ R(w_φ)S.
  - Hence R(w_φ)S is neither S nor S^c up to a null set, and w_φ ∉ Stab(ρ_P).
- **N-9 fails.** Example: L = 2, k_0 = (π, 0, 0), a(k_0) = 2/3.

**Premise check, one premise at a time.** The checks apply to ρ_T and ρ_P (and to ρ_T′).

| Premise | ρ_T, ρ_P |
| --- | --- |
| LIN, LIFT, b_A1 = 0 | the setting |
| lane 2's Theorem 1 | the setting: J_F exists on V_rest |
| H-link (one carrier copy) | a statement about the carrier; holds in the setting |
| H-cust, kinetic clause | M = μI_6, the setting |
| H-cust, condensate clause, and O-equivariance of Σ | Σ_c from ν = N(0, C_0) is block-scalar and O-equivariant |
| H5 | distinct κ_b |
| L-SDS | F-stationary, finite moments |
| translation and O invariance | yes |
| TPC | C = (label block) ⊕ C_0, with the label block ∝ P_{A_1} |
| H-PF with its clause, so N-2 and N-8 | a constraint on the field, not the state; admitted |
| SMD on P_rest∗ρ | P_rest∗ρ = ν, a Gaussian |
| N-1, the extension reading | ρ_T: the stabilizer statements are under R_ext. ρ_P: under any translation-commuting extension (w_φ ∈ SU(6)) |

Both witnesses violate N-9.
- ρ_T is not a single label sector, so it applies without the label-sector reading.
- ρ_P is a single label sector, so it applies under both readings, and is excluded only by
  R_π-invariance (R9.6).

### 4.3 Class of Q9 (rule applied per carrier, a refinement of PLAN §4)

| Carrier | Without the label-sector reading | Under the label-sector reading |
| --- | --- | --- |
| even L ≥ 2 | I (ρ_P; also ρ_T for L ≥ 8), unless R_π-invariance is required (for L ≤ 6) | I (ρ_P), unless the state is required to be R_π-invariant, in which case R (R9.6) |
| odd L ≥ 7 | I (ρ_T) | R (R9.2, a = 0) |
| odd L ∈ {3, 5} | O: no witness found | R (R9.2) |

Class D: none (R9.1–R9.6).

## 5. Controls

| Id | Result | Status |
| --- | --- | --- |
| P-1 | At abs(μ) < 1, L_0 = 0 and P_rest = I. LI is Theorem 1's uniqueness, Lemma PF is vacuous, and N-9 is SMD on ρ | green |
| P-2 | Under H-ZM the quotient identifies the slices and removes the labels, so N-2, N-8 and N-9 hold ([FS] C+2) | green |
| N-a | Proposition P's family is excluded only by H-PF's clause (§2.2), or by the unstated NAT-C (§2.1 R2.2(b)). It is never excluded by the stated structure | green |
| N-b | H-PF_u is checked against the clause by its spectral content (§3.3), and is admitted under the formula-only reading | green |
| N-c | ρ_T and ρ_P are checked against every premise of the stated set, C* and N-1 (§4.2 table) | green |
| N-d | P2a's covariance supports no class D or R | green |
| N-e | Extremality is tested against [A-rec] Proposition B (R9.3). The symmetries of F are tested for N-9 (R9.6) | green |
| X-1 | Fixed-string match at [P] for Main:44, Main:60, SM:136, SM:290, and Substratum:272 "Status (open)" | green |

**Power.** P-1 and P-2 check the setting only. N-b and N-c are the decisive countercontrols.

## 6. Passes, productivity and classification

**Passes.**
- **Pass 1, Q2.** Routes R2.1 to R2.3, and the reduction to H-PF.
- **Pass 2, Q8.** Routes R8.1 and R8.2, and Lemma PF.
- **Pass 3, Q9.** Routes R9.1 to R9.5, and witnesses ρ_T and ρ_P.
- **Pass 4, skepticism.** No new finding.
- **Pass 5, r2, applying the review.**
  - R2.2 corrected, and NAT-C recorded.
  - R9.6 added, and witness ρ_T′.
  - ρ_P extended to every even L ≥ 2.
  - Per-carrier classes.
  - The equivalence for N-8.

Stopping condition 1 holds for Q2, Q8 and Q9, with class O recorded for odd L ∈ {3, 5} without the
label-sector reading. Stopping condition 3 applies to R2.2(b): NAT-C is recorded and not adopted.

**Productivity (PLAN §7): gem.** Each N_k gets a class more informative than "candidate premise".
Conditional on O-1a and O-1b, the candidate-premise set reduces from three to one. The remaining one
is confirmed independent by a single-sector witness on every even L.

| Class | Findings |
| --- | --- |
| NEW | Lemma PF and the equivalence for N-8; ρ_P, for every even L ≥ 2 |
| POSITIVE | H-PF implies N-2 (§2.2); joint Gaussianity implies N-9 (R9.4); the reduction for a = 0 sectors (R9.2) |
| ELABORATING | R2.2 (the stated symmetries do not force LI; the commutant does, giving NAT-C); R9.3; R9.6 with ρ_T′; ρ_T extended to odd L ≥ 7 |
| CONFIRMING | ρ_T, re-checked |

Correctness bands unchanged: consistency-axis work (§A.23).

## 7. Scope

- Carrier T (d = 3) at the massless point, on the linear lift, with b_A1 = 0, for SM Theorem 5's
  consumers only. Carrier Z, H-PF-int, consumers outside Theorem 5 and the Z/q level are not
  addressed.
- The carried conditions remain carried and open: H-PF, L-SDS, TPC, SMD on the fluctuation law,
  LIN (posited), LIFT, and the SM:232 bridge.
- Each independence claim is relative to the stated premises of Main and SM, C*, N-1's extension
  reading, and the other premises listed in §4.2. It is not a claim that no extension of OI could
  supply N_k. In particular, NAT-C would supply N-2, and R_π-invariance with the label-sector
  reading would supply N-9 on even L.

## 8. Open nodes

- **O-1a (owner question, N-2).** Does H-PF's positive-frequency clause refer to the update F on
  V_rest, which is its stated domain? If yes, N-2 is class R. Dropping the clause weakens H-PF and
  makes N-2 class I. No other tamed reading exists (§2.2 step 3). If O-equivariance of J is
  required, this class I rests on the [W] transport step of R2.2(a), and holds only for L ≥ 7.
- **O-1b (owner question, N-8).** Is H-PF's clause extended to the stationary support in the
  trajectory form? If yes, N-8 is class R; this is equivalent to N-8 (§3.2). If H-PF is read as the
  formula on V_rest only, N-8 is class I. [FS] §4.2 records that H-PF does not say how φ extends.
- **O-2 (owner question).** Is Theorem 5's state a label sector fixed by the observer's records
  (R9.2)? If yes, N-9 reduces to SMD on sectors with a = 0. It stays independent on staggered
  sectors (ρ_P), unless the state is also required to be R_π-invariant (R9.6). That invariance is
  not stated.
- **O-3.** NAT-C, naturality of the complex structure under the linear commutant of F. It is
  recorded as a new premise and not adopted (stopping condition 3).
- **O-4.** Joint Gaussianity on T at μ = 1, and any T-analogue of [SMD-SRC]'s clustering theorem.
  For the SMD clustering unit's attention.
- **O-5.** Whether the selected measure, conditioned on registered labels, yields a condensate
  state. [A-rec] Proposition C concerns the unconditioned image.
- **O-6.** Odd L ∈ {3, 5} without the label-sector reading: class O, no witness found.
- **O-7.** H-PF itself remains open ([A-rec] §5).

## 9. Findings for routing (listed, not edited)

1. **[FS] PRESERVATION §2, the status of N-2 and N-8.** They are implied by H-PF under the readings
   O-1a and O-1b (§2.2, §3.2). Route: #1217.
2. **[FS] §3.4, N-9.** N-9 is independent within a single label sector on every even L (ρ_P),
   unless the state is required to be R_π-invariant. It reduces to SMD on sectors with zero
   staggered label under the label-sector reading. Route: #1217.

## 10. References not on `main` (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
| --- | --- | --- |
| #1169 comment 7208939261 | authorization | provenance: no result uses it |
| #1169 comment 7199704501 | work package | provenance |
| #1169 comment 7202075726, item 4 | the framing of N-2, N-8 and N-9 as candidate premises (§1) | support on `main`: quoted with author and time in [FS] PRESERVATION.md §1 |
| PR #1624 and its review comment 7209242260 | evidence of review | provenance |
| Issues #1217, #1169, #1049, #1216 (named in PLAN) | accountability and the scope boundary | provenance |
| commits `158f4155` (PLAN.md), `b3500e31` (r1) and the commit adding r2 | preregistration order, and the r1 text | support on `main` once merged; not before |
| [FS], [L2], [A-rec], [C3], [SMD-SRC] records | inputs to §2–§4 | support on `main` at [P] |

Support off `main`: none.

**Landing condition:** a merge without squash, so that the preregistration order of `158f4155`
before `b3500e31` stays reachable from `main`.

## 11. Verification status and remediation (§A.46 item 4)

**This table authorizes no work.** The categories are §A.46 item 4's. "Exploratory" means a paper
derivation not yet reviewed. "Partially verified" means checked by a model review only.

| Claim | Status | Missing | Issue | What would resolve it |
| --- | --- | --- | --- | --- |
| §2.2 steps 1–3, H-PF implies N-2 | partially verified (r1 review checked step 3; r2 strengthens it to all of 𝒢_+) | delta review; independent non-model verification | #1217 | recorded review |
| §2.2 step 4, the identification of H6-M's structure with H-PF's J | exploratory | review | #1217 | recorded review |
| R2.2(a), (b), with NAT-C | exploratory (new in r2); the O-equivariant transport is [W] | review | #1217 | recorded review |
| R2.3 | partially verified | independent non-model verification | #1217 | recorded review |
| Lemma PF, both directions, and §3.3 | partially verified (r1 review checked (⇒) and the consistency identity) | delta review | #1217 | recorded review |
| R8.2, the amplitude gauge | exploratory, conditional on an open warrant | review | #1217 | recorded review |
| R9.1, relying on [A-rec] Proposition C | partially verified (Proposition C model-reviewed in unit A) | independent non-model verification | #1217 | recorded review |
| R9.2, R9.3, R9.4 | partially verified (r1 review) | independent non-model verification | #1217 | recorded review |
| R9.6 and ρ_T′ | exploratory (new in r2) | review | #1217 | recorded review |
| ρ_T for even L ≥ 8 | partially verified ([FS] §3.4) | independent non-model verification | #1217 | recorded review |
| ρ_T extended to odd L ≥ 7 | partially verified (r1 review checked it) | independent non-model verification | #1217 | recorded review |
| ρ_P, every even L ≥ 2, with φ = 2π/3 | partially verified (r1 review checked it for large L; the extension to all even L follows the reviewer's hand argument, written here as [A]) | delta review; an exact finite control on L = 2 or 4 (needs authorization) | #1217 | review; authorized control |
| Outcome: no class D; N-9 class I on even L (no R_π-invariance) and on odd L ≥ 7 without the sector reading; N-2 and N-8 class R under O-1a and O-1b | conditional on O-1a, O-1b and O-2, and on C* | owner readings; review | #1217 | owner decisions; review |
