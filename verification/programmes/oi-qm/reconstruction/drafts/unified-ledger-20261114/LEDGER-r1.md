# Unified derivation ledger, r1: dependency map

Paper-only record under the owner authorization on #914 (comment 6877420015, `amaybaum`,
2026-11-14), serving the target recorded in #914 comments 6875046763, 6875548603 and 6877420015
and #1169 comment 6876591512. Reading, analysis and writing only. This record adopts no premise,
extension E or sector condition C, changes no scientific status, and proposes no tier, readiness,
authorization or status change. Statuses below are those the cited sources give; where this record
says "conflicting", "consistent" or "undetermined", the reason and the source are stated.

**Base.** All `papers/`, `book/` and `verification/` content was read at `c3b5f37a`; current `main`
(`dfeec843`) differs from it only in `AGENTS.md` (§A.46 items 2, 4 and the new item 8), so every
line reference below holds at `dfeec843`. Line numbers are physical lines; `papers/*.md` paragraphs
are single long lines.

**Vocabulary.** "Kernel" = Lean module on `main` under `verification/lean-mathlib/OIBridge/` (not
rebuilt here; no `sorry` or `axiom` declaration found by grep). "Exhaustive" = exhaustive finite
computation in a script on `main` (not run here). "Paper" = derivation on paper. "Numerical",
"conditional", "posited", "open", "refuted" as in the Code Review Rules. Part 4 classes: **CR** =
conditional reconstruction; **UD** = unified physical derivation (Part 4, #914 comment 6877420015).

## 0. Branch table

| Branch | Headline result at source | Status at source | Weakest link | First missing step | Part 4 class |
|---|---|---|---|---|---|
| QM (operational) | S ⟺ D ⟺ Q_fb at the finite observable-law level; exact finite operational QM iff completion conditions (i)–(v); bare finite OI ⇏ QM | Kernel (equivalence, characterization, non-implication); (iv) not supplied by the stated substratum (kernel) | Physical source of the added principles (posited as an "empirical controllability resource") | An independently justified operation, inside one model, that supplies continuously tunable state mixing and phases (condition (iv)) | CR |
| Bell | Screened local completion ⇒ CHSH ≤ 2; reference nearest-neighbour graph Bell-local; adopted branch: ontic parameter dependence with measurement independence | Paper proof + exhaustive 16-table check; H-Bell open | H-Bell (open hypothesis) | A preparation-indexed adjacency rule that gives quantum CHSH values with operational no-signalling | CR (open completion) |
| GR | Horizon calibration ħ = c³ε²/(4Gσ), S = A/(4l_p²), Newtonian weak field at fixed G | Paper, conditional (H-slope, H-count, horizon/frame conditions); Einstein equations imported via Jacobson, not derived | G3: covariant field equations and stress-energy coupling, open | A derivation of the covariant field equation from (S, φ) | CR (G1–G2 only) |
| Standard Model | Gauge group SU(3)×SU(2)×U(1), (3,2,1) multiplicities, 1⊕3 candidate sectors, hypercharges, 22 tabulated observables | Six-link decomposition kernel; physical carrier conditional on H-link, H-cust; generations on H-spin′; chirality open (H-χ′); cubic lattice and d = 3 empirically selected | H-link with H-cust; H-χ′ open | Forward derivation of the physical carrier (H-link) and of weak chirality (H-χ′) from the model | CR ("maximally tight compression" at source) |
| Cosmological constant | 10¹²² ratio read as S_dS; zero-point sum assigned to the emergent description | Descriptive distinction established (paper); dynamical decoupling conditional on G3; value of Λ an input | G3 coupling theorem | A coupling theorem showing the uniform emergent offset does not source curvature | CR |
| Cosmology (dark sector, expansion) | Type II running-vacuum reading, \|ν\| ~ 10⁻³²; ~95% dark budget; a₀ = cH/6; BTFR | Conditional (H-count, H-slope, H-frame, H-Hawking; G3); form not derived; budget partly definitional; factor 1/6 imported; two rotation-curve tensions | Matter-to-boundary coupling map (open, G3) | The H-dependence of the uniform/structured split of boundary entropy, and the relaxation kernel | CR |
| Black-hole information | Information conserved by bijectivity; cycle-averaged Page curve under H-scramble and H-decouple | Conservation by premise (A2); H-scramble refuted in the counted setting (paper proof, exhaustive check); Page curve has no instance as stated; GSL open | H-scramble | A preparation or partition that yields entanglement across the black-hole/radiation cut, and a scrambling statement attainable under it | Open (no instance) |

## 1. The common model as the corpus states it

The single object is the observation triple (S, φ, V) (`papers/Main.md`:42). Its inputs, with
status at source:

| Input | Content | Status at source | Site |
|---|---|---|---|
| Axiom 1 | tokened differentiation occurs | indubitable floor | `papers/Main.md`:36 |
| Ledger (i) | Axiom 2, recurrence | posited (countermodel for non-derivability) | `papers/Main.md`:724 |
| Ledger (ii) / A1 | total finiteness of the bijective representative | posited; E3 bounds only C_V × C_B under H-BD | `papers/Main.md`:724; `papers/Substratum.md`:92 |
| Ledger (iii) / A2 | bijectivity | part-empirical (observed doubly stochastic statistics) plus eventual-image principle | `papers/Main.md`:724; `papers/Substratum.md`:94 |
| Ledger (iv) | maximal-entropy measure selection | posited | `papers/Main.md`:724 |
| Ledger (v) | hidden-sector mixing hypothesis (C2 slow-bath form) | open; motivated only numerically, by a rounded map outside A5 | `papers/Main.md`:724; `papers/Substratum.md`:135 |
| Ledger (vi) / E4 | spatial isotropy | empirical input | `papers/Main.md`:724 |
| Ledger (vii) / A5 | linearity of the update | posited; affine part derived from amplitude-scale gauge (SM §4.1); no derivation from bare OI found on the record searched | `papers/Main.md`:724; `papers/Substratum.md`:100; `verification/programmes/hydrodynamics/round-h-d-a5-status-adjudication/result.md`:647–700 |
| Ledger (viii) | site factorization | posited (dynamics not shown to select it) | `papers/Main.md`:724 |
| Ledger (ix) / A3 | bounded coupling degree (family form) | posited | `papers/Main.md`:724 |
| Ledger (x) | nearest-neighbour range; simple-cubic reference graph | posited (beyond A3) | `papers/Main.md`:724; `papers/SM.md`:226 |
| Ledger (xi) / A4 | center independence | posited; anchored to homogeneity of law | `papers/Substratum.md`:98 |
| Ledger (xii) / A6 | background independence (covariant link interface) | posited; restricts no rule; kernel records A3–A6 as formalization gaps | `papers/Substratum.md`:102; census family "manuscript axioms A1-A6" |
| Ledger (xiii) | second-order form x(t+1) = F(x(t)) − x(t−1) | posit of the selected lattice model (kernel `ruleDynamics`) | `papers/Main.md`:724 |
| Ledger (xiv) | measurement independence p(Ω∣a,b) = p(Ω) | posited on the initial condition | `papers/Main.md`:724, 404–410 |
| C1–C4 | coupling, persistence, capacity, readback | diagnostics of a realization; C4 not discharged at the cosmological cut | `papers/Main.md`:70–78; `papers/GR.md`:52 |
| E1–E7 | unitary QM, Bell violation, boundary entropy, isotropy, propagating gravity, stable matter, ρ_s/ρ_crit ≈ 1 | empirical inputs of the reverse reconstruction | `papers/Substratum.md`:76–88 |

No common extension E and no sector condition C is stated anywhere in the corpus (searched:
`papers/`, `book/`, `verification/programmes/oi-qm/PROGRAMME.md`). The reverse reconstruction
(Theorem 23, `papers/Substratum.md`:193) takes observed QM (E1) and Bell data (E2) as inputs; it is
a uniqueness statement for the local lattice/gauge residue, not a forward derivation.

## 2. QM (operational)

**2.1 Results and status.**
- S ⟺ D ⟺ Q_fb on every finite horizon (`papers/Main.md`:14–18, 97). Kernel: `finite_horizon_equivalence`, `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S` (`OIBridge/Equivalence.lean`). Universal over finite laws, so representability does not single out the memory-bearing sector (`papers/Main.md`:18).
- C4 ⟺ positive conditional memory; readout-relevant hidden memory in every faithful completion. Kernel for the pushforward identity; the CMI vanishing criterion and one reading step are stated as not formalized (`papers/Main.md`:97).
- Operational-completion characterization: on a finite carrier, with complex matrix kinematics taken as given, available families are exactly the Kraus instruments iff (i)–(v) (`papers/GR.md`:212–216; `papers/Main.md`:562). Kernel: `exactAll_iff_physical_general`, `five_way_minimality`, `oi_alone_not_qm`. The kinematics itself is not derived (`papers/GR.md`:212).
- Under the stated substratum interventions, (iv) is not supplied (kernel `substratumGen_not_control`, `papers/Main.md`:80); with one continuously tunable state-mixing operation added "as an empirical controllability resource" the result is operational QM (kernel `substratum_plus_control_qm`, converse `qm_generated_by_substratum_extension`; `papers/Main.md`:588; `papers/GR.md`:256). Every operation the present interface sources preserves nonnegative entries (kernel `frozen_sourcing_verdict`, carried by no manuscript; `verification/programmes/oi-qm/PROGRAMME.md`:40, 80–84).
- OI⁺ ⟺ exact finite endomorphic operational QM, each added principle independent (kernel `carrier_general_oiPlus`, `oiPlus_independence`; `papers/Main.md`:584–588). A characterization of an extension, not an entailment from bare OI (`papers/Main.md`:588).
- Approximate inclusion: one finite reversible realization reproduces a bounded quantum envelope to accuracy ε (paper proof with qubit-instance probe checks; `papers/Main.md`:596–598). Exact inclusion on one fixed finite carrier is obstructed (classical-dimension Proposition, paper proof; `papers/Main.md`:558); any exact endpoint needs a closure beyond one carrier whose finite predictive rank is not proved (`papers/Main.md`:356). The quasilocal completion exists and is unique given its stages, with no state or representation selected (kernel family "quasilocal completion"; `papers/Main.md`:588).
- Representability plus coherence does not select the relating unitary evolution (`papers/Main.md`:20).

**2.2 Chain to the common model.** Axiom 1 + Definition → Lemma 1 (stipulated finite capacity) →
Lemmas 2–3 (partition; bijectivity part-empirical; measure posited) → S ⟺ D ⟺ Q_fb (kernel) →
C1–C4 diagnostics (kernel/paper) → operational QM only with (iv) and the OI⁺ principles added
(kernel for the implication; the added operation posited). Weakest link: the added operation.

**2.3 Additional premises.** Complex matrix kinematics (taken as given; open). Completion
conditions (iii)–(v) (not supplied; (iv) shown not supplied). Phases (a stated intervention
principle, not a consequence; kernel `onesFixing_not_phasesAvailable`, `papers/GR.md`:256). The
state-mixing datum (postulate; census family "state-mixing coupling construction"). (G1)–(G4)
genericity for the Barandes route (`papers/Main.md`:716). Sector condition C and access closure:
not stated in the corpus.

**2.4 First missing step.** A physically sourced operation, in the same model, supplying condition
(iv) (and the phases), together with a sector condition C stated on the model with both sector
directions. Accountable Issues: #1169, #1236 (planning record only).

**2.5 Compatibility.** See §9 rows QM–Bell, QM–GR, QM–SM, QM–BH. Main point: the exact inclusion
target needs a completion beyond one finite carrier (`papers/Main.md`:356, 558), while A1 (ledger
(ii)) is used by the recurrence results, by `papers/GR.md`:585 and by the Page-curve cycle averages.

**2.6 Test.** None stated as decisive: "no memory-witness outcome therefore falsifies the
ontology at present" (`papers/Main.md`:718–720). Tabletop tests with tunable hidden capacity are
named without a predicted outcome (`papers/Main.md`:722).

**2.7 Classification.** S/C/L: C (conditional on added principles), Layer 0, mixed (substratum
dynamics with an emergent operational layer). Part 4: CR.

## 3. Bell

**3.1 Results and status.**
- Unrestricted OI realizes PR-box behaviour (response-table construction; `papers/Main.md`:360, 427). Paper, with negative control in a probe.
- Coupling-graph causal cone: influence moves one edge per update (`papers/Main.md`:362). Paper; an algebraic causal cone is kernel-checked in `OIBridge/QuasilocalAlgebra.lean`. No CHSH statement found in the kernel.
- Bell ceiling for a screened local completion, CHSH ≤ 2 (`papers/Main.md`:364–389). Paper proof; the pointwise bound over 16 response tables is exhaustive (`papers/oi_lattice_code/foundations/equivalence_recovery_probes.py`, check 11).
- Corollary: the nearest-neighbour cubic reference graph alone cannot supply option (a) for wings outside the graph cone (`papers/Main.md`:414). Paper.
- For a linear update (ledger (vii)) the dependence graph is the same at every state class, so a graph that varies between state classes requires an update outside (vii); the adopted branch "lies outside ledger item (vii)" (`papers/Main.md`:362, 414; `papers/SM.md`:104). Exact algebra (differences telescope).
- Measurement-dependent alternative: CHSH ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}, so I_ont ≥ 0.0309 bits for the quantum value; recorded, not adopted (`papers/Main.md`:416–423). Paper.
- H-Bell: prepared long-edge graphs must (i) supply parameter dependence, (ii) keep operational no-signalling, (iii) keep the metric/Ollivier–Ricci continuum limit (`papers/Substratum.md`:131–133). Open. Round `verification/programmes/oi-qm/h-bell/round-hb-1-obligation-shape/` has a preregistration only.

**3.2 Chain.** Site factorization (viii) → coupling graph → cone (paper) → Bell ceiling under
(ii)–(iv) (paper) → observed violation (E2) forces giving up ontic parameter independence →
preparation-indexed adjacency (proposed) → H-Bell (open). Weakest link: H-Bell.

**3.3 Premises.** (viii) site factorization (posited); (xiv) measurement independence (posited);
determinism (A2); M1-B, the branch assignment of Bell data (`papers/Substratum.md`:123), a modeling
premise; H-Bell (open). Exclusion of supraquantum correlations in the physical sector: required by
the target (#914 comment 6875548603); no mechanism stated in the corpus.

**3.4 First missing step.** A specified preparation-indexed edge rule (or response map) for which
the CHSH value is the quantum one and the remote marginal is setting-independent.

**3.5 Compatibility.** Conflicting with a global A5 as used by SM Stage 2(b) (§9 row Bell–SM).
Undetermined with GR curvature (H-Bell (iii)). Which cone is the physical c (graph cone, ℓ₁ reach
1/‖n̂‖₁, against wave speed 1/√3) is not derived (`papers/Main.md`:414).

**3.6 Test.** None stated beyond E2 itself, which already excludes the reference-graph-only model
for spacelike wings outside the graph cone (`papers/Main.md`:414).

**3.7 Classification.** L (pending H-Bell), Layer 0 (spatial constitution), substratum. Part 4: CR,
completion open.

## 4. GR (field equations and matter–geometry coupling)

**4.1 Results and status.**
- Ladder: G1 horizon identities (this paper's register); G2 weak-field consistency; G3 covariant field equations with conservation/Bianchi structure and continuum limit, open; G4 cosmological implications conditional on G3 (`papers/GR.md`:12).
- ħ = c³ε²/(4Gσ), ε = 2√σ l_p, S = A/(4l_p²): conditional on H-slope, H-count, horizon and frame conditions, local boost structure, symmetric rate ratio; the count S = σA/ε² unconditional (`papers/GR.md`:12, 24, 28). Paper. The relation fixes only ε/√σ (`papers/GR.md`:536–545).
- The Einstein equations are used through Jacobson's relation and not derived (`papers/GR.md`:162; `book/ch07-gravity.md`:44). Closure, Lovelock and spin-2 routes require hypotheses not established (`papers/GR.md`:162).
- Discrete Einstein equation κ_OR = α𝒯 is a target form; the hop-metric Ollivier route fails at the reference instantiation (ℓ₁ metric, √2 stretch), and the equation is not established by the cited chain (`papers/SM.md`:144–150; `papers/Substratum.md`:171). Lattice Bisognano–Wichmann form is an open hypothesis (`papers/SM.md`:140–142).
- Newtonian a = GM/r² and Poisson equation at fixed G from holographic equipartition, on an assumed energy shell; N_dof = A/l_p² adopted, not derived; nonlinear G_μν = 8πG T_μν not established (`papers/GR.md`:689–697). Paper, consistency level.
- Matter coupling: three completions for a laboratory source in superposition, selection open (`papers/GR.md`:350); whether the uniform offset sources curvature is the open G3 coupling step (`papers/GR.md`:352). Accountable Issue: #873.

**4.2 Chain.** Cosmological horizon as the partition (`papers/GR.md`:40, which takes GR's causal
structure as given) → C1–C3 checked, C4 not discharged (`papers/GR.md`:46–52) → H-count classical
temperature (`papers/GR.md`:58) → H-slope KMS matching (`papers/GR.md`:74) → ħ calibration →
Jacobson input → (G3 open). Weakest link: G3; at G1, H-slope.

**4.3 Premises.** H-count, H-slope, H-balance, H-frame, H-Hawking (i)–(v) ((iv),(v) discharged by
§4), H-state split into H-shell, H-energy, H-spectrum, H-BD (posited), H-BG, H-local-lift, local
boost structure, symmetric rate ratio, σ = 1 for quoted ε (`papers/GR.md`:58–60, 88, 122, 328,
649). H-slope and H-count are selection conditions that do not follow from bijectivity
(`papers/Substratum.md`:181). Energy shell: assumed, not a consequence of Lemma 3
(`papers/GR.md`:697).

**4.4 First missing step.** The covariant field equation, including which stress-energy sources
curvature, from (S, φ) (G3), with a curvature construction that works on the reference graph.

**4.5 Compatibility.** GR's geometry-first ordering (classical metric prior to the trace-out,
`papers/GR.md`:340–348) against SM §3.1 geometry emerging from a coupling graph that varies with
the state (`papers/SM.md`:104, 158), which requires an update outside A5: undetermined/tension (§9).
H-shell assumes weak boundary coupling while C1 requires nonzero cross-boundary coupling; the
source states the tension (`papers/GR.md`:60).

**4.6 Test.** GW250114 tests the classical area theorem, which the framework preserves, not the
1/4 coefficient (`papers/GR.md`:12, 318). Free-dispersion Lorentz violation O((kε)²), interactions
open (`book/appendix-a-prediction-status.md`:113). Gravitationally mediated entanglement tests
depend on the open (a)–(c) selection (`papers/GR.md`:350). No echoes expected (`papers/GR.md`:597).

**4.7 Classification.** Calibration C, Layer 0, mixed; field equations imported (E-type input).
Part 4: CR at G1–G2; GR ⊆ OI not established.

## 5. Standard Model (gauge group, matter, interactions, parameters)

**5.1 Results and status.**
- Six signed links decompose exactly as 6 = T₁(3) ⊕ E(2) ⊕ A₁(1) (Theorem 7, `papers/SM.md`:374). Kernel (census family "representation bridge and counting": `theorem_7`, `LinkDecomposition`); integer certificates in `verification/lean/OI_Gauge_Certificates.lean`.
- Identification of the link space with the physical carrier: H-link (single-copy clause K = 6); custodial route H-cust (condensate clause a premise); component-blind trace-out H-blind (`papers/SM.md`:12, 26, 32, 374).
- Gauge group U(3)×U(2)×U(1) from the bicommutant; reduction to SU(3)×SU(2)×U(1) uses a specified charged matter action and anomaly cancellation (`papers/Substratum.md`:163). Paper.
- Simple cubic selected among the 14 Bravais lattices as the one compatible with the observed gauge group (Theorem 7b, `papers/SM.md`:390); "empirically-anchored", "forced by the observed gauge group" (`papers/SM.md`:14, 56, 1424).
- d = 3 by filters E5–E7 within A4's periodic-lattice class; self-consistency strength; E7 inherits H-count (`papers/SM.md`:30, 1424; `papers/Substratum.md`:157).
- 1 ⊕ 3 taste decomposition proved (Theorem 8, kernel `theorem_8`); three physical generations conditional on H-spin′ (free kernel refuted and 4D-staggered route negative, numerical probes; condensate-dressed form open); chirality H-χ′ open, minimal embedding certified vector-like (`papers/SM.md`:543, 1320).
- Hypercharges unique given the family pattern and chirality, apart from Y_Q = 0 (Theorem 15, `papers/SM.md`:589). Paper (exact algebra).
- Couplings: 1/α₀ = 23.25 computed; δ₀ empirical; SU(2), SU(3) retrodictions; A·B comparison inconclusive (`papers/SM.md`:14, 1273–1276). The Haar-measure induced theory confines in Monte Carlo, against the deconfined phase the matching needs; candidate resolution via H-observer-bundle and H-Y-vertex (`papers/SM.md`:801–811).
- Parameters: of 22 tabulated observables, 2 S, 5 C, rest L/M/R/P/E (`papers/SM.md`:1269–1316); m_s, m_c, CP phases, neutrino masses open or solution-specific (`papers/SM.md`:1322). Strong CP: θ ∈ {0, π}; θ̄ open under H-top, H-det (`papers/SM.md`:655, 669).
- The observer-level operator: "the map φ → L_obs → Δ_g is not proved anywhere in this framework" (`papers/SM.md`:232).
- Source self-classification: "a tight compression of the Standard Model onto the cubic-lattice commitment … rather than … a derivation of the Standard Model from first principles" (`papers/SM.md`:14, 1428; `book/ch19-open-problems.md`:224).

**5.2 Chain.** (S, φ) + (viii) + A3–A6 + (x) → wave equation (`papers/SM.md`:224, uses A5) → cubic
lattice (selected by observed gauge group) → Theorem 7 (kernel) → H-link/H-cust → gauge group →
staggered tastes → H-spin′ → H-χ′ → hypercharges → induced coupling + empirical threshold. The SM
paper consumes "the emergent quantum description and its Born-rule statistics" from [Main]
(`papers/SM.md`:22). Weakest link: H-χ′ (open), then H-link.

**5.3 Premises.** A3–A6, (viii), (x), (xiii); H-link, H-cust, H-blind, H-spin′, H-χ′, H-top, H-det,
H-observer-bundle, H-Y-vertex; alphabet-size hypothesis (`papers/SM.md`:56); E4–E7; site and
internal factorizations as Tier 3 stipulations (`papers/SM.md`:1426).

**5.4 First missing step.** The physical carrier identification (H-link) and weak chirality (H-χ′)
derived from the model; before them, the observer-level lift φ → L_obs (`papers/SM.md`:232).

**5.5 Compatibility.** Uses A5 (Stage 2(b), `papers/Substratum.md`:159), which conflicts with the
Bell route and with SM's own §3.1 geometry as stated (§9). Uses QM as an input (E1; `papers/SM.md`:22).

**5.6 Test.** JUNO sin²θ₁₂ = 1/3 − 1/(4π²) as a forward test (`book/appendix-a-prediction-status.md`:98);
detection of proton decay falsifies; monopole non-observation (`papers/SM.md`:831, 839); no θ̄/EDM
prediction (`papers/SM.md`:655).

**5.7 Classification.** Gauge group C (H-link, H-cust), Layer 0, substratum; the lattice and d = 3
are E-type inputs; generations C (H-spin′); chirality open. Part 4: CR.

## 6. Cosmological constant

**6.1 Results and status.** Two descriptions: classical substratum ρ ~ H²/G vs emergent QFT
ρ_QFT ~ M_Pl⁴ (`papers/GR.md`:334–336). Ratio ~ S_dS (dimensional identity; `papers/GR.md`:362).
Descriptive distinction established; dynamical decoupling conditional on G3: two gravitational
completions share the same substratum, partition, transition law and calibration while differing
by the offset (`papers/GR.md`:352). The value of Λ is an input set by initial conditions
(`papers/GR.md`:356). Higgs and QCD vacuum shifts treated the same way, conditional on the same
coupling step (`papers/GR.md`:569–575). Paper.

**6.2 Chain.** QM branch (emergent Ĥ_eff) + GR branch (geometry-first ordering, `papers/GR.md`:340–348)
→ H_tot vs Ĥ_eff distinction (`papers/GR.md`:358) → G3 coupling (open). Weakest link: G3.

**6.3 Premises.** Geometry-first ordering (stated as forced by definiteness, non-circularity and
universality of ħ, `papers/GR.md`:344–348; status: argument on paper, its dynamical content
conditional on G3); H-local-lift for the local emergent QFT (`papers/GR.md`:328); spatial product
structure of C_V.

**6.4 First missing step.** The G3 coupling theorem stated for the uniform offset.

**6.5 Compatibility.** Requires the same metric to be classical at the partition boundary (GR) and
to emerge from the substratum graph (SM §3.1): undetermined (§9). The ν magnitude in §7 imports the
emergent running that §6.2 denies gravitates absolutely; the source states two readings
(`papers/GR.md`:400).

**6.6 Test.** None stated for the dissolution; the descriptions are stated to be non-adjudicable
from accessible data (`papers/GR.md`:362). The ν test belongs to §7.

**6.7 Classification.** Descriptive part: paper result; dynamical dissolution C pending G3, Layer
0, mixed; Λ value E. Part 4: CR.

## 7. Cosmology (dark sector, expansion)

**7.1 Results and status.**
- Running vacuum Λ_eff(H) = Λ₀ + 3ν(H² − H₀²)/(8πG): form "not a distinctive prediction" (every smooth model has it); content is the Type II channel, a structural reading, not a derived law (`papers/GR.md`:374–380). |ν| ≈ |ν_QFT| ~ 10⁻³², conditional on the §7.3 split, not at theorem level (`papers/GR.md`:382–398; `book/appendix-a-prediction-status.md`:109, class L).
- ρ_s = ρ_crit identity; ~95% invisible budget, fraction 1 − Ω_B by construction, partly definitional (`papers/GR.md`:418–452). Its step (ii-b) needs the geometry-first ordering (`papers/GR.md`:448–450).
- a₀ = cH/6 with the factor imported from Verlinde; BTFR; conditional on H-count, H-slope, H-frame, H-Hawking (`papers/GR.md`:466–486). MOND-like core vs CDM-like linear growth: crossover not derived, relaxation kernel uncomputed (`papers/GR.md`:524).
- Tensions: Jiao et al. (2023) Milky Way decline and Genzel et al. high-z curves (`papers/GR.md`:12, 536–545); DESI phantom-crossing preference 3–4σ against w ≈ −1 (`papers/GR.md`:412).
- Expansion history: H value an initial-condition input (`papers/GR.md`:356); inflation "not addressed" (`book/ch19-open-problems.md`:194); Hubble tension open (`book/ch19-open-problems.md`:168).

**7.2 Chain.** Horizon partition → H-count/H-slope de Sitter temperature (conditional) → Jacobson
Clausius at the horizon (imported) → geometry-first ordering → Q = M_Bc² (local assumption,
`papers/GR.md`:466) → Verlinde factor (imported). Weakest link: matter-to-boundary coupling (G3).

**7.3 Premises.** As §4.3, plus C2 at the horizon (τ_B ≳ 1/H, "not derived from the substratum
dynamics", `papers/GR.md`:456), Q = M_Bc², elasticity assumption of [20], emergent locality of
boundary coarse-graining (`papers/GR.md`:400 remark).

**7.4 First missing step.** The H-dependence of the uniform/structured split of boundary entropy,
which fixes ν (`papers/GR.md`:382–386), and the relaxation kernel.

**7.5 Compatibility.** ν magnitude uses SM masses through the Shapiro–Solà formula
(`papers/GR.md`:390–394) and the same emergent-locality premise as Lorentz invariance
(`papers/GR.md`:400): consistent as stated, undetermined in substance. E7, used for d = 3 in the SM
branch, is an inferred ΛCDM-pipeline quantity (`papers/Substratum.md`:88).

**7.6 Test.** DESI Y5: |ν| ≳ 10⁻³ refutes the magnitude at the specific-representative level
(`papers/GR.md`:591–593); detection of particle dark matter accounting for the structured sector
falsifies the corollary (`papers/GR.md`:460); rotation-curve comparisons not yet quantitative
(`papers/GR.md`:12).

**7.7 Classification.** a₀ C (factor imported), budget C (partly definitional), ν L, Layer 0/1,
mixed. Part 4: CR.

## 8. Black-hole information

**8.1 Results and status.**
- Information conserved because φ is bijective by premise; how much the radiation carries is not settled by bijectivity (`book/ch19-open-problems.md`:72). Bijectivity does not imply recovery from accessible records, and complete endpoint access with bijectivity suffices (exhaustive finite computation, exploratory, internally reviewed: `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md`).
- Nested trace-outs consistent (Theorems A.1–A.4, `papers/GR.md`:601). GSL open; Theorem A.6 bound two-sided (`papers/GR.md`:603).
- Page curve: Theorems A.8–A.9 conditional on H-scramble and H-decouple with the full product shell (`papers/GR.md`:605, 797, 831). H-scramble fails for every bijection on a definite configuration with an aligned bipartition; the theorems "as stated have no instance" (`papers/GR.md`:805, 813–823). Paper proof; exhaustive check (`verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md`, C1, C6(a)). Entropy at an aligned cut is bounded by the initial distribution's entropy (C2 there). Page time 0.646 t_evap conditional on β = 1 and the half-entropy turnover (`papers/GR.md`:605; BH-04).
- Status row G11: open (`book/appendix-a-prediction-status.md`:111).

**8.2 Chain.** A2 (premise) → nested partition (paper) → H-scramble (refuted in the counted
setting) → Page value. Weakest link: H-scramble.

**8.3 Premises.** A2; H-scramble (refuted in its counted setting; untested otherwise); H-decouple
(open); full product energy shell (open for an evaporating hole); β = 1; the island ↔ cycle
correspondence (conjectural, `papers/GR.md`:861).

**8.4 First missing step.** A preparation (initial superposition) or a non-aligned bipartition that
the model supplies, under which a scrambling statement holds (`papers/GR.md`:815;
`papers/Introduction.md`:169).

**8.5 Compatibility.** Conflicting with finite configuration orbits in the counted setting (proved).
The exact linear rule splits large energy shells into many cycles at prime q (`papers/Main.md`:724
(v); `papers/SM.md`:294): tension with single-shell cycle typicality, undetermined.

**8.6 Test.** Controls stated in the programme record (non-scrambling permutation must fail). No
observational test of the Page curve is stated; standard ringdown without echoes is expected
(`papers/GR.md`:597).

**8.7 Classification.** Open (G11 uncounted). Part 4: neither CR nor UD at present.

## 9. Joint-satisfiability table

"Known not to" means a stated result makes the two premises jointly inconsistent as stated.

| Pair | Premises A | Premises B | One model known to satisfy both? | Reason / source |
|---|---|---|---|---|
| QM–Bell | completion (i)–(v), added control | (viii), (xiv), H-Bell | undetermined | Composition of entangled preparations needs coherent instruments (`papers/Main.md`:572); neither is sourced |
| QM–GR | finite carrier, C1–C4; Ĥ_eff | horizon partition presupposing GR causal structure; H-state, H-energy | undetermined | `papers/GR.md`:40, 60: Ĥ_eff not shown to survive the trace-out; C4 not discharged at the horizon (`papers/GR.md`:52) |
| QM–SM | operational QM from the model | E1 (observed QM) as input; Born statistics consumed | undetermined | SM uses QM as input (`papers/SM.md`:22; `papers/Substratum.md`:76, 123); forward trace is #1211 |
| QM–CC | Ĥ_eff offset invisible to quantum data | G3 coupling | undetermined | `papers/GR.md`:352 |
| QM–Cosmology | C2 slow bath at horizon | τ_B ≳ 1/H not derived | undetermined | `papers/GR.md`:456 |
| QM–BH | exact QM needs closure beyond one finite carrier; coherent preparation | A1 cycle averages; superposed initial state | undetermined | `papers/Main.md`:356, 558; `papers/GR.md`:815 |
| Bell–GR | preparation-indexed long edges | Ollivier–Ricci/continuum curvature | undetermined | H-Bell (iii) open; hop-metric route fails even on the reference graph (`papers/SM.md`:150; `papers/Substratum.md`:171) |
| Bell–SM | update outside (vii) | A5 linearity in Stage 2(b), wave equation | known not to, for a global A5 | `papers/Main.md`:362, 414; `papers/SM.md`:104, 224. Undetermined if A5 is restricted to the reference class; no source treats that restriction |
| Bell–CC | — | G3 | undetermined | no shared premise traced |
| Bell–Cosmology | — | emergent locality of boundary coarse-graining | undetermined | long edges vs locality premise of `papers/GR.md`:400; not traced further |
| Bell–BH | entangling preparation | H-scramble needs superposed initial state | undetermined | both need a preparation resource not sourced |
| GR–SM | geometry-first ordering; harmonic boundary modes (SM wave equation, `papers/GR.md`:695) | A5; G(x) varying with the state requires leaving A5 | known not to, for SM §3.1 geometry with a global A5; otherwise undetermined | `papers/SM.md`:104, 158 |
| GR–CC | G3 open | G3 coupling | consistent as dependency | CC dissolution is conditional on the GR step |
| GR–Cosmology | H-count, H-slope, H-frame, H-Hawking | the same, plus Q = M_Bc² | consistent as stated (same premises) | `papers/GR.md`:466 |
| GR–BH | horizon conditions | H-decouple, full shell | undetermined | `papers/GR.md`:605 |
| SM–CC | Higgs and QCD vacuum shifts | uniform-offset decoupling | undetermined | `papers/GR.md`:569–575, conditional on G3 |
| SM–Cosmology | SM masses; d = 3 via E7 | Shapiro–Solà ν; E7 inherits H-count | consistent as dependency | `papers/GR.md`:390; `papers/SM.md`:30 |
| SM–BH | A5 exact linear rule | single-shell typicality | undetermined (tension) | `papers/SM.md`:294 |
| CC–Cosmology | offset does not gravitate | emergent running enters ν | consistent under either reading stated | `papers/GR.md`:400 |
| CC–BH | — | — | undetermined | no shared premise traced |
| Cosmology–BH | cosmological horizon primary partition | BH horizon not an epistemic partition | consistent as stated | `papers/GR.md`:597 |

Additional stated tensions inside a branch: C1 (nonzero coupling) against H-shell (weak boundary
coupling), `papers/GR.md`:60; C2 slow-bath motivation from a rounded map outside A5,
`papers/Main.md`:724 (v); MOND-like vs CDM-like regimes, `papers/GR.md`:524; graph cone vs wave
speed as the physical c, `papers/Main.md`:414.

## 10. Shared missing mechanisms

| # | Mechanism | Corpus statement | Branches blocked |
|---|---|---|---|
| M1 | Observer-interface lift: a derived map from φ to the observer-level operator and generator, preserving locality and isotropy | φ → L_obs → Δ_g not proved (`papers/SM.md`:232); H-local-lift (`papers/GR.md`:328); Ĥ_eff vs H_tot (`papers/GR.md`:60); relating evolution not selected (`papers/Main.md`:20) | QM, SM, GR, Cosmology (ν), CC |
| M2 | Nonclassical operation resource: continuously tunable state mixing and phases | not supplied (kernel `substratumGen_not_control`, `frozen_sourcing_verdict`); posited as a resource (`papers/Main.md`:588) | QM, Bell (coherent composite instruments), BH |
| M3 | Preparation resource: coherent or superposed preparations, entangling preparations, the hidden prior μ_H | μ_H not fixed by the partition (`papers/GR.md`:88); superposed initial state needed (`papers/GR.md`:815); entangling preparation supplies long edges (`papers/Substratum.md`:131) | BH, Bell, QM, GR (H-state) |
| M4 | A nonlinear or preparation-indexed update | Bell branch outside (vii) (`papers/Main.md`:414); G(x) varying with the state outside A5 (`papers/SM.md`:104); mixing evidence from a rounded map (`papers/Main.md`:724 (v)) | Bell, GR (SM §3.1 geometry), QM (C2 slow form), BH (typicality); conflicts with SM Stage 2(b) |
| M5 | Completion beyond one finite carrier | classical-dimension obstruction (`papers/Main.md`:558); closure rank not proved (`papers/Main.md`:356); quasilocal completion selects no state (`papers/Main.md`:588); G3 continuum limit (`papers/GR.md`:12) | QM (exact inclusion), GR; in tension with A1 uses (recurrence, BH cycle averages) |
| M6 | Matter–geometry coupling theorem (G3) | `papers/GR.md`:12, 350, 352; matter-to-boundary map (`book/appendix-a-prediction-status.md`:102) | GR, CC, Cosmology |
| M7 | Physical discharge of C4 at the physical cuts | not discharged at the cosmological cut (`papers/GR.md`:52); sealed core carries no routed witness (`verification/programmes/physical-realization/round-c4-1-physical-discharge/result.md`:30–45) | QM (physical realization), GR, Cosmology (memory effect), SM prerequisites |
| M8 | Continuum geometry from the graph | hop-metric Ollivier route fails; re-founding on Laplacian geometry proposed (`papers/SM.md`:150; `papers/Substratum.md`:171) | GR, Bell (H-Bell (iii)), Cosmology |
| M9 | Energy shell and density-of-states conditions | shell assumed (`papers/GR.md`:697); H-count, H-slope selection conditions (`papers/Substratum.md`:181) | GR, Cosmology, CC, BH (full shell) |

## 11. Document disagreements and mirror gaps

- D1. `book/ch19-open-problems.md`:20 heads §19.2 "Problems resolved"; its entries state "the paradox is not resolved" (:72), strong CP "Not resolved" (:80), quantum gravity "Partially addressed" (:28); the section's opening sentence (:22) describes the entries as resolutions, dissolutions and conditional constructions.
- D2. H-Bell section reference: `papers/Main.md`:20 cites [Substratum §3.3]; `papers/Introduction.md`:145 cites [Substratum §3.2]; the definition is at `papers/Substratum.md`:131–133, inside §3.2 (Stage 1), and its Stage-2 use at :171, inside §3.3.
- D3. The five completion conditions are cited as [GR §3.3] (`papers/Substratum.md`:14; `book/ch01-observation.md`:185; `book/ch00-introduction.md`:55) and as Main §3.4 (`papers/Main.md`:80). Both sites carry the statement (`papers/GR.md`:212–216; `papers/Main.md`:562); no content difference found.
- D4. The statement that a coupling graph varying between state classes needs an update outside (vii)/A5 is at `papers/Main.md`:362, 414 and `papers/SM.md`:104. Not found in `book/` or in the H-Bell definition (`papers/Substratum.md`:131–133) on the phrases searched ("item (vii)", "outside A5", "varies with the state", A5 near Bell or G(x)). Not traced further.
- D5. The dark-sector corollary is stated "under Lemmas 1–3 and conditions (C1)–(C4)" (`papers/GR.md`:418); its proof step (ii-b) uses the geometry-first ordering (`papers/GR.md`:448–450), step (i) uses Jacobson's Clausius relation (:426), and the abstract places the dark sector at G4, conditional on G3 (`papers/GR.md`:12).
- D6. `book/ch19-open-problems.md`:178 states the framework "does not carry an obligation" to derive the baryon-to-photon ratio; the adopted Part 4 requires accounting for "other claimed downstream consequences" (#914 comment 6877420015). Planning record against manuscript; recorded as a question (Q6), not a correction.

## 12. Open owner questions

1. **One observer interface.** The branches use different cuts: the abstract visible/hidden partition (QM), the cosmological horizon (GR, CC, cosmology), the component-complete site observer (SM, H-blind), nested horizons (BH). Must Part 4's single model carry one interface, or a stated family of nested partitions (GR Appendix A) counted as one interface?
2. **Linearity.** Keep A5 globally (excluding the stated Bell route and SM §3.1 geometry), restrict it to the reference state class, or replace it? Which A5-dependent results (wave equation, Stage 2(b), harmonic boundary modes, the eight located uses in round H-D) are to serve as preserved controls under §A.29?
3. **Empirical selection.** Do the simple-cubic Bravais type (selected by the observed gauge group) and d = 3 (filters E5–E7) count under Part 4 as admissible empirical inputs, or as assumptions introduced to reproduce the outcome that Part 4 excludes?
4. **Geometry order.** Is a classical metric at the partition boundary a premise of the model (`papers/GR.md`:340–348), or must it be derived from (S, φ) (`papers/SM.md`:104; `papers/GR.md`:689)? The QM branch's physical partition currently presupposes GR causal structure (`papers/GR.md`:40).
5. **Carrier.** Is the single model a finite substratum (A1, used by recurrence and Page cycle averages) or a completion (needed for exact QM inclusion)? If a completion, which finite-carrier results must be transferred to it?
6. **Scope of Part 4.** Are solution-specific quantities (CP phases, m_s, m_c, neutrino masses, baryon asymmetry; `papers/SM.md`:1322; `book/ch19-open-problems.md`:178) inside the derivation obligation, or recorded empirical inputs?
7. **Bell sector.** Must C exclude PR-type correlations through H-Bell's no-signalling and quantum-bound clauses, given that unrestricted OI realizes PR boxes (`papers/Main.md`:360)?
8. **Initial-condition posits.** Are measurement independence (xiv) and the hidden prior μ_H admissible as posits about initial conditions, or must the model derive them?
9. **QM as input to SM.** Must the SM branch be re-derived forward from the model plus E (the question of #1211), or does the reverse reconstruction (E1 as input) count as an intermediate for Part 4?
10. **Black-hole information.** Is information conservation by the premise A2 accepted for Part 4, or is recovery from accessible radiation records required (BH-01 shows the two differ)?
11. **Manuscript disagreements D1–D5.** Should any be scheduled as a separate correction unit under §A.25? This ledger authorizes none.
