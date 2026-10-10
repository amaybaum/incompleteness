# Thread C — FOUR-COMP: four-copy coherence from a composition principle — RESULT (research only)

Base: certified `main` at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`, read-only at `pt/base/`. Inputs: `pt/inputs/`
(manifest of 41 files). Protocol `pt/PROTOCOL.md` (sha256 `239dc123…`), amendment 1 (`b41aa0e7…`), amendment 2
(`2a2f78f3…`), all verified and applied. Nothing here is adopted, frozen or governed; no git write, no CI, no GitHub
access, no agent spawned. There is no Lean toolchain: the Lean text in §1.A7 is UNBUILT. Running record: `NOTES.md`.

Evidence tags (three levels kept apart): **[K]** certified at L (landed declaration, `file:line` under
`pt/base/verification/lean-mathlib/OIBridge/`: CI CompositeInterface, KF KInfFoundations, CD CompositeDimension);
**[D]** kernel-checked in the design run at `ff9c3a35`, not certified (`pt/inputs/fourcopy/`); **[W]** written
argument; **[X]** exact computation in `pt/C/`, replayed byte for byte, stated for the instance it checks; **[L]**
literature or standard result not re-derived here; **[M]** Mathlib v4.33.0 source (`db584cd`).

Notation. Tokens 0–3; grouping A = 01|23, grouping B = 02|13; pair cones K_p ⊆ W 3. `tp x y := flatW (prodState x y)`
(a token product of the pair chart); S = {e_x, e_y, e_z, −e_z} (pure states). For a carrier V with product data PA
(grouping A) and PB (grouping B): p_A(x) = PA.prodState (tp x0 x1) (tp x2 x3), p_B(x) = PB.prodState (tp x0 x2)
(tp x1 x3); the coordinate readouts T_A(v)_abcd = PA.prodEff (tabCoord a b) (tabCoord c d) v and
T_B(v)_abcd = PB.prodEff (tabCoord a c) (tabCoord b d) v; H(x)_abcd = hom x0_a hom x1_b hom x2_c hom x3_d.

## 0. Answer

Instance: KT(4; 01|23, 02|13) with 3-ball tokens and pair cones K_p ⊆ W 3. Targets: FCC (`FourCopyCoherent`), and
the token clauses `tokA`, `tokB` of `KT4Core` (the audited hypothesis H).

- **FCC — CONDITIONAL; sufficiency proved [W + X; Lemma B1 is D].** Named principles: **N0** the four tokens carry one
  real carrier on which each grouping is a COMP-1 pre-composite of the pair bodies (landed definitions; constructible
  for every quadruple); **N1** one body; **N2** TokProdState: independently prepared tokens compose to the same state
  in both groupings (regrouping invariance of independent preparation; used only at the 256 products of S). From
  N0–N2 every field of `KT4Core` follows, token clauses included, and FCC follows under hadm — with no local
  tomography beyond the setting's W 3, no operation of any kind (no idle extension, no IE₁), no closedness and no
  cone premise beyond hadm. Each of N0, N1, N2 is classed independently motivated, and every proper sub-conjunction
  holds on every quadruple of nonempty pair bodies, so the cone constraint arises only from the conjunction; N2 names
  no cone, effect or inequality and is the state-level coherence of parallel composition. The conjunction is not a weaker
  substitute for FCC: over carriers, ∃(N0 ∧ N1 ∧ N2) ⟺ FCC under hadm, each direction proved. The route therefore
  relocates the four-copy content into regrouping invariance, which nothing certified at L supplies: L has no
  structure with three or more tokens. FCC is not DERIVED: the M_tok data satisfy every pair hypothesis, and both FCC
  families fail there at −1/8 [X].
- **tokA — CONDITIONAL; sufficiency proved [W + X]** from N0's product data and N2 alone (no one body, no positivity,
  no hadm, no local tomography). Weakest variant found: first-order independent preparation IP₁ᴬᴮ with N0 ∧ N1 ∧ hadm
  [W + X], which relative to those premises is equivalent to tokA.
- **tokB — CONDITIONAL; sufficiency proved [W + X]**, symmetric: from N2, or from IP₁ᴮᴬ with N0 ∧ N1 ∧ hadm.
- **Exclude M_tok, without sufficiency** (necessary-condition evidence only). Each of the following excludes the mixed
  assignment (Q3, Q3, Q3, twin), and each is **refuted as a route** by an exact model:
  - one-directional IP₁ with N0 ∧ N1 ∧ hadm: hybrids with all four pair hypotheses [W], ¬FCC and ¬C [X];
  - uniformity, one pair type across bipartitions, one pair type up to per-token charts: uniform K_c, with all pair
    hypotheses [W], FCC −1 and ¬IE₁ [X];
  - relabelling covariance: the anchor sum on uniform K_c [X].
- **Survives every tested model** (sufficiency for FCC rests on [W + L]): FCC restricted to the gate-supplied link
  instances. It is a restriction of the target, not a composition principle. It suffices for the theorem's conclusion
  relative to the pair hypotheses (a reading of the design proof [W]); its equivalence with FCC relative to those
  hypotheses rests on the written classification argument [W + L].

Outcome class (protocol): **DERIVED-CONDITIONAL** (→ CONDITIONAL under amendment 2) for FCC, tokA and tokB.

## 1. Routes and countermodels, node by node

### 1.A The decisive node: regrouping invariance gives `KT4Core` (protocol C1, C4)

**A1. Exposed assumption (NEW).** The audited theorem `kt4_forward_ie1` takes `H : KT4Core` [D FourCopyHeadline:120–124;
X c1 S0.head]. KT4Core's token clauses are stated only at the product states of each grouping: `tokA` for x ∈ pairBody
K01, y ∈ pairBody K23 at `stA x y`, and `tokB` likewise [D FourCopyCore:111–114; X c2 S0.core]. `KT4.tok :
TokenCoherent` is stated on the whole body PA.Ω [D FourCopyCore:64–68; X c2 S0.tok], and `KT4.toCore` reads it only
at products [D FourCopyBridge:232–234; X c2 S0.toCore].

The prior routes to the token clauses target the body-level clause, and that is why they need local tomography:
- EQ5-PREM Theorem A: IP₁ᴮᴬ ∧ LT ∧ one body ∧ PairAdm ⇒ TokenCoherent;
- SOURCE §3.7: TokProdState ⟺ tok relative to LT(PA).

ASSUMPTIONS.md §4.2 carries both over to KT4Core. For the clauses the headline actually reads, neither local
tomography nor body-level token coherence is needed (A2), and the route's premises force neither (A4, PAD).

**A2. The route (sufficiency proved).** Premises:
- N0: a real normed space V with PA : PreComposite (pairBody K01) (pairBody K23) V and PB : PreComposite (pairBody K02)
  (pairBody K13) V;
- N1: PA.Ω = PB.Ω;
- N2: p_A(x) = p_B(x) for x ∈ S⁴;
- hadm, for the last step only.

Take stA, stB, effA, effB := PA.prodState, PB.prodState, PA.prodEff, PB.prodEff. Step by step:

1. **Data and evaluation laws.** These are the ProductData fields [K CI:210–218]: bi-affine prodState (combo laws for
   every a + b = 1 at every chart point, CI:212–215), bilinear prodEff (CI:216), prodEff_apply (CI:217–218).
2. **posBA.** Let e be an effect on pairBody K02 and f an effect on pairBody K13, and let x ∈ pairBody K01,
   y ∈ pairBody K23.
   - PA.prodState x y ∈ PA.Ω by prod_mem [K CI:227], and PA.Ω = PB.Ω by N1.
   - PB.prodEff e f is an effect on PB.Ω [K CI:228–229], so its value there is ≥ 0.

   This is KT4.toCore's argument [D FourCopyBridge:228–231]. posAB is symmetric.
3. **tokB.** Fix (a, b, c, d) and set Φ(u, w) := PA.prodEff (tabCoord a b) (tabCoord c d) (PB.prodState u w) and
   Ψ(u, w) := u_{4a+c} w_{4b+d}.
   - Φ is affine in each argument: combo laws, and PA.prodEff · · ∈ V →ᵃ[ℝ] ℝ.
   - At (tp x0 x2, tp x1 x3) with x ∈ S⁴, N2 turns Φ into PA.prodEff (…) (…) (p_A(x)) = hom x0_a hom x1_b hom x2_c
     hom x3_d by prodEff_apply, and this equals Ψ.
   - On H00 × H00, H00 = {u : u_0 = 1}, every bi-affine map is a bilinear form uᵀ C w [X c3 E1: a symbolic identity
     over the general bi-affine map, 289 coefficients]. H00 contains every pairBody, because flatW index 0 is entry
     (0, 0) [M Logic/Equiv/Fin/Basic.lean:334].
   - The 16 token products tp s t (s, t ∈ S) form an invertible matrix [X c3 E2, det 256; c2 G4]. So TPm C_Φ TPmᵀ =
     TPm C_Ψ TPmᵀ forces C_Φ = C_Ψ [W], and Φ = Ψ on pairBody K02 × pairBody K13.
   - Then effA (tabCoord a b) (tabCoord c d) (stB x y) = Φ(x, y) = x_{4a+c} y_{4b+d}, which is
     effB (tabCoord a c) (tabCoord b d) (stB x y) by PB's prodEff_apply. That is tokB.
4. **tokA.** The same argument with Φ′(u, w) := PB.prodEff (tabCoord a c) (tabCoord b d) (PA.prodState u w).
5. **FCC.** Lemma B1, `fourCopyCoherent_of_kt4Core`, with hadm's maxCone bound and scaling [D FourCopyBridge:269–322;
   X c3 S0.B1].

What each premise is used for:
- N0 supplies the fields' form;
- N1 is used only by posBA and posAB;
- N2 is used only by tokA and tokB, so the token clauses hold for arbitrary cones;
- hadm is used only by B1.

Not used: local tomography of the four-token composite; TokenCoherent on the body; closedness; any gate, operation or
idle extension; IE₁ or IE₂; Q3 or PSD as a premise; the region tower; any (o) step.

**A3. Satisfiability and the converse (each direction separately witnessed, §A.34).**
- *Satisfiable.* In the model MSIG — PA = modelData and PB = σ ∘ modelData on V = ℝ^{17×17}, σ = ιRπ + (id − ιπ) —
  N2, tokA and tokB hold as symbolic identities in all arguments [X c2 M.MSIG; σ an involution with σι = ιR,
  c2 G1, G2]. With uniform Q3 and Ω = conv(A products ∪ B products), N0 and N1 hold [W]. MSIG therefore satisfies
  N0–N2, KT4Core and FCC.
- *Converse: FCC ∧ hadm ⇒ ∃V with N0 ∧ N1 ∧ N2.*
  - In MSIG the cross values are exactly the FCC forms: PB.prodEff e f (p_A) = fourVal X Y Ẽ F̃ and PA.prodEff e f
    (p_B) = g2 ẽ f̃ L L′ for normalized arguments [X c3 V1, V2: symbolic identities for the MSIG maps].
  - Give MSIG the hull body. Every cross value is then ≥ 0 by FCC and ≤ 1 by the complement identity [W]. So N0 and N1
    hold, and N2 holds by c2.
  - Hence ∃V.(N0 ∧ N1 ∧ N2) ⟺ FCC, and ⟺ ∃V. KT4Core, relative to hadm [W + X; ⇒ uses B1, D].

**A4. Each premise cannot be dropped; what the premises do not force.** Each model below satisfies the remaining
premises, and the target fails there. Such a model shows that the remaining premises are insufficient; it does not
show that the dropped premise is necessary.

| dropped | model (cones in the order 01, 23, 02, 13) | holds | fails (exact) |
|---|---|---|---|
| N1, one body | SEPH: the MSIG maps with separate minimal bodies, on (Q3, Q3, Q3, twin) | N0 with separate bodies; N2, tokA, tokB [X c2 M.MSIG]; TokenCoherent on all of V, since π∘σ = R∘π [W from X c2 G2]; LT of both groupings [W; K CI:342, CI:740] | FCC; B's product effect of the dual tables phiW/4, L′/4 at A's product of phiW, phiW is −1/8 [X c2 X1] |
| N2, TPS | ANC: the anchor sum, anchors at flat E00, on (Q3, Q3, Q3, twin) | N0 ∧ N1 [X c2 P.ANC + W] | TPS, tokA, tokB [X c2 M.ANC]; FCC, −1/8 [X c1 W2, W3] |
| N2, with local tomography of both groupings added | MTW and MTH (token 3 read through ρ = actT reflY or θ = actT(−I)), on (Q3, Q3, Q3, twin) | N0 ∧ N1 [X c2 P.MTW, P.MTH + W]; LT of both groupings [W, as EQ5-SOURCE/PREM] | TPS; first-order identity fails at token 3 only, in both directions [X c2 M.tw3]; FCC |
| N0's full effect quantifier, restricted to products of token effects | the MSIG maps with the hull body, on (Q3, Q3, Q3, twin) | restricted N0 ∧ N1 ∧ N2: B's token-product effects at A's products factor as (g0ᵀXg1)(g2ᵀYg3) ≥ 0 [X c2 X3 + W] | FCC |

- Every proper sub-conjunction of {N0, N1, N2} holds on every quadruple of nonempty pair bodies [W + X c2]:
  - {N0, N1}: the anchor sum;
  - {N0, N2}: SEPH-type separate minimal bodies;
  - {N2}: the MSIG product data.

  The cone constraint FCC arises only from the conjunction.
- *Not forced: PAD* (uniform Q3; the MSIG maps on V = ℝ^{17×17} × ℝ with one extra body point v* that B reads
  shifted).
  - N0, N1, N2, KT4Core and FCC hold.
  - LT(PA), LT(PB), TokenCoherent and single-token marginal coherence all fail at v* [X c2 L1, L2; countercontrol L2c].

  The route's premises therefore force neither local tomography nor body-level token coherence.
- *Not forced: a quantum four-token body.* MSIG with the hull body, and the four-token pair network PN₄ of EQ4-P, are
  four-token bodies other than PSD₁₆ that satisfy N0–N2 on uniform Q3 [W].

**A5. The weakest variant: first-order independent preparation (sufficiency proved).**

Definitions:
- IP₁ᴮᴬ: for x ∈ S⁴, the single-token marginal entries of T_A(p_B(x)) are hom x_t (12 numbers per preparation).
- IP₁ᴬᴮ: the same with T_B(p_A(x)).

Route to tokB from IP₁ᴮᴬ, given N0, N1 and hadm (products in the cones; K01, K23 ⊆ maxCone):
1. **Vanishing.** h := tabCoord 0 0 − unitEff vanishes on pairBody K01, so c·h is an effect for every real c. Hence
   PA.prodEff h f = 0 on PA.Ω for every effect f, and for every affine f, by exists_effect_rescale [W; K CI:148,
   CI:93; D B1a FourCopyBridge:85, :111]. So T := T_A(p_B(x)) has T_0000 = 1 (prodEff_unit).
2. **Positivity.** For effects g_t of the ball, T(g0, g1, g2, g3) = PA.prodEff (t(g0,g1)) (t(g2,g3)) (p_B(x)) ∈
   [0, 1], with t(g, g′) = Σ ĝ_a ĝ′_b tabCoord a b.
   - t(g, g′) is an effect on pairBody K whenever K ⊆ maxCone [W: complement identity].
   - p_B(x) ∈ PA.Ω by N1.
3. **Purity.** With pure marginals, T = H(x) [W purity lemma; core identity X c3 U1; countercontrols X c3 U2 (purity
   is load-bearing), U3 (positivity is load-bearing)].
4. **Extension** as in A2, step 3, gives tokB.

So, relative to N0 ∧ N1 ∧ hadm: tokB ⟺ IP₁ᴮᴬ and tokA ⟺ IP₁ᴬᴮ. The forward direction is the route above; the reverse
is specialization.

Each ingredient cannot be dropped:
- **Positivity (one body).** CORR has IP₁ in both directions [X c3 U4, U5], while T_A(p_B(x)) = H(x) + 2 C0 (a
  correlation with zero marginals). The token clauses and TPS fail. A's product of token effects is −1/4 at B's token
  product, so no body carries COMP-1 positivity for both groupings [X c3 U6].
- **Both directions.** HBA, on (Q3, Q3, K_c, K_c) with cnot gates and identity locals:
  - holds: hcls, hadm, hcl, hgate [W c1 K.W]; N0 ∧ N1 [W: famII holds there, since K_c ⊆ Q3]; IP₁ᴮᴬ and tokB
    [X c2 M.HBA];
  - fails: IP₁ᴬᴮ and tokA [X c2 M.HBA]; famI, at −1 [X c1 K7]; IE₁ for K_c [X c4 N1–N3]; hence C.

  HAB is the mirror, on (K_c, K_c, Q3, Q3) [X c2 M.HAB; c1 K8]. **Route refuted:** "the pair hypotheses + N0 + N1 +
  one-directional IP₁ ⇒ C". Each direction alone still excludes the mixed assignment (B1).

STMC (single-token marginal coherence on Ω) gives IP₁ in both directions by specialization, so N0 ∧ N1 ∧ STMC ⇒ H
[W + X]. PAD shows STMC is not needed for H.

**A6. Independence assessment (protocol: independently motivated or restatement).**

| premise | statement | alone | assessment |
|---|---|---|---|
| N0 | each grouping is a COMP-1 pre-composite of the pair bodies on one carrier (landed definitions [K CI:210–230]; the factor bodies are the standalone pair bodies, H0 at four tokens) | vacuous: constructible from landed definitions for every quadruple (anchor sum, separate hulls) | independently motivated: "the four tokens form a system that is a composite of the pairs, whichever way they are grouped" |
| N1 | PA.Ω = PB.Ω; it can be weakened to cross membership of the product states | vacuous with N0 (anchor sum) | independently motivated: regrouping invariance of the state space |
| N2 | TokProdState on S⁴ | satisfiable for every quadruple (SEPH, MSIG data) | independently motivated: regrouping invariance of independent preparation, the state-level coherence (associativity and commutativity, naturality on states) of parallel composition. It mentions no cone, no effect and no inequality, so it is not FCC in other words. Relative to N0 it is strictly stronger than tokA ∧ tokB: the landed S2 carrier and EQ5-PREM's PAD2 have the token clauses without TPS |
| IP₁ (both directions) | first moments on pure token products | — | independently motivated: a token prepared in x is found in x by single-token tests of either grouping. Relative to N0 ∧ N1 ∧ hadm it is equivalent to the token clauses (A5); it is the weakest form found |

Two records bear on this assessment.
- EQ5-PREM classed TPS as a relabelling. That classification was made relative to LT and to the body-level clause
  TokenCoherent, where TPS ⟺ tok. Here the target is the product-level clause pair, no LT is assumed, and TPS is
  strictly stronger than the target (A6, row N2).
- Over carriers, the conjunction N0 ∧ N1 ∧ N2 is equivalent to FCC under hadm (A3). So the route does not reduce the
  strength of the four-copy assumption. It identifies the assumption with "the four tokens compose into one
  regrouping-invariant system". Certified main does not contain that system: L declares nothing with three or more
  tokens [X c0_census_L; audited SOURCE s0 at bcbc516f, with no Lean change since].

Verdict: CONDITIONAL, not UNRESOLVED. The premises are stated precisely, each is independently motivated, and none is
a restatement of the target.

**A7. UNBUILT Lean statement (design only; no toolchain; not a kernel proof).**

```lean
-- UNBUILT. Names follow the design modules at ff9c3a35.
def TokProdState {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    {Ω01 Ω23 Ω02 Ω13 : Set (Fin 16 → ℝ)} (PA : PreComposite Ω01 Ω23 V) (PB : PreComposite Ω02 Ω13 V) : Prop :=
  ∀ x0 x1 x2 x3 : Fin 3 → ℝ, x0 ∈ eball 3 → x1 ∈ eball 3 → x2 ∈ eball 3 → x3 ∈ eball 3 →
    PA.prodState (flatW (prodState x0 x1)) (flatW (prodState x2 x3)) =
      PB.prodState (flatW (prodState x0 x2)) (flatW (prodState x1 x3))

structure KT4Minus (K01 K23 K02 K13 : Set (W 3)) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] where
  PA : PreComposite (pairBody K01) (pairBody K23) V
  PB : PreComposite (pairBody K02) (pairBody K13) V
  one_body : PA.Ω = PB.Ω

-- A2 step 3: needs the affine-extension lemma on the hyperplane {u | u 0 = 1} (UNBUILT).
theorem KT4Minus.tokB_of_tps (H : KT4Minus K01 K23 K02 K13 V) (hT : TokProdState H.PA H.PB) :
    ∀ a b c d : Fin 4, ∀ x ∈ pairBody K02, ∀ y ∈ pairBody K13,
      H.PA.prodEff (tabCoord a b) (tabCoord c d) (H.PB.prodState x y) =
        H.PB.prodEff (tabCoord a c) (tabCoord b d) (H.PB.prodState x y) := sorry
-- tokA_of_tps symmetric; toCoreOfTPS : KT4Core … V with posBA/posAB as in KT4.toCore;
-- fourCopyCoherent_of_tps := fourCopyCoherent_of_kt4Core (hadm …) (H.toCoreOfTPS hT).
```

### 1.B The mixed assignment (Q3, Q3, Q3, twin) (protocol C3)

**B1. Both families fail (famII NEW).**
- famI: fourVal phiW phiW (phiW/4) (L′/4) = −1/8 [X c1 W2; landed F10, replayed in c0].
- famII: g2 (phiW/4) (phiW/4) phiW L′ = −1/8, with L′ = diag(1,−1,1,−1) = actT reflY sing4 ∈ twin [X c1 W1, W3].
- Countercontrols: in each family, replacing the twin argument by a Q3 one gives +1/4 [X c1 W2c, W3c].

Since each direction of first-order token identity yields one family (A5), either single direction, with N0 ∧ N1 ∧
hadm, already excludes the mixed assignment. That is necessary-condition evidence, not sufficiency (HBA, HAB).

**B2. The classified family.** On {Q3, twin}⁴, FCC holds exactly at the 8 coboundary (even) twist patterns:
- the per-token transport identity, symbolic, for all 16 sign charts [X c1 T1];
- the coboundary enumeration [X c1 T2];
- an exact −1/8 witness for each odd pattern [X c1 T3];
- the even patterns, by transport from uniform Q3 [W; landed F2/F3].

This confirms EQ3 p2 Z and proves the design package's open `fourCopyCoherent_chart` for this family by T1.

**B3. Tree obstruction (NEW; an exact obstruction for a class of routes).** Let a principle be a conjunction of
conditions, each reading the cones, gates and locals of at most three of the four pairs, and each invariant under
per-token reflection charts. If it holds at the quantum data (uniform Q3, cnot gates, identity locals), it holds at
M_tok's data:
- on every 3-pair subset, M_tok's twist pattern is a coboundary [X c1 R1], which fails on the full cycle [X c1 R1c];
- the chart transport carries cones and gates, cnot to cnotTw [X c1 I4, I6, R2 + W].

So no such principle implies FCC. A principle that excludes the mixed assignment must couple all four pairs, or depend
on the charts. The class includes per-pair co-self-duality, single-token marginal consistency of the cones, and
pair⊗token three-token composites; the last are satisfiable on every admissible quadruple [W, entangled-core
argument].

**B4. "One pair type" conditions exclude it but are insufficient and unnecessary.**
- Uniformity, "one pair type across bipartitions" (K01 = K02 and K23 = K13, or the other matching) and "one pair type
  up to per-token charts" (U*) all exclude (Q3, Q3, Q3, twin).
- Each is refuted as a route by uniform K_c = cone(SEP ∪ cnot SEP) with cnot gates and identity locals:
  - hcls, hadm, hcl and hgate hold [W c1 K.W];
  - FCC fails at −1 [X c1 K1–K7];
  - IE₁ fails [X c4 N1–N3], so C fails.

  K_c is a simpler exact analogue of EQ3's C_H.
- None is necessary: (Q3, Q3, twin, twin) is an even pattern, so FCC holds [X c1 T1, T2 + W], and it violates
  uniformity and both matchings.
- On the classified family, U* is exactly FCC (B2).

**B5. Answer to C3.** At the cone level, on the family the classification produces, the exclusion is a consistency
(cocycle) condition: the twist pattern must be a coboundary, that is, one pair type up to per-token charts. It is not
"one pair type across bipartitions" in a fixed chart, which is too strong there and insufficient in general (B4).
Beyond that family, any intrinsic condition on at most three pair cones is blind to it (B3).

At the carrier level, the composition principle that excludes the mixed assignment *and* derives FCC is regrouping
invariance, N1 ∧ N2 on N0. Its content is token identity across groupings: the identification of each token in
grouping B with the same token in grouping A. That is a consistency condition of composition, not a pair-type
condition. Even one direction of first-order token identity excludes the assignment (B1).

### 1.C Other candidates (protocol C2)

- **Entangled core.** If any one argument of famI or famII is separable, the value reduces to a pairing of Lorentz
  vectors through a maxCone table [X c1 E1, E2: symbolic identities + W]. FCC therefore fails only at configurations
  whose four arguments are all non-separable. A principle constraining only configurations with a product state or a
  product effect is implied by hadm, so it does not imply FCC (refuted as a route).
- **Link instances.** The design proof reads FCC only through PairLinked at targets 01 and 02, with the two link-pair
  arguments fixed to gate-supplied tables (Bell tables, rotated links), and at the four parity witnesses
  [X c4 U1, U2: source checks on FourCopyHeadline and FourCopyIE1; W reading]. Relative to the pair hypotheses,
  link-FCC therefore suffices for C [W]. The written classification gives P ∧ C ⇒ FCC [W + L], so link-FCC ⟺ FCC ⟺ C
  relative to P (confirming EQ3-AUDIT §4). Link-FCC survives every model tested here; it is a restriction of the
  target, not a composition principle.
- **Relabelling covariance.** In the anchor sum on uniform cones, the component swap carries PA's product data to
  PB's [X c3 L1, countercontrol L1c]. With uniform K_c, FCC fails, so the route is refuted.
- **Restatements, not sources:**
  - the common-composite sandwich in token-indexed coordinates (⟺ FCC [W]);
  - swap/conditioning closure: conditional states of one grouping's pair, after a test on the other, are states
    (⟺ FCC [X c1 I1, I2 + W]);
  - regrouping invariance of token-product statistics, RI_op = TokenCoherent [EQ5-PREM R1].
- **Symmetric monoidal composition** with a natural associator and braiding implies N0 ∧ N1 ∧ N2 on the instance [W + L]:
  sufficient, and strictly stronger.
- **Operation-level token identity** (OLTI-rev) is (o)-type and forbidden as a premise. It is refuted anyway by MTH
  [W, as EQ5-PREM's M_θ].

### 1.D Field-by-field relations (protocol C1; record)

| KT4Core field / FCC | supplied by |
|---|---|
| stA, stB, effA, effB, bilinearity, effA_apply, effB_apply | N0's ProductData [K CI:210–218] (also IP₀, independent preparation within a grouping: automatic) |
| posBA, posAB | N1 with each grouping's own prodEff_effect, with the full IsEffectOn quantifier [K CI:228–229] |
| tokA, tokB | N2 with the combo laws (A2); or IP₁ᴬᴮ, IP₁ᴮᴬ with N1 and hadm (A5); or STMC; or TokenCoherent (RI_op) by specialization; or IP₁ (one direction) with LT, by EQ5-PREM Theorem A |
| FCC | all of the above, with hadm, through Lemma B1 [D] |
| (not read) | one-body vacuity (RI₀ alone), relabelling covariance (RI_L), LT of either grouping, closedness, gates |

Cone-level candidates (uniformity, U*, sub-plaquette conditions, co-self-duality) supply no carrier field. They bear
on FCC only, and each is refuted as a route (B3, B4).

### 1.E Passes and fixed point (§A.31)

| pass | content | outcome |
|---|---|---|
| 1 | nodes A–D | NEW: A1, A2, A4 (SEPH, the sub-conjunction statement, PAD), A5 (the one-direction hybrids with all pair hypotheses, the LT-free IP₁ route), B1 (famII), B3 |
| 2 | after amendment 1: the route re-derived step by step | ELABORATING: one body weakenable to cross membership; TPS needed only on S⁴; tokA needs neither one body nor hadm |
| 3 | setting assumptions: H0 at four tokens; two-copy LT in W 3; shared per-token charts; the flattening convention | CONFIRMING |
| 4 | missed candidates: associativity without commutativity cannot relate 01|23 to 02|13; process closure is FCC restated; STMC; pair⊗token composites; link instances | ELABORATING |

Three consecutive passes without NEW: fixed point. Node log: NOTES N6–N7.

## 2. The ledger (certified versus added)

| premise | used by | class | anchor | note |
|---|---|---|---|---|
| ProductData: bi-affine prodState, bilinear prodEff, evaluation law | A2 steps 1, 3, 4; A5 | [K] definition | CI:210–218 (combo laws CI:212–215) | the form of N0's assertion; asserting that the four-token system has this structure is N0 |
| PreComposite: Ω, convex, prod_mem, prodEff_effect over all IsEffectOn effects, prodEff_unit | A2 step 2; A5 steps 1–2 | [K] definition | CI:223–230; IsEffectOn KF:116 | the full effect quantifier cannot be dropped (A4) |
| unitEff is an effect; exists_effect_rescale | A5 step 1 | [K] theorem | CI:93; CI:148 | IP₁ variant only |
| W 3, prodState, hom (the two-copy table carrier) | setting | [K] definition; its local-tomography content is [A] K2 OPEN | CD:95–97; ROADMAP:1001–1006 | built into the audited theorem's typing; the route adds no further LT |
| KT4Core, FourCopyCoherent, PairAdm, flatW, pairBody, tabCoord | statement | [D] definitions | FourCopyCore:47–57, 99–114; FourCopyDefs:43, 56–60 | not certified |
| Lemma B1 `fourCopyCoherent_of_kt4Core` | A2 step 5 | [D] | FourCopyBridge:269–322 | not certified |
| B1a `abs_le_00_of_maxCone`, `abs_le_one_of_maxCone` | A5 step 1 | [D] | FourCopyBridge:85, 111 | IP₁ variant only |
| hadm (PairAdm: products in K, K ⊆ maxCone, convex cone) | A2 step 5 (maxCone bound, scaling); A5 (maxCone bound, products) | hypothesis of the audited theorem; source [A] K2 OPEN (transport [T]) | ROADMAP:1001; result.md Q3 | shared with the theorem, not added by the route |
| finProdFinEquiv (a, b) = b + 4a | A2 step 3 (H00 contains every pairBody) | [M] | Mathlib Logic/Equiv/Fin/Basic.lean:334 | any bijection with (0, 0) ↦ 0 serves |
| **N0** four-token carrier, each grouping a COMP-1 pre-composite of the pair bodies | A2, A5 | **[N]** | — | vacuous alone; independently motivated |
| **N1** one body (or cross membership) | A2 step 2; A5 step 2 | **[N]** | — | vacuous with N0; independently motivated |
| **N2** TokProdState on S⁴ | A2 steps 3–4 | **[N]** | — | independently motivated; not a restatement (A6) |
| **N2′** IP₁ᴬᴮ ∧ IP₁ᴮᴬ (alternative to N2) | A5 | **[N]** | — | independently motivated; equivalent to the token clauses relative to N0 ∧ N1 ∧ hadm |

No premise of the route is IE₁, IE₂, a quantum cone, the complex region tower, an (o) step or operation-level idle
extension.

## 3. Candidate table

Models:
- From c2/c3: ANC (anchor sum), MRHO (M_ρ), MTW (M_tw), MTH (M_θ), MT (transposed factor), SEPH, HBA, HAB, PAD, MSIG,
  CORR.
- Cone-level: Mtok = (Q3, Q3, Q3, twin) with the landed data; Kc = uniform K_c.
- Landed: MtokC (the anchor carrier on uniform Q3).

Codes:
- **R**: the candidate holds and the target fails (route refuted);
- **n**: the candidate fails there;
- **✓**: the candidate and the target hold;
- **—**: not a predicate on that model.

The target is FCC, together with tokA ∧ tokB for carrier rows.

| # | candidate | class | ANC | MRHO, MTW, MTH | SEPH | HBA, HAB | Kc (and ANC on Kc) | MT, MtokC | PAD, MSIG | sufficiency / independence |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | N0 ∧ N1 ("one four-token state space, composite in both groupings") | [N] | R | R | n | R | R (ANC) | MT: tok R; MtokC — | ✓ | refuted |
| 2 | N0 ∧ N1 ∧ LT of both groupings | [N] + K2 | n | R [W LT] | n | n | — | ✓ (MT) | MSIG ✓, PAD n | refuted (MTW, MTH) |
| 3 | N2 on ProductData without one body | [N] | n | n | R | n | — | n | ✓ | refuted (SEPH) |
| 4 | **N0 ∧ N1 ∧ N2** | [N] | n | n | n | n | n | n | ✓ | **sufficiency proved** (A2); independently motivated |
| 5 | **N0 ∧ N1 ∧ IP₁ᴮᴬ ∧ IP₁ᴬᴮ** (CORR: n) | [N] | n | n | n | n | n | n | ✓ | **sufficiency proved** (A5); independently motivated |
| 6 | N0 ∧ N1 ∧ IP₁ᴮᴬ only (IP₁ᴬᴮ only) | [N] | n | n | n | R (HBA; HAB) | n | n | ✓ | refuted; excludes Mtok (B1) |
| 7 | N0 ∧ N1 ∧ STMC | [N] | n | n | n | n | n | n | MSIG ✓, PAD n | sufficiency proved (via 5); not necessary (PAD) |
| 8 | N0 with effects restricted to token products ∧ N1 ∧ N2 | [N] | — | — | — | — | — | — | ✓ | refuted (Mtok cones, c2 X3) |
| 9 | relabelling covariance ∧ N0 ∧ N1 | [N] | R on Kc | — (pair bodies differ) | n | — | R (ANC on Kc) | — | ✓ | refuted; excludes Mtok |
| 10 | RI_op = TokenCoherent, with N0 ∧ N1 | restatement of the body-level token clause | n | n | n (one body) | n | n | n | ✓ | sufficient (specialization); a restatement, not a source |
| 11 | uniformity (shared chart) | [N] cone | — | Mtok n | — | — | R | ✓ | ✓ | refuted; excludes Mtok; not necessary |
| 12 | one pair type across bipartitions | [N] cone | — | Mtok n | — | n | R | ✓ | ✓ | refuted; excludes Mtok; not necessary |
| 13 | U*: one pair type up to per-token charts | [N] cone | — | Mtok n | — | n | R | ✓ | ✓ | refuted; on {Q3, twin}⁴ ⟺ FCC |
| 14 | intrinsic conditions on ≤ 3 pair cones (co-self-duality, marginal consistency, pair⊗token composites) | class | — | Mtok R | — | — | R | ✓ | ✓ | refuted as a class (B3) |
| 15 | FCC at gate-supplied link instances | restriction of the target | — | Mtok n | — | n | n | ✓ | ✓ | survives all; sufficient relative to the pair hypotheses [W + L] |
| 16 | sandwich, swap closure | restatement of FCC | — | Mtok n | — | n | n | ✓ | ✓ | a restatement, not a source |
| 17 | symmetric monoidal composition (natural associator, braiding) | [N], stronger than row 4 | n | n | n | n | n | n | ✓ | sufficient through row 4 [W + L] |
| 18 | OLTI-rev (rotations of a token act identically through both groupings) | (o)-type: flagged | — | MTH R [W] | — | — | — | — | ✓ | refuted; forbidden as a premise |

PN₅ is relevant only as a non-quantum model of rows 4, 5 and 7 at four tokens (PN₄ body with Q3 pairs) [W, EQ4-P].
It shows these rows do not force K₄ = PSD₁₆. MtokC and MT are models of ¬TPS ∧ ¬IP₁ ∧ FCC, so TPS and IP₁ are not
necessary for FCC for given carrier data.

## 4. Cross-thread notes

- **Thread A (hcl).**
  - The route uses no closedness; FCC derived this way holds for non-closed cones as well (the K_cl type).
  - A completion that is to feed the route must keep each grouping's product map bi-affine on the pair chart: the
    COMP-1 combo laws on the chart, or bi-affinity on bodies whose affine hull is the hyperplane.
  - Four-copy local tomography is not needed, but the pair cones live in W 3, whose two-copy local tomography is K2.
- **Thread B (hgate).**
  - The design proof consumes FCC only at gate-supplied link instances (c4). There, hgate's role is to supply the link
    tables in the cones and duals.
  - K_c and the hybrids HBA, HAB satisfy hgate (two-sided: cnot is an involution) and fail C. So gate preservation does
    not repair a failure of four-copy coherence.
  - K_c is a closed, admissible, cnot-invariant, uniform cone with an exact cnot-invariant witness E0 ∈ K_c* outside
    Q3 [X c1 K1–K9], available as a foil.
- **Thread D (hcls, hadm).**
  - The route uses hadm only through B1 (maxCone bound, scaling), and the IP₁ variant also uses the products clause.
  - The token clauses via N2 need no hadm at all.
- **Integration (K2).** The four-copy premise separates cleanly from K2: given regrouping invariance (N1 ∧ N2 on N0),
  H follows without four-copy local tomography. Relative to the pair hypotheses it yields IE₁ through the audited
  theorem [D], so a state-level composition principle carries the operation-level idle extension of rotations. The
  remaining four-copy requirement is a four-token composite with token identity, which L does not contain.

## 5. What is not claimed

- **No DERIVED claim.** Nothing certified at L has three or more tokens [X c0_census_L; audited SOURCE s0]. FCC fails
  on M_tok's data, which satisfy hcls, hadm, hcl and hgate [landed Q1-MAP, replayed c0; X c1 W2, W3].
- **No adoption.** N0–N2 and IP₁ are candidate principles. No status change is proposed, and nothing says that the
  observer-native framework supplies regrouping invariance.
- **Necessity.** N0 ∧ N1 ∧ N2 is necessary for FCC only in the existential sense of A3: some carrier with them exists
  when FCC holds. For given carrier data neither TPS nor IP₁ is necessary (MtokC, MT, the landed S2 carrier). Every
  "cannot be dropped" model shows insufficiency only.
- **Scope of [X].** Each exact computation is for the instance it checks: the stated models, tables and matrices, or
  universal symbolic identities in the arguments named. Universal statements rest on the written arguments of A2, A3
  and A5, with those ingredients.
- **No kernel proof of the route.** The Lean text of A7 is UNBUILT. Lemma B1 and the headline are [D], not certified.
  The classification argument (P ∧ IE₁ ⇒ {Q3, twin}) is [W + L], one standard Lie-theory input, and is not
  kernel-checked.
- **Not established here:**
  - W2: whether gate-invariant admissible K = T(K*) forces Q3 or the twin;
  - three-token structure, IE₂, other groupings (03|12), KT(n) for n ≠ 4;
  - the quantum four-token body.
- **Cited, not re-derived:** the LT of MTW and MTH (EQ5-SOURCE/PREM), the PN hierarchy (EQ4-P), EQ3's C_H.
- **Bands.** Consistency-axis work; bands unchanged.

## 6. Evidence log

`python3 -I -B`, Python 3.11.15, sympy 1.14.0, run from `pt/C/`. Arguments: `<OIB>` = `../base/verification/lean-mathlib/OIBridge`,
`<FCP>` = `../inputs/fourcopy`. Each decision rule was fixed in the script header before the first run, and pre-run
edits are recorded in NOTES N4. No timing appears in stdout. Each `.err` holds only the appended `exit=0` (sha256
`19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061`). Every replay is byte-identical (`cmp` on `.out`
and `.err`). There were no failed runs and no `.runN.*` files.

| script | sha256 (script) | output | sha256 (output) | checks | verdict | runs; replay |
|---|---|---|---|---|---|---|
| landed `kt4_prem1_probe.py` (c0 replay, read-only) | `c2fdcaafb45bd261abf4809b60a98b1dd3a1c55a84038d72eadecef97baeeec9` (blob `5609d96a`) | `c0_landed_probe_replay.out` | `1873134134102bccaa27a12dfb9afd9ea1a8297fcf5cfe74531adc4696471d8a` | 79 PASS, 0 FAIL | `kt4_prem1_probe: OK -- 79 checks` | 1; identical |
| `c1_cone_level.py <OIB> <FCP>` | `096a98301cabf2040d64b0ad1e0aee2cb45bcfdbc0c5d85cfeb1b320e0a03a6c` | `c1_cone_level.out` | `37053fb7c02617f14d92ed4a955a8867c5fd423ff8e13df0a05261007881d9d0` | 40/40 | `C1-CONE-LEVEL-EXACT` | 1; identical |
| `c2_carrier_models.py <OIB> <FCP>` | `e66c0af8759d611b36aaccfa5a8c4960b3dc14483ef3725ed62b91227f8894b5` | `c2_carrier_models.out` | `403764315700b9c6e4a3f8ffa1cbb661c9ed11c939233fffaebb74f288548dae` | 36/36 | `C2-CARRIER-MODELS-EXACT` | 1; identical |
| `c3_route_ingredients.py <OIB> <FCP>` | `845a914e87f6ae2787e4dbc4476c54e1aadf10f4037f28b9edee82ae4e18f8a4` | `c3_route_ingredients.out` | `ccb06b066c4f4cb67b114fd80d814cad235ac4d2e7354b367b1d969d6e1e54ed` | 17/17 | `C3-ROUTE-INGREDIENTS-EXACT` | 1; identical |
| `c4_supplements.py <FCP>` | `908cc1e9f63930a5abe5dee02fd1a8d1ba8e64b2417fa77108e98a884073d8de` | `c4_supplements.out` | `a0466c6c7d6ad7d46f6b29ec47e3fbcdfcfdddfa1ce9108977f0b8b8e7325673` | 7/7 | `C4-SUPPLEMENTS-EXACT` | 1; identical |
| `c0_census_L.out` (read-only command log, not a script) | — | `c0_census_L.out` | `54adaca796d95eb1fd0b0f85b0e6084952232414687ed9d9da0d4643a687833d` | — | no Lean change since `bcbc516f`; no three-or-more-token declaration at L | — |

Check ids cited above refer to these outputs: c1 S0–S6, c2 S0–S5, c3 S0–S4, c4 S1–S2.

## 7. Integrity

- **Start** (`.start_marker`, 2026-10-10T04:33:48Z, written before any other file): the inputs manifest was silent,
  exit 0; base HEAD was `9f9f8257a980a1819fbbc1dc0019917cf8678626`; `git -C base status --porcelain` was empty; the
  PROTOCOL.md sha256 matched; `pt/C/` was empty.
- **During the run:** amendments 1 and 2 arrived and were hash-verified (NOTES N3, N5). The base status was empty after
  every script run. No file appeared in `pt/C/` that this thread did not write.
- **End** (2026-10-10T05:41:05Z, after the last edit of this file's content above §7):
  - the inputs manifest was silent, exit 0;
  - base HEAD was `9f9f8257a980a1819fbbc1dc0019917cf8678626`, and `git -C base status --porcelain` was empty (0 lines);
  - the sha256 of PROTOCOL.md (`239dc123…`), amendment 1 (`b41aa0e7…`) and amendment 2 (`2a2f78f3…`) matched;
  - there was no `__pycache__` or `.pyc` under `base/`;
  - `pt/C/` held 28 files and no subdirectory, every one written by this thread: `.start_marker`, `NOTES.md`,
    `RESULT.md`, `c0_census_L.out`, and for each of `c0_landed_probe_replay`, `c1_cone_level`, `c2_carrier_models`,
    `c3_route_ingredients`, `c4_supplements` its `.out`, `.err`, `.replay.out`, `.replay.err` (and the `.py` for
    c1–c4);
  - every script and output hash in §6 was recomputed and matched, every replay was again byte-identical, and the
    landed probe's hash was unchanged.
- **Integrity events:** none. No quarantine was needed.
