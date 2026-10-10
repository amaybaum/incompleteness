# D-LEDGER — Thread D: where composite closedness comes from (off-repo research ledger)

Status: one depth-first pass, complete for this pass. The §A.31 fixed point is **not** reached (§6).

## 0. Base, scope, evidence layers

- **Base.** `wt-06b` at `06b6f94e479bc19a28979c72316823cbdd0fb62b` (`git rev-parse HEAD`). Read-only:
  `git status --porcelain` printed nothing at the end of the pass. The only git commands run were `rev-parse`,
  `status`, `log --oneline` and `diff --stat 68b6df06 HEAD -- OIBridge/`. That diff adds one file, `SharpTests.lean`
  (K1-SHARP-TESTS-1), and changes nothing else. So every file:line that K2C and AC cite in `CompositeDimension`,
  `K2Guard`, `CompositeInterface`, `StageCompletion`, `CompletionAction` and `TransitiveBody` is still valid. The
  citations used here were re-read at the base. Every write is under `scratchpad/dthread/`. Paths are relative to
  `verification/lean-mathlib/OIBridge/`.
- **Scope.** Ungoverned research. Nothing here is adopted, frozen or certified, and no ROADMAP or manuscript wording
  is proposed. Every named hypothesis is a premise.
- **Layers.** They are kept distinct, and none substitutes for another.
  - `[K]` kernel declaration at the base (file:line).
  - `[R]` a reading of what a landed proof consumes.
  - `[X]` exact computation (sympy rationals, Gaussian rationals, `Fraction`). Kernel tables are parsed from the
    Lean source.
  - `[M]` exact computation in the matrix model (dictionary `w_{μν} = Tr((σ_μ⊗σ_ν)ρ)`): evidence about QM, not
    about the kernel.
  - `[W]` written argument.
  - `[L]` literature-standard fact, not re-proved.
  - `[P]` prior off-repo research used as data: K2C, AC, K2 (k2d), SA, P ledgers.
  - `[S]` uncompiled Lean sketch. There is no toolchain here.
- **Prior ledgers read, not edited.** K2C (G3 / AW-K2C-2, node 3e `K_d`, node 3c `U`), AC (AC-3 / AW-AC-2, N3.1–N3.3,
  N2.1–N2.3), K2 (D6, T7, P3.c), SA (K2-a…K2-d), P (G-P11).

## 1. Question 1 — is composite closedness DERIVABLE from landed completion machinery?

### 1.1 Inventory of the landed completion and closure objects (P1, 24/24, `[K]` with mechanical file:line evidence)

| object | file:line | what it closes | topology | composite-level? |
|---|---|---|---|---|
| `CSpace D := lp (fun _ : Label D => ℝ) ∞` | StageCompletion:128 | carrier of one tower's completed states | **sup norm** of ℓ^∞ over stage labels | no (one `DirectedStages`) |
| `body D := closure (convexHull ℝ (range (prepVec D)))` | StageCompletion:141–142 | **states** of one tower (CMP-1) | sup norm | no |
| `body_subset` (a closed convex condition true on the preparations holds on the body) | StageCompletion:171 | — (the extension principle) | sup norm | no |
| `stageEffects := range (coord D)` | StageCompletion:176 | effects are **not** closed; the coordinate functionals only | — | no |
| `body_isClosed` | CompletionAction:202 | states | sup norm | no |
| `mapsTo_chartBody` (an affine extension of data on the generators maps the whole chart body into itself) | CompletionAction:286, closedness consumed at :295 | **invariance from generator data, via closedness** | chart (finite-dim) | no |
| `OpDatum.τ : Prep D → CSpace D`, `mem_body` | CompletionAction:46–48 | operations are **not** completed. The codomain admits limits, but no theorem produces them (AC `[P]`) | — | no |
| `chartBody_isClosed`, `chartBody_isCompact`, `chartBody_interior_nonempty` | TransitiveBody:84, :109, :121 | states, in the chart of a `FiniteRank` body | chart | no |
| `MulClosed`, `idDatum`, `ord1_core` (ORD-1) | CompositionOrder:63, :228 | **algebraic** composition closure of operation data on **one** tower (header :2–5: "iterated operation data") | none | **no**. "Composition" here means sequential composition, not composite systems |
| `Quasilocal ι Q := UniformSpace.Completion (localAlg ι Q)`, `closure_iUnion_stage`, `quasiState_unique` | QuasilocalAlgebra:625–626, :712, :879 | the **observable algebra** (C*-norm completion) and states as continuous functionals | C*-norm | composite regions `S × R`, but at matrix level (`Matrix … ℂ`, :165, :418). The composite state space there is the complex PSD set, which presupposes the conclusion K2 is meant to reach |
| `DenseUnitaryControl`, `ChanWithin`; the convention "dense availability is never identified with exact availability" | DiscreteCompletion:13 and §A | **operations**, matrix level, operator norm | operator norm | matrix-level only |
| `CompletedOI`, `MonoidalCompletion`, `TypedCompletion` | headers | "completion" in the sense of completion *principles* | none | no topological content |
| COMP-1 `ProductData` / `PreComposite` / `Composite` | CompositeInterface:210 / :223–230 / :243–246 | fields `prodState…prodEff_apply` / `Ω, convex, prod_mem, prodEff_effect, prodEff_unit` / `lt`. **No closedness, compactness, continuity or boundedness field** | none | yes, but nothing completes it |
| COMP-1 consumers | — | **none**. No module outside CompositeInterface names `PreComposite`, `minPre`, `maxPre` or the `Composite` instances (P1 b). EffectSpace:50, K1Bridge:39, K2Guard:38 and SharpTests:34 only `open` the namespace | — | — |
| COMP-1 disclaimer | CompositeInterface:54–55 | "The stage-level product of two `DirectedStages` and the bridge from completed product towers to this interface are not part of this module" | — | — |
| joint tower / product of `DirectedStages` | — | **absent**. No declaration takes two `DirectedStages` (P1 c) | — | — |
| DIM-1 `maxCone`, `jointStates`; K2-GUARD-1 `CandidateCone` | CompositeDimension:186, :190; K2Guard:95 | no closedness clause. No `IsClosed (maxCone …)` or `IsClosed (jointStates …)` theorem exists (P1 e). `CandidateCone` has neither a closedness nor a convexity clause | — | composite-level, not completed |

Outside these modules, every topological `closure`/`IsClosed` in code lines is matrix-level: OrbitReachability,
PositiveReachability, QuasilocalAlgebra, QuasilocalCharacterization, ReachabilitySeam, SecondOrderLayer and
SwapLayer (P1 d). CompositeInterface:775 is the factor simplex, and OrbitNormalization:139 is a single-system lemma.

**Verdict 1 (`[K]` + P1).** No landed completion construction is applied to any composite-level object.
- CMP-1, OPACT-1 and TRB-1 close the **state set of one directed tower**.
- ORD-1 is not composite-level.
- The quasilocal completion is composite-level, but only at matrix level, where closedness is inherited from the
  complex PSD cone and so presupposes the target.
- COMP-1's body is not closed by any field or theorem, and no theorem consumes COMP-1.

Closedness of the composite body is therefore **not derivable from landed objects**.

### 1.2 The conditional derivation: what *would* make closedness inherited

The single-system body is closed **by definition** (SC:141). The same definitional choice, applied to a joint tower,
makes composite closedness a theorem. That is the whole sense in which it can be "inherited". Here is the chain, with
each link labelled.

| link | statement | layer |
|---|---|---|
| J1 | a joint tower `D_AB : DirectedStages` with SC∞, containing product preparations with product tables, whose factor marginals are the factor towers | **not landed** (CI:54–55; P1 c) |
| J2 | stage-level test locality in bilinear form: finitely many product labels `ℓ_{μν}` (16 at d = 3), and each label's value on every stage preparation is a fixed affine combination of the `val ℓ_{μν}` | **premise** (LT plus product-effect bilinearity, read on the tower; K2 D6 `[P]`) |
| J3 | J2 holds on the whole completed body: each relation is an equality of continuous functionals (`evalCLM` SC:151), so a closed convex condition, extended by `body_subset` SC:171 | `[K]`-cheap (not landed) |
| J4 | the reading `r := (coord ℓ_{μν})` is injective on `body D_AB` (J3). **Lemma: an affine map injective on a convex set is injective on the direction of its affine span.** Hence `FiniteRank (body D_AB)` with dimension ≤ 15 | `[W]` + P3.1 (40 exact constructive instances; non-convex countercontrol P3.2) |
| J5 | `CompletionChart` exists, and `chartBody` is closed and compact | `[K]` CA:154, TB:84, TB:109 |
| J6 | `r(body) = (r ∘ chart)(chartBody)` is a continuous image of a compact set, so compact, so **closed** in `W 3` | `[W]` (Mathlib `IsCompact.image`) |
| J7 | `Ω := r(body)` is a PreComposite over the **completed** factor bodies: convex (linear image); `prod_mem` for limit factor states by J6 plus continuity of `prodState` (P4.3); `prodEff_effect`/`unit` from the stage values by `body_subset` | `[W]` |

Conclusion of the chain: `IsClosed Ω`, with no closedness premise. Two links are load-bearing, each shown by its own
countermodel.
- **J4 (finite rank) is load-bearing for J6 under CMP-1's sup-norm topology (P3.3, `[X]` truncations + `[W]`).**
  - Realise the graph of the c₀ unit ball, `{((1+f(x))/2, ((1+x_n)/2)_n)}` with `f = Σ 2^{-n} x_n`, as a CMP-1 body.
    The preparations are rescaled finitely supported rational points; the labels are the coordinates plus a unit; SC∞
    is trivial.
  - The body is sup-norm closed, convex and bounded. Its reading through the single label `f` is the open interval
    (0, 1).
  - The maximum on the N-cube is `1 − 2^{-N}` exactly (N ≤ 24). The value 1 forces `x = all-ones`, which is not in
    c₀.
  - So "closed in `CSpace`" does not survive projection to finitely many tests without finite rank.
  - The pointwise (probability) closure would contain the all-ones point. On bounded sets it is compact
    (Tychonoff), and it would make every finite reading closed unconditionally.
- **J1 is where the content lives.** Applied to the **product** tower (preparations `P_A × P_B`, product table), the
  chain gives the minimal body of the completed factors.
  - That body is closed and compact (`[W]`), and it is not gate-invariant: `f = ω00 − ω11 + ω22 − ω33 ≥ 0` on every
    product (symbolic), `f(phiW) = −2` (P4.2).
  - Closedness obtained this way is cheap. What decides the body is which joint preparations the tower carries,
    i.e. gate and local operation data on `D_AB`.

**Pressure test (this branch is favourable, so maximum skepticism).**
- (a) The "derivation" is definitional. Closedness is `isClosed_closure` (CA:202), applied to a tower that does not
  exist. It is a relocation, not a source.
- (b) It needs J2. J2 is the unsourced LT/PTQ content of K2. It is stated at stage level and extends to limits for
  free (J3), and that extension is the only genuinely free step.
- (c) The topology is a hidden choice. CMP-1 uses the sup norm. Under finite rank all candidate topologies agree on
  the span. Without it they differ (P3.3, AC-10 `[P]`).
- (d) OPACT-1's `mapsTo_chartBody` (CA:286–297) is the exact single-system template of K2C's G3: closed body plus
  data on the generators gives invariance of the whole body. On a joint tower it would transfer verbatim. **Read
  this way, closedness converts invariance of the preparation set into invariance of the body. It does not supply
  the invariance.**

## 2. Question 2 — the minimal independent premise

The setting is the downstream consumer: dense-countable cone pinning (K2C node 3e, sketch `eq_Q3_of_dense`). Write
`D` for the rational rotations `R(q)`, `q ∈ ℚ⁴∖0`. Every rational rotation has this form: `q_i q_j/|q|² ∈ ℚ` gives
`q ∝` a rational vector `[W]`. Write `G_D := ⟨cnot, actT R, actC R : R ∈ D⟩` and `K_d := cone conv(G_D · products)`.

### 2.1 The structure of the admissible class (`[W]` from P2 ingredients; the central new fact)

Let `𝒦` be the class of convex `G_D`-invariant candidate cones (`CandidateCone`, K2Guard:95, plus convexity).

1. **Upper bound, no closedness needed.**
   - If `ω ∈ K ∖ Q3`, some `g ∈ G` sends `ω` outside `maxCone` (K2C `U↑`). The set `{g : gω ∉ maxCone}` is open and
     nonempty, and `G_D` is dense in `G`, so a rational word does it.
   - Exact instance with a **rational** word (P2.7): `ω = (16/25)Id − P_ψ` with `ψ = (4|00⟩+3|11⟩)/5`.
     - `ω` is not PSD: its eigenvalue is −9/25.
     - `g = actC R_y ∘ cnot`, with `R_y = [[7/25,0,−24/25],[0,1,0],[24/25,0,7/25]]`, gives value −9/25 on `g ω`.
     - Countercontrol: the same word gives value 1 on `P_ψ`.
   - So every `K ∈ 𝒦` satisfies `K ⊆ Q3`.
2. **Lower bound.** `K ⊇ K_d` (products, convexity, `G_D`-invariance).
3. **Closure.** `cl K_d = Q3`.
   - `cl(G_D · pure products) = G · pure products`, which is all pure states by K2C transitivity.
   - `cl K_d` is a closed convex cone, so it contains `Q3`. It is contained in `Q3` because `Q3` is closed.
4. **Hence `𝒦 = { K : K_d ⊆ K ⊆ Q3, K convex, G_D-invariant }`, and within `𝒦`:**
   `IsClosed K ⇔ K = Q3 ⇔ K ⊇ cl(K_d) ⇔ ext-closedness (cl(pure states of K) ⊆ K)`.
   - Every non-closed member lies in `[K_d, Q3)`.
   - Within `𝒦`, closedness carries the **entire** residual content of the identification. It is not a technical
     add-on.
5. **Same closure-invariant structure.** Every `K ∈ 𝒦` has `cl K = Q3`, `int K = int Q3` (Rockafellar Thm 6.3
   `[L]`, with `int K_d ≠ ∅` by P2.6: 16 rational products span `W 3`, exact rank 16), and dual cone
   `K* = (cl K)* = Q3* = Q3`.
   - So every member has **the same effect cone** and **the same full-rank states**. The members differ only on
     rank-deficient boundary states.
   - Exact interior control: the entangled full-rank Werner(1/2) state `= (cnot(prodState xplus z3) + prodState 0 0)/2`
     lies in `K_d`. The field-neutral witness `F = (w00+w11−w22+w33)/4` is ≤ 1/2 on products (symbolic) and equals
     5/8 on it (P2.8).
   - `cl K` is `G_D`-invariant and closed, so it is `G`-invariant (linear maps are continuous). **No non-closed
     member of `𝒦` has a different closure-invariant structure.**

### 2.2 The candidate premises compared

| candidate | implied by / implies | field-neutral | finite QM satisfies it | does the downstream job |
|---|---|---|---|---|
| (a) `IsClosed Ω` (body, in `V`) | ⇔ (b) when Ω is bounded and lies in the hyperplane `unit = 1` (`prodEff_unit` CI:230); ⇔ (c) under LT; ⇐ (d) | yes | yes: `Q3 = ρ⁻¹(PSD)`, ρ a linear bijection (P4.4 `[X]`), PSD closed `[L]` | yes, and within `𝒦` it is ⇔ the conclusion |
| (b) cone closed only | (b) ⇒ (a) whenever the unit pairing is continuous, which holds on a finite-rank body (D-2): Ω = cone ∩ {unit = 1}. (a) ⇒ (b) needs a bounded body. Bounded for two balls: `|ω_{μν}| ≤ 1` on the joint-state slice (P3.5a, exact identities). Countercontrol: the padded maximal body is unbounded in height (P3.5b) | yes | yes | same as (a) for a Composite on compact factors |
| (c) sequential closedness in the probability topology (initial topology of the product-effect values) | sequential = closed in finite dimension. ⇔ (a) on `aff Ω` under LT, because LT plus the J4 lemma make the reading injective on a finite-dimensional span. **Differs without LT**: in the padded control, `(ω₀,0)` and `(ω₀,1)` agree on every product effect, so the norm-closed `P.Ω × [0,1]` has probability-closure `P.Ω × ℝ` (P3.4; `[K]` CI:843, :885) | yes | yes | same as (a) under LT |
| (d) "the composite is the completion of its finite-stage joint states": `Ω = cl conv(joint stage states)` | ⇒ (a). (a) does not give (d), because (d) also fixes which states. The **containment** form (d⁻) `Ω ⊇ cl conv(joint stage states)` is weaker than (a) for bodies that contain the stage states | yes | yes: QM states are the closure of the Gaussian-rational states `[L]` | (d⁻) with stage states `= G_D · products` does it, and is the **weakest** premise found |

**Answer 2.**
- The weakest closedness-type premise found is (d⁻): the composite body contains every limit of its finite-stage
  joint states. It is strictly weaker than (a) in general.
- On the admissible class `𝒦`, (a), (b), (c), (d) and (d⁻) all coincide, and each is equivalent to `K = Q3`.
- All are field-neutral, and finite QM satisfies all of them (reverse direction).
- (a)–(c) separate only off the class: an unbounded body for (b), and failure of LT for (c).

## 3. Question 3 — failure countermodels

| claim refuted | countermodel | layer |
|---|---|---|
| convexity alone pins the composite body | `ball3MinComposite ≠ ball3MaxComposite`. Both are kernel `Composite`s on two balls (CI:807, :811), and `phiW ∈ max ∖ min` (P4.2) | `[K]` + `[X]` |
| convexity is unneeded given full G-invariance | `K_nc = ℝ≥0·(G·products)` | K2C P5.3 `[P]` |
| invariance under a dense countable family plus convexity pins it | **`K_d` with an explicit missing pure state** `ψ* = (1, e^{√2}, e^{√3}, e^{√5})`. Details below the table | `[X]` + `[W]` + `[L]` (Lindemann–Weierstrass) |
| a non-closed dense-invariant body can have a different closure-invariant structure | **no**: §2.1 item 5 (same closure, interior and dual; `cl K` is G-invariant) | `[W]` + `[L]` + P2.6, P2.8 |
| closedness of the factor bodies transfers to the composite | `Ω' := SEP-slice ∪ relint(jointStates)`, and also `K_d`'s slice. Details below the table | `[X]` + `[W]` + `[L]` |
| the completion of the composite is the composite of the completions | **product tower:** its completion is the minimal body of the completed factors (closed, not gate-invariant, P4.2). **Joint tower:** contains the composite of completions only through joint closure (P4.3, below) | `[X]` + `[P]` AC |

The `K_d` countermodel (third row):
- Each `G_D` element is `Ad V` with `V ∈ GL₄(ℚ(i))` up to scalar:
  - P2.2: `U~_q` has entries in `ℤ[i]`; `Ad(I⊗U~_q)/|q|² = actT R(q)` and `Ad(U~_q⊗I)/|q|² = actC R(q)` exactly;
  - P2.1: the parsed `cnot` is `Ad(CNOT)`.
- A pure state of `K_d` is `∝ V(a⊗b)`, by extremality of rank-1 in the PSD cone `[L]`. So `ψ ∈ K_d` iff
  `Q_V(ψ) = Segre(Vψ) = 0` for some word `V`.
- `Q_V(1,X,Y,Z)` is a nonzero polynomial over `ℚ(i)`. All 819 words of length ≤ 3 over 9 letters were checked
  (rank-4 forms, nonzero dehomogenisation, P2.3). `[W]` for all words: `V` is invertible.
- `e^{√2}, e^{√3}, e^{√5}` are algebraically independent `[L]`. The ℚ-independence hypothesis is checked exactly by
  `[ℚ(√2,√3,√5):ℚ] = 8` (P2.4c). Hence `Q_V(ψ*) ≠ 0` for every `V`.
- `ψ*` is entangled: `Segre(ψ*) = e^{√5} − e^{√2+√3} ≠ 0`, since `√5 ≠ √2+√3` exactly (P2.4a–b).
- So `P_{ψ*} ∈ Q3 ∖ K_d`.
- Controls (P2.5):
  - the Schmidt family `(1,0,0,t)` is sent to products by CNOT for **every** `t`, so one transcendental is not
    enough;
  - the twisted cubic is a product;
  - `phiW ∈ K_d` is entangled and pure, so `K_d` does contain entangled pure states.
- **This strengthens K2C node 3e** (`[W]`, "no explicit missing pure state is exhibited") **to an explicit point.**
- `K_d`'s normalised slice is a full COMP-1 `Composite` on `modelData` (lt by `modelData_ext` CI:740).

The `Ω'` countermodel (fifth row):
- `idW` lies on the relative boundary of `jointStates`: the product of sharp effects at `x` and `−x` takes the value
  `(1−|x|²)/4 = 0` (P4.1b).
- `idW` is not separable: the singlet functional is `(1 − x·y)/4` on products and −1/2 on `idW` (P4.1c).
- `idW` is a limit of relative-interior points (segment to the centre, P4.1d identity; line-segment principle
  `[L]`).
- So `Ω'` is convex, contains the products, lies in `maxBody`, satisfies `lt` on the model carrier, and **is not
  closed** on two compact balls.

The joint-tower half of the last row:
- In AC's 3/5 tower no reduced word of length ≤ 8 sends `e_z` to `−e_z` (13120 words), while `xxzXZxx` gets within
  squared distance `16/78125` (P4.3a–b). Torsion-freeness `[P]` AC N2.1–N2.3.
- `sharp(−e_z)⊗sharp(e_z)` reads `(1−u₃)(1+v₃)/4` on `prodState u v`. It equals 1 only at `(−e_z, e_z)` (P4.3c).
- So `prodState(−e_z, e_z)` is outside the stage-product hull and inside its closure. `prod_mem` over the completed
  factor (CI:227) holds only for the closed hull.

## 4. Question 4 — the K2-GUARD-1 obstruction and the cone-uniqueness sketch: what changes

| statement | consumes closedness? | if closedness is **derived** (J1–J7) | if closedness is **assumed** (a premise on the body) |
|---|---|---|---|
| `no_candidateCone_cnot_reflY` | **no** (one finite chain; `CandidateCone` K2Guard:95 has no closedness or convexity) | unchanged | unchanged |
| K2C control-copy and one-rotation corollaries | no | unchanged | unchanged |
| reflection in the closure of a raw family | — | `det` is continuous and `{det = −1}` is clopen, so closure adds no reflection (AC N3.4 `[P]`). Unchanged | unchanged |
| K2C `U↑` (`subset_Q3_of_rotInvariant`) and its dense form | no (§2.1 item 1, rational word P2.7) | unchanged | unchanged |
| K2C `U↓` with **exact** SO(3)² | no. Closedness is then a **consequence** (`K = Q3`, closed) | unchanged | the premise is redundant |
| K2C `eq_Q3_of_dense` (`hcl : IsClosed K`) | **yes**. Within `𝒦`, `hcl ⇔ K = Q3` | `hcl` becomes a lemma about the bridged body. The theorem's premises move to J1/J2, and to joint `OpDatum`s whose invariance on the body comes from `mapsTo_chartBody`'s pattern (CA:286). The `D`-invariance clause of the body is then derived from data on preparations | `hcl` carries exactly the gap `[K_d, Q3)`. Nothing else in the hypothesis list discriminates inside that interval |
| K2 T7 `compose_elementary` (`hLie`) | through A6 | a raw dense lifted family suffices, given the bridged closed body (AC-3 `[P]`) | same, with `hcl` added to the list |
| DIM-1 selectors `dim_of_nativeGate`, `three_of_nativeGate` (CD:2723, :2748) | no (`maxCone` is only a target). `Entangling` holds inside `K_d` (`phiW`, P2.5c) | unchanged | unchanged |
| COMP-1 laws L1–L11 | no | unchanged | a `Closed` field would be independent of the other nine, since `Ω'` and `K_d` satisfy them all |

## 5. Gem-finding (§A.31)

**Productivity test.** A finding is a gem iff it is strictly stronger than the K2C G3 / AC-3 restatement ("a dense
route needs a closed composite body; COMP-1 has no closedness field") **and** it constrains an obligation or exposes
a hidden assumption. In this pass the test is written into the ledger after the probes ran, as K2C and AC also did.
That order is recorded here.

| id | finding | class | layer |
|---|---|---|---|
| D-1 | **Within the dense-countable class, closedness is equivalent to the identification itself, and operationally invisible.** `𝒦 = [K_d, Q3]`, and `IsClosed ⇔ = Q3 ⇔ ⊇ cl K_d`. Every member has the same closure, interior and dual (effect) cone; they differ only by missing rank-deficient states. There is an explicit missing pure state `ψ* = (1, e^{√2}, e^{√3}, e^{√5})`. **Hidden assumption exposed:** "closed body" in AW-K2C-2 reads like regularity, but here it is the whole remaining content, and no finite-precision statistic can detect it. **Pressure test:** the equivalence uses K2C's `U↑`, whose dense form was re-checked here with a rational word (P2.7). The interior equality needs finite dimension (`W 3`) and `int K_d ≠ ∅` (P2.6). LW is `[L]`; without it the missing point is only measure-theoretic (K2C). The finding is not favourable to the framework. It sharpens what an unsourced premise must carry | **NEW** | `[W]` + `[X]` P2 + `[L]` |
| D-2 | **Inheritance from CMP-1 is definitional, and survives projection only through finite rank.** A composite body defined as the bridged CMP-1 completion of a joint tower is closed with no closedness premise, by J1–J7. The step "closed in `CSpace`" to "closed in `W 3`" needs FiniteRank, which LT supplies through the lemma (injective on convex ⇒ injective on the span direction, P3.1/3.2). The c₀ countermodel (P3.3) shows that the sup-norm completion fails without it, while the pointwise completion would not. **Hidden assumptions:** (i) the topology of the completion: sup norm vs probability; (ii) LT ⇒ finite rank. Corollary `[W]`: every COMP-1 `Composite` on compact factors has `dim aff Ω ≤ (dA+1)(dB+1) − 1` and a bounded body, in any `V`, via `prodEff_eq_of_eff_eq` CI:342. So "closed" is unambiguous for Composites, though closedness itself is not implied (`Ω'`, `K_d`) | **NEW** | `[W]` + `[X]` P3 + `[K]` |
| D-3 | **The composite of completions is not the completion of the composite.** The product tower's completion is the minimal body (closed, not gate-invariant). Over completed factors, a joint tower satisfies `prod_mem` only through joint closure (3/5 tower, exact). Closedness from completion is cheap; which joint preparations exist is the content | ELABORATING (sharpens K2 D6 and AC-3) | `[X]` P4.2–4.3 + `[W]` |
| D-4 | **Exact continuous local actions make closedness a consequence.** `U↓` with all of SO(3)² gives `K = Q3`, which is closed. A closedness premise is needed only in the countable regime. Closedness and exact continuous availability are alternative premises, and closed + dense recovers the continuous invariance | POSITIVE | `[W]` (K2C U) |
| D-5 | **OPACT-1 already contains the single-system form of the trade-off.** `mapsTo_chartBody` (CA:286–297) turns generator data into whole-body invariance by consuming `body_isClosed` (CA:295). The composite version would reuse it verbatim on a joint tower | POSITIVE | `[R]` |
| D-6 | Closedness of the factor bodies does not transfer: `Ω'` is a locally tomographic Composite on two compact balls with a non-closed body. The minimal and maximal bodies of compact factors are closed (`[W]`; no kernel lemma) | CONFIRMING (AW-K2C-2, AW-AC-2) with an exact instance | `[X]` P4.1 + `[W]` |
| D-7 | Body-closed, cone-closed and probability-closed coincide for Composites on compact factors, and separate only without LT (padding) or without boundedness | ELABORATING | `[X]` P3.4–3.5 + `[W]` |
| D-8 | K2-GUARD-1, `U↑` and the DIM-1 selectors consume no closedness. The orientation obstruction is closure-invariant | CONFIRMING (K2C, AC N3.4) | `[K]` + `[P]` |
| D-9 | **Naming trap.** ORD-1 `CompositionOrder` is sequential composition of operation data on one tower (CO:2–5, :63), not a composite-level object. The quasilocal completion is composite-level only at matrix level | CONFIRMING (inventory) | `[K]` P1 |

**Cross-propagation markers.**
- **AW-D-1.** Any premise or sourcing round that targets composite closedness on a countable-family route carries
  the full cone identification within `𝒦`. It should be stated as such (for example as the containment (d⁻)), not
  as regularity.
- **AW-D-2.** Any bridge from a joint tower to COMP-1 must fix the completion topology. With CMP-1's sup norm it needs
  finite rank, which LT in bilinear form supplies. Bears on K2, K∞-Stage (FiniteRank) and COMP-1.

## 6. Verdict and fixed point

- **Derivable?** **Not from landed objects** (`[K]`, P1). No landed completion is applied to any composite-level
  object. Closedness **is** derivable, by the definitional route `isClosed_closure`, from a not-landed joint tower
  with stage-level bilinear test locality (J1–J7: `[K]` links J3/J5, `[W]` links J4/J6/J7, exact controls P3).
  Finite rank is load-bearing for the sup-norm completion (P3.3).
- **Minimal premise.** (d⁻): the body contains the limits of its finite-stage joint states. It is weaker than
  closedness in general. On the admissible class all closedness-type premises (a)–(d⁻) coincide with `K = Q3`. All
  are field-neutral, and finite QM satisfies all of them.
- **Countermodels.** All exact or written with exact ingredients:
  - convexity alone: min ≠ max (`[K]`);
  - dense countable invariance plus convexity: `K_d` with explicit `ψ*` (`[X]` + `[L]`);
  - factor closedness does not transfer: `Ω'` (`[X]` + `[W]`);
  - product-tower completion = minimal body (`[X]` + `[W]`).
- **Fixed point.** Not reached: two NEW findings (D-1, D-2). The next pass should:
  - attempt a closedness-free alternative to (d⁻), for example a premise on the effect side. D-1 suggests none
    exists, because the effect cone is identical across `𝒦`;
  - check whether the pointwise completion of CMP-1 changes any landed single-system theorem;
  - state the J4 lemma and `Composite.finiteRank` as kernel targets.
- **§A.23.** Consistency-axis work only. Bands unchanged.

## 7. Probe log

Every probe was run from `scratchpad/dthread/` as `python3 -I <script> <args>`, with
`W=../wt-06b/verification/lean-mathlib/OIBridge`. Each was run, then rerun into `replay/`, and `cmp` reported every
output **byte-identical**. Hashes are the first 16 hex digits of sha256. Floats appear only in display strings.

| probe | command | script | output | result |
|---|---|---|---|---|
| helpers | — | `dlib.py` `9ac4ed345a19fb35` | — | — |
| P1 inventory | `p1_inventory.py $W` | `095f0e9437b85dc4` | `p1_out.txt` `3684ed12efdb7fc5` | 24/24, `VERDICT NO-LANDED-COMPOSITE-COMPLETION` |
| P2 interval | `p2_interval.py $W/CompositeDimension.lean` | `7878f1666652742e` | `p2_out.txt` `11f101009c35fe07` | 19/19, `VERDICT INTERVAL-INGREDIENTS-EXACT` (~15 s) |
| P3 bridge steps | `p3_rank_topology.py 7` | `b2cd7e9ec4732b4f` | `p3_out.txt` `53e32a33cf23a297` | 6/6, `VERDICT BRIDGE-STEPS-EXACT` |
| P4 transfer | `p4_transfer.py $W/CompositeDimension.lean 8` | `62b79f0288daf1b8` | `p4_out.txt` `1f31846038a64db1` | 9/9, `VERDICT TRANSFER-FAILS-EXACT` |

**Run history (recorded, not hidden).**
- **P1 run 0** (`p1_inventory.run0.py` `b7218adcc0ea8618`, `p1_out.run0.txt` `b18892e04ab6f119`) printed
  `VERDICT INVENTORY-CONTRADICTS-PREMISE`, with 1 failure in check `d.closure-scope`.
  - Cause: the regex read comments and identifiers such as `subset_closure (` and "ancilla closure (".
  - The hits were inspected. They are algebraic closures (`Submonoid`/`Subgroup`/`AddSubgroup.closure`), prose, and
    matrix-level topological closures.
  - The check was rewritten to read code lines only and to classify each module as matrix-level or real-carrier. The
    decision rule's intent ("only single-tower state closures on real carriers") is unchanged, and the rule text in
    the docstring was not edited. This is a probe defect, not a result. It is kept as evidence.
- **P3.** Before the first full run, four items that passed by construction (`True`) were converted:
  - 3.3b became a `[W]` note;
  - 3.4 and 3.5b became literal definitional instances, labelled as such;
  - 3.3c and 3.3d are printed as "[tautological, not counted]".
  The count fell from 10 to 6.
- **P4.** 4.3c (a field-neutral extremality certificate) was added after the first run, replacing a written appeal
  to extremality. 4.1d checks an identity only.
- **Load-bearing points left unchecked by computation:**
  - Lindemann–Weierstrass;
  - Rockafellar 6.3;
  - extremality of rank-1 in the PSD cone;
  - the open-set density step of `U↑`;
  - Carathéodory compactness of the minimal body;
  - the c₀ realisation as a tower;
  - J4/J6/J7 as stated in general;
  - block-positivity of `(16/25)Id − P_ψ` (`[L]`: the largest Schmidt coefficient squared is 16/25).

## 8. Lean sketches (UNCOMPILED; names indicative; `sorry` = `[W]`)

```lean
-- J4: injective on a convex set ⇒ injective on its direction
theorem injOn_direction_of_injOn_convex {E F : Type*} [AddCommGroup E] [Module ℝ E] [AddCommGroup F]
    [Module ℝ F] {K : Set E} (hK : Convex ℝ K) (r : E →ᵃ[ℝ] F) (hinj : Set.InjOn r K) :
    ∀ v ∈ (affineSpan ℝ K).direction, r.linear v = 0 → v = 0 := sorry
-- D-2 corollary for COMP-1 (compact factors ⇒ finite rank, any V)
theorem Composite.finiteRank {ΩA ΩB V} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (C : Composite ΩA ΩB V) (hA : IsCompact ΩA) (hB : IsCompact ΩB) :
    StageCompletion.FiniteRank C.Ω := sorry   -- via prodEff_eq_of_eff_eq (CI:342) and the lemma above
-- J6
theorem isClosed_image_body {D : DirectedStages} (C : CompletionAction.CompletionChart D) {k : ℕ}
    (r : CSpace D →L[ℝ] (Fin k → ℝ)) : IsClosed (r '' StageCompletion.body D) := sorry
    -- (chartBody_isCompact C).image, using hspan to rewrite body as chart '' chartBody
-- D-1, within the dense class (two directions separately, §A.34)
theorem eq_Q3_of_isClosed_dense {K} (hK : CandidateCone K) (hc : IsConvexCone K) (hD : DInvariant K)
    (hcl : IsClosed K) : K = Q3 := sorry
theorem isClosed_of_eq_Q3 {K} (h : K = Q3) : IsClosed K := sorry   -- Q3 = certW⁻¹(PSD), closed
theorem subset_Q3_of_dense {K} (hK : CandidateCone K) (hD : DInvariant K) : K ⊆ Q3 := sorry  -- no closedness
-- countermodels
theorem exists_nonclosed_composite_ball3 :
    ∃ C : Composite ball3 ball3 (Model.Carrier 3 3), ¬ IsClosed C.Ω := sorry   -- Ω' or K_d slice
```

## 9. Not decided here

- No OI construction supplies a joint tower, J2, or gate-generated joint preparations.
- Whether the pointwise completion should replace the sup-norm one. That is an owner question about K∞-Stage, and
  no wording is proposed.
- Whether a closedness-free, effect-side premise can select `Q3` in the countable regime. D-1 is evidence against
  it, since every member of `𝒦` has the same effect cone.
- Every negative statement is scoped to the constructions tested: the rational-quaternion family `D`, the 3/5 tower,
  the c₀ tower, `Ω'`, and the padding control.
