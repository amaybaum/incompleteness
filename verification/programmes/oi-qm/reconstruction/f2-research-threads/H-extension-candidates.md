# Thread H: candidate extension principles past the frozen-sourcing barrier, ranked

**Base.** M = `5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5`. Every repository `file:line` was read in the
detached worktree `scratchpad/threads/wt-H` at M. Lean paths are under
`verification/lean-mathlib/OIBridge/`. ROADMAP = `verification/ROADMAP.md`, PROGRAMME =
`verification/programmes/oi-qm/PROGRAMME.md`, FSA = `verification/programmes/substratum/frozen-sourcing-audit.md`.
I also read these branches (not merged at M): `origin/draft/oi-state-operation-source-1` @75c38757,
`origin/research/state-operation-source-design-20261013` @24dabc9d,
`origin/plan/compatibility-source-20261013` @f48b11fd, and the planning placeholders
`origin/plan/drive-source-20261013` @9fc5ec2e, `origin/plan/p0-evolution-source-20261013` @1bcc8cb6 and
`origin/plan/joint-tests-source-20261013` @0e0b3ddc. Nothing in the repository was edited, no branch was
moved and nothing was pushed. Lean was not compiled. This is research only: it changes no status and
proposes no manuscript text.

**Labels.**

- [K] kernel theorem or definition at M.
- [D] design: an unadopted branch, draft or placeholder.
- [W] written argument here.
- [X] exact computation.
- [N] numerical computation (float64) whose controls are green. I added this label because several
  probes are numerical and must not be read as [X].
- [U] unsourced.
- [L] literature.

Probes are in `scratchpad/threads/H-work/`: `probe_H.py` (33 checks, all PASS, output in
`probe_H.out`) and `probe_H2.py` (output in `probe_H2.out`). Run them with `python3 -I`; they need
numpy and scipy.

***

## 0. What a candidate has to beat

The frozen-sourcing no-go is stated through `NonnegBounded`. A second look at the record shows that
four further invariants guard the same door. Each one is closed under the kernel's closure operations
or under limits.

| # | invariant | where | what it excludes |
|---|---|---|---|
| I1 | `NonnegBounded`: every available operation preserves entrywise-nonnegative matrices in the configuration basis | FrozenSourcing.lean:65; `permTheory_nonnegBounded` :79, `obsTheory_nonnegBounded` :84 [K] | the phases (:99) and `DenseUnitaryControl`, by two witnesses: the quarter phase (:173) and the phase-free rotation (:199, :240) [K] |
| I2 | configuration level / diagonal preservation | `substratumClass` StructuralClosure.lean:180; `substratum_residual` :383; `not_layerFlowExecutable_of_preservesDiag` (lift-source audit T1) [K] | layer flows and any non-monomial operator, even when the stipulated phases are present |
| I3 | `OnesFixing`: every admissible isometry fixes the all-ones ray | InstrumentRealization.lean:180; `onesClass` :446 contains every gate flow of a layer; `onesTheory_layerFlowExecutable` FlowEndpoint.lean:87, `onesTheory_not_phasesAvailable` :177, `onesTheory_not_qm` :205 [K] | the phases. Also dense control [W]: the condition K·1 = z·1 with \|z\| = 1 is closed under norm limits, and the quarter phase on one configuration moves the ray. This step is not a kernel theorem. |
| I4 | countable projective image | `uncountable_of_layerFlowExecutable` PolarizationClosure.lean:135; `polarizedTheoryC_not_pairFlowSourced` PairFlowEquivalence.lean:211 [K] | exact flows, and so exact QM through `qm_iff_derivedOI_pairFlowSourced` PairFlowEquivalence.lean:199 [K] |
| I5 | **new here:** at odd q, Wigner positivity in the substratum's own per-site (previous, current) frame | [N] P2.d, P2.a, P6.b; [L] Gross 2006 (J. Math. Phys. 47, 122107); Veitch, Ferrie, Gross, Emerson 2012 (New J. Phys. 14, 113011) | density, for every candidate whose operations are images of affine-symplectic substratum maps. I5 is I1 moved into another frame (§7, AW-H1). |

**A consequence for the F2 target [W from K].** Take any sourcing map that assigns operations only to
processes of a finite substratum. There are countably many finite carriers, each with finitely many
bijections, and countably many closure steps. This is the counting argument the polarization closure
audit uses (`verification/audits/foundations/polarization-closure-audit.md:55–65`), so the map's
projective image is countable. By I4, exact finite operational QM is then out of reach. The most such
an extension can reach is `DenseFiniteQM` (DiscreteCompletion.lean:59). Exact QM needs an added
continuum, such as a real duration or a real coupling.

So F2 carries a decision the owner has to make: target `DenseFiniteQM`, or accept a continuum as a
named principle.

***

## 1. Harvest from the corpus (§A.19)

| source | what it says | status at M |
|---|---|---|
| **A6** | Substratum.md:102: covariance under site-dependent internal-index transformations G(n), with the link coupling transported as M → G M G⁻¹ | FSA:43–46: "a gap with no predicate". ROADMAP:65: `CONDITIONAL`, with the meaning `A6Cov`. `a6cov_all` BackgroundIndependence.lean:161 holds identically, so the covariant form carries no constraint. The complex carrier fails A1: `cx3b_complex_not_A1` A6Instantiation.lean:512; a6-instantiation/result.md:260–285 [K] |
| **Observer-level lift rows** | ROADMAP:1496–1500: phases, dense control, executable intermediate layer flow and the stated lift are all `INDEPENDENT` | Formulations L1, L2 and L4 are representational. L3, the harmonic wave-operator lift on ℂ^sites, is underdetermined: no map to ℂ^Conf is stated. Lift-source audit :293–322; `coherentLiftClass_eq_substratumClass` LiftSource.lean:164 [K] |
| **Arc D** | PROGRAMME:450–468: "whether the currently missing continuous off-diagonal control resource can be derived from a deeper OI condition, or whether it is genuinely an independent empirical principle" | The sufficiency side is closed (`krausDense_of_denseControl`, `fixedGateTheory_denseFiniteQM`). The sourcing side is the FSA no-go. GR.md:258 states that "a selectable local coupling that is a bijection at every parameter value induces only permutation operators" |
| **Track B** | PROGRAMME §3.13–3.19 (:220–340): the Barandes lift is not fixed by the visible data. Act 5 `SA2`: the identity against the swap on the same Γ. Act 6 `UB2`. Act 7 `DC2a` | No operation sourced. Arc D's RD1 quarantine applies: representational presence sources nothing (PROGRAMME:104–112) |
| **Continuous time** | Track B act 8 `CE1` (track-b/act-08-continuous-extension/result.md:1–40) concerns the visible stochastic law, not operations. The continuous-time audit:72–86 shows each layer is an involution with an exact one-parameter group `unit g t = 1 + (e^{iπt} − 1)p` | The interpolation is extra structure and is not unique: `flows_differ_half` RegionLimit.lean:281, `continuous_extension_not_unique` :296; GR.md:84 on the logarithm branch; ROADMAP:1529 [K] |
| **H-Bell** | Substratum.md:130–132: preparation-indexed graphs must (i) supply ontic parameter dependence, (ii) preserve no-signalling, and (iii) keep Ollivier–Ricci stability | ROADMAP:67 `OPEN`. `h-bell/round-hb-1-obligation-shape/` has a preregistration only. SM.md:102: bijectivity holds "regardless of whether the coupling is state-dependent" |
| **"C5"** | c5-discovery-audit.md:78–106 tests two families: tunable coupling (dead) and symplectic polarization | Verdict C, underdetermined (:228–268). The polarization closure audit then found O1 positive and O2 negative for `PolC`. `grep` finds no "C5" in `papers/` or `book/` [X] |
| **P0 selection** | ROADMAP:63; acts 11–17. TJ1: no cross-time coupling. TJ3: four frozen selectors fail at one configuration (ROADMAP:542–600) | `OPEN`. No selection principle adopted |
| **Interface drafts** | draft/oi-state-operation-source-1 (withdrawn before F, preregistration.md:3–7): LC is insufficient, DT restates preservation, PS grants Q3 inclusion (:63–73, :136–160). Compatibility research (@f48b11fd, `spectrality-preservation-research/result.md`): SP ⇒ stopped-map preservation stays OPEN; coPSD is preserved by every local CP branch, fails CNOT, and excludes the Bell projector | [D]. Lesson: local consistency does not fix the joint cone. A source has to fix the state cone and the entangling operations together |
| **Manuscripts' own motivation** | Main.md:296–320: the visible channel of the linear F₂ update has a Clifford-conjugated Weyl-mixture normal form. Main.md:568: with the phase intervention stated, QM holds exactly when one layer flow is executable. Main.md:424–425: the slow-bath motivation assumes a Hamiltonian ETH hidden sector. GR.md:258: the phase intervention as an "intervention principle" | The Weyl/Clifford structure is already present at representation level. The ETH motivation presupposes quantum dynamics (AW-H4) |

***

## 2. The candidates, ranked

### E1 (rank 1, recommended): stroboscopic Weyl registration, R ⊕ T

**(a) The principles in OI's terms.**

- **R, registration.** An embedded observer registers the instantaneous value of an accessible site:
  the current component of the substratum's per-site pair (previous, current) (SM.md:100–102;
  continuous-time audit :34–46). It never registers both components in one act. The previous component
  is incompleteness inside the site, traced out under the canonical counting measure (Main.md:56–60).
  - The observer's description of N registered sites is an amplitude function on V^N, with V = ℤ/q.
  - A substratum process that preserves the symplectic form acts on the description by its Weil image
    (Weil 1964, Acta Math. 111, 143 [L]). Such processes are the leapfrog with a symmetric coupling,
    translations, and couplings to embedded meters through the substratum's own linear dynamics.
  - The image is fixed up to phase. The intertwiner nullspace is one-dimensional in every tested case
    [N P2.a].
- **T, stroboscopic time.** The substratum update is the period-one sample of a continuous evolution of
  the description, generated by the principal logarithm of the update's Weil image. An interaction of
  any real duration is an operation, for any observer-selectable symmetric coupling or source term.
  This is the "selectable local coupling" of GR.md:258, made symplectic.

**(b) `NonnegBounded` and the other invariants.** The carrier changes from ℂ^Conf to ℂ^{V^N}, so the
configuration-bijection class is replaced, not enlarged.

- **R alone.** R places the Weil images into availability: the zero-coupling leap's Fourier-type map
  and the chirps. These are not entrywise-nonnegativity-preserving on ℂ^{V^N}, so I1 fails in the
  amplitude frame. But R's theory is Wigner-positive (I5 [N P2.d]). It reproduces the rooted classical
  marginals exactly [N P2.a] and a back-acting classical two-time law [N P6.b], and its group is
  the Clifford group: finite modulo phases. So R
  breaks I1 only in one frame.
- **T.** T is what places I1-, I3-, I4- and I5-violating operations into availability: exp(t·log W(L))
  and exp(t·log X) at non-integer t.
  - [N P4.c]: with the leaps plus translations, the generated Lie algebra is all of u(q^N) at
    (q, N) = (3, 1), (5, 1) and (3, 2). By Jurdjevic–Sussmann 1972 (J. Diff. Eq. 12, 313) [L], the
    reachable set is then the whole unitary group up to phase, so control is exact.
  - [N P4.b]: with the leaps alone, every image commutes with the parity x ↦ −x and the algebra stays
    inside u(even) ⊕ u(odd), dimension 5 of 9 at q = 3.

**(c) Measurements and compatibility.**

- **Tests.** Registration is the native test. A test in another basis is an available unitary followed
  by registration. Validity holds by construction: Born weights of positive descriptions.
- **Registration must be symplectic.** It has to have back-action on the previous component of the
  registered site. The interface's bare read-write copy (`permClass_readWrite`,
  SubstratumInterfaceAudit.lean:412) has no Weil image [N P6.a]. It also keeps a full memory of the
  previous registration, which R forbids [N P6.c]. With a symplectic embedded meter, the two-time law
  coincides with Born statistics [N P6.b].
- **Compatibility.** Operations are conjugations on the same description space, so `PairCompat` holds
  for K = the PSD cone of the registered carrier, and H-CAR is R's tensor product over sites. Both come
  from R's kinematics, not from an independent derivation. The joint-tests placeholder warns against
  exactly this (plan/joint-tests-source @0e0b3ddc). Complex kinematics, the K row, sits in R's
  premises.

**(d) Hard to vary.**

Controls E1 must preserve:

- C-1: OI's rooted visible law at integer times, under the counting measure [N P2.a].
- C-2: the two-time law with an embedded meter [N P6.b].
- C-3: the FSA no-go for the unextended interface. E1 claims nothing for `permTheory`.
- C-4: I4. T introduces the continuum openly.
- C-5: `polarizedTheoryC_not_qm` PolarizationClosure.lean:620.

Predictions and postdictions beyond the barrier:

- P-1 (postdiction). OI's canonical measure on the hidden half (Main.md:56) is exactly the Wigner
  function of a registered-value eigenstate. In the linear sector, OI's rooted visible law is Born
  statistics [N P2.a]; the Born two-time law agrees with a back-acting classical law [N P6.b], not with
  OI's monitored law (check B). This explains why the two descriptions coincide there.
- P-2. A discrete uncertainty and back-action relation. No preparation fixes both components of a site
  [N P2.c], and registration disturbs the unregistered component (P6).
- P-3. Every whole-period protocol is classically simulable [L Veitch 2012; Gottesman,
  quant-ph/9807006]. Nonclassicality enters only through sub-period durations.
- P-4. Parity superselection holds unless the selectable couplings include a source term (P4.b, P4.c).
- P-5. The alphabet must be odd.
  - With the two layers imaged separately (the kernel's construction), q = 2 contradicts OI's own
    visible law. [X P1.d]: H·S²·H = X sends cur = 0 to cur = 1 on the word swap·shear·shear·swap,
    while the classical word leaves cur = 0. [N P1.f]: no pair of single-qubit Clifford layer images
    reproduces the law on all words up to length 8.
  - Imaging the leaps alone at q = 2, two sites: for the coupling M = [[1,1],[1,1]], no Clifford image
    is consistent even under its own powers. For the pair of couplings 0 and I, no image pair is
    consistent [N probe_H2].
- P-6. The controllable algebra is computed from the rule's couplings. The observer theory therefore
  becomes rule-dependent, unlike `obsTheory_rule_independent` (SubstratumInterfaceAudit.lean:779).

Control conflicts E1 must face:

- **q gauge.** P-5 conflicts with SM's q gauge: "All proofs work for any q ≥ 2; no prediction depends
  on q" (SM.md:56, 90–92).
- **Structured priors.** P-2 conflicts with Main.md:60's allowance of structured hidden priors.
- **Read-write interventions.** P6 conflicts with the interface's bare read-write interventions.

Variants rejected:

- R with arbitrary registration logic. A non-affine bijection is not a projective homomorphism image
  [X P3.a]: Toffoli·Z₃·Toffoli is not proportional to Z₃, although the classical maps commute.
- T with an unfixed logarithm branch (RegionLimit.lean:281, :296). The principal branch must be part of
  T's statement before any test.

**(e) The fresh sourcing argument, and the first probe.**

1. **Consistency theorem for R (odd q).** The Weil map on the affine-symplectic process group is a
   projective homomorphism. Integer-time Born statistics equal the classical rooted law, single-time
   and two-time with symplectic meters (Wigner covariance, Gross 2006 [L]).
2. **Lie-rank theorem for T at every N.** Single-site fullness plus one entangling coupling should give
   universality (Brylinski & Brylinski 2002, "Universal quantum gates", Mathematics of Quantum
   Computation [L]).
3. **Carrier-general assembly.** Every finite carrier is a block of some ℂ^{q^N}. Exact control then
   gives `DrivesElementary` (SubstratumSource.lean:77) and `QuantumArchitecture` (:86), and with them
   `genTheory_qm_of_quantumArchitecture` (:136).

The first probe is in §5.

### E2 (rank 2): contextual realization map (Track B lift with a P0 selection)

**(a) Principle.** The observer's description of a realization is a unitary lift of its indivisible
rooted law (PROGRAMME §3.5, §3.17), selected by a named cross-time principle (P0). A visible
intervention acts through the induced change of lift. The map from procedures to substratum processes
depends on the hidden context (memory), not only on the operational class.

**(b) Invariants.** Nothing at M places an operation into availability:

- RD1: representational presence is a disqualified ground (PROGRAMME:104–112).
- `CU1a`, `SA2`.
- TJ1 and TJ3 (ROADMAP:542–600).
- Induced action on visible laws is stochastic with monomial Kraus operators: `stochasticChannel_kraus_monomial`, LiftSource.lean:251.

E2 is the only route in the corpus that is structurally able to avoid both a continuum and I5. Its
state map is not a fixed linear frame, and contextuality is necessary for QM (Spekkens 2008, PRL 101,
020401 [L]).

**(c) Measurements and compatibility.** Measurement would go through Barandes's division events
(PROGRAMME:290). Compatibility is undetermined.

**(d) Hard to vary.** No rule is named, so this is undetermined. The controls are known: a selection
must act on the off-diagonal fibre-Gram data (act 12 `SH1`) and on the threading (act 13 `CT2`). It
must not be one of the four refuted selectors (act 17).

**(e) Sourcing and first probe.** E2 needs a stated induced-operation map and a gauge-invariance
theorem. Cheapest probe: take Main.md:420's two-visible/two-hidden map φ(v, h) = (v ⊕ h, h). Compute
the induced change of lift for one bijective intervention, under two lifts related by the strong-right
gauge. If the visible-level induced operation differs, the map is undefined without a selection; that
is the expected outcome given `SA2` and `CT4`.

### E3 (rank 3): R alone (Weyl–Lagrangian registration, odd q)

Statement and invariants are as in E1. R breaks I1 in the amplitude frame and keeps I5. Its group is
finite modulo phases, so there is no density. It reproduces OI's rooted law [N P2], and a different, back-acting two-time law [N P6.b]; OI's monitored
law is not reproduced (check B).

R supplies the phases at site level, a non-monomial Fourier map, and a native, disturbing measurement.
It is the explanatory half of E1, and it is predicted insufficient alone.

The kernel's `PolC` (PolarizationClosure.lean:150) is not R. It adds the q = 2 layer images
(C5Discovery.lean:192, :196), which contradict OI's law (P1). It also adds arbitrary relabellings and
permutations of the polarized carrier, which R does not source (P3). Those additions are what produce
`polarizedTheoryC_phasesAvailable` (:448), the non-Clifford block (:724) and, new here [N P5], a dense
subgroup of U(4)/phase at level two. The level-two generators are the swap image, its relabelling,
CNOT, `phaseGate` (1,1) from `polC_phaseGate` (:443), and the shear image. The probe finds an
infinite-order element modulo scalars and an Ad-irreducible action; the Clifford-only control finds no
infinite-order element. `PolC`'s positives are therefore not sourcing evidence (AW-H2).

### E4 (rank 4): T alone on the configuration carrier

Each substratum layer is the time-one value of its exact gate flow (continuous-time audit CT2;
`LayerFlowExecutable` LiftAudit.lean:112). T alone breaks I1, I2 and I4:
`gateFlow_half_not_preservesDiag` LiftAudit.lean:155 and `gateFlow_half_not_monomial`
ExecSource.lean:183 [K].

I3 catches it. FlowEndpoint.lean:177 [K]; [N P4.a]: the principal logarithms of the shear, swap and
leap permutations generate ones-fixing algebras far from full, of dimension 4/16, 31/256 and 20/81.
ROADMAP:1499 already records the resource as `INDEPENDENT`.

E4 gives flows without phases, and readouts stay classical. It predicts no relative phase against the
uniform ray, so it is insufficient alone. It is the T half of E1.

### E5 (rank 5): H-Bell preparation-indexed adjacency

Principle as at Substratum.md:130–132. A state-dependent rule is still a bijection (SM.md:102). It
stays at configuration level, `obsTheory_rule_independent` applies, and I1 does not move. E5 supplies
neither operations nor tests: Bell violation is downstream of off-diagonal local control (thread E,
AW-E3).

Under E1, E5's role changes. At sub-period times the substratum is no longer the observer's ontic
model, so Main §3.3's Bell accounting applies to the integer-time shadow. That has to be re-examined.
As a control for E1: the integer-time sector should satisfy CHSH ≤ 2 at odd q, since it is
noncontextual (Spekkens 2007, PRA 75, 032110 [L]). Violation should need sub-period durations.

### E6 (rank 6): A6 as an operational gauge principle

On the finite carrier, a site-dependent G(n) ∈ AddAut(V) is a configuration bijection, so it lies in
`permClass` (SubstratumInterfaceAudit.lean:236) and I1 holds. The transported coupling changes only
the rule, and rule independence hides the rule. `a6cov_all` carries no constraint.

On the complex carrier, U(6) acts on field values in ℂ⁶, not on ℂ^Conf, and the carrier fails A1
(`cx3b_complex_not_A1`). E6 is dead. See AW-H3.

### E0 (reference only, excluded): control or phases as a premise

This covers Arc D's control, `FixedGateSourced α` (DiscreteCompletion.lean:34), GR's phase
intervention (GR.md:258) and Main's executability assumption (Main.md:568). They are sufficient [K]
but explain nothing, and both FSA:163–172 and the owner exclude them. Any candidate whose sourcing map
reduces to "this gate or flow is available" falls here.

***

## 3. Comparison table

| | principle | breaks I1? (operation) | I3 | I4 | I5 | tests / compatibility | independent prediction | controls held / conflicts | evidence |
|---|---|---|---|---|---|---|---|---|---|
| **E1** R⊕T | registration of the current half + continuous description time | yes: exp(t log W(L)), t ∉ ℤ | broken | broken | broken | native registration; PSD by R's kinematics | P-1 to P-6: Born = OI rooted law at integer times; uncertainty and back-action; parity superselection; q odd | C-1 held; C-2 held for the back-acting two-time law; conflicts with q gauge, structured priors, bare read-write copy | [N] P2, P4, P6; [X] P1.d, P3.a; [L] |
| E2 Track B lift | context-dependent lift + P0 selection | not at M | ? | ? | possibly (contextual) | division events; ? | none yet | RD1, SA2, TJ3 constrain it | [K] acts 6–17, [D] |
| E3 R | registration alone | only in the amplitude frame | broken | holds | **holds** | native; PSD | P-1, P-2, P-5 | C-1 held; C-2 held for the back-acting two-time law | [N] P2, P6 |
| E4 T on Conf | gate flows of the layers | yes: unit g t | **holds** | broken | n/a | classical readout | no phases (refuted) | FlowEndpoint | [K], [N] P4.a |
| E5 H-Bell | preparation-indexed adjacency | no | holds | holds | holds | none | composite / no-signalling | rule independence | [K], [W] |
| E6 A6-op | local gauge as control | no (finite); off-carrier (ℂ) | holds | holds | n/a | none | none | `a6cov_all` vacuous; fails A1 | [K] |
| E0 | control as premise | by fiat | by fiat | by fiat | by fiat | by fiat | none | excluded | [K] |

***

## 4. Maximum skepticism on E1 (§A.31, depth-first)

**Productivity test, fixed first.** A node is a gem if it yields something strictly stronger than
restating the barrier, and it either constrains E1 or exposes a hidden assumption.

- **N1. Is E1 "add the missing control as a premise" under a new name?** Split R from T.
  - R lists no gates. Its operations are forced images (nullspace dimension 1). On its own it is
    Wigner-classical (P2.d, P6.b), so it carries no operational nonclassicality.
  - All of E1's nonclassical content is in T. T posits a continuous unitary evolution of the
    description between updates. Together with P2 and P6, that makes the classical substratum the
    integer-time Wigner shadow of a continuous quantum evolution.
  - The owner's objection therefore applies to T in a modified form. T does not choose gates: the
    generators come from the rule, and the reachable algebra is a falsifiable output (P4.b). But T
    does posit the continuum that I4 requires.
  - E1 explains which control is available, why phases appear, why measurement disturbs, and why OI's
    laws equal Born statistics in the linear sector. It does not explain why the description evolves
    between updates.
  - **Verdict: BORDERLINE as an explanation; POSITIVE as an F2 sufficiency candidate.**
- **N2. Consistency with S⇔D⇔Q_fb.** At odd q, the single-time (rooted) law agrees exactly in the
  probes [N]. The two-time agreement of P6.b is with a classical law whose intermediate registration
  is symplectic and back-acting, re-randomizing the hidden half. OI's monitored trajectory law reads
  `x₁` without disturbance, and it is not reproduced: at q = 3, N = 1, every entry of
  `P(x₁, x₂ | x₀)` differs for each coupling, and given `x₁` the law of `x₂` depends on `x₀` under OI
  and not under E1 (`../f2-census-checks/monitored_law.py`, check B [X]). Both agreements depend on the
  counting measure on the conjugate component (P2.c fails with a point prior); the two-time agreement
  also depends on symplectic registration (P6.a, P6.c). **NEW: E1 reproduces OI's rooted law, not its monitored two-time law;
  two-time agreement requires replacing OI's non-disturbing readout by back-acting registration.**
- **N3. q = 2.** The kernel's images are not even multiplicative: S² = Z while the shear is an
  involution [X P1.b]. They contradict the visible law [X P1.d], and no Clifford layer pair works
  [N P1.f]. Leaps alone also fail for odd-diagonal couplings [N probe_H2]. So E1 needs odd q, against
  SM's q gauge. **NEW: a control conflict.**
- **N4. The kernel's `PolC` is dense at level two [N P5].** The relabellings and the single-configuration
  phase at level two (CS) carry this result. P3 shows those are not homomorphic images of substratum
  processes. **NEW: a hazard. Do not propagate as a sourcing result.**
- **N5. Parity.** The leaps alone are superselected. Universality needs source terms. **ELABORATING:**
  this is a prediction.
- **N6. Necessity, assessed separately.** Within E1, each principle is necessary relative to the
  other: R alone is caught by I5 and T alone by I3. Neither is shown necessary absolutely, because E2
  might avoid T. "Minimal" is not claimed.
- **N7. Generalization [W + L].** Suppose an extension maps classical substratum processes to observer
  operations by a fixed covariant linear frame map, with states as distributions in that frame. Then
  the operational theory inherits a nonnegative quasi-probability representation, is noncontextual,
  and is not QM (Spekkens 2008 [L]; Kochen–Specker 1967 [L]). So within the corpus there are two ways
  out: a continuum (E1's T), or a context-dependent realization map (E2). This is stated for fixed
  covariant frame maps only, not for every extension. **NEW.**
- **N8. Literature cross-check.**
  - R is the OI instance of the epistemic-restriction programme. Spekkens 2007; Bartlett, Rudolph,
    Spekkens 2012 (PRA 86, 012103) [L]: linear symplectic dynamics with that restriction yields
    stabilizer or Gaussian QM. R inherits that ceiling.
  - T plays the role that Hardy's continuity axiom (Hardy 2001, quant-ph/0101012, Axiom 5) and
    Masanes–Müller continuous reversibility (New J. Phys. 13, 063001, 2011) play as postulates [L].
    E1 computes which transformations occur, but still posits continuity.
  - Barnum–Wilce local tomography (Found. Phys. 44, 192, 2014) [L] is built into R's tensor product.
  - Dakić–Brukner (arXiv:0911.0695) [L] take the elementary system to be one bit. E1's elementary system
    has q states with q odd, so qubits must be emergent. This is a tension with K1's d = 3 selector,
    recorded and not resolved.
  - Chiribella–D'Ariano–Perinotti purification (PRA 84, 012311, 2011) [L] has a natural candidate in
    the symplectic meter couplings. Not shown.

***

## 5. Recommendation and first probe

**Recommended: E1 (R ⊕ T).** It is the only candidate that supplies, through one stated map, all
three of the owner's step-2 items:

- non-monomial and phase operations: computed from the rule's own generators;
- valid measurements: registration through symplectic embedded coupling, with derived disturbance;
- compatible transformations: conjugations on the description that registration reads.

It reproduces OI's rooted visible law (C-1) and a back-acting two-time law (C-2); OI's monitored two-time
law is not reproduced (check B). It is hard to vary
(P-1 to P-6), and it can be killed cheaply.

**Required caveat (N1).** The nonclassical datum is T, the continuity of the description's evolution
between updates. The owner should rule explicitly whether that counts as a physical principle or as
control by another name. Before investing in E1, the owner should also decide two other things: the
q-gauge conflict, and dense versus exact as the F2 target (§0).

**First probe: exact q = 3, N = 1, then N = 2.** The numerical versions are done and green:
P2.a, P2.d, P4.b, P4.c and P6.b.

1. Certify over ℚ(ω, √−3) that the leap's Weil image intertwines the Weyl operators.
2. Certify that integer-time Born statistics equal the classical marginal, as exact rationals, both
   single-time and with a symplectic meter.
3. Certify that the Lie algebra generated by the logarithms of the leap images (f ∈ ℤ₃) and the
   translation is u(3). The logarithms are rational multiples of 2πi on eigenspaces.

**Decision rule, preregistered as a rule and not as numbers.**

- E1 is consistent if step 1 and step 2 hold exactly for every symmetric coupling.
- E1 is sufficient at N if the rank is full.
- E1 fails if step 2 fails for any symmetric coupling, or if the rank is deficient for every admissible
  generator set.

Countercontrols, each of which must behave as recorded:

- non-symmetric coupling: no image (P2.b);
- point prior on the previous component (P2.c);
- bare copy (P6.a);
- leaps without translations: parity (P4.b);
- configuration-carrier flows: ones-fixing (P4.a);
- q = 2: the kill test (P1, probe_H2).

***

## 6. Assumption-watch markers (cross-propagation)

- **AW-H1.** `NonnegBounded` is frame-relative. A candidate that moves operations into another fixed
  linear frame where they act as point maps inherits the invariant there: the Wigner frame, for Weil
  polarization at odd q. The decisive necessary condition is that no positive representation exists
  in any frame.
- **AW-H2.** `PolC`'s phases at every level, its non-Clifford block and its level-two density (P5)
  come from imports the polarization map does not source: the q = 2 images and the arbitrary
  relabellings and permutations. They are not evidence for a polarization principle.
- **AW-H3.** A5 is linearity of the rule on field values. It is not linearity of the observer's
  amplitude space ℂ^Conf. A complex field carrier is a first-quantized object (cf. lift L3), and it
  fails A1.
- **AW-H4.** Main.md:424–425 motivates the slow-bath condition with an ETH Hamiltonian hidden sector,
  which presupposes quantum dynamics. Using it to source T would be circular.
- **AW-H5.** The interface's non-disturbing read-write copy is incompatible with any Weil-covariant
  registration (P6). This bears on how C4 readback is modelled under an extension.
- **AW-H6.** SM's q gauge (SM.md:90) is not invariant under polarization: q = 2 behaves differently
  from odd q.

***

## 7. Evidence ledger: the probes

All of these are in `scratchpad/threads/H-work/`.

| probe | result | label |
|---|---|---|
| P1.b, P1.d | S² = Z (not a scalar); H·S²·H = X, while the classical word leaves cur = 0 | [X] |
| P1.e, P1.f | 24 Cliffords modulo phase; 0 of 576 layer-image pairs reproduce the law (words ≤ 8) | [N], exhaustive |
| probe_H2 | q = 2, two sites, leaps only. Images consistent under powers alone: [4, 8, 8, 16, 8, 16, 16, 0] over the 8 symmetric couplings. Joint pairs: 8, 0, 0, 0 | [N], exhaustive over sign patterns |
| P2.a, P2.b, P2.c, P2.d | odd q: Born = classical (error ≤ 3e-15); no image for a non-symmetric coupling; point prior not reproduced; Wigner covariant | [N] |
| P3.a, P3.b, P3.c | Toffoli is not a projective homomorphism image; CNOT is | [X] for P3.a |
| P4.a, P4.b, P4.c | Conf flows are ones-fixing and not full; leaps alone are parity-superselected; leaps + translations generate the full u(d) | [N] |
| P5.a, P5.b, P5.c | `PolC` level two: an infinite-order element modulo scalars (degree-bounded check), Ad-irreducible (commutant dimension 2); Clifford-only control has no infinite-order element | [N] |
| P6.a, P6.b, P6.c | bare copy has no image; symplectic registration gives two-time law = Born; the bare copy keeps memory | [N] |

***

## 8. Ten-line summary

1. Besides `NonnegBounded` (I1), four more invariants guard the barrier: configuration level, ones-fixing, countability, and a new frame twin (I5: Wigner positivity in the (previous, current) frame at odd q).
2. Countability [K] means exact QM needs an added continuum. Without one, F2 can at most reach `DenseFiniteQM`. The owner has to choose the target.
3. Recommended: E1 = R ⊕ T. R: observers register the current half and are covariant under the Weil image. T: the update is a stroboscopic sample of continuous description time.
4. E1 supplies phases, non-monomial and exact control (full u(q^N) at the tested sizes [N]), disturbing registration-based tests and compatibility, all through one stated map.
5. E1 reproduces OI's single-time (rooted) visible law exactly at odd q [N], and a different, back-acting two-time law; OI's non-disturbing monitored two-time law is not reproduced (check B [X], q = 3). This postdicts Lemma 3's measure as the Wigner function of registered eigenstates.
6. Skeptic finding: R alone is Wigner-classical, so all nonclassicality lies in T. T posits continuity, not gates. The owner's "control as premise" objection applies in that modified form.
7. E1 has costs: q must be odd (q = 2 contradicts OI's law: H·S²·H = X [X]), against SM's q gauge; point priors are excluded; and registration must be symplectic, not a bare copy.
8. The kernel's `PolC` is dense at level two [N], but only through unsourced relabellings and permutations [X P3]. It is not a sourcing result.
9. Rank 2 is E2, the contextual Track-B lift: the only corpus route that might avoid a continuum, but with no operation map stated. E4 (T alone) is caught by ones-fixing [K]. E5 (H-Bell) and E6 (A6) cannot move I1 [K].
10. First probe: exact q = 3 certification of the Weil intertwining, Born = classical (with meter) and the u(3) Lie rank, with five countercontrols and the q = 2 kill test.
