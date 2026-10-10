# T6 — TEST: does the complete applicable premise set at L force (b)? (stage 6, Q-EX-FULL, step 4)

Thread T6, research only, read-only on the corpus. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`).
Governing texts: `PROTOCOL-STAGE6.md` (`b277b7c1…`), amendment 1 (`59019538…`, A1.6–A1.7), amendment 2
(`748f1764…`, A2.1–A2.4 — the launch conditions and the outcome statement), with AUDIT-I, AUDIT-G, AUDIT-R binding.
Evidence levels: [K] certified at L (file:line), [W] written argument (complete, given here), [X] exact computation in
`pt/T6/` (script, check id), [A] audited record cited and not recomputed, [D] design module (not at L), [L] unverified
literature. Abbreviations: CD = CompositeDimension.lean, KIF = KInfFoundations.lean, CI = CompositeInterface.lean.

## §0 Verdict (two-way form of `PROTOCOL-STAGE6.md` step 4, stated by A2.4)

**INDEPENDENCE.** The complete applicable premise set at L does not force (b) in its weakest sufficient form.
- **Derivation side: failed, with the wall located.** No chain from inventory items at their actual status reaches
  (b). At L no H→P, M→P or G→P bridge exists at the level of declarations (t1); the only kernel theorems that
  quantify over a pair cone are the reflY no-go and its restatement, and no theorem at L concludes that a pair cone
  is invariant under `actC g` or `actT g` for any `g` (t2); every object-specific discharge is a closed statement
  about one object off the pair carrier (t2). Every remaining route is CONDITIONAL-shaped on an item that is
  do-not-assume, design-run [D], PT-record or level-M without a bridge (§2.5).
- **Countermodel: K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F**, rebuilt with my own exact code from the kernel's definitions
  (t3, 17/17): it satisfies every non-hypothesis item that reaches the pair cone at L — row by row against R6's
  audited Table A2, re-checked by my own exact scripts (t4: 115 SATISFIES, 3 SATISFIES vacuously, 68 NOT REACHED,
  13 FAILS, every FAILS row a hypothesis) — and it violates (b) in every weakest sufficient form, on either token
  and in the mixed placement: every member `R_a(t)` with `sin t ≠ 0` of every coordinate flow (indeed of every
  rotation axis, t5), and `cyc3^{±1}`, moves K(Z_F) out, with the exact witness
  `ipW(R_a(t)_τ z_s, R_a(π/2)_τ p_s) = −sin(t)/8` against a pure state `R_a(π/2)_τ p_s ∈ Q3 ∩ Z_F* ⊆ K(Z_F)`.
- **The missing assumption (§5):** (b) itself for two non-commuting native flows on one token — `K` invariant
  under `actτ R_x(t)` and `actτ R_z(t)` for all `t` (ball3Drive's flow and its `J`-conjugate; equivalently the drive
  through the NOT with the phase flow). It fails the disguise test: it restates I3.153 (b_DJ) and the clause of
  I3.165 (K2, "local actions compatible with the composite cone"), both do-not-assume, and is the drive instance of
  OI⁺-1 (I4.3 / I4.82 / I4.96, level M, do-not-assume). The candidates that pass the disguise test and would close
  the gap are not items at L: λ (KT4Core with `tok`, [D], no structure with three or more tokens at L) and pair
  homogeneity H (PT-record candidate, [W + L]).
- **Scope.** "Independent of the premises at L that reach the pair cone, as stated" — not of every extension of the
  framework. The 68 H-, M-, G-level items are NOT REACHED (no bridge at L), never satisfied or failed; no
  embedded-observer realization of K(Z_F) is claimed, and none is obstructed at L (R6 §6, statement (ii)).

## §1 The target, fixed before the first node (NOTES N1, N2)

Kernel conventions (read at L): `W 3 = Fin 4 → Fin 4 → ℝ` (CD:97), index 0 the unit, 1–3 the ball's coordinates
(Pauli X, Y, Z under the dictionary); `actT N ω = ω·Hom(N)ᵀ`, `actC N ω = Hom(N)·ω` (CD:198, :201; `Hom(N) = 1 ⊕ N`);
`cnot` the signed permutation of CD:741–786 (= Ad(CNOT), control first, [X t3 D0a]); `nflip = diag(1,−1,−1) = R_x(π)`
(CD:797), axis `z3 = e_z` (CD:793). The certified drive `ball3Drive` (KIF:449): flow `rot3 t = R_z(t)` (KIF:411), NOT
`rot3 π = diag(−1,−1,1)`, `J = cyc3 : (x,y,z) ↦ (z,x,y)` (KIF:425), a rotation by 2π/3 about (1,1,1)
([X t3 D0b: R(U_J) = cyc3]). Hence `J R_z(t) J⁻¹ = R_x(t)` — the PT stages' "drive through the NOT" — and
`J R_x(t) J⁻¹ = R_y(t)`.

The weakest sufficient forms (INTEGRATION-NOTE-STAGE5 §2; A1.6):
- (b) for the drive with its J-conjugate on one token: `{R_x, R_y}` (PT convention) or `{R_z, R_x}` (ball3Drive);
- (b) for the drive with the substratum phase flow about z on one token: `{R_x, R_z}`;
- A1.6's "(b) for {flow, J} on one token": the flow (`R_x` or `R_z`) and `J = cyc3`; and the mixed placement (flow on
  the control, J on the target).
Every one of them contains `R_x` or `R_z` on some token. A cone that, on each token, is left by some member of `R_x`
and by some member of `R_z` violates all of them; I also test `R_y` and `cyc3^{±1}` directly.
Decision vocabulary (base amendment 2): DERIVED / CONDITIONAL / INDEPENDENT / UNRESOLVED; productivity test and gem
classes fixed in NOTES N1.3 before the first node.

## §2 The derivation attempts (depth-first, first)

Each step: label, premise id(s) with status at L (from `pt/R6/r1_inventory.out` and the inventories), level.

### §2.1 D1 — the H-, M-, G-level items: is there a bridge to `W 3` at L? [X t1 + W]
- [X t1, run 2] Import graph of the 214 kernel modules and the root: the modules defining the pair vocabulary
  (`W` CD:97, `maxCone` CD:186, `actT`/`actC`, `cnot`, `NativeGate`, `IsNot`; `CandidateCone` K2Guard:95) are
  CompositeDimension and K2Guard; the modules defining the H/M/G vocabulary (FiniteOperationalTheory
  OperationalAssembly:594, HasParallelReferenceExtension ReferenceExtension:447, ImplementationLocality and
  ContextStable ImplementationLocality:370, :359, StructurallyClosed StructuralClosure:183, substratumClass :180,
  LayerFlowExecutable LiftAudit:112, DerivedOI RouteB:141, EmbeddedObservation :123, ObservationalIndependence
  CompletedOI:129 / CarrierGeneralOIPlus:73, OICore, RealizesSealedOICore, QuantumArchitecture, DrivesElementary,
  HasCompositeUnitaryControl, PhysicalCompletionConditions, WellFormed, ShadowQuantum, PairFlowSourced,
  InertSpectatorCompositionality) are 16 other modules. The only module whose import closure reaches both is the
  root `OIBridge`, and none of the root's 65 declarations carries a token of either vocabulary. Countercontrols: one
  synthetic import edge makes 12 modules reach both; a synthetic two-vocabulary declaration is flagged.
- [W] A Lean declaration can name only what its module's import closure defines. Hence no declaration at L states a
  relation between an H/M/G object and `W 3`: **no H→P, M→P or G→P bridge theorem exists at L**, verified for each
  route — α (I4.3 HasParallelReferenceExtension, assumed), β (I4.31 ImplementationLocality, I4.29 ContextStable,
  assumed in general), γ (I4.45 StructurallyClosed, assumed for an extension), δ (I4.56 LayerFlowExecutable,
  do-not-assume), ζ (I4.110 EmbeddedObservation, I4.87 ObserverRecursion), I4.241 DerivedOI, I4.80/I4.88/I4.102
  CompletedOI/OIPlus, the sealed core and its realizations (I1.41–I1.60, H→M only).
- [K + W] The M-level spectator clauses are statements on `Matrix (A × Fin n) ℂ` with the spectator adjoined as
  `R × (A × Fin n)` (ReferenceExtension.lean:447–451) or as `tensorOf (1 : Matrix R R ℂ) K` (ImplementationLocality
  .lean:359–361): the composite is the Kronecker product with the PSD cone by construction, and no M-level item has
  a parameter that a non-quantum pair cone could instantiate. A transcription to `W 3` would identify the pair cone
  with that composite — i.e. assume `Q3` (I3.144, do-not-assume) — or would be (b) for the class (do-not-assume).
- [X t1 B5] Manuscripts and roadmap: one line carries both vocabularies, ROADMAP.md:68 (row P1), which records the
  lift from the elementary `d = 3` system to the matrix carriers as OPEN (K2 OPEN, Kₙ "no theorem lifts …") — an
  obligation, not a bridge.
- **Node verdict D1:** no route through an H-, M- or G-level item reaches the pair cone at L. Each enters only
  through an obligation (K2, ROADMAP.md:1001–1006; P1, ROADMAP.md:68), not a premise. CONFIRMING (AUDIT-I §2, G6
  NO-MEET), at declaration level.

### §2.2 D2 — the P/O-level kernel content and the KC edges [X t2 + W]
- [X t2 (a)] Declarations at L that bind a set of pair vectors: definitions `maxCone` (CD:186), `jointStates`
  (CD:190), `maxConeOf` (EffectSpace:411), `jointStatesOf` (K1Bridge:59), `CandidateCone` (K2Guard:95),
  `productSet` (:179), `cnotOrbit` (:182); theorems: only `no_candidateCone_cnot_reflY` (K2Guard:143) and its
  restatement in `k2guard_orientation` (:277).
- [X t2 (b)] The 39 theorems at L that mention `actC`/`actT`: 33 equalities (carrier identities `toOp_actC`,
  `actT_actT`, …; gate relations with involutions `cnot_relT`, `cnot_relC`, `gate_actC`, …; product identities
  `actT_tens`, `actC_tens`, `actT_prodState`), one conclusion `False` (the no-go), four memberships — of which
  `reflY_mem_productSet` concerns the fixed product set, `k2guard_orientation` carries the invariance only as an
  antecedent of `→ False`, and `c5_sep`, `relT_not_dimension_selecting` are `d = 5` controls about products — and
  one `¬ Even d`. **No theorem at L concludes the invariance of any pair cone under `actC g` or `actT g`.**
- [K] The no-go (I3.44, proved [K]): `CandidateCone K → cnot-invariance → actT reflY-invariance → False` — it
  forbids an operation; it forces none. I3's bridges B1–B7 (I3 RESULT §0) transfer effect availability (B1, B2: the
  product-test cone equals `maxCone (eball 3)`), products (B3), identities on products (B4), the Lorentz effect cone
  (B5), the π-rotation NOT (B6), `eball_three` (B7): an upper bound `K ⊆ maxCone` and single-token facts, never an
  operation on a non-product vector.
- [X t2 (c)] Anc(P) over G6's edges R, RA, RN and KC: 25 nodes (21 records at levels P/O, 4 kernel declarations);
  the one KC edge inside it is I3.12 → I3.1 (the gate theorems depend on the carrier). The kernel-completed
  dependencies add no H/M/G premise to any pair object (countercontrol: a synthetic edge I3.1 → I1.1 does).
- **Node verdict D2:** the P-level content constrains `K` by H1/CandidateCone (I3.43, I3.147), the upper bound
  `K ⊆ maxCone`, `cnot`- (and G16-) invariance as hypotheses (I3.132, I3.148), self-duality H3 (I3.149, PT-record;
  `dualW` [D]), closedness (I3.131), the slice conditions (I3.114, I3.116, I3.118, I3.159), and the reflY no-go.
  None mentions a flow member or `J` acting on a non-product pair vector. ELABORATING.

### §2.3 D3 — the discharges for particular objects [X t2 (d) + W]
| discharge | statement (L) | object, carrier | reaches CD |
|---|---|---|---|
| `substratumClass_contextStable` | StructuralClosure.lean:261 | the monomial class `substratumClass` | no |
| `mixC_contextStable` | StateMixingCoupling.lean:442 | `MixC` | no |
| `substratumClass_structurallyClosed` | StructuralClosure.lean:316 | `substratumClass` | no |
| `hcompRealized_consistent_with_parallelReferenceExtension` | SpectatorBridge.lean:472 | ∃ T : FiniteOperationalTheory (Fin 2) | no |
| `layerFlowExecutable_of_control` | LiftAudit.lean:117 | T with `HasCompositeUnitaryControl` | no |
| `implementationLocality_of_qm`, `reversibleImplementationLocality_of_qm` | ImplementationLocality.lean:1017, MicroscopicReversibility.lean:329 | T with `ExactAllFiniteEndomorphicQuantumOps` | no |
| `embeddedObservation_of_qm`, `genTheory_embeddedObservation` | EmbeddedObservation.lean:327, ImplementationLocality.lean:904 | exact QM; `genTheory 𝓘 arch A` | no |
| `substratumTheory_derivedOI` | RouteB.lean:290 | `substratumTheory A` | no |
- [W] Each is a closed statement about one object whose composite is the Kronecker product (or the monomial class on
  configurations). A statement about one fixed object cannot constrain an arbitrary `K ⊆ W 3`; transcribed by the [D]
  dictionary it would at most say that `Q3` (resp. the monomial transcription) satisfies (b) — a retention fact. For
  the substratum class even the transcription is insufficient: the monomial class contains neither the flow nor `J`
  (`U_J` is not monomial), and its pair transcription admits the EXOTIC-E alternative A4c (`c = 513/512`, R6 Table
  A3-seeds; stage 5 γ).
- **Node verdict D3:** no discharge reaches the composite cone in `W 3`; all of them stay on the matrix carrier or
  the substratum class. CONFIRMING (G6 §3), with the carriers read from the statements.

### §2.4 D4 — the direct chain from the items that reach the cone, step by step
The best chain the reached items allow, with the labels the protocol requires:
| step | content | label | premise (id, status at L, level) |
|---|---|---|---|
| 1 | every product state of the ball lies in `K` | hypothesis, satisfiable | I3.43 `CandidateCone` (assumed; hypothesis of I3.44), I3.147 H1 (PT-record), P |
| 2 | `K ⊆ maxCone (eball 3)` | hypothesis | I3.43 (assumed), P; B1 `maxConeOf_avail_eq` EffectSpace:572 [K] identifies the bound |
| 3 | `cnot K ⊆ K` (level (ii): G16) | hypothesis | I3.132 `hgate` (assumed), I3.148 H2 (PT-record), P |
| 4 | `K = dualW K` | hypothesis | I3.149 H3 (PT-record; `dualW` [D] I3.143), P |
| 5 | the token admits the flow and `J` | [K] as a body symmetry; operational availability OPEN | I3.67 `ball3Drive` KIF:449 [K]; I3.168 K∞-Act, I3.169 K∞-Drive (open), O |
| 6 | `actτ R(t) K ⊆ K` for the flow and `J` | **no premise at L** | the clause exists only as I3.150–I3.153 (b) forms (PT-record, do-not-assume), I3.137 IE1 / I3.142 IE1Drive ([D], do-not-assume), I3.165 K2's clause (open, do-not-assume), I3.146 P-ACT2's idle-extension reading (= IE1) |
Steps 1–5 do not imply step 6: K(Z_F) satisfies 1–5 and violates 6 (§3). Supplying step 6 by any listed item is circular
(the item is (b) or contains it). **The derivation fails at step 6**; with steps 1–5 alone the target is not reached
by any [W] argument, since a [W] argument would contradict the countermodel.

### §2.5 The CONDITIONAL-shaped routes (recorded; none is a derivation at L)
| route | chain | status of the item used | why not admissible at L |
|---|---|---|---|
| α OI⁺-1 / observational independence | I4.3 / I4.82 ⇒ spectator stability of the drive ⇒ (b) | assumed (level M), do-not-assume | needs an M→P bridge (none, D1); transcription = (b) for every available operation (circular) |
| β implementation locality | I4.31 with I4.29 ContextStable for a class containing the drive | ContextStable: theorem for the monomial class only (StructuralClosure:261); assumed otherwise; level M | as α; for the monomial class the transcription is insufficient (A4c) |
| γ structural closure of an extension | I4.45 for an extension containing the drive | assumed (level M) | as α |
| δ layer-flow executability, ∀ level | I4.56 | do-not-assume (level M) | as α; its ∀-level clause is the spectator clause (stage 5 D5 N1c) |
| ζ embedded observation / observer recursion | I4.110, I4.87 | assumed / do-not-assume (level M) | as α; the pair-level drivability reading is satisfied by K(Z_F) (stage 5 ζ, [A]) |
| λ four-token coherence with `tok` | I3.133 `H` (KT4Core) ⇒ I3.137 IE1 by `kt4_forward_ie1` ⇒ (b) | not at L — [D]; `tok` I3.134 NOT REACHED (no ≥3-token structure at L) | the central step is a design-run theorem [D], neither [K] nor [W]; the premise is not an item at L |
| pair homogeneity | I3.160 H ⇒ `K = Q3` ⇒ (b) | PT-record candidate | the step H ⇒ `Q3` is [W + L] (Koecher–Vinberg, Jordan–von Neumann–Wigner unverified here); H not at L |
| K2's local-action clause; P-ACT2 | I3.165; I3.146 | open; assumed (named premise of KT4-PREM-1) | the clause is (b) (do-not-assume); P-ACT2's idle-extension reading is IE1 |
| the gluing clause | Main.md:552 (I2.12, level H) | proved [M], no kernel anchor | level H; takes `I_a ⊗ I_b` as input — the composite action itself (R6 §6 marker) |

### §2.6 Verdict of the derivation side
No DERIVATION: no chain from items at their actual status reaches (b); every CONDITIONAL-shaped route either uses a
do-not-assume item (circular), or an item not at L ([D], PT-record), or a level-M item with no bridge. The wall is
exact: at L nothing quantifies over a pair cone and concludes anything about a single-token action on it except the
reflY no-go (t2). Alone this would be UNRESOLVED; the countermodel of §3 makes the outcome INDEPENDENCE.

## §3 The countermodel K(Z_F) [W + X t3, t5]

### §3.1 Definition (stage 3 X `K4` / U `K_F`; R6 Table A2; rebuilt here)
`z_s = (E00 + s1 E13 + s2 E22 − s1 s2 E31)/4` for `s = (s1, s2) ∈ {±1}²`, `Z_F = {z_s}`;
`K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F`, with `Q3 = {ω : M(ω) ⪰ 0}`, `M(ω) = Σ ω_μν σ_μ⊗σ_ν`, duals for `ipW` (Euclidean on
the 16 entries; `tr(M(a)M(b)) = 4 ipW(a, b)` [X t3 D0d]). `Q3` enters only the construction and verification of the
model, never a premise.

### §3.2 The structure of the defects [X t3 Z1, Z2, Z6]
`M(z_s) = I/2 − P_s` with `P_s = (I − s1 X⊗Z − s2 Y⊗Y + s1 s2 Z⊗X)/4`, the four joint eigenprojectors of the commuting
pair (X⊗Z, Y⊗Y): orthogonal rank-one projectors onto maximally entangled states with `Σ_s P_s = I`. Hence
`ipW(z_s, z_t) = [s = t]/4`, `tr M(z_s) = 1`, and `M(z_s) P_s = −P_s/2`: `z_s ∉ Q3`, so `K(Z_F) ≠ Q3`.
`p_s := table(P_s) = (E00 − s1 E13 − s2 E22 + s1 s2 E31)/4 ∈ Q3`, `ipW(z_s, p_s) = −1/8`.

### §3.3 H3, self-duality: a complete proof [W], ingredients [X]
Write `A = Q3 ∩ Z_F*`, `C = cone Z_F`, `K = A + C`; trace-pairing units, `⟨M(z_s), M(z_t)⟩ = [s = t]`.
1. `K ⊆ K*`: `⟨A, A⟩ ≥ 0` (PSD matrices pair nonnegatively), `⟨A, Z_F⟩ ≥ 0` (definition of `Z_F*`),
   `⟨z_s, z_t⟩ ≥ 0` (§3.2); bilinearity.
2. `K* = A* ∩ Z_F*` and `A* = cl(Q3* + C) = cl(Q3 + C)` (duality of closed convex cones in finite dimension;
   `Q3* = Q3`; `C` finitely generated, hence closed). `Q3 + C` is closed: along a convergent sequence `q_k + c_k`
   the traces of `q_k ⪰ 0` and of `c_k = Σ λ_{k,s} z_s` (`tr M(z_s) = 1`) are bounded, so both are bounded and a
   subsequence converges in the closed cones. So `K* = (Q3 + C) ∩ Z_F*`.
3. Let `w = q + Σ λ_s z_s ∈ K*`, `q ⪰ 0`, `λ ≥ 0`. For each t, `⟨w, z_t⟩ = ⟨q, z_t⟩ + λ_t ≥ 0`, and
   `⟨q, z_t⟩ = tr(q)/2 − ⟨ψ_t|q|ψ_t⟩`. Since `Σ_t ⟨ψ_t|q|ψ_t⟩ = tr q` with nonnegative terms, at most one t has
   `⟨q, z_t⟩ < 0`. If none, `q ∈ A` and `w ∈ K`.
4. If `t` is the one, put `μ = −⟨q, z_t⟩ > 0` (so `λ_t ≥ μ`) and `q' = q + μ M(z_t)`. **Correction lemma:**
   `q' ⪰ 0`. Proof: in the splitting `span ψ_t ⊕ ψ_t^⊥` write `q = [[a, b†], [b, Q]]`, `a = ⟨ψ_t|q|ψ_t⟩`; then
   `μ = (a − tr Q)/2 > 0`, so `a > tr Q ≥ 0`, and `q' = [[a − μ/2, b†], [b, Q + (μ/2) I₃]]` with
   `a − μ/2 = (3a + tr Q)/4 > 0`. From `q ⪰ 0`: `Q ⪰ b b†/a` and `|b_i|² ≤ a Q_ii`, so `‖b‖² ≤ a tr Q`. The Schur
   complement of `q'` is `Q + (μ/2)I − b b†/(a − μ/2) ⪰ (μ/2) I − b b† (μ/2)/(a(a − μ/2)) ⪰
   (μ/2)(1 − tr Q/(a − μ/2)) I ⪰ 0`, because `a − μ/2 ≥ tr Q ⟺ a ≥ tr Q`. ∎
   Then `⟨q', z_t⟩ = −μ + μ = 0`, `⟨q', z_u⟩ = ⟨q, z_u⟩ ≥ 0` for `u ≠ t`, so `q' ∈ A`, and
   `w = q' + (λ_t − μ) z_t + Σ_{u≠t} λ_u z_u ∈ K`.
So `K(Z_F) = K(Z_F)*`; it is closed and a convex cone. [X t3 Z4] controls the lemma on 600 exact rational PSD
instances (278 with a negative pairing, each corrected into `Q3 ∩ Z_F*`); countercontrol CC-Z4: for the
non-orthogonal family `{z_s, actC Rx(cos 3/5) z_s}` a pure state has two negative pairings, so step 3 genuinely
uses orthogonality. This proof does not cite the stage-3 surgery theorems SD1/SD2 [A]; it agrees with them.

### §3.4 H1, H2 at level (ii), and the slice conditions [X t3 Z3, Z5, Z7, Z8; W]
- **H1** [X Z3]: `4 ipW(prodState x y, z_s) = 1 + x·M_s y` with `M_s` a signed permutation, and
  `2(1 + x·M_s y) = |x + M_s y|² + (1 − |x|²) + (1 − |y|²)` identically; `M(prodState x y) = (I + x·σ)⊗(I + y·σ)`
  is PSD on the ball. Products lie in `Q3 ∩ Z_F* ⊆ K`.
- **H2, level (ii)** [X Z5]: `Gbig = ⟨cnot, actC D ∘ actT D′ (D, D′ signed diagonal, det D det D′ = 1)⟩` has order
  64, every element permutes `Z_F` and fixes the (0,0) entry, and every generator is `M ↦ V M V†` or `M ↦ V Mᵀ V†`
  (16 + 16; `cnot = Ad(CNOT)`), so `Gbig ⊆ Aut(Q3)` and `g(Q3 ∩ Z_F*) = Q3 ∩ Z_F*` (`g` is `ipW`-orthogonal).
  G16 — generated by `cnot` and orientation-even signed-diagonal locals (PROTOCOL-STAGE3.md:51–52) — is a subgroup.
- **`K ⊆ maxCone (eball 3)`** [W]: an effect `e` on the ball has `ehom e = (e0, e⃗)` with `e0 ≥ |e⃗|`, a nonnegative
  combination of `hom 0` and `hom ê`; so `ehom e ⊗ ehom f ∈ cone SEP` and `prodEffVal e f ω = ipW(ω, ehom e ⊗ ehom f)
  ≥ 0` for `ω ∈ K = K* ⊆ SEP*`. With H1: `CandidateCone K(Z_F)`, `hadm`.
- **Slice** [W]: `Ω = {ω ∈ K : ω₀₀ = 1}` is convex, contains the products, every product of effects takes values
  in [0, 1] on it (`e⊗f = 1⊗1 − (1−e)⊗f − 1⊗(1−f)`), the unit pairing is `ω₀₀ = 1`; it is closed and bounded
  (inside `maxBody`), hence compact; `cnot` preserves `K` and fixes `ω₀₀`, so `JointReversible {cnot}`, INV2 and
  S2 Pair hold; LT holds on the carrier [X Z8: the product effects span `W 3`]. `PreComposite`, `Composite`
  (CI:223, :243, :445).
- **I3.44 consistency** [X Z7]: `actT reflY z_(−1,−1)` pairs `−1/8` with `z_(1,−1) ∈ K`, as the kernel theorem
  `no_candidateCone_cnot_reflY` (K2Guard:143) requires of a `cnot`-invariant candidate cone.

### §3.5 The violation of (b) in its weakest sufficient forms [X t3 B, t5]
- **Witnesses** [X t3 B], on each token τ ∈ {C, T}: `R_x(π/2)`, `R_y(π/2)`, `R_z(π/2)`: `−1/8`; `R_x(t)`, `R_z(t)` at
  `(cos t, sin t) = (3/5, 4/5)`: `−1/10`; `cyc3`, `cyc3⁻¹`: `−1/8` — each the pairing of `g z_s` with a certified
  `y ∈ K` (a rotated Bell-type pure state, trace-one projector with all `ipW(y, z_u) ≥ 0`; 64 certified). Since
  `K ⊆ K*`, `ipW(g z_s, y) < 0` with `z_s, y ∈ K` proves `g z_s ∉ K`.
- **Flow law** [X t3 B flow law; t5 for every axis]: for every unit axis `n`, every token and every `s`,
  `ipW(R_n(t)_τ z_s, R_n(π/2)_τ p_s) = −sin(t)/8` identically (modulo `|n| = 1`), and `R_n(π/2)_τ p_s` is a pure
  state with pairings `0` and `(1 − n_i²)/8` against the defects, so it lies in `K`. Hence **every member with
  `sin t ≠ 0` of every one-parameter rotation subgroup of either token moves K(Z_F) out** (for `sin t < 0` use `−n`).
- **Consequence.** (b) fails for the drive through the NOT (`R_x`), for ball3Drive's flow (`R_z`), for their
  J-conjugates (`R_y`, `R_x`) and for `J = cyc3`, on the control, on the target and in the mixed placement: every
  weakest sufficient form of §1 is violated, and so is every stronger one (I3.150 (b_S4), I3.151 (b_n) for every
  axis, IE1 I3.137, IE1Drive I3.142, K2's clause I3.165).
- **Countercontrols** [X t3]: `nflip` and `rot3 π` (symmetries of K(Z_F), in Gbig) permute `Z_F` and give no
  negative pairing over the 104-element pool; every rotated pure state is a trace-one projector (the modeled
  operations preserve `Q3`, §A.21); at the half-turn the flow law gives `0` (t5 A3).

## §4 Row by row against R6's audited Table A2 (K(Z_F)) [X t4 + W]

Every one of the 199 rows is printed with R6's verdict, my verdict, its status at L and my re-check in
`t4_rows.out` (`ROW` lines); `t4_rows.py` prints VERDICT ROWS-OK. Grouped here by R6's class, every id cited:

| R6 class → T6 verdict | rows | my re-check |
|---|---|---|
| cone → SATISFIES (12) | I3.43, I3.114, I3.116, I3.118, I3.130, I3.131, I3.132, I3.147, I3.148, I3.149, I3.156, I3.159 | t3 Z1–Z5, Z8 (PASS) with §3.3–§3.4 |
| kthm → SATISFIES (1) | I3.44 | t3 Z7 (the theorem's consequence holds: `actT reflY` moves K) |
| def → SATISFIES (12) | I3.1, I3.2, I3.3, I3.4, I3.5, I3.6, I3.7, I3.11, I3.49, I3.113, I3.115, I3.143 | binder scan: no `Set (W …)` variable; the definitions are the ones t3 transcribes (D0) |
| thm → SATISFIES (23) | I3.12–I3.17, I3.20, I3.22, I3.25–I3.28, I3.30, I3.32–I3.34, I3.41, I3.42, I3.46, I3.120–I3.122, I3.185 | binder scan (proved theorems that quantify over no pair cone) |
| gate → SATISFIES (7) | I3.9, I3.10, I3.23, I3.29, I3.35, I3.36, I3.129 | binder scan; the gate is the kernel's `cnot` (t3 D0a) |
| inh → SATISFIES (46) | I3.8, I3.18, I3.19, I3.21, I3.24, I3.31, I3.37–I3.40, I3.45, I3.47, I3.50, I3.52, I3.53, I3.57, I3.69, I3.76, I3.78–I3.80, I3.82, I3.83, I3.87–I3.89, I3.92, I3.94, I3.95, I3.97, I3.98, I3.101, I3.111, I3.124–I3.128, I3.164, I3.166–I3.169, I3.173, I3.186, I4.236 | binder scan: single-token statements; the tokens are `eball 3 = ball3` with `nflip`, `z3`, `cnot`, as for `Q3` |
| b1 → SATISFIES (13) | I3.48, I3.51, I3.54–I3.56, I3.58, I3.60, I3.73–I3.75, I3.170–I3.172 | binder scan; their pair consequence is the bound `K ⊆ maxCone`, met (§3.4) |
| d4s → SATISFIES (1) | I3.138 | [D] parity of the gate's twist bits (`cnot` with identity locals), K-blind |
| d4v → SATISFIES vacuously (3) | I3.139, I3.140, I3.187 | the hypothesis fails: IE1 fails (t3 B), so by the [D] theorem's contrapositive `H` fails; I3.187 uses IE1 |
| hmg → NOT REACHED (56) | I1.17; I4.3, I4.4, I4.14, I4.29, I4.31, I4.42, I4.45, I4.56, I4.65–I4.70, I4.73, I4.74, I4.80, I4.82, I4.85, I4.87, I4.88, I4.96, I4.99, I4.102, I4.110, I4.115, I4.118, I4.120, I4.123, I4.124, I4.127, I4.128, I4.133, I4.137, I4.143, I4.144, I4.179, I4.187, I4.210, I4.215, I4.216, I4.241, I4.244, I4.245; I2.3, I2.29–I2.35, I2.62, I2.63, I2.69 | each I4 declaration lives in a module whose import closure excludes CompositeDimension (t4); manuscript items: no bridge at L (t1) |
| nr → NOT REACHED (12) | I3.96, I3.99, I3.104, I3.105, I3.134, I3.136, I3.141, I3.145, I3.146, I3.154, I3.157, I3.158 | three-or-more-token content or the absent P-STAGE2/P-ACT2; no pair-cone theorem at L carries them (t2 (a)) |
| dna → FAILS, hypothesis (9) | I3.137, I3.142, I3.144, I3.150, I3.151, I3.152, I3.153, I3.155, I3.165 | do-not-assume (or K2's do-not-assume clause); my witnesses: t3 B / flow law / t5 (I3.137, I3.142, I3.150, I3.151 every axis, I3.153, I3.165), t3 Z6 (I3.144); I3.152 (R1) and I3.155 (FC ⟺ IE1 given hgate) cited [A] |
| d4f → FAILS, hypothesis (2) | I3.133, I3.135 | not at L — [D]; R6 r2 C9 [A] (FCC −1/2); my verdict does not use these failures |
| cand → FAILS, hypothesis (2) | I3.160, I3.161 | PT-record candidates; stage 4 Y6 [A]; my verdict does not use these failures |

Totals: SATISFIES 115 + 3 vacuous = 118, NOT REACHED 68, FAILS 13 — R6's tally, reproduced by my own code. **Every
non-hypothesis row is SATISFIES or NOT REACHED; every FAILS row is a hypothesis** (status "not at L — [D]",
"PT-record", "open", or the do-not-assume flag; none "proved [K]", none a definition at L).

Rows with no kernel declaration found by the scan (16), read: I3.1 (`W d`, CD:97: the carrier the model lives in);
I3.125 (`NativeGateBall.parity`: NativeGateBall is imported by CompositeDimension, so by scoping it cannot name a pair
cone); I3.129 `NClass`, I3.138 `EvenCycle`, I3.143 `ipW`/`dualW` ([D] definitions about the gate or the pairing —
the pairing is the one t3 uses, D0d); I3.164 K1, I3.166–I3.173 K∞ and its seams (ROADMAP rows about one token,
pair-blind, open for `Q3` alike); I3.185 (the names `actT_prodState`, `actT_tens`, `actC_tens`, `toOp_actC` were cut in
R6's one-line column; t2 (b) lists them as equalities on products); I4.236 (the scope of K∞'s geometric branch, a
single-token statement whose pair reading fails for `Q3` alike [A]).

Under the base protocol's stricter wording ("the assumed items as hypotheses it must satisfy unless … do-not-assume"):
the non-do-not-assume hypotheses K(Z_F) fails are I3.133, I3.135 (status "not at L — [D]") and I3.160, I3.161 (status
"PT-record") — none is an assumed item at L (A2.3: every FAILS row is "never a theorem or definition at L"), so the
stricter wording binds none of them. If one adjoined them as premises anyway, the verdict relative to the enlarged set
would read CONDITIONAL(λ; [D] hypothesis, unsourced at L, via a [D] step) and CONDITIONAL(H; PT-record, via [W + L])
— neither is a derivation at L (§2.5).

## §5 The missing assumption, isolated

**Exact content that closes the gap.** For one token τ ∈ {C, T}:
  (A_miss) `∀ t, ∀ ω ∈ K: actτ R_x(t) ω ∈ K and actτ R_z(t) ω ∈ K`,
i.e. (b) for ball3Drive's flow `R_z` (KIF:411, :449) and its `J`-conjugate `R_x = cyc3 ∘ R_z ∘ cyc3⁻¹` — equivalently
for the drive through the NOT with the substratum phase flow about z. With H1–H3 it closes the gap: `R_x` and `R_z`
generate SO(3), so A_miss gives (b_S4) on that token, and (b_S4) with H1–H3 forces `K = Q3` (stage 4 Y2 [W + X],
audited [A]); then every form of (b) holds [W: `Q3` is invariant under local unitaries]. It is minimal within the
native repertoire (stage 5 C5 census [A]: each single flow, `{J}`, `{NOT, J}` leave exotic alternatives); its pair
`{R_x, R_y}` (the PT drive with its J-conjugate) closes the gap equally.
K(Z_F) shows how much is missing: it admits **no** one-parameter rotation subgroup of either token (t5), so even one
continuous local symmetry of the pair cone is not supplied by L.

**Disguise test of A_miss: fails.** It is stated through the composite action of single-token operations. It
restates the do-not-assume items I3.153 (b_DJ) (PT-record, open) and I3.150 (b_S4) for two generators, the clause
"local actions compatible with the composite cone" of I3.165 (K2, ROADMAP.md:1001–1005, OPEN), and it is the instance
for the drive and one off-frame partner of observational independence (I4.82 / I4.96 = I4.3
`HasParallelReferenceExtension`, level M, do-not-assume), read in `W 3` through a transcription L does not have.
**Candidates that pass the disguise test and would close the gap** — none is an item at L: λ (I3.133 KT4Core with
the token clauses I3.134; passes, EQ3-AUDIT §2 item 4 [A]; [D], no structure with three or more tokens at L); pair
homogeneity H (I3.160; passes — a property of `K` alone; PT-record, `H ⇒ Q3` [W + L], minimality UNRESOLVED);
extreme-ray transitivity T (I3.161; passes; excludes the known cones only, EXCLUDES-ALL UNRESOLVED). An H→P bridge
that realizes the pair as a composite of two embedded observers with local instruments `I_a ⊗ I_b` (Main.md:552)
would supply A_miss, but its composition clause is the idle extension itself (R6 §6 marker): it fails the disguise
test at level H.

## §6 Level distinction and the realization question
- Hidden-history level (H: Axioms 1–2, C1–C4, the sealed core, the realization theorems) and composite-cone level
  (P: `W 3`, `K`) are kept apart. No H-level item reaches K(Z_F): there is no H→P bridge at L (t1, declaration
  level); each is NOT REACHED in Table A2, never "satisfied" or "failed".
- The INDEPENDENCE is a cone-level statement. L attaches no embedded-observer realization to any cone in `W 3`, and
  proves no obstruction (R6 r5 [A]; t1 finds no declaration mentioning both vocabularies). Whether H-level premises,
  through a future proved bridge, would exclude K(Z_F) is open; any such bridge is an obligation (K2; P1), not a
  premise at L.

## §7 Pressure tests (both directions)
- **Against a derivation (favourable branch):** the one kernel theorem quantifying over pair cones was read for
  hidden positive content (it concludes `False` from an invariance, forbidding `reflY`; t3 Z7 confirms K(Z_F) obeys
  it). B1/B2 were read for an operation transfer: they transfer effect availability only. The discharges were read
  for their carriers: all off P. No step survived.
- **Against a too-easy independence:** (i) every row of Table A2 is re-checked by my own code (t4), every cone row by
  exact checks written without R6's code (t3), self-duality by a complete proof rather than the cited SD1/SD2; (ii) the
  violation is shown for the weakest forms, not only for stronger ones: single flows on each token, every member with
  `sin t ≠ 0`, every axis (t3, t5); (iii) the FAILS rows were checked to be hypotheses from their recorded statuses;
  (iv) countercontrols: the witness search finds nothing for the symmetries `nflip`, `rot3 π`; the modeled actions
  keep `Q3`; the binder scan fires on the no-go and not on `maxCone`; the bridge scan fires on a synthetic edge.
- **Residual risk named:** the Q3/PSD dictionary `pauliW` is a design-module object [D] at L (AUDIT-I §5.4); here it
  is part of the construction of a model, not a premise, and every model property is checked in `W 3` coordinates.

## §8 Gem classification (§A.31; productivity test of NOTES N1.3)
- ELABORATING: the derivation's wall located exactly — at L exactly two declarations quantify over a pair cone with a
  one-token map, both the reflY no-go; none concludes an invariance (t2).
- ELABORATING: a self-contained H3 proof for orthogonal Bell-type defects (one-correction lemma) and a closed-form
  witness family `−sin(t)/8` for every axis — K(Z_F) has no one-parameter local rotation symmetry (t3, t5).
- CONFIRMING: NO-MEET at declaration level (t1); the discharges stay off the pair carrier; R6's Table A2 for K(Z_F).
- POSITIVE: R6's classification of the 199 rows survives an independent re-check.
- No NEW structural blind spot was found; the minor finding (record): with the certified `ball3Drive`, the two
  weakest forms of INTEGRATION-NOTE-STAGE5 §2 are the same pair of flows `{R_z, R_x}` (the drive's J-conjugate is the
  drive through the NOT); they differ (`{R_x, R_y}` vs `{R_x, R_z}`) only under the PT convention that calls `R_x`
  the drive. BORDERLINE.

## §9 What is not claimed
No status of any inventory item changes. No claim that (b) is independent of every extension of the framework, of a
future H→P bridge, or of the hypotheses λ, H, T. No embedded-observer realization of K(Z_F) and no obstruction. The
[D] theorem `kt4_forward_ie1` and the stage-4 theorem "(b_S4) with H1–H3 forces `Q3`" are cited [A], not re-proved.
Instance checks (t3 Z4) are instance-scoped; the universal statements rest on the [W] proofs of §3.3 and the
symbolic identities of t3/t5.
