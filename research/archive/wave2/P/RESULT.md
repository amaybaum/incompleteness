# Thread P — V4′, the seed-orbit availability licence (read-only at L)

L = `f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`. Paths are under `verification/lean-mathlib/OIBridge/`.
Abbreviations: KF = KInfFoundations, OG = OrbitGeneration, ON = OrbitNormalization, OA = OperationalAssembly,
IL = ImplementationLocality, SS = SubstratumSource, MR = MicroscopicReversibility, DC = DiscreteCompletion.

Evidence levels:
- **kernel**: a landed identifier at L, cited by file:line.
- **exact**: `p_checks.py`, sympy exact arithmetic. Result `OK -- 37 checks, 0 failures`; the replay is
  identical. sha256 prefixes: script `55fc4a7c…`, output `68ee6f0b…`. Run 1 had one failure, a wrong
  expectation (NOTES.md, script log), kept in `p_checks.run1.out`.
- **written**: an argument given here.
- **candidate**: Lean text in `candidate_SeedOrbitLicence.lean.txt`. It is not compiled and proves nothing.

## Verdict

- **V4′ cannot yet be licensed.** At L the field-neutral vocabulary has no notion of an available
  transformation and no sequential composition (kernel absence, §1).
- **Minimal extension.** The smallest extension that can state the licence is a single-system record: available
  effects plus available transformations. Three named premises then give V4′ on the drive's words:
  - **SEED-AVAIL**: the seed r is an available effect;
  - **SEQ**: an available effect read after an available transformation is available;
  - **TRANS±**: the flow, J and J⁻¹ are available transformations.
- **The statement is a genuine implication, but not a discharge.**
  - V4′ on the words is *equivalent* to the existence of some subfamily that contains r and is closed under the
    generators (P-2).
  - So the candidate licenses V4′ only if the effect family and the transformation set are fixed independently of
    the seed orbit, and SEQ and TRANS± have a source of their own.
  - Neither SEQ nor TRANS± has a source at L, in any field. In the ℂ regime both are postulated or definitional
    (§3).
- **Status.** V4′ stays **open**. Its content is relocated into three named premises, each shown load-bearing by an
  exact countermodel in which the other two hold.

Gem classification (§A.31):
- **NEW** — G2, the decomposition with its independence certificates.
- **ELABORATING** — G1 (only one system is needed) and G3 (exact availability vs limit closure).
- **CONFIRMING** — G4 (V4′ contains SEED-AVAIL).
- **BORDERLINE** — G5 (whether J⁻¹ must be named separately).

***

## 1. Question (1): what composition makes r ∘ g⁻¹ available

**The composition.** "Apply the reversible operation g⁻¹, then read r":
- In the Schrödinger reading, the state x is carried to g⁻¹x and then read, so the outcome probability is
  r(g⁻¹x).
- The test is therefore `r.comp g.symm.toAffineMap`, which is `seedTransport r g` (OG:49–53).
- V4′ (OG:74) asks for this test to be available for every g ∈ G.

**What the landed vocabulary offers (kernel; grep at L).**
- KF provides:
  - bodies and effects (`IsEffectOn` KF:116);
  - `SupportingEffectComplete` KF:135, `SingletonFaces` KF:139, `fullEffects` KF:149;
  - `ElementaryDrivability` KF:264–276: flow, J, and their preservation of Ω;
  - `CopyNatural` KF:284.
- **No availability anywhere.** None of the `ElementaryDrivability` fields mentions availability. The structure
  states that certain affine maps are automorphisms of Ω; it does not state that an observer can perform them.
- OG adds the function `seedTransport` and the named propositions. ON adds `words` (ON:53) and the
  premise-free G-AUT step `preservesBody_words` (ON:79).
- **Nothing anywhere states that a transformation is available, or that availability is closed under sequential
  composition.**
- KF, OG and ON are imported only by the aggregator (`OIBridge.lean:246–248`).
- The only field-neutral constructions closed under precomposition are not connected to KF's
  `V →ᵃ[ℝ] ℝ`. Both live on finite carriers `S → ℝ` and act by permutations:
  - `ClassicalBranchDomain.evolve` (DomainGlue:136);
  - `actWord` / `ctrlRel` (ControlledQuotient:56/79).

**Minimal definitional extension (candidate, §B of the .lean.txt).**
- `BodyOperationalTheory Ω` has fields `eff`, `trans`, `eff_effect`, `trans_maps`.
  - The last two are consistency fields only.
  - Control E5: a transformation that leaves Ω, here 2·id, would force `r ∘ T` to take the value 3/2. That is not
    an effect.
- `SeqClosed Θ := ∀ e ∈ eff, ∀ T ∈ trans, e ∘ T ∈ eff`. This is a named proposition, deliberately not a field, so
  that it has countermodels.
- `DriveAvailable Θ D := (∀ t, D.flow t ∈ trans) ∧ D.J ∈ trans ∧ D.J.symm ∈ trans`.
  - The flow needs no separate inverse clause, because `(D.flow t).symm = D.flow (−t)`. This is `drive_flow_symm_apply`
    (OG:150) followed by `AffineEquiv.ext`.

**Circularity check (written; it becomes kernel via candidate P-2).**
- P-2: `SeedOrbitAvailable (words S) r avail ↔ ∃ A ⊆ avail, r ∈ A ∧ GenClosed S A`.
  - (→) Take A = `seedOrbit (words S) r`. Then (r∘g⁻¹)∘s = r∘(s⁻¹g)⁻¹, and s⁻¹g is a word.
  - (←) Monotonicity, then P-1.
- So the closure axiom, **restricted to the seed's orbit, is V4′ restated.**
- On the whole family, closure under the generators is strictly stronger than V4′:
  - CM3 (exact E4): avail = `directionalFamily` ∪ {`unsharpSeed`} satisfies V4′ by `seedOrbit_ball3Drive` (ON:679).
  - But `unsharpSeed ∘ J⁻¹ = 3/4 + v₀/4` is neither directional (its constant term is not 1/2; compare
    `ball3_sharp_eq` OG:278) nor `unsharpSeed`.
- Hence the candidate is a licence only when (eff, trans) are given before the orbit is known. With
  `eff := seedOrbit`, V4′ holds by definition (`seedOrbitAvailable_self` OG:144) and nothing is licensed.

## 2. Question (2): exact words vs closure

**(a) Exact finite words.**
- `boundaryTransitive_ball3Drive` (ON:667) is exact on finite words. Every sphere point is
  `(rot3 ψ * rotX θ) e_z` (`exists_word_pole` ON:658), with `rotX θ = cyc3 · rot3 θ · cyc3⁻¹` (ON:581).
- The angles ψ, θ are arbitrary reals built from arccos (`exists_euler_angles` ON:614).
- So (a) needs, exactly:
  - SEED-AVAIL;
  - SEQ;
  - `rot3 t ∈ trans` for every real t — a continuum of exactly available operations;
  - `cyc3 ∈ trans`.
- `cyc3⁻¹` need not be named separately, because cyc3³ = 1 (exact E1.2). Hence `e ∘ cyc3⁻¹ = (e ∘ cyc3) ∘ cyc3`
  (E1.6).
- Candidate P-6 then reaches every `ballEffect b` with Σb² = 1 through `ballEffect_mem_avail` (OG:369),
  `preservesBody_driveWords3` (ON:674) and `boundaryTransitive_ball3Drive` (ON:667).
- No limit is used.

**What fails with fewer operations (exact E8).**
- Take generators fixed at one angle: S = {rot3(arccos 3/5), cyc3}.
- Every word is a rational orthogonal matrix. Checked for all 5461 words of length ≤ 6; written for all lengths,
  since rational matrices are closed under products and transposes.
- So the orbit of e_z is rational, and `ballEffect(√2/2, √2/2, 0)` is not in the seed orbit.
- Therefore `BoundaryTransitive ball3 (words S)` fails, and OG-1's theorem does not apply. This holds even though
  ⟨S⟩ is dense in SO(3): rot3(arccos 3/5) has infinite order (E8.5 to n = 60; Niven, written).
- This is the field-neutral shadow of `fixedGateTheory_not_qm` (DC:1948; countability through
  `mixTheoryR_not_qm` StateMixingCoupling:679).

**(b) Closure.** Recovering the directional family from countably many available transformations would
additionally need three things:
- **LIMIT**: a field-neutral limit closure of `eff`, e.g. closure under uniform convergence on Ω. This is the
  analogue of `ClosureAvail` (DC:63), which the corpus defined but deliberately did not adopt ("dense
  availability is never identified with exact availability", DC:13).
- **DENSE**: a density theorem for the generated group in a boundary-transitive group. Not field-neutral at L.
  The ℂ analogue is `fixedGateTheory_denseUnitaryControl` (DC:1942) for `DenseUnitaryControl` (DC:45).
- **CONT**: the continuity bound |be(b)(v) − be(b′)(v)| ≤ |b − b′|/2 on the ball. Written (Cauchy–Schwarz); exact
  instance E9.
- With LIMIT, J⁻¹ also comes for free on a compact automorphism group, since a closed submonoid of a compact group
  is a subgroup (citation-level, standard).

**Recommendation.** Do not pursue (b) while D3 stays unadopted. (a) suffices for the landed control drive.

## 3. Question (3): the landed matrix-regime analogue

**The theorem.** `circuit_available` (OA:757): prepare, apply `conjChannel U`, read the ancilla, discard; the
result is an available family on the system. It is assembled from three ingredients:
- **op**: `HasCompositeUnitaryControl T` (OA:665), a named hypothesis: every unitary on `A × Fin n` is available;
- **bind**: `availExt_bind` (OA:617), a **structure field** of `FiniteOperationalTheory` (OA:594), i.e. postulated;
- **readout**: `readout_avail` (OA:642), a structure field. Its form is derived (`readout_is_localLuders` OA:658),
  its existence is not.

**The generated version.** In `genTheory` (IL:852), availability is *defined* as the inductive `InstAvail`
(IL:268), so its pieces hold by construction:
- bind = constructor `InstAvail.bind` (IL:280);
- op = `InstAvail.op` (IL:271), which needs `𝓘 T K`, supplied by `DrivesElementary` (SS:77) through
  `genTheory_avail_conj` (SS:103);
- readout = `InstAvail.readout` (IL:273);
- inverse availability is the separately named `DaggerStable` (MR:216). It is a field of `QuantumArchitecture`
  (SS:86) next to `drives`.

**What it imports, and why it cannot be a field-neutral source.**
- Every object is typed `Matrix _ _ ℂ →ₗ[ℂ] Matrix _ _ ℂ`.
- The state space is the imported density-matrix body, and the readout form uses the ℂ uniqueness theorem
  `mapSpectatorIndependent_iff_localLuders`.
- More basically, even there SEQ is not derived. It is either postulated (`availExt_bind`) or true by definition
  of an inductive closure (`InstAvail.bind`).
- The matrix regime therefore confirms the *shape* of the decomposition. It supplies no evidence for SEQ or
  TRANS±.
- G1 (ELABORATING): the field-neutral licence uses three of `InstAvail`'s five constructors, namely readout→SEED,
  op→TRANS and bind→SEQ. `coarse` and `discard` are not needed, and neither are composites.
  - G's C8 needed a register and a discard because its sharp readout lived on a register.
  - OG-1's P1 puts the sharp seed on Ω itself.
  - Pressure test: this reduces the vocabulary needed; it adds no evidence. SEED-AVAIL is still unsourced. In the
    ℂ regime, a system-level readout is `InstAvail.readout` with trivial spectator and needs `arch.proj`, which is a
    hypothesis on the class.

## 4. Question (4): countermodels (exact, on ball3 / ball3Drive; seed r = `ballEffect e₂`)

For every row:
- P1 holds (E2.1; `ballEffect_sharp` OG:233);
- `PreservesBody ball3 driveWords3` holds (ON:674);
- `BoundaryTransitive ball3 driveWords3` holds (ON:667);
- `ball3Drive` exists (KF:449).

Only the premise named in the first column is broken.

| id | eff | trans | fails | holds | V4′(driveWords3) | checks |
|---|---|---|---|---|---|---|
| CM1 | {be e₂, be(−e₂)} (a perfectly distinguishing pair) | driveWords3 | SEQ | SEED, TRANS± | fails: r∘cyc3⁻¹ = be e₀ is 1 at e₀, while both members give 1/2 | E2 |
| CM2 | {be e₂, be(−e₂), 1, 0} | range rot3 | TRANS(J) | SEED, SEQ (closed under every rotation about z) | fails: be e₀ ∉ eff | E3 |
| CM2′ | {be e₀, be e₁, be e₂} | {1, cyc3, cyc3⁻¹} | TRANS(flow) | SEED, SEQ | fails: r∘(rot3(arccos 3/5)·cyc3)⁻¹ = be(3/5, 4/5, 0) ∉ eff | E10.3–5 |
| CM0 | {1, 0} | driveWords3 | SEED | SEQ, TRANS± | fails at g = 1 | E10.1–2 |
| CM3 | directionalFamily ∪ {unsharpSeed} | — | generator closure of the whole family | V4′ | **holds** | E4 |
| NEC | fullEffects ball3 | {1} | TRANS (and SEQ is vacuous) | — | **holds** (`isEffectOn_seedTransport` OG:94 for any G with PreservesBody) | written + kernel |
| C+ | fullEffects ball3 | fullAut3 (OG:521) | — | all | holds | written + kernel |

Conclusions:
- SEED, SEQ and TRANS± are pairwise independent, and each is load-bearing given the other two (CM0, CM1, CM2,
  CM2′).
- Together they are sufficient (P-4), not necessary (NEC).
- The only necessary-and-sufficient form is P-2.
- Requested countermodel 2 (effects closed under precomposition but the transformations not available) is
  meaningful: CM2 and CM2′ realize it with V4′ failing. NEC realizes it with V4′ holding, so the distinction
  between operational availability and invariance of the effect family is real.

## 5. Deliverable (COMMON-LIMITS item 9)

### (a) Candidate theorem statement (candidate; full text in `candidate_SeedOrbitLicence.lean.txt`)

```lean
theorem seedOrbitAvailable_of_operational {Ω : Set V} (Θ : BodyOperationalTheory Ω)
    (D : ElementaryDrivability Ω) {r : V →ᵃ[ℝ] ℝ}
    (hseed : r ∈ Θ.eff)                 -- SEED-AVAIL
    (hseq : SeqClosed Θ)                -- SEQ
    (htrans : DriveAvailable Θ D) :     -- TRANS± (flow, J, J⁻¹)
    SeedOrbitAvailable (words (Set.range D.flow ∪ {D.J})) r Θ.eff
```

Companions:
- P-1 `seedOrbitAvailable_of_genClosed` (generic, any S);
- P-2 `seedOrbitAvailable_words_iff` (the circularity certificate);
- P-3 consistency;
- P-5 `cyc3_symm_eq_sq`;
- P-6 `directional_available_of_operational`, the ball corollary. It takes P1, SEED, SEQ, `∀ t, rot3 t ∈ trans`
  and `cyc3 ∈ trans`.

### (b) Dependency chain

- P-1: `words` (ON:53), `Subgroup.closure_induction` (used in the same way at ON:84), `mul_apply'` (ON:69),
  `inv_apply'` / `symm_eq_inv` (ON:73–75), `seedTransport` (OG:49). **No open premise.**
- P-2: P-1 plus `seedOrbit` (OG:60). **No open premise.**
- P-4: P-1, `drive_flow_symm_apply` (OG:150). **Open premises: SEED-AVAIL, SEQ, TRANS±**, all named and unsourced.
- P-6: P-4 restricted to the generators, then `ballEffect_mem_avail` (OG:369), `preservesBody_driveWords3` (ON:674),
  `boundaryTransitive_ball3Drive` (ON:667). From there, `lorentz_of_available` (OG:422) carries it to
  `lorentz_of_effects` (NativeGateBall:105). **Open premises: P1, SEED-AVAIL, SEQ, TRANS(flow, J).**
- Missing for the (b) route: LIMIT, DENSE (both absent field-neutrally) and CONT (written).
- Missing for a *discharge* of V4′: an independent source for SEQ and TRANS±. No landed construction supplies one,
  in any field; ℂ supplies the shape only (§3).

### (c) Countermodel and circularity audit

- **Per hypothesis:** SEED → CM0; SEQ → CM1; TRANS(J) → CM2; TRANS(flow) → CM2′.
- **TRANS(J⁻¹):** redundant on ball3Drive (E1.2). For an infinite-order J (exact E7: rotation about x with
  cos = 3/5), J⁻¹ = rot3(π)·J·rot3(π) is again a forward word. Whether it is redundant in general is not settled
  (G5, BORDERLINE).
- **`eff_effect` / `trans_maps`:** unused by P-4; E5 shows why `trans_maps` is needed for consistency.
- **P1 and K∞-R:** OG-1's own controls, `not_boundaryTransitive_flow` (OG:620) and `not_seedOrbit_unsharp_eq`
  (OG:670).
- **No step imports the conclusion.** P-4 derives V4′ from premises that do not mention the seed orbit. P-2 is
  stated precisely so that a premise which *does* mention it (eff := seedOrbit) is recognizable as V4′ restated.
- **No dimension three.** P-1, P-2 and P-4 are over an arbitrary real normed V. ball3 appears only in P-6 and in the
  controls, as an instance. Nothing is taken from NB-1.
- **No sourced drive.** D is a hypothesis. `elementaryDrivability_of_substratum` is absent from the tree at L
  (grep). No route through the substratum is used.

## 6. Recommendation

**What is ready.** A small preregistered kernel round, "the operational decomposition of V4′", is admissible:
G2 passes the productivity test (strictly stronger than the restatement; independence certificates).
- **Scope:** P-1, P-2, the record with SEQ and TRANS as named propositions, P-4, P-5, P-6, and controls CM0, CM1,
  CM2, CM2′, CM3, NEC, C+ and the countable negative CN (E8).
- **Decision rule, preregistered:** the round's verdict may say only "V4′ ⟸ SEED-AVAIL ∧ SEQ ∧ TRANS±, each
  load-bearing, jointly satisfiable (C+), not necessary (NEC), and equivalent to generator-closure of a subfamily
  (P-2)".
- **Status after the round:** V4′ stays **open**. Its manuscript label may move from "named hypothesis" to
  "conditional on SEQ and TRANS±" only if the corpus adopts the record. Correctness bands are unchanged; this is
  consistency-axis work.

**What it must not do.**
- It must not call V4′ derived.
- It must not adopt LIMIT/D3.
- It must not identify TRANS± with `ElementaryDrivability`: CM2 shows the drive's existence does not make it
  available as an operation.

**What remains open.** A real licence needs an independent source for SEQ (an operational-closure principle of
OI) and for TRANS± (that the drive is executable before a readout). The latter is the field-neutral counterpart of
`DrivesElementary ∧ DaggerStable`. Until such a source is in view, the round is bookkeeping. Under §A.28 it should
be opened only if a status surface needs the decomposition; otherwise keep it record-only, here.

## Files
- `RESULT.md` — this report.
- `NOTES.md` — DFS nodes and the productivity test.
- `p_checks.py`, `p_checks.out`, `rerun.out` — the replay; `p_checks.run1.out` — the failed run 1.
- `candidate_SeedOrbitLicence.lean.txt`.
