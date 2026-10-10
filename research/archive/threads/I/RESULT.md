# Thread I — V4′ derivability (seed-orbit availability), read-only at 6d0abf6b

Lines are at `6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a`, under `verification/lean-mathlib/OIBridge/`.
Abbreviations: KF = KInfFoundations, DG = DomainGlue, OQ = ObservabilityQuotient, PQ = PassiveQuotient,
Eq = Equivalence, CQ = ControlledQuotient, SC = StructuralClosure, RB = RouteB, OA = OperationalAssembly.

Evidence levels:
- **kernel**: a landed identifier;
- **exact**: `i_checks.py`, `OK -- 33 checks, 0 failures`, replay identical, sha256 `23d7b1b3…bc839b`.
  The first run had one failed check, a wrong expectation (see §3, A2), kept in `i_checks.run1.out`;
- **written**: an argument stated here.

Nothing here is a kernel result unless it names a landed identifier.

| target | verdict |
| --- | --- |
| (a) passive dynamics, G = ⟨φ⟩ | **DERIVED** on the finite carrier: ontic or minimal passive. Restricted precomposition is a constructor (`evolve`) whose operational licence is the passive multi-time law. Not connected to KF's `avail` |
| (b) elementary drive, G = ⟨flow(ℝ), J⟩ | **NEEDS-PREMISE**: no landed construction touches it. Minimal rule V4′-gen, stated in §2 |

Neither verdict is CIRCULAR:
- (a) rests on the passive law, not on an effect family;
- (b) has no derivation to be circular.

***

## 1. (a) Passive dynamics: DERIVED

**The construction that makes the visible readout available.**
- The passive law reads the visible factor along the orbit:
  - `RevReal.traj` (Eq:176) is `(step^k s).1`;
  - `RevReal.law` (Eq:180) is the pushforward of `init` along `traj`;
  - `trajProb` (PQ:339) and `itiIndicator` (DG:149) are its finite-itinerary form.

  So the time-k readout of the visible value is, by definition, r ∘ φ^k, where r = 1[vis = i].
- Its domain form is `ClassicalBranchDomain φ vis` (DG:134), with three constructors:
  - `shell` (DG:135);
  - **`evolve` (DG:136): w ↦ (s ↦ w (φ s))**;
  - `branch i` (DG:138): conditioning on vis = i.

  r itself is the term `branch i shell`. `itiIndicator_mem` (DG:156) proves that every event of the passive law is
  in the domain.

**The landed constructor that acts as restricted precomposition.** `ClassicalBranchDomain.evolve` (DG:136), and
its graded twin `BranchDomainK.evolve` (OQ:112), is precomposition restricted to the one map φ.
- **Semantics.** For w = 1[vis = i], w ∘ φ is the event "visible value i one step later" (Heisenberg reading).
  - For a weight μ, `quotMeasure_evolve` (PQ:393) treats μ ∘ φ as the evolved preparation.
  - On a finite carrier with counting measure the two readings agree: ⟨r, φ_*μ⟩ = ⟨r ∘ φ, μ⟩ (exact A1).
  - The direction is not vacuous: ⟨r ∘ φ, μ⟩ ≠ ⟨r ∘ φ⁻¹, μ⟩ for the test law (exact A1).
- **It is restricted, not the forbidden closure.** It precomposes with the generator φ only.
  - On the label-symmetric 4-cycle, r ∘ swap(0,1) = (0,1,1,0) is not ∼∞-invariant, so it is outside
    span ClassicalBranchDomain. The kernel step is `classicalBranch_span_eq_invariant` (OQ:316); the computation
    is exact A3.
  - The constructor therefore does not close availability under arbitrary reversible maps.
- **Licence.** Membership is by construction, so "derived" rests on the licence. The licence is the passive law
  itself: reading vis at time k is an observation, and no effect family is presupposed. That is why the verdict
  is DERIVED and not CIRCULAR.

**Replacing s by g⁻¹s, for g = φ^m (written; each step is kernel or exact):**
- r ∘ g⁻¹ = r ∘ φ^(−m) = r ∘ φ^((ord − m) mod ord), because φ^(ord φ) = 1. This is the same device as
  `itiRelInf_symm_evolve` (PQ:118) and `itiRelInf_iff_orderOf` (OQ:304).
- Hence r ∘ g⁻¹ = `evolve`^((ord − m) mod ord) (`branch i shell`) ∈ ClassicalBranchDomain, for every g ∈ ⟨φ⟩.
  This is checked exactly for all m on Z/5 (A1).
- At the span level, the same conclusion follows from kernel results alone:
  - r ∘ φ^(−m) is ∼∞-invariant. Apply `itiRelInf_symm_evolve` m times, then read the case k = 0.
  - `classicalBranch_span_eq_invariant` (OQ:316) then puts it in the span.
- On the minimal carrier the statement descends unchanged: `quotPerm` (PQ:168), `quotVis` (PQ:161),
  `quotMeasure_branch` (PQ:410).

**Kernel status.** No single landed identifier states "∀ g ∈ ⟨φ⟩, r ∘ g⁻¹ ∈ ClassicalBranchDomain". It is a
one-line constructor term plus `pow_orderOf_eq_one`. A candidate is `branchDomain_orbit_mem` (cheap).

**Caveats (exact).**
- **A2: the inverse costs horizon.** On Z/5 with vis = 1[s = 0]:
  - r ∘ φ⁻¹ = 1[s = 1] is ∼_K-invariant only from K = 4 on, so it is outside span BranchDomainK 2;
  - the direct constructor term needs K = 5 = ord φ.

  At a finite accessible horizon K < ord φ, the passive group is reached only in its forward part, r ∘ φ^k for
  k < K. The first run had predicted span horizon = ord φ; the measured value is 4. The expectation was wrong and
  has been corrected.
- **A4: passive transport is inert for K∞.** A monomial (passive or substratum) conjugation of a diagonal
  projector stays diagonal (exact A4; kernel `substratum_residual`, SC:383). The ⟨φ⟩-orbit of a diagonal seed
  stays among classical readouts and never produces an off-axis effect.
- **Scope.** All of this lives on a finite carrier (S → ℝ). No landed module maps it into KF's
  `avail : Set (V →ᵃ[ℝ] ℝ)`: KF is imported only by the aggregator `OIBridge.lean:246`. That map is P1
  territory, which this thread does not address.

***

## 2. (b) Elementary drive group: NEEDS-PREMISE

**Kernel facts.**
- `ElementaryDrivability` (KF:264–276) has fields `flow`, `flow_preserves`, `J`, `J_preserves`, and others.
  None of them mentions `avail`.
- `avail` occurs only as a binder in:
  - `SupportingEffectComplete` (KF:135);
  - `SingletonFaces` (KF:139);
  - `exposedPoints` (KF:851);
  - `KInf1` (KF:1013). KInf1 takes `Nonempty (ElementaryDrivability Ω)` and `avail` as independent arguments.
- No other module imports KF or uses `ElementaryDrivability`.

**No field-neutral active law reaches the drive.**
- `ControlledQuotient` is field-neutral. It defines `ctrlRel` (CQ:79) through `vis ∘ actWord w` (CQ:56). This is
  readout after a menu word, so it is precomposition by definition, for a menu `acts : A → Equiv.Perm S`. But:
  1. the menu is a free parameter;
  2. it is a relation/quotient, not an availability family;
  3. its actions are permutations of a finite carrier, and inverses come from finite order
     (`ctrlRel_symm_evolve`, CQ:100).
- Written: a continuous ℝ-flow realized by permutations of a finite set is constant on the connected ℝ. So a
  drive with `N_moves` cannot be a menu letter faithfully realized on a finite carrier.
- The comb's control τ (`VStep`, OIRealization:166) is matrix-typed and monomial.
- Matrix-layer corroboration, cited as statements about the matrix theory only:
  - the matrix theory *postulates* `availExt_bind` (OA:617) and `readout_avail` (OA:642);
  - even with that closure postulated, the substratum-generated theory satisfies `DerivedOICore` and lacks the
    off-diagonal rotation (`substratumTheory_falsifierUnavailable` RB:302, `routeB_target` RB:384).

**Countermodel (exact B1–B2; smallest available family).**
- Ω = `ball3`, D = `ball3Drive`, seed r = `ballEffect e₂`.
- avail₀ = {`ballEffect e₂`, `ballEffect(−e₂)`}. This is a perfectly distinguishable pair at the poles: the two
  sum to 1 and each is certain at its pole.
- The flow fixes r: r ∘ rot3(π/2)⁻¹ = r.
- But r ∘ J⁻¹ = `ballEffect e₀`:
  - it is 1 at (1,0,0), which is `isBoundaryState_ball3` (KF:1080);
  - both members of avail₀ give 1/2 there;
  - so r ∘ J⁻¹ ∉ avail₀.
- With avail = `fullEffects ball3` (KF:149), the same (Ω, D) satisfies V4′.

So V4′ is independent of everything landed about (Ω, D, avail).

**The premise cannot be weakened to the seed alone (exact B3).**
- Closing only the seed under single generators gives avail₂ = {`ballEffect e₂`, `ballEffect e₀`}, because the
  flow fixes e₂.
- The word J² sends r to `ballEffect e₁`. That effect is 1 at e₁, where both members of avail₂ give 1/2.

**Minimal unlanded rule (weakest form), V4′-gen: generator-wise transport, restricted to one seed's orbit.**
Given Ω, D : `ElementaryDrivability Ω`, `avail`, and one native sharp seed r ∈ avail (with
`PerfectlyDistinguishable Ω x ![r, 1 − r]` for some x), there is A ⊆ avail such that:
- r ∈ A;
- e ∈ A ⇒ e.comp (D.flow t).toAffineMap ∈ A, for all t (this covers inverses, since flow(−t) = flow(t)⁻¹);
- e ∈ A ⇒ e.comp D.J.toAffineMap ∈ A and e.comp D.J.symm.toAffineMap ∈ A.

**Properties of V4′-gen.**
- It is equivalent to the orbit form ∀ g ∈ Subgroup.closure (range D.flow ∪ {D.J}),
  r.comp g.symm.toAffineMap ∈ avail. Take A = the orbit; the converse is immediate.
- It is strictly weaker than closing all of `avail` under G-precomposition, which is the forbidden general
  closure. It constrains only one orbit.
- The J.symm clause is redundant when J has finite order: `cyc3` has order 3 (exact B3).
- In operational terms: for this one seed, a test from its orbit performed after one elementary drive step
  (flow(t), J or J⁻¹) is an available test.

***

## 3. Exact checks (`i_checks.py`)

| id | statement | result |
| --- | --- | --- |
| A1 | Z/5: `evolve`^(ord−1)(`branch` `shell`) = r ∘ φ⁻¹; ∀ g ∈ ⟨φ⟩, r ∘ g⁻¹ = `evolve`^((L−m) mod L) r; ⟨r, φ_*μ⟩ = ⟨r ∘ φ, μ⟩; ⟨r ∘ φ, μ⟩ ≠ ⟨r ∘ φ⁻¹, μ⟩ | pass |
| A2 | r ∘ φ⁻¹ is ∼_K-invariant for K ≥ 4 only (span horizon 4); constructor-term horizon 5. Run 1 had asserted 4 = 5 and failed | corrected, pass |
| A3 | 4-cycle, vis = s mod 2: every r ∘ g⁻¹ (g ∈ ⟨φ⟩) is ∼∞-invariant; r ∘ swap(0,1) = (0,1,1,0) is not | pass |
| A4 | the four real monomials on Fin 2 keep \|0⟩⟨0\| diagonal | pass |
| B0 | `cyc3` and rot3(π/2) are orthogonal | pass |
| B1 | r ∘ rot(π/2)⁻¹ = r; r ∘ J⁻¹ = be(e₀); r ∘ J⁻² = be(e₁); be(e₀) ∘ rot(π/2)⁻¹ = be(e₁) | pass |
| B2 | the poles pair is a perfectly distinguishable effect pair (checked on grid points); (r ∘ J⁻¹)(1,0,0) = 1 vs 1/2, 1/2 | pass |
| B3 | be(e₁) separates from avail₂ at e₁; J³ = 1 | pass |

Here be(·) is `ballEffect`.

***

## 4. Candidates (nothing frozen)

| id | statement | cost |
| --- | --- | --- |
| I1 | `branchDomain_orbit_mem`: ∀ m i, ClassicalBranchDomain φ vis (fun s => if vis ((φ⁻¹ ^ m) s) = i then 1 else 0) | cheap |
| I2 | `branchDomainK_inverse_horizon`: the A2 countermodel (horizon 2 excludes r ∘ φ⁻¹) | cheap |
| I3 | `v4gen_independent`: on ball3/`ball3Drive`, V4′-gen holds for `fullEffects` and fails for avail₀ | cheap |
