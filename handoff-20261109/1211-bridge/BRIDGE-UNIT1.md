# OI-SM-QM-BRIDGE, unit 1: source trace of the quantum content of the SM chain

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Revision r5, after the
independent reviews REVIEW-UNIT1.md (r1, REVISE), REVIEW-UNIT1-r2.md (r2, REVISE),
REVIEW-UNIT1-r3.md (r3, REVISE) and REVIEW-UNIT1-r4.md (r4, REVISE); pending a fresh, independent
review.** Nothing
here is promoted, adopted or proposed for the manuscripts. A review ACCEPT, if reached,
authorizes nothing further (#1211 c.6738806776).

- **Accountable home:** #1211 (OI-SM-QM-BRIDGE); parent programme #1169.
- **Authorization:** owner (amaybaum), 2026-11-09, "Make Active, and start unit 1",
  recorded in #1211 comment 6738806776. That record lists "no computation;", no
  construction or execution of an experiment, no Lean work, no new physical assumption, no
  freeze or dispatch, and no manuscript change, PR or merge. A later owner decision, recorded
  in #1211 comment 6739843458, reads "Allow generic checks (as #1210)": exact checks of paper
  claims on generic mathematical objects are allowed and labelled; a result supported only by
  such a check is marked *computation-supported*; no computation is run on an OI mechanism.
  The r1 sanity-check script (§13) was run before that permission and falls outside the
  authorization in force when it ran; it is recorded as such. The r2, r3, r4 and r5 checks (§13)
  were run under the later permission. This unit makes no git or GitHub write.
- **Boundaries kept:** #1210 files (scratchpad/qphen/) and Q-C2-1 material were not opened
  or touched. #1169 / #1210 work was read only where it is merged on `main`.
- **Source snapshot.** Every citation is `path:line` at `origin/main` =
  `fd539e150759a6ea51ab279aeeac80fc06050ade` (2026-11-09 08:36 +0200). "Sub" =
  `papers/Substratum.md`, "SM" = `papers/SM.md`, "Main" = `papers/Main.md`, "GR" =
  `papers/GR.md`, "QP" = `verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md`,
  "QPR" = the same directory's `PROOF-RECOVERY.md`, "OB/" = `verification/lean-mathlib/OIBridge/`.
- **Reading coverage.** Read in full: Sub; SM §§1–5 (SM:1–673) and SM §6.1, §8.3 tier text
  (SM:677–690, SM:1420–1428); Main §§1–2, §3.1–§3.3, and the §3.4 statements, remarks and
  ledger lines cited below; QP §0–§1 and §4–§5 plus nodes 1–3 and 10; QPR in full. Skimmed:
  GR §3.3 opening; the oi-qm reconstruction index and the heads of
  `bridge-compatibility-audit/result.md`, `oi-qm-ext-1/probability-source-assessment.md`,
  `oi-qm-ext-1/whole-model-bridge.md`; the H-Bell round-1 preregistration head. Lean modules
  were inspected only to confirm that cited identifiers exist and, in one case, to read a
  definition (§8, F9). No kernel build was run. Statements about unread parts of the corpus
  are not made; where a negative ("none identified") is stated, its search scope is given.
  Not read in r1, read in r2 at the lines cited: `mechanism-1-20261107/DESIGN.md` (MECH-1)
  head and :870–893; `mechanism-2-20261108/DESIGN.md` (MECH-2) head and §0;
  `minacc-1-20261108/DESIGN.md` (M-INACC-1) head, :268–282, :578–590, and its `RESULT.md` §0
  (all under `verification/programmes/oi-qm/reconstruction/`); `oi-qm-ext-1/two-mode-drive.md`
  §§1–3; `substratum/a5-linear-affine-20261104/A5-LINEAR-AFFINE.md` row R5; SM:104–112, SM:130,
  SM:136, SM:176, SM:505, SM:511, SM:809; Sub:393–395; GR:260 and GR:270; Structure:152 and
  :1153; book `ch05-gauge-structure.md`:91, `ch06-matter-content.md`:28, `ch10-chemistry.md`:36
  and the FULL mirrors cited in §8; Issue #1188's body.
  Not read in r1 or r2, read in r3: under `verification/audits/foundations/`,
  `exec-source-audit.md` (from its "What the outcomes mean" section to the end),
  `lift-source-audit.md` (its outcome and the wave-operator requirement),
  `c5-discovery-audit.md` (in full), `polarization-closure-audit.md` (outcome and status),
  `coherent-continuum-source-audit.md` (outcome), `state-mixing-coupling-audit.md` (head);
  the Lean statements cited from them, read at their declarations: `obligations_independent`
  (OB/C5Discovery.lean:59), `exists_nonMonomial_of_layerFlowExecutable` (OB/ExecSource.lean:52),
  `uncountableNonMonomialRays_of_layerFlowExecutable` and `uncountableNonMonomialRays_of_qm`
  (OB/CoherentContinuumSource.lean:163, :195), `uncountable_of_layerFlowExecutable`,
  `polarizedTheoryC_derivedOI`, `polarizedTheoryC_not_qm` (OB/PolarizationClosure.lean:135,
  :606, :620), `onesTheory_layerFlowExecutable`, `onesTheory_not_qm` (OB/FlowEndpoint.lean:89,
  :208), `obsTheory`, `obsTheory_rule_independent`, `obs_availExt_le_substratum`
  (OB/SubstratumInterfaceAudit.lean:770, :780, :837), `substratumClass`
  (OB/StructuralClosure.lean:180), `ConfigurationLevel` (OB/ManuscriptAxioms.lean:125),
  `availExt_bind` (OB/OperationalAssembly.lean:617); Main:566, Main:584, Main:600; GR:262, GR:268;
  QP:240–259, QP:342–381, QP:846–916; MECH-2 §0 and :526–536.
  Read in r4: GR:248–258 (phase-free richness and its equivalence) and GR:266; Sub:129;
  `c5-discovery-audit.md`:18–48; `lift-source-audit.md`:95–102 (census) and :250–300 (scope
  amendment and verdicts); MECH-2 DESIGN:543–567 (Proposition B); QP:124–150 (class N); and, at
  their declarations, `ReadWriteFamily` (OB/ReadWriteControl.lean:86–89), `PhaseFreeRichness` and
  `oiPlusMin_iff_qm` (OB/MinimalRepertoire.lean:423, :569), `flow` (OB/ReachabilitySeam.lean:95),
  `PhasesAvailable` and `derivedOI_of_qm` (OB/RouteB.lean:132, :228), `onesTheory`,
  `onesTheory_not_phaseFree` and `flow_endpoint_refuted_general` (OB/FlowEndpoint.lean:53, :144,
  :157), `onesFixing_not_phasesAvailable` (OB/PhaseSource.lean:55),
  `phaseFree_of_derivedOI_layerFlowExecutable` and `qm_of_derivedOI_layerFlowExecutable`
  (OB/DerivedQ3.lean:207, :214),
  `gateFlow_mulVec_ones` (OB/InstrumentRealization.lean:491).
  Read in r5: GR:250, GR:258 and GR:270 again; `phase-source-audit.md`:207–232 (scope amendment)
  and :283–287; `verification/programmes/substratum/frozen-sourcing-audit.md`:287–291; and, at
  their declarations, `gateFlow`, `gateFlow_isolation` and `avail_conj_mul`
  (OB/LiftAudit.lean:47, :660, :770), `unit` and `unit_mul_unit` (OB/SecondOrderCircuit.lean:356,
  :392), `transition` (OB/LieRankSource.lean:199), `gateFlow_isolation_flip`
  (OB/DerivedQ3.lean:81), `onesTheory_no_quarter_flow` and `onesTheory_not_qm`
  (OB/FlowEndpoint.lean:121, :208).

***

## 0. Summary

**Central question.** How much of the quantum mechanics that the SM chain uses is generated by
(a) the finite bijection with its visible/hidden trace-out, (b) the spatial/lattice
constitution, and (c) the embedded observer's actual access, and where is quantum structure
supplied instead?

**Short answer, scoped to the corpus at `fd539e15`.**

1. **(a) alone** generates classical finite stochastic laws with memory, a universal
   fixed-basis unitary/Born *representation* of them, recurrence-cycle indivisibility and
   unavoidable hidden predictive memory. It generates no quantum-specific content: the
   representation is universal (Markov laws included), the Born dictionary is part of the
   definition of $Q_{\rm fb}$ and its exponent is not selected, and without spatial structure
   the same construction realizes PR-box correlations (Main:20, Main:362, Main:556).
2. **(b)** adds exact geometry and representation theory (graph cones, the six-link
   $3\oplus2\oplus1$, the taste $1\oplus3$, observer-level isotropy, the staggered
   $\varepsilon$-grading, reciprocity of transition counts). Its quantum-relevant outputs are
   mostly negative: the reference graph is Bell-local (CHSH $\le2$), and on its bipartite,
   center-free, linear class the non-adaptive native route to the quarter phase $S$ is excluded
   and at most two mutually disturbing native reads exist (QP:26–47, QP:323–338).
3. **(c)** as currently specified is itself largely supplied: terminal registration, ready
   cells and armable couplings (apparatus-1's P1–P3, H-PREP) are supplied access posits, and
   the only preparation the operational structure assumes is a maximally mixed ancilla
   (OB/OperationalAssembly.lean:594 ff.).
4. **Supplied, not generated:** complex matrix kinematics and the tensor-product composite
   (Main:218, Main:564); full reversible control, condition (iv) (Main:82); the phase
   intervention (Main:590); the continuous state-mixing ("layer flow") operation, not
   sourced by the stated substratum dynamics with the observer's read/write access nor by any
   stated lift formulation that lands in the operational interface, the site-space
   wave-operator formulation being unresolved rather than excluded (Main:590, GR:270);
   the Born exponent (Main:556); quantum Bell violation (H-Bell, Sub:131–133); the
   observer-level wave operator (SM:232); the fermionic measure (SM:290–292). The complex
   structure on the six-link carrier, which Theorem 5's unitary stabilizer needs, is not
   derived in SM (the real-to-complex step is named open at SM:809); a candidate exists on
   the real lift off its null modes (§8, F4).
5. **The forward-direction sentence Sub:68** ("established by [SM §§3.1, 4–5] and [Main]")
   does not hold as made. Main's forward results stop at finite-law representability and a
   conditional operational characterization; SM's forward chain declares that it *consumes*
   the emergent quantum description and Born statistics (SM:22–24), and several of its steps
   take quantum or quantum-field-theoretic structure as input (§3).
6. **Native obstruction (Q6).** QP's Lemma G1 rests on the bipartite, center-free read
   pattern of the second-order update (QP:240–257), and Lemma G2 adds affinity of the
   sector map at its step 3 (QP:362–369). The premise these share with SM is that read
   pattern, not linearity: it is what SM uses at SM:539 (Theorem 12's identification) and
   SM:569 (the premise $\Gamma A\Gamma=-A$ of the trace-out grading identity), and G1's sector
   split survives nonlinear rules with that pattern (§10). The minimal repair QP names, NNB, is a P3-armable
   same-sublattice coupling, local to a protocol; it removes that scalar bipartiteness where
   it is armed. Its transfer to the staggered operator's anticommutation
   $\{D,\varepsilon\}=0$ (Theorems 3, 12, 13) is the separate bridge that SM:306 and
   QP:298–305 name, and is not established here (§10).
7. **Smallest next proof questions** (§11): NQ1, the complex structure on the six-link
   carrier: the null modes of the real lift at $\alpha=1/d$, whether $\Sigma$ is $J$-linear for
   the real lift's positive-frequency $J$, and the lift itself; NQ2, what the records on
   state-dependent graphs (MECH-1, MECH-2, M-INACC-1) leave open: confinement to a preparation
   class, an armable symmetric NNB coupling under P1–P3, exact coexistence with the reference
   class's scalar bipartiteness, and the link to H-Bell.
8. **Frontier of the forward chain** (§5.1–§5.3). The chain is proved up to the finite
   observable-law level, $S\iff D\iff Q_{\rm fb}$ (Main:548), whose operations on the
   configuration carrier are monomial. Beyond that level the sources show three unsupported
   implications, none derived from another in the sources read, set out in parallel with their
   carriers and scopes in §5.3: the phase (O1; GR:260); state mixing, whose necessary condition
   is FI-1 below and whose layer-flow form is O2 (GR:270); and quantum Bell violation (H-Bell,
   S9). Their independence holds in scoped senses. The phase and the *layer flow* are
   kernel-proved independent on the two-state carrier (`obligations_independent`): the layer
   gate flows fix the all-ones ray (`gateFlow_mulVec_ones`) and the phase moves it (GR:260).
   The phase is not independent of state mixing in every form: phase-free richness, one
   continuously driven transition with the exchanges, gives with implementation locality and
   embedded observation exact finite endomorphic operational QM, the phases included
   (GR:250–256, Main:590), and GR:258 states that "the quarter phase is dispensable at every
   level". No phase operation enters that repertoire (GR:250), and none is needed because the
   complex driven transition carries the phase: the phase obligation moves inside the mixing
   obligation, as the requirement that the mixing source be that transition and not a real
   rotation, and is not removed (§5.1 (b)). H-Bell is posed within the bijective dynamics, as preparation-indexed adjacency or a
   nonlocal response map on the SM/GR graph with a curvature-stability condition
   (Sub:131–133); in the sources read it is not derived from FI-1 and does not derive it, and
   no independence theorem is stated. **FI-1** is: *the finite bijective dynamics with
   the observer's stated access supplies a non-monomial admissible operator on the
   configuration carrier at level one*. Its statement and its negative use a finite
   configuration carrier with a bijection and the stated read/write access, not the site
   factorization or the second-order form (§5.1 *Conditionality*). It is necessary, in one
   direction only, for exact finite endomorphic operational QM within the structural
   architecture on that carrier (GR:270;
   `exists_nonMonomial_of_layerFlowExecutable`), not for reproducing quantum statistics to
   finite accuracy (Main:566, Main:600), and not sufficient (`polarizedTheoryC_not_qm`, on the
   two-state carrier); a strictly stronger necessary condition is proved
   (`uncountableNonMonomialRays_of_layerFlowExecutable`). Only with the phase taken as stated
   (Main:590, GR:268) is FI-1 the first unsupported step on the route to that target. Status:
   not supplied by the stated read/write access (`obs_availExt_le_substratum`, `substratumClass`
   monomial) or by any stated lift formulation that lands in the operational interface
   (`coherentLiftClass_eq_substratumClass`); **open** for the site-space wave-operator
   formulation of SM §4.1 (the unproved map $\varphi\to L_{\rm obs}\to\Delta_g$ of SM:232
   together with the unstated map from it to the configuration carrier, GR:270), for the
   undecided realizations of the lift's channels, for the C5 polarization candidate's
   unsupplied map, and for extended access. The earliest unproved *assumptions* are the stated
   inputs; the site factorization is upstream of the spatial route, the cell-based access posits
   and H-Bell, not of FI-1 (§5.2).

***

## 1. Conventions

**Proof level** (where the statement lives):
- **F (fundamental):** statements about the finite triple $(S,\varphi,V)$, its exact marginals
  and its configuration-level structure.
- **O (observer):** statements about observer-level objects: visible laws, their
  representations, operational theories, observer-level operators obtained after a trace-out
  or posited as a lift.
- **Q (field-theoretic):** statements in an emergent lattice or continuum quantum field theory
  (Lagrangians, Grassmann/determinant measures, Yang–Mills terms, RG running).

**Status:** *proved* [layer], *disproved* [counterexample], *conditional* [named hypotheses],
*open* [named gap]. Verification layers: **K** Lean kernel (identifier named in the source),
**A** exact algebra or written proof, **X** exhaustive finite computation, **N** numerical,
**I** imported external theorem, **P** prose argument only. A chain step takes its weakest
link. Kernel identifiers were checked for existence only (§0).

**Justification type for a premise** (column (ii) of the ledger):
- **D** derived from independently justified OI principles (the two axioms, (S, φ, V), and
  results already proved from them);
- **Op** an operational principle stated independently of QM agreement but not derived;
- **E** empirical selection (chosen because it matches an observation; the observation may be
  quantum);
- **QS** selected by agreement with QM/SM output (column (iii) used as the reason) where
  the selecting target is defined by the theory rather than observed; selection by an
  observed quantity, quantum or not, is E;
- **St** stipulation (definitional or modelling choice with no stated selection reason);
- **C** consistency (shown compatible with other premises; not a reason for it).

Column (iii), "reproduces the QM/SM prediction", is never counted as support for column (ii).

***

## 2. The two anchor corrections, checked

1. **Site factorization is SM §2.4.** Sub §2 has no §2.4 (Sub headings: Sub:42 §2, Sub:66 §3;
   §2 is unnumbered paragraphs Sub:44–62). SM §2.4 (SM:64–74) states: "Given a product
   identification, φ determines its coupling graph; the dynamics alone has not been shown to
   select the identification, which is therefore an input — site factorization, item (viii) of
   the posit ledger [Main §4.5]" (SM:68). Confirmed. Sub:459 also cites "[SM, §2.4]" for space
   as coupling structure, consistent with the correction.
2. **Direction of Sub §3.1–§3.2.** Stage 1 takes E1 ("Unitary quantum mechanics … states as
   vectors in a complex Hilbert space, unitary time evolution, self-adjoint observables,
   Born-rule outcome statistics", Sub:76) and E2 (Bell violations, Sub:78) as inputs, and its
   output is the existence of a triple $(S,\varphi,V)$ realizing the observed law (Sub:123–127,
   Sub:137). This is QM → $(S,\varphi,V)$. Stage 2 also consumes E4–E7 (Sub:145) and selects the
   cubic lattice from the observed gauge group (Sub:203). Confirmed: nothing in Sub §3.1–§3.2,
   and nothing in Theorem 23 (Sub:193), is used below as support for substratum → QM.
   Likewise the gluing and uniform-continuum theorems of Main §3.4 (Main:566, Main:600) take
   quantum instrument families as input and encode them in a hidden register; they are
   QM → OI realization results and are not counted toward the forward bridge.

***

## 3. The forward-direction claim (Sub:68), traced

Sub:68: "The forward direction — from (S, φ) to observed physics — is established by
[SM §§3.1, 4–5] and the companion paper [Main]." Each cited forward result is traced below to
what it proves and to what it takes as input.

### 3.1 Main's forward content

| Main result | What it establishes | Quantum structure taken as input |
|---|---|---|
| $S\iff D\iff Q_{\rm fb}$ (Main:82 (1), Main:99, Main:548; K `finite_horizon_equivalence`) | Finite-horizon visible laws = visible marginals of finite reversible systems = fixed-basis unitary/Born representations | The Born dictionary is "part of the definition of $Q_{\rm fb}$"; "the equivalence exhibits the Born form and does not select the quadratic exponent" (Main:20, Main:556). The unitaries are permutations, so $\lvert U\rvert^p$ gives the same table for every $p>0$ (Main:556). The embedding $\mathbb C^n$ is a choice of ambient linear algebra (Main:268). |
| Readback, memory, indivisibility (Main:99, Main:137–147; K `pIndivisible_of_rooted_identity_return_of_overlap` et al.) | Classical: C4 ⟺ $M_t>0$; hidden predictive memory in every faithful completion; recurrence-cycle P-indivisibility | None; these are classical stochastic-process statements. |
| Born-form representation of $T_{ij}$ (Main:288) | $T_{ij}$ equals the diagonal of a permutation-dilated CPTP channel | Representation identity; "does not select the quadratic exponent" (Main:288). |
| One-step coherence (Main:306–322; K `entanglementBreaking_twirl` etc.) | For the $\mathbb F_2$ linear nearest-neighbour update with a bulk, the channel's linear extension to off-diagonal inputs is not entanglement-breaking | Requires off-diagonal input states, which the substratum does not prepare; Main itself: it "supplies neither the observable algebra, nor preparations and interventions, nor tensor composition, nor multi-time statistics" (Main:326). The channel is a Weyl twirl acting "with no phase" (Main:306). |
| Operational completion (Main:82 (4), Main:564, Main:584–590; K `exactAll_iff_physical_general`, `five_way_minimality`, `oi_alone_not_qm`) | Characterization: with complex matrix kinematics *taken as given*, exact finite operational QM ⟺ five conditions (i)–(v); each independent of the C1–C4 process | Complex matrix kinematics, the tensor-product composite and local tomography are taken as given, "deriving that kinematics is open" (Main:218). Condition (iv), full reversible control, "is not supplied" by the substratum's stated interventions (Main:82; K `substratumGen_not_control`). Phases enter "as a stated intervention principle rather than a consequence" (Main:590). Derived but not an operation: an exact strongly continuous path of $*$-automorphisms from the identity to the update, with no one-parameter-group law and no generator (Main:274, Main:590; K `driveQ_isContinuousPath`); the layer flow at intermediate times is not executable by the stated class (GR:270). |
| Bell (Main:362–429) | Bell ceiling CHSH $\le2$ for screened local deterministic completions; PR box realizable without spatial restriction | A completion reproducing quantum Bell correlations gives up ontic parameter independence or measurement independence (Main:403–406); the framework gives up the first; the measurement-dependent alternative needs $I_{\rm ont}\ge0.0309$ bits (Main:22). No-signalling and Tsirelson are not derived for the SM/GR graph (Main:429). |

Main's own summary of the boundary: "the exact equivalence claim is at the finite
observable-law level; universal Hilbert-space representability is not promoted into a
uniqueness theorem for operational quantum mechanics entire" (Main:22); "A Layer-1 result does
not by itself establish any Layer-4 claim" (Main:99).

### 3.2 SM's forward content

SM declares its dependence explicitly: "The present paper consumes only the emergent quantum
description and its Born-rule statistics" (SM:22), and invokes "the Born rule at the
ancilla-marginal level, whose trivial-ancilla form is $T_{ij}(t)=|U_{ij}(t)|^2$" (SM:24). The
"emergent quantum description" that Main delivers is $Q_{\rm fb}$; SM's §§3–6 use considerably
more. Steps of SM §§3.1, 4–5 that take quantum or field-theoretic structure as input:

| SM step | Quantum / QFT input used |
|---|---|
| §3.1 area law, real case (SM:122–124) | "entanglement entropy … [3]" of the Gaussian (quantized harmonic-oscillator) state; the mod-$q$ case is a classical mutual-information bound, the proportional form is the quantum Gaussian statement (SM:150 (i)). |
| §3.1 lattice Bisognano–Wichmann (SM:140–142) | Thermal reduced state of a quantized oscillator vacuum, $T_U=\hbar\kappa/(2\pi ck_B)$; the lemma is imported from the coupled-oscillator literature [6]. |
| §3.2 stable-matter filter (SM:176) | The atomic-stability filter as stated includes a quantum statement, the non-existence of normalizable bound states of the $d$-dimensional Coulomb *Hamiltonian*, beside the classical Ehrenfest argument and the classical gravitational-orbit instability. |
| §4.1 wave operator (SM:222, SM:232) | "a real/complex wave operator is an observer-level lift whose derivation must be stated separately"; "the map $\varphi\to L_{\rm obs}\to\Delta_g$ is not proved anywhere in this framework" (SM:232). |
| §4.4–§4.6 stabilizer (SM:340–344, SM:374) | A unitary group $\mathrm U(6)$ and $\Sigma=\langle\phi\phi^\dagger\rangle$ on a *complex* carrier; H-link is stated as $V_{\rm link}\otimes\mathbb C^m$ (SM:362); SM:505: the carrier is "equipped after-the-fact with the complex inner-product structure $V_K=\mathbb C^6$"; SM:809 names "the real-to-complex step" as an open joint of the explicit map. See F4. |
| §4.2 staggered factorization (SM:286–292) | Operator identity only; the "measure and observable map relating those scalar variables to the determinant-pseudofermion representation" is open (SM:290–292). |
| §4.7.1.1–§4.8 (SM:485, SM:545, SM:551) | Effective actions $\bar\psi K_{\rm eff}\psi$ (Grassmann/fermion bilinears) and "the Schur complement over the hidden sublattice — a standard procedure in lattice QFT [12, 17]". |
| §4.7 spin–statistics (SM:454) | "Singlet → spin-0 → boson … Triplet → spin-1/2 → fermion": imports the spin–statistics association; conditional on H-spin'. |
| §4.11 (SM:611) | "The unique renormalizable unitarity-preserving mechanism is the Higgs [13, 14]" — QFT import; the Higgs doublet is phenomenological input (SM:468). |
| §5.2 Theorem 18 (SM:635) | θ-term of an emergent Yang–Mills Lagrangian; T-invariance of that Lagrangian inherited by assertion. |
| §6.1 (SM:681–683; cited by §4.6 Remark SM:428) | Induced coupling from "the fermion determinant", vertex $V_j=igμT^\alpha\cos(\cdot)$, one-loop staggered vacuum polarization; uses the fermionic measure whose substratum source SM:290–292 lists as open. |

Steps of SM §§3.1, 4–5 that are native (no quantum input): Theorem 1a and Corollary 1a
(SM:242–268, classical Koopman/Mori–Zwanzig, explicitly "without assuming quantum mechanics",
SM:268); the form lemma (SM:224); Theorem 7 (SM:374); Theorem 8 (SM:434); Theorem 3
(SM:302); Theorem 17 and Theorem 19 (SM:625, SM:641, proved by counting; K `theorem_19`);
Proposition 20 (SM:647); Theorem 15's anomaly algebra given its inputs (SM:589).

### 3.3 Verdict on Sub:68

**Finding F1.** As made, Sub:68 overstates the forward direction. (a) Main's forward content
reaches finite-law representability (universal, non-selective) and a characterization of
operational QM *conditional on* complex kinematics given and five conditions, one of which the
substratum is shown not to supply. (b) SM's forward chain takes the emergent quantum
description as a declared prerequisite and, at the steps listed in §3.2, uses quantum and
quantum-field-theoretic structure (quantized oscillator states, a Coulomb Hamiltonian, a
complex carrier, Grassmann effective actions, the fermion determinant, an emergent Yang–Mills
Lagrangian) whose derivation from $(S,\varphi,V)$ is either stated open in SM itself
(SM:232, SM:290–292) or not addressed. The forward results that are native (§3.2, last
paragraph) are classical or representation-theoretic. Related assertions of the same form:
Sub:26 ("The trace-out at the visible-sector level produces … the wave function, the SM gauge
group, particle content"), Sub:459 ("Quantum mechanics is the observer's compressed
description of the visible sector"), Sub:463 (double-slit traversal statement). Each asserts
more than Main/SM prove, which stop at $Q_{\rm fb}$ and conditional operational/SM statements.
Sub's own scoped statements (Sub:14, Theorem 23 at Sub:193, Sub:373) stop where Main and SM
stop: complex matrix kinematics taken as given, condition (iv) not supplied, the SM-sector
hypotheses carried, Bell conditional on H-Bell. Sub:68 is therefore a sentence-level
overstatement, inconsistent with those statements in the same paper.
(Manuscript change is outside this unit's authorization; recorded only.)

***

## 4. Premise / bridge ledger

Columns: **(i)** mathematically well-defined; **(ii)** follows from independently justified
OI principles (justification type per §1; "none identified (open)" means no QM-independent
reason found in the files read, §0); **(iii)** reproduces the QM/SM prediction. Level and
status as in §1. Column (iii) is not support for column (ii).

| ID | Source | Exact assumption | Lvl | (i) | (ii) | (iii) | Status / gap |
|---|---|---|---|---|---|---|---|
| B1 | Main:44, Main:48–56; posit ledger Main:726 (i)–(ii) | Finite total $S$, bijection $\varphi$, proper $V\subsetneq S$ | F | Yes | Axiom 1 gives per-moment finiteness of $V$ (Main:48); total finiteness is a posit (ii); recurrence is Axiom 2 (i). **St/Op** | Not applicable alone | Posit; finiteness of hidden sector open beyond the finite representative (Sub:92). |
| B2 | Main:56, Main:62, Main:726 (iii); Sub:94 | Bijectivity of $\varphi$ | F | Yes | Partly: record-preservation prong is D; the hidden-margin prong uses "observed statistics … doubly stochastic class" and "unitary emergent statistics are unistochastic" (Main:62). **D + E (quantum data)** | Consistent with near-unitarity | Conditional; one prong is empirical selection from quantum statistics. |
| B3 | Main:56, Main:726 (iv) | Counting (maximal-entropy) measure / uniform hidden prior | F/O | Yes | **Op** ("standard but substantive epistemic postulate, not derived", Main:726 (iv)) | Fixes the probabilities that the Born form later represents | Posit. |
| B4 | SM:66–70; Main:726 (viii) | Site factorization $S=\prod_i S_i$ | F | Yes | **none identified (open)**; "Whether the observable law, the observer's registers or the dynamics select the spatial identification … is open" (SM:68); coupling-degree minimization fails (SM:68, ring counterexample) | Required for every spatial/SM result | Open (named gap SM:68). |
| B5 | Sub:96; Main:726 (ix) | Bounded coupling degree (A3) | F | Yes | **Op** (locality) | — | Posit. |
| B6 | SM:226, SM:70, Main:726 (x); Theorem 7b SM:390–416 | Nearest-neighbour simple-cubic graph | F | Yes | NN range: **St** ("adopted as the minimal local branch", SM:226). Simple-cubic Bravais type: **E** — selected "because $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm U(1)$ is observed" (SM:1424; Sub:203) | Yes, by construction of the selection | Posit + empirical selection. |
| B7 | Sub:98; Main:726 (xi); SM:236, SM:270–276 | Center independence A4 (translation clause; no-self-term clause); and observer-level CI ($p_0=0$) | F (A4); O (observer-level) | Yes | A4: **E** (its "observational anchor is the homogeneity of physical law"; whether the observer architecture independently warrants it is open, Sub:98); QP Lemma Q shows A4 does independent work at $q=2$ (QP:458–527). Observer-level CI: **none identified (open)** — "microscopic CI alone does not imply $p_0=0$" (SM:276, swap counterexample SM:236) | Needed for $A/(2d)$ and the wave branch | A4 posit; descent to observer level open (SM:276). |
| B8 | Sub:100, Sub:270–274; SM:240; Main:726 (vii) | Linearity A5 | F | Yes | Affine part: **Op** — follows from the amplitude-scale (additive-automorphism) gauge principle, which Sub:272 states is an "operational input … not a theorem"; deriving it from observer architecture "is … circular" (Sub:272). Affine → linear: **St** ("imposed", Sub:100; SM:240 counterexample to its derivation from CI); the corpus search of `A5-LINEAR-AFFINE.md` (WIP / UNVERIFIED, row R5) finds that none of its candidate principles "selects b = 0 with an independent justification" | Needed for oscillator/Gaussian and staggered structure | Posit (sharpened stipulation, Sub:274). |
| B9 | Sub:82 (E4); Main:726 (vi) | Spatial isotropy | F/O | Yes | **E** (empirical input E4). Quadratic isotropy at observer level is then D given cubic symmetry (Corollary 1a) | — | Empirical input. |
| B10 | Main:726 (xiii) | Second-order form $x(t+1)=F(x(t))-x(t-1)$ | F | Yes | **St** ("a posit of the selected lattice model, not derived and not an axiom of OI") | Gives bijectivity automatically (SM:106) and the phase-space pairing used in NQ1 | Posit. |
| B11 | Sub:102; Main:726 (xii); SM:114–118 | Background independence A6 (link data transported covariantly) | F/O | Yes | **St**; "in the form formalized imposes no restriction on the rule" (Main:726 (xii)); link dynamics by the Wilson functional "is not derived here" (SM:118) | Local gauge reading | Posit; link dynamics open. |
| B12 | SM:232, SM:316, SM:326 | Observer-level lift $\varphi\to L_{\rm obs}\to\Delta_g$ (normalization $\alpha=1/d$, real/complex wave operator, coarse-graining) | F→O | Target object well-defined; the map is not specified | **none identified (open)**; "not proved anywhere in this framework" (SM:232) | §4 dispersion, Lorentz argument, mode count rest on it | Open (named gap SM:232). |
| B13 | SM:360–366; SM:72 | **H-link**: $V_{\rm phys}\cong V_{\rm link}\otimes\mathbb C^m$; single-copy $m=1$ | O | Yes | **none identified (open)**; "No theorem … derives $m=1$" (SM:364). The $\otimes\mathbb C^m$ also carries the carrier's complex structure (F4); it is not listed among Theorem 5's premises, and SM:809 names the real-to-complex step as open | Gives $K=6$, $N_f=6$, the $(3,2,1)$ carrier | Conditional bridge; open. |
| B14 | SM:340–344, SM:374, SM:136 | **H-cust** (kinetic clause; condensate clause) and $O$-equivariance of $\Sigma$ | O | Yes | Kinetic clause: **D** at the symmetric point for the component-complete site observer (Prop. 4b, SM:334–336). Condensate clause and $O$-equivariance of $\Sigma$: **none identified (open)**; "a hypothesis on the solution rather than a consequence of the dynamics" (SM:136) | $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$ stabilizer | Conditional; condensate clause open. |
| B15 | SM:12, SM:334–338 | **H-blind** (observation commutes with signed permutations of carrier components) | O | Yes | **D** for the branch's own observer class at $M=\mu I_6$ (SM:336); **none identified (open)** for other observer classes | Common cone | Proved for one class; conditional otherwise. |
| B16 | SM:448–452 | **H-spin'** (triplet tastes are physical spin-1/2) | O/Q | Yes | **none identified (open)**; free-kernel form H-spin *disproved* (Clifford relations fail; SM:452); 4D route disproved (SM:452); dressed-kernel candidate class nonempty, selection open | Three generations of spin-1/2 matter | Open (H-spin refuted; H-spin' open). |
| B17 | SM:543–545, SM:555 | **H-χ'** (taste-chirality-selective SU(2) embedding) | O/Q | Yes | **none identified (open)**; minimal embedding certified vector-like (SM:543). Anomaly cancellation is **C**, explicitly "a consistency check on the hypothesis rather than a derivation of it" (SM:555) | Chiral SU(2) | Open. |
| B18 | SM:464–468 | Higgs doublet $(\mathbf1,\mathbf2,+\tfrac12)$ | Q | Yes | **E** ("taken as phenomenological input", SM:468) | Yes by input | Input. |
| B19 | SM:170–210; Sub:84–88 | $d=3$ via E5–E7 | O/Q | Yes | **E**; E6 uses the quantum Coulomb bound-state statement (SM:176); E7 is an inferred cosmological quantity (Sub:88) and inherits the GR horizon conditions (SM:196) | $d=3$ | Self-consistency selection (SM:1424). |
| B20 | Sub:123, Sub:131–133; Main:403–414, Main:429 | **M1-B / ontic parameter dependence**, measurement independence, **H-Bell** (preparation-indexed adjacency with operational no-signalling and curvature stability) | F/O | Partly: "preparation-indexed adjacency" is not specified as a rule | Ontic parameter dependence: **E + St** — a completion reproducing the observed Bell violation (E2) must give up ontic parameter independence or measurement independence (Main:403–406); which one is given up is a choice (St), the measurement-dependent alternative requiring $I_{\rm ont}\ge0.0309$ bits (Main:22). Measurement independence: **Op** ("a posit about the initial condition, not derived", Main:407). H-Bell: **none identified (open)** | Quantum Bell violation by design | Open; reference graph gives CHSH $\le2$ (proved). |
| B21 | Main:20, Main:556, Main:226 | Born dictionary $p=\lvert U\rvert^2$ (definition of $Q_{\rm fb}$); quadratic exponent | O | Yes | Dictionary: **St** (definitional). Exponent: **none identified (open)**; "a frontier item about the dictionary's origin" (Main:556) | Yes by definition | Definitional; exponent selection open. |
| B22 | Main:218, Main:564, Main:82 (4), Main:590 | Complex matrix kinematics with tensor-product composite; five completion conditions; (iv) full reversible control | O | Yes | Kinematics: **none identified (open)** ("deriving that kinematics is open", Main:218). (iv): not supplied by the substratum's stated interventions (K `substratumGen_not_control`, two-state carrier). Which of (i)–(iii), (v) the substratum supplies: open (Main:82) | Exact finite operational QM iff (i)–(v) (K) | Characterized; sourcing open; (iv) negative on the stated intervention class. |
| B23 | Main:590; GR:260, GR:270 | Phase intervention; layer-flow executability (continuous state mixing) | O | Yes | Phases: **St** — "a stated intervention principle rather than a consequence of its finite states and bijective dynamics". Layer flow: **none identified (open)**; "the executability of that flow being an assumption not derived"; the observer-level lift, "in every formulation stated that lands in the operational interface, derives neither a non-monomial admissible operator nor the layer flow, the site-space wave-operator formulation being unresolved rather than excluded" (K `obs_not_layerFlowExecutable`, `substratumTheory_not_layerFlowExecutable`, `coherentLiftClass_eq_substratumClass`) | With both added, equivalent to operational QM (K `derivedOI_qm_iff_layerFlowExecutable'`) | Open; negative for the stated substratum dynamics with read/write access and for the stated lift formulations that land in the operational interface; unresolved for the site-space wave-operator formulation (no operational map from it to the configuration carrier is stated, GR:270). |
| B24 | SM:290–292; SM:681 | Fermionic measure: map from scalar substratum variables to the determinant-pseudofermion representation; Gaussian stationary law | F→Q | Target well-defined; map unspecified | **none identified (open)**; "Both are open; the operator identity alone establishes neither" (SM:290); exact linear rule not single-cycle on shells (SM:296) | Needed for §6 induced couplings | Open. |
| B25 | QP:124–176 (apparatus-1 posits); QP:805–840 | Access posits P1 (terminal registration), P2 (half-known ready cells), P3 (armable couplings), E-iso, H-PREP; extension NNB; premise I | O | Yes | P1–P3, E-iso: **St** (supplied access posits, QP:173). H-PREP: open identification (QPR:21–22). NNB: **none identified (open)**; candidate source: odd cycles in the state-dependent graph (QP:822–827), examined for SM:112's rule and a symmetrized variant in MECH-1 DESIGN:877–893, MECH-2 §0 and M-INACC-1 (§10). I: **QS** — "defined by the target and is easy to vary" (QP:836) | NNB gives encoded $S$, H at single-qubit stabilizer scope; fails composites (QP:746–768) | Supplied/conditional; I not adopted. |
| B26 | Main:274, Main:226; GR §3.2 | Continuous-time interpolation $U_t=e^{-i\hat Ht}$; $\hbar$ | O | Yes | **St**: "additional structure, chosen rather than derived" (Main:274). Derived, but not an available operation: an exact strongly continuous path of $*$-automorphisms from the identity to the update's Heisenberg action, with no one-parameter-group law and no generator (Main:274; K `driveQ_isContinuousPath`). $\hbar$'s value conditional on H-slope (Sub:181–185) | Hamiltonian form | Choice; conditional. |
| B27 | Main:726 (v); Sub:135 | Hidden-sector mixing hypothesis (ETH-motivated) | F/O | Yes | **Op** (physical motivation only); open for the realized hidden sector (Sub:135; SM:296 shows the exact linear rule is not single-cycle) | Slow-bath form of C2 | Open. |

**Counts.** Rows of the 27 whose column (ii) carries each type (a row can carry several): D
wholly 0; D for one prong or a stated restricted class 4 (B2 record-preservation prong, B9
observer-level quadratic isotropy given cubic symmetry, B14 kinetic, B15); Op 6 (B1, B3, B5, B8 affine, B20 measurement independence, B27); E 7 (B2, B6
Bravais, B7 A4, B9, B18, B19, B20 ontic dependence); QS 1 (B25 I); St 10 (B1, B6, B8, B10,
B11, B20, B21, B23, B25, B26); C 1 (B17); "none identified (open)" 14 (B4, B7, B12–B17,
B20–B25). These counts are of this table only and carry no weight beyond it.

***

## 5. Chain ledger: substratum → observer lattice → SM → QM

Each step is classified by proof level and by status with its verification layer; the
weakest-link column states what the step inherits.

| # | Step | Source | Lvl | Status [layer] | Inherits / named gap |
|---|---|---|---|---|---|
| S1 | $(\varphi,V,\mu_H)\mapsto$ visible stochastic law $T(t)$ | Main:86–92, Main:117 | F | Proved [A] | B1–B3 |
| S2 | $S\iff D\iff Q_{\rm fb}$ | Main:548, Main:99 | O | Proved [K] | Born dictionary definitional; exponent not selected (B21) |
| S3 | C4 ⟺ $M_t>0$; hidden predictive memory in every faithful completion | Main:99, Main:173–176 | F/O | Proved [K for the pushforward identity; A for CMI vanishing criterion, "not formalized", Main:99] | — |
| S4 | Recurrence-cycle P-indivisibility | Main:115–145 | F | Proved [K + A] | Total finiteness posit |
| S5 | Permutation-dilated channel is CPTP, diagonal-preserving; CP-indivisible in that class | Main:282–336 | O | Proved [A, X] | — |
| S6 | One-step non-EB coherence for the $\mathbb F_2$ linear update with bulk | Main:296–326 | O | Proved [A + K] for that realization, $q$ prime | Off-diagonal inputs not sourced; no phase generated (Main:306) |
| S7 | Operational completion characterization | Main:564, Main:584–590 | O | Proved [K] as a characterization | Complex kinematics given; (iv) not supplied; phases stated; layer flow not executable by the stated substratum and lift classes, site-space wave-operator formulation unresolved (B22, B23) |
| S8 | Graph causal cone; Bell ceiling under screened local hypotheses | Main:364–391 | F | Proved [A + X check 11] | B4 site factorization |
| S9 | Quantum Bell violation on the SM/GR graph | Sub:131–133, Main:414–416, Main:429 | F/O | Conditional on H-Bell; open | B20 |
| S10 | Form lemma: center-free, isotropic, linear NN rule $=\alpha\sum_{j\sim i}x_j - x_i(t-1)$ | SM:224–228 | F | Proved [A] within its hypotheses | B4–B8, B10 |
| S11 | Theorem 1a / Corollary 1a: equivariant projection forbids quadratic anisotropy | SM:242–268 | O | Proved [A; K `ohInvariant_iff`, `rem_littleO`, `rem_bigO`] | Nondegeneracy $b_m\ne0$ not supplied (SM:264) |
| S12 | Corollary 1b: $T=A/(2d)$ | SM:270–276 | O | Conditional on observer-level CI | B7 descent open |
| S13 | $\varphi\to L_{\rm obs}\to\Delta_g$ | SM:232 | F→O | Open | B12 |
| S14 | Theorem 2: $D_{\rm st}^2=-\tfrac14\Box_{\rm lat}$ | SM:286 | O (operator) | Proved [I, Susskind] as an operator identity | Measure reduction open (B24) |
| S15 | Theorem 3: chiral symmetry ⟺ vanishing onsite terms (opposite-parity hopping) | SM:302–304 | O | Proved [K `scalar_center_chiral_iff`] | Identification with substratum CI open (SM:306) |
| S16 | Theorem 7: six links $=T_1\oplus E\oplus A_1$ | SM:374–376 | F (geometry) | Proved [A + K `theorem_7`] | — (physical reading needs B13) |
| S17 | Theorem 5: stabilizer $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$ | SM:340–344 | O | Conditional on H-link + H-cust + $O$-equivariant $\Sigma$ + complex carrier | B13, B14, F4 |
| S18 | Reduction to $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm U(1)$; Prop. 14a | Sub:163; SM:579–585 | O | Conditional: "a specified charged matter action" and amplitude-scale gauge (Sub:163); Prop. 14a proved [A] as group theory, physical selection of $K$ "additional physical input" (SM:585) | B8, B13 |
| S19 | Local gauge invariance | SM:114–118 | O | Conditional on A6; link dynamics not derived | B11 |
| S20 | Theorem 8: taste $4=1\oplus3$ | SM:434–436 | O (geometry) | Proved [A + K `theorem_8`] | — |
| S21 | Theorem 9 / generations / spin–statistics | SM:448–454 | O/Q | H-spin *disproved* [X, exact probes, SM:452]; H-spin' open | B16 |
| S22 | Theorem 12: checkerboard = $\gamma_5\otimes\xi_5$ grading | SM:535–537 | O | Proved [A + X exact probe] | Bipartite NN graph (B6) |
| S23 | Theorem 13: chirality | SM:543–545 | O/Q | Conditional on H-χ'; minimal embedding vector-like [X] | B17 |
| S24 | Theorem 15: hypercharges | SM:589 | Q (algebra) | Proved [I + A] given chiral group, five-rep family pattern, family universality | Pattern selection open (SM:458) |
| S25 | Theorem 19: reciprocity $T_{ij}=T_{\theta j,\theta i}$ | SM:641–643 | F | Proved [K `theorem_19`] | Second-order form (B10) gives the involution |
| S26 | Theorem 18: $\theta\in\{0,\pi\}$ | SM:633–635 | Q | Conditional on an emergent T-invariant Lagrangian with a θ-term | Emergent Lagrangian not derived |
| S27 | §6 induced coupling $1/\alpha_0=23.25$ | SM:681–683 | Q | Computed [N/A, lattice integral] on the conditional branch; uses the fermion determinant | B13, B24; thresholds fitted (R class) |
| S28 | $d=3$ | SM:170–210 | O/Q | Conditional (self-consistency, empirical filters) | B19 |
| S29 | Discrete Einstein via hop-metric Ollivier curvature | SM:144–150 | F→O | Hop-metric route **disproved** for the reference family [A: $\ell_1$ hop metric, $\sqrt2$ diagonal stretch at every scale, SM:150]; continuum Einstein open | Route (A) proposed, not carried out |

**Weakest links of the composite chain.** Substratum → $Q_{\rm fb}$: proved (S1–S5), but
non-selective. $Q_{\rm fb}$ → operational QM: open (S7; B22–B23). Substratum → observer-level
wave operator: open (S13). Observer-level operator → SM gauge group: conditional on H-link,
H-cust, complex carrier (S17). → SM matter: conditional on H-spin', H-χ', Higgs input,
fermion measure (S21, S23, B18, B24). → Bell: conditional on H-Bell (S9). The composite
"substratum → SM as a quantum field theory" therefore takes the status **open**, with the
first open links at S7 and S13 (both before any SM-specific bridge).

### 5.1 FI-1 and the frontier of the forward chain

**Statement.** The forward chain is proved through S1–S6: the finite bijection with its
visible/hidden trace-out gives finite visible laws and their fixed-basis unitary/Born
representation, $S\iff D\iff Q_{\rm fb}$ (Main:548), and on the configuration carrier the
operations it supplies are monomial (permutations, read/write, and the phase when adjoined;
Main:270, GR:260, GR:270). Beyond that level the chain needs several implications it does not
have, which the sources keep separate (*Position*, below). The one stated here is

> **(FI-1)** *the substratum's finite bijective dynamics, with the visible/hidden trace-out
> and the observer's stated read/write access, supplies a non-monomial admissible operator on
> the configuration carrier at level one* (the carrier $S\times\mathrm{Fin}\,1$ of
> K `exists_nonMonomial_of_layerFlowExecutable`; GR:270, "a non-monomial admissible operator at
> level one").

"Non-monomial" and "state-mixing" are different predicates for a general Kraus operator:
$K=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ is non-monomial and $X\mapsto KXK^\dagger$ preserves
diagonal states; for unitaries the two coincide [A; exact check K2]. FI-1 uses the first. The
stronger requirement, an available operation that does not preserve diagonal states, is also
necessary (K `gateFlow_half_not_preservesDiag`).

- **Conditionality.** FI-1 is posed on a stated input, not on an implication: the observer's
  stated read/write access. In the kernel that access is a family of permutations supported on
  two *states* of an arbitrary finite carrier (`ReadWriteFamily (a b : S)`,
  OB/ReadWriteControl.lean:86–89), its theory `permTheory` is defined on every finite carrier,
  and the observer theory depends on the substratum only through its configuration set
  (K `obsTheory_rule_independent`; "configuration-level sourcing consumes nothing of A3–A6",
  SubstratumInterfaceAudit docstring). The necessity theorem and its companion hold for every
  finite carrier and every involution with a moved point
  (K `exists_nonMonomial_of_layerFlowExecutable`, `layerFlowExecutable_of_control`), and the
  equivalence is "stated for each involution with a moved configuration, whether or not it is a
  gate of that factorization" (GR:270). So FI-1's statement, its one-directional necessity and
  its negative under the stated access hold on any finite configuration set with a bijection,
  and consume neither the site factorization (B4) nor the second-order form (B10). Those two
  inputs act upstream of other things: the physical identification of the carrier with lattice
  fields and the choice of its shear and swap layers (the concrete instance
  K `derivedOI_qm_iff_layerFlowExecutable_swap'`, GR:270); the cell-based access posits
  P1–P3, E-iso and H-PREP of QP's class N (QP:124–176), whose processes QP:846–877 maps into the
  same `permTheory` by a paper argument, so that FI-1's negative covers them without resting on
  them; the spatial route and S13, FI-1's candidate source 1; and H-Bell's graph (S8, S9). The
  phase is not used by the statement, the necessity or the negative: the substratum class,
  which contains the phase, is monomial as well (`substratumClass`).
- **Scope of necessity.** FI-1 is necessary, in one direction only, for exact finite
  endomorphic operational QM within the structural architecture on the configuration carrier.
  A theory generated by an architecture (`genTheory 𝓘 arch S`, the class in which the theorem
  is proved) that executes one layer flow of an involution with a moved configuration has a
  non-monomial admissible operator at level one (GR:270;
  K `exists_nonMonomial_of_layerFlowExecutable`), and exact QM executes every layer flow
  (GR:270; K `layerFlowExecutable_of_control`). With the phase intervention stated,
  executability is equivalent to that QM (Main:590, GR:268; K `derivedOI_qm_iff_layerFlowExecutable'`);
  the phase is used for the equivalence, not for the necessity. Three limits:
  - *Not sufficient.* The polarized closure `PolC` has the phases, non-monomial admissible
    operators and the whole closure `DerivedOI`, executes no layer flow and is not QM
    (K `polarizedTheoryC_derivedOI`, `polarizedTheoryC_not_qm`, both on the two-state carrier,
    which suffices to refute a universal implication; `polarizedTheoryC_not_layerFlowExecutable`,
    on every finite carrier).
  - *Not the sharpest necessary condition.* Executability forces uncountably many pairwise
    non-proportional non-monomial rays at level one
    (K `uncountableNonMonomialRays_of_layerFlowExecutable`; also
    `uncountable_of_layerFlowExecutable`), which `PolC` fails
    (`coherent-continuum-source-audit.md`, route S4). Exact QM implies it directly on the
    two-state carrier (K `uncountableNonMonomialRays_of_qm`); the general-carrier form follows
    by the same composition but is not stated as a theorem.
  - *Not necessary for weaker targets.* Finite reversible deterministic realizations by fixed
    bijections, monomial on their configuration carrier, reproduce arbitrary finite quantum
    experiments, incompatible measurements and adaptive interventions included, to any finite
    accuracy (Main:566, Main:584), with two-sided ε-density (Main:600). These are QM → OI
    results and do not count toward the forward bridge (§2); they confine FI-1's necessity to
    the exact target. On encoded carriers, non-monomial encoded maps arise without FI-1: QP's
    NNB gives encoded $S$ and $H$ at single-qubit stabilizer scope while every operation stays
    in `permTheory` (QP:79–98, QP:846–877); MECH-2's Theorem U2 places the encoded unitaries
    that fixed bijections induce in $A_4\wr S_n$, whose tetrahedral rotations include
    non-monomial ones, and its Theorem NC gives a noncontextual configuration-level model of the
    encoded theory (MECH-2 §0). Neither is a counterexample to "not supplied".
- **Closest derived objects.** The layer flows, one-parameter unitary groups of the layers'
  gates (OB/SecondOrderCircuit.lean, OB/SwapLayer.lean), carried to the all-sites layer as
  automorphisms of the quasilocal algebra (OB/SecondOrderLayer.lean), and the exact continuous
  path of Main:274 (K `driveQ_isContinuousPath`; B26) are derived, and the flows'
  intermediate-time points are non-monomial (K `gateFlow_not_monomial`). They are mathematical
  objects, not available operations (`coherent-continuum-source-audit.md`, route S5;
  `exec-source-audit.md`, entries X2 and X5). "Supplies" in FI-1 means "makes available as an
  admissible operator".
- **Source anchors.** Main:590; GR:268, GR:270; Main:218 (complex matrix kinematics taken as
  given); SM:232 (the map $\varphi\to L_{\rm obs}\to\Delta_g$ "is not proved anywhere in this
  framework"); `exec-source-audit.md` (outcome: the frontier "is two named assumptions, the
  phase intervention and the executability", with the necessary condition "a non-monomial
  admissible operator at level one"); `c5-discovery-audit.md` (T0,
  K `obligations_independent`, on the two-state carrier); `coherent-continuum-source-audit.md`
  (the strengthened condition; outcome 2, "no current source").
- **Status.** Not supplied by the stated read/write access. Every operation it supplies is
  configuration-level: the observer theory is `permTheory` on the configuration space
  (K `obsTheory`, OB/SubstratumInterfaceAudit.lean:770) and lies inside the substratum theory
  (K `obs_availExt_le_substratum`, :837), whose class is the monomial operators
  (`substratumClass := IsMonomial`, OB/StructuralClosure.lean:180); the read-write operators are
  permutation matrices (GR:260; K `bijectiveOperator_monomial`, `readWriteOperator_monomial`);
  `exec-source-audit.md`'s scope amendment states "every operation supplied by the stated
  observer access is configuration-level, in `obsTheory 𝒮` permutation-valued". Feed-forward is
  part of every finite operational theory (`availExt_bind`, OB/OperationalAssembly.lean:617), so
  adaptive processes are covered at configuration level, and QP:851–863 maps the adaptive
  processes of QP's class N, with or without NNB, into `permTheory` by a paper argument. Not
  supplied by any lift formulation stated that lands in the operational interface
  (K `coherentLiftClass_eq_substratumClass`; GR:270). The layer-flow negatives
  (`substratumTheory_not_layerFlowExecutable`, `obs_not_layerFlowExecutable`) concern
  executability, of which FI-1 is only a necessary condition, and are not cited for its
  failure; `readWriteSourced_not_qm` is excluded (§8 F9). **Open**, as candidate sources:
  1. the site-space wave-operator formulation of SM §4.1, "unresolved rather than excluded".
     Two gaps stand there: the map $\varphi\to L_{\rm obs}\to\Delta_g$ itself is not proved
     (SM:232), and no operational map from that formulation to the configuration carrier is
     stated (GR:270;
     `lift-source-audit.md` records what such a map would have to supply);
  2. whether every realization of the lift's channels is configuration-level (GR:270);
  3. the C5 discovery audit's candidate 2: a polarization of the per-site phase space
     $V\times V$, whose Weil image sends the swap layer to the Hadamard matrix, which is not
     monomial (K `hadamard_not_monomial`, `polGen_not_configurationLevel`); verdict C,
     underdetermined, because the corpus does not supply the map (`c5-discovery-audit.md`,
     test 8 and T6). The closure `PolC` built from it executes no layer flow (above). NQ1
     studies a structure of the same kind, a complex structure on the real lift's phase space
     (§11); the two are related as phase-space structures the corpus does not supply, and no
     map between them is stated;
  4. extended access, such as a coupling that is not bijection-valued, which Main:590 adds "as
     an empirical controllability resource" and which `state-mixing-coupling-audit.md`
     constructs only from a postulated datum ("the datum is a postulate, and nothing here
     derives it", OB/StateMixingCoupling.lean:7).

  The adaptive question the corpus leaves open concerns the encoded quarter phase $S$
  (QP:897–915; `quarter-phase-feedback-20261107/RESULT.md`), a different object, which by the
  previous bullet does not need FI-1.
- **Position.** (a) Every earlier step (S1–S6) is proved. (b) The phase is not generated
  either (GR:260: every isometry the dynamics and stated access supply fixes the all-ones ray;
  for any architecture whose admissible isometries do so, failure exhibited at level one), and
  it is an obligation independent of the *layer flow*: the substratum theory has the phases and
  executes no layer flow, while the ones-fixing theory executes every layer flow, has no quarter
  phase and is not QM (K `obligations_independent`, on the two-state carrier;
  `onesTheory_layerFlowExecutable`, `onesTheory_not_qm`; exact check K4 illustrates the two
  necessary conditions, a non-monomial operator and an operator moving the all-ones ray, as
  independent at the operator level). The independence is from the layer flow, not from state
  mixing in every form. The layer flow fixes the all-ones ray and, with the sourced closure and
  without the phase, does not give phase-free richness (K `onesTheory_not_phaseFree`, on the
  two-state carrier, and `flow_endpoint_refuted_general`); with the phase it does
  (K `phaseFree_of_derivedOI_layerFlowExecutable`). A continuously driven transition
  $e^{-itX_{ab}}$ on three or more states sends the all-ones vector to
  $e^{-it}(e_a+e_b)+\sum_{c\ne a,b}e_c$, so it moves that ray at every $t\notin2\pi\mathbb Z$; it
  is non-monomial at $t\notin\tfrac{\pi}{2}\mathbb Z$, a restriction needed for non-monomiality
  only [A; exact checks D and Y]. One such transition with the exchanges, implementation locality
  and embedded observation gives exact finite endomorphic operational QM, the phases included
  (GR:250–258; Main:590; K `oiPlusMin_iff_qm`, `derivedOI_of_qm`). No phase operation enters that
  repertoire (GR:250), but the drive carries the phase. On three states
  $e^{-i\theta X_{ab}}=e^{-i\theta}\,G_{(ab)}(2\theta/\pi)\,\mathrm{diag}(1,1,e^{i\theta})$, with
  $G_{(ab)}$ the layer flow of the transposition, so the driven transition is that layer flow
  times a continuous relative phase on the configurations it fixes [A; the single-transposition
  case of K `gateFlow_isolation` (OB/LiftAudit.lean:660) with the group law `unit_mul_unit`;
  GR:270; exact check I]. At a quarter turn, composed with the exchange,
  $e^{-i\frac{\pi}{2}X_{ab}}\,\mathrm{swap}(a\,b)=-i\,\mathrm{diag}(1,1,i)$, whose conjugation
  channel is the quarter phase on the third state; availability is closed under that composition
  (K `avail_conj_mul`, OB/LiftAudit.lean:770), and permutation transport carries it to every
  state of a three-state level [A; exact check Q]. There the drive is monomial and still moves the
  all-ones ray. On larger levels the phases follow through the equivalence
  (K `derivedOI_of_qm`). A real rotation $e^{\theta(E_{ab}-E_{ba})}$ also moves the ray and mixes
  states, but with the permutations it generates only real orthogonal operators,
  $\mathfrak{so}(3)$ on three states against $\mathfrak{su}(3)$ for the driven transition, and no
  quarter phase [A; exact check R]; it is the "pair rotation at a quarter turn, which carries no
  phase at all" of `frozen-sourcing-audit.md`:289. So under phase-free richness no separate phase
  operation is needed because the complex driven transition contains the phase: the phase
  obligation moves inside the mixing obligation, as the requirement that the mixing source be that
  complex transition and not a real rotation, and is not removed. Beside the layer flow the phase
  is a separate obligation. FI-1 is
  therefore the first unsupported step on the route to exact finite endomorphic operational QM
  only once the phase is taken as stated, which is how Main:590 and GR:268 state their
  equivalence; it does not precede the phase in any logical order. (c) H-Bell (S9) is a further
  unsupported implication, not derived from FI-1 and not deriving it in the sources read. It is
  posed within the bijective dynamics, as preparation-indexed adjacency on the state-dependent
  graph $G(x)$ (Sub:131), which is configuration-level by construction; Main:566 and Main:584
  add that quantum statistics alone need no non-monomial operator at finite accuracy, though
  their realizations have no spatial graph (Main:362) and H-Bell's condition (iii) is a
  curvature condition on the prepared graphs (Sub:133). No independence theorem between H-Bell
  and FI-1 or the phase is stated. (d) On permutation unitaries the Born exponent has no
  content: their entries are 0 or 1, so $\lvert U\rvert^p$ gives the same table for every
  $p>0$ (Main:556). On weighted monomial Kraus families, such as QP:855's $2^{-k/2}P_\sigma$,
  the $\lvert K\rvert^p$ table is normalized only at $p=2$ [A; exact check K3], a consequence
  of the quadratic Kraus normalization, not a selection of the exponent. (e) SM's forward
  chain consumes the emergent quantum description (SM:22). The bridges whose content is
  operational or field-theoretic, H-spin', H-χ' and the fermionic measure, presuppose the
  operational QM for which FI-1 is necessary. The carrier's complex structure (F4, NQ1) is
  posed on the real lift and does not presuppose FI-1. (f) On the spatial route, site
  factorization, the nearest-neighbour cubic graph, A4 and A5 enter as stated inputs (B4–B8),
  not implications; the open implications there are S13, the map
  $\varphi\to L_{\rm obs}\to\Delta_g$ on which SM §4's dispersion, Lorentz and mode-count
  statements rest, and S12, the descent of center independence to the observer level
  (SM:276). S13 is the same SM §4.1 lift as FI-1's open candidate source 1 (GR:270 names it
  "the observer-level lift of [SM §4.1]"), so the quantum route and the spatial route meet at
  that object.
- **Not established here.** That FI-1 fails for the site-space formulation or for the
  polarization candidate's map; that no extension of the access supplies it; any order among
  the phase, FI-1 and H-Bell; any independence among them beyond the scoped forms in (b) and
  (c).

### 5.2 The foundation questions, answered from the sources

Owner instruction of 2026-11-09 (relayed by the coordinating session). Status terms:
*derived*, *independently justified*, *assumed*, *open*, *excluded under stated conditions*;
and *not derived* where the sources show non-derivation without exclusion.

| Question | Answer from the sources | Status | Sources |
|---|---|---|---|
| Site factorization | Not derived from OI and not independently justified. "The dynamics alone has not been shown to select the identification, which is therefore an input"; the coupling-degree minimization route fails on a ring counterexample. It is item (viii) of the posit ledger, and every spatial result and the kernel's `Substratum` take it as given. FI-1's statement and its negative under the stated access do not use it (§5.1 *Conditionality*). | **Assumed**; whether it is derivable is open | SM:66–70; Main:726 (viii); B4 |
| Observer read/write access | OI does not establish it; the access is stated. The kernel sources the read-write families and exchanges into `permClass`, whose theory is the observer theory, and proves the structural closure of the substratum class with the phases stipulated; the native-class posits P1–P3 and E-iso are supplied access posits, H-PREP is an open identification, and the only preparation assumed is a maximally mixed ancilla. The interface the forward construction needs for exact finite operational QM is not established: the stated one lacks the phases and executes no layer flow, and the phases are adjoined by stipulation. | Access **assumed**; its sufficiency for the target **excluded under stated conditions** (the stated access, on the configuration carrier) | `SubstratumInterfaceAudit` Q2 (OB, docstring); GR:260 (`substratumClass_structurallyClosed`); QP:173; QPR:21–22; `prepAvail_uniform`; Sub:361; K `obs_not_phasesAvailable`, `obs_not_layerFlowExecutable`, `obs_not_derivedOI`; Main:590 |
| Non-monomial mixing | Not generated by the stated dynamics with the stated access, nor by any stated lift formulation that lands in the operational interface (FI-1, §5.1). Each construction on `main` that has it adds it: the stipulated gate flows (`onesTheory`, the stipulation `LayerFlowExecutable`), a postulated mixing datum (`state-mixing-coupling-audit.md`), or a polarization map the corpus does not supply (`PolC`, which is not QM). | **Excluded under stated conditions** for the stated access (configuration carrier, level one); **not derived** by the lift formulations that land, which derive neither target, whether every realization of the lift's channels is configuration-level being undecided (GR:270); **open** for the four candidate sources of §5.1 | §5.1 Status; `exec-source-audit.md`; `coherent-continuum-source-audit.md` |
| Existing results | None of the files read closes the gap under the same hypotheses. The executability-source audit is negative for the stated access and underdetermined for the lift; the lift-source audit is negative for the formulations that land and underdetermined for the wave lift; the C5 discovery audit's verdict is C; the polarization closure is split (O1 positive and O2 negative for `PolC`); the coherent-continuum audit finds "no current source"; the state-mixing coupling audit closes the gap only from a postulated datum (K `mixTheory_qm`); QP, MECH-1, MECH-2 and M-INACC-1 treat encoded maps, which stay in `permTheory`. Main:566, Main:584 and Main:600 are QM → OI results at finite accuracy. | **Open** (search scope: the header's coverage list) | the audits named; QP:846–877; MECH-2 §0; §2 |
| SM wave-operator route | Neither established nor excluded. The map $\varphi\to L_{\rm obs}\to\Delta_g$ is "not proved anywhere in this framework"; no map from the site-space operator to the configuration carrier is stated, and the lift-source audit records what one would have to supply (an image in a class the stated access generates, non-monomial, and for the flow the gate flow at every time). The three formulations the lift-source audit tests (L1, L2, L4) derive neither target; whether every realization of the L1 and L2 channels is configuration-level is not decided (GR:270; `lift-source-audit.md` scope amendment). | **Open** ("unresolved rather than excluded"); **not derived** by the formulations that land | SM:232; GR:270; `lift-source-audit.md` (outcome; requirement on $\Theta$); `coherent-continuum-source-audit.md` route S7; K `coherentLiftClass_eq_substratumClass` |

**Two notions of "earliest", kept apart.**
- *The earliest unproved assumption.* The posits under S1, total finiteness, bijectivity (one
  prong empirical) and the counting measure (B1–B3; Main:726 (ii)–(iv)), are OI's stated
  foundation; the finite-law level is proved from them. Beyond that level the forward route
  rests on stated inputs that act in different places. FI-1's statement and negative use the
  stated read/write access on a finite configuration carrier with a bijection; the phase
  intervention, stated as an assumption on the substratum class (GR:260), enters FI-1's
  position as first, not its statement or its negative (§5.1 *Conditionality*). The site
  factorization (B4), with the second-order form (B10), is upstream of the physical
  identification of the carrier with lattice fields and of its layers, the graph cone, the
  cell-based access posits P1–P3, E-iso and H-PREP (QP:124–176), the spatial route with S13,
  and H-Bell's graph. It is not upstream of FI-1 itself.
- *The earliest missing mathematical mechanism.* The sources read establish no order among
  three missing mechanisms (§5.3): a source of the phase (O1); a source of state mixing, with
  FI-1 as its necessary condition and the layer flow (O2) as one form; and the H-Bell response
  mechanism. Only relative to the phase taken as stated is FI-1 the first, and then the
  mechanism is one supplying a non-monomial admissible operator at level one and beyond it the
  uncountable non-monomial family; no source supplies it from the stated dynamics and access.
  Under phase-free richness no separate phase mechanism is needed, because one continuously
  driven transition with the exchanges carries the phase within the primitive-source equivalence
  (GR:250–258; §5.1 (b)); the phase requirement then falls on the mixing mechanism, which must be
  that complex transition and not a real rotation. On the spatial route the missing mechanism is the lift
  $\varphi\to L_{\rm obs}\to\Delta_g$ (S13), which is also FI-1's candidate source 1.

**Scope of the necessity claim.** Non-monomial mixing is shown necessary for exact finite
endomorphic operational QM within the structural architecture, on the configuration carrier at
level one, and for nothing wider (§5.1, *Scope of necessity*).

**The proposed dependency chain.** The owner's proposed chain is "a proposed dependency
structure, not an established derivation". Arrow by arrow:

| Arrow | What the sources support | Direction and hypotheses |
|---|---|---|
| OI substratum and independently justified observation principles → observer-accessible coherent state mixing | Not supported. The observation principles available are stated, not independently justified (row 2 above), and with them the implication is excluded under stated conditions (row 3; K `obs_not_layerFlowExecutable`; `exec-source-audit.md`, "negative for the stated access") | Only necessary conditions are proved, in the converse direction: exact QM ⟹ executability ⟹ FI-1 (GR:270). Open for the four candidate sources of §5.1 |
| Coherent state mixing → candidate first missing dynamical mechanism | Supported as a requirement, not as an identification: executability requires a non-monomial admissible operator at level one and uncountably many non-monomial rays (K, §5.1). No source names the mechanism; FI-1 alone is not sufficient (`PolC`) | Necessity only, within the structural architecture on the configuration carrier |
| → complex structure, phases and probability law | Not supported as consequences of mixing in general. Phases: independent of the *layer flow* (K `obligations_independent`, two-state carrier; the ones-fixing theory executes every layer flow, has no quarter phase and is not QM), because the layer flow fixes the all-ones ray; not independent of mixing in the form of phase-free richness, one continuously driven transition with the exchanges, which with implementation locality and embedded observation gives exact QM and with it the phases (GR:250–258, Main:590; K `oiPlusMin_iff_qm`, `derivedOI_of_qm`), the complex drive carrying the phase where a real rotation would not (§5.1 (b)). Complex structure: complex matrix kinematics is taken as given in the formalism in which these statements are made (Main:218), and the SM carrier's complex structure is not derived (F4; SM:809). Probability law: the Born dictionary is definitional and its exponent not selected (Main:556) | The sources support instead two conditionals, with complex kinematics given: the layer flow and the phase together, within the closure, give exact finite endomorphic operational QM (Main:590, GR:268; K `qm_of_derivedOI_layerFlowExecutable`), the phase being an input beside the layer flow; and phase-free richness, with implementation locality and embedded observation, gives the same QM with no phase operation in its repertoire (GR:250–258; K `oiPlusMin_iff_qm`), the complex drive carrying the phase (§5.1 (b)). Which form a mixing source would take decides whether the phase is a separate input or a requirement on the mixing source itself |
| → compatible preparations, measurements and composition | Supported conditionally: within the closure with both obligations, the theory is exact finite endomorphic operational QM on the carrier, its instruments included. Main:590 states a typed form, which drops the endomorphic qualifier, for the primitive-source equivalence (K `typed_determined_of_oiPlusMin`); a typed form of the layer-flow closure statement is not stated. The tensor-product composite and local tomography are taken as given (Main:218); a physical preparation mechanism is open (B25, §6); NNB fails composites (QP:746–768) | Conditional on the closure, both obligations and complex kinematics with the composite given |

So the sources support a branching structure rather than a chain: the stated inputs (the
read/write access for FI-1's line; site factorization and the second-order form for the spatial
line and H-Bell's graph); the phase and state mixing, with FI-1 as the latter's necessary
condition, independent where the mixing takes the layer-flow form and jointly sufficient within
the closure, while under phase-free richness the phase branch is carried inside the mixing branch,
as the requirement that the mixing source be the complex driven transition, and is not removed;
H-Bell beside them; and the lift S13 as an open candidate source of FI-1 and the spatial route's
open link.

### 5.3 The three gaps in parallel

Owner direction of 2026-11-09 (#1169 c.6740778880): phase, FI-1 and H-Bell presented in
parallel, each with its carrier and scope, keeping three distinctions apart. The owner calls them
"independent unresolved obligations" and calls state mixing "a promising common research target",
the shared-gap convergence remaining provisional. The sources support the independence in the
scoped senses stated after the table; whether state mixing is shared with the phase depends on the
form a mixing source takes.

| Gap | Carrier | Scope | Proved toward it, and constraints | Open |
|---|---|---|---|---|
| **Phase (O1)** | The configuration carrier. `PhasesAvailable`: the quarter phase on every state is available at every level (OB/RouteB.lean:132). Its encoded counterpart, the encoded quarter phase $S$, is a separate object on an encoded carrier | An all-level availability requirement on a finite operational theory, not an exactness predicate; exact QM implies it (K `derivedOI_of_qm`). The encoded $S$ is at single-qubit stabilizer scope (QP) | **Not supplied** by the stated access (K `obs_not_phasesAvailable`, failure exhibited at level 2). For any architecture whose admissible isometries fix the all-ones ray, failure at level one, with no claim at each composite level (GR:260; K `onesFixing_not_phasesAvailable`, `substratumClass_not_onesFixing`). **Necessary condition:** an operator moving the all-ones ray, not shown sufficient (GR:260). **Available by stipulation**, as a member of the substratum class (K `phase_monomial`; Main:590), **not derived**. **Mathematically available** in `PolC` on the two-state carrier (K `polarizedTheoryC_phasesAvailable`), through a polarization map the corpus does not supply. **Conditional:** supplied by phase-free richness with implementation locality and embedded observation, through exact QM (GR:250–258; K `oiPlusMin_iff_qm`, `derivedOI_of_qm`); the driven transition carries the phase (§5.1 (b)) and is itself unsourced. **Encoded:** non-adaptive native $S$ excluded on class N (QP Lemma G2); NNB supplies $S$ at a C-CP cost (premise I, QP:805–840); MECH-2's Theorem U2 excludes encoded $S$ for every fixed bijection under the frame $R1^{\otimes n}$ and H-LIFT | A source, from the stated dynamics and access, of the configuration-level phase or of a mixing resource of the phase-free-richness form (the complex driven transition); moving the all-ones ray is necessary, not sufficient (GR:260; `phase-source-audit.md`:212–221): a real rotation moves it and, with the permutations, supplies no phase (§5.1 (b)). On the encoded side, adaptive native $S$ (QP:897–915) |
| **State mixing (FI-1; the layer flow O2)** | The configuration carrier at level one, $S\times\mathrm{Fin}\,1$, for any finite configuration set with a bijection. Encoded non-monomial maps are a different object and do not meet FI-1 | Exact finite endomorphic operational QM within the structural architecture, for a theory generated by an architecture. FI-1 is not necessary for finite-accuracy reproduction of quantum statistics (Main:566, Main:584, Main:600) | **Necessity**, one direction only (K `exists_nonMonomial_of_layerFlowExecutable`), with a stronger form (K `uncountableNonMonomialRays_of_layerFlowExecutable`). **Not sufficient** (`PolC`, two-state carrier). **Not supplied** by the stated read/write access; **not derived** by the lift formulations that land (§5.1 *Status*). **Mathematically available, not derived:** the gate flows and `driveQ` (§5.1 *Closest derived objects*). **Available by stipulation:** `onesTheory` and `LayerFlowExecutable`, and the postulated datum of `state-mixing-coupling-audit.md`. **Two forms:** the layer flow fixes the all-ones ray and, with the phase, gives QM within the closure (K `qm_of_derivedOI_layerFlowExecutable`), without it does not give phase-free richness (K `flow_endpoint_refuted_general`); a continuously driven transition on three or more states moves that ray at every $t\notin2\pi\mathbb Z$ and, with the exchanges, implementation locality and embedded observation, gives QM with no phase operation in its repertoire, the complex drive carrying the phase (GR:250–258; §5.1 (b)) | The four candidate sources of §5.1: the site-space wave lift (S13), the lift's channel realizations, C5 candidate 2's map, and extended access |
| **H-Bell** | Configuration (ontic) level on the SM/GR graph: preparation-indexed adjacency on the state-dependent graph $G(x)$, or an equivalent nonlocal response map, with diagonal outcome statistics (Sub:131; Main:414) | The preparation-indexed graphs must (i) supply the ontic parameter dependence that M1-B requires for the observed violation E2, (ii) preserve operational no-signalling, and (iii) satisfy a metric/Ollivier–Ricci stability condition on the prepared graph family (Sub:129–133). Condition (iii) is geometric, so H-Bell is not an outcome-statistics condition alone. The sources state no exactness qualifier | **Reference graph Bell-local**, CHSH $\le2$, under measurement independence and screened wings (Main:416). The **unrestricted response class reaches the PR box** (Main:362), so the quantum set is not selected natively. Finite response constructions **realize no-signalling target laws** (Main:429); Main:566 and Main:584 realize quantum statistics at finite accuracy, with no spatial graph. Which hypothesis is given up is a **choice** (Main:403–406). **Constraint on any H-Bell mechanism:** MECH-2's Proposition B (M-FIX), "a necessary condition derived from H-Bell": given determinism and measurement independence, (i)–(ii) with a violation imply that the available preparation laws do not span the response-relevant functions (MECH-2 DESIGN:543–567); that record promotes no claim | H-Bell (i)–(iii) for a specified preparation-indexed rule (Sub:133) |

**The independence, scoped.**
- *Phase and layer flow.* Kernel-proved independent on the two-state carrier: the substratum
  theory has the phases and no layer flow, the ones-fixing theory the reverse
  (K `obligations_independent`).
- *Phase and FI-1, as predicates.* Neither implies the other: the substratum theory has the phases
  and only monomial operators (`substratumClass`), and the ones-fixing theory has a non-monomial
  admissible operator at level one and no quarter phase [K composition:
  `onesTheory_layerFlowExecutable` with `exists_nonMonomial_of_layerFlowExecutable`, and
  `onesTheory_not_phasesAvailable` (OB/FlowEndpoint.lean:180); not stated as one theorem]. Their necessary conditions, a
  non-monomial operator and an operator moving the all-ones ray, are independent at the operator
  level (exact check K4), but one operator can meet both: a continuously driven transition on
  three or more states at $t\notin\tfrac{\pi}{2}\mathbb Z$ [A; exact check D].
- *Phase and state mixing, as obligations.* Not independent in every form. Beside a mixing source
  of the layer-flow form, which fixes the all-ones ray, the phase is a separate input. A mixing
  source of the phase-free-richness form needs no separate phase operation (GR:250; Main:590)
  because it carries the phase: the driven transition is the transposition's layer flow times a
  continuous relative phase on the configurations it fixes, and at a quarter turn with the
  exchange it is the quarter phase on a third state [A, from K `gateFlow_isolation` with
  `unit_mul_unit`; GR:270; exact checks I and Q; §5.1 (b)]. There the phase obligation is
  carried inside the mixing obligation, as the requirement that the source be that complex
  transition, and is not removed; a real rotation
  moves the all-ones ray and mixes states but, with the exchanges, generates only real orthogonal
  operators [A; exact check R]. So the owner's "common research target" can be shared with the
  phase only if the mixing source moves the all-ones ray (GR:260's necessary condition, not shown
  sufficient), and is shared with it when the source is the complex driven transition of
  phase-free richness.
- *H-Bell and the other two.* Not derived from FI-1 or the phase, and not deriving either, in the
  sources read; posed on a different object (a preparation-indexed rule on the SM/GR graph). No
  independence theorem is stated.

**H-Bell's target, exact or finite-accuracy.** The sources state no exactness qualifier for
H-Bell; its target is the observed violation E2 through M1-B (Sub:129, Sub:131), which is
empirical and of finite precision, so the finite-accuracy reading is the one faithful to the
sources (the r3 review's reading, adopted here). *Reviewer-supplied bound, not adopted here as an established claim*; both its parts are exact
algebra [A] (REVIEW-UNIT1-r3.md §4, REVIEW-UNIT1-r4.md §4; re-checked by exact checks B and H):
under the counting measure (B3) every probability a finite realization produces is a ratio of
counts, hence rational, so the Tsirelson-point law, with $P(a{=}b)=(2+\sqrt2)/4$ irrational, has
no exact finite realization of that kind, while rational quantum laws violating CHSH exist (a
maximally entangled state gives CHSH $=6\cos\alpha-4\cos^3\alpha$, which is $344/125$ at
$\cos\alpha=4/5$, all sixteen probabilities
rational and no-signalling). An exact reading of H-Bell would therefore exclude part of the
quantum Bell set, not every violation.

**Three distinctions, kept apart.**
- **Configuration versus encoded carrier.** FI-1 and the phase (O1) are statements about the
  configuration carrier. Encoded $S$ and $H$, and encoded tetrahedral rotations, are maps on
  encoded carriers. They can be non-monomial, or phase-like, while every configuration-level
  operation stays in `permTheory` (QP:846–877; MECH-2 §0). An encoded result neither meets nor
  refutes FI-1.
- **Mathematically available versus derived from OI.** The gate flows, `driveQ`, `PolC`'s phases
  and Hadamard, the stipulated `onesTheory` and the postulated mixing datum exist as mathematical
  objects or stipulated classes. None is derived from the stated dynamics and access (§5.1;
  `coherent-continuum-source-audit.md`, routes S5 and S8).
- **Generating coherent mixing versus the full probability and composition rules.** FI-1 is
  necessary, not sufficient (`PolC` has non-monomial operators, the phases and the closure, and
  is not QM). Exact QM follows from the layer flow together with the phase, within the closure
  (K `qm_of_derivedOI_layerFlowExecutable`), and not from the layer flow with the sourced closure
  and without the phase, on the two-state carrier (K `onesTheory_not_qm`); it follows also from
  phase-free richness with implementation locality and embedded observation
  (K `oiPlusMin_iff_qm`), whose driven transition carries the phase (§5.1 (b)). In both, complex matrix kinematics
  and the tensor-product composite are taken as given (Main:218), the Born exponent is not
  selected by the finite-law construction (Main:556), the physical preparation mechanism is
  open (B25), and H-Bell is not addressed.

***

## 6. Quantum-ingredient ledger

For each ingredient: the actual OI mechanism and source if one exists, its scope, and
otherwise the first missing physical operation or source. No QM operator is treated as
arising from the substratum unless a cited derivation produces it.

| Ingredient | OI mechanism (source) | Scope / status | First missing physical operation or source |
|---|---|---|---|
| **Coherent state composition** (tensor-product composites of coherent states, local tomography) | Site factorization gives $\mathbb C^{\prod S_i}=\bigotimes_i\mathbb C^{S_i}$ for the *classical embedding* (Main:268, B4) | Classical product of configuration spaces only. Quantum composite kinematics "taken as given … deriving that kinematics is open" (Main:218). QP's NNB construction "is a single-system mechanism" and fails two-qubit stabilizer correlations (QP:746–768) | A physical preparation of coherent (off-diagonal) states on a composite, plus a source for the tensor-product composite rule within the operational interface (B22). |
| **Complex phases** | Phase intervention adjoined as "a stated intervention principle" (Main:590). The substratum's permutation unitaries are real 0/1 matrices (Main:270); the one-step coherent channel acts "with no phase" (Main:306). Non-adaptive native $S$ excluded on the bipartite center-free linear class (QP Lemma G2, QP:342). On the physical carrier, every isometry the dynamics and stated access supply fixes the all-ones ray, so the quarter phase fails at level one, with no claim at each composite level (GR:260; K `onesFixing_not_phasesAvailable`, `substratumClass_not_onesFixing`) | Supplied, not generated. Adaptive native $S$ open (QP:897–915). The six-link carrier's complex structure (needed for $\mathrm{SU}(3)$) enters through H-link's $\otimes\mathbb C^m$ and SM:505, and its real-to-complex step is named open at SM:809; a candidate $J$ exists on the real lift off its null modes (F4) | On the configuration carrier, a source of the phase (O1) from the stated dynamics and access, or of the complex driven transition of phase-free richness, which carries it; moving the all-ones ray is necessary, not sufficient (§5.3). On an encoded carrier, a native operation implementing a phase not in $\{0,\pi\}$ (first: the encoded quarter phase $S$). For the six-link carrier, the identification of $\Sigma$ with a $J$-Hermitian covariance and the null-mode sector (NQ1). |
| **Noncommuting instruments** | Native minimal reads with reciprocal kick (apparatus-1, cited at QP:154–157): two mutually disturbing binary reads (QP:323–338) | At most two mutually disturbing native reads, adaptive processes included (QP:332). A third (Y-type) needs NNB (QP:60–64). Requires access posits P1–P3 (B25) | A third read complementary to both, i.e. an armable non-graded coupling (NNB) or another non-bipartite source; and, for the full instrument algebra, full reversible control (iv), which the stated interventions do not supply (B22). |
| **Born statistics** | Probabilities are counting-measure marginals of the bijection (Main:117, Main:86–92) under the max-entropy measure (B3). Their Born *form* is a representation identity (Main:288) | Diagonal/transition layer only. Quadratic exponent "not SELECT[ed]": permutation entries are 0/1 (Main:556). Coherent-instrument probabilities need the operational completion (B22) | An independently justified selection of the quadratic functional on non-monomial (state-mixing) operations, which presupposes a source of non-monomial admissible operators (FI-1, §5.1). Probability-source questions Q1–Q3 of `oi-qm-ext-1/probability-source-assessment.md` (lines 28–32) are the open record. |
| **Bell-compatible correlations** | Graph cone + screened local completion ⟹ CHSH $\le2$ (Main:366–391). Quantum value reachable only via adopted ontic parameter dependence; proposed implementation: preparation-indexed adjacency (Main:414; Sub:131) | Reference graph: Bell-local (proved). Violation: conditional on H-Bell (open). Unrestricted response-table class reaches PR box (Main:362) — no Tsirelson selection natively | A specified preparation-indexed adjacency rule (or response map) that supplies the ontic parameter dependence M1-B requires for the observed violation E2, with operational no-signalling and curvature stability (H-Bell (i)–(iii), Sub:129–133; §5.3). |
| **Operational no-signalling** | Graph cone: an intervention reading/writing region $A$ cannot alter components outside $B(A,k)$ after $k$ steps (Main:364) | Holds pointwise on the reference graph, where it coexists only with CHSH $\le2$. With ontic parameter dependence it "is an additional requirement … not a consequence" (Main:414, Main:429) | A mechanism that enforces no-signalling on averaged outcomes while ontic parameter dependence is present (part of H-Bell). |
| **Interference** | "Write-then-read": hidden-sector records retrieved later change visible statistics (Sub:44); revival of distinguishability, e.g. the six-hidden-state model's $T(2,0)=I$ (Main:186–202) | Classical non-Markovian revival (P-indivisibility). Not phase-tunable amplitude interference: no phase parameter is available natively (row "Complex phases"); coherent inputs are not prepared (S6) | A continuously tunable state-mixing operation with a native phase: the layer flow (beam-splitter) together with a separate phase, or a complex driven transition, which carries the phase (§5.1 (b)). Main:590 and GR:270: the stated substratum dynamics with read/write access, and every stated lift formulation that lands in the operational interface, supply neither the non-monomial operation nor the layer flow (read/write: `obs_availExt_le_substratum` with `substratumClass` monomial; lift: `coherentLiftClass_eq_substratumClass`); the site-space wave-operator formulation is unresolved rather than excluded (FI-1, §5.1). The exact continuous path of $*$-automorphisms (`driveQ_isContinuousPath`, Main:274) is derived but is not an available operation. |
| **Particle statistics** (fermionic/bosonic) | Fermionic: Susskind operator identity $D_{\rm st}^2=-\tfrac14\Box_{\rm lat}$ (SM:286); NN4 "does not apply" because no Grassmann fields exist at the bijection level (SM:565). Bosonic: the lattice scalar field (classical, $\mathbb Z_q$-valued) | Operator identity only. "The bosonic and fermionic descriptions are related by an exact change of variables" (SM:288) is not supported by the identity (F7). Spin–statistics mapping imported under H-spin' (SM:454). Fock/occupation statistics of quanta not derived; the quantized-oscillator vacuum is imported in SM:122–142 | The measure and observable map from substratum scalar variables to the determinant-pseudofermion (Grassmann) representation, and the stationary Gaussian law (SM:290–292). |
| **Repeatable preparation / readout** | Readout: passive record fibres identify hidden quantities exactly when constant on the fibre (Sub:348–357); Lüders update "transcribes Bayesian updating … for the represented diagonal sector" (Main:654). Preparation: only a maximally mixed ancilla is assumed (OB/OperationalAssembly.lean, `prepAvail_uniform`) | Repeatable classical readout of diagonal records: sourced (C2-structural by reversibility). Known-value preparation: supplied access posit P2 via the open identification H-PREP (QPR:21–22). Sub:361: "It supplies no physical record-storage or intervention mechanism" | A physical preparation mechanism (what loads a known value or a distribution into hidden/ready cells), the first open question of the probability-source assessment (line 28). |

**Tally (ingredients, at the level the SM chain needs them).**
- *Sourced (natively, within stated scope):* classical repeatable readout of diagonal records;
  graph-cone kinematic no-signalling on the reference graph; classical revival
  ("write-then-read").
- *Conditional (on named bridges or supplied posits):* two complementary binary reads (P1–P3);
  quantum Bell correlations (H-Bell); phases and full reversible control (stated intervention
  principle; condition (iv)); a third complementary read and encoded $S$ (NNB).
- *Missing (first missing operation named above):* coherent composite kinematics; native
  complex phases; Born exponent selection; continuous state mixing (not supplied by the
  stated substratum and lift classes, open for the site-space wave-operator lift; hence
  amplitude interference); fermionic measure; physical preparation.

***

## 7. Three-way distinction

| (i) Exact geometric / algebraic decomposition | (ii) Conditional SM interpretation | (iii) Physically implemented QFT / operational quantum prediction |
|---|---|---|
| $S\iff D\iff Q_{\rm fb}$ (Main:548) | $T_1\to$ colour, $E\to$ weak isospin, $A_1\to$ hypercharge (SM:380; H-link, H-cust) | None established. The operational completion is a characterization with complex kinematics given and (iv) not supplied (Main:82, Main:564) |
| Readback ⟺ memory; recurrence indivisibility (Main:99, Main:137) | Stabilizer $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$ (Theorem 5; H-link, H-cust, complex carrier) | No fermionic measure from the substratum (SM:290–292) |
| Graph cone; Bell ceiling CHSH $\le2$ (Main:364–391) | Local gauge invariance (A6; link dynamics not derived, SM:118) | §6 induced couplings use the fermion determinant and SM RG running on an ambient QFT; three thresholds fitted (SM:681; Sub:518–523): ambient/background calculation, not a native OI prediction |
| Form lemma (SM:224); Theorem 1a / Corollary 1a (SM:242–268) | Three generations of spin-1/2 matter (H-spin', H-link $m=1$) | Quantitative §7 predictions are compared through continuum perturbation theory (Sub:225–227) |
| Six-link $3\oplus2\oplus1$ (Theorem 7); taste $1\oplus3$ (Theorem 8) | Chiral SU(2) (H-χ') | Bell violation on the SM/GR graph: conditional on H-Bell |
| Staggered $\varepsilon$-grading $=\gamma_5\otimes\xi_5$ (Theorem 12); $\Gamma_VK_{\rm eff}(E)\Gamma_V=-K_{\rm eff}(-E)$ (SM:569) | Higgs in the singlet taste's $E$ projection (input doublet, Theorem 11) | Continuous-time Hamiltonian law: "additional structure" (Main:274, Main:590) |
| Theorem 3 (K); Theorem 19 (K); Proposition 20 | Hypercharges given the family pattern (Theorem 15) | — |
| Prop. 14a, Prop. 15a (group theory) | $d=3$ (E5–E7); simple-cubic Bravais type (selected by observed gauge group) | — |
| QP Lemmas G1, G2, Q (QP:240, QP:342, QP:460) | $\theta\in\{0,\pi\}$ for a T-invariant emergent Lagrangian (Theorem 18) | — |

The (i) column is independent of QM where the source says so (SM:268, SM:1422). Nothing in
column (i) is a quantum ingredient of §6: the decompositions are representation theory of
real cubic actions, classical stochastic-process theory, or a universal representation.

***

## 8. Findings (circularity, overstatement, consistency)

Each finding names its source and the evidence. None is acted on (no manuscript authority).

- **F1. Forward-direction overstatement (Sub:68).** See §3.3. Core finding of the unit.
- **F2. Bell branch selected by the observed violation.** Measurement independence is a
  posit (Main:407). "A completion reproducing quantum Bell correlations gives up" ontic
  parameter independence or measurement independence, and "the framework gives up the first"
  (Main:403–406); the measurement-dependent alternative is bounded by
  $I_{\rm ont}\ge0.0309$ bits (Main:22). Its SM/GR implementation H-Bell is open (Sub:133).
  Column (ii) for ontic parameter dependence: none identified; type E (the observed
  violation, E2) plus St (which hypothesis is given up). This is a selection, not a
  derivation; the unrestricted class reaches the PR box (Main:362), so the framework does not
  natively select the quantum Bell set.
- **F3. Bijectivity anchored partly by quantum statistics.** Lemma 3's hidden-margin prong
  uses "the observed statistics … doubly stochastic class" and "unitary emergent statistics are
  unistochastic" (Main:62; ledger Main:726 (iii)). The empirical input is quantum. Main's
  alternative, reversibility as "the orthodox assumption of mainstream physics" (Main:66), is
  itself motivated by quantum unitarity ("Unitary evolution in quantum mechanics *is*
  information conservation"), so it relocates the quantum anchor rather than removing it.
  Main:62 and Sub:94 state the empirical anchor openly.
- **F4. The $\mathrm{SU}(3)$ factor requires a complex structure on the six-link carrier that
  Theorem 5 does not list among its premises.** The substratum's field values are
  real/$\mathbb Z_q$ (SM:565: "a real scalar bijection"); the observer-level branch is a "real
  lift" (SM:240, SM:292). For a real carrier $\mathbb R^6$ with the cubic action, a generic
  $O$-equivariant symmetric $\Sigma=aP_{T_1}+bP_E+cP_{A_1}$ has stabilizer
  $O(3)\times O(2)\times O(1)$ in $O(6)$ (Lie algebra dimension 4); only on a complex carrier
  $\mathbb C^6$ with Hermitian $\Sigma$ is the stabilizer $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$
  (dimension 14). The statement is Schur's lemma for real-type irreducibles, all three of
  $T_1,E,A_1$ being of real type [A]; exact check `probes/r2_generic_checks.py` C1 (real
  commutant dimension 3; multiplicities $(1,2,3)$; 4 and 14). In the corpus the complex
  structure enters through H-link's $V_{\rm link}\otimes\mathbb C^m$ (SM:362) and is named
  twice: SM:505 ("equipped after-the-fact with the complex inner-product structure
  $V_K=\mathbb C^6$") and SM:809, where "the real-to-complex step" is one of the open joints
  of the explicit map $\boldsymbol\phi\mapsto M\in\mathrm{SU}(N)$. It is not listed among
  Theorem 5's premises (SM:340–342), and Sub:163, Structure:152, Structure:1153, FULL:736,
  FULL:939 and FULL:1226 present the unitary group of the block algebra without stating that
  it presupposes the complex structure.
  *Candidate on the real lift.* For one non-null Fourier mode of the real lift,
  $f=\begin{pmatrix}0&1\\-1&a\end{pmatrix}$ with $a=2\cos\omega$, $0<\omega<\pi$, the
  positive-frequency complex structure $J=(f-\cos\omega)/\sin\omega$ satisfies $J^2=-1$,
  commutes with $f$ and is symplectic [A: $f^2=af-1$ gives $J^2=-1$]; on six degenerate
  components, $J\otimes I_6$ commutes with the cubic action, and the commutant of $f\otimes I_6$
  in $\mathfrak{sp}(12,\mathbb R)$ is $\mathfrak u(6)$ (exact check C2(a)–(b): dimension 36,
  every element commuting with $J\otimes I_6$). So the real lift's dynamics carries a
  $\mathrm U(6)$ on its non-null sector, and SM:130's "custodial $\mathrm U(6)$ of the real
  lift" is defensible there; this $J$ is defined mode by mode and is nonlocal in space. At the
  null modes of $\alpha=1/d$ (SM:292) the mode map is $\pm$ a unipotent ($a=2$, $(f-I)^2=0$,
  constant mode; $a=-2$, $(f+I)^2=0$, staggered mode); its commutant is $\{tI+r(f\mp I)\}$,
  which contains no square root of $-1$, and the commutant of
  the cubic action on the six components is block-scalar and real, so no complex structure
  commuting with both exists [A; exact check C2(c) at $a=2$, with countercontrol]. For a stationary
  product covariance $K\otimes\Sigma$ on one non-null mode, the stabilizer has dimension 14
  inside that $\mathfrak u(6)$ against 4 inside configuration-space $\mathfrak o(6)$
  (computation-supported: exact check C2(d), agreeing with the reviewer's probe R1).
  `oi-qm-ext-1/two-mode-drive.md` §3 builds the zero-coupling analogue, "Multiplication by i
  is exactly the zero-coupling quarter-turn J", and shows $T_kJ-JT_k\neq0$ for a coupled step.
  *Status.* The complex structure is **not derived** in SM; a candidate exists off the null
  modes. Open: the null-mode sector at $\alpha=1/d$; whether SM's
  $\Sigma=\langle\phi\phi^\dagger\rangle$ is the $J$-Hermitian covariance of the real lift
  (shown above only for a stationary product covariance on one mode); and the lift itself
  (B12). This is NQ1.
- **F5. Level inconsistency for the gauge sector.** SM:428 states the SM gauge group "lives at
  the substratum … a literal algebraic structure on the lattice, existing before any trace-out
  is performed", and SM:515 that gauge bosons "live at the bijection level". The theorem that
  produces the group is stated on the observer-level branch: "its components are observer-level
  field values, not the $\mathbb Z/q\mathbb Z$ alphabet of the substratum" (SM:312); the matrix
  equation "is not identified with the fundamental finite bijection without the coarse-graining
  bridge" (SM:316); Theorem 5 is "exact conditional on H-link + H-cust" (SM:344) and uses
  $\Sigma=\langle\phi\phi^\dagger\rangle$, an expectation on a complex carrier. The level
  statements at SM:428 and SM:515, and SM:511's placement of the commutant
  $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$ "at the bijection level", are stronger than
  Theorem 5 supports. The competing anchor is Sub:393–395, which places the SM gauge group at
  Level 2, the emergent QFT, "obtained from the stabilizer of the equivariant condensate", with
  only $\mathcal G_{\rm sub}$ at the substratum level.
- **F6. SM's forward chain imports QM at the dimension filter and the gravitational lemmas.**
  The atomic-stability filter E6 as stated includes a quantum statement, the Coulomb
  bound-state statement, beside the classical Ehrenfest and orbit-instability arguments
  (SM:176); the real-case area law and the
  lattice Bisognano–Wichmann lemma are statements about quantized oscillator states with $\hbar$
  (SM:122–142). These inputs are not derived from $(S,\varphi,V)$ in the files read. They do not
  affect the gauge-group algebra but they are part of what Sub:68 cites as the forward direction
  ("SM §3.1").
- **F7. SM:288 asserts more than Theorem 2.** "The bosonic and fermionic descriptions are
  related by an exact change of variables on the lattice." Theorem 2 is an operator identity;
  the Remark immediately after states that the measure and observable maps are open and that
  "a scalar Gaussian with covariance proportional to $\Box_{\rm lat}^{-1}$ is therefore not
  converted into this determinant-pseudofermion measure by a constant field normalization"
  (SM:290–292). A change of variables relating the two descriptions is therefore not
  established. The same "exact change of variables" wording appears in book
  `ch05-gauge-structure.md`:91 and its mirror FULL:1409.
- **F8. Spin–statistics is imported.** SM:454 maps spin-0 to bosons and spin-1/2 to fermions
  "from the lattice"; the mapping is the relativistic spin–statistics association, not derived
  from the substratum, and is conditional on H-spin' (which is open, and whose free-kernel form
  is refuted, SM:452). Representation labels give spin under H-spin', not statistics, and the
  fermionic measure is open (SM:290–292). Two book statements assert more: `ch06-matter-content.md`:28
  (mirror FULL:1541), that "at the level of the algebraic labels" the spin–statistics
  correspondence "follows from the lattice representation theory — with the physical spin
  identification riding H-spin' (SM §4.7) — not from a separate spin-statistics postulate". The
  book states the H-spin' qualifier; the finding stands because H-spin' gives spin, not
  statistics, and the fermionic measure that statistics would need is open; and
  `ch10-chemistry.md`:36, which obtains the Pauli principle from "the spin-statistics theorem — a
  consequence of the emergent QFT's Lorentz invariance", while emergent Lorentz invariance at
  loop level is open (SM:130 (iii)) and the fermionic measure is open. Each is a finding in its
  own right.
- **F9. A cited kernel theorem is vacuous; already tracked as #1188.** Main:590 cites `readWriteSourced_not_qm`
  (OB/ReadWriteControl.lean:174) for "finite reversible read-write dynamics … does not itself
  generate quantum state mixing". Its hypothesis `ReadWriteSourced T`
  (OB/ReadWriteControl.lean:158–160) requires every available single-outcome conjugation
  `conjChannel V` at ancilla level $n$ to have $V$ equal to a permutation matrix. Reading the
  definitions: `readout_avail` and `readout_is_localLuders` make the level-1 readout available
  and equal to `localLuders 0` (OB/OperationalAssembly.lean), which on a one-state ancilla is the
  identity map; `availExt_coarse` gives it as a `Unit`-outcome family; and
  `conjChannel (i • 1) = conjChannel 1 = id` (OB/MonoidalCompletion.lean:360). The hypothesis
  then demands $i\cdot\mathbb 1=$ `permMatrix σ` on a nonempty carrier, which is false, so
  `ReadWriteSourced T` holds for no theory on a nonempty carrier and the theorem has no
  instances. QP:865 records the same vacuity. (`MonoidalCompletion.lean:360` is the
  definition of `conjChannel`; the identity $\mathrm{conjChannel}(i\cdot1)=\mathrm{id}$ follows
  from it.) This is a paper reading of the definitions, not a kernel check (Lean work is
  outside this unit). The defect is tracked as #1188 (KERNEL-VAC-1, open), whose owner
  decision of 2026-11-07 reads "Do not use it as scientific evidence"; M-INACC-1 DESIGN:585
  likewise does not cite it. #1188 lists the other citation sites: GR:260,
  `verification/README.md`:298, `verification/audits/operational/completion-assumption-audit.md`:95,
  `verification/programmes/substratum/route-b-audit.md`:29, `source-audit.md`:100 and :121, and
  the `RouteB.lean` docstring (:13). The other kernel citations at Main:590
  (`substratum_plus_control_qm`, `substratumTheory_not_layerFlowExecutable`,
  `obs_not_layerFlowExecutable`, `coherentLiftClass_eq_substratumClass`,
  `derivedOI_qm_iff_layerFlowExecutable'`) exist at the cited files and were not audited here;
  the negative conclusion of Main:590 needs to rest on them, not on `readWriteSourced_not_qm`.
- **F10. Interference language.** Sub:44 ("Interference in the mechanism picture is
  write-then-read") and Sub:463 (double-slit traversal) describe classical non-Markovian revival
  as interference. Amplitude interference with a tunable phase needs a phase and a state-mixing
  operation (§6), neither generated. Sub:44's own paragraph names the unresolved step ("its
  simultaneous extension to the full coherent local instrument/composite algebra"); the
  finding concerns the word "interference" in Sub:44 and the traversal statement at Sub:463,
  which assert more than the cited results establish.
- **F11. Minor.** SM:112 "undirected degree bounded in [3, 2]": the undirected neighbours of
  $i$ are $\{i-1,i+1\}$, plus $i+2$ when $x_{i+1}=0$, plus $i-2$ when $x_{i-1}=0$, so the
  degree takes the values 2, 3 and 4; already recorded at M-INACC-1 DESIGN:274–278. SM:106
  "The P-indivisibility proof applies without modification" to state-dependent graphs: the
  recurrence argument does apply to any bijection of a finite phase space; the statement holds.

***

## 9. Question 5: can any restriction be motivated without QM/SM agreement?

| Restriction / bridge | Independent motivation found | Type |
|---|---|---|
| Site factorization | none identified (open); SM:68 counterexample to the minimization route | St |
| Nearest-neighbour range | none identified beyond minimality ("adopted", SM:226) | St |
| Simple-cubic Bravais type | none: selected by the observed gauge group (SM:1424) | E |
| Center independence A4 | observational anchor: homogeneity of physical law; warrant from the observer architecture open (Sub:98); Lemma Q gives it independent consequences at $q=2$ (QP:460) | E |
| Observer-level CI | none identified (open) | — |
| Affine rule | amplitude-scale gauge (operational principle, Sub:270–272); derivation from observer architecture circular (Sub:272) | Op |
| Linearity beyond affine | none ("imposed", Sub:100; A5-LINEAR-AFFINE R5) | St |
| Isotropy | empirical E4; quadratic isotropy then D at observer level | E |
| A6 | none needed in the formalized form (imposes no restriction, Main:726 (xii)) | St |
| Observer normalization / coarse-graining | none identified (open) (SM:232) | — |
| H-link (incl. $m=1$, incl. $\otimes\mathbb C$) | none identified (open) (SM:364) | — |
| H-cust | kinetic clause D at symmetric point (Prop. 4b); condensate clause none identified (open) | D (partial) |
| H-blind | D for the component-complete site observer (SM:336) | D (restricted) |
| H-spin' | none identified (open); free-kernel version refuted | — |
| H-χ' | none identified (open); anomaly cancellation is consistency only (SM:555) | C |
| H-Bell / ontic parameter dependence | none: one of two hypotheses must go to reach the observed Bell violation, and the framework gives up this one (Main:403–406; alternative Main:22) | E + St |
| Born exponent | none identified (open) (Main:556) | — |
| Complex kinematics / tensor composite | none identified (open) (Main:218) | — |
| Full reversible control (iv), phase intervention, layer flow | none; (iv) not supplied by stated interventions (K); phases stated (Main:590) | St |
| Fermionic measure | none identified (open) (SM:290–292) | — |
| NNB | candidate only: odd cycles in the state-dependent graph (QP:822–827); SM:112's rule and a symmetrized variant examined in MECH-1, MECH-2, M-INACC-1 (§10); not established | — |
| Premise I | none: "defined by the target and is easy to vary" (QP:836) | QS |

Search scope for "none identified": Sub; SM §§1–5, SM §6.1 at SM:677–690 and the §8.3 tier
text; Main §§1–2, §3.1–§3.3, and the §3.4 and §4.5 lines cited; QP and QPR to the extent listed;
and the r2 and r3 additions; all as listed in the header. A negative here is a statement about these files at
`fd539e15`, not about the whole corpus.

***

## 10. Question 6: native obstructions and what they locate

**What QP establishes (paper proofs, reviewed per QP:21–24).** On the native class N — the
second-order, linear, center-free update on the nearest-neighbour cubic graph, with the hidden
sector running the same rule and the access posits P1–P3, E-iso, H-PREP supplied (QP:124–176):

1. Lemma G1 (QP:240–259): every armed coupling preserves a split of slot variables into two
   sublattice-time sectors; the proof uses bipartiteness and $k_{ii}=0$ (center independence),
   and "that is the only place the induction uses $k_{ii}=0$".
2. Node 2 (QP:323–338): at most two mutually disturbing native reads, adaptive processes
   included.
3. Lemma G2 (QP:342 ff.): for non-adaptive processes, no encoding of a qubit admits an encoded
   quarter phase $S$ with native X reads and the comparator's statistics, for any number of
   cells and any hidden sector (QP:36–41). Adaptive processes: open (QP:897–915).
4. Lemma Q (QP:460): at $q=2$ the native step conserves $Q=\sum_ix_i(t)x_i(t-1)$; under P1/P2
   no functional with $Q^*=1$ is ever determined.
5. Minimal departure NNB (same-sublattice symmetric coupling) gives encoded $S$ and H at
   single-qubit stabilizer scope; it introduces a second encoded reflection that breaks C-CP
   unless premise I holds, and it fails composites (QP:79–98, QP:805–840, QP:746–768).
6. On a protocol's finite cone, available operations lie in `permTheory`'s, which excludes
   composite unitary control and exact finite QM (QP:846–877; the subtheory transfer is a paper
   argument).

**Connection to the SM chain (scoped).** QP:298–305 already states the cross-level relation:
SM's exact chiral (sublattice) symmetry of the observer-level staggered operator "is the same
bipartite structure at another level. That correspondence is an analogy across levels, which
SM itself says needs a bridge." SM:306 names that bridge: identifying Theorem 3's onsite terms
"with center dependence of the second-order substratum update requires a separate bridge".
What this unit adds is where SM uses the bipartiteness of the scalar dynamics directly:
Theorem 12's identification rests on it ("the wave equation is nearest-neighbor, so the cubic
lattice is bipartite", SM:539), and SM:569's trace-out identity
$\Gamma_VK_{\rm eff}(E)\Gamma_V=-K_{\rm eff}(-E)$ "for any site partition" has the premise
$\Gamma A\Gamma=-A$ for the nearest-neighbour operator $A$; the Nielsen–Ninomiya discussion
rests on that grading (SM:565–569). The premise SM shares with QP here is the bipartite,
center-free read pattern, not linearity: SM:569's $\Gamma A\Gamma=-A$ excludes both
same-sublattice and diagonal entries of $A$, and G1's induction (QP:254–257) uses only which
sites the update reads. With "a function of" in place of "a linear combination of", that
induction holds for any center-free second-order rule whose update at $i$ reads only
opposite-colour sites, whatever its nonlinearity [A; exact check K1 on a generic bipartite
graph, with self-term and same-colour-read countercontrols; exact check L(ii) adds a *linear*
rule with one same-colour read, which breaks the split, so the read pattern and not
nonlinearity is what breaks it]. Linearity enters G1's Lagrangian
consequences and, as affinity of the sector map, G2's step 3 (QP:362–369).
NNB is a coupling that P3 may arm between two cells of the
same sublattice (QP:805–806), local to a protocol. Where armed it adds to the scalar coupling a
term $h$ with $\Gamma h\Gamma=+h$, so the premise $\Gamma A\Gamma=-A$ of SM:569's one-line
identity fails for the armed graph, and SM:539's ground for Theorem 12 does not hold there.
Whether the identity or the identification themselves fail on the armed region is not derived
here. The transfer to the staggered operator — whether NNB breaks $\{D,\varepsilon\}=0$, on
which Theorems 3, 12, 13 rest — is the bridge of SM:306 and QP:298–305, and it is not
automatic: on a ring, $D'=\tfrac12(T-T^{-1})+\tfrac{\mu}{2}(T^3-T^{-3})$ satisfies
$\{D',\varepsilon\}=0$ for every $\mu$, while its square $-4D'^2$ has a same-sublattice
coupling $-2\mu$ on each scalar sublattice [A: the $T^{\pm4}$ terms of $D'^2$; exact check
`probes/r2_generic_checks.py` C3; the reviewer's probe R2 is the same countercontrol]. A
same-sublattice term added directly to $D$ does break it ($\{D+h,\varepsilon\}=2h\varepsilon$;
C3 control), but NNB is not defined as such a term.

Consequences, each scoped to N and the non-adaptive class:
- On the SM chain's own structural branch, the complex phase $i$ (as the encoded $S$) is not
  generated by non-adaptive native processes. This is a precisely scoped missing source, not an
  impossibility for adaptive or extended mechanisms.
- The one minimal repair identified (NNB) removes, where armed, the scalar-dynamics
  bipartiteness that SM:539 and SM:569 use. A mechanism that supplies phases through
  same-sublattice couplings must either confine them to a state or preparation class on which
  those statements are not used, or re-derive them without exact scalar bipartiteness; any
  consequence for Theorems 3, 12, 13 runs through the SM:306 bridge. This is an
  assumption-watch marker for #1169 and for any later H-χ' or H-Bell work: QP's own marker
  ("Any proposal that relies on a non-bipartite native graph … must re-examine Lemma G1 and
  C-CP", QP:954–956) applies to SM:539 and SM:569 as well.
- The state-dependent graph is the common candidate for both repairs: QP names its odd cycles
  as the first decisive check for NNB (QP:822–827), and Sub:131 names preparation-indexed edges as
  the H-Bell route. SM's explicit state-dependent example reads a same-sublattice site:
  $R(i,x)=i+2$ when $x_{i+1}=0$ (SM:112). Records on `main` examine it:
  - MECH-1 DESIGN:877–893 (odd $q$): the rule is non-affine, so its joint encoded action is
    not CP; with the switching cells fixed on a ring of $L\ge5$ sites the adjacency is not
    symmetric, so the branch map is not symplectic and not CP; its controlling cells are
    ordinary dynamical cells, which that record's Proposition T′(i) does not permit.
  - MECH-2 §0 ($q=2$): the rule's edges are not reciprocal for $L\ge5$; under the frame
    $R1^{\otimes n}$ and H-LIFT, every encoded unitary channel a fixed bijection induces lies in
    $A_4\wr S_n$, so there is no encoded $S$, $T$ or CNOT (Theorem U2); Lemma Q's conservation
    fails for the rule. MECH-2:530–534 attributes the failure of apparatus-1's type grading for
    this rule to its nonlinearity. By the induction above, nonlinearity alone keeps the sector
    split; in the rule's form $f_i(u)=u_{i-1}\oplus(u_{i+1}\vee u_{i+2})$ (MECH-2 §0 item 1),
    on an even ring, the induction fails only at the same-colour read $u_{i+2}$. The
    attribution therefore names a feature that does not by itself break the grading; the
    record's conclusion that apparatus-1's exclusion of a native $Y$ read does not carry over
    is unaffected.
  - M-INACC-1 DESIGN §2.4 and RESULT §0 ($q=2$): for the symmetrized switched graph $G_\sigma$,
    $Q$ is conserved but Lemma Q(iii)'s protection fails; its mechanism-off limit $N_0$, with all
    $\{i,i+2\}$ edges, is QP's NNB-type linear class.

  MECH-1 and MECH-2 are paper-only research records that "promote no claim"; M-INACC-1 is
  WIP / UNVERIFIED with a model review. They are cited as the record, not as established
  premises. What they leave open is NQ2.

**Classification (§A.31), against `main` at `fd539e15`.** Labels are relative to a `git grep`
of `papers/`, `book/` and `verification/` for each finding's terms; none of the findings below
is NEW.
- Q6 connection: ELABORATING. QP:298–305 and SM:306 state the cross-level relation and its
  bridge; added: SM:539 and SM:569 rest on the scalar-dynamics bipartiteness that armed NNB
  removes, with the C3 countercontrol on the transfer to $D$.
- Q6 shared premise and MECH-2:530–534: ELABORATING. QP:254–257 and QP:954–956 place G1's
  ground in the bipartite, center-free graph; added: the split's survival for nonlinear rules
  with that read pattern, and the correction of MECH-2's attribution to nonlinearity.
- F4: ELABORATING. The substratum carries "no complex structure" (Substratum §4, as quoted in
  `verification/audits/foundations/phase-source-audit.md`:74), and SM:505 and SM:809 name the
  step; added: the 4 versus 14 stabilizer count, its absence from Theorem 5's premises, the
  candidate $J$ off the null modes and the null-mode obstruction.
- FI-1 (§5.1): CONFIRMING. Main:590, GR:268 and GR:270 state each part, and
  `exec-source-audit.md`, `c5-discovery-audit.md` and `coherent-continuum-source-audit.md`
  state the frontier it belongs to: two named assumptions, the phase and the layer flow,
  kernel-proved independent of each other, with a strengthened necessary condition; GR:250–258
  states the phase-free form, whose repertoire has no phase operation (§5.1 (b), §5.3). The
  relation of that form to the phase is ELABORATING: `gateFlow_isolation`, GR:270 and
  `frozen-sourcing-audit.md`:289 contain its parts; added: the three-state isolation form, the
  quarter-turn identity and the real-rotation countercontrol, with the consequence that the drive
  carries the phase rather than dispensing with it (§5.1 (b)).
- F1: ELABORATING. The anchor correction in #1211 c.6738806776 anticipated the direction issue;
  the step-by-step trace of what the forward results consume is the elaboration.
- F5: ELABORATING. Sub:393–395, SM:312 and SM:316 state the observer-level placement; the
  inconsistency with SM:428, SM:511 and SM:515 was not found recorded.
- F8: ELABORATING. Spin and statistics premises are recorded for downstream chemistry claims
  (`verification/audits/manuscript/dimension-dependency-reconciliation-20261029/README.md`:8);
  added: the book counterclaims at ch06:28 / FULL:1541 and ch10:36.
- F2 (Main:403–406), F3 (Main:62, Sub:94), F6 (SM:150 (i), SM:176), F7 (SM:290–292), F9
  (#1188, QP:865), F10 (Sub:44), F11 (M-INACC-1 DESIGN:274–278): CONFIRMING; the source in
  parentheses already states the substance.

***

## 11. Smallest discriminating next proof questions

**NQ1 (complex structure on the carrier).** Let the real lift of the second-order linear update
act on phase space $(u,v)\in\mathbb R^{N}\otimes\mathbb R^{6}\oplus\mathbb R^{N}\otimes\mathbb R^{6}$
(B10, SM:296 notation), with its conserved bilinear forms (the symplectic pairing and
$E(u,v)$, SM:296) and the cubic action on the six-link index. Off the null modes the
positive-frequency $J$ commutes with the update and the cubic action, and on each non-null
mode the symplectic commutant of the mode map on the six components is $\mathfrak u(6)$ (F4). The questions that remain are:
(a) the null modes at $\alpha=1/d$ (constant and, for even $L$, staggered; SM:292), where no
complex structure commuting with the mode map and the cubic action exists: are they excluded
from the sector the observer uses, constrained, or the place where the complex structure fails;
(b) whether SM's condensate $\Sigma=\langle\phi\phi^\dagger\rangle$ is $J$-Hermitian for that $J$
beyond a stationary product covariance on one mode (several modes, the interacting and
condensate-dressed case), so that its stabilizer is $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$;
(c) the lift itself (B12, S13).
- *Why it is discriminating:* positive answers to (a) and (b) source Theorem 5's complex
  structure on the real lift, conditional on (c); a negative answer to (b) makes the complex
  structure a bridge of its own on the SM gauge chain, independent of the real lift's
  $\mathrm U(6)$.
- *Why it is small:* (a) is linear algebra on the null modes, given the constraint the
  observer's sector imposes; (b) is a comparison of two covariances once $\Sigma$'s definition on
  the real lift is fixed.
- *Scope guard:* the question is posed on the real lift; a positive answer there does not by
  itself source a complex structure at the fundamental level, whose alphabet is
  $\mathbb Z/q\mathbb Z$ (SM:312).
- *Assumption-watch link:* the C5 discovery audit's candidate 2, a polarization of the per-site
  phase space $V\times V$ acted on by the Weil representation (verdict C, the map not supplied;
  §5.1, FI-1's candidate source 3), is a phase-space structure of the same kind as the
  positive-frequency $J$. No map between the two is stated, and an answer to NQ1 does not by
  itself supply the polarization map, or the reverse.

**NQ2 (state-dependent same-sublattice couplings versus the reference grading).** The records
cited in §10 settle the first checks for SM:112's rule (directed, not symplectic, not CP at odd
$q$; no encoded $S$ under $R1^{\otimes n}$ and H-LIFT at $q=2$) and for the symmetrized
$G_\sigma$ (Lemma Q(iii)'s protection fails at $q=2$). What they leave open: for state-dependent
rules satisfying SM §3.1's constraints (i)–(iii) (SM:108), does there exist a rule such that
(a) its same-sublattice couplings are active only on a preparation class disjoint from the
vacuum/uniform reference class; (b) on that class an armable *symmetric* same-sublattice
coupling (QP's NNB) is available to the observer under P1–P3; (c) on the reference class the
scalar-dynamics bipartiteness that SM:539 and SM:569 use holds exactly (the consequence for
$D_{\rm st}$ running through SM:306); and (d) the same preparation-indexed edges serve as
H-Bell's (Sub:131)?
- *Why it is discriminating:* it decides whether QP's minimal phase repair and the SM chirality
  grading can coexist through the same preparation-indexing mechanism that H-Bell proposes; a
  negative answer separates them; a positive answer gives NNB a native source and links it to
  H-Bell (a hard-to-vary joint requirement: the same preparation-indexed edges would have to
  serve the Bell and the phase roles, cf. §A.29).
- *Records to start from:* MECH-1 DESIGN:877–893, MECH-2 §0, M-INACC-1 RESULT §0.

**Scoped negative conclusion (holds at `fd539e15` for the classes stated).** With the SM
chain's structural premises — finite bijection, site factorization, nearest-neighbour bipartite
cubic graph, A4, A5, second-order form — and the observer access as currently supplied (P1–P3,
H-PREP; maximally mixed ancilla as the only assumed preparation):
- generated: classical finite stochastic laws with memory and their universal fixed-basis
  representation; graph locality and the Bell-local ceiling; two complementary binary reads;
  the $Q$ parity selection rule at $q=2$; exact cubic representation theory; reciprocity;
- not generated: native complex phases (non-adaptive $S$ excluded; phases a stated principle);
  full reversible control and continuous state mixing (condition (iv) and the layer flow, per
  the kernel citations other than F9, for the stated substratum dynamics with read/write access
  and the stated lift formulations that land in the operational interface; the site-space
  wave-operator formulation unresolved rather than excluded); the Born exponent; quantum Bell
  violation; the fermionic measure;
- not derived: the carrier's complex structure (named open at SM:809; a candidate exists on
  the real lift off its null modes, F4).
- Therefore the quantum content the SM chain uses (complex Hilbert-space kinematics, Grassmann
  measures, unitary QFT, Born statistics on coherent instruments) is at present supplied by the
  observer-level lift and by named and unnamed bridges, not generated by the substratum, the
  lattice or the observer's specified access. The phase, state mixing (with FI-1 as its
  necessary condition) and H-Bell are unsupported obligations, with the carriers and scopes of
  §5.3, none derived from another in the sources read. The phase is independent of the layer
  flow; under phase-free richness it is not a separate operation, being carried by the complex
  driven transition, so the mixing source must be that transition and not a real rotation. FI-1
  is the first
  unsupported step toward exact finite endomorphic operational QM within the structural
  architecture, on the configuration carrier, only with the phase taken as stated. The earliest
  unproved assumptions are the stated inputs: the read/write access for FI-1, and the site
  factorization for the spatial route and H-Bell (§5.2).
  Adaptive native processes, state-dependent graphs beyond the records cited in §10, the
  site-space wave-operator lift and extended mechanisms are outside this conclusion and remain
  open.

***

## 12. Questions for the owner

1. **F4 bridge naming (answered, conditional).** The owner answered in #1211 c.6740537555:
   "Complex structure: Yes, track it independently if the review confirms it is an additional
   premise. It should not be hidden inside an SM bridge assumption." The decision takes effect
   only on a review ACCEPT. The r1, r2 and r3 reviews each confirmed that the complex structure
   is a premise of Theorem 5 that SM:340–342 does not list (F4). Any manuscript wording change
   needs separate authorization.
2. **F1, F4, F5, F7, F8, F10 (answered, conditional).** The owner answered in the same comment:
   "Manuscript corrections: Yes, use a separate correction unit after the audit. Unsupported
   statements should be narrowed without changing the scientific results." This also takes
   effect only on a review ACCEPT. Sites: Sub:68, Sub:26, Sub:459, Sub:463, Sub:44 (F1, F10);
   Sub:163, Structure:152, Structure:1153, FULL:736, FULL:939, FULL:1226, SM:340 (F4);
   SM:428, SM:511, SM:515 (F5); SM:288, ch05:91, FULL:1409 (F7); ch06:28, FULL:1541, ch10:36
   (F8). They are recorded here only.
3. **Next unit.** The owner has deferred the choice of unit 2 (2026-11-09, relayed by the
   coordinating session): the next unit "should address the earliest unresolved dependency that
   can actually advance the proof". This unit selects neither NQ1 nor NQ2. §5.2 and §5.3 list
   the unresolved dependencies the choice would be made from: the stated inputs (site
   factorization, the access), FI-1 with its four candidate sources (one of them S13, which the
   spatial route shares), the phase, and H-Bell. NQ1 and NQ2 are questions those dependencies
   raise; NQ2 touches the quarter-phase line of #1169 and the H-Bell obligation.
4. **MECH-2:530–534.** Should the correction of that record's attribution of the grading
   failure to nonlinearity (§10) be recorded where MECH-2 is tracked? It changes none of that
   record's conclusions.

F9 is decided by #1188's owner decision ("Do not use it as scientific evidence"); the reviewer
is designated by #1211 c.6738806776 (a fresh, independent reviewer).

***

## 13. Verification scope

- Paper trace only. No simulation, enumeration campaign, Lean build, manuscript edit, git
  write, PR, GitHub write, freeze or dispatch occurred.
- r1 sanity checks: `probes/check_carrier_and_grading.py` (in this scratchpad folder), run
  once with `python3 -I`, before the owner's generic-check permission (#1211 c.6739843458) and
  outside the authorization then in force (c.6738806776, "no computation;"). Check A:
  stabilizer Lie-algebra dimension of a generic $O$-equivariant symmetric $\Sigma$ on the six
  signed links, 4 in $\mathfrak{so}(6)$ and 14 in $\mathfrak u(6)$; eigenvalue multiplicities
  $(1,2,3)$. Check B: $\lVert\{D_{\rm nn},\varepsilon\}\rVert=0$ and
  $\lVert\{D_{\rm nn}+0.1D_{\rm same},\varepsilon\}\rVert=0.8$ on an 8-site ring, for a
  symmetric adjacency, not $D_{\rm st}$. No r2 statement rests on them.
- r2 exact checks, under that permission: `probes/r2_generic_checks.py`, output
  `probes/r2_generic_checks.out` (all PASS), run with `python3 -I`; exact sympy on generic
  mathematical objects (the cubic rotation group on six signed vectors; a $2\times2$
  symplectic mode map tensored with $I_6$; shift operators on a 12-site ring), importing no
  earlier script. C1 supports F4's stabilizer count; C2 supports F4's candidate $J$, its
  $\mathfrak u(6)$ commutant, the stationary-covariance stabilizer (C2(d), the one statement
  marked computation-supported) and the null-mode obstruction, with a countercontrol; C3 is
  the §10 countercontrol on the transfer to $D$, with its control. No check is run on an OI
  mechanism; they are controls on algebra stated in the text, not evidence for a physical
  result.
- r3 exact checks, under the same permission: `probes/r3_generic_checks.py`, output
  `probes/r3_generic_checks.out` (all PASS), run with `python3 -I`, importing no earlier
  script; exact arithmetic on generic objects only (a fixed six-vertex bipartite graph that is
  neither a ring nor a cubic lattice, with per-vertex Boolean update functions; $2\times2$ and
  $3\times3$ matrices). K1 checks, exhaustively over all $2^{12}$ initial configurations for
  five ticks, that the functional sector split of §10 holds for a nonlinear rule with a
  bipartite, center-free read pattern, with the linear rule as control and a self-term and a
  same-colour read as countercontrols that break it; it is a witness for the hand induction,
  not a proof of it. K2 (n1: non-monomial versus state-mixing), K3 (the exponent on
  permutation matrices and on a weighted monomial Kraus family) and K4 (an operator-level
  illustration of the independence in §5.1 (b)) check algebra stated in §5.1. No statement is
  supported only by these checks.
- r4 exact checks, under the same permission: `probes/r4_generic_checks.py`, output
  `probes/r4_generic_checks.out` (all PASS), run with `python3 -I`, importing no earlier script;
  exact arithmetic on generic objects only (integers mod $p$ for $p\le13$; exact $2\times2$ and
  $3\times3$ complex matrices; $\mathbb F_2$ rules on the complete bipartite graph $K_{2,4}$;
  two-qubit rational matrices). J: $J_0^2=-I$ over every $\mathbb F_p$ checked, which refutes
  the r3 scope guard of NQ1, with the existence criterion for a symplectic $J$ commuting with
  the mode map and a null-mode countercontrol (§11; the criterion is not used in the text).
  D: a driven transition on three states is non-monomial and moves the all-ones ray, on two
  states it keeps it, and an involution's gate flow keeps it (§5.1 (b), §5.3). L: a linear rule
  with one same-colour read breaks the sector split, against the linear opposite-colour control
  (§10). B: the reviewer-supplied rational CHSH witness and the irrationality of the Tsirelson
  value (§5.3). No statement is supported only by these checks.
- r5 exact checks, under the same permission: `probes/r5_generic_checks.py`, output
  `probes/r5_generic_checks.out` (all PASS), run with `python3 -I`, importing no earlier script;
  exact sympy with a symbolic real angle on generic objects only ($2\times2$, $3\times3$ and
  $4\times4$ complex matrices built by hand from the transition generator and the gate-flow
  formula; two-qubit matrices). The closed-form drive is certified as the exponential by its
  initial value and differential equation. I: the isolation form of the driven transition and the
  single-transposition case of the kernel-shaped isolation identity, with a countercontrol that
  drops the relative phase. Y: the image of the all-ones vector for every angle and the pair-block
  entries, with monomiality sampled, a two-state control and a gate-flow control. Q: the
  quarter-turn identity, its channel equal to the quarter phase on the third state and, by
  permutation transport, on every state of the three-state level, with countercontrols (the
  exchange alone; two states). R: the real rotation, its non-monomiality and motion of the ray,
  the Lie dimensions 3 against 8, and the reality of its channels against the quarter phase. H:
  CHSH $=6\cos\alpha-4\cos^3\alpha$ for every $\alpha$ (§5.3). They check algebra stated in
  §5.1 (b) and §5.3; no statement is supported only by them.
- Kernel identifiers cited were confirmed to exist at `fd539e15` (grep of the named files).
  In r3 the statements of `obligations_independent`, `exists_nonMonomial_of_layerFlowExecutable`,
  `uncountableNonMonomialRays_of_layerFlowExecutable`, `uncountableNonMonomialRays_of_qm`,
  `uncountable_of_layerFlowExecutable`, `obs_availExt_le_substratum`, `obsTheory`,
  `obsTheory_rule_independent`, `substratumClass`, `ConfigurationLevel` and `availExt_bind`
  were read at their declarations; in r4 and r5 those listed in the header's r4 and r5 lines
  were. None was re-verified or audited beyond that reading and the definition reading in F9.
- Limits: SM §§6–9 beyond the lines cited, Main §3.4 beyond the lines cited, GR beyond §3.3's
  opening and GR:260, GR:270, Structure beyond the lines cited, the book beyond the lines
  cited, and the remaining oi-qm records (apparatus-1 in full, native-y-continuation, track-b,
  track-i, oi-qm-ext-1 beyond two-mode-drive §§1–3 and heads, MECH-1/MECH-2/M-INACC-1 beyond
  the parts listed in the header) were not read in full; nor were the foundations audits
  beyond the parts listed in the header, or the other audits under
  `verification/audits/foundations/`. Negative statements in §9 are bounded
  by the header's coverage list.
