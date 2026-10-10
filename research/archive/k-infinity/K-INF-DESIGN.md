# K∞ — pre-quantum operational completion: design note (read-only, scratchpad; nothing governed)

**Purpose.** Define the field-neutral object K0 lacks, and its completion, so that ballness, full effects and
drivability can be *asked* rather than assumed. No ℂ, no inner product, no ball, no effect duality in any
definition.

## 1. The finite observer object

A finite observer stage `σ` is `(P_σ, E_σ, p_σ, 𝓡_σ)`:
- `P_σ`: a finite set of physically realizable preparations;
- `E_σ`: a finite set of readbacks, including the unit readback `1`;
- `p_σ : E_σ × P_σ → [0, 1]`, the probability pairing;
- `𝓡_σ`: the physically supplied reversible transformations.

States are preparations modulo operational indistinguishability, `s ∼ s' ⇔ p(e|s) = p(e|s')` for all `e`. The finite
state space `Ω_σ = conv{p(·|s) : s ∈ P_σ} ⊂ [0,1]^{E_σ}` is a **polytope**, as the convex hull of a finite set.

- **Lemma F1** (to be kernel-checked): a finite `P_σ` gives a polytope `Ω_σ`, and every affine image of a polytope is
  a polytope. So no finite stage is a ball in any dimension `≥ 2`.
- **Finite-level obstructions already in the corpus**, which F1 joins:
  - effects: `Main.md:540`;
  - drivability: `substratum_residual`, `readWriteSourced_not_qm`.

## 2. The completion K∞

Take a directed family of stages `σ ≤ τ`, with maps carrying readbacks and preparations forward consistently. Set
`E_∞ = ⋃ E_σ` and

`Ω_∞ = cl conv { p(·|s) : s a realizable preparation at some stage } ⊂ [0,1]^{E_∞}`,

closed in the product topology of the operational probabilities.
- `Ω_∞` is compact (Tychonoff) and convex **by construction**. A countable union of finite preparation sets can have
  a closure with a continuum of extreme points, so a ball is not excluded at `∞`.
- Physical effects at `∞`: `E_∞^phys ⊆ Aff_c(Ω_∞, [0,1])`, the continuous affine maps into `[0,1]`. Full effects are
  **not** part of the definition.
- Transformations at `∞`: the closure of the lifted `𝓡_σ`, acting affinely and continuously on `Ω_∞`.

## 3. The forks, each a separate question

**Fork A — transitive drivability and the ball.**
- *Bit*: the largest perfectly distinguishable set has size two.
- *`DrivesElementary∞`* is stated group-theoretically, without ℂ:
  1. a continuous one-parameter subgroup `R_t` of `𝓡_∞` fixing the classical frame's axis, **with `N = R_{t₀}` for
     some `t₀`**: the native NOT lies on the flow, so the NOT is continuously interpolable (in matrices,
     `flow(transition) (π/2) = −iX`, whose conjugation is `N`);
  2. one reversible `J` with `J R_t J⁻¹ ⊄ {R_t}`. This is the quarter phase's role, moving the axis.
- *Question*: do `DrivesElementary∞`, the bit property, and the observer symmetries actually sourced give pure-state
  transitivity?
- **Caution, per owner:** "bit plus transitivity implies a Euclidean ball" is not frozen. The convex hull of an orbit
  of a compact group is an orbitope, generally not a ball. The minimal convex-geometric theorem needed must be
  audited first, and the classical reconstructions (Dakić–Brukner, Masanes–Müller) use more.
- *Built-in countermodels for (1)*:
  - the classical bit, a segment, whose reversible group is `Z₂`: NOT is not continuously interpolable;
  - the square gbit, whose reversible group is dihedral: likewise.

**Fork B — full effects.** Is `E_∞^phys = Aff_c(Ω_∞, [0,1])`?
- The candidate countermodel is the `Main.md:540` four-state model, which has the ball geometry and restricted
  effects. It must be checked against the Fork A conditions before it counts as an independence witness.

**Fork C — copy naturality.** For copies `A, B` with the canonical identification `e`, require `e N_A e⁻¹ = N_B`. It
has to arise from naturality of the construction, not from one global symbol `N`. NB-1's `d = 5` two-NOT countermodel
shows the premise is load-bearing.

**Fork D — composition.** Only after A–C. A 3-ball with full effects, one common `N`, and `DrivesElementary∞` give the
full local `SO(3)` (the flow circle about `N`'s axis plus its `J`-conjugate). Then K2 (read-only) gives `Q` or `PT(Q)`,
and K3 follows.

## 4. A cheap exact check suggested by Fork A (conjecture, not a result)

If `N` lies on a continuous flow, `N` is in the identity component, so `det N = +1` on the ball's `d` coordinates. For
the NB-1 form `N = diag(+1 on p transverse axes; −1 on q transverse axes and on z)`, `det N = (−1)^{q+1}`, which is `+1`
iff `q` is odd. Against NB-1's controls:

| model | `(p, q)` | `det N` | continuously interpolable NOT? |
| --- | --- | --- | --- |
| C3, the qubit (`d = 3`) | (1, 1) | +1 | allowed |
| C5, the J/K map (`d = 5`) | (1, 3) | +1 | allowed |
| C2N control NOT `N_A` (`d = 5`) | (2, 2) | −1 | **excluded** |
| C2N target NOT `N_B` | (1, 3) | +1 | allowed |
| C7 (`d = 7`) | (3, 3) | +1 | allowed |

- **Reading, to be checked, not claimed.** A continuous-NOT principle would exclude the two-NOT countermodel's
  `N_A`, but not the J/K map, nor C7. C7 is excluded by positivity anyway.
- It would **not** replace copy naturality in general: another two-NOT pair with both `q` odd must be checked. That is
  the next cheap exact test.
- Maximum skepticism applies: this is a favourable-looking reading of one parity.

## 5. First steps (read-only)

1. The audit of the minimal convex-geometric theorem needed for Fork A: what, beyond a bit with a transitive compact
   group, forces a Euclidean ball.
2. The exact two-NOT parity test from §4: search for pairs `(N_A, N_B)`, both with `q` odd, meeting both NB-1
   relations and positivity, at `d = 5` and `d = 7`.
3. Kernel formalization of Lemma F1 and of the definitions in §1–§2, as a design artifact only.

***

## 6. Side probe result — continuous NOT does not replace copy naturality (exact; `two_not_d7.py`)

- **Analytic.** S5 forces `p_A = q_A = (d−1)/2`, and continuous interpolability needs `q_A` odd, so `d ≡ 3 (mod 4)`.
  `d = 5` is excluded, and at `d = 7` the only admissible splits are `(3,3)` on the control and `(1,5)` on the target.
- **Exact at `d = 7`.** The J/K map exists with `N_A` of split `(3,3)` and `N_B` of split `(1,5)`, both of determinant
  `+1`, and satisfies:
  - the frame and `G² = I`;
  - `J` and `K` are orthogonal complex structures, with `N_A J N_A = −J`;
  - Rt with `N_B` and Rc with `(N_A, N_B)`;
  - the complex-CNOT reduction formula, on the full multi-affine grid.

  Positivity follows by the written reduction to the qubit case; a numerical cross-check gives a minimum of
  −6.4e−16.
- **Control.** With one common `N = N_B` on both copies, Rc fails.
- **Conclusion.** A continuously interpolable NOT removes the `d = 5` two-NOT countermodel but not the loophole.
  Copy naturality (Fork C) stays an independent, load-bearing premise.

## 7. Fork A theorem audit — the ball lemma and what must be sourced

**Lemma B, the ball lemma.** Let `Ω` be a compact convex set with nonempty interior in a finite-dimensional real
affine space, and let `K` be a group of affine automorphisms of `Ω` acting transitively on the boundary `∂Ω`. Then `Ω`
is affinely a Euclidean ball.

*Proof sketch, elementary; a candidate for the kernel:*
1. `Aff(Ω)` is compact: it is closed, and bounded because it preserves a body with interior. So `K̄` is compact.
2. `K̄` fixes the barycentre `c`.
3. Averaging gives a `K̄`-invariant inner product.
4. A single orbit lies on one sphere about `c`, so `∂Ω ⊆ S(c, r)`.
5. Every ray from the interior point `c` leaves `Ω` at distance `r`, so `Ω = B(c, r)`.

**Consequences for the premises:**
- "All boundary states are pure plus transitivity on pure states" is exactly transitivity on the boundary, which is
  the premise of Lemma B.
- **Binary capacity is not needed for the lemma.** A ball has capacity two automatically. It may still be needed to
  *source* the premises.

**What K∞ must source, then:**
- **(A1) Transitivity.** If the completed preparations are generated by reversible maps from the classical frame
  state, so that `Ω_∞` is the closed convex hull of an orbit (an orbitope), transitivity on pure states is automatic,
  since the pure states are the orbit.
- **(A2) Boundary purity**, which becomes the crux. An orbitope generally has non-extreme boundary points. By Lemma
  B, boundary purity of a drivability orbitope holds exactly when it is a ball.
- **`DrivesElementary∞` alone cannot give (A2).** The group generated by one circle and one conjugate of it can be
  any compact Lie group, since every compact semisimple Lie algebra is generated by two elements. Its orbitope need
  not be strictly convex.

**Next exact step in this thread (not yet run).** Test whether **binary capacity** is what forces (A2). The question is
whether there is an orbitope of a compact group with:
- a circle through the NOT (`N = R_{t₀}`);
- binary capacity (at most two perfectly distinguishable states);
- a non-extreme boundary point.

A known non-example: the SO(3) Veronese orbitope is the real qutrit, which has capacity three. If no such orbitope
exists, Fork A reduces to **orbit-generated preparations + binary capacity + `DrivesElementary∞` ⇒ ball**. Composites
and local tomography would not be needed at this stage, which is narrower than the Dakić–Brukner and Masanes–Müller
premises.

## 8. Fork A, refined (owner's refinement, checked)

**Why capacity alone is the wrong premise.** Capacity is measured by the physical effects, and Fork B allows
`E_phys ⊊ E_full`. A non-ball orbit hull can therefore have operational capacity two just because its effects are too
restricted to separate three states. The premise has to be effect-rich enough to make bit-ness geometric.

**The two readback premises:**
- **(SEC), supporting-effect completeness.** Every supporting hyperplane of `Ω_∞` is represented by some physical
  binary effect. This is much weaker than full effects.
- **(SF), binary singleton faces.** The certain-outcome face `{ω : e(ω) = 1}` of every physical binary effect is empty
  or a single state.

**Lemma C.** (SEC) + (SF) ⇒ `Ω_∞` is strictly convex.
- *Proof.* Suppose a segment `[x, y]` lies in `∂Ω`. A supporting hyperplane at its midpoint exposes a face containing
  the midpoint in its relative interior. Faces are extreme subsets, so the face contains `x` and `y`. (SEC) represents
  that face as the certain-outcome face of a physical effect, and (SF) makes it a single state, a contradiction.
- Checked. Note that (SF) is strict convexity stated on the effect side, restricted to exposed faces. The lemma moves
  the burden from geometry to readback; it does not remove it.

**The chain for Fork A.**
1. Lemma C gives strict convexity: every boundary state is pure.
2. Orbit-generated preparations (A1) give transitivity on the pure states.
3. Lemma B then gives a ball.

`DrivesElementary∞` is no longer used for ballness. It is used afterwards: the NOT lies on the flow, and SO(3) follows
in K2. Binary capacity is automatic for a ball.

**Controls, each showing one premise load-bearing in Lemma C** (to be checked exactly):

| model | (SEC) | (SF) | strictly convex? |
| --- | --- | --- | --- |
| square gbit with its four facet effects | holds | fails: the certain faces are edges | no |
| "stadium" body, effects exposing only its round arcs | fails | holds for the available effects | no |
| qubit ball with all effects | holds | holds | yes |

**Consequence for Fork B's candidate witness.** The `Main.md:540` four-state model has the ball's geometry, but its
tetrahedral effects never reach 1 on the ball. So it has no certain outcomes, operational capacity one, and fails
(SEC). It cannot serve as Fork B's independence witness as it stands. A full-effects witness has to keep a sharp
binary measurement and satisfy (SEC) and (SF), while still lacking some effect in `Aff_c(Ω, [0,1])`. For the ball,
such a witness would need effects exposing every boundary point but missing some interior-valued effect.

**Next step.** A source audit, in progress: does the stochastic-interface and C4 readback machinery supply (SEC) or
(SF), or refute them at a finite stage? Only if neither can be sourced does the fallback search run: a connected
orbit hull with rich physical effects, capacity two and mixed boundary points.

## 9. Readback source audit (read-only, at `D`; spot-checked) — and a correction to §1

**Correction to §1 and to the "three finite obstructions" synthesis.**
- Lemma F1 is valid only as stated: a *finite set of preparations* gives a polytope.
- A finite *ontic* substratum does not give finitely many preparations. Mixtures over finitely many ontic states
  already form a continuum.
- `Main.md:540` records the ontic version of the inference as invalid, and its four-state SIC model carries the whole
  Bloch ball inside `Δ₃`. So ball geometry is **not** obstructed at a fixed finite stage.
- The finite obstructions are two, not three: **effects** and **drivability**. The earlier "states: finite
  preparations give a polytope" is withdrawn as an obstruction. It holds only under a modelling choice of finitely
  many realizable preparations, which the corpus does not make.

**(SEC) — absent from the corpus, and refuted at any fixed finite classical realization for the qubit.**
- `Main.md:538-540`, certified in `nogo_probes.py`: no fixed finite realization is operationally equivalent to one
  qubit's full theory.
- In the SIC model the sharp effect `|0⟩⟨0|` has no valid response function (`½ + √3/2 > 1` at an ontic vertex). In
  Lemma C's terms, the effects that support the ball at its pure states are exactly what is unavailable.
- **So K0's finite-stage obstruction is precisely (SEC), the premise Lemma C needs.** If (SEC) holds anywhere, it can
  only hold in the completion. K∞ must supply sharp supporting effects in the limit, and nothing in the corpus does
  today:
  - `RegionLimit` is spatial and not a refinement; observables extend only by tensoring with the identity;
  - `CoherentContinuumSource` T5 says the coherent continuum is not sourced by the substratum.
- **Nearest positive result.** `ObservabilityQuotient` shows full QM follows exactly when the observer cut is
  informationally complete. That is state *separation*, not boundary *exposure*, and it is itself not established:
  C1–C4 are "not complete observability".

**(SF) — absent, neither assumed nor derived.**
- The only built-in readout is the ancilla basis readout (`readout_is_localLuders`, `OperationalAssembly.lean:658`).
  A certain outcome there fixes the ancilla index, not the system state.
- `ObservabilityQuotient`'s non-singleton itinerary classes concern *configurations*. Operational states are already
  quotiented, so this does **not** refute (SF) for operational states. It shows only that (SF) cannot be read off the
  configuration level.
- The stochastic interface "selects no readout", and its row is OPEN.

**Vocabulary hazard.** The corpus's C4 "readback" means hidden memory feeding back into later visible statistics. It is
not an effect or a test on states. K∞ must not borrow the word for effects.

**Where Fork A stands.**
- Ballness needs (SEC) + (SF) + orbit-generated preparations.
- (SEC) is provably unavailable at a fixed finite stage for the qubit, so it has to come from the completion.
- (SF) is unaddressed.
- The sharpest K∞ question is now: **can a completion of finite observer stages supply sharp supporting effects — a
  limit of finite response functions that reaches `0` and `1` on the boundary — without importing them?**

## 10. K∞-E: what a completion of finite effects can and cannot supply (analytic; `exposed_sic.py` exact)

**Point-exposing sharpness** (owner's formulation): for every boundary state `ω` a physical effect `e` with `e(ω) = 1`
and `e(σ) < 1` for `σ ≠ ω`. Checked: it implies every boundary point is exposed, hence extreme, hence strict
convexity. Mathematically it is the surgical premise.

**Theorem F2 (finite-stage counting bound).** In a classical realization on `N` ontic states, with effects the
`[0,1]`-valued affine functions on the simplex `Δ_{N−1}`, a state `ω` of an embedded strictly convex body `Ω` is
point-exposable only if `ω` lies on a facet of `Δ`, and each facet meets `Ω` in at most one point. So **at most `N`
boundary states are point-exposable.**
- *Proof.* `e(ω) = 1` with `e = Σ cᵢpᵢ`, `cᵢ ≤ 1`, `pᵢ(ω) ≥ 0`, `Σpᵢ = 1` forces `cᵢ = 1` wherever `pᵢ(ω) > 0`. If all
  `pᵢ(ω) > 0` then `e ≡ 1`, not exposing. So some `pᵢ(ω) = 0`: `ω` is on facet `i`. A strictly convex body contains no
  segment, so its intersection with the flat facet is at most one point.
- *SIC instance, exact.* The four tangency points `r = −aᵢ` are exposed by `e = 1 − pᵢ`; every other pure state has all
  `pᵢ > 0` and is not exposable. `Main.md:540`'s single-effect obstruction becomes a count: 4 of a continuum.

**Theorem F3 (what a limit of effects gives).** Let `E_∞` be the closure of the union of finite valid effects, each
finite stage a classical realization of the same `Ω`. A limit of exposing effects is a **supporting** effect at the
limit point. A supporting effect at `ω` exposes `ω` iff the face it exposes is `{ω}`, which for every `ω` is exactly
strict convexity of `Ω`. Hence:

> **point-exposing sharpness in the limit ⇔ (SEC) ∧ strict convexity of `Ω_∞`.**

The completion can supply (SEC), if the finite stages' tangency sets become dense in `∂Ω`; it **cannot generate
strict convexity, only certify it.** Lemma C is a valid theorem, but as a sourcing route it is circular: the
point-exposing effects a completion produces presuppose the strict convexity they were to prove.

**Consequences.**
1. **Two sources, cleanly separated.** Sharpness of effects comes from K∞-E (a refining completion). Strict
   convexity of the state body must come from the preparation and dynamics side.
2. **(SEC) makes capacity geometric.** With every supporting hyperplane available, perfect distinguishability of `k`
   states is a property of the body. So the owner's objection to "capacity two" as a premise is answered by (SEC), and
   the non-circular Fork A question is again:
   > **orbit-generated preparations + binary capacity + (SEC) ⇒ strictly convex?**
   Its countermodel would be a connected orbit hull with (SEC), capacity two, and a non-extreme boundary point.
3. **What K∞-E needs from the substratum:** a *refining* family of classical realizations of one system, with
   `N_n → ∞` and tangency points dense in `∂Ω`. The corpus's directed system (`RegionLimit`) enlarges regions at
   fixed spacing and is not a refinement. Whether spatial enlargement refines the effect set of a fixed subsystem is
   the first K∞-E sourcing question.

**Standing.** K∞-E and K∞-R are separate obligations, with copy naturality a third; a single completion principle
supplying both K∞-E and K∞-R is a hypothesis, not established.

## 11. Side probe result: binary capacity does not force strict convexity, even with full effects (`orbit_hull_capacity.py`)

**Convention.** Full effects: every affine `0 ≤ e ≤ u`. So capacity is intrinsic to the body.

**Lemma D (central symmetry bounds capacity).** A compact convex body symmetric about its centre `c` has capacity
`≤ 2`. *Proof.* Perfectly distinguishing effects `eᵢ = aᵢ + ⟨Bᵢ, x − c⟩` that are `≥ 0` and vanish somewhere have
`aᵢ = h(−Bᵢ) = h(Bᵢ)` (`h` the support function, symmetric); then `1 = eᵢ(ωᵢ) ≤ 2aᵢ`, so `aᵢ ≥ ½`; `Σeᵢ = u` gives
`Σaᵢ = 1`, hence `k ≤ 2`. ∎

**Countermodels** (connected orbit hulls, transitive on their extreme points, centrally symmetric hence capacity 2,
with flat boundary faces):
- **T, the torus orbitope** `conv(S¹×S¹) ⊂ ℝ⁴`, group `SO(2)²` (abelian). Flat 2-face `{s = 0} × disk`, exposed by
  `e = (1 + cos s)/2`.
- **S, the Stiefel orbitope** `conv V₂(ℝ³) ⊂ ℝ^{3×2}` (the spectral-norm unit ball), group `SO(3)`, **non-abelian**,
  containing circles and their non-commuting conjugates, so a `DrivesElementary∞`-type structure. The face exposed by
  a rank-one functional is a flat disk.

**Controls.** The Carathéodory orbitope `C₂` (not centrally symmetric) has capacity 3, with the exact triple at
`t = 0, 2π/3, 4π/3` and `eᵢ = (4/9)(1 − cos(t − tⱼ))(1 − cos(t − tₖ))`, `Σeᵢ ≡ 1`. The 3-ball has capacity 2 and is
strictly convex. LP relaxations (nonnegativity on 4000–6000 sampled extreme points) agree: capacity-3 infeasible on
30 random triples for T, S and the ball; feasible for `C₂` at the exact triple.

**Verdict.** `orbit-generated + connected (even non-abelian) drivability + binary capacity + full effects ⇏ strict
convexity`. The route is closed. Strict convexity is independent content, and the honest premise is (SF): the
certain-outcome face of every sharp binary effect is a single state. T and S both violate (SF) (their certain faces
are a disk), the ball satisfies it. In operational terms: **in a bit, certainty of a sharp yes/no outcome identifies
the state.**

## 12. Primary audit: the region limit does not refine a subsystem's effects (read-only at `D`; spot-checked)

**Verdict: does not refine.**
- The extension map is `X ↦ X ⊗ 1` on the adjoined sites: `RegionLimit.lean:102` (`inclObs R X := tensorOf X 1`),
  `RegionTower.lean:123-125`. State restriction is the partial trace, dual to it. The limit algebra is the closure of
  the union of stages. The quasilocal audit records this as "not new structure".
- There is no stage-indexed effect set to refine. Availability (`availT`, `TypedCompletion.lean:167`; `InstAvail`)
  has no region argument, and it is already closed under attaching a uniform ancilla of *every* finite size, running
  an available family and discarding (`InstAvail.discard`, `ImplementationLocality.lean:285`). So
  `E_Λ(S) = E_{Λ'}(S)` holds by construction: option (b), spectators only.
- **The only way effects grow is a control hypothesis.** `circuit_available` yields new system instruments from an
  ancilla only under `HasCompositeUnitaryControl`; the substratum's own operations are monomial and preserve the
  diagonal (`preservesDiag_conj_of_monomial`, `SubstratumInterface.lean:126`), its knob has finite range
  (`readWriteOperator_range_finite`, `CoherentContinuumSource.lean:292`), and its falsifier is unavailable
  (`substratumTheory_falsifierUnavailable`, `RouteB.lean:302`). Ancilla-assisted effects stay classical.
- No statement makes a fixed subsystem's ontic states or readouts grow along the directed system; the corpus's growth
  statements are in precision and horizon (`Main.md:538, 554, 574`).

**Consequence for K∞-E.** H-∞'s completion cannot be reinterpreted as an effect completion. A refining family of
realizations of one system, with tangency points dense in `∂Ω`, is a **new mechanism**, and the corpus locates the
only known source of non-classical effects in exactly the control resource K∞-R needs. So K∞-E and K∞-R are not
merely parallel: in the present kernel, sharp effects on a subsystem come *from* drivability plus ancilla closure
(Naimark), not from region growth. That is evidence for the single-completion hypothesis, of a specific shape:

> **Hypothesis K∞-1.** In a completion supplying `DrivesElementary∞`, sharp supporting effects on `S` arise by
> attach-then-readout closure from the drivable transitions (a field-neutral Naimark step), with no separate
> effect-completion principle.

If true, (SEC) follows from K∞-R; (SF) remains, by §11, independent.

**The K∞ left-hand side, as the evidence now stands:** K∞-R (field-neutral drivability, possibly yielding (SEC) via
K∞-1) + (SF) singleton faces + copy naturality. Everything downstream — ball (Lemma B + C), `d = 3` (NB-1), `SO(3)`,
`Q` up to orientation (K2), typed Kraus (K3) — is proved, landed, or mapped.

## 13. K∞-1M — the matrix witness is a landed theorem (read at `D`; evidence level 2)

**Question.** In the complex operational interface, does `DrivesElementary`, with the structural stabilities the
substratum already has, give every rank-one qubit projective effect without assuming `HasCompositeUnitaryControl`?

**Answer: yes, and more.** The chain, each link with no dagger or inverse-control premise:

| link | theorem | premises |
| --- | --- | --- |
| `DrivesElementary 𝓘 ⇒ ElementaryTransitionRichness (genTheory 𝓘)` | `genTheory_elementary`, `SubstratumSource.lean:109` | `Architecture 𝓘` |
| `⇒ LieRankRichness` | `lieRank_of_elementary`, `LieRankSource.lean:476` | `[Nonempty A]` only |
| `⇒ HasCompositeUnitaryControl` | `control_of_lieRank`, `MicroscopicReversibility.lean:114` | none |
| control + preparation + readout `⇒` measurement circuits | `circuit_available`, `OperationalAssembly.lean:757` | the interface's closure rules; `readout_is_localLuders` |
| `⇒` all finite endomorphic instruments | `fullInstruments_of_control`, `StinespringAssembly.lean:197` | `FiniteIsometryExtensionSF`, discharged by `finiteIsometryExtensionSF_discharged`, `IsometryExtension.lean:116` |

And the composition is already stated: **`genTheory_qm_of_quantumArchitecture`** (`SubstratumSource.lean:136`):
`QuantumArchitecture 𝓘 ⇒ ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 A)`, through `qm_of_oiPlusElem`. Since
`substratum_residual` shows the substratum class has the other four clauses of `QuantumArchitecture` (architecture,
context, label and dagger stability) and lacks only `DrivesElementary`, drivability is exactly the missing piece, and
supplying it yields every finite quantum instrument, rank-one projective effects included.

**Boundary.** This is `matrix K∞-R ⇒ matrix K∞-E`, proved. Every link runs through `Matrix (A × Fin n) ℂ`: the Lie
algebra `su`, unitary control, the Lüders readout `id ⊗ ℒ_k`, and the matrix circuit. The field-neutral analogue,
`DrivesElementary∞ ⇒ sharp supporting effects`, is open, and it is the content of hypothesis K∞-1.

**Standing after K∞-1M.** At the matrix level K∞-E is not an independent premise. The left-hand side is
> K∞-R + singleton faces (SF) + copy naturality,
and the field-neutral programme is: reproduce, before assuming ℂ, (i) the Naimark step `DrivesElementary∞ ⇒ (SEC)`,
and (ii) the sourcing of (SF), which §11 shows no dynamical or capacity premise can replace.

## 14. Singleton-face sourcing audit (read-only at `D`; spot-checked): (SF) is absent at every level

**(a) Matrix level, SF-M: unstated, trivially derivable, and non-selecting.** No theorem says a rank-one effect's
certain set is one pure state; no "pure", "certain" or "face" predicate exists. The interfaces carry no state-space
field: states are implicitly all density matrices (`SeparatesStates`, `PassiveObservation.lean:208`). On the qubit,
`ρ_kk = 1` with trace one and positivity forces `ρ = |k⟩⟨k|`, a few lines via `psd_pair_kernel`
(`OperationalRigidity.lean:413`). But because the state space is *imported* as all density matrices, SF-M holds in
every model, the diagonal and gap countermodels included: **it is a property of the imported kinematics, not a
principle that selects anything.** This is the K0 gap again, seen from the effect side.

**(b) Observer level: absent, and C4 points the other way on larger carriers.** C1–C4 (`Main.md:76-80`) say nothing
about certainty identifying a state. C4 reads "two visible histories with the same current state induce different
next-step laws" (`Main.md:80`): a certain current visible value does not fix the next-step law. Passive observation
reads only block weights (`CentralObservation.lean:433, 516`); `no_complete_internal_observer`
(`InternalObserver.lean:206`) shows a record block certain on outcome `o` contains all of `A` when `|A| ≥ 2`. The
stochastic interface and embedded observation are silent.

**(c) Manuscripts: not found.** No sharp-test, certainty, maximal-information or subspace-axiom language; the
reconstruction axioms are cited only as external axiom sets (`Main.md:352`).

**(d) Counter-direction: only on carriers larger than one bit.** Every certain-but-non-identifying readout found
(internal observer records, `id_A ⊗ ℒ_k`, C4) lives on a composite or a register. None is a binary system, so none
refutes (SF) as stated for bits.

**Standing after the audit.** (SF) is an explicit physical principle unless K∞ finds a source, and §11 shows nothing
dynamical or capacity-based can replace it. Its operational content — *in a bit, certainty of a sharp yes/no outcome
identifies the state* — is small, and the corpus's own "observation incompleteness" theorems do not contradict it,
since they all concern more than one bit.

## 15. The K∞ read-only round — summary of standing

| premise | status | source of the status |
| --- | --- | --- |
| K∞-R, field-neutral drivability | **open**; load-bearing (`substratum_residual`, `readWriteSourced_not_qm`) | §7, §13 |
| K∞-E, sharp supporting effects | **derived from K∞-R at the matrix level** (`genTheory_qm_of_quantumArchitecture`); field-neutral Naimark step open (K∞-1) | §12, §13 |
| (SF), singleton faces | **open**; independent of dynamics, capacity and full effects (Lemma D; torus, Stiefel) | §11, §14 |
| copy naturality | **open**; load-bearing at `d = 5` and `d = 7` (two-NOT J/K maps) | §6 |
| strict convexity + transitivity ⇒ ball | proved (Lemma B, elementary) | §7 |
| (SEC) + (SF) ⇒ strict convexity | proved (Lemma C) | §8 |
| region limit refines effects | **refuted** (`X ↦ X ⊗ 1`; availability ancilla-closed) | §12 |
| finite stage exposes ≤ N states | proved (Theorem F2; SIC: 4 of a continuum) | §10 |

Candidate small kernel artifacts, if a design round is opened: Lemmas B, C, D; Theorem F2; SF-M on the qubit; and the
field-neutral definitions of §1–2. None is governed; nothing is committed.

## 16. Queued after KINF-1 → ROADMAP K → hygiene (owner-agreed order; nothing started)

1. **NOT-conjugacy reduction (candidate theorem, untested).** If `N_B = g N_A g⁻¹` for a reversible frame-preserving
   local automorphism `g` of copy B, then `G̃ = (I⊗g⁻¹) G (I⊗g)` satisfies Rt and Rc with `N_A` on both factors, F
   with the same corners, and P± (local cone automorphisms preserve `min` and `max`), so NB-1 applies. Copy
   naturality would then reduce to *type covariance of native inversion*: identical system types have NOTs in the
   same frame-preserving conjugacy class. The split `(p, q)` is the computational classifier, not the definition;
   do not equate them until checked. Both surviving countermodels have different splits: d = 5, (2,2) vs (1,3);
   d = 7, (3,3) vs (1,5). Exact probe: relabel those models and a constructed conjugate-NOT pair (must collapse to
   one `N`) with the k-scripts.
2. **Update-rule source audit** (pattern of the K0 audit): whether C4, embedded observation or record-writing says,
   before matrix QM, that a certain sharp maximal outcome erases dependence on the incoming state within that
   outcome. Today SF-as-update-rule is a relocation, not a derivation; the square gbit is the control.
3. **Field-neutral observation architecture** `(system, contexts, outcomes, interactions)` in the KInfFoundations
   vocabulary; context homogeneity + continuity is a consolidation of transitivity and K∞-R, not a derivation;
   mandatory controls: square gbit, torus orbitope, Stiefel orbitope.

## 17. Alternative sources (owner discussion, 2026-10-01; nothing started)

Working hypothesis, not adopted: K∞-R ← continuous dynamics; SF ← measurement update or purification;
copy naturality ← composition / system type. Facts bearing on each: FrozenSourcing (INDEPENDENT) for dynamics;
torus/Stiefel show connected transitive groups do not give SF; K0 audit: purification existence only,
uniqueness fails (`fiber_freedom`); self-duality assumed only for PSD and taken as a premise by NB-1.

- **Scope note for the successor foundations round:** do not freeze SF as *the* geometric premise; the
  homogeneity + self-duality (Koecher–Vinberg) route subsumes SF and NB-1 already assumes self-dual effects.
- **Queued probe 1b (beside the conjugacy reduction):** three-copy consistency. Take a two-NOT pair with
  mismatched splits (d = 5: (2,2)/(1,3); d = 7: (3,3)/(1,5)), add a third copy with pairwise native gates
  meeting NB-1's relations, and test whether any mismatched assignment survives. Death at three copies would
  mean composition sources (part of) copy naturality without the conjugacy reduction.

**Promotion rule (owner, 2026-10-01).** ROADMAP = established status + genuinely open obligations; this note =
candidate mechanisms, competing routes, planned probes. An option enters the ROADMAP only when a governed result
supports it, a governed countermodel rules it out, or it materially changes the formal statement of an open
obligation. Of §17, only the geometric-route neutrality sentence qualifies now (patch:
`k-roadmap/roadmap-geometry-neutrality.patch`, to land as its own change after PR #775).
