# Independent-premise source checkpoint for the X screen (PR #864)

Research only, consistency axis (§A.23). No premise is adopted; no native round, F or E, dispatch, status change,
commit or merge. The scripts below are design-evidence checks kept beside this file: they belong to no preregistered
screen and certify no verdict. Scope: owner comment 6280945976 (2026-10-20). This text incorporates the correction
pass after the independent review `rev864/REVIEW.md` (CONFIRMED WITH CORRECTIONS); the pre-review text is
`SOURCE-CHECKPOINT.original.md` and the change list is `CORRECTIONS.md`.

**Reads.** PR #864 head `85e949ad` (REPORT, op-fork, mi-plus incl. A1–A2), premise memo at
`staging/premise-memo-864-20261018` `641ae161` (PREMISE-MEMO.md, CORRECTIONS.md), F2 memo `acfef447` §1–§4,
PR #864 comments through 6280945976 (incl. the readout-as-interaction search 6250325705 and its review 6250527074).
Papers and kernel at `origin/main` `92de3143` (2026-10-20); Lean paths are under `verification/lean-mathlib/OIBridge/`.
All repository reads were `git show`; nothing in the repository was written.

**Tags.** [AT] kernel declaration at `92de3143` (grep-checked); [EC] exact computation in `src_witness.py` (block id
given); [W] written argument; [W, new] first made here, not independently reviewed; [L] standard mathematics or
literature, not checked line by line here; [U] unresolved; [rec] recorded in the cited screen.

**Domain and fixtures** as in the memo: SEP ⊆ K ⊆ maxCone; fixed identification of native operations and tests;
Γ = partial transpose on token 2; K_B = SEP + ℝ₊B; K(Z_F) = (Q3 ∩ Z_F\*) + cone(Z_F) with defects
z_{s,t} = (I + sX⊗Z + tY⊗Y − stZ⊗X)/4 (as in `probes/p3_fixtures_op.py`); K_Γ = Q3 + ℝ₊Γ(B); S = native SWAP.

## 1. Examined sets not repeated here

- REPORT C1–C15 and intake R1–R5: SP, self-duality/homogeneity, local tomography, no higher-order interference,
  Hardy/Masanes–Müller continuous reversibility, the interacting continuous pair group, OP (weak, strong),
  Dakić–Brukner, E1/E1-L, E2, E4/T, E3/E5/E6, PC, MI, time orientation as preservation; E0, OI⁺-1/(b)/IE1/H-OI_g/H-T,
  LO, DT, PS, limit closure.
- MI+ C0–C13 and ledger rows S1–S24.
- Readout-as-interaction search (20 rows) and its review (about 40 further modules): hidden predictive memory,
  overlap identity, comb blindness, observability/interventional quotients, five-way minimality, hidden coherence,
  phase source, count reciprocity, coherent-extension classification (including the review's reversibility fork:
  unitary or antiunitary branch on the PSD cone), fixed-basis unitary representation, Stinespring/instrument dilation,
  quasilocal C\*-completion, GR coherent-completion classification, spectator compositionality, weak composite
  interface, Wigner's-friend covariance, ancilla interference, Derived Q3, the sharp-update principle; K2Guard,
  dimension-selector family, IndependenceCensus, causal separation, separability threshold and Weyl twirl,
  DiagonalTheory, DynamicsGlue, orientation and CP-world modules, Track B dilation acts, observer-partition covariance.
- Premise memo rows: EA, PC, MI, CPK, GRV, OI⁺1, SP, SP+Φ, OPw, OPs, OPs⊕PC, LT, HC, GEO, DRV-a, DRV-p, SWP, NST,
  SD, UPD, OVr, OVc, OVn, MEV (with the reviewed MEV ≠ OV-LU correction and witness X_c), CH, TH, SET and composites.

## 2. Candidates examined in this checkpoint

N1–N4 are not in the sets above. N5–N9 are checked against them and recorded as confirming, with exact
certificates where the earlier record had a written argument only.

| id | premise (operational form) | source: found / not found (in the examined set) | gate it independently supports | assumptions imported (PSD/CP flagged) | exact witness or countercontrol | G2 / G3 / G6 |
|---|---|---|---|---|---|---|
| **N1 EXC** | *Exchange continuity* (defined once in §3.1). EXC-24: every native pair bijection that is a symmetry of the physical pair state space is continuously connected to doing nothing through symmetries of that space (Ad_P ∈ Aut(K) ⇒ Ad_P ∈ Aut(K)₀). EXC-S: the native exchange is such a symmetry, Ad_S ∈ Aut(K)₀ | **Not found for K.** Nearest OI anchors are operation-side on the operator algebra: the exact drive `unit g t` of any involutive self-adjoint unitary (SecondOrderCircuit.lean:356, `unit_one` :377, `gate_drive` :469; configuration involutions via `localGate_isGate` :771), the on-site swap layer as a continuous one-parameter group (`swapQ_add_time` SwapLayer.lean:494, `continuous_swapQ_time` :446), "depth two is the trivial component" (continuous-time-audit.md:69, :129), connectedness of the unitary group (`exact_of_local` ReachabilitySeam.lean:251). These are statements about \*-automorphisms of a C\*-algebra, whose state order is PSD; transferring them to K is N2. Literature analogues [L]: Hardy's continuity axiom; Wigner (symmetries connected to the identity are unitary) | G3 [EC E2, E2b + W, L topology]. G5 exclusion aspect for all three named fixtures: Γ(Q3) [EC E2b + L], K(Z_F) [EC E4 + W, new], K_B [W, new + L]; controls unprepared, so no G5 headline PASS. G7, G8, M1 [W] | Continuity of K's symmetry group, a non-native (uncountable) structure (A1/G4 obligations unchanged). H-CAR for the exchange (memo U1). EXC-S contains S ∈ Aut(K), a named-operation preservation clause that holds on Q3, Γ(Q3), K_B, K(Z_F) and so carries no exclusion there; EXC-24 asserts no preservation. No PSD or CP evaluation of a competing cone's elements; no membership | E1 (ΓAd_SΓ = T∘Ad_S); E2 (8 of 24 native perms preserve Γ(Q3); the 4 with sign −1 for the Γ-transported bracket are exactly the coset S·{I, I⊗X, X⊗I, X⊗X}, checked in `src_witness_v2.py`); E2b (on pure rays of Γ(Q3), S acts as v ↦ conj(Sv)); E3 (path U(t) = Π_s + e^{iπt}Π_a, U(1) = S); E4 (defect algebra; S maps z_{1,1} ↦ z_{−1,1}); kill test (E1b instance): under the Γ-transported identification P ↦ Γ∘Ad_P∘Γ of all native operations, Γ(Q3) satisfies EXC-24 and EXC-S. Survivors, against both definitions: K_Γ (EXC-24, EXC-S, MI; E3 + E12), K_S (EXC-24, EXC-S, fails MI; E5 + `exc_survivors.py` S3–S4), K_H\* (EXC-24, EXC-S, MI, MEV, ≠ Q3; `exc_survivors.py` S2–S5) | G2 FAIL: (i) meaningful as a symmetry statement; (ii) no OI sourcing argument for K; (iii) consequence beyond compatibility only as a retrodiction (no SWAP-symmetric pair cone satisfying EXC-S is a simplex) [W]. G3 PASS. G6 OPEN. G4 FAIL standalone (adds no operation) |
| **N2 SDP** | *Swap-drive preservation.* The kernel's drive of the native exchange, Ad U(t), maps physical pair states to physical pair states for every t | Operation side found [AT] on the operator algebra (as N1). Its availability as an observer operation is the layer-flow hypothesis, which the corpus states is not implied (GR.md:268–272, `derivedOI_qm_iff_layerFlowExecutable'`); continuous time is "available, locally and exactly, rather than that OI supplies it" (continuous-time-audit.md:141). K side: **not found**; it is a transfer clause | G3 [EC E11]. G5 exclusion aspect: Γ(Q3) [EC E11], K(Z_F) [EC E13, witness found by search], K_B [EC E13 + W]; controls unprepared. G4 conditional on availability of the drive (it is non-real and non-monomial at t = 1/2) | H-CAR (U1); the transfer clause itself (preservation of K by a named operation family, class (iii)); branch of the drive fixed by the kernel (exp(πit)) | E11: Ad U(1/2) sends an element of Γ(Q3) to a matrix with product/Bell pairing −1/2. E13: W = \|w⟩⟨w\|, w = (0, 1, −1, −i), lies in K(Z_F)\* and gives −3/4 on U(1/2) z_{1,1} U(1/2)†; U(1/2)\|01⟩ is entangled and not ∝ Φ⁺, so it is not a pure state of K_B. SDP ⇒ EXC-S [W] | G2 FAIL (bare transfer clause, F2 §2.3). G3 PASS. G6 OPEN |
| **N3 DC-or** | *Common orientation of the dynamical correspondence.* If K is a symmetric cone, the correspondence observable → generator on K restricts with one orientation on both tokens; equivalently native symmetries of K are not time-reversing | **Not found.** "Dynamical correspondence" does not occur in the corpus; the corpus's orientation results (GR.md:184–214) concern one global orientation of PSD coherent completions | G3, conditional on the Jordan import [EC E2: S reverses the Γ-transported Lie bracket] | K a symmetric cone (self-duality + homogeneity, the Jordan route [I]); Alfsen–Shultz dynamical correspondence [L]. No PSD on competing cones, but a strong external structural import | E2 (as N1). On symmetric cones its content for native automorphisms coincides with EXC [W] | G2 FAIL ((ii) unsourced). G3 PASS conditional. G6 OPEN |
| **N4 REG-SYM** | *Exchange-symmetric register.* The pair cone is the two-token section and marginal of a token-permutation-symmetric three-token cone | **Not found** as an independent source (register composition is a premise of #829 [CD]) | none | — ; restricting to the family Γ_A(QK3) would import the PSD form | E9: Γ_A(GHZ) has eigenvalue −1/2 for every nonempty proper A, so within the partial-transpose family only QK3 is S₃-symmetric. Countercontrol [W]: the S₃-symmetrization of {Y⊗ρ : Y ∈ Γ(Q3), ρ a token state} is a symmetric three-token cone with pair sections Γ(Q3) | G2 FAIL. G3 FAIL. G6 OPEN |
| N5 GTR | *One global time reversal.* Physical descriptions are covariant under a single global antiunitary (transpose of all tokens together) | Found: GR.md:184 (operational antiunitary invariance); GR.md:198–204 (orientation of coherent completions is global) | none | GR's global-orientation conclusion for composites rests on PSD state families (D3) | E7: T∘Γ₂ = Γ₁ and Γ₁ = Γ₂∘T, so T(Γ(Q3)) = Γ(Q3). E10: the Γ-completion (Γσ, ΓG) keeps all data, Hermiticity, span and unit and fails only PSD (Γ(B) has eigenvalue −1/2) | G2 not reached. G3 FAIL. G6 OPEN |
| N6 SFR | *Shared spatial frame.* Both token balls are referred to the one lattice orientation | Global lattice orientation found in prose (Main.md:656, a fixed global parameter). Identification of the token ball with spatial directions **not found**: the token is a two-configuration register (H-CAR); the physical-spin identification H-spin′ is open and concerns emergent fields (SM.md:446–452) | none alone; it would supply CH's cross-token identification (memo G1 defect of CH) if the identification were made [U] | H-CAR; the unmade ball–space identification | E7 (global T) and memo F-β (local unitaries): a frame common to both tokens leaves Γ(Q3) invariant | G2 FAIL. G3 FAIL alone. G6 OPEN |
| N7 CORR | Correlation-set principles: information causality, no simultaneous encoding, macroscopic locality, local orthogonality, Tsirelson/CHSH bounds | Examined as memo row SET [W] | none | — | E8: Tr[(e⊗f)Γ(X)] = Tr[(e⊗fᵀ)X] symbolically, and f ↦ fᵀ is the y-reflection of the token ball, so the product-test correlation sets of Q3 and Γ(Q3) coincide | G3 FAIL (CONFIRMING) |
| N8 INT | Intrinsic single-cone postulates not listed before: bit symmetry, strong symmetry, ideal compression, purity preservation, pure sharpness, no-restriction, energy observability with K's own generators | Literature [L]; no OI source | none | — | E10 + P1 [rec]: Γ is a unit-preserving, trace-isometric order isomorphism Q3 → Γ(Q3), so each postulate holds on Γ(Q3) iff on Q3 [W]. With a fixed link of observables to native generators, energy observability becomes N3 | G3 FAIL (CONFIRMING) |
| N9 C1–C4 | The substratum posits: non-trivial, record-persistent, high-capacity hidden sector with readback (Main.md:72–80) | Found (diagnostics of the visible law) | none | — | memo F-α: configuration-diagonal content, fixed by Γ [rec] | G3 FAIL (CONFIRMING) |

## 3. The favourable branch: exchange continuity (N1)

### 3.1 Statement

For a closed convex cone K let Aut(K) be its linear automorphism group (a closed subgroup of GL(Herm 4)) and Aut(K)₀
its identity component. The two forms used throughout this file:

- **EXC-24:** for every native pair permutation P with Ad_P ∈ Aut(K), Ad_P ∈ Aut(K)₀.
- **EXC-S:** Ad_S ∈ Aut(K)₀. This contains S ∈ Aut(K). EXC-24 together with S ∈ Aut(K) implies EXC-S; EXC-S does
  not imply EXC-24 (K_H below, by a written argument).

No unit, test family or positivity of competing elements enters. The topology is the one Aut(K) inherits from GL;
unit-preserving or not makes no difference to the component of Ad_S on the fixtures [W]. Each named fixture has
S ∈ Aut(K) ∖ Aut(K)₀ (§3.2), so each fails both forms.

### 3.2 Per-fixture argument

Each argument uses one fact: a path in Aut(K) from the identity induces a homotopy, through homeomorphisms of the set
Ext(K) of extreme rays, from the identity to the endpoint's action.

- **Q3 satisfies EXC.** Every native permutation matrix is unitary, U(4) is connected, and the explicit path
  U(t) = Π_s + e^{iπt}Π_a reaches S (E3). This is the kernel's `unit S t`.
- **Γ(Q3) fails.** Ext(Γ(Q3)) = {Γ(P_v)} ≅ ℂP³. On it, Ad_S acts as v ↦ conj(Sv) (E2b), an antiholomorphic map,
  which acts by −1 on H₂(ℂP³; ℤ) [L]; the identity acts by +1, so Ad_S ∉ Aut(Γ(Q3))₀. This homology route is the
  independent one: it needs no classification of Aut(Q3). The bracket-sign computation (E2) is E1 transported, not
  an independent fact. With [A,B]_Γ = Γ(i[ΓA, ΓB]), the sign s(α) given by α([A,B]_Γ) = s·[αA, αB]_Γ is −1 for S
  and for the other three automorphisms of the coset S·{I, I⊗X, X⊗I, X⊗X}. Using s as a component invariant needs
  Kadison's theorem [L] (every unital order automorphism of Q3 is Ad_U or T∘Ad_U, so s is defined on the unital
  automorphisms) and a retraction from Aut(K) to its unital part [W]. The E2 "controls" on Γ∘Ad_U∘Γ and Γ∘T∘Γ hold by
  transport for any involution Γ and test only the code path.
- **K(Z_F) fails** [W, new; ingredients EC E4]. Every element of K(Z_F) is y + Σ c_j z_j with y ∈ L ⊆ Q3. If
  z_m = a + b in K(Z_F), pairing with P_m = I/2 − z_m (rank one; Tr(P_m z_m) = −1/2, Tr(P_m z_{m′}) = 1/2,
  Tr z = 1, E4) and with the trace forces a, b ∝ z_m, so each defect is extreme. Ext(K(Z_F)) ⊆ Ext(L) ∪ {defects},
  L consists of PSD matrices, and each normalized defect has eigenvalue −1/2, so the defect rays are isolated in
  Ext(K(Z_F)). A connected group fixes every isolated extreme ray. Ad_S preserves K(Z_F) (it permutes Z_F and is
  unitary, E4) and moves z_{1,1} to z_{−1,1}, so Ad_S ∉ Aut(K(Z_F))₀.
- **K_B fails** [W, new]. Ext(K_B) = {pure products} ∪ {B}: every element is extreme in Q3 ⊇ K_B, and extreme rays
  of a sum lie among those of the summands. The pure products form a connected copy of S² × S², and B is isolated
  (product overlap with Φ⁺ is at most 1/2). Every automorphism therefore preserves the product component. Ad_S acts
  there by exchanging the factors, which exchanges the two generators of H₂(S² × S²) [L], so it is not homotopic to
  the identity and Ad_S ∉ Aut(K_B)₀. The same argument excludes SEP; maxCone = SEP\* is excluded through the
  continuous isomorphism α ↦ (α\*)⁻¹ of automorphism groups, which fixes the self-adjoint involution Ad_S. The
  classical cone has four isolated extreme rays, and S swaps two of them; it is a positive control of the conditional
  mathematics only (F2 §3.3).

### 3.3 Pressure test (§A.31, favourable branch)

1. **PSD/CP import.** None found. No competing element is evaluated in the PSD order. The arguments use each
   fixture's own extreme rays, plus the fixed memberships L ⊆ Q3 and K_B ⊆ Q3, which are memberships and not imports
   (memo §4 convention). The Γ(Q3) step needs no classification of Aut(Q3); E2b and homology suffice.
2. **Where the force comes from.** It comes from the fixed identification of the native exchange. The consistent
   re-identification is the Γ-transported identification of all native operations, P ↦ Γ∘Ad_P∘Γ (re-identifying
   SWAP alone is not a homomorphism of the native group, since S = CN₁₂CN₂₁CN₁₂). It sends Ad_S to T∘Ad_S (E1), and
   under it Γ(Q3) satisfies EXC-24 and EXC-S, since Γ∘Aut(Q3)₀∘Γ = Aut(Γ(Q3))₀ and every native permutation lies in
   Aut(Q3)₀ [W; E1b is the SWAP instance]. This is the G3 reading and the same kill test as UPD's. EXC adds a
   cross-token orientation datum: S is orientation-reversing on Γ(Q3).
3. **Transfer clause.** EXC-24 asserts no preservation. EXC-S contains the preservation clause S ∈ Aut(K), which
   holds on all four reference cones and carries no exclusion there. Whether an existential clause about K's symmetries is read
   under F2 G2 as a transfer clause is a gate ambiguity for the owner (§5).
4. **Vacuity.** EXC-24 is vacuous on a cone with no nontrivial native symmetry. Its exclusions rest on the fixtures
   having the native SWAP as a symmetry, so it is a G3/G5 instrument and not a selection principle on the domain.
5. **Sufficiency.** Neither form implies K ⊆ Q3, and neither implies K = Q3 together with MI and MEV. Each survivor
   below other than K_Γ is generated by pure states, so its extreme rays are exactly its generator rays; a native permutation that
   maps one of them outside the generator set is not an automorphism.
   - K_Γ = Q3 + ℝ₊Γ(B) satisfies EXC-24, EXC-S and MI (E3, E12; Q3 ⊆ K_Γ), and K_Γ ⊄ Q3.
   - K_S = cone(U(t)·SEP) satisfies EXC-24 and EXC-S. The group 𝒰 = {U(t)(V⊗V)} preserves it and is connected, it
     contains the four native permutations commuting with S (I, S, X⊗X, S·X⊗X), and each of the other 20 maps a pure
     state of K_S outside U(t)·Prod (`exc_survivors.py` S1–S4). K_S lies in Q3 (so MEV, CH and UPD hold) and fails MI:
     W = I/2 − B commutes with U(t), is block-positive, and Tr(WB) = −1/2 (E5).
   - K_H\* = cone(𝒰·(SEP ∪ G)) satisfies EXC-24, EXC-S, MI (B ∈ G) and MEV (K_H\* ⊆ Q3), and P_singlet ∉ K_H\*, so
     K_H\* ≠ Q3 (`exc_survivors.py` S2–S5). These steps use only the inclusion "pure states ⊆ Sym ∪ U(t)·Prod"
     (S2) and witnesses taken from U(t)·Prod. Equality of the pure set with Sym ∪ U(t)·Prod (Takagi [L]) is not
     needed. The construction is the reviewer's, re-verified here with separate code.
   - K_H = cone(U(t)·(SEP ∪ G)) satisfies EXC-S, MI and MEV, and P_singlet ∉ K_H (S6), but fails EXC-24.
     Ad_{X⊗X} preserves K_H and swaps |00⟩ and |11⟩, the two points where G_pure meets U(t)·Prod (S6 [EC]).
     Elsewhere on G_pure the extreme-ray set is locally a 2-manifold; every point of U(t)·Prod has neighbourhoods
     containing a 4-ball. So every homeomorphism of Ext(K_H) preserves the pair {|00⟩, |11⟩}, and a path from the
     identity fixes each point. Hence Ad_{X⊗X} ∉ Aut(K_H)₀. [W: the reviewer's argument, checked by reading here,
     not independently reviewed.]
   - EXC with SP or OP: [U].
6. **Source.** The OI-anchored route to EXC runs through the kernel drive, and it requires the drive to preserve K.
   That requirement is N2, a transfer clause; the intrinsic form is a posit. Constructed with knowledge of the target,
   like CH.
7. **Relation to earlier records.** REPORT:153 ("native product tests and local permutations are Γ-compatible, so
   only entangling native operations can separate") holds for preservation; the memo had already corrected its
   "only entangling" reading through CH. Memo §6(c) at `641ae161`, in full:

   > **(c) An entangling operation is not necessary.** CH excludes Γ(Q3) and K(Z_F) using fixed product tests alone,
   > with native SWAP supplying the cross-token identification [EC, dc; W]. This bears on the reading in REPORT's
   > gate ambiguities ("only entangling native operations can separate"), which is correct for native tests only.
   > - Every examined Γ-breaker carries a cross-token orientation datum [W, scoped by F-α and F-β], fixed
   >   independently of K, that involves a non-configuration token resource: a test, a preparation, or local
   >   operations entering a joint protocol.
   > - §A.31: NEW (scoped); under maximum skepticism the CH instance itself is not viable as X (G1).

   F-γ (memo §1) already identifies the Γ ambiguity with the relative orientation of the two token frames, and CH
   already uses native SWAP for the cross-token identification. In substance EXC is a further instance of that
   pattern: a cross-token orientation datum fixed independently of K, here SWAP's component in Aut(K). What is new
   is the form. EXC uses no test, preparation or local operation in a joint protocol; its non-native ingredient is
   the identity component of Aut(K).

§A.31 classification: **NEW (scoped, form) / ELABORATING (substance)**. Native SWAP is an orientation-reversing
automorphism of Γ(Q3) [EC + L]. A symmetry-topology clause separates Q3 from Γ(Q3) [EC + L] and excludes K(Z_F)
[EC ingredients + W, new] and K_B [W, new] without tests, membership or PSD evaluation. The [W, new] steps were
checked by one independent review, not by a reviewed record. It is unsourced and insufficient alone.

## 4. Result by the owner's five distinctions

- **Source found / not found (examined set).** No candidate N1–N4 has an independent OI source for its cone-level
  content. Operation-side kernel facts were found for N1/N2: the exact continuous drive of native involutions on the
  operator algebra. Found sources for N5, N6 (global orientation) and N9 do not separate Q3 from Γ(Q3). This is a
  scoped not-found, limited to the candidates and corpus listed here; it is not a no-go.
- **Gate independently supported.** G3: N1 and N2 [EC]; N3 conditional on the Jordan import. G5 exclusion aspect
  for K_B, K(Z_F), Γ(Q3): N1 [EC + W, new] and N2 [EC]; controls unprepared. No candidate supports G2(ii), G4
  standalone, or G6.
- **Assumptions imported.** N1: continuity of K's symmetry group; H-CAR for the exchange. N2: a transfer clause plus
  availability of the drive. N3: the Jordan route. N4: a PSD-form family restriction. N5: PSD state families inside
  GR's classification. None of N1–N3 evaluates PSD or CP on a competing cone.
- **Witnesses.** `src_witness.py` (49 checks), its relabelled successor `src_witness_v2.py` (51 checks) and
  `exc_survivors.py` (16 checks), each all PASS over two byte-identical runs; listed in §6.
- **Unresolved.** G2 for every candidate (no sourcing argument; for N1 the transfer-clause reading is an open gate
  question). G3 resolved only for N1, N2 and conditionally N3, each with no source. G6 OPEN for all. G4: no
  candidate supplies a sourced continuous resource; N2's drive is constructed in the kernel, but its availability is
  the open layer-flow hypothesis (GR.md:272).

## 5. Points needing an owner decision

1. **Gate reading.** Under F2 G2, does an existential clause about K's own symmetries count as a transfer clause?
   EXC-24 is the form without any preservation assertion. It needs a ruling before any EXC screen, in the manner of
   the memo's U3 for UPD.
2. **Source node.** Is there a route from the kernel's operator-algebra drive (`gate_drive`, SwapLayer) to
   automorphisms of a candidate cone K that is not the compatibility obligation X-4? N2 shows that the direct route
   is X-4 itself.
3. **Composite screen.** Should EXC ⊕ SP and EXC ⊕ OPs be preregistered? K_Γ, K_S and K_H\* already show that
   EXC (either form) needs partners beyond MI and MEV: K_H\* satisfies EXC-24 ∧ EXC-S ∧ MI ∧ MEV and is not Q3.
4. **Review status.** One independent review has read the [W, new] arguments of §3.2 (K(Z_F), K_B, SEP and maxCone
   exclusions) and found no gap. The K_H topological step (§3.3 item 5) is the reviewer's written argument and has not
   been reviewed by a second party.
5. **G6.** A decision rule for an independent prediction. Nothing found here qualifies: EXC's consequences (an
   interacting continuous symmetry, nonclassicality of SWAP-symmetric pair cones) are retrodictions.

## 6. Exact witness scripts and outputs (record only)

Environment: the container has no system SymPy, so SymPy 1.13.3 was installed in a scratch venv
(`venv/`, Python 3.13.16). Runs used `venv/bin/python -I -B`. Exact Rational/I/symbolic arithmetic only.

| file | sha256 | note |
|---|---|---|
| `src_witness.py` | `bfce213f85b26d08868c1fd80a0db8dbe84bb35a6c585310265afca9d6fa78eb` | E1–E13, E1b, E2b, 5 negated restatements (labelled MUT in this version), kept unchanged |
| `src_witness.run1.out`, `src_witness.run2.out` | `2dfcfda34ecbc735d54032d8cf2ee7e76307401e214984ac800649bf6aeee110` (both) | 49 PASS, 0 FAIL, rc 0, byte-identical |
| `src_witness_v2.py` | `66738e2723df9f4432acbfda8702fa55f99010ea2e9fc00e22427446d8d88dcd` | as `src_witness.py`, with: MUT block renamed NEG (negated restatements); E2 coset check added; brT = −br identity added; E10 label narrowed; E13 comment names `sdp_zf_search.py` |
| `src_witness_v2.run1.out`, `.run2.out` | `21a631b1dd93b02b73d907b603b5d231362ffc6a1550d8b2a8000c1817054f1f` (both) | 51 PASS, 0 FAIL, rc 0, byte-identical |
| `exc_survivors.py` | `738f36a936d8a22f9271fddcc075171384a61fe1b8ace42339a05938afc1d64c` | S1–S6: U(t)·Prod criterion, 𝒰, K_S, K_H\*, K_H ingredients |
| `exc_survivors.run1.out`, `.run2.out` | `2bb0ff4de4090b55332a10dd6fef4e7ea0daf73620f03624deffbc7c1c62ec3d` (both) | 16 PASS, 0 FAIL, rc 0, byte-identical |
| `sdp_zf_search.py` / `.out` | `62ef2233…f91` / `82996068…5b5` (full digests below) | exploratory grid search that found E13's K(Z_F) witness; E13 re-checks it |
| `run1-harness-error/run1.out`, `…/src_witness.py.at-run1` | `9222e9df…15f1`, `e5deb4dd…02e8` | earlier run, 38 PASS / 1 FAIL |

Full digests: `sdp_zf_search.py` `62ef2233307f9498c3c35c2ce47d8fac89c7a54a2358101a8014b5777b526f91`,
`sdp_zf_search.out` `82996068e48ad5c9095533303adcefb98ef4c04951ba4a21d9a4d1a449e669b5`.

**The failed check in the earlier run.** The non-vacuity check chose two commuting basis elements (I⊗X and X⊗I), so
the bracket it tested was zero by construction. It was corrected to I⊗X and I⊗Y. Two controls were added at the
same time (sign on both components of Aut(Γ(Q3))). No other check changed in that edit; E11–E13, E1b and E2b were
added afterwards. The earlier output and script are kept in `run1-harness-error/`.

**What the checks certify.**
- E2 replays REPORT P2's count (8 of 24), each of the 16 failures with an exact −1/2 pairing; `src_witness_v2.py`
  also checks that the four sign −1 automorphisms are the coset S·{I, I⊗X, X⊗I, X⊗X}.
- Several checks are code-path controls or restatements, not independent facts. The E2 controls on Γ∘Ad_U∘Γ and
  Γ∘T∘Γ hold by transport. "Every native permutation has sign +1 w.r.t. Q3" holds because permutation matrices are
  unitary. E1b is E1 rewritten with Γ² = id. The NEG block (MUT in `src_witness.py`) negates facts already checked
  and does not mutate the checker. Its "Γ → full transpose" item is false by the identity brT = −br (checked in v2),
  so it is not a sensitivity test.
- E10 computes that Γ keeps every pairing Tr(σG), the unit and Hermiticity, is an involution, and that Γ(B) is not
  PSD. It does not compute anything further about the Γ-completion.
- The E11 control ("Ad_S preserves Γ(Q3)") is only an absence of witnesses among the test states. Preservation
  itself follows from E1.
- Everything marked [W] or [L] in §3.2 and §3.3 is argument, not computation.

## 7. Assumption-watch markers

- **AW-S1 (NEW in form).** S ∈ Aut(Γ(Q3)) lies in the non-identity component: it reverses the orientation of Γ(Q3)'s
  pure-state manifold. Preservation-level Γ-compatibility (P2) and orientation-level compatibility differ.
- **AW-S2 (ELABORATING AW-X2/F-β).** Every OI-anchored continuous structure found (kernel drive, unitary-group
  connectedness, emergent Hamiltonian generator Main.md:336, GR's global orientation) sits on the PSD/C\* carrier.
  Its bearing on a candidate K passes through X-4 (compatibility) or through the PSD import.
- **AW-S3 (ELABORATING).** Within the partial-transpose family, the Γ ambiguity is specific to two tokens: exchange
  symmetry on three or more tokens leaves only QK (E9). Outside the family it does not exclude Γ(Q3) pairs (N4
  countercontrol).
- **AW-S4.** The swap-drive clause (N2) excludes all three named fixtures, where PC misses K(Z_F). Its G2 status is
  that of DRV-p/OI⁺1, class (iii).
