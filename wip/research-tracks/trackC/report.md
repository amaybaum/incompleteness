# TRACK C REPORT: does spectrality imply preservation under the available operations? (#832, #831; baseline #820)

## 0. The question as answered

- **Generic question: OPEN.** SP on the common domain (closed convex C, SEP ⊆ C ⊆ maxCone, trace normalization) ⇒ Φ_1 preservation is neither proved nor refuted.
- **C1, a theorem over a defined class [W + X + Lit].** A symmetric C in the domain is Q3 or ΓQ3. All local CP maps (every Φ_k, both local flows) preserve it, and CNOT preserves it iff C = Q3.
- **C2, exact counterexamples [X + W].** SP cones that keep closedness, convexity and normalization and drop exactly one domain clause fail Φ_1 at depth one:
  - CX1 drops maxCone;
  - CX2 drops SEP ⊆ C.

  Both clauses are therefore necessary for any SP ⇒ preservation theorem, even among order-isomorphic copies of Q3. #832's CNOT tilt drops both.
- **C3 [X + W].** An in-domain cone, the fidelity cut C_W, fails Φ_1 and also fails SP. It is consistent with the implication, but it is not evidence for it.
- **C4 [W + X].** A polytope is SP iff it is a simplex. SP is never a property of a non-classical finite OI stage, so it can only be a completion-level postulate. The same is true of quantum theory.
- **What remains:** any counterexample must be a non-symmetric SP cone in the domain.

## 1. Baseline verified

- #832: `check.py`, `independent.py`, `next_check.py` and `next_independent.py` replay byte-identically to their saved outputs, and the outputs match the pinned SHA256SUMS / NEXT-SHA256SUMS digests (112 and 341 controls; −1/400; −2).
- #820: `spectrality_independent.py` replays byte-identically.
- #820's `independent_check.py` was not replayed, because it reads repository paths.

## 2. Findings

### C1: symmetric-cone rigidity

**Statement.** Let C be a closed convex cone with SEP ⊆ C ⊆ maxCone on Herm(4), linearly isomorphic to the cone of a Euclidean Jordan algebra. Then C ∈ {Q3, ΓQ3}.

**Converse (separate witness, [W]).** Q3 and ΓQ3 are symmetric and lie in the domain: Γ maps products to products, and ⟨Γ(Y), A⊗B⟩ = ⟨Y, A⊗Bᵀ⟩.

**Proof.**
- **(A) C is irreducible.** Pure products are extreme in maxCone, by the pure-marginal lemma: X ∈ maxCone with Tr((|a⊥⟩⟨a⊥|⊗I)X) = 0 forces X = |a⟩⟨a|⊗σ (R7 is its negative control). Hence pure products are extreme in C. Extreme rays of a direct sum lie in the summands, and the product-ray set (CP¹×CP¹) is connected and spanning.
- **(B) Classification [Lit: Jordan–von Neumann–Wigner; Koecher–Vinberg].** By the classification, the irreducible symmetric cones of dimension 16 are Herm₄(C)₊ and Λ₁₆.
- **(C) Λ₁₆ is excluded.** Trace is strictly positive on maxCone∖{0}, so the trace-normalized base of a Lorentz cone would be an ellipsoid, which has frames of size at most 2. But the four product projectors form a 4-frame in every domain cone (R3).
- **(D) The isomorphic copy is rigid.** Let C = L(Q3).
  - F_a = |a⟩⟨a|⊗PSD(C²) is an exposed face of C, and L⁻¹(F_a) = PSD(S_a) with dim S_a = 2.
  - Order isomorphisms between copies of Λ₄ are Lorentz similarities, Y ↦ A Y A† or A Yᵀ A† [Lit: Loewy–Schneider; R4 checks that both forms are Lorentz similarities].
  - The lines P(S_a) are pairwise skew, likewise the lines P(S'_b), and each P(S_a) meets each P(S'_b) once.
  - [Lit] Three skew lines lie on a unique smooth quadric, and the lines meeting all three lie in its other ruling. So all the lines lie on a quadric projectively equivalent to the Segre quadric. Take T with T(Segre) = that quadric, composing with SWAP if needed.
  - Then L' := Ad_{T⁻¹}∘L⁻¹ sends F_a to |σ(a)⟩⟨σ(a)|⊗PSD(C²) and G_b to PSD(C²)⊗|τ(b)⟩⟨τ(b)|.
  - F_a ∩ G_b is a ray, so N_a(|b⟩⟨b|) ∝ |τ(b)⟩⟨τ(b)| for every a; O⁺(1,3) acts faithfully on null rays ([Lit] SL(2,ℂ) → SO⁺(1,3) surjective), so N_a = c(a)N. The scalars factor as c(a)/μ(a) = d(b)/ν(b) = κ, and since products span, L' = κ M⊗N with M, N Lorentz similarities.
  - Hence C = (Θ₁⊗Θ₂)(Q3) ∈ {Q3, Γ₁Q3, Γ₂Q3} = {Q3, ΓQ3}, using Γ₁ = ᵀ∘Γ₂ and SWAP covariance (R2).
- **(E) Consequences.** For ΓQ3, Γ∘Ad_{A⊗B}∘Γ = Ad_{A⊗B̄} on all 16 matrix units (R1), so every local CP map preserves it; for Φ₁ specifically, R6. CNOT maps |+0⟩ to a Bell state with ⟨singlet|Γ(Bell)|singlet⟩ = −1 (R5).

**Corollary [Lit].** Barnum–Hilgert (J. Lie Theory 2020, abstract): spectral + strongly symmetric ⇒ a simplex or a simple EJA state space. Simplices are impossible here, because pure products give infinitely many extreme points. So SP + strong symmetry + domain ⇒ C ∈ {Q3, ΓQ3} ⇒ every Φ_k preserves C.

**§A.31 pressure test.**
- SP does no work inside the symmetric class; the domain does.
- Strong symmetry asserts a transitive automorphism group, which is a preservation-type premise.
- The theorem says nothing about the non-symmetric SP cones where a counterexample would live, and it does not give CNOT.
- C1 is closely related to Barnum–Graydon–Wilce, *Composites and categories of EJAs* (Quantum 2020): for simple factors, composites are summands of the universal tensor product. It is not claimed as new mathematics.

### C2: relaxed-domain counterexamples

Both use σ = (I + ½ I⊗σ_x)/4.

- **CX1, maxCone dropped.** C_σ = {X : X + Tr(X)σ ⪰ 0} = L(Q3) with L(Y) = Y − ½Tr(Y)σ. It is closed, contains Q3 and hence SEP, and has trace-positive normalization.
  - SP certificate: frames X_i = 2P_i − σ with effects E_i = ½P_i + ½Tr(P_iσ)I. Then ΣE_i = I, Tr(E_jX_i) = δ_ij, and Tr(E_j L(Y)) = ½Tr(P_jY) on all units (CX1a, CX1b).
  - It is not inside maxCone: |00⟩⟨00| − I/20 ∈ C_σ, and ⟨11|·|11⟩ = −1/20 (CX1c).
  - Φ_1 failure: X = L(|00⟩⟨00|) ∈ C_σ, but for u = |1⟩⊗(1,i), ⟨u|L⁻¹(Φ_1X)|u⟩ = −1/16 (CX1d).
  - Controls: Q3 is preserved, and a rotation-invariant σ gives 0 on the same witness (CX1e).
- **CX2, SEP dropped.** C'_σ = {X : X − ½Tr(X)σ ⪰ 0} = L₂(Q3) lies inside Q3 and excludes |00⟩⟨00|.
  - X₂ = |00⟩⟨00| + σ is a member, and for u = |1⟩⊗(1,−i) the value after Φ_1 is −1/8 (CX2).

### C3: an in-domain non-SP cone that fails Φ_1

C_W = {X ⪰ 0 : Tr(WX) ≥ 0} with W = I/2 − Φ⁺. It satisfies SEP ⊆ C_W ⊆ Q3.
- **Φ_1 failure:** ρ = |00−i11⟩⟨00−i11|/2 has Tr(Wρ) = 0, but Tr(WΦ₁ρ) = −1/4 and Tr(W Ad_{I⊗D}ρ) = −2/5 (CW2).
- **SP failure [W + X: CW3].**
  - C_W* = Q3 + ℝ₊W. Frame effects therefore have the form E_i = Q_i + w_iW.
  - Frame members are M_w-orthogonal, where M_w = I − wW and w = Σw_i ∈ [0,2]. When w > 0, at most one member lies off the face Tr(W·) = 0.
  - ρ_bad = (2/5)Φ⁺ + (3/10)|01⟩⟨01| + (1/5)|10⟩⟨10| + (1/10)Φ⁻ is in C_W. It commutes with every M_w, and M_w^{1/2}ρ_bad M_w^{1/2} has simple spectrum for every w ∈ [0,2).
  - Pure states of C_W are rank one (face-dimension count r² ≤ 2), and w includes the completing effect I − ΣE_i. The spectrum of M_w ρ_bad is 2/5 + w/5, (3/10)(1 − w/2), (1/5)(1 − w/2), (1/10)(1 − w/2), linear in w, with coincidences only at w ∈ {2, −6/5, −2/3, −2/7}; so simplicity holds on all of [0,2), not on samples.
  - So its only candidate frame contains Φ⁺, which is outside C_W. At w = 2, ΣQ_i = 2Φ⁺ forces Q_i = q_iΦ⁺, and frames then have at most 2 members, while ρ_bad has rank 4 (independent review).

### C4: the source of SP

- **[W] A polytope is SP iff it is a simplex.** A polytope has finitely many frames, so frames smaller than full size cannot cover it. A full frame gives an affine bijection onto the standard simplex. Exact controls: triangle passes; square and hexagon fail, with uncovered points (PS1–PS3).
- **Consequence.** Every finite stage body (and, by NG1 [A], every finite-Ω completion) is a polytope, so SP holds there only if the system is classical.
- **SP of a ball completion is not inherited from its stages.** Under FiniteRank, stagewise SP would force a simplex completion [sketch: limits of (d+1)-point hulls are (d+1)-point hulls]. SP is therefore a completion-level postulate, as it is in quantum theory.
- **Assumption-watch [Lit + W].** By Hammer (1954), every point of a convex body lies on an affine diameter. So every strictly convex body is SP with frames of size 2, and SP carries no symmetry content for a single system. Any SP ⇒ preservation implication must come from the product faces of the pair domain.

### C5: relation to #829 and #831

- At k=2, ΓQ3 satisfies every #829 premise except H2, and in addition SP, self-duality and closedness. So H2 is not implied by any of these.
- Within the symmetric class, H2 selects Q3.
- Against #831's design induction theorem (compiled design, not adopted), conditional on that theorem: Φ_1 fails on C_σ and C'_σ, so any carrier family with one of these as its pair member must violate one of its primitive, attach or discard premises [W].

## 3. Premise map

| premise | status | citation | necessity witness |
|---|---|---|---|
| SP on the pair | introduced (BMU 2014, Postulate 1, as in #820); source open | completion-level only (C4) | — |
| strong symmetry / symmetric class | introduced [Lit]; source open; preservation-type | C1 | outside the class: open |
| SEP ⊆ C | introduced (#829 H1); open | — | CX2 |
| C ⊆ maxCone | introduced; record validity sourced only in the stage vocabulary (Track B), reaching C only via the chart | KInfFoundations.lean:63–72 | CX1 |
| closedness | introduced; used in the #820 Φ_k ⇔ flow equivalence | — | — |
| availability of Φ_k | sourced under its inventory premises | BridgeFiniteProtocol.lean:236, :269 [K] | — |
| C preserved by Φ_1 | open in general; proved in the symmetric class | C1 | C_W (not SP), CX1, CX2, #832 tilt |
| CNOT preservation | open; not implied by SP + domain + symmetry | R5 | ΓQ3 |

## 4. Countermodels

| cone | SP | domain | Φ_1 preserved | CNOT preserved | source |
|---|---|---|---|---|---|
| K_B, K(Z_F) | no | yes | no | (no / yes) | #820 |
| SEP | no | yes | yes | no | #820 |
| ΓQ3 | yes | yes | yes | no | R1, R5, R6; #832 |
| CNOT-tilted coPSD | yes | fails both clauses | no | — | #832 |
| C_σ | yes | not inside maxCone | no | — | CX1 |
| C'_σ | yes | does not contain SEP | no | — | CX2 |
| C_W | no | yes | no | — | CW1–CW3 |
| polytope stages | SP iff simplex | — | — | — | PS1–PS3 |

## 5. Most decisive next step

Decide whether every SP cone in the domain is symmetric. If so, C1 closes the implication; if not, the non-symmetric ones are the only possible counterexamples.

- **First fork:** in an SP cone of the domain, is the face generated by two non-orthogonal pure products that share no factor order-isomorphic to Λ₄?
  - If yes for all such pairs, the face lattice carries the skew-line/quadric structure that C1's step (D) used, and the reconstruction may extend.
  - If no, an SP-compatible non-ball face is the seed of a counterexample, to be tested against Φ_1 with exact certificates.

## 6. Non-claims

- The generic implication remains open.
- No physical OI source of SP, strong symmetry or the domain clauses is given.
- CX1 and CX2 are outside the domain, and are not physical OI models.
- C_W failing SP is not evidence for the implication.
- C1 is a written argument resting on standard classification results that were not re-read in full; only finite identities and witnesses are exactly certified.
- Nothing was certified in Lean, and no K2, K3, P0 or manuscript status changes.

## 7. Files (trackC/)

| file | sha256 / result |
|---|---|
| `symrigid_exact.py` | `b4efd8af5a95ea858ff8da7d8e10df67e48903cfd6a7e165358f45f08c4108d6` (17 checks, 7 mutations, PASS) |
| `symrigid_exact-output.txt` | `4fce648f5689e79531bc5133f97fb761f7e1b389ce3a02daded3720773e484a4` |
| `polytope_sp_exact.py` | `ec93e2d0b54609436b84c78ec8124a129b83d2cdb6a910f721bbe47ec0c2f170` (3 checks, 3 mutations, PASS) |
| `polytope_sp_exact-output.txt` | `b23a044d91befc01b669e37899a247686d2e7045a2f4b99535aced70574a3c39` |
| `replay-832/`, `replay-820/` | byte-identical replays |

Reproduce with `python3 -I <script> | cmp - <output>`. The SymPy replays use `…/scratchpad/venv/bin/python`.

Harness note: one planned polytope mutation (`drop_lower`) did not change the target and was replaced by `hex_center` before any verdict was relied on.
