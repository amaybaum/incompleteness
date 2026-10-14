# Thread E — Bell correlations and the composite clause of a finite OI→QM theorem

Base: `main` at M = `5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5`. Read-only research note. Every `file:line`
is at M, paths under `verification/lean-mathlib/OIBridge/` unless stated. Nothing here changes a status.

Labels: **[K]** kernel declaration at M (file:line); **[K-inst]** a direct instantiation or two-line
composition of [K] declarations that is *not itself* a named kernel theorem; **[D]** design evidence
(branch + run id, not adopted); **[W]** written argument in this note; **[X]** exact computation
(script and output below); **[L]** published literature, cited, not reproduced; **[U]** unsourced or
unchecked.

Exact checker: `threads/E-work/e_bell_check.py` (stdlib only, Fractions, Q(√2), Gaussian rationals).
It transcribes the kernel's own objects: `hom`, `prodState`, `pairVal`, `actT`, `sgn/pc/pt/cnotFun`,
`phiW`, `xplus`, `z3` (CompositeDimension.lean :100, :161, :164, :198, :741–758, :1213, :1220), `sharpVec`
(EffectSpace.lean :57), `pauli`/`dict` (EqvK2Schema.lean :25, :78), `reflY`/`idW` (K2Guard.lean :46, :101).
Run `python3 -I -B e_bell_check.py`: 12 checks, 0 failures, `VERDICT E-BELL-EXACT`. Output SHA256
`df6c2f6b…414c`, replayed byte-identically, stderr empty. Three mutations are rejected: M1, the
unsigned cnot, fails C1; M2, the uncorrelated sum, fails C4, C5 and C8b; M3, the product input,
fails C4. Finite checks are controls. Universal statements are the [W] arguments.

***

## 0. Two objects that must stay apart

**(i) Operational Bell content.** The joint state cone and the local tests of the operational theory
give a set of behaviours `p(a|x)`. Within that set: entangled states, CHSH violation up to 2√2,
no-signalling, and local tomography. This content belongs to ROADMAP row K, clause **K2**
(ROADMAP.md :1010–1018), and to its k-token continuation.

**(ii) H-Bell.** This is the substratum and gravity obligation. Preparation-indexed state-dependent
graphs must preserve operational no-signalling **and** satisfy the Ollivier–Ricci stability condition
(ROADMAP.md :954–969; papers/Substratum.md :132 adds an ontic-parameter conjunct). Upstream of it, the
hop metric of the cubic reference graph is ℓ¹ and fails before any Bell edge is added. H-Bell is a
question about the hidden-ontology realization: a deterministic completion that must, by the Bell
ceiling of papers/Main.md §3.3 (:356–394), use ontic parameter dependence. It is not a question about
the operational behaviour set.

Record facts:

- ROADMAP :1018 says "K2 does not discharge H-Bell".
- PROGRAMME.md Arc E (:485–503) asks for the relation between OI composites and the quantum
  correlation set, including any extra principle. Rule 5 (:569) keeps single-system and Bell claims
  distinct.
- **HB-1** (`verification/programmes/oi-qm/h-bell/round-hb-1-obligation-shape/preregistration.md`,
  merged a96b3571 on 2026-09-15) is a type-P census control plane with a zero definition budget. It
  is **frozen and never executed**. `verification/infrastructure/round-v3-12-retirement-census/preregistration.md`
  :222–227 lists it among the "legacy rounds never executed". Its blob is pinned in
  `verification/infrastructure/legacy-records.json` :246. Under §A.37, continuing it is a new native
  round that cites it.
- The research ledger (`origin/research/equivalence:research/equivalence/LEDGER.md`, base 9f9f8257)
  says: "the operational Bell content belongs to K2 (pair cone), not to H-Bell (NOTES-E6 §1)".
  **Re-verified at M: this still holds.** No kernel object for H-Bell exists, and HB-1 has no
  result. The ledger's K2 row is stale. It predates `pairCone_eq_Q3_of_drive_maxCone` and still
  lists H3 and ReachPure. Its ROADMAP line references shift by about one line at M.

**Consequence for the target.** The target theorem should carry clause (i) and state an explicit
non-claim about (ii). Section 7 also gives a consistency fact. If the operational clause attains 2√2,
the Bell ceiling forces any deterministic completion to be non-screened or non-graph-local. That is
H-Bell's subject. It is not a contradiction, and it stays outside the theorem.

***

## 1. What is proved at M about the pair cone (OI-PAIR-MAXCONE-1)

Record: `verification/programmes/oi-qm/reconstruction/round-oi-pair-maxcone-1/{preregistration,result}.md`,
receipt `verification/receipts/OI-PAIR-MAXCONE-1.json`, outcome `OI-PAIR-MAXCONE-1-PROVED`. Modules:
EqvK2Schema, EqvK2Converse, EqvK2Block, EqvK2Generation, BridgeDictionary, BridgeConverge and
EqvK2MaxCone, registered kernel-only.

Objects [K]:

- The carrier is `W 3 = Fin 4 → Fin 4 → ℝ` (CompositeDimension.lean :97). Its docstring says local
  tomography is the premise this carrier encodes.
- `prodState` :161; `maxCone Ω` :186, nonnegativity on every product of effects of Ω; `cnot` :775,
  a signed permutation of the 16 entries; `actT N` :198, N acting on the target (second) token.
- `dict ω = ¼ Σ ω_μν σ_μ⊗σ_ν` (EqvK2Schema.lean :78). `dictEquiv` :216 is an equivalence onto the
  Hermitian 4×4 matrices.
- `Q3 = {ω | dict ω PSD}` :239, the two-qubit PSD cone. `Q3_selfDual` :343.

Theorems [K], all in EqvK2MaxCone.lean, `K : Set (W 3)`:

| decl | line | hypotheses → conclusion |
|---|---|---|
| `subset_Q3_of_maxCone_block` | :116 | `K ⊆ maxCone (eball 3)` + `BlockInvariant K` → `K ⊆ Q3` (no products, no cone closure) |
| `Q3_subset_of_products_cone_block` | :107 | products of `eball 3` in K (H1) + addition + nonnegative scaling + `BlockInvariant K` → `Q3 ⊆ K` |
| `pairCone_eq_Q3_of_block_maxCone` | :130 | H1, hadd, hsmul, hmax, BlockInvariant → `K = Q3` |
| `pairCone_eq_Q3_iff_block_maxCone` | :145 | given H1, hadd, hsmul, hmax: `K = Q3 ↔ BlockInvariant K`. Forward witness `blockInvariant_of_eq_Q3` :139 |
| **`pairCone_eq_Q3_of_drive_maxCone`** | **:153** | H1, hadd, hsmul, hmax, **hH2** (`∀ω∈K, cnot ω ∈ K`), **hA** (`∀t, actT (rotLin t)` and `actT cycEquiv` preserve K) → `K = Q3` |
| `pairCone_eq_Q3_iff_drive_maxCone` | :174 | given H1, hadd, hsmul, hmax: `K = Q3 ↔ (hH2 ∧ hA)`. Forward witness `driveInvariant_of_eq_Q3` :165 |
| `maxCone_bound_of_sharp_available` | :194 | `K ⊆ maxConeOf avail` + `sharpFamily 3 ⊆ avail` → `K ⊆ maxCone` (no EffectsOn) |
| `pairCone_eq_Q3_of_sharp_available` | :204 | the generator theorem, with hmax replaced by validity on an available family that contains the sharp tests |

Hypothesis map:

- **Products clause:** H1 says products lie in K. That is membership, not preparation.
- **Explicit cone closure:** hadd, hsmul.
- **Product-test positivity:** hmax, or hvalid together with `sharpFamily 3 ⊆ avail`.
- **Gate:** hH2. This is *invariance* of K under the table map `cnot`.
- **Local actions:** hA. This is *invariance* under the full third-axis flow and the cyclic map on
  the target token only. It derives SU(2)×SU(2) block invariance through
  `EqvK2Generation.blockInvariant_of_drive` :426.
- Self-duality, topological closedness and ReachPure are not used.

The result note lists the open source obligations: the physical state/test identification, product
preparation and cone realization, product-test validity on the actual pair, enough available tests,
and preservation by the gate and the actions.

Related kernel facts at M:

- **Entangled witness [K].** `phiW` (CompositeDimension.lean :1220) is the table diag(1,1,−1,1).
  `cnot_prodState_xplus_z3 : cnot (prodState xplus z3) = phiW` :1222. Also `phiW_not_product` :1232,
  `phiW_mem_jointStates` :1246, and `entangling_cnot` :1380 (an extreme non-product joint state).
- **Orientation no-go [K].** `K2Guard.no_candidateCone_cnot_reflY` :143: no K with products ⊆ K ⊆
  maxCone is invariant under both `cnot` and the one-copy reflection `reflY`. Also
  `actT_reflY_phiW : actT reflY phiW = idW` :106.
- **COMP-1 interface [K].** `PreComposite` and `Composite` (CompositeInterface.lean :223, :243). The
  product pairing `prodEff` is bilinear by type (:210–220).
  - Local tomography is the field `lt` (:243) and is never derived.
  - The padding control `no_composite_over_paddedPre` :895 shows that `lt` is independent of the
    other eight fields.
  - `eff_margA` :376 (L3): `e (margA ω) = prodEff e unit ω`.
  - `condA_prodState` :332 (L9) is no-signalling **on product states only**.
  - The body lies between the minimal and maximal bodies (`minBody_subset` :461, `subset_maxBody` :467).
- **k-token at M.** No k-token carrier, dictionary or theorem exists. Every carrier is two-slot. The
  ROADMAP lists "composition beyond two tokens" as open (:1016–1017).

***

## 2. What follows for correlations — and what is proved where

### 2.1 Bounded search for the inference

At M, `git grep -i 'tsirelson|CHSH|signal'` over `verification/lean-mathlib` and `verification/lean`
finds no CHSH, Tsirelson, Bell-inequality or general no-signalling declaration. The only hits are the
L9 docstring (CompositeInterface.lean :36, :331) and `sqrt 2` arithmetic in QuantumRepresentationT2.lean.

The same search on the research branches finds no CHSH/Tsirelson Lean either. The hits are archive
prose and probes (`research/equivalence`, `research/archive`, `research/overview`, `research/bridge`,
`research/countermodels`). The draft and plan branches carry only copies of PROGRAMME and HB-1.

**So the step "K = Q3 ⇒ quantum (Tsirelson-bounded) correlations" is proved nowhere in the kernel.**
It is standard quantum mechanics (Tsirelson 1980) [L]. The pair-specific steps below are [W] and
[X] in this note.

### 2.2 Exact facts on the kernel's own objects [X] (`e_bell_check.py`)

- **C1.** `cnot (prodState xplus z3) = phiW`, which replays CompositeDimension.lean :1222.
- **C9.** `dict phiW = |Φ+⟩⟨Φ+|` exactly.
- **C11.** `T_ij = Tr(dict phiW · σ_i⊗σ_j)` for i, j ∈ {1,2,3}. This is the dictionary for correlators.
- **C2–C5.** Use product sharp tests `sharpEff(±a) ⊗ sharpEff(±b)` with
  `a ∈ {x̂, ẑ}` and `b ∈ {(x̂±ẑ)/√2}`. All probabilities lie in [0,1] and sum to 1. Marginals do not
  depend on the remote setting. The correlator is exactly `aᵀTb`, so the local terms cancel.
  **CHSH(phiW) = 2√2 exactly.**
- **C6 (control).** On 729 rational product tables, |CHSH| ≤ 2 at the same settings.
- **C7 (control).** With only diagonal (z-only) dichotomic observables at their extreme points, the
  maximum CHSH on phiW is exactly 2.
- **C8/C10.** `idW = actT reflY phiW` (dict = SWAP/2) lies in maxCone. Its dict has
  `⟨ψ⁻|·|ψ⁻⟩ = −1` (unnormalized), so idW ∉ Q3. At reflected settings it also reaches exactly 2√2.
  Mutation M1 shows that CHSH in the x–z plane does not distinguish phiW from idW. Only C1 does.

### 2.3 Written consequences [W]

**W1: Tsirelson from product-test validity alone, pair level.**
Take ω ∈ maxCone(eball 3) with ω00 = 1. The sharp effects give
`ω00 + s⟨a,ω_·0⟩ + t⟨ω_0·,b⟩ + st aᵀTb ≥ 0` for s, t = ±1 and unit a, b. Summing the (+,−) and
(−,+) cases gives aᵀTb ≤ 1. Summing (+,+) and (−,−) gives aᵀTb ≥ −1. So ‖T‖_op ≤ 1.

With sharp observables, CHSH = a₀ᵀT(b₀+b₁) + a₁ᵀT(b₀−b₁) ≤ |b₀+b₁| + |b₀−b₁| ≤ 2√2. For general
dichotomic tests `A = 2e−1`, CHSH is bilinear, so its maximum is at extreme observables: ±1, or
traceless sharp. If any observable is trivial, CHSH ≤ 2 by marginal consistency.

So **every normalized table in maxCone(eball 3) obeys CHSH ≤ 2√2 under all dichotomic product
tests.** hmax alone gives this. Neither H2, hA nor cone closure is needed.

**W2: the whole pair behaviour set (W + L).**
Through dict, maxCone(eball 3) is exactly the cone of block-positive 4×4 operators, so maxCone and
Q3 are not equal. Every positive map M₂→M₂ is decomposable (Størmer 1963; Woronowicz 1976 [L]).
Hence every block-positive W equals P + Γ(Q) with P, Q ⪰ 0 and Γ the partial transpose on one token.
Tr Γ(Q) = Tr Q, and `Tr(Γ(Q)·E⊗F) = Tr(Q·E⊗Fᵀ)`, where Fᵀ is again a POVM.

So every normalized maxCone behaviour is a convex combination of two qubit-pair quantum behaviours,
and therefore lies in the finite-dimensional quantum set C_q. The general bipartite statement is
Barnum et al., PRL 104, 140401 (2010) [L]. **Hazard:** this fails for three or more parties. Local
quantum tests on positive-on-products operators can give supra-quantum correlations (Acín et al.,
PRL 104, 140404 (2010) [L]). Whether a qubit-token instance exists is not checked here [U].
Multi-party Q-up therefore needs the k-token *upper inclusion* (K ⊆ QK k), not the k-fold maxCone.

**W3: attainment needs only H1 + H2, plus sharp tests.**
H1 puts `prodState xplus z3` in K, and H2 puts its cnot image in K. By C1 that image is phiW. By
C4, phiW reaches 2√2 with four sharp tests, two per side. No local flow and no cone closure is
needed for the *value*. Equality of the full behaviour set (Q-down) does need Q3 ⊆ K, i.e. the
lower inclusion at :107, and its realization.

**W4: no-signalling.**
Let {f_b} be any outcome family on B with Σ_b f_b = unit. By bilinearity of `prodEff` (a
LinearMap field), `Σ_b prodEff(e, f_b) ω = prodEff(e, unit) ω`. By `eff_margA` :376 that equals
`e(margA ω)`, which is independent of B's setting. This is a two-line lemma on `PreComposite` [W].
It is **not** stated at M. Only the product-state case L9 is stated.

**W5: orientation does not affect correlations.**
Γ(Q3) (the coPSD cone) gives the same behaviour set as Q3, because each local POVM can be
transposed. The K2(e) orientation question (`no_candidateCone_cnot_reflY`; #832's tilt
classification) is therefore about *operations*, not about the correlation clause.

**W6: the substratum's own class gives no Bell violation (assumption-watch).**
For `substratumClass = IsMonomial` (StructuralClosure.lean :180; SubstratumInterface.lean :75),
`realized_of_instAvail` (ImplementationLocality.lean :530) writes every branch of every available
family as `Σ conj(K_i)` with K_i monomial. So every available effect `Σ K_i†K_i` is **diagonal**
in the computational basis.

For any input ρ, even an entangled one supplied from outside,
`p(ab|xy) = Σ_{ij} ρ_{ij,ij} E^x_a(i) F^y_b(j)`. That is an explicit local hidden-variable model, so
CHSH ≤ 2. This uses the same ingredients as `substratumGen_not_control` (StructuralClosure.lean :348).

CNOT *is* monomial, so it is admissible in that class (`monomial_permMatrix` SubstratumInterface.lean
:85). Without a non-monomial local rotation it cannot create entanglement from basis states. The
operational Bell clause is therefore downstream of the same off-diagonal-control residual as K3
(`substratum_residual` :383, ¬DrivesElementary). This is a shared ingredient, **not** an
identification with the Bell ceiling of Main §3.3, which is about deterministic completions.

***

## 3. Owner refinement: preparations, settings and joint protocols — availability, not cones

### 3.1 What the cone results give (existence in cones, no availability)

- **Pair.** Under the hypotheses of :153, K = Q3. Every two-qubit density table, entangled ones
  (phiW) included, is a *member* of K.
- **Local tests.** These are affine effects of eball 3. `maxConeOf_avail_eq` (EffectSpace.lean :572)
  identifies the cone of available tests with maxCone under K∞ premises.
- **Not established.** None of this says a member of K is *preparable*, or that cnot or the local
  actions are *operations* someone can perform. H1, hH2 and hA are membership and invariance clauses.
- **Table world.** There is no protocol object on the table carrier `W 3`. It has no InstAvail, no
  instrument, no multi-outcome measurement except `SharpReadout` (CompositeInterface.lean :393,
  two-outcome), and no sequential composition.

### 3.2 What is proved available at M, and through which protocol object

| Bell ingredient | Object at M | Status and hypotheses carried |
|---|---|---|
| Incompatible local measurement settings (pair table world) | `sharpFamily_subset_avail` EffectSpace.lean :374 | [K] conditional: `PreservesBody`, `SharpSeed`, `BoundaryTransitive`, `SeedOrbitAvailable` (K∞-Trans/Seed/V4). Gives every sharp direction, hence incompatible pairs (x̂, ẑ, (x̂±ẑ)/√2). `sharpEff b + sharpEff(−b) = 1` gives binary measurements [W]. These are *test availability* on one token. Their validity on joint preparations is hmax/hvalid, unsourced. |
| Generic protocol constructors (matrix carriers) | `InstAvail` ImplementationLocality.lean :268: `op` (admissible isometry), `readout` (Lüders register readout, admissible projectors), `coarse`, `bind` (sequential and conditional composition), `discard` (uniform ancilla) | [K] definitions. Every Bell protocol is an InstAvail term [K-inst]: reset, local rotation (`op` on `1⊗K`), CNOT (`op`), readout of A (`readout` with `prodComm`), `bind` readout of B, `coarse`. It needs memberships `𝓘` of every operator used. `Architecture.proj` gives register projectors. Reindexed projectors need `LabelInvariant`. |
| Local action next to an untouched party | `instAvail_spectator` :789, `instAvail_withSpectator` :820 | [K] conditional on `ContextStable` + `LabelInvariant`. |
| Pure-state preparation | `BridgeFiniteProtocol.instAvail_reset` :111 and `reset_uniformAttach_eq_pure` :143 (Work = Token × Fin 4); `OperationalAssembly.pureSeedPrep_available_of_swap` :675; genTheory `prepAvail` = available channel ∘ uniformAttach (ImplementationLocality.lean :860) | [K] conditional on reset-permutation memberships, or on swap availability. Prepares *computational-basis* pure states only. |
| Continuous local flow (one token) | `finite_protocol_available` BridgeFiniteProtocol.lean :236, `balanced_finite_available` :256, `finite_protocol_spectator` :269 (OI-FINITE-PROTOCOL-1, receipt present) | [K] conditional on `Architecture`, the circuit, reset and correction memberships, and (spectator) `ContextStable`/`LabelInvariant`. The channel `(1−(3/8)^k) Ad_D + (3/8)^k id` with diagonal `D = diag(1,(3+4i)/5)` (:167) is **diagonal-preserving**: a z-phase, no basis change. Limit availability is not proved. The closed-cone limit ⇒ full z-flow preservation step is [W] on #820. |
| Channel protocol | OI-CHANNEL-1 (`round-oi-channel-1-audit/result.md`) | Adds **no Lean**. Depths 0–6 are [X]; the all-depth recurrence is [W]. Transfer to an arbitrary pair cone and general-k InstAvail are stated as open. |
| Entangling operation | Table: `cnot` :775 with `nativeGate_cnot` :1160 and `entangling_cnot` :1380 (properties of a candidate gate, not availability). Matrix: CNOT is a permutation matrix, so it belongs to any class with transposition swaps (`DrivesElementary`.2.1, SubstratumSource.lean :77) and to `substratumClass` | Table side: not available; the pair theorem uses only invariance hH2. Matrix side: [K-inst], available via `InstAvail.op` once a membership is given. Membership is free in the substratum class but useless there (W6). |
| Every Bell protocol at once | `genTheory_qm_of_quantumArchitecture` SubstratumSource.lean :136 ⇒ `ExactCompositeQuantumOps` (AncillaClosure.lean :364) | [K-inst] conditional on `QuantumArchitecture` (Architecture, Context, Label, Dagger, **DrivesElementary**). On `A × Fin (k+1)` every normalized Kraus instrument is available. That includes a preparation channel onto Φ+ and every product of local POVMs. Bell statistics follow by standard QM; no CHSH theorem exists. **DrivesElementary is unsourced, and false for the substratum class** (`substratum_residual` StructuralClosure.lean :383). |
| Local transposition excluded | `transposeMap_not_kraus` CompositeSoundness.lean :382; `factorExchange_exposes_ancTranspose` FactorExchange.lean :140; table side `no_candidateCone_cnot_reflY` | [K]. Local operations on entangled composites must be completely positive. |
| Local tomography | `Composite.lt` field; W 3 encodes it | Premise [K-field]; never sourced. |

### 3.3 What is only assumed or unsourced

1. **Preparation of product states (H1 as preparation).** Unsourced. On the matrix side,
   non-computational-basis product states (|+⟩) need non-monomial ops.
2. **CNOT and local actions as available operations on joint preparations,** as opposed to
   invariance hH2/hA. hA (A_miss) is unsourced, and so is K∞-Drive's `J`. The finite protocol gives
   only the z-phase flow, conditionally.
3. **Product-test validity on joint preparations (hmax/hvalid).** Unsourced (#836).
4. **Cone realization:** every member of K is preparable, needed for Q-down. Unsourced.
5. **The table↔matrix bridge.** `TransferClause` (BridgeDictionary.lean :311,
   `transferClause_iff` BridgeConverge.lean :71) is a *design statement*, not a premise anywhere. K3
   is not connected to the pair cone (ROADMAP :1017–1018).
6. **Off-diagonal local control (DrivesElementary).** Unsourced. By W6, *every* Bell violation
   depends on it, or on an equivalent non-diagonal test or preparation source.
7. **k-token carriers, multi-token local tomography, and grouping of tokens into parties.** Unsourced.
8. **The physical source of joint-test validity, four-copy coherence (FCC) and composition.**
   Placeholders only (#836, #837/#838).

***

## 4. Gaps between the adopted pair result and full finite composite QM with Bell correlations

| # | gap | needed for |
|---|---|---|
| G1 | **Availability vs membership:** product preparations, CNOT and local actions as operations; cone realization | attainment (Q-down) |
| G2 | **Incompatible local settings as available tests on joint preparations** (sharp family on each token *and* their validity on K) | any violation; W6 shows diagonal-only gives LHV |
| G3 | **k tokens / multi-party:** k-token carrier, k-fold dictionary, k-token cone theorem; maxConeK alone is insufficient for n ≥ 3 [L] | multi-party Q-up and Q-down; GHZ/Mermin/Svetlichny |
| G4 | **Parties with several tokens:** joint local measurements within a party, via available intra-party CNOT/flows or joint-test availability; qubit-power local dimension 2^m covers finite-dim C_q by isometric embedding [W] | full C_q (e.g. local dimension > 2, non-projective POVMs via Naimark) |
| G5 | **Local instruments on composites:** post-measurement update, sequential and conditional protocols, preservation of K by every built instrument (CP); the table world has no instrument notion | steering, sequential Bell tests, teleportation; "local operations" |
| G6 | **Table↔matrix bridge and the relation to K3** (TransferClause; K3's `ExactCompositeQuantumOps` is on `A × Fin n` matrix carriers by type) | one theorem covering both |
| G7 | **No-signalling and local tomography stated and proved** at the interface (W4 lemma; `lt` sourced or kept as a named premise) | the clause's corollaries |
| G8 | **Arbitrary local carriers (Kₙ)**, not needed for the correlation *set* (embedding) but needed for "full composite QM" | composite QM beyond qubit powers |
| G9 | **Orientation/antiunitary (K2(e)):** harmless for correlations (W5), but must be fixed for operations (K2Guard) | operations clause |

***

## 5. Which drafts address which gap (all unadopted at M)

| draft | what it does | gaps | evidence |
|---|---|---|---|
| #829 `origin/draft/ktoken-maxcone-1` (625f853f, D = dee3b5ae, behind M by 19) | Control-plane draft KTOKEN-MAXCONE-1: `WK k`, `prodStateK`, `maxConeK`, `dictK`, `QK k`, `cnotK i j` (i < j), `actK j` (j ≠ 0). Proposes `kCone_eq_QK_of_drive_maxCone`, the iff with one witness per direction, and the k = 2 recovery. Exact k = 3 countercontrols (ZERO3, SCALE3, ADD3, SHIFT3, SEP3, ORBIT3, CUT3, SLICE3). Non-inference rule: sources nothing. | G3 at cone level (Q-up and Q-down membership); SLICE3 is a product-test-positive non-PSD operator, the G3 hazard | [U] draft; no module |
| `origin/research/finite-reconstruction-design-20261013` (8b431a18) | argument.md: written all-k proof via a Gray-code multiplexor and recursive pure-state reachability. FinitePauli, FiniteWalsh and FiniteCircuit compile (23 theorems) in run 38457070337; KN-DESC carrier descent design | G3 [W]; G8 interface; synthesis links 1–4 still open | [D] + [W] + [X] (242 checks) |
| #820 `origin/research/bridge-compatibility-20261013` | Availability does not imply pair-cone preservation: the K_B = SEP + ℝ₊B witness, depth-one trace −1/4 [W+X]. Closed cone: finite stopped maps ⇔ Ad_D ⇔ full z-flow [W]. Spectrality (SP) screen, UNRESOLVED | G1, G5 (negative: preservation must be sourced) | [W] + [X] + [D] |
| #832 `origin/plan/compatibility-source-20261013` | Every unitarily tilted coPSD cone meeting the product domain equals Γ(Q) and is preserved; centrally symmetric bases excluded. SP ⇒ preservation is OPEN | G9, G5 (model families) | [W] + [X] |
| #831 `origin/draft/preserve-induct-1` + `origin/research/preservation-induction-design-20261013` | Conditional `instAvail_preserves`: primitive preservation, attach and discard ⇒ every InstAvail-built branch preserves an independently given carrier cone family. Compiled in run 38450187534 | G5 (conditional) | [D] |
| #836 `origin/plan/joint-tests-source-20261013` | Placeholder: physical source of joint-test validity, product tests and the composition interface | G2 validity, G7 (LT) | plan only |
| #837 / #838 four-copy placeholders | Source of FCC, the substantive residue of the four-copy IE1 route to local-action invariance; adoption of design `kt4_forward_ie1` (KT4-PREM-1 audited, receipt at M) | G1/G3 (local actions hA via IE1) | plan only; [D] design theorem |
| HB-1 (frozen, never executed) | H-Bell census | none of G1–G9 (object (ii)) | legacy record |

No draft addresses G2's validity source, G6 (the table↔matrix bridge as a theorem), the W4
no-signalling lemma, or W6's diagonal no-go as a kernel theorem.

***

## 6. The correlation clause the target theorem should carry

**Setting.**

- Elementary tokens are `eball 3` systems.
- There are n parties. Party i holds a group of m_i tokens, and k = Σ m_i.
- A **Bell protocol** is an available normalized joint preparation together with, for each party i
  and setting x_i ∈ X_i (finite), an available local measurement {E^{(i)}_{a|x_i}}_{a ∈ A_i} on that
  party's group. A local measurement is an available instrument family, coarse-grained, acting with
  the other groups as spectators.
- Its behaviour is `p(a|x) = ⟨⊗_i E^{(i)}_{a_i|x_i}, ω⟩`.
- Write B_OI(n, m, X, A) for the set of behaviours of available protocols.
- Write C_q(n, 2^m, X, A) = {Tr(ρ ⊗_i M^{(i)}_{a_i|x_i})} with ρ a density operator on
  ⊗_i (ℂ²)^{⊗m_i} and the M POVMs.

**Clause Corr.** Under hypotheses H-Corr, for all n, m, X, A, two statements are proved separately
(§A.34):

- **(Q-up)** `B_OI(n,m,X,A) ⊆ C_q(n,2^m,X,A)`.
- **(Q-down)** `C_q(n,2^m,X,A) ⊆ B_OI(n,m,X,A)`.

Equality follows. Named corollaries, each with its own proof:

- (NS) no-signalling of every available behaviour;
- (LT) available joint states are determined by product-test statistics;
- (T) for n = 2, m = (1,1), |X_i| = |A_i| = 2: CHSH ≤ 2√2 on B_OI, and 2√2 is attained;
- (CP) every available local instrument, extended by the identity on the other groups, maps
  available joint states to available joint states, and the local transpose is not available.

The union over m gives the finite-dimensional quantum set. Its closure C_qa, the commuting-operator
set C_qc and infinite dimensions are excluded (H-∞).

**H-Corr, the availability hypotheses the clause must carry** (cone clauses alone are insufficient):

1. **Carrier.** k-token carrier with multi-token local tomography (a premise, as `Composite.lt` /
   `W d` now).
2. **Preparations.** Every product of `eball 3` states is preparable, and convex mixing of available
   preparations is available (this replaces H1, hadd, hsmul as membership).
3. **Tests.** On every token the sharp family is available (`sharpFamily 3 ⊆ avail`, currently from
   K∞-Trans/Seed/V4), and product tests are valid on every available joint preparation (hmax_k /
   hvalid_k).
4. **Operations.** CNOT(i→j) for i < j, and the full third-axis flow and cyclic map on each token
   j ≠ 0, are *available operations* that post-compose onto available preparations. In particular
   they preserve the joint cone, which gives hH2_k and hA_k. Q-up needs only the preservation part;
   Q-down needs availability, through pure-state reachability.
5. **Protocol closure.** Sequential and conditional composition, coarse-graining and spectator
   locality: `InstAvail.bind`/`coarse`, plus `ContextStable` and `LabelInvariant` in the matrix
   reading.
6. **Preservation.** Every available local instrument preserves the joint cone (sourced, or
   discharged conditionally by a PRESERVE-INDUCT-type theorem from primitive preservation).
   Availability alone does not imply this (#820).
7. **Bridge.** The state/test identification between the operational joint states and the tables
   (dict) is a named bridge premise, not a definition.

**Minimal sub-clause** (pair, attainment only): H1-as-preparation, availability of one CNOT on it,
availability and validity of the four sharp tests, and hmax. These give CHSH = 2√2 (W3 + C4) and
CHSH ≤ 2√2 for every available pair behaviour (W1). For the pair, hmax alone already gives Q-up
(W2). It does not for n ≥ 3.

**Explicitly outside the clause (non-claims).**

- H-Bell: the hidden-ontology realization by preparation-indexed graphs with micro-level
  no-signalling and Ollivier–Ricci stability, and its upstream curvature re-founding.
- Bell-inclusive full-substratum uniqueness.
- Any claim that the substratum class supplies hypothesis 3 or 4. By W6 it cannot: monomial-only
  protocols give CHSH ≤ 2.

**Evidence today.**

- **Q-up (pair):** [K] cone theorem + [W] W1/W2.
- **Q-down (pair):** [K] cone lower inclusion; availability [U].
- **(T):** [X] + [W].
- **(NS):** [W] (two-line lemma missing at M).
- **k-token:** [D]/[W] (#829, design branch), not adopted.
- **CHSH/Tsirelson:** no kernel theorem anywhere.

***

## 7. Assumption-watch markers (cross-propagation)

- **AW-E1.** "Cone equality ⇒ Bell content" silently assumes availability of preparations, settings
  and entangling operations (G1/G2). Any K2-closure wording must name them.
- **AW-E2.** Bipartite: the maxCone upper bound already gives the quantum behaviour set. Multipartite:
  it does not [L]. Do not extrapolate W2 to k tokens.
- **AW-E3.** Bell violation is downstream of off-diagonal local control, the same residual as K3,
  Arc D and K∞-Drive's `J` (W6). It is not a new independent obligation, and nothing at M discharges it.
- **AW-E4.** No-signalling at the operational level (W4) is a bilinearity fact. It is a different
  object from H-Bell's micro-level no-signalling of prepared graphs. Do not identify the two
  (shared word, no formal map).
