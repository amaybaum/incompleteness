# Node 6 (A2 track, node 1): the quantum appearance in an observer's records

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. This is the
first node of the A2 track (PLAN, "A2 track"), run under the owner's guiding principle of 2026-10-20 and the owner's
node-6 guidance of the same day (three outcomes kept apart; record statistics first; no-go theorems applied with their
exact assumptions; derivation from observational limits preferred over building quantum structure in).

**Base.** Thread records at `research/missing-component-20261020` = `649027c9` (PLAN = `../PLAN.md`, N1 =
`../oa-node1/NODE.md`, MC1–MC5 = `../mc-node{1..5}/NODE.md`, each with its review outcome). `main` = `55a0e80a`;
`papers/` and `verification/lean-mathlib/` are identical to `df9e601e` (`git diff --quiet`), so paper and Lean lines
hold at both. Lean paths are under `verification/lean-mathlib/OIBridge/`; every [AT] name was confirmed by `git grep` of
its declaration at `55a0e80a`. Book lines are at `55a0e80a`.

**Tags.** [AT] adopted kernel theorem; [W] written argument here; [EC] exact computation here (`probe/p6.py`, SymPy
1.14.0, Python 3.13.16, `-I -B`, two runs byte-identical); [NUM] floating-point evidence, never evidence of exactness
(one comparison, B3); [UP] unsourced premise; [L] literature, cited from memory unless stated; [rec] recorded in the
cited record, not re-derived. Probe checks on preparation contextuality are named P1–P5, to keep them apart from the
corpus's conditions C1–C4.

**Productivity test (fixed before the node, from the brief).** Gem iff the node yields a fact strictly stronger than
"A2 needs M and R", and either identifies which structural feature of the deeper reality or of the observational
limitation is necessary for the quantum appearance, or exposes a hidden assumption in how the thread has framed the
problem. The owner's node-6 guidance arrived after the test was fixed and before any probe was run. It governs the
classification (§5) and the no-go analysis (§2); the test was not changed.

**Three outcomes (owner, 2026-10-20), used throughout and kept apart.**
- *Emergence*: quantum statistics follow from the deeper dynamics plus limited observation, without assuming the answer.
- *Reproduction*: a model matches QM experimentally but introduces quantum-like structure as an independent assumption.
- *Failure*: the model cannot reproduce a measurable quantum phenomenon.

***

## 0. Headline

1. **Which observable the A2 track measures [W, EC A1–A4; corpus].** There are three observables for "the world looks
   quantum":
   - R0, per-menu representability of record laws (Main §3.4, S ⟺ D ⟺ Q_fb). Every finite law is in it, PR boxes
     included (A4; Main:356), so R0 cannot be the target.
   - R1(d, m, K, ε): one finite reversible realization (bijective dynamics, configuration readout, mixed hidden prior)
     and a map from quantum protocols of dimension d, at most m outcomes and horizon at most K to its protocols, such
     that each quantum protocol's record law is within ε in total variation of its image's, and each realization
     protocol's law is within ε of a quantum law. A composite enters as one d_A·d_B-dimensional system, so an
     instrument on it may depend on both parts' settings; local subsystem structure is not part of R1. This is the
     owner's "quantum behaviour in the statistics of an observer's records", at fixed dimension, outcome bound, horizon
     and tolerance.
   - R2, availability under G3 on the visible carriers (F2's `DenseFiniteQM`). The quantum system is the visible
     configuration register itself.

   MC3's cone lemma and MC5's clauses M and R are R2 statements. They do not bind R1: a κ1–κ4 construction (bijections,
   configuration readout, mixed hidden prior) keeps every visible map in the cone 𝒞(C) (A2), yet its records equal the
   qubit's sequential Pauli statistics on all 234 protocols checked (A1). At R1 the corpus already proves Reproduction
   at fixed d, m, K and ε, with a composite treated as one system (Main:576–578, the quantum-shadow realizations; a
   paper theorem with probe checks, not kernel-certified). Local composite structure is the operational-lifting problem
   Main:534 and :578 leave open; Main:580 calls what remains selection (route (ii)), and the book names the selection
   problem at appendix-c:228 and :234. PLAN's A2 track (PLAN:204–212) draws its task from R2 results and leaves open
   whether availability is the right observable (PLAN:209–210); this node answers that question at R1.
2. **Classification of the A2 question at this node's scope: (c) undetermined.** Reproduction at R1 is established
   (corpus) and is not Emergence, because the shadow realizations code quantum instruments into their tables. Failure
   is established for two constructions:
   - the finite-range, measurement-independent deterministic completion, for Bell (Main §3.3; B1);
   - every preparation-noncontextual model whose parity mixtures are exactly operationally equivalent, for
     parity-oblivious multiplexing (P1–P3).

   No Emergence of quantum statistics was found. The decisive open question is related to the corpus's selection
   problem; appendix-c:228 states that problem for the non-commutative operational structure, and the question here is
   its form at R1, sharpened in item 3.
3. **What Emergence at R1 would need (necessary, not jointly sufficient) [EC, W, L]:**
   - *N1, preparation contextuality, given exact operational equivalence.* In a model whose two parity mixtures are
     exactly operationally equivalent, as QM's are, POM success above 3/4 requires preparation contextuality (P3,
     general by coarse-graining Λ to the four response pairs; Spekkens et al. 2009 [L]); QM gives (1+1/√2)/2 ≈ 0.854.
     Agreement within ε does not supply the exact equivalence: a parity readout of bias ε makes the record map
     injective, so the model is preparation noncontextual for want of equivalent pairs, while POM success stays at
     17/20 (review check `leak.py`). A finite-precision N1 needs a robust noncontextuality inequality with secondary
     procedures (Mazurek et al. 2016 [L]), not applied here. History readback (C4) does not supply N1 (P1), nor do
     knowledge balance (P2) or bijectivity (§2.4).
   - *N2, for Bell.* Under determinism, either ontic parameter dependence or measurement dependence of at least 0.0309
     bits is needed (Main §3.3; B2, B3); the level of description is not an escape (B1). In the parameter-dependence
     branch with a setting-independent prior, remote dependence is not enough: GF(2)-affine dynamics with bit readouts
     stays at |S| = 2 across cones (B1m, B1a; general, since affine maps compose and B1a covers every affine pair), so
     q⊕r must contain the product of the settings at some microstate. The measurement-dependence branch needs no
     nonaffinity: B3's models are constant in the settings and reach S = 4.
   - *N3, a magnitude-fixing principle.* Each nonclassicality mechanism found here spans the whole range from the
     classical ceiling to the no-signalling or GPT maximum, with a free weight w: S = 2 + 2w for one long edge (B2b),
     and POM success (1+w)/2 for destructive complementary readouts (P5). The two are the same convexity pattern (a
     mixture of a classical and a maximal model), not independent findings. The quantum values 2√2 and (1+1/√2)/2 sit
     inside the ranges, at different weights (√2 − 1 and 1/√2), and are selected by nothing examined. Restriction can
     overshoot QM (P5 at w = 1 gives POM = 1) as well as fall short of it (the toy theory has no Bell violation;
     appendix-c:232).
   - *N4, response-relevant capacity unbounded in the precision.* Main:580 item (3) gives the exact obstruction: no fixed
     finite classical carrier reproduces full qubit behaviour. For a fixed carrier the set of behaviours over all priors
     is closed (finitely many bijections, compact prior simplex), so an obstruction that already holds on a finite test
     set gives one at some ε_N > 0 [W]. Hence the carrier must grow as ε → 0 (Hardy's excess baggage [L]).
   - *N5, Kochen–Specker through memory.* With labelled instruments fixed (Main:550), Kochen–Specker contextuality must
     be carried by hidden memory that earlier measurements update (K1; [W]; Kleinmann et al. 2011 [L]).
4. **Emergent features found are classical-compatible.** These follow from OI's limits without assuming QM:
   - double stochasticity of uniform-prior one-step laws (D1, a replay of Main §3.1), necessary for unistochasticity;
   - operational no-signalling from graph cones (Main §3.3);
   - C4 memory.

   Each also holds in classical local, noncontextual theories, so none separates quantum from classical record
   statistics.
5. **G6: none.** The preregistered rule (§3) rejects each candidate.

***

## 1. Branch node L1 (B1): which observable is "the world looks quantum"?

### 1.1 What the corpus already claims (§A.19)

- **R0 is universal.** S ⟺ D ⟺ Q_fb on every finite horizon (Main:82, :532; `finite_horizon_equivalence`,
  `Equivalence.lean`). Main:534 says representability is not the discriminating content and names "exact
  coherent/composite compatibility" as the residual operational-lifting problem. Main:356 says bare finite OI
  representability realizes PR-box behaviour.
- **R1 Reproduction is a paper theorem.** The uniform continuum realization (Main:576) gives, for each (d, m, K, ε), one
  finite reversible realization R mutually ε-dense with the operational quantum theory: the R1(d, m, K, ε) of §0.
  Main:578 takes a sequence R_n along K_n → ∞, ε_n → 0 and states: "As classes this is density, not identity:
  D_finite is strictly larger — the response-table construction realizes arbitrary finite stochastic behavior, quantum
  or not … the remaining question (route (ii)) is the operational-lifting problem". Main:580 calls what remains
  "precisely selection — route (ii)". The single-dynamics corollary (Main:560) makes the realization one map with a
  program register. Main:576 is a paper theorem with probe checks, not kernel-certified. A composite enters it as one
  system of dimension d_A·d_B; local structure is not part of it.
- **The selection problem is named.** Book appendix-c:228 ("Whether embedded observation selects the non-commutative
  structure is the framework's open selection problem"), restated at :234; appendix-c:232 ("restricted access does not
  by itself single out quantum theory"). Appendix-c:228 concerns the non-commutative operational structure. The R1
  Emergence question of this node is related to it, not identical to it.
- **The kernel's emergence result is R2-shaped and is a uniqueness.** `QuasilocalCharacterization.lean`:
  - the region completion is the unique member, up to canonical isomorphism, of the class of quasilocal systems with the
    substratum's configuration matrix algebras as stages (`systemEquiv_unique` :385, `canon_unique` :359);
  - with dynamics, two OI systems with the same substratum dynamics are canonically isomorphic (`systemEquiv_dyn` :497);
  - the induced dynamics has real transported entries, and a one-site phase is induced by no reversible finite-range
    substratum dynamics (`phaseQ_ne_heisQ` :792).

  Per §A.34 this is uniqueness given those stages. It does not derive quantum statistics, and its quantum system is the
  configuration algebra: G3 on visible carriers, which is R2.

### 1.2 The checks [EC]

- **A0–A1.** A Spekkens-type toy bit as an OI construction:
  - hidden ontic pair (a, b), fresh hidden disturbance bits r_t, visible pointers p_t;
  - measurement Z: p ^= a, then b ^= r; X: p ^= b, then a ^= r; Y: p ^= a⊕b, then a ^= r and b ^= r. Every step is a
    bijection of the 2^8 states (A0);
  - preparations are mixed priors on a pair of ontic states.

  Records equal sequential Lüders records of the six qubit Pauli eigenstates for all 39 sequences of length ≤ 3, 234/234
  exact (A1), with complementarity and order dependence (A1b).
- **A2.** The pointer's induced map for one measurement has four 0/1 partial-permutation Kraus operators. Its Kraus
  channel equals Ad_U followed by the partial trace on all four matrix units. This is the cone lemma on the visible
  carrier.
- **A3.** The same carrier admits non-disturbing bijections (p ^= a without r). They are bijective (A0), and their
  records leave QM: an X repeat survives an intervening Z. The qubit-like restriction is a choice of accessible
  bijections, not a consequence of κ1–κ4.
- **A4.** A response table with global setting dependence gives S = 4. R0 contains non-quantum laws.

### 1.3 Verdict at L1

PLAN's A2 track draws its task (M, R and O-B "directly") from R2 results and poses as a question whether availability
is the right observable (PLAN:209–210). The answer at R1: the cone lemma (MC3) and clauses M and R (MC5) concern
operations available on visible configuration registers under G3. At R1, interference-type and non-real-basis (Y)
record statistics are met by κ1–κ4 constructions (A1; Main:576), as Reproduction. What remains at R1 is not M or R but
the gap between Reproduction and Emergence: κ1–κ4 is universal at R0 and dense at R1 for fixed (d, m, K) (Main:578), so
it constrains nothing until a selection principle is added.

**HA-6.1.** The A2 track takes M and R as requirements "at every precision" from the R2 endpoint `DenseFiniteQM`. Under
the guiding principle these are R2 requirements. At R1 the corpus already has Reproduction at fixed d, m, K and ε, and
the open item is related to selection (Emergence). Class: ELABORATING (an answer to the question PLAN:209–210 poses;
Main:578, :580 and appendix-c:228 state the selection problem).

**Decisive branch for L2.** A selection principle has to meet the no-go theorems at R1. These are the constraints that
bind record statistics whatever the observable rung, so L2 applies them with their exact assumptions.

***

## 2. Branch node L2 (B2/B3): necessary features, with each theorem's exact assumptions

Owner safeguard: no conclusion that OI needs a quantum or nonlocal substratum. For each theorem, the table states which
assumption an observationally incomplete model satisfies or relaxes, and then tests whether the observed statistics can
still be reproduced.

### 2.1 Assumption table

| theorem [L] | assumptions | OI's κ1–κ4 class | relaxation available | reproduces? (check) | outcome |
|---|---|---|---|---|---|
| Bell / CHSH, Main's ceiling (i)–(iv) | determinism; settings as interventions; readout before cones meet; one setting-independent pre-setting ensemble; response-complete Ω. In Jarrett's split, outcome independence is automatic under determinism, so the burden falls on parameter independence | determinism constitutional; graph cones exact for finite-range φ; measurement independence a property of the prior, retained by the corpus (Main:82) | ontic parameter dependence (Main's adopted branch (a), Main:392); measurement dependence (branch (b), recorded); readout after cone crossing | local and measurement-independent: no (B1, \|S\| ≤ 2 exhaustively). One long edge: yes, S = 4 with operational no-signalling (B2), and S = 2 + 2w for any rational w (B2b). Measurement-dependent local: yes, any S, within Main's bound (B3 [NUM]) | Failure (local, measurement-independent). Reproduction (either relaxation), with S a free weight |
| level of description (is the trace-out an escape?) | records are averages of pointwise boxes | — | — | no: B1 computes the records after the trace-out, with hidden memory present | not an escape (Methodology:385 agrees) |
| Bell with nonlinearity | — | 2-bit reversible blocks are all affine (B1m); SM's exact reference dynamics "is the linear rule … over ℤ/qℤ", with "the mod-q wraparound / threshold-crossing at the alphabet boundary" a bounded nonlinearity (SM.md:296) | nonaffine gates; state-dependent adjacency (SM.md:112; Main:392, :394 preparation-indexed edges); a nonlinear readout | parameter-dependence branch, setting-independent prior: GF(2)-affine dynamics with bit readouts gives \|S\| = 2 at every Ω even with remote dependence (B1a, all 64 affine pairs, 48 with remote dependence); a Toffoli-class long edge reaches 4 (B2). Measurement-dependence branch: no nonaffinity needed (B3) | in the parameter-dependence branch, remote dependence must be nonaffine in the settings [EC for GF(2); W for ℤ/qℤ with homomorphic readouts, a case that exists only for even q] |
| Kochen–Specker | outcome determinism; measurement noncontextuality | outcome-deterministic; each labelled instrument is one fixed map and context enters only through the state (Main:550) | contextual outcome values, which Main:550 states is the only combination KS permits | Peres–Mermin has no noncontextual assignment (0/512, K1). With fixed instruments applied in sequence, an outcome cannot depend on later choices, so the context must be carried by hidden memory that earlier measurements update [W; Kleinmann et al. 2011, L] | constrains R1: contextual values through measurement-updated memory; memory size not computed |
| preparation contextuality (Spekkens 2005; POM, Spekkens et al. 2009) | ontological-model framework (Λ, μ_P, ξ_M); preparation noncontextuality (exactly operationally equivalent procedures have equal μ) | OI induces an ontological model: Λ the response-relevant microstate, μ_P from the prior and bijections, ξ deterministic. The framework applies. The observer's description is the operational class of a procedure; the epistemic object is μ_P | PNC is neither implied nor excluded by κ1–κ4 (P1, P2 noncontextual; P4, P5 contextual) | given exact parity obliviousness, PNC models give POM ≤ 3/4 (P3, exact LP, general by coarse-graining). Contextual: up to 1 (P5), and 17/20 at N = 100 for a hidden-label model (P4). Under ε-agreement only, PNC is vacuous (`leak.py`) | Failure for any PNC model with exact parity obliviousness (knowledge balance; C4-type readback alone). Reproduction (P4); contextuality from a posited restriction with a free magnitude (P5) |
| PBR | framework; preparation independence (product preparations give product μ); quantum predictions for an entangled measurement | the canonical uniform prior is a product, so PI holds when the systems' response-relevant data are disjoint blocks [W]; it fails when they share hidden data (co-embedding, Methodology:389) | shared hidden sector | not computed. With PI, R1 Reproduction needs ψ-ontic response-relevant data [L]. In Main:576 the instrument labels sit in the visible intervention record, which the controlled step reads; with that record counted in Λ, Λ determines the protocol and hence ψ [W]. In the toy construction, responses do not read the preparer's record (§2.4) | constrains Emergence accounts with disjoint partners to ψ-ontic response-relevant data. With a shared sector, PBR does not bind |
| ψ-epistemic overlap bounds (Barrett–Cavalcanti–Lal–Maroney 2014; Leifer 2014) | framework only, d ≥ 3, exact QM; robust forms exist [L, not read] | framework applies | — | not computed | a ψ-epistemic Emergence account cannot attribute most nonorthogonal indistinguishability to ontic overlap at large d [L] |
| Hardy excess baggage | framework, exact qubit statistics | finite Λ at any fixed stage | — | Main:580 item (3), with the compactness step of N4 | response-relevant capacity must grow without bound in the precision (N4) |

Whether an observer's description counts as an epistemic state in PBR's sense [W]: PBR's ψ labels a preparation's
operational statistics. At R1, a tomographically complete quantum-appearing theory fixes ψ from the statistics. The
non-uniqueness of the fixed-basis dilation Θ (Main:212 (i)) concerns the R0 representation, not the operational state.
So the framework applies to OI at the level of procedures. The assumption OI can relax is PI, not the framework.

### 2.2 Verdicts at L2

- **Bell (CONFIRMING with exact OI-native instances; one narrow addition).** Main §3.3 and Methodology:393 already
  state the ceiling, the two relaxations and that "no-signaling, hidden memory, and indivisibility are all insufficient
  by themselves to select the quantum correlation set". The addition is narrow. In the parameter-dependence branch with
  a setting-independent prior, remote dependence through GF(2)-affine dynamics with bit readouts cannot exceed 2. This
  holds generally, because affine maps compose and B1a covers every affine pair of response functions. So q⊕r must
  contain the product of the settings at some microstate. The reference SM update is linear over ℤ/qℤ apart from the
  mod-q threshold nonlinearity at the alphabet boundary; the state-dependent graph is not linear (SM.md:112, :296). For
  ℤ/qℤ the statement is [W] with homomorphic readouts, which exist only for even q. With a non-homomorphic readout the
  readout itself is a nonlinearity; that case was not checked. The measurement-dependence branch needs no
  nonaffinity (B3).
- **Preparation contextuality (the decisive sub-branch: absent from the papers).** `git grep -i "preparation
  contextual"` over `papers/` returns nothing; Main:550 disclaims Spekkens noncontextuality without using it.
  - **P1.** A delay line (x, h) ↦ (h, x) satisfies C4 exactly: P(x₂ = 0 | x₁ = 0, x₀ = 0) = 1 and
    P(x₂ = 0 | x₁ = 0, x₀ = 1) = 0. Its record map on hidden distributions, derived from the dynamics, has rank 4/4.
    So exactly operationally equivalent preparations have identical ontic distributions: it is preparation
    noncontextual.
  - **P2.** The toy bit's single-measurement statistics already determine the ontic distribution (rank 4/4).
  - **P3.** Exact LP over models on four ontic states with every deterministic response function: under PNC with exact
    parity obliviousness, the maximum POM success is exactly 3/4, and with the toy's decodings also 3/4. Without parity
    obliviousness it is 1 (countercontrol). The LP is general for two binary measurements. For fixed μ, deterministic
    responses are optimal. Coarse-graining Λ to the four response pairs preserves both the PNC equality and the
    success.
  - **P4.** A hidden-label construction stores which of the four Bloch vectors was prepared and a uniform
    u ∈ {0,…,N−1}, and writes [u < N·round_N(p)] into a pointer, which is a bijection. It is parity-oblivious exactly,
    on 16 XZ-plane axes and ±Y. Its success is 3/4, 7/8 and 17/20 at N = 4, 8 and 100. The parity mixtures'
    hidden-label supports are computed to be disjoint. Reproduction: the Born weights are coded into the table. At
    N = 8 it overshoots QM (7/8 > 0.854), as an ε-approximant may.
  - **P5.** On a classical 2-bit ontology, the accessible readouts are destructive and complementary: reading bit y
    XORs fresh hidden randomness into the other bit. The construction is a bijection, is parity-oblivious on all 14
    sequences of length ≤ 3 (and so on adaptive ones of that length), and its parity mixtures differ ontically. With
    weight w on the deterministic preparation, success is exactly (1 + w)/2: 1 at w = 1, 17/20 at w = 7/10, and 3/4
    at w = 1/2. Its Z and X steps are the toy bit's on all 16 states. Its contextuality needs the toy's Y readout,
    a bijection on the same carrier, withheld: adding it breaks parity obliviousness for every w > 0 (review check
    `c5y.py`). Contextuality follows from a posited limit on observation. The weight w is free, and at w = 1 it reaches
    the GPT maximum (this is the gbit; Barrett 2007 [L]).
  - **Robustness (review check `leak.py`).** P5 extended by a destructive parity readout of bias ε (ε = 1/100, 1/1000)
    is within about 3ε of parity obliviousness on all 39 sequences of length ≤ 3, and its record map has rank 4/4. It
    is therefore preparation noncontextual, vacuously, while POM success stays at 1 (w = 1) or 17/20 (w = 7/10).
    PNC with the 3/4 ceiling binds only under exact operational equivalence.

  **Necessary feature N1 [EC; L].** In a model whose parity mixtures are exactly operationally equivalent, as QM's are,
  reproducing the quantum POM value requires preparation contextuality. The hidden sector must then retain
  response-relevant preparation information that no accessible protocol reveals. C4 concerns memory that is read back;
  N1 concerns memory that is never read back. P1 shows C4 does not imply N1, and P2 shows the toy bit's knowledge
  balance does not either. At finite precision N1 is not established: it would need a robust noncontextuality
  inequality with secondary procedures (Mazurek et al. 2016 [L]), which this node does not apply.
- **Magnitude (N3).** B2b and P5 show one convexity pattern in two settings. A mechanism that produces the nonclassical
  feature at all produces every value from the classical ceiling (2; 3/4) to the maximum (4; 1), set by a prior weight.
  The quantum values (2√2; (1+1/√2)/2) are interior and unselected. This is §A.29's adjustable-to-any-outcome pattern.
  Observed Bell values are not above 2√2 beyond error [L]; under §A.24 that is a raw-direct datum, which these
  mechanisms accommodate only by tuning w.

### 2.3 Pressure test of the favourable readings (§A.31)

- *P5 as Emergence.* The destruction is a hidden-randomness coupling. P5's dynamics are the toy bit's Z and X steps, and
  its contextuality needs the toy's Y readout, a bijection on the same carrier, withheld (`c5y.py`). So the restriction
  is posited, as the toy bit's is (A3), and the label is not Emergence. As a model of QM it is Failure at untuned w
  (POM = 1 at w = 1, which QM forbids and a finite-precision experiment separates) and Reproduction only at w = 1/√2.
- *B2/B2b as support for branch (a).* B2 shows the adopted branch can reproduce quantum S values. B2b shows it fits
  every S in [2, 4] equally well. That is support for Reproduction, not for Emergence.
- *A1 as a derivation.* The 234/234 match is guaranteed by the toy theory's construction (the stabilizer fragment).
  It shows that R1 is not bound by the cone lemma. It is no evidence for Emergence (A3).
- *P1–P3 as a finite-precision constraint.* They are not one (`leak.py`); N1 is stated under exact equivalence.

### 2.4 Node L3: does bijectivity supply N1? [W]

Reversibility forbids erasing the difference between two preparation procedures, so the difference persists somewhere in
the global microstate. In the toy construction it persists in the preparer's record register, which the responses do
not read, while the system's response-relevant marginals of operationally equivalent mixtures are identical (P2:
noncontextual). So bijectivity places the information but does not put it into the response-relevant data. **Verdict:
N1 is not supplied by bijectivity or by C4. It is an additional requirement on the trace-out.** [W, with the P2
instance.]

***

## 3. Branch node L4 (B4): G6 at A2

**Decision rule, fixed before this section (MC5 §7 control 5):** a candidate counts iff it gives a finite-precision
statistic that differs from QMfin on some protocol, its size is fixed by OI quantities without free parameters, and both
outcomes are possible.

| candidate | verdict |
|---|---|
| finite-N discretization of Born weights (P4, Main:576 nets) | size set by N, a free stage parameter: rejected |
| super-quantum POM or CHSH at untuned weights (P5, B2b) | size set by w: rejected; the observed values constrain w (accommodation) |
| a capacity limit on generic entanglement: response-relevant memory or computation exponential in the number of entangled qubits, against C3's ~10^122 (Main:78) | threshold logarithmic in the capacity (n ~ 400 for memory) but construction-dependent: the shadow nets cost O(m·16^n·log 1/δ) record bits (Main:576), the lower bounds rest on complexity conjectures and Markovian-model theorems [L: Montina 2008; Regev–Klartag 2011; Davies 2007, not read], and the deviation's form is unspecified. Size not fixed: rejected. Recorded as a direction only |

**Verdict: no G6.**

***

## 4. Controls (§A.29)

| # | control | type | outcome |
|---|---|---|---|
| 1 | cone lemma reproduced on the toy construction's visible carrier (A2): Kraus channel against the Ad_U and partial-trace route | must-hold, two code paths | holds |
| 2 | non-disturbing bijections on the same carrier leave QM (A3) | can-fail: would fail if κ1–κ4 forced the restriction | QM fails as predicted |
| 3 | Bell ceiling under OI's actual readout, local automaton (B1) | must-hold path check. Deterministic local boxes give ±2 at every point, so attainment is automatic, and the cone check passes by geometry; its sensitivity is shown separately (control 4) | \|S\| ≤ 2 on 576 rule pairs × 64 microstates |
| 4 | cone check sensitivity (B1m): four steps on the same ring | can-fail countercontrol | remote dependence detected at 23 552 points |
| 5 | PR negative control (Main:407 calls it mandatory): one nonaffine long edge (B2) | must-fail for locality | S = 4, operational no-signalling |
| 6 | PNC POM ceiling under exact parity obliviousness (P3) | must-hold; general by coarse-graining | 3/4 |
| 7 | POM without parity obliviousness (P3) | can-fail countercontrol | 1 |
| 8 | PNC under ε-agreement (`leak.py`) | countercontrol on the scope of N1 | PNC vacuous, POM 1 or 17/20 |
| 9 | P5 with the toy's Y readout restored (`c5y.py`) | countercontrol on P5's label | parity obliviousness broken for w > 0 |
| 10 | KS operator identities computed (K1) | must-hold | hold |
| 11 | Main §3.1 replay (D1): 21 matrices, 6 failing the necessary condition | replay of a recorded count | matches |
| 12 | PLAN controls: `permTheory_not_qm`, `substratum_residual`, rooted law and M1, K_B/K(Z_F)/Γ(Q3), no E0 positing | — | not engaged: no candidate is proposed at R2. At R1 the analogue of "representability does not stand in for availability" is control 2 together with A4 (R0 does not stand in for R1) |
| 13 | G6 with preregistered rule | — | fails (§3) |

Independent-review mutations (the reviewer's working directory, not copied): the reviewer reports that the probe's controls fail when
broken [rec].

***

## 5. The three outcomes, classified

| result | outcome | why |
|---|---|---|
| toy-bit construction (A1) | Reproduction of the stabilizer fragment; Failure for exact-equivalence POM > 3/4, Bell and continuous interference | the knowledge-balance restriction is an independent posit (A3); PNC (P2) |
| quantum-shadow realizations (Main:576–578), hidden-label model (P4) | Reproduction | quantum instruments and Born weights are coded in the tables |
| local, measurement-independent deterministic completion (B1; Main §3.3) | Failure | \|S\| ≤ 2 |
| long edge (B2, B2b), measurement dependence (B3) | Reproduction possible; over-generates | S is a free weight in [2, 4] |
| destructive complementary readouts (P5) | contextuality from a posited restriction, not Emergence; as a model of QM, Failure at untuned w (POM = 1 at w = 1) and Reproduction only at tuned w | P5's steps are the toy bit's Z and X steps; its contextuality needs the toy's Y readout withheld, a bijection on the same carrier (`c5y.py`), so the restriction is a choice of accessible bijections, as for the toy bit (A3) |
| double stochasticity under the uniform prior (D1), operational no-signalling (Main §3.3), C4 memory | Emergence of classical-compatible features | each holds in classical theories; none separates |
| Emergence of quantum statistics proper | none found | — |

***

## 6. Re-reading node 5's headline under the guiding principle

Each sentence below attributes to the empirical question, or to OI, what was shown for operations under G3 on visible
carriers (R2) or for the listed constructions.

1. MC5:298–300. Proposed replacement:

   > **What is empirically at stake, at the level of availability.** U and O conflict only with the A1 target
   > definition: at A2 they are not needed (MC2), and no finite-precision experiment separates the two endpoints (§5).
   > As available operations under G3 on visible carriers, M and R are needed at every precision, so their realization
   > question cannot be avoided by relaxing exactness. Record statistics are a different observable: there the corpus
   > reproduces quantum statistics at fixed dimension, outcome bound, horizon and tolerance with configuration-bijection
   > processes (Main.md:576), and the open question is selection (`mc-node6`).
2. Optional clarification. MC5:52–56 (§0 item 3) and :293–294, "No construction examined supplies M by substratum
   dynamics while keeping κ2 … and supervenience". This is already scoped to realization. "As an available operation"
   could be added, since at R1 the toy bit and the shadow realizations keep κ2 and supervenience and supply M-type
   record statistics as Reproduction.
3. Optional clarification. MC5:40, "and no source exists in OI for the constructions examined". It could read "no
   construction examined supplies a source".
4. MC5:48 and :275 ("(i) is ruled out …", "(i) Can it emerge from OI? Ruled out for these constructions") are scoped
   correctly. Under the guiding principle they concern emergence of available operations (R2); the owner's Emergence
   question at R1 is open (§0 item 2).
5. PLAN:209: "The track therefore has to address" becomes "At that endpoint the track has to address".

MC5's §4 list of excluded constructions, its "not a claim about every observer-level extension" and its §9 scope note
are correctly scoped and need no change.

***

## 7. Hidden-assumption markers

| # | assumption | where | finding | class |
|---|---|---|---|---|
| HA-6.1 | A2 means `DenseFiniteQM` under G3, so M and R bind "at every precision" | PLAN:204–212; MC5:298–300 | R2 framing. At R1 the corpus has Reproduction at fixed d, m, K, ε (Main:576–578), and the open item is related to selection. PLAN:209–210 poses the question; this is an answer | ELABORATING (Main:578, :580; appendix-c:228) |
| HA-6.2 | C4 (history readback), OI's discriminating content, carries the hidden memory the quantum appearance needs | Main:534 reads C4 as discriminating against Markov, not against classical; the A2 track is silent | C4 does not imply preparation contextuality (P1). Under exact equivalence, the needed memory is response-relevant and never read back (N1) | BORDERLINE: no paper claims C4 suffices, but N1 is absent from the papers and from the thread; scoped to exact equivalence |
| HA-6.3 | an access restriction can only under-generate relative to QM | appendix-c:232 | restriction can also overshoot: destructive complementary readouts give POM = 1 (P5). Appendix-c:232 already states that restricted access does not single out quantum theory | CONFIRMING |
| HA-6.4 | ontic parameter dependence suffices for S > 2 under measurement independence | Main §3.3 states necessity only | in the parameter-dependence branch, affine remote dependence stays at 2 (B1a) | record-only |
| HA-6.5 | Bell is the sole place where the magnitude of nonclassicality is unselected | Methodology:393 | the same convexity pattern appears with preparation contextuality (P5) | record-only |

Assumption-watch markers:
- **AW-MC6-1.** A claimed A2 result names its rung: R0 (representability), R1(d, m, K, ε) (records of one realization at
  fixed dimension, outcome bound, horizon and tolerance, a composite entering as one system) or R2 (G3 availability).
  The cone lemma and clauses M and R are R2.
- **AW-MC6-2.** A positive-looking result is classified as Emergence, Reproduction or Failure. Matching QM by coding
  instruments, Born weights or a tuned weight into the realization is Reproduction. A posited restriction on accessible
  bijections that is tuned or chosen to match is not Emergence.
- **AW-MC6-3.** Emergence at R1 must meet:
  - N1, invisible response-relevant preparation memory, in any model that keeps QM's operational equivalences exactly.
    Without exact equivalences, PNC is vacuous at finite precision, so a finite-precision N1 needs a robust inequality;
  - N2, ontic parameter or measurement dependence for Bell, nonaffine in the settings in the parameter-dependence branch;
  - N3, a magnitude-fixing principle that confines CHSH to [2, 2√2] and POM to [3/4, (1+1/√2)/2] and admits the
    quantum values;
  - N4, capacity unbounded in precision;
  - N5, Kochen–Specker contextuality carried by measurement-updated memory.
- **AW-MC6-4.** No-go theorems are applied with their exact assumptions. The OI-induced ontological model satisfies the
  framework. What it can relax is measurement independence, parameter independence, PNC, measurement noncontextuality
  (realized at R1 only through measurement-updated hidden memory) and PI. None of these relaxations by itself makes the
  substratum quantum, and none selects the quantum magnitude.
- **AW-MC6-5.** Preparation-indexed edges added to a linear update with parity readouts give |S| ≤ 2. Branch (a)
  (Main:392, :394) needs setting dependence that enters nonlinearly (state-dependent adjacency read at the settings, or
  a nonlinear readout).

***

## 8. Literature (Step 4)

Cited from memory. Bibliographic data not re-verified, texts not read in this node, except the corpus's own citations
as they appear in Main.
- J. S. Bell, Physics 1, 195 (1964); S. Kochen, E. P. Specker, J. Math. Mech. 17, 59 (1967); A. Peres, Phys. Lett. A
  151, 107 (1990); N. D. Mermin, Phys. Rev. Lett. 65, 3373 (1990); J. P. Jarrett, Noûs 18, 569 (1984); M. Kleinmann,
  O. Gühne, J. R. Portillo, J.-Å. Larsson, A. Cabello, New J. Phys. 13, 113011 (2011) (memory cost of contextuality).
- R. W. Spekkens, Phys. Rev. A 71, 052108 (2005) (preparation contextuality); R. W. Spekkens, D. H. Buzacott, A. J.
  Keehn, B. Toner, G. J. Pryde, Phys. Rev. Lett. 102, 010401 (2009) (parity-oblivious multiplexing); R. W. Spekkens,
  Phys. Rev. A 75, 032110 (2007) (toy theory); S. D. Bartlett, T. Rudolph, R. W. Spekkens, Phys. Rev. A 86, 012103
  (2012) (epistemically restricted Liouville mechanics); D. Schmid, J. H. Selby, E. Wolfe, R. Kunjwal, R. W. Spekkens,
  PRX Quantum 2, 010331 (2021) (noncontextuality iff simplex embeddability); M. D. Mazurek, M. F. Pusey, R. Kunjwal,
  K. J. Resch, R. W. Spekkens, Nat. Commun. 7, 11780 (2016) (robust noncontextuality inequalities, secondary
  procedures).
- M. F. Pusey, J. Barrett, T. Rudolph, Nat. Phys. 8, 475 (2012); P. G. Lewis, D. Jennings, J. Barrett, T. Rudolph,
  Phys. Rev. Lett. 109, 150404 (2012); J. Barrett, E. G. Cavalcanti, R. Lal, O. J. E. Maroney, Phys. Rev. Lett. 112,
  250403 (2014); M. S. Leifer, Quanta 3, 67 (2014); L. Hardy, Stud. Hist. Phil. Mod. Phys. 35, 267 (2004).
- B. S. Tsirelson (Cirel'son), Lett. Math. Phys. 4, 93 (1980); S. Popescu, D. Rohrlich, Found. Phys. 24, 379 (1994);
  J. Barrett, Phys. Rev. A 75, 032304 (2007) (GPTs, gbit); M. Pawłowski et al., Nature 461, 1101 (2009); M. Navascués,
  Y. Guryanova, M. J. Hoban, A. Acín, Nat. Commun. 6, 6288 (2015).
- A. Montina, Phys. Rev. A 77, 022104 (2008); O. Regev, B. Klartag, STOC 2011; P. C. W. Davies, Fluct. Noise Lett. 7,
  C37 (2007).
- Corpus citations used as cited there: Barandes–Hasan–Kagan, arXiv:2512.18105 (Main ref. [24]); Hall–Branciard (Main
  ref. [57]).

***

## 9. Not verified

- R1(d, m, K, ε) is defined in words (§0 item 1). No kernel definition exists, and Main:576 is a paper theorem with
  probe checks. Whether R2 with the domain premises implies R1 is [W].
- A1 covers the six Pauli eigenstates and sequences of length ≤ 3. Mixed preparations and longer sequences are not
  checked. The match is guaranteed by construction and is not evidence for Emergence.
- B1 is a ring of 8 with 2-cell blocks, two steps, exhaustive over rules. The automaton is affine (B1m), so B1 tests the
  cone path, not nonaffine local dynamics. The general local ceiling is Main's theorem [rec], certified in the corpus
  (`equivalence_recovery_probes.py` check 11 [rec]). A nonaffine local exhaustive check was not run.
- N2's nonaffinity claim is [EC] and general for GF(2)-affine dynamics with bit readouts. For linear dynamics over
  ℤ/qℤ with homomorphic readouts (even q only) it is [W]. Non-homomorphic readouts were not examined.
- B3's bound comparison is [NUM] (50 digits). The mutual informations are exact symbolic expressions.
- The P3 LP on four ontic states is general for two binary measurements: deterministic responses are optimal for fixed
  μ, and coarse-graining Λ to the four response pairs preserves the PNC equality and the success. It assumes exact
  parity obliviousness.
- N1 is established only under exact operational equivalence. No robust inequality (Mazurek et al. 2016) was applied,
  so no finite-precision N1 is claimed.
- P4's disjointness is computed from the mixture definitions and holds by construction.
- P4 and P5 check parity obliviousness over their stated accessible sets (18 axes; sequences of length ≤ 3, adaptive
  ones following from these) and not over a closure of those sets.
- N4's compactness step is [W] and presupposes that the obstruction of Main:580 item (3) already holds on a finite test
  set.
- N5 (KS through measurement-updated memory) is [W] with [L]. The memory size was not computed.
- §2.4 (bijectivity does not supply N1) rests on one instance (P2) and a written argument.
- PBR and the ψ-epistemic bounds were not computed. The PI analysis and the ψ-ontic reading of Main:576 are [W].
- Literature in §8 is from memory. The capacity direction in §3 rests on unread literature and complexity conjectures.
- [rec] rows (Main, Methodology, book appendix-c, SM, MC1–MC5, the reviewer's mutation report) were taken as recorded.

***

## 10. Files (`probe/`)

| file | role |
|---|---|
| `p6.py` | blocks A (observable ladder), B (Bell under OI readout), P1–P5 (preparation contextuality), K (Peres–Mermin), D (double stochasticity replay); 19 checks |
| `p6.run1.out`, `p6.run2.out` | 19 PASS, 0 FAIL; byte-identical |
| `SHA256SUMS` | digests of the three files |
| `review/leak.py`, `review/c5y.py` | the independent reviewer's checks, copied unchanged: PNC vacuous under ε parity leakage; P5 with the toy's Y readout restored |
| `review/leak.run{1,2}.out`, `review/c5y.run{1,2}.out` | outputs; each pair byte-identical |
| `review/SHA256SUMS` | digests of the six review files |

Run: `python3 -I -B p6.py` (with SymPy) from `probe/` (about one minute); the review checks from
`probe/review/`.

***

## 11. Productivity verdict

**Gem: yes, narrow.** Facts strictly stronger than "A2 needs M and R":
- *An answer to the A2 track's posed question.* M and R bind at R2 only. At R1 the corpus already proves Reproduction at
  fixed d, m, K and ε, and the open question is related to selection (HA-6.1).
- *Necessary features of the incompleteness:*
  - N1: under exact operational equivalence, preparation contextuality through invisible response-relevant memory,
    which C4, knowledge balance and bijectivity do not supply (P1–P3, §2.4);
  - N2: nonaffinity in the parameter-dependence branch (B1a);
  - N3: a magnitude-fixing principle. Every mechanism found spans classical to maximal with a free weight (B2b, P5),
    one convexity pattern in two settings;
  - N5: Kochen–Specker contextuality through measurement-updated memory.

**Classification: ELABORATING overall, with one BORDERLINE item (HA-6.2) and a CONFIRMING core (Bell).** No item is
claimed NEW:
- R1 Reproduction and the selection problem are in Main:576–580 and appendix-c:228;
- the Bell analysis is Main §3.3 and Methodology:393;
- the PNC ceiling is Spekkens et al. [L];
- over-generation by restriction is CONFIRMING (appendix-c:232; standard in GPT literature [L]);
- the nonaffinity remark is record-only.

**Answer to the node question.** Observational incompleteness, in the κ1–κ4 class, can make a non-quantum reality's
records agree with QM at fixed dimension, outcome bound, horizon and tolerance, but so far only as Reproduction
(corpus), with a composite entering as one system. Whether it can do so as Emergence is undetermined. The deeper
reality would need N1–N5:
- hidden, response-relevant preparation memory that is never read back, in any model keeping QM's operational
  equivalences exactly;
- a relaxation of parameter or measurement independence for composites, nonaffine in the settings if it is parameter
  dependence;
- capacity unbounded in the precision;
- Kochen–Specker contextuality carried by memory that measurements update;
- a principle fixing the size of the nonclassicality at the quantum values.

The incompleteness mechanism must supply N1 and N3, which no mechanism examined does.

***

## 12. Proposed PLAN text

**Status bullet (after `mc-node5/`):**

> - **`mc-node6/`, A2 track node 1, the quantum appearance in an observer's records: ELABORATING, one BORDERLINE item,
>   [W/EC].**
>   - Three rungs: R0, per-menu representability (universal, PR included); R1(d, m, K, ε), record laws of one
>     realization within ε of QM's in both directions at fixed dimension, outcome bound and horizon, a composite
>     entering as one system; R2, availability under G3 on visible carriers (`DenseFiniteQM`). The cone lemma and
>     clauses M and R are R2 statements. A κ1–κ4 toy-bit construction keeps every visible map in the cone and
>     reproduces the qubit's sequential Pauli records exactly on the 234 protocols checked. At R1 the corpus already
>     proves Reproduction (Main:576–578, a paper theorem). Local composite structure is the operational-lifting problem
>     it leaves open (Main:534, :578), and Main:580 and book appendix-c:228 name what remains as selection.
>   - Outcomes: Reproduction at R1 (corpus). Failure for the finite-range, measurement-independent completion (Bell),
>     and for every preparation-noncontextual model whose parity mixtures are exactly operationally equivalent
>     (parity-oblivious multiplexing ≤ 3/4 against QM's (1+1/√2)/2). No Emergence of quantum statistics found.
>     Contextuality from destructive complementary readouts comes from a posited restriction, as the toy bit's
>     statistics do. The emergent features found (double stochasticity, operational no-signalling, C4 memory) are
>     classical-compatible.
>   - Necessary for Emergence at R1 (not jointly sufficient):
>     - N1: in a model that keeps QM's operational equivalences exactly, preparation contextuality through
>       response-relevant memory that is never read back. History readback (C4) does not imply it, nor do knowledge
>       balance or bijectivity. Without exact equivalences, preparation noncontextuality is vacuous at finite
>       precision, so a finite-precision N1 needs a robust inequality;
>     - N2: for Bell, ontic parameter dependence or measurement dependence. In the parameter-dependence branch the
>       remote dependence must be nonaffine in the settings (GF(2)-affine remote dependence stays at 2), which bears on
>       preparation-indexed edges in a linear update (Main:392);
>     - N3: a principle fixing the magnitude. One long edge gives S = 2 + 2w, and destructive complementary readouts
>       give POM success (1+w)/2, with w free. Restriction overshoots QM as well as falls short;
>     - N4: response-relevant capacity unbounded in the precision;
>     - N5: with labelled instruments fixed (Main:550), Kochen–Specker contextuality carried by hidden memory that
>       earlier measurements update.
>   - G6: none under the preregistered rule.

**Replacement for PLAN:204–212 (A2 track paragraph), proposed:**

> A separate track, alongside the A1 benchmark. Question: can observational limitations make a deeper, non-quantum
> reality's record statistics agree with QM to arbitrary accessible precision, without QM at the fundamental level?
> Results are classed as Emergence, Reproduction or Failure. At the level of availability under G3 (R2, `DenseFiniteQM`),
> U and O are not needed and M and R are, and the cone lemma (`mc-node3`) keeps the present construction's available
> maps in the monomial cone. At the level of record statistics (R1), M and R are not obstructions: κ1–κ4 constructions
> reproduce interference-type and complex-basis record statistics, and the corpus proves Reproduction at fixed
> dimension, outcome bound, horizon and tolerance, a composite entering as one system (Main:576–578); local composite
> structure stays open (Main:534, :578). The track's question at R1 is Emergence, related to the corpus's selection
> problem, under the necessary features N1–N5 of `mc-node6`. It inherits this thread's method, its controls and G6.
> Negative results are acceptable outcomes and are scoped to the construction examined.

**Next node for the A2 track (proposed): does any principle stated in the corpus fix the size of the nonclassicality?**

> - *Question.* For `mc-node6`'s two families, one long edge (S = 2 + 2w) and destructive complementary readouts
>   (POM (1+w)/2), does a principle already stated in the corpus, applied to κ1–κ4 realizations, confine S to
>   [2, 2√2] and POM success to [3/4, (1+1/√2)/2] while admitting the quantum values to within ε? The question is
>   whether OI's principles derive the quantum boundary (for CHSH, |S| ≤ 2√2, Tsirelson) with no freely adjustable
>   parameter, not merely whether they exclude S = 4. The quantum weights differ between the families (√2 − 1 and
>   1/√2), so the test is stated in S and POM, not in w. Candidates:
>   - Lemma 3's selection of the counting measure (Main:56). Under it the weight is fixed by the architecture, not
>     chosen: a uniform control bit gives w = 1/2 and S = 3 (B2b), and finite uniform priors give only rational weights.
>     The node must state which architectures the principle admits;
>   - partition covariance of reduced descriptions (Main:676);
>   - preparation-indexed bounded-degree long edges under H-Bell (Main:392, :394). One such edge with operational
>     no-signalling already realizes every S in [2, 4] (B2b), so this candidate passes only if H-Bell's
>     continuum-curvature condition constrains w. That is the hypothesis to test;
>   - the capacity condition C3 (Main:78), a lower bound, kept as a countercontrol.
> - *Decision rule, preregistered.* The principle is stated in terms of OI's observational principles before any
>   computation. It contains no free parameter tuned to the quantum value; any parameter it has is fixed by OI's own
>   structure, and the node records how. A principle passes iff it:
>   - (i) excludes every S in (2√2 + ε, 4] and every POM success in ((1+1/√2)/2 + ε, 1], with ε fixed in advance;
>   - (ii) admits realizations within ε of 2√2 and of (1+1/√2)/2, which shows the quantum values are achievable;
>   - (iii) admits every classical model.
>
>   It fails otherwise. Excluding only S = 4 and POM = 1 does not fix the magnitude, because post-quantum values lie
>   between the quantum and maximal ones. "Classical model" in (iii) means a κ1–κ4 realization whose induced
>   ontological model is local and measurement-independent in the Bell scenario (S ≤ 2), or preparation noncontextual
>   with exact parity obliviousness in the POM scenario (success ≤ 3/4). Within the families these are w = 0 for the
>   long edge and w ≤ 1/2 for the readouts; outside them they include the delay line (P1) and the toy bit (A1, P2).
>   Passing on the two families is necessary, not sufficient. A principle that passes is then tested for the bound
>   S ≤ 2√2 + ε over every realization it admits in a stated small architecture class, exhaustively where finite,
>   before any claim that it derives the Tsirelson boundary.
> - *Controls.* PR and gbit excluded (must-fail). S = 3 at w = 1/2 excluded (must-fail). The classical delay line and
>   the toy bit kept (must-hold). C3 shown vacuous (countercontrol).
> - *Productivity test.* Gem iff a principle passes, or fails for an identified structural reason that propagates to
>   N1–N3. Negative results are acceptable outcomes.

***

## Review outcome

Independent review: accept with notes. The node was committed as `mc-node6/` at `c2991007` before the notes were
applied. The reviewer's checks `leak.py` and `c5y.py` are copied unchanged into `probe/review/` with their outputs,
each run twice and byte-identical, and `SHA256SUMS`. The reviewer's mutations are not copied. The
notes are applied in place above. The pre-review text is not kept here: `NODE.md` sha256
`ef6e974332a57df490c0233660473d35a28e8b8dc1f3d6416e7c0bf0f417657e`, `p6.py` sha256
`069a77fd99448e798ed0ae68880f486bb254e174670e5a1a3b9478e1e65e2c10`.

| item | verdict | applied as |
|---|---|---|
| core: classification (c), ELABORATING, no Emergence, probe sound with controls that fail when broken | CONFIRMED | — |
| H1 N1 and exact equivalence | CORRECTED | N1 stated under exact operational equivalence; `leak.py` added (control 8); finite-precision N1 needs a robust inequality (Mazurek et al. 2016 [L]), not applied (§0, §2.1, §2.2, §2.3, AW-MC6-3, §9, §12) |
| H2 P5 not Emergence | CORRECTED | P5's steps are the toy bit's; restriction posited as in A3; `c5y.py` added (control 9); §2.1, §2.2, §2.3, §5, §12 relabelled |
| H3 R1, Reproduction scope, citations | CORRECTED | R1(d, m, K, ε) defined with composites as one system; Main:576 a paper theorem; Main:578 operational lifting, Main:580 selection; appendix-c:228, :234 (not :230); selection called related, not identical (§0, §1, HA-6.1, §11, §12) |
| M1 Kochen–Specker | CORRECTED | KS row restated per Main:550 with measurement-updated memory (N5); the vacuous context check removed from K1 |
| M2 N2 wording | CORRECTED | branch-scoped; generality of the GF(2) statement; even-q scope; SM.md:296's threshold nonlinearity quoted; AW-MC6-5 added |
| M3 next node | CORRECTED | reviewer's text, strengthened per the owner's direction of 2026-10-20 (Tsirelson boundary derived, no tuned parameter, achievability, classical models kept, "classical model" defined, a general check after a family pass) |
| M4 markers | CORRECTED | "omits both" withdrawn (PLAN:209–210 poses the question); HA-6.3 CONFIRMING; HA-6.4, HA-6.5 record-only |
| L1 vacuous checks | CORRECTED | P1's record map derived from the dynamics; P4's disjointness computed (by construction, noted in §9); B1 relabelled as a path check with sensitivity in B1m; `p6.py` rerun twice, byte-identical, digests updated |
| L2 LP generality | CORRECTED | §2.2 P3, control 6, §9 |
| L3 check names | CORRECTED | C1–C5 renamed P1–P5 |
| L4 compactness | CORRECTED | N4 with the closedness step [W] |
| L5 N3 independence | CORRECTED | one convexity pattern in two settings |
| L6 PBR row | CORRECTED | labels in the visible intervention record (Main:576), read by the controlled step; consistency with §2.4 stated |
| L7 0.104 | CORRECTED | removed with H1 |
