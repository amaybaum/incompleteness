# Thread B — interface lemmas between KTOKEN-MAXCONE-1 (#829) and KN-DESC-1 (#823)

Base: main `M = 5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5`. No file under `verification/lean-mathlib/` changed
between `D = dee3b5ae` and `M` (`git diff --stat dee3b5ae 5bfdaba6 -- verification/lean-mathlib/` is empty), so kernel
line numbers are the same at `D` and `M`. Worktree used: `scratchpad/threads/wt-B` (detached at M). Nothing in the
repository was edited.

Evidence labels: **[K]** kernel at M (file:line under `verification/lean-mathlib/OIBridge/`); **[D]** design source
on a branch plus its run; **[W]** written argument (a record's, or mine where marked "mine"); **[X]** exact
computation; **[U]** unsourced. Branches: `R` = `origin/research/finite-reconstruction-design-20261013` (design head
`d3a95be6`, branch head `8b431a18`, which only changes documentation); `P829` = `origin/draft/ktoken-maxcone-1`
(`625f853f`); `P823` = `origin/draft/kn-desc-1` (`8c3a262a`).

Design run 38457070337 [D]: `gh run view` gives conclusion `success`, head `d3a95be6a0049ee1450f438803ebcf2896f69744`,
job `design-build` 115502431432 `success`. I did not re-read the axiom prints: the job-log download host is blocked by
the proxy, and I did not try to get around that. They are as recorded in `R:…/finite-reconstruction-design/formalization.md:21-25`
and `R:…/carrier-descent-design/result.md:74-79`.

My exact checker is `scratchpad/threads/B_interface_check.py` (standard library only, exact arithmetic in
Q(√2)(i)). It has 57 checks and 0 failures. Its output is `B_interface_check.out`, with sha256 `5028838c…` (script) and
`3f41480…` (output). Two hand mutations were each rejected: a sign error in `cycMat` gave 6 FAILs, and a sign error in
the transition flow gave 8 FAILs. The labels below (X0–X7, A0–A1) refer to its check names.

***

## 1. The objects on each side

### 1a. #829 side (state cones, product tests, local actions, gates)

**No k-token cone object exists in any source.** `git grep -E "maxConeK|cnotK|actK|prodStateK|dictK"` over `*.lean`
and `*.py` on `R`, `P829`, `origin/research/equivalence`, `origin/main` and `origin/dev-equivalence/maxcone-20261012`
returns nothing [X]. The k-token surface exists only as proposed text in the preregistration
`P829:verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/preregistration.md` [W]:

| object | P829 prereg line | role |
|---|---|---|
| `WK k := (Fin k → Fin 4) → ℝ` | :56 | table carrier |
| `prodStateK`, `maxConeK`, `dictK`, `QK` | :57–62 | products, product-test cone, Pauli dictionary, PSD cone |
| `cnotK i j`, `actK j N` | :63–66 | CNOT on tables, local action on token j |
| `H1` (products of `eball 3`), `H2` (`cnotK i j`, **`i < j`**), `A` (`actK j (rotLin t)`, `actK j cycEquiv`, **`(j:ℕ) ≠ 0`**) | :67–69 | premises; the gate inventory is triangular and never drives token 0 |
| `subset_QK_of_maxCone_drive`, `QK_subset_of_products_cone_drive`, `kCone_eq_QK_of_drive_maxCone`, `driveInvariantK_of_eq_QK`, `kCone_eq_QK_iff_drive_maxCone`, `pairCone_eq_Q3_of_kToken` | :70–76 | proposed theorems |
| `dictK_cnotK`, `dictK_actK_rotLin`, `dictK_actK_cyc`, `pairCarrierEquiv`, … | :79–81 | proposed supporting declarations, unbuilt |

**What is compiled for it** [D, R @ d3a95be6, run 38457070337]: 23 theorems that hold for every `n` but are generic
finite algebra. None of them is a cone theorem.
- `finite-reconstruction-design/FinitePauli.lean` (14 theorems): `tensor_mul` :15, `tensor_trace` :27, `tensor_star` :33,
  `tensor_conjugation` :39, `pauliWord_hermitian` :66, `pauliWord_orthogonal` :74, `pauliWord_complete` :89,
  `coordinates_dictionary` :128, `pauliWord_reconstruction` :135, `dictionary_coordinates` :165,
  `dictionary_hermitian` :183, `coordinates_dictionary_real` :189, `coordinates_real` :194,
  `dictionary_coordinates_real` :201. Definitions: `Carrier`/`Bits`/`Labels` :45–60 (with `Bits (n+1) = Bits n × Fin 2`,
  so the newest token is the rightmost factor), `pauliWord` :62, `dictionary` :177, `coordinates` :180.
- `FiniteWalsh.lean` (6 theorems): `hadamard_symmetric` :17, `hadamard_orthogonal` :20, `walsh_symmetric` :24,
  `walsh_orthogonal` :29, `walsh_permuted_orthogonal` :57, `multiplexorAngles_recover` :68.
- `FiniteCircuit.lean` (3 theorems): `normalForm_mul` :16, `circuit_normalForm` :50, `closed_circuit_rotation` :62.
- The carriers differ from #829's. Here the carrier is `Bits n`; #829 proposes `Fin k → Fin 2`; KN-DESC uses `Fin (2^k)`.
  `formalization.md:61-62` records that the reindexing to `{0,1}^n` and the five k = 2 transports are not implemented.
- The written all-k argument is `argument.md` §§1–5 [W]. The exact k = 3 layer is `exact_check.py`, with 242 checks per
  the record. That script needs SymPy, which is absent here, so I did not re-run it.

**Pair-level anchor at M, round OI-PAIR-MAXCONE-1** [K]. These objects are used in place of the H3 schema.
- Theorems: `EqvK2MaxCone.lean`: `pairCone_eq_Q3_of_drive_maxCone` :153 (hH1, hadd, hsmul, hmax, hH2 `cnot`, hA
  `actT (rotLin t)` ∧ `actT cycEquiv` on the target ⟹ `K = Q3`); `driveInvariant_of_eq_Q3` :165;
  `pairCone_eq_Q3_iff_drive_maxCone` :174; `subset_Q3_of_maxCone_block` :116; `Q3_subset_of_products_cone_block` :107;
  `maxCone_bound_of_sharp_available` :194; `pairCone_eq_Q3_of_sharp_available` :204.
- Objects: `CompositeDimension.lean` `W` :97, `prodState` :161, `maxCone` :186, `actT` :198, `cnot` :775.
  `EqvK2Schema.lean` `pauli` :25, `dict` :78, `coordOf` :157, `coordOf_dict` :160, `dict_coordOf` :203, `Q3` :239.
- Gates as matrices, with the dictionary intertwinings landed at k = 2: `BridgeDictionary.lean` `cnotMat` :66 (control
  first) and `dict_cnot` :71. `EqvK2Converse.lean` `phaseMat` :65 (= diag(1, e^{it})), `cycMat` :106 (= (I − i(X+Y+Z))/2),
  `dict_actT_rotLin` :153 (conjugation by `tensorOf 1 (phaseMat …)`), `dict_actT_cyc` :163 (by `tensorOf 1 cycMat`),
  `Q3_aMiss` :174. `EqvK2Generation.lean` `su_euler` :323, `blockInvariant_of_drive` :426, `Q3_cnot` :503.
- **A landed pair compatibility clause.** `BridgeDictionary.TransferClause 𝓘 K` (BridgeDictionary.lean:311): for every
  admissible one-token unitary `U` (`𝓘 (Fin 2) U`), `K` is invariant under Ad(1 ⊗ U). Related theorems in
  `BridgeConverge.lean`: `transferClause_iff` :71 (table form, both directions), `transferClause_mono` :84,
  `transfer_flow_table` :103 (`TransferClause substratumClass K` ⟹ `actT (rotLin t)` preserves K),
  `transfer_nflip_of_substratum` :143, `transferClause_Q3` :152 (Q3 satisfies it for every class).

### 1b. #823 side (ImplementationClass, admitted operators, DrivesElementary, QuantumArchitecture)

Landed at M [K]:
- `ImplementationClass` ImplementationLocality.lean:244 (`∀ S [Fintype] [DecidableEq], Matrix S S ℂ → Prop`),
  `InstAvail` :268, `ContextStable` :359 (`𝓘 S K → 𝓘 (R × S) (tensorOf 1_R K)`; the spectator goes on the **left**;
  R is any finite type), `LabelInvariant` :364 (reindex along any `S ≃ S'`), `fullClass` :374, `Architecture` :506
  (`one`, `mul`, `smul` with ‖a‖ ≤ 1, `proj`, `block`).
- `DaggerStable` MicroscopicReversibility.lean:216. `DrivesElementary` SubstratumSource.lean:77 (at every carrier:
  `flow (transition a b) t`, `permMatrix (swap a b)`, `phaseGate a`). `QuantumArchitecture` :86.
  `fullClass_quantumArchitecture` :151. `diagClass_not_drivesElementary` :174.
- Generators: `transition` LieRankSource.lean:199, `phaseGate` :209, `flow` ReachabilitySeam.lean:95,
  `flow_transition_closedForm` LiftAudit.lean:276, `permMatrix` CoherentLift.lean:92, `permMatrix_mul'`
  LieRankSource.lean:232, `ancBlock` AncillaClosure.lean:457, `tensorOf` MonoidalCompletion.lean:193.
- Classes used as controls: `diagClass` LieRankSource.lean:88 (`_arch` :90, `_contextStable` :104,
  `_labelInvariant` :112, `_daggerStable` :117). `substratumClass` StructuralClosure.lean:180 (`IsMonomial`,
  SubstratumInterface.lean:75: `permMatrix σ * diagonal d`). `substratum_residual` :383 (four closure clauses hold;
  ¬DrivesElementary).

Design [D], `R:…/carrier-descent-design/KnDescentDesign.lean` @ d3a95be6, run 38457070337: `DrivesElementaryAt` :51;
`drivesElementaryAt_of_drives` :57; `compress_mem` :64; `transition_submatrix` :102; `flow_transition_self` :109
(`flow (transition a a) t = 1 + (e^{−2it} − 1) E_aa`); `flow_transition_submatrix` :118; `permMatrix_swap_submatrix` :134;
`phaseGate_submatrix` :141; `drivesElementaryAt_of_embedding` :152; `le_two_pow` :164; `drivesElementary_of_pow` :173;
`quantumArchitecture_iff_pow` :190 (→ `drivesElementaryAt_of_drives`, ← `drivesElementary_of_pow`);
`drivesElementaryAt_fullClass` :202. These are 12 theorems and 1 definition. Every statement is about matrices on
arbitrary finite carriers. The proofs use `ContextStable`, `LabelInvariant` and `Architecture.block`. **No state cone
appears anywhere on this side.** This confirms the owner's reading: the theorems assume the carrier-general matrix
framework and close under spectators.

### 1c. The interface record (quoted)

`R:verification/programmes/oi-qm/reconstruction/finite-reconstruction-design/argument.md:178-186` (identical text at
d3a95be6 :177–185), §6 "What does and does not combine with KN-DESC":

> The initial k-token cone result supplies none of these implementation memberships.
> A valid combined finite theorem must additionally name:
>
> - a dictionary identifying the physical k-token carrier with H_k;
> - a common implementation class and its closure clauses;
> - an admitted repertoire on every qubit-power carrier strong enough for the
>   three `DrivesElementaryAt` families (including each parameterized transition
>   flow, swap and quarter phase), rather than cone preservation alone;
> - the state/operation compatibility premises for that same class and cone family.

It continues at :188–192: "Even full state-space equality does not imply a complete operational repertoire: the
identity-only inventory preserves the whole PSD cone and drives no nontrivial transition. … Descent does not
manufacture a three-level physical system out of qubit registers."

Companion statements:
- `R:…/carrier-descent-design/result.md:37-40`: "To use it here one still needs a dictionary into the same
  implementation class and admission of the exact finite words. A cone identification alone does not give that
  repertoire interface."
- `formalization.md:59-60` (carrier identification "remains a premise") and :101–103 ("supply no
  implementation-class membership for KN-DESC and discharge no … state/operation compatibility premise").
- P829 prereg :155–157 (combination "only through a map to operational carriers and a drivability source, neither
  supplied here") and P823 prereg :146–153.
- The plan branches restate the gaps in general form: `origin/plan/joint-tests-source-20261013`
  `…/research-planning/joint-test-validity-source.md:9,16`, and `origin/plan/compatibility-source-20261013`
  `…/physical-compatibility.md:20`. Main has no file with these phrases.

***

## 2. The four separations as candidate lemmas

Notation: `Tok k` stands for whichever k-token carrier is fixed (`Bits k` or `Fin k → Fin 2`). `localMat j U` is U on
token j with identity elsewhere. `cnotMatK i j` is the matrix of `cnotK i j`.

### L1 — physical carrier identification

**L1-M (mathematical part, provable).**
```lean
def bitsEquivFun (k) : Bits k ≃ (Fin k → Fin 2);   def labelsEquivFun (k) : Labels k ≃ (Fin k → Fin 4)
def bitsEquivFin (k) : Bits k ≃ Fin (2 ^ k);       theorem card_bits (k) : Fintype.card (Bits k) = 2 ^ k
theorem dictK_eq_dictionary (ω : WK k) :
  dictK ω = Matrix.reindex (bitsEquivFun k) (bitsEquivFun k) (dictionary k (ω ∘ labelsEquivFun k))
theorem drivesElementaryAt_congr (hL : LabelInvariant 𝓘) (e : S ≃ S') :
  DrivesElementaryAt 𝓘 S → DrivesElementaryAt 𝓘 S'
def pairCarrierEquiv : W 3 ≃ₗ[ℝ] WK 2   -- with its five transports (dict, prodState, pairing, cnot, actT)
```
- **Directions.** The dictionary is already two-sided at `Bits` [D]: `coordinates_dictionary_real` FinitePauli:189 and
  `dictionary_coordinates_real` :201. `drivesElementaryAt_congr` is applied once with `e` and once with `e.symm`.
- **Composes with.** `drivesElementary_of_pow` (it needs `Fin (2^k)`), the #829 theorems on `Fin k → Fin 2`, and
  `pairCone_eq_Q3_of_drive_maxCone` through `pairCarrierEquiv`.
- **Evidence now.** The inverse pair at `Bits` [D]. `drivesElementaryAt_congr` is available today as
  `drivesElementaryAt_of_embedding arch hC hL e.symm.toEmbedding` [D]. A proof using LabelInvariant alone needs
  reindex-of-flow, which follows from the closed forms LiftAudit.lean:276 [K] and KnDescentDesign:109 [D].
- **Physical part, H-CAR (introduced premise, not provable).** The k-token physical system is implemented on `Tok k`,
  its state set is `dictK '' K k`, and adjoining a token is the right factor. This is multi-token local tomography plus
  the token-order convention (P829 :152–153). The research notes say the k-token chart needs the parity/IE₂ premises
  (`origin/research/equivalence@424aa33b:research/equivalence/NOTES-E3.md:111-115`) [W]. In Lean it shows up only as
  the choice of map used in L4.
- **One trap.** ContextStable puts spectators on the left, while `Bits` grows on the right. The token-order map in
  `dictK_eq_dictionary` must be fixed once and used in L3 and L4.

### L2 — a common implementation class (the combined theorem)

```lean
theorem kToken_cone_and_descent {𝓘} (arch : Architecture 𝓘) (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘)
    (hpow : ∀ k, DrivesElementaryAt 𝓘 (Fin (2 ^ k)))
    (K : ∀ k, Set (WK k)) (hcompat : ∀ k, ConeCompat 𝓘 k (K k))          -- L4
    (hH1 : ∀ k, H1 (K k)) (hadd …) (hsmul …) (hmax : ∀ k, K k ⊆ maxConeK (eball 3)) :
    DrivesElementary 𝓘 ∧ ∀ k, K k = QK k
-- pair instance, all inputs landed except L3b at Fin 2 × Fin 2:
theorem pairCone_eq_Q3_of_drives (arch) (hd : DrivesElementary 𝓘) {K : Set (W 3)}
    (hcompat : ∀ U, 𝓘 (Fin 2 × Fin 2) U → Uᴴ * U = 1 → ∀ ω ∈ K, coordOf (U * dict ω * Uᴴ) ∈ K)
    (hH1) (hadd) (hsmul) (hmax) : K = Q3
```
- **Direction: forward only.** The proof chains `drivesElementary_of_pow` [D] for the first conjunct. For the second
  conjunct, per k: L1-M, then L3b, then L4′, then `kCone_eq_QK_of_drive_maxCone` (proposed). The pair instance ends in
  `pairCone_eq_Q3_of_drive_maxCone` :153 [K] through `dict_cnot` :71, `dict_actT_rotLin` :153, `dict_actT_cyc` :163 and
  `coordOf_dict` :160.
- **The converse has a known countermodel.** Take `𝓘 = diagClass`, or `substratumClass`, with `K k = QK k` (`Q3` at
  k = 2). The closure clauses are landed (LieRankSource :90/:104/:112/:117; StructuralClosure :383). `hcompat` holds
  because admitted isometries are unitary and the PSD cone is unitarily invariant (`transferClause_Q3` :152 at the
  pair; Mathlib `PosSemidef.mul_mul_conjTranspose_same` for every k). Every cone premise holds. Yet ¬DrivesElementary
  (SubstratumSource :174; StructuralClosure :370). So "cone equality ∧ clauses ∧ compat ⟹ drivability" is false
  [K + W], and no iff may be displayed (§A.34).
- **Positive control.** `fullClass` with QK satisfies every premise (`fullClass_quantumArchitecture` :151,
  `drivesElementaryAt_fullClass` [D]).
- **What the theorem uses.** It never uses DaggerStable. It uses hC only for the drivability conjunct on carriers that
  are not powers of two (see L7).
- **What it trades.** It replaces #829's state-side hH2 and hA by hpow plus H-COMPAT. Those hypotheses are strictly
  stronger: they drive token 0 and every CNOT direction. Nothing is sourced; this is consistency work, so the
  correctness bands are unchanged.

### L3 — the admitted generators

**L3b (drivability ⟹ #829's gates are admitted). Plausibly provable from `Architecture.one/mul` alone.**
```lean
theorem permMatrix_mem_of_drivesAt (arch) (h : DrivesElementaryAt 𝓘 T) (σ : Equiv.Perm T) : 𝓘 T (permMatrix σ)
theorem diagonal_mem_of_drivesAt (arch) (h) (d : T → ℂ) (hd : ∀ a, ‖d a‖ = 1) : 𝓘 T (Matrix.diagonal d)
theorem cnotMatK_mem (arch) (h : DrivesElementaryAt 𝓘 (Tok k)) (i j) (hij : i ≠ j) : 𝓘 _ (cnotMatK i j)
theorem localRot_mem (arch) (h) (j t) : 𝓘 _ (localMat j (phaseMat (cos t) (sin t)))
theorem localCyc_mem (arch) (h) (j) : 𝓘 _ (localMat j cycMat)
```
These give gates on every token and in every CNOT direction, which is more than #829's triangular H2/A needs.
- **Explicit exact words** [X]:
  - CNOT(i→j) is the product of the swaps `(a, a⊕e_j)` over `bit_i(a) = 1, bit_j(a) = 0`
    (X1-CNOT-FROM-SWAPS-k2/k3; A1 matches the landed `cnotMat`).
  - `phaseMat(t)` on token j is the product of self-flows `flow (transition a a) (−t/2)` over `bit_j(a) = 1`
    (X1-ROT).
  - `cycMat = Rz(π/2)·Rx(π/2)` exactly (X0-CYC-EULER; the reverse order fails). So `cycMat` on token j is the product
    over control words of `flow(transition p p)(π/8) · flow(transition q q)(−π/8) · flow(transition p q)(π/4)`
    (X1-CYC-k2/k3; dropping one block is rejected). This needs neither `su_euler` nor `phaseGate`.
- **The general SU(2) case** goes through `su_euler` :323 [K]. Its two-level factors are
  `rotRe(c,s) = phaseGate q · flow(transition p q)(θ) · phaseGate q³` and `dUnit` as two self-flows (X7) [X].
  `permMatrix_mem_of_drivesAt` uses `Equiv.Perm.swap_induction_on` (Mathlib) and `permMatrix_mul'` :232 [K].
- **Composes with.** Upstream, KN-DESC's hpow (after `drivesElementaryAt_congr`). Downstream, L4′.
- **Corollary [W, mine].** DrivesElementaryAt plus Architecture admit every monomial unitary, which is the unitary part
  of `substratumClass`.

**L3a (#829's gates are admitted ⟹ drivability).** This is needed only to source hpow from token-level gates
(NOTES-E3:111-115).
- **(i) Without LabelInvariant it fails for products of the gates (mine).** Every triangular generator (CNOT(i→j) with
  i < j; rotations and `cyc` on tokens j ≥ 1) commutes with Z on token 0. So does every product of them. No transition
  or swap across token 0 does (X3-TRIANGULAR-COMMUTES-Z0, X3-TRANSITION-ACROSS-TOKEN0-NOT, X3-SWAP-ACROSS-TOKEN0-NOT;
  k = 2, 3) [X + W]. I have not built a full Architecture countermodel that also allows `proj`, `block` and
  ContextStable; the claim is scoped to products of the gates. At k = 1 the triangular inventory is empty.
- **(ii) With LabelInvariant and Architecture, for k ≥ 2: plausibly true.** Relabelling the bits gives token-0 gates
  (X3-RELABEL-GIVES-TOKEN0-CYC). After that, exact multi-controlled synthesis is needed: the Gray multiplexors of
  `argument.md` §3 with `multiplexorAngles_recover` and `circuit_normalForm` [D], plus the still-open obligations 1–3
  of `formalization.md:86-95`. Even then it reaches the cone side only through **H-GEN** (introduced: every cone gate
  under which K is invariant is admitted). The countermodel `(diagClass, QK)` shows H-GEN is not implied.

### L4 — state–operation compatibility

```lean
def ConeCompat (𝓘) (k) (K : Set (WK k)) : Prop :=                          -- H-COMPAT (introduced premise)
  ∀ U : Matrix (Tok k) (Tok k) ℂ, 𝓘 _ U → Uᴴ * U = 1 → ∀ ω ∈ K, dictKInv (U * dictK ω * Uᴴ) ∈ K
theorem driveInvariantK_of_compat (hcomp : ConeCompat 𝓘 k K)
    (hcnot : ∀ i j, i < j → 𝓘 _ (cnotMatK i j))
    (hloc : ∀ j, (j:ℕ) ≠ 0 → ∀ t, 𝓘 _ (localMat j (phaseMat (cos t) (sin t))) ∧ 𝓘 _ (localMat j cycMat)) :
    H2 K ∧ A K                                                             -- L4′, provable
theorem transferClause_of_pairCompat (hC : ContextStable 𝓘) (h : pairCompat 𝓘 K) :
    BridgeDictionary.TransferClause 𝓘 K                                    -- links to the landed clause
```
- **Directions.** L4′ uses one direction: admitted ⟹ preserved. The reverse, **H-OPSAT** (a unitary that preserves K is
  admitted), is needed for any cone-to-drivability use. Without it the converse fails, by the `diagClass`/QK
  countermodel.
- **Composes with.**
  - The intertwinings: at k = 2 they are landed [K] (`dict_cnot`, `dict_actT_rotLin`, `dict_actT_cyc`, `dict_coordOf`).
    At k they are the proposed `dictK_cnotK`/`dictK_actK_*` (P829 :79–80), unbuilt.
  - The rotation half of A at the pair is already derivable: `TransferClause substratumClass K` ⟹ `transfer_flow_table`
    :103 [K]. A two-token clause is still needed for CNOT, because TransferClause covers one-token U only.
  - The protocol lift through `PreservationInduction.instAvail_preserves`
    (`origin/research/preservation-induction-design-20261013`, PreservationInduction.lean:55, with
    `PrimitivePreservation` :25) [D, run 38450187534 per its build-status.md; not re-verified]. Its attach/discard
    clauses (:33, :37) need the cone family on `S × Fin m` for **every** m. The k-token side supplies cones only on
    qubit-power carriers (see L10).
- **Evidence now.** H-COMPAT is not sourced [U]. Availability does not imply it: the pair cone K_B
  (`origin/research/bridge-compatibility-20261013`, `bridge-compatibility-audit/result.md`) shows an available
  depth-one map leaving the cone [W + X].
- **New pair-level countermodel (mine).** Let `K_mono` be the conic hull of the conjugates of pure products by
  monomial unitaries.
  - It satisfies: the four closure clauses of `substratumClass`; H-COMPAT for `substratumClass` (by construction);
    TransferClause; hH1 (mixed products are nonnegative sums of pure ones); hadd; hsmul; hmax (K_mono ⊆ Q3 ⊆ maxCone);
    hH2 (`cnotMat` is monomial); and the rotation half of hA (X4-MONOMIAL-CNOT-ROT).
  - It is not invariant under `cyc`, and K_mono ≠ Q3. Take `v = phaseGate(1,1)|++⟩`, which is in the orbit. Then
    `(1⊗cycMat)v = (−i, 1, 1−i, 0)` has support 3, while monomial images of products have support 1, 2 or 4
    (X6-*) [X]. A rank-one PSD matrix is a positive sum only of multiples of itself, so this element lies outside
    K_mono [W].
  - So with compatibility, the substratum's monomial repertoire supplies hH2 and the rotation clause but **not the
    cyclic, off-axis clause**. This is the cone-side image of `¬DrivesElementary substratumClass`. Classification:
    NEW (scoped to k = 2). It is related to #829's ORBIT3, which is at k = 3 with GL(3,F₂) only.

***

## 3. Further missing lemmas

- **L5 — k-token intertwinings and product law.** `dictK_cnotK`, `dictK_actK_rotLin`, `dictK_actK_cyc`,
  `dictK_prodStateK` (a k-fold tensor of `tokMat (hom (x i))`), and a k-fold `pairVal_nonneg_of_maxCone`. These are
  #829 design items (P829 :79–80, :206–209). Pure algebra on top of `tensor_conjugation` and the FinitePauli inverse
  pair, so plausibly provable. Pair versions are landed [K].
- **L6 — test-side interface.**
  `maxConeK_bound_of_sharp_available : K ⊆ maxConeOfK avail → sharpFamilyK ⊆ avail → K ⊆ maxConeK (eball 3)`. This is
  the k-fold form of EqvK2MaxCone.lean:194 [K]. Linking `avail` to admitted readout projectors
  (`InstAvail.readout`, ImplementationLocality:268) requires a validity premise on joint preparations. That is the
  plan in `joint-test-validity-source.md`, unsourced [U]. The mathematical part is plausibly provable.
- **L7 — divisor descent without ContextStable, and why odd spectators are load-bearing.**
  ```lean
  theorem drivesElementaryAt_of_block (arch) [NeZero m] : DrivesElementaryAt 𝓘 (S × Fin m) → DrivesElementaryAt 𝓘 S
  theorem drivesElementaryAt_of_dvd (arch) (hL) [Nonempty S] (h : DrivesElementaryAt 𝓘 T)
      (hdvd : Fintype.card S ∣ Fintype.card T) : DrivesElementaryAt 𝓘 S
  ```
  - The block identities are exact (X5-BLOCK-DESCENT for (|S|, m) = (3,2), (3,4), (2,2), (5,2)) [X]. So within
    qubit-power carriers, descent needs only `block` and LabelInvariant, not hC.
  - **Countermodel (W; the class is from NOTES-E3:58-63).** "Every matrix at sizes 2^j, unit-disk diagonals elsewhere."
    It satisfies Architecture, LabelInvariant and DaggerStable, and drives every `Fin (2^k)`. It **is**
    ContextStable for every spectator of size 2^m (X5-POW2-SPECTATOR-KEEPS-DIAGONAL). It fails hC only at odd
    spectators (X5-ODD-SPECTATOR-BREAKS-DIAGONAL) and does not drive `Fin 3`.
  - So any interface that reaches only qubit-power carriers (H-CAR) leaves `DrivesElementary` at `Fin 3` dependent on
    the carrier-general hC, or on a corner-compression clause (NOTES-E3:125-133). Classification: ELABORATING; the
    research thread has priority.
- **L8 — the swap family is redundant.**
  `permMatrix (swap a b) = phaseGate a * phaseGate b * flow (transition a b) (π/2)` for `a ≠ b`, and `swap a a = 1`.
  Exact for n = 2…5; dropping one phase is rejected (X2) [X]. So
  `drivesElementaryAt_of_flows_phases (arch)` holds: the qubit-power repertoire obligation reduces to two families.
  Plausibly provable from LiftAudit:276 at s = π/2. Classification: ELABORATING. This is a different reduction from
  round 59's phase-free repertoire.
- **L9 — the hH1 seed.** With H-COMPAT, admitted local unitaries (L3b), hadd and hsmul, a single pure product in `K k`
  gives every `eball 3` product. Written, and low priority.
- **L10 — extending the cone family beyond qubit-power carriers**, or restricting protocols to qubit-power ancillas.
  This is needed before H-COMPAT can be lifted to `InstAvail` protocols through PreservationInduction. Open; no
  candidate yet.

***

## 4. Status of each candidate lemma

| lemma | status | new premise needed | known countermodel / obstruction |
|---|---|---|---|
| L1-M carrier triangle, `drivesElementaryAt_congr`, `pairCarrierEquiv` | plausibly provable (pure reindexing; half already in FinitePauli) | none | none |
| H-CAR physical carrier identification | not provable | **H-CAR** (k-token local tomography + token order) | none needed; unsourced [U] |
| L2 combined theorem, forward | provable once L1-M, L3b, L4′ and #829's theorem exist; the pair instance needs only L3b@pair | H-COMPAT, hpow, closure clauses (all retained) | converse refuted: `(diagClass or substratumClass, QK)` [K + W] |
| L3b drivability ⟹ gates | plausibly provable from `Architecture.one/mul`; exact words checked k = 2, 3 | none | none |
| L3a(i) gates ⟹ drivability, products of gates only | false | — | Z on token 0 commutes with every triangular product [X + W]; k = 1 inventory empty |
| L3a(ii) with LabelInvariant, k ≥ 2 | plausibly true; needs exact multiplexor synthesis (formalization.md obligations 1–3, open) | **H-GEN** to connect to cone invariance | `(diagClass, QK)` without H-GEN |
| L4 H-COMPAT | not provable from current hypotheses | **H-COMPAT** | K_B (#820): availability does not imply preservation [W + X] |
| L4′ compat + admitted gates ⟹ H2 ∧ A | provable once L5 exists (landed at k = 2) | — | — |
| L4 reverse (preservation ⟹ admission) | not provable | **H-OPSAT** | `(diagClass, QK)`; `(substratumClass, K_mono)` shows compat with the monomial class misses the `cyc` clause [X + W] |
| L5 intertwinings / product law | plausibly provable | none | none |
| L6 test interface | mathematical part plausibly provable; physical part open | product-test validity on joint preparations | — |
| L7 divisor descent | plausibly provable (block identities exact) | none | qubit-power-spectator class does not drive `Fin 3` [W + X] |
| L8 swap redundancy | plausibly provable (exact n ≤ 5) | none | — |
| L9, L10 | L9 written; L10 open | L10 may need a carrier-general cone family | — |

***

## 5. Recommended build order

1. **L8 and L3b on a generic carrier `T`.** Matrix-only. Uses landed `permMatrix_mul'`, `su_euler`, LiftAudit:276 and
   KN-DESC's `flow_transition_self`. This is the cheapest step and is decisive for every later one.
2. **The pair interface `pairCone_eq_Q3_of_drives`.** Use the OI-PAIR-MAXCONE-1 anchor
   (`pairCone_eq_Q3_of_drive_maxCone` :153) with the landed intertwinings, plus `transferClause_of_pairCompat`. Build
   with three controls: `(fullClass, Q3)` positive; `(diagClass, Q3)` refuting the converse; `(substratumClass, K_mono)`
   showing the cyclic clause is load-bearing.
3. **L1-M and L5.** These are shared with #829's own design and should be coordinated with its module: carrier
   triangle, `pairCarrierEquiv`, k-token intertwinings.
4. **L4′ and the k-token combined theorem L2**, after `kCone_eq_QK_of_drive_maxCone` exists.
5. **L7** (divisor descent and the qubit-power-spectator countermodel), to scope what L2 says about carriers that are
   not powers of two.
6. **L6** (test side), jointly with the joint-tests plan.
7. **L3a(ii)** (exact synthesis), only if a route sourcing hpow from token gates is chosen. It still needs H-GEN.

Throughout, H-CAR, H-COMPAT, H-GEN, H-OPSAT, hpow and the closure clauses stay explicit hypotheses. No item sources
OI physics, and K2 and Kₙ stay OPEN.
