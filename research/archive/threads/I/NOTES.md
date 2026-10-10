# Thread I — running notes

Worktree: `threads/I/wt`, detached at 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a (removed at end).
Paths below are relative to `verification/lean-mathlib/OIBridge/`.

## Survey (in order)
1. KF (KInfFoundations.lean). `avail : Set (V →ᵃ[ℝ] ℝ)` appears only as a binder in SEC (135), SF (139),
   `exposedPoints` (851), `KInf1` (1013). No structure field and no hypothesis links it to `ElementaryDrivability`
   (264–276) or to anything ontic. `grep ElementaryDrivability|KInfFoundations.` outside KF: only the aggregator
   `OIBridge.lean:246 import`. So no landed module consumes KF or supplies its `avail`.
2. `ball3Drive` (KF:449): flow = `rot3` (rotation about axis 2), N = flow π, J = `cyc3` (order 3).
3. Equivalence.lean `RevReal` (157): `traj` (176) = `(step^k s).1`; `law` (180) = pushforward of `init` along
   `traj`. The time-k readout is `vis ∘ step^k` by definition of the passive law.
4. DomainGlue.lean `ClassicalBranchDomain` (134): constructors `shell` (135), `evolve` (136: w ↦ w ∘ φ),
   `branch` (138). `itiIndicator_mem` (156): every itinerary indicator — the passive law's own events — is in it.
5. ObservabilityQuotient.lean `BranchDomainK` (108, `evolve` 112), `branchDomainK_invariant` (127),
   `branchDomain_span_eq_itineraryInvariant` (270), `classicalBranchDomain_iff_horizon` (281),
   `itiRelInf_iff_orderOf` (304), `classicalBranch_span_eq_invariant` (316).
6. PassiveQuotient.lean: `itiRelInf_symm_evolve` (118) uses φ⁻¹ = φ^(orderOf φ − 1); `quotPerm` (168),
   `quotMeasure_evolve` (393), `quotMeasure_branch` (410), `trajProb` (339).
7. ControlledQuotient.lean (field-neutral; no Matrix/ℂ): `actWord` (56), `ctrlRel` (79) = agreement of
   `vis ∘ actWord w` for every word of a menu `acts : A → Equiv.Perm S` (a free parameter);
   `ctrlRel_symm_evolve` (100), `ctrlRel_le_itiRelInf` (112). This is the only field-neutral active law found.
   It is a relation/quotient, not an availability family, and its menu is finite-carrier permutations.
8. StructuralClosure.lean `substratum_residual` (383): substratum (monomial) class does not drive elementary
   transitions. RouteB.lean `substratumTheory_falsifierUnavailable` (302), `routeB_target` (384): matrix layer.
9. OperationalAssembly.lean `FiniteOperationalTheory` (594), `availExt_bind` (617), `readout_avail` (642):
   the matrix theory postulates feed-forward composition and readout availability. Cited only as postulates.
10. Field-neutral module census (no `Matrix`/`ℂ` token): Averaging, BackgroundIndependence, C3Necessity,
    CanonicalMeasure, CombRealization, ControlledQuotient, EdgeRigidity, FactorUniqueness, FiniteEntropy,
    Finiteness, GaugeDimension, HiddenMemory, HomometricSix, HydroSourceAudit, IdempotentTrace, Irreducibility,
    LevelOneRecursion, PiccardBridge, Reciprocity, TasteBranching. (DomainGlue/PassiveQuotient/
    ObservabilityQuotient import ℂ for the glue theorems, but their branch-domain/quotient parts are
    real/combinatorial.) `inductive` census: only `ClassicalBranchDomain` and `BranchDomainK` are field-neutral
    closure inductives with a precomposition constructor; the rest (PolGen, Gen2, InstAvail, archGen, PolC,
    FlowR, MixR, Gen, Step, VStep) are matrix-typed.

## Exact checks
`i_checks.py` (Fractions only). Run 1 (`i_checks.run1.out`): 31/32 PASS, one FAIL — check A2 asserted that the
least horizon at which r∘φ⁻¹ enters span(BranchDomainK K) equals orderOf φ = 5; measured 4 (at K = 4 the
itinerary 0000 already isolates s = 1). Expectation was wrong, not the code. Corrected check computes the
horizon and states the measured split: span horizon 4, direct constructor-term horizon 5. Run 2
(`i_checks.out`) `OK -- 33 checks, 0 failures`, replay identical (`rerun.out`).
sha256(i_checks.py) = 23d7b1b367b1f4c27d4fd49cedbc6db2c94b6113b32702198060ac9567bc839b.
B2's effect check on the ball is on the half-integer grid only; the analytic statement (|v₂| ≤ 1 on ball3) is
immediate.

## Skeptic pass on the favourable branch (a)
- Is `evolve` a hidden closure postulate? It is a constructor of an inductive *definition*: membership is
  by construction, so "derived" must rest on the operational licence, which is the passive multi-time law
  (time-k readout = vis∘φ^k in `RevReal.traj`, `itiIndicator`). The constructor is restricted to the single
  generator φ (A3: a transposition outside ⟨φ⟩ leaves the span, by OQ:316). Not the forbidden general closure.
- Inverse direction: only via finiteness (φ⁻¹ = φ^(ord−1)); costs horizon (A2). In an infinite carrier the
  inverse would not be a forward time shift (CombRealization's ℤ remark shows finiteness is load-bearing
  elsewhere too).
- Scope: the result lives on the finite carrier / minimal carrier. No landed map takes it to KF's `avail`.
- Content: passive transport of a diagonal seed is diagonal (A4; `substratum_residual`), so ⟨φ⟩-orbit
  availability never supplies off-axis effects. Derived but inert for the K∞ use.
