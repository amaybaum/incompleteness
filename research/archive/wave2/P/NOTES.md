# Thread P — working notes (V4′ licence)

Base: L = f7f5c3b0c621cc3e4b57e3709d11d9d580c81149, worktree wave2/wt-P-v4prime (clean, detached).
Read: COMMON-LIMITS.md; OIBridge/{OrbitGeneration, OrbitNormalization, KInfFoundations, OperationalAssembly,
ImplementationLocality §InstAvail/§genTheory, SubstratumSource §DrivesElementary/QuantumArchitecture,
MicroscopicReversibility §DaggerStable, DiscreteCompletion §A and §Canonical, TypedCompletion §B};
background threads G/REPORT.md, I/RESULT.md, M/RESULT.md (V4′ rows) — every claim re-checked at L.
No wave-2 sibling directory read. No Lean/lake run.

## Productivity test (fixed before starting)
A gem iff the thread yields a fact strictly stronger than "V4′ follows from a closure axiom" (the obvious
restatement) AND that fact constrains the licence (an independence/necessity certificate, a minimal vocabulary)
or exposes a hidden assumption. Otherwise record-only.

## DFS nodes
N1  Field-neutral vocabulary has transformations / sequential composition?  CHECK grep at L.
    KF defines bodies, effects (IsEffectOn KF:116), SEC/SF, ElementaryDrivability (KF:264, maps only), CopyNatural.
    OG adds seedTransport (OG:49) — precomposition as a function, no availability. Importers of KF/OG/ON: only the
    aggregator OIBridge.lean:246-248. No `trans`/`availTrans` anywhere outside ℂ modules. VERDICT: absent.
N1.1 Field-neutral precomposition constructs elsewhere: DomainGlue `ClassicalBranchDomain.evolve` (DG:136),
    ControlledQuotient `actWord`/`ctrlRel` (CQ:56/79): finite carriers S → ℝ, permutations, not KF's
    V →ᵃ[ℝ] ℝ; no map into KF. VERDICT: not usable.
N2  Minimal extension: record (eff, trans) + SEQ + TRANS. Does SEQ restate V4′?  CHECK algebra.
    V4′(words S) ⟺ ∃ A ⊆ avail, r ∈ A, A generator-closed (witness seedOrbit; (r∘g⁻¹)∘s = r∘(s⁻¹g)⁻¹).
    SEQ on the whole family strictly stronger: CM3 (E4). VERDICT: implication genuine; content = V4′ unless
    (eff, trans) fixed independently of the orbit.
N2.1 Is SEQ alone enough with a native sharp readout?  CM2 (E3): no, J must be available. CM2' (E10.3-5): flow too.
N2.2 Is TRANS alone enough?  CM1 (E2): no.
N2.3 Is SEED-AVAIL inside V4′?  1 ∈ words, so yes; CM0 (E10.1-2). CONFIRMING (OG-1 docstring, M row P2).
N2.4 Are SEQ, TRANS necessary?  No: (fullEffects ball3, {1}) has V4′ (OG:94). Sufficient route only.
N2.5 J⁻¹: ball3Drive J³ = 1 (E1.2) so redundant; infinite-order J example (E7) inverse via flow half-turn.
    General: unresolved, not needed. Matrix analogue carries it as DaggerStable (MR:216), separately named.
N3  Words vs closure.  OG-1 boundaryTransitive_ball3Drive (ON:667): exact finite words rot3 ψ * rotX θ
    (ON:658-663), ψ, θ real (arccos-based, ON:614). So (a) needs flow(t) ∈ trans for a continuum of exact t.
    Countable trans: words rational (E8) → orbit misses (√2/2, √2/2, 0) → ¬BoundaryTransitive. (b) needs LIMIT
    (D3 analogue) + group density + continuity bound (E9). Matrix analogues ℂ-only (DC:45, DC:1942, DC:63).
N4  Matrix analogue: circuit_available (OA:757) = op (HasCompositeUnitaryControl OA:665) + bind (availExt_bind
    OA:617, a field) + readout (readout_avail OA:642, a field). genTheory (IL:852): bind := InstAvail.bind
    (constructor IL:280), op := InstAvail.op (IL:271) needing 𝓘 ∋ U (DrivesElementary SS:77). All over
    Matrix _ _ ℂ; SEQ is postulated (field) or definitional (inductive closure), never derived.
N5  Circularity / item 9(c): general theorem over arbitrary V; no NB-1, no dimension 3; drive is a hypothesis;
    elementaryDrivability_of_substratum absent from tree at L (grep). OK.

## Outputs
NEW        G2 — V4′ conflates two independent operational premises (SEQ, TRANS±) plus SEED-AVAIL; each has an
           exact countermodel with the other two holding; and the precise iff (generator-closed subfamily).
ELABORATING G1 — minimal extension is single-system: three of InstAvail's five constructors (readout, op, bind);
           coarse and discard unused, no composite/register (G's C8 needed them for a register readout; OG-1's P1
           puts sharpness on Ω). Pressure-tested: a vocabulary reduction, not an evidence gain.
ELABORATING G3 — exact (a) needs a continuum of exact flow operations; fixed-angle trans fails BoundaryTransitive
           exactly (rational witness); (b) needs LIMIT + DENSITY, neither field-neutral at L.
CONFIRMING G4 — V4′ contains SEED-AVAIL.
BORDERLINE G5 — J⁻¹ availability (TRANS±): redundant on controls, general status open.
Fixed point: passes over N3, N4, N5 gave no NEW after G2.

## Script log
run 1: 37 checks, 1 FAIL (E10.4): wrong expectation — I took cyc3 e2 = e1; cyc3 (v0,v1,v2) = (v2,v0,v1)
gives cyc3 e2 = e0, so the transported seed is be(3/5, 4/5, 0), not be(-4/5, 3/5, 0). Kept as p_checks.run1.out.
Corrected expectation; E10.5's conclusion unchanged (the point is outside the closed family either way).
run 2 (p_checks.out) = replay (rerun.out): OK -- 37 checks, 0 failures; replay identical.
