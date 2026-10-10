# EQ5-PREM — can existing observational principles supply the physical premises of KT(4)? Result (research only)

Base: certified `bcbc516f`, snapshot `scratchpad/eq/base/`. Inputs: the EQ4-F package at `f0d37906`
(`scratchpad/eq5/inputs/`). Protocol: `scratchpad/eq5/PROTOCOL-PREM.md` (sha256 `7d3dcf6f44455650…`, verified), with the
shared rules of `scratchpad/eq5/PROTOCOL.md`. It builds on EQ4-SOURCE (`scratchpad/eq5/SOURCE/`), read with the
coordinator's audit `eqreview/EQ5-SOURCE-AUDIT.md`, and on `eq5/F/DEPGRAPH.md` §7.

Nothing here is adopted, frozen or governed. There was no git write, no CI, and no ROADMAP or manuscript edit. No Lean
toolchain exists, so every Lean text cited from the package is UNBUILT. `scratchpad/eq5/SIX/` was not read. The running
record is `NOTES.md` (N0–N6).

**Evidence tags.**
- **[K]** landed at the base (`file:line` under `verification/lean-mathlib/OIBridge/`). Module abbreviations:
  - CI CompositeInterface, CD CompositeDimension, K2G K2Guard, CA CompletionAction, SC StageCompletion;
  - OG OrbitGeneration, ES EffectSpace, EO EmbeddedObservation, CGO CarrierGeneralOIPlus;
  - RE ReferenceExtension, SB SpectatorBridge, MC MonoidalCompletion, AI AntiunitaryInvariance.
- **[X]** exact computation in this directory, replayed byte for byte (`q0`–`q5`, with check ids).
- **[W]** written argument.
- **[E]** exact exploration (a lead).
- **[X SOURCE …]** evidence of the SOURCE thread, cited with hashes re-checked (§3).

## 0. Answers

**Part A, four-token coherence: NOT SOURCED.**

What is absent:
- No landed or adopted principle implies `TokProdState` or `TokenCoherent` (`tok`) [X q0, q1].
- The programme principles that carry regrouping or token identity are complex-typed and import-separated from the ball
  side [X q0 T1, I1]. They are:
  - embedded observation's `RegroupingInvariant` and `RelabellingInvariant` [K EO:98, :106];
  - OI⁺'s observational independence, which is inert-spectator compositionality [K CGO:73, RE:447, SB:223];
  - `HComp` [K MC:311];
  - the typed interface;
  - the region tower.

  Every route through them imports the complex matrix cone. Observational independence and `HComp` are also (o)-type.
- As sources of `tok`, their field-neutral shadows are refuted by exact countermodels, each of which satisfies the
  shadow while `tok` fails [X q1]:
  - "one body" is refuted by the anchor sum;
  - relabelling covariance is refuted by M_id, M_T and the anchor sum;
  - operation-level token identity for reversible token operations is refuted by the new antipodal model **M_θ** and by
    the anchor sum.

What survives every countermodel is token identity itself. It comes in forms that range from restatements to one
strictly weaker premise:
- the restatements: TokProdState; regrouping invariance of token-product statistics; four-token product data;
  token-indexed carriers;
- the weaker premise: **first-order independent preparation (IP₁).** Take independently prepared pure token states.
  The single-token marginals that one grouping reads on the other grouping's product state are the prepared states.

**Theorem A (new):** IP₁ implies `tok` under three conditions [W + X q2, q1]:
- local tomography of one grouping (COMP-1's `lt`, i.e. the `KT4LT` form);
- one body;
- admissible pair cones (PairAdm; the maximal-cone bound is what the key lemma uses).

Local tomography and one body are load-bearing, and so are all four tokens of IP₁ and, inside the key lemma, purity
and positivity [X q1, q2]. PairAdm is part of every KT(4) statement and was not tested separately.

IP₁ is not a restatement of `tok`. It constrains 12 marginal values on product preparations, and it reaches `tok` only
through a purity lemma and local tomography. It is still a token-identity premise, and nothing at the base supplies it.

Identity for irreversible token operations (discard-and-prepare) also survives, and gives TokProdState under a span
condition [X q5 + W]. It is an (o)-type premise.

**Part B, gate preservation: NOT SOURCED.**

Refuted formulations. Every formulation of physical reversibility or operational availability that does not restate
gate preservation is refuted by an exact countermodel [X q3, q4]:
- K1 (`IsNot`, `NativeGate`, `Entangling`), K1-BRIDGE-1/EFF-1 availability, and N-CLASS with CandidateCone, convex cone
  and closedness: refuted by the landed bodies MAX and MIN with `cnot`, and by TWIN;
- product-level reversibility: refuted by MAX;
- self-duality and the IIP-1 isometry: refuted by TWIN.

**New countermodel TWIN = (twin, `cnot`).** The cone is self-dual, IE₁, closed and a CandidateCone. Its gate is
N-CLASS and satisfies every K1 premise. Yet `cnot` does not preserve it.
- hgate's content is the alignment of the gate's chart with the cone's chart.
- No principle that is blind to that alignment can supply it.

Surviving formulations. Each restates hgate (∧ hinv ∧ hcl) on the whole body, on generators, or by duality:
- COMP-1 `JointReversible` / `PreservesBody` of the pair body;
- effect-side availability (V4′ transported);
- K∞-Act transported to the pair (OPACT-1 operation data on the pair's completed body);
- the operational completion of the product states under the gate.

The weakest additional principle is "the native gate is an automorphism of the standalone pair's state space". In the
programme's own vocabulary this is K∞-Act for the pair, from which the base derives body preservation [K seams audit
:44]. It is a restatement.

Four-copy consistency does not supply hgate either. Uniform SEP and uniform maxCone are FourCopyCoherent, and `cnot`
preserves neither [X q3 F + W].

**Part C (record).** Stage completion's body is closed by definition, so a completion-body route that supplies hgate
also supplies hcl. COMP-1 bodies are only convex. Details are in §1.C.

**The owner's caution.** Nothing here derives `tok`, hgate or a quantum cone from the observational axioms.
- Every positive statement is a sufficiency statement with named, unsourced premises.
- Every negative statement is an exact model of the stated premises in which the target fails. Such a model shows
  insufficiency only.

## 1. Answers to A1–A3, B1–B3 and C

### 1.A1 The predicates on the KT(4) data, and their relations

**Setting.** KT4⁻ is `KT4` without `tok` (package :262–267):
- PA : PreComposite (pairBody K01) (pairBody K23) V;
- PB : PreComposite (pairBody K02) (pairBody K13) V;
- `one_body : PA.Ω = PB.Ω`.

The pair cones are PairAdm (CandidateCone ∧ IsConvexCone).

Notation:
- The A-table is T_A(ω)_abcd = PA.prodEff (tabCoord a b) (tabCoord c d) ω.
- The B-table, in token order, is T_B(ω)_abcd = PB.prodEff (tabCoord a c) (tabCoord b d) ω.
- For token Bloch vectors x = (x₀, x₁, x₂, x₃):
  - p_A(x) = PA.prodState (flatW (prodState x₀ x₁)) (flatW (prodState x₂ x₃));
  - p_B(x) = PB.prodState (flatW (prodState x₀ x₂)) (flatW (prodState x₁ x₃));
  - H(x) = hom x₀ ⊗ hom x₁ ⊗ hom x₂ ⊗ hom x₃.
- `tok` is T_A = T_B on PA.Ω (package :253–257).

Four facts are used throughout:
- **F1, vanishing on the body.** `unitEff` and `tabCoord 0 0` agree on every pair body. So on PA.Ω, and likewise on PB.Ω,
  the table determines every product-effect value [W; ingredients `exists_effect_rescale` K CI:148 and
  `prodEff_expand` K CI:290; SOURCE §3.7].
- **F2, token-product effects.** For effects g, g′ of the ball, set t(g, g′) := Σ ĝ_a ĝ′_b tabCoord a b. It is an
  `IsEffectOn` effect of pairBody K whenever K ⊆ maxCone (eball 3), i.e. under CandidateCone.2 [W]:
  - nonnegativity is the definition of maxCone [K CD:186];
  - the upper bound is the complement identity.
- **F3, evaluation.** T_A(p_A(x)) = H(x) and T_B(p_B(x)) = H(x), by each grouping's `prodEff_apply` [X q1 V1, and the
  M_σ rows].
- **F4, span.** The tables H(x), for x ∈ S⁴ with S = {e_x, e_y, e_z, −e_z}, form a basis of W4 [X q2 L4].

**The predicates.**

| name | statement on the KT4⁻ data | informal reading |
|---|---|---|
| IP₀ | each grouping's product states lie in Ω, and its product effects factorize on its own products | independent preparation within one grouping (automatic: `prod_mem`, `prodEff_apply`, COMP-1 L1 [K CI:306]) |
| **IP₁ᴮᴬ** | for pure x and every token t, the token-t entries of T_A(p_B(x)) are hom x_t | first-order independent preparation across groupings |
| IP₁ᴬᴮ | the same for T_B(p_A(x)) | the mirror |
| IPᴮᴬ, IPᴬᴮ | T_A(p_B(x)) = H(x); T_B(p_A(x)) = H(x) | full independent preparation across groupings |
| STMC | T_A and T_B agree on all of Ω on the 13 index patterns with at most one nonzero index | single-token marginal coherence (SOURCE CP4) |
| TPS | p_A(x) = p_B(x) | `TokProdState` (SOURCE CP1) |
| RI₀ | PA.Ω = PB.Ω | regrouping invariance as one body (the field `one_body`) |
| RI_L | some affine automorphism Φ of V with Φ(Ω) = Ω carries PA's product data to PB's | regrouping invariance as relabelling covariance |
| RI_op | PA.prodEff (t(g₀,g₁)) (t(g₂,g₃)) = PB.prodEff (t(g₀,g₂)) (t(g₁,g₃)) on Ω, for all affine g | regrouping invariance of token-product statistics |
| tok | T_A = T_B on PA.Ω | `TokenCoherent` |

**Relations.** All are relative to KT4⁻ with PairAdm cones. Each implication has its own witness. LT(·) is COMP-1's
`lt` for that grouping.

- **R1. tok ⟺ RI_op.**
  - (⇒) Expand t(g, g′) in `tabCoord` and use the bilinearity of `prodEff`.
  - (⇐) Take basis functionals: t(e_a, e_b) = tabCoord a b.
  - [W] RI_op is `tok` in other words: a relabelling.
- **R2. tok ⇒ STMC ⇒ IP₁ᴮᴬ, IP₁ᴬᴮ.**
  - The first arrow is specialization.
  - The second: STMC at p_B(x) ∈ PB.Ω = PA.Ω, then F3 [W].
  - The converses fail without LT [X q1 S1, S3]: PAD3 has STMC, IP₁ and ¬tok; PAD1 has IP₁, ¬STMC and ¬tok.
- **R3. tok ⇒ IPᴮᴬ, and TPS ⇒ IPᴮᴬ ∧ IPᴬᴮ** [W]. The first: `tok` at p_B(x) ∈ PA.Ω, then F3. The second: F3, with
  no LT.
- **R4. IP₁ᴮᴬ ⇒ IPᴮᴬ,** given one body and K01, K23 ⊆ maxCone. This is the purity lemma below [W + X q2].
  Symmetrically, IP₁ᴬᴮ ⇒ IPᴬᴮ given K02, K13 ⊆ maxCone.
- **R5. IPᴮᴬ ∧ LT(PB) ⇒ tok** [W]:
  1. T_A and T_B agree on the B-products (IPᴮᴬ and F3).
  2. T_B is injective on Ω (LT(PB) with F1).
  3. T_B(Ω) lies in the normalized slice of W4, which is the affine span of the T_B-images of the B-products (F4).
  4. T_A ∘ T_B⁻¹ is affine on T_B(Ω) and is the identity on an affinely spanning subset, so it is the identity.

  Symmetrically, IPᴬᴮ ∧ LT(PA) ⇒ tok.
- **R6. IPᴮᴬ ∧ LT(PA) ⇒ TPS** [W]. T_A(p_B(x)) = H(x) = T_A(p_A(x)), with both points in PA.Ω; then F1 and LT(PA).
  With CandidateCone.1 and LT(PA), TPS ⇒ tok (SOURCE §3.7 (⇐)) [W; X SOURCE s1 T4].
- **R7. tok ∧ LT(PA) ⇒ TPS** (SOURCE §3.7 (⇒)). Without LT, tok ⇏ TPS (PAD2) and TPS ⇏ tok (PAD1) [X q1 S1, S2].
- **R8.** RI₀ ⇏ tok, TPS: the anchor sum. RI_L ⇏ tok, TPS [X q1]:
  - M_id with Φ = id;
  - M_T with Φ = σ∘τ₁;
  - both anchor members, with Φ the swap.
- **R9. One body is load-bearing in R4.** SEPB has IP₁ᴮᴬ and LT(PA), separate bodies, and ¬tok. A product of token
  effects of PA takes the value −1/2 at a PB product, so no common body exists [X q1 S4].
- **R10. All four tokens are load-bearing.** In M_tw and M_θ, IP₁ᴮᴬ holds at tokens 0, 1 and 2, fails at token 3, and
  tok fails [X q1 S5].

**The purity lemma** [W; ingredients X q2].

Statement. Let T be a normalized n-token table that is nonnegative on every product of effects of the 3-ball, and whose
single-token marginals x₁, …, x_n are pure (|x_t| = 1). Then T = hom x₁ ⊗ … ⊗ hom x_n.

Proof:
1. Fix effects F = (f₂, …, f_n) on tokens 2..n. The functional g ↦ T(g, F) is nonnegative on the effect cone of the
   ball, which is the Lorentz cone Lor [K CD:869, CD:930 `lor_ehom`, CD:916 `isEffectOn_affOf`]. Lor is self-dual, so
   the coefficient vector c_F lies in Lor.
2. Replacing f₂ by u − f₂ gives c_F′ ∈ Lor with c_F + c_F′ = c_(u, f₃, …). Telescoping down to all-unit effects gives
   the marginal hom x₁.
3. When |x₁| = 1, hom x₁ spans an extreme ray of Lor (the Cauchy–Schwarz equality case; the identity behind it is
   q2 L2). Both summands of a decomposition of an extreme-ray vector lie on that ray.
4. So every c_F is a multiple of hom x₁, and T(g, F) = g(x₁) T(u, F). That is, T factorizes in token 1 (q2 L3).
5. The remaining (n−1)-token table is normalized, nonnegative on product effects, and has pure marginals. Induct. □

The two-token core of the step is the exact identity set q2 L1. Write T = hom z ⊗ hom y + C. Positivity at
g_z = (1, −z)/2, together with T(g_z, u) = 0, forces zᵀC = 0. Then |c⃗_f|² − c_(f,0)² = |Cf|², so the Lorentz condition
forces C = 0.

Countercontrols:
- **Purity is load-bearing.** The classically correlated table with mixed marginals is nonnegative on all product
  effects and is not a product [X q2 CC1].
- **Positivity is load-bearing.** A non-product table with pure marginals has the exact negative product-effect value
  −1/40 [X q2 CC2].
- **Leads [E].** Four STMC-respecting twists of W4 each get an exact negative product-effect witness at an axis-aligned
  pure product: −1/2, −1/8, −1/2 and −1/8 [q2 LEAD lines]. This includes SOURCE's e1 twist.

**Application (R4).** Take pure x and set T := T_A(p_B(x)).
- T is normalized (F1).
- T is nonnegative on products of token effects (F2, one body, `PA.prodEff_effect`).
- By IP₁ᴮᴬ its marginals are the pure x_t.

So T = H(x). By multi-affinity in x (PB.prodState and prodState are affine in each argument), T_A(p_B(x)) = H(x) for
every x in the ball.

**Theorem A (first-order token identity suffices; new).** Let H be KT4⁻ data with PairAdm pair cones, and let PA or PB
be locally tomographic. Then IP₁ᴮᴬ ⟹ `TokenCoherent`.
- Route [W]: R4, then R5 if LT(PB) holds, or R6 and SOURCE §3.7 if LT(PA) holds.
- Exact ingredients: q2 L1–L4 and q1.
- These hypotheses are load-bearing (PairAdm, assumed throughout, was not tested separately):
  - LT: PAD1, PAD3;
  - one body: SEPB;
  - the fourth token: M_tw, M_θ;
  - purity and positivity inside the lemma: q2 CC1, CC2.
- Every step is (s)-type. None uses IE₁, IE₂, the quantum cone, the region tower, or an (o) step.

**Corollary A′.** Relative to KT4⁻ + PairAdm + LT of one grouping, these are equivalent:

  tok ⟺ IP₁ᴮᴬ ⟺ IP₁ᴬᴮ ⟺ STMC ⟺ IPᴮᴬ ⟺ IPᴬᴮ ⟺ RI_op.

- Each (⇒) is by specialization (R1–R3).
- Each (⇐) is through Theorem A or its mirror.
- With LT(PA), the list also includes TPS (R6, R7).
- It suffices to assume IP₁ᴮᴬ on the 4⁴ = 256 products of the states e_x, e_y, e_z, −e_z. The marginal map is
  multi-affine in x, and these states affinely span the ball (q2 L4).

**P/A/C.** Theorem A is a sufficiency statement. IP₁ is not necessary for the headline conclusion: M_id and M_T satisfy
`KT4LT` minus `tok` and the conclusion, and IP₁ fails in both [X q1; X SOURCE s1 I1–I2 + W]. No necessity is claimed.

**The two A1 notions, answered.**

"Independent preparation" splits into three levels:
- within a grouping (IP₀): automatic;
- across groupings at first order (IP₁);
- across groupings in full (IP).

"Regrouping invariance" also splits into three:
- one body (RI₀): vacuous;
- relabelling covariance (RI_L): refuted;
- invariance of token-product statistics (RI_op): `tok` itself.

How they relate to TokProdState and TokenCoherent:
- Without local tomography they separate (PAD1–PAD3, SEPB).
- With local tomography of one grouping, IP₁ (first order, on product preparations, one direction) already carries all
  of `tok` (Theorem A).

### 1.A2 Census of the programme (full table in §2.A)

Refutation rule: a countermodel refutes "candidate ⇒ target" iff it satisfies the candidate and violates the target,
with target `tok` or TPS. All six countermodels violate both targets [X q1 C2]:
- the five SOURCE countermodels: the anchor sum (members ANCc and ANCz), M_ρ, M_tw, M_id, M_T;
- the new model M_θ.

**The new model M_θ** [X q1, q4 + W]. M_θ is M_tw with token 3's reflection ρ = actT reflY replaced by the antipodal
map θ = actT(−id).
- PB.prodState L L′ = σ(pState L (θL′)), PB.prodEff E F = pEff E (F∘θ) ∘ σ, and the body is ι(B4).
- θ maps twin onto Q3: at the Pauli level θ = Ad(σ_y)∘T [X q1 V4]. So the PSD assembly of M_tw applies unchanged:
  - cross values: fourVal X Y Ẽ (θF̃) and fourVal ẽ f̃ L (θL′) [X q1 V3];
  - evaluation laws [X q1 V1].
- The pair data are those of M_tw: cones (Q3, Q3, Q3, twin) and gates (cnot, cnot, cnot, cnotTw). Every pair premise
  holds [X SOURCE s1 P2, P3, P6, R5, R6; X q4 for cnotTw's K1 clauses].
- Local tomography holds for both groupings [X q1 LTA, LTB].
- tok fails, and so does `kt4_forward`'s parity conclusion: the twist bits are forced to (0, 0, 0, 1) [X q1; X SOURCE s1
  R6].
- **Operation-level token identity for every local rotation holds.** θ commutes with every rotation, so a rotation of
  token 3 acts identically through both groupings [X q1 OLTI, four rational rotations; W for all of SO(3)].

Interpretation [W]: M_θ is the one-token analogue of the antiunitary ambiguity that the base shows invisible to all
circuit data at the global level [K AI header: a simultaneous transpose of every object preserves every circuit
probability]. Here it acts at one token through one grouping. KT(4)'s cross-grouping consistency would detect it, but
only through `tok`.

**Schema for pair-level and single-system principles** [X q1 + W].
- M_id has exactly the pair data of the token-coherent M_σ for uniform Q3 with `cnot` gates, and `tok` fails in it.
- So any principle that is a predicate on pair data (pair cones, gates, single-token bodies and their operations) and
  holds for the two-copy quantum theory is refuted by M_id.
- For the odd pattern, the same holds with M_ρ, M_tw and M_θ, whose pair premises hold [X SOURCE s2, X q4].
- This covers the remaining census candidates: K1, K2, K∞ (including Copy), Kₙ as stated, SC/CMP-1, ORD-1, IIP-1,
  OPACT-1, EFF-1, K1-BRIDGE-1, TRB-1, OG-1, NB-1, DIM-1, COMP-1 L1/L9, and operational no-signalling.

**The matrix-world principles.** Their stated forms are complex-typed and import-separated from the ball side [X q0 T1,
I1], and are flagged circular. Their field-neutral shadows:

| programme principle | field-neutral shadow | verdict |
|---|---|---|
| embedded observation (R) | RI₀ | refuted (anchor sum) |
| embedded observation (L) | RI_L | refuted (M_id, M_T, anchor sum) |
| observational independence / inert spectators / H_comp, restricted to reversible token operations | OLTI-rev | refuted (M_θ, ANCc) |
| observational independence restricted to irreversible token operations | OLTIres | not refuted: it fails in every countermodel, M_θ included; (o)-type [X q5] |
| typed interface, whose coherence "is automatic for a typed theory" because carriers are product types [K typed-completion audit :57–60] | token-indexed carriers (TIC) | a relabelling that also carries four-copy local tomography |

### 1.A3 The survivors

**Relabellings: `tok` or TPS with token identity built into the statement, the carrier or the labels.**
- TPS (SOURCE CP1).
- RI_op (R1).
- Four-token product data (SOURCE CP2).
- TIC.
- A joint four-token protocol tower with token-indexed labels (SOURCE CP3; not landed; finite classical towers give
  polytopes, so it has no ball-token instance).

**Reductions: not restatements, unsourced.**
- **IP₁ (weakest), IP and STMC.** Derivation: Theorem A and Corollary A′.
- **Independence assessment of IP₁:**
  - It is motivated as the minimal operational meaning of "the same four tokens": a token prepared in x is found in x by
    single-token tests, whichever pair it is grouped with.
  - It is also the operational content, read on the four-token body, of the package's built-in per-token charts
    (DEPGRAPH §7.4). This sharpens SOURCE row 13: chart sharing at first order already carries all of `tok`, given LT.
  - It is not stated anywhere in the programme [X q0 F: no cross-grouping vocabulary in the field-neutral core].
  - It is a token-identity premise at first order. It reduces what a source must deliver. It does not supply it.

**(o)-type: OLTIres.** For every token t and pure state s, an affine self-map of (V, Ω) resets token t to s in every
product of both groupings.
- Derivation [W + X q5 D]:
  1. The composite of the four resets is constant on the affine span of the A-products.
  2. Where the B-products lie in that span, B-covariance gives p_B(s) = p_A(s).
  3. Hence TPS, and then `tok` given LT(PA).
- The span condition holds on the COMP-1 coordinate carrier with bodies in ι(W4): the A-products span the normalized
  slice of ι(W4) [X q5 C2], and the B-products lie in it [X q1, the LTA rows]. It is an extra condition in general.
- Status: [U]. Its matrix-world ancestor, observational independence, is landed only as a complex-typed definition.
  Flagged (o): it is an operation on part of the four-token composite.
- **Finding:** in an observational-independence-type principle, the token-identity content sits in the irreversible
  token operations (discard-and-prepare), not in the reversible ones (M_θ).

### Outcome A: NOT SOURCED

- No landed or adopted principle implies TokProdState or `tok`.
- No independently motivated principle stated elsewhere in the programme implies it without a flag. The stated
  principles that would do so are complex-typed (circular) or (o)-type, and their field-neutral shadows are refuted or
  are relabellings.
- **Weakest additional principle found:** IP₁ᴮᴬ, together with local tomography of one grouping (COMP-1's `lt`; the
  `KT4LT` form).
- **Is it a restatement?** No: it is strictly weaker as a formula and reaches `tok` only through Theorem A. But it is a
  first-order token-identity premise.
- **Caveat on counting premises:** replacing `tok` by IP₁ in a headline uses `KT4LT`, i.e. local tomography of one
  grouping. LT is a COMP-1 `Composite` field and is K2 OPEN as a source.

### 1.B1 Physical reversibility and operational availability at the pair body

The landed vocabulary:
- `PreservesBody Ω G` [K OG:69] says each g ∈ G maps Ω into Ω and so does g⁻¹. COMP-1's `JointReversible` is this
  predicate for a composite body [K CI:445].
- OPACT-1's `OpDatum` maps every stage preparation into the completed body [K CA:46–48]. With `AffineRespect` and an
  inverse datum it induces a body-preserving affine equivalence [K CA:352].
- DIM-1's `NativeGate` positivity is product-level: `posFwd`, `posInv` [K CD:222–223].
- K1-BRIDGE-1's `NativeGateOf` replaces maxCone by an available family's cone [K K1Bridge:49]. With every effect
  available that cone is maxCone [K ES:415].

The precise formulations, for a pair (K, N):

| formulation | statement |
|---|---|
| PR, physical reversibility | N is an affine automorphism of the pair body: `PreservesBody` (normalized slice of K) {N}. Equivalent to hgate ∧ hinv, by scaling, since N fixes ω₀₀ [W]. |
| PRP, product-level reversibility relative to K | N and N⁻¹ map every product state into K |
| OA, operational availability | N maps states to states. On the body this is hgate. On a generating set of preparations, with the body their completion, it is OPACT-1's `mem_body` (K∞-Act for the pair). In the Heisenberg picture it is N*(dualW K) ⊆ dualW K, which for closed convex K is hgate by the bipolar theorem [W]. |
| EFF-1 / K1-BRIDGE-1 availability | the product-level `NativeGateOf` with the full effect family |
| K1 | `IsNot`, `NativeGate` and `Entangling` for N |

### 1.B2 Tests (full table in §2.B)

The landed countermodels, re-derived [X q3]:
- **MAX.** idW ∈ maxCone: the pairings on the generators of the effect cone are 1, ½, ½ and (1 + b·c)/4. But
  cnot idW = chainW takes the value −½ at a sharp pair.
- **MIN.** F(ω) = ω₀₀ − ω₁₁ + ω₂₂ − ω₃₃ is a sum of squares on products, while F(phiW) = −2 and
  phiW = cnot(prodState xplus z3).

**The new countermodel TWIN = (twin, cnot)** [X q3 G-TWIN + W]. Its properties:
- **CandidateCone.** The products lie in twin: t1, t2 (pauliW(prodState x y) = r(x) ⊗ r(y)). And twin ⊆ maxCone: t3.
- **Closed convex cone** [W].
- **Self-dual** [W: t6 + Q3 self-dual].
- **IE₁** [W].
- **The gate.** `cnot` is N-CLASS with identity locals and satisfies `NativeGate` [K CD:1160; t5] and `Entangling`
  [K CD:1380].
- **IIP-1 isometry** [W: t7 + Ad SU(4) irreducible]. `cnot` is an orthogonal signed permutation fixing e₀₀, the
  centroid. The IIP-1 form of twin is Euclidean.
- **hgate fails** (t4): prodState xplus z3 ∈ twin, but cnot of it is phiW ∉ twin, since actT reflY phiW = idW and
  v†pauliW(idW)v = −1.
- **hinv fails**, since `cnot` is an involution.

What the tests show:
- K1, NativeGateOf with full effects, and the pair premises are refuted by MAX, MIN and TWIN.
- PRP is refuted by MAX.
- Self-duality and the IIP-1 isometry are refuted by TWIN.
- IE₁ of the cone also holds in all three. As a premise it would be flagged anyway (IE₁ as a premise).

**Chart-blindness** [W]. Let P = P_gate(N) ∧ P_cone(K), where:
- P_gate holds for `cnot`;
- P_cone holds for Q3 and is invariant under K ↦ actT reflY K.

Then TWIN satisfies P and violates hgate. Self-duality, IE₁, CandidateCone, closedness, the IIP-1 form, and every K1 or
availability clause are of this form. So hgate's content is the alignment of the gate's chart with the cone's chart. In
Theorem C's form K_p = twistQ3 (orient A_p B_p), hgate is where the gates' orientation enters the classification.

**Four-token level** [X q3 F + W].
- FourCopyCoherent's two families factorize on generators for uniform SEP and for uniform maxCone.
- So both are FourCopyCoherent, and KT4 data exist by SOURCE §3.6 (⇒).
- With `cnot` gates, hcls, hadm and hcl hold and hgate fails. KT(4) does not supply hgate (cf. DEPGRAPH §7.6).

A remark, recorded only: uniform (twin, cnot) satisfies every hypothesis of `kt4_forward` except hgate and hinv. It also
satisfies `kt4_forward`'s existential conclusion with τ ≡ 1, though not Theorem C's `orient` form. So the existential
headline does not display the gate–cone alignment [W; uniform twin is FourCopyCoherent by the per-token chart transport
ε = (0, 1, 1, 0), the package's open `fourCopyCoherent_chart`].

### 1.B3 The survivors

Each survivor is a restatement of hgate, in one of three forms:
- **On the whole body:** JR / `PreservesBody` (= hgate ∧ hinv).
- **On generators:** OPACT-1 operation data on the pair's completed body, i.e. K∞-Act transported. Its operative clause
  `mem_body` is N(preparation) ∈ body, and its `body` is closed [K SC:141–142], so it bundles hgate ∧ hinv ∧ hcl. The
  operational completion of the products under the gate is the same plus minimality.
- **By duality:** effect-side availability, i.e. V4′ transported [K OG:74 for the single-system predicate]. For closed
  convex K it is hgate by the bipolar theorem.

K∞-Drive transported is the same: flows preserve the body by definition.

None of the landed countermodels satisfies any of these, as expected [X q3 T-consistency].

### Outcome B: NOT SOURCED

- **Weakest additional principle:** the native gate is an automorphism of the standalone pair's state space.
- In the programme's vocabulary this is K∞-Act for the pair. The seams audit already derives body preservation from
  K∞-Act for the elementary system [K kinf-seams-audit :44].
- K∞-Act is OPEN and unsourced [K ROADMAP :1014].
- **Is it a restatement?** Yes, of hgate ∧ hinv (and hcl in the completion form).
- Every non-restating formulation is refuted by MAX, MIN or TWIN.

### 1.C Closedness (`hcl`): record only

- **C1.** Stage completion supplies closedness by definition: `body D` is the closure of the convex hull of the
  preparation vectors [K SC:141–142]; `body_isClosed` [K CA:202]. A route that realizes the pair body as a completion
  body (the B3 family) delivers hcl, hgate and hinv as one operational bundle.
- **C2.** COMP-1's body is only convex [K CI:226]. The min and max bodies of compact factors are closed [W]. SOURCE's
  closure foil shows that hgate ∧ hinv ⇏ hcl.
- **C3.** MAX, MIN and TWIN are all closed, so closedness does not help hgate [X q3].
- **C4.** Two uses of closedness are cited, not re-derived [DEPGRAPH §4.2 (R), §7.2]:
  - under orthogonality and closedness, hinv follows from hgate;
  - closedness is redundant for the parity conclusion.
- **C5.** Theorem A uses no closedness. TWIN's IIP-1 check uses compactness of the normalized slice [W].

## 2. Candidate tables

Verdict codes:
- **R**: refutes. The candidate holds and the target fails there.
- **n**: the candidate fails there. No refutation.
- **—**: not a predicate on these data. The reason is in the last column.

### 2.A Part A (targets `tok` and TPS)

The six countermodels violate both targets [X q1 C2]. Status codes:
- [K] landed (as a theorem, or as a definition whose assertion is not landed, where so marked);
- [A] adopted;
- [T] transported (a single-system or two-copy statement applied per token or per pair);
- [U] unsourced.

The ANC column covers the two members, ANCc (anchors at the pair-body centre) and ANCz (anchors at the +z product).

| # | candidate (anchor) | status | ANC (c / z) | M_ρ | M_tw | M_id | M_T | M_θ | survives | independence, flags |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RI₀ one body (field `one_body`; shadow of EO (R)) | (R) [K EO:98, complex]; shadow [U] | R / R | R | R | R | R | R | no | vacuous |
| 2 | RI_L relabelling covariance (shadow of EO (L)) | (L) [K EO:106, complex]; shadow [U] | R / R | — (pair bodies differ) | — | R | R | — | no | — |
| 3 | OLTI-rev, rotations of a token act identically through both groupings (shadow of observational independence / inert spectators / H_comp on reversible operations) | [K CGO:73, RE:447, SB:223, MC:311, complex]; shadow [U] | R / n | n | n | n | n | **R** | no | (o) |
| 4 | OLTIres, resets of a token act identically through both groupings (irreversible part) | shadow [U] | n / n | n | n | n | n | n | yes | ⇒ TPS under the span condition [W + X q5]; (o) |
| 5 | STMC (SOURCE CP4) | [U] | n / n | n | n | n | n | n | yes | ⇒ tok with LT (via IP₁); not a restatement |
| 6 | **IP₁ᴮᴬ** (also IP₁ᴬᴮ) | [U] | n / n | n | n | n | n | n | yes | weakest; Theorem A; not a restatement; token identity at first order |
| 7 | IPᴮᴬ, IPᴬᴮ | [U] | n / n | n | n | n | n | n | yes | ⇒ tok with LT; reduction |
| 8 | TPS (SOURCE CP1) | [U] | n / n | n | n | n | n | n | yes | ⟺ tok given LT(PA) (SOURCE §3.7); relabelling |
| 9 | RI_op | [U] | n / n | n | n | n | n | n | yes | ⟺ tok by R1; relabelling |
| 10 | four-token product data (CP2) / token-indexed carrier TIC (shadow of the typed interface's product-type coherence, typed-completion audit :57–60) | [U]; ancestor [K, complex] | n | n | n | n | n | n | yes | relabelling; TIC also carries four-copy LT |
| 11 | joint four-token protocol tower (CP3; PT/CT, SA-LEDGER) | not landed | — | — | — | — | — | — | — | relabelling (token-indexed labels); finite classical towers give polytopes; CT routes through RegionTower: flag |
| 12 | K1: `IsNot`, `NativeGate`, `Entangling` per pair | [U] premises (K1 CONDITIONAL, ROADMAP:984–1000); landed for cnot [K CD:838, :1160, :1380] | R | R | R | R | R | R | no | pair data only (q4 for cnotTw) |
| 13 | K∞-Copy, one common NOT per token type | [U] (ROADMAP:1027) | R | R | R | R | R | R | no | all gates use nflip [X q4 N4] |
| 14 | K2, the two-copy composite: LT, cone, local actions | [U] (OPEN, ROADMAP:1001) | R | R | R | R | R | R | no | pair data only |
| 15 | K∞ single-system seams: Stage, Act, Drive, Trans, Seed, V4, Geom | [U] (OPEN, ROADMAP:1007–1057) | R | R | R | R | R | R | no | single-token data, unconstrained by KT(4) [W] |
| 16 | Kₙ as stated | [U] (OPEN, ROADMAP:1058) | R (iterated-composite reading) | R | R | R | R | R | no | K3 interfaces complex [kn census §3] |
| 17 | stage completion / SC∞ (CMP-1), ORD-1, IIP-1, OPACT-1, EFF-1, K1-BRIDGE-1, TRB-1, OG-1, NB-1, DIM-1 | [K] | R | R | R | R | R | R | no | single-system or two-copy |
| 18 | COMP-1 L1 `margA_prodState`, L9 `condA_prodState` (within-grouping marginals, no signalling on products) | [K CI:306, :332] | R | R | R | R | R | R | no | within one grouping; IP₁ is their cross-grouping analogue |
| 19 | operational no-signalling (adopted Bell branch, Main.md:82, :628) | [A] (not in the posit ledger) | R | R | R | R | R | R | no | within one composite |
| 20 | Axiom 1, tokened differentiation (Main.md §1.2) | [A] (axiom) | R (vacuous) | R | R | R | R | R | no | not about composites |
| 21 | Lemma 2 product decomposition; substratum site identity | Main.md §1.2 | — | — | — | — | — | — | — | no landed lift to the ball side [X q0 I1]; the lifting is Main.md's open hypothesis (:82) |
| 22 | region-tower site identity | [K, complex] | — | — | — | — | — | — | — | circular: imports the complex matrix cone |
| 23 | matrix-world forms of rows 1–4 and 10 (EO, OI⁺, H_comp, typed interface) | [K, complex; characterizations, not asserted] | — | — | — | — | — | — | — | circular (complex); OI and H_comp also (o) |

### 2.B Part B (target hgate)

| # | candidate (anchor) | status | MAX | MIN | TWIN | survives | independence, flags |
|---|---|---|---|---|---|---|---|
| 1 | K1: `IsNot`, `NativeGate` (product-level two-sided positivity), `Entangling` | [U] premises; landed for cnot [K CD:838, :1160, :1380] | R | R | R | no | gate-only |
| 2 | NativeGateOf with full-effect availability (EFF-1 / K1-BRIDGE-1) | [K K1Bridge:49, ES:415]; availability premises [U] | R | R | R | no | product-level |
| 3 | N-CLASS + CandidateCone + IsConvexCone + IsClosed (the other pair premises) | hcls [U] route; hadm [T]; hcl [U] | R | R | R | no | — |
| 4 | self-duality, dualW K = K | [U] ("a stronger independently sourced alternative such as self-duality … not presently sourced", ROADMAP:1040–1043) | n | n | **R** | no | cone-only, chart-blind |
| 5 | IIP-1 isometry: N preserves the body's invariant inner product and centroid | IIP-1 [K] for automorphisms; as a premise [U] | — (not computed) | — (not computed) | **R** | no | chart-blind |
| 6 | IE₁ of the cone | the headline's own conclusion | R | R | R | no | [W] (each cone is invariant under local rotations); flagged: IE₁ as a premise |
| 7 | PRP: N and N⁻¹ map the products into K | [U] | **R** | n | n | no | — |
| 8 | KT(4) with every pair premise except hgate (four-copy consistency), uniform cones with cnot | [U] | R (uniform maxCone FourCopyCoherent) | R (uniform SEP FourCopyCoherent) | R (uniform twin, by the per-token chart transport; package's open `fourCopyCoherent_chart`) | no | [X q3 F + W]; SOURCE §3.6 (⇒) supplies the KT4 data |
| 9 | JR / `PreservesBody` of the pair body under {N} | predicate [K CI:445, OG:69]; assertion [U] | n | n | n | yes | restatement: hgate ∧ hinv |
| 10 | effect-side availability: N*(dualW K) ⊆ dualW K (V4′ transported) | V4′ [K OG:74] single-system; pair [U] | n | n | n | yes | restatement by duality (with hcl) |
| 11 | K∞-Act for the pair: OPACT-1 operation data on the pair's completed body | OPACT-1 [K CA:46, :352]; K∞-Act [U] (OPEN, ROADMAP:1014) | n | n | n | yes | restatement on generators; also gives hcl |
| 12 | operational completion: pair body = closed hull of the products' orbit under the gate | [U] (stage-level product of towers open, COMP-1 result :105) | n | n | n | yes | restatement plus minimality |
| 13 | K∞-Drive for the pair: N on a flow of body automorphisms | [U] | n | n | n | yes | restatement (flows preserve the body by definition) |
| 14 | substratum reversibility (Main.md Lemma 3, posit (iii)) | [A] | — | — | — | — | needs the unlanded operational lifting; through the region tower it is complex (flag) |

## 3. Evidence log (sha256, first 16 hex digits)

Running conditions:
- Every script runs as `python3 -I -B` from `scratchpad/eq5/PREM/`.
- Each decision rule was fixed in the script header before the first run.
- Pre-run edits are recorded in NOTES N3.
- No timing appears in stdout. Each `.err` holds only the appended `exit=0` (sha `19eaf43821a7660e`).
- Every replay is byte-identical (`cmp` on `.out` and `.err`).
- Python 3.11.15, sympy 1.14.0. There were no failed runs and no `.runN.*` files.

| script | sha | output | sha | checks | verdict | runs |
|---|---|---|---|---|---|---|
| `q0_census.py` | `a64bf2636650ea77` | `.out` | `db99032569b6e59e` | 11/11 | `Q0-CENSUS-COMPLETE` | run 1; replay identical |
| `q1_tok_models.py` | `db688057771bfe0a` | `.out` | `9dded6d5707e9406` | 13/13 | `Q1-PART-A-MODELS-EXACT` | run 1; replay identical |
| `q2_purity.py` | `a9f95269a0a61cb6` | `.out` | `d24a769210c29707` | 8/8 | `Q2-PURITY-LEMMA-INGREDIENTS-EXACT` (and 4 leads) | run 1; replay identical |
| `q3_gate.py` | `4be541b1f28d8637` | `.out` | `5907132ff66297e1` | 7/7 | `Q3-PART-B-GATE-EXACT` | run 1; replay identical |
| `q4_pair_gates.py` | `2d92ca5af97c3b71` | `.out` | `5e643f28a4bd4e19` | 5/5 | `Q4-PAIR-GATES-EXACT` | run 1; replay identical |
| `q5_resets.py` | `38b448576fc7e746` | `.out` | `04a05cb6916c85d9` | 4/4 | `Q5-RESETS-EXACT` | run 1; replay identical |

Arguments (`<base>` = `scratchpad/eq/base`, `<OI>` = `<base>/verification/lean-mathlib/OIBridge`, `<in>` =
`scratchpad/eq5/inputs`):

| script | arguments |
|---|---|
| q0 | `<OI> <base> <in>` |
| q1 | `<OI> /home/user/leanprover-community/mathlib4 <in>` |
| q2 | `<OI>` |
| q3 | `<OI>` |
| q4 | `<OI> <in>` |
| q5 | none |

Cited evidence. Each hash was recomputed and matches its own record:

| evidence | file | sha (.py / .out) | record |
|---|---|---|---|
| PSD assembly and pair data of M_ρ, M_tw, M_id, M_T; the anchor-sum identities | SOURCE `s1_kt4_models` | `3c7b3c993b7d5527` / `c0d3c490f42a46bb` | SOURCE RESULT §10 |
| landed gate countermodels (re-derived here in q3) | SOURCE `s2_pair_premises` | `fcf2c56b103ed2cc` / `1815cb58c292e8e0` | SOURCE RESULT §10 |
| the STMC twist lead (re-derived here in q2 and q1 SEPB) | SOURCE `e1_stmc_twist` | `8f7ed449ccbbd674` / `73bd137b9965f487` | SOURCE RESULT §10 |
| the independent audit of SOURCE | `eqreview/audit_source` | `95b0f2477977b104` / `b3d5ff9382e6d1f6` | EQ5-SOURCE-AUDIT §2 |

## 4. Integrity

**At start** (`integrity_start.log`, 10:22:17Z, before any other write):
- PROTOCOL-PREM sha verified.
- Base manifest and inputs manifest both silent, exit 0.
- HEAD `f0d37906a83585efdaca8e3ee3404410e869c43e` on `claude/network-tool-access-8jtdhm`, `git status --porcelain`
  empty, reflog top `f0d37906 HEAD@{0}: commit: EQ4-F preflight …`.
- `.start_marker` (10:18:43Z) was present, written at launch.

**At end** (NOTES N6):
- Both manifests silent, exit 0. No `__pycache__` under the base. The Mathlib checkout is at `db584cd6` with a clean
  status.
- HEAD unchanged at `f0d37906`, and the reflog top three entries are unchanged.

**Anomaly, recorded and not repaired (§A.26).** The working tree, clean at start, now has eight untracked files under
`verification/lean-mathlib/OIBridge/`, with mtimes 10:54–11:12Z:

| file | sha |
|---|---|
| `FourCopyBipolar.lean` | `661d292675661310` |
| `FourCopyBridge.lean` | `febb3d1fc9658275` |
| `FourCopyCore.lean` | `9fce26e66fdec1e9` |
| `FourCopyEuler.lean` | `13c03eb6f9506543` |
| `FourCopyHeadline.lean` | `7a544c11d1c77a35` |
| `FourCopyIE1.lean` | `ddb33c259eac1326` |
| `FourCopyLocal.lean` | `12c1cd6cc79a651b` |
| `FourCopyTables.lean` | `defae9a298f3a602` |

What is known about them:
- This thread did not write them. All of its writes are in `scratchpad/eq5/PREM/` (listing in NOTES N6).
- Their contents were not read.
- No script of this thread reads the repository working tree. Every input it reads (the base snapshot, the inputs
  package, one Mathlib file) verifies unchanged.
- So no measurement here rests on them. All measurements and replays had finished before they were found, and none was
  run afterwards.

Other files newer than the start marker, outside this directory:
- `scratchpad/eq5/SIX/` (96 files): the concurrent thread's own directory, not read.
- `scratchpad/eqreview/quarantine-SIX-stray/MANIFEST.txt` (10:21:33Z): the coordinator's quarantine of a SIX stray. Only
  its name and mtime were listed.

**Writes:** only `scratchpad/eq5/PREM/`.

## 5. What is not claimed

- **No source.** Nothing here sources `tok`, TokProdState, hgate, hinv or hcl. Both outcomes are NOT SOURCED.
  - Theorem A and the OLTIres route are sufficiency statements whose premises (IP₁ and LT; OLTIres and the span
    condition) are unsourced.
  - OLTIres is (o)-type.
- **No necessity.** Nothing is claimed "required" or "necessary". Every countermodel is a model of P ∧ ¬C and shows
  insufficiency only. IP₁ is not necessary for the headline conclusion (M_id, M_T).
- **Not from the observational axioms.** Nothing here says that four-copy consistency, or the observational axioms,
  force quantum cones. The countermodels use Q3, twin and PSD₁₆ as models, never as premises.
- **Scope.** Statements are for the instance KT(4; 01|23, 02|13) with 3-ball tokens, as in the package. Nothing is
  claimed for other groupings, KT(n) for other n, or KT∞.
  - The purity lemma is proved for the 3-ball. Its proof uses only extremality and cone duality, but no other body is
    checked here.
  - The IIP-1 entries for MAX and MIN are not evaluated.
  - "Chart-blind" is the stated factorized form only.
- **Status of the routes.** Theorem A, R1–R10, the purity lemma, the chart-blindness statement and the OLTIres
  derivation are written arguments with exact ingredients. Nothing is kernel-checked.
- **Cited, not re-derived:** the PSD assembly of the SOURCE countermodels (SOURCE and its audit), and DEPGRAPH's (R) and
  §7.2.
- **M_θ.** Its validity is the M_tw assembly with θ in place of ρ, checked in the exact parts listed in §1.A2.
- **Status of IP₁.** No status change is proposed. IP₁, OLTIres and TIC are candidate formulations, not adopted
  premises.
- **Bands.** This is consistency-axis work only. Bands are unchanged.
