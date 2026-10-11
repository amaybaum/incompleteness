# NOTES-O10 — HO-9's constraint carried to the pair, with HO-13's target

Thread `research/origin`, round 3, node O10. Base L = `9f9f8257`; kernel paths under
`verification/lean-mathlib/OIBridge/` at L. Evidence levels as in NOTES-O1. Script: `experiments/o10_pair.py`.
Received and used only at their labels: HO-13 v1 item 2 (the target: `J = cyc3` and `R_z(θ₀)`, `cos θ₀ = 3/5`, on one
token; CONDITIONAL on H2, H3 and the two invariances), HO-12 v1 items 1 and 4 (the SPEC target), HO-3 v1 items 1–3
(phiW in every candidate cone; `S_CHSH(phiW) = 14/5` at the stated settings; product registers are Bell-local).

**Productivity test, fixed before starting (§A.31).** A finding counts only if it is strictly stronger than HO-3
item 3 and HO-9 item 6 ("product-register composites are Bell-local") and either (i) decides whether a re-preparing
token law carries HO-13's two operations on one token with the exact witness, or (ii) locates exactly which feature
of a pair re-preparing law is necessary for a candidate cone (and what it imports), with exact instances on both sides.

## S0 — predictions, written before the first run of `o10_pair.py` (2026-10-11T00:40:27Z)

One token (the Kochen–Specker towers of O6-I):

- **A1.** The kernel's `cyc3` (KInfFoundations.lean:425, `cyc3_apply` :427) is the matrix J = [[0,0,1],[1,0,0],[0,1,0]]:
  orthogonal, det 1, order 3, J e_z = e_x. `R_z(θ₀)` (the `rotFun` of `ball3Drive`, :449, at cos 3/5, sin 4/5) is
  orthogonal, det 1, fixes e_z; e^{iθ₀} = (3+4i)/5 has minimal polynomial 5x² − 6x + 5 (not monic over ℤ), so infinite
  order. Expected: all hold.
- **A2.** On the sphere tower, a substratum rotation R carries the cosine density ρ_ψ to ρ_{Rψ} (the identity
  ψ·(Rᵀλ) = (Rψ)·λ), so it acts on the completed body, the ball, as ψ ↦ Rψ. Expected: exact for J and R_z(θ₀).
- **A3.** The witness for J with the tower's own frame dephasing (observe-and-forget of the z readout, ψ ↦ ψ_z e_z):
  (1, 1/2); J e_z = e_x is pure and z-balanced; the frame face z = + of the ball is the single state e_z, so the
  dephasing is the body's frame dephasing, not memory erasure. Expected: exact.
- **A4.** R_z(θ₀) commutes with the frame dephasing: P_coh = P_deph for every seed. Expected: exact.
- **A5.** The sphere tower's stage-crossing datum g (O6-I K7: R_z(a), cos a = 3/5) is R_z(θ₀) itself: a rotation about
  the frame axis. The circle tower's datum R(a) moves the frame point (P(+0) = 4/5 after it); the only isometries of
  the disk fixing the frame point are the identity and one reflection, so the circle tower has no infinite-order
  frame-axis rotation; its order-3 rotation gives P = 1/4 (not balanced) and its balanced rotations have order 4.
  Expected: exactly so.
- **A6.** J R_z(θ₀) J⁻¹ = R_x(θ₀); with two infinite-order rotations about the non-parallel axes e_z and e_x the
  generated group's closure is SO(3) (written step, classification of closed subgroups [L]). Expected: the identity holds
  exactly.

The pair (settings of HO-3: a0 = e_x, a1 = e_z, b0 = (4/5, 0, 3/5), b1 = (4/5, 0, −3/5)):

- **B1.** Product law (each readout re-prepares its own token only): the 16 deterministic sign patterns give
  S ∈ {−2, 2}, and each pattern is realized by Kochen–Specker hidden directions, so |S| ≤ 2 for every hidden
  distribution of the pair, correlated or not, and after every joint substratum map applied before the readouts; on
  products of tower states the maximum is 8/5. Expected: exactly so.
- **B2.** With a joint substratum bijection (a controlled rotation, B's hidden direction rotated so that e_z goes to
  Cλ_A, C = diag(1, −1, 1)) from the product ρ_uniform ⊗ ρ_{e_z}, the pair's table is (1, 0; 0, C/2): E(u, v) = uᵀCv/2
  exactly (from E[sgn(u·λ)λ] = u/2 for λ uniform on S²); its CHSH value is 7/5; its partial transpose has the eigenvalue
  −1/8, so the table is entangled: the product-law composite reaches non-separable tables and stays Bell-local.
  Expected: exactly so.
- **B3.** cnot(prodState xplus z3), computed from the kernel's tables `sgn`, `pc`, `pt` (CompositeDimension.lean:741–758),
  is diag(1, 1, −1, 1) = phiW (the landed identity at :1222); its density matrix is the rank-one |Φ⁺⟩⟨Φ⁺|; S = 14/5 > 2.
  So phiW is not a state of any product-law composite, cnot is not one of its operations, and it realizes no candidate
  cone. Expected: exactly so.
- **B4.** Collapse law (reading A re-prepares B into the table's conditional state ψ_B = (s + aCᵀu)/(1 + a r·u)):
  sequential statistics equal (1 + a r·u + b s·v + ab uᵀCv)/4 in both orders, no-signaling holds, S(phiW) = 14/5, and
  B's re-prepared state depends on A's setting at fixed outcome (e_x versus e_z). Expected: exact (symbolic).
- **B5.** Forced form: a law re-preparing B into a state of its own ball that reproduces a table's statistics has
  exactly ψ_B = (s + aCᵀu)/(1 + a r·u) (unique solution of the linear conditions for v = e_x, e_y, e_z). Expected:
  unique.
- **B6.** A law whose re-preparation of B does not take A's setting (only A's outcome and the pre-readout hidden state)
  cannot realize phiW: the required conditional states at (+, e_x) and (+, e_z) are the distinct pure states e_x, e_z,
  and under the uniform hidden direction the set where both readouts give + has measure 1/4 > 0; on the eight octants
  the conditions are infeasible. Expected: infeasible.
- **B7.** Such a setting-free law can still exceed 2 off the table space: with λ_A uniform and B re-prepared by octant
  pattern, S = 12/5 exactly and B's marginal is setting-independent, but the four correlators admit no table of the
  maximal cone (their bilinear fit has a singular value above 1: p(1) = −17/50 for the characteristic polynomial of
  C_bᵀC_b). Expected: exactly so.
- **B8.** Disguise of the collapse law: two pair states with the same hidden marginals (phiW, and the uncorrelated
  state with uniform marginals) require different laws (ψ_B = aCu versus 0), so the law reads the table's correlation
  block; after any readout the pair is a product, so from products the law alone reaches only separable tables and phiW
  needs cnot as a given pair operation. Expected: exactly so.

Run 1 of `o10_pair.py` (2026-10-11T00:45:02Z): `VERDICT TOKEN-REALIZED-PAIR-ONLY-BY-THE-CONE-OWN-LAW`, every prediction
above met, six countercontrols expected-false; replay byte-identical. Pre-run edits before any run: A5's symbolic solve
replaced (as first written it solved a trivial system), an unused variable removed, B8's zero-marginals check added, the
Kronecker product written out.

## 0. Verdict

1. **One token: the sphere tower carries HO-13's pair, with the exact witness; the circle tower carries neither.**
   On the Kochen–Specker sphere tower J = `cyc3` is a rotation of the substratum S² (a bijection of the stated kind)
   and acts on the completed body, the ball, as ψ ↦ Jψ; with the tower's own frame dephasing (observe-and-forget of
   the z readout, ψ ↦ ψ_z e_z, which is the body's frame dephasing: the frame face is the single state e_z) the
   sandwich is exactly (1, 1/2) [X A2, A3]. The tower's stage-crossing datum g = R_z(a), cos a = 3/5 (O6-I K7) **is**
   HO-13's R_z(θ₀): a rotation about the frame axis of the completed body, of infinite order (5x² − 6x + 5 not monic)
   [X A1, A5]; J R_z(θ₀) J⁻¹ = R_x(θ₀) [X A6], so the two generate a group dense in SO(3) [W + L]. The circle tower's
   datum R(a) moves the frame point (P(+0) = 4/5 afterwards): the disk's only isometries fixing the frame point are the
   identity and one reflection, its order-3 rotation is unbalanced (1/4), its balanced rotations have order 4 [X A5].
   Label: CONDITIONAL on the cosine re-preparation law (outside the stated access; O8: false there).
2. **The pair, product law: Bell-local whatever the correlations; non-separable but never phiW.** If each readout
   re-prepares only its own token, every CHSH value of every hidden distribution of the pair — correlated or not, after
   any joint substratum map applied before the readouts — lies in [−2, 2]: the 16 deterministic sign patterns give ±2
   and all are realized by Kochen–Specker directions [X B1]. A joint substratum bijection (a controlled rotation of B's
   hidden direction) does reach a non-separable table, (1, 0; 0, C/2) with C = diag(1, −1, 1), whose partial transpose
   has the eigenvalue −1/8, at S = 7/5 [X B2]. phiW = cnot(prodState xplus z3) (recomputed from the kernel's tables) has
   S = 14/5 [X B3]: it is not a state of any product-law composite, cnot is not one of its operations, and no candidate
   cone is realized. This strengthens HO-3 item 3 and O5-SRC2 (product registers with π × id) to arbitrary correlated
   preparations and joint substratum maps: the obstruction is the Bell bound, not separability.
3. **Cross-token laws: phiW needs the law to take the first readout's setting, and then the law is the table's own
   conditioning rule.** A law re-preparing B from A's outcome and the pre-readout hidden state only (not A's setting)
   cannot realize phiW: its required conditional states at (+, e_x) and (+, e_z) are the distinct pure states e_x, e_z,
   and the set where both readouts give + has measure 1/4 under the uniform hidden direction; a vector average in the
   unit ball equal to a unit vector forces every term to equal it, so the two requirements collide [X B6 + W]. Such a
   law can still exceed 2 off the table space (S = 12/5 exactly, no-signaling), but its correlators fit no table of the
   maximal cone (p(1) = −17/50 < 0) [X B7]. A law that takes A's setting and reproduces a table's statistics is unique:
   ψ_B = (s + aCᵀu)/(1 + a r·u) [X B5]; with it the composite reproduces every table's bilinear statistics in both
   orders, no-signaling, and S(phiW) = 14/5 [X B4]. **This is the exact composite with |S| > 2: CONDITIONAL on the
   collapse law and on cnot as a pair operation.**
4. **Disguise test of that law: it fails.** It is the candidate cone's own conditioning rule: phiW and the uncorrelated
   state with the same (uniform) hidden marginals need different laws (e_x versus 0 at (+, e_x)), so the law reads the
   table's correlation block — the entangled sector — rather than the substratum configuration [X B8]; and since every
   readout leaves the pair in a product, the law with local operations reaches only mixtures of products from products,
   so phiW needs cnot given (H2) [X B8 + W]. It is the branch-(a) nonlocal response of HO-3, with its form forced.
5. **Reading against HO-12/HO-13 (at their labels).** The re-preparing premise supplies SRC's token half — J and an
   infinite-order frame-axis rotation on one token, with their spectator stability on the product composite (its state
   set is invariant under local rotations) — and nothing of the pair half: the composite satisfies H1 and both token
   invariances and fails H2 (cnot) and H3; by HO-13 item 1 [CONDITIONAL] H2 and H3 are exactly what remains. HO-9 item 6
   (SRC via KB-D is token-only) extends to the continuous form and to every re-preparing pair law short of the cone's own.

## 1. One token

- *Kernel objects.* `cyc3_apply` [K KInfFoundations.lean:427] fixes J = [[0,0,1],[1,0,0],[0,1,0]]; `rotFun`
  [K :351] at (cos, sin) = (3/5, 4/5) is R_z(θ₀), the flow of `ball3Drive` [K :449] at θ₀ [X A1].
- *Covariance.* For orthogonal R, ψ·(Rᵀλ) = (Rψ)·λ, so ρ_ψ ∘ R⁻¹ = ρ_{Rψ}: a substratum rotation acts on the tower's
  states by rotating the Bloch vector, and the response (1 + ψ·u)/2 (O6 K7) is carried along [X A2 + W].
- *Witness.* e_z → J → e_x (pure, z-balanced) → [ψ ↦ ψ_z e_z] → 0 → J⁻¹ → 0: P = 1/2; without the dephasing P = 1 [X A3].
  The dephasing is the body's frame dephasing (the projection on the frame axis; frame face {e_z}), not memory erasure
  in the sense of O1-T7a.
- *Frame-axis rotation.* R_z(θ₀) commutes with the dephasing: P_coh = P_deph for every seed [X A4] — the
  continuous abelian half of HO-12 item 4 lives here, at one rational angle (HO-13 item 2).
- *Stage crossing.* The tower's own stage-crossing datum is R_z(θ₀) (O6-I K7), so on the sphere tower HO-13's
  infinite-order rotation is the stage-crossing generator itself, as `not_stagePreserving_of_infiniteOrderOn`
  [K CompositionOrder.lean:378] requires; J has order 3 and may be stage-preserving.

## 2. The pair — product law

Write the CHSH functional at HO-3's settings as S = Σ ±E. For hidden variables with local deterministic responses
(sgn(u·λ_A), sgn(v·λ_B)) every λ gives S ∈ {−2, 2} [X B1]; this covers every hidden distribution, every correlated
preparation, every joint substratum map applied before the readouts, and every re-preparation acting on the read token
only (it does not touch the other token's hidden variable before that token's readout). Products of tower states reach at
most 8/5 here (Cauchy–Schwarz with b0 + b1 = (8/5, 0, 0), b0 − b1 = (0, 0, 6/5)) [X B1 + W]. The controlled rotation of
B's hidden direction gives E(u, v) = uᵀCv/2 from E[sgn(u·λ)λ] = u/2 [X B2]: a Werner-type table at visibility 1/2,
entangled (partial-transpose eigenvalue −1/8) and Bell-local (S = 7/5).

## 3. The pair — cross-token laws

- *Setting-free* (B re-prepared from A's outcome and the pre-readout hidden state): phiW's conditional B-states given
  A's outcome are pure, so the re-preparation must equal them almost everywhere on each outcome set; at the settings
  e_x and e_z the outcome-+ sets overlap with measure 1/4 and demand e_x and e_z there [X B6 + W]. The overlap is not an
  artifact of the uniform representation: any tower state with zero Bloch vector (a mixture of cosine densities ρ_n)
  puts positive mass on the lune {x > 0, z > 0}, since a component missing it has n in the closed quadrant
  {n_x ≤ 0, n_z ≤ 0, n_y = 0} and such components cannot average to 0 [W]. Off the table space
  such laws can violate CHSH (the octant-pattern law: S = 12/5, operationally no-signaling) but realize no W 3 table:
  the bilinear fit of its correlators, C_b = [[9/10, 3/10], [2/5, 4/5]], has a singular value above 1 (p(1) = −17/50),
  while every table of the maximal cone has |uᵀCv| ≤ 1 [X B7 + W].
- *With A's setting*: the B-state is forced to be the table's conditional state (unique solution of the linear
  conditions for v = e_x, e_y, e_z) [X B5]; the resulting statistics are the table's bilinear form in either order,
  without signaling [X B4]. For phiW, ψ_B = aCu, and B's re-prepared state depends on A's setting at fixed outcome
  (e_x versus e_z): parameter dependence at the hidden level.

## 4. Classification (§A.31)

- **NEW, O10-N1.** On the Kochen–Specker sphere tower the stage-crossing datum is HO-13's frame-axis rotation R_z(θ₀),
  and `cyc3` is a substratum rotation with the exact witness: the re-preparing premise realizes SRC's token target
  exactly; the circle tower cannot (its datum moves the frame).
- **NEW, O10-N2.** Product-law composites reach non-separable tables through joint substratum maps and still never
  exceed the Bell bound: the obstruction to every candidate cone is the bound, not separability.
- **NEW, O10-N3.** For phiW a cross-token re-preparation must take the first readout's setting (outcome and hidden state
  do not suffice, because phiW's conditional states are pure), and then it is forced to be the table's conditioning
  rule; the only re-preparing realization of a candidate cone is the cone's own law with cnot given (disguise: fails).
- **ELABORATING, O10-E1.** A setting-free law can violate CHSH (12/5) only off the table space.
- **CONFIRMING, O10-C1.** HO-3 items 1–3, O5-SRC2, O6-I K7 (recomputed: phiW, 14/5, R_z(a)).
