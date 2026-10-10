# EQ4-P — the three-copy obstruction: result (research and design only)

Base: certified main `bcbc516f`, read-only at `scratchpad/eq/base/` (manifest checked at the start and at the end).
Protocol: `scratchpad/eq4/PROTOCOL.md` (frozen; not edited). Nothing here is adopted, frozen or governed. No Lean
toolchain exists here: every Lean text is **UNBUILT**. Running record: `NOTES.md` (N0–N9). Writes: only
`scratchpad/eq4/P/`.

Evidence tags:
- **[K]** landed kernel identifier at the base, `file:line` under `verification/lean-mathlib/OIBridge/`;
- **[X pN]** exact computation in this directory (own Gaussian-rational library `eq4_lib.py`, small sympy identities),
  over green controls and countercontrols, replayed byte for byte;
- **[W]** written argument (NOTES or the probe header), not kernel-checked;
- **[E xN]** exact-arithmetic exploration (a search or a sample): a lead, not a certificate;
- **[F xN]** floating-point exploration: certifies nothing;
- **[L, unverified]** literature not read at the source (egress to the hosts was blocked).

Abbreviations: P_j (j = 2b + t) the GHZ-basis projectors (fibre b = 2b₁ + b₂, t = 0 for GHZ₊, 1 for GHZ₋);
GD the GHZ-diagonal sector; S = cone{e_j + e_k} in GHZ-basis eigenvalue coordinates; W3 = ½ − GHZ;
κ = ½ + |000⟩⟨111| + h.c.; Z = {X : PT_j X ⪰ 0, j = 1, 2, 3}; PN_n the pair-network cone (tensor products of PSD
blocks of size ≤ 2); B_tw = cone{PT_j(σ_ij) ⊗ ρ_k} (the all-twin hull); C the CNOT Choi state.

## 0. Answer to the decisive question

> Can consistency across larger composite systems force the required extension of operations without assuming uniform
> composition or introducing the extension principle in disguise?

**Open.** Positive at the level of uniform composition, negative at five tokens, undecided at six tokens, with the wall
named and narrowed:

- **Uniform composition is derived, not assumed, inside six tokens.** One-token teleportation (a KT pairing on five
  tokens with one Bell state and one Bell effect) moves a token between triples; the three five-token instances
  KT(5; 40|312, 43|012), KT(5; 51|432, 54|132), KT(5; 02|534, 05|234) give `K₀₁₂ = K₃₄₅` (relabelled); five tokens give
  S₃ symmetry and local-filter (hence LU) invariance; KT(6; 012|345, 03|1425, 14|25) gives `K₃ = T(K₃*)` (c = 0) or
  `K₃ = K₃*` (c = 1) [X p1, p2 + W]. The mixed configuration (BS*, BS) is excluded inside six tokens at **−1/8**
  [X p2 B2]; nine tokens are not needed.
- **The CNOT Choi lever is the extension principle restated.** E3 holds direction by direction (KT on ≤ 7 tokens; 8 for
  the effect form) [X p4 + W]; generation from (s) and (2) steps never produces C or a GHZ-class state, and conditioning
  on larger-group effects is circular [X p5 + W].
- **Five tokens: negative.** The pair-network hierarchy `K_F = PN_F` (|F| ≤ 5; `K₃ = BS ≠ PSD₈`, full duals as effect
  sets) satisfies every KT constraint among families of at most five tokens [X p6 + W].
- **Six tokens: open.** Named wall: *the existence of a six-token family (K₃, K₄, K₅, K₆) with K₃ ≠ PSD₈ — equivalently
  (E3) with no GHZ-class state in K₃ — satisfying every crossing constraint among the subfamilies of six tokens.*
  Exact results that locate it:
  1. colouring lemma: every closed network of one-token PSD, two-token PSD and Z-type nodes, of any size, has value
     ≥ 0, so no finite network inequality of that form excludes W3-type elements [W + X p8];
  2. maximality: every co-self-dual K₃ leaves cone(BS ∪ Z) (certificate ν, ⟨ν, Zν⟩ = −4) [X p8]; every c = 1 K₃
     leaves cone(B_tw ∪ Z) (F, G, tr(FG) = −½) [X p10];
  3. **the GHZ-diagonal sector conditions do not decide it.** The section K₃ ∩ GD is a self-dual, G-invariant
     (|G| = 192), single-token-filter-invariant cone between twirl(BS) = S and S* [W + X p11], and that problem has
     the exact GHZ-free solution
     `K_A = cone{P_j + P_k, I − 2P_j, I − 2P_j + 2P_p (p ≠ j)}`, invariant under all 8! position permutations,
     containing W3 and κ, with PSD part exactly S [X p12 + W]; the c = 1 problem has the solution
     `K_tw = cone(twirl(B_tw) ∪ G·(I − 2P₀ + 2P₁))` [X p13]. Any closure at six tokens must use information the
     GHZ-diagonal twirl discards.
  Sharpened wall: *does K_A (or another GHZ-free sector solution) lift to an LU- and filter-invariant co-self-dual K₃
  that extends to K₄, K₅, K₆?* K_A passed every further necessary condition tested: filter-orbit co-self-positivity
  [F x9], the E2 (2,2,1) contraction on all generator pairs and sampled filter images [E x10], Bell-link ring, K₄ and
  3×3 Latin networks [E x11]. No lift was constructed and none was excluded.
- **Missing principle.** Choi availability of the native gate is IE₂ restated relative to P (both directions proved).
  Purification (pure = extreme ray) and transitivity (as cone automorphisms) are implied by IE₂ relative to P, so they
  are necessary in the owner's sense (P ∧ IE₂ ⇒ A, [W]; its density step uses EQ2's generation result, whose
  universality ingredient is [L, unverified]); their sufficiency is open, and purification's reduces to
  excluding mixed GHZ-free extreme rays on E. Transitivity read as an operation on parts of composites is an (o)-type
  premise. No candidate was shown to select the quantum completion without being IE₂ in disguise.

**Outcome table for IE₂ (owner's five cases).**

| case | at ≤ 5 tokens | at 6 tokens |
|---|---|---|
| 1. coherence alone selects the quantum cone | no (case 5 holds) | not established, not excluded |
| 2. coherence + uniform composition selects it | — | uniform composition is derived inside six tokens, so 2 coincides with 1 at the triple level; not established |
| 3. an additional finite symmetry selects it | — | invariance under G — even under all 8! permutations of the GHZ basis — does not select it (K_A); no other symmetry principle tested |
| 4. coherence yields only one inclusion | — | not the situation: both inclusions of K₃ = T(K₃*) are derived |
| 5. an exact countermodel survives everything | **yes**: the PN hierarchy | only a sector-level model (K_A; c = 1: K_tw); no full model |

**Classification: case 5 at five tokens; undecided between cases 1 and 5 at six tokens.**

## 1. Finding

### 1.1 N1 — the mixed configuration (Priority 1)

- **E1 confirmed** [X p1 + W], aligned and general charts, c = 0 and c = 1, general k. Exact: for all six matchings on
  each of A∪B, B∪C, A∪C, the Bell-state conditional is `(1/8)·T(Π_π f)` and the Bell-effect value
  `(1/8)·tr(x·T(Π_π y))` (all units); twin links give `(1/8)Π_π f`; general k (k = 1..4) gives `2^{-k} T Π` and
  `2^{-k} Π`. Pigeonhole: W3 ∈ BS* (Cauchy–Schwarz sum-of-squares, symbolic), W3 ∉ BS (eigenvalue −½); (BS, BS) fails
  (I3) and (BS*, BS*) fails (II3) at **−1/16** for every matching; all 8 assignments repeat a cone on a linked pair;
  c = 1: F, G ∈ B_tw* (symbolic block determinant `(|α|² − |β|²)²/4`), tr(FG) = −½, failures at −1/16, W3 ∈ B_tw by an
  explicit six-term decomposition. General charts reduce to the aligned case through LU invariance and `τ = δε + c`.
- **Gem (item 1, and item 4): six tokens decide Priority 1.** Teleportation lemma: on KT(5; zp|qst, zq|pst) with the
  Bell state of (z, q) and the Bell effect of (z, p), `tr[(Φ⁺_zp ⊗ g)(Φ⁺_zq ⊗ y)] = ¼·tr(g·y(p→q))` [X p2 A1–A2], so
  with closedness and full effects `K_pst = K_qst` (renamed); twin–twin: the same; Bell–twin: `PT_q` [X A3]; a product
  link does not teleport [X A4]. Composition of the three steps above gives `(1/64)` times the relabelling
  (0→3, 1→4, 2→5) on all units [X B1]; GHZ ∈ BS* = K₀₁₂ carried to (3,4,2) against W3 ∈ BS* = K₃₄₅* gives **−1/8**
  [X B2]; c = 1: (B_tw*, B_tw) at −1/8 [X B3]; S₃ symmetry from five tokens [X C]; general charts: the moved token
  gets `homMap(R₁ᵀR₂)` with parity `ε_p + ε_q` (c cancels) [X D1–D4]. Premises used: one body per token set, closedness
  and full effect sets of the intermediate triples, the gate on standalone link pairs; no uniform composition, no (o)
  step. Smallest instance: six tokens. **Hidden assumption exposed:** the audit's "(BS*, BS) satisfies every six-copy
  family" holds for the grouping 012|345 and its link groupings only; the mixed triples of the same six tokens exclude
  it. The route is through mixed triples, not through the four-token group cones.

### 1.2 N2 — the Choi lever (Priority 2)

- **E2 confirmed** [X p3 + W]. For a crossing (A|B, C|D) with P, Q, R, U the intersections:
  `(Λ_x ⊗ Λ_y)(K_B*) ⊆ K_A`, `Λ_x(g) = tr_R[(g ⊗ 1_P)x]`, **Choi(Λ_x) = PT_R(x)** [X E1–E3, five crossing types].
  Uniform corollary: `K_n ⊇ (id ⊗ Φ_y)(K_{n−b+a})` for every y ∈ K_{a+b}, where for c = 0 `Φ_y = Λ_y ∘ T` has
  **Choi matrix y** (input first) and for c = 1 Λ_y has Choi `PT_U(y)` [X U1–U3; (n,a,b) = (3,2,2), (4,1,2), (2,2,1),
  (3,1,2)]. The one-empty-intersection remark is confirmed [X M].
- **E3 confirmed, one direction at a time** (§A.34) [X p4 + W]:

| direction | witness | instance | evidence |
|---|---|---|---|
| (iv)⇒(ii) | the gate on two tokens of a triple is Ad(CNOT ⊗ 1); applied to `\|+⟩⟨+\| ⊗ Φ⁺` ∈ BS it gives ψ with Det ψ = 1/4 | K₃ ⊇ BS + (iv) | [X IV2, K1] |
| (ii)⇒(i) | own orbit lemma (Det = discriminant of det(sM₀ + tM₁); Det = 0 on cut products; constructive factorization), density, SLOCC invariance from five-token filters (singular included), closedness, co-self-duality | 5 and 6 tokens | [W + X II1a–d]; no Dür–Vidal–Cirac citation needed |
| (i)⇒(iv) | PSD₈ is unitarily invariant | — | [W]; control [X I4] |
| (iii)⇒(iv) | crossing (012\|345, 03\|1245), Bell link (0,3), C on (1,2,4,5): conditional `½(rename ⊗ Ad CNOT)` | 6 tokens (S₄ symmetry of K₄ for the arrangement of C, from teleportation at k = 4 [X p3 T]) | [X III4] |
| (i)⇒(iii) | crossing (0123\|456, 0145\|236), copy Choi state 2·GHZ, ψ₃ (Det 4): conditional `¼·C` | 7 tokens | [X I3] |
| (iii) state ⟺ effect | T(C) = C and K₄ = T(K₄*) | 8 tokens | [X D1 + W] |

- **The owner's distinction.** Definable: C ⪰ 0, C² = 4C, T(C) = C, so ρ ↦ tr(Cρ)/4 ∈ [0, 1] on every four-token body
  inside PSD₁₆ [X D1]. Not automatic: `w ∝ 1/16 − C/32` is ≥ 0 on every product across every 2|2 and 1|3 cut and
  tr(Cw) = **−2/7** [X D2]. Available on the actual four-token composite ⟺ C ∈ K₄ ⟺ (E3) IE₂.
- **Generation (N2.4).** Extended no-generation lemma [W + X p5]: PN is closed under products, transposition, local CP
  maps, closure, and conditioning of PN states on PN effects and of PN effects on PN states in every crossing (the
  contraction graph has degree ≤ 2); C ∉ PN₄ (Schmidt ranks [2,4,4,2,2,2,2]), GHZ, ψ₃ ∉ BS; a GHZ-class input escapes
  [X C′]. Using an effect of a larger group requires certifying it in K_G* first, which for C is (iii) itself.
  **No KT instance of any size forces (iii) by generation from (s) and (2) steps; KT can only exclude.**

### 1.3 N3 — the reduced wall

- **Five-token countermodel** (gem, item 3, as a lower bound) [X p6 + W]: described in §0. It fails at six tokens
  (−1/16) [X p6 S].
- **Six-token reduction** [X p7 + W]: the 3|3 × 3|3 ring is implied by the five-token constraints (ring = tr(MN), both
  contractions confined to the self-dual twin cone); with K₄ minimal, the remaining content is the K₄ ("glue")
  network, which is also the (1,2,1,2) Choi-closure crossing [X G]. Bell-link values for W3: theta 1/4, ring 7/4,
  K₄ 5/16, 5/16 [X W].
- **Colouring lemma** (NEW) [W + X p8]: proof by a 2-colouring of the contracted multigraph from an Euler circuit
  through an auxiliary vertex, then a partial transpose on the coloured token set making every node PSD. Colourings
  certified on theta, ring, both K₄ splits and the nine-token Latin square [X C1]; countercontrol: GHZ against W3 admits
  no colouring and gives −1/16 [X C2].
- **Maximality certificates** (NEW): c = 0, ν = I − 2GHZ₊ + 4GHZ₋ ∈ BS*, ⟨ν, z⟩ ≥ 0 on Z (symbolic on Z^GD),
  ⟨ν, Zν⟩ = **−4** [X p8 M1–M3]; c = 1, F and G nonnegative on Z^GD (symbolic), tr(FG) = **−½** [X p10].
- **The sector problem, decided** (NEW, item 4: a closure route ruled out with an exact model).
  Reduction [W; exact ingredients X p11]: the twirl over ⟨XXX, ZZ1, 1ZZ⟩ is the pinching in the GHZ basis on all 64
  units [H1]; Z₁, X₁, X₂, X₃, S₁S₂, SWAP₁₂, SWAP₂₃ permute the P_j and generate G = S₄ ⋉ (even within-fibre swaps),
  order 192 [H2]; T fixes GD [H3]; twirl(BS) = S [S1 + p1 P1]; single-token filters act on GD as nonnegative
  combinations of four elements of G [F]. So K₃ ∩ GD is a G-invariant self-dual cone between S and S*; if the orthant
  were its only solution, GHZ₊ ∈ K₃ and E3 would close the wall.
  **K_A** [X p12 + W]: 92 generators; written proof of K_A = K_A* (pairwise nonnegativity with the bound
  `⟨I − 2P_j + 2P_p, I − 2P_{j′} + 2P_{p′}⟩ = 8 + 4(δ_{jj′} − δ_{jp′} − δ_{pj′} + δ_{pp′}) ≥ 0`, the 8 being the sector
  dimension, and an explicit decomposition of every point of K_A*); exact double description in two orders returns
  exactly the generators, each extreme; the written decomposition reproduces 300 random exact points of K_A* (150 with a
  negative entry); K_A ∩ R⁸₊ = S; GHZ₊ ∉ K_A. Explorations [E x3–x8]: extreme-ray completions from S find only the
  orthant; non-extreme greedy completion regresses (rays approaching (−1, 1⁶, 3)); seeding with κ and that limit ray
  gives K_A (after adding W3) and a second solution K_B (not certified).
- **c = 1** (NEW, item 4) [X p13]: twirl commutes with every PT_j and PT_j maps GD into GD [B1]; S_tw = twirl(B_tw) is
  generated by the G-orbits of e₀ + e₁ and t = (1,1,1,1,1,−1,1,−1) [B2 + W: block argument], cross-checked on 30
  random B_tw generators [B3]; K_tw (36 generators) is G-invariant, pairwise ≥ 0, equal to its dual by exact double
  description (two orders) and by an independent exact simplex on 300 random points of K_tw* [T1–T3]; W3 ∈ cone(S_tw),
  GHZ₊ ∉ K_tw, F ∉ K_tw [T4]. A first written decomposition for K_tw was wrong and is not relied on (NOTES N3.8).
  **c = 1 is not excluded by the GHZ-diagonal sector conditions**; it remains undecided.
- Explorations with no lead: x1, x2 (networks with SLOCC images of W3 and κ, minima ≈ 1e−18) [F]; x7 (filter-orbit
  condition on ρ(β, z) coincides with the sector bound β ≤ 3z²) [F]; x9, x16 (filter-orbit co-self-positivity of K_A,
  K_B, K_tw generators, worst −5e−17) [F]; x10, x11, x15 (contractions and networks with K_A / K_tw nodes) [E]. The
  twin-link contraction test (x15) also passes for GHZ, so it does not discriminate at that instance.
- **Fixed point (§A.31):** not reached; one pass without a NEW finding since the last NEW one (K_tw), the protocol asks
  for 3–4.

### 1.4 N4 — candidate principles (entered because N3 did not close)

P = KT∞ with the transported pair premises, closedness and full `IsEffectOn` effect sets; C = IE₂. Common fact [W]:
P ∧ IE₂ ⇒ K_n = PSD_n for every n (E3, then E2 with a = b = 2 makes every K_n gate-invariant on any two tokens, the
gate and local unitaries generate a dense subgroup — EQ2's generation result, whose universality ingredient is
[L, unverified] — closedness and co-self-duality at 2n tokens).

| candidate | (a) level | (b) P ∧ A ⇒ IE₂ | (c) P ∧ IE₂ ⇒ A | (d) model of P ∧ IE₂ ∧ ¬A | classification |
|---|---|---|---|---|---|
| Choi availability of the gate (iii) | state-level form, operation content | proved, 6 tokens [X p4 III4 + W] | proved, 7 tokens [X p4 IV2, II1, I3 + W] | none | **IE₂ in disguise** relative to P |
| purification Pur₁ (pure = extreme ray) | state-level | open: support lemma — any w ∈ BS* with tr₃w = D/2 is supported on E = span{\|00⟩,\|11⟩} ⊗ C² and PSD there [W + X p9 S1–S4]; rank-one purifications are GHZ-class (Det = (u₀w₁ − u₁w₀)²) [X S3]; remaining case: mixed PSD extreme rays on E (ω_{1/2} exists as an operator: PSD, rank 4 on E, not biseparable, −1/8) [X R] | proved (common fact) | none (P ∧ IE₂ gives QM) | implied by IE₂; sufficiency open |
| transitivity, reading 1 (operations acting on composites) | operation-level | — | proved | none | reintroduces (o)-type extension; circular as a premise |
| transitivity, reading 2 (automorphisms of K_n) | geometric | open | proved | none | implied by IE₂; sufficiency open |

Bearing of N3.7 [W, partly heuristic]: in any K₃ whose GD section is K_A, a PSD element must have GHZ-fidelity ≤ ½ after
every local filter (its filtered twirls lie in K_A ∩ R⁸₊ = S); ω_{1/2} (fidelity 5/8) is excluded. Whether this
excludes every purification of D/2 within one token — which would make Pur₁ fail in every K_A-type completion — is
research question RQ4, not a claim.

### 1.5 N5 — literature

`WebFetch https://arxiv.org/abs/1006.4651` failed (`getaddrinfo ENOTFOUND arxiv.org`); not routed around. From search
summaries only, all **[L, unverified]**: Gühne–Seevinck NJP 12 053002 (2010) (GHZ-diagonal criteria; not load-bearing,
own Cauchy–Schwarz proof and the side fact twirl(BS) = S); Dür–Vidal–Cirac PRA 62 062314 (2000) (GHZ and W classes;
superseded here by the own orbit lemma); Chiribella–D'Ariano–Perinotti PRA 81 062348 (2010) (purification with
uniqueness, on top of local discriminability and causality); Barnum–Wilce arXiv 1202.4513 and Barnum–Graydon–Wilce
Quantum 4, 359 (2020) (Jordan-algebraic composites; presuppose homogeneous self-dual cones, which KT does not supply —
K_A is self-dual and highly symmetric but not shown homogeneous); Müller–Ududec PRL 108 130401 (2012) (bit symmetry
forces self-duality). No source addressing the tripartite wall was found (summaries only).

## 2. Target theorems (UNBUILT)

No Lean toolchain; the text below is design only, in operator form. The bridge to the base's table vocabulary (`W 3`,
`cnot`, `phiW`, `prodState`, `pairVal`, `IsEffectOn`, `PreComposite`, `Composite`) is the transcription control
[X p1 K0–K5: `cnot` = Ad(CNOT) in the Pauli dictionary, `phiW` = coords(Φ⁺), `idW` = coords(SWAP/2), `reflY` = one-qubit
transpose, `pairVal` ↔ operator pairing]. Multi-token families need COMP-1 carriers the base does not have; each
statement is therefore phrased with its KT instance as an explicit hypothesis family of inequalities.

```lean
-- UNBUILT. Op n := Matrix (Fin (2^n)) (Fin (2^n)) ℂ; cones are closed convex subsets of Hermitian Op n.
-- KTPair K S A B C D : the crossing inequalities ⟨K_A* ⊗ K_B*, K_C ⊗ K_D⟩ ≥ 0 of the bipartitions A|B, C|D of S.

/-- T1 (E2). Conditional of a crossing; Choi matrix with the transpose pinned. -/
theorem crossing_conditional (x : Op (P ∪ R)) (y : Op (Q ∪ U)) (f : Op (R ∪ U)) :
    condA f (x ⊗ y) = (lam x ⊗ lam y) f ∧ choi (lam x) = ptranspose R x
theorem crossing_inclusion (hKT : KTPair K S A B C D) (hcl : ∀ F, IsClosed (K F)) :
    ∀ x ∈ K C, ∀ y ∈ K D, (lam x ⊗ lam y) '' (dual (K B)) ⊆ K A

/-- T2 Teleportation (five tokens). -/
theorem teleport (hKT : KTPair K {z,p,q,s,t} {z,p} {q,s,t} {z,q} {p,s,t}) (hcl) (heff) (hgate : bell z q ∈ K {z,q}) :
    K {p,s,t} ≅[rename p q] K {q,s,t}

/-- T3 Six-token uniformity and the exclusion of (BS*, BS). -/
theorem six_token_uniform (h : KT on the three five-token instances) : K {0,1,2} ≅[0↦3,1↦4,2↦5] K {3,4,5}
theorem no_mixed_BS (h) : ¬ (K {0,1,2} = BSstar ∧ K {3,4,5} = BS)   -- certificate value −1/8

/-- T4 (E1, triangle). Symmetry and co-self-duality from KT(6; 012|345, 03|1425, 14|25). -/
theorem co_self_dual (h) : (∀ π : Perm (Fin 3), permute π (K3) = K3) ∧ K3 = transpose '' dual K3      -- c = 0

/-- T5 (E3), one theorem per direction, each with its instance size (§1.2 table):
    e3_iv_ii, e3_ii_i, e3_i_iv, e3_iii_iv, e3_i_iii, e3_iii_state_effect. -/

/-- T6 Orbit lemma. -/
theorem ghz_orbit (ψ : ℂ^8) (h : hyperdet ψ ≠ 0) : ∃ A B C : GL (Fin 2) ℂ, (A ⊗ B ⊗ C) • ghzVec = ψ

/-- T7 No generation. -/
theorem pn_closed_conditioning : ∀ crossing, ∀ x y ∈ PN, ∀ e f ∈ PN, condA (e ⊗ f) (x ⊗ y) ∈ PN
theorem cnot_choi_not_pn : choiCNOT ∉ PN 4

/-- T8 Five-token countermodel. -/
theorem five_token_model : ∀ F, F.card ≤ 5 → KTCoherent (fun F => PN F) F ∧ PN 3 ≠ PSD 3

/-- T9 Colouring lemma. -/
theorem coloring_network_nonneg (N : ClosedNetwork) (h : ∀ v, N.node v ∈ PSD1 ∪ PSD2 ∪ Zcone) : 0 ≤ N.value

/-- T10 Maximality certificates. -/
theorem max_c0 : ν ∈ dual (cone (BS ∪ Zcone)) ∧ ⟪ν, Ad Z₀ ν⟫ = -4
theorem max_c1 : F ∈ dual (cone (Btw ∪ Zcone)) ∧ G ∈ dual (cone (Btw ∪ Zcone)) ∧ ⟪F, G⟫ = -1/2

/-- T11 Purification support lemma. -/
theorem purif_support (w) (hw : w ∈ BSstar) (hm : ptrace 3 w = D/2) : supportedOn E w ∧ PosSemidef (restrict E w)

/-- T12 Sector reduction and the two sector models (polyhedral, over ℚ⁸). -/
theorem sector_reduction (hK : Admissible K3) : SectorSolution (K3 ∩ GD)       -- G-invariant, self-dual, S ≤ · ≤ S*
theorem KA_self_dual : dual KA = KA ∧ G_invariant KA ∧ S ≤ KA ∧ KA ≠ orthant    -- written proof available
theorem Ktw_self_dual : dual Ktw = Ktw ∧ G_invariant Ktw ∧ Stw ≤ Ktw             -- certificate: 36 extreme rays
```

## 3. Hypotheses ledger (independence evidence under the P/A/C rule)

| hypothesis | tag | source | used by | independence evidence |
|---|---|---|---|---|
| KT on the stated families (one body per token set; COMP-1 on each bipartition) | (s) | unsourced at the base (the protocol's KT∞) | everything | the PN hierarchy satisfies it on ≤ 5 tokens with K₃ = BS [X p6]: KT(≤ 5) does not give IE₂ |
| full `IsEffectOn` effect sets | (s) | [K KF:116, CI:228 `prodEff_effect`] | all exclusions | dropping it removes every dual-side argument (the exclusions use the full duals) |
| closedness of every body (H-closed) | (s) | premise; cf. [K CI:431] `condA_mem`, which assumes `IsCompact ΩA` | inclusions (I) | needed for `K** = K`; not tested for independence |
| native gate (and inverse) on standalone pairs | (2) | transported two-copy premises | Bell links, filters, teleportation | the five-token countermodel satisfies it [X p6 K1] |
| pair cones Q3 / twin, IE₁, chart parity | (s)+(2) | KT(4) (EQ3, settled) | charts, c | — |
| uniform composition | — | **derived** (six tokens) [X p2] | — | not assumed anywhere |
| LU / filter invariance of triples | — | **derived** (five tokens) [X p4 II1d] | E3, sector | — |
| co-self-duality K₃ = T(K₃*) | — | **derived** (six tokens) [X p1] | E3, sector | — |
| A₁ Choi availability | (s) form | candidate | — | P ∧ A₁ ⇔ P ∧ IE₂ (both proved): not independent of C |
| A₂ purification Pur₁ | (s) | candidate | — | P ∧ IE₂ ⇒ A₂ [W]; P ∧ A₂ ⇒ IE₂ open |
| A₃ transitivity (reading 2) | geometric | candidate | — | P ∧ IE₂ ⇒ A₃ [W]; P ∧ A₃ ⇒ IE₂ open |

Models: P(≤ 5 tokens) ∧ ¬IE₂: the PN hierarchy [X p6]. Sector conditions ∧ ¬IE₂: K_A (c = 0) [X p12], K_tw (c = 1)
[X p13] — models of necessary conditions only, not of P at six tokens. No model of P(6) ∧ ¬IE₂ and no proof of
P(6) ⇒ IE₂.

## 4. Missing lemmas

- **ML1 (the wall, first half).** Lift of K_A, or of any GHZ-free solution of the sector problem, to a closed,
  LU- and filter-invariant, S₃-symmetric K₃ with K₃ = T(K₃*) and K₃ ∩ GD = K_A — or an obstruction that uses
  information outside GD (general product filters, other twirl sectors, the full 64-dimensional co-self-duality).
- **ML2 (the wall, second half).** Extension of such a K₃ to K₄, K₅, K₆ satisfying every crossing constraint among six
  tokens (the K₄ glue network and the E2 maps with a + b = 4 included).
- **ML3.** The c = 1 versions of ML1–ML2 for K_tw.
- **ML4.** Purification sufficiency: exclusion of mixed PSD extreme rays on E with marginal D/2 in every GHZ-free
  completion.
- **ML5.** Structure of the twirled general product filters twirl ∘ Ad(A ⊗ B ⊗ C) on GD (single-token filters are
  certified [X p11 F]; K_A and K_tw pass sampled and float tests only).
- **ML6.** Twin-link (c = 1) filter teleportation: written only (p2 A3 certifies the unfiltered twin case).
- **ML7 (formal).** COMP-1 carriers for families of five or more tokens; orbit lemma over ℂ; Euler circuits in
  multigraphs; partial trace and partial transpose on `Matrix (Fin (2^n))`.

## 5. Formalization strategy (proposed; nothing frozen; the owner decides)

| proposed round | content | cost | prerequisites |
|---|---|---|---|
| F-a crossing calculus | T1 (E2 identity, Choi with transposes) on explicit matrices | low–medium | partial trace / transpose definitions |
| F-b exclusion certificate | T3's −1/8 and the pigeonhole values −1/16 (E1) as rational matrix identities | low | conventions of F-a; the transcription control |
| F-c sector model K_A | T12 for K_A: self-positivity and the written decomposition, a finite case analysis over ℚ⁸ | low–medium | none beyond ℚ linear algebra |
| F-d teleportation and uniformity | T2, T3 as consequences of explicit crossing-inequality hypotheses | medium | interface `FiveTokenCoherent K …` (inequality families, no carrier) |
| F-e E3 cycle | T5: (iv)⇒(ii) cheap; (iii)⇒(iv), (i)⇒(iii) medium (six-, seven-token identities); (ii)⇒(i) heavy (T6, density, closure) | medium–high | F-a; T6 |
| F-f colouring lemma | T9 | medium | Euler circuits in multigraphs (not checked against the Mathlib snapshot) |
| F-g five-token model | T8 | high | all crossing types on ≤ 5 tokens |

Recommendation for the owner: if a kernel design check is wanted, F-b and F-c are the cheapest decisive items (one
exclusion, one sector model); this thread runs none.

## 6. Research questions

- **RQ1 (the wall).** Does a six-token family exist whose K₃ has GD section K_A? Next computation proposed: the
  ten-dimensional GHZ-coherence sector (diagonal entries and the |000⟩⟨111| coherence; the fixed space of the local
  phases with zero sum), on which the diagonal-filter semigroup acts within the sector. Written observations: a
  K_A-compatible section there must give zero coherence to operators supported on {|000⟩, |111⟩} alone (K_A's two-
  position faces are single rays) and needs W3-type elements to be self-dual.
- **RQ2.** Classification of the solutions of the sector problem: K_A and K_B were found (x8); is the solution set
  finite, or a continuum? Is K_A the only solution whose PSD part is S?
- **RQ3.** c = 1: does K_tw lift; can c = 1 be excluded at six tokens by constraints outside GD?
- **RQ4.** In a K_A-type completion, is every purification of D/2 within one extra token excluded (Pur₁ fails), so
  that purification would exclude all K_A-type completions?
- **RQ5.** Is there a finite KT network with κ-type nodes and a negative value? The colouring lemma does not cover κ;
  all sampled networks are ≥ 0, several exactly 0 (κ sits on the boundary of its own filter-orbit condition:
  ⟨κ, Z₀κ⟩ = 0).
- **RQ6.** Which symmetry, beyond those derived from P, would select the orthant in the sector — and is any such symmetry
  IE₂ in disguise relative to P (the owner's P/A/C test)?

## 7. Evidence and probe log

**Exact probes** (all `python3 -I -B`, argument `scratchpad/eq/base/verification/lean-mathlib/OIBridge`; sha256 first
16 hex; recorded = replayed output):

| probe | checks | verdict | runs / pre-run edits | script | output |
|---|---|---|---|---|---|
| p1_e1_triangle | 26/26 | P1-E1-TRIANGLE-EXACT | 1 / a dead expression removed | 8e7d701fc4b5ea3f | 14ba9e6cfab7924d |
| p2_teleport | 14/14 | P2-TELEPORT-EXACT | 1 / D3 restructured | ca6ec9111fdddf31 | 658c3c3bf3b6bc4e |
| p3_crossing_calculus | 10/10 | P3-CROSSING-CALCULUS-EXACT | 1 / none | 2250f6fb65113148 | 650e2945f0678ac5 |
| p4_e3_directions | 12/12 | P4-E3-DIRECTIONS-EXACT | 2 (run 1 kept, see below) / `Fr(sp.Rational(…))` → `int` | bfdb1c1f8624f018 | 37c59c5366bb2747 |
| p5_generation | 5/5 | P5-GENERATION-EXACT | 1 / countercontrol moved to type (1,2,1,2) | cb73c052ba0e1994 | bbf6fcbf20f0acfa |
| p6_five_token_model | 7/7 | P6-FIVE-TOKEN-MODEL-EXACT | 1 / none | 2983706025fe7966 | 7c563f65161a7cf0 |
| p7_wall_reduction | 7/7 | P7-WALL-REDUCTION-EXACT | 1 / contraction over P only; slice pair; unused expression | da018fbebd67a5f6 | a1f7d3242234c2b9 |
| p8_coloring | 10/10 | P8-COLORING-EXACT | 1 / none | ad1c3a6223febb4f | 68f03717d57ff60f |
| p9_purification | 6/6 | P9-PURIFICATION-EXACT | 1 / none | 39e26888d1b15936 | d6214a8c255207ea |
| p10_c1_maximality | 5/5 | P10-C1-MAXIMALITY-EXACT | 1 / none | ce76aaf573f3a918 | 6b332a3197881cc1 |
| p11_sector_reduction | 8/8 | P11-SECTOR-REDUCTION-EXACT | 1 / `.scale` on a scalar → `* 2` | cac1d35e0838b198 | 8c246bf96c570713 |
| p12_sector_selfdual | 5/5 | P12-SECTOR-SELFDUAL-EXACT | 1 / none | cf549d138c825579 | 27776d481e2eba78 |
| p13_c1_sector | 8/8 | P13-C1-SECTOR-EXACT | 1 / comparison with t/2 (and its header line) | 0e3dbec81d2ba7a8 | 6345758fd01285aa |

Library `eq4_lib.py` cc2c6aca94007ac8 (a stray expression in `hyperdet` fixed before any use). Replays: `run_all.py`
(p1–p13) **VERDICT RUN-ALL-OK** — exit 0, empty stderr, byte-identical stdout for all 13 (runs over p1–p10 and p1–p12
kept as `run_all.run1.*`, `run_all.run2.*`); `run_x.py` (exact explorations x3, x4, x6, x8, x10–x15) **VERDICT
RUN-X-OK**. Every `python3 -I` run has a fresh hash seed, so identical replays also test determinism.

**Explorations** (leads only; hashes in NOTES N9): x1, x2 network minima with W3 / κ nodes [F]; x3–x6, x8 sector
searches [E] (x5 stopped by hand in a regress; its `.err` has no exit line because `pkill` also ended the wrapper);
x7 filter-orbit bound [F]; x9, x16 filter-orbit co-self-positivity of K_A, K_B, K_tw [F]; x10, x11 K_A contraction and
networks [E]; x12–x15 c = 1 sector searches and tests [E].

**Harness errors and deviations.**
- p4 run 1: `TypeError` (`1 / trw`, no `__rtruediv__` on the Gaussian-rational class) after 11 passing checks, before
  any verdict; kept as `p4_e3_directions.run1.{py,out,err}`; fixed to `L.ONE / trw`, decision rule unchanged.
- Pre-run edits as listed in the table (each made before the script's first run).
- x2: the κ / W3 choice per node is keyed to the sign of a parameter that BFGS may move (recorded in its own comment);
  every evaluated configuration is still a valid candidate; its docstring carries a stray line copied from x1.
- Bell-network values for κ and the 3×3 Latin value 13/8 were first computed in an unrecorded inline exploration;
  they are re-certified under a decision rule in p11 N.
- A first written decomposition for K_tw was wrong (it ignored sign cancellations on a fibre); K_tw's self-duality
  rests on the exact double description and the independent exact simplex in p13, not on that decomposition.
- Egress: arXiv blocked (`getaddrinfo ENOTFOUND`); not routed around; literature is [L, unverified].

**Integrity.**
- Start (04:01 UTC): base manifest silent, exit 0; repository clean, HEAD `bc3bf9bc846c138de5f5b45f386a75244da4f21f`;
  `scratchpad/eq4/P/` empty; `.start_marker` 2026-10-09T04:01:01Z.
- End (07:11 UTC): base manifest silent, exit 0; repository clean; **HEAD is
  `f0d37906a83585efdaca8e3ee3404410e869c43e`, not bc3bf9bc.** Read-only inspection: bc3bf9bc is an ancestor; the reflog
  shows checkouts to `claude/eq4f-preflight` and `claude/network-tool-access-8jtdhm` and a commit "EQ4-F preflight
  (design only, not for merge): four-copy package statement layer" (2026-10-09 06:58:32 +0000). This thread ran no git
  write (only `status`, `rev-parse`, `cat-file`, `merge-base --is-ancestor`, `log`, `diff --stat`, `reflog`). Recorded
  as a provenance anomaly in the repository caused by another writer (§A.26); it does not touch this thread's evidence,
  which reads kernel conventions only from the base snapshot (manifest intact). No measurement was run after its
  detection; nothing outside `scratchpad/eq4/P/` was modified.
- Every file under `scratchpad/eq4/P/` is newer than the start marker and was written by this thread. Newer files
  elsewhere in the scratchpad (`eqreview/REVIEW.md`, `eqreview/audit_eq4f.*`, `eqreview/replayEQ4F/*`,
  `eq4/names.txt`, `eq4/preflight/*`) belong to other agents and were neither written nor read here.
