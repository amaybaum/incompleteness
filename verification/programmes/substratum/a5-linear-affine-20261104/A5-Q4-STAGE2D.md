# A5-Q4-STAGE2D — the Stage 2(d) stabilizer under an affine offset (#1049, Q4)

**Status: WIP / UNVERIFIED. Paper-only.** Authorized by the owner in chat on 2026-11-04, recorded at
#1049 comment 6624263637 ("Q4 is prioritized"), under #1049's paper-only authorization
(comment 6622105211). No code, enumeration or Lean was written or run. Every step was done by hand.
Nothing here is adopted, promoted or propagated.

**Base.** `origin/main` at `1609dc440f5a12d05b750f6d894bb91d09a099a3`. `File:N` means `papers/File.md`
line N at that commit. The parent assessment is `A5-LINEAR-AFFINE.md` at `f07f55d0` (D3, D16, R10,
§6 Q4).

**Labels.** [K] kernel-checked · [P] paper record · [D] derivation here, unreviewed · [L] literature
from memory · [O] owner decision.

**Notation.** V_K = V_3 ⊕ V_2 ⊕ V_1 (T₁ ⊕ E ⊕ A₁), the complex lift of the six-link carrier.
- G_0 = U(3)×U(2)×U(1), the block-diagonal unitaries.
- U(1)_diag = {(cI_3, cI_2, c)} is the common phase. U(1)_S = {(I_3, I_2, t)} is the singlet-block
  circle.
- K = {(cI_3, dI_2, c²/d)}, from SM:579, Proposition 14a.
- b ∈ V_K is the internal part of a uniform affine offset.
- H := {g ∈ G_0 : gb = b}.

***

## §1 Decision criteria (fixed before §3)

The **downstream outputs** are those the corpus derives from Stage 2(d):
- (O1) the group after the common-phase removal (Substratum:163);
- (O2) G_0/K ≅ S(U(3)×U(2)) (SM:579);
- (O3) the faithful charged-family image P/ℤ₆ (SM:593);
- (O4) the anomaly-fixed hypercharges and their normalization (SM:589, Theorem 15; Theorem 14);
- (O5) the A6 promotion to local invariance (Substratum:163; SM:114).

The readings below compare them under two **readings**: (L) the stabilizer of b-free data, and (A)
the stabilizer of the affine rule.

- **(i) Independent of b.** This outcome is reached if both of the following hold:
  - the object whose stabilizer Stage 2(d) computes does not contain b;
  - under reading (A) with b ≠ 0, every one of O1–O5 is reproduced. This means isomorphic groups,
    the same action on every carrier the corpus assigns charges on, and the same charges.
- **(ii) Hidden use of A5.** This outcome is reached if, under (A) with b ≠ 0, some output among
  O1–O5 fails or changes, and no subgroup of H reproduces it. A changed hypercharge, a missing
  U(1), or a different global form would each count.
- **(iii) Conditional on a convention.** This outcome is reached if O1–O5 agree only given a choice
  the corpus does not state. Examples are a carrier choice, admitting time-dependent frames, or
  reading the "singlet-block" identification modulo a subgroup.
- **(iv) Undecidable.** This outcome is reached if the sources do not fix the object, the carrier or
  the charged action well enough to decide.

**Controls (§A.29).** The conclusion must preserve the following:
- (C-a) the b = 0 results exactly;
- (C-b) Theorem 7's (3,2,1) decomposition [K];
- (C-c) Theorem 15's hypercharges.

**Required countercontrols.** A carrier on which (L) and (A) differ, so that an equivalence is not
vacuous. And an offset outside A₁ that does break the construction, so that the A₁ hypothesis is
load-bearing.

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

The object is the **O-action** (its bicommutant) or a generic O-equivariant **operator**. It is not
the update rule. Stage 2's Output (Substratum:149) names the "coupling matrix eigenvalue
multiplicities (3, 2, 1)".

**S2. SM:340–344 (Theorem 5) [P].** The object is the stabilizer in U(6) of the condensate
Σ = ⟨φφ†⟩ = aP_{T₁} + bP_E + cP_{A₁}, under H-link + H-cust. SM:344 adds:
> "The reduction from the natural unitary stabilizer to the Standard-Model group carries the
> separate amplitude-scale-gauge/background-independence premises […] and a specified charged
> matter action."

**S3. SM:376 and SM:493 [P].**
- SM:376: "the condensate is Σ = diag(aI_3, bI_2, c), while the coupling matrix itself is scalar".
- SM:493: "The substratum dynamics is locally U(6) invariant", and "the O-equivariant condensate Σ
  breaks U(6) → U(3)×U(2)×U(1)", with 22 cross-block modes gapped.

**S4. Other derivation sites [P].** They name three different objects:
- the **commutant of the coupling matrix M**: Structure:152, Explainer:830–840, and Substratum:102
  ("transformations … that leave the coupling itself unchanged");
- the **block algebra of the O-action**: Structure:152, :1153, and book ch02:102 together with its
  FULL.md:745 mirror;
- the **condensate stabilizer**: book ch04:118 and ch05:119–123.

The identification A₁ → hypercharge appears at SM:380, SM:491 ("End(V_1) = 1 — the U(1)
hypercharge boson"), Explainer:840 and ch02:102.

**S5. Downstream group theory [P].**
- SM:577, Theorem 14: hypercharge is a combination Q = αB + βL + γS of the three block circles.
- SM:579, Proposition 14a: G_0/K ≅ S(U(3)×U(2)). SM:585 adds that "on the full native End(V_3⊕V_2⊕V_1)
  conjugation carrier the kernel is only the common scalar circle".
- SM:593, Proposition 15a: the faithful image is S(U(3)×U(2)), with hypercharge circle
  z ↦ (z⁻²I_3, z³I_2).
- SM:519–539, §4.7.1.2: matter is placed on V_K ⊗ V_K*, and gauge bosons in End(V_K).
- SM:464, Theorem 11: the Higgs is placed in the E projection of the singlet taste (a V_K carrier),
  with its hypercharge "taken as phenomenological input".

**S6. Kernel [K].** No Lean module computes the Stage 2(d) stabilizer.
- `A6Instantiation.lean:62–70` states that the (3,2,1) decomposition, the condensate stabilizer and
  the reduction to SU(3)×SU(2)×U(1) "are neither consumed nor judged".
- `BackgroundIndependence.A6Glob F M` (line 107) is a predicate on the **rule F**: every constant
  g ∈ AddAut V commuting with M commutes with F. For F = `linkF` it reduces to the commutant of M.
  For an affine F = linkF + b it would add the condition gb = b. The kernel's notion is therefore
  rule-level, whereas Substratum:102's text is coupling-level. The two coincide at b = 0.

**Trace verdict [P].** No corpus site takes the stabilizer of the update rule, and none mentions an
offset. The objects used are the O-action, M and Σ, and b enters none of them. The parent
assessment's phrase "stabilizer of the linear part" is accurate only for the M-commutant sites.
Under SM's route the linear part at the symmetric point has stabilizer U(6) (S3), and the
U(3)×U(2)×U(1) comes from Σ.

***

## §3 Work, depth-first

**N0. Where b lies [D].**
- Exact translation commutation makes the offset uniform (parent B0.3(a)).
- Isotropy applied with the same internal O-action that makes M or Σ equivariant forces ρ(g)b = b,
  so b ∈ V_1 = A₁.
- In the link basis A₁ is spanned by (1,1,1,1,1,1). So b gives every component the same offset.

*Hypothesis H-b:* the O-action of H-link acts on the offset as on the field.

**N1. The group under each reading [D].**
- **(L)** The stabilizer is G_0, by S1 or S2. b does not enter.
- **(A), M-route.** On the lift a constant unitary g commutes with z ↦ Lz + β iff [g, M] = 0 and
  gb = b. With generic block-scalar M this gives H = U(3)×U(2)×{1}, since g acts on V_1 by a phase
  and that phase must be 1.
- **(A), Σ-route.** With scalar M, the dynamics' internal symmetry is Stab_{U(6)}(b) = U(5)×{1},
  acting on V_3 ⊕ V_2. Intersecting with Stab(Σ) = G_0 again gives H.
- **(A), up to amplitude gauge.** Consider the set of g that preserve the rule up to a common
  rescaling: gΦ_b g⁻¹ = Φ_{λb} for some unit λ. Every g ∈ G_0 does this, with λ the phase of g on
  V_1. So this set is G_0. This is the reading under which rescaling is a relabelling ([O] Q2 for
  shifts; Substratum:270).

Under every reading of (A) the strict stabilizer is H, and the circle U(1)_S is not in H. This
reproduces the candidate.

**N2. Is H the same group as the one the corpus actually uses? [D]** There are three checks, all
exact group theory.

*(a) O1, the common-phase quotient.*
- H ∩ U(1)_diag = {1}.
- H · U(1)_diag = G_0, since (A, B, z) = (z⁻¹A, z⁻¹B, 1)·(z, z, z).
- So the inclusion induces H ≅ G_0/U(1)_diag.

Under (A) the common phase is not a symmetry, because it moves b. So there is nothing to remove,
and H is already the reduced group. The parent's D3(iv) observation is the same fact seen from the
other side. Both readings reach U(3)×U(2).

*(b) O2, Proposition 14a, which needs no common-phase step.*
- K is central, hence normal.
- (A, B, z) = (A, zB, 1)·(I_3, z⁻¹I_2, z), and (I_3, z⁻¹I_2, z) ∈ K (take c = 1, d = z⁻¹). So
  H · K = G_0.
- The second isomorphism theorem gives H/(H∩K) ≅ G_0/K ≅ S(U(3)×U(2)), with
  H ∩ K = {(cI_3, c²I_2, 1)} ≅ U(1).
- The "singlet-axis circle" that SM:579 retains, F(I_3, I_2, t) = (t⁻²I_3, t³I_2), is attained
  inside H by the circle (I_3, tI_2, 1). Check: det C = 1 and det D = t², so
  F(I_3, tI_2, 1) = (t⁻²I_3, t²·t I_2) = (t⁻²I_3, t³I_2). ✓

This check does not depend on the owner's Q2 decision or on Substratum:163's common-phase removal.

*(c) O3, Proposition 15a.*
- S(U(3)×U(2)) = {(E, J, 1) : det E det J = 1} is a subgroup of H.
- The hypercharge circle z ↦ (z⁻²I_3, z³I_2, 1) lies in it, since the determinant is z⁻⁶z⁶ = 1.
- The intrinsic representations of SM:597 (d_R = E, u_R = (det E)⁻¹E, Q = E⊗J, L = (det J)⁻¹J,
  e_R = det E, H = J) are functions of (E, J) alone, so H carries them.

**N3. Charges, O4 [D].**
- On any carrier of Hom(V_j, V_i) type, a block-phase element (e^{iθ_3}, e^{iθ_2}, e^{iθ_1}) acts by
  e^{i(θ_i − θ_j)}. The common phase acts trivially there.
- So on End(V_K) and V_K ⊗ V_K*, which are the gauge-boson and matter carriers of SM §4.7.1.1–.2,
  αB + βL + γS acts as (α−γ)B + (β−γ)L ∈ Lie(H).
- Every charge vector Theorem 14 can produce on these carriers is therefore produced by
  U(1)_B × U(1)_L ⊂ H.
- Theorem 15's anomaly solve takes SU(3)×SU(2)×U(1) and the family pattern as its inputs. Neither b
  nor the number of block circles enters it. Its normalization is fixed by Q_em = T₃ + Y. So the
  hypercharges (1/6, 2/3, −1/3, −1/2, −1) are unchanged.
- **The different U(1).** The direct answer to Q4's second question is the hypercharge circle of
  Proposition 15a, (z⁻²I_3, z³I_2, 1) ∈ H, with the same charges on every carrier the corpus uses
  for fermions.
- Modulo the common phase, the singlet direction itself is represented in H by
  (t̄I_3, t̄I_2, 1). On Hom-type carriers it acts exactly as U(1)_S does.

**N4. Countercontrols [D].**
- *(a) A carrier on which the readings differ.* On V_K itself, (I_3, I_2, t) ∈ G_0 rotates the A₁
  component, but every element of H fixes V_1 pointwise. The equivalence of N2–N3 therefore holds
  on carriers of Hom type, or modulo U(1)_diag or K, and not on the fundamental carrier.
  - The corpus uses the fundamental carrier for the singlet-taste Higgs (Theorem 11). Its
    hypercharge there is input, and under (A) the A₁ projection is neutral.
  - Under (A) the E projection carries Y = β. The anomaly-fixed lepton doublet on Hom(V_E, V_A₁)
    has Y_{A₁} − Y_E = −β, so Y_H = 1/2 and Y_L = −1/2 are mutually consistent with Y_{A₁} = 0.
    I found no conflict.
- *(b) An offset outside A₁.* If H-b is dropped and b has a T₁ component, the stabilizer of b in
  U(3) is U(2). Then SU(3) itself is lost, and no subgroup of H restores color. So H-b is
  load-bearing. An offset that is not cubic-invariant would be a genuine break. E4 applied to the
  offset excludes it, and the corpus does not state that application.

**N5. Does the offset survive into the generator? [D]** Yes. It is not a central constant.
- In Koopman form U_Φ = T(β) U_L, where T(β) is a field translation. For the Koopman unitary R_g of
  g, R_g T(β) R_g⁻¹ = T(gβ). So T(β) commutes with R_g iff gb = b.
- In a continuum Lagrangian lift the offset is a linear source term b·φ_{A₁} (a tadpole [L]). It is
  not invariant under phase rotation of φ_{A₁}.
- The Lie algebra of internal symmetries of the dynamics is therefore Lie(H) = u(3) ⊕ u(2), which
  has dimension 13. This is not u(3) ⊕ u(2) ⊕ u(1), of dimension 14.
- Lie(H) equals Lie(G_0)/u(1)_diag, the Lie algebra after Substratum:163's quotient. The 13 gauge
  generators, 8 + 1 + 3 + 1, coincide with the count of the linear reading after the quotient. Both
  exceed the Standard Model's 12 by the H∩K, or K, circle, which Proposition 14a leaves to "further
  carrier/coarse-graining construction" (SM:585) under either reading.

**N6. What does change [D].**
- *(a) The cross-mode account.* Take SM:493's symmetric-point dynamics (U(6)) under (A). The 10 real
  generators of Hom(V_1, V_3⊕V_2) ⊕ h.c. and the A₁ phase are broken **explicitly** by b, not
  **spontaneously** by Σ. So 10 of the 22 cross-block modes are not gauge directions of the dynamics
  at all. This changes their accounting, as "gapped at M_X by the Higgs mechanism", not the gauge
  group.
- *(b) Proposition 4b survives.* With b ∝ (1,…,1) the six components are still identical
  independent systems. The connected response is still d·I₆, so H-cust's kinetic clause at the
  symmetric point holds. Odd q breaks the signed permutations to S₆, but the product argument does
  not need them.
- *(c) Wording.* "The singlet-block direction as the hypercharge U(1)" (Substratum:163; ch02:102
  and its FULL mirror), "A₁ → hypercharge" (SM:380), "End(V_1) = 1 — the U(1) hypercharge boson"
  (SM:491) and Explainer:840 hold literally only at b = 0. For b ≠ 0 they hold modulo U(1)_diag or
  K.
  - Even at b = 0, Proposition 15a's hypercharge circle is not U(1)_S. It is the image of U(1)_S
    under F. So the literal wording is already loose relative to SM:579–597, independent of b.
- *(d) Pressure test (§A.31).* N2–N3 favour the framework. Their weak points are these:
  - They need H-b.
  - They hold only on carriers of Hom type, or modulo U(1)_diag or K. The corpus states that matter
    and gauge bosons sit on such carriers (SM:519–539), and that the charged action realizing F is
    not yet constructed (SM:585), so neither reading has a constructed charged action.
  - A time-dependent symmetry g_t(z) = gz + (I−g)p(t) intertwines Φ for every g ∈ G_0, so
    Φ∘g_t = g_{t+1}∘Φ, using gL = Lg. It would restore G_0, but its admissibility is not
    established (parent §3.3.7), and it is not used here.
  - Uniform offsets only. A4 "up to gauge" allows non-uniform b, which is not examined.

**N7. Side findings, independent of b [D].**
- *(a) Coupling matrix.* Substratum:149/163, Structure:152 and Explainer:830–840 make the coupling
  matrix M carry the (3,2,1) and give the gauge group as its commutant. SM:376 and SM:493 say that
  M is scalar and that Σ carries the (3,2,1). SM:376's "(Remark below)" points to SM:382, which
  says that the earlier argument selecting a scalar M "does not hold". This is a cross-document
  variance to propagate (§A.25), not adjudicated here.
- *(b) Count of non-gauge U(1)s.* SM:587 counts "two combinations of (B, L, S) orthogonal to
  hypercharge". After the common-phase removal of Substratum:163, only one of them acts
  nontrivially on the Hom-type carriers. Low confidence; flagged for review.

***

## §4 Results

| # | Claim | Verdict | Hypotheses | Support | Does NOT establish |
|---|---|---|---|---|---|
| Q4-1 | Stage 2(d) and its mirrors take the stabilizer of the O-action, of M, or of Σ; no site takes that of the update rule | holds | — | [P] S1–S4 | that the rule-level reading is excluded (the kernel `A6Glob` is rule-level) |
| Q4-2 | Under (A) with b ≠ 0 the stabilizer is H = U(3)×U(2)×{1}, and U(1)_S is lost | holds; reproduces the candidate | H-b; lift; uniform b | [D] N1 | that this changes any output |
| Q4-3 | H ≅ G_0/U(1)_diag; H/(H∩K) ≅ G_0/K ≅ S(U(3)×U(2)); S(U(3)×U(2)) ≤ H | holds | as Q4-2 | [D] N2 | that either reading has a constructed charged action |
| Q4-4 | On Hom-type carriers H realizes every charge vector of Theorem 14. Theorem 15's hypercharges and normalization are unchanged. The hypercharge circle (z⁻²I_3, z³I_2, 1) lies in H | holds | as Q4-2; matter on V_K ⊗ V_K* | [D] N3; [P] SM:589–597 | that the family pattern is selected (it is open under both readings) |
| Q4-5 | The offset enters the dynamics' symmetry algebra: Lie(H) has dimension 13, not 14, and equals Lie(G_0)/u(1)_diag | holds | as Q4-2 | [D] N5 | — |
| Q4-6 | Residues: 10 cross modes are explicitly broken (N6a); the literal "singlet-block = hypercharge" holds only modulo U(1)_diag or K (N6c); the fundamental carrier differs (N4a) | holds | as Q4-2 | [D] | an observable consequence |
| Q4-7 | H-b is load-bearing: a T₁ offset loses SU(3) | holds | — | [D] N4b | that the corpus excludes such offsets |

**Outcome: (i) for the group-level construction**, meaning O1–O5 and the hypercharges, under H-b,
**with a scoped (iii) residue.**
- The residue consists of the literal singlet-block identification, the cross-mode account and the
  fundamental-carrier action, which agree only modulo U(1)_diag or K (Q4-6).
- **Not (ii).** No output among O1–O5 fails.
- The candidate's premise "the stabilizer of the linear part is U(3)×U(2)×U(1)" holds only on the
  M-commutant route.

***

## §5 Consequences (proposals only)

- **D16 and R10 (parent).** Restate R10 as "U(1)_S is lost; H reproduces O1–O5 (Q4-3, Q4-4); not a
  hidden use of A5 at group level, conditional on H-b". Restate D16 accordingly. A5's status is
  unchanged, as the owner decided [O].
- **The parent's D3(iii).** Correct it to name the route. On the Σ-route the linear part's
  stabilizer is U(6), and the affine part is U(5)×1.
- **#914 / the SM thread.**
  - Record H-b as an assumption-watch marker, next to the parent's N9/Q3 marker.
  - Propose scoping the singlet-block wording (N6c) to "modulo the common phase, or modulo K".
  - Propose resolving the variance in N7a. Neither is a manuscript edit here.
- No change is proposed to Theorem 15, Proposition 14a or Proposition 15a.

***

## §6 Open items and owner questions

- **Q4a.** Does E4 apply to the offset? This is H-b. If it does not, an anisotropic b breaks SU(3)
  (Q4-7), and A5 becomes load-bearing.
- **Q4b.** Is Stage 2(d)'s symmetry group meant to commute with the rule (as kernel `A6Glob` does)
  or with the coupling (as Substratum:102 does)? Q4-3 makes the answer immaterial at group level,
  but not for N6a.
- **Q4c.** Which of the M-commutant and Σ-stabilizer accounts is maintained (N7a)?
- **Q4d.** This links to the parent's Q3 (A6 and offsets). Under E1 the local group is H at every
  site. Under E3, b behaves as a charged background in A₁ whose unbroken group is H.
- **Open.** Non-uniform offsets; real versus complex lift (a real lift gives O(3)×O(2)×O(1), and a
  b ≠ 0 removes the O(1) factor); the SM:587 count (N7b).

***

## §7 Proposed computation (separate authorization only)

None is needed for the verdict, since Q4-2 to Q4-5 are exact finite group theory. If the owner
wants a mechanical control, a Lean or exact-algebra check could cover three statements:
- H·K = G_0 and H ∩ K at the level of the scalar torus;
- the carrier charge table of N3 for the five SM representations;
- the countercontrol of N4b.

The decision rules would be fixed in advance (equality of the image and charge tables; the
countercontrol differing). This would be CI-scale under §A.40, and it would not be run without
approval.
