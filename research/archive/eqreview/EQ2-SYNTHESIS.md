# EQ2 synthesis — dependencies, two theorem statements, and the next research question

Research only, base `bcbc516f`. Nothing here is adopted, frozen or governed, and governance stays frozen. Thread
results: `scratchpad/eq2/{A,B,C}/RESULT.md`. Replays and independent checks: `scratchpad/eqreview/REVIEW.md`.

Evidence tags:
- **[K]** landed kernel identifier at the base.
- **[X]** exact computation, replayed byte for byte.
- **[X\*]** exact computation in independent code of mine.
- **[W]** written proof, not kernel-checked.
- **[L]** literature, unverified.

No item below is kernel-checked unless it carries [K]. The exact checks support the general statements; they are not
Lean proofs of them.

## 1. Verification

| thread | replay | independent check | flags |
|---|---|---|---|
| EQ2-A (composition, IE₂) | 9/9 identical | `review_eq2a_cm` 28/28: countermodels, transported premises, IE₂ failure, chart parity. `review_eq2a_cm2` 13/13: twisted hull not self-dual, orbit bound, transposed gate class | float x3 was a false negative, superseded by exact a4c (recorded by the thread) |
| EQ2-B (two systems) | 7/7 identical | `review_eq2b` 56/56: 4-parameter tangent family (rank 124 over 24 sphere points), ±1 forcing, 8/8 split, orientation 4 Q3 / 4 twin / 8 none | parametrization map `(a,a₂,b₁,b₂) = (a,a′,−b′,−b)`; "no SVD at the pin" means singular values but no decomposition |
| EQ2-C (dimension, K∞) | 8/8 identical | BP-S proof re-read | "Spec2 holds at every level" should read "Spec_k (frames of the capacity) and SS hold at every level; Spec2 is the capacity-two case" |

Integrity:
- The base manifest holds (1317 files).
- The repository is clean.
- No thread wrote outside its directory.

## 2. Three separations

**(a) Two-system mathematics.** The gate case of Theorem A′ has an exact route with no Lie theory and no compactness.
- **N-CLASS** [X][X\*]: every `CtrlGate` at d = 3 is `ℓ₁ ∘ cnot ∘ ℓ₂` with `ℓᵢ ∈ O(3)×O(3)`. It rests on a written
  reduction to landed lemmas (corner forms RSB:60/99, tangent orthogonality RSB:129, the parity theorem RSP:329) plus
  an exact rank certificate.
- **ORIENT** [X][X\*]: with local invariance and a candidate cone, the gate is in `L·{cnot, T∘cnot}·L` (cone Q3) or its
  `R_B`-conjugate (the twin). The reflection classes admit no candidate cone: [K] for `R_B` (K2G:143), [X] for `R_A`.
- **Transitivity and group form**: EQ2-A's Lie-free universality (two-level decomposition, Barenco recursion,
  closed-form 2×2 square roots, SWAP routing) [X instances, W general, L Barenco 1995]. It replaces both EQ2-B's
  Lemma TRANS, which needed a 2×2 SVD, and KAK.
- **`driveWords3 = SO(3)`** [K ON:53/571/658 + X]. The countability obstruction does not arise.

None of this is a kernel proof; N-CLASS needs its certificate formalized (EQ2-B R1–R2).

**(b) Cone selection and composition are separate problems.**
- **Two copies.** With IE₁ and the gate, the composite is Q3 or the twin. Both satisfy every two-copy premise,
  exchange symmetry included: the twin is SWAP-invariant [X a5 E4].
  - The per-token chart (I, R) maps one to the other [X], so under D1 the choice is a convention.
  - No type-uniform chart presents the twin [X review_pass2 C1].
- **Three copies.**
  - The pair twist bits τ are free data. A coherent per-token chart exists iff every cycle of τ is even [X].
  - The transported two-copy premises allow an odd cycle (`M_odd`, `M_tw`) and the biseparable hull (`M_bs`) [X][X\*].
  - Parity and generation both need a three-copy principle.
- **Gate class at three copies (new).** IE₂ with H0 excludes the transposed class `T∘cnot` [X\*].
  - At two copies `T∘cnot` maps Q3 onto Q3.
  - Its idle extension sends `|0⟩⟨0| ⊗ Φ⁺` to a state whose (1,2) marginal is `PT(Φ⁺)`.
  - So the two-copy premises admit a gate class that composition excludes.

**(c) Gate classification is not generation.**
- N-CLASS says what the native gate is.
- Generation says that the physical local operations and that gate generate every required unitary:
  - two copies: `⟨L, cnot⟩` is the presented PU(4);
  - n copies: tree-edge gates and locals give PU(2ⁿ).
- The physical local operations are the composite lifts of `driveWords3` (SO(3) ≅ PU(2) through the Pauli dictionary,
  [X] EQ2-B A.5), so generation presupposes IE₁ for the locals and IE₂ for the edge gates.
- For the `T∘cnot` class, the interaction group `L ⊔ G L G⁻¹` still contains `cnot` by an explicit finite word
  (`cnot ∘ actC(R_x θ) ∘ cnot = Ad exp(−iθ XX/2)`, [X] EQ2-B D.1).
- Generation is pure mathematics; availability is what the premises must supply.

## 3. Assumption-dependency table

Main rows (the five the owner named):

| item | proved implications into it | proved independent of | consumed by | status |
|---|---|---|---|---|
| **IE₁**: two-copy composite invariant under the lifts of `driveWords3` | ISP ⇒ IE₁ (instance). K₂ ∈ {Q3, twin} ⇒ IE₁ (trivial) | admissible, closed, convex, gate-invariant cones: `K_F` = cone(Clifford·products) [X EQ2-B b5]. Finite-subgroup invariance is insufficient; a dense subgroup needs closedness [X/W] | K2 cone theorem; generation (the locals) | **independent premise** |
| **IE₂**: idle extension of the pair interaction groups, tree closure form | ISP ⇒ IE₂ (instance). K_S = PSD_S in a chart ⇒ IE₂ for unitary conjugations (trivial). Product-effect form: automatic [X C12], no content | all transports of the landed two-copy premises together with IE₁, EX and pair-CX: `M_odd`, `M_tw`, `M_bs` [X][X\*] | parity, generation, exclusion of `T∘cnot` | **independent premise**; KT∞ route **open** |
| **cone selection** (Q3 vs twin; gate class) | IE₁ + gate + admissible ⇒ {Q3, twin} [X+W]. Per-token chart identifies them [X]. IE₂ + H0 ⇒ not `T∘cnot` [X\*]. Uniform composition (or EX) + IE₂ ⇒ every twist bit 0 ⇒ uniform chart [X a5 E5 + W] | EX alone (twin; `M_tw`) [X]. EX + IE₂ for the exchange only (`M_tw`) [X a5 E6] | the per-type theorem only (D1 makes it a convention otherwise) | **settled under D1**; per-type needs uniform composition + IE₂ |
| **parity** (all twist cycles even ⇔ coherent per-token chart) | IE₂ + IE₁ + K2 + H0 ⇒ parity [W, Theorem C]. KT₂ ⇒ every 4-cycle even, τ = δε + c [X D1–D2 + W]. On a tree every τ is a coboundary [X a2b S3d] | transported premises (`M_odd`) [X][X\*]. EX (`M_tw`) [X]. KT₂ leaves the global bit c (triangles) [X+W] | chart existence at n ≥ 3 | follows from IE₂; from kinematics only partly (**open**: KT∞) |
| **generation** (locals + gate ⊇ PU(4); tree edges ⊇ PU(2ⁿ)) | Lie-free U1–U5 [X instances, W, L]. Lie-algebra closure for every tree with n ≤ 7, with the forest countercontrol [X] | — (mathematics) | K_S = PSD_S (with the spectral-theorem bounds) | **theorem route** (formal work elementary, heavy) |

Further rows:

| item | status | evidence |
|---|---|---|
| **ISP** (native inert-spectator compositionality: an available operation stays available, acting identically, when an independent system is added) | one principle with IE₁ and IE₂ as instances. Matrix side: ISP ⇔ `HasParallelReferenceExtension` [K SB:233]; locality forces the form [K SB:188; native X a2b S0a] | its content is existence; the form is free |
| **H0** (composite consistency across sizes) | needed by the all-copy theorem; holds in every countermodel, hence insufficient | [X] |
| **KT₂ / KT∞** (COMP-1 on 2\|2 / on every bipartition) | KT₂ ⇒ 4-cycle parity. KT∞ ⇒ K₃ = Λ(K₃\*) [W, links X]. Both minimal hulls fail it [X]. `B_tw` has LU-invariant self-positive extensions [X a4d] | **open wall**; see §5 |
| **EX, CX, uniform composition** | insufficient alone at three copies (`M_tw`, `M_bs`) | [X] |
| **BP** | follows from Spec2 + SS at capacity two (BP-S) | [W]; each premise needed [X] |
| **FiniteRank** | ⇔ UFR ∧ (N) [W]. Independent of the protocol-tower structure [X] | open whether the gate premises force it |
| **K∞-Act data, V4** | theorem routes (prefix-closed effects, inverse-closed menus, label duals) | [W/X] |

## 4. Two theorem statements

### Theorem E — the strongest result from the existing premises

**Existing premises** are the hypotheses that landed theorems already take:
- the K∞ obligations as stated: stage data, K∞-Seed, K∞-Trans, K∞-V4, effect soundness and body preservation;
- DIM-1's carrier `W d`, which builds in local tomography;
- one common `IsNot`;
- the control-gate hypotheses (`CtrlGate`: frame, two-sided positivity, relC) with the entangling clause.

All of these are unsourced, as the ROADMAP's K row records.

1. [K] The single-system body is a Euclidean ball (TRB-1), and the cone of the available tests is `maxCone (eball d)`
   (EFF-1).
2. [K] `d ∈ {1, 3}`, and `d = 3` with the entangling clause (`dim_of_ctrlGate` RSB:739, `three_of_ctrlGate` RSB:753).
3. [X+W, not K] At d = 3 the gate is `ℓ₁ ∘ cnot ∘ ℓ₂` with `ℓᵢ ∈ O(3)×O(3)` (N-CLASS).
4. [K for `R_B`, X for `R_A`] The one-copy reflection classes leave no candidate cone invariant.
5. [X] Nothing more about composites follows:
   - a closed admissible gate-invariant two-copy cone need not be Q3 or the twin (`K_F`);
   - at three copies the transported premises admit `M_odd`, `M_tw` and `M_bs`, in which IE₂ fails.

In one line: a native qubit with a CNOT-class gate, and composite state spaces that these premises do not determine.

### Theorem C — conditional finite quantum equivalence (qubit-power carriers)

**Premises:**
- **(S)** single system: K∞-Stage (SC∞, FiniteRank), K∞-Act, K∞-Seed, K∞-V4, effect soundness, and, in place of
  K∞-Trans, Spec2 + SS at capacity two (BP-S);
- **(G)** two copies: the carrier `W d`, type covariance, `IsNot`, `CtrlGate`, entangling, `2 ≤ d`;
- **(I)** composition: H0, and ISP (instances IE₁ and IE₂ on a spanning tree of interacting pairs).

**Conclusions:**
1. `d = 3`. Gate route: EQ2-C composes landed theorems with cheap adapters.
2. K₂ ∈ {Q3, twin}, and the gate lies in `L·cnot·L` or its `R_B`-conjugate.
   - The transposed classes are excluded by IE₂ + H0.
   - Route: N-CLASS, ORIENT, U1–U5 transitivity.
3. A per-token chart family presents every token set's cone as `PSD(ℂ^{2^S})`, unique up to the global transpose.
   - Route: Lemma Kₙ-COPIES (written), parity from IE₂, generation from U1–U5.
4. Under the charts:
   - the available reversible operations are unitary conjugations;
   - states, effects, probabilities, composition and idle extension are preserved (operational equivalence, D1);
   - through the typed bridge (EQ2-A TA3: a two-line proof on landed `rfl` facts), the presented theory satisfies
     `ObservationalIndependence`;
   - `oiPlus_iff_qm` [K CGOP:207] needs all four OI⁺ conjuncts (CGOP:185): `WellFormed`,
     `ObservationalIndependence`, `ReversibleRichness`, `ObserverRecursion`. Generation is the expected source of
     `ReversibleRichness`. `WellFormed` and `ObserverRecursion` (instruments and conditioning) are not yet checked for
     the native presentation. Until they are, conclusion 4 ends at observational independence, not at the kernel
     equivalence.

**Converse:** qubit QM satisfies every premise [X/standard].

**Per-type corollary:** with uniform composition, or EX, a type-uniform chart exists.

**Kept conditional:** the intermediate theorem "equivalence given coherent charts" (EQ2-A TA1/TA3).

**Scope.**
- The theorem reaches composites of qubit-type tokens.
- Every finite carrier with its ancilla extensions (the K3 interfaces) needs a subsystem or subspace principle (Kₙ
  census Q2; EQ-D). It is not claimed here.
- Status: written and exact route; nothing kernel-checked beyond the cited landed pieces.

## 5. The key question

> Can "an available operation remains valid when an independent system is added" be derived from an observational
> consistency principle, without assuming quantum composition in advance?

What is settled:

1. **Form is free; existence is the content.** Under local tomography the only candidate extension is `g ⊗ id`
   ([K] SB:188; native [X] a2b S0a). The content is closure: `(g ⊗ id)(K_S) ⊆ K_S`.
   - "Joint statistics stay valid for every joint measurement" is equivalent to closure under the no-restriction
     hypothesis.
   - So that statistical restatement is a relabelling, not a derivation.
2. **Product-effect observations cannot detect a failure** [X C12]. Any observational principle that implies IE₂ must
   use entangled joint effects.
3. **The transported two-copy premises are insufficient** [X][X\*]. A three-copy principle is required.

The candidate I recommend investigating as the single principle is **composition coherence (KT∞)**: every grouping of
a finite family of systems into two parts is a valid composite of those parts. It is observational: it speaks only
of states, effects and probabilities of regrouped composites, and it presupposes no quantum composition. It already:
- forces every 4-cycle of twist bits to be even [X];
- forces co-self-duality of the three-copy cone [W];
- excludes both minimal hulls [X];
- (my written observation, unverified) at four copies, with Bell-type links on two disjoint pairs, forces the
  two-copy cone to satisfy `K₂ = T(K₂*)`. That excludes `K_F` (`K_F ⊊ Q3` gives `T(K_F*) ⊋ Q3`).
  - The observation rests on two assumptions not yet separated:
    - **uniform composition:** every pair composite is the same `K₂`. Without it, KT relates different pairs' cones.
    - **link states:** `Φ⁺` is both a state and an effect of the link pairs. Gate invariance of each standalone pair
      supplies both: `cnot(|+⟩⟨+| ⊗ |0⟩⟨0|) = Φ⁺`, and the dual action of cnot on a product effect.
  - The derivation uses state-level coherence and two-token operations only, never an operation on part of a larger
    composite. That is the condition for it not to presuppose IE.
  - EQ3 Amendment 1 asks the thread to check all of this.

So KT∞ might imply **both** idle-extension conditions:
- IE₁, by rigidity of gate-invariant co-self-dual admissible two-copy cones;
- IE₂, by forcing `K₃ = PSD₈` in a chart.

Two walls decide it:
- **W2 (two copies):** is every admissible, cnot-invariant cone with `K = T(K*)` either Q3 or the twin?
- **W3 (three copies; EQ2-A's wall):**
  - c = 1: does an LU-invariant `K₃ = K₃*` exist strictly between `B_tw` and `B_tw*` and extend to more copies?
  - c = 0: is `PSD₈` the only `T`-co-self-dual LU-invariant cone in the sandwich?

Either outcome is informative:
- A positive answer derives the inert-spectator requirement from composition coherence.
- An exact countermodel shows exactly which dynamical premise quantum mechanics adds to kinematic composition.

The fallback candidate, held in reserve (depth-first), is the OI-native **completion (purification)** principle:
every state of a composite is the marginal of a pure state of a larger one. It also excludes the three minimal hulls
(my written observation, unverified). In a pairwise hull the extreme rays are products of pure pieces, so a mixed
entangled pair state is the marginal of no extreme ray. It meets the same classification wall.

## 6. Corrections and flags carried forward

- EQ2-C: the Spec2 wording (see §1). BP-S itself is scoped correctly.
- EQ2-B:
  - the parametrization map;
  - singular values exist at the pin without a decomposition theorem;
  - the conclusion "Lemma TRANS needs an SVD-type argument" stands, but EQ2-A's Lie-free route supersedes it.
- EQ2-A:
  - x3's false negative, recorded and superseded;
  - "Theorem A′ itself still needs Lie theory" is superseded for the gate case by EQ2-B's N-CLASS route (A did not
    read B, by design).
- My earlier brief: `driveWords3` is not countable (EQ2-B's correction, verified in the kernel).
- `Matrix.PosSemidef.kronecker` is present at the v4.33.0 pin (Analysis/Matrix/Order.lean:213).
