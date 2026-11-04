# A5-Q4-STAGE2D — the Stage 2(d) stabilizer under an affine offset (#1049, Q4)

**Status: WIP / UNVERIFIED. Paper-only.** Authorized by the owner in chat on 2026-11-04, recorded at
#1049 comment 6624263637 ("Q4 is prioritized"), under #1049's paper-only authorization
(comment 6622105211). No code, enumeration or Lean was written or run. Every step was done by hand.
Nothing here is adopted, promoted or propagated.

**Revision.** Revised after the independent review of `8de75f7c` (ACCEPT WITH CHANGES). It addresses
B1–B3, S1–S6 and the nits. Points of partial disagreement are in §8.

**Base.** `origin/main` at `1609dc440f5a12d05b750f6d894bb91d09a099a3`. `File:N` means `papers/File.md`
line N at that commit. The parent assessment is `A5-LINEAR-AFFINE.md` at `f07f55d0` (D3, D16, R10,
§6 Q4).

**Labels.** [K] kernel-checked · [P] paper record · [D] derivation here, unreviewed · [L] literature
from memory · [O] owner decision.

**Notation.** V_K = V_3 ⊕ V_2 ⊕ V_1 (T₁ ⊕ E ⊕ A₁) is the complex lift of the six-link carrier.
- G_0 = U(3)×U(2)×U(1), the block-diagonal unitaries.
- U(1)_diag = {(cI_3, cI_2, c)} is the common phase. U(1)_S = {(I_3, I_2, t)} is the singlet-block
  circle.
- 𝒦 = {(cI_3, dI_2, c²/d)}, a 2-torus. It is SM:579's K, renamed here to avoid a clash with K = 6.
- F is SM:582's homomorphism G_0 → S(U(3)×U(2)), with kernel 𝒦.
- The offset: v ∈ V_K is the internal part of a uniform affine offset, and β = (0, v𝟙) is the
  two-slice offset.
- G_v := {g ∈ G_0 : gv = v}.
- Σ's block values are written (s_3, s_2, s_1).

**Readings.**
- **(L)** The stabilizer of offset-free data: the O-action, M or Σ.
- **(A-lin)** The constant **linear** internal unitaries that commute with the affine rule Φ.
- **(A-aff)** The constant **affine** internal maps z ↦ gz + w, with g ∈ G_0, that commute with Φ.
  This includes shift-conjugates, consistent with treating shifts as relabellings ([O] Q2).

**Resonance.** On the lift, with the normalized rule φ(t+1) = (1/d)M Σ_nn φ − φ(t−1), the uniform
mode of block a obeys g(t+1) = 2μ_a g(t) − g(t−1) + v_a. So κ_a = 2μ_a. Block a is **resonant** iff
μ_a = 1, which by SM:318 (Theorem 4) is exactly when the block is massless at k = 0.

***

## §1 Decision criteria (fixed before §3)

The **downstream outputs** are the following:
- (O1) the group after the common-phase removal (Substratum:163);
- (O2) G_0/𝒦 ≅ S(U(3)×U(2)) (SM:579);
- (O3) the faithful charged-family image P/ℤ₆ (SM:593);
- (O4) the anomaly-fixed hypercharges and their normalization (SM:589, Theorem 15; Theorem 14);
- (O5) the A6 promotion to local invariance (Substratum:163; SM:114).

Each outcome compares these outputs between (L) and an offset reading.

- **(i) Independent of the offset.** This is reached if both of the following hold:
  - the object whose stabilizer Stage 2(d) computes does not contain the offset;
  - under every offset reading with v ≠ 0, every one of O1–O5 is reproduced. This means isomorphic
    groups, the same action on every carrier the corpus assigns charges on, and the same charges.
- **(ii) Hidden use of A5.** This is reached if, under an offset reading with v ≠ 0, some output
  among O1–O5 fails or changes and no subgroup of the offset stabilizer reproduces it. A changed
  hypercharge, a missing U(1), or a different global form would each count.
- **(iii) Conditional on a convention.** This is reached if O1–O5 agree only given a choice the
  corpus does not state. Examples are a carrier choice, admitting time-dependent or affine frames,
  or reading the "singlet-block" identification modulo a subgroup.
- **(iv) Undecidable.** This is reached if the sources do not fix the object, the carrier or the
  charged action well enough to decide.

**Controls (§A.29).** The conclusion must preserve the following:
- (C-a) the v = 0 results exactly;
- (C-b) Theorem 7's (3,2,1) decomposition [K];
- (C-c) Theorem 15's hypercharges.

**Countercontrols.** The note needs a carrier on which the readings differ, so that the equivalence
is not vacuous. It also needs an offset outside A₁ that does break the construction.

***

## §2 What the sources say: which object's stabilizer

**S1. Substratum:163 (Stage 2(d)) [P].**
> "The unitary group of the bicommutant of the cubic-group action on V_K = V_3 ⊕ V_2 ⊕ V_1 —
> equivalently, the stabilizer of any generic O-equivariant operator on V_K — is U(3)×U(2)×U(1).
> […] Amplitude-scale invariance […] removes only the common overall phase […] The reduction to
> SU(3)×SU(2)×U(1), with the singlet-block direction as the hypercharge U(1), additionally uses a
> specified charged matter action and anomaly cancellation ([SM §4.9, Theorem 15]). Background
> independence (A6) […] then promotes the remaining global SU(3)×SU(2)×U(1) to local gauge
> invariance."

The object is the **O-action** (its bicommutant) or a generic O-equivariant **operator**. Stage 2's
Output (Substratum:149) names the "coupling matrix eigenvalue multiplicities (3, 2, 1)".

**S2. SM:340–344, Theorem 5 [P].** The object is the stabilizer in U(6) of the condensate
Σ = ⟨φφ†⟩ = s_3P_{T₁} + s_2P_E + s_1P_{A₁}, under H-link + H-cust. The ambient group is a symmetry of
the dynamics. SM:342 states that "the pre-condensate observer-level kinetic term is invariant under
the custodial unitary action".

**S3. SM:376 and SM:493 [P].**
- SM:376: the condensate is block-diagonal, "while the coupling matrix itself is scalar".
- SM:493: "The substratum dynamics is locally U(6) invariant", and Σ "breaks U(6) → U(3)×U(2)×U(1)",
  with 22 cross-block modes gapped.

So SM's route is Stab(Σ) ∩ Sym(dynamics), and an offset in the rule enters it through Sym(dynamics).

**S4. Other derivation sites [P].**
- The **commutant of M**: Structure:152, Explainer:830–840, and Substratum:102 ("transformations …
  that leave the coupling itself unchanged").
- The **O-action block algebra**: Structure:152, :1153, and ch02:102 with its FULL.md:745 mirror.
- The **condensate stabilizer**: ch04:118 and ch05:119–123.
- The A₁ → hypercharge identification: SM:380, SM:491 ("End(V_1) = 1 — the U(1) hypercharge boson"),
  Explainer:840 and ch02:102.
- Affine rules as such are discussed at Substratum:100, Substratum:220 and SM:240. None of these is a
  Stage 2(d) site.

**S5. Downstream group theory [P].**
- SM:577, Theorem 14: Q = αB + βL + γS, and "Three U(1) factors exist automatically".
- SM:579–585, Proposition 14a: G_0/𝒦 ≅ S(U(3)×U(2)). SM:585 adds that "on the full native
  End(V_3⊕V_2⊕V_1) conjugation carrier the kernel is only the common scalar circle".
- SM:587: "two combinations of (B, L, S) orthogonal to hypercharge".
- SM:593–597, Proposition 15a: the faithful image is S(U(3)×U(2)). The circle z ↦ (z⁻²I_3, z³I_2)
  appears in the proof at SM:595. SM:597 gives the intrinsic representations, which are not shown
  to be selected by the raw endomorphism carrier.
- SM:519–539: matter is placed on V_K ⊗ V_K*, and gauge bosons in End(V_K).
- SM:464, Theorem 11, with its Scope at SM:468: the Higgs sits in the E projection of the singlet
  taste, a V_K carrier, with its hypercharge "taken as phenomenological input".

**S6. Kernel [K].**
- No Lean module computes U(3)×U(2)×U(1). `A6Instantiation.lean:64–67` says the (3,2,1)
  decomposition, the condensate stabilizer and the reduction are "neither consumed nor judged", and
  `:405` excludes "the stabilizer in U(6)".
- `OIBridge.lean:436` `finrank_commutant` (= 3) supports Substratum:163's pointwise commutant U(1)³.
- `BackgroundIndependence.A6Glob F M` (definition at `:111`) is a **proposition**, not a stabilizer.
  It states that every M-commuting g ∈ AddAut V is a symmetry of the **rule** F, on the finite AddAut
  carrier. For F = `linkF` + v it is false unless the whole commutant fixes v. For example, g = −id
  moves v whenever 2v ≠ 0. The kernel's notion is rule-level; Substratum:102's text is
  coupling-level.

**Trace verdict [P].** No Stage 2(d) site computes the stabilizer of an affine rule. The SM route
(S2, S3) and kernel `A6Glob` take the symmetry of the dynamics as ambient, so the offset can enter
them. The parent's phrase "stabilizer of the linear part" fits the M-commutant sites. On the Σ-route
the linear part at the symmetric point has stabilizer U(6).

***

## §3 Work, depth-first

**N0. Where the offset lies [D].**
- Exact translation commutation makes the offset uniform (parent B0.3(a)).
- Isotropy applied with the same internal O-action that makes M or Σ equivariant forces ρ(g)v = v,
  so v ∈ V_1. In the link basis V_1 is spanned by (1,…,1).

*Hypothesis H-b:* the O-action of H-link acts on the offset as it acts on the field.

**N1. The group under each reading [D].**
- **(L)** G_0, by S1 or S2. The offset does not enter.
- **(A-lin), M-route.** A constant unitary g commutes with z ↦ Lz + β iff [g, M] = 0 and gv = v. With
  generic block-scalar M this gives G_v = U(3)×U(2)×{1}.
- **(A-lin), Σ-route.** With scalar M the linear symmetries of the rule are Stab_{U(6)}(v) = U(5)×{1}.
  Intersecting with Stab(Σ) gives G_v.
- **(A-aff)** (review B1, re-derived here). Take z ↦ gz + w. It commutes with Φ iff
  - Lg = gL, and
  - (L − I)w = (g − I)β.

  For g ∈ G_0 we have (g − I)β = (z_g − 1)β, where z_g is the phase of g on V_1. So:
  - **Off resonance in A₁ (μ_{A₁} ≠ 1).** β ∈ Im(I − L), with fixed point p = (x*𝟙, x*𝟙),
    x* = v/(2 − 2μ_{A₁}) ∈ V_1. Every g ∈ G_0 gives the symmetry g_p(z) = g(z − p) + p. The
    stabilizer is τ_p G_0 τ_{−p} ≅ G_0, and in the relabelled coordinate y = z − p the rule is linear.
  - **At resonance (μ_{A₁} = 1).** β ∉ Im(I − L). Over the lift, A commutes with translations, so the
    k = 0 sector of Im(2I − A) on V_1 is (2 − 2μ_{A₁})V_1 = 0. Then (z_g − 1)β lies in that image iff
    z_g = 1. The linear parts form exactly G_v.
- **Up to the amplitude gauge.** gΦ_v g⁻¹ = Φ_{z_g v} for every g ∈ G_0. So the set of g that preserve
  the rule up to a common rescaling is G_0.

So G_v, and the loss of U(1)_S, occurs under (A-lin) always, and under (A-aff) only at resonance.
Resonance holds at SM:232's observer-level normalization at scalar M (κ = 2). It is not generic on
the block-scalar M-route.

**N2. Is G_v the group the corpus uses? [D]**

*(a) O1.* G_v ∩ U(1)_diag = {1} and G_v · U(1)_diag = G_0, since
(A, B, z) = (z⁻¹A, z⁻¹B, 1)(z, z, z). So G_v ≅ G_0/U(1)_diag. Under (A-lin) the common phase is not a
symmetry, so G_v is already the reduced group.

*(b) O2, with no common-phase step.*
- 𝒦 is central.
- (A, B, z) = (A, zB, 1)(I_3, z⁻¹I_2, z), with the second factor in 𝒦. So G_v · 𝒦 = G_0.
- Hence G_v/(G_v ∩ 𝒦) ≅ G_0/𝒦 ≅ S(U(3)×U(2)), with G_v ∩ 𝒦 = {(cI_3, c²I_2, 1)}.
- F(I_3, tI_2, 1) = (t⁻²I_3, t³I_2). Check: det C = 1 and det D = t², so the first scalar is t⁻² and
  the second is t²·t = t³. This equals F(I_3, I_2, t), the singlet-axis image of SM:583.

*(c) O3 (corrected after review B2 and S4).*
- Proposition 15a's representations are representations of S(U(3)×U(2)) ≅ G_0/𝒦. G_v carries them
  **through the surjection F|_{G_v}** of (b).
- The subgroup {(E, J, 1)} ⊂ G_v is not a section of F, because F(E, J, 1) = (δ²E, δ⁻³J) with
  δ = det E. Nor is SM:583's section (E, J, det E) in G_v. A preimage in G_v is (E, (det E)J, 1):
  det C = δ and det D = δ² det J = δ, so F gives (E, J).
- **Lifts of the hypercharge circle z ↦ (z⁻²I_3, z³I_2).** In G_v these form a coset of G_v ∩ 𝒦:
  - (I_3, zI_2, 1) is one lift (by (b));
  - (z⁻²I_3, z⁻³I_2, 1) is another. Here det C = z⁻⁶ and det D = z⁻⁶, giving (z⁻²I_3, z³I_2).
  - Their ratio (z⁻²I_3, z⁻⁴I_2, 1) lies in G_v ∩ 𝒦.
  - The element (z⁻²I_3, z³I_2, 1) of the earlier draft is **not** a lift: F maps it to
    (z⁻¹⁴I_3, z²¹I_2).

**N3. Charges, O4 [D].**
- On Hom(V_j, V_i)-type carriers an element with block phases (e^{iθ_3}, e^{iθ_2}, e^{iθ_1}) acts by
  e^{i(θ_i − θ_j)}, and U(1)_diag acts trivially. So on End(V_K) and V_K ⊗ V_K*,
  αB + βL + γS acts as (α−γ)B + (β−γ)L ∈ Lie(G_v). Every charge vector Theorem 14 produces on these
  carriers is produced inside G_v.
- **Lift families agree.** Every (L)-lift of the hypercharge circle has the form h·u, with h ∈ G_v and
  u ∈ U(1)_diag ⊂ 𝒦. Since F(u) = 1, h is a G_v-lift, and it has the same action on Hom-type
  carriers.
  - Hand check, on (Hom(V₂,V₃), Hom(V₁,V₃), Hom(V₁,V₂)) per unit z:
    - (L)-lifts (I, I, z)·𝒦 give (s, −1−s, −1−2s);
    - G_v-lifts (I, zI_2, 1)·(G_v ∩ 𝒦) give (−1−a, a, 1+2a);
    - these are the same family, with a = −1−s.
  - At s = 1 this is (1, −2, −3), the weights of Q, d_R and L. Under (A-lin) it is realized by
    (z⁻²I_3, z⁻³I_2, 1).
  - u_R (charge 4) and e_R (charge −6) have no SM-weight home on the raw Hom-type carrier under
    either reading (SM:597).
- Theorem 15 takes SU(3)×SU(2)×U(1) and the family pattern as input. Neither the offset nor the
  number of block circles enters it, and its normalization is fixed by Q_em = T₃ + Y. So the
  hypercharges are unchanged.

**N4. Countercontrols [D].**
- *(a) The fundamental carrier.* On V_K itself, (I_3, I_2, t) ∈ G_0 rotates the A₁ component, while
  G_v fixes V_1 pointwise. This holds under (A-lin), or under (A-aff) at resonance. Off resonance
  under (A-aff), G_0 acts on V_K about p.
  - The corpus uses V_K for the singlet-taste Higgs, with its hypercharge as input (SM:468).
  - Under G_v the A₁ projection is neutral and the E projection carries Y = β.
  - One illustrative placement is consistent: the lepton doublet on Hom(V_E, V_{A₁}), with
    Y_{A₁} − Y_E = −β, gives Y_H = 1/2 and Y_L = −1/2. No corpus assignment is tested here, since
    SM:529 places only Q_L.
- *(b) An offset outside A₁.*
  - Under (A-lin), an offset with a T₁ component has stabilizer U(2) inside U(3), so SU(3) is lost.
    This happens whatever the resonance.
  - Under (A-aff) it does so only if T₁ is resonant (μ_{T₁} = 1). Otherwise a static shift removes it.
  - So H-b is load-bearing under (A-lin), and under (A-aff) at resonance.

**N5. Does the offset survive into the generator? [D]**
- In Koopman form U_Φ = T(β)U_L, with T(β) a field translation, and R_g T(β) R_g⁻¹ = T(gβ). Under
  (A-lin) the offset is not central: the symmetry algebra is Lie(G_v) = u(3) ⊕ u(2), of
  dimension 13 rather than 14.
- In a continuum lift the offset is a tadpole v·φ_{A₁} [L]. A field shift removes it iff the mode is
  massive (parent, "Reading" after B0.3), which is the off-resonance branch. There (A-aff) restores
  dimension 14.
- Lie(G_v) = Lie(G_0)/u(1)_diag, which has 8 + 1 + 3 + 1 generators, one more than the SM's 12.
- The surplus is one circle under each reading: G_v ∩ 𝒦 under (A-lin) and 𝒦/U(1)_diag under (L). Its
  removal needs the "further carrier/coarse-graining construction" of SM:585 either way.

**N6. Residues (each under (A-lin), or under (A-aff) at resonance) [D].**
- *(a) Cross modes.* At SM:493's symmetric point the offset explicitly breaks 11 = 36 − 25 generators:
  the 10 real cross generators of Hom(V_1, V_3⊕V_2) ⊕ h.c. and the A₁ phase. Σ does not break them
  spontaneously. Only the account of 10 of the 22 cross modes changes, not the group.
  - At the normalized scalar branch (μ = 1) the rule is resonant, so this residue stands there under
    both offset readings.
- *(b) Proposition 4b survives.* With v ∝ (1,…,1) the six components are identical independent
  systems, and the connected response is d·I₆. The signed flips are lost iff 2v ≠ 0, which the product
  argument (SM:336) does not need.
- *(c) Wording and counts that hold only modulo U(1)_diag or 𝒦:*
  - "the singlet-block direction as the hypercharge U(1)" (Substratum:163; ch02:102 and FULL:745);
  - "A₁ → hypercharge" (SM:380);
  - "End(V_1) = 1 — the U(1) hypercharge boson" (SM:491);
  - Explainer:840;
  - "Three U(1) factors exist automatically" (SM:577), since G_v's central torus is 2-dimensional;
  - SM:587's "two" non-gauge combinations, which become one under G_v, even on V_K.

  Even at v = 0, Proposition 15a's hypercharge circle is the F-image of U(1)_S, not U(1)_S itself.
- *(d) Pressure test of the branch favourable to the framework, N2–N3 (§A.31).*
  - These results need H-b.
  - They hold only on Hom-type carriers, or modulo U(1)_diag or 𝒦. The corpus places matter and gauge
    bosons there (SM:519–539) but uses V_K for the Higgs (SM:464).
  - Neither reading has a constructed charged action (SM:585).
  - The (A-aff) off-resonance branch removes the residues only by admitting affine internal maps,
    which the corpus's U(K) does not state.
  - The time-dependent g_t(z) = gz + (I−g)p(t) (Φ∘g_t = g_{t+1}∘Φ) would restore G_0 at resonance.
    It is not admitted, per parent §3.3.7.
  - Only uniform offsets are examined.

**N7. O5, A6 promotion (not examined; review B3).** The note does not derive it. Its form depends on
the parent's open Q3 (extensions E1–E3). One remark only, not counted as coverage: under E1
(untransported offset) the local group at each site would be G_v. Kernel `A6Cov` is stated for
additive links and does not decide this.

**N8. Side findings independent of the offset [D].**
- *(a) What carries (3,2,1).*
  - Substratum:149/163, Structure:152 and Explainer:838 make M block-scalar.
  - SM:376, SM:493 and SM:683 ("Since the coupling matrix is scalar, M = μ·I₆") make M scalar.
  - SM:376's "(Remark below)" points to SM:382, which withdraws the argument for a scalar M.
  - Explainer:828 lists linearity among the selection criteria.

  This is a cross-document variance to propagate (§A.25), not adjudicated here.
- *(b) The SM:587 count.* On Hom-type carriers the abelian part acts through T³/U(1)_diag, which is
  2-dimensional. Removing hypercharge leaves one direction. SM:587's "orthogonal" presupposes an
  unstated inner product. Two directions act only on V_K under (L). Moderate confidence; the reviewer
  concurs.

***

## §4 Results

| # | Claim | Verdict | Hypotheses | Support | Does not establish |
|---|---|---|---|---|---|
| Q4-1 | No Stage 2(d) site computes the stabilizer of an affine rule. SM's Σ-route and `A6Glob` take the dynamics' symmetry as ambient | holds | — | [P] S1–S6 | which ambient is intended (Q4b) |
| Q4-2 | The offset stabilizer is G_v = U(3)×U(2)×{1} under (A-lin), or under (A-aff) at μ_{A₁} = 1. Under (A-aff) off resonance it is τ_pG_0τ_{−p} ≅ G_0 | holds | H-b; lift; uniform offset | [D] N1 | which reading or resonance case is physical |
| Q4-3 | G_v ≅ G_0/U(1)_diag; G_v/(G_v∩𝒦) ≅ G_0/𝒦 ≅ S(U(3)×U(2)); Proposition 15a's representations pull back through F\|_{G_v} | holds | as Q4-2 | [D] N2 | a constructed charged action under either reading |
| Q4-4 | Hypercharge lifts in G_v form a coset of G_v∩𝒦, e.g. (I_3, zI_2, 1) or (z⁻²I_3, z⁻³I_2, 1). Their Hom-type charge family equals that of (L). Theorem 15's hypercharges are unchanged | holds | as Q4-2 | [D] N2(c), N3; [P] SM:589–597 | Hom-type homes for u_R and e_R (absent under both readings); family selection |
| Q4-5 | Lie(G_v) has dimension 13, equal to Lie(G_0)/u(1)_diag | holds | (A-lin), or (A-aff) at resonance | [D] N5 | — |
| Q4-6 | Residues: N6a (10 cross modes), N4a (V_K action), N6c (wording; SM:577 and :587 counts) | holds | as Q4-5 | [D] | an observable consequence |
| Q4-7 | H-b is load-bearing: a T₁ offset loses SU(3) | holds | (A-lin); or (A-aff) with μ_{T₁} = 1 | [D] N4b | that the corpus excludes such offsets |
| Q4-8 | O5 (A6 promotion) | not examined | — | — | anything about O5 |

**Outcome, by §1's rule (review S3).**
- **Overall: (iii).** O1–O4 agree between (L) and the offset readings either
  - on Hom-type carriers, or modulo U(1)_diag or 𝒦 (under (A-lin), or (A-aff) at resonance); or
  - fully, by admitting affine internal maps (under (A-aff) off resonance).

  Both are conventions the corpus does not state. On V_K, which the corpus uses for the Higgs, the
  actions differ in the first case.
- **Group-level component.** The abstract groups O1–O3 and the hypercharges O4 agree in every branch
  (Q4-3, Q4-4). Taken alone, these statements meet (i)'s requirements.
- **Not (ii).** No output among O1–O4 fails.
- **O5 is not classified** (Q4-8).

***

## §5 Consequences (proposals only)

- **Parent D16 and R10.** Restate R10 as follows: "U(1)_S is lost under (A-lin), or at A₁ resonance.
  G_v reproduces O1–O4 at group level (Q4-3, Q4-4). Carrier-level agreement is conditional (iii).
  O5 is open." Restate D16 to match. A5's status is unchanged, per the owner [O].
- **Parent D3(iii).** Name the route. On the Σ-route the linear part's stabilizer is U(6), and the
  offset's is U(5)×1. Add the resonance condition.
- **#914 / the SM thread.**
  - Record H-b and the resonance condition as assumption-watch markers, next to parent N9/Q3.
  - Propose scoping the N6c wording to "modulo the common phase, or modulo 𝒦".
  - Propose resolving N8a, and raise N8b.
  - None of this is a manuscript edit.

***

## §6 Open items and owner questions

- **Q4a.** Does E4 apply to the offset (H-b)?
- **Q4b.** Is the Stage 2(d) group meant to commute with the rule (as `A6Glob` and SM:342/493 have
  it) or with the coupling (as Substratum:102 has it)? And are its elements linear, (A-lin), or
  affine, (A-aff)?
- **Q4c.** Is the A₁ block resonant (μ_{A₁} = 1) on the maintained branch? Which account of
  (3,2,1), M or Σ, is maintained (N8a)?
- **Q4d.** O5, through parent Q3 (E1–E3).
- **Open.** Non-uniform offsets; the real lift (O(3)×O(2)×O(1), whose O(1) factor is lost);
  composite q.

***

## §7 Proposed computation (separate authorization only)

The verdict needs no computation. An optional exact control could check four statements:
- G_v · 𝒦 = G_0 and G_v ∩ 𝒦, on the scalar torus;
- the F-images of the N2(c) lifts, including the non-lift;
- the N3 Hom-type charge families;
- N4b under both offset readings.

Decision rules would be fixed in advance: equality of the image and charge tables, and the
countercontrol differing. This would be CI-scale under §A.40, and it would not be run without
approval.

***

## §8 Response to review (`8de75f7c`)

- **B1, B3, S1–S6 and the nits:** accepted and applied. The table header now reads "Does not".
- **B2:** accepted, with one refinement. The two lifts the review names are equivalent for F, since
  they differ by an element of G_v ∩ 𝒦, but not on Hom-type carriers. (I_3, zI_2, 1) gives
  (−1, 0, 1) on (Hom(V₂,V₃), Hom(V₁,V₃), Hom(V₁,V₂)), whereas (z⁻²I_3, z⁻³I_2, 1) gives (1, −2, −3).
  Q4-4 therefore states the coset, and the result that the lift families agree.
