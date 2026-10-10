# AC-LEDGER — thread AC: operational closure and a meaningful K∞-Act

Status: one depth-first pass, complete for this pass. The §A.31 fixed point is not reached (§7). Off-repo,
read-only, ungoverned. Nothing here is adopted, frozen or proposed as ROADMAP or manuscript wording.

## 0. Base, scope, evidence layers

- **Base.** `68b6df0651f14b2c8ab082635b8d2051918617a2` (K2-GUARD-1 landed, #800), worktree `scratchpad/wt-68b`.
  `git rev-parse HEAD` matches, and `git status --porcelain` was empty at the end of the pass. The only git
  commands run were `rev-parse`, `status`, `log`, `diff --stat` and `merge-base --is-ancestor`. Paths are under
  `verification/lean-mathlib/OIBridge/` unless stated.
- **Delta from the prior notes' bases.** `8daf2bc0` (SA, K2 ledger) is an ancestor of the base. `git diff --stat
  8daf2bc0 HEAD -- OIBridge/` shows one added file, `K2Guard.lean`, and nothing else. So every file:line cited by SA
  or the K2 ledger in an older module is still valid. Every citation used below was re-grepped at the base.
- **Evidence layers, kept distinct.**
  - `[K]` a kernel declaration at the base, with file:line.
  - `[R]` a reading of which hypothesis a landed proof consumes. This is not a certification.
  - `[X]` an exact computation in `scratchpad/ac/`, in Fraction or integer arithmetic (sympy 1.14 for one symbolic
    identity). Each was run twice with byte-identical output. Floats appear only in display strings marked
    "display only".
  - `[W]` a written argument, not kernel-checked.
  - `[L]` literature, not re-proved.
  - `[P]` prior off-repo research, used as data.
  - `[S]` an uncompiled Lean sketch (`AC_sketch.lean`). There is no toolchain here, and every `sorry` is `[W]`.
- **Prior research read and how it was used.**
  - `sa/SA-LEDGER.md` (protocol tower PT/CT, the collapse, P-A label dual, P5 inverse datum).
  - `opact/RESULT.md` and `opact/DESIGN-CONSTRAINTS.md` (the countable no-go for flows).
  - `drive/RESULT.md` (F-D2: the continuum is free on the completed body; F-D3, now kernel CO:348; LIMCLOSE-C;
    X-FR).
  - `oistage/RESULT.md` (NG1, NG2).
  - `rank/RESULT.md` (R0; the leap ranks).
  - `k2d/K2-LEDGER.md` (A1–A7, T5 = K2-GUARD-1, T6, T7).

  These are cited `[P]`. Where a conclusion here depends on one, the dependence is stated. The probes P1–P4 are new
  and do not re-run prior scripts.

## 1. Task 1 — inventory and what each consumer actually uses

### 1.1 The kernel objects `[K]`

| obligation | object | file:line | exact content |
|---|---|---|---|
| K∞-Stage | `DirectedStages` | StageCompletion:63 | a directed preorder of `FiniteStage`s (KF:63) with functorial forward maps |
| | `SCInf` | SC:78 | every forward map carries the table |
| | `body` | SC:141 | `closure (convexHull ℝ (range (prepVec D)))` in `lp … ∞`; the **state** completion |
| | `BinaryVisible` | SC:244 | a binary visible test, carried. Vacuous as stated (SA `[P]`) |
| | `FiniteRank` | SC:299 | `FiniteDimensional ℝ (affineSpan ℝ Ω).direction` |
| | elementary scope | — | not formalized (ROADMAP:1010–1013) |
| K∞-Act | `OpDatum` | CompletionAction:46 | `τ : Prep D → CSpace D` with `mem_body`. Completion-valued, so its codomain admits limits |
| | `StateRespect`, `AffineRespect` | CA:53, :58 | |
| | `CompletionChart`, `exists_completionChart` | CA:144, :154 | |
| | `induced`, `after`, `Undoes`, `inducedEquiv` | CA:277, :305, :325, :333 | |
| | `preservesBody_inducedEquiv`, `isEffectOn_pullback` | CA:352, :364 | |
| | `idDatum`, `affineRespect_idDatum` | CompositionOrder:228, :237 | the identity datum: bare existence of a K∞-Act datum is trivial (SA `[P]`) |
| | `StagePreserving`, `finiteOrderOn_of_stagePreserving`, `not_stagePreserving_of_infiniteOrderOn` | CO:234, :348, :378 | stage-preserving ⇒ finite order on the chart body |
| K∞-Drive | `ElementaryDrivability Ω` | KInfFoundations:264 | a continuous affine flow `ℝ → V ≃ᵃ V` preserving Ω, an involution `flow t₀` moving a point, and `J` off-axis. **A property of the body Ω: no operation family, no availability** |
| | consumers | KF:1013 (`KInf1`, as `Nonempty`); OG:161 `preservesBody_drive`; ON:107 `preservesBody_driveWords` | |
| | controls | KF:449 `ball3Drive`; KF:529 `not_drivable_Icc` | |
| K∞-Trans | `BoundaryTransitive Ω G` | OrbitGeneration:79 | `∀ x y` boundary, `∃ g ∈ G, g x = y`: exact transitivity |
| | `CoversBoundaryFrom` | OG:83 | the same from one fixed `x₀` |
| | countable no-go | EffectSpace:858 `not_boundaryTransitive_of_countable` | a countable `G` is never boundary transitive on `eball 3` |
| K∞-V4 | `SeedOrbitAvailable G r avail` | OG:74 | `∀ g ∈ G, seedTransport r g ∈ avail` |
| ball / effects / K1 | `eq_qBall_of_boundaryTransitive`; `exists_affine_image_eq_eball`; `chartBody_eq_eball` | TransitiveBody:457, :602, :651 | TRB-1 |
| | `sharpFamily_subset_avail`; `maxConeOf_avail_eq`; `fullEffects_subset_avail` | EffectSpace:374, :572, :718 | EFF-1 |
| | `nativeGate_of_avail`; `dim_of_nativeGateOf` | K1Bridge:107, :128 | K1-BRIDGE-1 |
| | `IsNot` | CompositeDimension:210 | a linear involution preserving Ω and flipping `z`. **No membership in any family `G`** |
| K2-GUARD-1 | `CandidateCone`; `no_candidateCone_cnot_reflY` | K2Guard:95, :143 | |
| K3 (exact availability) | `HasCompositeUnitaryControl` | OperationalAssembly:665 | |
| | `UniversalUnitaryReachability` | MonoidalCompletion:377 | |
| | `ExactAllFiniteEndomorphicQuantumOps` | LevelOneSeam:186 | |
| | stated convention | DiscreteCompletion:13 | "dense availability is never identified with exact availability" |
| | countable family not exact QM | DC:1948 `fixedGateTheory_not_qm`, via StateMixingCoupling:679 | |
| | the reachable group | ReachabilitySeam:20–29, :136 | takes the passive flows `e^{-itH}` **for all real t** as exact generators |
| COMP-1 | `PreComposite.Ω` | CompositeInterface:223–230 | convex, contains the products. **Not required closed or compact** |
| PT / CT (protocol and cone towers) | — | not landed | SA §2.1 `[P]` |

No topology on `V ≃ᵃ[ℝ] V` is used anywhere in OIBridge: grep finds no instance, and `flow_continuous` is stated
as joint continuity of `(t, x) ↦ flow t x`. Whether Mathlib carries such an instance was not checked, because
there is no Mathlib checkout here.

### 1.2 What each consumer uses from the operation family `[R]`

| consumer | what it reads of `G` | closed condition? |
|---|---|---|
| TRB-1 `eq_qBall_of_boundaryTransitive` (TB:457) | `PreservesBody`, then the invariant form `qnorm` (IIP:336, invariant under every `g` with `g '' Ω = Ω`) and transitivity, **only** to make `qnorm(· − c)` constant on the boundary (`boundary_qnorm_const` TB:375) and to put the centroid inside (TB:427). The rest of the proof uses no `G` | yes, via continuity of `qnorm` (§3, node N3.1) |
| EFF-1 `maxConeOf_avail_eq` (ES:572) | transitivity only through `sharpFamily_subset_avail` (ES:374), i.e. every sharp effect is available, and then only through the cone `maxConeOf` | yes: nonnegativity of a continuous bilinear expression (N3.2) |
| K1-BRIDGE-1 selectors (K1B:128, :138) | `hK` only through `maxConeOf_avail_eq` (K1B:113, :121) | yes, inherited |
| DIM-1 `dim_of_nativeGate` | nothing about `G`. `IsNot` (CD:210) does not ask that `N ∈ G` | not applicable |
| K2-GUARD-1 (K2G:143) | one element `reflY` and the gate | closure-invariant (det, N3.4) |
| OG-1 SEC `supportingEffectComplete_of_cover` (OG:177); `seedOrbit_ball3_eq` (OG:348); EFF-1 Q-SET (ES:718) | an available effect certain **exactly** at every boundary state; every sharp effect exactly in the seed orbit | **no** (exact existence) |
| `KInf1` (KF:1013) | `Nonempty (ElementaryDrivability Ω)` on the body, no `G` | body-level |
| K3 (OA:665, MC:377, LOS:186) | exact availability of every unitary channel | **no**, by the kernel's own convention (DC:13) |
| K2 T7 cone selection (`[P]` proposal: `hLie`, the closure is a Lie group) | invariance of the composite body under the lifted family | yes, **if the composite body is closed**. COMP-1 does not require that (N6.4) |

## 2. Task 2 — density (depth-first nodes)

**N2.1 Freeness of the rational rotation pair.** Take `R_x(θ)` and `R_z(θ)` with `cos θ = 3/5`, `sin θ = 4/5`.
- Proof `[X]+[W]`, complete:
  - `5R_s` is an integer matrix for each letter `s`, and each `A_s = 5R_s mod 5` has rank 1, with image line `ℓ_s`.
  - For each of the 12 ordered letter pairs `(s, t)` with `t ≠ s⁻¹`, `A_t ℓ_s ≢ 0 (mod 5)` (P1 F3).
  - Induction on a reduced word `W` of length `n`: `5ⁿW ≡ A_{s_n}…A_{s_1}` is a nonzero rank-1 matrix mod 5
    with image `ℓ_{s_n}`, because each step needs exactly one admissible pair to be nonzero. So `5ⁿW ≢ 0 (mod 5)`.
  - Hence `W ≠ I`, since `5ⁿI ≡ 0`. The group is **free of rank 2**, and every non-identity element has infinite
    order.
- Exhaustive confirmation: 4372 reduced words of length ≤ 7 (P1 F4).
- The exclusion of inverse pairs is load-bearing: the inverse pairs vanish mod 5 (F3 control).
- Countercontrols:
  - a same-axis pair commutes (F5);
  - the rational quarter turn has order 4 (F6).
- `[L]`: Świerczkowski, "A class of free rotation groups", *Indag. Math.* 5 (1994): orthogonal axes with rational
  `cos θ ∉ {0, ±½, ±1}` give a free group. The exact proof above does not depend on this citation.
- **Verdict: free (exact).**

**N2.2 Density in SO(3) `[W]`, elementary.** Let `H̄` be the closure of the group.
1. `H̄` is a closed subgroup of SO(3).
2. It contains `closure⟨R_z(θ)⟩`, an infinite closed subgroup of the circle `SO(2)_z` (infinite by N2.1), so it
   contains all of `SO(2)_z`. The same holds for `SO(2)_x`.
3. Euler: `SO(2)_z SO(2)_x SO(2)_z = SO(3)`. So `H̄ = SO(3)`.

General fact `[L]`: any two rotations of infinite order about non-collinear axes generate a dense subgroup, using
the classification of the closed subgroups of SO(3). Generic pairs in compact semisimple groups generate dense
subgroups (Kuranishi). Finite-precision illustration `[X]`, not a proof: nine rational unit targets are reached
within `|W e_z − t|² < 1/100` by words of length ≤ 7 (P1 F7).

**N2.3 The raw family is not transitive, with an explicit witness.**
- `−e_z` is never `W e_z` `[W]+[X]`. A rotation carrying `u` to `−u` has angle π, so it is an involution, and a free
  group has no torsion (P1 F9, with the control `R_x(π)`).
- The cardinality form is kernel: ES:858.
- **Verdict:** the raw family is not boundary transitive. Its closure SO(3) is transitive on the sphere `[L]`,
  standard.

**N2.4 A rational protocol-style tower carrying this family** `[X]` (P2). It is a reverse instance: it is built
from the ball and **sources nothing**.
- Labels are words. A preparation's point is `W e_z`. Effects are `(1 ± p(u)·x)/2`.
- Laws hold at stages 0..3 (T1). SC∞ holds by construction (T2, marked vacuous).
- FiniteRank: the table rank is 4 (T3).
- Label dual `p(e_{u,s} | a·w) = p(e_{a⁻¹u,s} | w)` holds on 3612 instances (T4).
- AffineRespect: 81 basis relations × 4 letters, 0 violated (T5). The countercontrol swap violates (T9).
- Not StagePreserving: 13 of 85 stage-3 preparations leave stage 3 (T6). CO:378 then confirms that the
  infinite-order generator crosses stages.
- Infinite order, finite window (T8).
- **Verdict:** K∞-Act data that are meaningful (not `idDatum`), countable, label-dual and infinite-order exist on a
  finite-rank tower whose completed body is the ball `[W]`, from density and the closed body.

**N2.5 Is "closure of a family of affine maps" well defined in the kernel's topology?**
- The kernel has no topology on `≃ᵃ[ℝ]` (§1.1).
- On the chart (`Fin d → ℝ`), pointwise convergence, convergence of linear-part matrices and translations, and
  convergence of the `d(d+1)` chart probabilities (DRIVE F-D4 `[P]`) all coincide `[W]`.
- Without FiniteRank they differ (DRIVE X-FR, OPACT E5 `[P]`).
- **Verdict:** well defined only after `CompletionChart`. And the weakened consumer predicates of §3 need **no**
  topology on operations at all: their closure is taken in `V`.

**N2.6 What density buys.** BoundaryTransitive holds for the closure and fails for the raw family. But the question
"what downstream needs" splits as in §1.2. See §3 for the decisive branch.

## 3. The decisive branch: which consumers need operational closure (gem pass)

**N3.1 TRB-1 needs only a dense orbit `[W]+[S]`.**

Define `DenseBoundaryOrbit Ω G x₀`: `x₀` is a boundary state, and every boundary state lies in
`closure {g x₀ : g ∈ G}`. The closure is taken in `V`. This is the closure-invariant analogue of
`CoversBoundaryFrom` (OG:83).

Proof that it suffices, under `PreservesBody`, compactness and nonempty interior:
1. **Constancy on the boundary.** `v ↦ qnorm Ω (v − c)` is continuous. Its level set through `x₀` is closed and
   contains the orbit, by `qnorm_sub_centroid_apply` (TB:362). So it contains every boundary state.
2. **The centroid is interior.** If the centroid `c` were a boundary state:
   - constancy gives `qnorm(x₀ − c) = 0`;
   - so every boundary state equals `c`, by `qnorm_pos` (TB:335);
   - but `exists_boundary_ray` gives two distinct boundary states along `±e`, a contradiction.
3. **The rest of TB:457 uses no `G`.** So `Ω` is the `Q`-ball, and TB:602's normalization follows verbatim.

Direction: only `BoundaryTransitive ⇒ DenseBoundaryOrbit` (one line, `subset_closure`). The converse is false (N2.3).

Pressure test (the branch is favourable, so maximum skepticism):
- (a) *Is the hypothesis trivially satisfiable?* No. Three countercontrols fail it:
  - the cylinder with `R_z(θ)`: orbits are dense only in circles, and every invariant form `a(x²+y²) + bz²` differs
    on the boundary states `(1,0,0)` and `(1,0,1)` (P4 C3);
  - the cube with the octahedral rotations: orbits are finite (P4 C2b);
  - kernel polytope exclusions TB:772 and TB:862 apply unchanged, because a dense orbit plus the conclusion forces a
    ball.
- (b) *Is pinning the form the real content?* No. Two raw generators pin the invariant form, with dimension 1 (P4 C1).
  But so does the finite octahedral group, and it preserves the cube (P4 C2b). Density of the orbit on **all**
  boundary states is the load-bearing hypothesis.
- (c) *Hidden use of exactness elsewhere in TRB-1?* `[R]` of TB:375, :427, :457, :602: none.
  - Boundary purity (TB:290) uses exact transitivity, but the ball theorem does not use TB:290.
- (d) *Compactness?* It is required. `chartBody` supplies it (TB:109, :121) because the body is the CMP-1
  **closure** (SC:141).
- **Verdict N3.1: TRB-1's conclusion holds for a raw countable dense family. No operational closure is needed.**

**N3.2 EFF-1 Q-CONE and K1-BRIDGE-1 need only a dense seed orbit `[W]+[S]+[X]`.**
- Each available transport is `sharpEff (g u)` (ES:362).
- `(b, b') ↦ prodEffVal (sharpEff b) (sharpEff b') ω` is continuous.
- Nonnegativity on a dense set of sphere pairs therefore passes to all pairs, and then `maxConeOf_sharpFamily`
  (ES:549) applies.
- Illustration on K2-GUARD-1's `chainW`: the kernel value `−1/2` is reproduced, and raw orbit directions alone
  already give `−36502/78125 < 0` (P4 C4). The control on product states gives all values ≥ 0 (C5).
- K1 reads `hK` only here (K1B:113, :121), so the relative selectors `dim_of_nativeGateOf` and
  `three_of_nativeGateOf_of_two_le` (K2G) need no closure either.
- **Verdict: closure-free.**

**N3.3 Exact-existence consumers do need closure `[X]+[W]`.**
- With `avail` the raw seed orbit, no available sharp effect is certain at `−e_z`. `sharpEff b` is certain only at
  `b` (P4 C6), and `−e_z` is not in the orbit (N2.3).
- So OG-1 SEC (OG:177), `seedOrbit_ball3_eq` (OG:348) and EFF-1 Q-SET (ES:718) fail for the raw family.
- K3 consumers require exact availability by the kernel's own convention (DC:13, ReachabilitySeam:20). DC:1948
  shows that a countable family is not exact QM.
- **Verdict:** operational closure is consumed **only** on the K∞-Geom / full-effect-set branch and at K3.

**N3.4 Orientation (K2-GUARD-1) is closure-invariant `[W]+[X]`.**
- Every affine automorphism of `eball` is orthogonal, so `det = ±1`. `det` is continuous, and `{det = −1}` is open
  and closed in O(d).
- So a raw family has a reflection in its closure iff it has one already. The 3/5 family is all det 1 (P1 F1, F4).
- K2 ledger A5 and H3 ("rotation-only transitivity witness") are met by the raw family in the dense form, and by
  SO(3) exactly.
- **Verdict: POSITIVE.**

**N3.5 K∞-Drive is body-level, and on the route it adds only `d ≥ 3` `[R]+[W]`.**
- `ElementaryDrivability Ω` (KF:264) quantifies over affine maps of `V`, not over an available family.
- Its landed consumers: `KInf1` (KF:1013, as `Nonempty`) and the drive words (ON:107), which serve as a source of `G`.
- Route: TRB-1 (or N3.1) gives `A '' chartBody = eball C.d` (TB:651). At `C.d = 3`, `eball 3 = ball3` (TB:671), and
  transporting `ball3Drive` (KF:449) along `A` gives `ElementaryDrivability (chartBody C)`. This is kernel-cheap and
  not landed.
- At `C.d = 2`, drivability fails: every `J ∈ O(2)` normalizes SO(2) (DRIVE X-OFF `[P]`; KINF-2's written disk
  exclusion). At `C.d = 1`, KF:529. At `C.d ≥ 4` it holds `[W]`.
- So on a transitive (or dense-orbit) body, K∞-Drive ⇔ `C.d ≥ 3` `[W]`. Its continuum is the mathematical closure
  inside `Aut(chartBody)` (DRIVE Γ `[P]`), never an operational availability.
- **Verdict:** the closure that K∞-Drive needs is mathematical, not operational. This class is BORDERLINE (§6).

**N3.6 Branch verdict.** On the landed route to `d = 3` (TRB-1 → EFF-1 → K1 → DIM-1 → K2-GUARD-1), **no consumer
needs an operational closure principle** once K∞-Trans is read in its dense form (N3.1–N3.2), with a raw countable
dense family. Closure is consumed:
- (i) by exact-existence predicates (N3.3: the K∞-Geom SEC branch, full effects, K3);
- (ii) by an operational reading of the drive (available flow members), which no landed theorem consumes;
- (iii) by K2's A7, if the raw family is torsion-free (§5).

## 4. Task 3 — justifying closure; circularity

| candidate principle | what it presupposes | circular? | verdict |
|---|---|---|---|
| **(i) finite-precision indistinguishability** (LIMCLOSE-C): a datum approximable, to every finite accuracy on finitely many stage effects and preparations, by available data is available | the probability topology, which is pointwise on stage coordinates. It is native: it is defined from the tables. It must be read on a finite-rank body, because otherwise limits leave the body and lose continuity (X-FR, E5 `[P]`) | **not circular** with respect to geometry. It mentions no ball, flow or inner product | **not derivable**: it is a convention, empirically idle at every finite precision. Being idle is both its justification and the reason it can be neither confirmed nor refuted. Its only consequences are for exact-existence predicates (N3.3). It **conflicts** with the kernel's standing K3 convention (DC:13). The limit datum keeps AffineRespect (coordinatewise limit of finite relations, `lp.ext`, no FiniteRank). It keeps `mem_body` given FiniteRank (coordinatewise convergence of body points in a finite-dimensional span is norm convergence) `[W]`. Inverses follow from compactness of `Aut(chartBody)` (DRIVE Γ1 `[P]`) |
| **(ii) continuity of the observed statistics** in a parameter | a parameter, i.e. a flow | **circular**: it is DRIVE route Φ, equivalent to DRIVE given OPACT-1 (DRIVE §2.1 `[P]`) | restatement |
| **(iii) CMP-1 completion** | the closure of the **state** set, `body = closure(convexHull(range prepVec))` (SC:141). `OpDatum`'s codomain is `body` (CA:46–48), so limits are *admitted as data*, but no theorem produces them | no | **it supplies state closure only, never operation closure.** By N3.1–N3.2, state closure is exactly what makes operation closure unnecessary for every closed-condition consumer. It also yields compactness of `chartBody` (TB:109) and so of `Aut(chartBody)`, the ambient group in which the mathematical closure of N3.5 lives |
| **(iv) continuous time**: free evolution available for every real duration (the matrix-level K3 form: ReachabilitySeam:29 takes `e^{-itH}` for all real `t` as generators) | a real time parameter | **circular** (route Φ) and **not substratum-native**: the OI update is a discrete step (OI-STAGE `[P]`; RegionTower). The dyadic tower X-CONT `[P]` shows that the continuity clause is load-bearing | restatement plus an added premise |

**Circularity verdict.**
- Only (i) is non-circular. It is a convention, not a theorem.
- On the route as landed it is **unneeded** except at the exact-existence consumers.
- At those consumers it collides with the kernel's explicit refusal to identify dense and exact availability.

## 5. Task 4 — record-writing and stage-raising

**N5.1 Selective record writing is not AffineRespect `[X]+[W]`.**
- A normalized selective branch is `x ↦ τ_v x / p_v(x)`. It respects mixtures iff `p_v` is constant on the segment,
  or the two images coincide.
- Exact instance on an imported control, the unsharp Lüders branch with `λ = 3/5`:
  - the branch is `x ↦ (4x, 4y, 3+5z)/(5+3z)`;
  - it maps the sphere onto the sphere (P3 R1, symbolic);
  - it violates AffineRespect: the centre goes to `(0, 0, 3/5)`, while the midpoint of the images of the poles is
    `0` (R1).
- So selective record writing never yields an `OpDatum` with AffineRespect, unless it is uninformative or constant.
  A constant output is affine and irreversible.

**N5.2 Non-selective record writing that is reversible on the body is uninformative.**
- NG2's eigenvector argument `[P]` never used that `W` is the time step. It needs only `Σ_v τ_v = M` with each
  `τ_v` positive and `M` a body automorphism. So:
  - every extreme ray is an eigenvector of each `M⁻¹τ_v`;
  - with `d+2` extreme points in general position, `M⁻¹τ_v = λ_v I`;
  - so the outcome law is state-independent `[W]`.
- Exact `[X]`:
  - five rational sphere points in general position force scalars (nullity 1, R4);
  - the tetrahedron, a simplex, has nullity 4 (R5): classical informative non-disturbing instruments exist;
  - the square is also forced to scalars (R6). **NG2's hypothesis is general position, not strict convexity.**
- The Lüders non-selective map `(4x/5, 4y/5, z)` is informative and not a body automorphism: `M⁻¹(1,0,0)` has
  squared norm `25/16` (R2, R3).
- `[L]`: "no information without disturbance" for non-classical GPTs (e.g. Pfister–Wehner 2013). It is not
  re-derived beyond the eigenvector lemma.

**N5.3 Stage raising does not obstruct reversibility; it is required for infinite order `[X]+[K]`.**
- The reversible group acts on the **quotient** `Prep / prepVec` through injective, non-surjective, stage-raising
  label maps. `w ↦ X·x·w` is injective and not the identity on labels, but it is the identity on prepVecs (P2 T7).
- CO:378 makes stage crossing necessary for infinite order, and P2 T6 exhibits it.
- So the reversible family is the induced action of non-reversible label maps, as SA described for PT `[P]`
  (CONFIRMING).

**N5.4 Substratum reversibility and body reversibility are logically independent, in both directions.**
- A substratum bijection that is not invertible on the body: SA P5(i) `[P]`.
- **New `[X]`:** `f(v,h) = (1−v, 0)` on `{0,1}²` is not injective, yet:
  - every protocol preparation vector (57 preparations, 40 effects) lies on the segment (R7);
  - the induced idle map is the affine swap, an involution, reversible on the body (R7).

**Task 4 verdict.**
- Record-writing operations cannot be the reversible family on any body with `d+2` extreme points in general
  position, the ball included. Selective branches fail AffineRespect, and a non-selective version that is reversible
  carries no information.
- The family that K∞-Act, K∞-Drive and K2 need must therefore be **record-free**: interventions, not observations.
  Record writing can only supply irreversible operations, or reversible ones on system plus record.
- The reversible family can arise as the induced action of non-reversible (stage-raising) label maps on the quotient.
  That is the PT mechanism, and it is consistent with escape E1 (invasive observation, which drops NG2's passivity).
- This is scoped to the constructions tested. No claim is made about every observer-level extension.

## 6. Task 5 — a unifying principle (named, not adopted)

**OPCOMP: operational completion of a local protocol menu.** It is three clauses.
- **(M) menu.** The reversible operations of a system are the label-dual operations of a prefix-closed,
  inverse-closed protocol menu: `τ_a x = prepVec(x·a)` with dual `e ↦ a·e` (SA P-A, P-C, P-F `[P]`).
- **(C) completion.** Every pointwise-statistics limit of menu data is included, on a completed body of finite rank.
  This is LIMCLOSE-C.
- **(L) locality.** On a joint tower the menu contains `a⊗id` and `id⊗b`, acting by the product label dual
  `(a·e)⊗f`.

**What it would source.**

| target | from which clause | what it gives | what it does not give |
|---|---|---|---|
| (a) meaningful K∞-Act | (M) | AffineRespect (label dual, exact P2 T4–T5), inverse data, `Undoes` on the quotient (P2 T7), body preservation (CA:352). (C) keeps all three under limits `[W]` | **non-triviality**: a menu containing only `idle` is satisfied by `idDatum` (CO:228) on a passive tower. Also not FiniteRank, and not infinite order |
| (b) K∞-Drive | (M) with an infinite-order element, plus the *mathematical* closure in `Aut(chartBody)` (DRIVE Γ `[P]`) | body-level drive at `d ≥ 3` (N3.5). (C) adds only the **operational** availability of flow members, which no landed consumer reads | infinite order, OFF, `d ≥ 3` |
| (c) the K2 local family | (L) | A2 `onProd` and A3 `onEff`, from the product label dual (`[W]`; SA K2-a expectation, unverified for the candidate body); A4 commutation (separate label slots). With raw density and a **closed** composite body, A6 as consumed (cone invariance). (C) supplies A7, a det-1 NOT, as the half-period of a circle if the menu has infinite order | the gate, entangling, PTQ for the gate, LT, the joint tower itself (A1 = `mem_body` of the joint datum), density of the raw menu, closedness of the composite body. A5 orientation is closure-invariant (N3.4), so OPCOMP neither supplies nor removes it |

**Countermodels: each component is not implied by the others.**

| situation | holds | fails | evidence |
|---|---|---|---|
| (M) without (C) | (a) meaningful (P2: infinite order, label-dual) | operational drive: countable no-go (OPACT §2 `[P]`); exact transitivity (ES:858; P1 F9). Body-level drive and the TRB-1 ball still hold (N3.1, N3.5) | `[X]` P1, P2 + `[K]` |
| (C) without a moving (M) | closure of `{idle}` | (a) is trivial (`idDatum`, CO:228) | `[K]` |
| (M)+(C) without compatible (L) | (a), (b) on `ball3` with a menu containing `reflY` (it lies in `fullAut`, ES:227) | (c): no candidate cone is invariant under `cnot` and `actT reflY` | `[K]` K2G:143 |
| (L) with a finite (M) | lifts of `nflip` and the gate (order-8 group `H`) | (b) (finite orbits ⇒ no drive, ON:127) and cone selection: `C_H ⊊ Q₃ ⊊ M_H` | `[K]` ON:127 + K2 T6 `[P]` |
| (c) with A6 | — | — | it **implies** body-level (b) at `d = 3` (the body is the ball; `ball3Drive`), so (c) and (b) are not independent `[W]` |

**Disguise check.** The natural *single* principle is "the reversible protocol operations have a dense orbit on the
pure states". That is K∞-Trans in its closure-invariant form (N3.1). It is **not** a new source, and it is kept
separate here as instructed. OPCOMP is a bundle of three logically independent clauses, not one principle. Its only
closure content is (C), which is DRIVE's LIMCLOSE-C, and by §3 (C) is consumed only off the landed `d = 3` route.

## 7. Task 6 — gem classification (§A.31)

**Productivity test.** The test is AGENTS.md §A.31 as stated. A finding is a gem iff:
1. it is strictly stronger than "closure is needed" or "closure is unneeded";
2. it constrains an obligation or exposes a hidden assumption.

The test was written into the ledger after the probes ran, as the K2 ledger did. I record that order honestly.

| id | finding | class | layer |
|---|---|---|---|
| AC-1 | TRB-1, EFF-1 Q-CONE and K1-BRIDGE-1 consume K∞-Trans only through closed conditions. `DenseBoundaryOrbit` suffices, and a raw countable dense family feeds the ball and the cone with **no operational closure**. ES:858 blocks only the exact predicate. Hidden assumption exposed: "a sourced transitive family must include limits of protocol operations" (SA §3.2; DRIVE's LIMCLOSE-C for V4′) is not needed by these consumers. It sources nothing: NG1, NG2 and the FiniteRank obstructions stand | **NEW** | `[W]+[S]` with `[X]` controls (P1 F7/F9, P4 C1–C5) |
| AC-2 | Consumer split. Operational closure is consumed only by exact-existence predicates: the OG-1 SEC/K∞-Geom branch, EFF-1 Q-SET and K3. Exact witness: `−e_z`. **Assumption-watch AW-AC-1:** any K∞-side closure premise must be reconciled with the K3-side convention (DC:13, DC:1948). The closure question relocates to the K∞ → K3 (Kₙ) seam, where K3 already takes exact continuous passive flows as generators (ReachabilitySeam:29) | **NEW** | `[K]+[X]+[W]` |
| AC-3 | The compactness/closedness of the body is what makes raw = closure for closed conditions. COMP-1's `PreComposite.Ω` (CI:223) is not required closed. **Assumption-watch AW-AC-2:** K2's cone selection may use the closure (T7 `hLie`) for a raw lifted family only if the composite body is closed, e.g. if it is itself a completion. Single-system countermodel: `conv(G·e_z)` is preserved by every raw member and not by `R_x(π)`, since `−e_z` is an extreme point absent from the countable orbit | **NEW** (hidden assumption in a proposal) | `[W]` + `[X]` P1 F9 |
| AC-4 | K∞-Drive is body-level. At chart dimension 3, K∞-Trans (or its dense form) gives K∞-Drive through TRB-1 and the transported `ball3Drive`. On a transitive body Drive ⇔ `C.d ≥ 3`. Its continuum is mathematical closure in `Aut(chartBody)`, not availability | **BORDERLINE** (a short composition of landed facts; its value is in ordering two obligations the ROADMAP lists separately) | `[R]+[W]` |
| AC-5 | The orientation obstruction is closure-invariant. A raw rotation-only dense family satisfies A5 and gives a rotation-only transitivity witness in closure | **POSITIVE** | `[W]+[X]` |
| AC-6 | A complete exact freeness proof for the 3/5 pair (mod-5, 12 pairs). A rational, countable, label-dual, infinite-order K∞-Act tower (P2): a reverse-instance control for future rounds | POSITIVE (tool) | `[X]+[W]` |
| AC-7 | Torsion-free raw families contain no NOT. DIM-1's `IsNot` does not need `N ∈ G`, but K2's A7 would. The NOT is a closure element (half-period, det 1) or an added generator | ELABORATING | `[W]` |
| AC-8 | NG2's eigenvector lemma applies to every reversible non-selective instrument, not only the time step. Its hypothesis is general position, not strict convexity (the square). Selective branches fail AffineRespect | ELABORATING (with CONFIRMING NG2) | `[X]+[W]+[L]` |
| AC-9 | Substratum and body reversibility are independent in both directions (new direction: R7). The reversible group acts on `Prep/prepVec` by stage-raising label maps | ELABORATING / CONFIRMING (SA, F-D3) | `[X]` |
| AC-10 | The closure topology is canonical only under FiniteRank | CONFIRMING (X-FR, E5) | `[P]` |

**Fixed point.** One pass, with three NEW findings (AC-1, AC-2, AC-3), so the fixed point is **not** reached. Next
passes:
- state and attempt `eq_qBall_of_denseBoundaryOrbit` against the kernel, where only a governed round could certify
  it;
- check whether the K∞-Geom SEC branch can itself be weakened to a closure-invariant form, for example SEC up to
  limits with a closed effect family;
- test AW-AC-2 on the K2 T7 hypotheses with an explicit non-closed composite.

**Cross-propagation markers.**
- AW-AC-1 bears on Kₙ and K3.
- AW-AC-2 bears on K2 and COMP-1.
- AC-1 bears on any future K∞-Trans sourcing round: the obligation could be stated in the dense form without loss for
  TRB-1, EFF-1 and K1. This is a research observation, not proposed wording.

**Correctness and consistency (§A.23).** All of this is consistency-axis work. Bands are unchanged.

**Side observation, not acted on.**
- ROADMAP:68 (the P1 status row) reads "K2 **OPEN** (read-only research, no governed round)". K2-GUARD-1 has landed
  as a native round (#800), and its result note says it does not alter the ROADMAP.
- ROADMAP:1001 ("no governed round records the classification or the cone theorem") remains accurate.
- Whether row 68's parenthesis is stale is for the owner. It is recorded here only, with no wording proposed.

## 8. Probe log

All probes are in `scratchpad/ac/`. Each was run as `python3 -I <script> [arg]` from that directory. Each was run
twice and the outputs compared with `cmp`; every comparison was byte-identical. Hashes are the first 16 hex digits
of sha256.

| probe | command | script | output (= rerun) | result |
|---|---|---|---|---|
| P1 freeness, density, antipode | `python3 -I p1_free_dense.py 7` | `1dba7dfbd7242d79` | `p1_out.txt` `cda05e83694d5d88` | 47/47 PASS, `VERDICT free-and-approximating` |
| P2 rational tower | `python3 -I p2_tower.py` | `ec5fca485058e11c` | `p2_out.txt` `60b878a005fe6164` | 9/9 PASS (T2 marked vacuous), `VERDICT tower-mechanisms-hold` |
| P3 record writing | `python3 -I p3_record.py` | `89b0f7cad18cae09` | `p3_out.txt` `0ee530ab971aaefa` | 14/14 PASS, `VERDICT record-writing-constraints-hold` |
| P4 consumers | `python3 -I p4_consumers.py 5` | `83b3cc47bdc0c4f8` | `p4_out.txt` `b8ebd0455a36cb58` | 14/14 PASS, `VERDICT consumer-classification-holds` |
| Lean sketch | — (uncompiled) | `AC_sketch.lean` `cf1449dd17285c5d` | — | `[S]` only |

Corrections recorded during the pass:
- P2 T2 was first printed as a plain PASS. It is vacuous by construction and was relabelled before the final runs.
- P4 C1 alone was first read as evidence for the closure-free ball. The finite octahedral group also pins the form,
  so countercontrol C2b was added before the final runs, and C1 is now read only as "pinning ≠ ball".

## 9. Not decided here

- No OI substratum is shown to supply a dense raw family. NG1 (finite carriers give polytopes), NG2 (passive
  observation), FiniteRank on infinite carriers (rank, P3 `[P]`) and the gate all remain.
- `eq_qBall_of_denseBoundaryOrbit` and `maxConeOf_avail_eq_of_dense` are uncompiled sketches.
- Whether SEC, K∞-Geom or K3 admit closure-invariant forms.
- Whether any observer-native principle supplies operational closure. None found is non-circular and derivable.
- Every negative statement here is scoped to the constructions tested: the 3/5 tower, the Lüders control, the
  `{0,1}²` toy and the kernel's landed predicates.
