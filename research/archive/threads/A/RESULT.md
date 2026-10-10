# Thread A — successor foundations design: RESULT (design only; nothing frozen, nothing governed)

Script: `threads/A/a_controls.py` (sha256 `446cdeb9…fd6a`). Output: `threads/A/a_controls.out` (sha256 `a98cd728…89f2`),
ending `a_controls: OK -- 90 exact checks (identity 20, witness 40, enumerate 6, sample 24)`. The output is byte-identical
on a second run. Each check is tagged with its kind. `[witness]`, `[identity]` and `[enumerate]` checks are decisive for
the claim they encode. `[sample]` checks are evidence only. `NOTE [written]` lines are written arguments, printed beside
the checks and not counted as checks.

## 1. Finding

Measuring properness relative to Ω repairs the unit-effect defect, and the unit can stay available. An effect `e` is
**proper on Ω** when some `y ∈ Ω` has `e y < 1`. Corrected (SEC) asks for a proper available effect certain at each
boundary state. Corrected (SF) bounds the certain faces of proper available effects only. Under these definitions:

- adding any non-proper effect changes neither predicate;
- Lemma C's proof goes through unchanged;
- with full effects, the 3-ball satisfies SEC, SF and drivability together, so the hypotheses of Lemma C and of
  `strictConvex_of_kInf1` are jointly satisfiable;
- `KInf1(ball, SIC response effects)` changes from trivially true to **false**.

The fix needs two further guards. First, properness must be tested on Ω and not on V. A syntactic test such as
`e ≠ const 1` makes the unit coordinate of every finite stage body proper and certain everywhere, which reproduces the
defect. Second, KINF-1's (SEC) and `StrictConvex` read the boundary from V's topology. Every finite stage body lies in
the hyperplane `v_unit = 1`, and so does the SIC body in simplex coordinates, so neither has interior points. There, (SEC)
fails with full effects for a reason of dimension alone, and the verdicts flip with the choice of ambient space. An
algebraic **boundary state** removes that dependence (`x ∈ Ω` with some `y ∈ Ω` such that `x + ε(x − y) ∉ Ω` for every
`ε > 0`), and with it Lemma C needs neither closedness nor full dimension. On open bodies both predicates hold
vacuously, so every premise must carry compactness.

**A new defect beyond the brief.** The frozen `ElementaryDrivability`, which the KINF-1 result note lists as
unaffected, does not mean what the preregistration says. It asks only that each flow member and `J` map Ω *into* Ω,
does not require the flow to be a group, and compares `J`'s conjugate with the flow on all of V. Exact witnesses show
three consequences:

- the square gbit is drivable (a rotate-and-shrink path from `I` to `−I`);
- the rebit disk is drivable (a contraction `J`);
- the disk embedded in ℝ⁴ is drivable with a `J` that is the identity on Ω.

The square gbit is the built-in countermodel of K-INF-DESIGN §3, and the J-clause exists to exclude the disk. Three
changes repair it: a group flow, `J` an Ω-automorphism, and the off-axis clause compared on Ω.

**Route neutrality.** Given (SEC), (SF) for any family is equivalent to *relative strict convexity* of the body. Each
direction has its own proof (L4 and L5 below). So the ball route's geometric input can be frozen as a property of the
body alone, `RelStrictConvex Ω`. The (SF) route then produces it by Lemma C. A self-duality/homogeneity route can reach
it only together with a capacity-two (rank-two) premise: the real qutrit and the classical trit have symmetric cones and
are not relatively strictly convex.

## 2. Evidence level

| claim | level |
| --- | --- |
| The unit and every effect identically 1 on Ω are not proper; adding them leaves SEC′/SF′ unchanged | written proof (two lines) + exact (`unit.*`, `stage.*`); kernel candidate L6 |
| Syntactic properness (`e ≠ const 1` on V) reproduces the defect on finite stage bodies | exact witness (`stage.unit_coordinate.*`, `cc.syntactic_proper_defeats_SF`) |
| Line extension: a proper effect certain at `x` makes `x` a boundary state; an effect certain at a non-boundary state is 1 on all Ω | exact identity (`line_extension`, `extension_is_affine_combo`) + written proof; kernel candidates L2, L3 |
| Lemma C (algebraic): convex + SEC′ + SF′ ⇒ RelStrictConvex | written proof (KINF-1's proof, with the properness witness passed through) + exact identity (`affine_combo`); kernel candidate L4 |
| Converse: RelStrictConvex ⇒ SF′ for every family | written proof; kernel candidate L5 |
| StrictConvex ⇒ RelStrictConvex (Mathlib bridge) | written proof; kernel candidate L7 |
| RelStrictConvex + full dimension ⇒ StrictConvex; boundary state ⇔ relative-boundary point, in finite dimension | literature: Rockafellar, *Convex Analysis* (1970), Thm 6.4; **not** proposed for the kernel |
| SEC′(full) holds on every bounded convex body in finite dimension | literature: Rockafellar Thm 11.6 (nontrivial supporting hyperplane at every relative-boundary point), rescaled into [0,1] by boundedness; written |
| V-frontier SEC fails with full effects on lower-dimensional bodies (finite stage, SIC body in ℝ⁴) | exact witness (`sic.R4.*`) + written (section 0 (ii)) |
| Square gbit: SF′ fails, RelStrictConvex fails, SEC′(facets) holds, capacity 2 | exact (`sq.*`); SEC′ is decisive by the H-representation |
| Frozen `ElementaryDrivability` holds for the square gbit | exact witness: path determinants `2(t−½)²+½`, convex-combination argument for "into", `N = −I`, `J` translation `(−1,1)` / `(½,−½)` (`sq.frozen.*`, `lean_convention.square`) |
| Corrected drivability excludes the square gbit | exact enumeration `|Aut(square)| = 8` (countercontrol: kite gives 2) + written (a continuous path into a finite set is constant) |
| Frozen J-clause holds for the disk (into-only J) and for the disk in ℝ⁴ (J trivial on Ω) | exact witnesses (`disk.frozen.*`, `disk4.*`) |
| Torus, Stiefel: SF′ fails, RelStrictConvex fails, centrally symmetric, corrected-drivable | exact witnesses (`torus.*`, `stiefel.*`); group law and onto-ness are those of rotation groups (written) |
| 3-ball: SF′(full), SEC′(full), RelStrictConvex, corrected-drivable | exact identity `1 − u·x = |x−u|²/2 + (1−|x|²)/2 + (1−|u|²)/2` + written normal-form argument; exact drivability witness; kernel candidate L8 |
| SIC ball: SEC′(response) fails at every rational sample pure state, holds at the four tangency points; frozen SEC held there through the unit | exact in ℚ(√3) (`sic.*`) + written (`response_eq_one_forces`) |
| Real qutrit: SF fails | exact witness (`rqutrit.SF_fails`); that its cone is symmetric is literature (Faraut–Korányi, *Analysis on Symmetric Cones*, 1994) |

## 3. Countermodels and controls

**What was run against the favourable finding** ("the corrected definitions work"), with maximum skepticism:

1. **Search for other trivializing effects.** Each candidate was checked:
   - constants `c < 1` are proper but have an empty certain face, so they are inert;
   - effects identically 1 on a lower-dimensional Ω but not constant on V are inert under Ω-relative properness, and
     **defeat the fix under syntactic properness** (`cc.syntactic_proper_defeats_SF`);
   - effects certain only off Ω are inert, because the algebraic boundary never leaves Ω (the V-frontier version
     reaches points outside Ω for non-closed Ω);
   - effects that are not effects on Ω are filtered by `IsEffectOn`.
2. **Degenerate bodies** (section 7 of the script):
   - empty and singleton bodies: every predicate is vacuous and drivability is impossible, so these are harmless;
   - **open bodies**: SEC′ and SF′ are vacuous and RelStrictConvex holds. Mathlib's `StrictConvex` behaves the same
     way (`Convex.strictConvex_of_isOpen`), so premises need `IsCompact`;
   - **lower-dimensional bodies**: these break the V-topological versions, as stated above;
   - **unbounded bodies**: SEC′(full) can fail because no proper effect exists (a half-plane), which is the safe
     direction;
   - **infinite-dimensional V**: compact sets have empty interior, and `V →ᵃ[ℝ] ℝ` contains discontinuous maps, so
     the geometric lemmas should carry `[FiniteDimensional ℝ V]`.
3. **The controls the brief names, with the intended verdict for each:**

| body | SEC′(full) | SF′(full) | RelStrictConvex | Drive′ (corrected) | frozen drive | capacity | intended verdict, and why |
| --- | --- | --- | --- | --- | --- | --- | --- |
| square gbit | holds | **fails** (edge) | fails | **fails** (Aut = D₄) | holds (defect) | 2 | excluded by SF and by drivability; KINF-1 excluded it only through the unit |
| torus orbitope | holds | **fails** (disk face) | fails | holds | holds | 2 (Lemma D) | SF independent of drivability, capacity and full effects (§11) |
| Stiefel orbitope | holds | **fails** (disk face) | fails | holds (non-abelian) | holds | 2 | the same, for a non-abelian group |
| 3-ball / Bloch | holds | **holds** | holds | holds | holds | 2 | positive control: the corrected hypotheses are jointly satisfiable |
| SIC ball, response effects | **fails** (holds at 4 points only) | holds (any family, by RelStrictConvex) | holds | holds (as a body) | — | — | `KInf1′(ball, response)` false, `KInf1′(ball, full)` true: K∞-1 is a non-trivial proposition about the family |
| classical bit `[−1,1]` | holds | holds | holds | fails | fails | 2 | SF does not exclude the bit; drivability does |
| classical trit | holds | fails | fails | fails | fails | 3 | — |
| disk (rebit) | holds | holds | holds | **fails** (J normalizes) | holds (defect) | 2 | excluded by the J clause alone, once corrected |
| real qutrit | holds | **fails** | fails | — | — | 3 | a symmetric cone without rank two is not RelStrictConvex |

The SIC row's SEC′ cell is the family's property, not full effects. Its "frozen drive" cell is blank because frozen
drivability was not tested on the SIC body as its own row; as a body it is the 3-ball.

4. **Countercontrols on the script itself** (section 8). Each mutation must give the opposite verdict, and each does:
   - testing properness syntactically, on V, makes SF fail;
   - the ball identity without its `|u|` term is false;
   - the polytope boundary test agrees with a direct ε-extension test, both at the centre and at (1,0);
   - with `J` taken from Aut(square), the conjugate is again linear, so the off-axis witness needs the contraction;
   - full effects are certain where the response effects fail;
   - the automorphism enumeration finds 2 on a kite, not 8.
5. **Not established here.** Corrected drivability's exclusion of the square and the disk rests on written arguments
   (finite Aut; Aut(disk) = O(2) normalizes SO(2)). The kernel checks neither. SEC′(full) on general bodies rests on
   the literature.

## 4. Proposed next theorem

### 4.1 Candidate declarations (Lean text is a candidate only, never built)

Every declaration below is `[FiniteDimensional ℝ V]`-agnostic unless marked. Six are kept from KINF-1 with their text
unchanged: `IsEffectOn`, `certainFace`, `fullEffects`, `PerfectlyDistinguishable`, `CentrallySymmetric` and `CopyNatural`.

```lean
def IsProperOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop := ∃ y ∈ Ω, e y < 1

def IsBoundaryState (Ω : Set V) (x : V) : Prop :=
  x ∈ Ω ∧ ∃ y ∈ Ω, ∀ ε : ℝ, 0 < ε → x + ε • (x - y) ∉ Ω

def SupportingEffectComplete (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ x, IsBoundaryState Ω x → ∃ e ∈ avail, IsEffectOn Ω e ∧ IsProperOn Ω e ∧ e x = 1

def SingletonFaces (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ avail, IsEffectOn Ω e → IsProperOn Ω e → (certainFace Ω e).Subsingleton

def RelStrictConvex (Ω : Set V) : Prop :=
  ∀ x ∈ Ω, ∀ y ∈ Ω, x ≠ y → ∀ a b : ℝ, 0 < a → 0 < b → a + b = 1 →
    a • x + b • y ∈ Ω ∧ ¬ IsBoundaryState Ω (a • x + b • y)

structure ElementaryDrivability (Ω : Set V) where
  flow : ℝ → V ≃ᵃ[ℝ] V
  flow_zero : flow 0 = AffineEquiv.refl ℝ V
  flow_add : ∀ s t, flow (s + t) = (flow t).trans (flow s)
  flow_continuous : Continuous fun q : ℝ × V => flow q.1 q.2
  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω          -- onto follows from flow_add at -t
  t₀ : ℝ
  N_involutive : ∀ x ∈ Ω, flow t₀ (flow t₀ x) = x
  N_moves : ∃ x ∈ Ω, flow t₀ x ≠ x
  J : V ≃ᵃ[ℝ] V
  J_preserves : ∀ x ∈ Ω, J x ∈ Ω
  J_symm_preserves : ∀ x ∈ Ω, J.symm x ∈ Ω
  J_off_axis : ∃ t, ∀ s, ∃ x ∈ Ω, J (flow t (J.symm x)) ≠ flow s x

def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  Nonempty (ElementaryDrivability Ω) → SupportingEffectComplete Ω avail
```

### 4.2 Candidate theorems (layer in brackets)

- **L1** `not_isProperOn_of_eq_one : (∀ y ∈ Ω, e y = 1) → ¬ IsProperOn Ω e`, with the corollary for
  `AffineMap.const ℝ V 1`. *[Lean]*
- **L2** `eq_one_of_certain_of_not_boundary : IsEffectOn Ω e → x ∈ Ω → ¬ IsBoundaryState Ω x → e x = 1 → ∀ y ∈ Ω, e y = 1`.
  *[Lean; proof by `affine_combo` with `(1+ε, −ε)`]*
- **L3** `isBoundaryState_of_certain_proper : IsEffectOn Ω e → IsProperOn Ω e → x ∈ Ω → e x = 1 → IsBoundaryState Ω x`.
  *[Lean]*
- **L4 (Lemma C)** `relStrictConvex_of_supporting_singleton : Convex ℝ Ω → SupportingEffectComplete Ω avail →
  SingletonFaces Ω avail → RelStrictConvex Ω`. *[Lean]*
- **L5** `singletonFaces_of_relStrictConvex : RelStrictConvex Ω → SingletonFaces Ω avail` (any `avail`). *[Lean]*
  Under `Convex ℝ Ω` and `SupportingEffectComplete Ω avail`, L4 gives `SingletonFaces Ω avail → RelStrictConvex Ω` and
  L5 gives the converse. Those are the two direction witnesses for any displayed "SF ⇔ relative strict convexity
  given SEC" (§A.34).
- **L6** `supportingEffectComplete_insert_iff`, `singletonFaces_insert_iff : ¬ IsProperOn Ω u → (P Ω (insert u avail) ↔ P Ω avail)`.
  *[Lean]* This is the KINF-1 defect stated as a theorem.
- **L7** `relStrictConvex_of_strictConvex : StrictConvex ℝ Ω → RelStrictConvex Ω`. *[Lean; continuity of
  `ε ↦ z + ε•(z − y)` at an interior point]*
- **L8** `singletonFaces_closedBall [StrictConvexSpace ℝ V] (x r avail) : SingletonFaces (Metric.closedBall x r) avail`.
  *[Lean; L5 ∘ L7 ∘ `strictConvex_closedBall`]* This is the positive control in the kernel: a two-state body (already
  `Icc (−1) 1 ⊂ ℝ`) satisfies SF with full effects, which the KINF-1 definition made impossible.
- **L9** `not_singletonFaces_square : ¬ SingletonFaces (Metric.closedBall (0 : Fin 2 → ℝ) 1) (fullEffects _)` (sup norm),
  witnessed by `(1 + x 0)/2`. *[Lean]*
- **L10** `not_supportingEffectComplete_unit : ¬ SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) {AffineMap.const ℝ ℝ 1}`.
  *[Lean]* This is the negative control: under KINF-1 the statement was false.
- **Kept from KINF-1, statements unchanged:** Lemma D, Lemma B, `exposed_*`, Theorem F2, `copyNatural_*` and
  `qubit_certain_face`. `strictConvex_of_kInf1` is restated with `RelStrictConvex` as its conclusion.
- **Exact layer (probe):** the table in section 3, from `a_controls.py`, sections 2–9.
- **Written:** corrected drivability excludes the square and the disk. SEC′(full) holds in finite dimension (Rockafellar
  6.4 and 11.6).

### 4.3 Route-neutral geometric slot

The round freezes `RelStrictConvex Ω` as the body-level input of the ball route. It freezes only the SF-route producer
(L4) and the converse (L5). It freezes no self-duality or homogeneity definition. A later round may add a producer
`… → RelStrictConvex Ω` from self-duality, homogeneity and capacity two, or the ball directly, which implies it. The
real qutrit and trit controls fix the scope: without a rank-two premise, no symmetric-cone route reaches the slot.

### 4.4 Preregistration skeleton (one page)

- **Clause.** The round fixes the corrected field-neutral vocabulary and proves L1–L10 and the kept KINF-1 lemmas. It
  sources no premise, decides no effect family, contains no reconstruction theorem, and edits no manuscript or roadmap
  row.
- **Declarations frozen whole:** those in 4.1 and the six kept from KINF-1, plus `FiniteStage`, `exposedPoints`,
  `simplex` and `ClassicallyExposed`. Hazard 5 of KINF-1 is carried over.
- **New hazard: semantic controls before `F`.** Every frozen predicate needs a kernel or exact witness *both* that it
  holds somewhere non-vacuously and that it fails somewhere. These are L8/L9 and L10, and a Lean-level drivability
  witness for the ball if affordable. Review compares each predicate's text with its prose meaning on the unit, a
  lower-dimensional body, an open body and a contraction `J`. This is the check whose absence halted KINF-1.
- **Theorems:** L1–L10, the kept KINF-1 lemmas, the restated `strictConvex_of_kInf1`, and a verdict conjunction.
- **Probe sections:**
  1. the unit and syntactic-properness controls;
  2. the square gbit, with the frozen versus corrected drivability witness;
  3. the torus;
  4. the Stiefel orbitope;
  5. the ball and disk;
  6. SIC, in ℚ(√3);
  7. degenerate bodies;
  8. the route-neutrality controls.

  Exact arithmetic only.
- **Not claimed:**
  - that OI supplies (SEC), (SF), drivability or copy naturality;
  - that `KInf1` holds for any physical family;
  - that `RelStrictConvex` plus transitivity gives a ball in the kernel (Lemma B still needs `frontier ⊆ sphere`);
  - that self-duality is preferred or excluded;
  - that corrected drivability's exclusions are kernel statements;
  - anything for infinite-dimensional V.

## 5. Dependencies

- **Thread D:** the self-duality/homogeneity producer for the 4.3 slot, and whether the rank-two premise can be sourced.
  Nothing here depends on D's verdict.
- **Corpus, read at landed main (`wt-threads`, head `4507b025`):**
  - the K∞ obligations, `verification/ROADMAP.md:995-1010`, and the KINF-1 halt paragraph at `:1012-1014`;
  - the KINF-1 result note and preregistration, `verification/programmes/oi-qm/reconstruction/round-kinf-1-foundations/`
    (prereg lines 179–193 for the frozen definitions);
  - `papers/Main.md:540`, the SIC model;
  - `verification/lean-mathlib/OIBridge/SubstratumSource.lean:77` (`DrivesElementary`);
  - `verification/lean-mathlib/OIBridge/CoherentExtension.lean:183`.
- **Reference, not authoritative:** `wt-kinf1/verification/lean-mathlib/OIBridge/KInfFoundations.lean`. The defects
  are at lines 121–128 (SEC/SF) and 178–188 (drivability: `flow_preserves`, `J_preserves`, `J_off_axis`).
- **Mathlib names assumed, not checked against the pinned version:** `strictConvex_closedBall` (seen in the local
  reference copy `mathlib-ref/StrictConvexSpace.lean:75`) and `Convex.strictConvex_of_isOpen` (`mathlib-ref/Strict.lean:105`).
- **Unsourced premises carried:** compactness and finite dimension of the body; the written drivability exclusions;
  the literature theorems Rockafellar 6.4/11.6 and Faraut–Korányi.
