# EQ-B running notes — reversible dynamics and gate sourcing (K∞-Act)

Thread B of the EQ programme. Research only; nothing here is adopted or governed. Writes only in `scratchpad/eq/B/`.
Base: certified `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`, read-only at `scratchpad/eq/base/`.

## 0. Productivity test (fixed before any node was walked, §A.31)

A finding of this thread is a **gem** iff it is strictly stronger than the obvious restatement ("the control gate,
K∞-Act, K∞-Trans and K∞-Copy are premises, and a principle that restates a premise derives it") **and** it does at
least one of:

- (A) **theorem route**: for a principle P stated in observer vocabulary (tests, outcomes, conditioning, reversible
  actions, joint cone), a written or exact proof that P yields the clause(s) it targets, a check that finite-dimensional
  complex QT satisfies P in its stated scope (converse), and a named foil that P excludes;
- (B) **separation**: an exact countermodel that satisfies P and fails a named CtrlGate (or K∞) clause, with the place
  where the selector's proof reads that clause located;
- (C) **incompatibility**: an exact QT witness showing P fails in complex QT;
- (D) **hidden assumption exposed**: a load-bearing ingredient that the candidate principle or the landed chain uses
  silently, with a countermodel or a proof showing it is load-bearing.

Anything weaker — e.g. "relC is used in the selector", or a re-labelling of relC as a principle with no separation and no
converse — is a **non-gem** (coherence relabelling) and is recorded only. Propagation bar: better than coherence.
Output classes: NEW / POSITIVE / ELABORATING / CONFIRMING / BORDERLINE. Every favourable branch gets a countercontrol.
Evidence layers: [K] kernel at bcbc516f (file:line), [X] exact computation in this directory (script + output),
[W] written proof here, [L] literature (verified against source / unverified), [P] prior off-repo ledger (re-verified
where relied on).

## 1. Node log (depth-first; verdict at each node)

Reading done first (§A.19): PROTOCOL, AGENTS, ROADMAP P1-K; RELC-SELECT-1, DIM-1, OPACT-1, TRB-1, OG-1, KTRANS-DENSE-1
results; CompositeDimension §B/§Q, RelcSelectBlock/Parity/C5; kinf-seams-audit; prior ledgers ac, drive, opact,
threads/B, relc, relt, possep, k2, ss (literature table), sa (verdict). wave2/O, pthread skimmed (headings only:
nothing on gates).

### B1 — QB1(a) conditioning (decisive branch, walked first)

- **B1.0 audit [R]** `RelcSelectBlock.lean` reads `hG.relC` at :95 (`gate_actC_ctrl`, used only by
  `gate_corner_neg_ctrl` :99–104) and :746 (parity, `finrank_plus_eq_finrank_minus_relC`). So the block reduction reads
  relC only as the −z-corner identity CI: `G(hom(−z)⊗Y) = hom(−z)⊗Ñ M₀ Y`; the selector reads full relC once more,
  for parity. Field-access count: frame 4, posFwd 7, posInv 3, relC 3 (one is `ctrlGate_of_nativeGate`).
- **B1.1 decomposition [W]+[X]**. Ñ preserves C = span(e₀, lift z) and T = lift(z^⊥); so relC ⇔ (relC on C⊗H) ∧
  (relC on T⊗H). On C⊗H, under the landed corner form, relC ⇔ CI. Call the T⊗H half **TR**:
  `G(lift(Nc)⊗Y) = (Ñ⊗Ñ) G(lift c⊗Y)`. Exact (b1 C2): cnot1, cnot: both halves hold; gC5: CI holds, TR fails;
  C7: a linear map with TR and ¬CI (rank 16, no positivity claimed). Verdict: relC = CI ∧ TR, halves independent.
- **B1.2 existential conditioning COND(N)** := slices `G(hom z⊗Y) = hom z⊗Y`, `G(hom(−z)⊗Y) = hom(−z)⊗ÑY`, + P±.
  COND ⇒ frame ∧ CI [W, trivial]. Exact (b1 C1): cnot1, cnot and **gC5** all satisfy COND (M₀ = I, M₁ = Ñ).
  gC5: IsNot, frame, P± are kernel (`isNot_nC5`, `gC5_frame`, `gC5_posFwd`, `gC5_posInv`), relC fails (kernel
  `gC5_not_relC`), d = 5. Verdict: **COND gives a strictly weaker gate**: the half of relC the block reduction reads
  (so p_N ≤ 1 by the landed proofs re-read with CI, [R]) and none of the half parity reads. Missing clause: TR.
  Weak corner form (M₁ unrelated to Ñ) is what COND gives for an unspecified corner-swapping action; it is already
  automatic from frame + P± (relt N2.1, [P] written) — no content.
- **B1.3 natural conditioning NC** (Cond single-valued on tests {±z} × actions {I,N}², with Slice, P±, Cov_N
  `(Ñ⊗I)Cond(z;·)(Ñ⊗I) = Cond(−z;·)`, Rel `Cond(−z;a,b) = Cond(z;b,a)`, Post_N `(I⊗Ñ)Cond(t;a,b) = Cond(t;Na,Nb)`).
  [W] Cov∘Rel∘Post ⇒ relC(N_A, N) where N_A is the control map used in Cov. Exact (b1 C6): with gC5, each PAIR of the
  three laws is realised by an explicit assignment and the third fails ⇒ the coherence of all three is the content
  (= TR given CI). QT converse (b2 Q2): the assignment with lift N ↦ X satisfies all three; with the SU(2) lift
  N ↦ iX, Post fails, and Ad(|0⟩⟨0|⊗I+|1⟩⟨1|⊗iX) has COND but not relC. Written: QT satisfies NC with tests over
  the whole sphere and Cov over all of SO(3) (conjugation is phase-blind), action domain {I, N}, for every lift with
  L(I) = I, L(N)² = I — spot checks Q2 exact. (Corrected in pass 5: an earlier wording, "over all of SO(3) with any
  lift L(S⁻¹) = L(S)⁻¹", left the action domain unstated; with Post over all target rotations NC is QT-incompatible,
  since it forces a homomorphic lift SO(3) → U(2) and lifts of π_x, π_z anticommute.)
- **B1.4 type-level copy** (bears on QB3). NC with Cov over the control's group 𝒢_A and actions from 𝒢_B: relC(g, N_B)
  for every z-flipper g ∈ 𝒢_A. If 𝒢_A = 𝒢_B (type-level reversible group) then g = N_B gives relC(N_B, N_B) ⇒
  CtrlGate ⇒ d ∈ {1,3} [K dim_of_ctrlGate]. Without it: **gC5 satisfies the two-NOT relation Rc(N_A, nC5) with the
  balanced N_A = diag(1,−1,1,−1,−1)** (b1 C5, exact), so NC with 𝒢_A = {I, N_A}, 𝒢_B ∋ nC5 holds at d = 5 with
  kernel positivity — a kernel-backed two-NOT countermodel (splits (3,3)/(2,4)). Provenance: the pair (J/K map, N_A)
  is NB-1's C2N (NB-1 preregistration, minimality table), whose positivity NB-1 wrote; the kernel now carries it via gC5.
- **B1.5 incompatibilities** (b2): Comp (conditioning composes, F(ST) = F(S)F(T)) on the Klein group: for every
  phase choice C(X)C(Z) = Ad(Z⊗I)C(Z)C(X) ≠ C(Z)C(X) (Q3, 16/16 exact) ⇒ QT-incompatible; Cov over O(3) fails for
  CNOT (Q4: r_y⊗I does not commute) ⇒ the Cov group must be orientation-restricted or {I,N}.

### B2 — QB1(b) continuous reversible interaction

- **B2.0 literature [L, unverified: search summaries only; arxiv/nature/ucl blocked by egress policy]**: Krumm–Müller
  npj QI 5, 7 (2019) Thm 1: gbits = d-balls, local group SO(d), no-signalling, tomographic locality, closed connected
  global group ⇒ for d ≠ 3 the global group is local. MMAP JMP 55 122203 (2014): only two-qubit QT has entanglement in
  the d-ball + LT + continuous reversible dynamics family. de la Torre et al. PRL 109 090403 (2012): qubits + one
  continuous reversible interaction ⇒ QT.
- **B2.1 QT converse [X]** (b2 Q5): CNOT lies on the one-parameter group G_t = Ad(|0⟩⟨0|⊗I + |1⟩⟨1|⊗(P₊+e^{it}P₋)),
  group law exact at cos t = 3/5, G_π = Ad(CNOT) = kernel cnot (Q1: equal exactly), COND(V_t) slices exact.
- **B2.2 the J/K flow (exploration [float], x1)**: transcribing G_t's tangent block (A_t, B_t) to the J/K data gives a
  one-parameter family at every odd d with G_π = the J/K gate; float minimisation finds posFwd and posInv values ≥ 0
  (min ≈ +1e−8) at d = 5, 7 for six values of t. Candidate written proof: V ≥ |x_T||e_T|(√(αβ) − |v_t†Ωv₀|) with
  Ω = [[P, ω̄],[ω, M]] ⪰ 0 and Binet–Cauchy slack (2 − 2cos t)(PM − |ω|²). To be made exact (b4).

- **B2.3 the J/K flow, exact (b4, jk.py)**. G_t: identity on hom z ⊗ H; hom(−z) ⊗ R_t on the −z slice
  (R_t = P₊ + cos t P₋ + sin t K P₋); c ⊗ A_t Y + Jc ⊗ B_t Y on the tangent sector. Exact at d = 3, 5, 7: G_0 = I,
  G_π = kernel cnot (d=3) / kernel gC5 (d=5), group law at cos t = 3/5, inverse G_−t, normalisation, COND(R_t) slices,
  operator-Schmidt rank 4 (non-product), G_π frame ∧ ¬relC at d = 5, 7. Symbolic S1 (value decomposition),
  S2 (key identity ⟨f,Y⟩⟨f,R_tY⟩ − ⟨f,A_tY⟩² − ⟨f,B_tY⟩² = (2−2cos t)(PM − |ω|²)), S3 (PM − |ω|² ≥ 0 by an explicit
  SOS: complex Lagrange identity) at d = 3, 5, 7. Written assembly: V ≥ |x_T||e_T|(√(αβ) − √(a′²+b′²)) ≥ 0 (AM–GM,
  Bessel for (x_T, Jx_T)). First S3-SOS attempt had a conjugation bug (FAIL at d = 5, 7); fixed (Lagrange minors
  a_i b_j − a_j b_i, no conjugation) and re-run: green. Countercontrols CC1 (R_−t with A_t, B_t: −18/25) and CC2 (J
  scaled 6/5: −1/5) exact negatives. Verdict: **a continuous reversible interaction (one-parameter group, two-sided
  positive, normalisation-preserving, non-product) exists at every odd d; its time-π member is the d = 5 kernel gate
  gC5, which fails relC.** (b) as stated is strictly weaker than CtrlGate.
- **B2.4 adding local rotations (b5)**. W5 = gC5 (I⊗L) gC5, L = 90° rotation in coordinate plane (2,4) of eball 5:
  exact rational pure-product witness with value −1.4138… < 0 (outside maxCone); same at d = 7 (W7, −1.4142…).
  Control: L in the (w₁,w₂)-plane (J/K commutant) nonnegative; d = 3 analogue cnot (I⊗L₃) cnot = Ad(CNOT(I⊗V)CNOT)
  exactly (a QT channel). Verdict: the J/K interaction does not share a joint state space with local SO(d) at d = 5, 7 —
  consistent with Krumm–Müller [L, unverified]; local transitivity inside one connected dynamical group is the
  clause that excludes d = 5, 7.

### B3 — QB1(c) role exchange

- **B3.1 [X]** (b3): ROLEX(h): SWAP G SWAP = (h⊗h)G(h⊗h)⁻¹. cnot: 2 signed-permutation solutions (Hadamard type,
  h z = x). cnot1: none (classical CNOT is not role-symmetric). **gC5: 8 solutions** (h z = e_x), and gC5 has the
  reversed frame on ±e_x. Verdict: role exchange gives a strictly weaker gate; gC5 is the countermodel; missing TR.

### B4 — QB2 (K∞-Act, K∞-Drive, K∞-Trans)

- **B4.1 [W]+[K]** BoundaryTransitive Ω G (PreservesBody, compact convex, interior) ⇔ PureTrans (transitive on
  extreme points) ∧ BP (every boundary state extreme): ⇒ by TransitiveBody :284 and :290; ⇐ trivial.
- **B4.2 [X]** (b6): the qutrit (complex QT; PU(3) connected and transitive on pure states) has the non-extreme
  boundary state diag(1,1,0)/2, so no family is boundary transitive on it (kernel :301): any principle satisfied by all
  of finite complex QT (e.g. continuous reversibility, MMAP's CR) cannot yield K∞-Trans; K∞-Trans is elementary-scoped.
  The Carathéodory orbitope with SO(2): CR ✓ (exact), BP ✗ (exact), capacity ≥ 3 (exact Fejér effects) — not
  elementary. Drive control: kernel not_boundaryTransitive_flow (BP ✓, PureTrans ✗).
- **B4.3 verdict**: CR yields K∞-Act-type data + PureTrans (QT ✓ all n; bit ✗ (discrete), gbit ✗); the missing clause
  for K∞-Trans is BP (= K∞-Geom's strict-convexity content). Inside capacity two, whether CR forces BP: OPEN (wall;
  MM 2011 obtain BP from a separate subspace-type postulate [L, unverified]).

### B5 — QB3 (K∞-Copy)

- **B5.1 [X]** gC5 satisfies Rc(N_A, nC5) (b1 C5) with N_A = diag(1,−1,1,−1,−1) balanced and nC5 unbalanced; with
  kernel frame, relT(nC5), P±: a two-NOT native gate at d = 5 (splits (3,3)/(2,4), not conjugate). NC with token
  groups (Cov over {I,N_A}, actions {I,nC5}) holds exactly (b1 C8). Verdict: K∞-Copy independent of (a), (a-nat-token),
  (b1), (c).
- **B5.2 [W]+[K]** NC with type-level availability (N_B ∈ 𝒢_A) ⇒ relC(N_B,N_B) ⇒ CtrlGate ⇒ d ∈ {1,3}; (b2) at d = 3
  with SO(3): all z-flipping NOTs in SO(3) are π-rotations about axes ⊥ z, conjugate under SO(2)_z (frame-preserving):
  type covariance automatic.

### B6 — converse-test side checks

- Rebit (d = 2) under COND: relt N2.3 [P] excludes frame + P± at d = 2 through a singular tangent block. Re-checked
  [W]: at d = 2 the tangent block is one L ∈ Lsig; σ = diag(1,−1) forces α = 0 in A, so L = [[0,a₁,0],[a₁,0,0],[0,0,0]]
  (rank ≤ 2 < 3); σ = −id forces a = 0 (first row zero). Not relied on for any verdict.
- Classical bit under (b): a one-parameter group with P± maps the four pure products (the vertices of the simplex
  maxCone(eball 1)) into the simplex in both directions, so it permutes them; continuity forces the identity [W].
- Boxworld: Gross et al. / Al-Safi–Short [L, unverified]: reversible maps are local maps and system permutations; a
  COND gate with T ≠ id is neither (A⊗B forces T = id; SWAP∘(A⊗B) forces a constant map) [W].

### Fixed-point passes (§A.31)

- Pass 1 (B1–B3): NEW: relC = CI ∧ TR with TR the parity half; COND ⇒ CI only (gC5); NC coherence = TR; J/K flow at
  every odd d; gC5 role-exchange symmetric; gC5 two-NOT. 
- Pass 2 (B2.4, B4, B5): NEW: local rotations kill the J/K interaction exactly (W5, W7); K∞-Trans = PureTrans ∧ BP with
  the qutrit witness. 
- Pass 3 (skeptic pass on the favourable branches NC ⇒ relC and (b2) ⇒ d = 3): no NEW finding; NC is QT-consistent
  only with a lift of N squaring to I (Q2 countercontrol iX) and only with Cov over the orientation-preserving group (Q4);
  (b2) rests on an unverified citation; W5/W7 corroborate it on the J/K family only.
- Pass 4 (converse tests re-read against every principle; d = 2 and boxworld): no NEW finding.
- Pass 5 (skeptic pass on the QT converse of NC, on QB3's type-level route, and on provenance): no NEW finding.
  Corrections only: the written QT converse of NC is scoped to tests over the sphere, Cov over SO(3) and actions {I, N}
  (Post over all target rotations is QT-incompatible [W]: it forces a homomorphic lift, and the Klein-group lifts
  anticommute, the mechanism Q3 checks exactly for Comp); G8 no longer called
  "weaker" than CopyNatural (not comparable as stated); NB-1 credited for the two-NOT countermodel C2N and for the
  written reduction of the J/K map's positivity to the complex CNOT; the bit's exclusion under (a)/(a′) named
  (Entangling: `three_of_ctrlGate`; for COND, `not_entangling_one_ctrl` reads only the frame). Kernel citations
  re-checked: all 35 identifiers in RESULT §5 sit at their cited lines in the base.
- Three consecutive passes (3, 4, 5) without NEW findings for QB1 and QB3: the lower end of §A.31's 3–4. QB2 stops at
  an OPEN wall (capacity-two CR ⇒ BP).

### Gem classification (§A.31 output classes)

| id | finding | class | evidence |
|---|---|---|---|
| G1 | relC = CI ∧ TR; the block reduction reads only CI, parity needs TR; conditioning supplies exactly CI (gC5: COND ∧ P± ∧ ¬relC at d = 5) | **NEW** (hidden assumption: "conditioning" and "relC" differ by the tangent half) | [W]+[X]+[K]+[R] |
| G2 | the J/K flow: a continuous reversible, two-sided-positive, non-product, entanglement-creating (b5 N2: witness −2) interaction at every odd d ≥ 3 through gC5; equal to the QT controlled-U(1) group at d = 3 | **NEW** (separates "continuous interaction" from the selector; exposes that the literature route needs local SO(d)). Builds on NB-1's written reduction of the J/K map's positivity to the complex CNOT; NB-1 has no flow | [X]+[W] |
| G3 | local rotations destroy it: exact W5, W7 | **NEW** (locates the excluding clause; corroborates Krumm–Müller on this family) | [X] |
| G4 | natural conditioning: Cov∘Rel = Post ⇔ TR (given CI); each pair satisfiable at d = 5; QT-consistent with lift N ↦ X, not with iX, not with Comp (Klein group), not with O(3)-Cov | **NEW** (a principle with separations and a converse, though it re-expresses relC) | [W]+[X] |
| G5 | gC5 two-NOT relation with a balanced N_A: kernel-positive two-NOT native gate at d = 5 | **ELABORATING** (NB-1's two-NOT countermodels, now with kernel positivity and an exact relation) | [X]+[K] |
| G6 | gC5 is role-exchange symmetric (8 signed permutations); cnot1 is not | **NEW** (minor: excludes (c) as a selector) | [X] |
| G7 | K∞-Trans = PureTrans ∧ BP; the qutrit fails it for every family while satisfying CR | **ELABORATING** (sharpens the ROADMAP's elementary-scope note into an equivalence with a QT witness) | [W]+[K]+[X] |
| G8 | type-level availability replaces copy naturality under NC; under (b2) at d = 3 type covariance is automatic | **POSITIVE** (an availability form of K∞-Copy — the target's NOT is a reversible map of the control, with Cov over every z-flipper of the control's group — in place of the identification N_A = N_B; conditional on NC; not shown weaker than CopyNatural in general, the two are not comparable as stated) | [W]+[K] |
